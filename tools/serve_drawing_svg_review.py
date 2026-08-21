#!/usr/bin/env python
"""Serve a local trilingual drawing SVG review interface."""

from __future__ import annotations

import argparse
import json
import mimetypes
import re
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REVIEW_DIR = REPO_ROOT / "work" / "drawing_svg_review"
STATIC_DIR = Path(__file__).resolve().parent / "drawing_svg_review"
LANGUAGES = ("de", "fr", "it")
DRAWING_FILE_PATTERN = re.compile(r"^([A-Za-z0-9_-]+)\.(de|fr|it)\.svg$")


def drawing_sort_key(stem: str) -> tuple[int, int | str, str]:
    if stem.isdigit():
        return (0, int(stem), stem)
    return (1, stem.casefold(), stem)


def discover_drawings(review_dir: Path) -> list[str]:
    """Return drawing stems present in every language review directory."""
    language_stems: list[set[str]] = []
    for language in LANGUAGES:
        language_dir = review_dir / language
        if not language_dir.is_dir():
            raise FileNotFoundError(f"Missing drawing review directory: {language_dir}")
        suffix = f".{language}.svg"
        stems = {
            path.name[: -len(suffix)]
            for path in language_dir.glob(f"*{suffix}")
            if path.is_file()
        }
        language_stems.append(stems)

    common_stems = set.intersection(*language_stems)
    return sorted(common_stems, key=drawing_sort_key)


def create_handler(review_dir: Path, static_dir: Path = STATIC_DIR) -> type[BaseHTTPRequestHandler]:
    resolved_review_dir = review_dir.resolve()
    resolved_static_dir = static_dir.resolve()

    class DrawingReviewHandler(BaseHTTPRequestHandler):
        server_version = "DrawingReview/1.0"

        def do_GET(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler API
            parsed = urlparse(self.path)
            path = unquote(parsed.path)

            if path in ("/", "/index.html"):
                self._serve_file(resolved_static_dir / "index.html", "text/html; charset=utf-8")
                return
            if path == "/assets/review.css":
                self._serve_file(resolved_static_dir / "review.css", "text/css; charset=utf-8")
                return
            if path == "/assets/review.js":
                self._serve_file(
                    resolved_static_dir / "review.js",
                    "text/javascript; charset=utf-8",
                )
                return
            if path == "/api/drawings":
                self._serve_manifest()
                return
            if path.startswith("/drawing/"):
                self._serve_drawing(path)
                return

            self._send_error(HTTPStatus.NOT_FOUND, "Resource not found.")

        def _serve_manifest(self) -> None:
            try:
                drawings = discover_drawings(resolved_review_dir)
            except FileNotFoundError as exc:
                self._send_error(HTTPStatus.INTERNAL_SERVER_ERROR, str(exc))
                return
            payload = json.dumps(
                {"drawings": drawings, "languages": list(LANGUAGES)},
                ensure_ascii=True,
            ).encode("utf-8")
            self._send_bytes(payload, "application/json; charset=utf-8")

        def _serve_drawing(self, request_path: str) -> None:
            parts = request_path.removeprefix("/drawing/").split("/")
            if len(parts) != 2:
                self._send_error(HTTPStatus.NOT_FOUND, "Drawing not found.")
                return
            language, filename = parts
            match = DRAWING_FILE_PATTERN.fullmatch(filename)
            if language not in LANGUAGES or match is None or match.group(2) != language:
                self._send_error(HTTPStatus.NOT_FOUND, "Drawing not found.")
                return

            language_dir = (resolved_review_dir / language).resolve()
            drawing_path = (language_dir / filename).resolve()
            if drawing_path.parent != language_dir or not drawing_path.is_file():
                self._send_error(HTTPStatus.NOT_FOUND, "Drawing not found.")
                return
            self._serve_file(drawing_path, "image/svg+xml")

        def _serve_file(self, path: Path, content_type: str | None = None) -> None:
            if not path.is_file():
                self._send_error(HTTPStatus.NOT_FOUND, "Resource not found.")
                return
            resolved_type = content_type or mimetypes.guess_type(path.name)[0]
            self._send_bytes(path.read_bytes(), resolved_type or "application/octet-stream")

        def _send_bytes(self, payload: bytes, content_type: str) -> None:
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(payload)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(payload)

        def _send_error(self, status: HTTPStatus, message: str) -> None:
            payload = json.dumps({"error": message}, ensure_ascii=True).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(payload)

        def log_message(self, format_string: str, *args: object) -> None:
            print(f"[drawing_review] {self.address_string()} {format_string % args}")

    return DrawingReviewHandler


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Serve the German, French, and Italian drawing SVG review exports."
    )
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--review-dir", type=Path, default=DEFAULT_REVIEW_DIR)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    review_dir = args.review_dir.resolve()
    drawings = discover_drawings(review_dir)
    if not drawings:
        raise SystemExit(f"No drawing is present in all three language directories: {review_dir}")
    if not STATIC_DIR.is_dir():
        raise SystemExit(f"Missing review interface files: {STATIC_DIR}")

    server = ThreadingHTTPServer((args.host, args.port), create_handler(review_dir))
    host, port = server.server_address[:2]
    print(f"[drawing_review] drawings={len(drawings)} review_dir={review_dir}")
    print(f"[drawing_review] url=http://{host}:{port}/")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[drawing_review] stopped")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
