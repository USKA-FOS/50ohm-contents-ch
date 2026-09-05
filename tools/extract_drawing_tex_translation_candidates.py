#!/usr/bin/env python3
"""Extract structured translation candidates from canonical drawing TeX files."""

from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CANONICAL_DRAWINGS = REPO_ROOT / "canonical" / "drawings"
DEFAULT_OUTPUT = (
    REPO_ROOT
    / "work"
    / "drawing_text_audit"
    / "drawing_tex_translation_candidates.csv"
)

FORMAT_COMMANDS = {
    r"\bfseries",
    r"\mdseries",
    r"\itshape",
    r"\slshape",
    r"\upshape",
    r"\scshape",
    r"\rmfamily",
    r"\sffamily",
    r"\ttfamily",
    r"\tiny",
    r"\scriptsize",
    r"\footnotesize",
    r"\small",
    r"\normalsize",
    r"\large",
    r"\Large",
    r"\LARGE",
    r"\huge",
    r"\Huge",
    r"\centering",
}

PROTECTED_COMMANDS = (
    "includegraphics",
    "qty",
    "SI",
    "unit",
    "num",
    "ohm",
    "volt",
    "ampere",
    "milli",
    "micro",
    "nano",
    "kilo",
    "mega",
    "giga",
    "tera",
    "percent",
    "hertz",
    "watt",
    "farad",
    "henry",
    "celsius",
    "degree",
    "ctikzvalof",
)
MATH_TEXT_NON_TRANSLATABLE = {"max", "min"}


@dataclass
class Candidate:
    canonical_reference: str
    figure_number: str
    index: int
    raw_tex_fragment: str
    format_commands: str
    protected_tokens: str
    translatable_text: str
    category: str
    to_be_translated: str = "true"


