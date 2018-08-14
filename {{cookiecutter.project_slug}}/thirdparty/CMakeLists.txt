set(third_party_dir ${CMAKE_CURRENT_LIST_DIR})

# make sure all dependencies are build in Release mode
set(CMAKE_BUILD_TYPE Release)

if(BUILD_TESTING)
    # Catch2
    include(UseCatch2.cmake)
endif(BUILD_TESTING)
