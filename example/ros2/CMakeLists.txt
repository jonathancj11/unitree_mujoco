cmake_minimum_required(VERSION 3.5)
project(stand_go2)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

include_directories(include)
link_directories(src)

set (
  DEPENDENCY_LIST
  unitree_go
  rclcpp
  std_msgs
)

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(unitree_go REQUIRED)
find_package(unitree_api REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rosbag2_cpp REQUIRED)

add_executable(stand_go2 src/stand_go2.cpp src/motor_crc.cpp)

ament_target_dependencies(stand_go2 ${DEPENDENCY_LIST})

# Instalar binario en "lib/stand_go2/"
install(
  TARGETS stand_go2
  DESTINATION lib/${PROJECT_NAME}
)

# Asegurar que "package.xml" se copie a "share/stand_go2/package.xml"
install(
  FILES package.xml
  DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()