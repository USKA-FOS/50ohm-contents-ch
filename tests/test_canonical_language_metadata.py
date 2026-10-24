from __future__ import annotations

from copy import deepcopy
import importlib
import json
from pathlib import Path

import pytest

from tools.canonical_language_metadata import sync_languages


def test_inventory_includes_media_only_languages_and_preserves_existing_state():
    meta = {
        "languages": ["es", "de"],
        "text_slots": [{"storage": {"files": {"de": "body.de.md"}}}],
        "language_variants": {"fr": {"asset_files": {"svg": "1.fr.svg"}}},
        "review_states": [{"language": "fr", "state": "to_be_reviewed"}],
    }
    before = deepcopy(meta)
    sync_languages(meta)
    assert meta.pop("languages") == ["de", "fr", "es"]
    before.pop("languages")
    assert meta == before


@pytest.mark.parametrize("tool,function,extra,expected", [
    ("import_drawing_tex_translations", "update_meta_for_tex", (), ["de", "fr", "it"]),
    ("import_drawing_feedback_review", "update_meta", (), ["de", "fr", "it"]),
    ("render_localized_drawing_svgs", "update_meta_for_svg", ("fr",), ["de", "fr"]),
])
def test_media_updaters_keep_language_inventory_complete(tmp_path, tool, function, extra, expected):
    module = importlib.import_module(f"tools.{tool}")
    path = tmp_path / "object.meta.json"
    meta = {
        "languages": [],
        "language_variants": {"de": {"asset_files": {"svg": "1.de.svg", "tex": "1.de.tex"}}},
        "metadata": {"asset": {"svg_path": "contents/drawings/1.svg", "tex_path": "contents/drawings/1.tex"}},
    }
    path.write_text(json.dumps(meta))
    getattr(module, function)(tmp_path, "1", *extra)
    updated = json.loads(path.read_text())
    assert updated["languages"] == expected
    assert updated["language_variants"]["de"] == meta["language_variants"]["de"]


def test_export_declares_media_languages_even_without_description_text(tmp_path, monkeypatch):
    monkeypatch.syspath_prepend(str(Path(__file__).resolve().parents[1] / "tools"))
    exporter = importlib.import_module("tools.export_canonical_model")
    monkeypatch.setattr(exporter, "REPO_ROOT", tmp_path)
    for language in ("de", "fr"):
        (tmp_path / f"1.{language}.svg").write_text("<svg/>")
    metadata = [
        {"metadata_scope": "language_asset", "metadata_key": f"{language}.svg",
         "value_json": json.dumps({"source_path": f"1.{language}.svg", "canonical_file": f"1.{language}.svg"})}
        for language in ("de", "fr")
    ]
    monkeypatch.setattr(exporter, "rows", lambda _conn, sql, _params: metadata if "FROM object_metadata" in sql else [])
    object_dir = tmp_path / "canonical" / "drawings" / "dr_test"
    object_dir.mkdir(parents=True)
    exporter.export_object(None, {"id": "old", "object_type": "drawing", "source_key": "1", "active": 1}, "dr_test", object_dir)
    meta = json.loads((object_dir / "object.meta.json").read_text())
    assert meta["languages"] == ["de", "fr"]
    assert meta["text_slots"] == []
