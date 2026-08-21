#!/usr/bin/env python3
"""Validate localized drawing TeX files against the canonical import contract.

The validator does not re-parse localized files heuristically anymore.
Instead, it rebuilds the expected `.fr.tex` and `.it.tex` content from the
German source `.de.tex` using the same translation-import logic as
`import_drawing_tex_translations.py`, then compares the expected text with the
actual localized files on disk.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CANDIDATES = REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_translation_candidates_2.csv"
DEFAULT_IMPORTED = REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_translation_imported_ok.csv"
DEFAULT_SPECIAL = REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_special_compounds_review.csv"
DEFAULT_REPORT = REPO_ROOT / "work" / "drawing_text_audit" / "localized_tex_structure_validation.json"


def normalize_trailing_newline(text: str) -> str:
    return text.rstrip("\n")


def load_import_module():
    module_path = REPO_ROOT / "tools" / "import_drawing_tex_translations.py"
    spec = spec_from_file_location("drawing_import_validator", module_path)
    module = module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_candidates(path: Path) -> dict[str, list[dict[str, str]]]:
    by_ref: dict[str, list[dict[str, str]]] = {}
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            by_ref.setdefault(row["canonical_reference"], []).append(row)
    return by_ref


def render_expected_localized(
    importer,
    ref: str,
    rows: list[dict[str, str]],
    normal_map: dict[tuple[str, str], dict[str, str]],
    special_map: dict[tuple[str, str], dict[str, dict[str, str]]],
) -> tuple[str, dict[str, str], list[dict[str, str]], bool]:
    object_dir = REPO_ROOT / ref
    de_tex_paths = sorted(object_dir.glob("*.de.tex"))
    if not de_tex_paths:
        raise FileNotFoundError(f"No .de.tex source found in {object_dir}")
    de_tex_path = de_tex_paths[0]
    de_text = de_tex_path.read_text(encoding="utf-8")
    rendered = {"fr": de_text, "it": de_text}
    diagnostics: list[dict[str, str]] = []
    touched = False

    for row in sorted(rows, key=lambda item: int(item["index"])):
        if row["to_be_translated"].strip().lower() != "true":
            continue

        term = importer.normalize_lookup_term(row["translatable_text"])
        raw_fragment = row["raw_tex_fragment"]

        if (ref, term) in special_map:
            line_map = special_map[(ref, term)]
            is_part_1 = term.endswith("-")
            for language in ("fr", "it"):
                translated = line_map[language]["part_1" if is_part_1 else "part_2"].strip()
                if not translated:
                    diagnostics.append(
                        {
                            "type": "missing_special_translation",
                            "ref": ref,
                            "figure": row["figure_number"],
                            "lang": language,
                            "index": row["index"],
                            "term": term,
                        }
                    )
                    continue
                replacement = importer.replace_fragment_text(raw_fragment, [translated])
                if raw_fragment in rendered[language]:
                    rendered[language] = rendered[language].replace(raw_fragment, replacement, 1)
                    touched = True
                else:
                    diagnostics.append(
                        {
                            "type": "missing_source_fragment",
                            "ref": ref,
                            "figure": row["figure_number"],
                            "lang": language,
                            "index": row["index"],
                            "term": term,
                        }
                    )
            continue

        payload = normal_map.get((ref, term))
        if not payload:
            diagnostics.append(
                {
                    "type": "missing_translation_mapping",
                    "ref": ref,
                    "figure": row["figure_number"],
                    "index": row["index"],
                    "term": term,
                }
            )
            continue

        for language in ("fr", "it"):
            translated = payload[language].strip()
            if not translated:
                diagnostics.append(
                    {
                        "type": "empty_translation",
                        "ref": ref,
                        "figure": row["figure_number"],
                        "lang": language,
                        "index": row["index"],
                        "term": term,
                    }
                )
                continue
            if row["category"] == "tikz_option_label":
                updated, replaced = importer.replace_tikz_option_label(rendered[language], term, translated)
                if replaced:
                    rendered[language] = updated
                    touched = True
                else:
                    diagnostics.append(
                        {
                            "type": "missing_option_label_source",
                            "ref": ref,
                            "figure": row["figure_number"],
                            "lang": language,
                            "index": row["index"],
                            "term": term,
                        }
                    )
                continue
            if row["category"].startswith("pgfplots_"):
                option_name = row["category"].removeprefix("pgfplots_")
                replacement = importer.replace_fragment_text(raw_fragment, [translated])
                updated, replaced = importer.replace_braced_option(
                    rendered[language], option_name, raw_fragment, replacement
                )
                if replaced:
                    rendered[language] = updated
                    touched = True
                continue
            if row["category"] == "circuitikz_bare_label":
                updated, replaced = importer.replace_circuitikz_bare_label(
                    rendered[language], term, translated
                )
                if replaced:
                    rendered[language] = updated
                    touched = True
                continue
            if row["category"] == "math_text":
                updated, replaced = importer.replace_math_text(rendered[language], term, translated)
                if replaced:
                    rendered[language] = updated
                    touched = True
                continue
            segments = importer.translation_segments_for_regular(raw_fragment, translated)
            protected_tokens = json.loads(row["protected_tokens"])
            protected_by_segment = importer.split_protected_tokens_by_segment(raw_fragment, protected_tokens)
            replacement = importer.replace_fragment_text(
                raw_fragment,
                segments,
                protected_tokens_by_segment=protected_by_segment,
            )
            if raw_fragment in rendered[language]:
                rendered[language] = rendered[language].replace(raw_fragment, replacement, 1)
                touched = True
            else:
                diagnostics.append(
                    {
                        "type": "missing_regular_source_fragment",
                        "ref": ref,
                        "figure": row["figure_number"],
                        "lang": language,
                        "index": row["index"],
                        "term": term,
                    }
                )

    return de_tex_path.name[:-7], rendered, diagnostics, touched


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates-csv", type=Path, default=DEFAULT_CANDIDATES)
    parser.add_argument("--imported-csv", type=Path, default=DEFAULT_IMPORTED)
    parser.add_argument("--special-csv", type=Path, default=DEFAULT_SPECIAL)
    parser.add_argument("--report-json", type=Path, default=DEFAULT_REPORT)
    parser.add_argument(
        "--canonical-ref",
        action="append",
        help="Limit validation to a canonical drawing reference; may be repeated.",
    )
    args = parser.parse_args()

    importer = load_import_module()
    by_ref = load_candidates(args.candidates_csv)
    if args.canonical_ref:
        selected_refs = set(args.canonical_ref)
        by_ref = {ref: rows for ref, rows in by_ref.items() if ref in selected_refs}
    normal_map = importer.build_normal_translation_map(importer.load_csv(args.imported_csv))
    special_map = importer.build_special_translation_map(importer.load_csv(args.special_csv))

    issues: list[dict[str, object]] = []
    validated_files = 0

    for ref, rows in sorted(by_ref.items()):
        try:
            figure, expected, diagnostics, touched = render_expected_localized(
                importer=importer,
                ref=ref,
                rows=rows,
                normal_map=normal_map,
                special_map=special_map,
            )
        except FileNotFoundError as exc:
            issues.append({"type": "missing_de_source", "ref": ref, "message": str(exc)})
            continue

        issues.extend(diagnostics)
        if not touched:
            continue
        object_dir = REPO_ROOT / ref
        for language in ("fr", "it"):
            target_path = object_dir / f"{figure}.{language}.tex"
            if not target_path.exists():
                issues.append({"type": "missing_file", "ref": ref, "figure": figure, "lang": language})
                continue
            actual = target_path.read_text(encoding="utf-8")
            if normalize_trailing_newline(actual) != normalize_trailing_newline(expected[language]):
                issues.append(
                    {
                        "type": "content_mismatch",
                        "ref": ref,
                        "figure": figure,
                        "lang": language,
                    }
                )
            validated_files += 1

    report = {
        "issue_count": len(issues),
        "validated_files": validated_files,
        "issues": issues,
    }
    args.report_json.parent.mkdir(parents=True, exist_ok=True)
    args.report_json.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"issue_count={len(issues)}")
    print(f"validated_files={validated_files}")
    print(f"report={args.report_json}")
    for issue in issues[:200]:
        print(json.dumps(issue, ensure_ascii=False))


if __name__ == "__main__":
    main()
