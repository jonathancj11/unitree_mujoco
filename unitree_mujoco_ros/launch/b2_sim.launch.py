# b2_sim.launch.py
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['/opt/unitree_mujoco/simulate/build/unitree_mujoco']
            output='screen'
        )
    ])
