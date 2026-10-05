"""Safety checks for the opt-in generated-work purge."""

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "purge_generated_work.py"
spec = importlib.util.spec_from_file_location("purge_generated_work", SCRIPT)
assert spec and spec.loader
purger = importlib.util.module_from_spec(spec)
spec.loader.exec_module(purger)


class PurgeGeneratedWorkTest(unittest.TestCase):
    def test_preview_preserves_and_apply_removes_only_selected_cache(self):
        with tempfile.TemporaryDirectory() as temporary:
            repo = Path(temporary)
            subprocess.run(["git", "init", "-q", str(repo)], check=True)
            cache = repo / "work" / "canonical_model"
            cache.mkdir(parents=True)
            (cache / "content_model.sqlite").write_bytes(b"test")
            review = repo / "work" / "photo_review" / "Review_result.xlsx"
            review.parent.mkdir()
            review.write_bytes(b"human decision")
            with patch.object(purger, "REPO", repo), patch.object(purger, "BUILD_LOCKS", ()):
                self.assertEqual(purger.purge(["canonical-model"]), [])
                self.assertTrue(cache.exists())
                self.assertEqual(purger.purge(["canonical-model"], apply=True), [cache])
            self.assertFalse(cache.exists())
            self.assertEqual(review.read_bytes(), b"human decision")

    def test_refuses_tracked_or_symlinked_directories(self):
        with tempfile.TemporaryDirectory() as temporary:
            repo = Path(temporary)
            subprocess.run(["git", "init", "-q", str(repo)], check=True)
            cache = repo / "work" / "canonical_model"
            cache.mkdir(parents=True)
            (cache / "tracked.txt").write_text("keep")
            subprocess.run(["git", "-C", str(repo), "add", "-f", "work/canonical_model/tracked.txt"], check=True)
            with patch.object(purger, "REPO", repo), patch.object(purger, "BUILD_LOCKS", ()):
                with self.assertRaisesRegex(ValueError, "tracked files"):
                    purger.purge(["canonical-model"], apply=True)
            self.assertTrue((cache / "tracked.txt").exists())
            subprocess.run(["git", "-C", str(repo), "rm", "--cached", "work/canonical_model/tracked.txt"],
                           check=True, capture_output=True)
            cache.rename(repo / "elsewhere")
            cache.symlink_to(repo / "elsewhere", target_is_directory=True)
            with patch.object(purger, "REPO", repo), patch.object(purger, "BUILD_LOCKS", ()):
                with self.assertRaisesRegex(ValueError, "symlinked path"):
                    purger.purge(["canonical-model"], apply=True)
            self.assertTrue((repo / "elsewhere" / "tracked.txt").exists())


if __name__ == "__main__":
    unittest.main()
