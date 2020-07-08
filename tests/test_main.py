"""Test cases for the __main__ module."""
from unittest.mock import Mock
from unittest.mock import patch

import click.testing
import pytest
from pytest_mock import MockFixture

from irpf_cei import __main__


@patch(
    "inquirer.prompt",
    side_effect=[{"trades": []}, {"": "Não"}, {"trades": []}, {"": "Sim"}],
)
def test_select_trades_empty(mock_inquirer_prompt: Mock) -> None:
    """It returns empty list."""
    trades = [("trade 1", 0), ("trade 2", 1)]
    assert __main__.select_trades(trades) == []


@patch("inquirer.prompt", return_value={"trades": [1]})
def test_select_trades_some_selected(mock_inquirer_prompt: Mock) -> None:
    """It returns list with id 1."""
    trades = [("trade 1", 0), ("trade 2", 1)]
    assert __main__.select_trades(trades) == [1]


@pytest.fixture
def runner() -> click.testing.CliRunner:
    """Fixture for invoking command-line interfaces."""
    return click.testing.CliRunner()


@pytest.fixture
def mock_cei_get_xls_filename(mocker: MockFixture) -> Mock:
    """Fixture for mocking cei.get_xls_filename."""
    return mocker.patch("irpf_cei.cei.get_xls_filename")


@pytest.fixture
def mock_cei_validate_header(mocker: MockFixture) -> Mock:
    """Fixture for mocking cei.validate."""
    mock = mocker.patch("irpf_cei.cei.validate_header")
    mock.return_value = 2019, "ABC"
    return mock


@pytest.fixture
def mock_cei_read_xls(mocker: MockFixture) -> Mock:
    """Fixture for mocking cei.read_xls."""
    return mocker.patch("irpf_cei.cei.read_xls")


@pytest.fixture
def mock_cei_clean_table_cols(mocker: MockFixture) -> Mock:
    """Fixture for mocking cei.clean_table_cols."""
    return mocker.patch("irpf_cei.cei.clean_table_cols")


@pytest.fixture
def mock_cei_group_trades(mocker: MockFixture) -> Mock:
    """Fixture for mocking cei.group_trades."""
    return mocker.patch("irpf_cei.cei.group_trades")


@pytest.fixture
def mock_select_trades(mocker: MockFixture) -> Mock:
    """Fixture for mocking __main__.select_trades."""
    return mocker.patch("irpf_cei.__main__.select_trades")


@pytest.fixture
def mock_cei_get_trades(mocker: MockFixture) -> Mock:
    """Fixture for mocking cei.get_trades."""
    return mocker.patch("irpf_cei.cei.get_trades")


@pytest.fixture
def mock_cei_calculate_taxes(mocker: MockFixture) -> Mock:
    """Fixture for mocking cei.calculate_taxes."""
    return mocker.patch("irpf_cei.cei.calculate_taxes")


@pytest.fixture
def mock_cei_output_taxes(mocker: MockFixture) -> Mock:
    """Fixture for mocking cei.output_taxes."""
    return mocker.patch("irpf_cei.cei.output_taxes")


@pytest.fixture
def mock_cei_goods_and_rights(mocker: MockFixture) -> Mock:
    """Fixture for mocking cei.goods_and_rights."""
    return mocker.patch("irpf_cei.cei.goods_and_rights")


@pytest.fixture
def mock_cei_output_goods_and_rights(mocker: MockFixture) -> Mock:
    """Fixture for mocking cei.output_goods_and_rights."""
    return mocker.patch("irpf_cei.cei.output_goods_and_rights")


@patch("irpf_cei.formatting.set_locale", return_value="")
def test_main_succeeds(
    mock_formatting_set_locale: Mock,
    runner: click.testing.CliRunner,
    mock_cei_get_xls_filename: Mock,
    mock_cei_validate_header: Mock,
    mock_cei_read_xls: Mock,
    mock_cei_clean_table_cols: Mock,
    mock_cei_group_trades: Mock,
    mock_select_trades: Mock,
    mock_cei_get_trades: Mock,
    mock_cei_calculate_taxes: Mock,
    mock_cei_output_taxes: Mock,
    mock_cei_goods_and_rights: Mock,
    mock_cei_output_goods_and_rights: Mock,
) -> None:
    """Exit with a status code of zero."""
    result = runner.invoke(__main__.main)
    assert result.output.startswith("Nome do arquivo: ")
    mock_cei_calculate_taxes.assert_called_once()
    mock_cei_output_taxes.assert_called_once()
    mock_cei_goods_and_rights.assert_called_once()
    mock_cei_output_goods_and_rights.assert_called_once()
    assert result.exit_code == 0


@patch("irpf_cei.formatting.set_locale", return_value="xyz")
def test_main_locale_fail(
    mock_formatting_set_locale: Mock,
    runner: click.testing.CliRunner,
    mock_cei_get_xls_filename: Mock,
    mock_cei_validate_header: Mock,
    mock_cei_read_xls: Mock,
    mock_cei_clean_table_cols: Mock,
    mock_cei_group_trades: Mock,
    mock_select_trades: Mock,
    mock_cei_get_trades: Mock,
    mock_cei_calculate_taxes: Mock,
    mock_cei_output_taxes: Mock,
    mock_cei_goods_and_rights: Mock,
    mock_cei_output_goods_and_rights: Mock,
) -> None:
    """Exit with `SystemExit` when locale not found."""
    result = runner.invoke(__main__.main)
    assert result.output.startswith("Erro: locale xyz não encontrado")
    assert type(result.exception) == SystemExit
