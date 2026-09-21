# Content Model Tools

## Python environment

Use Python 3.14, selected by the repository's `.python-version`. From the
repository root, install the locked Excel/YAML/template dependencies and pytest:

```bash
uv sync --locked
uv run --locked python -m pytest -q
```

Activate `.venv/bin/activate` before using bare `python` commands below.
Tests use temporary fixtures; they do not run a production site build or TeX
compilation. Preserve transferred `work/` data and human review inputs when
recreating an environment. The generator has its own Python 3.14 environment.

## Source Tree and Canonical Authority

`canonical/` is the authoritative model for the content represented by this
repository. The sibling directories `contents/`, `latex/`, `src/`, and `toc/`
are source and generator-support trees retained for synchronization,
comparison, and import workflows. They are not a second canonical model.

Changes made in one of these source trees must be reviewed and explicitly
imported into `canonical/` by the appropriate importer. No build or validation
tool may silently overwrite canonical objects from these directories. The
canonical tree is therefore the reference used for multilingual staging and
reproducible builds.

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

These commands cover initialization and model validation. In particular,
`export_canonical_model.py --replace-existing-canonical` must not be used to
refresh a multilingual canonical tree.

### Validate and incrementally import German `review/de/main`

```bash
git fetch origin review/de/main
python tools/validate_canonical_model.py
python tools/import_incremental_german_source.py
python tools/import_incremental_german_source.py \
  --review-workbook work/source_import_audits/german-source-import-review.xlsx \
  --apply
```

The first importer command is a dry-run. By default, the source is the local
`origin/review/de/main` commit, archived without changing the current branch. Apply
requires a clean `canonical/`, preserves ids and target payloads, marks changed
target states for review, deactivates missing objects as `to_be_deleted`, and
writes the accepted audit under `review/source_imports/`.

PNG, SVG and TeX changes are recorded as `media_review_required`; they
invalidate existing localized media variants. Image/SVG-only changes do so
without creating artificial text units.

Before the first controlled import, export an explicit review workbook:

```bash
python tools/export_german_source_import_review.py \
  --source-ref origin/review/de/main \
  --output work/source_import_audits/german-source-import-review.xlsx
```

This command is read-only for `canonical/`. It lists only objects whose source
content differs from the canonical content, plus new and missing objects. Each
row contains `new`, `updated`, or `deleted`, the affected source suffixes, the
source commit and a `decision` column. HTML candidates are initialized with
`to_be_imported`. Modified or deleted German `.tex` candidates require an
explicit decision; newly added `.tex` files are the exception and are
pre-initialized for import.

The workbook is the review boundary. Do not run the importer with `--apply`
until the workbook has been checked and the accepted workbook is recorded with
the import manifest. Every later campaign must use the previously accepted
source revision as its baseline; a dry-run must never silently redefine that
baseline.

When one German source update was applied in several import phases, combine
the accepted manifests before translating the target languages:

```bash
python tools/merge_german_source_import_audits.py \
  review/source_imports/german-source-import.0ebada583d.json \
  review/source_imports/german-source-import-remaining.json \
  --output review/source_imports/german-source-import-combined.json
```

The combined file is a translation scope only; it does not import anything.

Ambiguous renames, stale target HTML structure and missing complete editions
block apply. Questions are outside this importer’s scope.

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
uv run python tools/run_multilingual_canonical_build.py
```

By default this orchestration uses a fixed generator seed (`50`) so repeated
validation builds remain comparable even when the site generator shuffles
embedded question answers.

To override that seed explicitly:

```bash
uv run python tools/run_multilingual_canonical_build.py --generator-seed 123
```

### Build and promote a versioned site release

A release build requires all three languages, not entirely clean source
repositories: it reads canonical material and tools without rewriting them.
Canonical-writing imports still require clean canonical paths, regardless of
unrelated tool edits. The build records each source's commit, tags, dirty flag
and actual Git-visible worktree SHA-256 (excluding ignored artifacts), and
checks that this state has not changed during generation. Expected CLI failures
are reported as a short stderr message and exit code 1, without a traceback.
It cleans the
complete `work/build/` staging tree before generation, records the exact source
commits and exact-match tags, and writes per-language file counts and tree
digests to `work/build/release-manifest.json`:

```bash
uv run python tools/run_multilingual_canonical_build.py \
  --release-id beta-2026-09-13-01 \
  --beta
