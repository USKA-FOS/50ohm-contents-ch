from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from tools.extract_drawing_tex_translation_candidates import load_source_import_drawing_refs
from tools.import_incremental_german_source import FAMILIES, run_import, stable_id
from tools.run_multilingual_canonical_build import overlay_object_texts


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_text(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(payload, encoding="utf-8")


def make_source(root: Path) -> None:
    for family in FAMILIES:
        (root / "contents" / family.source_directory).mkdir(parents=True, exist_ok=True)
    (root / "toc").mkdir(parents=True, exist_ok=True)


def make_text_object(
    canonical: Path,
    *,
    family: str,
    object_id: str,
    object_type: str,
    source_directory: str,
    source_key: str,
    suffix: str,
    slot_key: str,
    slot_type: str,
    de: str,
    fr: str | None = None,
) -> Path:
    object_dir = canonical / family / object_id
    write_text(object_dir / f"body.de{suffix}", de)
    files = {"de": f"body.de{suffix}"}
    languages = ["de"]
    states = [{"language": "de", "state": "imported_approved"}]
    if fr is not None:
        write_text(object_dir / f"body.fr{suffix}", fr)
        files["fr"] = f"body.fr{suffix}"
        languages.append("fr")
        states.append({"language": "fr", "state": "approved"})
    write_json(object_dir / "object.references.json", [])
    write_json(object_dir / "object.annotations.json", [])
    write_json(
        object_dir / "object.meta.json",
        {
            "id": object_id,
            "object_type": object_type,
            "active": True,
            "source": {"path": f"contents/{source_directory}/{source_key}{suffix}", "format": suffix[1:], "key": source_key},
            "identifiers": [{"id_system": "file_stem", "id_value": source_key, "preferred": True}],
            "languages": languages,
            "review_states": states,
            "metadata": {},
            "asset_files": {},
            "text_slots": [{"slot_key": slot_key, "slot_type": slot_type, "sort_order": 0, "translation_group_key": None, "storage": {"kind": "text_file", "files": files}}],
            "reconstruction": {"strategy": "replace_source_file", "targets": [{"path": f"contents/{source_directory}/{source_key}{suffix}", "kind": "localized_text_file"}]},
        },
    )
    return object_dir


def make_drawing(canonical: Path) -> Path:
    object_id = stable_id("dr", "drawing", "100")
    object_dir = canonical / "drawings" / object_id
    write_text(object_dir / "100.de.tex", "Alt")
    write_text(object_dir / "100.de.svg", "<svg>alt</svg>")
    write_text(object_dir / "100.fr.tex", "Ancien")
    write_text(object_dir / "100.fr.svg", "<svg>ancien</svg>")
    write_json(object_dir / "object.references.json", [])
    write_json(object_dir / "object.annotations.json", [])
    write_json(
        object_dir / "object.meta.json",
        {
            "id": object_id,
            "object_type": "drawing",
            "active": True,
            "source": {"path": "contents/drawings/100", "format": "grouped_asset", "key": "100"},
            "identifiers": [{"id_system": "drawing_id", "id_value": "100", "preferred": True}],
            "languages": ["de", "fr"],
            "review_states": [{"language": "de", "state": "imported_approved"}, {"language": "fr", "state": "approved"}],
            "metadata": {"asset": {"svg_path": "contents/drawings/100.svg", "tex_path": "contents/drawings/100.tex"}, "language_asset": {"de.svg": {"source_path": "contents/drawings/100.svg", "canonical_file": "100.de.svg"}, "de.tex": {"source_path": "contents/drawings/100.tex", "canonical_file": "100.de.tex"}}},
            "asset_files": {},
            "text_slots": [],
            "language_variants": {"de": {"asset_files": {"svg": "100.de.svg", "tex": "100.de.tex"}}, "fr": {"asset_files": {"svg": "100.fr.svg", "tex": "100.fr.tex"}}},
            "reconstruction": {"strategy": "render_drawing_assets_and_description", "targets": []},
        },
    )
    return object_dir


def initialize_families(canonical: Path) -> None:
    for family in FAMILIES:
        (canonical / family.canonical_directory).mkdir(parents=True, exist_ok=True)
    (canonical / "structure" / "editions").mkdir(parents=True, exist_ok=True)


def test_incremental_import_handles_add_change_delete_html_and_drawing(tmp_path: Path) -> None:
    canonical = tmp_path / "canonical"
    source = tmp_path / "source"
    initialize_families(canonical)
    make_source(source)

    changed_id = stable_id("sc", "section_article", "changed")
    changed = make_text_object(
        canonical,
        family="sections",
        object_id=changed_id,
        object_type="section_article",
        source_directory="sections",
        source_key="changed",
        suffix=".md",
        slot_key="body_markdown",
        slot_type="markdown",
        de="Alt [photo:1:x:y]",
        fr="Ancienne traduction",
    )
    deleted_id = stable_id("sc", "section_article", "deleted")
    deleted = make_text_object(
        canonical,
        family="sections",
        object_id=deleted_id,
        object_type="section_article",
        source_directory="sections",
        source_key="deleted",
        suffix=".md",
        slot_key="body_markdown",
        slot_type="markdown",
        de="Wird entfernt",
        fr="Sera supprimé",
    )
    html_id = stable_id("in", "html_include", "widget")
    html = make_text_object(
        canonical,
        family="html_includes",
        object_id=html_id,
        object_type="html_include",
        source_directory="html",
        source_key="widget",
        suffix=".html",
        slot_key="body_html",
        slot_type="html",
        de="<div><p>Hallo</p><p>Welt</p></div>",
        fr="<div><p>Bonjour</p><p>Monde</p></div>",
    )
    drawing = make_drawing(canonical)

    write_text(source / "contents/sections/changed.md", "Neu [picture:2:x:y]")
    write_text(source / "contents/sections/added.md", "Neue Seite")
    write_text(source / "contents/html/widget.html", "<div><h1>Titel</h1><p>Hallo</p><p>Erde</p></div>")
    write_text(source / "contents/drawings/100.tex", "Alt")
    write_text(source / "contents/drawings/100.svg", "<svg>neu</svg>")
    write_text(source / "contents/drawings/200.tex", "Neue Zeichnung")
    write_text(source / "contents/drawings/200.svg", "<svg>neu 200</svg>")

    dry_report = tmp_path / "dry.json"
    dry = run_import(source, canonical_root=canonical, report_path=dry_report)
    assert dry["applied"] is False
    assert (changed / "body.de.md").read_text(encoding="utf-8") == "Alt [photo:1:x:y]"
    assert set(dry["translation_object_ids"]) == {
        changed_id,
        html_id,
        stable_id("sc", "section_article", "added"),
        stable_id("dr", "drawing", "200"),
    }

    applied_report = tmp_path / "applied.json"
    report = run_import(source, canonical_root=canonical, apply=True, report_path=applied_report)
    assert report["applied"] is True
    assert (changed / "body.de.md").read_text(encoding="utf-8") == "Neu [picture:2:x:y]"
    assert (changed / "body.fr.md").read_text(encoding="utf-8") == "Ancienne traduction"
    changed_meta = json.loads((changed / "object.meta.json").read_text(encoding="utf-8"))
    assert any(state == {"language": "fr", "state": "to_be_reviewed"} for state in changed_meta["review_states"])
    references = json.loads((changed / "object.references.json").read_text(encoding="utf-8"))
    assert references[0]["target_id_value"] == "2"

    deleted_meta = json.loads((deleted / "object.meta.json").read_text(encoding="utf-8"))
    assert deleted_meta["active"] is False
    assert deleted_meta["metadata"]["lifecycle"]["status"] == "to_be_deleted"
    assert (deleted / "body.fr.md").read_text(encoding="utf-8") == "Sera supprimé"

    assert (html / "body.fr.html").read_text(encoding="utf-8") == "<div><h1>Titel</h1><p>Bonjour</p><p>Erde</p></div>"
    assert (drawing / "100.fr.tex").read_text(encoding="utf-8") == "Ancien"
    assert (drawing / "100.fr.svg").read_text(encoding="utf-8") == "<svg>ancien</svg>"
    assert (drawing / "100.de.tex").read_text(encoding="utf-8") == "Alt"
    drawing_meta = json.loads((drawing / "object.meta.json").read_text(encoding="utf-8"))
    assert any(state == {"language": "fr", "state": "to_be_reviewed"} for state in drawing_meta["review_states"])
    assert drawing_meta["language_variants"]["fr"]["review_state"] == "to_be_reviewed"
    drawing_change = next(change for change in report["changes"] if change["object_id"] == stable_id("dr", "drawing", "100"))
    assert drawing_change["translation_required"] is False
    assert drawing_change["media_review_required"] is True
    assert (canonical / "drawings" / stable_id("dr", "drawing", "200") / "200.de.tex").is_file()


def test_exact_content_rename_preserves_object_id_and_translation(tmp_path: Path) -> None:
    canonical = tmp_path / "canonical"
    source = tmp_path / "source"
    initialize_families(canonical)
    make_source(source)
    object_id = stable_id("sc", "section_article", "old_name")
    object_dir = make_text_object(
        canonical,
        family="sections",
        object_id=object_id,
        object_type="section_article",
        source_directory="sections",
        source_key="old_name",
        suffix=".md",
        slot_key="body_markdown",
        slot_type="markdown",
        de="Gleicher Inhalt",
        fr="Même contenu",
    )
    write_text(source / "contents/sections/new_name.md", "Gleicher Inhalt")

    report = run_import(source, canonical_root=canonical, apply=True, report_path=tmp_path / "audit.json")
    rename = next(change for change in report["changes"] if change["action"] == "renamed")
    assert rename["object_id"] == object_id
    assert rename["translation_required"] is False
    meta = json.loads((object_dir / "object.meta.json").read_text(encoding="utf-8"))
    assert meta["source"]["key"] == "new_name"
    assert (object_dir / "body.fr.md").read_text(encoding="utf-8") == "Même contenu"


def test_structure_update_preserves_ids_and_only_invalidates_changed_text(tmp_path: Path) -> None:
    canonical = tmp_path / "canonical"
    source = tmp_path / "source"
    initialize_families(canonical)
    make_source(source)
    initial_toc = {
        "title": "Kurs",
        "chapters": [
            {
                "title": "Kapitel",
                "ident": "chapter",
                "sections": [{"title": "Alt", "ident": "section", "status": "prod"}],
            }
        ],
    }
    write_json(source / "toc/HB.json", initial_toc)
    initial_report = run_import(source, canonical_root=canonical, apply=True, report_path=tmp_path / "initial.json")

    edition_dir = canonical / "structure" / "editions" / "HB"
    old_de = json.loads((edition_dir / "edition.de.json").read_text(encoding="utf-8"))
    old_section = old_de["chapters"][0]["sections"][0]
    assert set(initial_report["translation_node_ids"]) == {
        old_de["id"],
        old_de["chapters"][0]["id"],
        old_section["id"],
    }
    assert (edition_dir / "edition.fr.json").is_file()
    assert (edition_dir / "edition.it.json").is_file()
    fr = json.loads(json.dumps(old_de))
    fr["title"] = "Cours"
    fr["chapters"][0]["title"] = "Chapitre"
    fr["chapters"][0]["sections"][0]["title"] = "Ancien"
    write_json(edition_dir / "edition.fr.json", fr)

    changed_toc = json.loads(json.dumps(initial_toc))
    changed_toc["chapters"][0]["sections"][0]["title"] = "Neu"
    write_json(source / "toc/HB.json", changed_toc)
    report = run_import(source, canonical_root=canonical, apply=True, report_path=tmp_path / "changed.json")

    new_de = json.loads((edition_dir / "edition.de.json").read_text(encoding="utf-8"))
    new_fr = json.loads((edition_dir / "edition.fr.json").read_text(encoding="utf-8"))
    new_section = new_de["chapters"][0]["sections"][0]
    assert new_section["id"] == old_section["id"]
    assert new_fr["title"] == "Cours"
    assert new_fr["chapters"][0]["title"] == "Chapitre"
    assert new_fr["chapters"][0]["sections"][0]["title"] == "Neu"
    assert report["translation_node_ids"] == [new_section["id"]]


def test_drawing_scope_requires_an_applied_source_import_audit(tmp_path: Path) -> None:
    audit = tmp_path / "audit.json"
    write_json(
        audit,
        {
            "workflow": "incremental_german_source_import",
            "applied": True,
            "changes": [
                {"object_id": "dr_0123456789ab", "object_type": "drawing", "action": "changed", "translation_required": True},
                {"object_id": "dr_111111111111", "object_type": "drawing", "action": "changed", "translation_required": False},
                {"object_id": "sc_222222222222", "object_type": "section_article", "action": "changed", "translation_required": True},
            ],
        },
    )
    assert load_source_import_drawing_refs(audit) == {"canonical/drawings/dr_0123456789ab"}

    payload = json.loads(audit.read_text(encoding="utf-8"))
    payload["applied"] = False
    write_json(audit, payload)
    try:
        load_source_import_drawing_refs(audit)
    except ValueError as exc:
        assert "was not applied" in str(exc)
    else:
        raise AssertionError("A dry-run audit must not select drawings for translation")


def test_build_staging_excludes_inactive_objects(tmp_path: Path) -> None:
    connection = sqlite3.connect(":memory:")
    connection.row_factory = sqlite3.Row
    connection.executescript(
        """
        CREATE TABLE content_object (
            id TEXT PRIMARY KEY, object_type TEXT, source_path TEXT,
            source_key TEXT, active INTEGER
        );
        CREATE TABLE text_slot (
            id TEXT PRIMARY KEY, object_id TEXT, slot_key TEXT, sort_order INTEGER
        );
        CREATE TABLE localized_text (
            text_slot_id TEXT, language TEXT, text_value TEXT
        );
        CREATE TABLE object_metadata (
            object_id TEXT, metadata_scope TEXT, metadata_key TEXT, value_json TEXT
        );
        """
    )
    for object_id, active in (("active", 1), ("deleted", 0)):
        connection.execute(
            "INSERT INTO content_object VALUES (?, 'section_article', ?, ?, ?)",
            (object_id, f"contents/sections/{object_id}.md", object_id, active),
        )
        connection.execute("INSERT INTO text_slot VALUES (?, ?, 'body_markdown', 0)", (f"slot-{object_id}", object_id))
        connection.execute("INSERT INTO localized_text VALUES (?, 'de', ?)", (f"slot-{object_id}", object_id))

    report = overlay_object_texts(connection, tmp_path / "staged", "de")
    assert report["written_files"] == 1
    assert (tmp_path / "staged/contents/sections/active.md").is_file()
    assert not (tmp_path / "staged/contents/sections/deleted.md").exists()
