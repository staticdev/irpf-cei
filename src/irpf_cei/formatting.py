"""Formatting module."""
import locale
import math
from typing import Any
from typing import Callable


def set_locale() -> str:
    """Sets locale.

    Returns:
        str: return needed locale.
    """
    # one gets available locale from shell `locale -a`
    loc = "pt_BR.utf8"
    try:
        locale.setlocale(locale.LC_ALL, loc)
    except locale.Error:
        return loc
    return ""


def get_currency_format() -> Callable[[Any], str]:
    """Return currency function.

    Returns:
        Callable[[Any], str]: function from current locale.
    """
    return locale.currency


def fmt_money(amount: float, ndigits: int = 2) -> str:
    """Return padded and rounded value."""
    if math.isnan(amount):
        return "N/A"
    rounded = round(amount, ndigits)
    result = str(rounded).replace(".", ",")
    rounded_digits = result.split(",")[1]
    missing_digits = ndigits - len(rounded_digits)
    padded_result = result + "0" * missing_digits
    return padded_result
