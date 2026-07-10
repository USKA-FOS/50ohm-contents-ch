from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any, Iterable

from build_content_model_db import Builder


REPO_ROOT = Path(__file__).resolve().parent.parent
CANONICAL_ROOT = REPO_ROOT / "canonical"
DB_PATH = REPO_ROOT / "work" / "canonical_model" / "content_model.sqlite"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def insert_row(connection: sqlite3.Connection, table: str, row: dict[str, Any]) -> None:
    columns = list(row)
    placeholders = ", ".join("?" for _ in columns)
    connection.execute(
        f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})",
        [row[column] for column in columns],
    )


def json_files(directory: Path) -> Iterable[Path]:
    return sorted(path for path in directory.rglob("*.json") if path.is_file())


def build_database() -> dict[str, int]:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    if DB_PATH.exists():
        DB_PATH.unlink()
    builder = Builder(DB_PATH)
    builder.create_schema()
    connection = builder.conn
    # Canonical node files are ordered by stable id, not by parent hierarchy.
    # Validate all foreign keys after loading the complete graph instead.
    connection.execute("PRAGMA foreign_keys = OFF")

    for path in json_files(CANONICAL_ROOT / "objects"):
        obj = read_json(path)
        metadata = read_json(CANONICAL_ROOT / "metadata" / "objects" / f"{obj['id']}.json")
        source = metadata["source"]
        insert_row(
            connection,
            "content_object",
            {
                "id": obj["id"],
                "object_type": obj["object_type"],
                "source_path": source["path"],
                "source_format": source["format"],
                "source_key": source["key"],
                "active": obj["active"],
            },
        )
        for identifier in metadata["identifiers"]:
            insert_row(connection, "object_identifier", identifier)
        for value in metadata["metadata"]:
            insert_row(connection, "object_metadata", value)

    for path in json_files(CANONICAL_ROOT / "texts" / "slots"):
        slot = read_json(path)
        localized = slot.pop("localized")
        insert_row(connection, "text_slot", slot)
        for text in localized:
            payload = (CANONICAL_ROOT / text.pop("path")).read_text(encoding="utf-8")
            text["text_value"] = payload
            insert_row(connection, "localized_text", text)

    for path in json_files(CANONICAL_ROOT / "structure" / "nodes"):
        node = read_json(path)
        metadata = read_json(CANONICAL_ROOT / "metadata" / "nodes" / f"{node['id']}.json")
        node["source_path"] = metadata["source_path"]
        insert_row(connection, "curriculum_node", node)
        for identifier in metadata["identifiers"]:
            insert_row(connection, "node_identifier", identifier)
        for value in metadata["metadata"]:
            insert_row(connection, "node_metadata", value)
        for placement in read_json(CANONICAL_ROOT / "structure" / "placements" / f"{node['id']}.json"):
            insert_row(connection, "content_placement", placement)

    for path in json_files(CANONICAL_ROOT / "texts" / "nodes"):
        node_text = read_json(path)
        for field in ("title", "abstract"):
            payload_path = node_text.pop(f"{field}_path")
            node_text[field] = (CANONICAL_ROOT / payload_path).read_text(encoding="utf-8") if payload_path else None
        insert_row(connection, "node_text", node_text)

    for path in json_files(CANONICAL_ROOT / "relations" / "references"):
        for reference in read_json(path):
            insert_row(connection, "object_reference", reference)
    for path in json_files(CANONICAL_ROOT / "relations" / "annotations"):
        for annotation in read_json(path):
            insert_row(connection, "text_annotation", annotation)
    for path in json_files(CANONICAL_ROOT / "review"):
        for state in read_json(path):
            insert_row(connection, "review_state", state)
    for path in json_files(CANONICAL_ROOT / "metadata" / "artifacts"):
        artifact = read_json(path)
        payload = (CANONICAL_ROOT / artifact.pop("payload_path")).read_bytes()
        artifact["payload"] = payload
        insert_row(connection, "source_artifact", artifact)

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
            "content_object", "object_identifier", "text_slot", "localized_text", "object_metadata", "review_state",
            "curriculum_node", "node_identifier", "node_text", "node_metadata", "content_placement",
            "object_reference", "text_annotation", "source_artifact",
        ]
    }
    builder.close()
    return counts


def main() -> None:
    print(json.dumps(build_database(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
