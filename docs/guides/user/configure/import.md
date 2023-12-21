# Importing dependencies

## Default behavior

## Controlling how dependencies are imported

|                    Option                    | Effect                                                 | Notes                                                                                      |
|:--------------------------------------------:|:-------------------------------------------------------|:-------------------------------------------------------------------------------------------|
|            [`CMAKE_PREFIX_PATH`]             | Where to look for system installed package             |                                                                                            |
|            [`<PackageName>_ROOT`]            | Where to look for system installed package             | It can happen that this is not enforced                                                    |
|    [`FETCHCONTENT_TRY_FIND_PACKAGE_MODE`]    | If `NEVER`, will use downloaded version                |                                                                                            |
|  [`FETCHCONTENT_SOURCE_DIR_<PACKAGENAME>`]   | Path to package source to use (instead of downloading) | Takes precedence of any other option                                                       |
| [`CMAKE_REQUIRE_FIND_PACKAGE_<PackageName>`] | Make optional dependency required                      | If dependency is already required via `FetchContent`, it ensure the system package is used |
| [`CMAKE_DISABLE_FIND_PACKAGE_<PackageName>`] | Disable finding system installed package               |                                                                                            |

Here `<PackageName>` is the case-sensitive name of the dependency, and
`<PACKAGENAME>` is the equivalent uppercase name.


[`CMAKE_PREFIX_PATH`]: inv:cmake:cmake:variable#variable:CMAKE_PREFIX_PATH
[`<PackageName>_ROOT`]: inv:cmake:cmake:variable#variable:<PackageName>_ROOT
[`FETCHCONTENT_TRY_FIND_PACKAGE_MODE`]: inv:cmake:cmake:variable#variable:FETCHCONTENT_TRY_FIND_PACKAGE_MODE
[`FETCHCONTENT_SOURCE_DIR_<PACKAGENAME>`]: inv:cmake:cmake:variable#variable:FETCHCONTENT_SOURCE_DIR_<uppercaseName>
[`CMAKE_REQUIRE_FIND_PACKAGE_<PackageName>`]: inv:cmake:cmake:variable#variable:CMAKE_REQUIRE_FIND_PACKAGE_<PackageName>
[`CMAKE_DISABLE_FIND_PACKAGE_<PackageName>`]: inv:cmake:cmake:variable#variable:CMAKE_DISABLE_FIND_PACKAGE_<PackageName>
