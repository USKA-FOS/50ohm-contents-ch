# Canonical Use Cases And Workflows

This document describes current target use cases and the workflows associated
with them.

It describes workflows only. It does not describe project history, migration
history, or the reasons earlier workflows changed.

## 1. Scope

This document covers the content-side workflow around:

- canonical import and update in `50ohm-contents-ch`;
- translation integration through `ai-translation-tool`;
- multilingual site reconstruction from canonical content;
- coordination boundary with `50ohm-question-pool`.

## 2. Global Rules

- canonical Git is the reference state;
- SQLite is the working-state strategy, not the source of truth;
- question objects are owned by `50ohm-question-pool`;
- `contents/questions/` in `50ohm-contents-ch` is outside the content
  reconstruction diff scope for now;
- before risky import or export operations, create a recovery tag;
- before applying translations to canonical content, the canonical repository
  should normally be clean;
- German source integration must be non-destructive toward existing canonical
  content.

## 3. External Boundary With Question Pool

The build boundary is:

- content input responsibility: `50ohm-contents-ch`, excluding question files;
- question input responsibility: `50ohm-question-pool` revision-1 catalogs;
- site output responsibility: `50ohm-contents-ch/work/build/{de,fr,it}`.

At build time, the content-side builder copies:

- `50ohm-question-pool/question_pool_rev1_ch-de.json` for German, or
  `50ohm-question-pool/builds/<lang>/question_pool_rev1_ch-<lang>.json` for
  French and Italian,
  to `contents/questions/fragenkatalog_4.json`;
- the same file again
  to `contents/questions/fragenkatalog_4pre.json`.

This copy must stay semantically identical to the source question-pool file.
The content-side build must not rewrite, enrich, or otherwise transform the
question catalog payload during staging.

The content-side workflows in this document therefore do not manage question
translation or question review.

## 4. Target Validation Condition

The target condition for the German baseline is:

`source input -> canonization -> reconstruction from canonical -> comparison = 0 differences`

For the current content workflow, that comparison excludes the
`contents/questions/` boundary handled by `50ohm-question-pool`.

## 5. Use Case UC1: First Canonical Initialization

### Goal

Create the initial canonical baseline from the existing German source site and
prove that the site input can be rebuilt from canonical data.

### Workflow

1. start from the original German content source;
2. import source data into the working SQLite model;
3. export canonical Git objects;
4. rebuild the working SQLite model from canonical only;
5. regenerate source-format content inputs from canonical;
6. compare reconstructed German inputs against the source inputs, excluding the
   question boundary;
7. commit and tag the validated canonical baseline.

### Success Criteria

- canonical directories exist for all modeled object families;
- reconstructed German content matches the source contract at `0 diff` within
  the agreed scope;
- SQLite rebuilt from canonical is internally consistent;
- the German site generator can consume the rebuilt German inputs.

## 6. Use Case UC2: Translation To French And Italian

### Goal

Translate canonical business content into `fr` and `it` while preserving all
existing translation constraints and without redefining the content model.

### Workflow

1. start from a committed canonical baseline;
2. run `ai-translation-tool` against `50ohm-contents-ch/canonical`;
3. extract translation units from canonical business objects;
4. translate batches with glossary-aware constraints;
5. persist translated unit results in the translation run cache;
6. apply translated results back into canonical target-language payload files;
7. review translated content and adjust review states as needed;
8. commit the updated canonical content;
9. rebuild the target-language site inputs and site outputs.

### Operational Rules

- translation units are derived from canonical objects;
- HTML is translated through extracted text segments, not as raw HTML blobs;
- large text bodies may be split only as derived translation units;
- `photo` and `drawing` descriptions are applied back as whole
  `<stem>.<lang>.txt` canonical files;
- applying translation results must not bypass the canonical model.

## 7. Use Case UC3: Build Sites From Canonical

### Goal

Generate the language-specific site inputs and site outputs using canonical
content plus question-pool build artifacts.

### Workflow

