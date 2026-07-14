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

- some runtime UI and generator-owned page fragments already come from this
  directory;
- the generator still contains German fallback strings and base templates for
  some of those same families;
- this is intentional for now and must be documented as a partial migration,
  not mistaken for a fully cleaned generator.
