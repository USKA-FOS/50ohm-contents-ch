# Technical markup corrections — 17 October 2026

The German canonical is the reference for technical markup. Translations must not introduce mathematical markup around measurements which are ordinary text in German. Existing German formulas must remain usable formulas in the translated body.

## Applied corrections

The existing local edits were preserved first in local recovery commit `3e16d02f0`; see `local-recovery-checkpoint.json`. The following corrections remain in the working tree and have not been pushed or tagged.

- 115 deterministic representation corrections in 33 French/Italian canonical files: missing or malformed delimiters, raw quantity/unit commands, equivalent notation, and target-only markup around measurements written as plain German text.
- Two separately reviewed corrections restore the Italian dipole example in `slides/sl_6bdd356d9797/body.it.md`: **315 m dipole length at 630 m wavelength**. The previous positional comparison had swapped these values when matching translated formulas. No automatic representation repair may change numerical values.
- Total: 35 accepted cases affecting 34 files after the recovery checkpoint. German canonical bodies are unchanged.

`markup-plan.json` contains the full before/after text, source hashes, operation details and tool hashes. `markup-decisions.csv` records accepted decisions. `markup-applied.json` records application. The apply tool checks hashes and replays deterministic markup repairs before writing; a modified numerical proposal is rejected.

## Tool changes

The validator now matches technical expressions by source content rather than occurrence position. It handles equivalent unit aliases and checks braces, standalone commands and numerical indices more strictly. `--markup-only` isolates representation repairs from semantic or ambiguous differences. Repairs are proposed before application and require decisions through the existing review/import workflow.

The Astro integration also needed a corrected relative script import after the language route relocation, and an explicit non-optional return type for loaded locale labels. These fixes are separate from canonical corrections.

## Verification

Final multilingual build: **20261017-002200**, successful for DE, FR and IT. Each language has 832 generated pages and 1,665 questions. Output: `50ohm-generator-next/frontend/dist/{de,fr,it}/index.html` relative to the orchestrator. Logs: `tmp/ch-preview-logs/20261017-002200`.

- Technical-format tests: 27 passed; content tests: 62 passed.
- Focused Ruff checks and Git whitespace checks passed.
- Astro check: 0 errors, 0 warnings, 39 existing hints.
- Re-running the representation repair planner proposes **zero additional changes**.
- No translated body contains a raw `\qty`, `\unit` or `\num` outside math; no translated body has math when its entire German counterpart has none. This does not establish semantic equivalence for every formula.

`verification.json` preserves canonical hashes, build audits, counts and remaining syntax findings. The broader diagnostic inventory still has 348 findings, including missing translated bodies, localized notation and structural/semantic differences; these are not 348 confirmed defects. Six body pairs have syntax diagnostics: one German slide with an unmatched delimiter (reported against both translations), two French section delimiter cases, and French/Italian slide brace cases. They do not block this Astro build; slides are not ported to Astro. They remain explicitly recorded for separate review.

The 145 known references to question identifiers absent from the Swiss pool remain unchanged. This task builds the Astro preview only: the classical `50ohm-site-releases` output must be regenerated before publishing these canonical corrections. No remote push or tag change was performed.
