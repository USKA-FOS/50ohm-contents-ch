from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import shutil
import subprocess
import tarfile
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from .validate_canonical_model import validate_canonical
except ImportError:
    from validate_canonical_model import validate_canonical


REPO_ROOT = Path(__file__).resolve().parent.parent
CANONICAL_ROOT = REPO_ROOT / "canonical"
WORK_REPORT_ROOT = REPO_ROOT / "work" / "source_import_audits"
ACCEPTED_REPORT_ROOT = REPO_ROOT / "review" / "source_imports"
TARGET_LANGUAGES = ("fr", "it")
MARKER_RE = re.compile(r"\[(question|photo|picture|table|include|ref|index|class|morse):([^\]]*)\]")
HTML_TOKEN_RE = re.compile(r"(?is)(<script\b.*?</script\s*>|<style\b.*?</style\s*>|<!--.*?-->|<[^>]+>)")


@dataclass(frozen=True)
class Family:
    source_directory: str
    canonical_directory: str
    object_type: str
    suffixes: tuple[str, ...]
    slot_key: str | None = None
    slot_type: str | None = None
    prefix: str = ""


FAMILIES = (
    Family("sections", "sections", "section_article", (".md",), "body_markdown", "markdown", "sc"),
    Family("slides", "slides", "slide_article", (".md",), "body_markdown", "markdown", "sl"),
    Family("solutions", "solutions", "solution_article", (".md",), "body_markdown", "markdown", "s"),
    Family("snippets", "snippets", "snippet", (".md",), "body_markdown", "markdown", "sn"),
    Family("static", "static_pages", "static_page", (".html",), "body_html", "html", "sp"),
    Family("html", "html_includes", "html_include", (".html",), "body_html", "html", "in"),
    Family("photos", "photos", "photo", (".png", ".txt"), prefix="ph"),
    Family("drawings", "drawings", "drawing", (".svg", ".tex", ".txt"), prefix="dr"),
)
FAMILY_BY_TYPE = {family.object_type: family for family in FAMILIES}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def stable_id(prefix: str, object_type: str, source_key: str) -> str:
    digest = hashlib.sha1(f"{object_type}::{source_key}".encode("utf-8")).hexdigest()[:12]
    return f"{prefix}_{digest}"


def stable_node_id(prefix: str, edition: str, node_type: str, ident: str) -> str:
    digest = hashlib.sha1(f"{edition}::{node_type}::{ident}".encode("utf-8")).hexdigest()[:12]
    return f"{prefix}_{digest}"


