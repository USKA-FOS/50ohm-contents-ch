from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CANONICAL_ROOT = REPO_ROOT / "canonical"
OBJECT_ID_RE = re.compile(r"^[a-z]{1,3}_[0-9a-f]{12}$")
OBJECT_FAMILIES = {
    "sections",
    "slides",
    "solutions",
    "snippets",
    "static_pages",
    "html_includes",
    "photos",
    "drawings",
    "tables",
    "legal_documents",
    "support_assets",
}
STORAGE_KINDS = {"text_file", "json_file", "description_file_bundle"}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def structure_signature(node: dict[str, Any]) -> dict[str, Any]:
    return {
        key: (
            [structure_signature(child) for child in value]
            if key in {"chapters", "sections"} and isinstance(value, list)
            else value
        )
        for key, value in node.items()
        if key not in {"title", "abstract"}
    }


def validate_canonical(canonical_root: Path = DEFAULT_CANONICAL_ROOT) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    object_ids: dict[str, Path] = {}
    source_identities: dict[tuple[str, str], Path] = {}
    object_count = 0

    for family in sorted(OBJECT_FAMILIES):
        family_root = canonical_root / family
        if not family_root.exists():
            warnings.append(f"missing optional family directory: {family}")
            continue
        for object_dir in sorted(path for path in family_root.iterdir() if path.is_dir()):
            object_count += 1
            meta_path = object_dir / "object.meta.json"
            references_path = object_dir / "object.references.json"
            annotations_path = object_dir / "object.annotations.json"
            for required in (meta_path, references_path, annotations_path):
                if not required.is_file():
                    errors.append(f"missing required file: {required.relative_to(canonical_root)}")
            if not meta_path.is_file():
                continue
            try:
                meta = read_json(meta_path)
            except (OSError, json.JSONDecodeError) as exc:
                errors.append(f"invalid JSON {meta_path.relative_to(canonical_root)}: {exc}")
                continue

            object_id = str(meta.get("id", ""))
            if not OBJECT_ID_RE.fullmatch(object_id):
                errors.append(f"invalid object id {object_id!r}: {meta_path.relative_to(canonical_root)}")
            if object_dir.name != object_id:
                errors.append(f"directory/id mismatch: {object_dir.name} != {object_id}")
            if object_id in object_ids:
                errors.append(
                    f"duplicate object id {object_id}: {object_ids[object_id].relative_to(canonical_root)} and "
                    f"{meta_path.relative_to(canonical_root)}"
                )
            object_ids[object_id] = meta_path

            object_type = str(meta.get("object_type", ""))
            source = meta.get("source")
            if not isinstance(source, dict):
                errors.append(f"missing source object: {meta_path.relative_to(canonical_root)}")
            else:
                source_key = source.get("key")
                if source_key is not None:
                    identity = (object_type, str(source_key))
                    if identity in source_identities:
                        errors.append(
                            f"duplicate source identity {identity}: "
                            f"{source_identities[identity].relative_to(canonical_root)} and "
                            f"{meta_path.relative_to(canonical_root)}"
                        )
                    source_identities[identity] = meta_path

            slots = meta.get("text_slots")
            if not isinstance(slots, list):
                errors.append(f"text_slots must be a list: {meta_path.relative_to(canonical_root)}")
                continue
            slot_keys: set[str] = set()
            declared_languages = {str(value) for value in meta.get("languages", [])}
            lifecycle_status = (((meta.get("metadata") or {}).get("lifecycle") or {}).get("status"))
            if not bool(meta.get("active", True)) and lifecycle_status != "to_be_deleted":
                errors.append(f"inactive object lacks lifecycle.status=to_be_deleted: {object_id}")
            for slot in slots:
                if not isinstance(slot, dict):
                    errors.append(f"invalid text slot: {meta_path.relative_to(canonical_root)}")
                    continue
                slot_key = str(slot.get("slot_key", ""))
                if not slot_key or slot_key in slot_keys:
                    errors.append(f"missing or duplicate slot_key {slot_key!r}: {meta_path.relative_to(canonical_root)}")
                slot_keys.add(slot_key)
                storage = slot.get("storage")
                if not isinstance(storage, dict) or storage.get("kind") not in STORAGE_KINDS:
                    errors.append(f"invalid storage for {object_id}.{slot_key}")
                    continue
                files = storage.get("files")
                if not isinstance(files, dict):
                    errors.append(f"storage.files must be an object for {object_id}.{slot_key}")
                    continue
                for language, relative_name in files.items():
                    payload_path = object_dir / str(relative_name)
                    if not payload_path.is_file():
                        errors.append(f"missing payload {object_id}.{slot_key}.{language}: {relative_name}")
                    if str(language) not in declared_languages:
                        errors.append(f"undeclared payload language {object_id}.{slot_key}.{language}")

            language_variants = meta.get("language_variants") or {}
            if not isinstance(language_variants, dict):
                errors.append(f"language_variants must be an object: {object_id}")
            else:
                for language, variant in language_variants.items():
                    if str(language) not in declared_languages:
                        warnings.append(f"asset language absent from languages list {object_id}.{language}")
                    if not isinstance(variant, dict):
                        errors.append(f"language variant must be an object: {object_id}.{language}")
                        continue
                    asset_files = variant.get("asset_files") or {}
                    if not isinstance(asset_files, dict):
                        errors.append(f"asset_files must be an object: {object_id}.{language}")
                        continue
                    for asset_kind, relative_name in asset_files.items():
                        if not (object_dir / str(relative_name)).is_file():
                            errors.append(f"missing asset {object_id}.{language}.{asset_kind}: {relative_name}")

            for auxiliary_path in (references_path, annotations_path):
                if not auxiliary_path.is_file():
                    continue
                try:
                    payload = read_json(auxiliary_path)
                except (OSError, json.JSONDecodeError) as exc:
                    errors.append(f"invalid JSON {auxiliary_path.relative_to(canonical_root)}: {exc}")
                    continue
                if not isinstance(payload, list):
                    errors.append(f"expected JSON list: {auxiliary_path.relative_to(canonical_root)}")
                elif auxiliary_path == references_path:
                    for reference in payload:
                        if not isinstance(reference, dict):
                            errors.append(f"invalid reference in {object_id}")
                            continue
                        if str(reference.get("source_slot_key", "")) not in slot_keys:
                            errors.append(
                                f"reference uses unknown slot {object_id}.{reference.get('source_slot_key')}"
                            )

    structure_root = canonical_root / "structure" / "editions"
    if not structure_root.is_dir():
        errors.append("missing structure/editions directory")
    else:
        node_ids: dict[str, Path] = {}
        for edition_dir in sorted(path for path in structure_root.iterdir() if path.is_dir()):
            meta_path = edition_dir / "edition.meta.json"
            de_path = edition_dir / "edition.de.json"
            for required in (meta_path, de_path):
                if not required.is_file():
                    errors.append(f"missing required structure file: {required.relative_to(canonical_root)}")
            if not de_path.is_file():
                continue
            try:
                de_tree = read_json(de_path)
            except (OSError, json.JSONDecodeError) as exc:
                errors.append(f"invalid JSON {de_path.relative_to(canonical_root)}: {exc}")
                continue
            if not isinstance(de_tree, dict):
                errors.append(f"edition tree must be an object: {de_path.relative_to(canonical_root)}")
                continue

            def validate_node(node: Any, path: Path) -> None:
                if not isinstance(node, dict):
                    errors.append(f"structure node must be an object: {path.relative_to(canonical_root)}")
                    return
                node_id = str(node.get("id", ""))
                if not OBJECT_ID_RE.fullmatch(node_id):
                    errors.append(f"invalid structure node id {node_id!r}: {path.relative_to(canonical_root)}")
                elif node_id in node_ids:
                    errors.append(f"duplicate structure node id {node_id}: {path.relative_to(canonical_root)}")
                else:
                    node_ids[node_id] = path
                for placement in node.get("placements", []):
                    if not isinstance(placement, dict) or str(placement.get("object_id", "")) not in object_ids:
                        errors.append(f"structure placement references unknown object: {node_id}")
                for child_key in ("chapters", "sections"):
                    children = node.get(child_key, [])
                    if not isinstance(children, list):
                        errors.append(f"{child_key} must be a list: {node_id}")
                        continue
                    for child in children:
                        validate_node(child, path)

            validate_node(de_tree, de_path)
            de_signature = structure_signature(de_tree)
            for language in ("fr", "it"):
                target_path = edition_dir / f"edition.{language}.json"
                if not target_path.exists():
                    warnings.append(f"missing structure language: {target_path.relative_to(canonical_root)}")
                    continue
                try:
                    target_tree = read_json(target_path)
                except (OSError, json.JSONDecodeError) as exc:
                    errors.append(f"invalid JSON {target_path.relative_to(canonical_root)}: {exc}")
                    continue
                if not isinstance(target_tree, dict) or structure_signature(target_tree) != de_signature:
                    errors.append(f"localized structure differs outside text fields: {target_path.relative_to(canonical_root)}")

    result = {
        "canonical_root": str(canonical_root),
        "object_count": object_count,
        "error_count": len(errors),
        "warning_count": len(warnings),
        "errors": errors,
        "warnings": warnings,
        "valid": not errors,
    }
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate the object-centric canonical model.")
    parser.add_argument("--canonical-root", type=Path, default=DEFAULT_CANONICAL_ROOT)
    args = parser.parse_args()
    report = validate_canonical(args.canonical_root.resolve())
    print(json.dumps(report, indent=2, ensure_ascii=False))
    if not report["valid"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
