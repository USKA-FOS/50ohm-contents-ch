#!/usr/bin/env python3
"""Inventory links in canonical text objects and optionally check web targets.

Unlike ``manage_site_link_registry.py``, this tool reads canonical object text
slots only. It never scans generated site pages or template-injected links.
HTTP targets are deduplicated across objects and languages; GitHub hosts are
listed but are never requested.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from dataclasses import dataclass
from datetime import UTC, datetime
from difflib import SequenceMatcher
from html.parser import HTMLParser
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter


ROOT = Path(__file__).resolve().parents[1]
CANONICAL = ROOT / "canonical"
DEFAULT_WORKBOOK = ROOT / "review" / "link_localization" / "canonical_link_registry.xlsx"
LANGUAGES = ("de", "fr", "it")
URL_SCHEMES = {"http", "https"}
GITHUB_HOSTS = {"github.com", "github.io", "githubusercontent.com", "githubassets.com"}
SITE_HOSTS = {"50ohm.uska.ch"}


@dataclass(frozen=True)
class Link:
    target: str
    text: str
    syntax: str
    target_span: tuple[int, int] | None = None
    markup_span: tuple[int, int] | None = None


@dataclass
class Occurrence:
    key: str
    link_de: Link | None
    link_fr: Link | None
    link_it: Link | None
    object_id: str
    object_type: str
    slot_key: str
    paths: dict[str, str]
    order: int
    match_fr: str
    match_it: str


class HTMLAnchorParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[Link] = []
        self.current: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "a":
            href = dict(attrs).get("href")
            if href is not None:
                self.links.append(Link(href.strip(), "", "html"))
                self.current = [""]

    def handle_data(self, data: str) -> None:
        if self.current is not None:
            self.current.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a" and self.current is not None:
            text = " ".join("".join(self.current[1:]).split())
            self.links[-1] = Link(self.links[-1].target, text, "html")
            self.current = None


def markdown_links(text: str) -> list[Link]:
    """Read inline Markdown links, including balanced parentheses in targets."""
    links: list[Link] = []
    i = 0
    while i < len(text):
        start = text.find("](", i)
        if start < 0:
            break
        # A preceding '!' is an image, not a hyperlink.
        label_start = text.rfind("[", 0, start)
        if label_start < 0 or text[label_start + 1 : start].find("]") >= 0:
            i = start + 2
            continue
        depth = 1
        j = start + 2
        if j < len(text) and text[j] == "<":
            end = text.find(">", j + 1)
            if end < 0:
                i = j
                continue
            target = text[j + 1 : end]
            close = text.find(")", end + 1)
            if close < 0:
                i = end + 1
                continue
            target_start = j + 1
            target_end = end
        else:
            target_start = j
            while j < len(text):
                char = text[j]
                if char == "\\" and j + 1 < len(text):
                    j += 2
                    continue
                if char == "(" and j and text[j - 1] != "\\":
                    depth += 1
                elif char == ")" and j and text[j - 1] != "\\":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            if j >= len(text) or depth != 0:
                i = start + 2
                continue
            raw_target = text[target_start:j].strip()
            leading_space = len(text[target_start:j]) - len(text[target_start:j].lstrip())
            # Standard Markdown allows an optional quoted title after a
            # whitespace-separated destination. Keep unquoted spaces intact:
            # malformed/localized targets must remain visible in the report.
            title_match = re.match(r"^(.*?)\s+([\"']).*\2\s*$", raw_target, re.DOTALL)
            target = title_match.group(1).strip() if title_match else raw_target
            target_start += leading_space
            target_end = target_start + len(target)
            close = j
        if target:
            label = text[label_start + 1 : start].replace("\\]", "]").strip()
            links.append(Link(
                target, label, "markdown",
                (target_start, target_end),
                (label_start, close + 1),
            ))
        i = close + 1
    return links


DARC_LINK_RE = re.compile(r"\[(ref|sec):([^\]\s]+)\]")


def mask_nonrendered_source(text: str) -> str:
    """Blank source comments and code examples while preserving character offsets."""
    chars = list(text)

    def blank(start: int, end: int) -> None:
        for index in range(start, end):
            if chars[index] not in "\r\n":
                chars[index] = " "

    for match in re.finditer(r"(?ms)^%[^\r\n]*|<!--[\s\S]*?-->", text):
        blank(match.start(), match.end())
    masked = "".join(chars)
    # Markdown fenced blocks and inline code are examples, not active links.
    fence_re = re.compile(r"(?ms)^[ \t]{0,3}(`{3,}|~{3,})[^\n]*\n.*?^[ \t]{0,3}\1[ \t]*$")
    chars = list(masked)
    for match in fence_re.finditer(masked):
        for index in range(match.start(), match.end()):
            if chars[index] not in "\r\n":
                chars[index] = " "
    masked = "".join(chars)
    chars = list(masked)
    for match in re.finditer(r"(?<!`)`+[^`\r\n]*`+", masked):
        for index in range(match.start(), match.end()):
            chars[index] = " "
    return "".join(chars)


def extract_links(text: str, slot_type: str) -> list[Link]:
    parsed_text = mask_nonrendered_source(text)
    if slot_type == "html":
        parser = HTMLAnchorParser()
        parser.feed(parsed_text)
        return parser.links
    if slot_type != "markdown":
        return []
    links = markdown_links(parsed_text)
    # Raw HTML anchors may occur inside Markdown text. Merge both syntaxes in
    # source order; the matching positions are recovered from their targets.
    parser = HTMLAnchorParser()
    parser.feed(parsed_text)
    links.extend(parser.links)
    for match in DARC_LINK_RE.finditer(parsed_text):
        kind, target = match.groups()
        links.append(Link(f"{kind}:{target}", f"[{kind}:{target}]", kind,
                          (match.start(2), match.end(2)), (match.start(), match.end())))
    # Recover source order without treating embedded questions/images as links.
    def first_position(link: Link) -> int:
        if link.syntax in {"ref", "sec"}:
            return parsed_text.find(f"[{link.syntax}:{link.target.split(':', 1)[1]}]")
        if link.syntax == "html":
            return parsed_text.find(f'href="{link.target}"') if f'href="{link.target}"' in parsed_text else parsed_text.find(f"href='{link.target}'")
        needle = f"]({link.target}"
        pos = parsed_text.find(needle)
        return pos if pos >= 0 else parsed_text.find(f"](<{link.target}>")

    return sorted(links, key=first_position)


def target_type(target: str, syntax: str) -> str:
    if syntax in {"ref", "sec"}:
        return "canonical object reference" if syntax == "ref" else "canonical section reference"
    parsed = urllib.parse.urlsplit(target)
    scheme = parsed.scheme.casefold()
    host = (parsed.hostname or "").casefold().rstrip(".")
    if scheme == "mailto":
        mail_domain = target.rsplit("@", 1)[-1].casefold().rstrip(">.")
        if mail_domain.endswith(".ch"):
            return "CH"
        if mail_domain.endswith(".de"):
            return "DE"
        return "contact URI"
    if scheme == "tel":
        return "contact URI"
    if scheme in URL_SCHEMES:
        if host in SITE_HOSTS:
            return "same-site absolute target"
        if is_github_host(host):
            return "GitHub"
        if host.endswith(".ch") or host.endswith(".swiss"):
            return "CH"
        # Matrix permalinks use matrix.to as the web host while their room ID
        # names the DARC server (for example, #50ohm:darc.de).
        if host.endswith(".de") or (
            host == "matrix.to"
            and re.search(r"(?:^|:)darc\.de(?:$|[/?&])", parsed.fragment, re.IGNORECASE)
        ):
            return "DE"
        return "Other external"
    if scheme or parsed.netloc:
        return f"other URI scheme: {scheme or 'protocol-relative'}"
    return "relative internal target"


def is_github_host(host: str) -> bool:
    return any(host == base or host.endswith("." + base) for base in GITHUB_HOSTS)


def stable_key(object_id: str, slot_key: str, target: str, syntax: str) -> str:
    parsed = urllib.parse.urlsplit(target)
    if parsed.scheme or parsed.netloc:
        # The same outbound href is one key even when repeated in different
        # objects or represented with different source markup.
        value = target
    else:
        # A relative path is interpreted from its source object/text slot.
        value = f"{object_id}\0{slot_key}\0{syntax}\0{target}"
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def align(source: list[Link], target: list[Link]) -> dict[int, int]:
    if len(source) == len(target):
        return dict(enumerate(range(len(target))))
    matcher = SequenceMatcher(
        a=[(link.syntax, link.target) for link in source],
        b=[(link.syntax, link.target) for link in target],
        autojunk=False,
    )
    result: dict[int, int] = {}
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        left, right = i2 - i1, j2 - j1
        if tag == "equal" or (tag == "replace" and left == right):
            result.update((i1 + n, j1 + n) for n in range(left))
    return result


def load_canonical_occurrences(canonical_root: Path) -> list[Occurrence]:
    result: list[Occurrence] = []
    for meta_path in sorted(canonical_root.rglob("object.meta.json")):
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        if not meta.get("active", True):
            continue
        object_id = str(meta.get("id", meta_path.parent.name))
        object_type = str(meta.get("object_type", ""))
        for slot in sorted(meta.get("text_slots", []), key=lambda item: item.get("sort_order", 0)):
            storage = slot.get("storage", {})
            if storage.get("kind") != "text_file":
                continue
            files = storage.get("files", {})
            texts: dict[str, str] = {}
            paths: dict[str, str] = {}
            links: dict[str, list[Link]] = {}
            for lang in LANGUAGES:
                name = files.get(lang)
                if not name:
                    links[lang] = []
                    continue
                path = (meta_path.parent / str(name)).resolve()
                try:
                    path.relative_to(canonical_root.resolve())
                except ValueError as exc:
                    raise ValueError(f"Text slot path escapes canonical object: {path}") from exc
                if not path.is_file():
                    links[lang] = []
                    continue
                texts[lang] = path.read_text(encoding="utf-8", errors="replace")
                paths[lang] = path.relative_to(canonical_root.parent).as_posix()
                links[lang] = extract_links(texts[lang], str(slot.get("slot_type", "")))

            de_links = links.get("de", [])
            aligned = {lang: align(de_links, links.get(lang, [])) for lang in ("fr", "it")}
            used = {lang: set(mapping.values()) for lang, mapping in aligned.items()}
            for order, de in enumerate(de_links):
                fr_index = aligned["fr"].get(order)
                it_index = aligned["it"].get(order)
                fr = links["fr"][fr_index] if fr_index is not None else None
                it = links["it"][it_index] if it_index is not None else None
                kind_for_key = de.syntax
                target_for_key = de.target
                key = stable_key(object_id, str(slot.get("slot_key", "")), target_for_key, kind_for_key)
                result.append(Occurrence(key, de, fr, it, object_id, object_type,
                                         str(slot.get("slot_key", "")), paths, order,
                                         "matched" if fr else "missing/unmatched",
                                         "matched" if it else "missing/unmatched"))
            # Include translated-only links as explicit rows rather than
            # silently losing unmatched additions inside a sequence.
            for lang in ("fr", "it"):
                for index, localized in enumerate(links[lang]):
                    if index in used[lang]:
                        continue
                    key = stable_key(object_id, str(slot.get("slot_key", "")), localized.target,
                                     f"{lang}-only:{localized.syntax}")
                    result.append(Occurrence(key, None, localized if lang == "fr" else None,
                                             localized if lang == "it" else None, object_id,
                                             object_type, str(slot.get("slot_key", "")), paths,
                                             index, "translation-only" if lang == "fr" else "",
                                             "translation-only" if lang == "it" else ""))
    return result


def unique_lines(values: list[str]) -> str:
    return "\n".join(dict.fromkeys(value for value in values if value))


def style_sheet(sheet, widths: list[int]) -> None:
    sheet.freeze_panes = "A2"
    sheet.auto_filter.ref = sheet.dimensions
    for cell in sheet[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor="245A75")
        cell.alignment = Alignment(vertical="top", wrap_text=True)
    for index, width in enumerate(widths, start=1):
        sheet.column_dimensions[get_column_letter(index)].width = width
    for row in sheet.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = Alignment(vertical="top", wrap_text=True)


def write_workbook(occurrences: list[Occurrence], output: Path, canonical_root: Path) -> int:
    previous_verified: dict[str, dict[str, tuple[str, str]]] = {}
    previous_checks: dict[str, tuple[object, ...]] = {}
    previous_manifest: dict[str, object] = {}
    if output.is_file():
        try:
            previous_book = load_workbook(output, read_only=True, data_only=True)
            previous_sheet = previous_book["Links"]
            previous_headers = {cell.value: cell.column for cell in previous_sheet[1] if cell.value}
            for old_row in previous_sheet.iter_rows(min_row=2, values_only=True):
                old_key = str(old_row[previous_headers["German link SHA-256"] - 1] or "")
                if not old_key:
                    continue
                previous_verified[old_key] = {}
                for lang in LANGUAGES:
                    link_value = str(old_row[previous_headers[f"Link {lang.upper()}"] - 1] or "")
                    status_value = str(old_row[previous_headers[f"Status {lang.upper()}"] - 1] or "")
                    for link, status in zip(link_value.splitlines(), status_value.splitlines()):
                        if link and status == "verified":
                            previous_verified[old_key][lang + "\0" + link] = (link, status)
            if "Checks" in previous_book.sheetnames:
                old_checks = previous_book["Checks"]
                old_check_headers = {cell.value: cell.column for cell in old_checks[1] if cell.value}
                for old_row in old_checks.iter_rows(min_row=2, values_only=True):
                    url = old_row[old_check_headers["Checked URL"] - 1]
                    if url:
                        previous_checks[str(url)] = tuple(old_row)
            if "Manifest" in previous_book.sheetnames:
                old_manifest = previous_book["Manifest"]
                previous_manifest = {
                    str(row[0]): row[1]
                    for row in old_manifest.iter_rows(min_row=2, values_only=True)
                    if row and row[0]
                }
            previous_book.close()
        except (KeyError, ValueError):
            previous_verified = {}
            previous_checks = {}
            previous_manifest = {}
    grouped: dict[str, list[Occurrence]] = defaultdict(list)
    for occurrence in occurrences:
        grouped[occurrence.key].append(occurrence)
    # The human-facing workbook is an external-link report keyed by the German
    # canonical link. Internal relative targets and DARC object references are
    # excluded from both Links and Occurrences.
    source_link_rows = len(occurrences)
    localized_only_count = sum(1 for row in occurrences if row.link_de is None and (row.link_fr or row.link_it))
    grouped = {
        key: rows for key, rows in grouped.items()
        if any(
            row.link_de and target_type(row.link_de.target, row.link_de.syntax)
            in {"CH", "DE", "Other external", "GitHub"}
            for row in rows
        )
    }
    report_keys = set(grouped)
    report_occurrences = [row for row in occurrences if row.key in report_keys]
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Links"
    headers = [
        "German link SHA-256", "German link key", "Target category DE",
        "Text DE", "Text FR", "Text IT", "Link DE", "Link FR", "Link IT",
        "Status DE", "Status FR",
        "Status IT", "DE occurrences", "Canonical objects",
    ]
    sheet.append(headers)
    for key, rows in sorted(grouped.items(), key=lambda item: (
        item[1][0].link_de.target if item[1][0].link_de else "",
        item[1][0].object_id, item[1][0].order,
    )):
        def links_for(lang: str) -> list[Link]:
            return [link for row in rows if (link := getattr(row, f"link_{lang}")) is not None]
        links = {lang: links_for(lang) for lang in LANGUAGES}
        source = links["de"][0] if links["de"] else None
        target_lists = {lang: list(dict.fromkeys(link.target for link in links[lang])) for lang in LANGUAGES}
        link_by_target = {lang: {link.target: link for link in links[lang]} for lang in LANGUAGES}

        def status_for(lang: str, target: str) -> str:
            preserved = key in previous_verified and lang + "\0" + target in previous_verified[key]
            prior_check = previous_checks.get(check_key(target))
            prior_state = str(prior_check[2]) if prior_check and len(prior_check) > 2 else ""
            if preserved and prior_state != "not found":
                return "verified"
            if prior_state:
                return prior_state
            return initial_status(link_by_target[lang][target])

        statuses = {
            lang: "\n".join(
                status_for(lang, target) for target in target_lists[lang]
            )
            if target_lists[lang] else "missing in canonical source"
            for lang in LANGUAGES
        }
        sheet.append([
            key, source.target if source else "", target_type(source.target, source.syntax) if source else "translation-only",
            unique_lines([link.text for link in links["de"]]),
            unique_lines([link.text for link in links["fr"]]),
            unique_lines([link.text for link in links["it"]]),
            unique_lines(target_lists["de"]), unique_lines(target_lists["fr"]),
            unique_lines(target_lists["it"]),
            statuses["de"], statuses["fr"], statuses["it"],
            sum(1 for row in rows if row.link_de),
            unique_lines([f"{row.object_id} ({row.object_type}; {row.slot_key})" for row in rows]),
        ])

    occ_sheet = workbook.create_sheet("Occurrences")
    occ_sheet.append([
        "German link SHA-256", "Canonical object ID", "Object type", "Text slot",
        "Source file DE", "Order DE", "Text DE", "Link DE", "Target category DE",
        "Source file FR", "Text FR", "Link FR", "FR match",
        "Source file IT", "Text IT", "Link IT", "IT match",
    ])
    for row in report_occurrences:
        occ_sheet.append([
            row.key, row.object_id, row.object_type, row.slot_key,
            row.paths.get("de", ""), row.order, row.link_de.text if row.link_de else "",
            row.link_de.target if row.link_de else "",
            target_type(row.link_de.target, row.link_de.syntax) if row.link_de else "",
            row.paths.get("fr", ""), row.link_fr.text if row.link_fr else "",
            row.link_fr.target if row.link_fr else "",
            row.match_fr, row.paths.get("it", ""), row.link_it.text if row.link_it else "",
            row.link_it.target if row.link_it else "",
            row.match_it,
        ])

    manifest = workbook.create_sheet("Manifest")
    manifest.append(["Field", "Value"])
    manifest_rows = [
        ("Created at (UTC)", datetime.now(UTC).isoformat(timespec="seconds")),
        ("Canonical root", str(canonical_root.resolve())),
        ("Scope", "Active canonical text slots; Links and Occurrences contain only outbound URLs present in German, with DE/FR/IT targets compared. No site output or template links."),
        ("Alignment rule", "Every active German link must have a counterpart in each existing localized text. FR/IT-only links are prohibited. CH targets may be localized; DE and other non-CH targets should match German."),
        ("Category policy", "Each German-keyed link has one category derived from its German target. FR/IT category columns are omitted; the Checks sheet classifies each actual HTTP(S) URL."),
        ("Languages", ", ".join(LANGUAGES)),
        ("Key", "SHA-256 of the exact German external href; the same href shares one key across objects and markup. Relative paths are scoped by object and text slot."),
        ("Network policy", "Only unique HTTP(S) targets are checked; URL fragments are removed; GitHub-family hosts are never requested."),
        ("External German link keys", len(grouped)),
        ("External link occurrences", len(report_occurrences)),
        ("Source hyperlink occurrences examined", source_link_rows),
        ("Links present only in FR/IT", localized_only_count),
        ("German link occurrences missing in FR", sum(1 for row in occurrences if row.link_de and not row.link_fr)),
        ("German link occurrences missing in IT", sum(1 for row in occurrences if row.link_de and not row.link_it)),
        ("German links with no FR text file", sum(1 for row in occurrences if row.link_de and not row.paths.get("fr"))),
        ("German links with no IT text file", sum(1 for row in occurrences if row.link_de and not row.paths.get("it"))),
        ("German links missing from an existing FR file", sum(1 for row in occurrences if row.link_de and row.paths.get("fr") and not row.link_fr)),
        ("German links missing from an existing IT file", sum(1 for row in occurrences if row.link_de and row.paths.get("it") and not row.link_it)),
        ("Non-CH target mismatches in existing FR texts", sum(1 for row in occurrences if row.link_de and row.link_fr and row.paths.get("fr") and target_type(row.link_de.target, row.link_de.syntax) != "CH" and row.link_de.target != row.link_fr.target)),
        ("Non-CH target mismatches in existing IT texts", sum(1 for row in occurrences if row.link_de and row.link_it and row.paths.get("it") and target_type(row.link_de.target, row.link_de.syntax) != "CH" and row.link_de.target != row.link_it.target)),
        ("Internal-only link occurrences excluded", source_link_rows - len(report_occurrences)),
        ("Same-site absolute links to convert to relative", sum(1 for row in occurrences if row.link_de and target_type(row.link_de.target, row.link_de.syntax) == "same-site absolute target")),
        ("DE link keys", sum(1 for rows in grouped.values() if any(row.link_de and target_type(row.link_de.target, row.link_de.syntax) == "DE" for row in rows))),
        ("CH link keys", sum(1 for rows in grouped.values() if any(row.link_de and target_type(row.link_de.target, row.link_de.syntax) == "CH" for row in rows))),
        ("Other external link keys", sum(1 for rows in grouped.values() if any(row.link_de and target_type(row.link_de.target, row.link_de.syntax) == "Other external" for row in rows))),
        ("GitHub target keys", sum(1 for rows in grouped.values() if any(getattr(row, f"link_{lang}") and target_type(getattr(row, f"link_{lang}").target, getattr(row, f"link_{lang}").syntax) == "GitHub" for row in rows for lang in LANGUAGES))),
    ]
    for item in manifest_rows:
        manifest.append(item)
    check_sheet = workbook.create_sheet("Checks")
    check_sheet.append(["Checked URL", "Target category", "Status", "HTTP response", "Final URL", "Detail", "Checked at UTC", "Canonical link keys"])
    used_urls = {
        check_key(link.target)
        for row in report_occurrences
        for lang in LANGUAGES
        if (link := getattr(row, f"link_{lang}")) is not None
        and target_type(link.target, link.syntax) in {"CH", "DE", "Other external"}
        and urllib.parse.urlsplit(link.target).scheme.casefold() in URL_SCHEMES
    }
    url_categories = {
        check_key(link.target): target_type(link.target, link.syntax)
        for row in report_occurrences
        for lang in LANGUAGES
        if (link := getattr(row, f"link_{lang}")) is not None
        and check_key(link.target) in used_urls
    }
    for url, old_row in sorted(previous_checks.items()):
        if url in used_urls:
            current_row = list(old_row)
            current_row[1] = url_categories[url]
            check_sheet.append(current_row)
    # Keep check summary metadata when the previous checked URLs remain in the
    # new external report. New targets remain visibly pending until checked.
    if previous_checks:
        for field in ("Last check at (UTC)", "HTTP requests sent", "GitHub requests sent", "HTTP 429 deferred targets"):
            if field in previous_manifest:
                manifest.append([field, previous_manifest[field]])
    manifest.append(["Unique non-GitHub HTTP URL candidates", len(used_urls)])
    style_sheet(check_sheet, [72, 28, 22, 15, 72, 62, 28, 66])
    style_sheet(sheet, [66, 48, 28, 38, 38, 38, 54, 54, 54, 28, 28, 28, 16, 62])
    style_sheet(occ_sheet, [66, 24, 22, 18, 55, 12, 35, 48, 28, 55, 35, 48, 18, 55, 35, 48, 18])
    style_sheet(manifest, [34, 115])
    output.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(output)
    return len(grouped)


def initial_status(link: Link | None) -> str:
    if link is None:
        return "missing in canonical source"
    kind = target_type(link.target, link.syntax)
    if kind == "GitHub":
        return "skipped (GitHub)"
    if kind == "same-site absolute target":
        return "same-site URL; use a relative path"
    if urllib.parse.urlsplit(link.target).scheme.casefold() in {"mailto", "tel"}:
        return "not web-checkable"
    if kind in {"canonical object reference", "canonical section reference"}:
        return "canonical reference; no HTTP check"
    if kind == "relative internal target":
        return "relative target; no HTTP check"
    if kind == "contact URI":
        return "not web-checkable"
    return "pending check"


def check_key(url: str) -> str:
    parts = urllib.parse.urlsplit(url.strip())
    return urllib.parse.urlunsplit((parts.scheme.casefold(), parts.netloc.casefold(), parts.path or "/", parts.query, ""))


def ascii_http_url(url: str) -> str:
    parts = urllib.parse.urlsplit(url)
    host = parts.hostname or ""
    host = f"[{host}]" if ":" in host else host.encode("idna").decode("ascii")
    if parts.port:
        host += f":{parts.port}"
    path = urllib.parse.quote(urllib.parse.unquote(parts.path), safe="/%:@!$&'()*+,;=-._~")
    query = urllib.parse.quote(urllib.parse.unquote(parts.query), safe="/?@!$&'()*+,;=:%-._~")
    return urllib.parse.urlunsplit((parts.scheme, host, path or "/", query, ""))


def check_url(url: str, timeout: float) -> tuple[str, str, str, str]:
    checked = check_key(url)
    try:
        request_url = ascii_http_url(checked)
    except (UnicodeError, ValueError) as error:
        return "invalid URL", "", "", str(error)
    request = urllib.request.Request(request_url, headers={"User-Agent": "50ohm-canonical-link-check/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            response.read(1)
            return "found", str(response.status), response.geturl(), f"HTTP {response.status}"
    except urllib.error.HTTPError as error:
        if error.code in {404, 410}:
            return "not found", str(error.code), error.geturl(), f"HTTP {error.code}: {error.reason}"
        return f"HTTP {error.code}", str(error.code), error.geturl(), str(error.reason)
    except urllib.error.URLError as error:
        reason = error.reason
        status = "timeout" if isinstance(reason, TimeoutError) else "network error"
        return status, "", "", str(reason)
    except (TimeoutError, OSError) as error:
        return ("timeout" if isinstance(error, TimeoutError) else "network error"), "", "", str(error)


def check_workbook(path: Path, timeout: float) -> tuple[int, int]:
    workbook = load_workbook(path)
    if "Links" not in workbook.sheetnames:
        raise ValueError("Workbook is missing its Links sheet; run scan first")
    links_sheet = workbook["Links"]
    headers = {cell.value: cell.column for cell in links_sheet[1] if cell.value}
    checks: dict[str, set[str]] = defaultdict(set)
    url_types: dict[str, str] = {}
    grouped_keys: dict[str, set[str]] = defaultdict(set)
    previous_verified: dict[tuple[str, str], bool] = {}
    for row_index in range(2, links_sheet.max_row + 1):
        key = str(links_sheet.cell(row_index, headers["German link SHA-256"]).value or "")
        for lang in LANGUAGES:
            link_col = headers[f"Link {lang.upper()}"]
            status_col = headers[f"Status {lang.upper()}"]
            targets = [x.strip() for x in str(links_sheet.cell(row_index, link_col).value or "").splitlines() if x.strip()]
            for target in targets:
                typ = target_type(target, "markdown")
                if typ == "GitHub":
                    continue
                elif (
                    typ in {"CH", "DE", "Other external"}
                    and urllib.parse.urlsplit(target).scheme.casefold() in URL_SCHEMES
                ):
                    normalized = check_key(target)
                    checks[normalized].add(key)
                    url_types[normalized] = typ
            status_col = headers[f"Status {lang.upper()}"]
            previous_statuses = str(links_sheet.cell(row_index, status_col).value or "").splitlines()
            for target, previous_status in zip(targets, previous_statuses):
                previous_verified[(lang, target)] = previous_status == "verified"
            # Statuses are applied after the global URL set has been checked.

    results: dict[str, tuple[str, str, str, str]] = {}
    paused_hosts: set[str] = set()
    actual_requests = 0
    for url in sorted(checks, key=lambda item: ((urllib.parse.urlsplit(item).hostname or "").casefold(), item)):
        host = (urllib.parse.urlsplit(url).hostname or "").casefold()
        if is_github_host(host):
            continue
        if host in paused_hosts:
            results[url] = ("HTTP 429 (host paused)", "429", "", "Not requested after an earlier HTTP 429 from this host")
            continue
        results[url] = check_url(url, timeout)
        actual_requests += 1
        if results[url][1] == "429":
            paused_hosts.add(host)

    check_sheet = workbook["Checks"] if "Checks" in workbook.sheetnames else workbook.create_sheet("Checks")
    check_sheet.delete_rows(1, check_sheet.max_row)
    check_sheet.append(["Checked URL", "Target category", "Status", "HTTP response", "Final URL", "Detail", "Checked at UTC", "Canonical link keys"])
    checked_at = datetime.now(UTC).isoformat(timespec="seconds")
    for url in sorted(checks):
        if url not in results:
            continue
        state, response, final, detail = results[url]
        check_sheet.append([url, url_types[url], state, response, final, detail, checked_at, "\n".join(sorted(checks[url]))])
    style_sheet(check_sheet, [72, 28, 22, 15, 72, 62, 28, 66])

    if "Manifest" not in workbook.sheetnames:
        manifest = workbook.create_sheet("Manifest")
        manifest.append(["Field", "Value"])
    else:
        manifest = workbook["Manifest"]
    manifest_rows = {str(row[0]): index for index, row in enumerate(manifest.iter_rows(values_only=True), start=1) if row and row[0]}
    check_summary = {
        "Last check at (UTC)": checked_at,
        "Unique non-GitHub HTTP URL candidates": len(checks),
        "HTTP requests sent": actual_requests,
        "GitHub requests sent": 0,
        "HTTP 429 deferred targets": sum(1 for result in results.values() if result[0] == "HTTP 429 (host paused)"),
    }
    for field, value in check_summary.items():
        if field in manifest_rows:
            manifest.cell(manifest_rows[field], 2).value = value
        else:
            manifest.append([field, value])
    style_sheet(manifest, [40, 115])

    # Apply the one result per normalized URL to each status cell.
    for row_index in range(2, links_sheet.max_row + 1):
        for lang in LANGUAGES:
            link_col = headers[f"Link {lang.upper()}"]
            status_col = headers[f"Status {lang.upper()}"]
            targets = [x.strip() for x in str(links_sheet.cell(row_index, link_col).value or "").splitlines() if x.strip()]
            states = []
            for target in targets:
                typ = target_type(target, "markdown")
                if typ == "GitHub":
                    states.append("skipped (GitHub)")
                elif typ == "same-site absolute target":
                    states.append("same-site URL; use a relative path")
                elif (
                    typ in {"CH", "DE", "Other external"}
                    and urllib.parse.urlsplit(target).scheme.casefold() in URL_SCHEMES
                ):
                    result = results.get(check_key(target))
                    state = result[0] if result else "not checked"
                    if previous_verified.get((lang, target)) and state != "not found":
                        state = "verified"
                    states.append(state)
                elif typ == "relative internal target":
                    states.append("verified" if previous_verified.get((lang, target)) else "relative target; no HTTP check")
                elif typ.startswith("canonical "):
                    states.append("verified" if previous_verified.get((lang, target)) else "canonical reference; no HTTP check")
                elif typ == "contact URI" or urllib.parse.urlsplit(target).scheme.casefold() in {"mailto", "tel"}:
                    states.append("verified" if previous_verified.get((lang, target)) else "not web-checkable")
                else:
                    states.append("not checked (unsupported target)")
            links_sheet.cell(row_index, status_col).value = "\n".join(states) if states else "missing in canonical source"
    workbook.save(path)
    return actual_requests, sum(len(values) for values in checks.values())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    scan = subparsers.add_parser("scan", help="Inventory active canonical object text slots")
    scan.add_argument("--canonical-root", type=Path, default=CANONICAL)
    scan.add_argument("--output", type=Path, default=DEFAULT_WORKBOOK)
    check = subparsers.add_parser("check", help="Check unique external canonical URLs; never request GitHub")
    check.add_argument("--workbook", type=Path, default=DEFAULT_WORKBOOK)
    check.add_argument("--timeout", type=float, default=12)
    args = parser.parse_args()
    if args.command == "scan":
        root = args.canonical_root.resolve()
        output = args.output.resolve()
        rows = load_canonical_occurrences(root)
        count = write_workbook(rows, output, root)
        external_occurrences = sum(
            1 for row in rows
            if row.link_de and target_type(row.link_de.target, row.link_de.syntax)
            in {"CH", "DE", "Other external", "GitHub"}
        )
        localized_only = sum(1 for row in rows if row.link_de is None and (row.link_fr or row.link_it))
        print(
            f"source_link_occurrences={len(rows)} external_german_keys={count} "
            f"external_occurrences={external_occurrences} fr_it_only_links={localized_only} "
            f"workbook={output}"
        )
        for row in rows:
            if row.link_de is None and (row.link_fr or row.link_it):
                for lang in ("fr", "it"):
                    link = getattr(row, f"link_{lang}")
                    if link:
                        print(
                            f"localized_only_link language={lang} object={row.object_id} "
                            f"slot={row.slot_key} source={row.paths.get(lang, '')} "
                            f"syntax={link.syntax} target={link.target!r}"
                        )
    else:
        count, references = check_workbook(args.workbook.resolve(), args.timeout)
        print(f"unique_http_targets_requested={count} link_target_references={references} github_requests=0 workbook={args.workbook.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
