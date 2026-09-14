# German Fallback Drawing Text Integration

This directory records the human review imported on 2026-09-14.

- The source workbook contained 225 text/drawing tuples.
- Exactly 131 rows marked `to_be_translated` were applied.
- The import touched 73 canonical drawing objects and produced or updated 73
  French and 73 Italian TeX files.
- The complete worksheet is preserved as
  `fallback_drawing_text_review.csv`.
- `fallback_drawing_text_import.audit.json` records the workbook hash, exact
  canonical references, selected-row counts, and replacement counts.
- `[[BR]]` means a line break without a hyphen; `[[BR-]]` means a hyphen
  followed by a line break.

No SVG was rendered during this import. Render the changed TeX assets and then
rebuild the complete visual-review export:

```bash
uv run python tools/render_localized_drawing_svgs.py --from-import-report --skip-existing
python tools/prepare_drawing_svg_review.py
```

The canonical TeX and metadata changes must be committed before rendering so
the text integration remains independently recoverable and reviewable.
