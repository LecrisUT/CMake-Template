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

include(CMakeDependentOption)
include(FeatureSummary)

cmake_dependent_option(TEMPLATE_TEST_COVERAGE "Template: Test with coverage" OFF "TEMPLATE_TESTS;Template_IS_TOP_LEVEL" OFF)
add_feature_info(Coverage TEMPLATE_TEST_COVERAGE "Compile with test coverage")
mark_as_advanced(TEMPLATE_TEST_COVERAGE)

#[==============================================================================================[
#                                     Project configuration                                     #
]==============================================================================================]

include(FetchContent)

if (TEMPLATE_TEST_COVERAGE)
	target_compile_options(Template_Template PRIVATE --coverage)
	target_compile_options(Template_Hello PRIVATE --coverage)
	target_link_options(Template_Template PUBLIC --coverage)
endif ()

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

function(Template_add_test test)
	#[===[.md
	# Template_add_test

	Internal helper for adding functional tests specific for the current template project

	## Synopsis
	```cmake
	Template_add_test(<name>
			[TEST_NAME <test_name>]
			[TARGET <target>]
			[LABELS <label1> <label2>])
	```

	## Options

	`<name>`
	  Path to the CMake project to be executed relative to `${CMAKE_CURRENT_SOURCE_DIR}`

	`TEST_NAME` [Default: `<name>`]
	  Name for the test to be used as the ctest name

	`LABELS`
	  Additional labels to be added

	]===]

	list(APPEND CMAKE_MESSAGE_CONTEXT "Template_add_test")

	set(ARGS_Options)
	set(ARGS_OneValue
			TEST_NAME
	)
	set(ARGS_MultiValue
			LABELS
	)
	cmake_parse_arguments(PARSE_ARGV 1 ARGS "${ARGS_Options}" "${ARGS_OneValue}" "${ARGS_MultiValue}")
	# Check required/optional arguments
	if (ARGC LESS 1)
		message(FATAL_ERROR "Missing test name")
	endif ()
	if (NOT DEFINED ARGS_TEST_NAME)
		set(ARGS_TEST_NAME ${test})
	endif ()
	set(extra_args)
	if (Template_IS_TOP_LEVEL)
		list(APPEND extra_args
				-DFETCHCONTENT_TRY_FIND_PACKAGE_MODE=ALWAYS
				# Generated Config file point to binary targets until it is installed
				-DTemplate_ROOT=${Template_BINARY_DIR}
				-DFETCHCONTENT_SOURCE_DIR_TEMPLATE=${Template_SOURCE_DIR}
		)
	endif ()

	add_test(NAME ${ARGS_TEST_NAME}
			COMMAND ${CMAKE_CTEST_COMMAND} --build-and-test ${CMAKE_CURRENT_SOURCE_DIR}/${test}
			${CMAKE_CURRENT_BINARY_DIR}/${test}
			# Use the same build environment as the current runner
			--build-generator "${CMAKE_GENERATOR}"
			--build-options -DCMAKE_CXX_COMPILER=${CMAKE_CXX_COMPILER}
			${extra_args}
			--test-command ${CMAKE_CTEST_COMMAND} --test-dir ${CMAKE_CURRENT_BINARY_DIR}/${test} --output-on-failure
	)
	set_tests_properties(${ARGS_TEST_NAME} PROPERTIES
			LABELS "${ARGS_LABELS}"
	)
endfunction()

foreach (test_type IN ITEMS
		unit
		functional
		package
)
	add_subdirectory(${test_type})
endforeach ()

catch_discover_tests(test-suite)
