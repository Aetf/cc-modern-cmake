cmake_minimum_required(VERSION 3.11)

project({{ cookiecutter.project_slug }} LANGUAGES C CXX)
set(PROJECT_VERSION "{{ cookiecutter.version }}")

#---------------------------------------------------------------------------------------
# Initial setups
#---------------------------------------------------------------------------------------
# Include utilities
include(cmake/Utilities.cmake)
list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)
# For feature_summary
include(FeatureSummary)

# Setup defaults
include(cmake/Defaults.cmake)
# Extra build types
include(cmake/BuildTypes.cmake)

#---------------------------------------------------------------------------------------
# Options
#---------------------------------------------------------------------------------------
option(BUILD_TESTING "Build test suite in default target" OFF)
add_feature_info(Tests BUILD_TESTING "build unit tests")

#---------------------------------------------------------------------------------------
# Find packages
#---------------------------------------------------------------------------------------
# Extra cmake helpers
find_package(ECM REQUIRED NO_MODULE)
list(APPEND CMAKE_MODULE_PATH ${ECM_MODULE_PATH})
include(ECMQtDeclareLoggingCategory)
include(ECMInstallIcons)
include(GNUInstallDirs)

{% if cookiecutter.with_qt %}
set(QT5_COMPONENTS Core Gui)
if(BUILD_TESTING)
    list(APPEND QT5_COMPONENTS Test)
endif(BUILD_TESTING)
find_package(Qt5 5.10 CONFIG REQUIRED COMPONENTS ${QT5_COMPONENTS})
{% endif %}

# Bundled thirdparty code
add_subdirectory(thirdparty)

feature_summary(INCLUDE_QUIET_PACKAGES FATAL_ON_MISSING_REQUIRED_PACKAGES WHAT ALL)

#---------------------------------------------------------------------------------------
# Set compiler options and detect features
#---------------------------------------------------------------------------------------
# Only set compile options after any inclusion of third party code
include(cmake/CompileOptions.cmake)

add_subdirectory(src)

if(BUILD_TESTING)
    add_subdirectory(tests)
endif(BUILD_TESTING)
