# Exporting

For exporting the project, we will focus on two aspects: what and how to export
([Targets and components]), and how to make the export equivalent to the
[`FetchContent`] users ([`<Project>Config.cmake` and `FetchContent`]).

## Targets and components

Here we have to consider what are the main targets that are installed and
exported by default, and which ones are linked to a `COMPONENT` as used by
[`find_package`]. Generally this is determined by what library or executable
files are linked to the target.

Unfortunately exporting and importing the targets linked to `COMPONENT` is not
straightforward, and it involves quite a lot of boilerplate. To try to decompose
this process, it requires:
- [`install(TARGETS)`][]: Add the installation instructions for the actual
  target.
- [`install(EXPORT)`] and [`export(EXPORT)`][]: Link the targets to a specific
  `<TargetFile>`/`COMPONENT`. A good format for the `<TargetFile>` is
  `<Project>Targets_<Component>.cmake`.
- Configure [`<Project>Config.cmake`] to import the `<TargetFile>` as requested
  by the equivalent `COMPONENT`.

This is more easily shown through an example. Let's consider and example project
`Example` with the main library `hello` and optional executable `say-hello`.
Disregarding the most of the paradigms for the sake of brevity, the project
files would look like this:

```{code-block} cmake
: caption: CMakeLists.txt
: emphasize-lines: 9-17,25-33

option(EXAMPLE_EXECUTABLE "Build the say-hello executable" OFF)

add_library(hello)
install(TARGETS hello
    EXPORT ExampleTargets
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

export(EXPORT ExampleTargets
    FILE ExampleTargets.cmake
    NAMESPACE Example::
)
install(EXPORT ExampleTargets
    FILE ExampleTargets.cmake
    NAMESPACE Example::
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/Example
)

if (EXAMPLE_EXECUTABLE)
    add_executable(say-hello)
    install(TARGETS say-hello
        EXPORT ExampleTargets_say-hello
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    )
    export(EXPORT ExampleTargets_say-hello
        FILE ExampleTargets_say-hello.cmake
        NAMESPACE Example::
    )
    install(EXPORT ExampleTargets_say-hello
        FILE ExampleTargets_say-hello.cmake
        NAMESPACE Example::
        DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/Example
    )
endif ()

configure_package_config_file(
    ExampleConfig.cmake.in ExampleConfig.cmake
    INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/Example
)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/ExampleConfig.cmake
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/Example
)
```
```{code-block}
: caption: ExampleConfig.cmake.in
: emphasize-lines: 3-6

@PACKAGE_INIT@

include(${CMAKE_CURRENT_LIST_DIR}/ExampleTargets.cmake)
if (say-hello IN_LIST Example_FIND_COMPONENTS)
    include(${CMAKE_CURRENT_LIST_DIR}/ExampleTargets_say-hello.cmake OPTIONAL RESULT_VARIABLE Example_say-hello_FOUND)
endif ()

check_required_components(Example)
```

:::{caution}
Do not use `-` as separator in the names of the Targets file. The generated
target files will glob for `<TargetFile>-*` and include them automatically.
:::

### `shared` and `static` components

Supporting both shared and static installations can be quite tricky, especially
when these can span multiple additional components. A good resource is Alex
Reinking's [blog post] on this subject, however, implementing this can be quite
tricky. For this I have a helper module [`PackageComps`] that simplifies this
implementation, and abstracts all of this boilerplate.

## `<Project>Config.cmake` and `FetchContent`

In order to make these two approaches equivalent, you only need to make sure
that the targets have appropriate namespaced aliases and that the variables are
exported appropriately.


```{code-block} cmake
: caption: CMakeLists.txt
: emphasize-lines: 2,6-10

add_library(hello)
add_library(Example::hello ALIAS hello)

if(NOT PROJECT_IS_TOP_LEVEL)
    return(PROPAGATE
        Example_VERSION
        Example_VERSION_MAJOR
        Example_VERSION_MINOR
        Example_VERSION_PATCH
        Example_VERSION_TWEAK
    )
endif ()
```

:::{attention}
Make sure that [`<Project>_VERSION`] and its equivalents are exported
:::

[blog post]: https://alexreinking.com/blog/building-a-dual-shared-and-static-library-with-cmake.html

[Targets and components]: #targets-and-components
[`<Project>Config.cmake` and `FetchContent`]: #projectconfigcmake-and-fetchcontent
[namespace]: namespace.md

[`FetchContent`]: inv:cmake:cmake:module#module:FetchContent
[`PackageComps`]: inv:cmake-extra:std:doc#cmake_modules/PackageComps
[`find_package`]: inv:cmake:cmake:command#command:find_package
[`install(TARGETS)`]: inv:cmake:cmake:command#command:install(targets)
[`install(EXPORT)`]: inv:cmake:cmake:command#command:install(export)
[`export(EXPORT)`]: inv:cmake:std:label#export(export)
[`<Project>Config.cmake`]: <inv:cmake:std:label#full signature>
[`<Project>_VERSION`]: inv:cmake:cmake:variable#variable:<PROJECT-NAME>_VERSION
