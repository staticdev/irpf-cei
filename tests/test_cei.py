"""Test cases for the CEI module."""
import datetime
import os
from unittest.mock import Mock, patch

import numpy as np
import pandas as pd
import pytest
from pytest_mock import MockFixture

from irpf_cei import cei


def test_date_parse() -> None:
    expected = datetime.datetime(day=1, month=2, year=2019)
    assert cei.date_parse(" 01/02/19 ") == expected


@pytest.fixture
def mock_pandas_read_excel(mocker: MockFixture) -> Mock:
    """Fixture for mocking pandas.read_excel."""
    mock = mocker.patch("pandas.read_excel")
    header = pd.DataFrame(
        {"Período de": ["01/01/2019 a 31/12/2019", "NAN", "NAN", "NAN", "INSTITUTION"]}
    )
    mock.return_value = header
    return mock


def test_read_xls(mock_pandas_read_excel: Mock) -> None:
    cei.read_xls("my.xls")
    mock_pandas_read_excel.assert_called_once()


def test_round_down() -> None:
    assert cei.round_down(5.999) == 5.99
    assert cei.round_down(8.5) == 8.50
    assert cei.round_down(5.555) == 5.55


@pytest.fixture
def cwd(fs: MockFixture, monkeypatch: Mock):
    fs.cwd = "/my/path"
    monkeypatch.setenv("HOME", "/home/user")


def test_get_xls_filename_not_found(fs: MockFixture, cwd: Mock) -> None:
    """It raises `SystemExit` when file is not found."""
    with pytest.raises(SystemExit):
        assert cei.get_xls_filename()


def test_get_xls_filename_current_folder(fs: MockFixture, cwd: Mock) -> None:
    """It returns filename found in current folder."""
    fs.create_file("/my/path/InfoCEI.xls")
    assert cei.get_xls_filename() == "InfoCEI.xls"  # adapted to your implementation


def test_get_xls_filename_download_folder(fs: MockFixture, cwd: Mock) -> None:
    """It returns filename found in downloads folder."""
    path = os.path.join("/home/user", "Downloads", "InfoCEI.xls")
    fs.create_file(path)
    assert cei.get_xls_filename() == path


def test_validate_period_success() -> None:
    """It returns reference year."""
    assert cei.validate_period("01/01/2020", "31/12/2020") == 2020


def test_validate_period_wrong_start_finish() -> None:
    with pytest.raises(SystemExit):
        assert cei.validate_period("01/12/2020", "31/12/2020")


def test_validate_period_different_years() -> None:
    with pytest.raises(SystemExit):
        assert cei.validate_period("01/01/2019", "31/12/2020")


def test_validate_header_empty_file(fs: MockFixture, cwd: Mock) -> None:
    fs.create_file("/my/path/InfoCEI.xls")
    with pytest.raises(SystemExit):
        cei.validate_header("/my/path/InfoCEI.xls")


@pytest.fixture
def mock_validate_period(mocker: MockFixture) -> Mock:
    """Fixture for mocking irpf_cei.cei.validate_period."""
    mock = mocker.patch("irpf_cei.cei.validate_period")
    mock.return_value = 2019
    return mock


def test_validate_header(
    mock_pandas_read_excel: MockFixture, mock_validate_period: MockFixture
) -> None:
    assert cei.validate_header("/my/path/InfoCEI.xls") == (2019, "INSTITUTION")


def test_clean_table_cols() -> None:
    df = pd.DataFrame(
        {
            "full_valued": [1, 2, 3],
            "all_missing1": [None, None, None],
            "some_missing": [None, 2, 3],
            "all_missing2": [None, None, None],
        }
    )
    expected_df = pd.DataFrame({"full_valued": [1, 2, 3], "some_missing": [None, 2, 3]})
    result_df = cei.clean_table_cols(df)
    pd.testing.assert_frame_equal(result_df, expected_df)


def test_group_trades() -> None:
    df = pd.DataFrame(
        {
            "Data Negócio": ["1", "1", "2", "2", "2", "2"],
            "Código": ["BOVA11", "PETR4", "PETR4", "BOVA11", "BOVA11", "BOVA11"],
            "C/V": [" C ", " V ", " V ", " V ", " C ", " C "],
            "Quantidade": [20, 30, 50, 80, 130, 210],
            "Valor Total (R$)": [10.20, 30.50, 80.13, 210.34, 550.89, 144.233],
            "Especificação do Ativo": [
                "ISHARES",
                "PETRO",
                "PETRO",
                "ISHARES",
                "ISHARES",
                "ISHARES",
            ],
        }
    )
    expected_df = pd.DataFrame(
        {
            "Data Negócio": ["1", "1", "2", "2", "2"],
            "Código": ["BOVA11", "PETR4", "BOVA11", "BOVA11", "PETR4"],
            "C/V": [" C ", " V ", " C ", " V ", " V "],
            "Quantidade": [20, 30, 340, 80, 50],
            "Valor Total (R$)": [10.20, 30.50, 695.123, 210.34, 80.13],
            "Especificação do Ativo": [
                "ISHARES",
                "PETRO",
                "ISHARES",
                "ISHARES",
                "PETRO",
            ],
        }
    )
    result_df = cei.group_trades(df)
    pd.testing.assert_frame_equal(result_df, expected_df)


