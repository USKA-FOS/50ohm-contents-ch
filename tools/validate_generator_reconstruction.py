from __future__ import annotations

import difflib
import argparse
from collections import Counter
from html import unescape
import json
import re
import shutil
import subprocess
from hashlib import sha256
from pathlib import Path
from typing import Any


CONTENT_REPO = Path(__file__).resolve().parent.parent
WORKSPACE_ROOT = CONTENT_REPO.parents[1]
SOURCE_INPUT = WORKSPACE_ROOT / "translator" / "site-original" / "app" / "50ohm-contents-ch"
APP_ROOT = WORKSPACE_ROOT / "translator" / "sites" / "app"
GENERATOR_ROOT = WORKSPACE_ROOT / "translator" / "50ohm-generator"
SOURCE_OUTPUT = APP_ROOT / "build" / "de"
RECONSTRUCTED_INPUT = CONTENT_REPO / "work" / "site-content"
STAGED_RECONSTRUCTED_INPUT = CONTENT_REPO / "work" / "generator-input" / "de"
RECONSTRUCTED_OUTPUT = CONTENT_REPO / "work" / "build" / "de"
VALIDATION_ROOT = CONTENT_REPO / "work" / "validation" / "generator-de"
IGNORED_COMPARE_PREFIXES = ("contents/questions/",)


