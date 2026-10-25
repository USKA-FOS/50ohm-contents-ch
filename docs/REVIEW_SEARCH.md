# Search in the continuous review site

The generator on `main` already builds `assets/question_index.json` and
`assets/index.json`. Search markup belongs to this content repository:
`contents/static/suche.html`.

Its fetch URLs must remain relative: `assets/question_index.json` and
`assets/index.json`. A leading slash would request assets at the domain root
and break deployments under a prefix such as `/review-de/`.

`review-build.yml` runs `tools/check_review_search.py` after generation and
before rsync deployment. It rejects absolute or missing index fetches, missing
or malformed JSON files, empty indexes and incorrect index types. A failed
check stops deployment. It does not change the generator or question source.

After updating or merging the search page, preserve these relative paths.
The normal workflow runs the check automatically; no additional operator step
is required. For a manual check, from the generator working directory:

```bash
python 50ohm-contents-ch/tools/check_review_search.py build
```

This is a read-only artifact check, not a browser interaction test. Test the
published search over HTTP(S), not via `file://`. The nginx URL mapping remains
server configuration and is not established by the deployment directory name.
