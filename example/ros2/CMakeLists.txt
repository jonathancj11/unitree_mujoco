cmake_minimum_required(VERSION 3.5)
project(stand_go2)

message(STATUS "DEBUG: Iniciando configuración de CMake para el proyecto ${PROJECT_NAME}")

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
  message(STATUS "DEBUG: C standard establecido a C99")
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
  message(STATUS "DEBUG: C++ standard establecido a C++14")
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
  message(STATUS "DEBUG: Se han añadido las opciones de compilación: -Wall -Wextra -Wpedantic")
endif()

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)
message(STATUS "DEBUG: Se ha añadido el directorio de includes: ${CMAKE_CURRENT_SOURCE_DIR}/include")

link_directories(${CMAKE_CURRENT_SOURCE_DIR}/src)
message(STATUS "DEBUG: Se ha añadido el directorio de link: ${CMAKE_CURRENT_SOURCE_DIR}/src")

set(
  DEPENDENCY_LIST
  unitree_go
  rclcpp
  std_msgs
)
message(STATUS "DEBUG: Lista de dependencias: ${DEPENDENCY_LIST}")

# Buscar dependencias
message(STATUS "DEBUG: Buscando dependencias con ament_cmake...")
find_package(ament_cmake REQUIRED)
message(STATUS "DEBUG: ament_cmake encontrado")

find_package(unitree_go REQUIRED)
message(STATUS "DEBUG: unitree_go encontrado")

find_package(unitree_api REQUIRED)
message(STATUS "DEBUG: unitree_api encontrado")

find_package(rclcpp REQUIRED)
message(STATUS "DEBUG: rclcpp encontrado")

find_package(std_msgs REQUIRED)
message(STATUS "DEBUG: std_msgs encontrado")

find_package(rosbag2_cpp REQUIRED)
message(STATUS "DEBUG: rosbag2_cpp encontrado")

# Agregar ejecutable
add_executable(stand_go2 src/stand_go2.cpp src/motor_crc.cpp)
message(STATUS "DEBUG: Ejecutable 'stand_go2' agregado con las fuentes: src/stand_go2.cpp y src/motor_crc.cpp")

ament_target_dependencies(stand_go2 ${DEPENDENCY_LIST})
message(STATUS "DEBUG: Dependencias de 'stand_go2' configuradas: ${DEPENDENCY_LIST}")

# Instalar binario en "lib/stand_go2/"
install(
  TARGETS stand_go2
  DESTINATION lib/${PROJECT_NAME}
)
message(STATUS "DEBUG: Configurada la instalación del ejecutable 'stand_go2' en lib/${PROJECT_NAME}")

# Asegurar que "package.xml" se copie a "share/stand_go2/package.xml"
install(
  FILES package.xml
  DESTINATION share/${PROJECT_NAME}
)
message(STATUS "DEBUG: Configurada la instalación de package.xml en share/${PROJECT_NAME}")

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
  message(STATUS "DEBUG: Dependencias para testing encontradas mediante ament_lint_auto")
endif()

ament_package()
message(STATUS "DEBUG: Configuración de CMake finalizada para el proyecto ${PROJECT_NAME}")
