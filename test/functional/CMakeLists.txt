set_property(DIRECTORY APPEND
		PROPERTY LABELS functional
)
add_test(NAME test-functional
		COMMAND $<TARGET_FILE:Template::Hello>
)
set_tests_properties(test-functional PROPERTIES
		PASS_REGULAR_EXPRESSION "^Hello, World!"
)
