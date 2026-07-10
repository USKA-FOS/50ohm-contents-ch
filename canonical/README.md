# Canonical Git Model

This directory is the generated canonical Git representation validated against
the current source import. It is now suitable for inspection and round-trip
validation; its adoption as the repository's operational source of truth still
requires an explicit migration decision.

The model is deliberately split by revision concern:

```text
canonical/
  objects/<object-type>/<nanoid>.json
  structure/
  texts/payload/<localized-text-nanoid>.txt
  texts/slots/<slot-nanoid>.json
  texts/nodes/<node-text-nanoid>.json
  metadata/objects/<object-nanoid>.json
  metadata/nodes/<node-nanoid>.json
  metadata/artifacts/<artifact-nanoid>.json
  relations/references/<object-nanoid>.json
  relations/annotations/<object-nanoid>.json
  review/<subject-kind>/<subject-nanoid>.json
  artifacts/<original-source-path>
```

Semantics:

- `objects/`
  - stable business identities and object type only
- `structure/`
  - TOC-like nodes and content placements
- `texts/`
  - localized payloads stored separately from every metadata file
- `metadata/`
  - source traceability, legacy identifiers, presentation metadata and artifact checksums
- `review/`
  - general and language-specific review state
- `relations/`
  - inline references and non-text annotations
- `artifacts/`
  - byte-exact source files used for site-compatible reconstruction

## Multilingual Rule

All non-question content objects and curriculum nodes must carry explicit
`de`, `fr`, and `it` text entries in the Git model. Until reviewed
translations exist, `fr` and `it` entries may intentionally point to payloads
initialized from `de`; that fallback is visible in Git and importable into
SQLite.

Questions are excluded from this content model rule. They are federated from
the canonical question-pool repository:

```text
../50ohm-question-pool/builds/{de,fr,it}/question_pool_rev0_ch-{language}.json
```

## Round-Trip Validation

The following commands are the canonical-model round trip:

```bash
python3 tools/export_canonical_model.py
python3 tools/ensure_canonical_multilingual.py
python3 tools/build_db_from_canonical_model.py
python3 tools/compare_model_databases.py
```

The initial round trip is exact for all tables and artifact payload hashes.
The generated comparison report is outside Git at
`work/canonical_model/comparison.json`.

SQLite files under `work/` are operational caches only. They must always be
rebuilt from this Git model and must never become a versioned source of truth
or an incremental state store.
