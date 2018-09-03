cmake_minimum_required(VERSION 3.5.1)
project(multiThreadSocketServer)

set(CMAKE_CXX_STANDARD 11)

include_directories(
        include
)

add_library(socketpp
        src/socketpp/socketpp.cpp
        include/socketpp/socketpp.hpp
        )

add_library(tcp-server
        src/tcp-server/tcp-server.cpp
        include/tcp-server/tcp-server.hpp
)

target_link_libraries(tcp-server
        pthread
        socketpp
)

add_executable(multiThreadSocketServer src/main.cpp)
target_link_libraries(multiThreadSocketServer tcp-server)
