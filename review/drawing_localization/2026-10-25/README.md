# Drawing TeX: redundant semicolon cleanup

The user requested an investigation of every `Missing character: There is no
; (U+003B) in font nullfont!` notice in the Revision_3.0.5 PDF builds, and removal
of proven redundant characters. No visible drawing text was changed.

## Findings and applied changes

All 57 notices per language and compilation pass are explained by 35 redundant
semicolons in 19 German canonical drawing sources. These drawings have no
localized TeX variants; FR/IT PDF preparation uses the German fallback.

| Cause | Semicolons removed | Notices in each complete catalogue pass |
| --- | ---: | ---: |
| Trailing delimiter after `\tikzstyle` definition | 13 | 18 |
| Trailing delimiter after self-terminated `\swr`, `\pwr`, `\vol`, `\qrg` macros | 20 | 36 |
| Duplicate delimiter after a path in drawing 490 | 1 | 1 |
| Trailing delimiter after `\pgfresetboundingbox` in drawing 952 | 1 | 2 |
| Total | 35 | 57 |

Drawing IDs: 36, 38, 52, 53, 55, 56, 57, 75, 490, 526, 527, 578, 580,
586, 587, 588, 627, 880, 952.

Valid delimiters after TikZ paths, including `\draw`, `\node`, `\addplot` and
`\useasboundingbox`, are retained. `\mdl` accepts its optional delimiter and
was left unchanged. Generic deletion of semicolons is unsafe.

The complete file list, line substitutions, before/after SHA-256 hashes,
29 affected question codes, baseline commits and verification results are in
[the applied audit](semicolon-cleanup.audit.json).

## Verification

All 29 affected questions were compiled before and after cleanup in each
language, with the existing PDF preparation support and the existing drawing
490 presentation normalization. Before cleanup each targeted build reproduces
all 57 notices; afterwards there are **zero missing-character notices**.

Extracted text is identical before and after. Rasterized pages are pixel
identical at 60 dpi: 14 pages for DE, 14 for FR, 15 for IT. This verifies the
entire affected question set, not just one illustrative drawing. Other
compilation diagnostics in these tests remain unchanged.

`tools/validate_canonical_model.py` reports 2,356 objects, zero errors and zero
warnings after application. `git diff --check` passes.

Scratch files and minimal compilation results live under the orchestrator's
ignored `tmp/drawing-semicolon-cleanup-20261025/`. During the initial cleanup,
the production PDF files, their original logs, existing SVGs and site releases
were not overwritten. The subsequent SVG refresh is documented below.
Run `tools/qp2pdf.sh <de|fr|it> --tag Revision_3.0.5` again to incorporate the
cleaned drawing sources in a full PDF. The filename tag labels the output;
the drawing sources are read from the current contents checkout.

## Other diagnostics remaining

The latest complete PDF builds remain the 24 October builds. Their second-pass
logs provide this baseline for diagnostics outside the semicolon cleanup:

| Language | Underfull boxes | Overfull boxes | Font warnings |
| --- | ---: | ---: | ---: |
| DE | 8 | 0 | 6 |
| FR | 0 | 1 | 6 |
| IT | 38 | 0 | 6 |

The French overfull box is 4.57323 TeX pt, approximately **1.61 mm**, in the
table of contents on page 4, for
“COMPATIBILITÉ ÉLECTROMAGNÉTIQUE, APPLICATION, PROTECTION DES PERSONNES”.
On 25 October the user confirmed that this small overflow is not visually
noticeable. No layout correction is requested for it.

Overflow reports must state the measured width in both TeX points and
millimetres, and explicitly describe an overflow of only a few millimetres as
small. Distinguish the measured box overflow from visible clipping or crossing
the printable page boundary; the warning alone proves neither. Retain the
warning and record any human visual assessment alongside it.

The conversion is `mm = TeX pt × 25.4 / 72.27`. Thus **10 TeX pt = 3.515 mm**,
approximately 1.67% of the 210 mm A4 page width. This is a size reference;
the user has not yet selected a general numerical acceptance threshold.

Underfull boxes concern line filling and were previously accepted without
changing the layout. Font warnings concern unavailable bold variants:
three TeX Gyre Pagella Math shapes, two `wasy` sizes, and one summary notice.
LaTeX substitutes the regular variants. They do not indicate another missing
semicolon. Those font and layout issues are outside this cleanup.

The full catalogues have not been recompiled in this operation; the verified
zero-semicolon result comes from the exhaustive affected-question builds.

## Subsequent SVG refresh

At the user's request, the documented renderer regenerated exactly the
19 affected German SVGs and updated their copies in `work/drawing_svg_review/de/`.
All metadata and human review states remain byte-for-byte unchanged. The
French and Italian sites continue to use German fallback for these drawings.
No PDFs, site releases or published review exports were regenerated.

All 19 drawing compilations succeeded. A second run skipped all 19 SVGs as
up to date, with zero failures. The canonical model has zero errors and zero
warnings. Source/output SHA-256 values, dimensions, the exact command and
the successful second-run report are in [the SVG audit](svg-refresh.audit.json).

Regeneration is not byte-identical to the older SVGs: Cairo rewrites paths and
identifiers, and autoscaling produces small width changes, at most **1.47 mm**
in this set. No text, diagram component or review decision was deliberately
changed. The pixel-identical PDF checks above concern the semicolon cleanup
itself; they must not be presented as a comparison of the old and regenerated
SVGs. SVG `pt` units are 1/72 inch, unlike TeX points (1/72.27 inch).

To repeat the scoped freshness check from the orchestrator (writes only selected
canonical SVGs/metadata if needed, render reports and local review copies):

```bash
pushd 50ohm-contents-ch >/dev/null
mapfile -t drawing_refs < <(uv run --locked python -c \
  'import json; from pathlib import Path; a=json.loads(Path("review/drawing_localization/2026-10-25/semicolon-cleanup.audit.json").read_text()); print("\n".join(str(Path(e["file"]).parent) for e in a["changed_files"]))')
render_args=(--language de --skip-existing)
for drawing_ref in "${drawing_refs[@]}"; do
  render_args+=(--canonical-ref "$drawing_ref")
done
uv run --locked python tools/render_localized_drawing_svgs.py "${render_args[@]}" \
  --report-json "$PWD/work/drawing_text_audit/semicolon-cleanup-20261025.render.json" \
  --log-file "$PWD/work/drawing_text_audit/semicolon-cleanup-20261025.render.log"
popd >/dev/null
```

Use absolute paths for custom `--log-file`/`--report-json` values: the current
renderer attempts to express the log path relative to the absolute repository
root when writing its final report. The first run's relative log argument
caused reporting to fail after all 19 SVGs had rendered successfully; the
absolute-path rerun verified freshness and wrote the successful report.
