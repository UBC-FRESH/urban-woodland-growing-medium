"""Documentation configuration sanity checks."""

import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_docs_conf_importable() -> None:
    conf_path = REPO_ROOT / "docs" / "conf.py"
    spec = importlib.util.spec_from_file_location("docs_conf", conf_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["docs_conf"] = module
    try:
        spec.loader.exec_module(module)
    finally:
        sys.modules.pop("docs_conf", None)
    assert module.project == "Urban Woodland Growing Medium"
    assert module.html_theme == "sphinx_rtd_theme"


def test_docs_index_lists_pages() -> None:
    index = (REPO_ROOT / "docs" / "index.rst").read_text()
    for page in ["specification", "design-basis", "development-workflow", "roadmap"]:
        assert page in index, page
