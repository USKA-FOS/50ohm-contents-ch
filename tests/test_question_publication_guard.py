from pathlib import Path

import pytest

from tools import run_multilingual_canonical_build as build


def setup(monkeypatch, tmp_path):
    (tmp_path / "work").mkdir()
    question_root = tmp_path / "questions"
    (question_root / "pool").mkdir(parents=True)
    (question_root / "pool/catalog.meta.json").write_text('{"schema_version":1,"pruned":{}}')
    monkeypatch.setattr(build, "CONTENT_REPO", tmp_path)
    monkeypatch.setattr(build, "QUESTION_POOL_REPO", question_root)
    return question_root


def test_site_build_requires_publication_sync_before_consuming_catalogs(tmp_path, monkeypatch):
    question_root = setup(monkeypatch, tmp_path)
    calls = []
    def verify(root, arguments):
        calls.append((root, arguments))
    monkeypatch.setattr(build, "run_question_pool_tool", verify)
    with build.question_pool_catalogs(None) as catalogs:
        assert catalogs["de"] == question_root / "question_pool_ch-de.json"
        assert catalogs["fr"] == question_root / "builds/fr/question_pool_rev1_ch-fr.json"
    assert len(calls) == 1 and calls[0][0] == question_root
    assert "--check" in calls[0][1]


def test_stale_publications_abort_site_build(tmp_path, monkeypatch):
    setup(monkeypatch, tmp_path)
    def reject(*_args):
        raise RuntimeError("publication mismatch: HB.rationale")
    monkeypatch.setattr(build, "run_question_pool_tool", reject)
    with pytest.raises(RuntimeError, match="HB.rationale"):
        with build.question_pool_catalogs(None):
            pytest.fail("Catalogs must not be consumed after a failed check")
