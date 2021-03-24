"""Test cases for the __main__ module."""
import click.testing
import pytest
from pytest_mock import MockerFixture

from irpf_cei import __main__


def test_select_trades_empty(mocker: MockerFixture) -> None:
    """It returns empty list."""
    mocker.patch(
        "inquirer.prompt",
        side_effect=[{"trades": []}, {"": "Não"}, {"trades": []}, {"": "Sim"}],
    )
    trades = [("trade 1", 0), ("trade 2", 1)]
    assert __main__.select_trades(trades) == []


def test_select_trades_some_selected(mocker: MockerFixture) -> None:
    """It returns list with id 1."""
    mocker.patch("inquirer.prompt", return_value={"trades": [1]})
    trades = [("trade 1", 0), ("trade 2", 1)]
    assert __main__.select_trades(trades) == [1]


@pytest.fixture
def runner() -> click.testing.CliRunner:
    """Fixture for invoking command-line interfaces."""
    return click.testing.CliRunner()


@pytest.fixture
def mock_cei_get_xls_filename(mocker: MockerFixture) -> MockerFixture:
    """Fixture for mocking cei.get_xls_filename."""
    return mocker.patch("irpf_cei.cei.get_xls_filename")


@pytest.fixture
def mock_cei_validate_header(mocker: MockerFixture) -> MockerFixture:
    """Fixture for mocking cei.validate."""
    mock = mocker.patch("irpf_cei.cei.validate_header")
    mock.return_value = 2019, "ABC"
    return mock


@pytest.fixture
def mock_cei_read_xls(mocker: MockerFixture) -> MockerFixture:
    """Fixture for mocking cei.read_xls."""
    return mocker.patch("irpf_cei.cei.read_xls")


@pytest.fixture
def mock_cei_clean_table_cols(mocker: MockerFixture) -> MockerFixture:
    """Fixture for mocking cei.clean_table_cols."""
    return mocker.patch("irpf_cei.cei.clean_table_cols")


@pytest.fixture
def mock_cei_group_trades(mocker: MockerFixture) -> MockerFixture:
    """Fixture for mocking cei.group_trades."""
    return mocker.patch("irpf_cei.cei.group_trades")


@pytest.fixture
def mock_select_trades(mocker: MockerFixture) -> MockerFixture:
    """Fixture for mocking __main__.select_trades."""
    return mocker.patch("irpf_cei.__main__.select_trades")


@pytest.fixture
def mock_cei_get_trades(mocker: MockerFixture) -> MockerFixture:
    """Fixture for mocking cei.get_trades."""
    return mocker.patch("irpf_cei.cei.get_trades")


@pytest.fixture
def mock_cei_calculate_taxes(mocker: MockerFixture) -> MockerFixture:
    """Fixture for mocking cei.calculate_taxes."""
    return mocker.patch("irpf_cei.cei.calculate_taxes")


@pytest.fixture
def mock_cei_output_taxes(mocker: MockerFixture) -> MockerFixture:
    """Fixture for mocking cei.output_taxes."""
    return mocker.patch("irpf_cei.cei.output_taxes")


@pytest.fixture
def mock_cei_goods_and_rights(mocker: MockerFixture) -> MockerFixture:
    """Fixture for mocking cei.goods_and_rights."""
    return mocker.patch("irpf_cei.cei.goods_and_rights")


@pytest.fixture
def mock_cei_output_goods_and_rights(mocker: MockerFixture) -> MockerFixture:
    """Fixture for mocking cei.output_goods_and_rights."""
    return mocker.patch("irpf_cei.cei.output_goods_and_rights")


def test_main_succeeds(
    mocker: MockerFixture,
    runner: click.testing.CliRunner,
    mock_cei_get_xls_filename: MockerFixture,
    mock_cei_validate_header: MockerFixture,
    mock_cei_read_xls: MockerFixture,
    mock_cei_clean_table_cols: MockerFixture,
    mock_cei_group_trades: MockerFixture,
    mock_select_trades: MockerFixture,
    mock_cei_get_trades: MockerFixture,
    mock_cei_calculate_taxes: MockerFixture,
    mock_cei_output_taxes: MockerFixture,
    mock_cei_goods_and_rights: MockerFixture,
    mock_cei_output_goods_and_rights: MockerFixture,
) -> None:
    """Exit with a status code of zero."""
    mocker.patch("irpf_cei.formatting.set_locale", return_value="")
    result = runner.invoke(__main__.main)
    assert result.output.startswith("Nome do arquivo: ")
    mock_cei_calculate_taxes.assert_called_once()
    mock_cei_output_taxes.assert_called_once()
    mock_cei_goods_and_rights.assert_called_once()
    mock_cei_output_goods_and_rights.assert_called_once()
    assert result.exit_code == 0


def test_main_locale_fail(
    mocker: MockerFixture,
    runner: click.testing.CliRunner,
    mock_cei_get_xls_filename: MockerFixture,
    mock_cei_validate_header: MockerFixture,
    mock_cei_read_xls: MockerFixture,
    mock_cei_clean_table_cols: MockerFixture,
    mock_cei_group_trades: MockerFixture,
    mock_select_trades: MockerFixture,
    mock_cei_get_trades: MockerFixture,
    mock_cei_calculate_taxes: MockerFixture,
    mock_cei_output_taxes: MockerFixture,
    mock_cei_goods_and_rights: MockerFixture,
    mock_cei_output_goods_and_rights: MockerFixture,
) -> None:
    """Exit with `SystemExit` when locale not found."""
    mocker.patch("irpf_cei.formatting.set_locale", return_value="xyz")
    result = runner.invoke(__main__.main)
    assert result.output.startswith("Erro: locale xyz não encontrado")
    assert type(result.exception) == SystemExit
