# Configuring the project

```{toctree}
:maxdepth: 1
:titlesonly: true
:hidden: true

options
import
```

The heart of a CMake project is the configure stage, where most of the user
experience diverge between each user and their needs.

We will first focus on the situation where you have downloaded the project from
[source]. The case where we are [using `FetchContent`] is more-or-less the same,
and will be explored in more details in the [importing projects] section.

:::{note}
This section only covers how you interact with CMake in order to pass
configuration options. The details of the configuration options standard
themselves are covered in [configuration options] section.
:::

[source]: ../download.md#source-project
[using `FetchContent`]: ../download.md#using-fetchcontent
[importing projects]: import.md
[configuration options]: options.md

## How do I configure the project?

::::{tab-set}
:::{tab-item} As an end-user
Use the [pre-defined presets][presets] that are defined by the project
maintainers. This can be complemented with [manual options] if needed.
:::
:::{tab-item} As an upstream developer
You should setup your [`CMakeUserPresets.json`] file. See the [presets] section
on how to interact with presets.
:::
:::{tab-item} As a downstream packager
Often times the packaging system will define the default configuration options
and pass them as [manual options], but sometimes they can also be introduced via
[environment variables].
:::
::::

:::{attention}
Do not create any `build` folder manually. Stay in the project's root path and
run your commands from there.
:::

## CMake presets

:::{admonition} Tl;dr
```console
$ cmake --preset default
```
:::

The project should be designed to have already provided all the common
configurations that the user would need. These already take care of:
- using the appropriate compiler
- setting up any compiler options needed
- detecting and importing the dependencies

Pay attention to the output of this configure step to check if there have been
any errors encountered. Some common issues are collected in the
[troubleshooting] section. If the configuration was successful, you will see
an output summary at the end listing the dependencies imported and the features
used.

[//]: # (TODO: Include an output example)

Note that this typically does not display all the configuration setup, e.g. the
compiler used. Pay attention to the full log for such information.

To get the list of all presets that are exported, use:
```console
$ cmake --list-presets
```

:::{caution}
The installation path cannot be set within the preset itself as that varies for
each person. By default, this is set to a system dependent path like
`/usr/local`, which you should not be installing to unless you are aware of the
consequences.

The installation path can be overwritten using when calling `cmake --install`:
```console
$ cmake --install ./build --prefix /path/to/install/prefix
```
But beware that this might affect projects that hard-code the installation path
at compile/build time.
:::

## `CMakeUserPresets.json`

:::{admonition} Tl;dr
```{code-block} json
:emphasize-lines: 9-11
:caption: CMakeUserPresets.json

{
  "version": 6,
  "configurePresets": [
    {
      "name": "debug",
      "displayName": "Debug",
      "binaryDir": "cmake-build-debug",
      "inherits": ["default"],
      "cacheVariables": {
        "CMAKE_BUILD_TYPE": "Debug"
      }
    }
  ]
}
```
:::

As the developer you would have specific configuration option that you always
want to use, such as setting the `BUILD_TYPE` to `Debug`. In order to save such
options, you can create your personal `CMakeUserPresets.json` outside of the git
version control. This is a simple json file, for which you are primarily
concerned about the `configurePresets` which is a list of preset objects. There
the crucial variables are:
- `name`: The name you interface with through `cmake --preset`
- `binaryDir`: The build directory
- `inherits`: A list of other presets that the current preset will add on top
- `cacheVariables`: A dictionary of configuration options to be setup

All the `cacheVariables` can be taken from the [manual options], but often times
the project would also export component-like presets so that you only need to
interface via the `inherits` field.

### Component presets

These component presets are just shortcuts for having to manually define
`cacheVariables`, and are a preferred way of designing a preset, mainly due to
the more natural naming it can use. They are typically found in a file like
`cmake/CMakePresets-components.json`. These component presets are typically
hidden, and, currently, there is no interface to print hidden interfaces.

:::{warning}
If there is a conflict in the `cacheVariables` defined in the cache presets used
by `inherits`, precedence goes to the first preset that defined in, and **NOT**
to the last preset to define it.

The `cacheVariables` defined in the current preset always takes precedence over
those defined from `inherits`.
:::

## Passing manual options

:::{admonition} Tl;dr
```console
$ cmake -b ./build -DAWESOME_PROJECT_COOL_OPTION=On
```
:::

Manually passing options is done by prepending `-D` to the option name and
assigning its value, i.e. `-D<Option_Name>=<Option_Value>`. For the list of
available options, it is best to simply navigate the top-level `CMakeLists.txt`
and find the [`option`] and [`cmake_dependent_option`] in the relevant section,
e.g.:
```cmake
#[==============================================================================================[
#                                            Options                                            #
]==============================================================================================]
option(TEMPLATE_TESTS "Template: Build test-suite" ${PROJECT_IS_TOP_LEVEL})
option(TEMPLATE_SHARED_LIBS "Template: Build as a shared library" ${PROJECT_IS_TOP_LEVEL})
option(TEMPLATE_INSTALL "Template: Install project" ${PROJECT_IS_TOP_LEVEL})
```

:::{note}
Option names are case-sensitive, make sure you pass it correctly to `-D`
argument.

These options should always be prefixed by the project's name (in this case
`TEMPLATE_*`), including the CMake native options (`CMAKE_*`).
:::

