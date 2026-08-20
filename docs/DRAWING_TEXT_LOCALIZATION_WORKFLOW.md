# Drawing Text Localization Workflow

This document describes the current workflow for localizing text embedded in
canonical drawing TeX assets.

## 1. Scope

Some drawing objects contain user-visible text inside `*.de.tex` files. The
site generator does not render TeX directly. It only consumes already-produced
SVG assets. Therefore, localized drawing text requires a dedicated workflow:

1. identify visible-text candidates in `*.de.tex`;
2. review which candidates are truly translatable business text;
3. create `*.fr.tex` and `*.it.tex` for validated cases;
4. regenerate `*.fr.svg` and `*.it.svg`;
5. declare localized TeX and SVG assets in the drawing object metadata;
6. let the generator resolve `.<lang>.svg` first, with German fallback.

The workflow is now implemented end to end up to SVG regeneration. A final
visual audit is still required because some rendered labels may remain in
German when they were filtered out, missing from the glossary, or split across
multiple TeX fragments.

## 2. Current Candidate CSV

The current extraction tool writes:

- `work/drawing_text_audit/drawing_tex_translation_candidates.csv`

Current columns:

- `canonical_reference`
- `figure_number`
- `index`
- `raw_tex_fragment`
- `format_commands`
- `protected_tokens`
- `translatable_text`
- `category`
- `to_be_translated`

Column meaning:

- `canonical_reference`: canonical drawing directory, for example
  `canonical/drawings/dr_d7c37c317051`
- `figure_number`: drawing business identifier, for example `1017`
- `index`: running index within the drawing
- `raw_tex_fragment`: original extracted TeX text fragment, kept for exact
  reinjection later
- `format_commands`: JSON list of leading formatting commands preserved outside
  translation
- `protected_tokens`: JSON list of protected technical macros or math tokens
  preserved outside translation
- `translatable_text`: human-readable text that should be reviewed and, when
  appropriate, translated
- `category`: extraction syntax family
- `to_be_translated`: default review value, initialized to `true`

Important limitation:

- this CSV is a visible-text candidate list, not a perfect German-language
  detector;
- some visible labels may be symbols, technical markers, non-German text, or
  labels that should remain unchanged;
- every row still requires review before translation.

## 2.1 Review Files Built From the Filtered CSV

After the editorial `to_be_translated` filtering is maintained in:

- `work/drawing_text_audit/drawing_tex_translation_candidates_2.csv`

the review helper regenerates the derived files by combining that filter with
the active glossary:

```bash
python tools/build_drawing_tex_translation_review_files.py
```

Inputs:

- filtered candidate CSV:
  `work/drawing_text_audit/drawing_tex_translation_candidates_2.csv`
- glossary:
  `../50ohm-ai-translation-glossary/glossary.yml`

Glossary lookup uses the actual glossary model:

- top-level list: `terms`
- source key: `source_term`
- translated labels: `translations.fr.term`, `translations.it.term`

Derived outputs:

- `drawing_tex_translation_unique_from_filter.csv`
- `drawing_tex_translation_unique_working_with_suggestions.csv`
- `drawing_tex_translation_simple_actions.csv`
- `drawing_tex_glossary_proposals_from_filter.csv`
- `drawing_tex_translation_manual_residual.csv`

This split is intentional:

- `simple_actions` contains exact glossary hits and low-risk mechanical cases;
- `glossary_proposals` isolates recurring labels worth promoting into the glossary;
- `manual_residual` is the real reviewer worklist after glossary resolution.

## 2.2 Review Import and Localized Asset Generation

After reviewer validation:

1. accepted non-special rows are extracted from
   `drawing_tex_translation_review_consolidated.csv`;
2. reviewed translations are reinjected into the canonical drawing objects;
3. localized `*.fr.tex` and `*.it.tex` files are created beside `*.de.tex`;
4. localized `*.fr.svg` and `*.it.svg` are rendered from those TeX files;
5. touched `object.meta.json` files are updated so the generator can resolve
   language-specific drawing assets.

Working files used by the import/render phase:

