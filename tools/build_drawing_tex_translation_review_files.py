#!/usr/bin/env python3
"""Build drawing TeX translation review CSVs from the filtered candidate list."""

from __future__ import annotations

import argparse
import csv
import re
from collections import OrderedDict
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FILTER = (
    REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_translation_candidates_2.csv"
)
DEFAULT_WORKING = (
    REPO_ROOT
    / "work"
    / "drawing_text_audit"
    / "drawing_tex_translation_unique_working_with_suggestions.csv"
)
DEFAULT_SIMPLE = (
    REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_translation_simple_actions.csv"
)
DEFAULT_GLOSSARY_PROPOSALS = (
    REPO_ROOT
    / "work"
    / "drawing_text_audit"
    / "drawing_tex_glossary_proposals_from_filter.csv"
)
DEFAULT_MANUAL = (
    REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_translation_manual_residual.csv"
)
DEFAULT_UNIQUE = (
    REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_translation_unique_from_filter.csv"
)
DEFAULT_GLOSSARY = REPO_ROOT.parent / "50ohm-ai-translation-glossary" / "glossary.yml"
FORCE_FALSE_TERMS = {"Si Substrate (Bulk)", "NPN", "PNP", "MHz"}


def load_glossary(glossary_path: Path) -> dict[str, dict[str, str]]:
    data = yaml.safe_load(glossary_path.read_text(encoding="utf-8")) or {}
    terms = data.get("terms", []) if isinstance(data, dict) else []
    glossary: dict[str, dict[str, str]] = {}
    for entry in terms:
        if not isinstance(entry, dict):
            continue
        source_term = str(entry.get("source_term", "")).strip()
        if not source_term:
            continue
        translations = entry.get("translations", {}) or {}
        glossary[source_term] = {
            "fr": str((translations.get("fr", {}) or {}).get("term", "")).strip(),
            "it": str((translations.get("it", {}) or {}).get("term", "")).strip(),
        }
    return glossary


def load_selected_rows(filter_csv: Path) -> OrderedDict[str, list[dict[str, str]]]:
    with filter_csv.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    grouped: OrderedDict[str, list[dict[str, str]]] = OrderedDict()
    for row in rows:
        if row.get("to_be_translated", "").lower() != "true":
            continue
        normalized = normalize_translatable_text(row["translatable_text"])
        if not normalized:
            continue
        row = dict(row)
        row["translatable_text"] = normalized
        grouped.setdefault(normalized, []).append(row)
    return grouped


def normalize_translatable_text(text: str) -> str:
    normalized = re.sub(r"^[~\s]+", "", text)
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return normalized


def classify(text: str, category: str, glossary: dict[str, dict[str, str]]) -> tuple[str, str, str, str, str]:
    if text in FORCE_FALSE_TERMS:
        return "", "", "should_be_false_in_filter", "no", "English technical expression; exclude from translation scope."

    glossary_match = glossary.get(text)
    if glossary_match:
        return (
            glossary_match["fr"],
            glossary_match["it"],
            "from_glossary",
            "already_present",
            "",
        )

    if text == "NF":
        return (
            "BF",
            "BF",
            "simple_direct_fill_and_add_to_glossary",
            "yes",
            "German Niederfrequenz translated consistently to BF in fr/it.",
        )

    match = re.fullmatch(r"(\d+)\. OW", text)
    if match:
        harmonic = int(match.group(1)) + 1
        return (
            f"H{harmonic}",
            f"H{harmonic}",
            "simple_direct_fill_and_add_to_glossary",
            "yes",
            "Oberwelle shorthand normalized to harmonic label.",
        )

    match = re.fullmatch(r"(\d+)\. OW\s+(\d+)\s+Harm\.", text)
    if match:
        harmonic = int(match.group(2))
        return (
            f"H{harmonic}",
            f"H{harmonic}",
            "simple_direct_fill_and_add_to_glossary",
            "yes",
            "Oberwelle/Harmonie shorthand normalized to harmonic label.",
        )

    match = re.fullmatch(r"(\d+)\. Filter", text)
    if match:
        index = match.group(1)
        return f"{index}. filtre", f"{index}. filtro", "simple_direct_fill", "optional", ""

    match = re.fullmatch(r"(\d+)\. Mischer", text)
    if match:
        index = match.group(1)
        return f"{index}. mélangeur", f"{index}. mixer", "simple_direct_fill", "optional", ""

    match = re.fullmatch(r"(\d+)\. Ziffer", text)
    if match:
        index = match.group(1)
        return f"{index}. chiffre", f"{index}. cifra", "simple_direct_fill", "optional", ""

    if category == "fragment_or_split_label":
        return "", "", "manual_fragment_rejoin", "no", ""

    return "", "", "manual_review", "consider", ""


