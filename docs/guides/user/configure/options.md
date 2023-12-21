# Configuration options

The configuration options that you will encounter would be one of the

[CMake native]: #cmake-native-options
[project specific]: #project-specific-options
[upstream project]: #upstream-project-options

## CMake native options

The full list of [cmake variables] can be overwhelming for newcomers, however
this is a great resource to find all that CMake can do. Here I will give just
list the very most basic options that you typically need to get started.

|          Option           | Effect                                  | Notes                                             |
|:-------------------------:|:----------------------------------------|---------------------------------------------------|
| [`CMAKE_<LANG>_COMPILER`] | Specify `<LANG>` compiler               |                                                   |
|  [`CMAKE_<LANG>_FLAGS`]   | Append `<LANG>` compiler flags          | Try to avoid [^1]                                 |
| [`CMAKE_INSTALL_PREFIX`]  | Specify where to install the project    |                                                   |
|   [`CMAKE_BUILD_TYPE`]    | Specify what build variant to configure | Can be set to `""` to disable CMake default flags |

Here `<LANG>` is typically one of `C`, `CXX`, `Fortran`, and
[many others][`enable_language`].

:::{important}
There are more options related to finding/importing dependencies explained in
the [import] section. Please read that section carefully.
:::

[^1]: Use project native options. Otherwise, these flags will propagate to all
      dependencies (consider the effect of `-Wall` flag)

## Project specific options

Consult with the actual project's documentation for the options available. Here
is just the list of options that are encouraged to be implemented by this
template.

|          Option           | Effect                                      | Notes                |
|:-------------------------:|:--------------------------------------------|:---------------------|
|     `<PROJECT>_TESTS`     | Build project's test-suite                  | Dynamic default [^2] |
|  `<PROJECT>_SHARED_LIBS`  | Build project's libraries as shared library | Dynamic default [^2] |
|    `<PROJECT>_INSTALL`    | Enable installing the project               | Dynamic default [^2] |

Here `<PROJECT>` is the project's option namespace, which is typically the
uppercase name of the project.

[^2]: If the project is the main CMake project, i.e. it is not being imported,
      the default is `ON`, otherwise it is `OFF`

## Upstream project options

CMake options are propagated to upstream dependencies that are imported if the
project is imported via `FetchContent` (see [import] section for more details).
You can thus control the options of these dependencies as well, e.g. you could
set `<PROJECT2>_TESTS=ON` to test the imported `<PROJECT2>` as well.

This, however, does not work with installed projects.

[import]: import.md#controlling-how-dependencies-are-imported

[cmake variables]: inv:cmake:cmake:manual#manual:cmake-variables(7)
[`enable_language`]: inv:cmake:cmake:command#command:enable_language
[`CMAKE_<LANG>_COMPILER`]: inv:cmake:cmake:variable#variable:CMAKE_<LANG>_COMPILER
[`CMAKE_<LANG>_FLAGS`]: inv:cmake:cmake:variable#variable:CMAKE_<LANG>_FLAGS
[`CMAKE_INSTALL_PREFIX`]: inv:cmake:cmake:variable#variable:CMAKE_INSTALL_PREFIX
[`CMAKE_BUILD_TYPE`]: inv:cmake:cmake:variable#variable:CMAKE_BUILD_TYPE