```

Add a release output to promote the validated result:

```bash
uv run python tools/run_multilingual_canonical_build.py \
  --release-id beta-2026-09-13-01 \
  --beta \
  --release-output ../50ohm-site-releases
```

`--release-output` must be the root of a Git repository and the release
tag must not already exist there. Promotion replaces only `de/`, `fr/`, `it/`,
and `release-manifest.json`, even if a previous build left them uncommitted.
There is no preliminary purge or temporary commit requirement for generated
sites. Promotion preserves `feedback/`, `drawing-review/`, `.git/`, and deployment
files. The generated artifacts are moved from `work/build/`, and the local
review links are redirected to their promoted locations. A failed build or
validation never changes the release repository.

The wrapper sets `generator_status: false` because its releases are built
offline and promoted atomically. This excludes the optional status widget and
its polling requests from release pages. Other wrappers are unaffected: the
generator default remains enabled when they omit this setting.

The feedback URL recorded in the manifest defaults to
`https://50ohm.jp2s.ch/feedback` and can be changed with `--feedback-url`.
Neither release mode nor promotion creates a Git commit, tag, or push. Those
remain explicit operator actions after inspection.

Release mode also passes `release_id`, `beta`, and `feedback_url` to the site
generator. Every generated regular page and Reveal.js presentation displays
the release id and feedback action. Beta releases additionally display the
localized warning and disclaimer. Development builds without `--release-id`
do not render these elements.

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
- generator subprocesses use `work/uv-cache/` unless `UV_CACHE_DIR` is already
  set, so builds do not depend on a writable user-level cache.

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

After an incremental German import, restrict the extraction to changed drawing
TeX listed by the accepted audit:

```bash
python tools/extract_drawing_tex_translation_candidates.py \
  --source-import-audit review/source_imports/<audit>.json
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
uv run python tools/import_drawing_tex_translations.py
```

This reads:

- `work/drawing_text_audit/drawing_tex_translation_candidates_2.csv`
- `work/drawing_text_audit/drawing_tex_translation_imported_ok.csv`
- `work/drawing_text_audit/drawing_tex_special_compounds_review.csv`

and generates `*.fr.tex` and `*.it.tex` beside the existing `*.de.tex` files,
while updating the touched drawing `object.meta.json` files to declare the new
language-specific TeX assets.

### Import the reviewed German-fallback drawing workbook

Dry-run validation:

```bash
python tools/import_fallback_drawing_text_review.py
```

Controlled canonical import:

```bash
python tools/import_fallback_drawing_text_review.py --apply
```

Only `decision=to_be_translated` rows are applied. `[[BR]]` inserts a line
break and `[[BR-]]` inserts a hyphen followed by a line break. The command
preserves the complete review worksheet as a tracked CSV and writes the
versioned audit under `review/drawing_localization/2026-09-14/`. It also
refreshes the working render report consumed by `--from-import-report`.

### Import the validated drawing feedback workbook

For the issue-based visual review workbook:

```bash
python tools/import_drawing_feedback_review.py
python tools/import_drawing_feedback_review.py --apply
```

The first command is a dry run. The second command applies only rows from the
`Translation review` sheet whose `decision` is `to_be_translated`. It preserves
existing localized TeX files and creates a localized file from the German
source only when that file does not exist. The import writes its audit to
`work/drawing_feedback_review_2026-09-16.import-audit.json`; unmatched source
terms are reported there and are not silently replaced.

For a subsequent review column, select it explicitly, for example:

```bash
python tools/import_drawing_feedback_review.py \
  --decision-column decision_2 \
  --audit work/drawing_feedback_review_2026-09-16.decision-2.import-audit.json
python tools/import_drawing_feedback_review.py \
  --decision-column decision_2 \
  --apply \
  --audit work/drawing_feedback_review_2026-09-16.decision-2.import-audit.json
```

