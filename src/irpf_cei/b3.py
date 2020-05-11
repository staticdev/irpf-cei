"""B3 module."""
import collections
import datetime
import sys
from typing import List


RatePeriod = collections.namedtuple("RatePeriod", ["start_date", "end_date", "rate"])

EMOLUMENTOS_PERIODS = [
    RatePeriod(
        datetime.datetime(2019, 1, 3), datetime.datetime(2019, 2, 1), 0.00004476
    ),
    RatePeriod(
        datetime.datetime(2019, 2, 4), datetime.datetime(2019, 3, 1), 0.00004032
    ),
    RatePeriod(
        datetime.datetime(2019, 3, 6), datetime.datetime(2019, 4, 1), 0.00004157
    ),
    RatePeriod(datetime.datetime(2019, 4, 2), datetime.datetime(2019, 5, 2), 0.0000408),
    RatePeriod(
        datetime.datetime(2019, 5, 3), datetime.datetime(2019, 6, 3), 0.00004408
    ),
    RatePeriod(
        datetime.datetime(2019, 6, 4), datetime.datetime(2019, 7, 1), 0.00004245
    ),
    RatePeriod(
        datetime.datetime(2019, 7, 2), datetime.datetime(2019, 8, 1), 0.00004189
    ),
    RatePeriod(
        datetime.datetime(2019, 8, 2), datetime.datetime(2019, 9, 2), 0.00004115
    ),
    RatePeriod(
        datetime.datetime(2019, 9, 3), datetime.datetime(2019, 10, 1), 0.00003756
    ),
    RatePeriod(
        datetime.datetime(2019, 10, 2), datetime.datetime(2019, 11, 1), 0.00004105
    ),
    RatePeriod(
        datetime.datetime(2019, 11, 4), datetime.datetime(2019, 12, 2), 0.0000411
    ),
    RatePeriod(
        datetime.datetime(2019, 12, 3), datetime.datetime(2020, 1, 2), 0.00003802
    ),
]
EMOLUMENTOS_AUCTION_RATE = 0.00007
LIQUIDACAO_RATE = 0.000275
ETFS = {
    "BBSD11",
    "XBOV11",
    "BOVB11",
    "IVVB11",
    "BOVA11",
    "BRAX11",
    "ECOO11",
    "SMAL11",
    "BOVV11",
    "DIVO11",
    "FIND11",
    "GOVE11",
    "MATB11",
    "ISUS11",
    "PIBB11",
    "SMAC11",
    "SPXI11",
}


def get_investment_type(code: str) -> str:
    """Checks if code is ETF, FII or STOCKS.

    Args:
        code (str): asset code.

    Returns:
        str: ETF, FII or STOCKS.
    """
    if code in ETFS:
        return "ETF"
    if (len(code) == 6 and code.endswith("11")) or (
        len(code) == 7 and code.endswith("11B")
    ):
        return "FII"
    else:
        return "STOCKS"


def get_trading_rate() -> float:
    """Return fixes trading rate.

    Returns:
        float: constant float.
    """
    return LIQUIDACAO_RATE


def get_emoluments_rates(
    dates: List[datetime.datetime], auction_trades: List[int]
) -> List[float]:
    """Get the list of emuluments rates.

    Args:
        dates (List[datetime.datetime]): list of trade days.
        auction_trades (List[int]): list of indexes of trades in auction.

    Returns:
        List[float]: list of rates.
    """
    rates = []
    last_period = 0
    for date in dates:
        for idx_period, period in enumerate(
            EMOLUMENTOS_PERIODS[last_period:], start=last_period
        ):
            if period.start_date <= date <= period.end_date:
                last_period = idx_period
                rates.append(period.rate)
                break
        else:
            sys.exit(
                "Nenhum período de emolumentos encontrado para a data: {}".format(date)
            )
    for trade in auction_trades:
        rates[trade] = EMOLUMENTOS_AUCTION_RATE
    return rates
