"""Test cases for the __main__ module."""
from unittest.mock import Mock, patch

import click.testing
import pytest
from pytest_mock import MockFixture

from irpf_cei import __main__


@patch(
    "inquirer.prompt",
    side_effect=[{"trades": []}, {"": "Não"}, {"trades": []}, {"": "Sim"}],
)
def test_select_trades_empty(mock_inquirer_prompt) -> None:
    trades = [("trade 1", 0), ("trade 2", 1)]
    assert __main__.select_trades(trades) == []


@patch("inquirer.prompt", return_value={"trades": [1]})
def test_select_trades_some_selected(mock_inquirer_prompt) -> None:
    trades = [("trade 1", 0), ("trade 2", 1)]
    assert __main__.select_trades(trades) == [1]


@pytest.fixture
def runner():
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


def test_main_succeeds(
    runner,
    mock_cei_get_xls_filename,
    mock_cei_validate_header,
    mock_cei_read_xls,
    mock_cei_clean_table_cols,
    mock_select_trades,
    mock_cei_get_trades,
    mock_cei_calculate_taxes,
    mock_cei_output_taxes,
    mock_cei_goods_and_rights,
    mock_cei_output_goods_and_rights,
):
    """It exits with a status code of zero."""
    result = runner.invoke(__main__.main)
    assert result.output.startswith("Nome do arquivo: ")
    mock_cei_calculate_taxes.assert_called_once()
    mock_cei_output_taxes.assert_called_once()
    mock_cei_goods_and_rights.assert_called_once()
    mock_cei_output_goods_and_rights.assert_called_once()
    assert result.exit_code == 0
