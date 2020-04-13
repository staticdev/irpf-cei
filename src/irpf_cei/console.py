"Irpf-cei console."
import click

from . import __version__, cei


@click.command()
@click.version_option(version=__version__)
def main() -> None:
    """ Gets csv from current folder and sort  """
    filename = cei.get_xls_filename()
    print("Filename: {}".format(filename))

    ref_year, institution = cei.validate(filename)
    source_df = cei.read_xls(filename)
    cei.output_bens_e_direitos(source_df, ref_year, institution)
