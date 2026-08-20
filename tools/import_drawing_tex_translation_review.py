#!/usr/bin/env python3
"""Import accepted drawing translation review rows, excluding special compounds."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REVIEW = (
    REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_translation_review_consolidated.csv"
)
DEFAULT_SPECIAL = (
    REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_special_compounds_review.csv"
)
DEFAULT_OUTPUT_CSV = (
    REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_translation_imported_ok.csv"
)
DEFAULT_OUTPUT_JSON = (
    REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_translation_imported_ok.json"
)


def load_special_terms(path: Path) -> set[str]:
    if not path.exists():
        return set()
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    special_terms: set[str] = set()
    for row in rows:
        special_terms.add(row.get("part_1_de", "").strip())
        special_terms.add(row.get("part_2_de", "").strip())
    return {term for term in special_terms if term}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--review-csv", type=Path, default=DEFAULT_REVIEW)
    parser.add_argument("--special-csv", type=Path, default=DEFAULT_SPECIAL)
    parser.add_argument("--output-csv", type=Path, default=DEFAULT_OUTPUT_CSV)
    parser.add_argument("--output-json", type=Path, default=DEFAULT_OUTPUT_JSON)
    args = parser.parse_args()

    special_terms = load_special_terms(args.special_csv)
    with args.review_csv.open(encoding="utf-8", newline="") as handle:
        review_rows = list(csv.DictReader(handle))

    accepted_rows: list[dict[str, str]] = []
    skipped_special = 0
    skipped_non_ok = 0
    skipped_missing_translation = 0
    for row in review_rows:
        term = row.get("source_term_candidate", "").strip()
        status = row.get("status", "").strip().lower()
        fr = row.get("fr_reviewed", "").strip()
        it = row.get("it_reviewed", "").strip()
        if term in special_terms:
            skipped_special += 1
            continue
        if status != "ok":
            skipped_non_ok += 1
            continue
        if not fr or not it:
            skipped_missing_translation += 1
            continue
        accepted_rows.append(
            {
                "item_id": row.get("item_id", ""),
                "source_term_candidate": term,
                "classification": row.get("classification", ""),
                "occurrence_count": row.get("occurrence_count", ""),
                "figure_numbers": row.get("figure_numbers", ""),
                "canonical_references": row.get("canonical_references", ""),
                "format_command_examples": row.get("format_command_examples", ""),
                "protected_token_examples": row.get("protected_token_examples", ""),
                "raw_tex_examples": row.get("raw_tex_examples", ""),
                "fr_reviewed": fr,
                "it_reviewed": it,
                "reviewer": row.get("reviewer", ""),
                "comment": row.get("comment", ""),
            }
        )

    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(accepted_rows[0].keys()) if accepted_rows else [])
        writer.writeheader()
        writer.writerows(accepted_rows)

    args.output_json.write_text(
        json.dumps(
            {
                "items": accepted_rows,
                "summary": {
                    "accepted_count": len(accepted_rows),
                    "skipped_special": skipped_special,
                    "skipped_non_ok": skipped_non_ok,
                    "skipped_missing_translation": skipped_missing_translation,
                },
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"accepted_count={len(accepted_rows)}")
    print(f"skipped_special={skipped_special}")
    print(f"skipped_non_ok={skipped_non_ok}")
    print(f"skipped_missing_translation={skipped_missing_translation}")
    print(f"output_csv={args.output_csv}")
    print(f"output_json={args.output_json}")


if __name__ == "__main__":
    main()
