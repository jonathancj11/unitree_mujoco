cmake_minimum_required(VERSION 3.5)
project(unitree_mujoco)

# --- Mensajes iniciales de depuración ---
message(STATUS "DEBUG: Iniciando configuración del proyecto ${PROJECT_NAME}")
message(STATUS "DEBUG: Directorio fuente: ${CMAKE_CURRENT_SOURCE_DIR}")
message(STATUS "DEBUG: Directorio binario: ${CMAKE_CURRENT_BINARY_DIR}")

# --- Configuración de políticas de CMake ---
cmake_policy(SET CMP0015 NEW)
cmake_policy(SET CMP0081 NEW)
message(STATUS "DEBUG: Políticas CMP0015 y CMP0081 establecidas en NEW")

# --- Buscar la dependencia principal ---
message(STATUS "DEBUG: Buscando ament_cmake...")
find_package(ament_cmake REQUIRED)
message(STATUS "DEBUG: ament_cmake encontrada")

# Si necesitas dependencias adicionales (por ejemplo, rclcpp, std_msgs), descomenta y agrega:
# message(STATUS "DEBUG: Buscando rclcpp...")
# find_package(rclcpp REQUIRED)
# message(STATUS "DEBUG: rclcpp encontrada")
# message(STATUS "DEBUG: Buscando std_msgs...")
# find_package(std_msgs REQUIRED)
# message(STATUS "DEBUG: std_msgs encontrada")

# --- Instalación de la carpeta launch/ ---
message(STATUS "DEBUG: Configurando la instalación de la carpeta 'launch/' en share/${PROJECT_NAME}")
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)
message(STATUS "DEBUG: Carpeta 'launch/' instalada en share/${PROJECT_NAME}")

# --- Instalación del package.xml ---
message(STATUS "DEBUG: Configurando la instalación del 'package.xml' en share/${PROJECT_NAME}")
install(
  FILES package.xml
  DESTINATION share/${PROJECT_NAME}
)
message(STATUS "DEBUG: Archivo 'package.xml' instalado en share/${PROJECT_NAME}")

# --- Finalización del paquete ament ---
ament_package()
message(STATUS "DEBUG: ament_package() completado para ${PROJECT_NAME}")

