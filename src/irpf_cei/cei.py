"""CEI XLS reader."""
import datetime
import glob
import locale
import math
import os
import sys
from typing import Tuple

import pandas as pd
import xlrd

import irpf_cei.b3


FILE_ENCODING = "iso-8859-1"
IRPF_INVESTIMENT_CODES = {"ETF": "74 (ETF)", "FII": "73 (FII)", "STOCKS": "31 (Ações)"}


def date_parse(value: str) -> datetime.datetime:
    """Parse dates from CEI report.

    Arguments:
        value {str} -- some %d/%m/%y date eg. " 01/02/19 "

    Returns:
        datetime.datetime -- proper object with the day, month, year set
    """
    return datetime.datetime.strptime(value.strip(), "%d/%m/%y")


def validate_period(first: str, second: str) -> int:
    """Considers the year from the first trade date """
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
    """Validates file header and
    returns reference year and institution name if valid.

    Arguments:
        filepath {str} -- CEI report's full path

    Returns:
        Tuple[int, str] -- reference year for the report and institution
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
def round_down(n: float, decimals: int = 2) -> float:
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


# TODO reproduce rounding calculation
def calculate_taxes(df: pd.DataFrame, ref_year: int) -> pd.DataFrame:
    """Groups emolumentos and liquidação taxes.

    Args:
        df (pd.DataFrame): grouped trades.

    Returns:
        pd.DataFrame: grouped trades with two new columns of calculated taxes.
    """
    df["Liquidação (R$)"] = (
        df["Valor Total (R$)"] * irpf_cei.b3.get_trading_rate()
    ).apply(round_down)
    df["Emolumentos (R$)"] = (
        df["Valor Total (R$)"] * irpf_cei.b3.get_emoluments_rate(ref_year)
    ).apply(round_down)
    return df


def goods_and_rights(source_df: pd.DataFrame, ref_year: int, institution: str) -> None:
    source_df = clean_table_cols(source_df)
    source_df = group_trades(source_df)
    source_df = calculate_taxes(source_df, ref_year)
    # sum totals of sells and buys
    source_df["Quantidade Compra"] = source_df["Quantidade"].where(
        source_df["C/V"].str.contains("C"), 0
    )
    source_df["Quantidade Venda"] = source_df["Quantidade"].where(
        source_df["C/V"].str.contains("V"), 0
    )
    source_df["Custo Total Compra (R$)"] = (
        source_df[["Valor Total (R$)", "Liquidação (R$)", "Emolumentos (R$)"]]
        .sum(axis="columns")
        .where(source_df["C/V"].str.contains("C"), 0)
    )
    source_df["Custo Total Venda (R$)"] = (
        source_df[["Valor Total (R$)", "Liquidação (R$)", "Emolumentos (R$)"]]
        .sum(axis="columns")
        .where(source_df["C/V"].str.contains("V"), 0)
    )
    with pd.option_context("display.max_rows", None, "display.max_columns", None):
        print("Valores calculados de emolumentos, liquidação e custo total:")
        print(source_df)
        result_df = (
            source_df.groupby(["Código"])
            .agg(
                {
                    "Quantidade Compra": "sum",
                    "Quantidade Venda": "sum",
                    "Custo Total Compra (R$)": "sum",
                    "Custo Total Venda (R$)": "sum",
                    "Especificação do Ativo": "first",
                }
            )
            .reset_index()
        )
        result_df["Preço Médio (R$)"] = (
            result_df["Custo Total Compra (R$)"] / result_df["Quantidade Compra"]
        ).round(decimals=3)
        output_assets(result_df, ref_year, institution)


def get_xls_filename() -> str:
    """ Returns first xls filename in current folder or Downloads folder """
    csv_filenames = glob.glob("InfoCEI*.xls")
    if csv_filenames:
        return csv_filenames[0]
    home = os.path.expanduser("~")
    csv_filenames = glob.glob(home + "/Downloads/InfoCEI*.xls")
    if csv_filenames:
        return csv_filenames[0]
    return sys.exit(
        "Erro: arquivo não encontrado, confira a documentação para mais informações."
    )


def output_assets(df: pd.DataFrame, ref_year: int, institution: str) -> None:
    """ Return a list of assets """
    # get available locale from shell `locale -a`
    loc = "pt_BR.utf8"
    locale.setlocale(locale.LC_ALL, loc)
    pd.set_option("float_format", locale.currency)
    print("========= Bens e Direitos =========")
    for row in df.iterrows():
        idx = row[0]
        content = row[1]
        code = content["Código"]
        print("============= Ativo {} =============".format(idx + 1))
        print(
            "Código: " + IRPF_INVESTIMENT_CODES[irpf_cei.b3.get_investment_type(code)]
        )
        print(
            (
                "Discriminação (sugerida): {} - Código: {} - Quantidade: {} - "
                "Preço Médio Compra: R$ {} - Corretora: {}"
            ).format(
                content["Especificação do Ativo"],
                code,
                str(content["Quantidade Compra"] - content["Quantidade Venda"]),
                str(content["Preço Médio (R$)"]).replace(".", ","),
                institution,
            )
        )
        print(
            "Situação em 31/12/{}: R$ {}".format(
                ref_year,
                content["Custo Total Compra (R$)"] - content["Custo Total Venda (R$)"],
            ).replace(".", ",")
        )
