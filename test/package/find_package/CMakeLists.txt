cmake_minimum_required(VERSION 3.20)
project(example_spglib LANGUAGES CXX)

find_package(Template REQUIRED CONFIG)

add_executable(main main.cpp)
target_link_libraries(main PRIVATE Template::Template)

enable_testing()
add_test(NAME smoke_test
		COMMAND $<TARGET_FILE:main>
)
set_tests_properties(smoke_test PROPERTIES
		PASS_REGULAR_EXPRESSION "^Hello, World!"
)
