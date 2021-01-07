"""Test cases for formatting module."""
import locale
from unittest.mock import Mock
from unittest.mock import patch

import numpy as np

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


def test_fmt_money_no_padding() -> None:
    """Return rounded value."""
    num = 1581.12357
    digits = 3
    expected = "1581,124"

    assert formatting.fmt_money(num, digits) == expected


def test_fmt_money_with_padding() -> None:
    """Return rounded and padded value."""
    num = 1581.1
    digits = 3
    expected = "1581,100"

    assert formatting.fmt_money(num, digits) == expected


def test_fmt_money_is_nan() -> None:
    """Return N/A."""
    num = np.nan
    digits = 2
    expected = "N/A"

    assert formatting.fmt_money(num, digits) == expected
