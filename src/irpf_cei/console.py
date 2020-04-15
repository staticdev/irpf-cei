"Irpf-cei console."
import click

import irpf_cei
import irpf_cei.cei


@click.command()
@click.version_option(version=irpf_cei.__version__)
def main() -> None:
    """ Gets csv from current folder and sort  """
    filename = irpf_cei.cei.get_xls_filename()
    click.secho("Filename: {}".format(filename), fg="blue")

    ref_year, institution = irpf_cei.cei.validate_header(filename)
    source_df = irpf_cei.cei.read_xls(filename)
    irpf_cei.cei.goods_and_rights(source_df, ref_year, institution)
