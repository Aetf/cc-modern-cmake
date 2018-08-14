set(unittest_SRCS
    test_{{ cookiecutter.project_slug }}.cpp
)

set(unittest_LIBRARIES
    {% if cookiecutter.with_qt -%}
    Qt5::Test
    {%- endif %}
)

# The Catch2 test runner
add_executable(unittests main.cpp ${unittest_SRCS})
target_link_libraries(unittests
    Catch2::Catch2
    ${unittest_LIBRARIES}
)
catch_discover_tests(unittests)
