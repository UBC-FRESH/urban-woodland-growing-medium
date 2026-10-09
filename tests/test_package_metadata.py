"""Package metadata consistency checks."""

import tomllib
from pathlib import Path

import woodland_spec

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_version_matches_pyproject() -> None:
    pyproject = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text())
    assert woodland_spec.__version__ == pyproject["project"]["version"]


def test_public_api_exports() -> None:
    assert callable(woodland_spec.build_document)
    assert callable(woodland_spec.build_updated_document)