def source_revision(
    source_root: Path,
    records: dict[tuple[str, str], dict[str, Any]],
    override: str | None = None,
) -> str:
    if override:
        return override
    try:
        return subprocess.check_output(
            ["git", "-C", str(source_root), "rev-parse", "HEAD"], text=True, stderr=subprocess.DEVNULL
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        digest = hashlib.sha256()
        for identity, record in sorted(records.items()):
            digest.update("::".join(identity).encode("utf-8"))
            digest.update(record["fingerprint"].encode("ascii"))
        return f"tree-{digest.hexdigest()}"


def object_fingerprint(files: dict[str, bytes]) -> str:
    digest = hashlib.sha256()
    for suffix, payload in sorted(files.items()):
        digest.update(suffix.encode("utf-8"))
        digest.update(b"\0")
        digest.update(payload)
        digest.update(b"\0")
    return digest.hexdigest()


def scan_source(source_root: Path) -> dict[tuple[str, str], dict[str, Any]]:
    contents_root = source_root / "contents"
    if not contents_root.is_dir():
        raise RuntimeError(f"Source root has no contents directory: {source_root}")
    records: dict[tuple[str, str], dict[str, Any]] = {}
    for family in FAMILIES:
        source_dir = contents_root / family.source_directory
        if not source_dir.is_dir():
            raise RuntimeError(f"Source is missing required directory: {source_dir}")
        grouped: dict[str, dict[str, bytes]] = {}
        paths: dict[str, dict[str, str]] = {}
        for path in sorted(source_dir.iterdir()):
            if not path.is_file() or path.suffix not in family.suffixes:
                continue
            if path.stem in grouped and path.suffix in grouped[path.stem]:
                raise RuntimeError(f"Duplicate source member: {path}")
            grouped.setdefault(path.stem, {})[path.suffix] = path.read_bytes()
            paths.setdefault(path.stem, {})[path.suffix] = str(path.relative_to(source_root))
        for source_key, files in grouped.items():
            identity = (family.object_type, source_key)
            records[identity] = {
                "family": family,
                "source_key": source_key,
                "files": files,
                "paths": paths[source_key],
                "fingerprint": object_fingerprint(files),
            }
    return records


def canonical_de_files(object_dir: Path, meta: dict[str, Any]) -> dict[str, bytes]:
    family = FAMILY_BY_TYPE[str(meta["object_type"])]
    files: dict[str, bytes] = {}
    if family.slot_key is not None:
        for slot in meta.get("text_slots", []):
            if str(slot.get("slot_key")) != family.slot_key:
                continue
            relative_name = ((slot.get("storage") or {}).get("files") or {}).get("de")
            if relative_name:
                files[Path(str(relative_name)).suffix] = (object_dir / str(relative_name)).read_bytes()
            break
        return files

    source_key = str((meta.get("source") or {}).get("key"))
    if family.object_type in {"photo", "drawing"}:
        variants = ((meta.get("language_variants") or {}).get("de") or {}).get("asset_files") or {}
        for relative_name in variants.values():
            path = object_dir / str(relative_name)
            if path.is_file():
                files[path.suffix] = path.read_bytes()
        for slot in meta.get("text_slots", []):
            relative_name = ((slot.get("storage") or {}).get("files") or {}).get("de")
            if relative_name:
                path = object_dir / str(relative_name)
                if path.is_file():
                    files[".txt"] = path.read_bytes()
                break
        for suffix in family.suffixes:
            fallback = object_dir / f"{source_key}.de{suffix}"
            if suffix not in files and fallback.is_file():
                files[suffix] = fallback.read_bytes()
    return files


def load_canonical_index(canonical_root: Path) -> dict[tuple[str, str], dict[str, Any]]:
    records: dict[tuple[str, str], dict[str, Any]] = {}
    for family in FAMILIES:
        family_root = canonical_root / family.canonical_directory
        for object_dir in sorted(path for path in family_root.iterdir() if path.is_dir()):
            meta = read_json(object_dir / "object.meta.json")
            source_key = str((meta.get("source") or {}).get("key", ""))
            identity = (family.object_type, source_key)
            if not source_key or identity in records:
                raise RuntimeError(f"Missing or duplicate canonical source identity: {identity}")
            files = canonical_de_files(object_dir, meta)
            records[identity] = {
                "family": family,
                "source_key": source_key,
                "files": files,
                "fingerprint": object_fingerprint(files),
                "object_dir": object_dir,
                "meta": meta,
            }
    return records


def unique_rename_matches(
    source_records: dict[tuple[str, str], dict[str, Any]],
    canonical_records: dict[tuple[str, str], dict[str, Any]],
) -> tuple[dict[tuple[str, str], tuple[str, str]], list[dict[str, Any]]]:
    added = set(source_records) - set(canonical_records)
    missing = set(canonical_records) - set(source_records)
    source_by_fingerprint: dict[tuple[str, str], list[tuple[str, str]]] = {}
    old_by_fingerprint: dict[tuple[str, str], list[tuple[str, str]]] = {}
    for identity in added:
        source_by_fingerprint.setdefault((identity[0], source_records[identity]["fingerprint"]), []).append(identity)
    for identity in missing:
        old_by_fingerprint.setdefault((identity[0], canonical_records[identity]["fingerprint"]), []).append(identity)
    matches: dict[tuple[str, str], tuple[str, str]] = {}
    ambiguous: list[dict[str, Any]] = []
    for key in sorted(set(source_by_fingerprint) & set(old_by_fingerprint)):
        new_items = source_by_fingerprint[key]
        old_items = old_by_fingerprint[key]
        if len(new_items) == 1 and len(old_items) == 1:
            matches[new_items[0]] = old_items[0]
        else:
            ambiguous.append({"object_type": key[0], "new": sorted(item[1] for item in new_items), "old": sorted(item[1] for item in old_items)})
    return matches, ambiguous


def review_state(meta: dict[str, Any], language: str, state: str) -> dict[str, str] | None:
    states = meta.setdefault("review_states", [])
    for item in states:
        if str(item.get("language")) == language:
            previous = str(item.get("state"))
            item["state"] = state
            return {"language": language, "from": previous, "to": state} if previous != state else None
    states.append({"language": language, "state": state})
    return {"language": language, "from": "absent", "to": state}


def present_languages(meta: dict[str, Any]) -> set[str]:
    languages = {str(language) for language in meta.get("languages", [])}
    for slot in meta.get("text_slots", []):
        languages.update(str(language) for language in ((slot.get("storage") or {}).get("files") or {}))
    languages.update(str(language) for language in (meta.get("language_variants") or {}))
    return languages


def parse_markers(text: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    references: list[dict[str, Any]] = []
    annotations: list[dict[str, Any]] = []
    order = 0
    for match in MARKER_RE.finditer(text):
        order += 1
        command, raw_payload = match.group(1), match.group(2)
        raw_marker = match.group(0)
        if command == "question":
            references.append({"source_slot_key": "body_markdown", "target_object_type": "question", "target_id_system": "question_code", "target_id_value": raw_payload.strip(), "relation_type": "references_question", "inline_alias": None, "inline_label": None, "raw_marker": raw_marker, "sort_order": order})
        elif command in {"photo", "picture"}:
            parts = raw_payload.split(":")
            if len(parts) >= 3:
                references.append({"source_slot_key": "body_markdown", "target_object_type": "photo" if command == "photo" else "drawing", "target_id_system": "photo_id" if command == "photo" else "drawing_id", "target_id_value": parts[0].strip(), "relation_type": "embeds_photo" if command == "photo" else "embeds_drawing", "inline_alias": parts[1].strip(), "inline_label": ":".join(parts[2:]).strip(), "raw_marker": raw_marker, "sort_order": order})
        elif command == "table":
            parts = raw_payload.split(":")
            if len(parts) >= 2:
                alias = parts[0].strip()
                references.append({"source_slot_key": "body_markdown", "target_object_type": "table_object", "target_id_system": "table_id", "target_id_value": alias, "relation_type": "embeds_table", "inline_alias": alias, "inline_label": ":".join(parts[1:]).strip(), "raw_marker": raw_marker, "sort_order": order})
        elif command == "include":
            references.append({"source_slot_key": "body_markdown", "target_object_type": "html_include", "target_id_system": "include_key", "target_id_value": raw_payload.strip(), "relation_type": "includes_object", "inline_alias": None, "inline_label": None, "raw_marker": raw_marker, "sort_order": order})
        elif command == "ref":
            alias = raw_payload.strip()
            references.append({"source_slot_key": "body_markdown", "target_object_type": None, "target_id_system": "inline_alias", "target_id_value": alias, "relation_type": "references_embedded_alias", "inline_alias": alias, "inline_label": None, "raw_marker": raw_marker, "sort_order": order})
        elif command in {"index", "class", "morse"}:
            parts = raw_payload.split(":", 1)
            annotations.append({"source_slot_key": "body_markdown", "annotation_type": {"index": "index_term", "class": "class_marker", "morse": "morse_marker"}[command], "annotation_key": parts[0].strip() if command == "index" else None, "annotation_value": (parts[1].strip() if len(parts) > 1 else None) if command == "index" else raw_payload.strip(), "raw_marker": raw_marker, "sort_order": order})
    return references, annotations


def html_tokens(html: str) -> tuple[list[str], list[tuple[int, str]], list[str]]:
    text_slots: list[str] = []
    segments: list[tuple[int, str]] = []
    structural: list[str] = []
    position = 0
    for match in HTML_TOKEN_RE.finditer(html):
        text = html[position:match.start()]
        text_slots.append(text)
        if re.search(r"\w", text, flags=re.UNICODE):
            segments.append((len(text_slots) - 1, text))
        token = match.group(0)
        structural.append(token)
        position = match.end()
    text = html[position:]
    text_slots.append(text)
    if re.search(r"\w", text, flags=re.UNICODE):
        segments.append((len(text_slots) - 1, text))
    return text_slots, segments, structural


def rebuild_html(html: str, replacements: dict[int, str]) -> str:
    text_slots, _, structural = html_tokens(html)
    result: list[str] = []
    for index, text in enumerate(text_slots):
        result.append(replacements.get(index, text))
        if index < len(structural):
            result.append(structural[index])
    return "".join(result)


def merge_html_target(old_source: str, new_source: str, old_target: str) -> tuple[str, dict[str, int]]:
    _, old_segments, old_structure = html_tokens(old_source)
    _, new_segments, _ = html_tokens(new_source)
    target_slots, _, target_structure = html_tokens(old_target)
    if old_structure != target_structure:
        raise RuntimeError("existing target HTML is not structurally aligned with the previous German payload")
    replacements: dict[int, str] = {}
    matcher = difflib.SequenceMatcher(
        a=[text for _, text in old_segments],
        b=[text for _, text in new_segments],
        autojunk=False,
    )
    for old_start, new_start, size in matcher.get_matching_blocks():
        for offset in range(size):
            old_slot = old_segments[old_start + offset][0]
            new_slot = new_segments[new_start + offset][0]
            replacements[new_slot] = target_slots[old_slot]
    return rebuild_html(new_source, replacements), {
        "old_segments": len(old_segments),
        "new_segments": len(new_segments),
        "preserved_translations": len(replacements),
        "pending_segments": len(new_segments) - len(replacements),
    }


def base_meta(family: Family, source_key: str, object_id: str, source_record: dict[str, Any]) -> dict[str, Any]:
    source_path = f"contents/{family.source_directory}/{source_key}"
    if family.slot_key is not None:
        suffix = next(iter(source_record["files"]))
        source_path += suffix
        canonical_name = f"body.de{suffix}"
        return {
            "id": object_id, "object_type": family.object_type, "active": True,
            "source": {"path": source_path, "format": suffix.lstrip("."), "key": source_key},
            "identifiers": [{"id_system": "file_stem", "id_value": source_key, "preferred": True}],
            "languages": ["de"], "review_states": [{"language": "de", "state": "imported_approved"}],
            "metadata": {}, "asset_files": {},
            "text_slots": [{"slot_key": family.slot_key, "slot_type": family.slot_type, "sort_order": 0, "translation_group_key": None, "storage": {"kind": "text_file", "files": {"de": canonical_name}}}],
            "reconstruction": {"strategy": "replace_source_file", "targets": [{"path": source_path, "kind": "localized_text_file"}]},
        }
    identifier = "photo_id" if family.object_type == "photo" else "drawing_id"
    strategy = "render_photo_description_file" if family.object_type == "photo" else "render_drawing_assets_and_description"
    return {
        "id": object_id, "object_type": family.object_type, "active": True,
        "source": {"path": source_path, "format": "grouped_asset", "key": source_key},
        "identifiers": [{"id_system": identifier, "id_value": source_key, "preferred": True}, {"id_system": "file_stem", "id_value": source_key, "preferred": False}],
        "languages": ["de"], "review_states": [{"language": "de", "state": "imported_approved"}],
        "metadata": {}, "asset_files": {}, "text_slots": [], "language_variants": {"de": {"asset_files": {}, "review_state": "imported_approved"}},
        "reconstruction": {"strategy": strategy, "targets": []},
    }


def update_tracking(meta: dict[str, Any], source_record: dict[str, Any], revision: str, status: str = "active") -> None:
    metadata = meta.setdefault("metadata", {})
    metadata["source_tracking"] = {
        "revision": revision,
        "status": status,
        "files": {source_record["paths"][suffix]: sha256_bytes(payload) for suffix, payload in sorted(source_record["files"].items())},
    }


def apply_source_record(
    canonical_root: Path,
    source_record: dict[str, Any],
    existing: dict[str, Any] | None,
    revision: str,
    action: str,
    translation_required: bool,
    media_review_required: bool,
) -> dict[str, Any]:
    family: Family = source_record["family"]
    source_key = source_record["source_key"]
    object_id = str(existing["meta"]["id"]) if existing else stable_id(family.prefix, family.object_type, source_key)
    object_dir = existing["object_dir"] if existing else canonical_root / family.canonical_directory / object_id
    object_dir.mkdir(parents=True, exist_ok=True)
    meta = existing["meta"] if existing else base_meta(family, source_key, object_id, source_record)
    transitions: list[dict[str, str]] = []
    html_alignment: dict[str, dict[str, int]] = {}

    old_key = str((meta.get("source") or {}).get("key", source_key))
    if action == "renamed":
        meta["source"]["key"] = source_key
        suffix = next(iter(source_record["files"])) if family.slot_key is not None else ""
        meta["source"]["path"] = f"contents/{family.source_directory}/{source_key}{suffix}"
        for identifier in meta.get("identifiers", []):
            if identifier.get("id_system") in {"file_stem", "photo_id", "drawing_id"}:
                identifier["id_value"] = source_key
        if family.slot_key is not None:
            target_path = f"contents/{family.source_directory}/{source_key}{next(iter(source_record['files']))}"
            meta["reconstruction"]["targets"] = [{"path": target_path, "kind": "localized_text_file"}]

    if family.slot_key is not None:
        suffix, payload = next(iter(source_record["files"].items()))
        slot = next(slot for slot in meta["text_slots"] if str(slot.get("slot_key")) == family.slot_key)
        files = slot["storage"].setdefault("files", {})
        de_name = str(files.get("de") or f"body.de{suffix}")
        old_de = (object_dir / de_name).read_text(encoding="utf-8") if (object_dir / de_name).exists() else ""
        new_de = payload.decode("utf-8")
        if family.slot_type == "html" and old_de != new_de:
            for language in TARGET_LANGUAGES:
                target_name = files.get(language)
                if target_name and (object_dir / str(target_name)).is_file():
                    merged, stats = merge_html_target(old_de, new_de, (object_dir / str(target_name)).read_text(encoding="utf-8"))
                    (object_dir / str(target_name)).write_text(merged, encoding="utf-8")
                    html_alignment[language] = stats
        (object_dir / de_name).write_bytes(payload)
        files["de"] = de_name
        text = new_de
        references, annotations = parse_markers(text) if family.slot_type == "markdown" else ([], [])
        write_json(object_dir / "object.references.json", references)
        write_json(object_dir / "object.annotations.json", annotations)
    else:
        variants = meta.setdefault("language_variants", {}).setdefault("de", {"asset_files": {}})
        variant_files = variants.setdefault("asset_files", {})
        metadata = meta.setdefault("metadata", {})
        asset_meta = metadata.setdefault("asset", {})
        language_asset = metadata.setdefault("language_asset", {})
        reconstruction_meta = metadata.setdefault("reconstruction", {})
        old_files = existing["files"] if existing else {}
        removed_suffixes = set(old_files) - set(source_record["files"])
        for suffix in removed_suffixes:
            old_name = None
            if suffix == ".txt":
                for slot in meta.get("text_slots", []):
                    old_name = ((slot.get("storage") or {}).get("files") or {}).pop("de", None)
                reconstruction_meta.get("description_canonical_files", {}).pop("de", None)
                asset_meta.pop("description_source_path", None)
            else:
                kind = "image" if family.object_type == "photo" else suffix.lstrip(".")
                old_name = variant_files.pop(kind, None)
                language_asset.pop(f"de.{kind}", None)
                asset_meta.pop({"image": "image_path", "svg": "svg_path", "tex": "tex_path"}[kind], None)
            if old_name:
                (object_dir / str(old_name)).unlink(missing_ok=True)
        for suffix, payload in source_record["files"].items():
            canonical_name = f"{source_key}.de{suffix}"
            (object_dir / canonical_name).write_bytes(payload)
            source_path = source_record["paths"][suffix]
            if suffix == ".txt":
                description_files = reconstruction_meta.setdefault("description_canonical_files", {})
                description_files["de"] = canonical_name
                reconstruction_meta.setdefault("description_source_format", "single_description")
                if not meta["text_slots"]:
                    group = f"{family.object_type}:{object_id}"
                    meta["text_slots"] = [
                        {"slot_key": "short_description", "slot_type": "plain_text", "sort_order": 1, "translation_group_key": group, "storage": {"kind": "description_file_bundle", "files": {"de": canonical_name}}},
                        {"slot_key": "long_description", "slot_type": "plain_text", "sort_order": 2, "translation_group_key": group, "storage": {"kind": "description_file_bundle", "files": {"de": canonical_name}}},
                    ]
                else:
                    for slot in meta["text_slots"]:
                        slot["storage"].setdefault("files", {})["de"] = canonical_name
                asset_meta["description_source_path"] = source_path
            else:
                kind = "image" if family.object_type == "photo" else suffix.lstrip(".")
                variant_files[kind] = canonical_name
                language_asset[f"de.{kind}"] = {"source_path": source_path, "canonical_file": canonical_name}
                asset_meta[{"image": "image_path", "svg": "svg_path", "tex": "tex_path"}[kind]] = source_path
        targets: list[dict[str, Any]] = []
        if family.object_type == "photo" and ".txt" in source_record["files"]:
            targets.append({"path": f"contents/photos/{source_key}.txt", "kind": "rendered_description_file", "slot_keys": ["short_description", "long_description"]})
        if family.object_type == "drawing":
            for suffix, asset_key in ((".svg", "svg_path"), (".tex", "tex_path")):
                if suffix in source_record["files"]:
                    targets.append({"path": f"contents/drawings/{source_key}{suffix}", "kind": "asset_file", "asset_key": asset_key})
            if ".txt" in source_record["files"]:
                targets.append({"path": f"contents/drawings/{source_key}.txt", "kind": "rendered_description_file", "slot_keys": ["short_description", "long_description"]})
        meta["reconstruction"]["targets"] = targets
        write_json(object_dir / "object.references.json", [])
        write_json(object_dir / "object.annotations.json", [])

    meta["active"] = True
    lifecycle = meta.setdefault("metadata", {}).setdefault("lifecycle", {})
    lifecycle["status"] = "active"
    lifecycle.pop("missing_since_revision", None)
    update_tracking(meta, source_record, revision)
    available_languages = present_languages(meta)
    meta["languages"] = [language for language in ("de", "fr", "it") if language in available_languages]
    meta["languages"].extend(sorted(available_languages - {"de", "fr", "it"}))
    if translation_required:
        for language in TARGET_LANGUAGES:
            has_language = language in available_languages
            transition = review_state(meta, language, "to_be_reviewed" if has_language else "to_be_translated")
            if transition:
                transitions.append(transition)
    elif media_review_required:
        for language in TARGET_LANGUAGES:
            if language in available_languages:
                transition = review_state(meta, language, "to_be_reviewed")
                if transition:
                    transitions.append(transition)
    if media_review_required:
        for language in TARGET_LANGUAGES:
            variant = (meta.get("language_variants") or {}).get(language)
            if isinstance(variant, dict):
                variant["review_state"] = "to_be_reviewed"
    write_json(object_dir / "object.meta.json", meta)
    return {"object_id": object_id, "old_source_key": old_key, "review_state_transitions": transitions, "html_alignment": html_alignment}


def mark_missing(record: dict[str, Any], revision: str) -> list[dict[str, str]]:
    meta = record["meta"]
    meta["active"] = False
    lifecycle = meta.setdefault("metadata", {}).setdefault("lifecycle", {})
    lifecycle["status"] = "to_be_deleted"
    lifecycle["missing_since_revision"] = revision
    write_json(record["object_dir"] / "object.meta.json", meta)
    return []


def node_index(root: dict[str, Any]) -> dict[tuple[str, str], dict[str, Any]]:
    result: dict[tuple[str, str], dict[str, Any]] = {}

    def walk(node: dict[str, Any]) -> None:
        ident = next(
            (
                str(item.get("id_value"))
                for item in node.get("identifiers", [])
                if item.get("id_system") in {"edition", "toc_ident"}
            ),
            "",
        )
        if ident:
            result[(str(node.get("node_type")), ident)] = node
        for key in ("chapters", "sections"):
            for child in node.get(key, []):
                walk(child)

    walk(root)
    return result


def localized_structure(
    new_source: dict[str, Any],
    old_source_index: dict[tuple[str, str], dict[str, Any]],
    old_target_index: dict[tuple[str, str], dict[str, Any]],
) -> tuple[dict[str, Any], list[str]]:
    pending_node_ids: list[str] = []

    def localize(node: dict[str, Any]) -> dict[str, Any]:
        localized = json.loads(json.dumps(node))
        ident = next(
            str(item["id_value"])
            for item in node["identifiers"]
            if item["id_system"] in {"edition", "toc_ident"}
        )
        identity = (str(node["node_type"]), ident)
        old_source = old_source_index.get(identity)
        old_target = old_target_index.get(identity)
        changed = old_source is None or old_target is None
        for field in ("title", "abstract"):
            new_value = node.get(field)
            old_value = old_source.get(field) if old_source else None
            if old_source is not None and old_target is not None and old_value == new_value:
                localized[field] = old_target.get(field)
            else:
                localized[field] = new_value
                if new_value is not None:
                    changed = True
        if changed:
            pending_node_ids.append(str(node["id"]))
        for key in ("chapters", "sections"):
            if key in node:
                localized[key] = [localize(child) for child in node[key]]
        return localized

    return localize(new_source), pending_node_ids


def plan_structures(
    source_root: Path,
    canonical_root: Path,
    object_ids: dict[tuple[str, str], str],
) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]], list[str], list[str]]:
    toc_root = source_root / "toc"
    structure_root = canonical_root / "structure" / "editions"
    entries: list[dict[str, Any]] = []
    payloads: dict[str, dict[str, Any]] = {}
    translation_node_ids: set[str] = set()
    errors: list[str] = []

    for toc_path in sorted(toc_root.glob("*.json")):
        edition = toc_path.stem
        source_payload = read_json(toc_path)
        edition_dir = structure_root / edition
        meta_path = edition_dir / "edition.meta.json"
        de_path = edition_dir / "edition.de.json"
        existing_meta = read_json(meta_path) if meta_path.exists() else None
        old_de = read_json(de_path) if de_path.exists() else None
        old_de_index = node_index(old_de) if old_de else {}

        def build_node(raw: dict[str, Any], node_type: str, ident: str, sort_order: int) -> dict[str, Any]:
            old = old_de_index.get((node_type, ident))
            prefix = {"curriculum_root": "ed", "curriculum_chapter": "ch", "curriculum_section": "se"}[node_type]
            node_id = str(old["id"]) if old else stable_node_id(prefix, edition, node_type, ident)
            structural = {"title", "abstract", "ident", "chapters", "sections"}
            node = {
                "id": node_id,
                "node_type": node_type,
                "sort_order": sort_order,
                "title": raw.get("title"),
                "abstract": raw.get("abstract"),
                "identifiers": [{"id_system": "edition" if node_type == "curriculum_root" else "toc_ident", "id_value": ident, "preferred": True}],
                "metadata": {key: value for key, value in raw.items() if key not in structural},
                "placements": [],
            }
            if node_type == "curriculum_root":
                node["chapters"] = [
                    build_node(chapter, "curriculum_chapter", str(chapter.get("ident", f"chapter_{index}")), index)
                    for index, chapter in enumerate(raw.get("chapters", []), start=1)
                ]
            elif node_type == "curriculum_chapter":
                node["sections"] = [
                    build_node(section, "curriculum_section", str(section.get("ident", f"section_{index}")), index)
                    for index, section in enumerate(raw.get("sections", []), start=1)
                ]
            else:
                for order, object_type in enumerate(("section_article", "slide_article"), start=1):
                    object_id = object_ids.get((object_type, ident))
                    if object_id:
                        node["placements"].append({"object_id": object_id, "placement_role": object_type, "sort_order": order, "visible_label": ident})
            return node

        new_de = build_node(source_payload, "curriculum_root", edition, 0)
        missing_targets = any(not (edition_dir / f"edition.{language}.json").is_file() for language in TARGET_LANGUAGES)
        action = "added" if old_de is None else ("unchanged" if old_de == new_de and not missing_targets else "changed")
        target_payloads: dict[str, Any] = {}
        pending_for_edition: set[str] = set()
        if action != "unchanged":
            for language in TARGET_LANGUAGES:
                target_path = edition_dir / f"edition.{language}.json"
                old_source_index = node_index(old_de) if old_de else {}
                old_target_index = node_index(read_json(target_path)) if target_path.exists() else {}
                target, pending = localized_structure(new_de, old_source_index, old_target_index)
                target_payloads[language] = target
                pending_for_edition.update(pending)
        translation_node_ids.update(pending_for_edition)
        payloads[edition] = {
            "meta": existing_meta or {"id": new_de["id"], "edition": edition, "source_path": f"toc/{edition}.json", "node_type": "curriculum_root"},
            "de": new_de,
            "targets": target_payloads,
            "raw_source": toc_path.read_bytes(),
        }
        entries.append({"edition": edition, "action": action, "pending_node_ids": sorted(pending_for_edition)})

    source_editions = {path.stem for path in toc_root.glob("*.json")}
    for edition_dir in sorted(path for path in structure_root.iterdir() if path.is_dir()):
        if edition_dir.name not in source_editions:
            entries.append({"edition": edition_dir.name, "action": "missing", "pending_node_ids": []})
            errors.append(f"source omits complete edition {edition_dir.name}; automatic removal is not supported")
    return entries, payloads, sorted(translation_node_ids), errors