which you can interpret as:
```cmake
option(<Option_Name> <Help_Text> <Default_Value>)
cmake_dependent_option(<Option_Name> <Help_Text> <Default_Value_If_Condition_True> <Condition> <Forced_Value_If_Condition_False>)
```

Because these options can be dynamic, this is the only reliable way of
identifying the project defined options available. You can sometimes use
[`ccmake`], to display the options, but this is not recommended because it will
not show the options that have been dynamically skipped.

## Beware of environment variables

Finally, be careful that environment variables can inject or alter the CMake
options. For the most part, you can ignore the [cmake specific][cmake-env], but
beware of the following environment variables:

|    Variable    |           Preferred alternative            | Effect                                          |
|:--------------:|:------------------------------------------:|:------------------------------------------------|
|     [`CC`]     |    [`CMAKE_C_COMPILER`][CMAKE_COMPILER]    | Selects C compiler used                         |
|    [`CXX`]     |   [`CMAKE_CXX_COMPILER`][CMAKE_COMPILER]   | Selects C++ compiler used                       |
|     [`FC`]     | [`CMAKE_Fortran_COMPILER`][CMAKE_COMPILER] | Selects Fortran compiler used                   |
|   [`CFLAGS`]   |         Project specified options          | Appends to [`CMAKE_C_FLAGS`][CMAKE_FLAGS]       |
|  [`CXXFLAGS`]  |         Project specified options          | Appends to [`CMAKE_CXX_FLAGS`][CMAKE_FLAGS]     |
|   [`FFLAGS`]   |         Project specified options          | Appends to [`CMAKE_Fortran_FLAGS`][CMAKE_FLAGS] |
|    `CPATH`     |             Unset the variable             | Uncontrollable consequences [^1]                |
| `LIBRARY_PATH` |             Unset the variable             | Uncontrollable consequences [^1]                |

It is recommended to just clear out these environment variables, if you are not
aware of how these may affect the build.

[presets]: #cmake-presets
[`CMakeUserPresets.json`]: #cmakeuserpresetsjson
[component presets]: #component-presets
[manual options]: #passing-manual-options
[environment variables]: #beware-of-environment-variables

[`option`]: inv:cmake:cmake:command#command:option
[`cmake_dependent_option`]: inv:cmake:cmake:command#command:cmake_dependent_option
[`ccmake`]: inv:cmake:cmake:manual#manual:ccmake(1)
[cmake-env]: inv:cmake:cmake:manual#manual:cmake-env-variables(7)

[`CC`]: inv:cmake:cmake:envvar#envvar:CC
[`CXX`]: inv:cmake:cmake:envvar#envvar:CXX
[`FC`]: inv:cmake:cmake:envvar#envvar:FC
[`CFLAGS`]: inv:cmake:cmake:envvar#envvar:CFLAGS
[`CXXFLAGS`]: inv:cmake:cmake:envvar#envvar:CXXFLAGS
[`FFLAGS`]: inv:cmake:cmake:envvar#envvar:FFLAGS
[CMAKE_COMPILER]: inv:cmake:cmake:variable#variable:CMAKE_<LANG>_COMPILER
[CMAKE_FLAGS]: inv:cmake:cmake:variable#variable:CMAKE_<LANG>_FLAGS

[^1]: <https://gitlab.kitware.com/cmake/cmake/-/issues/25363>

[troubleshooting]: ../troubleshooting.md
