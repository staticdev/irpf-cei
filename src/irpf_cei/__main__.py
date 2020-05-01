"""Command-line interface."""
import click

import irpf_cei.cei


@click.command()
@click.version_option()
def main() -> None:
    """ Gets csv from current folder and sort  """
    filename = irpf_cei.cei.get_xls_filename()
    click.secho("Filename: {}".format(filename), fg="blue")

    ref_year, institution = irpf_cei.cei.validate_header(filename)
    source_df = irpf_cei.cei.read_xls(filename)
    source_df = irpf_cei.cei.clean_table_cols(source_df)
    tax_df = irpf_cei.cei.calculate_taxes(source_df)
    irpf_cei.cei.output_taxes(tax_df)
    result_df = irpf_cei.cei.goods_and_rights(tax_df)
    irpf_cei.cei.output_goods_and_rights(result_df, ref_year, institution)


if __name__ == "__main__":
    main()  # pragma: no cover
