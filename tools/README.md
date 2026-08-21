# Content Model Tools

## Current Tool

### Build the validation SQLite database and full inventory

```bash
python3 tools/build_content_model_db.py
```

Default outputs:

- `work/global_model/content_model.sqlite`
- `work/global_model/object_inventory.json`
- `work/global_model/summary.json`

This tool:

- inventories all current `contents/` objects
- inventories all `toc/*.json` structure nodes
- imports current question-catalog data for validation joins
- keeps metadata separate from text payloads
- parses inline references and annotations
- writes a SQLite database for validation and inspection

The database also preserves every source artifact under `contents/`, `toc/`,
`latex/` and `src/`, plus the repository-level `README.md` and `LICENSE`.
These files are stored byte-for-byte so that source-compatible exports do not
rely on the working tree.

### Recreate and compare the current site-content tree

```bash
python3 tools/export_site_content_from_db.py
```

This recreates `work/site-content/` solely from `source_artifact` records in
the SQLite database. It compares SHA-256 checksums with the current source
tree and writes its report to `work/global_model/site_content_comparison.json`.

### Compare a German generator build from source and reconstruction

```bash
python3 tools/validate_generator_reconstruction.py
```

If the execution environment limits a long-running command, the same
validation can be run in three persistent steps:

```bash
python3 tools/validate_generator_reconstruction.py --step source
python3 tools/validate_generator_reconstruction.py --step reconstructed
python3 tools/validate_generator_reconstruction.py --step compare
```

### Export and validate the canonical Git model

```bash
python3 tools/export_canonical_model.py
python3 tools/ensure_canonical_multilingual.py
python3 tools/build_db_from_canonical_model.py
python3 tools/compare_model_databases.py
```

`canonical/` separates business identity, text payloads, metadata, structure,
relations, review states, and source artifacts. The final comparison checks
every modeled SQLite row and the SHA-256 of every binary artifact payload.

`ensure_canonical_multilingual.py` makes the Git model explicitly
multilingual for all non-question objects and curriculum nodes. Missing `fr`
and `it` payloads are initialized from `de` as operational fallbacks; question
objects remain federated from `../50ohm-question-pool`.

Current transitional state:

- `50ohm-question-pool` remains the authoritative home of questions;
- `canonical/` may still contain mirrored question objects with the same ids;
- this mirror is tolerated for now as a repository-history artifact, not as a
  second canonical authority.

### Build de/fr/it from canonical SQLite and federated questions

```bash
python3 tools/run_multilingual_canonical_build.py
```

By default this orchestration uses a fixed generator seed (`50`) so repeated
validation builds remain comparable even when the site generator shuffles
embedded question answers.

To override that seed explicitly:

```bash
python3 tools/run_multilingual_canonical_build.py --generator-seed 123
```

This command imports `canonical/` into `work/canonical_model/content_model.sqlite`,
stages three generator inputs under `work/generator-input/{de,fr,it}`, injects
question catalogs from `../50ohm-question-pool/builds/{language}/`, runs the
generator into `work/build/{de,fr,it}`, mirrors each successful build into
`../sites/app/build/{de,fr,it}` for local review, and writes a comparison report to a
run-specific directory under `work/validation/multilingual/runs/<run-id>/`.

Generator-owned multilingual UI content is now consumed directly from
`generator_extra_content/{de,fr,it}/` by `translator/50ohm-generator/`. The build no longer
applies a post-build HTML patch layer for the migrated `fr` and `it` UI
families. German fallback strings may still remain inside the generator as
technical defaults, but they are no longer the intended multilingual source
for those migrated families.

The SQLite database is runtime-only. It is deleted and rebuilt from the Git
canonical model at the start of each run; no previous SQLite state is read or
merged.

This rebuild principle is strict. The SQLite database is an operational
intermediate only and must never be treated as a previous-version store.

Current optimization:

- if `canonical/` is Git-clean,
- and `work/canonical_model/content_model.sqlite` already exists,
- and `work/canonical_model/content_model.state.json` matches both the current
  Git tree hash of `canonical/` and the current importer-tool signature,

then the validator reuses the existing SQLite database instead of rebuilding
it.

