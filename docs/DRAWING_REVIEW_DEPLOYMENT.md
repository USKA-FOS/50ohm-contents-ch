# Drawing Review Publication

This document describes the current drawing-review publication contract. It
documents the current behavior, not its history.

## Purpose

The review interface compares German, French, and Italian drawing SVGs. It
lists every German drawing and uses the German image as an explicit fallback
when a localized SVG is absent. `Translated only` displays drawings having
explicit SVGs in both French and Italian.

The interface is static. It can be served locally by the development server or
published under `/drawing-review/` without a Python process. It never writes to
canonical data.

## Manifest

`prepare_drawing_svg_review.py` creates a self-contained directory containing:

- `index.html` and `assets/`;
- `de/`, `fr/`, and `it/` SVG directories;
- `manifest.json`.

The manifest records a deterministic `review_id`, an asset digest, the
`50ohm-contents-ch` commit and canonical dirty state, every drawing number and
canonical ID, and per-language SVG availability. Feedback is accepted only
when these identities match the manifest currently deployed on the server.

## Local Review

Local preparation permits uncommitted SVGs so they can be visually checked
before their content commit:

```bash
python tools/prepare_drawing_svg_review.py
python tools/serve_drawing_svg_review.py
```

Open `http://127.0.0.1:8765/`.

## Publication

Public review output must represent a committed canonical state. Commit the
reviewed SVG and metadata changes first, then verify the canonical tree is
clean and publish into the release repository:

```bash
git status --short -- canonical
python tools/prepare_drawing_svg_review.py \
  --review-dir ../50ohm-site-releases/drawing-review \
  --feedback-url https://50ohm.jp2s.ch/feedback/ \
  --require-clean-source
```

The command refuses a dirty canonical source and refuses to overwrite
uncommitted `drawing-review/` files in the destination repository. Review and
commit the resulting release-repository changes before deployment.

## Feedback Contract

The issue button opens the common feedback form with:

- `context=drawing_review`;
- `review_id`;
- `drawing`;
- `canonical_id`;
- the form language.

The browser never receives GitHub credentials. The feedback API validates the
submitted identities against the deployed drawing manifest, stores the report
in SQLite, and creates the private GitHub issue through its existing backend.
