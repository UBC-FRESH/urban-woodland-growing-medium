"""Thin command-line interface over the woodland_spec builder APIs."""

from pathlib import Path
from typing import Annotated

import typer

import woodland_spec
from woodland_spec import build_document, build_updated_document

app = typer.Typer(
    help="Build the CWH woodland growing medium specification DOCX deliverables.",
)

ORIGINAL_NAME = "CWH_Woodland_Growing_Medium_Specification_Original.docx"
UPDATED_NAME = "CWH_Woodland_Growing_Medium_Specification_Updated.docx"


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"woodland-spec {woodland_spec.__version__}")
        raise typer.Exit


@app.callback(invoke_without_command=True)
def main(
    version: Annotated[
        bool,
        typer.Option("--version", help="Show the package version and exit."),
    ] = False,
) -> None:
    """woodland-spec command-line interface."""
    _version_callback(version)


@app.command()
def info() -> None:
    """Show package and deliverable status."""
    typer.echo(f"woodland-spec {woodland_spec.__version__}")
    typer.echo("Status: pre-tender draft; not issued for construction.")
    typer.echo("Deliverables:")
    typer.echo(f"  {ORIGINAL_NAME} (original, nine pages)")
    typer.echo(f"  {UPDATED_NAME} (updated, ten pages, adds Table 1A)")


@app.command()
def build(
    output_dir: Annotated[
        Path,
        typer.Option("--output-dir", help="Directory for the generated DOCX files."),
    ] = Path("outputs"),
) -> None:
    """Build the original and updated specification DOCX files."""
    output_dir.mkdir(parents=True, exist_ok=True)
    original_path = output_dir / ORIGINAL_NAME
    updated_path = output_dir / UPDATED_NAME
    build_document().save(str(original_path))
    build_updated_document().save(str(updated_path))
    typer.echo(f"Wrote {original_path}")
    typer.echo(f"Wrote {updated_path}")
    typer.echo(
        "Reminder: regenerated files need visual layout review in Word or "
        "LibreOffice before tender issue."
    )