If any of these conditions fail, the database is recreated from `canonical/`.

Concurrency model:

- the SQLite cache is shared across runs;
- a rebuild lock is taken only when the cache must actually be recreated;
- each language takes its own lock for staging and generation, so two runs for
  the same language cannot collide in `work/generator-input/<lang>` or
  `work/build/<lang>`;
- validation logs and reports are isolated per run under
  `work/validation/multilingual/runs/<run-id>/`.

The validator clears and recreates `translator/sites/app/build/de/` from the
V4 baseline `translator/site-original/app/50ohm-contents-ch/`, then clears and
recreates `work/build/de/` from `work/site-content/`. Before the latter build,
it overlays the V4 `contents/questions/` directory unchanged into
`work/generator-input/de/`; this deliberately holds the separate question
module constant while content reconstruction is validated. The comparison phase
also excludes `contents/questions/` entirely. Each build runs
from a private copy of the generator, so it never changes the shared generator
configuration. It captures both logs and compares the generated trees by path
and SHA-256 checksum. Its reports are stored in
`work/validation/generator-de/`.

Portability note:

- `translator/site-original/` is not recreated by the workspace bootstrap;
- workflows that compare against the original source snapshot still require it
  to exist locally;
- missing `translator/site-original/...` on a fresh machine is therefore a
  setup limitation, not a canonical-model corruption.

### Extract visible-text candidates from drawing TeX assets

```bash
python tools/extract_drawing_tex_translation_candidates.py
```

This command scans `canonical/drawings/*/*.de.tex` and writes:

- `work/drawing_text_audit/drawing_tex_translation_candidates.csv`

Current extraction scope:

- `node[...] { ... }`
- `node[...](){ ... }`
- `\node[...] { ... }`
- `\node[...](){ ... }`
- `\pgftext{ ... }`
- `\pgftext[<options>]{ ... }`

Important limitation:

- the output is a candidate list of visible text fragments;
- it is not a perfect German detector;
- manual review is still required before creating localized `*.fr.tex`,
  `*.it.tex`, and later `*.fr.svg`, `*.it.svg`.

### Build drawing-text review files from the filtered candidate CSV

```bash
python tools/build_drawing_tex_translation_review_files.py
```

This command reads:

- `work/drawing_text_audit/drawing_tex_translation_candidates_2.csv`
- `../50ohm-ai-translation-glossary/glossary.yml`

and regenerates:

- `work/drawing_text_audit/drawing_tex_translation_unique_from_filter.csv`
- `work/drawing_text_audit/drawing_tex_translation_unique_working_with_suggestions.csv`
- `work/drawing_text_audit/drawing_tex_translation_simple_actions.csv`
- `work/drawing_text_audit/drawing_tex_glossary_proposals_from_filter.csv`
- `work/drawing_text_audit/drawing_tex_translation_manual_residual.csv`

Glossary lookup is performed against the real glossary structure:

- top-level key `terms`
- source text in `source_term`
- translations in `translations.<lang>.term`

This avoids treating already-glossarized drawing terms as unresolved manual
items.

### Export special split-word drawing cases for separate review

```bash
python tools/export_drawing_tex_special_compounds.py
```

This writes:

- `work/drawing_text_audit/drawing_tex_special_compounds_review.csv`

It groups two-line compounds such as `Antennen-` + `tuner` so they can be
reviewed and line-broken explicitly in the target language.

### Import accepted drawing review rows, excluding special compounds

```bash
python tools/import_drawing_tex_translation_review.py
```

This reads:

- `work/drawing_text_audit/drawing_tex_translation_review_consolidated.csv`
- `work/drawing_text_audit/drawing_tex_special_compounds_review.csv`

and writes only accepted non-special rows to:

- `work/drawing_text_audit/drawing_tex_translation_imported_ok.csv`
- `work/drawing_text_audit/drawing_tex_translation_imported_ok.json`

### Import reviewed drawing translations and generate localized TeX files

```bash
python tools/import_drawing_tex_translations.py
```

This reads:

- `work/drawing_text_audit/drawing_tex_translation_candidates_2.csv`
- `work/drawing_text_audit/drawing_tex_translation_imported_ok.csv`
- `work/drawing_text_audit/drawing_tex_special_compounds_review.csv`

