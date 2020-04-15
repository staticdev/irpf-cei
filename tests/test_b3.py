"""Test cases for the B3 module."""
from irpf_cei import b3


def test_get_investment_type_etf() -> None:
    assert b3.get_investment_type("BOVA11") == "ETF"


def test_get_investment_type_fii() -> None:
    assert b3.get_investment_type("KNRI11") == "FII"


def test_get_investment_type_stock() -> None:
    assert b3.get_investment_type("PETR4") == "STOCKS"


def test_get_trading_rate() -> None:
    assert b3.get_trading_rate() == 0.000275


def test_get_emoluments_rate() -> None:
    assert b3.get_emoluments_rate(2019) == 0.00004105
