# Object-Centric Redesign Status 2026-07-12

## Scope of This Intermediate State

This commit captures the transition from the previous canonical layout to the
new object-centric canonical Git model.

It is intentionally an intermediate checkpoint:

- the old canonical layout is removed;
- the new object-centric canonical layout is generated in `canonical/`;
- reconstruction support artifacts are no longer stored inside `canonical/`;
- reconstruction usage is now logged so remaining support dependencies can be
  eliminated in later steps.

## Branch

- `design/object-centric-canonical`

## Decisions Already Applied

1. Canonical Git is business-object centric.
2. SQLite is an operational working database, not the editorial source of truth.
3. Fresh ids are used; no legacy ids are preserved in the new model.
4. Support artifacts do not belong in `canonical/`.
5. Reconstruction metadata belongs on canonical objects.
6. Generator-facing reconstruction remains separate from generator internals.

## Current Canonical Shape

The generated canonical tree now contains:

- `sections/`
- `slides/`
- `solutions/`
- `snippets/`
- `static_pages/`
- `html_includes/`
- `photos/`
- `drawings/`
- `tables/`
- `legal_documents/`
- `structure/editions/`

Each object now includes reconstruction metadata describing how it contributes
to generator input reconstruction.

## Support Artifacts

Support artifacts were moved out of canonical Git and are now exported to:

- `work/canonical_support/artifacts/`
- `work/canonical_support/artifacts.manifest.json`

These files are operational rebuild support only. They are no longer part of
the canonical Git model.

## Validation Completed

The following commands succeeded on this state:

```bash
cd /home/jjcarron/proj/50-Ohms/translator/50ohm-contents-ch

python3 tools/export_canonical_model.py
python3 tools/build_db_from_canonical_model.py
python3 tools/run_multilingual_canonical_build.py --skip-build
```

Observed counts:

- `2071` content objects
- `1783` curriculum nodes
- `3003` text slots
- `3003` localized texts
- `3876` support artifacts

## Reconstruction-Usage Logging

Per-language usage reports are now written to:

- `work/validation/multilingual/support-artifact-usage-de.json`
- `work/validation/multilingual/support-artifact-usage-fr.json`
- `work/validation/multilingual/support-artifact-usage-it.json`

Current measured state:

- `1988` paths replaced or rendered from canonical data
- `1890` paths still retained from support artifacts

Breakdown of replaced or rendered paths:

- `1005` rendered from canonical
- `981` overwritten from canonical
- `2` overwritten from question-pool

## What Still Depends On Support Artifacts

The remaining retained files are mostly technical resources rather than
translatable business text, especially:

- drawing source files such as `contents/drawings/*.svg`
- drawing source files such as `contents/drawings/*.tex`
- a few root-level repository files such as `README.md` and `LICENSE`

This means the text model is already much cleaner than before, but the model is
not yet fully self-sufficient for complete repository reconstruction.

## Immediate Next Step

The next redesign step should use the usage reports to remove the remaining
support-artifact dependency category by category.

Recommended order:

1. drawings technical assets
2. other binary/static assets
3. root repository support files

For each category:

- decide whether it belongs in canonical object metadata or in a separate
  explicitly modeled asset object;
- model it deliberately;
- rebuild canonical;
- rerun the usage report;
- verify that retained support paths shrink.

## Important Constraint For Tomorrow

Do not reintroduce support files into `canonical/`.

The current design line is:

- canonical Git contains business objects and structure;
- SQLite is a validated working strategy for import, joins, validation, and
  reconstruction, but not the source of truth;
- `work/` contains operational reconstruction support until the model can
  replace it fully.

## Later Workflow Decision

After this intermediate redesign checkpoint, the workflow direction was
clarified further:

- the destructive reset used during the model transition was a one-time
  migration maneuver, not a normal operating procedure;
- future source updates should start from canonical baseline and integrate new
  German source data non-destructively;
- objects missing from the refreshed German source should be marked
  `to_be_deleted` first, not physically removed immediately;
- the object may stay in canonical temporarily for review and later cleanup;
- if the object is gone in German, it is considered gone for all languages as a
  business object.
- when an object is marked `to_be_deleted`, its node content is left untouched
  until a later explicit cleanup step.
- workflow safety should rely on Git tags before each new source import and
  after each validated export, even though this is not yet enforced by tools.

This decision is intentionally documented as revisable later.
