# Accepted technical-format arbitration — 2026-10-16

This record applies the reviewed decisions in `arbitrage-v3.xlsx` to the Swiss canonical content. It preserves localized formula symbols and labels, corrects the reviewed unit/syntax/value defects, and normalizes deterministic equivalent notation to the German form.

Human decisions applied:

- `AI509` (`solutions/s_13c027bfe08e`): change both German occurrences of 1450 MHz to 1450 Hz; FR/IT already contain the calculated value.
- `AB409` (`solutions/s_4ef73a36fc9d`): use lowercase `p` in the Italian equation, matching the German equation. This is included in apply-pass-1.

`accepted-manifest.json` records the workbook and input hashes, every applied correction, and before/after hashes for each changed canonical file. The post-application scanner still reports localized notation and unpaired structural cases; those are recorded as findings, not treated as automatic errors.
