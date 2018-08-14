{%- set target_name = cookiecutter.project_slug.replace('-', '_') + "_main" -%}

add_executable({{ target_name }} main.cpp)
target_link_libraries({{ target_name }}
    PRIVATE
        {{ cookiecutter.project_slug | replace('-', '_') }}
)

install(TARGETS {{ target_name }}
    RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}"
)