@pytest.fixture
def mock_group_trades(mocker: MockFixture) -> Mock:
    """Fixture for mocking cei.group_trades."""
    mock = mocker.patch("irpf_cei.cei.group_trades")
    df = pd.DataFrame(
        {
            "Valor Total (R$)": [
                4618.5,
                935,
                # 10956
            ],
        }
    )
    mock.return_value = df
    return mock


def test_calculate_taxes_2019(mock_group_trades) -> None:
    ref_year = 2019
    expected_df = pd.DataFrame(
        {
            "Valor Total (R$)": [
                4618.5,
                935,
                # 10956
            ],
            "Liquidação (R$)": [
                1.27,
                0.25,
                # 3.01
            ],
            "Emolumentos (R$)": [
                0.18,
                0.03,
                # 0.45
            ],
        }
    )
    result_df = cei.calculate_taxes(pd.DataFrame(), ref_year)
    pd.testing.assert_frame_equal(result_df, expected_df)


def test_buy_sell_columns() -> None:
    df = pd.DataFrame(
        {
            "Data Negócio": ["1", "1", "2", "2", "2"],
            "Código": ["BOVA11", "PETR4", "BOVA11", "BOVA11", "PETR4"],
            "C/V": [" C ", " V ", " C ", " V ", " V "],
            "Quantidade": [20, 30, 340, 80, 50],
            "Valor Total (R$)": [10.20, 30.50, 695.123, 210.34, 80.13],
            "Liquidação (R$)": [1, 2, 5, 4, 3],
            "Emolumentos (R$)": [0.2, 0.3, 1.3, 0.8, 0.5],
        }
    )
    expected_df = pd.DataFrame(
        {
            "Data Negócio": ["1", "1", "2", "2", "2"],
            "Código": ["BOVA11", "PETR4", "BOVA11", "BOVA11", "PETR4"],
            "C/V": [" C ", " V ", " C ", " V ", " V "],
            "Liquidação (R$)": [1, 2, 5, 4, 3],
            "Emolumentos (R$)": [0.2, 0.3, 1.3, 0.8, 0.5],
            "Quantidade Compra": [20, 0, 340, 0, 0],
            "Custo Total Compra (R$)": [11.40, 0, 701.423, 0, 0],
            "Quantidade Venda": [0, 30, 0, 80, 50],
            "Custo Total Venda (R$)": [0, 32.80, 0, 215.14, 83.63],
        }
    )
    result_df = cei.buy_sell_columns(df)
    pd.testing.assert_frame_equal(result_df, expected_df)


def test_group_buys_sells() -> None:
    df = pd.DataFrame(
        {
            "Código": ["BOVA11", "PETR4", "BOVA11", "BOVA11", "PETR4"],
            "Quantidade Compra": [20, 0, 340, 0, 0],
            "Custo Total Compra (R$)": [11.40, 0, 701.423, 0, 0],
            "Quantidade Venda": [0, 30, 0, 80, 50],
            "Custo Total Venda (R$)": [0, 32.80, 0, 215.14, 83.63],
            "Especificação do Ativo": [
                "ISHARES",
                "PETRO",
                "ISHARES",
                "ISHARES",
                "PETRO",
            ],
        }
    )
    expected_df = pd.DataFrame(
        {
            "Código": ["BOVA11", "PETR4"],
            "Quantidade Compra": [360, 0],
            "Custo Total Compra (R$)": [712.823, 0],
            "Quantidade Venda": [80, 80],
            "Custo Total Venda (R$)": [215.14, 116.43],
            "Especificação do Ativo": ["ISHARES", "PETRO"],
        }
    )
    result_df = cei.group_buys_sells(df)
    pd.testing.assert_frame_equal(result_df, expected_df)


def test_average_price() -> None:
    df = pd.DataFrame(
        {
            "Código": ["BOVA11", "PETR4"],
            "Quantidade Compra": [360, 0],
            "Custo Total Compra (R$)": [712.823, 0],
        }
    )
    expected_df = pd.DataFrame(
        {
            "Código": ["BOVA11", "PETR4"],
            "Quantidade Compra": [360, 0],
            "Custo Total Compra (R$)": [712.823, 0],
            "Preço Médio (R$)": [1.980, np.nan],
        }
    )
    result_df = cei.average_price(df)
    pd.testing.assert_frame_equal(result_df, expected_df)


@patch("irpf_cei.cei.buy_sell_columns")
@patch("irpf_cei.cei.group_buys_sells")
@patch("irpf_cei.cei.average_price", return_value=pd.DataFrame())
def test_goods_and_rights(
    mock_average_price, mock_groups_buys_sells, mock_buy_sell_columns
) -> None:
    df = cei.goods_and_rights(pd.DataFrame())
    assert type(df) is pd.DataFrame


@patch("builtins.print")
def test_output_taxes(mock_print) -> None:
    cei.output_taxes(pd.DataFrame())
    mock_print.assert_called_once()


@patch("builtins.print")
def test_output_goods_and_rights(mock_print) -> None:
    df = pd.DataFrame(
        {
            "Código": ["BOVA11", "PETR4"],
            "Quantidade Compra": [360, 0],
            "Custo Total Compra (R$)": [712.823, 0],
            "Quantidade Venda": [80, 80],
            "Custo Total Venda (R$)": [215.14, 116.43],
            "Preço Médio (R$)": [1.980, np.nan],
            "Especificação do Ativo": ["ISHARES", "PETRO"],
        }
    )
    cei.output_goods_and_rights(df, 2019, "XYZ")
    assert mock_print.call_count == 3
