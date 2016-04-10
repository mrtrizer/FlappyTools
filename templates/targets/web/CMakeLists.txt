cmake_minimum_required(VERSION 2.8)

project(TestTest)

set(CMAKE_BUILD_TYPE Debug)

add_definitions("-std=c++1y")
include_directories("./src/" "../../src/")
add_subdirectory(../../engine engine)

file(GLOB SOURCES src/*.cpp ../../src/*.cpp ./*.cpp)

set(EXECUTABLE_NAME {!cmake.exec_name!})

add_executable(${EXECUTABLE_NAME} ${SOURCES})

target_link_libraries(${EXECUTABLE_NAME} FlappyEngine)

file(COPY res DESTINATION ${CMAKE_BINARY_DIR})

find_package(SDL_image)

add_definitions(-DSDL_IMAGE_FOUND)
