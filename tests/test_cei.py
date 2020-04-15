"""Test cases for the CEI module."""
import datetime
import os
from unittest.mock import Mock

import pytest
from pytest_mock import MockFixture

from irpf_cei import cei


def test_date_parse() -> None:
    expected = datetime.datetime(day=1, month=2, year=2019)
    assert cei.date_parse(" 01/02/19 ") == expected


@pytest.fixture
def mock_pandas_read_excel(mocker: MockFixture) -> Mock:
    """Fixture for mocking pandas.read_excel."""
    return mocker.patch("pandas.read_excel")


def test_read_xls(mock_pandas_read_excel: Mock) -> None:
    cei.read_xls("my.xls")
    mock_pandas_read_excel.assert_called_once()


def test_round_down() -> None:
    assert cei.round_down(5.999) == 5.99
    assert cei.round_down(8.5) == 8.50
    assert cei.round_down(5.555) == 5.55


@pytest.fixture
def cwd(fs: MockFixture, monkeypatch: pytest.MonkeyPatch):
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
