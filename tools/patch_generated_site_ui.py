from __future__ import annotations

import argparse
import json
from fnmatch import fnmatch
from pathlib import Path
from typing import Any


CONTENT_REPO = Path(__file__).resolve().parent.parent
DEFAULT_BATCH = Path(__file__).with_name("generated_site_ui_translation_batch.json")
DEFAULT_BUILD_ROOT = CONTENT_REPO / "work" / "build"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def match_path(patterns: list[str], relative_path: str) -> bool:
    return any(fnmatch(relative_path, pattern) for pattern in patterns)


def iter_html_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*.html") if path.is_file())


def apply_batch(*, build_root: Path, language: str, batch_path: Path = DEFAULT_BATCH) -> dict[str, Any]:
    batch = load_json(batch_path)
    files = iter_html_files(build_root)
    by_path = {str(path.relative_to(build_root)): path for path in files}
    texts = {rel: path.read_text(encoding="utf-8") for rel, path in by_path.items()}
    replacements: list[dict[str, Any]] = []

    for entry in batch["entries"]:
        replacement = entry["translations"].get(language)
        if not replacement or replacement == entry["source"]:
            continue
        replacements.append(
            {
                "id": entry["id"],
                "paths": entry.get("paths", ["*.html"]),
                "source": entry["source"],
                "replacement": replacement,
            }
        )

    counts: dict[str, int] = {entry["id"]: 0 for entry in replacements}
    files_changed: set[str] = set()

    for entry in replacements:
        for relative_path, text in list(texts.items()):
            if not match_path(entry["paths"], relative_path):
                continue
            occurrences = text.count(entry["source"])
            if not occurrences:
                continue
            texts[relative_path] = text.replace(entry["source"], entry["replacement"])
            counts[entry["id"]] += occurrences
            files_changed.add(relative_path)

    for relative_path in sorted(files_changed):
        by_path[relative_path].write_text(texts[relative_path], encoding="utf-8")

    unresolved: dict[str, list[str]] = {}
    for entry in replacements:
        remaining_paths = []
        for relative_path, text in texts.items():
            if not match_path(entry["paths"], relative_path):
                continue
            if entry["source"] in text:
                remaining_paths.append(relative_path)
        if remaining_paths:
            unresolved[entry["id"]] = remaining_paths

    return {
        "language": language,
        "build_root": str(build_root),
        "batch": str(batch_path),
        "files_scanned": len(files),
        "files_changed": len(files_changed),
        "replacement_counts": {key: value for key, value in counts.items() if value},
        "unresolved": unresolved,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--language", required=True, choices=("fr", "it"))
    parser.add_argument("--build-root", type=Path, required=True)
    parser.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    report = apply_batch(build_root=args.build_root, language=args.language, batch_path=args.batch)
    if args.report:
        write_json(args.report, report)
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
