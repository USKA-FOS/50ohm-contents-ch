"""Merge applied German source-import audits into one translation scope."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def load_audit(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("workflow") != "incremental_german_source_import":
        raise ValueError(f"Not a German source import audit: {path}")
    if payload.get("applied") is not True:
        raise ValueError(f"Source import audit was not applied: {path}")
    return payload


def merge(paths: list[Path]) -> dict:
    audits = [load_audit(path) for path in paths]
    revisions = {str(audit.get("source_revision")) for audit in audits}
    if len(revisions) != 1:
        raise ValueError(f"Audits do not share one source revision: {sorted(revisions)}")

    object_ids = sorted({str(value) for audit in audits for value in audit.get("translation_object_ids", [])})
    node_ids = sorted({str(value) for audit in audits for value in audit.get("translation_node_ids", [])})
    changes_by_key: dict[tuple[str, str], dict] = {}
    for audit in audits:
        for change in audit.get("changes", []):
            if change.get("action") == "unchanged":
                continue
            key = (str(change.get("object_type")), str(change.get("source_key")))
            changes_by_key[key] = change

    return {
        "schema_version": 1,
        "workflow": "incremental_german_source_import",
        "scope_type": "translation_scope",
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source_revision": next(iter(revisions)),
        "source_audits": [str(path) for path in paths],
        "applied": True,
        "translation_object_ids": object_ids,
        "translation_node_ids": node_ids,
        "changes": sorted(changes_by_key.values(), key=lambda item: (str(item.get("object_type")), str(item.get("source_key")))),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Merge applied German import audits into one translation scope.")
    parser.add_argument("audits", nargs="+", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    payload = merge([path.resolve() for path in args.audits])
    args.output.resolve().parent.mkdir(parents=True, exist_ok=True)
    args.output.resolve().write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    print(f"output={args.output.resolve()}")
    print(f"source_revision={payload['source_revision']}")
    print(f"translation_objects={len(payload['translation_object_ids'])}")
    print(f"translation_nodes={len(payload['translation_node_ids'])}")
    print(f"changes={len(payload['changes'])}")


if __name__ == "__main__":
    main()
