#!/usr/bin/env python
"""Rebuild the drawing SVG review export from canonical assets."""

from __future__ import annotations

import argparse
import json
import shutil
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CANONICAL_ROOT = REPO_ROOT / "canonical" / "drawings"
DEFAULT_REVIEW_DIR = REPO_ROOT / "work" / "drawing_svg_review"
LANGUAGES = ("de", "fr", "it")


def drawing_sort_key(stem: str) -> tuple[int, int | str, str]:
    if stem.isdigit():
        return (0, int(stem), stem)
    return (1, stem.casefold(), stem)


def collect_assets(canonical_root: Path) -> dict[str, dict[str, Path]]:
    assets: dict[str, dict[str, Path]] = {}
    for object_dir in sorted(canonical_root.iterdir()):
        if not object_dir.is_dir():
            continue
        german_files = sorted(object_dir.glob("*.de.svg"))
        if len(german_files) != 1:
            raise ValueError(
                f"Expected exactly one German SVG in {object_dir}, found {len(german_files)}"
            )
        german_path = german_files[0]
        stem = german_path.name.removesuffix(".de.svg")
        if stem in assets:
            raise ValueError(f"Duplicate drawing stem in canonical: {stem}")
        variants = {"de": german_path}
        for language in LANGUAGES[1:]:
            localized_path = object_dir / f"{stem}.{language}.svg"
            if localized_path.is_file():
                variants[language] = localized_path
        assets[stem] = variants
    return assets


def prepare_review(canonical_root: Path, review_dir: Path) -> dict[str, object]:
    canonical_root = canonical_root.resolve()
    review_dir = review_dir.resolve()
    if not canonical_root.is_dir():
        raise FileNotFoundError(f"Missing canonical drawings directory: {canonical_root}")

    assets = collect_assets(canonical_root)
    review_parent = review_dir.parent
    review_parent.mkdir(parents=True, exist_ok=True)
    staging_dir = Path(
        tempfile.mkdtemp(prefix=f".{review_dir.name}.staging-", dir=review_parent)
    )
    backup_dir = review_parent / f".{review_dir.name}.previous"

    try:
        for language in LANGUAGES:
            (staging_dir / language).mkdir()

        drawings: dict[str, dict[str, bool]] = {}
        for stem in sorted(assets, key=drawing_sort_key):
            variants = assets[stem]
            availability: dict[str, bool] = {}
            for language in LANGUAGES:
                source = variants.get(language)
                availability[language] = source is not None
                if source is not None:
                    shutil.copy2(source, staging_dir / language / source.name)
            drawings[stem] = availability

        report: dict[str, object] = {
            "drawing_count": len(assets),
            "explicit_variant_counts": {
                language: sum(language in variants for variants in assets.values())
                for language in LANGUAGES
            },
            "drawings": drawings,
        }
        (staging_dir / "manifest.json").write_text(
            json.dumps(report, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

        if backup_dir.exists():
            shutil.rmtree(backup_dir)
        if review_dir.exists():
            review_dir.rename(backup_dir)
        try:
            staging_dir.rename(review_dir)
        except Exception:
            if backup_dir.exists() and not review_dir.exists():
                backup_dir.rename(review_dir)
            raise
        if backup_dir.exists():
            shutil.rmtree(backup_dir)
        return report
    finally:
        if staging_dir.exists():
            shutil.rmtree(staging_dir)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--canonical-root", type=Path, default=DEFAULT_CANONICAL_ROOT)
    parser.add_argument("--review-dir", type=Path, default=DEFAULT_REVIEW_DIR)
    args = parser.parse_args()

    report = prepare_review(args.canonical_root, args.review_dir)
    counts = report["explicit_variant_counts"]
    print(
        "[drawing_review_export] "
        f"drawings={report['drawing_count']} "
        f"de={counts['de']} fr={counts['fr']} it={counts['it']} "
        f"review_dir={args.review_dir.resolve()}"
    )


if __name__ == "__main__":
    main()
