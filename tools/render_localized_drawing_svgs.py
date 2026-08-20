#!/usr/bin/env python3
"""Render localized drawing SVG assets from canonical drawing TeX files."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DRAWINGS_ROOT = REPO_ROOT / "canonical" / "drawings"
LATEX_SUPPORT_ROOT = REPO_ROOT / "latex_deleted"
PHOTOS_ROOT = REPO_ROOT / "contents" / "photos"
CANONICAL_PHOTOS_ROOT = REPO_ROOT / "canonical" / "photos"
DEFAULT_IMPORT_REPORT = (
    REPO_ROOT / "work" / "drawing_text_audit" / "drawing_tex_translation_import_report.json"
)
DEFAULT_REVIEW_DIR = REPO_ROOT / "work" / "drawing_svg_review"
SUPPORTED_LANGUAGES = ("fr", "it")
LATEX_SUPPORT_FILES = (
    "FiftyOhm.cls",
    "DARC-ausbildungsmaterialien.sty",
    "settings.tex",
    "settings-pre.tex",
)


def ensure_dependencies() -> list[str]:
    missing: list[str] = []
    for command in ("latexmk", "lualatex", "pdftocairo"):
        if shutil.which(command) is None:
            missing.append(command)
    for filename in LATEX_SUPPORT_FILES:
        if not (LATEX_SUPPORT_ROOT / filename).exists():
            missing.append(str(LATEX_SUPPORT_ROOT / filename))
    return missing


def resolve_photos_root() -> Path | None:
    if PHOTOS_ROOT.exists():
        return PHOTOS_ROOT
    if CANONICAL_PHOTOS_ROOT.exists():
        return CANONICAL_PHOTOS_ROOT
    return None


def tex_requires_photo_assets(tex_text: str) -> bool:
    return "\\includegraphics" in tex_text or "foto/" in tex_text or "foto" in tex_text


def load_import_report(path: Path) -> list[str]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    refs: list[str] = []
    for item in payload.get("updated_drawings", []):
        ref = str(item.get("canonical_reference", "")).strip()
        if ref:
            refs.append(ref)
    return refs


def infer_stem(tex_path: Path, language: str) -> str:
    suffix = f".{language}.tex"
    if not tex_path.name.endswith(suffix):
        raise ValueError(f"Unexpected localized TeX filename: {tex_path.name}")
    return tex_path.name[: -len(suffix)]


def render_tex_to_svg(*, tex_path: Path, stem: str, width_cm: float) -> None:
    drawing_dir = tex_path.parent
    language = tex_path.suffixes[-2].lstrip(".")
    output_svg = drawing_dir / f"{stem}.{language}.svg"
    tex_text = tex_path.read_text(encoding="utf-8")
    photos_root = resolve_photos_root()

    with tempfile.TemporaryDirectory(prefix="drawing_svg_", dir=REPO_ROOT) as tmp_dir_name:
        tmp_dir = Path(tmp_dir_name)
        img_dir = tmp_dir / "img"
        img_dir.mkdir(parents=True, exist_ok=True)

        include_path = img_dir / f"{stem}include.tex"
        include_path.write_text(tex_text, encoding="utf-8")

        aux_file = tmp_dir / f"{stem}.tex"
        aux_file.write_text(
            f"\\documentclass{{FiftyOhm}}\\DARCimageOnly{{{width_cm}cm}}{{{stem}include}}",
            encoding="utf-8",
        )

        for filename in LATEX_SUPPORT_FILES:
            shutil.copy2(LATEX_SUPPORT_ROOT / filename, tmp_dir / filename)

        if tex_requires_photo_assets(tex_text):
            if photos_root is None:
                raise SystemExit(
                    "This drawing requires photo assets, but neither "
                    f"{PHOTOS_ROOT} nor {CANONICAL_PHOTOS_ROOT} exists."
                )
            photo_link = tmp_dir / "foto"
            photo_link.symlink_to(photos_root)
            photo_link_2 = img_dir / "foto"
            photo_link_2.symlink_to(photos_root)

        subprocess.run(
            ["latexmk", "-lualatex", "-cd", str(aux_file)],
            check=True,
            cwd=tmp_dir,
            stdin=subprocess.DEVNULL,
        )
        subprocess.run(
            ["pdftocairo", "-svg", str(tmp_dir / f"{stem}.pdf"), str(output_svg)],
            check=True,
            cwd=tmp_dir,
            stdin=subprocess.DEVNULL,
        )


def update_meta_for_svg(object_dir: Path, stem: str, language: str) -> None:
    meta_path = object_dir / "object.meta.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))

    language_variants = meta.setdefault("language_variants", {})
    variant = language_variants.setdefault(language, {})
    asset_files = variant.setdefault("asset_files", {})
    asset_files["svg"] = f"{stem}.{language}.svg"
    asset_files.setdefault("tex", f"{stem}.{language}.tex")
    variant.setdefault("review_state", "to_be_reviewed")

    metadata = meta.setdefault("metadata", {})
    language_asset = metadata.setdefault("language_asset", {})
    svg_key = f"{language}.svg"
    svg_entry = language_asset.setdefault(svg_key, {})
    svg_entry["canonical_file"] = f"{stem}.{language}.svg"
    tex_key = f"{language}.tex"
    tex_entry = language_asset.setdefault(tex_key, {})
    tex_entry["canonical_file"] = f"{stem}.{language}.tex"

    meta_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def copy_to_review(*, svg_path: Path, language: str, review_dir: Path) -> Path:
    target_dir = review_dir / language
    target_dir.mkdir(parents=True, exist_ok=True)
    target_path = target_dir / svg_path.name
    shutil.copy2(svg_path, target_path)
    return target_path


def iter_target_tex_paths(*, languages: list[str], canonical_refs: list[str] | None) -> list[Path]:
    if canonical_refs:
        roots = [REPO_ROOT / ref for ref in canonical_refs]
    else:
        roots = sorted(DRAWINGS_ROOT.glob("*"))
    targets: list[Path] = []
    for root in roots:
        if not root.exists():
            continue
        for language in languages:
            targets.extend(sorted(root.glob(f"*.{language}.tex")))
    return targets


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--language", action="append", choices=SUPPORTED_LANGUAGES)
    parser.add_argument("--canonical-ref", action="append", help="Canonical drawing reference like canonical/drawings/dr_xxx")
    parser.add_argument("--from-import-report", action="store_true", help="Limit rendering to drawings listed in the latest drawing translation import report.")
    parser.add_argument("--import-report", type=Path, default=DEFAULT_IMPORT_REPORT)
    parser.add_argument("--width-cm", type=float, default=9.0)
    parser.add_argument("--copy-review-dir", type=Path, default=DEFAULT_REVIEW_DIR)
    parser.add_argument("--no-copy-review", action="store_true")
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Do not rerender when the target localized SVG already exists.",
    )
    args = parser.parse_args()

    missing = ensure_dependencies()
    if missing:
        raise SystemExit("Missing dependencies: " + ", ".join(missing))

    languages = args.language or list(SUPPORTED_LANGUAGES)
    canonical_refs = list(args.canonical_ref or [])
    if args.from_import_report:
        canonical_refs.extend(load_import_report(args.import_report))
    canonical_refs = sorted(dict.fromkeys(canonical_refs))

    tex_paths = iter_target_tex_paths(languages=languages, canonical_refs=canonical_refs or None)
    rendered: list[dict[str, Any]] = []
    skipped_existing = 0
    for tex_path in tex_paths:
        language = tex_path.suffixes[-2].lstrip(".")
        stem = infer_stem(tex_path, language)
        svg_path = tex_path.with_name(f"{stem}.{language}.svg")
        used_existing = args.skip_existing and svg_path.exists()
        if used_existing:
            skipped_existing += 1
        else:
            render_tex_to_svg(tex_path=tex_path, stem=stem, width_cm=args.width_cm)
        update_meta_for_svg(tex_path.parent, stem, language)
        record: dict[str, Any] = {
            "tex": str(tex_path.relative_to(REPO_ROOT)),
            "svg": str(svg_path.relative_to(REPO_ROOT)),
            "language": language,
        }
        if used_existing:
            record["used_existing_svg"] = True
        if not args.no_copy_review:
            review_path = copy_to_review(svg_path=svg_path, language=language, review_dir=args.copy_review_dir)
            record["review_copy"] = str(review_path.relative_to(REPO_ROOT))
        rendered.append(record)

    print(f"rendered_count={len(rendered)}")
    print(f"skipped_existing={skipped_existing}")
    print(f"languages={','.join(languages)}")
    if canonical_refs:
        print(f"scoped_drawings={len(canonical_refs)}")
    if not args.no_copy_review:
        print(f"review_dir={args.copy_review_dir}")


if __name__ == "__main__":
    main()
