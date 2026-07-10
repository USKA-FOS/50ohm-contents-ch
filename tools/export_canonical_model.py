from __future__ import annotations

import json
import shutil
import sqlite3
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = REPO_ROOT / "work" / "global_model" / "content_model.sqlite"
CANONICAL_ROOT = REPO_ROOT / "canonical"
GENERATED_DIRECTORIES = ("objects", "texts", "metadata", "structure", "relations", "review", "artifacts")


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def rows(connection: sqlite3.Connection, sql: str, params: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
    return [dict(row) for row in connection.execute(sql, params)]


def export_canonical_model() -> dict[str, int]:
    for directory in GENERATED_DIRECTORIES:
        target = CANONICAL_ROOT / directory
        if target.exists():
            shutil.rmtree(target)

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    object_count = 0
    for obj in rows(connection, "SELECT * FROM content_object ORDER BY object_type, id"):
        object_count += 1
        object_id = obj["id"]
        write_json(
            CANONICAL_ROOT / "objects" / obj["object_type"] / f"{object_id}.json",
            {"id": object_id, "object_type": obj["object_type"], "active": obj["active"]},
        )
        write_json(
            CANONICAL_ROOT / "metadata" / "objects" / f"{object_id}.json",
            {
                "id": object_id,
                "source": {
                    "path": obj["source_path"],
                    "format": obj["source_format"],
                    "key": obj["source_key"],
                },
                "identifiers": rows(connection, "SELECT * FROM object_identifier WHERE object_id=? ORDER BY id", (object_id,)),
                "metadata": rows(connection, "SELECT * FROM object_metadata WHERE object_id=? ORDER BY id", (object_id,)),
            },
        )
        write_json(
            CANONICAL_ROOT / "relations" / "references" / f"{object_id}.json",
            rows(connection, "SELECT * FROM object_reference WHERE source_object_id=? ORDER BY id", (object_id,)),
        )
        write_json(
            CANONICAL_ROOT / "relations" / "annotations" / f"{object_id}.json",
            rows(connection, "SELECT * FROM text_annotation WHERE source_object_id=? ORDER BY id", (object_id,)),
        )

    slot_count = 0
    for slot in rows(connection, "SELECT * FROM text_slot ORDER BY id"):
        slot_count += 1
        localized = []
        for text in rows(connection, "SELECT * FROM localized_text WHERE text_slot_id=? ORDER BY id", (slot["id"],)):
            text_path = Path("texts") / "payload" / f"{text['id']}.txt"
            payload_path = CANONICAL_ROOT / text_path
            payload_path.parent.mkdir(parents=True, exist_ok=True)
            payload_path.write_text(text.pop("text_value"), encoding="utf-8")
            text["path"] = str(text_path)
            localized.append(text)
        slot["localized"] = localized
        write_json(CANONICAL_ROOT / "texts" / "slots" / f"{slot['id']}.json", slot)

    node_count = 0
    for node in rows(connection, "SELECT * FROM curriculum_node ORDER BY id"):
        node_count += 1
        node_id = node["id"]
        source_path = node.pop("source_path")
        write_json(CANONICAL_ROOT / "structure" / "nodes" / f"{node_id}.json", node)
        write_json(
            CANONICAL_ROOT / "metadata" / "nodes" / f"{node_id}.json",
            {
                "id": node_id,
                "source_path": source_path,
                "identifiers": rows(connection, "SELECT * FROM node_identifier WHERE node_id=? ORDER BY id", (node_id,)),
                "metadata": rows(connection, "SELECT * FROM node_metadata WHERE node_id=? ORDER BY id", (node_id,)),
            },
        )
        write_json(
            CANONICAL_ROOT / "structure" / "placements" / f"{node_id}.json",
            rows(connection, "SELECT * FROM content_placement WHERE node_id=? ORDER BY id", (node_id,)),
        )
        for node_text in rows(connection, "SELECT * FROM node_text WHERE node_id=? ORDER BY id", (node_id,)):
            for field in ("title", "abstract"):
                value = node_text.pop(field)
                if value is not None:
                    text_path = Path("texts") / "node_payload" / f"{node_text['id']}_{field}.txt"
                    payload_path = CANONICAL_ROOT / text_path
                    payload_path.parent.mkdir(parents=True, exist_ok=True)
                    payload_path.write_text(value, encoding="utf-8")
                    node_text[f"{field}_path"] = str(text_path)
                else:
                    node_text[f"{field}_path"] = None
            write_json(CANONICAL_ROOT / "texts" / "nodes" / f"{node_text['id']}.json", node_text)

    review_groups: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for state in rows(connection, "SELECT * FROM review_state ORDER BY subject_kind, subject_id, id"):
        review_groups.setdefault((state["subject_kind"], state["subject_id"]), []).append(state)
    for (subject_kind, subject_id), states in review_groups.items():
        write_json(CANONICAL_ROOT / "review" / subject_kind / f"{subject_id}.json", states)

    artifact_count = 0
    for artifact in connection.execute("SELECT * FROM source_artifact ORDER BY source_path"):
        artifact_count += 1
        artifact = dict(artifact)
        payload = artifact.pop("payload")
        payload_path = Path("artifacts") / artifact["source_path"]
        target = CANONICAL_ROOT / payload_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
        artifact["payload_path"] = str(payload_path)
        write_json(CANONICAL_ROOT / "metadata" / "artifacts" / f"{artifact['id']}.json", artifact)

    connection.close()
    summary = {"objects": object_count, "text_slots": slot_count, "nodes": node_count, "artifacts": artifact_count}
    write_json(CANONICAL_ROOT / "export_summary.json", summary)
    return summary


def main() -> None:
    print(json.dumps(export_canonical_model(), indent=2))


if __name__ == "__main__":
    main()
