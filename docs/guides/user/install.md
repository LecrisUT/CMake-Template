# Installing the project

:::{admonition} Tl;dr
```console
$ cmake --install ./build-dir --prefix /path/to/install/prefix
```
:::

Finally, for the installation step, simply run the step mentioned above. There
is not much to mention regarding this step. In this case we do not have a preset
interface to run the install step.

The prefix specified expands where you will find your installed project:

| Type               | Path                                       |
|:-------------------|:-------------------------------------------|
| Executables        | `${prefix}/bin`                            |
| Libraries          | `${prefix}/lib64`                          |
| Headers            | `${prefix}/include`                        |
| Data               | `${prefix}/share`                          |
| CMake export files | `${prefix}/[lib64/share]/cmake/${project}` |

:::{warning}
In some project you would not be able to overwrite the installation path with
[`--prefix`]. In such cases, make sure you have passed the appropriate
[`CMAKE_INSTALL_PREFIX`] at the [configure] step.
:::

[configure]: configure/index.md
[`--prefix`]: inv:cmake:std:cmdoption#cmake--install.--prefix
[`CMAKE_INSTALL_PREFIX`]: inv:cmake:cmake:variable#variable:CMAKE_INSTALL_PREFIX