def strip_comments(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        escaped = False
        result_chars: list[str] = []
        for char in line:
            if char == "%" and not escaped:
                break
            result_chars.append(char)
            escaped = char == "\\"
        lines.append("".join(result_chars))
    return "\n".join(lines)


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


def skip_optional_blocks(text: str, index: int) -> int:
    while index < len(text) and text[index].isspace():
        index += 1
    while index < len(text) and text[index] == "[":
        depth = 1
        index += 1
        while index < len(text) and depth:
            if text[index] == "[":
                depth += 1
            elif text[index] == "]":
                depth -= 1
            index += 1
        while index < len(text) and text[index].isspace():
            index += 1
    while index < len(text) and text[index] == "(":
        depth = 1
        index += 1
        while index < len(text) and depth:
            if text[index] == "(":
                depth += 1
            elif text[index] == ")":
                depth -= 1
            index += 1
        while index < len(text) and text[index].isspace():
            index += 1
    return index


def looks_translatable(raw_text: str) -> bool:
    text = raw_text.strip()
    if not text:
        return False
    simplified = re.sub(r"\\[A-Za-z@]+(?:\s*\[[^]]*\])?", " ", text)
    simplified = re.sub(r"[{}_^&~]", " ", simplified)
    simplified = re.sub(r"\$[^$]*\$", " ", simplified)
    simplified = simplified.replace("\\\\", " ")
    simplified = re.sub(r"\s+", " ", simplified).strip()
    if not simplified:
        return False
    if re.search(r"[ÄÖÜäöüß]", simplified):
        return True
    letters = re.findall(r"[A-Za-zÄÖÜäöüß]{2,}", simplified)
    return bool(letters)


def extract_node_candidates(text: str) -> list[tuple[str, str]]:
    candidates: list[tuple[str, str]] = []
    cursor = 0
    while True:
        match = re.search(r"(?<!\\)\bnode\b", text[cursor:])
        if not match:
            break
        index = cursor + match.end()
        index = skip_optional_blocks(text, index)
        if index < len(text) and text[index] == "{":
            try:
                content, index_after = read_balanced_group(text, index)
            except ValueError:
                cursor = index + 1
                continue
            if looks_translatable(content):
                candidates.append(("node_text", content.strip()))
            cursor = index_after
        else:
            cursor = index
    return candidates


def extract_pgftext_candidates(text: str) -> list[tuple[str, str]]:
    candidates: list[tuple[str, str]] = []
    cursor = 0
    needle = r"\pgftext"
    while True:
        index = text.find(needle, cursor)
        if index == -1:
            break
        index += len(needle)
        index = skip_optional_blocks(text, index)
        if index < len(text) and text[index] == "{":
            try:
                content, index_after = read_balanced_group(text, index)
            except ValueError:
                cursor = index + 1
                continue
            if looks_translatable(content):
                candidates.append(("pgftext_text", content.strip()))
            cursor = index_after
        else:
            cursor = index
    return candidates


def extract_circuitikz_label_candidates(text: str) -> list[tuple[str, str]]:
    candidates: list[tuple[str, str]] = []
    cursor = 0
    pattern = re.compile(r"(?<![A-Za-z@])(?:l\^_|l\^|l_|l|i\^_|i\^|i_|i|v\^_|v\^|v_|v)\s*=\s*")
    while True:
        match = pattern.search(text, cursor)
        if not match:
            break
        index = match.end()
        if index < len(text) and text[index] == "{":
            try:
                content, index_after = read_balanced_group(text, index)
            except ValueError:
                cursor = index + 1
                continue
            if looks_translatable(content):
                candidates.append(("circuitikz_label", content.strip()))
            cursor = index_after
        else:
            bare = read_bare_option_value(text, index)
            if bare is None:
                cursor = index + 1
                continue
            content, index_after = bare
            if looks_translatable(content):
                candidates.append(("circuitikz_bare_label", content.strip()))
            cursor = index_after
    return candidates


def read_bare_option_value(text: str, index: int) -> tuple[str, int] | None:
    end = index
    while end < len(text) and text[end] not in ",]":
        end += 1
    value = text[index:end].strip()
    if not value:
        return None
    return value, end


def extract_tikz_option_label_candidates(text: str) -> list[tuple[str, str]]:
    candidates: list[tuple[str, str]] = []
    cursor = 0
    pattern = re.compile(r"(?<![A-Za-z@])label\s*=\s*")
    while True:
        match = pattern.search(text, cursor)
        if not match:
            break
        index = match.end()
        if index < len(text) and text[index] == "{":
            try:
                content, index_after = read_balanced_group(text, index)
            except ValueError:
                cursor = index + 1
                continue
        else:
            bare = read_bare_option_value(text, index)
            if bare is None:
                cursor = index + 1
                continue
            content, index_after = bare
        if looks_translatable(content):
            candidates.append(("tikz_option_label", content.strip()))
        cursor = index_after
    return candidates


def extract_pgfplots_option_candidates(text: str) -> list[tuple[str, str]]:
    candidates: list[tuple[str, str]] = []
    for option_name in ("title", "xlabel", "ylabel"):
        cursor = 0
        pattern = re.compile(rf"(?<![A-Za-z@]){option_name}\s*=\s*")
        while True:
            match = pattern.search(text, cursor)
            if not match:
                break
            index = match.end()
            if index >= len(text) or text[index] != "{":
                cursor = index
                continue
            try:
                content, index_after = read_balanced_group(text, index)
            except ValueError:
                cursor = index + 1
                continue
            if looks_translatable(content):
                candidates.append((f"pgfplots_{option_name}", content.strip()))
            cursor = index_after
    return candidates


def extract_math_text_candidates(text: str) -> list[tuple[str, str]]:
    candidates: list[tuple[str, str]] = []
    cursor = 0
    pattern = re.compile(r"\\text\s*")
    while True:
        match = pattern.search(text, cursor)
        if not match:
            break
        index = match.end()
        if index >= len(text) or text[index] != "{":
            cursor = index
            continue
        try:
            content, index_after = read_balanced_group(text, index)
        except ValueError:
            cursor = index + 1
            continue
        if looks_translatable(content) and content.strip() not in MATH_TEXT_NON_TRANSLATABLE:
            candidates.append(("math_text", content.strip()))
        cursor = index_after
    return candidates


def unwrap_textcolor_content(text: str) -> str:
    stripped = text.strip()
    if not stripped.startswith(r"\textcolor"):
        return text
    cursor = len(r"\textcolor")
    while cursor < len(stripped) and stripped[cursor].isspace():
        cursor += 1
    if cursor >= len(stripped) or stripped[cursor] != "{":
        return text
    try:
        _, cursor = read_balanced_group(stripped, cursor)
    except ValueError:
        return text
    while cursor < len(stripped) and stripped[cursor].isspace():
        cursor += 1
    if cursor >= len(stripped) or stripped[cursor] != "{":
        return text
    try:
        visible, cursor = read_balanced_group(stripped, cursor)
    except ValueError:
        return text
    return visible if not stripped[cursor:].strip() else text


def collect_leading_format_commands(text: str) -> tuple[list[str], str]:
    commands: list[str] = []
    rest = text.strip()
    while True:
        matched = None
        for command in sorted(FORMAT_COMMANDS, key=len, reverse=True):
            if rest.startswith(command) and (
                len(rest) == len(command) or not rest[len(command)].isalpha()
            ):
                matched = command
                break
        if matched is None:
            return commands, rest
        commands.append(matched)
        rest = rest[len(matched):].lstrip()


def read_command_with_groups(text: str, index: int) -> tuple[str, int] | None:
    match = re.match(r"\\([A-Za-z@]+)", text[index:])
    if not match:
        return None
    command_name = match.group(1)
    if command_name not in PROTECTED_COMMANDS:
        return None
    cursor = index + len(match.group(0))
    while cursor < len(text) and text[cursor].isspace():
        cursor += 1
    while cursor < len(text) and text[cursor] == "[":
        depth = 1
        cursor += 1
        while cursor < len(text) and depth:
            if text[cursor] == "[":
                depth += 1
            elif text[cursor] == "]":
                depth -= 1
            cursor += 1
        while cursor < len(text) and text[cursor].isspace():
            cursor += 1
    while cursor < len(text) and text[cursor] == "{":
        _, cursor = read_balanced_group(text, cursor)
        while cursor < len(text) and text[cursor].isspace():
            cursor += 1
    return text[index:cursor], cursor


def collect_protected_tokens(text: str) -> tuple[list[str], str]:
    tokens: list[str] = []
    output: list[str] = []
    i = 0
    while i < len(text):
        if text[i] == "$":
            end = i + 1
            while end < len(text):
                if text[end] == "$" and text[end - 1] != "\\":
                    end += 1
                    break
                end += 1
            token = text[i:end]
            tokens.append(token)
            output.append(" ")
            i = end
            continue
        if text[i] == "\\":
            command = read_command_with_groups(text, i)
            if command is not None:
                token, end = command
                tokens.append(token)
                output.append(" ")
                i = end
                continue
        output.append(text[i])
        i += 1
    return tokens, "".join(output)


def cleanup_translatable_text(text: str) -> str:
    cleaned = text.replace("\\\\", " ")
    cleaned = re.sub(r"\\,", " ", cleaned)
    cleaned = re.sub(r"\\[A-Za-z@]+\*?", " ", cleaned)
    cleaned = re.sub(r"[{}~]", " ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def build_structured_candidate(
    canonical_reference: str,
    figure_number: str,
    index: int,
    raw_content: str,
    category: str,
) -> Candidate:
    visible_content = unwrap_textcolor_content(raw_content)
    format_commands, remainder = collect_leading_format_commands(visible_content)
    protected_tokens, remainder = collect_protected_tokens(remainder)
    translatable_text = cleanup_translatable_text(remainder)
    return Candidate(
        canonical_reference=canonical_reference,
        figure_number=figure_number,
        index=index,
        raw_tex_fragment=(
            raw_content.strip()
            if category == "circuitikz_bare_label"
            else rf"\text{{{raw_content.strip()}}}"
            if category == "math_text"
            else "{" + raw_content.strip() + "}"
        ),
        format_commands=json.dumps(format_commands, ensure_ascii=False),
        protected_tokens=json.dumps(protected_tokens, ensure_ascii=False),
        translatable_text=translatable_text,
        category=category,
    )


def load_figure_number(meta_path: Path) -> str:
    payload = json.loads(meta_path.read_text(encoding="utf-8"))
    for identifier in payload.get("identifiers", []):
        if identifier.get("id_system") == "drawing_id":
            return str(identifier.get("id_value"))
    return str(payload.get("source", {}).get("key", ""))


def load_source_import_drawing_refs(path: Path) -> set[str]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("workflow") != "incremental_german_source_import":
        raise ValueError(f"Not an incremental German source import audit: {path}")
    if payload.get("applied") is not True:
        raise ValueError(f"Source import audit was not applied: {path}")
    drawing_ids = {
        str(change["object_id"])
        for change in payload.get("changes", [])
        if change.get("object_type") == "drawing"
        and change.get("translation_required") is True
        and change.get("action") in {"added", "changed", "reactivated", "renamed"}
    }
    return {f"canonical/drawings/{object_id}" for object_id in drawing_ids}


def build_candidates(canonical_references: set[str] | None = None) -> list[Candidate]:
    rows: list[Candidate] = []
    for meta_path in sorted(CANONICAL_DRAWINGS.glob("*/object.meta.json")):
        drawing_dir = meta_path.parent
        canonical_reference = str(drawing_dir.relative_to(REPO_ROOT))
        if canonical_references is not None and canonical_reference not in canonical_references:
            continue
        figure_number = load_figure_number(meta_path)
        tex_paths = sorted(drawing_dir.glob("*.de.tex"))
        index = 1
        for tex_path in tex_paths:
            content = strip_comments(tex_path.read_text(encoding="utf-8"))
            extracted = extract_node_candidates(content)
            extracted.extend(extract_pgftext_candidates(content))
            extracted.extend(extract_circuitikz_label_candidates(content))
            extracted.extend(extract_tikz_option_label_candidates(content))
            extracted.extend(extract_pgfplots_option_candidates(content))
            extracted.extend(extract_math_text_candidates(content))
            for category, raw_content in extracted:
                candidate = build_structured_candidate(
                    canonical_reference=canonical_reference,
                    figure_number=figure_number,
                    index=index,
                    raw_content=raw_content,
                    category=category,
                )
                if candidate.translatable_text:
                    rows.append(candidate)
                    index += 1
    return rows


def write_csv(rows: list[Candidate], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "canonical_reference",
                "figure_number",
                "index",
                "raw_tex_fragment",
                "format_commands",
                "protected_tokens",
                "translatable_text",
                "category",
                "to_be_translated",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(row.__dict__)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--source-import-audit",
        type=Path,
        help="Limit extraction to changed drawings from an applied German source import audit.",
    )
    args = parser.parse_args()
    canonical_references = (
        load_source_import_drawing_refs(args.source_import_audit.resolve())
        if args.source_import_audit
        else None
    )
    rows = build_candidates(canonical_references)
    write_csv(rows, args.output)
    print(f"rows={len(rows)}")
    if canonical_references is not None:
        print(f"scoped_drawings={len(canonical_references)}")
    print(f"output={args.output}")


if __name__ == "__main__":
    main()
