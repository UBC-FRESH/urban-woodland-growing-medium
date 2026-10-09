"""CLI behavior checks for the woodland-spec command."""

from typer.testing import CliRunner

import woodland_spec
from woodland_spec.cli import ORIGINAL_NAME, UPDATED_NAME, app

runner = CliRunner()


def test_version_option() -> None:
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert woodland_spec.__version__ in result.output


def test_info_command() -> None:
    result = runner.invoke(app, ["info"])
    assert result.exit_code == 0
    assert "pre-tender draft" in result.output
    assert ORIGINAL_NAME in result.output
    assert UPDATED_NAME in result.output


def test_build_command_writes_both_deliverables(tmp_path) -> None:
    result = runner.invoke(app, ["build", "--output-dir", str(tmp_path)])
    assert result.exit_code == 0
    original = tmp_path / ORIGINAL_NAME
    updated = tmp_path / UPDATED_NAME
    assert original.is_file() and original.stat().st_size > 0
    assert updated.is_file() and updated.stat().st_size > 0
