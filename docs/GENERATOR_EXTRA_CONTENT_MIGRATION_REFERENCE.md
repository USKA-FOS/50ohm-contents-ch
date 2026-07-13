# Generator Extra Content Migration Reference

This document describes the current state of the temporary
`generator_extra_content` layer.

It focuses on the current design and migration state only.
It does not narrate historical iterations beyond what is necessary to explain
the present architecture and the remaining work.

## Purpose

The site generator still owns a set of multilingual user-visible fragments
that are not yet represented as canonical business objects.

The current strategy is:

- keep canonical business content in the canonical model;
- move generator-owned multilingual content into
  `generator_extra_content/{de,fr,it}/`;
- make the generator branch in `translator/sites/app/generator/` consume those resources directly;
- keep generation source-driven rather than patch-driven.

This temporary layer exists to produce correct multilingual sites now, without
mixing additional generator-owned structures into the canonical business model
before that model is fully stabilized.

## What `generator_extra_content` Is

`generator_extra_content` is not a business-object repository.

It is a generator-side multilingual resource pack staged into the generator
input tree during build:

- source location:
  `50ohm-contents-ch/generator_extra_content/{de,fr,it}/`
- staged build location:
  `50ohm-contents-ch/work/generator-input/<lang>/generator_extra_content/`
- consumer:
  `translator/sites/app/generator/`

Typical resource types:

- `labels.json`: language-dependent UI strings consumed by templates;
- `templates/...`: language-specific template fragments or full template
  overrides for generator-injected pages.

## Current Build Rule

During multilingual build:

1. canonical content is staged for one target language;
2. `generator_extra_content/<lang>/` is copied beside that staged content;
3. `generator` detects the target language from the staged input root;
4. `generator` loads localized generator resources, with German fallback;
5. the site is generated directly from language-aware sources.

The intended end state is that generator-owned multilingual strings are solved
at generation time and not rewritten afterward by string replacement.

## What Has Already Left the Patch Layer

The following patch families are now absorbed by `generator` or by
language-specific resources in `generator_extra_content` and should no longer
require post-build replacement:

- `html-lang`
- `page-title-and-brand`
- `nav-start`
- `nav-lernen`
- `nav-suche`
- `nav-infos`
- `nav-pruefung`
- `footer-developed-with`
- `footer-developed-by-team`
- `footer-uska-offer`
- `footer-impressum`
- `footer-datenschutz`
- `button-slides`
- `button-download-tools`
- `button-edit-content`
- `button-open-issue`
- `button-show-diff`
- `alert-error`
- `alert-connection-error`
- `solution-button-text`
- `solution-aria-label`
- `solution-title`
- `solution-question-label`
- `solution-answer-label`
- `solution-wrong-label`
- `solution-card-title`
- `carousel-previous`
- `carousel-next`
- `index-online-lernen`
- `index-online-lernen-text`
- `index-h5-kurse`
- `index-kurse-text`
- `index-einsteiger`
- `index-upgrade`
- `index-full-course`
- `index-uska-chat-text`
- `index-ausbildung-button`
- `index-mitglied-heading`
- `index-mitglied-text`
- `index-mitglied-button`
- `index-videokurse-heading`
- `index-videokurse-text-1`
- `index-videokurse-text-2`
- `index-video-button-n`
- `index-video-button-ne`
- `index-video-button-a`
- `index-kurse-heading-2`
- `index-kurse-text-2`
- `index-kurse-button`
- `index-coaching-text`
- `index-coaching-button`
- `index-fragenkatalog-heading`
- `index-fragenkatalog-text-1`
- `index-fragenkatalog-text-2`
- `index-fragenkatalog-button`
- `index-photo-credit`

These elements now come from generator resources.

## Current Generator Resource Split

The current split is:

- repeated UI labels are stored in `generator_extra_content/*/labels.json`
- generator-owned page bodies can be stored as template overrides under
  `generator_extra_content/*/templates/...`

### A. Solution-related Labels

These are now generated from localized labels and no longer require patching.

Current authoritative generator sources:

- `translator/sites/app/generator/templates/html/question.html`
- `translator/sites/app/generator/templates/html/solution.html`
- `translator/sites/app/generator/templates/html/solution_question.html`

### B. Review-widget Alert Messages

These are now generated from localized labels and no longer require patching.

Current authoritative generator sources:

- `translator/sites/app/generator/templates/html/section-review-widget.html`
- `translator/sites/app/generator/templates/html/chapter-review-widget.html`

### C. Index Page Content

The landing page is now localized through language-specific template overrides:

- `50ohm-contents-ch/generator_extra_content/fr/templates/html/index.html`
- `50ohm-contents-ch/generator_extra_content/it/templates/html/index.html`

The German base template remains in:

- `translator/sites/app/generator/templates/html/index.html`

## Current Validation Result

Current multilingual validation shows that `fr` and `it` UI generation works
without any post-build UI patch step.

Current validation reports indicate:

- the generated sites build successfully for `fr` and `it`
- the migrated UI families are produced directly at generation time

This means the current system works and the UI layer is now produced directly
from source-level localization.

## Operational Consequence

The build pipeline now relies on localized generator resources directly.

Obsolete patch-time fallback machinery can be removed from the repository when
it is no longer needed for audit or archaeology.

## Scope Boundary

This layer is intentionally limited to generator-owned multilingual fragments.

It must not be used as a silent second canonical model for business objects.

If a piece of content is actually a business object, it belongs in the
canonical model and not in `generator_extra_content`.

## Presentation Summary

For project discussion, the current position can be summarized as follows:

- canonical business content is handled by the canonical model;
- generator-owned multilingual fragments are temporarily isolated in
  `generator_extra_content`;
- the forked generator now consumes these resources directly for `de`, `fr`,
  and `it`;
- the previous UI patch scope for `fr` and `it` has been migrated to
  source-time generation;
- the remaining work in this area is cleanup or later model refactoring, not
  additional UI translation migration.
