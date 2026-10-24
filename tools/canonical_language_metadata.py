"""Maintain the language inventory of canonical objects, including media.

This inventory records available payload declarations, not translation quality
or human approval. Existing explicit declarations are preserved.
"""
from __future__ import annotations

from typing import Any


def present_languages(meta: dict[str, Any]) -> set[str]:
    languages = {str(language) for language in meta.get("languages", [])}
    for slot in meta.get("text_slots", []):
        languages.update(str(language) for language in ((slot.get("storage") or {}).get("files") or {}))
    languages.update(str(language) for language in (meta.get("language_variants") or {}))
    return languages


def sync_languages(meta: dict[str, Any]) -> None:
    languages = present_languages(meta)
    meta["languages"] = [language for language in ("de", "fr", "it") if language in languages]
    meta["languages"].extend(sorted(languages - {"de", "fr", "it"}))
