# Namespacing

Until proper namespacing can be automatically implemented [^1], there are a few
standards that the wider community have converged upon. These standards are
designed so that the project is transparently imported via
[`find_package` and `FetchContent`].

## Options

The [project options] should be prefixed by `<PROJECT>_`, where `<PROJECT>` is
the uppercase name of the project.

The option's help text should also be prefixed by `<Project>: ` to indicate the
source of the option's definition. This is useful when an importing project
overrides or forces an imported project's option, i.e.:
```cmake
project(ProjectA)
option(PROJECTB_TESTS "ProjectA: Overload" ON)
FetchContent_Declare(ProjectB
        ...
)
```

## Targets

Both the actual target names and the aliases should be prefixed by the
`<Project>` namespace:

```cmake
add_library(Project_Hello)
add_library(Project::Hello ALIAS Project_Hello)
set_target_properties(Project_Hello PROPERTIES
        OUTPUT_NAME hello
        EXPORT_NAME Hello
)
```

:::{note}
Here we are setting [`OUTPUT_NAME`] and [`EXPORT_NAME`] to properly set the
target's file name and exported name.
:::

## Variables

Generally, we don't need to worry about the namespacing of variables since these
are not propagated outwards. However, this means that we have to explicitly
export the variables we want to export. The variables we want to export are
[`<Project>_VERSION`] and all variables exported in [`<Project>Config.cmake`].

## Message

For namespacing messages, you should push a relevant namespace on the
[`CMAKE_MESSAGE_CONTEXT`] stack. Just make sure to pop the namespace to sections
that are in a [`macro`] or [`include`].

[`CMAKE_MESSAGE_CONTEXT`]: inv:cmake:cmake:variable#variable:CMAKE_MESSAGE_CONTEXT
[`OUTPUT_NAME`]: inv:cmake:cmake:prop_tgt#prop_tgt:OUTPUT_NAME
[`EXPORT_NAME`]: inv:cmake:cmake:prop_tgt#prop_tgt:EXPORT_NAME
[`<Project>_VERSION`]: inv:cmake:cmake:variable#variable:<PROJECT-NAME>_VERSION
[`<Project>Config.cmake`]: <inv:cmake:std:label#full signature>
[`macro`]: inv:cmake:cmake:command#command:macro
[`include`]: inv:cmake:cmake:command#command:include

[`find_package` and `FetchContent`]: export.md#projectconfigcmake-and-fetchcontent
[project options]: TBD

[^1]: <https://gitlab.kitware.com/cmake/cmake/-/issues/22687>
