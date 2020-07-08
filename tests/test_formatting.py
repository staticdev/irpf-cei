"""Test cases for formatting module."""
import locale
from unittest.mock import Mock
from unittest.mock import patch

from irpf_cei import formatting


@patch("locale.setlocale")
def test_set_locale_success(mock_locale_setlocale: Mock) -> None:
    """Return empty string."""
    assert formatting.set_locale() == ""


@patch("locale.setlocale", side_effect=locale.Error())
def test_set_locale_error(mock_locale_setlocale: Mock) -> None:
    """Return pt_BR locale."""
    assert formatting.set_locale() == "pt_BR.utf8"


@patch("locale.currency")
def test_get_currency_format(mock_locale_currency: Mock) -> None:
    """Give no error."""
    assert formatting.get_currency_format()
