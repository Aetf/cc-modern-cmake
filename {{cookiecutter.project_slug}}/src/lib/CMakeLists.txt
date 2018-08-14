{%- set target_name = cookiecutter.project_slug.replace('-', '_') -%}
set({{ target_name }}_SRCS
    {{ cookiecutter.project_slug }}.cpp
)

include_directories("${PROJECT_SOURCE_DIR}/include")

add_library({{ target_name }}_static STATIC ${ {{- target_name }}_SRCS})
set_target_properties({{ target_name }}_static PROPERTIES
    OUTPUT_NAME {{ cookiecutter.project_slug }}
    PUBLIC_HEADER "${PROJECT_SOURCE_DIR}/include/{{ cookiecutter.project_slug }}/{{ cookiecutter.project_slug }}.h"
)
target_compile_options({{ target_name }}_static
    PUBLIC
        -fexceptions
)

add_library({{ target_name }} SHARED ${ {{- target_name }}_SRCS})
set_target_properties({{ target_name }} PROPERTIES
    VERSION "${PROJECT_VERSION}"
    SOVERSION "${PROJECT_VERSION_MAJOR}"
    PUBLIC_HEADER "${PROJECT_SOURCE_DIR}/include/{{ cookiecutter.project_slug }}/{{ cookiecutter.project_slug }}.h"
)
target_compile_options({{ target_name }}
    PUBLIC
        -fexceptions
)

install(TARGETS {{ target_name }} {{ target_name }}_static
    LIBRARY DESTINATION "${CMAKE_INSTALL_LIBDIR}"
    ARCHIVE DESTINATION "${CMAKE_INSTALL_LIBDIR}"
    PUBLIC_HEADER DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/{{ cookiecutter.project_slug }}"
)
