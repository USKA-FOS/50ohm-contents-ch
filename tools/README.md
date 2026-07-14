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
generator into `work/build/{de,fr,it}`, and writes a comparison report to a
run-specific directory under `work/validation/multilingual/runs/<run-id>/`.

Generator-owned multilingual UI content is now consumed directly from
`generator_extra_content/{de,fr,it}/` by `translator/50ohm-generator/`. The build no longer
applies a post-build HTML patch layer for `fr` and `it`.

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

## Related Compatibility Tool

The current review-site compatibility export for question catalogs is **not**
in this repository. It currently lives in:

- `../50ohm-question-pool/tools/export_generator_review_catalog.py`

Its role is to re-inject:

- `HB.rationale`
- top-level `pruned`

into a cleaned build catalog for the current review generator.