This tool modifies only canonical `.fr.tex` and `.it.tex` files (and their
metadata). It never compiles TeX or generates SVG files; rendering is a
separate, explicitly launched operation.

### Render localized drawing SVG files from localized TeX files

```bash
uv run python tools/render_localized_drawing_svgs.py --from-import-report --skip-existing
```

This renders `*.fr.svg` and `*.it.svg` from the available `*.fr.tex` and
`*.it.tex` files and updates the touched drawing `object.meta.json` files to
declare the language-specific SVG assets. The renderer can also copy processed
files into the working review directory, but those incremental copies are not
a complete or authoritative review export.

- `work/drawing_svg_review/fr/`
- `work/drawing_svg_review/it/`

Pass `--language de --language fr --language it` to render all three language
variants. Without explicit `--language` options, the localization default
remains FR and IT.

Behavior note:

- if the target localized SVG does not exist, it is rendered;
- each image reports `START`, then `OK` or `FAIL`; up-to-date images report
  `SKIP`, with output flushed immediately to the terminal;
- if the localized `.tex` file or a referenced photo is more than one second
  newer than the existing `.svg`, it is rendered again;
- a width difference between the localized SVG and the German reference does
  not trigger rendering; width differences are a rendering-quality concern,
  not evidence that the input `.tex` changed;
- existing up-to-date SVGs are skipped by default; `--skip-existing` remains
  accepted for compatibility;
- `--force` explicitly recompiles existing selected SVGs;
- `--metadata-only --no-copy-review` repairs localized TeX/SVG asset metadata
  without invoking LaTeX, modifying SVGs, or refreshing review copies;
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

- `latex/FiftyOhm.cls`
- `latex/DARC-ausbildungsmaterialien.sty`
- `latex/settings.tex`
- `latex/settings-pre.tex`

The generated review copies are not authoritative canonical data. They exist
only to support the visual audit of remaining untranslated or incorrectly
localized drawing labels after SVG rendering.

### Validate localized drawing TeX files against the import contract

```bash
uv run python tools/validate_localized_drawing_tex_structure.py
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

Rebuild the complete review export before every review session:

```bash
python tools/prepare_drawing_svg_review.py
```

This command constructs a temporary export from canonical, validates that
every drawing has exactly one German SVG, and atomically replaces
`work/drawing_svg_review`. It removes stale files from previous sessions. The
export contains every German drawing and only the explicit French and Italian
variants that exist in canonical.

```bash
uv run python tools/serve_drawing_svg_review.py
```

Open `http://127.0.0.1:8765/`. The read-only interface lists every German SVG.
For FR and IT, it displays the localized SVG when present and otherwise falls
back to the German SVG with a visible `Fallback DE` marker. Navigation is
available through the previous/next buttons, the drawing selector, and the
left/right arrow keys. The URL hash preserves the current drawing, and zoom is
synchronized across the three panels. `Translated only` retains drawings with
explicit FR and IT SVGs. The feedback button carries the review ID, drawing
number, and canonical ID to the common feedback form.

The interface reads review copies only. After changing or rerendering canonical
SVGs, rerun `prepare_drawing_svg_review.py` before inspecting them. The
interface never writes canonical data or review decisions.

Create a self-contained public export only from a committed canonical state:

```bash
python tools/prepare_drawing_svg_review.py \
  --review-dir ../50ohm-site-releases/drawing-review \
  --require-clean-source
```

See `docs/DRAWING_REVIEW_DEPLOYMENT.md` for the manifest and server contract.

Export one row per candidate `[text, drawing]` tuple for drawings using the
German fallback:

```bash
python tools/export_fallback_drawing_text_review.py
```

The output is
`work/drawing_text_audit/fallback_drawing_german_text_review.xlsx`. Its first
two columns are `text` and `drawing_number`; candidates newly found by improved
TeX syntax coverage are explicitly identified for human validation.

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
