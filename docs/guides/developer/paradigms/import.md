# Importing dependencies

The modern method of importing dependencies is to use
[`FetchContent_Declare(FIND_PACKAGE_ARGS)`] which allows the user to choose how
to import the dependency: from the system ([`find_package`]) or downloaded/local
source ([`FetchContent`]).

## Required dependency

If the dependency is required, and it is a CMake based project, you can
straightforwardly use [`FetchContent_Declare(FIND_PACKAGE_ARGS)`]. Note that
this feature is only introduced in CMake 3.24. Back-porting this feature can be
quite involved:
```cmake
if (CMAKE_VERSION VERSION_GREATER_EQUAL 3.24)
    FetchContent_Declare(ProjectB
        ...
        FIND_PACKAGE_ARGS CONFIG
    )
else ()
    if (NOT DEFINED FETCHCONTENT_SOURCE_DIR_PROJECTB)
        if (NOT DEFINED FETCHCONTENT_TRY_FIND_PACKAGE_MODE)
            set(FETCHCONTENT_TRY_FIND_PACKAGE_MODE OPT_IN)
        endif ()
        if (FETCHCONTENT_TRY_FIND_PACKAGE_MODE MATCHES "(OPT_IN|ALWAYS)")
            find_package(ProjectB QUIET CONFIG)
        endif ()
    endif ()
    if (NOT ProjectB_FOUND)
        FetchContent_Declare(ProjectB
                ...
        )
    endif ()
endif ()
```

See [controlling dependency import] for more details on how to control the
import.

## Optional dependency

For optional dependencies, unfortunately the fallthrough using
[`FetchContent_Declare(FIND_PACKAGE_ARGS)`] does not allow the dependency to not
be imported. For this the only clean design is to use `find_package`, with
[`CMAKE_REQUIRE_FIND_PACKAGE_<PackageName>`] and
[`CMAKE_DISABLE_FIND_PACKAGE_<PackageName>`] to control the dependencies.

## `Find<PackageName>.cmake`

In order to provide compatibility with non-CMake projects, you can provide a
[`Find<PackageName>.cmake`] file to search for this dependency. But keep in mind
that integrating this to make it work with the project's [export] can be quite
tricky, since these modules should not be exported outside of the project, in
order to avoid conflicts with other similarly defined modules.

If you still need such a module, an example module can look as follows:

```{code-block} cmake
: caption: FindExample.cmake

set(CMAKE_REQUIRE_FIND_PACKAGE_Example FALSE)
find_package(Example CONFIG QUIET)
if (Example_FOUND)
    find_package_handle_standard_args(Example CONFIG_MODE)
    return()
endif ()

pkg_search_module(Example IMPORTED_TARGET
    example
)
if (Example_FOUND)
    add_library(Example::hello ALIAS PkgConfig::Example)
    return ()
endif ()

find_library(Hello_LIBRARY
    NAMES hello
)
mark_as_advanced(Hello_LIBRARY)
find_path(Example_INCLUDE_DIR
    NAMES hello.h
    PATH_SUFFIXES example
)
mark_as_advanced(Example_INCLUDE_DIR)
find_package_handle_standard_args(Example
    REQUIRED_VARS Hello_LIBRARY Example_INCLUDE_DIR
)
if(Example_FOUND)
    set(Example_INCLUDE_DIRS ${Example_INCLUDE_DIR})
    set(Example_LIBRARIES ${Hello_LIBRARY})
    add_library(Example::hello UNKNOWN IMPORTED)
    set_target_properties(Example::hello PROPERTIES
        IMPORTED_LOCATION ${Hello_LIBRARY}
    )
    target_include_directories(Example::hello INTERFACE ${Example_INCLUDE_DIRS})
    target_link_libraries(Example::hello INTERFACE ${Example_LIBRARIES})
endif()
```

[controlling dependency import]: #dependency-import-options
[export]: export.md

[`FetchContent_Declare(FIND_PACKAGE_ARGS)`]: inv:cmake:std:label#fetchcontent-find_package-integration-examples
[`find_package`]: inv:cmake:cmake:command#command:find_package
[`FetchContent`]: inv:cmake:cmake:module#module:FetchContent
[`CMAKE_REQUIRE_FIND_PACKAGE_<PackageName>`]: inv:cmake:cmake:variable#variable:CMAKE_REQUIRE_FIND_PACKAGE_<PackageName>
[`CMAKE_DISABLE_FIND_PACKAGE_<PackageName>`]: inv:cmake:cmake:variable#variable:CMAKE_DISABLE_FIND_PACKAGE_<PackageName>
[`Find<PackageName>.cmake`]: <inv:cmake:std:label#find modules>
