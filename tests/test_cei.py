"""Test cases for the CEI module."""
import datetime
import os
from unittest.mock import Mock

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
