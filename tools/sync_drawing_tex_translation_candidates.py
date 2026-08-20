#!/usr/bin/env python3
"""Synchronize the filtered drawing translation candidate CSV with the current extractor output."""

from __future__ import annotations

import argparse
import csv
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CURRENT = REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_translation_candidates_2.csv"
DEFAULT_OUTPUT = DEFAULT_CURRENT
FORCE_FALSE_TERMS = {
    "4,7 nF",
    "47 nF",
    "DARCblue",
    "DARCorange",
    "DARCred",
    "De-Mapper",
    "Diode",
    "Germanium",
    "HF-Diode",
    "Mapper",
    "MWS",
    "PA",
    "PTFE 1,8 mm RG178",
    "Radial",
    "Radar",
    "right:a",
    "right:b",
    "Squelch",
    "SWR-Meter",
    "Transistor",
    "white",
}
FORCE_TRUE_TERMS = {
    "Kabel",
    "Kanalcodierer",
    "Koaxialkabel",
    "Kurzschluss- und Verpolungsgefahr",
    "Quellencodierer",
    "Sicherung",
    "Strahler",
    "Verbraucher",
}


def load_extractor_module():
    extractor_path = REPO_ROOT / "tools" / "extract_drawing_tex_translation_candidates.py"
    spec = spec_from_file_location("drawing_extractor_sync", extractor_path)
    module = module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_current_rows(path: Path) -> dict[tuple[str, str, str], dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return {
        (row["canonical_reference"], row["raw_tex_fragment"], row["category"]): row
        for row in rows
    }


def infer_flag(row: dict[str, str]) -> str:
    term = row["translatable_text"].strip()
    if term in FORCE_FALSE_TERMS:
        return "false"
    if term in FORCE_TRUE_TERMS:
        return "true"
    if term.endswith(" nF"):
        return "false"
    return "true"


def build_fresh_rows() -> list[dict[str, str]]:
    extractor = load_extractor_module()
    rows = []
    for candidate in extractor.build_candidates():
        rows.append(
            {
                "canonical_reference": candidate.canonical_reference,
                "figure_number": str(candidate.figure_number),
                "index": str(candidate.index),
                "raw_tex_fragment": candidate.raw_tex_fragment,
                "format_commands": candidate.format_commands,
                "protected_tokens": candidate.protected_tokens,
                "translatable_text": candidate.translatable_text,
                "category": candidate.category,
                "to_be_translated": candidate.to_be_translated,
            }
        )
    return rows


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    fieldnames = [
        "canonical_reference",
        "figure_number",
        "index",
        "raw_tex_fragment",
        "format_commands",
        "protected_tokens",
        "translatable_text",
        "category",
        "to_be_translated",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--current-csv", type=Path, default=DEFAULT_CURRENT)
    parser.add_argument("--output-csv", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    current_rows = load_current_rows(args.current_csv)
    fresh_rows = build_fresh_rows()
    merged_rows: list[dict[str, str]] = []
    preserved = 0
    inferred = 0

    for row in fresh_rows:
        key = (row["canonical_reference"], row["raw_tex_fragment"], row["category"])
        existing = current_rows.get(key)
        forced_flag = infer_flag(row)
        if row["translatable_text"].strip() in FORCE_FALSE_TERMS | FORCE_TRUE_TERMS or row["translatable_text"].strip().endswith(" nF"):
            row["to_be_translated"] = forced_flag
            inferred += 1
        elif existing is not None:
            row["to_be_translated"] = existing["to_be_translated"]
            preserved += 1
        else:
            row["to_be_translated"] = forced_flag
            inferred += 1
        merged_rows.append(row)

    write_rows(args.output_csv, merged_rows)
    print(f"rows={len(merged_rows)}")
    print(f"preserved={preserved}")
    print(f"inferred={inferred}")
    print(f"output={args.output_csv}")


if __name__ == "__main__":
    main()