def update_toc_support_asset(canonical_root: Path, edition: str, raw_source: bytes) -> None:
    source_path = f"toc/{edition}.json"
    support_root = canonical_root / "support_assets"
    object_dir = None
    meta = None
    for meta_path in support_root.glob("*/object.meta.json"):
        candidate = read_json(meta_path)
        if (candidate.get("source") or {}).get("path") == source_path:
            object_dir = meta_path.parent
            meta = candidate
            break
    if meta is None:
        object_id = stable_id("sa", "support_asset", f"{edition}.json")
        object_dir = support_root / object_id
        meta = {
            "id": object_id,
            "object_type": "support_asset",
            "active": True,
            "source": {"path": source_path, "format": "json", "key": f"{edition}.json"},
            "identifiers": [{"id_system": "file_path", "id_value": source_path, "preferred": True}],
            "languages": ["de"],
            "review_states": [{"language": "de", "state": "imported_approved"}],
            "metadata": {},
            "asset_files": {},
            "text_slots": [{"slot_key": "body_text", "slot_type": "plain_text", "sort_order": 0, "translation_group_key": None, "storage": {"kind": "text_file", "files": {"de": "body.de.txt"}}}],
            "reconstruction": {"strategy": "replace_source_file", "targets": [{"path": source_path, "kind": "localized_text_file"}]},
        }
        write_json(object_dir / "object.references.json", [])
        write_json(object_dir / "object.annotations.json", [])
    slot = meta["text_slots"][0]
    filename = slot["storage"].setdefault("files", {}).get("de", "body.de.txt")
    slot["storage"]["files"]["de"] = filename
    object_dir.mkdir(parents=True, exist_ok=True)
    (object_dir / filename).write_bytes(raw_source)
    meta["active"] = True
    write_json(object_dir / "object.meta.json", meta)


