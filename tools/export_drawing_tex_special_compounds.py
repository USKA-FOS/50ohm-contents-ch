#!/usr/bin/env python3
"""Export drawing-text split compounds that must be reviewed as multi-line words."""

from __future__ import annotations

import argparse
import csv
from collections import OrderedDict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CANDIDATES = (
    REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_translation_candidates_2.csv"
)
DEFAULT_REVIEW = (
    REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_translation_review_consolidated.csv"
)
DEFAULT_OUTPUT = (
    REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_special_compounds_review.csv"
)


def load_review_rows(path: Path) -> dict[str, dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return {row["source_term_candidate"]: row for row in rows}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates-csv", type=Path, default=DEFAULT_CANDIDATES)
    parser.add_argument("--review-csv", type=Path, default=DEFAULT_REVIEW)
    parser.add_argument("--output-csv", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    review_by_term = load_review_rows(args.review_csv)

    with args.candidates_csv.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    by_figure: OrderedDict[str, list[dict[str, str]]] = OrderedDict()
    for row in rows:
        by_figure.setdefault(row["figure_number"], []).append(row)

    grouped: OrderedDict[tuple[str, str, str], dict[str, object]] = OrderedDict()
    for figure_number, items in by_figure.items():
        items_sorted = sorted(items, key=lambda item: int(item["index"]))
        for idx, row in enumerate(items_sorted):
            if not row["translatable_text"].endswith("-"):
                continue
            if row["to_be_translated"].lower() != "true":
                continue

            partner = None
            if idx + 1 < len(items_sorted) and items_sorted[idx + 1]["to_be_translated"].lower() == "true":
                partner = items_sorted[idx + 1]
            elif idx > 0 and items_sorted[idx - 1]["to_be_translated"].lower() == "true":
                partner = items_sorted[idx - 1]
            if partner is None:
                continue

            key = (
                row["translatable_text"],
                partner["translatable_text"],
                row["translatable_text"][:-1] + partner["translatable_text"],
            )
            entry = grouped.setdefault(
                key,
                {
                    "part_1_de": row["translatable_text"],
                    "part_2_de": partner["translatable_text"],
                    "combined_de": row["translatable_text"][:-1] + partner["translatable_text"],
                    "figure_numbers": [],
                    "canonical_references": [],
                    "raw_tex_part_1": [],
                    "raw_tex_part_2": [],
                    "fr_partial_current": review_by_term.get(row["translatable_text"], {}).get("fr_reviewed", ""),
                    "it_partial_current": review_by_term.get(row["translatable_text"], {}).get("it_reviewed", ""),
                },
            )
            entry["figure_numbers"].append(figure_number)
            entry["canonical_references"].append(row["canonical_reference"])
            entry["raw_tex_part_1"].append(row["raw_tex_fragment"])
            entry["raw_tex_part_2"].append(partner["raw_tex_fragment"])

    output_rows: list[dict[str, str]] = []
    for value in grouped.values():
        output_rows.append(
            {
                "combined_de": str(value["combined_de"]),
                "part_1_de": str(value["part_1_de"]),
                "part_2_de": str(value["part_2_de"]),
                "figure_numbers": " | ".join(sorted(set(value["figure_numbers"]))),
                "canonical_references": " | ".join(sorted(set(value["canonical_references"]))),
                "raw_tex_part_1": " | ".join(dict.fromkeys(value["raw_tex_part_1"])),
                "raw_tex_part_2": " | ".join(dict.fromkeys(value["raw_tex_part_2"])),
                "fr_partial_current": str(value["fr_partial_current"]),
                "it_partial_current": str(value["it_partial_current"]),
                "fr_combined_reviewed": "",
                "it_combined_reviewed": "",
                "fr_line_1": "",
                "fr_line_2": "",
                "it_line_1": "",
                "it_line_2": "",
                "status": "",
                "reviewer": "",
                "comment": "",
            }
        )

    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output_rows[0].keys()) if output_rows else [])
        writer.writeheader()
        writer.writerows(output_rows)
    print(f"row_count={len(output_rows)}")
    print(f"output={args.output_csv}")


if __name__ == "__main__":
    main()
