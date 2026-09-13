from __future__ import annotations

import json
import subprocess
from pathlib import Path

import pytest

from tools import run_multilingual_canonical_build as build


def git(repository: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(repository), *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return completed.stdout.strip()


def initialize_release_repository(repository: Path) -> None:
    repository.mkdir()
    git(repository, "init", "-b", "main")
    git(repository, "config", "user.name", "Release Test")
    git(repository, "config", "user.email", "release-test@example.invalid")
    for language in build.LANGUAGES:
        language_root = repository / language
        language_root.mkdir()
        (language_root / "index.html").write_text(f"old {language}\n", encoding="utf-8")
    feedback_root = repository / "feedback"
    feedback_root.mkdir()
    (feedback_root / "index.html").write_text("feedback\n", encoding="utf-8")
    (repository / build.RELEASE_MANIFEST_NAME).write_text("{}\n", encoding="utf-8")
    git(repository, "add", ".")
    git(repository, "commit", "-m", "Initial release")


def create_build_tree(root: Path) -> None:
    root.mkdir()
    for language in build.LANGUAGES:
        language_root = root / language
        language_root.mkdir()
        (language_root / "index.html").write_text(f"new {language}\n", encoding="utf-8")
    (root / build.RELEASE_MANIFEST_NAME).write_text(
        json.dumps({"release_id": "beta-test-1"}) + "\n",
        encoding="utf-8",
    )


def test_release_request_requires_complete_build_and_release_id() -> None:
    with pytest.raises(ValueError, match="requires --release-id"):
        build.validate_release_request(
            release_id=None,
            release_output=Path("release"),
            beta=False,
            feedback_url=build.DEFAULT_FEEDBACK_URL,
            skip_build=False,
            languages=build.LANGUAGES,
        )

    with pytest.raises(ValueError, match="complete de/fr/it"):
        build.validate_release_request(
            release_id="beta-test-1",
            release_output=None,
            beta=True,
            feedback_url=build.DEFAULT_FEEDBACK_URL,
            skip_build=False,
            languages=("de",),
        )

    with pytest.raises(ValueError, match="safe as a Git tag"):
        build.validate_release_request(
            release_id="beta..test",
            release_output=None,
            beta=True,
            feedback_url=build.DEFAULT_FEEDBACK_URL,
            skip_build=False,
            languages=build.LANGUAGES,
        )


def test_release_manifest_describes_each_language_tree(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    build_root = tmp_path / "build"
    create_build_tree(build_root)
    monkeypatch.setattr(build, "BUILD_ROOT", build_root)
    sources = {
        "contents": {"repository": "contents", "commit": "a" * 40, "tags": []},
        "questions": {"repository": "questions", "commit": "b" * 40, "tags": ["Revision_2.6"]},
        "generator": {"repository": "generator", "commit": "c" * 40, "tags": []},
    }

    manifest = build.build_release_manifest(
        release_id="beta-test-1",
        beta=True,
        feedback_url=build.DEFAULT_FEEDBACK_URL,
        generator_seed=50,
        sources=sources,
    )

    assert manifest["release_id"] == "beta-test-1"
    assert manifest["release_tag"] == "beta-test-1"
    assert manifest["beta"] is True
    assert manifest["sources"] == sources
    assert set(manifest["artifacts"]) == set(build.LANGUAGES)
    assert all(manifest["artifacts"][language]["file_count"] == 1 for language in build.LANGUAGES)
    assert all(len(manifest["artifacts"][language]["sha256"]) == 64 for language in build.LANGUAGES)


def test_promotion_moves_release_and_preserves_feedback(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    release_repository = tmp_path / "release"
    initialize_release_repository(release_repository)
    build_root = tmp_path / "build"
    create_build_tree(build_root)
    review_root = tmp_path / "review-build"
    monkeypatch.setattr(build, "REVIEW_BUILD_ROOT", review_root)

    result = build.promote_release(build_root, release_repository, "beta-test-1")

    assert result["release_id"] == "beta-test-1"
    assert not (build_root / "de").exists()
    assert not (build_root / build.RELEASE_MANIFEST_NAME).exists()
    assert (release_repository / "de" / "index.html").read_text(encoding="utf-8") == "new de\n"
    assert (release_repository / "feedback" / "index.html").read_text(encoding="utf-8") == "feedback\n"
    assert json.loads((release_repository / build.RELEASE_MANIFEST_NAME).read_text(encoding="utf-8")) == {
        "release_id": "beta-test-1"
    }
    for language in build.LANGUAGES:
        assert (review_root / language).resolve() == (release_repository / language).resolve()
    assert not list(release_repository.glob(".release-promotion-backup-*"))


def test_promotion_rejects_dirty_release_repository(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    release_repository = tmp_path / "release"
    initialize_release_repository(release_repository)
    (release_repository / "de" / "index.html").write_text("local change\n", encoding="utf-8")
    build_root = tmp_path / "build"
    create_build_tree(build_root)
    monkeypatch.setattr(build, "REVIEW_BUILD_ROOT", tmp_path / "review-build")

    with pytest.raises(RuntimeError, match="Release repository is not clean"):
        build.promote_release(build_root, release_repository, "beta-test-1")

    assert (build_root / "de" / "index.html").read_text(encoding="utf-8") == "new de\n"
    assert (release_repository / "feedback" / "index.html").read_text(encoding="utf-8") == "feedback\n"


def test_promotion_rejects_existing_release_tag(tmp_path: Path) -> None:
    release_repository = tmp_path / "release"
    initialize_release_repository(release_repository)
    git(release_repository, "tag", "beta-test-1")
    build_root = tmp_path / "build"
    create_build_tree(build_root)

    with pytest.raises(RuntimeError, match="Release tag already exists"):
        build.promote_release(build_root, release_repository, "beta-test-1")