def apply_structures(canonical_root: Path, payloads: dict[str, dict[str, Any]], entries: list[dict[str, Any]]) -> None:
    actions = {entry["edition"]: entry["action"] for entry in entries}
    for edition, payload in payloads.items():
        if actions[edition] == "unchanged":
            continue
        edition_dir = canonical_root / "structure" / "editions" / edition
        write_json(edition_dir / "edition.meta.json", payload["meta"])
        write_json(edition_dir / "edition.de.json", payload["de"])
        for language, target in payload["targets"].items():
            write_json(edition_dir / f"edition.{language}.json", target)
        update_toc_support_asset(canonical_root, edition, payload["raw_source"])


def build_plan(
    source_root: Path,
    canonical_root: Path,
    *,
    source_revision_override: str | None = None,
) -> tuple[
    dict[str, Any],
    dict[tuple[str, str], dict[str, Any]],
    dict[tuple[str, str], dict[str, Any]],
    dict[str, dict[str, Any]],
]:
    validation = validate_canonical(canonical_root)
    if not validation["valid"]:
        raise RuntimeError(f"Canonical validation failed with {validation['error_count']} errors: {validation['errors'][:5]}")
    source_records = scan_source(source_root)
    canonical_records = load_canonical_index(canonical_root)
    revision = source_revision(source_root, source_records, source_revision_override)
    renames, ambiguous = unique_rename_matches(source_records, canonical_records)
    matched_old = set(renames.values())
    changes: list[dict[str, Any]] = []
    for identity, source_record in sorted(source_records.items()):
        old_identity = identity if identity in canonical_records else renames.get(identity)
        existing = canonical_records.get(old_identity) if old_identity else None
        if existing is None:
            action = "added"
        elif old_identity != identity:
            action = "renamed"
        elif not bool(existing["meta"].get("active", True)):
            action = "reactivated"
        elif existing["fingerprint"] != source_record["fingerprint"]:
            action = "changed"
        else:
            action = "unchanged"
        changed_suffixes = []
        if existing:
            changed_suffixes = sorted(
                suffix for suffix in set(existing["files"]) | set(source_record["files"])
                if existing["files"].get(suffix) != source_record["files"].get(suffix)
            )
        else:
            changed_suffixes = sorted(source_record["files"])
        translation_required = any(
            suffix in {".md", ".html", ".txt", ".tex"} for suffix in changed_suffixes
        )
        media_review_required = identity[0] in {"photo", "drawing"} and any(
            suffix in {".png", ".svg", ".tex"} for suffix in changed_suffixes
        )
        changes.append({
            "action": action,
            "object_id": str(existing["meta"]["id"]) if existing else stable_id(source_record["family"].prefix, identity[0], identity[1]),
            "object_type": identity[0], "source_key": identity[1],
            "previous_source_key": old_identity[1] if old_identity and old_identity != identity else None,
            "changed_suffixes": changed_suffixes,
            "translation_required": translation_required,
            "media_review_required": media_review_required,
        })
    for identity, record in sorted(canonical_records.items()):
        if identity not in source_records and identity not in matched_old:
            changes.append({"action": "missing", "object_id": str(record["meta"]["id"]), "object_type": identity[0], "source_key": identity[1], "previous_source_key": None, "changed_suffixes": [], "translation_required": False, "media_review_required": False})
    html_errors: list[str] = []
    for change in changes:
        if change["action"] not in {"changed", "reactivated"} or change["object_type"] not in {"static_page", "html_include"}:
            continue
        identity = (change["object_type"], change["source_key"])
        existing = canonical_records[identity]
        source_record = source_records[identity]
        old_source = existing["files"].get(".html", b"").decode("utf-8")
        new_source = source_record["files"].get(".html", b"").decode("utf-8")
        files = next(slot["storage"]["files"] for slot in existing["meta"]["text_slots"] if slot.get("slot_type") == "html")
        alignment: dict[str, Any] = {}
        for language in TARGET_LANGUAGES:
            relative_name = files.get(language)
            if not relative_name:
                continue
            try:
                _, stats = merge_html_target(
                    old_source,
                    new_source,
                    (existing["object_dir"] / str(relative_name)).read_text(encoding="utf-8"),
                )
                alignment[language] = {"safe": True, **stats}
            except (OSError, RuntimeError) as exc:
                alignment[language] = {"safe": False, "error": str(exc)}
                html_errors.append(f"{change['object_id']}:{language}: {exc}")
        change["html_alignment"] = alignment
    summary: dict[str, int] = {}
    for change in changes:
        summary[change["action"]] = summary.get(change["action"], 0) + 1
    object_ids = {
        (change["object_type"], change["source_key"]): str(change["object_id"])
        for change in changes
        if change["action"] != "missing"
    }
    structure_entries, structure_payloads, translation_node_ids, structure_errors = plan_structures(
        source_root, canonical_root, object_ids
    )
    report = {
        "schema_version": 1,
        "workflow": "incremental_german_source_import",
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source_root": str(source_root),
        "source_revision": revision,
        "canonical_head_before": subprocess.check_output(["git", "-C", str(REPO_ROOT), "rev-parse", "HEAD"], text=True).strip(),
        "summary": summary,
        "translation_object_ids": sorted(change["object_id"] for change in changes if change["translation_required"]),
        "translation_node_ids": translation_node_ids,
        "ambiguous_rename_candidates": ambiguous,
        "blocking_errors": structure_errors + html_errors,
        "structures": structure_entries,
        "changes": changes,
        "applied": False,
    }
    return report, source_records, canonical_records, structure_payloads