1. rebuild the working SQLite database from canonical content;
2. stage generator inputs for the requested languages;
3. inject the selected `question_pool_rev1_ch-<lang>.json` file into the expected
   generator question input paths `fragenkatalog_4.json` and
   `fragenkatalog_4pre.json`;
4. run the content generator per language;
5. inspect generated content under `work/build/<lang>/`.

### Success Criteria

- build completes for the requested language set;
- generated file sets are complete for the generator contract;
- support-artifact usage is traceable by report.

## 8. Use Case UC4: Integrate A New German Source Version

### Goal

Integrate a new German source revision while preserving stable object ids and
without destructively resetting the canonical baseline.

### Workflow

1. ensure the canonical repository is clean;
2. create a Git tag before the import;
3. rebuild the working SQLite model from the current canonical baseline;
4. integrate the new German source data into that working state;
5. preserve existing object ids when the source-side business object still
   matches;
6. export updated canonical objects non-destructively;
7. mark disappeared German business objects with a reversible status such as
   `to_be_deleted` instead of deleting them immediately;
8. generate a diff or audit report for changed, new, and deleted objects;
9. review German-side changes;
10. translate the objects that need target-language propagation;
11. review target-language results;
12. commit the validated canonical update;
13. create a new Git tag after the validated export;
14. rebuild multilingual sites.

### Business Rule For Deletion

- if a business object disappears from German source, it is considered removed
  for all languages;
- the whole node is marked `to_be_deleted`;
- the node content stays physically present until an explicit cleanup step;
- German, French, and Italian payloads are not partially rewritten for this
  state change.

## 9. Use Case UC5: Translation Propagation After Source Update

### Goal

Propagate German changes introduced by a new source import into `fr` and `it`
using reviewable translation states.

### Workflow

1. identify canonical objects affected by the German update;
2. update review states according to change policy;
3. select objects marked for translation;
4. run translation for the target language;
5. apply the results to canonical target-language payloads;
6. mark translated content `to_be_reviewed` or the agreed equivalent state;
7. perform human review;
8. mark approved content as approved;
9. commit the canonical update;
10. rebuild the target-language sites.

## 10. Use Case UC6: Cleanup Of `to_be_deleted` Objects

### Goal

Remove previously deactivated objects only after review confirms the deletion.

### Workflow

1. start from a committed canonical state where objects are already marked
   `to_be_deleted`;
2. confirm that the deletion is intended for the whole business object;
3. remove the canonical object directory and all of its language payloads;
4. remove or update structure placements that reference the object;
5. commit the cleanup;
6. rebuild and validate affected languages.

This cleanup is intentionally separate from the first integration of a new
German source version.

## 11. Current Implemented Workflow Pieces

Implemented and validated in the current system:

- canonical object-centric storage for content objects;
- canonical structure storage per edition;
- SQLite rebuild from canonical content;
- German site-input reconstruction from canonical content within the agreed
  scope;
- multilingual site generation from canonical content plus question-pool build
  artifacts;
- translation-unit extraction from object-centric canonical content;
- translation result reinjection into canonical target-language payloads;
- localized structure translation storage in `edition.<lang>.json`.

Partially implemented or still evolving:

- non-destructive German source update integration with automatic
  `to_be_deleted` handling;
- final cleanup workflow for deactivated objects;
- remaining elimination of support-artifact dependencies outside canonical.

## 12. Workflow Checkpoints

Recommended checkpoint discipline:

1. tag before a new source import;
2. validate canonical export and German rebuild;
3. commit the canonical update;
4. tag after the validated canonical export;
5. commit each applied target-language translation separately when possible;
6. rebuild the affected languages after each significant canonical update.

This checkpoint discipline is a documented workflow rule. It is not yet fully
enforced by tooling.

## 13. Workflow Anti-Patterns

The following are not valid operating workflows:

- deleting `canonical/` as a normal refresh strategy;
- rebuilding French or Italian by discarding existing translated canonical
  payloads;
- applying translations directly to generator outputs instead of canonical
  files;
- treating question-pool ownership as part of the content-side canonical scope;
- using runtime outputs under `work/build/` as source of truth.
