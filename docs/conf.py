"""Sphinx configuration for the urban woodland growing medium project."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from woodland_spec import __version__  # noqa: E402

project = "Urban Woodland Growing Medium"
author = "UBC FRESH Lab"
copyright = "2026, UBC FRESH Lab"
version = __version__
release = __version__

extensions = [
    "sphinx_rtd_theme",
]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "sphinx_rtd_theme"
html_title = "Urban Woodland Growing Medium"
