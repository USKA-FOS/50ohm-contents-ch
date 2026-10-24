# Canonical Link Review

This workflow reads links from the canonical object model. The human-facing
workbook is an **external-link report**, keyed by outbound links in the German
canonical text. It replaces the generated-site scan as the source for this
review. The earlier site-based registry remains available as a separate
diagnostic of rendered pages and template-added controls; its workbook is not
the canonical link inventory.

## Scope and source

The tool reads active objects under `canonical/`, follows each
`object.meta.json` text slot, and scans the text files listed for `de`, `fr`,
and `it`. It recognizes active Markdown inline links, HTML `<a href>` links,
and DARCdown `[ref:…]` and `[sec:…]` references while checking source
structure. Markdown comment lines beginning with `%`, HTML comments, fenced
code blocks, and inline-code examples are ignored.
The workbook lists only outbound targets present in German, grouped as `CH`,
`DE`, `Other external`, or `GitHub`. Relative links and canonical `[ref]`/`[sec]`
references are excluded from both `Links` and `Occurrences`. It does not scan
generated site pages, generator templates, page navigation, stylesheets,
scripts, or plain URLs that are not marked as links in the source.

The canonical alignment rule is: every active German link must have a
corresponding link in each existing French and Italian text, and French or
Italian text must not introduce links absent from German. Swiss (`CH`) targets
may be localized. German (`DE`) and other non-Swiss targets should remain
identical to German for now. The scan flags omissions and language-only links;
it does not create translations for objects whose localized text is absent or
marked `to_be_translated`.

Each reported occurrence retains its canonical object ID and type, text slot,
source file, link text, target, and corresponding target in each language. The
`Links` sheet groups external links under a SHA-256 key; `Occurrences` retains
object-level detail. The `Manifest` distinguishes missing links in existing
localized files from German-only objects with no localized file.

When corresponding language files have the same number of links, the tool
matches them by source order. If counts differ, it aligns unchanged targets
and marks missing or language-only links. Equal-count target changes remain
visible in the language columns for review.

## Target categories

The report uses these target categories for German-keyed links and individual
URL checks:

- `canonical object reference`: DARCdown `[ref:…]`;
- `canonical section reference`: DARCdown `[sec:…]`;
- `relative internal target`: a relative path or fragment;
- `same-site absolute target`: an absolute link to `50ohm.uska.ch`. It is
  excluded from the external-link workbook and should be changed to a relative
  path;
- `CH`: a target whose host or email domain ends in `.ch` or `.swiss`, including
  BAKOM and other Swiss government sites;
- `DE`: a target whose host or email domain ends in `.de`, including `darc.de`
  and `50ohm.de`. Matrix room permalinks naming the DARC `darc.de` server are
  also categorized as `DE`;
- `GitHub`: GitHub web properties. They are inventoried but never requested;
- `Other external`: another HTTP(S) target;
- `contact URI`: a `mailto:` or `tel:` target without a recognized `.ch` or
  `.de` domain.

`Target category DE` classifies the German href and applies to its whole
cross-language link key. The `Links` and `Occurrences` sheets therefore do not
repeat category columns for FR and IT. Swiss targets may differ by language;
DE and other non-CH targets are expected to match the German target. Internal
relative links, same-site absolute links, and canonical references do not
appear in the external-link sheets. Email addresses with `.ch` or `.de`
domains retain those categories but are marked not web-checkable. The `Checks`
sheet records the category of each actual HTTP(S) URL. GitHub links receive
the explicit status `skipped (GitHub)` and are not sent over HTTP.

## HTTP check policy

The checker builds one set of normalized HTTP(S) URLs across all reported
objects and all three languages. Contact URIs may be categorized as `CH` or
`DE`, but remain marked `not web-checkable`. URL fragments are removed because
they are not sent to the web server. Each distinct URL is requested at most
once in one run; repeated occurrences and language uses reuse that result.
GitHub-family hosts are excluded before requests are made.

Requests are made sequentially by host. After an HTTP 429, remaining URLs on
that host are recorded as `HTTP 429 (host paused)` and deferred to a later run.
The checker does not immediately retry the same URL. HTTP status is a machine
reachability result; it does not assign the human status `verified`.

The SHA key is calculated from the exact German external href, so the same URL
shares one key across objects and source markup. This key retains human
`verified` status across scans only when the key and language target are
unchanged. A changed German target gets a new key; it does not inherit the
previous decision. Relative paths use object-and-slot-scoped keys internally,
but are excluded from the workbook.

## Commands

Run from `50ohm-contents-ch`. The scan reads canonical files and writes the
review workbook only. It does not modify canonical objects or generated sites.

```bash
UV_CACHE_DIR=../tmp/uv-cache uv run --locked python tools/manage_canonical_link_registry.py scan
```

The default output is
`review/link_localization/canonical_link_registry.xlsx`. Check the unique
non-GitHub HTTP targets and update statuses and the `Checks` sheet:

```bash
UV_CACHE_DIR=../tmp/uv-cache uv run --locked python tools/manage_canonical_link_registry.py check
```

Options:

```text
scan  --canonical-root PATH  --output PATH
check --workbook PATH        --timeout SECONDS
```

The workbook's `Manifest` records the scan scope, alignment rule, missing-link
counts, localized-only links, and deduplication policy. The older
`manage_site_link_registry.py` workflow remains documented in
`SITE_LINK_LOCALIZATION_REVIEW.md` for future rendered-site investigations.
