# ReadTheDocs

Project link: [ReadTheDocs]

## Purpose

Host documentation with additional integrations:
- build documentation on pull-request
- host multiple versions
- allow the project to be linked using [inter-sphinx] and display pop-ups like
  in this documentation using [`sphinx-tippy`] or [`sphinx-hoverxref`]

## Configuration

See the `.readthedocs.yaml` file.

## Recommendation

Try to keep the ReadTheDocs setup as vanilla as possible, and have all the
custom settings inside the sphinx configuration instead.

[ReadTheDocs]: https://readthedocs.org
[inter-sphinx]: https://www.sphinx-doc.org/en/master/usage/quickstart.html#intersphinx
[`sphinx-tippy`]: inv:sphinx-tippy#index
[`sphinx-hoverxref`]: inv:sphinx-hoverxref#index
