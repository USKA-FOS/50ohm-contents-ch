# Multilingual Site Link Registry

> **Historical, rendered-site workflow:** This scans generated pages and
> includes generator-injected controls. It is retained for later site-output
> diagnostics. The current canonical-object link inventory is documented in
> [`CANONICAL_LINK_REVIEW.md`](CANONICAL_LINK_REVIEW.md) and uses
> `manage_canonical_link_registry.py`.

This workflow inventories hyperlinks in one generated German site and records
the corresponding French and Italian link text and targets. It also checks
whether each target can be reached in the generated language site or over
HTTP. The workbook is a human-editable review registry; it does not modify
canonical content or generated pages.

## Workbook structure

The full working registry is
`review/link_localization/site_link_registry.xlsx`. The human-facing report
requested for external destinations is
`review/link_localization/external_site_link_report.xlsx`; it contains only
rows classified as external, including their German/French/Italian text,
targets, statuses, occurrences, and check details.

The `Links` sheet has one row per distinct German link key, with:

- a SHA-256 key;
- a link type (`internal` or `external`), classified from the German target;
- text and target link columns for German, French, and Italian;
- suggested French/Italian targets when a relative German link is missing;
- a status column for each language;
- a count of German occurrences.

When a bare fragment such as `#section` is used, its meaning depends on the
current page. Its SHA-256 key therefore includes both the exact German href
and the German source page. Other links are keyed by the exact German href.

The scan covers generated page HTML files directly inside each language
directory. It excludes nested HTML demo and test files bundled under `assets/`
by third-party libraries; those are not pages in the 50Ohm site. It includes
all anchors in each generated site page, including content links and page
controls.

The `Occurrences` sheet preserves the page, anchor order, visible text, and
observed target href for each occurrence. It is useful when the same target is
used with different wording or in several page contexts. French and Italian
anchors are aligned with German anchors by page and source order. If a page's
link counts differ, exact href sequences are used to align unchanged links
around gaps; uncertain unmatched anchors stay unmatched instead of shifting
all later rows.

Internal links are validated against the generated language site: target files
and fragments must exist. A relative internal href must also be identical to
the German href. If its French or Italian anchor is missing, the workbook keeps
the observed link blank, reports `missing link`, and offers the German relative
href in the corresponding `Suggested link` column. This suggestion is not
written into canonical content or misrepresented as an observed link.

External links are checked over HTTP(S), grouped by host and checked
sequentially within each host. At most two hosts are checked concurrently by
default. On HTTP 429 the checker waits for `Retry-After` and retries that URL
once; if the requested wait exceeds the configured maximum, it records
`HTTP 429` without retrying early. If that retry still returns 429, further
URLs for that host are marked `HTTP 429 (host paused)` and are not probed during
this run. Set `--retry-429` and `--max-retry-wait` to adjust this behavior.
Email and telephone links are recorded as syntactically present because their
destinations cannot be probed as web pages.

The `Manifest` sheet records the generated release id, source commits, scan
time, and link counts. The `Checks` sheet is replaced on each check run with
the latest result and diagnostics for each tested target.

## Status meanings

- `not found`: the target page or fragment is missing from the local generated
  site, or an external HTTP URL returned 404 or 410.
- `missing link`: German has a relative internal link but the generated
  French/Italian page has no corresponding anchor.
- `missing external link`: German has an external link but no corresponding
  anchor was found in the generated French/Italian page. No URL is suggested;
  the localized external destination needs a separate decision.
- `relative link differs`: the localized internal href does not exactly match
  the German relative href.
- `found`: the local page and any fragment exist, or an HTTP target returned
  successfully after redirects. `mailto:` and `tel:` targets are only checked
  for syntactic presence.
- `verified`: a human has confirmed that the localized link is the correct
  destination for that language and context.
