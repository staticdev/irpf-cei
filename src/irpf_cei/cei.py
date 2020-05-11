"""CEI XLS reader."""
import datetime
import glob
import locale
import math
import os
import sys
from typing import List
from typing import Tuple

import pandas as pd
import xlrd

import irpf_cei.b3


FILE_ENCODING = "iso-8859-1"
IRPF_INVESTIMENT_CODES = {"ETF": "74 (ETF)", "FII": "73 (FII)", "STOCKS": "31 (Ações)"}


def get_xls_filename() -> str:
    """Returns first xls filename in current folder or Downloads folder."""
    filenames = glob.glob("InfoCEI*.xls")
    if filenames:
        return filenames[0]
    home = os.path.expanduser("~")
    filenames = glob.glob(os.path.join(home, "Downloads", "InfoCEI*.xls"))
    if filenames:
        return filenames[0]
    return sys.exit(
        "Erro: arquivo não encontrado, confira a documentação para mais informações."
    )


def date_parse(value: str) -> datetime.datetime:
    """Parse dates from CEI report."""
    return datetime.datetime.strptime(value.strip(), "%d/%m/%y")


def validate_period(first: str, second: str) -> int:
    """Considers the year from the first trade date."""
    if first.startswith("01/01") and second.startswith("31/12"):
        first_year = int(first[-4:])
        second_year = int(second[-4:])
    else:
        return sys.exit("Erro: emitir relatório do dia 1 de janeiro a 31 de dezembro.")
    if first_year == second_year and first_year >= 2019:
        return first_year
    return sys.exit(
        (
            "Erro: o período de {} a {} não é válido, favor verificar instruções "
            "na documentação."
        )
    )


def validate_header(filepath: str) -> Tuple[int, str]:
    """Validates file header.

    Arguments:
        filepath: CEI report's full path

    Returns:
        Tuple[int, str]: reference year for the report and institution name if valid.
    """
    try:
        basic_df = pd.read_excel(
            filepath,
            encoding=FILE_ENCODING,
            usecols="B",
            date_parser=date_parse,
            skiprows=4,
        )
    # exits if empty
    except (pd.errors.EmptyDataError, xlrd.XLRDError):
        sys.exit(
            (
                "Erro: arquivo {} não se encontra íntegro ou no formato de "
                "relatórios do CEI."
            ).format(filepath)
        )

    periods = basic_df["Período de"].iloc[0].split(" a ")
    ref_year = validate_period(periods[0], periods[1])

    instutition = basic_df["Período de"].iloc[4]
    return ref_year, instutition


def read_xls(filename: str) -> pd.DataFrame:
    """Reads xls.

    Args:
        filename (str): name of XLS file.

    Returns:
        pd.DataFrame: content of the file.
    """
    df = pd.read_excel(
        filename,
        encoding=FILE_ENCODING,
        usecols="B:K",
        parse_dates=["Data Negócio"],
        date_parser=date_parse,
        skipfooter=4,
        skiprows=10,
    )
    return df


# Source: https://realpython.com/python-rounding/
def round_down_money(n: float, decimals: int = 2) -> float:
    """Rounds float on second decimal cases.

    Args:
        n (float): number.
        decimals (int): Number of decimal cases. Defaults to 2.

    Returns:
        float: rounded number.
    """
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


def clean_table_cols(source_df: pd.DataFrame) -> pd.DataFrame:
    """Drops columns without values.

    Args:
        source_df (pd.DataFrame): full columns DataFrame.

    Returns:
        pd.DataFrame: DataFrame without columns with no value.
    """
    return source_df.dropna(axis="columns", how="all")


def get_trades(df: pd.DataFrame) -> List[Tuple[str, int]]:
    """Returns trades representations.

    Args:
        df (pd.DataFrame): trades DataFrame.

    Returns:
        trades: list of df indexes and string representations.
    """
    df["total_cost_rs"] = df["Valor Total (R$)"].apply(
        lambda x: "R$ " + str("{:.2f}".format(x).replace(".", ","))
    )
    df = df.drop(columns=["Valor Total (R$)"])
    list_of_list = df.astype(str).values.tolist()
    df = df.drop(columns=["total_cost_rs"])
    return [(" ".join(x), i) for i, x in enumerate(list_of_list)]


def group_trades(df: pd.DataFrame) -> pd.DataFrame:
    """Groups trades by day, asset and action.

    Args:
        df (pd.DataFrame): ungrouped trades.

    Returns:
        pd.DataFrame: grouped trades.
    """
    return (
        df.groupby(["Data Negócio", "Código", "C/V"])
        .agg(
            {
                "Quantidade": "sum",
                "Valor Total (R$)": "sum",
                "Especificação do Ativo": "first",
            }
        )
        .reset_index()
    )


