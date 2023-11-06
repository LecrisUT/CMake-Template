#[===[.md
# Findfmt

fmt compatibility module for Octopus

This file is specifically tuned for Template usage to unify the api with upstream package.

]===]

list(APPEND CMAKE_MESSAGE_CONTEXT Findfmt)
include(Template_Helpers)
Template_FindPackage(${CMAKE_FIND_PACKAGE_NAME}
		NAMES fmt
		PKG_MODULE_NAMES fmt
)

# Create appropriate aliases
if (${CMAKE_FIND_PACKAGE_NAME}_PKGCONFIG)
	add_library(fmt::fmt ALIAS PkgConfig::${CMAKE_FIND_PACKAGE_NAME})
endif ()
set_package_properties(${CMAKE_FIND_PACKAGE_NAME} PROPERTIES
		URL https://github.com/fmtlib/fmt
		DESCRIPTION "A modern formatting library "
)
list(POP_BACK CMAKE_MESSAGE_CONTEXT)
