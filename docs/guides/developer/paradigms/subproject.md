# Subproject

Separating the project into subproject makes it possible to import/build any
component of the project as standalone, or against a different version of the
main project, e.g. against a pre-installed version.

Examples of where you could make a project's feature into a subproject is for
bindings to other languages and for the project's [test-suite].

## When to define a subproject?

- The subproject is in a self-contained folder
- The feature is controlled by a [project option]
- The main project can be imported within the subproject

## Making it two-way compatible

Use [`<PROJECT>_VERSION`] and/or [`if(TARGET)`] to check if the project is run
from within the main project, and otherwise import the main project.

## How do I keep it in sync with the main

When calling the subproject through [`add_subdirectory`], the version
compatibility is guaranteed. The issue is with importing the main project to
match commits in [`FetchContent_Declare`]. Using built-in CMake functionality,
you do not have such a feature, but this can be done with an external module:
[`DynamicVersion`].

[`<Project>_VERSION`]: inv:cmake:cmake:variable#variable:<PROJECT-NAME>_VERSION
[`if(TARGET)`]: inv:cmake:cmake:command#command:if(target)
[`add_subdirectory`]: inv:cmake:cmake:command#command:add_subdirectory
[`DynamicVersion`]: inv:cmake-extra:std:doc#cmake_modules/DynamicVersion
[`FetchContent_Declare`]: inv:cmake:cmake:command#command:fetchcontent_declare

[test-suite]: TBD
[project option]: TBD
