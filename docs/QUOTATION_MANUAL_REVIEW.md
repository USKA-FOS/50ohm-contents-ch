# Manual review of quotations in canonical Markdown

This review replaces the long CSV as the working interface. The historical CSV,
its manifest and previous human decisions are preserved.

`tools/prepare_quotation_manual_review.py` prepares an Excel index and editable
copies of the three canonical Markdown payloads for each listed object. It uses
the shared translation `source_format_contract.formatting_inventory` extractor,
without introducing another quotation parser. It does not translate, change
canonical data or infer semantic correspondence from counts.

## Prepare a review

From the orchestrator, this command reads the existing 35-candidate manifest and
writes a **new** review directory under `work/`. The output directory must not
already exist. The translation-tool checkout is the sibling directory by
default; `--translation-tool-root` can select another checkout.

```bash
pushd 50ohm-contents-ch >/dev/null
uv run --locked python tools/prepare_quotation_manual_review.py \
  --candidates-manifest review/technical_format/2026-10-24/quotation-style-alignment/manifest.json \
  --output-dir work/quotation_manual_review/2026-10-24
popd >/dev/null
```

The dated directory above is the one prepared in this session. Choose another
output directory for a new review; the tool refuses to overwrite human edits.

## Review files in VS Code

Open `work/quotation_manual_review/2026-10-24/quotation-review.code-workspace`.
The review directory contains:

```text
quotation-review.xlsx
quotation-review.code-workspace
manifest.json
README.md
sc_<object-id>/
  body.de.md
  body.fr.md
  body.it.md
sl_<object-id>/...
s_<object-id>/...
```

The Excel sheet has exactly five columns: ID, original German Markdown filename,
DE quotation, FR quotation and IT quotation. Multiple quotations create multiple
rows for the object. Each quotation is shown in full up to 15 characters,
otherwise as its first 15 characters followed by an ellipsis. Cell comments
contain the full expression, its original delimiters and the line number.
Relative hyperlinks open the corresponding editable Markdown copy.

Each language follows its own occurrence order. A row is **not** proof that its
three expressions are semantically equivalent: a missing first quote can shift
the following entries. A dash means no recognised pair at that ordinal, not
missing translated text. Existing candidate counts are diagnostic evidence,
not automatic translation-quality decisions. All 35 candidates stay in the
review even if the shared extractor corrects a historical count.

Edit the copied Markdown files directly. Keep object folders, filenames and
`manifest.json` intact. Changes to excerpt cells do not change the Markdown.

## Later reintegration

No files are imported automatically. The manifest stores the original text and
SHA-256 of all 105 payloads, the canonical paths and the editable-copy paths.
This preserves the starting point even though some current canonical changes
have not yet been committed.

After the user explicitly requests reintegration:

1. Compare each edited copy against its saved original text; unchanged copies
   require no canonical write.
2. Require each affected canonical file to retain its original SHA-256. A
   concurrent canonical change is a conflict to resolve explicitly.
3. Present and validate the exact import plan before applying it. Apply the
   normal rules for German source changes and translation review states.
4. Preserve the human edits and archive the accepted plan/import receipt in
   versioned `review/`, alongside the canonical changes when committed.

This preparation tool intentionally implements only the review stage.

## Accepted manual review of 24 October 2026

The user reviewed all 35 objects and explicitly accepted language-specific
quotation differences: not every German quotation needs quotation marks in
French or Italian. The unchanged reviewed files are part of that decision.
The import plan, exact reviewed payloads, decisions and application receipt
are archived under `review/technical_format/2026-10-24/manual-quotation-review/`.
This accepted record supersedes the earlier automatic typography output for
the affected files; do not replay that output over the human corrections.
