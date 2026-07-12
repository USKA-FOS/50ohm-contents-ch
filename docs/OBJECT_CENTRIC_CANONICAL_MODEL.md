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
  content.de.json
  102.png
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

## Text Storage

Single-field objects store text in raw language files beside the object:

- Markdown -> `body.de.md`
- HTML -> `body.de.html`
- plain text -> `body.de.txt`

Multi-field objects store language content in one local JSON file:

- `content.de.json`

This keeps the object boundary intact while still allowing multiple text fields
to belong to one business object.

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
