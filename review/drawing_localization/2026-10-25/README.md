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
ignored `tmp/drawing-semicolon-cleanup-20261025/`. The production PDF files,
their original logs, existing SVGs and site releases were not overwritten.
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
