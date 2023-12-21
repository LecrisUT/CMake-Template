project = 'CMake Template'
copyright = '2023, Cristian Le'
author = 'Cristian Le'

extensions = [
    "myst_parser",
    "sphinx_design",
    "sphinx_togglebutton",
    "sphinx_copybutton",
    "sphinx_prompt",
    "breathe",
    "sphinx.ext.intersphinx",
    "sphinx_tippy",
    "sphinx.ext.todo",
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
myst_heading_anchors = 3

intersphinx_mapping = {
    "cmake": ("https://cmake.org/cmake/help/latest", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
    "rtd": ("https://docs.readthedocs.io/en/stable", None),
    "tmt": ("https://tmt.readthedocs.io/en/stable", None),
    "sphinx-tippy": ("https://sphinx-tippy.readthedocs.io/en/latest", None),
    "sphinx-hoverxref": ("https://sphinx-hoverxref.readthedocs.io/en/latest", None),
}

tippy_rtd_urls = [
    # Only works with RTD hosted intersphinx
    # "https://cmake.org/cmake/help/latest",
    "https://www.sphinx-doc.org/en/master",
    "https://docs.readthedocs.io/en/stable",
    "https://tmt.readthedocs.io/en/stable",
    "https://sphinx-tippy.readthedocs.io/en/latest",
    "https://sphinx-hoverxref.readthedocs.io/en/latest",
]

copybutton_exclude = ".linenos, .gp, .go"

linkcheck_ignore = [
    # pkgs.org gives 402 Client Error: Payment Required
    r"https://pkgs.org",
]

todo_include_todos = True
