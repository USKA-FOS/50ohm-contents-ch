# Accepted content reviews

For each accepted content-review task, keep the complete persisted review report
(`*.review.json`), the human-approved arbitration workbook (`*.approved.xlsx`),
and the canonical import audit (`*.import.json`) together. The audit records the
workbook and report hashes and every applied correction. Provider responses and
checkpoints remain in the translation tool's `work/` directory; do not replace
or discard them before the accepted canonical result is verified.

The `site-content-review-luna-mistral-v1.json` file predates this convention
and is retained as its historical accepted audit.
