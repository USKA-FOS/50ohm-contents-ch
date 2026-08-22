# Drawing Localization Handover

This document is a short operational handover for the current drawing
localization work. It complements, but does not replace,
`docs/DRAWING_TEXT_LOCALIZATION_WORKFLOW.md`.

## 1. Objective

Localize German drawing text from canonical `*.de.tex` assets into French and
Italian by:

- extracting visible translatable labels;
- validating what must actually be translated;
- creating `*.fr.tex` and `*.it.tex`;
- rendering `*.fr.svg` and `*.it.svg`;
- wiring those localized assets in `object.meta.json` so the generator can use
  them with German fallback.

## 2. Current State

As of 2026-08-22:

- import scope: `174` drawing objects
- localized TeX present:
  - `174` `*.fr.tex`
  - `174` `*.it.tex`
- localized SVG present:
  - `174` `*.fr.svg`
  - `174` `*.it.svg`
- German SVG review export:
  - `work/drawing_svg_review/de/`
- trilingual browser review:
  - `uv run python tools/serve_drawing_svg_review.py`
  - `http://127.0.0.1:8765/`
- visual review status:
  - all 174 localized drawings reviewed and approved;
- multilingual site build status:
  - DE, FR, and IT each contain the same 4,165-file output set;
  - no drawing asset is missing from FR or IT.

The current session snapshot is also recorded in:

- `work/drawing_text_audit/session_state_2026-08-21.md`

## 3. What Is Already Stable

- canonical localized drawing TeX import exists end to end;
- localized SVG rendering exists end to end;
- generator metadata was extended so localized drawing assets can be declared
  per language;
- the SVG renderer now:
  - rerenders when `.tex` is newer than `.svg`;
  - can continue after per-file failures;
  - reports every image to the terminal;
  - supports metadata-only repair without rendering;
  - writes a short JSON report and a detailed log.
- the browser review tool now displays DE, FR, and IT simultaneously with
  direct selection, previous/next navigation, keyboard navigation, and
  synchronized zoom.

## 4. Important Rules Already Validated

### 4.1 Text review must be done from TeX, not from SVG strings

Rendered SVG labels are converted into vector glyph paths, not stored as SVG
`<text>` nodes. Therefore:

- SVG is suitable for visual inspection only;
- string-level text checks must be done from `*.de.tex`, `*.fr.tex`,
  `*.it.tex`.

### 4.2 Non-translatable terms must not be “invented” per case

If a label should stay unchanged across languages, or if a technical term needs
consistent multilingual handling, the correct path is:

1. add or update the glossary entry;
2. rebuild the drawing review files;
3. regenerate localized TeX from approved inputs.

Do not introduce ad hoc per-file exceptions when the term is glossary-worthy.

### 4.3 Structural equality of localized TeX matters

Localized `*.fr.tex` and `*.it.tex` should remain structurally identical to
the German source except for validated text substitutions. Reordering or manual
rewrites are not acceptable unless explicitly validated.

## 5. Known Special Cases

### 5.1 Split labels

Some German labels are split across lines or TeX fragments, for example:

- hyphenated word halves across lines;
- labels visually composed from multiple nodes;
- mixed formatting commands plus text fragments.

Those cases are not safe for blind automatic translation and must be reviewed
with the dedicated review CSV files.

### 5.2 Embedded photo references inside drawings

Some drawing TeX files reference external photo assets. If those references are
missing or inconsistent, SVG rendering can fail.

A documented example exists here:

- `work/drawing_text_audit/source_reference_fix_689_photo_mapping_2026-08-21.md`

That note must be treated as a case-specific correction record, not as proof of
a general historical renumbering rule.

### 5.3 Residual German text

Even after import and rendering, some localized drawings may still show German
because:

- the label was excluded by the filter;
- the label was missing from the glossary;
- the label belongs to a split/special compound case;
- the localized SVG was not rendered yet;
- the drawing still falls back to the German asset.

## 6. Files That Matter Most

Primary workflow and rules:

- `docs/DRAWING_TEXT_LOCALIZATION_WORKFLOW.md`

Current state:

- `work/drawing_text_audit/session_state_2026-08-21.md`

Important audit/review inputs:

- `work/drawing_text_audit/drawing_tex_translation_candidates_2.csv`
- `work/drawing_text_audit/drawing_tex_translation_review_consolidated.csv`
- `work/drawing_text_audit/drawing_tex_special_compounds_review.csv`
- `work/drawing_text_audit/drawing_tex_translation_manual_residual.csv`
- `work/drawing_text_audit/localized_tex_structure_validation.json`
- `work/drawing_text_audit/drawing_svg_render_report.json`
- `work/drawing_text_audit/drawing_svg_render.log`

Visual SVG review export:

- `work/drawing_svg_review/de/`
- `work/drawing_svg_review/fr/`
- `work/drawing_svg_review/it/`

## 7. Expected Next Steps

The reviewed drawing set is complete. The next operational sequence is:

1. commit and push canonical assets, metadata, tools, and documentation;
2. publish the rebuilt DE, FR, and IT sites;
3. inspect the deployed sites for integration defects outside the drawing-only
   review interface;
4. route any later drawing correction through the same extract, import, render,
   review, and rebuild workflow.

## 8. What A New Agent Must Not Assume

- `174` is the localized working subset, not the total number of German
  drawings in canonical;
- exported German SVGs do not expose their text as searchable SVG text nodes;
- a rendering failure does not necessarily mean the translation is wrong;
- a visually unchanged label is not automatically an error: it may be a valid
  non-translated technical term;
- any case-specific source-reference fix must be documented separately when it
  changes canonical source relationships.
