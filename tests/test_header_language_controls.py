import json
from pathlib import Path

import pytest
from jinja2 import Environment, FileSystemLoader


ROOT = Path(__file__).resolve().parents[1] / "generator_extra_content"


@pytest.mark.parametrize("language", ["de", "fr", "it"])
@pytest.mark.parametrize("beta", [False, True])
def test_header_language_controls(language, beta):
    labels = json.loads((ROOT / language / "labels.json").read_text(encoding="utf-8"))
    env = Environment(loader=FileSystemLoader(ROOT / "de" / "templates"))
    controls = env.get_template("html/header-language-controls.html").make_module(dict(
        lang=language, beta=beta, release_id="test-release",
        feedback_url="/feedback/", ui=lambda key: labels[key],
    ))
    html = str(controls.beta_control()) + str(controls.language_controls())
    for target in ("de", "fr", "it"):
        assert f'data-site-language="{target}"' in html
    assert f'lang="{language}" aria-current="true"' in html
    assert html.count('aria-current="true"') == 1
    assert ('<strong>BETA</strong>' in html) is beta
    if beta:
        assert labels["beta_disclaimer"] in html
