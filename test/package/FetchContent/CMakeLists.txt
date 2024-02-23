cmake_minimum_required(VERSION 3.20...3.29)
project(example_spglib LANGUAGES CXX)

include(FetchContent)

if (DEFINED ENV{PACKIT_SOURCE_URL})
	set(git_repo $ENV{PACKIT_SOURCE_URL})
else ()
	set(git_repo https://github.com/LecrisUT/CMake-Template)
endif ()
if (DEFINED ENV{PACKIT_SOURCE_SHA})
	set(git_tag $ENV{PACKIT_SOURCE_SHA})
elseif (DEFINED ENV{PACKIT_COMMIT_SHA})
	set(git_tag $ENV{PACKIT_COMMIT_SHA})
else ()
	set(git_tag main)
endif ()

FetchContent_Declare(Template
		GIT_REPOSITORY ${git_repo}
		GIT_TAG ${git_tag}
)
FetchContent_MakeAvailable(Template)

add_executable(main main.cpp)
target_link_libraries(main PRIVATE Template::Template)

enable_testing()
add_test(NAME smoke_test
		COMMAND $<TARGET_FILE:main>
)
set_tests_properties(smoke_test PROPERTIES
		PASS_REGULAR_EXPRESSION "^Hello, World!"
)