def sha256_file(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def tree_manifest(root: Path) -> dict[str, str]:
    return {
        str(path.relative_to(root)): sha256_file(path)
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def compare_trees(left: Path, right: Path) -> dict[str, Any]:
    left_manifest = {
        path: digest
        for path, digest in tree_manifest(left).items()
        if not path.startswith(IGNORED_COMPARE_PREFIXES)
    }
    right_manifest = {
        path: digest
        for path, digest in tree_manifest(right).items()
        if not path.startswith(IGNORED_COMPARE_PREFIXES)
    }
    left_paths = set(left_manifest)
    right_paths = set(right_manifest)
    changed = sorted(path for path in left_paths & right_paths if left_manifest[path] != right_manifest[path])
    return {
        "left_file_count": len(left_manifest),
        "right_file_count": len(right_manifest),
        "only_in_left": sorted(left_paths - right_paths),
        "only_in_right": sorted(right_paths - left_paths),
        "content_mismatches": changed,
    }


def normalize_log(log: str) -> str:
    """Ignore package-install timing emitted by uv's isolated runner."""
    return re.sub(r"Installed (\d+) packages in \d+ms", r"Installed \1 packages in <duration>", log)


def compare_slide_semantics(left_root: Path, right_root: Path, paths: list[str]) -> list[str]:
    question_pattern = re.compile(r'<div class="question-text">(.*?)</div>\s*<div class="answers">(.*?)</div>\s*</div>', re.DOTALL)
    answer_pattern = re.compile(r'<b>[A-D]:</b>\s*(.*?)</p>', re.DOTALL)

    def questions(path: Path) -> Counter[tuple[str, tuple[str, ...]]]:
        return Counter(
            (
                unescape(re.sub(r"\s+", " ", question).strip()),
                tuple(
                    sorted(
                        unescape(re.sub(r"\s+", " ", answer).strip())
                        for answer in answer_pattern.findall(answers)
                    )
                ),
            )
            for question, answers in question_pattern.findall(path.read_text(encoding="utf-8"))
        )

    return [path for path in paths if questions(left_root / path) != questions(right_root / path)]


def build_config(input_root: Path, output_root: Path) -> dict[str, str]:
    return {
        "input": str(input_root),
        "questions": "fragenkatalog_ch.json",
        "questions_upstream": "fragenkatalog_4pre.json",
        "repo_base_url": "https://github.com/USKA-FOS/50ohm-contents-ch",
        "output": str(output_root),
    }


def run_build(label: str, input_root: Path, output_root: Path) -> tuple[int, Path]:
    status_path = VALIDATION_ROOT / f"{label}.status.json"
    if status_path.exists():
        status_path.unlink()
    if output_root.exists():
        shutil.rmtree(output_root)
    output_root.parent.mkdir(parents=True, exist_ok=True)
    log_path = VALIDATION_ROOT / f"{label}.log"
    runner_root = VALIDATION_ROOT / f"generator-{label}"
    if runner_root.exists():
        shutil.rmtree(runner_root)
    # Run from a private generator copy so an interrupted validation can never
    # leave translator/50ohm-generator/config/config.json altered.
    shutil.copytree(GENERATOR_ROOT, runner_root, ignore=shutil.ignore_patterns(".git", "__pycache__", ".venv"))
    (runner_root / "config" / "config.json").write_text(
        json.dumps(build_config(input_root, output_root), indent=2) + "\n", encoding="utf-8"
    )
    completed = subprocess.run(
        ["uv", "run", "python3", "build.py"],
        cwd=runner_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False,
    )
    log_path.write_text(completed.stdout, encoding="utf-8")
    status_path.write_text(
        json.dumps({"exit_code": completed.returncode}, indent=2) + "\n", encoding="utf-8"
    )
    return completed.returncode, log_path


def stage_reconstructed_input() -> None:
    """Keep V4 question inputs constant while validating non-question content."""
    if STAGED_RECONSTRUCTED_INPUT.exists():
        shutil.rmtree(STAGED_RECONSTRUCTED_INPUT)
    shutil.copytree(RECONSTRUCTED_INPUT, STAGED_RECONSTRUCTED_INPUT)
    staged_questions = STAGED_RECONSTRUCTED_INPUT / "contents" / "questions"
    shutil.rmtree(staged_questions)
    shutil.copytree(SOURCE_INPUT / "contents" / "questions", staged_questions)


def ensure_inputs() -> None:
    if not RECONSTRUCTED_INPUT.is_dir():
        raise SystemExit(f"Missing reconstructed input: {RECONSTRUCTED_INPUT}")
    if not SOURCE_INPUT.is_dir():
        raise SystemExit(f"Missing V4 source input: {SOURCE_INPUT}")


def run_source_build() -> None:
    ensure_inputs()
    VALIDATION_ROOT.mkdir(parents=True, exist_ok=True)
    status, _ = run_build("source", SOURCE_INPUT, SOURCE_OUTPUT)
    if status != 0:
        raise SystemExit("Source generator build failed; inspect work/validation/generator-de/source.log")


def run_reconstructed_build() -> None:
    ensure_inputs()
    VALIDATION_ROOT.mkdir(parents=True, exist_ok=True)
    stage_reconstructed_input()
    status, _ = run_build("reconstructed", STAGED_RECONSTRUCTED_INPUT, RECONSTRUCTED_OUTPUT)
    if status != 0:
        raise SystemExit("Reconstructed generator build failed; inspect work/validation/generator-de/reconstructed.log")


def compare_results() -> dict[str, Any]:
    required = [VALIDATION_ROOT / "source.log", VALIDATION_ROOT / "reconstructed.log"]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise SystemExit(f"Cannot compare incomplete builds: {', '.join(missing)}")

    source_status_path = VALIDATION_ROOT / "source.status.json"
    reconstructed_status_path = VALIDATION_ROOT / "reconstructed.status.json"
    source_status = json.loads(source_status_path.read_text())["exit_code"] if source_status_path.exists() else None
    reconstructed_status = (
        json.loads(reconstructed_status_path.read_text())["exit_code"] if reconstructed_status_path.exists() else None
    )
    source_log = VALIDATION_ROOT / "source.log"
    reconstructed_log = VALIDATION_ROOT / "reconstructed.log"

    source_text = source_log.read_text(encoding="utf-8")
    reconstructed_text = reconstructed_log.read_text(encoding="utf-8")
    normalized_source_log = normalize_log(source_text)
    normalized_reconstructed_log = normalize_log(reconstructed_text)
    log_diff = "".join(
        difflib.unified_diff(
            normalized_source_log.splitlines(keepends=True),
            normalized_reconstructed_log.splitlines(keepends=True),
            fromfile="source.log",
            tofile="reconstructed.log",
        )
    )
    diff_path = VALIDATION_ROOT / "logs.diff"
    diff_path.write_text(log_diff, encoding="utf-8")

    comparison = compare_trees(SOURCE_OUTPUT, RECONSTRUCTED_OUTPUT)
    semantic_mismatches = compare_slide_semantics(
        SOURCE_OUTPUT, RECONSTRUCTED_OUTPUT, comparison["content_mismatches"]
    )
    summary: dict[str, Any] = {
        "source_input": str(SOURCE_INPUT),
        "source_output": str(SOURCE_OUTPUT),
        "reconstructed_input": str(STAGED_RECONSTRUCTED_INPUT),
        "reconstructed_output": str(RECONSTRUCTED_OUTPUT),
        "source_build_exit_code": source_status,
        "reconstructed_build_exit_code": reconstructed_status,
        "raw_logs_identical": source_text == reconstructed_text,
        "normalized_logs_identical": not log_diff,
        "site_comparison": comparison,
        "slide_semantic_mismatches": semantic_mismatches,
    }
    summary_path = VALIDATION_ROOT / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--step", choices=("all", "source", "reconstructed", "compare"), default="all")
    args = parser.parse_args()
    if args.step in {"all", "source"}:
        run_source_build()
    if args.step in {"all", "reconstructed"}:
        run_reconstructed_build()
    if args.step in {"all", "compare"}:
        print(json.dumps(compare_results(), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
