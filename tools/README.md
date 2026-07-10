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

### Build de/fr/it from canonical SQLite and federated questions

```bash
python3 tools/run_multilingual_canonical_build.py
```

This command imports `canonical/` into `work/canonical_model/content_model.sqlite`,
stages three generator inputs under `work/generator-input/{de,fr,it}`, injects
question catalogs from `../50ohm-question-pool/builds/{language}/`, runs the
generator into `work/build/{de,fr,it}`, and writes a comparison report to
`work/validation/multilingual/summary.json`.

The SQLite database is runtime-only. It is deleted and rebuilt from the Git
canonical model at the start of each run; no previous SQLite state is read or
merged.

The validator clears and recreates `translator/sites/app/build/de/` from the
V4 baseline `translator/site-original/app/50ohm-contents-ch/`, then clears and
recreates `work/build/de/` from `work/site-content/`. Before the latter build,
it overlays the V4 `contents/questions/` directory unchanged into
`work/generator-input/de/`; this deliberately holds the separate question
module constant while content reconstruction is validated. Each build runs
from a private copy of the generator, so it never changes the shared generator
configuration. It captures both logs and compares the generated trees by path
and SHA-256 checksum. Its reports are stored in
`work/validation/generator-de/`.

## Related Compatibility Tool

The current review-site compatibility export for question catalogs is **not**
in this repository. It currently lives in:

- `../50ohm-question-pool/tools/export_generator_review_catalog.py`

Its role is to re-inject:

- `HB.rationale`
- top-level `pruned`

into a cleaned build catalog for the current review generator.
