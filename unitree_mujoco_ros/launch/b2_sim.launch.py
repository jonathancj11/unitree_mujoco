# b2_sim.launch.py
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    # Aquí asumimos que el binario se llama "simulate_b2" 
    # o algo así, y está en /opt/unitree_mujoco/simulate/build
    # ajusta la ruta según tu binario real
    return LaunchDescription([
        ExecuteProcess(
            cmd=['/opt/unitree_mujoco/simulate/build/simulate_b2'],  # ajusta el nombre real
            output='screen'
        )
    ])
