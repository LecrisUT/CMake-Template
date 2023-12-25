# Project options

It is important to avoid name-clashing with the options, therefore all the
options defined by the project must be appropriately [namespaced]. Here we will
look on some good default options to implement.

## `<PROJECT>_TESTS`

This option enables the build of the [test-suite] from the main project.

It is important to set the default value to [`PROJECT_IS_TOP_LEVEL`]: when the
project is imported through [`FetchContent`], it will not automatically populate
the importing project's tests with the dependent's tests.

## `<PROJECT>_INSTALL`

This option enables the installation of the project when calling [`cmake
--install`].

It is important to set the default value to [`PROJECT_IS_TOP_LEVEL`]: when the
project is imported through [`FetchContent`], it will not also install the
dependent project and accidentally overwrite the system installation. This works
well in combination with [`<PROJECT>_SHARED_LIBS`].

## `<PROJECT>_SHARED_LIBS`

This option sets [`BUILD_SHARED_LIBS`] limited to the scope of the project only.

It is recommended to set the default value to [`PROJECT_IS_TOP_LEVEL`]: when the
project is imported through [`FetchContent`], it will not create an additional
runtime dependency. This works well in combination with [`<PROJECT>_INSTALL`].

## Dependency flags

For most dependencies, it is preferred to make the dependencies optional and use
the built-in CMake variables [`CMAKE_REQUIRE_FIND_PACKAGE_<PackageName>`] and
[`CMAKE_DISABLE_FIND_PACKAGE_<PackageName>`] to control how these dependencies
should be treated.

Exception to the rule are dependencies that drastically change the project's
behavior, e.g. MPI or OpenMP, and dependencies that have various variants, e.g.
FFTW or MKL. A common pattern is to use the `<PROJECT>_<Dependency>` as the
option name.

## Other feature options

Other options are up to the discretion of the project. Here it is useful to
mention [`add_feature_info`] as a way to display a useful summary for the user
through [`FeatureSummary`].

[namespaced]: namespace.md#options
[test-suite]: test-suite.md#as-a-subproject
[`<PROJECT>_SHARED_LIBS`]: #project_shared_libs
[`<PROJECT>_INSTALL`]: #project_install

[`PROJECT_IS_TOP_LEVEL`]: inv:cmake:cmake:variable#variable:PROJECT_IS_TOP_LEVEL
[`FetchContent`]: inv:cmake:cmake:module#module:FetchContent
[`cmake --install`]: inv:cmake:std:cmdoption#cmake.--install
[`BUILD_SHARED_LIBS`]: inv:cmake:cmake:variable#variable:BUILD_SHARED_LIBS
[`CMAKE_REQUIRE_FIND_PACKAGE_<PackageName>`]: inv:cmake:cmake:variable#variable:CMAKE_REQUIRE_FIND_PACKAGE_<PackageName>
[`CMAKE_DISABLE_FIND_PACKAGE_<PackageName>`]: inv:cmake:cmake:variable#variable:CMAKE_DISABLE_FIND_PACKAGE_<PackageName>
[`add_feature_info`]: inv:cmake:cmake:command#command:add_feature_info
[`FeatureSummary`]: inv:cmake:cmake:module#module:FeatureSummary
