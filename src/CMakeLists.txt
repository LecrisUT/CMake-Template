target_sources(Template_Hello PRIVATE
		main.cpp
)
target_sources(Template_Template PRIVATE
		template.cpp
)

target_link_libraries(Template_Template PRIVATE fmt::fmt)
target_link_libraries(Template_Hello PRIVATE Template_Template)
set_target_properties(Template_Template PROPERTIES
		PUBLIC_HEADER template.h
)
target_include_directories(Template_Template PUBLIC
		"$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>"
		"$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>"
)

if (TEMPLATE_INSTALL)
	install(TARGETS Template_Hello
			EXPORT TemplateTargets
			RUNTIME COMPONENT Template_Runtime
	)
	install(TARGETS Template_Template
			EXPORT TemplateTargets
			LIBRARY COMPONENT Template_Runtime NAMELINK_COMPONENT Template_Development
			ARCHIVE COMPONENT Template_Development
			PUBLIC_HEADER COMPONENT Template_Development
			RUNTIME COMPONENT Template_Runtime
	)
endif ()
