# Canonical Data Model Reference

This document is a model reference only.

It describes the current canonical repository model and its operational SQLite
counterpart. It does not describe history, migration steps, or earlier model
variants.

## 1. Scope

This reference covers:

- the canonical Git structure under `50ohm-contents-ch/canonical/`;
- the operational SQLite model created in
  `work/canonical_model/content_model.sqlite`;
- the mapping between the two;
- the current meaning of `object.meta.json`, `object.references.json`,
  `object.annotations.json`, `edition.meta.json`, and `edition.<lang>.json`.

This reference does not define:

- translation prompts or batching rules;
- generator command lines;
- Git process history;
- question-pool internals.

Questions are handled canonically in `50ohm-question-pool`. The content model
in this repository may still reference question objects by business identifier,
but question ownership remains external to this repository.

## 2. Purpose Of The Model

The purpose of this model is to represent the business content of the German
site as stable multilingual objects that can be:

- identified independently from visible content or publication codes;
- stored canonically in Git;
- translated into French and Italian without changing object identity;
- reconstructed back into the source-site file contract;
- versioned and reviewed as coherent editorial units.

The canonical model is therefore not only a storage format. It is the
reference representation used to:

- separate stable object identity from mutable text;
- keep all languages of one business object together;
- preserve the metadata required for reconstruction and lifecycle management;
- provide a deterministic bridge toward SQLite, translation, and site rebuild.

## 3. Modeling Principles

- the business object is the canonical unit;
- one business object is stored in one directory;
- the object identifier is stable and independent from visible content;
- language variants of the same business object live in the same directory;
- canonical Git is the source of truth;
- SQLite is a working representation used for import, validation, joins,
  reconstruction, translation support, and deterministic export.

## 4. Canonical Top-Level Layout

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
  support_assets/

  structure/
    editions/
      <edition>/
        edition.meta.json
        edition.<lang>.json
```

Each object family directory contains one subdirectory per object id.

Examples:

```text
canonical/sections/sc_6a07c44d86cf/
canonical/photos/ph_563d2e772bfa/
canonical/drawings/dr_b4bfdee9ee99/
```

## 5. Object-As-Directory Rule

The canonical object is the directory, not one file inside the directory.

This is a core rule of the model:

- the directory is the business object boundary;
- all files inside that directory belong to the same object;
- all language variants inside that directory are variants of the same object;
- `object.meta.json`, references, annotations, text payloads, and media files
  are not separate canonical objects;
- the object is the full package made of those dependent items.

For example, a photo object is not only `102.de.png` and not only `102.de.txt`.
The photo object is the whole directory:

```text
canonical/photos/ph_563d2e772bfa/
  object.meta.json
  102.de.png
  102.de.txt
  102.fr.txt
  object.references.json
  object.annotations.json
