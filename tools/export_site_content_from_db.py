from __future__ import annotations

import json
import shutil
import sqlite3
from hashlib import sha256
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
WORK_ROOT = REPO_ROOT / "work"
DB_PATH = WORK_ROOT / "global_model" / "content_model.sqlite"
TARGET_ROOT = WORK_ROOT / "site-content"
REPORT_PATH = WORK_ROOT / "global_model" / "site_content_comparison.json"


def export_site_content() -> dict[str, object]:
    if TARGET_ROOT.exists():
        shutil.rmtree(TARGET_ROOT)
    TARGET_ROOT.mkdir(parents=True)

    connection = sqlite3.connect(DB_PATH)
    rows = connection.execute(
        "SELECT source_path, checksum_sha256, payload FROM source_artifact ORDER BY source_path"
    ).fetchall()

    mismatches: list[dict[str, str]] = []
    for source_path, expected_checksum, payload in rows:
        target_path = TARGET_ROOT / source_path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_bytes(payload)

        actual_checksum = sha256(target_path.read_bytes()).hexdigest()
        source_checksum = sha256((REPO_ROOT / source_path).read_bytes()).hexdigest()
        if actual_checksum != expected_checksum or source_checksum != expected_checksum:
            mismatches.append(
                {
                    "source_path": source_path,
                    "database_checksum": expected_checksum,
                    "source_checksum": source_checksum,
                    "export_checksum": actual_checksum,
                }
            )

    connection.close()
    report: dict[str, object] = {
        "database": str(DB_PATH),
        "export_root": str(TARGET_ROOT),
        "artifact_count": len(rows),
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
    }
    REPORT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return report


def main() -> None:
    report = export_site_content()
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
