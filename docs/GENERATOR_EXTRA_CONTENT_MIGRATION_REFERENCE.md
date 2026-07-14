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
- make the generator branch in `translator/50ohm-generator/` consume those resources directly;
- keep generation source-driven rather than patch-driven.

This temporary layer exists to produce correct multilingual sites now, without
mixing additional generator-owned structures into the canonical business model
before that model is fully stabilized.

The target of this sanitation work is not "zero diff" at any cost.

The real target is:

- generator-visible multilingual runtime content must no longer be authored in
  the generator source tree;
- migrated content must be owned by localized resources outside the generator;
- intentional output differences are acceptable when they correct previously
  wrong German-only or partially localized pages.

## Current Status

The current migration is intentionally partial.

What is already true:

- the validated multilingual build keeps the rendered output under control;
- the migrated generator-owned UI families are resolved at generation time
  from `generator_extra_content`;
- the build no longer relies on a post-build translation patch for those
  migrated families.

What is not yet true:

- the generator is not yet a fully minimal shell containing only pure build
  mechanics;
- some technical fallbacks and loader structures still exist in
  `translator/50ohm-generator/`;
- that remaining material is still part of the generator source tree and must
  continue to shrink until runtime-visible multilingual content is fully owned
  by localized resources.

This document therefore describes a controlled intermediate state:

- output behavior is stabilized enough to validate the migration;
- multilingual generator-owned content is being isolated;
- remaining cleanup work is still explicitly visible and must not be confused
  with canonical business content.

## What `generator_extra_content` Is

`generator_extra_content` is not a business-object repository.

It is a generator-side multilingual resource pack staged into the generator
input tree during build:

- source location:
  `50ohm-contents-ch/generator_extra_content/{de,fr,it}/`
- staged build location:
  `50ohm-contents-ch/work/generator-input/<lang>/generator_extra_content/`
- consumer:
  `translator/50ohm-generator/`

Typical resource types:

- `labels.json`: language-dependent UI strings consumed by templates;
- `templates/...`: language-specific template fragments or full template
  overrides for generator-injected pages.

Current checked-in resources are:

- `generator_extra_content/{de,fr,it}/labels.json`
- `generator_extra_content/{de,fr,it}/templates/slide/help.html`
- `generator_extra_content/{de,fr,it}/templates/slide/next.html`
- `generator_extra_content/{de,fr,it}/templates/html/index.html`
- `generator_extra_content/{de,fr,it}/templates/html/kurse-liste.html`
- `generator_extra_content/{de,fr,it}/templates/html/kurse-karte.html`
- `generator_extra_content/{de,fr,it}/templates/html/patenkarte.html`
- `generator_extra_content/{de,fr,it}/templates/html/todo.html`

## Current Build Rule

During multilingual build:

1. canonical content is staged for one target language;
2. `generator_extra_content/<lang>/` is copied beside that staged content;
3. `generator` detects the target language from the staged input root;
4. `generator` loads localized generator resources, with German fallback;
5. the site is generated directly from language-aware sources.

The intended end state is that generator-owned multilingual strings are solved
at generation time and not rewritten afterward by string replacement.

The migration validation rule is therefore:

- no unintended regressions;
- no new generator-owned multilingual runtime text in the generator;
- intentional diffs are acceptable when they replace previously incorrect
  output with the localized authoritative version.

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

- `translator/50ohm-generator/templates/html/question.html`
- `translator/50ohm-generator/templates/html/solution.html`
- `translator/50ohm-generator/templates/html/solution_question.html`

### B. Review-widget Alert Messages

These are now generated from localized labels and no longer require patching.

Current authoritative generator sources:

- `translator/50ohm-generator/templates/html/section-review-widget.html`
- `translator/50ohm-generator/templates/html/chapter-review-widget.html`

### C. Index Page Content

The landing page is now localized through language-specific template overrides:

- `50ohm-contents-ch/generator_extra_content/de/templates/html/index.html`
- `50ohm-contents-ch/generator_extra_content/fr/templates/html/index.html`
- `50ohm-contents-ch/generator_extra_content/it/templates/html/index.html`

### D. Generator-Owned Utility Pages

The following generated pages are now also localized through
`generator_extra_content` for all three languages:

- `kurse_vor_ort_liste.html`
- `kurse_vor_ort_karte.html`
- `patenkarte.html`
- `todo.html`

Their authoritative sources are:

- `generator_extra_content/{de,fr,it}/templates/html/kurse-liste.html`
- `generator_extra_content/{de,fr,it}/templates/html/kurse-karte.html`
- `generator_extra_content/{de,fr,it}/templates/html/patenkarte.html`
- `generator_extra_content/{de,fr,it}/templates/html/todo.html`

### E. Slide Help and Slide Navigation Fragments

The reveal.js help and next-page fragments are now provided through localized
template overrides:

- `50ohm-contents-ch/generator_extra_content/de/templates/slide/help.html`
- `50ohm-contents-ch/generator_extra_content/fr/templates/slide/help.html`
- `50ohm-contents-ch/generator_extra_content/it/templates/slide/help.html`
- `50ohm-contents-ch/generator_extra_content/de/templates/slide/next.html`
- `50ohm-contents-ch/generator_extra_content/fr/templates/slide/next.html`
- `50ohm-contents-ch/generator_extra_content/it/templates/slide/next.html`

## What Still Remains Inside the Generator

The generator should now be understood as a runtime consumer of localized
resources, not as the authority for multilingual page content.

What may still remain inside the generator is limited to the following:

### 1. Technical fallback behavior

Some templates, renderers, or code paths may still carry fallback behavior for
defensive execution if localized resources are missing.

Current role:

- they are technical safeguards, not authoritative content;
- they must not be treated as the source for normal multilingual builds;
- if a user-visible runtime text is still effectively owned there, that is a
  cleanup gap to remove.
- they are not intended to be the authoritative multilingual source.

### 2. Non-authoritative runtime stubs

The generator still contains template files at the original paths, but these
now act only as non-authoritative stubs documenting that the real runtime
content lives in `generator_extra_content`.

Current role:

- preserve the template path contract expected by the generator;
- keep runtime authority outside `50ohm-generator`;
- make it explicit that these templates must not become a second source of
  multilingual page content.

### 3. Non-runtime documentation, tests, and comments

German text also remains in generator documentation, tests, CSS comments, and
LaTeX helper files.

These are not part of the multilingual site-content migration boundary unless
they directly affect generated runtime output.

## Boundary Rule

The migration rule is not "move every German string out of the repository."

The actual rule is:

- move generator-owned multilingual runtime content out of hard-coded
  generator paths into language-scoped resources where practical;
- keep pure technical fallbacks allowed for now, as long as the validated
  builds remain correct;
- do not move canonical business objects into `generator_extra_content`;
- do not silently invent a second content model inside the generator.

## Current Validation Result

Current multilingual validation shows that `de`, `fr`, and `it` UI generation
works without any post-build UI patch step.

Current validation reports indicate:

- the generated sites build successfully for `de`, `fr`, and `it`
- the migrated UI families and generator-owned utility pages are produced
  directly at generation time
- differences against an older accepted baseline must now be interpreted,
  not blindly rejected, because some previous pages were themselves wrong or
  incompletely localized

This means the current system works and the runtime generator-owned text layer
is now produced directly from source-level localization for the migrated
families.

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
- the previous UI patch scope has been migrated to source-time generation;
- the remaining work in this area is explicit cleanup of remaining
  generator-resident runtime content or later migration of that content into
  canonical objects once the model is ready.
