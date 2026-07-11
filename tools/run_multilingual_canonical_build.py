from __future__ import annotations

import argparse
import json
import shutil
import sqlite3
import subprocess
from collections import defaultdict
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
from typing import Any

from build_db_from_canonical_model import build_database as build_canonical_database


CONTENT_REPO = Path(__file__).resolve().parent.parent
WORKSPACE_ROOT = CONTENT_REPO.parents[1]
QUESTION_POOL_REPO = CONTENT_REPO.parent / "50ohm-question-pool"
GENERATOR_ROOT = WORKSPACE_ROOT / "translator" / "sites" / "app" / "generator"
SOURCE_INPUT = WORKSPACE_ROOT / "translator" / "site-original" / "app" / "50ohm-contents-ch"
DB_PATH = CONTENT_REPO / "work" / "canonical_model" / "content_model.sqlite"
INPUT_ROOT = CONTENT_REPO / "work" / "generator-input"
BUILD_ROOT = CONTENT_REPO / "work" / "build"
VALIDATION_ROOT = CONTENT_REPO / "work" / "validation" / "multilingual"
LANGUAGES = ("de", "fr", "it")
QUESTION_OBJECT_TYPES = {
    "question",
    "question_catalog_file",
    "question_layout_file",
    "question_metadata_file",
    "questions_readme",
}


def reset_runtime_state() -> None:
    """Remove runtime-only state before deriving anything from canonical Git."""
    for path in (
        DB_PATH,
        VALIDATION_ROOT / "summary.json",
    ):
        if path.exists():
            path.unlink()


