# Generator Extra Content

This directory stores multilingual content that is currently injected by the
site generator outside the canonical business-object model.

Short-term rule:

- `generator_extra_content/{de,fr,it}/` is the temporary authoritative source
  for generator-injected multilingual content;
- the forked generator consumes these resources directly during build;
- this layer is intentionally separate from the canonical model until a later
  migration decides which parts truly belong in canonical business objects.

Current resource types:

- `labels.json`: shared UI labels used by the forked generator;
- `templates/...`: language-specific template overrides for generator-owned
  injected content such as slide help pages and the localized landing page.

Important scope rule:

- this directory is a temporary multilingual resource pack for
  generator-injected runtime content;
- it is not a replacement canonical model;
- if content is actually a business object, it must remain in `canonical/`
  and not be moved here.

Current migration state:

- generator-owned runtime pages and fragments now come from this directory for
  `de`, `fr`, and `it`;
- the generator still contains technical loader stubs and label lookups, but
  the authoritative runtime text no longer belongs in `50ohm-generator`;
- validation is based on correct localized output, not on preserving old wrong
  pages unchanged;
- if a new generated page or fragment introduces visible text, that text must
  be added here rather than directly to the generator.
