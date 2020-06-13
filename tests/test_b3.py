"""Test cases for the B3 module."""
import datetime

import pytest

from irpf_cei import b3


def test_get_investment_type_etf() -> None:
    """It returns ETF."""
    assert b3.get_investment_type("BOVA11") == "ETF"


def test_get_investment_type_fii() -> None:
    """It returns FII."""
    assert b3.get_investment_type("DOVL11B") == "FII"


def test_get_investment_type_stock() -> None:
    """It returns STOCKS."""
    assert b3.get_investment_type("PETR4") == "STOCKS"


def test_get_investment_not_found() -> None:
    """It returns NOT_FOUND."""
    assert b3.get_investment_type("OMG3M3") == "NOT_FOUND"


def test_get_trading_rate() -> None:
    """It returns fixed float value."""
    assert b3.get_trading_rate() == 0.000275


def test_get_emoluments_rates_error() -> None:
    """It raises `SystemExit` when date is not found."""
    series = [datetime.datetime(1930, 2, 20)]
    with pytest.raises(SystemExit):
        assert b3.get_emoluments_rates(series, [])


def test_get_emoluments_rates_sucess_no_auction() -> None:
    """It returns date rates."""
    series = [
        datetime.datetime(2019, 2, 20),
        datetime.datetime(2019, 3, 6),
        datetime.datetime(2019, 5, 14),
        datetime.datetime(2019, 12, 31),
    ]
    expected = [0.00004032, 0.00004157, 0.00004408, 0.00003802]
    result = b3.get_emoluments_rates(series, [])
    assert result == expected


def test_get_emoluments_rates_sucess_with_auction() -> None:
    """It returns date rates and auction rates."""
    series = [
        datetime.datetime(2019, 2, 20),
        datetime.datetime(2019, 3, 6),
        datetime.datetime(2019, 5, 14),
        datetime.datetime(2019, 12, 31),
    ]
    expected = [0.00004032, 0.00007, 0.00007, 0.00003802]
    result = b3.get_emoluments_rates(series, [1, 2])
    assert result == expected