def sha256_file(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def tree_manifest(root: Path) -> dict[str, str]:
    if not root.exists():
        return {}
    return {
        str(path.relative_to(root)): sha256_file(path)
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def rows(connection: sqlite3.Connection, sql: str, params: tuple[Any, ...] = ()) -> list[dict[str, Any]]:
    return [dict(row) for row in connection.execute(sql, params)]


def choose_language(values: dict[str, str], language: str) -> str | None:
    return values.get(language) or values.get("de") or next(iter(values.values()), None)


def export_artifacts(connection: sqlite3.Connection, target_root: Path) -> int:
    if target_root.exists():
        shutil.rmtree(target_root)
    target_root.mkdir(parents=True)
    count = 0
    for row in connection.execute("SELECT source_path, payload FROM source_artifact ORDER BY source_path"):
        target = target_root / row["source_path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(row["payload"])
        count += 1
    return count


def append_usage(
    usage: list[dict[str, Any]],
    *,
    path: str,
    action: str,
    origin: str,
    object_id: str | None = None,
    object_type: str | None = None,
    slot_keys: list[str] | None = None,
) -> None:
    usage.append(
        {
            "path": path,
            "action": action,
            "origin": origin,
            "object_id": object_id,
            "object_type": object_type,
            "slot_keys": slot_keys or [],
        }
    )


def overlay_object_texts(connection: sqlite3.Connection, target_root: Path, language: str) -> dict[str, Any]:
    query = """
        SELECT o.id AS object_id, o.object_type, o.source_path, o.source_key,
               s.slot_key, lt.language, lt.text_value
        FROM content_object o
        JOIN text_slot s ON s.object_id = o.id
        JOIN localized_text lt ON lt.text_slot_id = s.id
        WHERE o.object_type NOT IN ({})
        ORDER BY o.id, s.sort_order, lt.language
    """.format(",".join("?" for _ in QUESTION_OBJECT_TYPES))
    grouped: dict[tuple[str, str], dict[str, Any]] = defaultdict(lambda: {"texts": {}})
    for row in rows(connection, query, tuple(sorted(QUESTION_OBJECT_TYPES))):
        key = (row["object_id"], row["slot_key"])
        grouped[key].update(
            {
                "object_type": row["object_type"],
                "source_path": row["source_path"],
                "source_key": row["source_key"],
            }
        )
        grouped[key]["texts"][row["language"]] = row["text_value"]

    by_object: dict[str, dict[str, Any]] = defaultdict(dict)
    written = 0
    usage: list[dict[str, Any]] = []
    for (object_id, slot_key), payload in grouped.items():
        by_object[object_id]["object_type"] = payload["object_type"]
        by_object[object_id]["source_path"] = payload["source_path"]
        by_object[object_id]["source_key"] = payload["source_key"]
        by_object[object_id]["object_id"] = object_id
        by_object[object_id].setdefault("slot_keys", []).append(slot_key)
        by_object[object_id][slot_key] = choose_language(payload["texts"], language)

    for payload in by_object.values():
        object_type = payload["object_type"]
        source_path = payload["source_path"]
        text = payload.get("body_markdown") or payload.get("body_html") or payload.get("body_text")
        if source_path and text is not None and source_path.startswith("contents/"):
            append_usage(
                usage,
                path=str(source_path),
                action="overwritten_from_canonical",
                origin="content_object",
                object_id=str(payload["object_id"]),
                object_type=str(object_type),
                slot_keys=sorted(payload.get("slot_keys", [])),
            )
            (target_root / source_path).write_text(text, encoding="utf-8")
            written += 1
            continue
        if object_type in {"photo", "drawing"} and payload.get("source_key"):
            family = "photos" if object_type == "photo" else "drawings"
            short_text = payload.get("short_description") or ""
            long_text = payload.get("long_description") or short_text
            relative_target = Path("contents") / family / f"{payload['source_key']}.txt"
            append_usage(
                usage,
                path=str(relative_target),
                action="rendered_from_canonical",
                origin="content_object",
                object_id=str(payload["object_id"]),
                object_type=str(object_type),
                slot_keys=sorted(payload.get("slot_keys", [])),
            )
            target = target_root / relative_target
            target.write_text(
                f"1) Kurzbeschreibung:\n{short_text}\n\n2) Ausführliche Beschreibung:\n{long_text}\n",
                encoding="utf-8",
            )
            written += 1
    return {"written_files": written, "usage": usage}


def children_by_parent(connection: sqlite3.Connection, source_path: str) -> dict[str | None, list[dict[str, Any]]]:
    children: dict[str | None, list[dict[str, Any]]] = defaultdict(list)
    for node in rows(
        connection,
        """
        SELECT id, node_type, parent_node_id, sort_order
        FROM curriculum_node
        WHERE source_path=?
        ORDER BY parent_node_id, sort_order
        """,
        (source_path,),
    ):
        children[node["parent_node_id"]].append(node)
    return children


def localized_node_texts(connection: sqlite3.Connection, language: str) -> dict[str, dict[str, str | None]]:
    values: dict[str, dict[str, dict[str, str | None]]] = defaultdict(dict)
    for text in rows(connection, "SELECT node_id, language, title, abstract FROM node_text ORDER BY node_id, language"):
        values[text["node_id"]][text["language"]] = {"title": text["title"], "abstract": text["abstract"]}
    return {node_id: choose_node_language(localized, language) for node_id, localized in values.items()}


def choose_node_language(localized: dict[str, dict[str, str | None]], language: str) -> dict[str, str | None]:
    return localized.get(language) or localized.get("de") or next(iter(localized.values()))


def apply_node_text(payload: dict[str, Any], text: dict[str, str | None] | None) -> None:
    if not text:
        return
    if text.get("title") is not None:
        payload["title"] = text["title"]
    if "abstract" in payload and text.get("abstract") is not None:
        payload["abstract"] = text["abstract"]


def overlay_toc_texts(connection: sqlite3.Connection, target_root: Path, language: str) -> dict[str, Any]:
    node_texts = localized_node_texts(connection, language)
    written = 0
    usage: list[dict[str, Any]] = []
    for toc_path in sorted((target_root / "toc").glob("*.json")):
        source_path = str(toc_path.relative_to(target_root))
        children = children_by_parent(connection, source_path)
        roots = children.get(None, [])
        if not roots:
            continue
        root = roots[0]
        payload = load_json(toc_path)
        apply_node_text(payload, node_texts.get(root["id"]))

        def walk(container: dict[str, Any], parent_id: str) -> None:
            node_children = children.get(parent_id, [])
            json_children = container.get("chapters", container.get("sections", []))
            for node, child_payload in zip(node_children, json_children):
                apply_node_text(child_payload, node_texts.get(node["id"]))
                walk(child_payload, node["id"])

        walk(payload, root["id"])
        append_usage(
            usage,
            path=source_path,
            action="overwritten_from_canonical",
            origin="curriculum_node",
            object_id=str(root["id"]),
            object_type=str(root["node_type"]),
            slot_keys=["title", "abstract"],
        )
        write_json(toc_path, payload)
        written += 1
    return {"written_files": written, "usage": usage}


def iter_questions(payload: dict[str, Any]):
    for exam_part in payload.get("sections", []):
        for chapter in exam_part.get("sections", []):
            for question in chapter.get("questions", []):
                yield question
            for section in chapter.get("sections", []):
                for question in section.get("questions", []):
                    yield question


def source_rationales() -> tuple[dict[str, Any], dict[str, Any]]:
    source = load_json(SOURCE_INPUT / "contents" / "questions" / "fragenkatalog_ch.json")
    rationales = {question["number"]: question.get("HB.rationale") for question in iter_questions(source)}
    return rationales, deepcopy(source.get("pruned", {}))


def stage_questions(target_root: Path, language: str) -> dict[str, Any]:
    questions_dir = target_root / "contents" / "questions"
    questions_dir.mkdir(parents=True, exist_ok=True)
    source_build = QUESTION_POOL_REPO / "builds" / language / f"question_pool_rev0_ch-{language}.json"
    payload = load_json(source_build)
    rationales, pruned = source_rationales()
    question_count = 0
    for question in iter_questions(payload):
        number = question.get("number")
        question["HB.rationale"] = rationales.get(number) if language == "de" else None
        question_count += 1
    payload["pruned"] = pruned if language == "de" else {}
    write_json(questions_dir / "fragenkatalog_ch.json", payload)
    # The review generator shows correction/diff markup whenever the upstream
    # catalog differs from the selected catalog. For localized builds, the
    # canonical question-pool build is the source of truth, so the upstream
    # compatibility file must be identical.
    write_json(questions_dir / "fragenkatalog_4pre.json", payload)
    return {
        "question_catalog": str(source_build),
        "questions": question_count,
        "usage": [
            {
                "path": "contents/questions/fragenkatalog_ch.json",
                "action": "overwritten_from_question_pool",
                "origin": "question_pool",
                "object_id": None,
                "object_type": "question_catalog_file",
                "slot_keys": [],
            },
            {
                "path": "contents/questions/fragenkatalog_4pre.json",
                "action": "overwritten_from_question_pool",
                "origin": "question_pool",
                "object_id": None,
                "object_type": "question_catalog_file",
                "slot_keys": [],
            },
        ],
    }


def retained_support_artifacts(target_root: Path, usage_entries: list[dict[str, Any]]) -> list[str]:
    replaced = {entry["path"] for entry in usage_entries}
    retained: list[str] = []
    for path in sorted(target_root.rglob("*")):
        if not path.is_file():
            continue
        relative = str(path.relative_to(target_root))
        if relative not in replaced:
            retained.append(relative)
    return retained


def usage_action_counts(usage_entries: list[dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for entry in usage_entries:
        action = str(entry["action"])
        counts[action] = counts.get(action, 0) + 1
    return counts


def stage_language(connection: sqlite3.Connection, language: str) -> dict[str, Any]:
    target_root = INPUT_ROOT / language
    artifact_count = export_artifacts(connection, target_root)
    text_report = overlay_object_texts(connection, target_root, language)
    toc_report = overlay_toc_texts(connection, target_root, language)
    question_info = stage_questions(target_root, language)
    usage_entries = text_report["usage"] + toc_report["usage"] + question_info["usage"]
    retained = retained_support_artifacts(target_root, usage_entries)
    usage_report = {
        "language": language,
        "replaced_or_rendered": usage_entries,
        "retained_paths": retained,
        "retained_count": len(retained),
        "action_counts": usage_action_counts(usage_entries),
    }
    usage_report_path = VALIDATION_ROOT / f"support-artifact-usage-{language}.json"
    write_json(usage_report_path, usage_report)
    return {
        "input_root": str(target_root),
        "source_artifacts": artifact_count,
        "localized_text_files": text_report["written_files"],
        "localized_toc_files": toc_report["written_files"],
        "question_catalog": question_info["question_catalog"],
        "questions": question_info["questions"],
        "support_artifact_usage": {
            "report_path": str(usage_report_path),
            "replaced_or_rendered_count": len(usage_entries),
            "action_counts": usage_report["action_counts"],
            "retained_paths": retained[:500],
            "retained_count": len(retained),
        },
    }


def build_config(input_root: Path, output_root: Path) -> dict[str, str]:
    return {
        "input": str(input_root),
        "questions": "fragenkatalog_ch.json",
        "questions_upstream": "fragenkatalog_4pre.json",
        "repo_base_url": "https://github.com/USKA-FOS/50ohm-contents-ch",
        "output": str(output_root),
    }


def run_generator(language: str) -> dict[str, Any]:
    VALIDATION_ROOT.mkdir(parents=True, exist_ok=True)
    runner_root = VALIDATION_ROOT / f"generator-{language}"
    output_root = BUILD_ROOT / language
    BUILD_ROOT.mkdir(parents=True, exist_ok=True)
    if runner_root.exists():
        shutil.rmtree(runner_root)
    if output_root.exists():
        shutil.rmtree(output_root)
    shutil.copytree(GENERATOR_ROOT, runner_root, ignore=shutil.ignore_patterns(".git", "__pycache__", ".venv"))
    write_json(runner_root / "config" / "config.json", build_config(INPUT_ROOT / language, output_root))
    completed = subprocess.run(
        ["uv", "run", "python3", "build.py"],
        cwd=runner_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False,
    )
    log_path = VALIDATION_ROOT / f"{language}.log"
    log_path.write_text(completed.stdout, encoding="utf-8")
    return {
        "exit_code": completed.returncode,
        "log": str(log_path),
        "output_root": str(output_root),
        "output_files": len(tree_manifest(output_root)),
    }


def compare_outputs(builds: dict[str, dict[str, Any]]) -> dict[str, Any]:
    manifests = {language: tree_manifest(BUILD_ROOT / language) for language in LANGUAGES}
    result: dict[str, Any] = {}
    for language in LANGUAGES:
        manifest = manifests[language]
        result[language] = {
            "file_count": len(manifest),
            "html_count": sum(1 for path in manifest if path.endswith(".html")),
            "asset_count": sum(1 for path in manifest if path.startswith("assets/")),
        }
    de_paths = set(manifests["de"])
    for language in ("fr", "it"):
        paths = set(manifests[language])
        result[f"de_vs_{language}"] = {
            "only_in_de": sorted(de_paths - paths)[:200],
            "only_in_language": sorted(paths - de_paths)[:200],
            "only_in_de_count": len(de_paths - paths),
            "only_in_language_count": len(paths - de_paths),
        }
    result["all_builds_succeeded"] = all(builds[language]["exit_code"] == 0 for language in LANGUAGES)
    return result


def run(*, skip_build: bool = False) -> dict[str, Any]:
    reset_runtime_state()
    db_counts = build_canonical_database()
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    staged = {language: stage_language(connection, language) for language in LANGUAGES}
    connection.close()

    builds = {language: run_generator(language) for language in LANGUAGES} if not skip_build else {}
    comparison = compare_outputs(builds) if builds else {}
    report = {
        "database": str(DB_PATH),
        "database_counts": db_counts,
        "staged": staged,
        "builds": builds,
        "comparison": comparison,
    }
    write_json(VALIDATION_ROOT / "summary.json", report)
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-build", action="store_true")
    args = parser.parse_args()
    report = run(skip_build=args.skip_build)
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
