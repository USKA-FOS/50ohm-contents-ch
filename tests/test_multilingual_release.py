from __future__ import annotations

import json
import subprocess
from pathlib import Path

import pytest
from jinja2 import Environment, FileSystemLoader

from tools import run_multilingual_canonical_build as build
from tools import import_incremental_german_source as importer


EXTRA_CONTENT_ROOT = Path(__file__).resolve().parents[1] / "generator_extra_content"


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


def test_read_only_build_accepts_dirty_tools_and_records_actual_source(tmp_path: Path, monkeypatch) -> None:
    repository = tmp_path / "source"
    initialize_release_repository(repository)
    clean = build.source_repository_state(repository, "source")
    (repository / "tool.py").write_text("print('local tool')\n", encoding="utf-8")
    changed = build.source_repository_state(repository, "source")
    assert changed["commit"] == clean["commit"]
    assert changed["dirty"] is True
    assert changed["worktree_sha256"] != clean["worktree_sha256"]
    (repository / "tool.py").write_text("print('new local tool')\n", encoding="utf-8")
    assert build.source_repository_state(repository, "source")["worktree_sha256"] != changed["worktree_sha256"]
    monkeypatch.setattr(build, "release_source_states", lambda: {"source": build.source_repository_state(repository, "source")})
    with pytest.raises(RuntimeError, match="changed during the build"):
        build.verify_release_source_states({"source": changed})


def test_source_fingerprint_detects_dirty_canonical_and_deletions(tmp_path: Path) -> None:
    repository = tmp_path / "source"
    initialize_release_repository(repository)
    canonical = repository / "canonical"
    canonical.mkdir()
    material = canonical / "body.de.md"
    material.write_text("German text\n", encoding="utf-8")
    git(repository, "add", "canonical")
    git(repository, "commit", "-m", "Add material")
    before = build.source_repository_state(repository, "source")
    material.write_text("Updated German text\n", encoding="utf-8")
    after = build.source_repository_state(repository, "source")
    assert after["dirty"] is True
    assert before["worktree_sha256"] != after["worktree_sha256"]
    material.unlink()
    assert build.source_repository_state(repository, "source")["worktree_sha256"] != after["worktree_sha256"]


def test_cli_expected_failure_is_reported_without_traceback(monkeypatch, capsys) -> None:
    def fail(**kwargs):
        raise RuntimeError("test validation error")
    monkeypatch.setattr(build, "run", fail)
    monkeypatch.setattr(build.sys, "argv", ["build"])
    with pytest.raises(SystemExit) as exc:
        build.main()
    assert exc.value.code == 1
    assert capsys.readouterr().err == "Build failed: test validation error\n"


def test_canonical_writer_blocks_dirty_material_but_not_dirty_tools(tmp_path, monkeypatch) -> None:
    repository = tmp_path / "source"
    initialize_release_repository(repository)
    material = repository / "canonical" / "body.de.md"
    material.parent.mkdir()
    material.write_text("German text\n", encoding="utf-8")
    git(repository, "add", "canonical")
    git(repository, "commit", "-m", "Add material")
    monkeypatch.setattr(importer, "REPO_ROOT", repository)
    (repository / "tool.py").write_text("local tool\n", encoding="utf-8")
    importer.ensure_clean_canonical()
    material.write_text("Local material\n", encoding="utf-8")
    with pytest.raises(RuntimeError, match="canonical/ has uncommitted changes"):
        importer.ensure_clean_canonical()


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


def test_generator_config_receives_release_context_only_in_release_mode() -> None:
    development = build.build_config(Path("input"), Path("output"), generator_seed=50)
    release = build.build_config(
        Path("input"),
        Path("output"),
        generator_seed=50,
        release_id="beta-test-1",
        beta=True,
        feedback_url="https://example.invalid/feedback",
    )

    assert "release_id" not in development
    assert "beta" not in development
    assert "feedback_url" not in development
    assert release["release_id"] == "beta-test-1"
    assert release["beta"] is True
    assert release["feedback_url"] == "https://example.invalid/feedback"


@pytest.mark.parametrize("language", build.LANGUAGES)
def test_release_fragments_use_localized_labels(language: str) -> None:
    labels = json.loads((EXTRA_CONTENT_ROOT / language / "labels.json").read_text(encoding="utf-8"))
    environment = Environment(loader=FileSystemLoader(EXTRA_CONTENT_ROOT / "de" / "templates"))
    environment.globals.update(
        ui=lambda key, default="": labels.get(key, default),
        lang=language,
        release_id="beta-test-1",
        beta=True,
        feedback_url="https://50ohm.jp2s.ch/feedback",
    )

    regular = environment.get_template("html/release-beta-warning.html").render()
    footer = environment.get_template("html/release-footer.html").render()
    slide = environment.get_template("slide/release-overlay.html").render()

    assert labels["beta_disclaimer"] in regular
    assert labels["feedback_button"] in regular
    assert "beta-test-1" in footer
    assert "window.location.pathname" in footer
    assert labels["beta_disclaimer"] in slide
    assert "beta-test-1" in slide


def test_generator_status_widget_handles_missing_status_file() -> None:
    template = (
        Path(__file__).resolve().parents[2]
        / "50ohm-generator"
        / "templates"
        / "html"
        / "generator_status.html"
    ).read_text(encoding="utf-8")
    assert ".catch(() =>" in template
    assert "generator_status.json" in template


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


def test_promotion_replaces_dirty_generated_artifacts_and_preserves_other_paths(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    release_repository = tmp_path / "release"
    initialize_release_repository(release_repository)
    (release_repository / "de" / "index.html").write_text("local change\n", encoding="utf-8")
    (release_repository / "de" / "obsolete.html").write_text("obsolete\n", encoding="utf-8")
    (release_repository / "feedback" / "index.html").write_text("local feedback\n", encoding="utf-8")
    review = release_repository / "drawing-review"
    review.mkdir()
    (review / "index.html").write_text("drawing review\n", encoding="utf-8")
    build_root = tmp_path / "build"
    create_build_tree(build_root)
    monkeypatch.setattr(build, "REVIEW_BUILD_ROOT", tmp_path / "review-build")

    build.promote_release(build_root, release_repository, "beta-test-1")

    assert (release_repository / "de" / "index.html").read_text(encoding="utf-8") == "new de\n"
    assert not (release_repository / "de" / "obsolete.html").exists()
    assert (release_repository / "feedback" / "index.html").read_text(encoding="utf-8") == "local feedback\n"
    assert (review / "index.html").read_text(encoding="utf-8") == "drawing review\n"


def test_promotion_rejects_existing_release_tag(tmp_path: Path) -> None:
    release_repository = tmp_path / "release"
    initialize_release_repository(release_repository)
    git(release_repository, "tag", "beta-test-1")
    build_root = tmp_path / "build"
    create_build_tree(build_root)

    with pytest.raises(RuntimeError, match="Release tag already exists"):
        build.promote_release(build_root, release_repository, "beta-test-1")
