project = 'CMake Template'
copyright = '2023, Cristian Le'
author = 'Cristian Le'

extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx_togglebutton",
    "breathe",
    "sphinx.ext.intersphinx",
]

templates_path = []
exclude_patterns = [
    'build',
    '_build',
    'Thumbs.db',
    '.DS_Store',
]
source_suffix = [".md"]


html_theme = 'furo'

myst_enable_extensions = [
    "tasklist",
    "colon_fence",
]

intersphinx_mapping = {
    "cmake": ("https://cmake.org/cmake/help/latest", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
    "rtd": ("https://docs.readthedocs.io/en/stable", None),
    "tmt": ("https://tmt.readthedocs.io/en/stable", None),
}