def ensure_clean_canonical() -> None:
    status = subprocess.check_output(["git", "-C", str(REPO_ROOT), "status", "--porcelain", "--", "canonical"], text=True)
    if status.strip():
        raise RuntimeError("Refusing incremental import because canonical/ has uncommitted changes.")


def run_import(
    source_root: Path,
    *,
    canonical_root: Path = CANONICAL_ROOT,
    apply: bool = False,
    report_path: Path | None = None,
    source_revision_override: str | None = None,
) -> dict[str, Any]:
    if apply:
        ensure_clean_canonical()
    report, source_records, canonical_records, structure_payloads = build_plan(
        source_root,
        canonical_root,
        source_revision_override=source_revision_override,
    )
    if apply and (report["ambiguous_rename_candidates"] or report["blocking_errors"]):
        raise RuntimeError("Import plan contains blocking ambiguities or structural errors; inspect the dry-run audit.")
    if apply:
        rename_lookup = {
            (change["object_type"], change["source_key"]): (change["object_type"], change["previous_source_key"])
            for change in report["changes"] if change["action"] == "renamed"
        }
        for change in report["changes"]:
            identity = (change["object_type"], change["source_key"])
            action = change["action"]
            if action == "unchanged":
                continue
            if action == "missing":
                change["review_state_transitions"] = mark_missing(canonical_records[identity], report["source_revision"])
                continue
            old_identity = identity if identity in canonical_records else rename_lookup.get(identity)
            details = apply_source_record(
                canonical_root,
                source_records[identity],
                canonical_records.get(old_identity),
                report["source_revision"],
                action,
                bool(change["translation_required"]),
                bool(change["media_review_required"]),
            )
            change.update(details)
        apply_structures(canonical_root, structure_payloads, report["structures"])
        post_validation = validate_canonical(canonical_root)
        if not post_validation["valid"]:
            raise RuntimeError(f"Post-import canonical validation failed: {post_validation['errors'][:5]}")
        report["applied"] = True
        report["post_validation"] = {"object_count": post_validation["object_count"], "error_count": 0}
    if report_path is None:
        revision_label = re.sub(r"[^0-9A-Za-z._-]", "_", report["source_revision"][:40])
        root = ACCEPTED_REPORT_ROOT if apply else WORK_REPORT_ROOT
        report_path = root / f"german-source-import.{revision_label}.json"
    write_json(report_path, report)
    report["report_path"] = str(report_path)
    return report


