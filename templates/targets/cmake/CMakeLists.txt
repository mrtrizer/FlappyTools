cmake_minimum_required(VERSION 2.8)

project({!name!})

set(CMAKE_BUILD_TYPE Debug)

add_definitions("-std=c++1y")
include_directories("./src/" "../../src/")
add_subdirectory(../../engine engine)

file(GLOB SOURCES src/*.cpp ../../src/*.cpp ./*.cpp)

set(EXECUTABLE_NAME {!cmake.exec_name!})

add_executable(${EXECUTABLE_NAME} ${SOURCES})

target_link_libraries(${EXECUTABLE_NAME} FlappyEngine)

add_custom_command(TARGET ${EXECUTABLE_NAME}
        PRE_BUILD
        COMMAND flappy prebuild cmake
        COMMAND cp ${CMAKE_CURRENT_LIST_DIR}/res ${CMAKE_BINARY_DIR} -R
)

find_package(PNG)
find_package(SDL_image)

if (PNG_FOUND)
    add_definitions(-DPNG_FOUND)
endif()

if (SDL_IMAGE_FOUND)
    add_definitions(-DSDL_IMAGE_FOUND)
endif()
