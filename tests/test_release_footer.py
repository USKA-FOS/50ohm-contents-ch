import json
from pathlib import Path

import pytest
from jinja2 import Environment, FileSystemLoader


ROOT = Path(__file__).resolve().parents[1] / "generator_extra_content"


@pytest.mark.parametrize("language", ["de", "fr", "it"])
@pytest.mark.parametrize("feedback_url", [None, "https://example.test/feedback/"])
def test_release_footer_preserves_localized_release_and_feedback(language, feedback_url):
    labels = json.loads((ROOT / language / "labels.json").read_text(encoding="utf-8"))
    env = Environment(loader=FileSystemLoader(ROOT / "de" / "templates"))
    html = env.get_template("html/release-footer.html").render(
        release_id="beta-test", lang=language, feedback_url=feedback_url,
        ui=lambda key: labels[key],
    )
    assert 'class="site-footer-release small"' in html
    assert f'{labels["release_label"]}: <strong>beta-test</strong>' in html
    assert 'border-top' not in html
    assert ('data-feedback-link' in html.split("<script>")[0]) is bool(feedback_url)
    if feedback_url:
        assert labels["feedback_button"] in html
        assert f'data-feedback-base="{feedback_url}"' in html
    assert "searchParams.set('release_id', 'beta-test')" in html