- Other explicit status values include HTTP response codes such as `HTTP 401`,
  `HTTP 403`, `HTTP 429`, and `HTTP 500`, `HTTP 429 (host paused)` for URLs
  deferred after a host-level rate limit, plus `timeout`, `network error`, and
  `local check inconclusive`. They describe the check outcome; they are not all
  proof that a destination is broken.

The checker assigns the machine results described above; it never assigns
`verified`. A reviewer sets `verified` in the `Links` sheet after confirming
both the target and its intended language/context. A missing or changed
internal target downgrades a previous verification. An inconclusive network
result preserves a prior human `verified` decision; the exact HTTP response
remains in `Checks`.

The upstream translation pipeline uses the same source-owned rule for
relative/internal Markdown and HTML links: the target href must be copied
exactly from German and cannot be omitted. External URLs are not rewritten by
the checker; language-specific destinations require an approved mapping.

## Commands

Run from `50ohm-contents-ch`. Both commands are writes to the review workbook;
neither changes canonical data or the release site.

Scan the current generated `de`, `fr`, and `it` sites. If the default workbook
already exists, verified mappings are reused only when the German SHA-256 key
is unchanged:

```bash
UV_CACHE_DIR=../tmp/uv-cache uv run --locked python tools/manage_site_link_registry.py scan
```

Check local internal files/fragments and external HTTP targets, then update
statuses and the `Checks` sheet:

```bash
UV_CACHE_DIR=../tmp/uv-cache uv run --locked python tools/manage_site_link_registry.py check
```

Create the external-only Excel report from the checked full registry. This
filters the existing workbook without another network run; no internal-link
rows appear in the report:

```bash
UV_CACHE_DIR=../tmp/uv-cache uv run --locked python tools/manage_site_link_registry.py external-report
```

Options include `--site-root`, `--output` for `scan`, and `--workbook`,
`--site-origin`, `--timeout`, and `--workers` for `check`. See the script's
`--help` for exact arguments.

## Initial inventory

The first workbook was generated from release
`beta-2026-10-17-QP_Revision_3.0.4` in `50ohm-site-releases`. The release
manifest identifies content commit `b2477352a5c4e84ae7622ec47ff9fcba92c67ff1`
and generator commit `19af725826dc4b560d93d155d6079e1fe7630e33`.

The release contains 1,180 top-level generated HTML pages per language, with
30,070 German anchor occurrences and 4,416 distinct German link keys. Six
Italian anchors remain unmatched in `A_psk.html` and `NEA_psk.html`; the
workbook shows these missing mappings explicitly rather than shifting later
links. The `Checks` sheet and status columns report link-check results
separately from structural matching findings.

The missing Italian source references were corrected in canonical content on
2026-10-23. The correction details and generated relative hrefs are recorded in
[`review/link_localization/internal_link_correction_2026-10-23.json`](../review/link_localization/internal_link_correction_2026-10-23.json).
The release inventory above remains a historical snapshot; it was not rebuilt
after that canonical correction.

External check results for the initial inventory, checked on 2026-10-23. The
external-only workbook contains 690 link keys per language. All status cells
have explicit values; rate-limited targets are not left blank.

| Language | External results |
| --- | --- |
| German | 139 found; 5 not found; 3 HTTP 429; 536 host-paused after HTTP 429; 7 other explicit HTTP/network statuses |
| French | 132 found; 12 not found; 3 HTTP 429; 536 host-paused after HTTP 429; 7 other explicit HTTP/network statuses |
| Italian | 134 found; 10 not found; 3 HTTP 429; 536 host-paused after HTTP 429; 7 other explicit HTTP/network statuses |

External 404s and the explicit HTTP/network outcomes are listed with URLs in
the report's `Checks` sheet. Internal-link corrections are maintained
separately in canonical content, not included as rows in this report.
`HTTP 429 (host paused)` means the checker waited and retried one URL on that
host, received another 429, then deferred its remaining URLs for this run
instead of sending more requests.
