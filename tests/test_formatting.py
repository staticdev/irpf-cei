"""Test cases for formatting module."""
import locale

import numpy as np
from pytest_mock import MockerFixture

from irpf_cei import formatting


def test_set_locale_success(mocker: MockerFixture) -> None:
    """Return empty string."""
    mocker.patch("locale.setlocale")
    assert formatting.set_locale() == ""


def test_set_locale_error(mocker: MockerFixture) -> None:
    """Return pt_BR locale."""
    mocker.patch("locale.setlocale", side_effect=locale.Error())
    assert formatting.set_locale() == "pt_BR.utf8"


def test_get_currency_format(mocker: MockerFixture) -> None:
    """Give no error."""
    mocker.patch("locale.currency")
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
