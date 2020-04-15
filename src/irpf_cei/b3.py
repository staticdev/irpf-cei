EMOLUMENTOS = {2019: 0.00004105, 2020: 0.00003006}
LIQUIDACAO = 0.000275
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
    if code in ETFS:
        return "ETF"
    if (len(code) == 6 and code.endswith("11")) or (
        len(code) == 7 and code.endswith("11B")
    ):
        return "FII"
    else:
        return "STOCKS"


def get_trading_rate() -> float:
    return LIQUIDACAO


def get_emoluments_rate(year: int) -> float:
    return EMOLUMENTOS[year]