```

Meaning of this package:

- `ph_563d2e772bfa/` is the object;
- `102.de.png` is one language-specific asset variant belonging to that
  object;
- `102.de.txt` and `102.fr.txt` are translatable description payloads
  belonging to that same object;
- `object.meta.json` declares identity, storage, reconstruction, review state,
  and language presence for the object;
- `object.references.json` and `object.annotations.json` describe structured
  information extracted from the object text.

The same packaging rule applies to all object families.

## 6. Identifier Format

The current identifier format is:

- `<prefix>_<hex12>`

Rules:

- prefix length is at most 3 characters before the underscore;
- the suffix is 12 hexadecimal characters;
- ids are stable for a given source-side business key;
- ids are not derived from translated text.

Current prefixes:

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
- `sa_` support asset

## 7. Object Families

Current `content_object.object_type` families modeled by this repository:

- `section_article`
- `slide_article`
- `solution_article`
- `snippet`
- `static_page`
- `html_include`
- `photo`
- `drawing`
- `table_object`
- `legal_document`
- `support_asset`

Current structure node families:

- `curriculum_root`
- `curriculum_chapter`
- `curriculum_section`

## 8. Canonical Object Directory

Each object directory contains:

- `object.meta.json`
- `object.references.json`
- `object.annotations.json`
- zero or more language files
- zero or more language-specific media files

These items do not all play the same role. The directory usually contains:

- authoritative business payloads:
  - markdown bodies
  - HTML bodies
  - canonical description files
  - JSON payload files when a family stores text that way
- language-specific media assets:
  - image files
  - SVG files
  - TeX files
- structured metadata and control files:
  - `object.meta.json`
  - `object.references.json`
  - `object.annotations.json`

### 8.1 `object.meta.json`

`object.meta.json` is the primary object descriptor. It contains:

- `id`: canonical object id;
- `object_type`: business object family;
- `active`: boolean activity flag;
- `source`: original source contract:
  - `path`
  - `format`
  - `key`
- `identifiers`: stable external or source-facing identifiers;
- `languages`: currently present language set in canonical storage;
- `review_states`: review state records by language;
- `metadata`: structured object metadata grouped by scope;
- `text_slots`: text-bearing slots belonging to the object;
- `reconstruction`: reconstruction strategy and targets;
- `language_variants`: per-language media variant mapping for objects that carry
  language-dependent assets.

Purpose of `object.meta.json`:

- declares what the object is;
- lists which language payloads belong to it;
- lists which media variants belong to it;
- records metadata needed for reconstruction and workflow;
- records review state and language presence;
- tells the SQLite rebuild layer how to read the object.

`object.meta.json` is metadata and control information. It is not itself the
business text to translate.

### 8.2 `object.references.json`

`object.references.json` contains parsed inline links and embeddings originating
from the object text.

Each entry describes:

- the source slot via `source_slot_key`;
- the source marker via `raw_marker`;
- the target type via `target_object_type`;
- the target lookup contract via `target_id_system` and `target_id_value`;
- the relation semantic via `relation_type`;
- optional inline alias and label;
- `sort_order` inside the source slot.

Typical `relation_type` values currently used:

- `references_question`
- `embeds_photo`
- `embeds_drawing`
- `includes_object`
- `embeds_table`
- `references_embedded_alias`

Purpose of `object.references.json`:

- preserve structured outgoing links extracted from the object payload;
- keep those links independent from raw text parsing during later steps;
- support validation, rebuild, and future editing workflows.

It is derived structured metadata, not translatable primary content.

### 8.3 `object.annotations.json`

`object.annotations.json` contains parsed non-reference markers extracted from
text, for example:

- class markers;
- index terms;
- morse markers.

Each entry describes:

- the source slot via `source_slot_key`;
- the semantic annotation type;
- optional key and value;
- the original marker via `raw_marker`;
- `sort_order` inside the source slot.

Purpose of `object.annotations.json`:

- preserve structured semantic markers extracted from text;
- avoid losing information that is not plain prose;
- support reconstruction and future processing.

It is derived structured metadata, not translatable primary content.

## 9. Text Slot Model In Canonical Git

Each entry of `text_slots` defines one logical text slot.

Common fields:

- `slot_key`
- `slot_type`
- `sort_order`
- `translation_group_key`
- `storage`

Current `slot_type` values:

- `markdown`
- `html`
- `plain_text`

Current `storage.kind` variants:

- `text_file`
- `json_file`
- `description_file_bundle`

The purpose of `text_slots` is to tell the system:

- which business text exists on the object;
- which file carries that text for each language;
- how translation units map back to canonical payloads;
- how SQLite must rebuild its `text_slot` and `localized_text` rows.

### 9.1 `text_file`

Used when one slot maps directly to one language-qualified file.

Examples:

- `body.de.md`
- `body.fr.md`
- `body.de.html`

Storage shape:

```json
{
  "kind": "text_file",
  "files": {
    "de": "body.de.md",
    "fr": "body.fr.md"
  }
}
```

This is authoritative translatable content.

### 9.2 `json_file`

Used when multiple logical slot values share a local JSON payload file.

Storage shape:

```json
{
  "kind": "json_file",
  "files": {
    "de": "content.de.json",
    "fr": "content.fr.json"
  },
  "json_field": "field_name"
}
```

The JSON file is the authoritative canonical payload file. The extracted
logical field is the translatable text view used by the operational model.

### 9.3 `description_file_bundle`

Used by `photo` and `drawing` descriptions.

One source-like language file is the canonical payload for the whole
description, even when the operational model exposes derived slots such as
`short_description` and `long_description`.

Example:

```json
{
  "kind": "description_file_bundle",
  "files": {
    "de": "1021.de.txt",
    "fr": "1021.fr.txt"
  }
}
```

Operational rule:

- the language file `1021.<lang>.txt` is the authoritative canonical payload;
- any derived split into short and long description belongs to the operational
  model, not to the authoritative file contract.

## 10. Per-Family Canonical Patterns

### 10.1 Section, Slide, Solution, Snippet

Typical files:

```text
object.meta.json
body.de.md
body.fr.md
object.references.json
object.annotations.json
```

Directory meaning:

- the directory is one multilingual article-like object;
- `body.<lang>.md` files are the authoritative translatable content;
- `object.meta.json` describes identity, storage, and reconstruction;
- `object.references.json` stores extracted links;
- `object.annotations.json` stores extracted semantic markers.

Typical text contract:

- one markdown body slot
- storage kind `text_file`

What is translated:

- the markdown body payload.

What is metadata:

- `object.meta.json`
- `object.references.json`
- `object.annotations.json`

### 10.2 Static Page And HTML Include

Typical files:

```text
object.meta.json
body.de.html
body.fr.html
object.references.json
object.annotations.json
```

Directory meaning:

- the directory is one multilingual HTML-bearing object;
- `body.<lang>.html` files are the authoritative content payloads;
- the full HTML file remains the canonical payload, even though translation
  operates on extracted text segments.

Typical text contract:

- one HTML body slot
- storage kind `text_file`
- translation is performed on extracted text segments, but canonical storage
  remains full HTML files

What is translated:

- the visible text content carried by the HTML payload.

What is metadata:

- `object.meta.json`
- `object.references.json`
- `object.annotations.json`

### 10.3 Photo

Typical files:

```text
object.meta.json
102.de.png
102.de.txt
102.fr.txt
object.references.json
object.annotations.json
```

Directory meaning:

- the directory is one multilingual photo object;
- image files such as `102.de.png` are dependent media variants belonging to
  that object;
- description files such as `102.de.txt` and `102.fr.txt` are the authoritative
  translatable text payloads belonging to that same object;
- the object is the whole package, not the image alone and not the text alone.

Additional canonical semantics:

- `language_variants.<lang>.asset_files.image` maps the image file for each
  language when needed;
- description payloads are language-qualified text files;
- current reconstruction metadata records whether the source description format
  was split or single-file.

What is translated:

- the description file `102.<lang>.txt`.

What is content but usually not translated automatically:

- image assets such as `102.de.png`, unless a future workflow adds
  language-specific media variants.

What is metadata:

- `object.meta.json`
- `object.references.json`
- `object.annotations.json`

### 10.4 Drawing

Typical files:

```text
object.meta.json
1021.de.svg
1021.de.tex
1021.de.txt
1021.fr.txt
object.references.json
object.annotations.json
```

Directory meaning:

- the directory is one multilingual drawing object;
- `1021.de.svg` and `1021.de.tex` are dependent source assets belonging to that
  object;
- `1021.de.txt` and `1021.fr.txt` are the authoritative text payloads for the
  drawing description;
- the object is the full package made of media assets, text payloads, and
  metadata.

Additional canonical semantics:

- `language_variants.<lang>.asset_files.svg` maps the SVG file;
- `language_variants.<lang>.asset_files.tex` maps the TeX file when present;
- description payloads are language-qualified text files.

What is translated:

- the description text payload when present.

What is content but usually not translated automatically:

- SVG and TeX asset files, unless a future workflow introduces localized asset
  variants.

What is metadata:

- `object.meta.json`
- `object.references.json`
- `object.annotations.json`

### 10.5 Table Object

Current state:

- tables are canonical business objects;
- they are referenced through table markers and aliases;
- they may carry little or no direct text payload depending on the source.

Directory meaning:

- the directory is one reusable embedded object;
- the payload may be minimal today, but the object boundary is still the
  directory.

What is translated:

- only explicit text payloads if present.

What is metadata:

- aliasing, identifiers, references, and reconstruction data.

### 10.6 Legal Document And Support Asset

Current state:

- these objects preserve repository-level or build-support material;
- they are modeled for reconstruction traceability;
- they are not part of the normal translatable business-content scope.

Directory meaning:

- the directory is one non-regular business object whose main purpose is
  preservation, reconstruction, or support traceability;
- the object may have files, but its normal lifecycle is not the same as
  editorial multilingual content.

What is translated:

- usually nothing in the standard content translation workflow.

What is metadata:

- most of the object package, including reconstruction and source-trace data.

## 11. Structure Model In Canonical Git

Curriculum structure is stored per edition under:

```text
canonical/structure/editions/<edition>/
  edition.meta.json
  edition.de.json
  edition.fr.json
  edition.it.json
