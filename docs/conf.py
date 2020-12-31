"""Sphinx configuration."""
from datetime import datetime


project = "IRPF CEI"
author = "Thiago Carvalho D'Ávila"
copyright = f"{datetime.now().year}, {author}"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx_rtd_theme"]
autodoc_typehints = "description"
html_theme = "sphinx_rtd_theme"
