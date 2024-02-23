# Minimum version follows the current Ubuntu LTS and RHEL version
cmake_minimum_required(VERSION 3.25...3.29)

#[=============================================================================[
#                           Basic project definition                           #
]=============================================================================]

list(APPEND CMAKE_MESSAGE_CONTEXT Template)
project(Template
		VERSION 0.1.0
		DESCRIPTION "CMake project template"
		HOMEPAGE_URL https://github.com/LecrisUT/CMake-Template
		LANGUAGES CXX
)

# Specify C++ standard used in the project.
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS ON)

#[=============================================================================[
#                                   Options                                   #
]=============================================================================]

include(CMakeDependentOption)
include(FeatureSummary)

option(TEMPLATE_TESTS "Template: Build test-suite" ${PROJECT_IS_TOP_LEVEL})
option(TEMPLATE_SHARED_LIBS "Template: Build as a shared library" ${PROJECT_IS_TOP_LEVEL})
option(TEMPLATE_INSTALL "Template: Install project" ${PROJECT_IS_TOP_LEVEL})


#[=============================================================================[
#                            Project configuration                            #
]=============================================================================]

list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)

# Include basic tools
include(FetchContent)
include(CMakePackageConfigHelpers)
include(GNUInstallDirs)

# Define basic parameters
if (NOT CMAKE_BUILD_TYPE)
	set(CMAKE_BUILD_TYPE Release)
endif ()
set(BUILD_SHARED_LIBS ${TEMPLATE_SHARED_LIBS})

#[=============================================================================[
#                              External packages                              #
]=============================================================================]

FetchContent_Declare(fmt
		GIT_REPOSITORY https://github.com/fmtlib/fmt
		GIT_TAG master
		FIND_PACKAGE_ARGS MODULE
)

FetchContent_MakeAvailable(fmt)

feature_summary(
		FILENAME ${CMAKE_CURRENT_BINARY_DIR}/Template.info
		VAR Template_Info
		DESCRIPTION "Template features and external libraries"
		FATAL_ON_MISSING_REQUIRED_PACKAGES
		WHAT ALL
)

# Report configuration
message(STATUS "Build type: ${CMAKE_BUILD_TYPE}")
message(STATUS ${Template_Info})

#[=============================================================================[
#                               Main definition                               #
]=============================================================================]

# Main project
add_executable(Template_Hello)
set_target_properties(Template_Hello PROPERTIES
		EXPORT_NAME Hello
		OUTPUT_NAME hello
)
add_executable(Template::Hello ALIAS Template_Hello)
add_library(Template_Template)
set_target_properties(Template_Template PROPERTIES
		VERSION ${PROJECT_VERSION}
		SOVERSION ${PROJECT_VERSION_MAJOR}
		EXPORT_NAME Template
		OUTPUT_NAME template
)
add_library(Template::Template ALIAS Template_Template)
# Main definitions inside src
add_subdirectory(src)

# Testing
if (TEMPLATE_TESTS)
	enable_testing()
	add_subdirectory(test)
endif ()

#[=============================================================================[
#                              Install or Export                              #
]=============================================================================]

# Installation
if (TEMPLATE_INSTALL)
	# pkg-config files
	configure_file(cmake/template.pc.in template.pc @ONLY)
	install(FILES ${CMAKE_CURRENT_BINARY_DIR}/template.pc
			DESTINATION ${CMAKE_INSTALL_LIBDIR}/pkgconfig
			COMPONENT Template_Development
	)

	# cmake export files
	write_basic_package_version_file(
			${CMAKE_CURRENT_BINARY_DIR}/TemplateConfigVersion.cmake
			VERSION ${PROJECT_VERSION}
			COMPATIBILITY SameMajorVersion
	)
	configure_package_config_file(
			cmake/TemplateConfig.cmake.in
			${CMAKE_CURRENT_BINARY_DIR}/TemplateConfig.cmake
			INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/Template
	)
	install(FILES ${CMAKE_CURRENT_BINARY_DIR}/TemplateConfigVersion.cmake
			${CMAKE_CURRENT_BINARY_DIR}/TemplateConfig.cmake
			DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/Template
			COMPONENT Template_Development
	)

	export(EXPORT TemplateTargets
			FILE TemplateTargets.cmake
			NAMESPACE Template::
	)
	install(EXPORT TemplateTargets
			FILE TemplateTargets.cmake
			NAMESPACE Template::
			DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/Template
			COMPONENT Template_Development
	)
endif ()

# Make project available for FetchContent
if(NOT PROJECT_IS_TOP_LEVEL)
	# Propagate variables
	return(PROPAGATE
			Template_VERSION
			Template_VERSION_MAJOR
			Template_VERSION_MINOR
			Template_VERSION_PATCH
			Template_VERSION_TWEAK
	)
endif ()
