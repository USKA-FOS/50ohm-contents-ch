from __future__ import annotations

import argparse
import fcntl
import json
import os
import shutil
import sqlite3
import subprocess
import sys
from collections import defaultdict
from contextlib import contextmanager
from copy import deepcopy
from datetime import UTC, datetime
from hashlib import sha256
from pathlib import Path
from typing import Any

from build_db_from_canonical_model import build_database as build_canonical_database


CONTENT_REPO = Path(__file__).resolve().parent.parent
WORKSPACE_ROOT = CONTENT_REPO.parent
QUESTION_POOL_REPO = CONTENT_REPO.parent / "50ohm-question-pool"
GENERATOR_ROOT = WORKSPACE_ROOT / "50ohm-generator"
SOURCE_INPUT = WORKSPACE_ROOT / "site-original" / "app" / "50ohm-contents-ch"
SUPPORT_ROOT = CONTENT_REPO / "work" / "canonical_support"
DB_PATH = CONTENT_REPO / "work" / "canonical_model" / "content_model.sqlite"
DB_STATE_PATH = CONTENT_REPO / "work" / "canonical_model" / "content_model.state.json"
INPUT_ROOT = CONTENT_REPO / "work" / "generator-input"
BUILD_ROOT = CONTENT_REPO / "work" / "build"
REVIEW_BUILD_ROOT = WORKSPACE_ROOT / "sites" / "app" / "build"
VALIDATION_ROOT = CONTENT_REPO / "work" / "validation" / "multilingual"
LOCK_ROOT = CONTENT_REPO / "work" / "locks"
GENERATOR_EXTRA_CONTENT_ROOT = CONTENT_REPO / "generator_extra_content"
EDITION_ROOT = CONTENT_REPO / "canonical" / "structure" / "editions"
LANGUAGES = ("de", "fr", "it")
DEFAULT_GENERATOR_SEED = 50
OBJECT_FAMILY_DIRECTORIES = {
    "section_article": "sections",
    "slide_article": "slides",
    "solution_article": "solutions",
    "snippet": "snippets",
    "static_page": "static_pages",
    "html_include": "html_includes",
    "photo": "photos",
    "drawing": "drawings",
    "table_object": "tables",
    "legal_document": "legal_documents",
    "support_asset": "support_assets",
}
QUESTION_OBJECT_TYPES = {
    "question",
    "question_catalog_file",
    "question_layout_file",
    "question_metadata_file",
    "questions_readme",
}


def reset_runtime_state() -> None:
    """Ensure runtime directories exist before deriving anything from canonical Git."""
    for path in (VALIDATION_ROOT, LOCK_ROOT, DB_PATH.parent):
        path.mkdir(parents=True, exist_ok=True)


