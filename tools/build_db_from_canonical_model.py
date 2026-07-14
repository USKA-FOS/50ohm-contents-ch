from __future__ import annotations

import json
import sqlite3
from hashlib import sha256
from pathlib import Path
from typing import Any, Iterable

from build_content_model_db import Builder, ReferenceTarget, split_description_text, stable_id


REPO_ROOT = Path(__file__).resolve().parent.parent
CANONICAL_ROOT = REPO_ROOT / "canonical"
SUPPORT_ROOT = REPO_ROOT / "work" / "canonical_support"
DB_PATH = REPO_ROOT / "work" / "canonical_model" / "content_model.sqlite"
CONTENTS_ROOT = REPO_ROOT / "contents"
TOC_ROOT = REPO_ROOT / "toc"
LEGAL_FILES = ("README.md", "LICENSE")
SUPPORT_DIRECTORIES = ("latex", "src")
OBJECT_FAMILY_DIRECTORIES = (
    "sections",
    "slides",
    "solutions",
    "snippets",
    "static_pages",
    "html_includes",
    "photos",
    "drawings",
    "tables",
    "legal_documents",
    "support_assets",
)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def object_dirs(directory: Path) -> Iterable[Path]:
    return sorted(path for path in directory.iterdir() if path.is_dir()) if directory.exists() else []


def storage_files_with_fallback(directory: Path, files: dict[str, str] | None) -> dict[str, str]:
    resolved = dict(files or {})
    if not resolved:
        return resolved

    for relative_name in list(resolved.values()):
        name = Path(relative_name).name
        parts = name.split(".")
        if len(parts) < 3:
            continue
        stem = ".".join(parts[:-2])
        suffix = parts[-1]
        for language in ("fr", "it"):
            candidate_name = f"{stem}.{language}.{suffix}"
            candidate_path = directory / candidate_name
            if language not in resolved and candidate_path.exists():
                resolved[language] = candidate_name
    return resolved


def import_source_artifacts_from_repo(connection: sqlite3.Connection) -> None:
    source_paths = [
        path
        for root in (CONTENTS_ROOT, TOC_ROOT, *(REPO_ROOT / name for name in SUPPORT_DIRECTORIES))
        if root.exists()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    ]
    for name in LEGAL_FILES:
        path = REPO_ROOT / name
        if path.exists():
            source_paths.append(path)

    objects_by_path = {
        row["source_path"]: row["id"]
        for row in connection.execute(
            "SELECT id, source_path FROM content_object WHERE source_path IS NOT NULL"
        )
    }
    for path in sorted(source_paths, key=lambda item: str(item.relative_to(REPO_ROOT))):
        relative_path = str(path.relative_to(REPO_ROOT))
        payload = path.read_bytes()
        connection.execute(
            """
            INSERT INTO source_artifact(id, object_id, source_path, media_type, checksum_sha256, payload)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                stable_id("artifact", relative_path),
                objects_by_path.get(relative_path),
                relative_path,
                path.suffix.lstrip(".") or "plain",
                sha256(payload).hexdigest(),
                payload,
            ),
        )


def import_source_artifacts_from_support(connection: sqlite3.Connection) -> bool:
    manifest_path = SUPPORT_ROOT / "artifacts.manifest.json"
    if not manifest_path.exists():
        return False
    manifest = read_json(manifest_path)
    if not manifest:
        return False
    imported = 0
    for artifact in manifest:
        payload_path = SUPPORT_ROOT / artifact["payload_path"]
        if not payload_path.exists():
            continue
        payload = payload_path.read_bytes()
        connection.execute(
            """
            INSERT INTO source_artifact(id, object_id, source_path, media_type, checksum_sha256, payload)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                str(artifact["id"]),
                artifact.get("object_id"),
                str(artifact["source_path"]),
                str(artifact["media_type"]),
                str(artifact["checksum_sha256"]),
                payload,
            ),
        )
        imported += 1
    return imported > 0


