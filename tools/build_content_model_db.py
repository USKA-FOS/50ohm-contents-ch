from __future__ import annotations

import json
import re
import shutil
import sqlite3
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from typing import Any, Iterable


REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENTS_ROOT = REPO_ROOT / "contents"
TOC_ROOT = REPO_ROOT / "toc"
WORK_ROOT = REPO_ROOT / "work" / "global_model"
DB_PATH = WORK_ROOT / "content_model.sqlite"
INVENTORY_PATH = WORK_ROOT / "object_inventory.json"
SUMMARY_PATH = WORK_ROOT / "summary.json"
LEGAL_FILES = ("README.md", "LICENSE")
SUPPORT_DIRECTORIES = ("latex", "src")
QUESTION_POOL_ROOT = REPO_ROOT.parent / "50ohm-question-pool" / "pool" / "questions"

NANOID_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
MARKER_RE = re.compile(r"\[(question|photo|picture|table|include|ref|index|class|morse):([^\]]*)\]")


def stable_id(namespace: str, *parts: str, size: int = 21) -> str:
    material = "::".join([namespace, *parts]).encode("utf-8")
    digest = sha256(material).digest()
    value = int.from_bytes(digest, "big")
    chars: list[str] = []
    alphabet_len = len(NANOID_ALPHABET)
    for _ in range(size):
        value, index = divmod(value, alphabet_len)
        chars.append(NANOID_ALPHABET[index])
    return "".join(chars)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(path: Path, payload: Any) -> None:
    path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def ensure_clean_workdir() -> None:
    WORK_ROOT.mkdir(parents=True, exist_ok=True)
    if DB_PATH.exists():
        DB_PATH.unlink()


def grouped_numeric_assets(root: Path) -> dict[str, dict[str, Path]]:
    grouped: dict[str, dict[str, Path]] = {}
    for path in sorted(root.iterdir()):
        if not path.is_file():
            continue
        grouped.setdefault(path.stem, {})[path.suffix] = path
    return grouped


@dataclass(frozen=True)
class ReferenceTarget:
    target_object_type: str | None
    target_id_system: str
    target_id_value: str
    relation_type: str
    inline_alias: str | None = None
    inline_label: str | None = None


