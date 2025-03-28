cmake_minimum_required(VERSION 3.5)
project(unitree_mujoco)  # <-- este nombre define el nombre del paquete

find_package(ament_cmake REQUIRED)
# Si necesitas depender de rclcpp, sensor_msgs, etc., añádelos:
# find_package(rclcpp REQUIRED)
# find_package(std_msgs REQUIRED)

# Instala la carpeta launch/ y su contenido
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

# Instalar el package.xml
install(
  FILES package.xml
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
