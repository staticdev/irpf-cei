import click.testing
import pytest

from irpf_cei import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_main_succeeds(runner):
    """It exits with a status code of zero."""
    result = runner.invoke(console.main)
    assert result.exit_code == 0