def build_database() -> dict[str, int]:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    if DB_PATH.exists():
        DB_PATH.unlink()

    builder = Builder(DB_PATH)
    builder.create_schema()
    connection = builder.conn
    connection.execute("PRAGMA foreign_keys = OFF")

    for family in OBJECT_FAMILY_DIRECTORIES:
        for directory in object_dirs(CANONICAL_ROOT / family):
            meta = read_json(directory / "object.meta.json")
            source = meta["source"]
            builder.add_external_object(
                object_id=str(meta["id"]),
                object_type=str(meta["object_type"]),
                source_path=source.get("path"),
                source_format=source.get("format"),
                source_key=source.get("key"),
            )
            connection.execute("UPDATE content_object SET active=? WHERE id=?", (int(bool(meta.get("active", True))), str(meta["id"])))

            for identifier in meta.get("identifiers", []):
                builder.add_identifier(
                    str(meta["id"]),
                    str(identifier["id_system"]),
                    str(identifier["id_value"]),
                    preferred=bool(identifier.get("preferred", False)),
                )

            for scope, scope_payload in sorted((meta.get("metadata") or {}).items()):
                if not isinstance(scope_payload, dict):
                    continue
                for key, value in sorted(scope_payload.items()):
                    builder.add_metadata(str(meta["id"]), str(scope), str(key), value)

            for state in meta.get("review_states", []):
                builder.add_review_state("content_object", str(meta["id"]), state.get("language"), str(state["state"]))

            for slot in meta.get("text_slots", []):
                slot_id = builder.add_text_slot(
                    str(meta["id"]),
                    str(slot["slot_key"]),
                    str(slot["slot_type"]),
                    translation_group_key=slot.get("translation_group_key"),
                    sort_order=int(slot.get("sort_order", 0)),
                )
                storage = slot["storage"]
                if str(storage["kind"]) == "text_file":
                    for language, relative_name in sorted(storage_files_with_fallback(directory, storage.get("files")).items()):
                        builder.add_localized_text(slot_id, str(language), (directory / relative_name).read_text(encoding="utf-8"))
                elif str(storage["kind"]) == "json_file":
                    json_field = str(storage["json_field"])
                    for language, relative_name in sorted(storage_files_with_fallback(directory, storage.get("files")).items()):
                        payload = read_json(directory / relative_name)
                        builder.add_localized_text(slot_id, str(language), str(payload.get(json_field, "")))
                elif str(storage["kind"]) == "description_file_bundle":
                    for language, relative_name in sorted(storage_files_with_fallback(directory, storage.get("files")).items()):
                        raw_text = (directory / relative_name).read_text(encoding="utf-8")
                        short_text, long_text, _, _ = split_description_text(raw_text)
                        value = short_text if str(slot["slot_key"]) == "short_description" else long_text
                        builder.add_localized_text(slot_id, str(language), value)
                else:
                    raise RuntimeError(f"Unsupported slot storage kind: {storage['kind']}")

            for reference in read_json(directory / "object.references.json"):
                builder.add_reference(
                    str(meta["id"]),
                    str(reference["source_slot_key"]),
                    str(reference["raw_marker"]),
                    int(reference.get("sort_order", 0)),
                    ReferenceTarget(
                        reference.get("target_object_type"),
                        str(reference["target_id_system"]),
                        str(reference["target_id_value"]),
                        str(reference["relation_type"]),
                        inline_alias=reference.get("inline_alias"),
                        inline_label=reference.get("inline_label"),
                    ),
                )

            for annotation in read_json(directory / "object.annotations.json"):
                builder.add_annotation(
                    str(meta["id"]),
                    str(annotation["source_slot_key"]),
                    str(annotation["annotation_type"]),
                    annotation.get("annotation_key"),
                    annotation.get("annotation_value"),
                    str(annotation["raw_marker"]),
                    int(annotation.get("sort_order", 0)),
                )

    for edition_dir in object_dirs(CANONICAL_ROOT / "structure" / "editions"):
        edition_meta = read_json(edition_dir / "edition.meta.json")
        localized_payloads = {
            path.stem.split(".")[-1]: read_json(path)
            for path in sorted(edition_dir.glob("edition.*.json"))
            if path.name != "edition.meta.json"
        }
        edition_payload = localized_payloads.get("de")
        if edition_payload is None:
            raise RuntimeError(f"Missing edition.de.json in {edition_dir}")

        def build_language_index(node: dict[str, Any], language: str, index: dict[str, dict[str, Any]]) -> None:
            index[str(node["id"])] = {
                "language": language,
                "title": node.get("title"),
                "abstract": node.get("abstract"),
            }
            for child in node.get("chapters", []):
                build_language_index(child, language, index)
            for child in node.get("sections", []):
                build_language_index(child, language, index)

        localized_node_index: dict[str, dict[str, dict[str, Any]]] = {}
        for language, payload in localized_payloads.items():
            language_index: dict[str, dict[str, Any]] = {}
            build_language_index(payload, language, language_index)
            for node_id, values in language_index.items():
                localized_node_index.setdefault(node_id, {})[language] = values

        def insert_node(node: dict[str, Any], parent_node_id: str | None) -> None:
            connection.execute(
                """
                INSERT INTO curriculum_node(id, edition, node_type, parent_node_id, sort_order, source_path)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    str(node["id"]),
                    str(edition_meta["edition"]),
                    str(node["node_type"]),
                    parent_node_id,
                    int(node.get("sort_order", 0)),
                    edition_meta.get("source_path"),
                ),
            )
            for identifier in node.get("identifiers", []):
                builder.add_node_identifier(
                    str(node["id"]),
                    str(identifier["id_system"]),
                    str(identifier["id_value"]),
                    preferred=bool(identifier.get("preferred", False)),
                )
            for language, values in sorted(localized_node_index.get(str(node["id"]), {}).items()):
                builder.add_node_text(
                    str(node["id"]),
                    values.get("title"),
                    values.get("abstract"),
                    language=str(language),
                )
            for key, value in sorted((node.get("metadata") or {}).items()):
                builder.add_node_metadata(str(node["id"]), str(key), value)
            for placement in node.get("placements", []):
                builder.add_placement(
                    node_id=str(node["id"]),
                    object_id=str(placement["object_id"]),
                    placement_role=str(placement["placement_role"]),
                    sort_order=int(placement.get("sort_order", 0)),
                    visible_label=placement.get("visible_label"),
                )
            for child in node.get("chapters", []):
                insert_node(child, str(node["id"]))
            for child in node.get("sections", []):
                insert_node(child, str(node["id"]))

        insert_node(edition_payload, None)

    if not import_source_artifacts_from_support(connection):
        import_source_artifacts_from_repo(connection)

    connection.commit()
    connection.execute("PRAGMA foreign_keys = ON")
    integrity = connection.execute("PRAGMA integrity_check").fetchone()[0]
    if integrity != "ok":
        raise RuntimeError(f"SQLite integrity failure: {integrity}")
    foreign_key_errors = connection.execute("PRAGMA foreign_key_check").fetchall()
    if foreign_key_errors:
        raise RuntimeError(f"SQLite foreign-key failures: {len(foreign_key_errors)}")

    counts = {
        table: connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
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
    }
    builder.close()
    return counts


def main() -> None:
    print(json.dumps(build_database(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
