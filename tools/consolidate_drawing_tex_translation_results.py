#!/usr/bin/env python3
"""Consolidate external drawing-text translations into a manual review CSV."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANUAL = (
    REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_translation_manual_residual.csv"
)
DEFAULT_OUTPUT = (
    REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_translation_review_consolidated.csv"
)


def build_item_id(row: dict[str, str]) -> str:
    material = "||".join(
        [
            row.get("source_term_candidate", ""),
            row.get("canonical_references", ""),
            row.get("figure_numbers", ""),
        ]
    )
    return f"dtx_{hashlib.sha1(material.encode('utf-8')).hexdigest()[:12]}"


def load_translated_units(path: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    if not path.exists():
        return result
    for item_path in sorted(path.glob("*.json")):
        payload = json.loads(item_path.read_text(encoding="utf-8"))
        item_id = str(payload.get("id", "")).strip()
        fields = payload.get("fields") or {}
        if item_id:
            result[item_id] = str(fields.get("text", "") or "")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-csv", type=Path, default=DEFAULT_MANUAL)
    parser.add_argument("--fr-dir", type=Path, required=True)
    parser.add_argument("--it-dir", type=Path, required=True)
    parser.add_argument("--output-csv", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    with args.input_csv.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    fr = load_translated_units(args.fr_dir)
    it = load_translated_units(args.it_dir)

    consolidated: list[dict[str, str]] = []
    for row in rows:
        item_id = build_item_id(row)
        consolidated.append(
            {
                "item_id": item_id,
                "source_term_candidate": row.get("source_term_candidate", ""),
                "classification": row.get("classification", ""),
                "occurrence_count": row.get("occurrence_count", ""),
                "figure_numbers": row.get("figure_numbers", ""),
                "canonical_references": row.get("canonical_references", ""),
                "format_command_examples": row.get("format_command_examples", ""),
                "protected_token_examples": row.get("protected_token_examples", ""),
                "raw_tex_examples": row.get("raw_tex_examples", ""),
                "fr_ai": fr.get(item_id, ""),
                "it_ai": it.get(item_id, ""),
                "fr_reviewed": "",
                "it_reviewed": "",
                "status": "",
                "reviewer": "",
                "comment": "",
            }
        )

    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(consolidated[0].keys()) if consolidated else [])
        writer.writeheader()
        writer.writerows(consolidated)
    print(f"row_count={len(consolidated)}")
    print(f"fr_found={sum(1 for row in consolidated if row['fr_ai'])}")
    print(f"it_found={sum(1 for row in consolidated if row['it_ai'])}")
    print(f"output={args.output_csv}")


if __name__ == "__main__":
    main()
