# Canonical language inventory

`object.meta.json.languages` lists the languages declared by an object's text
payloads and media variants. It is an inventory, not proof of a complete
translation or human approval. Revision statuses remain independent.

`tools/canonical_language_metadata.py` supplies `present_languages(meta)` and
`sync_languages(meta)`. The latter adds all languages from
`text_slots[].storage.files` and `language_variants`, preserves existing explicit
declarations, and orders DE/FR/IT before any other languages. It does not scan
arbitrary filenames, fabricate a localized variant from a German fallback,
rewrite payloads or approve a review state. File existence is verified by the
canonical model validator.

The canonical exporter, incremental German importer, reviewed drawing-TeX
import, drawing-feedback import and localized SVG renderer synchronize the
inventory before saving metadata. The fallback drawing importer uses the same
TeX metadata updater. The independent translation engine also merges existing
text and media declarations when importing a translated text field.

## Repair of 24 October 2026

The 29 `asset language absent from languages list` warnings concerned 16
objects. The accepted repair added only missing language declarations:

- 13 drawings gained FR and IT declarations;
- drawing 1041 gained DE;
- photos 160 and 331 gained DE.

All referenced media existed before the repair. Payloads and review states were
preserved. The exact before/after metadata and hashes are recorded in
[`languages-inventory-sync.plan.json`](../review/metadata/2026-10-24/languages-inventory-sync.plan.json).
The plan was validated in memory against the current canonical files before
writing. The applied receipt is
[`languages-inventory-sync.applied.json`](../review/metadata/2026-10-24/languages-inventory-sync.applied.json).
The full model validates with **zero errors and zero warnings** afterwards.

Earlier quotation-review CSVs and the warning explanation are historical
snapshots; they are not overwritten by this repair.

## Verification

From the orchestrator, read-only validation of canonical data:

```bash
pushd 50ohm-contents-ch >/dev/null
uv run --locked python tools/validate_canonical_model.py
popd >/dev/null
```

Regression tests check media-only export and the metadata writers. All test
artifacts, including Python temporary directories, stay under the orchestrator's
ignored `tmp/` directory:

```bash
mkdir -p tmp
check_dir=$(mktemp -d "$PWD/tmp/language-quote-check.XXXXXX")
pushd 50ohm-contents-ch >/dev/null
env TMPDIR="$check_dir" UV_CACHE_DIR="$check_dir/uv-cache" \
  uv run --locked --no-sync python -m pytest \
  tests/test_canonical_language_metadata.py \
  tests/test_incremental_german_source_import.py \
  tests/test_drawing_tex_localization.py \
  --basetemp="$check_dir/content" -q
popd >/dev/null
```

This test command writes disposable fixtures only; it does not change canonical
data or generate sites, PDFs, TeX images or AI translations.
