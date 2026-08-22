from __future__ import annotations

import importlib.util
import os
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def load_tool(name: str):
    path = REPO_ROOT / "tools" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


extractor = load_tool("extract_drawing_tex_translation_candidates")
importer = load_tool("import_drawing_tex_translations")
renderer = load_tool("render_localized_drawing_svgs")


class DrawingCandidateExtractionTest(unittest.TestCase):
    def test_extracts_pgfplots_text_options(self):
        source = r"title={Eingangssignal}, xlabel={\textbf{Frequenz [MHz]}}, ylabel={$t$}"
        self.assertEqual(
            extractor.extract_pgfplots_option_candidates(source),
            [
                ("pgfplots_title", "Eingangssignal"),
                ("pgfplots_xlabel", r"\textbf{Frequenz [MHz]}"),
            ],
        )

    def test_extracts_bare_circuitikz_labels(self):
        source = r"to [amp, l_=HF] ++(1,0) to [amp, l_=1.ZF] ++(1,0)"
        self.assertEqual(
            extractor.extract_circuitikz_label_candidates(source),
            [
                ("circuitikz_bare_label", "HF"),
                ("circuitikz_bare_label", "1.ZF"),
            ],
        )

    def test_extracts_visible_text_without_textcolor_name(self):
        candidate = extractor.build_structured_candidate(
            "canonical/drawings/dr_test",
            "1",
            1,
            r"\textcolor{DARCblue}{phys. Stromrichtung!}",
            "node_text",
        )
        self.assertEqual(candidate.translatable_text, "phys. Stromrichtung!")

    def test_extracts_text_inside_math(self):
        self.assertEqual(
            extractor.extract_math_text_candidates(r"$f_\text{ZF}$"),
            [("math_text", "ZF")],
        )


class DrawingTranslationImportTest(unittest.TestCase):
    def test_expands_explicit_line_break_marker(self):
        self.assertEqual(
            importer.normalize_translation_text(r"\shortstack{ligne 1[[BR]]ligne 2}"),
            r"\shortstack{ligne 1\\ligne 2}",
        )

    def test_single_word_translation_removes_obsolete_source_line_break(self):
        source = r"{Spannungs-\\messgerät}"
        segments = importer.translation_segments_for_regular(source, "voltmètre")
        self.assertEqual(importer.replace_fragment_text(source, segments), "{voltmètre}")

    def test_preserves_nested_declaration_formatting(self):
        source = r"{\textbf{\large Frequenz [MHz]}}"
        self.assertEqual(
            importer.replace_fragment_text(source, ["Fréquence [MHz]"]),
            r"{\textbf{\large Fréquence [MHz]}}",
        )

    def test_preserves_nested_formatting_and_explicit_protected_token(self):
        token = r"$\mathbf{\mathrm{a}_0}$"
        source = rf"{{\textbf{{\large Grunddämpfung {token} je 100\,m Leitungslänge in dB}}}}"
        translated = rf"Atténuation de base {token} par 100\,m de longueur de câble en dB"
        self.assertEqual(
            importer.replace_fragment_text(source, [translated], [[token]]),
            rf"{{\textbf{{\large {translated}}}}}",
        )

    def test_replaces_only_matching_pgfplots_option(self):
        source = "title={Eingangssignal}, label={Eingangssignal}"
        updated, replaced = importer.replace_braced_option(
            source, "title", "{Eingangssignal}", "{signal d'entrée}"
        )
        self.assertTrue(replaced)
        self.assertEqual(updated, "title={signal d'entrée}, label={Eingangssignal}")

    def test_replaces_bare_circuitikz_label(self):
        updated, replaced = importer.replace_circuitikz_bare_label(
            "to [amp, l_=1.ZF, name=x]", "1.ZF", "1.FI"
        )
        self.assertEqual(replaced, 1)
        self.assertEqual(updated, "to [amp, l_=1.FI, name=x]")

    def test_replaces_math_text_without_changing_math(self):
        updated, replaced = importer.replace_math_text(r"$f_\text{ZF}$", "ZF", "FI")
        self.assertTrue(replaced)
        self.assertEqual(updated, r"$f_\text{FI}$")


class DrawingRendererTest(unittest.TestCase):
    def test_uses_german_svg_width(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            tex_path = root / "471.fr.tex"
            tex_path.write_text("", encoding="utf-8")
            (root / "471.de.svg").write_text(
                '<svg width="707.636pt" height="211.2pt"></svg>', encoding="utf-8"
            )
            width = renderer.source_width_cm(tex_path, "471", None)
            self.assertAlmostEqual(width, 24.87, places=2)

    def test_accepts_unitless_german_svg_width_from_pdftocairo(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            tex_path = root / "689.fr.tex"
            tex_path.write_text("", encoding="utf-8")
            (root / "689.de.svg").write_text(
                '<svg width="260.588" height="260.588"></svg>', encoding="utf-8"
            )
            width = renderer.source_width_cm(tex_path, "689", None)
            self.assertAlmostEqual(width, 9.16, places=2)

    def test_rerenders_existing_svg_when_german_width_differs(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            tex_path = root / "471.fr.tex"
            svg_path = root / "471.fr.svg"
            tex_path.write_text("", encoding="utf-8")
            svg_path.write_text('<svg width="299pt"></svg>', encoding="utf-8")
            (root / "471.de.svg").write_text(
                '<svg width="707.636pt"></svg>', encoding="utf-8"
            )
            self.assertTrue(
                renderer.should_rerender(
                    tex_path=tex_path,
                    svg_path=svg_path,
                    skip_existing=True,
                )
            )

    def test_rerenders_when_included_photo_is_newer(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            tex_path = root / "689.fr.tex"
            svg_path = root / "689.fr.svg"
            photo_path = root / "205.de.png"
            tex_path.write_text(r"\includegraphics{foto/205}", encoding="utf-8")
            svg_path.write_text('<svg width="260pt"></svg>', encoding="utf-8")
            (root / "689.de.svg").write_text(
                '<svg width="260pt"></svg>', encoding="utf-8"
            )
            photo_path.write_bytes(b"new photo")
            svg_path.touch()
            svg_mtime = svg_path.stat().st_mtime
            os.utime(photo_path, (svg_mtime + 1, svg_mtime + 1))
            with patch.object(renderer, "build_photo_asset_map", return_value={"205": photo_path}):
                self.assertTrue(
                    renderer.should_rerender(
                        tex_path=tex_path,
                        svg_path=svg_path,
                        skip_existing=True,
                    )
                )


if __name__ == "__main__":
    unittest.main()
