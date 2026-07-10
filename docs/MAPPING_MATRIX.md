# Mapping Matrix

## Purpose

This matrix maps the current source repository into the global model used for
SQLite validation and future canonical Git export.

## Source Families

| Source | Canonical object | Text slots | Metadata | Structure / refs | Notes |
| --- | --- | --- | --- | --- | --- |
| `contents/questions/fragenkatalog3b.json` | `question_catalog_file` plus one `question` per question | `question_text`, `answer_a`, `answer_b`, `answer_c`, `answer_d` | `class` and imported source attributes | nested question-catalog structure nodes and question placements | validation import only; canonical Swiss questions stay in `50ohm-question-pool` |
| `contents/questions/metadata3b.json` | `question_metadata_file` | none | per-question presentation metadata such as `picture_*`, `layout`, `directus_id` | keyed by question code | reconstruction-critical metadata |
| `contents/metadata/question_layout.json` | `question_layout_file` | none | per-question layout scalars and layout type | keyed by question code | reconstruction-critical metadata |
| `contents/questions/README.txt` | `questions_readme` | `body_text` | file path | none | tracked because it lives under `contents/` |
| `toc/*.json` | `toc_file` plus structure nodes | node `title`, node `abstract` | every non-structural JSON property, including `status`, `class`, `video_url`, `edition` | chapter/section hierarchy and placements to section and slide objects | modeled node-by-node and preserved byte-for-byte |
| root `README.md`, `LICENSE` | `legal_document` plus source artifact | none | source path, checksum | none | retained byte-for-byte; not a site-generation or translation input |
| root `latex/**/*`, `src/**/*` | source-support artifact | none | source path, checksum | none | retained byte-for-byte for repository reconstruction; not translatable content |
| `contents/sections/*.md` | `section_article` | `body_markdown` | file stem, source path | references and annotations parsed from body | placed from `toc` by `ident` |
| `contents/slides/*.md` | `slide_article` | `body_markdown` | file stem, source path | references and annotations parsed from body | placed from `toc` by `ident` |
| `contents/solutions/*.md` | `solution_article` | `body_markdown` | file stem, source path | references and annotations parsed from body | currently not placed by `toc` |
| `contents/snippets/*.md` | `snippet` | `body_markdown` | file stem, source path | references and annotations parsed from body | reusable text family |
| `contents/static/*.html` | `static_page` | `body_html` | file stem, source path | inline markers if present | includes sidebar variants as independent objects |
| `contents/html/*.html` | `html_include` | `body_html` | file stem, source path | may be referenced by `[include:...]` | part of the model, not optional |
| `contents/photos/<id>.png` + `contents/photos/<id>.txt` | `photo` | `short_description`, `long_description` when `.txt` exists | image path, numeric photo id | referenced by `[photo:...]` | one canonical object per numeric id |
| `contents/drawings/<id>.svg` + `.tex` + `.txt` | `drawing` | `short_description`, `long_description` when `.txt` exists | svg path, tex path, numeric drawing id | referenced by `[picture:...]` | one canonical object per numeric id |
| inline `[question:CODE]` | `object_reference` | none | raw marker | `references_question` | target resolved by question code |
| inline `[photo:ID:ALIAS:TEXT]` | `object_reference` | none | raw marker, alias, inline label | `embeds_photo` | target resolved by numeric photo id |
| inline `[picture:ID:ALIAS:TEXT]` | `object_reference` | none | raw marker, alias, inline label | `embeds_drawing` | target resolved by numeric drawing id |
| inline `[table:ALIAS:TEXT]` | synthetic `table_object` plus `object_reference` | optional later label text | alias and inline label | `embeds_table` | no standalone source file today |
| inline `[include:KEY]` | `object_reference` toward `html_include` | none | raw marker | `includes_object` | target resolved by file stem |
| inline `[ref:ALIAS]` | `object_reference` | none | raw marker, alias | `references_embedded_alias` | semantic link inside a source object |
| inline `[index:...]` | `text_annotation` | none | raw marker | `index_term` | not a persistent content object by default |
| inline `[class:...]` | `text_annotation` | none | raw marker | `class_marker` | semantic annotation |
| inline `[morse:...]` | `text_annotation` | none | raw marker | `morse_marker` | semantic annotation |

## Immediate Validation Expectations

- every `sections/*.md` and `slides/*.md` file should be identifiable by file
  stem and mappable from `toc` `ident` values;
- every question reference should resolve to an imported question object;
- every photo and drawing reference should resolve to a numeric media object or
  be reported as missing;
- `contents/html/*.html` and `contents/metadata/question_layout.json` are part
  of the mandatory reconstruction model.
