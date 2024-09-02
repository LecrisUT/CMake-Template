cmake_minimum_required(VERSION 3.25...3.29)
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
if (CMAKE_VERSION VERSION_GREATER_EQUAL 3.27)
    # https://stackoverflow.com/a/77990416
    set_property(TEST smoke_test APPEND PROPERTY
            ENVIRONMENT_MODIFICATION "PATH=path_list_prepend:$<JOIN:$<TARGET_RUNTIME_DLL_DIRS:main>,\;>"
    )
endif ()
