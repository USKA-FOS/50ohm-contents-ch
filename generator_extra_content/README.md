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
  injected content such as slide help pages.
