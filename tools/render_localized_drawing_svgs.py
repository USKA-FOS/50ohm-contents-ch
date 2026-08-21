#!/usr/bin/env python3
"""Render localized drawing SVG assets from canonical drawing TeX files."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import tempfile
import traceback
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
DEFAULT_RENDER_REPORT = (
    REPO_ROOT / "work" / "drawing_text_audit" / "drawing_svg_render_report.json"
)
DEFAULT_RENDER_LOG = (
    REPO_ROOT / "work" / "drawing_text_audit" / "drawing_svg_render.log"
)
TEXMF_CACHE_ROOT = REPO_ROOT / "work" / "drawing_text_audit" / "texmf-cache"
TEXMF_VAR_ROOT = REPO_ROOT / "work" / "drawing_text_audit" / "texmf-var"
SUPPORTED_LANGUAGES = ("de", "fr", "it")
DEFAULT_LANGUAGES = ("fr", "it")
LATEX_SUPPORT_FILES = (
    "FiftyOhm.cls",
    "DARC-ausbildungsmaterialien.sty",
    "settings.tex",
    "settings-pre.tex",
)
PHOTO_INCLUDE_PATTERN = re.compile(r"\\includegraphics(?:\[[^]]*\])?\{foto/([^}]+)\}")
SVG_WIDTH_PATTERN = re.compile(r'<svg\b[^>]*\bwidth="([0-9.]+)(pt)?"')
TEX_POINTS_PER_INCH = 72.27


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


def build_photo_asset_map(language: str) -> dict[str, Path]:
    if not CANONICAL_PHOTOS_ROOT.exists():
        return {}
    mapping: dict[str, Path] = {}
    for meta_path in sorted(CANONICAL_PHOTOS_ROOT.glob("*/object.meta.json")):
        payload = json.loads(meta_path.read_text(encoding="utf-8"))
        object_dir = meta_path.parent
        variants = payload.get("language_variants", {}) or {}

        asset_name = (
            ((variants.get(language, {}) or {}).get("asset_files", {}) or {}).get("image")
            or ((variants.get("de", {}) or {}).get("asset_files", {}) or {}).get("image")
        )
        if not asset_name:
            continue
        asset_path = object_dir / asset_name
        if not asset_path.exists():
            continue

        keys: set[str] = set()
        for identifier in payload.get("identifiers", []):
            value = str(identifier.get("id_value", "")).strip()
            if value:
                keys.add(value)
        source_key = str((payload.get("source", {}) or {}).get("key", "")).strip()
        if source_key:
            keys.add(source_key)
        keys.add(asset_path.stem.split(".")[0])

        for key in keys:
            mapping[key] = asset_path
    return mapping


def materialize_photo_assets(target_dir: Path, language: str) -> None:
    photo_map = build_photo_asset_map(language)
    target_dir.mkdir(parents=True, exist_ok=True)
    for key, asset_path in photo_map.items():
        suffix = asset_path.suffix
        named_target = target_dir / f"{key}{suffix}"
        if named_target.exists() or named_target.is_symlink():
            named_target.unlink()
        named_target.symlink_to(asset_path)

        bare_target = target_dir / key
        if bare_target.exists() or bare_target.is_symlink():
            bare_target.unlink()
        bare_target.symlink_to(named_target.name)


def extract_photo_refs(tex_text: str) -> list[str]:
    return [match.group(1).strip() for match in PHOTO_INCLUDE_PATTERN.finditer(tex_text)]


def validate_photo_refs(tex_text: str, language: str) -> None:
    refs = extract_photo_refs(tex_text)
    if not refs:
        return
    available = build_photo_asset_map(language)
    missing = sorted({ref for ref in refs if ref not in available})
    if missing:
        raise SystemExit(
            "Missing canonical photo assets for localized drawing render: "
            + ", ".join(missing)
        )


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


def source_width_cm(tex_path: Path, stem: str, override: float | None) -> float:
    if override is not None:
        return override
    de_svg = tex_path.with_name(f"{stem}.de.svg")
    if not de_svg.exists():
        raise FileNotFoundError(f"Missing German reference SVG: {de_svg}")
    header = de_svg.read_text(encoding="utf-8", errors="replace")[:2048]
    match = SVG_WIDTH_PATTERN.search(header)
    if not match:
        raise ValueError(f"German reference SVG has no numeric width: {de_svg}")
    return float(match.group(1)) / TEX_POINTS_PER_INCH * 2.54


def svg_width_pt(svg_path: Path) -> float | None:
    if not svg_path.exists():
        return None
    header = svg_path.read_text(encoding="utf-8", errors="replace")[:2048]
    match = SVG_WIDTH_PATTERN.search(header)
    if not match:
        return None
    return float(match.group(1))


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
            validate_photo_refs(tex_text, language)
            photo_link = tmp_dir / "foto"
            materialize_photo_assets(photo_link, language)
            photo_link_2 = img_dir / "foto"
            materialize_photo_assets(photo_link_2, language)

        env = os.environ.copy()
        env.setdefault("TEXMFCACHE", str(TEXMF_CACHE_ROOT))
        env.setdefault("TEXMFVAR", str(TEXMF_VAR_ROOT))
        Path(env["TEXMFCACHE"]).mkdir(parents=True, exist_ok=True)
        Path(env["TEXMFVAR"]).mkdir(parents=True, exist_ok=True)

        latex_result = subprocess.run(
            ["latexmk", "-lualatex", "-cd", str(aux_file)],
            cwd=tmp_dir,
            env=env,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        if latex_result.returncode:
            tail = latex_result.stdout[-8000:]
            raise RuntimeError(f"latexmk failed for {tex_path}:\n{tail}")
        cairo_result = subprocess.run(
            ["pdftocairo", "-svg", str(tmp_dir / f"{stem}.pdf"), str(output_svg)],
            cwd=tmp_dir,
            env=env,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        if cairo_result.returncode:
            tail = cairo_result.stdout[-8000:]
            raise RuntimeError(f"pdftocairo failed for {tex_path}:\n{tail}")


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


def should_rerender(*, tex_path: Path, svg_path: Path, skip_existing: bool) -> bool:
    if not svg_path.exists():
        return True
    if tex_path.stat().st_mtime > svg_path.stat().st_mtime:
        return True
    stem = infer_stem(tex_path, tex_path.suffixes[-2].lstrip("."))
    de_width = svg_width_pt(tex_path.with_name(f"{stem}.de.svg"))
    localized_width = svg_width_pt(svg_path)
    if de_width is not None and localized_width is not None:
        if abs(de_width - localized_width) > 0.01:
            return True
    return not skip_existing


def append_log(log_path: Path, message: str) -> None:
    if message:
        print(message.rstrip(), flush=True)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(message.rstrip() + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--language", action="append", choices=SUPPORTED_LANGUAGES)
    parser.add_argument("--canonical-ref", action="append", help="Canonical drawing reference like canonical/drawings/dr_xxx")
    parser.add_argument("--from-import-report", action="store_true", help="Limit rendering to drawings listed in the latest drawing translation import report.")
    parser.add_argument("--import-report", type=Path, default=DEFAULT_IMPORT_REPORT)
    parser.add_argument(
        "--width-cm",
        type=float,
        default=None,
        help="Override the German SVG reference width instead of preserving it.",
    )
    parser.add_argument("--copy-review-dir", type=Path, default=DEFAULT_REVIEW_DIR)
    parser.add_argument("--no-copy-review", action="store_true")
    parser.add_argument("--report-json", type=Path, default=DEFAULT_RENDER_REPORT)
    parser.add_argument("--log-file", type=Path, default=DEFAULT_RENDER_LOG)
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip only existing SVGs that are up to date and match the German width.",
    )
    args = parser.parse_args()

    missing = ensure_dependencies()
    if missing:
        raise SystemExit("Missing dependencies: " + ", ".join(missing))

    languages = args.language or list(DEFAULT_LANGUAGES)
    canonical_refs = list(args.canonical_ref or [])
    if args.from_import_report:
        canonical_refs.extend(load_import_report(args.import_report))
    canonical_refs = sorted(dict.fromkeys(canonical_refs))

    tex_paths = iter_target_tex_paths(languages=languages, canonical_refs=canonical_refs or None)
    rendered: list[dict[str, Any]] = []
    failed: list[dict[str, Any]] = []
    skipped_existing = 0
    append_log(args.log_file, "")
    append_log(args.log_file, "=== render_localized_drawing_svgs run start ===")
    for tex_path in tex_paths:
        language = tex_path.suffixes[-2].lstrip(".")
        stem = infer_stem(tex_path, language)
        svg_path = tex_path.with_name(f"{stem}.{language}.svg")
        record: dict[str, Any] = {
            "tex": str(tex_path.relative_to(REPO_ROOT)),
            "svg": str(svg_path.relative_to(REPO_ROOT)),
            "language": language,
        }
        try:
            rerender = should_rerender(
                tex_path=tex_path,
                svg_path=svg_path,
                skip_existing=args.skip_existing,
            )
            used_existing = not rerender and svg_path.exists()
            if used_existing:
                skipped_existing += 1
                record["used_existing_svg"] = True
                append_log(args.log_file, f"SKIP  {record['svg']} (up-to-date)")
            else:
                append_log(args.log_file, f"START {record['tex']} -> {record['svg']}")
                width_cm = source_width_cm(tex_path, stem, args.width_cm)
                record["width_cm"] = width_cm
                render_tex_to_svg(tex_path=tex_path, stem=stem, width_cm=width_cm)
                append_log(args.log_file, f"OK    {record['svg']}")
            update_meta_for_svg(tex_path.parent, stem, language)
            if not args.no_copy_review:
                review_path = copy_to_review(svg_path=svg_path, language=language, review_dir=args.copy_review_dir)
                record["review_copy"] = str(review_path.relative_to(REPO_ROOT))
            rendered.append(record)
        except Exception as exc:
            failure = {
                **record,
                "error_type": type(exc).__name__,
                "error": str(exc),
            }
            failed.append(failure)
            append_log(args.log_file, f"FAIL  {record['tex']} -> {record['svg']}")
            append_log(args.log_file, traceback.format_exc())
            continue

    args.report_json.parent.mkdir(parents=True, exist_ok=True)
    report = {
        "rendered_count": len(rendered),
        "failed_count": len(failed),
        "skipped_existing": skipped_existing,
        "languages": languages,
        "scoped_drawings": len(canonical_refs),
        "rendered": rendered,
        "failed": failed,
        "log_file": str(args.log_file.relative_to(REPO_ROOT)),
    }
    args.report_json.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"rendered_count={len(rendered)}")
    print(f"failed_count={len(failed)}")
    print(f"skipped_existing={skipped_existing}")
    print(f"languages={','.join(languages)}")
    if canonical_refs:
        print(f"scoped_drawings={len(canonical_refs)}")
    print(f"report_json={args.report_json}")
    print(f"log_file={args.log_file}")
    if not args.no_copy_review:
        print(f"review_dir={args.copy_review_dir}")


if __name__ == "__main__":
    main()
