# Guides

```{toctree}
: maxdepth: 2
: titlesonly: true

user/index
developer/index
```

## What are these guides?

In this template project, you will find a [user guide] and a [developer guide]
intended to answer common questions that either a [user] or a [developer] would
have when encountering a project that uses this template.

Feel free to reference and/or [include] these guides or sections of it in your
documentation.

[user]: user/who-is-the-user.md
[developer]: developer/who-is-the-developer.md
[user guide]: user/index.md
[developer guide]: developer/index.md
[include]: #including-these-guides-in-your-downstream-project

## Including these guides in your downstream project

The best way to include these guides is if your project uses a
[sphinx backend][rtd-sphinx] for your documentation. There you can simply link
to it using [inter-sphinx]. For example, include the following configurations
to your `docs/conf.py` file:

```{code-block} python
: caption: docs/conf.py
: emphasize-lines: 5

extensions = [
    "sphinx.ext.intersphinx",
]
intersphinx_mapping = {
    "template-guide": ("https://lecrisut-cmake-template.readthedocs.io/en/latest/", None),
}
```

:::{note}
If you want to have the links pop-up like in this documentation, use either
[`sphinx-tippy`] or [`sphinx-hoverxref`]. The latter produces better results,
however it does [not yet support Markdown documents][sphinx-hoverxref-issue].
:::

Then, you can use it in your documentation files as follows:

::::{tab-set}
:::{tab-item} Markdown
```{code-block} markdown
: caption: docs/example.md
: emphasize-lines: 4

Refer to the [following guide][template-user-guide] for a basic how-to interact
with a CMake project...

[template-user-guide]: inv:template-user-guide:std:doc#guides/user/index
```
:::
:::{tab-item} reStructuredText
```{code-block} rst
: caption: docs/example.rst
: emphasize-lines: 1

Refer to the :external+template-user-guide:std:doc:`following guide<template-user-guide>`
for a basic how-to interact with a CMake project...
```
:::
:::{tab-item} (Result)
Refer to the [following guide][user guide] for a basic how-to interact with a
CMake project...
:::
::::

[rtd-sphinx]: inv:rtd:std:doc#intro/getting-started-with-sphinx
[//]: # (TODO: Fix the intersphinx link)
[inter-sphinx]: https://www.sphinx-doc.org/en/master/usage/quickstart.html#intersphinx
[`sphinx-tippy`]: inv:sphinx-tippy#index
[`sphinx-hoverxref`]: inv:sphinx-hoverxref#index
[sphinx-hoverxref-issue]: https://github.com/readthedocs/sphinx-hoverxref/issues/250
