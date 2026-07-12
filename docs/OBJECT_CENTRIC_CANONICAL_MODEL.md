# Object-Centric Canonical Model

## Purpose

This document defines the new direction for the `50ohm-contents-ch` canonical
Git model.

The product goal is to take an existing German 50Ohms site, extract its
business objects from the current source structure, assign them stable internal
identifiers independent from visible content codes, and store them in a
canonical Git structure where one object is represented by one directory.

That canonical object directory is intended to hold the language variants of
the same business object together, so the object remains the stable editorial
unit across German, French, and Italian.

The design goal is therefore:

- Git-first canonical storage;
- human-maintainable object boundaries;
- one object directory per business object;
- all language variants stored with that object;
- deterministic site reconstruction in the original source format;
- SQLite used as a validated working database strategy, but not treated as the
  source of truth.

The source-update workflow is intentionally non-destructive toward canonical
Git. Canonical content is the reference baseline; source imports are expected
to update that baseline, not recreate it from nothing during normal operation.

The question-pool repository is the reference style for this direction.

This is a fresh model, not a compatibility layer over the previous canonical
layout.

Questions are handled separately in `50ohm-question-pool`, but according to the
same canonical principle: stable internal object ids, language variants grouped
with the object, and deterministic rebuilt publication outputs.

## Current Redesign Scope

This first redesign step covers:

- object-centric canonical export for German content objects;
- object-centric structure export for curriculum editions;
- SQLite rebuild from the new canonical layout as the operational working
  database.

It does **not** yet cover:

- French and Italian canonical payload generation in the new layout;
- translation-tool adaptation to the new layout;
- generator adaptation, which should remain independent of the internal model.

## Top-Level Layout

```text
canonical/
  _model.json
  export_summary.json

  sections/
  slides/
  solutions/
  snippets/
  static_pages/
  html_includes/
  photos/
  drawings/
  tables/
  legal_documents/

  structure/
    editions/
      <edition>/
        edition.meta.json
        edition.de.json
```

Support artifacts used only for repository reconstruction are intentionally kept
outside the canonical Git model:

```text
work/
  canonical_support/
    artifacts/
      ...
    artifacts.manifest.json
```

## Identifier Policy

Every canonical object id follows the current content-model convention:

- `prefix_` + `12` hexadecimal characters
- prefix length is at most `3` characters before the underscore
- deterministic from a stable source-side key
- no inherited ids from the previous content canonical model

Examples:

- `sc_c19e8f4f9d0e`
- `ph_8f3d771302c4`
- `dr_5a1d9db6c8b2`
- `ed_6f1e5f2a7d14`

The previous content-canonical id is intentionally not preserved in the new
model.

### Prefix Registry

- `ed_` edition root
- `ch_` curriculum chapter node
- `se_` curriculum section node
- `sc_` section article
- `sl_` slide article
- `s_` solution article
- `sn_` snippet
- `sp_` static page
- `in_` html include
- `ph_` photo
- `dr_` drawing
- `tb_` table object
- `ld_` legal document

## Object Layout

Each business object lives in its own directory.

Example for a section article:

```text
canonical/sections/sc_c19e8f4f9d0e/
  object.meta.json
  body.de.md
  object.references.json
  object.annotations.json
```

Example for a photo:

```text
canonical/photos/ph_8f3d771302c4/
  object.meta.json
  102.de.png
  102.de.txt
  object.references.json
  object.annotations.json
```

Example for a drawing:

```text
canonical/drawings/dr_b4bfdee9ee99/
  object.meta.json
  1021.de.svg
  1021.de.tex
  1021.de.txt
  object.references.json
  object.annotations.json
```

## Object Metadata

Each object directory contains `object.meta.json` with:

- canonical object id;
- object type;
- active flag;
- source path, format, and stable source key;
- reconstruction strategy and reconstruction targets;
- identifiers;
- metadata grouped by scope;
- review states;
- text-slot definitions;
- available languages;
- copied asset filenames where relevant.

For `photo` and `drawing`, `object.meta.json` must also expose the language
variant mapping of the visual asset. The imported German file is the initial
default variant and therefore becomes `*.de.<ext>` in canonical storage.

## Text Storage

Single-field objects store text in raw language files beside the object:

- Markdown -> `body.de.md`
- HTML -> `body.de.html`
- plain text -> `body.de.txt`

Multi-field objects store language content in one local JSON file:

- `content.de.json`

This keeps the object boundary intact while still allowing multiple text fields
to belong to one business object.

`photo` and `drawing` descriptions are stored as source-like per-language files
named `<stem>.<lang>.txt`. The working SQLite model may still split them into
`short_description` and `long_description` slots, but canonical Git keeps the
language-qualified description file itself.

## Source-Update Status Strategy

Source updates are expected to work from canonical baseline, not from an empty
canonical tree.

Current agreed strategy:

- load the working SQLite database from canonical;
- integrate the incoming German source data non-destructively;
- keep stable canonical ids for matching objects;
- mark German objects missing from the new source with a reversible state such
  as `to_be_deleted` instead of deleting them immediately;
- keep the canonical directory and links temporarily so review and cleanup can
  happen later under Git control.

Important business rule:

- if an object disappears from German source, it is considered removed for all
  languages, not only for German;
- the full node should therefore be treated as `to_be_deleted`, not only one
  language variant;
- when this state is set, the node content is left untouched for `de`, `fr`,
  and `it` until a later explicit cleanup step removes the node.

This is a deliberate transitional policy and must remain documented so it can
be revised later if needed.

Recommended Git workflow around source updates:

- create a Git tag before each new source import;
- validate the resulting canonical export;
- create another Git tag after that validated export.

This is currently documented discipline, not enforced by the tools.

## Structure Storage

Curriculum structure is exported per edition:

```text
canonical/structure/editions/NE/
  edition.meta.json
  edition.de.json
```

`edition.de.json` contains the German nested curriculum tree with:

- root node data;
- chapter nodes;
- section nodes;
- node metadata;
- placements toward canonical object ids.

This keeps structure local to the edition while avoiding a highly fragmented
filesystem tree for every individual node.

## Artifacts

Repository reconstruction artifacts remain separate from business objects:

- `work/canonical_support/artifacts/...`
- `work/canonical_support/artifacts.manifest.json`

This preserves rebuild capability without forcing raw source-support files into
the canonical Git tree.

The reconstruction layer now logs, per language build, which support artifacts
were:

- overwritten from canonical objects;
- rendered from canonical objects;
- overwritten from question-pool outputs;
- still retained untouched.

This report is written into `work/validation/multilingual/summary.json` and is
the basis for removing remaining support-artifact dependencies later.

## SQLite Role

SQLite is a validated working-database strategy.

Its role is operational rather than editorial:

- first import the original site data into a normalized working database;
- export canonical Git objects from that database;
- on subsequent runs, rebuild the working database from canonical Git;
- integrate source-site changes while preserving existing stable ids;
- support joins, integrity checks, reconstruction logic, and deterministic
  exports.

SQLite is therefore part of the workflow strategy, but it is not the source of
truth. Canonical Git objects remain the source of truth.

## Current Validation Result

The current redesign step successfully rebuilds SQLite from the new canonical
layout with:

- `2071` content objects
- `1783` curriculum nodes
- `3003` text slots
- `3003` localized texts
- `3876` source artifacts

This count intentionally excludes question objects from the content canonical
Git model at this stage. Questions remain canonically owned by
`50ohm-question-pool`.
