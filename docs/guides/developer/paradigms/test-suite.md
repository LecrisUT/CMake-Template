# Test-suite

As a testing framework, consider [catch2] and [GoogleTest] for their good CMake
compatibility. Here we will focus on the overall test-suite design and CMake
native testing.

## As a subproject

One useful design is to make the test-suite as a [subproject]. This makes it
possible to run the tests post-installation, e.g. for [conda] or Fedora
packaging. Depending on how the tests are imported, some unit-tests or packaging
test would have to be excluded.

## Define `<Project>_add_test`

For functional and packaging tests, it can be useful to define a
`<Project>_add_test` helper function wrapping around [`ctest --build-and-test`],
which makes sure we import the main project appropriately. This is particularly
useful for testing libraries and examples as self-contained CMake projects.

## Packaging tests

A specific use-case of [`<Project>_add_test`] is to test the packaging and
importing of the project. This template covers testing [`FetchContent`],
[`find_package`], and [`PkgConfig`].

[catch2]: https://github.com/catchorg/Catch2
[GoogleTest]: https://google.github.io/googletest
[conda]: https://conda.io/projects/conda/en/latest/index.html

[`ctest --build-and-test`]: inv:cmake:std:cmdoption#ctest.--build-and-test
[`FetchContent`]: inv:cmake:cmake:module#module:FetchContent
[`find_package`]: inv:cmake:cmake:command#command:find_package
[`PkgConfig`]: inv:cmake:cmake:module#module:FindPkgConfig

[subproject]: subproject.md
[`<Project>_add_test`]: #define-project_add_test
