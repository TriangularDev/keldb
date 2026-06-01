import os

os.system("python3 -m build && pip install dist/*.whl --force-reinstall")

project = "KelDB"

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
]

html_theme = "sphinx_rtd_theme"

autosummary_generate = True

autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": True,
}