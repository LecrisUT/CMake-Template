cmake_minimum_required(VERSION 3.20...3.29)
project(example_spglib LANGUAGES CXX)

find_package(PkgConfig REQUIRED)
pkg_check_modules(Template REQUIRED IMPORTED_TARGET template)

add_executable(main main.cpp)
target_link_libraries(main PRIVATE PkgConfig::Template)

enable_testing()
add_test(NAME smoke_test
		COMMAND $<TARGET_FILE:main>
)
set_tests_properties(smoke_test PROPERTIES
		PASS_REGULAR_EXPRESSION "^Hello, World!"
)
