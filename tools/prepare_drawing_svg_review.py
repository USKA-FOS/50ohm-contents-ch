#!/usr/bin/env python
"""Rebuild the drawing SVG review export from canonical assets."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from urllib.parse import urlsplit


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CANONICAL_ROOT = REPO_ROOT / "canonical" / "drawings"
DEFAULT_REVIEW_DIR = REPO_ROOT / "work" / "drawing_svg_review"
LANGUAGES = ("de", "fr", "it")
STATIC_DIR = Path(__file__).resolve().parent / "drawing_svg_review"
DEFAULT_FEEDBACK_URL = "https://50ohm.jp2s.ch/feedback/"
REVIEW_ID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,99}$")


def drawing_sort_key(stem: str) -> tuple[int, int | str, str]:
    if stem.isdigit():
        return (0, int(stem), stem)
    return (1, stem.casefold(), stem)


def collect_assets(canonical_root: Path) -> dict[str, dict[str, object]]:
    assets: dict[str, dict[str, object]] = {}
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
        variants: dict[str, Path] = {"de": german_path}
        for language in LANGUAGES[1:]:
            localized_path = object_dir / f"{stem}.{language}.svg"
            if localized_path.is_file():
                variants[language] = localized_path
        assets[stem] = {
            "canonical_id": object_dir.name,
            "canonical_reference": f"canonical/drawings/{object_dir.name}",
            "variants": variants,
        }
    return assets


def asset_digest(assets: dict[str, dict[str, object]]) -> str:
    digest = hashlib.sha256()
    for stem in sorted(assets, key=drawing_sort_key):
        digest.update(f"{stem}\0{assets[stem]['canonical_id']}\0".encode())
        variants = assets[stem]["variants"]
        assert isinstance(variants, dict)
        for language in LANGUAGES:
            path = variants.get(language)
            if not isinstance(path, Path):
                continue
            digest.update(f"{stem}.{language}.svg\0".encode())
            digest.update(path.read_bytes())
    return digest.hexdigest()


def git_source_state() -> dict[str, object]:
    commit = subprocess.check_output(
        ["git", "-C", str(REPO_ROOT), "rev-parse", "HEAD"], text=True
    ).strip()
    dirty = bool(
        subprocess.check_output(
            ["git", "-C", str(REPO_ROOT), "status", "--porcelain", "--", "canonical"],
            text=True,
        ).strip()
    )
    return {"commit": commit, "dirty": dirty}


def validate_publication_context(feedback_url: str, review_id: str) -> None:
    parsed = urlsplit(feedback_url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("feedback_url must be an absolute HTTP or HTTPS URL")
    if not REVIEW_ID_PATTERN.fullmatch(review_id):
        raise ValueError("review_id contains unsupported characters or exceeds 100 characters")


def ensure_review_output_clean(review_dir: Path) -> None:
    try:
        repository = Path(
            subprocess.check_output(
                ["git", "-C", str(review_dir.parent), "rev-parse", "--show-toplevel"],
                text=True,
                stderr=subprocess.DEVNULL,
            ).strip()
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return
    try:
        relative = review_dir.resolve().relative_to(repository.resolve())
    except ValueError:
        return
    status = subprocess.check_output(
        ["git", "-C", str(repository), "status", "--porcelain", "--", str(relative)],
        text=True,
    )
    if status.strip():
        raise RuntimeError(f"Refusing to replace uncommitted drawing review output: {review_dir}")


def prepare_review(
    canonical_root: Path,
    review_dir: Path,
    *,
    feedback_url: str = DEFAULT_FEEDBACK_URL,
    review_id: str | None = None,
    source_state: dict[str, object] | None = None,
    require_clean_source: bool = False,
) -> dict[str, object]:
    canonical_root = canonical_root.resolve()
    review_dir = review_dir.resolve()
    if not canonical_root.is_dir():
        raise FileNotFoundError(f"Missing canonical drawings directory: {canonical_root}")

    assets = collect_assets(canonical_root)
    digest = asset_digest(assets)
    review_id = review_id or f"drawing-review-{digest[:12]}"
    source_state = source_state or git_source_state()
    validate_publication_context(feedback_url, review_id)
    if require_clean_source and source_state.get("dirty") is not False:
        raise RuntimeError("Refusing drawing review publication because canonical/ is not clean")
    ensure_review_output_clean(review_dir)
    review_parent = review_dir.parent
    review_parent.mkdir(parents=True, exist_ok=True)
    staging_dir = Path(
        tempfile.mkdtemp(prefix=f".{review_dir.name}.staging-", dir=review_parent)
    )
    backup_dir = review_parent / f".{review_dir.name}.previous"

    try:
        for language in LANGUAGES:
            (staging_dir / language).mkdir()
        shutil.copy2(STATIC_DIR / "index.html", staging_dir / "index.html")
        (staging_dir / "assets").mkdir()
        for asset_name in ("review.css", "review.js"):
            shutil.copy2(STATIC_DIR / asset_name, staging_dir / "assets" / asset_name)

        drawings: dict[str, dict[str, object]] = {}
        for stem in sorted(assets, key=drawing_sort_key):
            drawing = assets[stem]
            variants = drawing["variants"]
            assert isinstance(variants, dict)
            availability: dict[str, bool] = {}
            for language in LANGUAGES:
                source = variants.get(language)
                availability[language] = source is not None
                if source is not None:
                    shutil.copy2(source, staging_dir / language / source.name)
            drawings[stem] = {
                "canonical_id": drawing["canonical_id"],
                "canonical_reference": drawing["canonical_reference"],
                "availability": availability,
            }

        report: dict[str, object] = {
            "schema_version": 1,
            "context_type": "drawing_review",
            "review_id": review_id,
            "feedback_url": feedback_url,
            "asset_sha256": digest,
            "sources": {"50ohm-contents-ch": source_state},
            "drawing_count": len(assets),
            "explicit_variant_counts": {
                language: sum(
                    language in drawing["variants"] for drawing in assets.values()
                )
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
    parser.add_argument("--feedback-url", default=DEFAULT_FEEDBACK_URL)
    parser.add_argument("--review-id")
    parser.add_argument(
        "--require-clean-source",
        action="store_true",
        help="Refuse publication when canonical/ has uncommitted changes.",
    )
    args = parser.parse_args()

    report = prepare_review(
        args.canonical_root,
        args.review_dir,
        feedback_url=args.feedback_url,
        review_id=args.review_id,
        require_clean_source=args.require_clean_source,
    )
    counts = report["explicit_variant_counts"]
    print(
        "[drawing_review_export] "
        f"drawings={report['drawing_count']} "
        f"de={counts['de']} fr={counts['fr']} it={counts['it']} "
        f"review_id={report['review_id']} "
        f"review_dir={args.review_dir.resolve()}"
    )


if __name__ == "__main__":
    main()