```

Not every language file is required to exist at all times. `de` is the
structural baseline currently expected to exist.

The edition directory itself is the canonical structure object for that
edition. `edition.de.json`, `edition.fr.json`, and `edition.it.json` are
language variants of that same structure object.

### 11.1 `edition.meta.json`

Current fields:

- `edition`
- `id`
- `node_type`
- `source_path`

Purpose of `edition.meta.json`:

- identify the edition object;
- declare the source-side edition contract;
- anchor the localized structure files belonging to that edition.

### 11.2 `edition.<lang>.json`

This file stores the full localized node tree for one edition and one
language.

Each node may contain:

- `id`
- `node_type`
- `title`
- `abstract`
- `identifiers`
- `metadata`
- `placements`
- child arrays:
  - `chapters`
  - `sections`

Placement entries contain:

- `object_id`
- `placement_role`
- `sort_order`
- `visible_label`

Purpose of `edition.<lang>.json`:

- carry the localized structure tree for that edition;
- keep titles and abstracts together with the node hierarchy;
- keep object placements associated with the structure they belong to.

What is translated:

- node `title`
- node `abstract`

What is metadata:

- identifiers
- structural hierarchy
- placements
- non-text node metadata

## 12. SQLite Working Model

The operational database schema contains these tables:

- `content_object`
- `object_identifier`
- `text_slot`
- `localized_text`
- `object_metadata`
- `review_state`
- `curriculum_node`
- `node_identifier`
- `node_text`
- `node_metadata`
- `content_placement`
- `object_reference`
- `text_annotation`
- `source_artifact`

### 12.1 `content_object`

One row per business object.

Fields:

- `id`
- `object_type`
- `source_path`
- `source_format`
- `source_key`
- `active`

### 12.2 `object_identifier`

One row per identifier attached to a business object.

Fields:

- `id`
- `object_id`
- `id_system`
- `id_value`
- `preferred`

### 12.3 `text_slot`

One row per logical text slot.

Fields:

- `id`
- `object_id`
- `slot_key`
- `slot_type`
- `translation_group_key`
- `sort_order`

### 12.4 `localized_text`

One row per slot and per language.

Fields:

- `id`
- `text_slot_id`
- `language`
- `text_value`

### 12.5 `object_metadata`

Structured metadata attached to content objects.

Fields:

- `id`
- `object_id`
- `metadata_scope`
- `metadata_key`
- `value_json`

### 12.6 `review_state`

Review lifecycle records for content objects and other reviewable subjects.

Fields:

- `id`
- `subject_kind`
- `subject_id`
- `language`
- `state`

### 12.7 `curriculum_node`

One row per structure node.

Fields:

- `id`
- `edition`
- `node_type`
- `parent_node_id`
- `sort_order`
- `source_path`

### 12.8 `node_identifier`

Identifiers attached to structure nodes.

Fields:

- `id`
- `node_id`
- `id_system`
- `id_value`
- `preferred`

### 12.9 `node_text`

Localized text attached to structure nodes.

Fields:

- `id`
- `node_id`
- `language`
- `title`
- `abstract`

### 12.10 `node_metadata`

Structured non-text properties of structure nodes.

Fields:

- `id`
- `node_id`
- `metadata_key`
- `value_json`

### 12.11 `content_placement`

Links structure nodes to business objects in presentation order.

Fields:

- `id`
- `node_id`
- `object_id`
- `placement_role`
- `sort_order`
- `visible_label`

### 12.12 `object_reference`

Normalized inline links and embeddings extracted from object texts.

Fields:

- `id`
- `source_object_id`
- `source_slot_key`
- `target_object_type`
- `target_id_system`
- `target_id_value`
- `relation_type`
- `inline_alias`
- `inline_label`
- `raw_marker`
- `sort_order`

### 12.13 `text_annotation`

Normalized non-reference markers extracted from object texts.

Fields:

- `id`
- `source_object_id`
- `source_slot_key`
- `annotation_type`
- `annotation_key`
- `annotation_value`
- `raw_marker`
- `sort_order`

### 12.14 `source_artifact`

Byte-preserved source files used for exact reconstruction and validation.

Fields:

- `id`
- `object_id`
- `source_path`
- `media_type`
- `checksum_sha256`
- `payload`

## 13. Git-To-SQLite Correspondence

The operational correspondence is:

- one object directory -> one `content_object` row;
- one canonical identifier entry -> one `object_identifier` row;
- one `text_slots` entry -> one `text_slot` row;
- one language payload for one slot -> one `localized_text` row;
- one metadata leaf entry -> one `object_metadata` row;
- one review state entry -> one `review_state` row;
- one structure node in `edition.<lang>.json` -> one `curriculum_node` row for
  structure plus one `node_text` row per language;
- one placement entry -> one `content_placement` row;
- one object reference entry -> one `object_reference` row;
- one annotation entry -> one `text_annotation` row.

For `photo` and `drawing`:

- canonical `*.txt` files are preserved as authoritative language payloads;
- SQLite may still expose multiple logical slots from the same canonical file;
- multiple `localized_text` rows can therefore correspond to one canonical
  description file.

## 14. Review-State Expectations

Current review-state usage in canonical Git:

- stored in `object.meta.json` under `review_states`;
- optionally stored in `language_variants.<lang>.review_state` for media
  variants.

Current review-state usage in SQLite:

- stored in `review_state`.

The state vocabulary is operational and may evolve, but the storage location is
fixed by this model:

- review state is metadata;
- review state is not embedded in business-text payload files.

## 15. Reconstruction Metadata

Each object may define a reconstruction contract in `object.meta.json` under
`reconstruction`.

Current patterns include:

- `replace_source_file`
- `render_photo_description_file`
- `render_drawing_assets_and_description`
- target kinds such as:
  - `localized_text_file`
  - `asset_file`
  - `rendered_description_file`

This contract tells the rebuild layer how canonical payloads map back to source
paths such as:

- `contents/sections/*.md`
- `contents/static/*.html`
- `contents/photos/*.txt`
- `contents/drawings/*.svg`
- `contents/drawings/*.tex`

## 16. Out-Of-Scope Runtime Material

This reference does not treat the following as canonical source of truth:

- generated site output under `work/build/`;
- transient generator input staging under `work/generator-input/`;
- translation run caches under `ai-translation-tool/work/ai_output/`.

Those artifacts may depend on the canonical model, but they are not part of
the model itself.