and generates `*.fr.tex` and `*.it.tex` beside the existing `*.de.tex` files,
while updating the touched drawing `object.meta.json` files to declare the new
language-specific TeX assets.

### Render localized drawing SVG files from localized TeX files

```bash
python tools/render_localized_drawing_svgs.py --from-import-report
```

This renders `*.fr.svg` and `*.it.svg` from the available `*.fr.tex` and
`*.it.tex` files, updates the touched drawing `object.meta.json` files to
declare the language-specific SVG assets, and copies the generated SVG files
into:

- `work/drawing_svg_review/fr/`
- `work/drawing_svg_review/it/`

Pass `--language de --language fr --language it` to render all three language
variants. Without explicit `--language` options, the localization default
remains FR and IT.

Behavior note:

- if the target localized SVG does not exist, it is rendered;
- each image reports `START`, then `OK` or `FAIL`; up-to-date images report
  `SKIP`, with output flushed immediately to the terminal;
- if the localized `.tex` file is newer than the existing `.svg`, it is
  rendered again;
- `--skip-existing` now skips only SVG files that already exist and are at
  least as recent as their corresponding localized `.tex` file;
- rendering continues after per-file failures instead of aborting the whole
  run;
- a short JSON summary is written to
  `work/drawing_text_audit/drawing_svg_render_report.json`;
- a detailed text log is written to
  `work/drawing_text_audit/drawing_svg_render.log`.

System dependencies required on the workstation:

- `latexmk`
- `lualatex`
- `pdftocairo`

Repository-local support files also required:

- `latex_deleted/FiftyOhm.cls`
- `latex_deleted/DARC-ausbildungsmaterialien.sty`
- `latex_deleted/settings.tex`
- `latex_deleted/settings-pre.tex`

The generated review copies are not authoritative canonical data. They exist
only to support the visual audit of remaining untranslated or incorrectly
localized drawing labels after SVG rendering.

### Validate localized drawing TeX files against the import contract

```bash
python tools/validate_localized_drawing_tex_structure.py
```

This validator rebuilds the expected `.fr.tex` and `.it.tex` files from the
German `.de.tex` sources by reusing the exact import logic from
`tools/import_drawing_tex_translations.py`, then compares the expected content
with the localized files present in `canonical/drawings/`.

It is intentionally stricter and more reliable than the previous heuristic
token-count check:

- it validates the exact import contract;
- it avoids false positives caused by compact translated labels such as `H2`,
  `H3`, `H4`, or `r~=~${1}:{7}$`;
- it only expects localized files for drawings that are actually touched by the
  reviewed translation import.
- it ignores a final trailing newline difference, because that is only a file
  serialization detail and not a TeX-content divergence.

It reads:

- `work/drawing_text_audit/drawing_tex_translation_candidates_2.csv`
- `work/drawing_text_audit/drawing_tex_translation_imported_ok.csv`
- `work/drawing_text_audit/drawing_tex_special_compounds_review.csv`

and writes:

- `work/drawing_text_audit/localized_tex_structure_validation.json`

### Review localized drawing SVG files in the browser

```bash
python tools/serve_drawing_svg_review.py
```

Open `http://127.0.0.1:8765/`. The read-only interface discovers drawing stems
available in all three `work/drawing_svg_review/{de,fr,it}/` directories and
shows the three SVG variants together. Navigation is available through the
previous/next buttons, the drawing selector, and the left/right arrow keys.
The URL hash preserves the current drawing, and zoom is synchronized across
the three panels.

Run its desktop and mobile browser checks with:

```bash
npm install
npx playwright install chromium
npm run test:drawing-review
```

On a new Ubuntu workstation, Playwright may first require:

```bash
sudo env PATH="$PATH" npx playwright install-deps chromium
```

## Related Compatibility Tool

The current review-site compatibility export for question catalogs is **not**
in this repository. It currently lives in:

- `../50ohm-question-pool/tools/export_generator_review_catalog.py`

Its role is to re-inject:

- `HB.rationale`
- top-level `pruned`

into a cleaned build catalog for the current review generator.
