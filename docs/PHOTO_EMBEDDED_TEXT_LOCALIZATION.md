# Photo Embedded Text Localization

## Status

This document records a proposed workflow for photographs that contain visible
German text. It is a planning reference only. The workflow has not yet been
applied to photo `270`.

## Problem

Some canonical photographs contain German labels directly in the bitmap. A
translated page therefore still displays German text, for example:

- `https://50ohm.jp2s.ch/fr/photos/270.png`

Ordinary text translation cannot localize these labels because they are part
of the raster image.

## Mandatory Display Rule

When a photo containing visible text is selected for localization:

- create localized DE, FR, and IT SVG variants;
- use the SVG drawing everywhere the visual is displayed;
- replace every editorial `[photo:<id>:...]` use with the corresponding
  drawing reference in every language;
- do not leave a page displaying the raster photo directly;
- retain a cleaned raster only as a technical background dependency of the TeX
  drawing when required.

The fact that a PNG remains present in a build as a drawing dependency is not
an error. The error is a generated page that still references that PNG as its
displayed content.

After all display references have migrated, remove obsolete annotated photo
objects that have no remaining business or technical use. Keep or replace the
background dependency with a pure photo containing no added explanatory text.

## Preferred Strategy

Use the same general composition principle as drawing `689`:

1. retain a language-neutral raster image as the visual background;
2. remove the embedded German labels from that background;
3. place the labels with TeX;
4. generate language-specific DE, FR, and IT SVG files;
5. make the site reference the localized drawing asset instead of the original
   German-labelled photograph.

This is preferable to maintaining three independently edited raster images
because label content remains reviewable as text and positioning remains
shared between languages.

## Required Steps

1. Record the source photo id, canonical object id, proposed drawing id, and
   every canonical object that displays the photo.
2. Search all DE, FR, and IT payloads for `[photo:<id>:` and search drawing TeX
   for `foto/<id>` to distinguish direct display from background inclusion.
3. Verify that the intended drawing identifier is available. Do not assume the
   photo id is also free in the drawing namespace.
4. Create a cleaned background image without embedded text. This is normally a
   manual image-editing operation.
5. Create a German TeX drawing that includes the cleaned background and places
   the original German labels at explicit coordinates.
6. Extract the visible labels through the drawing-text localization workflow.
7. Add or correct reusable terminology in the shared glossary.
8. Generate French and Italian TeX variants by changing text only. Geometry,
   background, lines, colors, and other technical properties must remain
   aligned with German.
9. Render and visually review the DE, FR, and IT SVG variants.
10. Add the drawing and its localized asset metadata to canonical storage,
    including both `canonical_file` and generator `source_path` values.
11. Replace every `[photo:<id>:<alias>:<label>]` marker with the matching
    `[picture:<drawing-id>:<alias>:<label>]` marker in all affected DE, FR, and
    IT payloads. For example, `[photo:205:...]` becomes `[picture:689:...]`.
    Preserve the language-specific label and alias unless a reviewed correction
    requires a change.
12. Regenerate the affected `object.references.json` entries so they declare
    `embeds_drawing`, `drawing_id`, and the selected drawing identifier rather
    than the former photo target.
13. Search the complete canonical tree again and require zero remaining direct
    `[photo:<id>:` markers for every migrated photo.
14. Rebuild all three sites.
15. Search generated HTML and require zero direct `photos/<id>.<ext>` display
    references for every migrated photo. Every former display location must
    instead reference `pictures/<drawing-id>.svg`.
16. Verify references to the old annotated photo object. If none remain, remove
    the obsolete canonical photo object in a dedicated reviewed cleanup.
17. Verify that every retained raster background is a pure photograph rather
    than an image carrying added language-dependent labels.

## Complexity And Risks

The implementation is moderately complex but follows an existing process. The
main manual work is cleaning the raster background and positioning the labels.

The main risks are:

- changing technical or visual information while cleaning the bitmap;
- overwriting a canonical photo that is still published directly as a PNG;
- choosing a drawing identifier that is already in use;
- leaving an old `photo` reference in one of the source texts;
- changing geometry between languages instead of changing text only;
- omitting localized asset metadata and silently excluding an SVG from a
  translated site build.

## Validation Criteria

The conversion is complete only when:

- every previous use of the German-labelled photo has been accounted for;
- DE, FR, and IT use the intended localized SVG;
- the background and non-text geometry are identical across languages;
- all visible labels have been reviewed;
- the multilingual build succeeds with identical file sets for all three
  languages;
- no generated page still references the obsolete German-labelled bitmap.

## Shared Background Constraint

Before cleaning a canonical photo, distinguish these uses:

- direct publication through a marker such as `[photo:205:...]`, which emits
  `/photos/205.png`;
- indirect inclusion as a raster background in drawing TeX, such as
  `\includegraphics{foto/205}` in drawing `689`.

If both uses exist, cleaning the existing canonical PNG in place also changes
the directly published photo. The implementation must therefore either:

- migrate every direct display use to the localized drawing, which is mandatory
  for an image selected for translation; and
- either use the cleaned canonical photo only as a background dependency or
  preserve the original photo and create a separate cleaned background asset.

Current example: photo `205` is used directly by canonical section
`sc_2588300696d4` and slide `sl_e50538afb0d9`, and indirectly as the background
of drawing `689`.

