"""Command-line interface."""
from typing import Any
from typing import List
from typing import Tuple

import click
import inquirer

import irpf_cei.cei
import irpf_cei.formatting


def select_trades(trades: List[Tuple[str, int]]) -> Any:
    """Checkbox selection of auction trades.

    Args:
        trades (List[Tuple[str, int]]): list of all trades and indexes.

    Returns:
        Any: list of indexes of selected auction trades.
    """
    click.secho(
        (
            "Para o cálculo dos emolumentos é necessário informar operações"
            "realizadas em horário de leilão. Essa informação é obtida com "
            "a sua corretora através de relatórios de ordem de compra."
        ),
        fg="green",
    )
    while True:
        selection = inquirer.prompt(
            [
                inquirer.Checkbox(
                    "trades",
                    message=(
                        "Quais operações foram realizadas em horário de leilão? "
                        "(Selecione apertando espaço e ao terminar aperte enter)"
                    ),
                    choices=trades,
                )
            ]
        )["trades"]
        if len(selection) == 0:
            answer = inquirer.prompt(
                [
                    inquirer.List(
                        "",
                        message="Nenhuma operação selecionada.\nIsso está correto?",
                        choices=["Sim", "Não"],
                    )
                ]
            )[""]
            if answer == "Sim":
                return []
        else:
            return selection


@click.command()
@click.version_option()
def main() -> None:
    """Sequecence of operations for trades."""
    response = irpf_cei.formatting.set_pt_br_locale()
    if not response:
        click.secho(
            f"Erro: {response.value['message']}",
            fg="red",
            err=True,
        )
        # Raises SystemExit
        raise click.ClickException("")
    filename = irpf_cei.cei.get_xls_filename()
    click.secho(f"Nome do arquivo: {filename}", fg="blue")

    ref_year, institution = irpf_cei.cei.validate_header(filename)
    source_df = irpf_cei.cei.read_xls(filename)
    source_df = irpf_cei.cei.clean_table_cols(source_df)
    source_df = irpf_cei.cei.group_trades(source_df)
    trades = irpf_cei.cei.get_trades(source_df)
    auction_trades = select_trades(trades)
    tax_df = irpf_cei.cei.calculate_taxes(source_df, auction_trades)
    irpf_cei.cei.output_taxes(tax_df)
    result_df = irpf_cei.cei.goods_and_rights(tax_df)
    irpf_cei.cei.output_goods_and_rights(result_df, ref_year, institution)


if __name__ == "__main__":
    main()  # pragma: no cover