def resolve_source_ref(source_ref: str) -> tuple[Path, str, tempfile.TemporaryDirectory[str]]:
    revision = subprocess.check_output(["git", "-C", str(REPO_ROOT), "rev-parse", f"{source_ref}^{{commit}}"], text=True).strip()
    archive = subprocess.check_output(["git", "-C", str(REPO_ROOT), "archive", "--format=tar", revision])
    temporary = tempfile.TemporaryDirectory(prefix="50ohm-main-source-")
    root = Path(temporary.name)
    archive_path = root / "source.tar"
    archive_path.write_bytes(archive)
    with tarfile.open(archive_path) as handle:
        handle.extractall(root, filter="data")
    archive_path.unlink()
    return root, revision, temporary


def main() -> None:
    parser = argparse.ArgumentParser(description="Non-destructively import a newer German source tree into canonical Git.")
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--source-root", type=Path, help="Checkout containing contents/ and toc/.")
    source.add_argument("--source-ref", default="origin/main", help="Git ref to import without creating a checkout (default: origin/main).")
    parser.add_argument("--canonical-root", type=Path, default=CANONICAL_ROOT)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--apply", action="store_true", help="Apply the validated plan. The default is dry-run.")
    args = parser.parse_args()
    temporary = None
    revision_override = None
    if args.source_root:
        source_root = args.source_root.resolve()
    else:
        source_root, revision_override, temporary = resolve_source_ref(args.source_ref)
    try:
        report = run_import(
            source_root,
            canonical_root=args.canonical_root.resolve(),
            apply=args.apply,
            report_path=args.report.resolve() if args.report else None,
            source_revision_override=revision_override,
        )
    finally:
        if temporary is not None:
            temporary.cleanup()
    print(f"report={report['report_path']}")
    print(json.dumps(report["summary"], indent=2, sort_keys=True))
    print(f"translation_objects={len(report['translation_object_ids'])}")
    print(f"applied={report['applied']}")


if __name__ == "__main__":
    main()