def summarize_json_like_values(group: list[dict[str, str]], key: str) -> str:
    values: list[str] = []
    seen: set[str] = set()
    for row in group:
        value = row.get(key, "")
        if value and value not in seen:
            values.append(value)
            seen.add(value)
    return " | ".join(values[:5])


def summarize_group(group: list[dict[str, str]]) -> tuple[str, str, str, str, str]:
    figure_numbers = " | ".join(sorted({row["figure_number"] for row in group if row["figure_number"]}))
    references = " | ".join(
        sorted({row["canonical_reference"] for row in group if row["canonical_reference"]})
    )
    raw_examples: list[str] = []
    seen: set[str] = set()
    for row in group:
        raw = row["raw_tex_fragment"]
        if raw not in seen:
            raw_examples.append(raw)
            seen.add(raw)
    return (
        figure_numbers,
        references,
        " | ".join(raw_examples[:5]),
        summarize_json_like_values(group, "format_commands"),
        summarize_json_like_values(group, "protected_tokens"),
    )


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--filter-csv", type=Path, default=DEFAULT_FILTER)
    parser.add_argument("--glossary", type=Path, default=DEFAULT_GLOSSARY)
    parser.add_argument("--unique-output", type=Path, default=DEFAULT_UNIQUE)
    parser.add_argument("--working-output", type=Path, default=DEFAULT_WORKING)
    parser.add_argument("--simple-output", type=Path, default=DEFAULT_SIMPLE)
    parser.add_argument("--glossary-output", type=Path, default=DEFAULT_GLOSSARY_PROPOSALS)
    parser.add_argument("--manual-output", type=Path, default=DEFAULT_MANUAL)
    args = parser.parse_args()

    glossary = load_glossary(args.glossary)
    grouped = load_selected_rows(args.filter_csv)

    unique_rows: list[dict[str, str]] = []
    working_rows: list[dict[str, str]] = []

    for text, group in grouped.items():
        (
            figure_numbers,
            references,
            raw_examples,
            format_command_examples,
            protected_token_examples,
        ) = summarize_group(group)
        glossary_match = glossary.get(text)
        unique_rows.append(
            {
                "source_term_candidate": text,
                "classification": group[0]["category"],
                "occurrence_count": str(len(group)),
                "figure_numbers": figure_numbers,
                "canonical_references": references,
                "format_command_examples": format_command_examples,
                "protected_token_examples": protected_token_examples,
                "raw_tex_examples": raw_examples,
                "already_in_glossary": "true" if glossary_match else "false",
                "glossary_fr": glossary_match["fr"] if glossary_match else "",
                "glossary_it": glossary_match["it"] if glossary_match else "",
            }
        )

        fr, it, handling, glossary_addition, notes = classify(text, group[0]["category"], glossary)
        working_rows.append(
            {
                "source_term_candidate": text,
                "classification": group[0]["category"],
                "occurrence_count": str(len(group)),
                "figure_numbers": figure_numbers,
                "canonical_references": references,
                "format_command_examples": format_command_examples,
                "protected_token_examples": protected_token_examples,
                "raw_tex_examples": raw_examples,
                "already_in_glossary": "true" if glossary_match else "false",
                "glossary_source_term": text if glossary_match else "",
                "glossary_fr": glossary_match["fr"] if glossary_match else "",
                "glossary_it": glossary_match["it"] if glossary_match else "",
                "fr": fr,
                "it": it,
                "suggested_handling": handling,
                "suggested_glossary_addition": glossary_addition,
                "notes": notes,
            }
        )

    simple_rows = [
        {
            "source_term_candidate": row["source_term_candidate"],
            "classification": row["classification"],
            "occurrence_count": row["occurrence_count"],
            "figure_numbers": row["figure_numbers"],
            "canonical_references": row["canonical_references"],
            "format_command_examples": row["format_command_examples"],
            "protected_token_examples": row["protected_token_examples"],
            "already_in_glossary": row["already_in_glossary"],
            "fr": row["fr"] or row["glossary_fr"],
            "it": row["it"] or row["glossary_it"],
            "suggested_handling": row["suggested_handling"],
            "suggested_glossary_addition": row["suggested_glossary_addition"],
            "notes": row["notes"],
        }
        for row in working_rows
        if row["suggested_handling"]
        in {"from_glossary", "simple_direct_fill_and_add_to_glossary", "simple_direct_fill"}
    ]

    glossary_rows = [
        {
            "de": row["source_term_candidate"],
            "fr": row["fr"] or row["glossary_fr"],
            "it": row["it"] or row["glossary_it"],
            "classification": row["classification"],
            "occurrence_count": row["occurrence_count"],
            "figure_numbers": row["figure_numbers"],
            "canonical_references": row["canonical_references"],
            "format_command_examples": row["format_command_examples"],
            "protected_token_examples": row["protected_token_examples"],
            "rationale": "drawing tex recurring label",
        }
        for row in working_rows
        if row["suggested_glossary_addition"] == "yes"
    ]

    manual_rows = [
        {
            "source_term_candidate": row["source_term_candidate"],
            "classification": row["classification"],
            "occurrence_count": row["occurrence_count"],
            "figure_numbers": row["figure_numbers"],
            "canonical_references": row["canonical_references"],
            "format_command_examples": row["format_command_examples"],
            "protected_token_examples": row["protected_token_examples"],
            "raw_tex_examples": row["raw_tex_examples"],
            "suggested_handling": row["suggested_handling"],
            "notes": row["notes"],
            "fr": row["fr"],
            "it": row["it"],
        }
        for row in working_rows
        if row["suggested_handling"] in {"manual_review", "manual_fragment_rejoin"}
    ]

    write_csv(
        args.unique_output,
        [
            "source_term_candidate",
            "classification",
            "occurrence_count",
            "figure_numbers",
            "canonical_references",
            "format_command_examples",
            "protected_token_examples",
            "raw_tex_examples",
            "already_in_glossary",
            "glossary_fr",
            "glossary_it",
        ],
        unique_rows,
    )
    write_csv(args.working_output, list(working_rows[0].keys()) if working_rows else [], working_rows)
    write_csv(args.simple_output, list(simple_rows[0].keys()) if simple_rows else [], simple_rows)
    write_csv(
        args.glossary_output,
        list(glossary_rows[0].keys()) if glossary_rows else [],
        glossary_rows,
    )
    write_csv(args.manual_output, list(manual_rows[0].keys()) if manual_rows else [], manual_rows)

    print(f"selected_rows={sum(len(group) for group in grouped.values())}")
    print(f"unique_rows={len(grouped)}")
    print(f"glossary_hits={sum(1 for row in working_rows if row['suggested_handling'] == 'from_glossary')}")
    print(f"simple_rows={len(simple_rows)}")
    print(f"manual_rows={len(manual_rows)}")
    print(f"manual_output={args.manual_output}")


if __name__ == "__main__":
    main()