## First Known Candidate

- photo `270`, currently visible as `/fr/photos/270.png`

Additional candidates should be inventoried before implementation so they can
be processed as one controlled batch.

## Batch Inventory

The reviewer inventory is stored outside Git at:

- `work/photo_review/Review_result.xlsx`
- sheet `PNG`

It covers the 157 flattened canonical PNG review copies. Before any asset or
reference change, record at least:

| Source photo id | Canonical photo object | Target drawing id | Direct canonical users | TeX background users | Status |
| --- | --- | --- | --- | --- | --- |
| 205 | `ph_24f64631b390` | 689 | `sc_2588300696d4`, `sl_e50538afb0d9` | drawing 689 | existing SVG; direct references still need migration |
| 209 | `ph_0eaa421db7f7` | 748 | `sc_8162bd5007c7` | none | obsolete German-annotated composite; migrate direct references, then remove if unused |
| 168 | `ph_eb7f115b13b4` | 748 | none | drawing 748 | retain as the pure photographic background |
| 270 | to be confirmed | to be assigned | to be inventoried | none known | candidate |

Add the remaining reviewed candidates to this table before implementation.

### Reviewer Categories

The workbook currently identifies 30 photos through three overlapping review
columns. These classifications are reviewer input and do not by themselves
authorize an implementation choice.

Marked `conversion tex SVG` (`20`):

- `66`, `167`, `178`, `190`, `205`, `209`, `247`, `248`, `257`, `259`
- `260`, `261`, `264`, `265`, `266`, `267`, `268`, `270`, `271`, `307`

Marked `to_be replaced` (`9`):

- `79`, `80`, `86`, `91`, `99`, `102`, `103`, `145`, `322`

Marked `photo_of_text_document` (`7`):

- `79`, `80`, `91`, `99`, `102`, `103`, `319`

Category intersections:

- `79`, `80`, `91`, `99`, `102`, and `103` are both replacement candidates
  and photos of text documents;
- `319` is marked only as a photo of a text document. Its selected treatment is
  `localized_document_images`, not TeX/SVG composition;
- `86`, `145`, and `322` are replacement candidates not marked as text
  documents.

Reviewer comments that affect processing:

- `79`, `80`, `86`, `91`, `99`, `102`, `103`, `145`: adapt for Switzerland;
- `167`: adapt for Switzerland despite being marked as containing no text;
- `190`: contains a woodland sign with `Sportgerät`;
- `205`: corrected photo; handle its direct display uses before cleanup;
- `209`: an equivalent localized drawing already exists as drawing `748`;
- `319`: text document; use reviewed language-specific document images;
- `322`: map that may need replacement.

Rows `167` and `205` are marked `No Text` in the language review columns but
remain explicit TeX/SVG conversion candidates. Preserve this reviewer decision
until each case is visually assessed; do not remove them from scope through an
automatic text-detection filter.

### Decision Required Per Candidate

Before implementation, assign one explicit treatment to every marked photo:

- `shared_photo_plus_tex_svg`: clean shared photo background plus localized
  DE/FR/IT TeX and SVG;
- `localized_document_images`: separate reviewed DE/FR/IT document images;
- `replacement_asset`: replace with a new Swiss-appropriate asset;
- `existing_drawing_migration`: replace direct photo references with an
  existing localized drawing, as for photo `209` and drawing `748`;
- `no_change`: only after a documented reviewer correction to the inventory.

The selected treatment must be recorded before changing canonical files so the
batch remains auditable and partial migrations can be detected.

Current explicit treatment decision:

- `319`: `localized_document_images`.

### Existing 168 / 209 / 748 Pattern

Drawing `748` already implements the intended split:

- photo `168` is the pure photographic background;
- drawing `748` includes `foto/168` and supplies localized labels through TeX;
- photo `209` is the older German-annotated composite;
- slide `sl_bb865457964e` already displays drawing `748`;
- section `sc_8162bd5007c7` still displays photo `209` in all three languages.

The batch correction must migrate the section from `[photo:209:...]` to
`[picture:748:...]`. Once repository-wide and generated-site checks confirm
that photo `209` is unused, its canonical object can be removed. Photo `168`
must remain as drawing `748`'s background dependency.

## Document Image Exception

Some reviewed candidates may be photographs or scans of documents whose text
is the primary content rather than an annotation placed over a photograph.
Those cases may use separate DE, FR, and IT image assets instead of a shared
clean raster plus TeX overlay when a genuine localized document already
exists.

The same display rule still applies:

- the site must select the appropriate language-specific asset everywhere;
- the German document image must not remain visible on FR or IT pages;
- the choice between localized document images and TeX/SVG composition must be
  recorded per candidate before implementation.

## Batch Verification Commands

For one source photo and target drawing:

```bash
rg -n '\[photo:205(?::|\])|foto/205' canonical

rg -n 'photos/205\.(png|jpg|jpeg|webp)|pictures/689\.svg' \
  work/build/de work/build/fr work/build/it \
  -g '*.html'
```

Interpretation after migration:

- `foto/205` may remain in drawing TeX as a background dependency;
- `[photo:205:...]` must not remain in canonical editorial payloads;
- generated HTML must not display `photos/205.png`;
- every former display location must use `pictures/689.svg`.
