#!/usr/bin/env python3
"""Preview or remove known runtime caches and obsolete content-build work."""

from __future__ import annotations

import argparse
import fcntl
import shutil
import subprocess
from contextlib import ExitStack
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
TARGETS: dict[str, tuple[str, ...]] = {
    "generator-input": ("work/generator-input",),
    "canonical-model": ("work/canonical_model",),
    "global-model": ("work/global_model",),
    "build": ("work/build",),
    "build-run1": ("work/build_run1",),
    "generator-copies": tuple(
        f"work/validation/multilingual/generator-{language}"
        for language in ("de", "fr", "it")
    ),
    "uv-cache": ("work/uv-cache",),
}
BUILD_LOCKS = tuple(
    REPO / "work" / "locks" / name
    for name in (
        "canonical-db-rebuild.lock",
        "multilingual-build-de.lock",
        "multilingual-build-fr.lock",
        "multilingual-build-it.lock",
    )
)


def checked_targets(names: list[str]) -> list[Path]:
    paths = [REPO / relative for name in names for relative in TARGETS[name]]
    for path in paths:
        for ancestor in (path, *path.relative_to(REPO).parents):
            candidate = ancestor if isinstance(ancestor, Path) and ancestor.is_absolute() else REPO / ancestor
            if candidate.is_symlink():
                raise ValueError(f"Refusing a symlinked path: {candidate}")
        if path.exists() and not path.is_dir():
            raise ValueError(f"Expected a directory: {path}")
        relative = path.relative_to(REPO)
        tracked = subprocess.run(
            ["git", "-C", str(REPO), "ls-files", "--cached", "--", str(relative)],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
        if tracked:
            raise ValueError(f"Refusing tracked files under {relative}: {tracked.splitlines()[0]}")
    return paths


def size_bytes(path: Path) -> int:
    if not path.exists():
        return 0
    result = subprocess.run(["du", "-sk", "--", str(path)], capture_output=True, text=True, check=True)
    return int(result.stdout.split()[0]) * 1024


def purge(names: list[str], apply: bool = False) -> list[Path]:
    paths = checked_targets(names)
    existing = [path for path in paths if path.exists()]
    sizes = {path: size_bytes(path) for path in paths}
    for path in paths:
        size = sizes[path]
        state = f"{size / (1024 ** 2):.1f} MiB" if path.exists() else "absent"
        print(f"{path.relative_to(REPO)}: {state}")
    print(f"Total: {sum(sizes.values()) / (1024 ** 3):.2f} GiB")
    if not apply:
        print("Preview only. Add --apply to remove these directories.")
        return []

    with ExitStack() as stack:
        for lock_path in BUILD_LOCKS:
            lock_path.parent.mkdir(parents=True, exist_ok=True)
            handle = stack.enter_context(lock_path.open("a+", encoding="utf-8"))
            try:
                fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError as error:
                raise RuntimeError(f"Build in progress; lock is held: {lock_path}") from error
        # Recheck immediately before deletion, after taking the build locks.
        checked_targets(names)
        for path in existing:
            shutil.rmtree(path)
            print(f"Removed: {path.relative_to(REPO)}")
    return existing


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("categories", nargs="*", choices=tuple(TARGETS),
                        help="Default: all listed categories")
    parser.add_argument("--apply", action="store_true", help="Actually remove the listed directories")
    args = parser.parse_args()
    try:
        purge(args.categories or list(TARGETS), apply=args.apply)
    except (ValueError, RuntimeError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Purge refused: {error}\n")


if __name__ == "__main__":
    main()
