# Importing dependencies

This section covers both how to import a project in another CMake project
([importing]), and how a user can control where a project is found ([finding]).

## Importing dependencies in a CMake project

:::{admonition} Tl;dr
```cmake
include(FetchContent)
FetchContent_Declare(awesome-project
        GIT_REPOSITORY https://github.com/user/awesome-project
        GIT_TAG main
        FIND_PACKAGE_ARGS CONFIG
)
FetchContent_MakeAvailable(awesome-project)
```
:::

The best way to consume a project is within CMake, using the
[`FetchContent`/`find_package` integration]. This will run [`find_package`]
first to try and import the system installed [packaged] version, and if none is
available it will git clone the [source] project and include it as
[`add_subdirectory`]. See the [configuration] section on how to configure the
included project.

From there, navigate the dependency's top-level `CMakeLists.txt` to find the
available targets you can use.

If you need to overwrite the upstream project's options, simply add the
[`option`] before the [`FetchContent_MakeAvailable`] call, e.g.:
```cmake
option(PROJECT2_TESTS "Project1: Override" OFF)

FetchContent_MakeAvailable(Project2)
```

### Making a dependency optional

Currently, the only clear design for supporting optional dependencies is by
avoiding [`FetchContent`] and using [`find_package`] only:

```cmake
find_package(awesome-project)
```

See the [controlling] section on how to disable or make it a required
dependency.

:::{todo}
Make the optional dependency work with [`FetchContent`]. Currently, there is no
clear way how to combine [`find_package`] and [`FetchContent`] fallthrough.
Key part is the interaction with [`CMAKE_REQUIRE_FIND_PACKAGE_<PackageName>`]
and [`CMAKE_DISABLE_FIND_PACKAGE_<PackageName>`].
:::

## How dependencies are found

Here we assume that all projects in the chain use the modern [importing]
approach to define their dependencies.

### Default behavior

By default, the project will first try to find the [`<PackageName>Config.cmake`]
file from the system installed [packaged], and if that fails, it would either
use [`FetchContent`] to download the [source] project if it is a required
dependency, or simply disable the feature if it is an [optional dependency].

### Controlling how dependencies are imported

:::{table}
:name: dependency-import-options

|                    Option                    | Effect                                                 | Notes                                                                                      |
|:--------------------------------------------:|:-------------------------------------------------------|:-------------------------------------------------------------------------------------------|
|            [`CMAKE_PREFIX_PATH`]             | Where to look for system installed package             |                                                                                            |
|            [`<PackageName>_ROOT`]            | Where to look for system installed package             | It can happen that this is not enforced                                                    |
|    [`FETCHCONTENT_TRY_FIND_PACKAGE_MODE`]    | If `NEVER`, will use downloaded version                |                                                                                            |
|  [`FETCHCONTENT_SOURCE_DIR_<PACKAGENAME>`]   | Path to package source to use (instead of downloading) | Takes precedence of any other option                                                       |
| [`CMAKE_REQUIRE_FIND_PACKAGE_<PackageName>`] | Make optional dependency required                      | If dependency is already required via `FetchContent`, it ensure the system package is used |
| [`CMAKE_DISABLE_FIND_PACKAGE_<PackageName>`] | Disable finding system installed package               |                                                                                            |
:::

Here `<PackageName>` is the case-sensitive name of the dependency, and
`<PACKAGENAME>` is the equivalent uppercase name.

:::{caution}
[`CMAKE_REQUIRE_FIND_PACKAGE_<PackageName>`] and
[`CMAKE_DISABLE_FIND_PACKAGE_<PackageName>`] options propagate to other
dependencies in the chain. Normally this would not be an issue, unless a project
uses [`Find<PackageName>.cmake`] and do not take this into account [^1].
:::

### Troubleshooting the dependency search

:::{admonition} Tl;dr
```console
$ cmake -b ./build --debug-find-pkg=<PackageName>
```
:::

The most comprehensive way of finding out how a dependency has been searched is
to use the [`--debug-find-pkg`] option. This does not cover the
[`Find<PackageName>.cmake`], where the find process is non-standard.

[importing]: #importing-dependencies-in-a-cmake-project
[finding]: #how-dependencies-are-found
[controlling]: #controlling-how-dependencies-are-imported
[optional dependency]: #making-a-dependency-optional

[packaged]: ../download.md#packaged-version
[source]: ../download.md#source-project
[configuration]: options.md#upstream-project-options

[`FetchContent`]: inv:cmake:cmake:module#module:FetchContent
[`find_package`]: inv:cmake:cmake:command#command:find_package
[`FetchContent`/`find_package` integration]: inv:cmake:std:label#fetchcontent-find_package-integration-examples
[`add_subdirectory`]: inv:cmake:cmake:command#command:add_subdirectory

[`CMAKE_PREFIX_PATH`]: inv:cmake:cmake:variable#variable:CMAKE_PREFIX_PATH
[`<PackageName>_ROOT`]: inv:cmake:cmake:variable#variable:<PackageName>_ROOT
[`FETCHCONTENT_TRY_FIND_PACKAGE_MODE`]: inv:cmake:cmake:variable#variable:FETCHCONTENT_TRY_FIND_PACKAGE_MODE
[`FETCHCONTENT_SOURCE_DIR_<PACKAGENAME>`]: inv:cmake:cmake:variable#variable:FETCHCONTENT_SOURCE_DIR_<uppercaseName>
[`CMAKE_REQUIRE_FIND_PACKAGE_<PackageName>`]: inv:cmake:cmake:variable#variable:CMAKE_REQUIRE_FIND_PACKAGE_<PackageName>
[`CMAKE_DISABLE_FIND_PACKAGE_<PackageName>`]: inv:cmake:cmake:variable#variable:CMAKE_DISABLE_FIND_PACKAGE_<PackageName>

[`FetchContent_MakeAvailable`]: inv:cmake:cmake:command#command:fetchcontent_makeavailable
[`option`]: inv:cmake:cmake:command#command:option
[`<PackageName>Config.cmake`]: <inv:cmake:std:label#full signature>
[`Find<PackageName>.cmake`]: <inv:cmake:std:label#find modules>
[`--debug-find-pkg`]: inv:cmake:std:cmdoption#cmake.--debug-find-pkg

[^1]: <https://gitlab.kitware.com/cmake/cmake/-/merge_requests/8951#note_1442376>
