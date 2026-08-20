#!/usr/bin/env python3
"""Import reviewed drawing text translations and generate localized TeX files."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CANDIDATES = (
    REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_translation_candidates_2.csv"
)
DEFAULT_IMPORTED = (
    REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_translation_imported_ok.csv"
)
DEFAULT_SPECIAL = (
    REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_special_compounds_review.csv"
)
DEFAULT_REPORT = (
    REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_translation_import_report.json"
)


def normalize_lookup_term(value: str) -> str:
    value = re.sub(r"^[~\s]+", "", value or "")
    value = re.sub(r"\s+", " ", value).strip()
    return value


def normalize_translation_text(value: str) -> str:
    return (value or "").replace("\\\\", "\\").strip()


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def split_refs(value: str) -> list[str]:
    return [item.strip() for item in value.split("|") if item.strip()]


def split_figure_numbers(value: str) -> list[str]:
    return [item.strip() for item in value.split("|") if item.strip()]


def build_normal_translation_map(rows: list[dict[str, str]]) -> dict[tuple[str, str], dict[str, str]]:
    result: dict[tuple[str, str], dict[str, str]] = {}
    for row in rows:
        term = normalize_lookup_term(row["source_term_candidate"])
        payload = {
            "fr": normalize_translation_text(row["fr_reviewed"]),
            "it": normalize_translation_text(row["it_reviewed"]),
        }
        for ref in split_refs(row["canonical_references"]):
            result[(ref, term)] = payload
    return result


def build_special_translation_map(rows: list[dict[str, str]]) -> dict[tuple[str, str], dict[str, dict[str, str]]]:
    result: dict[tuple[str, str], dict[str, dict[str, str]]] = {}
    for row in rows:
        line_map = {
            "fr": {
                "part_1": normalize_translation_text(row["fr_line_1"]),
                "part_2": normalize_translation_text(row["fr_line_2"]),
            },
            "it": {
                "part_1": normalize_translation_text(row["it_line_1"]),
                "part_2": normalize_translation_text(row["it_line_2"]),
            },
        }
        part_1 = normalize_lookup_term(row["part_1_de"])
        part_2 = normalize_lookup_term(row["part_2_de"])
        for ref in split_refs(row["canonical_references"]):
            result[(ref, part_1)] = line_map
            result[(ref, part_2)] = line_map
    return result


def translation_segments_for_regular(raw_fragment: str, translation_text: str) -> list[str]:
    inner = raw_fragment[1:-1] if raw_fragment.startswith("{") and raw_fragment.endswith("}") else raw_fragment
    source_segments = inner.split("\\\\")
    if "\\\\" in translation_text:
        parts = [part.strip() for part in translation_text.split("\\\\")]
        if len(parts) == len(source_segments):
            return parts
    if len(source_segments) == 1:
        return [translation_text.strip()]
    if len(translation_text.strip().split()) <= 1:
        return [translation_text.strip()] + [""] * (len(source_segments) - 1)

    words = translation_text.strip().split()
    if not words:
        return [""] * len(source_segments)
    source_weights = []
    for segment in source_segments:
        tokens = re.findall(r"\S+", re.sub(r"\\[A-Za-z@]+\*?", " ", segment))
        source_weights.append(max(1, len(tokens)))
    total_weight = sum(source_weights)
    assigned: list[list[str]] = [[] for _ in source_segments]
    cursor = 0
    for index, weight in enumerate(source_weights):
        remaining_segments = len(source_segments) - index
        remaining_words = len(words) - cursor
        if remaining_segments == 1:
            take = remaining_words
        else:
            proportional = round(len(words) * weight / total_weight)
            min_take = 1
            max_take = remaining_words - (remaining_segments - 1)
            take = min(max(proportional, min_take), max_take)
        assigned[index] = words[cursor:cursor + take]
        cursor += take
    if cursor < len(words):
        assigned[-1].extend(words[cursor:])
    return [" ".join(part).strip() for part in assigned]


def split_protected_tokens_by_segment(raw_fragment: str, protected_tokens: list[str]) -> list[list[str]]:
    inner = raw_fragment[1:-1] if raw_fragment.startswith("{") and raw_fragment.endswith("}") else raw_fragment
    source_segments = inner.split("\\\\")
    per_segment: list[list[str]] = [[] for _ in source_segments]
    remaining = list(protected_tokens)
    for index, segment in enumerate(source_segments):
        cursor = 0
        while remaining:
            token = remaining[0]
            position = segment.find(token, cursor)
            if position == -1:
                break
            per_segment[index].append(token)
            remaining.pop(0)
            cursor = position + len(token)
    return per_segment


PLACEHOLDER_PATTERN = re.compile(r"§P(\d+)§")


def read_balanced_group(text: str, brace_index: int) -> tuple[str, int]:
    if brace_index >= len(text) or text[brace_index] != "{":
        raise ValueError("brace_index must point to an opening brace")
    depth = 0
    chars: list[str] = []
    i = brace_index
    while i < len(text):
        char = text[i]
        if char == "{":
            depth += 1
            if depth > 1:
                chars.append(char)
        elif char == "}":
            depth -= 1
            if depth == 0:
                return "".join(chars), i + 1
            chars.append(char)
        else:
            chars.append(char)
        i += 1
    raise ValueError("unbalanced braces")


def rebuild_wrapped_segment(source_segment: str, translated: str) -> str | None:
    stripped = source_segment.strip()
    leading_ws_len = len(source_segment) - len(source_segment.lstrip())
    trailing_ws_len = len(source_segment) - len(source_segment.rstrip())
    leading_ws = source_segment[:leading_ws_len]
    trailing_ws = source_segment[len(source_segment) - trailing_ws_len:] if trailing_ws_len else ""
    if not stripped.startswith("\\"):
        return None

    def wrap_result(value: str) -> str:
        return leading_ws + value + trailing_ws

    if stripped.startswith(r"\textcolor"):
        cursor = len(r"\textcolor")
        while cursor < len(stripped) and stripped[cursor].isspace():
            cursor += 1
        if cursor >= len(stripped) or stripped[cursor] != "{":
            return None
        color_arg, cursor = read_balanced_group(stripped, cursor)
        while cursor < len(stripped) and stripped[cursor].isspace():
            cursor += 1
        if cursor >= len(stripped) or stripped[cursor] != "{":
            return None
        inner_arg, cursor = read_balanced_group(stripped, cursor)
        if stripped[cursor:].strip():
            return None
        rebuilt_inner = rebuild_wrapped_segment(inner_arg, translated)
        if rebuilt_inner is None:
            rebuilt_inner = translated
        return wrap_result(rf"\textcolor{{{color_arg}}}{{{rebuilt_inner}}}")

    command_match = re.match(r"\\([A-Za-z@]+\*?)", stripped)
    if not command_match:
        return None
    cursor = command_match.end()
    while cursor < len(stripped) and stripped[cursor].isspace():
        cursor += 1
    if cursor >= len(stripped) or stripped[cursor] != "{":
        return None
    inner_arg, cursor = read_balanced_group(stripped, cursor)
    if stripped[cursor:].strip():
        return None
    rebuilt_inner = rebuild_wrapped_segment(inner_arg, translated)
    if rebuilt_inner is None:
        rebuilt_inner = translated
    return wrap_result(stripped[:command_match.end()] + "{" + rebuilt_inner + "}")


def distribute_translation_over_spans(source_spans: list[str], translated: str) -> list[str]:
    if not source_spans:
        return []
    if len(source_spans) == 1:
        return [translated]

    words = translated.strip().split()
    if not words:
        return [""] * len(source_spans)

    weights = [max(1, len(re.findall(r"\S+", span))) for span in source_spans]
    total_weight = sum(weights)
    assigned: list[list[str]] = [[] for _ in source_spans]
    cursor = 0
    for index, weight in enumerate(weights):
        remaining_spans = len(source_spans) - index
        remaining_words = len(words) - cursor
        if remaining_spans == 1:
            take = remaining_words
        else:
            proportional = round(len(words) * weight / total_weight)
            min_take = 1
            max_take = remaining_words - (remaining_spans - 1)
            take = min(max(proportional, min_take), max_take)
        assigned[index] = words[cursor:cursor + take]
        cursor += take
    if cursor < len(words):
        assigned[-1].extend(words[cursor:])
    return [" ".join(part).strip() for part in assigned]


def dedupe_boundary_punctuation(text: str, next_literal: str) -> str:
    trimmed = text.rstrip()
    if not trimmed or not next_literal:
        return text
    if next_literal[0] in ")]}" and trimmed.endswith(next_literal[0]):
        return trimmed[:-1].rstrip() + (" " if text.endswith(" ") else "")
    return text


def replace_alpha_span_preserving_context(source: str, translated: str) -> str:
    matches = list(re.finditer(r"[A-Za-zÀ-ÖØ-öø-ÿß]+", source))
    if len(matches) != 1:
        return translated
    if re.search(r"[(){}[\],.:;~=+$\\\\]", translated):
        return translated
    match = matches[0]
    if not match:
        return translated
    prefix = source[:match.start()]
    suffix = source[match.end():]
    return prefix + translated + suffix


def replace_fragment_text(
    raw_fragment: str,
    translated_segments: list[str],
    protected_tokens_by_segment: list[list[str]] | None = None,
) -> str:
    inner = raw_fragment[1:-1] if raw_fragment.startswith("{") and raw_fragment.endswith("}") else raw_fragment
    source_segments = inner.split("\\\\")
    if len(source_segments) != len(translated_segments):
        raise ValueError(f"Segment count mismatch for fragment {raw_fragment}")
    rebuilt_segments: list[str] = []
    protected_tokens_by_segment = protected_tokens_by_segment or [[] for _ in source_segments]
    if len(protected_tokens_by_segment) != len(source_segments):
        raise ValueError(f"Protected-token segment mismatch for fragment {raw_fragment}")

    for source_segment, translated, protected_tokens in zip(
        source_segments,
        translated_segments,
        protected_tokens_by_segment,
    ):
        masked = source_segment
        placeholders: list[str] = []
        for index, token in enumerate(protected_tokens):
            placeholder = f"§P{index}§"
            masked = masked.replace(token, placeholder, 1)
            placeholders.append(placeholder)

        parts = re.split(r"(§P\d+§)", masked)
        translatable_indices = [
            index for index, part in enumerate(parts)
            if not PLACEHOLDER_PATTERN.fullmatch(part) and re.search(r"[A-Za-zÀ-ÖØ-öø-ÿ]", part)
        ]
        match = re.match(r"^(\s*(?:\\[A-Za-z@]+\*?\s*)*)", source_segment)
        prefix = match.group(1) if match else ""
        if protected_tokens and translatable_indices:
            if translated and all(token in translated for token in protected_tokens):
                rebuilt = rebuild_wrapped_segment(source_segment, translated)
                rebuilt_segments.append(rebuilt if rebuilt is not None else translated)
                continue
            source_spans = [parts[index] for index in translatable_indices]
            translated_spans = distribute_translation_over_spans(source_spans, translated)
            for index, translated_span in zip(translatable_indices, translated_spans):
                next_literal = ""
                for follower in parts[index + 1:]:
                    if PLACEHOLDER_PATTERN.fullmatch(follower):
                        continue
                    next_literal = follower
                    break
                rebuilt_span = replace_alpha_span_preserving_context(parts[index], translated_span)
                parts[index] = dedupe_boundary_punctuation(rebuilt_span, next_literal)
            rebuilt = "".join(parts)
            for index, token in enumerate(protected_tokens):
                rebuilt = rebuilt.replace(f"§P{index}§", token)
            rebuilt_segments.append(rebuilt)
            continue

        remainder = source_segment[len(prefix):].strip()
        leading_markers = ""
        marker_match = re.match(r"^([~\s]+)", remainder)
        if marker_match:
            leading_markers = marker_match.group(1)
        rebuilt = rebuild_wrapped_segment(source_segment, translated) if translated else None
        if rebuilt is not None:
            rebuilt_segments.append(rebuilt)
        elif prefix and remainder.startswith("{") and remainder.endswith("}"):
            rebuilt_segments.append(prefix + "{" + translated + "}")
        elif prefix and translated:
            rebuilt_segments.append(prefix + leading_markers + translated)
        elif translated:
            rebuilt_segments.append(leading_markers + translated)
        else:
            rebuilt_segments.append(prefix + translated)
    return "{" + "\\\\".join(rebuilt_segments) + "}"


def update_meta_for_tex(object_dir: Path, stem: str) -> None:
    meta_path = object_dir / "object.meta.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    language_variants = meta.setdefault("language_variants", {})
    for language in ("fr", "it"):
        variant = language_variants.setdefault(language, {})
        asset_files = variant.setdefault("asset_files", {})
        asset_files["tex"] = f"{stem}.{language}.tex"
        variant.setdefault("review_state", "to_be_reviewed")
    metadata = meta.setdefault("metadata", {})
    language_asset = metadata.setdefault("language_asset", {})
    for language in ("fr", "it"):
        key = f"{language}.tex"
        language_asset[key] = {
            "canonical_file": f"{stem}.{language}.tex",
        }
    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def replace_tikz_option_label(text: str, source_term: str, translated: str) -> tuple[str, bool]:
    for source, target in (
        (f"label={source_term}", f"label={translated}"),
        (f"label = {source_term}", f"label = {translated}"),
        (f"label={{{source_term}}}", f"label={{{translated}}}"),
        (f"label = {{{source_term}}}", f"label = {{{translated}}}"),
    ):
        if source in text:
            return text.replace(source, target, 1), True
    return text, False


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidates-csv", type=Path, default=DEFAULT_CANDIDATES)
    parser.add_argument("--imported-csv", type=Path, default=DEFAULT_IMPORTED)
    parser.add_argument("--special-csv", type=Path, default=DEFAULT_SPECIAL)
    parser.add_argument("--report-json", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()

    candidates = load_csv(args.candidates_csv)
    normal_map = build_normal_translation_map(load_csv(args.imported_csv))
    special_rows = load_csv(args.special_csv)
    special_map = build_special_translation_map(special_rows)

    by_ref: dict[str, list[dict[str, str]]] = {}
    for row in candidates:
        by_ref.setdefault(row["canonical_reference"], []).append(row)

    report: dict[str, Any] = {"updated_drawings": [], "languages": {"fr": 0, "it": 0}}
    for ref, rows in sorted(by_ref.items()):
        object_dir = REPO_ROOT / ref
        de_tex_paths = sorted(object_dir.glob("*.de.tex"))
        if not de_tex_paths:
            continue
        de_tex_path = de_tex_paths[0]
        stem = de_tex_path.name[:-7]
        original_text = de_tex_path.read_text(encoding="utf-8")
        rendered = {"fr": original_text, "it": original_text}
        touched = False

        for row in sorted(rows, key=lambda item: int(item["index"])):
            if row["to_be_translated"].lower() != "true":
                continue
            term = normalize_lookup_term(row["translatable_text"])
            raw_fragment = row["raw_tex_fragment"]
            if (ref, term) in special_map:
                line_map = special_map[(ref, term)]
                is_part_1 = term.endswith("-")
                for language in ("fr", "it"):
                    translated = line_map[language]["part_1" if is_part_1 else "part_2"].strip()
                    if not translated:
                        continue
                    replacement = replace_fragment_text(raw_fragment, [translated])
                    if raw_fragment in rendered[language]:
                        rendered[language] = rendered[language].replace(raw_fragment, replacement, 1)
                        touched = True
                continue

            payload = normal_map.get((ref, term))
            if not payload:
                continue
            for language in ("fr", "it"):
                translated = payload[language].strip()
                if not translated:
                    continue
                if row["category"] == "tikz_option_label":
                    updated, replaced = replace_tikz_option_label(rendered[language], term, translated)
                    if replaced:
                        rendered[language] = updated
                        touched = True
                    continue
                segments = translation_segments_for_regular(raw_fragment, translated)
                protected_tokens = json.loads(row["protected_tokens"])
                protected_by_segment = split_protected_tokens_by_segment(raw_fragment, protected_tokens)
                replacement = replace_fragment_text(
                    raw_fragment,
                    segments,
                    protected_tokens_by_segment=protected_by_segment,
                )
                if raw_fragment in rendered[language]:
                    rendered[language] = rendered[language].replace(raw_fragment, replacement, 1)
                    touched = True

        if not touched:
            continue

        for language in ("fr", "it"):
            target_path = object_dir / f"{stem}.{language}.tex"
            target_path.write_text(rendered[language], encoding="utf-8")
            report["languages"][language] += 1
        update_meta_for_tex(object_dir, stem)
        report["updated_drawings"].append(
            {
                "canonical_reference": ref,
                "de_tex": str(de_tex_path.relative_to(REPO_ROOT)),
                "fr_tex": str((object_dir / f'{stem}.fr.tex').relative_to(REPO_ROOT)),
                "it_tex": str((object_dir / f'{stem}.it.tex').relative_to(REPO_ROOT)),
            }
        )

    args.report_json.parent.mkdir(parents=True, exist_ok=True)
    args.report_json.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"updated_drawings={len(report['updated_drawings'])}")
    print(f"fr_files={report['languages']['fr']}")
    print(f"it_files={report['languages']['it']}")
    print(f"report={args.report_json}")


if __name__ == "__main__":
    main()
