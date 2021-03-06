cmake_minimum_required(VERSION 3.7...3.21)
project(2048 LANGUAGES CXX)
enable_testing()

set(SOURCES src/2048.cpp src/gameboard.cpp src/gameboard-graphics.cpp src/game.cpp src/game-graphics.cpp src/game-input.cpp src/game-pregamemenu.cpp src/global.cpp src/loadresource.cpp src/menu.cpp src/menu-graphics.cpp src/saveresource.cpp src/scores.cpp src/scores-graphics.cpp src/statistics.cpp src/statistics-graphics.cpp src/tile.cpp src/tile-graphics.cpp)

if(CMAKE_CXX_COMPILER_ID STREQUAL GNU)
  string(APPEND CMAKE_CXX_FLAGS " -Wall")
elseif(CMAKE_CXX_COMPILER_ID STREQUAL Clang)
  string(APPEND CMAKE_CXX_FLAGS " -Wall")
elseif(CMAKE_CXX_COMPILER_ID MATCHES "^Intel")
  if(WIN32)
    string(APPEND CMAKE_CXX_FLAGS " /W3")
  else()
    string(APPEND CMAKE_CXX_FLAGS " -w2")
  endif()
elseif(CMAKE_CXX_COMPILER_ID STREQUAL NVHPC)
  string(APPEND CMAKE_CXX_FLAGS " -a")
endif()

add_executable(2048 ${SOURCES})
target_include_directories(2048 PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/src/headers/)
target_compile_features(2048 PRIVATE cxx_std_14)

# --- test

find_program(PWSH NAMES pwsh powershell)
if(PWSH)
  add_test(NAME basic COMMAND ${PWSH} -c \"echo 4 | $<TARGET_FILE:2048>\")
elseif(UNIX)
  add_test(NAME basic COMMAND sh -c "echo 4 | $<TARGET_FILE:2048>")
endif()

# --- install

install(TARGETS 2048
  RUNTIME DESTINATION bin)

install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/data
        DESTINATION ${CMAKE_INSTALL_PREFIX})
