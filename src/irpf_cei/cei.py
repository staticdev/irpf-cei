"""CEI XLS reader."""
import datetime
import glob
import locale
import math
import os
import sys
from typing import Tuple

import pandas as pd


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
FILE_ENCODING = "iso-8859-1"


def get_inv_code(code: str) -> str:
    if code in ETFS:
        return "74 (ETF)"
    if (len(code) == 6 and code.endswith("11")) or (
        len(code) == 7 and code.endswith("11B")
    ):
        return "73 (FII)"
    else:
        return "31 (Ações)"


def read_xls(filename: str) -> pd.DataFrame:
    return pd.read_excel(
        filename,
        encoding=FILE_ENCODING,
        usecols="B:K",
        parse_dates=["Data Negócio"],
        date_parser=date_parse,
        skipfooter=4,
        skiprows=10,
    )


# Source: https://realpython.com/python-rounding/
def round_down(n: float, decimals: int = 2) -> float:
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier


def bens_e_direitos(source_df: pd.DataFrame, ref_year: int) -> pd.DataFrame:
    # filter buy operations
    buy_df = source_df.drop(source_df[source_df["C/V"].str.contains("V")].index)
    # group by day and asset
    buy_df = (
        buy_df.groupby(["Data Negócio", "Código"])
        .agg(
            {
                "Quantidade": "sum",
                "Preço (R$)": "first",
                "Valor Total (R$)": "sum",
                "Especificação do Ativo": "first",
            }
        )
        .reset_index()
    )
    # calculate new fields
    buy_df["Liquidação (R$)"] = (buy_df["Valor Total (R$)"] * LIQUIDACAO).apply(
        round_down
    )
    buy_df["Emolumentos (R$)"] = (
        buy_df["Valor Total (R$)"] * EMOLUMENTOS[ref_year]
    ).apply(round_down)
    buy_df["Custo Total (R$)"] = (
        buy_df["Valor Total (R$)"]
        + buy_df["Liquidação (R$)"]
        + buy_df["Emolumentos (R$)"]
    )
    print("Valores calculados de emolumentos, liquidação e custo total:")
    print(buy_df)
    result_df = (
        buy_df.groupby(["Código"])
        .agg(
            {
                "Quantidade": "sum",
                "Custo Total (R$)": "sum",
                "Especificação do Ativo": "first",
            }
        )
        .reset_index()
    )
    result_df["Preço Médio (R$)"] = (
        result_df["Custo Total (R$)"] / result_df["Quantidade"]
    ).round(decimals=3)
    return result_df


def output_bens_e_direitos(
    source_df: pd.DataFrame, ref_year: int, institution: str
) -> None:
    with pd.option_context("display.max_rows", None, "display.max_columns", None):
        source_df = clean_table(source_df)
        bens_direitos_df = bens_e_direitos(source_df, ref_year)
        output(bens_direitos_df, ref_year, institution)


def validate(filename: str) -> Tuple[int, str]:
    """
    Validates file and
    returns reference year and institution name if valid
    """
    try:
        basic_df = pd.read_excel(
            filename,
            encoding=FILE_ENCODING,
            usecols="B",
            date_parser=date_parse,
            skiprows=4,
        )
    # exits if empty
    except pd.errors.EmptyDataError:
        sys.exit("Erro: arquivo %s está vazio." % filename)

    periods = basic_df["Período de"].iloc[0].split(" a ")
    ref_year = validate_period(periods[0], periods[1])

    instutition = basic_df["Período de"].iloc[4]
    return ref_year, instutition


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


def output(df: pd.DataFrame, ref_year: int, institution: str) -> None:
    """ Return a list of declarations """
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
        print("Código: " + get_inv_code(code))
        print(
            (
                "Discriminação (sugerida): {} - Código: {} - Preço Médio Compra: R$"
                " {} - Corretora: {}"
            ).format(
                content["Especificação do Ativo"],
                code,
                str(content["Preço Médio (R$)"]).replace(".", ","),
                institution,
            )
        )
        print(
            "Situação em 31/12/{}: R$ {}".format(
                ref_year, str(content["Custo Total (R$)"])
            ).replace(".", ",")
        )


def date_parse(value: str) -> datetime.datetime:
    return datetime.datetime.strptime(value.strip(), "%d/%m/%y")


def validate_period(first: str, second: str) -> int:
    """ Considers the year from the first trade date """
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


def clean_table(source_df: pd.DataFrame) -> pd.DataFrame:
    return source_df.loc[:, ~source_df.columns.str.contains("^Unnamed")]
