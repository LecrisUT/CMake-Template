cmake_minimum_required(VERSION 3.25...3.29)
project(example_spglib LANGUAGES CXX)

find_package(Template REQUIRED CONFIG)

# Make sure the executable is runnable after the pip install
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH True)

add_executable(main main.cpp)
target_link_libraries(main PRIVATE Template::Template)

install(TARGETS main DESTINATION ${SKBUILD_SCRIPTS_DIR})
