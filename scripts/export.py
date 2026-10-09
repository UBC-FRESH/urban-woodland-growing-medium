#!/usr/bin/env python3
"""Export specification Markdown to DOCX (default) or HTML.

The Markdown files under ``specification/`` are the maintained source of
truth; this script is the only supported way to produce distributable
documents from them. It is a thin wrapper over pandoc (via pypandoc).

Examples:

    python scripts/export.py                     # all specs -> outputs/*.docx
    python scripts/export.py --format html       # all specs -> outputs/*.html
    python scripts/export.py specification/cwh-urban-woodland-growing-medium.md

PDF export is intentionally not wired up yet: pandoc needs a separate PDF
engine and none is installed. See context/decisions.md.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pypandoc

ROOT = Path(__file__).resolve().parent.parent
SPEC_DIR = ROOT / "specification"

# One level-1 heading in the source becomes the Word "Title" style, and the
# remaining levels line up with Heading 1 / Heading 2 in the original
# deliverables.
PANDOC_ARGS = ["--standalone", "--shift-heading-level-by=-1"]


def export(source: Path, fmt: str, output_dir: Path) -> Path:
    """Convert one Markdown specification to ``fmt`` and return the target path."""
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / f"{source.stem}.{fmt}"
    pypandoc.convert_file(
        str(source),
        fmt,
        format="md",
        outputfile=str(target),
        extra_args=PANDOC_ARGS,
    )
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "source",
        nargs="?",
        type=Path,
        default=None,
        help="Markdown file to export (default: every *.md in specification/)",
    )
    parser.add_argument("--format", choices=["docx", "html"], default="docx")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "outputs",
        help="Directory for generated documents (default: outputs/)",
    )
    args = parser.parse_args()

    sources = [args.source] if args.source else sorted(SPEC_DIR.glob("*.md"))
    if not sources:
        print(f"no specification Markdown found in {SPEC_DIR}", file=sys.stderr)
        return 1

    for source in sources:
        target = export(source, args.format, args.output_dir)
        print(f"wrote {target}")
    if args.format == "docx":
        print(
            "Reminder: visual layout review in Word or LibreOffice is a manual "
            "pre-tender step."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
