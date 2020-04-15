"""Test cases for the CEI module."""
import datetime
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


def test_round_down() -> None:
    assert cei.round_down(5.999) == 5.99
    assert cei.round_down(8.5) == 8.50
    assert cei.round_down(5.555) == 5.55


def test_read_xls(mock_pandas_read_excel) -> None:
    cei.read_xls("my.xls")
    mock_pandas_read_excel.assert_called_once()


@pytest.fixture
def mock_glob_glob_none(mocker: MockFixture) -> Mock:
    """Fixture for mocking glob.glob."""
    mock = mocker.patch("glob.glob")
    mock.return_value = []
    return mock


@pytest.fixture
def mock_os_path_expanduser(mocker: MockFixture) -> Mock:
    """Fixture for mocking os.path.expanduser."""
    mock = mocker.patch("os.path.expanduser")
    mock.return_value = "/home/user"
    return mock


def test_get_xls_filename_not_found(
    mock_glob_glob_none, mock_os_path_expanduser
) -> None:
    with pytest.raises(SystemExit):
        assert cei.get_xls_filename()
        mock_glob_glob_none.assert_called()
        mock_os_path_expanduser.assert_called_once()


@pytest.fixture
def mock_glob_glob_found(mocker: MockFixture) -> Mock:
    """Fixture for mocking glob.glob."""
    mock = mocker.patch("glob.glob")
    mock.return_value = ["/current/path/InfoCEI.xls"]
    return mock


def test_get_xls_filename_current_folder(mock_glob_glob_found) -> None:
    assert cei.get_xls_filename() == "/current/path/InfoCEI.xls"
    mock_glob_glob_found.assert_called_once()


@pytest.fixture
def mock_glob_glob_found_download(mocker: MockFixture) -> Mock:
    """Fixture for mocking glob.glob."""
    values = {
        "InfoCEI*.xls": [],
        "/home/user/Downloads/InfoCEI*.xls": ["/home/user/Downloads/InfoCEI.xls"],
    }

    def side_effect(arg):
        return values[arg]

    mock = mocker.patch("glob.glob")
    mock.side_effect = side_effect
    return mock


def test_get_xls_filename_download_folder(
    mock_glob_glob_found_download, mock_os_path_expanduser
) -> None:
    assert cei.get_xls_filename() == "/home/user/Downloads/InfoCEI.xls"
    mock_os_path_expanduser.assert_called_once()
    mock_glob_glob_found_download.assert_called_with(
        "/home/user/Downloads/InfoCEI*.xls"
    )
