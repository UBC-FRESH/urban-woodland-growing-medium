"""Content guards for the Markdown specification source of truth.

These tests replace the old builder-content tests: the specification is now
edited directly as Markdown, so the guards check the source itself for the
required properties, key authored defaults, structural integrity, and the
sentence-per-line convention that keeps diffs reviewable.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "specification" / "cwh-urban-woodland-growing-medium.md"

REQUIRED_PHRASES = [
    # Identity and status
    "CWH Woodland Growing Medium Specification",
    "Section 32 91 13",
    "authored project requirements, not published CWH regulatory limits",
    # Profile and authored defaults
    "300 mm Layer A over 600 mm Layer B",
    "30 m³",
    "5.0–8.0%",
    "1.0–3.0%",
    "5.0–6.5",
    "≤2.0 dS/m",
    "≤4",
    # Table 1A requested properties (13 rows)
    "C:N Carbon to nitrogen",
    "Organic matter % of total dry weight",
    "Sand % of total dry weight",
    "Silt % of total dry weight",
    "Clay % of total dry weight",
    "Total silt and clay",
    "Acidity pH",
    "Maximum particle size",
    "Nitrogen N",
    "Phosphorus P ppm",
    "Potassium K ppm",
    "EC saturated extract at 25°C",
    "SAR saturated extract",
    # Unverified supplied figures, preserved with their caveat
    "phosphorus 324 ppm and potassium 1,956 ppm",
    "not acceptance targets, minimums, maximums or fertilizer instructions",
    # Structure
    "Part 6 Protection completion and measurement",
    "Appendix A Technical basis and references",
    "The Vancouver GRI planting guidelines were not used.",
    # Deployment contexts and BEC13 anchoring
    "UW-M sheltered mesic",
    "UW-D slightly dry",
    "UW-X very dry",
    "Default adjustments by deployment context",
    "CWHdm3",
    "CWHdm1",
    "CWHxs",
    "CDFmm",
    "subxeric",
    "BEC13",
    "CCISS",
    "edatopic",
    "40 m³ where depth is less than 900 mm",
    "8.0–12.0%",
    "Eastern Variant",
    "FdcHw–Red huckleberry–Salal",
    "PlcFdc–Rock mosses–Clad lichens",
    "Land Management Handbook 77",
]

EXPECTED_H2 = [
    "## Deployment contexts",
    "## Part 1 General requirements",
    "## Part 2 Materials",
    "## Table 1 Growing medium laboratory acceptance",
    "## Table 1A Requested properties summary",
    "## Part 3 Verification protocols and site preparation",
    "## Part 4 Installation",
    "## Part 5 Installed quality assurance and acceptance",
    "## Part 6 Protection completion and measurement",
    "## Appendix A Technical basis and references",
]

# Abbreviations that legitimately contain a period followed by a capital.
ABBREVIATIONS = ["B.C.", "e.g.", "i.e.", "U.S."]


def test_source_exists():
    assert SPEC.is_file(), f"missing specification source {SPEC}"


def test_required_phrases_present():
    text = SPEC.read_text(encoding="utf-8")
    missing = [phrase for phrase in REQUIRED_PHRASES if phrase not in text]
    assert not missing, f"missing required phrases: {missing}"


def test_heading_structure():
    lines = SPEC.read_text(encoding="utf-8").splitlines()
    h1 = [line for line in lines if line.startswith("# ") and not line.startswith("## ")]
    assert h1 == ["# CWH Woodland Growing Medium Specification"]
    for heading in EXPECTED_H2:
        assert heading in lines, f"missing heading {heading!r}"


def test_table_row_counts():
    lines = SPEC.read_text(encoding="utf-8").splitlines()
    tables, current = [], []
    for line in lines:
        if line.startswith("|"):
            current.append(line)
        elif current:
            tables.append(current)
            current = []
    if current:
        tables.append(current)
    # Schedule, deployment-context adjustments, Table 1, Table 1A, hold
    # points, field checks (line counts include header and separator lines).
    assert [len(t) for t in tables] == [11, 12, 16, 15, 7, 9]


def test_one_sentence_per_line():
    """Prose lines must not contain a second sentence starting mid-line."""
    for lineno, raw in enumerate(SPEC.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith(("#", "|")):
            continue
        for abbr in ABBREVIATIONS:
            line = line.replace(abbr, abbr.replace(".", "\x00"))
        line = re.sub(r"(\d)\.(\d)", lambda m: m.group(1) + "\x00" + m.group(2), line)
        line = line.replace("https://", "https:\x00\x00")
        bad = re.search(r"[.!?] [A-Z(]", line)
        assert not bad, f"line {lineno} appears to hold two sentences: {raw}"


def test_no_trailing_whitespace_or_tabs():
    for lineno, line in enumerate(SPEC.read_text(encoding="utf-8").splitlines(), 1):
        assert line == line.rstrip(), f"trailing whitespace on line {lineno}"
        assert "\t" not in line, f"tab character on line {lineno}"
