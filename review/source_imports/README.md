# German Source Import Manifests

`canonical/` is the authoritative content model. This directory stores the
versioned manifests that record which German source revision was accepted into
that model.

The workflow is:

1. fetch `origin/review/de/main`;
2. export the candidate workbook with
   `tools/export_german_source_import_review.py`;
3. review and decide every candidate requiring explicit approval;
4. run the importer only for the approved workbook;
5. commit the canonical changes and the accepted manifest together.

The `source_revision` in an accepted manifest becomes the baseline for the
next import. A dry-run report is not an accepted baseline and must not be used
as one. The manifests are versioned because they provide the audit trail for
the source-to-canonical transition; the SQLite database and generated sites do
not replace them.
