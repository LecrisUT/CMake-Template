cmake_minimum_required(VERSION 3.20)

#[==============================================================================================[
#                                   Basic project definition                                   #
]==============================================================================================]

list(APPEND CMAKE_MESSAGE_CONTEXT Test)
project(Template_test)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS ON)

#[==============================================================================================[
#                                            Options                                            #
]==============================================================================================]

#[==============================================================================================[
#                                     Project configuration                                     #
]==============================================================================================]

include(FetchContent)

#[==============================================================================================[
#                                       External packages                                       #
]==============================================================================================]

set(external_libs)
if (NOT Template_IS_TOP_LEVEL)
	FetchContent_Declare(Template
			GIT_REPOSITORY https://github.com/LecrisUT/CMake-Template
			GIT_TAG main
			FIND_PACKAGE_ARGS CONFIG
	)
	list(APPEND external_libs Template)
endif ()
FetchContent_Declare(Catch2
		GIT_REPOSITORY https://github.com/catchorg/Catch2
		GIT_TAG v3.4.0
		FIND_PACKAGE_ARGS CONFIG
)
list(APPEND external_libs Catch2)

FetchContent_MakeAvailable(${external_libs})

#[==============================================================================================[
#                                        Main definition                                        #
]==============================================================================================]

enable_testing()
include(Catch)

add_executable(test-suite)
target_link_libraries(test-suite PRIVATE Catch2::Catch2WithMain Template::Template)

add_subdirectory(unit)
add_subdirectory(package)

catch_discover_tests(test-suite)
