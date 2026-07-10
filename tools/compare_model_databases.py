from __future__ import annotations

import json
import sqlite3
from hashlib import sha256
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DB = REPO_ROOT / "work" / "global_model" / "content_model.sqlite"
CANONICAL_DB = REPO_ROOT / "work" / "canonical_model" / "content_model.sqlite"
REPORT_PATH = REPO_ROOT / "work" / "canonical_model" / "comparison.json"
TABLES = (
    "content_object", "object_identifier", "text_slot", "localized_text", "object_metadata", "review_state",
    "curriculum_node", "node_identifier", "node_text", "node_metadata", "content_placement",
    "object_reference", "text_annotation", "source_artifact",
)


def normalize(value: Any) -> Any:
    if isinstance(value, bytes):
        return {"blob_sha256": sha256(value).hexdigest(), "size": len(value)}
    return value


def table_rows(connection: sqlite3.Connection, table: str) -> list[dict[str, Any]]:
    connection.row_factory = sqlite3.Row
    return [{key: normalize(value) for key, value in dict(row).items()} for row in connection.execute(f"SELECT * FROM {table} ORDER BY id")]


def compare() -> dict[str, Any]:
    source = sqlite3.connect(SOURCE_DB)
    canonical = sqlite3.connect(CANONICAL_DB)
    result: dict[str, Any] = {"source": str(SOURCE_DB), "canonical": str(CANONICAL_DB), "tables": {}}
    for table in TABLES:
        left = table_rows(source, table)
        right = table_rows(canonical, table)
        left_by_id = {row["id"]: row for row in left}
        right_by_id = {row["id"]: row for row in right}
        changed = sorted(identifier for identifier in left_by_id.keys() & right_by_id.keys() if left_by_id[identifier] != right_by_id[identifier])
        result["tables"][table] = {
            "source_count": len(left),
            "canonical_count": len(right),
            "only_in_source": sorted(left_by_id.keys() - right_by_id.keys()),
            "only_in_canonical": sorted(right_by_id.keys() - left_by_id.keys()),
            "changed": changed,
        }
    source.close()
    canonical.close()
    result["identical"] = all(
        not values["only_in_source"] and not values["only_in_canonical"] and not values["changed"]
        for values in result["tables"].values()
    )
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return result


def main() -> None:
    result = compare()
    print(json.dumps({"identical": result["identical"], "tables": {name: {key: len(value) if isinstance(value, list) else value for key, value in info.items()} for name, info in result["tables"].items()}}, indent=2))


if __name__ == "__main__":
    main()