- `work/drawing_text_audit/drawing_tex_translation_review_consolidated.csv`
- `work/drawing_text_audit/drawing_tex_special_compounds_review.csv`
- `work/drawing_text_audit/drawing_tex_translation_imported_ok.csv`
- `work/drawing_text_audit/drawing_tex_translation_imported_ok.json`
- `work/drawing_text_audit/drawing_tex_translation_import_report.json`
- `work/drawing_svg_review/fr/`
- `work/drawing_svg_review/it/`

Canonical outputs created by this phase:

- `canonical/drawings/*/*.fr.tex`
- `canonical/drawings/*/*.it.tex`
- `canonical/drawings/*/*.fr.svg`
- `canonical/drawings/*/*.it.svg`
- updated `canonical/drawings/*/object.meta.json`

## 3. Syntaxes Currently Extracted

The current extraction is intentionally conservative and only targets syntax
families that usually render visible text in TikZ/PGF:

### 3.1 `node_text`

This category is extracted from text groups attached to TikZ nodes, including:

- `node[...] { ... }`
- `node[...](){ ... }`
- `\node[...] { ... }`
- `\node[...](){ ... }`

Examples:

```tex
\draw[DARCblue](top2.north) node[anchor=south] {Inversionsschicht};
\draw(foo.center) node[anchor=south east](){Anode};
\node[above] {\small LR41 \qty{1.5}{\volt}};
```

When present, the extractor currently treats these commands as leading format
commands rather than as text to translate:

- `\bfseries`
- `\mdseries`
- `\itshape`
- `\slshape`
- `\upshape`
- `\scshape`
- `\rmfamily`
- `\sffamily`
- `\ttfamily`
- `\tiny`
- `\scriptsize`
- `\footnotesize`
- `\small`
- `\normalsize`
- `\large`
- `\Large`
- `\LARGE`
- `\huge`
- `\Huge`
- `\centering`

Protected non-translatable technical tokens currently include:

- `\includegraphics[...] {...}`
- `\qty{...}{...}`
- `\SI{...}{...}`
- `\unit{...}`
- `\num{...}`
- unit and magnitude macros such as `\volt`, `\ohm`, `\percent`
- math fragments delimited by `$...$`

### 3.2 `pgftext_text`

This category is extracted from PGF text placement commands:

- `\pgftext{ ... }`
- `\pgftext[<options>]{ ... }`

Example:

```tex
\pgftext[x=0.45\pgf@circ@res@left]{\ctikzvalof{bipoles/twoport/text}}
```

## 4. What Is Explicitly Not Treated As Authoritative Text Yet

The current candidate extractor does not attempt to interpret or translate:

- arbitrary trailing brace groups in unrelated TeX commands;
- math expressions as such;
- style arguments, coordinates, or node identifiers;
- macro definitions;
- labels inferred indirectly through custom macros.

Those cases must be reviewed separately if later evidence shows that they
produce user-visible translatable text.

## 5. Review Rule

When a row is ambiguous:

- do not translate automatically;
- inspect the generated image visually;
- decide manually whether the candidate is:
  - visible business text to translate;
  - visible but not to translate;
  - not actually the intended visible business text.

The extractor may therefore over-report some labels on purpose. Missing visible
business text is considered worse than presenting a few false positives for
review.

## 6. Render and Audit Commands

Render localized SVG assets from the import report:

```bash
python tools/render_localized_drawing_svgs.py --from-import-report
```

Required workstation tools:

- `latexmk`
- `lualatex`
- `pdftocairo`

Required repository support files:

- `latex_deleted/FiftyOhm.cls`
- `latex_deleted/DARC-ausbildungsmaterialien.sty`
- `latex_deleted/settings.tex`
- `latex_deleted/settings-pre.tex`

The renderer also copies the generated SVG files to:

- `work/drawing_svg_review/fr/`
- `work/drawing_svg_review/it/`

These review directories are the expected input for the post-render audit.

## 7. Current Audit Rule

SVG generation success is not sufficient to declare the drawing localization
complete.

After each render run:

1. inspect the localized SVG review directories visually;
2. record remaining German labels or incorrectly translated labels;
3. decide whether the cause is:
   - missing glossary coverage;
   - a filtered candidate that should have been translated;
   - a multi-fragment compound that needs dedicated handling;
   - a deliberate fallback to German.

Examples already observed during the current audit cycle include figure `865`
(`Reflektion`, `Bodenwelle`) and figure `972` (`NF`).
