# Validation Log

## Source-Artifact Reconstruction

Decision: source-compatible reconstruction is validated from byte-preserved
artifacts in SQLite, not by reserializing parsed text or JSON values. This
avoids accidental formatting, whitespace, or binary-asset changes.

Procedure:

```bash
python3 tools/build_content_model_db.py
python3 tools/export_site_content_from_db.py
```

Result of the initial validation:

- `3,876` artifacts exported to `work/site-content/`
- `0` checksum mismatches
- coverage: `contents/`, `toc/`, `latex/`, `src/`, `README.md`, `LICENSE`

The generated comparison report is intentionally outside Git at:

- `work/global_model/site_content_comparison.json`

## TOC Semantic Import

Decision: TOC JSON is simultaneously retained as source bytes and modeled as
curriculum nodes. This makes its chapter and section hierarchy queryable while
keeping exact source reconstruction possible.

Validation compares every property of every JSON root, chapter, and section
against the imported node text, identifier, or metadata. The initial result is
zero missing or mismatched properties across all seven TOC files.

## German Review-Site Build

Procedure run from `translator/sites/app/generator`:

```bash
./build_local_review_site.sh de
```

Result: the generator produced `translator/sites/app/build/de/index.html` and
`4,165` generated files.

Important limitation: this command uses the independent configured input
`translator/sites/app/inputs/50ohm-contents-ch-de`, whose question catalog and
question metadata differ from the source currently imported into this
repository's SQLite database. The generator reports many unresolved question
references in that existing German input. These warnings do not indicate a
byte-level reconstruction mismatch; they are a pending question-pool and
metadata reconciliation task before an end-to-end build from the global model
can be considered clean.

## V4 Question-Input Rule For Reconstruction Comparison

The historical `contents/questions/fragenkatalog3b.json` in this repository is
not a valid V4 generator input. Generator comparisons instead use the two V4
interfaces from `translator/site-original/app/50ohm-contents-ch/`:

- `fragenkatalog_ch.json`
- `fragenkatalog_4pre.json`

They are currently byte-identical, but are retained as two distinct input
roles. For a reconstruction comparison, the V4 `contents/questions/` directory
is overlaid unchanged into the generated validation input. This keeps the
separately canonical question module out of scope while comparing the rest of
the content model.

## V4 Source Versus Reconstruction Result

The initial V4 comparison uses the staged V4 question input described above.
Both builds produce `4,165` files with identical path sets. Their generator
logs are identical after normalizing the non-deterministic `uv` package-install
duration.

Sixty slide HTML files differ byte-for-byte because the generator calls
`random.shuffle` without a seed when presenting answer choices. A semantic
comparison of every affected slide confirms zero differences in question text
or answer sets. This is generator nondeterminism, not a loss in the imported
content model.

## Canonical Git Round Trip

The canonical Git representation is generated into `canonical/` with separate
files for business identity, localized text, metadata, structure, relations,
review state and source artifacts. A new SQLite database is then created only
from that Git representation.

Initial result: all fourteen modeled tables are identical to the original
SQLite import, with no missing or changed row. This includes all `3,876`
source artifacts, whose binary payloads are compared by SHA-256.
