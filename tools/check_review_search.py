#!/usr/bin/env python3
"""Check generated search assets before publishing a site under a URL prefix."""
import json
from pathlib import Path
import re
import sys


def check(build_dir):
    root = Path(build_dir)
    html = (root / "suche.html").read_text(encoding="utf-8")
    targets = re.findall(r"fetch\(\s*['\"]([^'\"]+)['\"]", html)
    for name in ("question_index.json", "index.json"):
        expected = "assets/" + name
        matching = [target for target in targets if target.split("/")[-1] == name]
        if matching != [expected]:
            raise ValueError(f"{name}: expected one relative fetch {expected!r}, got {matching!r}")
        payload = json.loads((root / expected).read_text(encoding="utf-8"))
        expected_type = dict if name == "question_index.json" else list
        if not isinstance(payload, expected_type) or not payload:
            raise ValueError(f"{expected}: expected a nonempty {expected_type.__name__}")
        print(f"OK {expected}: {len(payload)} entries")
    print("Search is ready for deployment under a URL prefix.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python tools/check_review_search.py BUILD_DIRECTORY")
    try:
        check(sys.argv[1])
    except (OSError, ValueError) as error:
        sys.exit(f"Search validation failed: {error}")
