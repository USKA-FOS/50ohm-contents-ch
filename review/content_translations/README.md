# Accepted content translations

This directory keeps the applied reports for canonical site-content translation
runs. Each `<task-id>.applied.json` records the exact source-import audit, target
language, scope, and number of canonical payloads updated. The complete model
responses, unit checkpoints, and batch reports remain in the translation tool's
`work/ai_output/runs/<task-id>/` directory and must be preserved until human
validation and canonical integration are complete.

For the German source import `1b1bc3d6a`, the French and Italian reports each
record 217 cached translation units and 132 updated payloads. Their Luna review,
approved arbitration workbook, and import audit are stored in
`../content_reviews/` under task id
`content-review-1b1bc3d6a-deepseek-v3.2-luna-v1`.
