from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sqlite3
from collections import defaultdict
from pathlib import Path
from typing import Any

from build_content_model_db import canonical_media_filename


REPO_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = REPO_ROOT / "work" / "global_model" / "content_model.sqlite"
CANONICAL_ROOT = REPO_ROOT / "canonical"
SUPPORT_ROOT = REPO_ROOT / "work" / "canonical_support"

OBJECT_FAMILY_LAYOUT = {
    "section_article": ("sections", "sc"),
    "slide_article": ("slides", "sl"),
    "solution_article": ("solutions", "s"),
    "snippet": ("snippets", "sn"),
    "static_page": ("static_pages", "sp"),
    "html_include": ("html_includes", "in"),
    "photo": ("photos", "ph"),
    "drawing": ("drawings", "dr"),
    "table_object": ("tables", "tb"),
    "legal_document": ("legal_documents", "ld"),
    "support_asset": ("support_assets", "sa"),
}
EXCLUDED_OBJECT_TYPES = {
    "question",
    "question_catalog_file",
    "question_layout_file",
    "question_metadata_file",
    "questions_readme",
    "toc_file",
}
NODE_PREFIX = {
    "curriculum_root": "ed",
    "curriculum_chapter": "ch",
    "curriculum_section": "se",
}
TEXT_FILE_EXT = {
    "markdown": "md",
    "html": "html",
    "plain_text": "txt",
    "text": "txt",
}


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def rows(connection: sqlite3.Connection, sql: str, params: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
    return [dict(row) for row in connection.execute(sql, params)]


def decode_value(value_json: str) -> Any:
    return json.loads(value_json)


def slugify(value: str) -> str:
    slug = re.sub(r"[^0-9A-Za-z]+", "_", value.strip()).strip("_").lower()
    return slug or "unnamed"


def stable_id(prefix: str, key: str) -> str:
    digest = hashlib.sha1(key.encode("utf-8")).hexdigest()[:12]
    return f"{prefix}_{digest}"


def source_key_for_object(obj: dict[str, Any]) -> str:
    if obj.get("source_key"):
        return str(obj["source_key"])
    if obj.get("source_path"):
        return Path(str(obj["source_path"])).stem
    return str(obj["id"])


def assign_object_ids(objects: list[dict[str, Any]]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for obj in objects:
        _, prefix = OBJECT_FAMILY_LAYOUT[str(obj["object_type"])]
        mapping[str(obj["id"])] = stable_id(prefix, f"{obj['object_type']}::{source_key_for_object(obj)}")
    return mapping


def preferred_identifier(identifiers: list[dict[str, Any]], preferred_system: str) -> str | None:
    for identifier in identifiers:
        if str(identifier["id_system"]) == preferred_system:
            return str(identifier["id_value"])
    preferred = next((item for item in identifiers if int(item.get("preferred", 0)) == 1), None)
    if preferred is not None:
        return str(preferred["id_value"])
    return None


def assign_node_ids(connection: sqlite3.Connection) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for node in rows(connection, "SELECT * FROM curriculum_node ORDER BY edition, node_type, id"):
        node_id = str(node["id"])
        node_type = str(node["node_type"])
        if str(node["edition"]) == "question_catalog_de":
            continue
        identifiers = rows(connection, "SELECT * FROM node_identifier WHERE node_id=? ORDER BY id", (node_id,))
        ident = preferred_identifier(identifiers, "toc_ident") or preferred_identifier(identifiers, "edition") or node_id
        prefix = NODE_PREFIX[node_type]
        stable_key = f"{node['edition']}::{node_type}::{ident}"
        mapping[node_id] = stable_id(prefix, stable_key)
    return mapping


def grouped_metadata(metadata_rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    grouped: dict[str, dict[str, Any]] = defaultdict(dict)
    for row in metadata_rows:
        grouped[str(row["metadata_scope"])][str(row["metadata_key"])] = decode_value(str(row["value_json"]))
    return dict(grouped)


def grouped_node_metadata(metadata_rows: list[dict[str, Any]]) -> dict[str, Any]:
    return {str(row["metadata_key"]): decode_value(str(row["value_json"])) for row in metadata_rows}


def simplify_identifiers(identifier_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "id_system": str(row["id_system"]),
            "id_value": str(row["id_value"]),
            "preferred": bool(int(row.get("preferred", 0))),
        }
        for row in identifier_rows
    ]


def simplify_review_states(review_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "language": row.get("language"),
            "state": str(row["state"]),
        }
        for row in review_rows
    ]


def slot_storage_name(slot_key: str, slot_type: str) -> str:
    if slot_key in {"body_markdown", "body_html", "body_text"}:
        return "body"
    return slot_key


def render_description_text(short_text: str, long_text: str, metadata: dict[str, dict[str, Any]]) -> str:
    reconstruction = metadata.get("reconstruction", {})
    description_format = reconstruction.get("description_source_format", "split_descriptions")
    description_preamble = reconstruction.get("description_preamble")
    if description_format == "single_description":
        return long_text
    return (
        (f"{description_preamble}\n\n" if description_preamble else "")
        + f"1) Kurzbeschreibung: {short_text}\n\n"
        + f"2) Ausführliche Beschreibung: {long_text}"
    )


def export_object(
    connection: sqlite3.Connection,
    obj: dict[str, Any],
    new_object_id: str,
    object_dir: Path,
) -> dict[str, Any]:
    legacy_object_id = str(obj["id"])
    slot_rows = rows(connection, "SELECT * FROM text_slot WHERE object_id=? ORDER BY sort_order, slot_key", (legacy_object_id,))
    identifiers = simplify_identifiers(
        rows(connection, "SELECT * FROM object_identifier WHERE object_id=? ORDER BY id", (legacy_object_id,))
    )
    metadata = grouped_metadata(rows(connection, "SELECT * FROM object_metadata WHERE object_id=? ORDER BY id", (legacy_object_id,)))
    review_states = simplify_review_states(
        rows(connection, "SELECT * FROM review_state WHERE subject_kind='content_object' AND subject_id=? ORDER BY id", (legacy_object_id,))
    )
    references = rows(connection, "SELECT * FROM object_reference WHERE source_object_id=? ORDER BY id", (legacy_object_id,))
    annotations = rows(connection, "SELECT * FROM text_annotation WHERE source_object_id=? ORDER BY id", (legacy_object_id,))

    localized_by_slot: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for slot in slot_rows:
        localized_by_slot[str(slot["id"])] = rows(
            connection,
            "SELECT * FROM localized_text WHERE text_slot_id=? ORDER BY language, id",
            (str(slot["id"]),),
        )

    multi_slot = len(slot_rows) > 1
    language_json_payloads: dict[str, dict[str, str]] = defaultdict(dict)
    exported_slots: list[dict[str, Any]] = []
    exported_languages: set[str] = set()
    media_description_keys = {"short_description", "long_description"}
    use_media_description_bundle = (
        str(obj["object_type"]) in {"photo", "drawing"}
        and {str(slot["slot_key"]) for slot in slot_rows} == media_description_keys
        and obj.get("source_key")
    )

    if use_media_description_bundle:
        values_by_language: dict[str, dict[str, str]] = defaultdict(dict)
        for slot in slot_rows:
            for text in localized_by_slot[str(slot["id"])]:
                language = str(text["language"])
                exported_languages.add(language)
                values_by_language[language][str(slot["slot_key"])] = str(text["text_value"])
        description_files: dict[str, str] = {}
        description_source_path = metadata.get("asset", {}).get("description_source_path")
        for language, values in sorted(values_by_language.items()):
            filename = canonical_media_filename(str(obj["source_key"]), language, ".txt")
            if language == "de" and description_source_path:
                source = REPO_ROOT / str(description_source_path)
                if source.exists():
                    shutil.copy2(source, object_dir / filename)
                else:
                    short_text = values.get("short_description", "")
                    long_text = values.get("long_description", short_text)
                    (object_dir / filename).write_text(
                        render_description_text(short_text, long_text, metadata),
                        encoding="utf-8",
                    )
            else:
                short_text = values.get("short_description", "")
                long_text = values.get("long_description", short_text)
                (object_dir / filename).write_text(
                    render_description_text(short_text, long_text, metadata),
                    encoding="utf-8",
                )
            description_files[language] = filename
        for slot in slot_rows:
            exported_slots.append(
                {
                    "slot_key": str(slot["slot_key"]),
                    "slot_type": str(slot["slot_type"]),
                    "translation_group_key": slot.get("translation_group_key"),
                    "sort_order": int(slot.get("sort_order", 0)),
                    "storage": {
                        "kind": "description_file_bundle",
                        "files": description_files,
                    },
                }
            )
    else:
        for slot in slot_rows:
            slot_id = str(slot["id"])
            slot_key = str(slot["slot_key"])
            slot_type = str(slot["slot_type"])
            sort_order = int(slot.get("sort_order", 0))
            translation_group_key = slot.get("translation_group_key")
            localized_files: dict[str, str] = {}

            for text in localized_by_slot[slot_id]:
                language = str(text["language"])
                exported_languages.add(language)
                value = str(text["text_value"])
                if multi_slot:
                    filename = f"content.{language}.json"
                    language_json_payloads[language][slot_key] = value
                    localized_files[language] = filename
                else:
                    extension = TEXT_FILE_EXT.get(slot_type, "txt")
                    basename = slot_storage_name(slot_key, slot_type)
                    filename = f"{basename}.{language}.{extension}"
                    (object_dir / filename).write_text(value, encoding="utf-8")
                    localized_files[language] = filename

            storage: dict[str, Any]
            if multi_slot:
                storage = {
                    "kind": "json_file",
                    "json_field": slot_key,
                    "files": localized_files,
                }
            else:
                storage = {
                    "kind": "text_file",
                    "files": localized_files,
                }

            exported_slots.append(
                {
                    "slot_key": slot_key,
                    "slot_type": slot_type,
                    "translation_group_key": translation_group_key,
                    "sort_order": sort_order,
                    "storage": storage,
                }
            )

    for language, payload in language_json_payloads.items():
        write_json(object_dir / f"content.{language}.json", payload)

    asset_files: dict[str, str] = {}
    language_variants: dict[str, dict[str, Any]] = defaultdict(lambda: {"asset_files": {}})
    language_assets = metadata.get("language_asset", {})
    for key, payload in sorted(language_assets.items()):
        language, _, asset_kind = key.partition(".")
        if not asset_kind or not isinstance(payload, dict):
            continue
        source_path = payload.get("source_path")
        canonical_file = payload.get("canonical_file")
        if not source_path or not canonical_file:
            continue
        source = REPO_ROOT / str(source_path)
        if source.exists():
            shutil.copy2(source, object_dir / str(canonical_file))
            language_variants[language]["asset_files"][asset_kind] = str(canonical_file)
    if not language_variants:
        for key, source_path in sorted(metadata.get("asset", {}).items()):
            source = REPO_ROOT / str(source_path)
            if source.exists():
                target_name = source.name
                shutil.copy2(source, object_dir / target_name)
                asset_files[key] = target_name

    meta = {
        "id": new_object_id,
        "object_type": str(obj["object_type"]),
        "active": bool(int(obj["active"])),
        "source": {
            "path": obj.get("source_path"),
            "format": obj.get("source_format"),
            "key": obj.get("source_key"),
        },
        "reconstruction": {
            "strategy": reconstruction_strategy(str(obj["object_type"]), obj.get("source_path"), obj.get("source_key")),
            "targets": reconstruction_targets(str(obj["object_type"]), obj.get("source_path"), obj.get("source_key")),
        },
        "identifiers": identifiers,
        "metadata": metadata,
        "review_states": review_states,
        "text_slots": exported_slots,
        "languages": sorted(exported_languages),
        "asset_files": asset_files,
    }
    if language_variants:
        review_by_language = {state.get("language"): state.get("state") for state in review_states if state.get("language")}
        for language, payload in language_variants.items():
            if language in review_by_language:
                payload["review_state"] = review_by_language[language]
        meta["language_variants"] = dict(sorted(language_variants.items()))
    write_json(object_dir / "object.meta.json", meta)

    exported_references = [
        {
            "source_slot_key": str(row["source_slot_key"]),
            "target_object_type": row.get("target_object_type"),
            "target_id_system": str(row["target_id_system"]),
            "target_id_value": str(row["target_id_value"]),
            "relation_type": str(row["relation_type"]),
            "inline_alias": row.get("inline_alias"),
            "inline_label": row.get("inline_label"),
            "raw_marker": str(row["raw_marker"]),
            "sort_order": int(row.get("sort_order", 0)),
        }
        for row in references
    ]
    exported_annotations = [
        {
            "source_slot_key": str(row["source_slot_key"]),
            "annotation_type": str(row["annotation_type"]),
            "annotation_key": row.get("annotation_key"),
            "annotation_value": row.get("annotation_value"),
            "raw_marker": str(row["raw_marker"]),
            "sort_order": int(row.get("sort_order", 0)),
        }
        for row in annotations
    ]
    write_json(object_dir / "object.references.json", exported_references)
    write_json(object_dir / "object.annotations.json", exported_annotations)
    return meta


def reconstruction_strategy(object_type: str, source_path: Any, source_key: Any) -> str:
    if source_path and str(source_path).startswith("contents/"):
        return "replace_source_file"
    if object_type == "support_asset" and source_path:
        return "replace_source_file"
    if object_type == "legal_document" and source_path:
        return "replace_source_file"
    if object_type == "photo":
        return "render_photo_description_file"
    if object_type == "drawing":
        return "render_drawing_assets_and_description"
    return "none"


def reconstruction_targets(object_type: str, source_path: Any, source_key: Any) -> list[dict[str, Any]]:
    if source_path and str(source_path).startswith("contents/"):
        return [
            {
                "path": str(source_path),
                "kind": "localized_text_file",
            }
        ]
    if object_type == "support_asset" and source_path:
        return [
            {
                "path": str(source_path),
                "kind": "localized_text_file",
            }
        ]
    if object_type == "legal_document" and source_path:
        return [
            {
                "path": str(source_path),
                "kind": "localized_text_file",
            }
        ]
    if object_type == "photo" and source_key:
        return [
            {
                "path": f"contents/photos/{source_key}.txt",
                "kind": "rendered_description_file",
                "slot_keys": ["short_description", "long_description"],
            }
        ]
    if object_type == "drawing" and source_key:
        return [
            {
                "path": f"contents/drawings/{source_key}.svg",
                "kind": "asset_file",
                "asset_key": "svg_path",
            },
            {
                "path": f"contents/drawings/{source_key}.tex",
                "kind": "asset_file",
                "asset_key": "tex_path",
            },
            {
                "path": f"contents/drawings/{source_key}.txt",
                "kind": "rendered_description_file",
                "slot_keys": ["short_description", "long_description"],
            }
        ]
    return []


def build_node_payload(
    connection: sqlite3.Connection,
    old_node_id: str,
    new_node_ids: dict[str, str],
    new_object_ids: dict[str, str],
    children_by_parent: dict[str | None, list[dict[str, Any]]],
) -> dict[str, Any]:
    node = rows(connection, "SELECT * FROM curriculum_node WHERE id=?", (old_node_id,))[0]
    node_text_rows = rows(connection, "SELECT * FROM node_text WHERE node_id=? ORDER BY id", (old_node_id,))
    node_text = next((row for row in node_text_rows if str(row["language"]) == "de"), None)
    identifiers = simplify_identifiers(rows(connection, "SELECT * FROM node_identifier WHERE node_id=? ORDER BY id", (old_node_id,)))
    metadata = grouped_node_metadata(rows(connection, "SELECT * FROM node_metadata WHERE node_id=? ORDER BY id", (old_node_id,)))
    placements = [
        {
            "object_id": new_object_ids.get(str(row["object_id"]), str(row["object_id"])),
            "placement_role": str(row["placement_role"]),
            "sort_order": int(row["sort_order"]),
            "visible_label": row.get("visible_label"),
        }
        for row in rows(connection, "SELECT * FROM content_placement WHERE node_id=? ORDER BY sort_order, id", (old_node_id,))
    ]
    payload = {
        "id": new_node_ids[old_node_id],
        "node_type": str(node["node_type"]),
        "sort_order": int(node["sort_order"]),
        "title": node_text.get("title") if node_text else None,
        "abstract": node_text.get("abstract") if node_text else None,
        "identifiers": identifiers,
        "metadata": metadata,
        "placements": placements,
    }
    child_nodes = children_by_parent.get(old_node_id, [])
    if child_nodes:
        key = "chapters" if str(node["node_type"]) == "curriculum_root" else "sections"
        payload[key] = [
            build_node_payload(connection, str(child["id"]), new_node_ids, new_object_ids, children_by_parent)
            for child in child_nodes
        ]
    return payload


def export_structure(connection: sqlite3.Connection, new_object_ids: dict[str, str], new_node_ids: dict[str, str]) -> int:
    all_nodes = rows(
        connection,
        """
        SELECT * FROM curriculum_node
        WHERE edition != 'question_catalog_de'
        ORDER BY edition, parent_node_id, sort_order, id
        """,
    )
    children_by_parent: dict[str | None, list[dict[str, Any]]] = defaultdict(list)
    roots_by_edition: dict[str, dict[str, Any]] = {}
    for node in all_nodes:
        if str(node["edition"]) == "question_catalog_de":
            continue
        parent_node_id = node.get("parent_node_id")
        if parent_node_id is None:
            roots_by_edition[str(node["edition"])] = node
        children_by_parent[parent_node_id].append(node)

    count = 0
    for edition, root in sorted(roots_by_edition.items()):
        count += 1
        edition_dir = CANONICAL_ROOT / "structure" / "editions" / edition
        edition_dir.mkdir(parents=True, exist_ok=True)
        payload = build_node_payload(connection, str(root["id"]), new_node_ids, new_object_ids, children_by_parent)
        write_json(
            edition_dir / "edition.meta.json",
            {
                "id": new_node_ids[str(root["id"])],
                "edition": edition,
                "source_path": root.get("source_path"),
                "node_type": str(root["node_type"]),
            },
        )
        write_json(edition_dir / "edition.de.json", payload)
    return count


def export_artifacts(connection: sqlite3.Connection, new_object_ids: dict[str, str]) -> int:
    artifact_root = SUPPORT_ROOT / "artifacts"
    manifest: list[dict[str, Any]] = []
    count = 0
    for artifact in connection.execute("SELECT * FROM source_artifact ORDER BY source_path"):
        count += 1
        artifact = dict(artifact)
        payload = artifact.pop("payload")
        source_path = str(artifact["source_path"])
        target_path = artifact_root / source_path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_bytes(payload)
        manifest.append(
            {
                "id": str(artifact["id"]),
                "object_id": new_object_ids.get(str(artifact.get("object_id"))) if artifact.get("object_id") else None,
                "source_path": source_path,
                "media_type": str(artifact["media_type"]),
                "checksum_sha256": str(artifact["checksum_sha256"]),
                "payload_path": str(Path("artifacts") / source_path),
            }
        )
    write_json(SUPPORT_ROOT / "artifacts.manifest.json", manifest)
    return count


def reset_export_targets(*, replace_existing: bool) -> None:
    canonical_exists = CANONICAL_ROOT.exists() and any(CANONICAL_ROOT.iterdir())
    support_exists = SUPPORT_ROOT.exists() and any(SUPPORT_ROOT.iterdir())
    if canonical_exists and not replace_existing:
        raise RuntimeError(
            "Refusing to replace existing canonical/. "
            "Canonical Git is the reference baseline. "
            "Use --replace-existing-canonical only for explicit initialization or controlled migration work."
        )
    if support_exists and not replace_existing:
        raise RuntimeError(
            "Refusing to replace existing work/canonical_support/. "
            "Use --replace-existing-canonical only for explicit initialization or controlled migration work."
        )
    if CANONICAL_ROOT.exists():
        shutil.rmtree(CANONICAL_ROOT)
    if SUPPORT_ROOT.exists():
        shutil.rmtree(SUPPORT_ROOT)
    CANONICAL_ROOT.mkdir(parents=True)
    SUPPORT_ROOT.mkdir(parents=True)


def export_canonical_model(*, replace_existing: bool = False) -> dict[str, int]:
    reset_export_targets(replace_existing=replace_existing)

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    objects = rows(connection, "SELECT * FROM content_object ORDER BY object_type, source_key, source_path, id")
    exported_objects = [obj for obj in objects if str(obj["object_type"]) in OBJECT_FAMILY_LAYOUT]
    new_object_ids = assign_object_ids(exported_objects)
    new_node_ids = assign_node_ids(connection)

    object_count = 0
    for obj in exported_objects:
        object_count += 1
        family, _ = OBJECT_FAMILY_LAYOUT[str(obj["object_type"])]
        object_dir = CANONICAL_ROOT / family / new_object_ids[str(obj["id"])]
        object_dir.mkdir(parents=True, exist_ok=True)
        export_object(connection, obj, new_object_ids[str(obj["id"])], object_dir)

    structure_count = export_structure(connection, new_object_ids, new_node_ids)
    artifact_count = export_artifacts(connection, new_object_ids)

    write_json(
        CANONICAL_ROOT / "_model.json",
        {
            "model": "object-centric-canonical",
            "version": 1,
            "languages": ["de"],
            "exported_object_types": sorted(OBJECT_FAMILY_LAYOUT),
            "excluded_object_types": sorted(EXCLUDED_OBJECT_TYPES),
            "support_artifacts_root": str(SUPPORT_ROOT.relative_to(REPO_ROOT)),
        },
    )
    summary = {
        "objects": object_count,
        "structure_editions": structure_count,
        "artifacts": artifact_count,
    }
    write_json(CANONICAL_ROOT / "export_summary.json", summary)
    connection.close()
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--replace-existing-canonical",
        action="store_true",
        help="Allow replacing canonical/ and work/canonical_support/. Use only for explicit initialization or migration work.",
    )
    args = parser.parse_args()
    print(json.dumps(export_canonical_model(replace_existing=args.replace_existing_canonical), indent=2))


if __name__ == "__main__":
    main()