def sha256_file(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def tree_manifest(root: Path) -> dict[str, str]:
    if not root.exists():
        return {}
    return {
        str(path.relative_to(root)): sha256_file(path)
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def path_manifest(root: Path) -> list[str]:
    if not root.exists():
        return []
    return [str(path.relative_to(root)) for path in sorted(root.rglob("*")) if path.is_file()]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def decode_value(value_json: str) -> Any:
    return json.loads(value_json)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def make_run_id(languages: tuple[str, ...]) -> str:
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    return f"{timestamp}-{os.getpid()}-{'-'.join(languages)}"


def validation_run_root(run_id: str) -> Path:
    return VALIDATION_ROOT / "runs" / run_id


@contextmanager
def file_lock(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a+", encoding="utf-8") as handle:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


@contextmanager
def language_lock(language: str):
    with file_lock(LOCK_ROOT / f"multilingual-build-{language}.lock"):
        yield


def command_output(*args: str) -> str:
    completed = subprocess.run(
        list(args),
        cwd=CONTENT_REPO,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True,
    )
    return completed.stdout.strip()


def canonical_git_is_clean() -> bool:
    return command_output("git", "-C", str(CONTENT_REPO), "status", "--porcelain", "--", "canonical") == ""


def canonical_tree_hash() -> str:
    return command_output("git", "-C", str(CONTENT_REPO), "rev-parse", "HEAD:canonical")


def importer_signature() -> str:
    tool_files = (
        CONTENT_REPO / "tools" / "build_content_model_db.py",
        CONTENT_REPO / "tools" / "build_db_from_canonical_model.py",
    )
    digest = sha256()
    digest.update(sys.version.encode("utf-8"))
    for path in tool_files:
        digest.update(str(path.relative_to(CONTENT_REPO)).encode("utf-8"))
        digest.update(path.read_bytes())
    return digest.hexdigest()


def support_artifact_signature() -> str:
    manifest_path = SUPPORT_ROOT / "artifacts.manifest.json"
    digest = sha256()
    if not manifest_path.exists():
        digest.update(b"missing")
        return digest.hexdigest()
    manifest_bytes = manifest_path.read_bytes()
    digest.update(manifest_bytes)
    manifest = json.loads(manifest_bytes.decode("utf-8"))
    for artifact in manifest:
        payload_path = SUPPORT_ROOT / str(artifact["payload_path"])
        digest.update(str(artifact["source_path"]).encode("utf-8"))
        digest.update(str(artifact.get("checksum_sha256", "")).encode("utf-8"))
        if payload_path.exists():
            digest.update(payload_path.read_bytes())
        else:
            digest.update(b"missing-payload")
    return digest.hexdigest()


def current_db_state() -> dict[str, Any]:
    return {
        "canonical_tree_hash": canonical_tree_hash(),
        "importer_signature": importer_signature(),
        "support_artifact_signature": support_artifact_signature(),
    }


def should_rebuild_database() -> tuple[bool, str, dict[str, Any]]:
    state = current_db_state()
    if not DB_PATH.exists():
        return True, "database_missing", state
    if not DB_STATE_PATH.exists():
        return True, "state_missing", state
    if not canonical_git_is_clean():
        return True, "canonical_dirty", state
    previous_state = load_json(DB_STATE_PATH)
    if previous_state.get("canonical_tree_hash") != state["canonical_tree_hash"]:
        return True, "canonical_changed", state
    if previous_state.get("importer_signature") != state["importer_signature"]:
        return True, "importer_changed", state
    if previous_state.get("support_artifact_signature") != state["support_artifact_signature"]:
        return True, "support_artifacts_changed", state
    return False, "reused", state


def prepare_canonical_database() -> dict[str, Any]:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    rebuild, reason, state = should_rebuild_database()
    if rebuild:
        with file_lock(LOCK_ROOT / "canonical-db-rebuild.lock"):
            rebuild, reason, state = should_rebuild_database()
            if rebuild:
                if DB_PATH.exists():
                    DB_PATH.unlink(missing_ok=True)
                db_counts = build_canonical_database()
                write_json(DB_STATE_PATH, state)
                return {
                    "database": str(DB_PATH),
                    "state_file": str(DB_STATE_PATH),
                    "reused": False,
                    "reason": reason,
                    "counts": db_counts,
                    "state": state,
                }
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    counts = {
        table: connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        for table in (
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
        )
    }
    connection.close()
    return {
        "database": str(DB_PATH),
        "state_file": str(DB_STATE_PATH),
        "reused": True,
        "reason": reason,
        "counts": counts,
        "state": state,
    }


def rows(connection: sqlite3.Connection, sql: str, params: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
    return [dict(row) for row in connection.execute(sql, params)]


def choose_language(values: dict[str, str], language: str) -> str | None:
    return values.get(language) or values.get("de") or next(iter(values.values()), None)


def export_artifacts(connection: sqlite3.Connection, target_root: Path) -> int:
    if target_root.exists():
        shutil.rmtree(target_root)
    target_root.mkdir(parents=True)
    count = 0
    for row in connection.execute("SELECT source_path, payload FROM source_artifact ORDER BY source_path"):
        target = target_root / row["source_path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(row["payload"])
        count += 1
    return count


def append_usage(
    usage: list[dict[str, Any]],
    *,
    path: str,
    action: str,
    origin: str,
    object_id: str | None = None,
    object_type: str | None = None,
    slot_keys: list[str] | None = None,
) -> None:
    usage.append(
        {
            "path": path,
            "action": action,
            "origin": origin,
            "object_id": object_id,
            "object_type": object_type,
            "slot_keys": slot_keys or [],
        }
    )


def overlay_object_texts(connection: sqlite3.Connection, target_root: Path, language: str) -> dict[str, Any]:
    query = """
        SELECT o.id AS object_id, o.object_type, o.source_path, o.source_key,
               s.slot_key, lt.language, lt.text_value
        FROM content_object o
        JOIN text_slot s ON s.object_id = o.id
        JOIN localized_text lt ON lt.text_slot_id = s.id
        WHERE o.object_type NOT IN ({})
        ORDER BY o.id, s.sort_order, lt.language
    """.format(",".join("?" for _ in QUESTION_OBJECT_TYPES))
    grouped: dict[tuple[str, str], dict[str, Any]] = defaultdict(lambda: {"texts": {}})
    for row in rows(connection, query, tuple(sorted(QUESTION_OBJECT_TYPES))):
        key = (row["object_id"], row["slot_key"])
        grouped[key].update(
            {
                "object_type": row["object_type"],
                "source_path": row["source_path"],
                "source_key": row["source_key"],
            }
        )
        grouped[key]["texts"][row["language"]] = row["text_value"]

    reconstruction_metadata: dict[str, dict[str, Any]] = defaultdict(dict)
    for row in rows(
        connection,
        """
        SELECT object_id, metadata_key, value_json
        FROM object_metadata
        WHERE metadata_scope='reconstruction'
        ORDER BY object_id, metadata_key
        """,
    ):
        reconstruction_metadata[str(row["object_id"])][str(row["metadata_key"])] = decode_value(str(row["value_json"]))

    by_object: dict[str, dict[str, Any]] = defaultdict(dict)
    written = 0
    usage: list[dict[str, Any]] = []
    for (object_id, slot_key), payload in grouped.items():
        by_object[object_id]["object_type"] = payload["object_type"]
        by_object[object_id]["source_path"] = payload["source_path"]
        by_object[object_id]["source_key"] = payload["source_key"]
        by_object[object_id]["object_id"] = object_id
        by_object[object_id].setdefault("slot_keys", []).append(slot_key)
        by_object[object_id][slot_key] = choose_language(payload["texts"], language)

    for payload in by_object.values():
        object_type = payload["object_type"]
        source_path = payload["source_path"]
        text = None
        for slot_key in ("body_markdown", "body_html", "body_text"):
            if slot_key in payload and payload[slot_key] is not None:
                text = payload[slot_key]
                break
        if source_path and text is not None:
            append_usage(
                usage,
                path=str(source_path),
                action="overwritten_from_canonical",
                origin="content_object",
                object_id=str(payload["object_id"]),
                object_type=str(object_type),
                slot_keys=sorted(payload.get("slot_keys", [])),
            )
            (target_root / source_path).write_text(text, encoding="utf-8")
            written += 1
            continue
        if object_type in {"photo", "drawing"} and payload.get("source_key"):
            family = "photos" if object_type == "photo" else "drawings"
            relative_target = Path("contents") / family / f"{payload['source_key']}.txt"
            object_dir = canonical_object_dir(str(object_type), str(payload["object_id"]))
            canonical_candidate = None
            if object_dir is not None:
                preferred = object_dir / f"{payload['source_key']}.{language}.txt"
                fallback = object_dir / f"{payload['source_key']}.de.txt"
                if preferred.exists():
                    canonical_candidate = preferred
                elif fallback.exists():
                    canonical_candidate = fallback
            if canonical_candidate is not None:
                rendered_text = canonical_candidate.read_text(encoding="utf-8")
                origin = "content_object_description_file"
                action = "overwritten_from_canonical"
            else:
                short_text = payload.get("short_description") or ""
                long_text = payload.get("long_description") or short_text
                description_format = reconstruction_metadata.get(str(payload["object_id"]), {}).get(
                    "description_source_format",
                    "split_descriptions",
                )
                description_preamble = reconstruction_metadata.get(str(payload["object_id"]), {}).get(
                    "description_preamble"
                )
                if description_format == "single_description":
                    rendered_text = long_text
                else:
                    rendered_text = (
                        (f"{description_preamble}\n\n" if description_preamble else "")
                        +
                        f"1) Kurzbeschreibung: {short_text}\n\n"
                        f"2) Ausführliche Beschreibung: {long_text}"
                    )
                origin = "content_object"
                action = "rendered_from_canonical"
            append_usage(
                usage,
                path=str(relative_target),
                action=action,
                origin=origin,
                object_id=str(payload["object_id"]),
                object_type=str(object_type),
                slot_keys=sorted(payload.get("slot_keys", [])),
            )
            target = target_root / relative_target
            target.write_text(rendered_text, encoding="utf-8")
            written += 1
    return {"written_files": written, "usage": usage}


def canonical_object_dir(object_type: str, object_id: str) -> Path | None:
    family = OBJECT_FAMILY_DIRECTORIES.get(object_type)
    if not family:
        return None
    return CONTENT_REPO / "canonical" / family / object_id


def overlay_object_assets(connection: sqlite3.Connection, target_root: Path, language: str) -> dict[str, Any]:
    asset_rows = rows(
        connection,
        """
        SELECT o.id AS object_id, o.object_type, m.metadata_scope, m.metadata_key, m.value_json
        FROM content_object o
        JOIN object_metadata m ON m.object_id = o.id
        WHERE m.metadata_scope IN ('asset', 'language_asset')
        ORDER BY o.id, m.metadata_scope, m.metadata_key
        """
    )
    usage: list[dict[str, Any]] = []
    written = 0
    object_types = {str(row["object_id"]): str(row["object_type"]) for row in asset_rows}
    grouped_language_assets: dict[tuple[str, str], dict[str, dict[str, Any]]] = defaultdict(dict)
    fallback_assets: list[dict[str, Any]] = []
    for row in asset_rows:
        if str(row["metadata_scope"]) == "language_asset":
            metadata_key = str(row["metadata_key"])
            lang_key, _, asset_kind = metadata_key.partition(".")
            if asset_kind:
                grouped_language_assets[(str(row["object_id"]), asset_kind)][lang_key] = decode_value(str(row["value_json"]))
        else:
            fallback_assets.append(row)

    handled_fallback_keys: set[tuple[str, str]] = set()
    for (object_id, asset_kind), variants in grouped_language_assets.items():
        selected = variants.get(language) or variants.get("de")
        if not isinstance(selected, dict):
            continue
        source_path = selected.get("source_path")
        canonical_file = selected.get("canonical_file")
        object_type = object_types.get(object_id)
        object_dir = canonical_object_dir(str(object_type), object_id) if object_type else None
        if object_dir is None:
            continue
        canonical_asset = object_dir / str(canonical_file)
        if not canonical_asset.exists():
            continue
        target = target_root / str(source_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(canonical_asset, target)
        append_usage(
            usage,
            path=str(source_path),
            action="overwritten_from_canonical",
            origin="content_object_asset",
            object_id=object_id,
            object_type=str(object_type),
            slot_keys=[asset_kind],
        )
        written += 1
        handled_fallback_keys.add((object_id, asset_kind))

    fallback_key_map = {
        "image_path": "image",
        "svg_path": "svg",
        "tex_path": "tex",
    }
    for row in fallback_assets:
        object_id = str(row["object_id"])
        object_type = str(row["object_type"])
        metadata_key = str(row["metadata_key"])
        if metadata_key == "description_source_path":
            continue
        if (object_id, fallback_key_map.get(metadata_key, metadata_key)) in handled_fallback_keys:
            continue
        source_path = str(decode_value(str(row["value_json"])))
        object_dir = canonical_object_dir(object_type, object_id)
        if object_dir is None:
            continue
        source_name = Path(source_path).name
        canonical_asset = object_dir / source_name
        if not canonical_asset.exists():
            continue
        target = target_root / source_path
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(canonical_asset, target)
        append_usage(
            usage,
            path=source_path,
            action="overwritten_from_canonical",
            origin="content_object_asset",
            object_id=object_id,
            object_type=object_type,
            slot_keys=[metadata_key],
        )
        written += 1
    return {"written_files": written, "usage": usage}


def children_by_parent(connection: sqlite3.Connection, source_path: str) -> dict[str | None, list[dict[str, Any]]]:
    children: dict[str | None, list[dict[str, Any]]] = defaultdict(list)
    for node in rows(
        connection,
        """
        SELECT id, node_type, parent_node_id, sort_order
        FROM curriculum_node
        WHERE source_path=?
        ORDER BY parent_node_id, sort_order
        """,
        (source_path,),
    ):
        children[node["parent_node_id"]].append(node)
    return children


def localized_node_texts(connection: sqlite3.Connection, language: str) -> dict[str, dict[str, str | None]]:
    values: dict[str, dict[str, dict[str, str | None]]] = defaultdict(dict)
    for text in rows(connection, "SELECT node_id, language, title, abstract FROM node_text ORDER BY node_id, language"):
        values[text["node_id"]][text["language"]] = {"title": text["title"], "abstract": text["abstract"]}
    return {node_id: choose_node_language(localized, language) for node_id, localized in values.items()}


def choose_node_language(localized: dict[str, dict[str, str | None]], language: str) -> dict[str, str | None]:
    return localized.get(language) or localized.get("de") or next(iter(localized.values()))


def apply_node_text(payload: dict[str, Any], text: dict[str, str | None] | None) -> None:
    if not text:
        return
    if text.get("title") is not None:
        payload["title"] = text["title"]
    if "abstract" in payload and text.get("abstract") is not None:
        payload["abstract"] = text["abstract"]


def stage_toc_files(target_root: Path, language: str) -> dict[str, Any]:
    toc_root = target_root / "toc"
    toc_root.mkdir(parents=True, exist_ok=True)
    written = 0
    usage: list[dict[str, Any]] = []
    for edition_dir in sorted(EDITION_ROOT.iterdir()):
        if not edition_dir.is_dir():
            continue
        edition_meta = load_json(edition_dir / "edition.meta.json")
        source_path = edition_dir / f"edition.{language}.json"
        if not source_path.exists():
            source_path = edition_dir / "edition.de.json"
        target_path = toc_root / f"{edition_meta['edition']}.json"
        write_json(target_path, load_json(source_path))
        append_usage(
            usage,
            path=str(target_path.relative_to(target_root)),
            action="overwritten_from_canonical",
            origin="curriculum_root",
            object_id=str(edition_meta["id"]),
            object_type=str(edition_meta["node_type"]),
            slot_keys=["title", "abstract"],
        )
        written += 1
    return {"written_files": written, "usage": usage}


def overlay_toc_texts(connection: sqlite3.Connection, target_root: Path, language: str) -> dict[str, Any]:
    staged = stage_toc_files(target_root, language)
    if language == "de":
        return staged
    node_texts = localized_node_texts(connection, language)
    written = staged["written_files"]
    usage: list[dict[str, Any]] = list(staged["usage"])
    for toc_path in sorted((target_root / "toc").glob("*.json")):
        source_path = str(toc_path.relative_to(target_root))
        children = children_by_parent(connection, source_path)
        roots = children.get(None, [])
        if not roots:
            continue
        root = roots[0]
        payload = load_json(toc_path)
        apply_node_text(payload, node_texts.get(root["id"]))

        def walk(container: dict[str, Any], parent_id: str) -> None:
            node_children = children.get(parent_id, [])
            json_children = container.get("chapters", container.get("sections", []))
            for node, child_payload in zip(node_children, json_children):
                apply_node_text(child_payload, node_texts.get(node["id"]))
                walk(child_payload, node["id"])

        walk(payload, root["id"])
        append_usage(
            usage,
            path=source_path,
            action="overwritten_from_canonical",
            origin="curriculum_node",
            object_id=str(root["id"]),
            object_type=str(root["node_type"]),
            slot_keys=["title", "abstract"],
        )
        write_json(toc_path, payload)
        written += 1
    return {"written_files": written, "usage": usage}


def iter_questions(payload: dict[str, Any]):
    for exam_part in payload.get("sections", []):
        for chapter in exam_part.get("sections", []):
            for question in chapter.get("questions", []):
                yield question
            for section in chapter.get("sections", []):
                for question in section.get("questions", []):
                    yield question


def source_rationales() -> tuple[dict[str, Any], dict[str, Any]]:
    source = load_json(
        QUESTION_POOL_REPO / "builds" / "de" / "question_pool_rev0_ch-de.json"
    )
    rationales = {question["number"]: question.get("HB.rationale") for question in iter_questions(source)}
    return rationales, deepcopy(source.get("pruned", {}))


def stage_questions(target_root: Path, language: str) -> dict[str, Any]:
    questions_dir = target_root / "contents" / "questions"
    questions_dir.mkdir(parents=True, exist_ok=True)
    source_build = QUESTION_POOL_REPO / "builds" / language / f"question_pool_rev0_ch-{language}.json"
    payload = load_json(source_build)
    rationales, pruned = source_rationales()
    question_count = 0
    for question in iter_questions(payload):
        number = question.get("number")
        question["HB.rationale"] = rationales.get(number) if language == "de" else None
        question_count += 1
    payload["pruned"] = pruned if language == "de" else {}
    write_json(questions_dir / "fragenkatalog_ch.json", payload)
    # The review generator shows correction/diff markup whenever the upstream
    # catalog differs from the selected catalog. For localized builds, the
    # canonical question-pool build is the source of truth, so the upstream
    # compatibility file must be identical.
    write_json(questions_dir / "fragenkatalog_4pre.json", payload)
    return {
        "question_catalog": str(source_build),
        "questions": question_count,
        "usage": [
            {
                "path": "contents/questions/fragenkatalog_ch.json",
                "action": "overwritten_from_question_pool",
                "origin": "question_pool",
                "object_id": None,
                "object_type": "question_catalog_file",
                "slot_keys": [],
            },
            {
                "path": "contents/questions/fragenkatalog_4pre.json",
                "action": "overwritten_from_question_pool",
                "origin": "question_pool",
                "object_id": None,
                "object_type": "question_catalog_file",
                "slot_keys": [],
            },
        ],
    }


def retained_support_artifacts(target_root: Path, usage_entries: list[dict[str, Any]]) -> list[str]:
    replaced = {entry["path"] for entry in usage_entries}
    retained: list[str] = []
    for path in sorted(target_root.rglob("*")):
        if not path.is_file():
            continue
        relative = str(path.relative_to(target_root))
        if relative not in replaced:
            retained.append(relative)
    return retained


def usage_action_counts(usage_entries: list[dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for entry in usage_entries:
        action = str(entry["action"])
        counts[action] = counts.get(action, 0) + 1
    return counts


def stage_language(
    connection: sqlite3.Connection,
    language: str,
    *,
    validation_root: Path,
) -> dict[str, Any]:
    target_root = INPUT_ROOT / language
    artifact_count = export_artifacts(connection, target_root)
    text_report = overlay_object_texts(connection, target_root, language)
    asset_report = overlay_object_assets(connection, target_root, language)
    toc_report = overlay_toc_texts(connection, target_root, language)
    if GENERATOR_EXTRA_CONTENT_ROOT.exists():
        staged_extra_root = target_root / "generator_extra_content"
        if staged_extra_root.exists():
            shutil.rmtree(staged_extra_root)
        shutil.copytree(GENERATOR_EXTRA_CONTENT_ROOT, staged_extra_root)
    question_info = stage_questions(target_root, language)
    usage_entries = text_report["usage"] + asset_report["usage"] + toc_report["usage"] + question_info["usage"]
    retained = retained_support_artifacts(target_root, usage_entries)
    usage_report = {
        "language": language,
        "replaced_or_rendered": usage_entries,
        "retained_paths": retained,
        "retained_count": len(retained),
        "action_counts": usage_action_counts(usage_entries),
    }
    usage_report_path = validation_root / f"support-artifact-usage-{language}.json"
    write_json(usage_report_path, usage_report)
    return {
        "input_root": str(target_root),
        "source_artifacts": artifact_count,
        "localized_text_files": text_report["written_files"],
        "canonical_asset_files": asset_report["written_files"],
        "localized_toc_files": toc_report["written_files"],
        "question_catalog": question_info["question_catalog"],
        "questions": question_info["questions"],
        "support_artifact_usage": {
            "report_path": str(usage_report_path),
            "replaced_or_rendered_count": len(usage_entries),
            "action_counts": usage_report["action_counts"],
            "retained_paths": retained[:500],
            "retained_count": len(retained),
        },
    }


def validate_staged_generator_input(target_root: Path) -> None:
    required_dirs = [
        target_root / "toc",
        target_root / "contents" / "questions",
        target_root / "contents" / "html",
        target_root / "contents" / "drawings",
        target_root / "contents" / "photos",
        target_root / "contents" / "sections",
        target_root / "contents" / "slides",
        target_root / "contents" / "snippets",
        target_root / "contents" / "static",
        target_root / "contents" / "solutions",
        target_root / "generator_extra_content",
    ]
    required_files = [
        target_root / "contents" / "questions" / "fragenkatalog_ch.json",
        target_root / "contents" / "questions" / "fragenkatalog_4pre.json",
        target_root / "contents" / "questions" / "metadata3b.json",
    ]
    for edition_dir in sorted(EDITION_ROOT.iterdir()):
        if edition_dir.is_dir():
            edition = load_json(edition_dir / "edition.meta.json")["edition"]
            required_files.append(target_root / "toc" / f"{edition}.json")

    missing_dirs = [str(path.relative_to(target_root)) for path in required_dirs if not path.is_dir()]
    missing_files = [str(path.relative_to(target_root)) for path in required_files if not path.is_file()]
    empty_dirs = []
    for path in required_dirs:
        if path.is_dir() and not any(path.iterdir()):
            empty_dirs.append(str(path.relative_to(target_root)))
    if missing_dirs or missing_files or empty_dirs:
        problems = []
        if missing_dirs:
            problems.append(f"missing_dirs={missing_dirs}")
        if missing_files:
            problems.append(f"missing_files={missing_files}")
        if empty_dirs:
            problems.append(f"empty_dirs={empty_dirs}")
        raise RuntimeError(
            "Staged generator input is incomplete: " + "; ".join(problems)
        )


def build_config(input_root: Path, output_root: Path, *, generator_seed: int) -> dict[str, Any]:
    return {
        "input": str(input_root),
        "questions": "fragenkatalog_ch.json",
        "questions_upstream": "fragenkatalog_4pre.json",
        "repo_base_url": "https://github.com/USKA-FOS/50ohm-contents-ch",
        "output": str(output_root),
        "random_seed": generator_seed,
    }


def sync_review_build(language: str, output_root: Path) -> Path:
    target_root = REVIEW_BUILD_ROOT / language
    target_root.parent.mkdir(parents=True, exist_ok=True)
    if target_root.exists():
        shutil.rmtree(target_root)
    shutil.copytree(output_root, target_root)
    return target_root


def run_generator(language: str, *, validation_root: Path, generator_seed: int) -> dict[str, Any]:
    validation_root.mkdir(parents=True, exist_ok=True)
    runner_root = validation_root / f"generator-{language}"
    output_root = BUILD_ROOT / language
    validate_staged_generator_input(INPUT_ROOT / language)
    BUILD_ROOT.mkdir(parents=True, exist_ok=True)
    if runner_root.exists():
        shutil.rmtree(runner_root)
    if output_root.exists():
        shutil.rmtree(output_root)
    shutil.copytree(GENERATOR_ROOT, runner_root, ignore=shutil.ignore_patterns(".git", "__pycache__", ".venv"))
    write_json(
        runner_root / "config" / "config.json",
        build_config(INPUT_ROOT / language, output_root, generator_seed=generator_seed),
    )
    completed = subprocess.run(
        ["uv", "run", "python3", "build.py"],
        cwd=runner_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False,
    )
    log_path = validation_root / f"{language}.log"
    log_path.write_text(completed.stdout, encoding="utf-8")
    if completed.returncode != 0:
        raise RuntimeError(
            f"Generator build failed for {language}; see log {log_path}"
        )
    review_output_root = sync_review_build(language, output_root)
    return {
        "exit_code": completed.returncode,
        "log": str(log_path),
        "output_root": str(output_root),
        "output_files": len(path_manifest(output_root)),
        "review_output_root": str(review_output_root),
        "generator_seed": generator_seed,
        "ui_patch": None,
    }


def compare_outputs(builds: dict[str, dict[str, Any]], languages: tuple[str, ...]) -> dict[str, Any]:
    manifests = {language: path_manifest(BUILD_ROOT / language) for language in languages}
    result: dict[str, Any] = {}
    for language in languages:
        manifest = manifests[language]
        result[language] = {
            "file_count": len(manifest),
            "html_count": sum(1 for path in manifest if path.endswith(".html")),
            "asset_count": sum(1 for path in manifest if path.startswith("assets/")),
        }
    if "de" in manifests:
        de_paths = set(manifests["de"])
        for language in ("fr", "it"):
            if language not in manifests:
                continue
            paths = set(manifests[language])
            result[f"de_vs_{language}"] = {
                "only_in_de": sorted(de_paths - paths)[:200],
                "only_in_language": sorted(paths - de_paths)[:200],
                "only_in_de_count": len(de_paths - paths),
                "only_in_language_count": len(paths - de_paths),
            }
    result["all_builds_succeeded"] = all(builds[language]["exit_code"] == 0 for language in languages)
    return result


def run(
    *,
    skip_build: bool = False,
    languages: tuple[str, ...] = LANGUAGES,
    generator_seed: int = DEFAULT_GENERATOR_SEED,
) -> dict[str, Any]:
    reset_runtime_state()
    run_id = make_run_id(languages)
    run_validation_root = validation_run_root(run_id)
    run_validation_root.mkdir(parents=True, exist_ok=True)
    db_info = prepare_canonical_database()
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    staged: dict[str, dict[str, Any]] = {}
    builds: dict[str, dict[str, Any]] = {}
    for language in languages:
        with language_lock(language):
            staged[language] = stage_language(
                connection,
                language,
                validation_root=run_validation_root,
            )
            if not skip_build:
                builds[language] = run_generator(
                    language,
                    validation_root=run_validation_root,
                    generator_seed=generator_seed,
                )
    connection.close()
    comparison = compare_outputs(builds, languages) if builds else {}
    report = {
        "run_id": run_id,
        "validation_root": str(run_validation_root),
        "report_path": str(run_validation_root / "summary.json"),
        "database": str(DB_PATH),
        "database_counts": db_info["counts"],
        "database_reused": db_info["reused"],
        "database_reason": db_info["reason"],
        "database_state": db_info["state"],
        "generator_seed": generator_seed,
        "staged": staged,
        "builds": builds,
        "comparison": comparison,
    }
    write_json(run_validation_root / "summary.json", report)
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-build", action="store_true")
    parser.add_argument(
        "--generator-seed",
        type=int,
        default=DEFAULT_GENERATOR_SEED,
        help=(
            "Deterministic seed passed to the site generator for answer shuffling. "
            f"Defaults to {DEFAULT_GENERATOR_SEED} for reproducible validation builds."
        ),
    )
    parser.add_argument(
        "--language",
        choices=LANGUAGES,
        help="Limit staging and build to a single language.",
    )
    args = parser.parse_args()
    languages = (args.language,) if args.language else LANGUAGES
    report = run(
        skip_build=args.skip_build,
        languages=languages,
        generator_seed=args.generator_seed,
    )
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
