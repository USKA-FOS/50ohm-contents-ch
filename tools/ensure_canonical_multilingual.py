from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from build_content_model_db import stable_id


REPO_ROOT = Path(__file__).resolve().parent.parent
CANONICAL_ROOT = REPO_ROOT / "canonical"
TARGET_LANGUAGES = ("de", "fr", "it")
QUESTION_OBJECT_TYPES = {
    "question",
    "question_catalog_file",
    "question_layout_file",
    "question_metadata_file",
    "questions_readme",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def object_types() -> dict[str, str]:
    result: dict[str, str] = {}
    for path in (CANONICAL_ROOT / "objects").glob("*/*.json"):
        payload = load_json(path)
        result[payload["id"]] = payload["object_type"]
    return result


def ensure_payload(path: Path, source_payload_path: Path) -> None:
    if not path.exists():
        path.write_text(source_payload_path.read_text(encoding="utf-8"), encoding="utf-8")


def ensure_slot_languages(types_by_object: dict[str, str], *, dry_run: bool) -> int:
    changed = 0
    for path in sorted((CANONICAL_ROOT / "texts" / "slots").glob("*.json")):
        slot = load_json(path)
        if types_by_object.get(slot["object_id"]) in QUESTION_OBJECT_TYPES:
            continue
        localized = slot.get("localized", [])
        by_language = {entry["language"]: entry for entry in localized}
        source = by_language.get("de") or next(iter(by_language.values()), None)
        if source is None:
            continue
        source_payload_path = CANONICAL_ROOT / source["path"]
        for language in TARGET_LANGUAGES:
            if language in by_language:
                continue
            localized_id = stable_id("ltxt", slot["id"], language)
            payload_path = Path("texts") / "payload" / f"{localized_id}.txt"
            localized.append(
                {
                    "id": localized_id,
                    "language": language,
                    "path": str(payload_path),
                    "text_slot_id": slot["id"],
                }
            )
            changed += 1
            if not dry_run:
                ensure_payload(CANONICAL_ROOT / payload_path, source_payload_path)
        if not dry_run and changed:
            slot["localized"] = sorted(localized, key=lambda entry: (entry["text_slot_id"], entry["language"]))
            write_json(path, slot)
    return changed


def ensure_node_languages(*, dry_run: bool) -> int:
    changed = 0
    existing_by_node_language: dict[tuple[str, str], dict[str, Any]] = {}
    for path in sorted((CANONICAL_ROOT / "texts" / "nodes").glob("*.json")):
        payload = load_json(path)
        payload["_path"] = path
        existing_by_node_language[(payload["node_id"], payload["language"])] = payload

    source_by_node: dict[str, dict[str, Any]] = {}
    for (node_id, language), payload in existing_by_node_language.items():
        if language == "de":
            source_by_node[node_id] = payload
    for (node_id, _), payload in existing_by_node_language.items():
        source_by_node.setdefault(node_id, payload)

    for node_id, source in sorted(source_by_node.items()):
        for language in TARGET_LANGUAGES:
            if (node_id, language) in existing_by_node_language:
                continue
            node_text_id = stable_id("ntxt", node_id, language)
            created: dict[str, Any] = {
                "id": node_text_id,
                "language": language,
                "node_id": node_id,
            }
            for field in ("title", "abstract"):
                source_path = source.get(f"{field}_path")
                if source_path is None:
                    created[f"{field}_path"] = None
                    continue
                payload_path = Path("texts") / "node_payload" / f"{node_text_id}_{field}.txt"
                created[f"{field}_path"] = str(payload_path)
                if not dry_run:
                    ensure_payload(CANONICAL_ROOT / payload_path, CANONICAL_ROOT / source_path)
            changed += 1
            if not dry_run:
                write_json(CANONICAL_ROOT / "texts" / "nodes" / f"{node_text_id}.json", created)
    return changed


def ensure_review_languages(types_by_object: dict[str, str], *, dry_run: bool) -> int:
    changed = 0
    for subject_id, object_type in sorted(types_by_object.items()):
        if object_type in QUESTION_OBJECT_TYPES:
            continue
        path = CANONICAL_ROOT / "review" / "content_object" / f"{subject_id}.json"
        if not path.exists():
            continue
        states = load_json(path)
        by_language = {state.get("language"): state for state in states}
        source_state = by_language.get("de", {}).get("state", "imported_approved")
        for language in TARGET_LANGUAGES:
            if language in by_language:
                continue
            states.append(
                {
                    "id": stable_id("rvs", "content_object", subject_id, language, source_state),
                    "language": language,
                    "state": source_state,
                    "subject_id": subject_id,
                    "subject_kind": "content_object",
                }
            )
            changed += 1
        if not dry_run:
            write_json(path, sorted(states, key=lambda state: (str(state.get("language")), state["id"])))
    return changed


def ensure_multilingual(*, dry_run: bool = False) -> dict[str, int]:
    types_by_object = object_types()
    return {
        "slot_localizations_added": ensure_slot_languages(types_by_object, dry_run=dry_run),
        "node_localizations_added": ensure_node_languages(dry_run=dry_run),
        "review_states_added": ensure_review_languages(types_by_object, dry_run=dry_run),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    print(json.dumps(ensure_multilingual(dry_run=args.dry_run), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
