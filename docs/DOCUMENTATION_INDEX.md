# Documentation Index

This file indexes the current documentation set for `50ohm-contents-ch`.

It states what each document is for and whether it is current reference,
contextual support, or a candidate for later cleanup.

## Reference Status

- `current reference`: should be used first
- `contextual`: may still be useful, but is not the primary source of truth
- `candidate for cleanup`: overlaps too much with newer references and should
  be reviewed later

## Current Documents

| Document | Role | Status |
| --- | --- | --- |
| [CANONICAL_DATA_MODEL_REFERENCE.md](./CANONICAL_DATA_MODEL_REFERENCE.md) | authoritative description of the current canonical Git model and SQLite counterpart | current reference |
| [CANONICAL_USE_CASES_AND_WORKFLOWS.md](./CANONICAL_USE_CASES_AND_WORKFLOWS.md) | authoritative description of current use cases and workflows | current reference |
| [DOCUMENTATION_INDEX.md](./DOCUMENTATION_INDEX.md) | entry point and status index for documentation | current reference |
| [GENERATOR_EXTRA_CONTENT_MIGRATION_REFERENCE.md](./GENERATOR_EXTRA_CONTENT_MIGRATION_REFERENCE.md) | reference for the temporary generator-owned multilingual content layer, its migration boundary, and what still remains inside the generator | current reference |
| [VALIDATION_LOG.md](./VALIDATION_LOG.md) | records validation findings, rules derived from validation, and operational validation evidence | contextual |
| [MAPPING_MATRIX.md](./MAPPING_MATRIX.md) | source-to-model mapping aid, especially for import coverage and marker families | contextual |
| [GLOBAL_CANONICAL_MODEL.md](./GLOBAL_CANONICAL_MODEL.md) | older broad conceptual note about the global model scope | candidate for cleanup |
| [OBJECT_CENTRIC_CANONICAL_MODEL.md](./OBJECT_CENTRIC_CANONICAL_MODEL.md) | older object-centric design note overlapping with the new data-model reference | candidate for cleanup |
| [OBJECT_CENTRIC_REDESIGN_STATUS_2026-07-12.md](./OBJECT_CENTRIC_REDESIGN_STATUS_2026-07-12.md) | point-in-time redesign status snapshot | contextual |

## Reading Order

For a new contributor:

1. read [CANONICAL_DATA_MODEL_REFERENCE.md](./CANONICAL_DATA_MODEL_REFERENCE.md)
2. read [CANONICAL_USE_CASES_AND_WORKFLOWS.md](./CANONICAL_USE_CASES_AND_WORKFLOWS.md)
3. read [GENERATOR_EXTRA_CONTENT_MIGRATION_REFERENCE.md](./GENERATOR_EXTRA_CONTENT_MIGRATION_REFERENCE.md) for generator-owned multilingual content outside canonical
4. use [VALIDATION_LOG.md](./VALIDATION_LOG.md) for evidence and constraints
5. use [MAPPING_MATRIX.md](./MAPPING_MATRIX.md) for detailed source mapping

## Maintenance Rule

When the canonical model changes:

- update `CANONICAL_DATA_MODEL_REFERENCE.md`
- update `CANONICAL_USE_CASES_AND_WORKFLOWS.md` if workflows or scope changed
- update `GENERATOR_EXTRA_CONTENT_MIGRATION_REFERENCE.md` if generator-owned multilingual resources or generation rules changed
- update this index if document status changed

Older overlapping documents may remain temporarily, but their status here must
reflect whether they are still authoritative.
