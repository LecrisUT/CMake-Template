# Minimum version follows the current Ubuntu LTS and RHEL version
cmake_minimum_required(VERSION 3.20)
# CMake version compatibility. This allows to future-proof implementations and easily update
# when bumping cmake_minimum_required

#[==============================================================================================[
#                                   Basic project definition                                   #
]==============================================================================================]

list(APPEND CMAKE_MESSAGE_CONTEXT Template)
project(Template
		VERSION 0.1.0
		DESCRIPTION "CMake project template"
		HOMEPAGE_URL https://github.com/LecrisUT/CMake-Template
		LANGUAGES CXX
)

# Back-porting to PROJECT_IS_TOP_LEVEL to older cmake
# TODO: Remove when requiring cmake >= 3.21
if (NOT DEFINED Template_IS_TOP_LEVEL)
	if (CMAKE_PROJECT_NAME STREQUAL PROJECT_NAME)
		set(PROJECT_IS_TOP_LEVEL ON)
	else ()
		set(PROJECT_IS_TOP_LEVEL OFF)
	endif ()
	set(Template_IS_TOP_LEVEL ${PROJECT_IS_TOP_LEVEL})
endif ()

# Specify C++ standard used in the project.
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS ON)

#[==============================================================================================[
#                                            Options                                            #
]==============================================================================================]

include(CMakeDependentOption)
include(FeatureSummary)

option(TEMPLATE_TESTS "Template: Build test-suite" ${PROJECT_IS_TOP_LEVEL})
option(TEMPLATE_SHARED_LIBS "Template: Build as a shared library" ${PROJECT_IS_TOP_LEVEL})
option(TEMPLATE_INSTALL "Template: Install project" ${PROJECT_IS_TOP_LEVEL})


#[==============================================================================================[
#                                     Project configuration                                     #
]==============================================================================================]

list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)

# Include basic tools
include(FetchContent)
if (TEMPLATE_INSTALL)
	include(CMakePackageConfigHelpers)
	if (UNIX)
		include(GNUInstallDirs)
	endif ()
endif ()

# Define basic parameters
if (NOT CMAKE_BUILD_TYPE)
	set(CMAKE_BUILD_TYPE Release)
endif ()
set(BUILD_SHARED_LIBS ${TEMPLATE_SHARED_LIBS})

#[==============================================================================================[
#                                       External packages                                       #
]==============================================================================================]

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

#[==============================================================================================[
#                                        Main definition                                        #
]==============================================================================================]

# Main project

#[==============================================================================================[
#                                       Install or Export                                       #
]==============================================================================================]
