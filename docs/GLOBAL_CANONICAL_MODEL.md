# Global Canonical Model

## Purpose

This document consolidates the current design direction for the future
canonical model of `50ohm-contents-ch`.

It supersedes older partial notes by applying these rules:

- the most recent repository-local and workspace documentation wins;
- `50ohm-question-pool` remains the current canonical home of Swiss question
  objects;
- `50ohm-contents-ch` still belongs to the same global data universe and must
  be modeled coherently with the question pool;
- SQLite is an operational intermediate representation, not the source of
  truth.

## Confirmed Scope

The modeled data set includes:

- all files under `contents/`
- all `toc/*.json` files
- all source-support files under `latex/` and `src/`
- repository-level legal documents `README.md` and `LICENSE`
- question-catalog-derived question objects imported for validation
- synthetic relational objects implied by the content, such as:
  - table objects discovered from `[table:...]`
  - inline references
  - structure nodes
  - placements

The modeled scope therefore includes:

- `contents/questions/`
- `contents/metadata/`
- `contents/sections/`
- `contents/slides/`
- `contents/solutions/`
- `contents/snippets/`
- `contents/static/`
- `contents/html/`
- `contents/photos/`
- `contents/drawings/`
- `toc/*.json`

## Main Principles

### 1. Stable internal ids

Every persistent modeled object receives a stable internal id.

For the current validation phase, ids are deterministically generated from
stable source-side keys such as:

- question code
- file stem
- numeric drawing id
- numeric photo id
- include key
- toc edition and node path

This avoids coupling ids to mutable translated text.

### 2. Canonical Git model remains the source of truth

The long-term source of truth remains a text-based Git model.

SQLite may be used to:

- ingest current sources
- validate relations
- inspect coverage
- detect orphans
- rebuild deterministic Git files
- regenerate site-facing exports

### 3. Strict separation of business text and metadata

A metadata change must not be treated as a material text revision.

Therefore the model separates:

- content objects
- localized text payloads
- metadata records
- review states
- placements
- references

This is mandatory for translation lifecycle management.

### 4. Question pool stays canonically separate for now

`50ohm-question-pool` remains the canonical Git home of Swiss question objects.

However, the global model must still be able to represent questions inside the
same relational workspace so that:

- section and slide links to questions resolve deterministically;
- current question metadata can be joined to current content;
- future reconciliation between repositories remains possible.

At the current stage, `50ohm-contents-ch/canonical` may still mirror question
objects with the same stable ids. This is accepted as a transitional storage
duplication caused by the two repositories evolving separately over time. It
does not create a second question identity and does not change the authority
boundary: the question pool still owns question canon.

### 5. Generator compatibility is a bridge concern

The current static review generator still requires:

- per-question `HB.rationale`
- top-level `pruned`

These fields are review-site compatibility metadata, not canonical translated
business text.

The current bridge exporter is:

- `translator/50ohm-question-pool/tools/export_generator_review_catalog.py`

Its role is to re-inject `HB.rationale` and `pruned` into a cleaned build
catalog for generator compatibility.

## Core Object Families

### Structure

- `curriculum_root`
- `curriculum_chapter`
- `curriculum_section`
- `question_catalog_root`
- `question_catalog_section`

Each TOC JSON is represented both as a preserved source artifact and as a
tree of modeled root, chapter and section nodes. Every non-structural property
of a JSON node is retained: `title` and `abstract` are localized node text,
`ident` is an identifier, and all other properties are structured node
metadata. This prevents the model from treating TOC files as opaque blobs.

### Main content

- `question`
- `section_article`
- `slide_article`
- `solution_article`
- `snippet`
- `static_page`
- `html_include`

### Reusable media

- `photo`
- `drawing`
- `table_object`

### Source and metadata carriers

- `question_catalog_file`
- `question_metadata_file`
- `question_layout_file`
- `toc_file`
- `questions_readme`
- `legal_document`

## Minimal Relational Axes

The validation database must materialize at least these axes:

1. objects
2. object identifiers
3. text slots
4. localized texts
5. object metadata
6. review states
7. structure nodes
8. structure node texts and metadata
9. placements
10. object references
11. text annotations

## Review-State Rule

Review state must live in metadata tables, never inside the business-text
payload itself.

The target model therefore supports:

- a general review state
- a per-language review state

The current source import may initialize German text as approved-like imported
state without implying that the future Git model must keep the same literal
enum values.

## Metadata Rule

Metadata currently required for reconstruction includes at least:

- question presentation metadata from `contents/questions/metadata3b.json`
- question layout metadata from `contents/metadata/question_layout.json`
- toc metadata such as `status`, `class`, `video_url`
- source file paths for all current objects
- drawing and photo asset paths

`directus_id` must be preserved as a legacy reference or metadata value, but it
is not treated as canonical identity.

`photo` and `drawing` media assets must also be referencable per language, with
the imported German asset acting as the default initial variant.

## Translation Rule

The translation pipeline must evolve toward generic text items.

The model therefore stores texts as slots, not as opaque files.

Examples:

- question stem
- question answers
- section body
- slide body
- short photo description
- long photo description
- short drawing description
- long drawing description
- static HTML body

Question stem and answers remain one translation group.

Photo and drawing descriptions must stay local to their own object. A global
group such as all drawing descriptions or all photo descriptions is invalid.

In canonical Git, these descriptions are language-qualified files such as
`1021.de.txt`, `1021.fr.txt`, and `1021.it.txt`. Visual media may also become
language-qualified when needed, for example `1021.de.svg` and later
`1021.fr.svg`.

For HTML-bearing objects, the canonical slot may remain HTML, but translation
must operate on extracted text segments rather than on raw HTML source.

For large Markdown or plain-text bodies, the canonical object remains whole but
the translation-preparation layer may split derived units on blank lines and
reassemble them after translation.

## Reconstruction Rule

The global model must support reconstruction of:

- the current site inputs from the canonical Git model
- the current site inputs from the SQLite validation database

This requires preserving:

- legacy question codes
- media numeric ids
- file stems
- inline aliases
- raw inline markers
- current toc placements
- byte-exact source artifacts for every current `contents/` and `toc/` file
- `README.md` and `LICENSE` as non-translatable legal artifacts
- `latex/` and `src/` as byte-exact source-support artifacts required by the
  current repository-level reconstruction workflow

Question-generator inputs remain deliberately outside the current reconstruction
diff target. `contents/questions/` stays under the separate
`50ohm-question-pool` cycle until that integration boundary is worked on
explicitly.

## Initial Canonical Git Skeleton

The current repository does not yet hold the final canonical Git model.

The intended future split inside a canonical repository is:

```text
canonical/
  objects/
  structure/
  texts/
  metadata/
  review/
  exports/
```

This is a structural target only for now.

## Current Implementation Goal

The first implementation milestone is:

1. formalize the consolidated model
2. ingest current source data into SQLite
3. validate counts and relations against the real repository
4. keep the current site and current tools largely unchanged

Only after that should a canonical Git layout be written and adopted.

## Recorded Validation

The initial SQLite import, source-artifact reconstruction, TOC semantic check,
and German review-site build are recorded in `docs/VALIDATION_LOG.md`.