def calculate_taxes(df: pd.DataFrame, auction_trades: List[int]) -> pd.DataFrame:
    """Calculates emolumentos and liquidação taxes based on reference year.

    Args:
        df (pd.DataFrame): grouped trades.
        auction_trades (List[int]): list of auction trades.

    Returns:
        pd.DataFrame: trades with two new columns of calculated taxes.
    """
    df["Liquidação (R$)"] = (
        df["Valor Total (R$)"] * irpf_cei.b3.get_trading_rate()
    ).apply(round_down_money)
    df["Emolumentos (R$)"] = (
        df["Valor Total (R$)"]
        * irpf_cei.b3.get_emoluments_rates(df["Data Negócio"].array, auction_trades)
    ).apply(round_down_money)
    return df


def buy_sell_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Create columns for buys and sells with quantity and total value.

    Args:
        df (pd.DataFrame): grouped trades.

    Returns:
        pd.DataFrame: grouped trades with four new columns of buys and sells.
    """
    df["Quantidade Compra"] = df["Quantidade"].where(df["C/V"].str.contains("C"), 0)
    df["Custo Total Compra (R$)"] = (
        df[["Valor Total (R$)", "Liquidação (R$)", "Emolumentos (R$)"]]
        .sum(axis="columns")
        .where(df["C/V"].str.contains("C"), 0)
    ).round(decimals=2)
    df["Quantidade Venda"] = df["Quantidade"].where(df["C/V"].str.contains("V"), 0)
    df["Custo Total Venda (R$)"] = (
        df[["Valor Total (R$)", "Liquidação (R$)", "Emolumentos (R$)"]]
        .sum(axis="columns")
        .where(df["C/V"].str.contains("V"), 0)
    ).round(decimals=2)
    df.drop(["Quantidade", "Valor Total (R$)"], axis="columns", inplace=True)
    return df


def group_buys_sells(df: pd.DataFrame) -> pd.DataFrame:
    """Groups buys and sells by asset.

    Args:
        df (pd.DataFrame): ungrouped buys and sells.

    Returns:
        pd.DataFrame: grouped buys and sells.
    """
    return (
        df.groupby(["Código"])
        .agg(
            {
                "Quantidade Compra": "sum",
                "Custo Total Compra (R$)": "sum",
                "Quantidade Venda": "sum",
                "Custo Total Venda (R$)": "sum",
                "Especificação do Ativo": "first",
            }
        )
        .round(decimals=2)
        .reset_index()
    )


def average_price(df: pd.DataFrame) -> pd.DataFrame:
    """Computes average price.

    Args:
        df (pd.DataFrame): buys and sells without average price.

    Returns:
        pd.DataFrame: buys and sells with average price.
    """
    df["Preço Médio (R$)"] = (
        df["Custo Total Compra (R$)"] / df["Quantidade Compra"]
    ).round(decimals=3)
    return df


def goods_and_rights(source_df: pd.DataFrame) -> pd.DataFrame:
    """Calls methods for goods and rights.

    Args:
        source_df (pd.DataFrame): raw DataFrame.

    Returns:
        pd.DataFrame: goods and rights DataFrame.
    """
    result_df = buy_sell_columns(source_df)
    result_df = group_buys_sells(source_df)
    result_df = average_price(result_df)
    return result_df


def output_taxes(tax_df: pd.DataFrame):
    """Prints tax DataFrame.

    Args:
        tax_df (pd.DataFrame): calculated tax columns.
    """
    with pd.option_context("display.max_rows", None, "display.max_columns", None):
        print("Valores calculados de emolumentos, liquidação e custo total:\n", tax_df)


def output_goods_and_rights(
    result_df: pd.DataFrame, ref_year: int, institution: str
) -> None:
    """Returns a list of assets."""
    # get available locale from shell `locale -a`
    loc = "pt_BR.utf8"
    locale.setlocale(locale.LC_ALL, loc)
    pd.set_option("float_format", locale.currency)
    print("========= Bens e Direitos =========")
    for row in result_df.iterrows():
        idx = row[0]
        content = row[1]
        code = content["Código"]
        print(
            (
                "============= Ativo {} =============\n"
                "Código: {}\n"
                "Discriminação (sugerida): {} - Código: {} - Quantidade: {} - "
                "Preço Médio Compra: R$ {} - Corretora: {}\n"
                "Situação em 31/12/{}: R$ {}\n"
            ).format(
                idx + 1,
                IRPF_INVESTIMENT_CODES[irpf_cei.b3.get_investment_type(code)],
                content["Especificação do Ativo"],
                code,
                str(content["Quantidade Compra"] - content["Quantidade Venda"]),
                str(content["Preço Médio (R$)"]).replace(".", ","),
                institution,
                ref_year,
                str(
                    content["Custo Total Compra (R$)"]
                    - content["Custo Total Venda (R$)"]
                ).replace(".", ","),
            )
        )