class Builder:
    def __init__(self, db_path: Path) -> None:
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.objects: dict[tuple[str, str], str] = {}
        self.synthetic_tables: dict[str, str] = {}
        self.synthetic_nodes: dict[tuple[str, str], str] = {}
        self.counts: dict[str, int] = {}

    def increment(self, key: str, amount: int = 1) -> None:
        self.counts[key] = self.counts.get(key, 0) + amount

    def create_schema(self) -> None:
        self.conn.executescript(
            """
            PRAGMA foreign_keys = ON;

            CREATE TABLE content_object (
                id TEXT PRIMARY KEY,
                object_type TEXT NOT NULL,
                source_path TEXT,
                source_format TEXT,
                source_key TEXT,
                active INTEGER NOT NULL DEFAULT 1
            );

            CREATE TABLE object_identifier (
                id TEXT PRIMARY KEY,
                object_id TEXT NOT NULL REFERENCES content_object(id),
                id_system TEXT NOT NULL,
                id_value TEXT NOT NULL,
                preferred INTEGER NOT NULL DEFAULT 0
            );

            CREATE TABLE text_slot (
                id TEXT PRIMARY KEY,
                object_id TEXT NOT NULL REFERENCES content_object(id),
                slot_key TEXT NOT NULL,
                slot_type TEXT NOT NULL,
                translation_group_key TEXT,
                sort_order INTEGER NOT NULL DEFAULT 0
            );

            CREATE TABLE localized_text (
                id TEXT PRIMARY KEY,
                text_slot_id TEXT NOT NULL REFERENCES text_slot(id),
                language TEXT NOT NULL,
                text_value TEXT NOT NULL
            );

            CREATE TABLE object_metadata (
                id TEXT PRIMARY KEY,
                object_id TEXT NOT NULL REFERENCES content_object(id),
                metadata_scope TEXT NOT NULL,
                metadata_key TEXT NOT NULL,
                value_json TEXT NOT NULL
            );

            CREATE TABLE review_state (
                id TEXT PRIMARY KEY,
                subject_kind TEXT NOT NULL,
                subject_id TEXT NOT NULL,
                language TEXT,
                state TEXT NOT NULL
            );

            CREATE TABLE curriculum_node (
                id TEXT PRIMARY KEY,
                edition TEXT NOT NULL,
                node_type TEXT NOT NULL,
                parent_node_id TEXT REFERENCES curriculum_node(id),
                sort_order INTEGER NOT NULL DEFAULT 0,
                source_path TEXT
            );

            CREATE TABLE node_identifier (
                id TEXT PRIMARY KEY,
                node_id TEXT NOT NULL REFERENCES curriculum_node(id),
                id_system TEXT NOT NULL,
                id_value TEXT NOT NULL,
                preferred INTEGER NOT NULL DEFAULT 0
            );

            CREATE TABLE node_text (
                id TEXT PRIMARY KEY,
                node_id TEXT NOT NULL REFERENCES curriculum_node(id),
                language TEXT NOT NULL,
                title TEXT,
                abstract TEXT
            );

            CREATE TABLE node_metadata (
                id TEXT PRIMARY KEY,
                node_id TEXT NOT NULL REFERENCES curriculum_node(id),
                metadata_key TEXT NOT NULL,
                value_json TEXT NOT NULL
            );

            CREATE TABLE content_placement (
                id TEXT PRIMARY KEY,
                node_id TEXT NOT NULL REFERENCES curriculum_node(id),
                object_id TEXT NOT NULL REFERENCES content_object(id),
                placement_role TEXT NOT NULL,
                sort_order INTEGER NOT NULL DEFAULT 0,
                visible_label TEXT
            );

            CREATE TABLE object_reference (
                id TEXT PRIMARY KEY,
                source_object_id TEXT NOT NULL REFERENCES content_object(id),
                source_slot_key TEXT NOT NULL,
                target_object_type TEXT,
                target_id_system TEXT NOT NULL,
                target_id_value TEXT NOT NULL,
                relation_type TEXT NOT NULL,
                inline_alias TEXT,
                inline_label TEXT,
                raw_marker TEXT NOT NULL,
                sort_order INTEGER NOT NULL DEFAULT 0
            );

            CREATE TABLE text_annotation (
                id TEXT PRIMARY KEY,
                source_object_id TEXT NOT NULL REFERENCES content_object(id),
                source_slot_key TEXT NOT NULL,
                annotation_type TEXT NOT NULL,
                annotation_key TEXT,
                annotation_value TEXT,
                raw_marker TEXT NOT NULL,
                sort_order INTEGER NOT NULL DEFAULT 0
            );

            CREATE TABLE source_artifact (
                id TEXT PRIMARY KEY,
                object_id TEXT REFERENCES content_object(id),
                source_path TEXT NOT NULL UNIQUE,
                media_type TEXT NOT NULL,
                checksum_sha256 TEXT NOT NULL,
                payload BLOB NOT NULL
            );
            """
        )

    def add_object(
        self,
        *,
        object_type: str,
        source_path: str | None,
        source_format: str | None,
        source_key: str | None,
        active: bool = True,
    ) -> str:
        registry_key = (object_type, source_key or source_path or "")
        object_id = self.objects.get(registry_key)
        if object_id is None:
            object_id = stable_id("obj", object_type, source_key or "", source_path or "")
            self.objects[registry_key] = object_id
            self.conn.execute(
                """
                INSERT INTO content_object(id, object_type, source_path, source_format, source_key, active)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (object_id, object_type, source_path, source_format, source_key, int(active)),
            )
            self.increment("content_object")
        return object_id

    def add_external_object(
        self, *, object_id: str, object_type: str, source_path: str | None, source_format: str | None, source_key: str | None
    ) -> str:
        """Register an object whose canonical id is owned by another repository."""
        registry_key = (object_type, source_key or source_path or object_id)
        self.objects[registry_key] = object_id
        self.conn.execute(
            "INSERT INTO content_object(id, object_type, source_path, source_format, source_key, active) VALUES (?, ?, ?, ?, ?, 1)",
            (object_id, object_type, source_path, source_format, source_key),
        )
        self.increment("content_object")
        return object_id

    def add_identifier(self, object_id: str, id_system: str, id_value: str, *, preferred: bool = False) -> None:
        identifier_id = stable_id("oid", object_id, id_system, id_value)
        self.conn.execute(
            """
            INSERT OR REPLACE INTO object_identifier(id, object_id, id_system, id_value, preferred)
            VALUES (?, ?, ?, ?, ?)
            """,
            (identifier_id, object_id, id_system, id_value, int(preferred)),
        )

    def add_text_slot(
        self,
        object_id: str,
        slot_key: str,
        slot_type: str,
        *,
        translation_group_key: str | None = None,
        sort_order: int = 0,
    ) -> str:
        slot_id = stable_id("slot", object_id, slot_key)
        self.conn.execute(
            """
            INSERT OR REPLACE INTO text_slot(id, object_id, slot_key, slot_type, translation_group_key, sort_order)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (slot_id, object_id, slot_key, slot_type, translation_group_key, sort_order),
        )
        return slot_id

    def add_localized_text(self, slot_id: str, language: str, text_value: str) -> None:
        localized_id = stable_id("ltxt", slot_id, language)
        self.conn.execute(
            """
            INSERT OR REPLACE INTO localized_text(id, text_slot_id, language, text_value)
            VALUES (?, ?, ?, ?)
            """,
            (localized_id, slot_id, language, text_value),
        )

    def add_metadata(self, object_id: str, metadata_scope: str, metadata_key: str, value: Any) -> None:
        metadata_id = stable_id("meta", object_id, metadata_scope, metadata_key)
        self.conn.execute(
            """
            INSERT OR REPLACE INTO object_metadata(id, object_id, metadata_scope, metadata_key, value_json)
            VALUES (?, ?, ?, ?, ?)
            """,
            (metadata_id, object_id, metadata_scope, metadata_key, json.dumps(value, ensure_ascii=False, sort_keys=True)),
        )

    def add_review_state(self, subject_kind: str, subject_id: str, language: str | None, state: str) -> None:
        review_id = stable_id("rvs", subject_kind, subject_id, language or "", state)
        self.conn.execute(
            """
            INSERT OR REPLACE INTO review_state(id, subject_kind, subject_id, language, state)
            VALUES (?, ?, ?, ?, ?)
            """,
            (review_id, subject_kind, subject_id, language, state),
        )

    def add_source_artifact(self, path: Path, object_id: str | None) -> None:
        relative_path = str(path.relative_to(REPO_ROOT))
        payload = path.read_bytes()
        artifact_id = stable_id("artifact", relative_path)
        self.conn.execute(
            """
            INSERT OR REPLACE INTO source_artifact(
                id, object_id, source_path, media_type, checksum_sha256, payload
            ) VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                artifact_id,
                object_id,
                relative_path,
                path.suffix.lstrip(".") or "plain",
                sha256(payload).hexdigest(),
                payload,
            ),
        )

    def add_node(
        self,
        *,
        edition: str,
        node_type: str,
        source_path: str,
        path_key: str,
        parent_node_id: str | None,
        sort_order: int,
    ) -> str:
        registry_key = (edition, path_key)
        node_id = self.synthetic_nodes.get(registry_key)
        if node_id is None:
            node_id = stable_id("node", edition, path_key)
            self.synthetic_nodes[registry_key] = node_id
            self.conn.execute(
                """
                INSERT INTO curriculum_node(id, edition, node_type, parent_node_id, sort_order, source_path)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (node_id, edition, node_type, parent_node_id, sort_order, source_path),
            )
            self.increment("curriculum_node")
        return node_id

    def add_node_identifier(self, node_id: str, id_system: str, id_value: str, *, preferred: bool = False) -> None:
        identifier_id = stable_id("nid", node_id, id_system, id_value)
        self.conn.execute(
            """
            INSERT OR REPLACE INTO node_identifier(id, node_id, id_system, id_value, preferred)
            VALUES (?, ?, ?, ?, ?)
            """,
            (identifier_id, node_id, id_system, id_value, int(preferred)),
        )

    def add_node_text(self, node_id: str, title: str | None, abstract: str | None) -> None:
        text_id = stable_id("ntxt", node_id, "de")
        self.conn.execute(
            """
            INSERT OR REPLACE INTO node_text(id, node_id, language, title, abstract)
            VALUES (?, ?, ?, ?, ?)
            """,
            (text_id, node_id, "de", title, abstract),
        )

    def add_node_metadata(self, node_id: str, metadata_key: str, value: Any) -> None:
        metadata_id = stable_id("nmeta", node_id, metadata_key)
        self.conn.execute(
            """
            INSERT OR REPLACE INTO node_metadata(id, node_id, metadata_key, value_json)
            VALUES (?, ?, ?, ?)
            """,
            (metadata_id, node_id, metadata_key, json.dumps(value, ensure_ascii=False, sort_keys=True)),
        )

    def import_node_payload(self, node_id: str, payload: dict[str, Any], *, structural_keys: set[str]) -> None:
        """Preserve every non-structural TOC property on its modeled node."""
        self.add_node_text(node_id, payload.get("title"), payload.get("abstract"))
        for key, value in sorted(payload.items()):
            if key not in structural_keys | {"title", "abstract", "ident"}:
                self.add_node_metadata(node_id, key, value)

    def add_placement(
        self,
        *,
        node_id: str,
        object_id: str,
        placement_role: str,
        sort_order: int,
        visible_label: str | None = None,
    ) -> None:
        placement_id = stable_id("place", node_id, object_id, placement_role, str(sort_order), visible_label or "")
        self.conn.execute(
            """
            INSERT OR REPLACE INTO content_placement(id, node_id, object_id, placement_role, sort_order, visible_label)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (placement_id, node_id, object_id, placement_role, sort_order, visible_label),
        )

    def add_reference(self, source_object_id: str, source_slot_key: str, marker: str, order: int, target: ReferenceTarget) -> None:
        reference_id = stable_id("oref", source_object_id, source_slot_key, str(order), marker)
        self.conn.execute(
            """
            INSERT OR REPLACE INTO object_reference(
                id, source_object_id, source_slot_key, target_object_type, target_id_system,
                target_id_value, relation_type, inline_alias, inline_label, raw_marker, sort_order
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                reference_id,
                source_object_id,
                source_slot_key,
                target.target_object_type,
                target.target_id_system,
                target.target_id_value,
                target.relation_type,
                target.inline_alias,
                target.inline_label,
                marker,
                order,
            ),
        )

    def add_annotation(
        self,
        source_object_id: str,
        source_slot_key: str,
        annotation_type: str,
        annotation_key: str | None,
        annotation_value: str | None,
        marker: str,
        order: int,
    ) -> None:
        annotation_id = stable_id("anno", source_object_id, source_slot_key, str(order), marker)
        self.conn.execute(
            """
            INSERT OR REPLACE INTO text_annotation(
                id, source_object_id, source_slot_key, annotation_type, annotation_key,
                annotation_value, raw_marker, sort_order
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (annotation_id, source_object_id, source_slot_key, annotation_type, annotation_key, annotation_value, marker, order),
        )

    def ensure_table_object(self, alias: str) -> str:
        object_id = self.synthetic_tables.get(alias)
        if object_id is None:
            object_id = self.add_object(
                object_type="table_object",
                source_path=None,
                source_format="synthetic",
                source_key=alias,
            )
            self.add_identifier(object_id, "table_id", alias, preferred=True)
            self.synthetic_tables[alias] = object_id
        return object_id

    def parse_and_store_markers(self, source_object_id: str, slot_key: str, text_value: str) -> None:
        order = 0
        for match in MARKER_RE.finditer(text_value):
            order += 1
            command = match.group(1)
            raw_payload = match.group(2)
            marker = match.group(0)

            if command == "question":
                target = ReferenceTarget("question", "question_code", raw_payload.strip(), "references_question")
                self.add_reference(source_object_id, slot_key, marker, order, target)
                continue

            if command in {"photo", "picture"}:
                parts = raw_payload.split(":")
                if len(parts) >= 3:
                    target = ReferenceTarget(
                        "photo" if command == "photo" else "drawing",
                        "photo_id" if command == "photo" else "drawing_id",
                        parts[0].strip(),
                        "embeds_photo" if command == "photo" else "embeds_drawing",
                        inline_alias=parts[1].strip(),
                        inline_label=":".join(parts[2:]).strip(),
                    )
                    self.add_reference(source_object_id, slot_key, marker, order, target)
                continue

            if command == "table":
                parts = raw_payload.split(":")
                if len(parts) >= 2:
                    alias = parts[0].strip()
                    self.ensure_table_object(alias)
                    target = ReferenceTarget(
                        "table_object",
                        "table_id",
                        alias,
                        "embeds_table",
                        inline_alias=alias,
                        inline_label=":".join(parts[1:]).strip(),
                    )
                    self.add_reference(source_object_id, slot_key, marker, order, target)
                continue

            if command == "include":
                key = raw_payload.strip()
                target = ReferenceTarget("html_include", "include_key", key, "includes_object")
                self.add_reference(source_object_id, slot_key, marker, order, target)
                continue

            if command == "ref":
                alias = raw_payload.strip()
                target = ReferenceTarget(None, "inline_alias", alias, "references_embedded_alias", inline_alias=alias)
                self.add_reference(source_object_id, slot_key, marker, order, target)
                continue

            if command == "index":
                parts = raw_payload.split(":", 1)
                annotation_key = parts[0].strip() if parts else None
                annotation_value = parts[1].strip() if len(parts) > 1 else None
                self.add_annotation(source_object_id, slot_key, "index_term", annotation_key, annotation_value, marker, order)
                continue

            if command == "class":
                self.add_annotation(source_object_id, slot_key, "class_marker", None, raw_payload.strip(), marker, order)
                continue

            if command == "morse":
                self.add_annotation(source_object_id, slot_key, "morse_marker", None, raw_payload.strip(), marker, order)

    def import_simple_text_file(self, family: str, object_type: str, slot_key: str, slot_type: str) -> dict[str, str]:
        objects_by_stem: dict[str, str] = {}
        root = CONTENTS_ROOT / family
        for path in sorted(root.glob("*")):
            if not path.is_file():
                continue
            object_id = self.add_object(
                object_type=object_type,
                source_path=str(path.relative_to(REPO_ROOT)),
                source_format=path.suffix.lstrip("."),
                source_key=path.stem,
            )
            objects_by_stem[path.stem] = object_id
            self.add_identifier(object_id, "file_stem", path.stem, preferred=True)
            slot_id = self.add_text_slot(object_id, slot_key, slot_type)
            self.add_localized_text(slot_id, "de", path.read_text(encoding="utf-8"))
            self.add_review_state("content_object", object_id, "de", "imported_approved")
            self.parse_and_store_markers(object_id, slot_key, path.read_text(encoding="utf-8"))
        return objects_by_stem

    def import_raw_file_object(self, path: Path, object_type: str, slot_key: str = "body_text", slot_type: str = "text") -> str:
        object_id = self.add_object(
            object_type=object_type,
            source_path=str(path.relative_to(REPO_ROOT)),
            source_format=path.suffix.lstrip("."),
            source_key=path.name,
        )
        slot_id = self.add_text_slot(object_id, slot_key, slot_type)
        self.add_localized_text(slot_id, "de", path.read_text(encoding="utf-8"))
        self.add_review_state("content_object", object_id, "de", "imported_approved")
        return object_id

    def import_photos(self) -> dict[str, str]:
        objects_by_id: dict[str, str] = {}
        for stem, members in grouped_numeric_assets(CONTENTS_ROOT / "photos").items():
            object_id = self.add_object(
                object_type="photo",
                source_path=f"translator/50ohm-contents-ch/contents/photos/{stem}",
                source_format="grouped_asset",
                source_key=stem,
            )
            objects_by_id[stem] = object_id
            self.add_identifier(object_id, "photo_id", stem, preferred=True)
            self.add_identifier(object_id, "file_stem", stem)
            if ".png" in members:
                self.add_metadata(object_id, "asset", "image_path", str(members[".png"].relative_to(REPO_ROOT)))
            if ".txt" in members:
                raw_text = members[".txt"].read_text(encoding="utf-8")
                short_text, long_text = split_description_text(raw_text)
                short_slot = self.add_text_slot(object_id, "short_description", "plain_text", translation_group_key="photo_descriptions", sort_order=1)
                long_slot = self.add_text_slot(object_id, "long_description", "plain_text", translation_group_key="photo_descriptions", sort_order=2)
                self.add_localized_text(short_slot, "de", short_text)
                self.add_localized_text(long_slot, "de", long_text)
                self.add_review_state("content_object", object_id, "de", "imported_approved")
        return objects_by_id

    def import_drawings(self) -> dict[str, str]:
        objects_by_id: dict[str, str] = {}
        for stem, members in grouped_numeric_assets(CONTENTS_ROOT / "drawings").items():
            object_id = self.add_object(
                object_type="drawing",
                source_path=f"translator/50ohm-contents-ch/contents/drawings/{stem}",
                source_format="grouped_asset",
                source_key=stem,
            )
            objects_by_id[stem] = object_id
            self.add_identifier(object_id, "drawing_id", stem, preferred=True)
            self.add_identifier(object_id, "file_stem", stem)
            if ".svg" in members:
                self.add_metadata(object_id, "asset", "svg_path", str(members[".svg"].relative_to(REPO_ROOT)))
            if ".tex" in members:
                self.add_metadata(object_id, "asset", "tex_path", str(members[".tex"].relative_to(REPO_ROOT)))
            if ".txt" in members:
                raw_text = members[".txt"].read_text(encoding="utf-8")
                short_text, long_text = split_description_text(raw_text)
                short_slot = self.add_text_slot(object_id, "short_description", "plain_text", translation_group_key="drawing_descriptions", sort_order=1)
                long_slot = self.add_text_slot(object_id, "long_description", "plain_text", translation_group_key="drawing_descriptions", sort_order=2)
                self.add_localized_text(short_slot, "de", short_text)
                self.add_localized_text(long_slot, "de", long_text)
                self.add_review_state("content_object", object_id, "de", "imported_approved")
        return objects_by_id

    def import_questions(self) -> dict[str, str]:
        catalog_path = CONTENTS_ROOT / "questions" / "fragenkatalog3b.json"
        raw_object_id = self.add_object(
            object_type="question_catalog_file",
            source_path=str(catalog_path.relative_to(REPO_ROOT)),
            source_format="json",
            source_key=catalog_path.name,
        )
        payload = load_json(catalog_path)
        self.add_metadata(raw_object_id, "stats", "top_level_sections", len(payload.get("sections", [])))

        questions_by_code: dict[str, str] = {}
        root_node = self.add_node(
            edition="question_catalog_de",
            node_type="question_catalog_root",
            source_path=str(catalog_path.relative_to(REPO_ROOT)),
            path_key="question_catalog_de",
            parent_node_id=None,
            sort_order=0,
        )
        self.add_node_text(root_node, "Question Catalog DE", None)

        def walk_sections(sections: list[dict[str, Any]], parent_node_id: str, path_parts: list[str]) -> None:
            for section_index, section in enumerate(sections, start=1):
                title = str(section.get("title", "")).strip()
                node_type = "question_catalog_section"
                path_key = "/".join(path_parts + [title or f"untitled_{section_index}"])
                node_id = self.add_node(
                    edition="question_catalog_de",
                    node_type=node_type,
                    source_path=str(catalog_path.relative_to(REPO_ROOT)),
                    path_key=path_key,
                    parent_node_id=parent_node_id,
                    sort_order=section_index,
                )
                self.add_node_text(node_id, title, None)

                for question_index, question in enumerate(section.get("questions", []), start=1):
                    code = str(question.get("number", "")).strip()
                    if not code:
                        continue
                    object_id = questions_by_code.get(code)
                    if object_id is None:
                        object_id = self.add_object(
                            object_type="question",
                            source_path=str(catalog_path.relative_to(REPO_ROOT)),
                            source_format="json",
                            source_key=code,
                        )
                        questions_by_code[code] = object_id
                        self.add_identifier(object_id, "question_code", code, preferred=True)
                        self.add_metadata(object_id, "question", "class", question.get("class"))
                        translation_group = f"question:{code}"
                        for order, slot_name in enumerate(
                            ["question_text", "answer_a", "answer_b", "answer_c", "answer_d"],
                            start=1,
                        ):
                            slot_id = self.add_text_slot(
                                object_id,
                                slot_name,
                                "plain_text",
                                translation_group_key=translation_group,
                                sort_order=order,
                            )
                            field_name = "question" if slot_name == "question_text" else slot_name
                            self.add_localized_text(slot_id, "de", str(question.get(field_name, "")))
                        self.add_review_state("content_object", object_id, "de", "imported_approved")
                    self.add_placement(
                        node_id=node_id,
                        object_id=object_id,
                        placement_role="question",
                        sort_order=question_index,
                        visible_label=code,
                    )

                walk_sections(section.get("sections", []), node_id, path_parts + [title or f"untitled_{section_index}"])

        walk_sections(payload.get("sections", []), root_node, ["question_catalog_de"])
        return questions_by_code

    def import_questions_from_pool(self) -> dict[str, str]:
        """Federate current question objects from their independently canonical pool."""
        questions_by_code: dict[str, str] = {}
        for meta_path in sorted(QUESTION_POOL_ROOT.glob("*/question.meta.json")):
            meta = load_json(meta_path)
            question_id = meta["id"]
            code = meta["internal_code"]
            self.add_external_object(
                object_id=question_id,
                object_type="question",
                source_path=str(meta_path.relative_to(REPO_ROOT.parent)),
                source_format="question_pool",
                source_key=code,
            )
            questions_by_code[code] = question_id
            self.add_identifier(question_id, "question_pool_id", question_id, preferred=True)
            self.add_identifier(question_id, "question_code", code)
            for key, value in sorted(meta.items()):
                if key not in {"id", "internal_code", "review_status", "review_status_fr", "review_status_it"}:
                    self.add_metadata(question_id, "question_pool", key, value)
            self.add_review_state("content_object", question_id, None, meta.get("review_status", "approved"))
            for language in ("fr", "it"):
                self.add_review_state("content_object", question_id, language, meta.get(f"review_status_{language}", "to_be_translated"))
            for language in ("de", "fr", "it"):
                text_path = meta_path.parent / f"question.{language}.json"
                text = load_json(text_path)
                for order, slot_name in enumerate(["question_text", "answer_a", "answer_b", "answer_c", "answer_d"], start=1):
                    slot_id = self.add_text_slot(
                        question_id, slot_name, "plain_text", translation_group_key=f"question:{question_id}", sort_order=order
                    )
                    field_name = "question" if slot_name == "question_text" else slot_name
                    self.add_localized_text(slot_id, language, str(text.get(field_name, "")))
                self.add_metadata(question_id, "question_pool_presentation", f"{language}_pictures", {
                    key: text.get(key) for key in text if key.startswith("picture_")
                })
        return questions_by_code

    def import_question_metadata(self, questions_by_code: dict[str, str]) -> None:
        metadata_path = CONTENTS_ROOT / "questions" / "metadata3b.json"
        raw_object_id = self.add_object(
            object_type="question_metadata_file",
            source_path=str(metadata_path.relative_to(REPO_ROOT)),
            source_format="json",
            source_key=metadata_path.name,
        )
        payload = load_json(metadata_path)
        self.add_metadata(raw_object_id, "stats", "entries", len(payload))
        for code, metadata in sorted(payload.items()):
            question_id = questions_by_code.get(code)
            if question_id is None:
                continue
            for key, value in sorted(metadata.items()):
                self.add_metadata(question_id, "question_presentation_legacy", key, value)

    def import_question_layout(self, questions_by_code: dict[str, str]) -> None:
        layout_path = CONTENTS_ROOT / "metadata" / "question_layout.json"
        raw_object_id = self.add_object(
            object_type="question_layout_file",
            source_path=str(layout_path.relative_to(REPO_ROOT)),
            source_format="json",
            source_key=layout_path.name,
        )
        payload = load_json(layout_path)
        self.add_metadata(raw_object_id, "stats", "entries", len(payload))
        for code, metadata in sorted(payload.items()):
            question_id = questions_by_code.get(code)
            if question_id is None:
                continue
            for key, value in sorted(metadata.items()):
                self.add_metadata(question_id, "question_layout", key, value)

    def import_toc(self, section_objects: dict[str, str], slide_objects: dict[str, str]) -> None:
        for toc_path in sorted(TOC_ROOT.glob("*.json")):
            edition = toc_path.stem
            payload = load_json(toc_path)
            raw_object_id = self.add_object(
                object_type="toc_file",
                source_path=str(toc_path.relative_to(REPO_ROOT)),
                source_format="json",
                source_key=toc_path.name,
            )
            self.add_metadata(raw_object_id, "stats", "chapters", len(payload.get("chapters", [])))

            root_node = self.add_node(
                edition=edition,
                node_type="curriculum_root",
                source_path=str(toc_path.relative_to(REPO_ROOT)),
                path_key=edition,
                parent_node_id=None,
                sort_order=0,
            )
            self.import_node_payload(root_node, payload, structural_keys={"chapters"})
            self.add_node_identifier(root_node, "edition", edition, preferred=True)

            for chapter_index, chapter in enumerate(payload.get("chapters", []), start=1):
                chapter_ident = str(chapter.get("ident", f"chapter_{chapter_index}"))
                chapter_key = f"{edition}/{chapter_ident}"
                chapter_node = self.add_node(
                    edition=edition,
                    node_type="curriculum_chapter",
                    source_path=str(toc_path.relative_to(REPO_ROOT)),
                    path_key=chapter_key,
                    parent_node_id=root_node,
                    sort_order=chapter_index,
                )
                self.add_node_identifier(chapter_node, "toc_ident", chapter_ident, preferred=True)
                self.import_node_payload(chapter_node, chapter, structural_keys={"sections"})

                for section_index, section in enumerate(chapter.get("sections", []), start=1):
                    section_ident = str(section.get("ident", f"section_{section_index}"))
                    section_key = f"{chapter_key}/{section_ident}"
                    section_node = self.add_node(
                        edition=edition,
                        node_type="curriculum_section",
                        source_path=str(toc_path.relative_to(REPO_ROOT)),
                        path_key=section_key,
                        parent_node_id=chapter_node,
                        sort_order=section_index,
                    )
                    self.add_node_identifier(section_node, "toc_ident", section_ident, preferred=True)
                    self.import_node_payload(section_node, section, structural_keys=set())

                    if section_ident in section_objects:
                        self.add_placement(
                            node_id=section_node,
                            object_id=section_objects[section_ident],
                            placement_role="section_article",
                            sort_order=1,
                            visible_label=section_ident,
                        )
                    if section_ident in slide_objects:
                        self.add_placement(
                            node_id=section_node,
                            object_id=slide_objects[section_ident],
                            placement_role="slide_article",
                            sort_order=2,
                            visible_label=section_ident,
                        )

    def import_source_artifacts(self) -> None:
        """Store source bytes so a site-content tree can be recreated from SQLite alone."""
        source_paths = [
            path
            for root in (CONTENTS_ROOT, TOC_ROOT, *(REPO_ROOT / name for name in SUPPORT_DIRECTORIES))
            for path in sorted(root.rglob("*"))
            if path.is_file()
        ]
        legal_objects: dict[str, str] = {}
        for name in LEGAL_FILES:
            path = REPO_ROOT / name
            legal_objects[name] = self.add_object(
                object_type="legal_document",
                source_path=name,
                source_format=path.suffix.lstrip(".") or "plain",
                source_key=name,
            )
            source_paths.append(path)

        objects_by_path = {
            row["source_path"]: row["id"]
            for row in self.conn.execute(
                "SELECT id, source_path FROM content_object WHERE source_path IS NOT NULL"
            )
        }
        objects_by_path.update(legal_objects)
        for path in sorted(source_paths, key=lambda item: str(item.relative_to(REPO_ROOT))):
            self.add_source_artifact(path, objects_by_path.get(str(path.relative_to(REPO_ROOT))))

    def write_inventory(self) -> None:
        objects = [
            dict(row)
            for row in self.conn.execute(
                """
                SELECT
                    o.id,
                    o.object_type,
                    o.source_path,
                    o.source_format,
                    o.source_key,
                    o.active,
                    COUNT(DISTINCT i.id) AS identifier_count,
                    COUNT(DISTINCT s.id) AS slot_count,
                    COUNT(DISTINCT m.id) AS metadata_count
                FROM content_object o
                LEFT JOIN object_identifier i ON i.object_id = o.id
                LEFT JOIN text_slot s ON s.object_id = o.id
                LEFT JOIN object_metadata m ON m.object_id = o.id
                GROUP BY o.id
                ORDER BY o.object_type, o.source_key, o.source_path
                """
            )
        ]
        dump_json(INVENTORY_PATH, objects)

    def summary(self) -> dict[str, Any]:
        return {
            "content_objects_by_type": {
                row["object_type"]: row["count"]
                for row in self.conn.execute(
                    "SELECT object_type, COUNT(*) AS count FROM content_object GROUP BY object_type ORDER BY object_type"
                )
            },
            "table_counts": {
                table: self.conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
                for table in [
                    "content_object",
                    "object_identifier",
                    "text_slot",
                    "localized_text",
                    "object_metadata",
                    "review_state",
                    "curriculum_node",
                    "node_identifier",
                    "node_text",
                    "node_metadata",
                    "content_placement",
                    "object_reference",
                    "text_annotation",
                    "source_artifact",
                ]
            },
        }

    def commit(self) -> None:
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()


def split_description_text(raw_text: str) -> tuple[str, str]:
    short_match = re.search(r"1\)\s*Kurzbeschreibung:\s*(.+?)(?:\n\s*\n|\n2\)|$)", raw_text, flags=re.DOTALL)
    long_match = re.search(r"2\)\s*(?:Ausführliche Beschreibung:)?\s*(.+)$", raw_text, flags=re.DOTALL)
    short_text = short_match.group(1).strip() if short_match else raw_text.strip()
    long_text = long_match.group(1).strip() if long_match else raw_text.strip()
    return short_text, long_text


def build_database() -> dict[str, Any]:
    ensure_clean_workdir()
    builder = Builder(DB_PATH)
    builder.create_schema()

    section_objects = builder.import_simple_text_file("sections", "section_article", "body_markdown", "markdown")
    slide_objects = builder.import_simple_text_file("slides", "slide_article", "body_markdown", "markdown")
    builder.import_simple_text_file("solutions", "solution_article", "body_markdown", "markdown")
    builder.import_simple_text_file("snippets", "snippet", "body_markdown", "markdown")
    builder.import_simple_text_file("static", "static_page", "body_html", "html")
    builder.import_simple_text_file("html", "html_include", "body_html", "html")
    builder.import_photos()
    builder.import_drawings()
    builder.import_raw_file_object(CONTENTS_ROOT / "questions" / "README.txt", "questions_readme")

    questions_by_code = builder.import_questions_from_pool()
    builder.import_question_metadata(questions_by_code)
    builder.import_question_layout(questions_by_code)
    builder.import_toc(section_objects, slide_objects)
    builder.import_source_artifacts()

    builder.commit()
    builder.write_inventory()
    summary = builder.summary()
    dump_json(SUMMARY_PATH, summary)
    builder.close()
    return summary


def main() -> None:
    summary = build_database()
    print(f"sqlite={DB_PATH}")
    print(f"inventory={INVENTORY_PATH}")
    print(f"summary={SUMMARY_PATH}")
    print(json.dumps(summary["table_counts"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
