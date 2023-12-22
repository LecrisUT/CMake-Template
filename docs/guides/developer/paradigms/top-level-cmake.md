# Top level `CMakeLists.txt`

The top-level `CMakeLists.txt` should be as navigable as the project's top-level
`README.md` file. For this reason, I encourage to organize the top-level file as
follows:

## Sectioning

There are various ways of writing a section separator. In this template I use
comment blocks spanning roughly 80 characters wide:
```cmake
#[=============================================================================[
#                           Basic project definition                           #
]=============================================================================]
```

This format may be changed in the future once sphinx cmake documentation is
further developed.

More important here is the division of the sections that is documented here.

### Preamble

This is the part just before any actual section separation that has to be
defined for all CMake projects.

This section consists of:
- [`cmake_minimum_required`][]: Specify the minimum CMake version supported by
  the project. Should be covered by the CI, along with `latest` version.
- [`cmake_policy`][]: Allow for future CMake compatibility.

### Basic project definition

This section defines the main metadata of the project.

This section consists of:
- [`project`][]: Define main project metadata.
- [`CMAKE_<LANG>_STANDARD`] and equivalents: Specify the language standards used
  for the whole project. Should always be specified.

:::{warning}
Do **NOT** set [`CMAKE_<LANG>_STANDARD`] as a cached variable. This would affect
the values of other projects. Use a [project option] instead to re-define this
value.
:::

This is also where the [`CMAKE_MESSAGE_CONTEXT`] stack should be pushed onto.

### Options

It is preferred to have the options section within the main `CMakeLists.txt`
file, being as brief as possible, and with minimal logic.

This section consist of:
- [`option`][]: Define basic boolean options
- [`set(CACHE)`][]: Define non-boolean options
- [`cmake_dependent_option`][]: Define dependent boolean option

Further documentation of the options should be done in the sphinx documentation,
not in the `CMakeLists.txt` file.

### Project configuration

Here is where much of the CMake boilerplate configuration occurs, e.g. setting
[`BUILD_SHARED_LIBS`] variable locally according to the
[`<PROJECT>_SHARED_LIBS`] option.

This section should be as minimal as possible, having most of it deferred to
`src/CMakeLists.txt` and further on.

### External packages

Here is where all the required and optional dependencies are defined.

This section consist of:
- [`find_package`][]: Import system-installed packages
- [`FetchContent_Declare`][]: Define downloadable dependencies
- [`FetchContent_MakeAvailable`][]: Import the projects defined by the previous
  command
- [`feature_summary`] with `FATAL_ON_MISSING_REQUIRED_PACKAGES`: Make sure
  required dependencies defined in [`set_package_properties`] are treated
  properly

For readability, another call to [`feature_summary`] with `FILENAME` and `VAR`
should occur prior to that with [`cmake_language(DEFER)`] printing, as shown in
the template.

### Main definition

Here is where the exported targets are defined, along with their basic
properties. The main definition and linkage is deferred to the
`src/CMakeLists.txt` and further on.

This section consist of:
- [`add_library`][]: Create library targets
- [`add_executable`][]: Create executable targets
- [`set_target_properties`][]: Set basic target properties
- [`add_subdirectory`][]: Import the main CMake project definitions
- [`enable_testing`][]: Enable [`ctest`]

:::{attention}
Make sure [`enable_testing`] is called at this top-level, otherwise [`ctest`]
would not be executable in the build directory.
:::

Some target definitions can be deferred to a subproject if they are gated by a
project option, e.g. in the case of binding APIs.

### Install or Export

Finally, the install and export configurations are defined

This section consist of:
- [`install(FILE)`][]: Define the installed files. Primarily the files relevant
  for CMake package importing.
- [`install(EXPORT)`] and [`export(EXPORT)`][]: Define the component files for
  [`find_package`].
- [`configure_file`], [`write_basic_package_version_file`], and
  [`configure_package_config_file`][]: Configure the [`<Project>Config.cmake`]
  files
- [`return(PROPAGATE)`] or [`set(PARENT_SCOPE)`][]: Export the variables defined
  in [`<Project>Config.cmake`] for projects using [`FetchContent`] as well

More details can be found in the [export] section

[`cmake_minimum_required`]: inv:cmake:cmake:command#command:cmake_minimum_required
[`cmake_policy`]: inv:cmake:cmake:command#command:cmake_policy
[`project`]: inv:cmake:cmake:command#command:project
[`CMAKE_<LANG>_STANDARD`]: inv:cmake:cmake:variable#variable:CMAKE_<LANG>_STANDARD
[`option`]: inv:cmake:cmake:command#command:option
[`set(CACHE)`]: inv:cmake:cmake:command#command:set(cache)
[`cmake_dependent_option`]: inv:cmake:cmake:command#command:cmake_dependent_option
[`BUILD_SHARED_LIBS`]: inv:cmake:cmake:variable#variable:BUILD_SHARED_LIBS
[`find_package`]: inv:cmake:cmake:command#command:find_package
[`FetchContent_Declare`]: inv:cmake:cmake:command#command:fetchcontent_declare
[`FetchContent_MakeAvailable`]: inv:cmake:cmake:command#command:fetchcontent_makeavailable
[`feature_summary`]: inv:cmake:cmake:command#command:feature_summary
[`set_package_properties`]: inv:cmake:cmake:command#command:set_package_properties
[`cmake_language(DEFER)`]: inv:cmake:cmake:command#command:cmake_language(defer)
[`add_library`]: inv:cmake:cmake:command#command:add_library
[`add_executable`]: inv:cmake:cmake:command#command:add_executable
[`set_target_properties`]: inv:cmake:cmake:command#command:set_target_properties
[`add_subdirectory`]: inv:cmake:cmake:command#command:add_subdirectory
[`enable_testing`]: inv:cmake:cmake:command#command:enable_testing
[`ctest`]: inv:cmake:cmake:manual#manual:ctest(1)
[`install(FILE)`]: inv:cmake:cmake:command#command:install(files)
[`install(EXPORT)`]: inv:cmake:cmake:command#command:install(export)
[`configure_file`]: inv:cmake:cmake:command#command:configure_file
[`write_basic_package_version_file`]: inv:cmake:cmake:command#command:write_basic_package_version_file
[`configure_package_config_file`]: inv:cmake:cmake:command#command:configure_package_config_file
[`export(EXPORT)`]: inv:cmake:std:label#export(export)
[`<Project>Config.cmake`]: <inv:cmake:std:label#full signature>
[`return(PROPAGATE)`]: inv:cmake:cmake:command#command:return
[`set(PARENT_SCOPE)`]: inv:cmake:cmake:command#command:set(normal)
[`FetchContent`]: inv:cmake:cmake:module#module:FetchContent

[export]: TBD
[project option]: TBD
[`<PROJECT>_SHARED_LIBS`]: TBD
[`CMAKE_MESSAGE_CONTEXT`]: namespace.md#message
