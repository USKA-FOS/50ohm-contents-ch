#!/usr/bin/env python3
"""Export drawing TeX manual residual rows as generic translation input JSON."""

from __future__ import annotations

import json
import argparse
import csv
import hashlib
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANUAL = (
    REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_translation_manual_residual.csv"
)
DEFAULT_OUTPUT = (
    REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_translation_input.json"
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


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-csv", type=Path, default=DEFAULT_MANUAL)
    parser.add_argument("--output-json", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    with args.input_csv.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    items: list[dict[str, object]] = []
    for row in rows:
        item_id = build_item_id(row)
        items.append(
            {
                "id": item_id,
                "source_text": row["source_term_candidate"],
                "origin": {
                    "workflow": "drawing_tex_manual_residual",
                    "classification": row.get("classification", ""),
                    "occurrence_count": row.get("occurrence_count", ""),
                    "figure_numbers": row.get("figure_numbers", ""),
                    "canonical_references": row.get("canonical_references", ""),
                    "format_command_examples": row.get("format_command_examples", ""),
                    "protected_token_examples": row.get("protected_token_examples", ""),
                    "raw_tex_examples": row.get("raw_tex_examples", ""),
                    "suggested_handling": row.get("suggested_handling", ""),
                    "notes": row.get("notes", ""),
                },
            }
        )

    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps({"items": items}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"row_count={len(rows)}")
    print(f"output={args.output_json}")


if __name__ == "__main__":
    main()
