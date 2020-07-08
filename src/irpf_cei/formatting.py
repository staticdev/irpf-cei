"""Formatting module."""
import locale
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
