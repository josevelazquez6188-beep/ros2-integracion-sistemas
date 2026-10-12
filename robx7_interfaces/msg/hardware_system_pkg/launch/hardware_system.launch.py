
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='hardware_system_pkg',
            executable='hardware_emulator',
            name='hardware_emulator',
            output='screen'
        ),
        Node(
            package='hardware_system_pkg',
            executable='monitor_node',
            name='monitor_node',
            output='screen',
            parameters=[{
                'umbral_temperatura': 75
            }]
        ),
        Node(
            package='hardware_system_pkg',
            executable='operator_node',
            name='operator_node',
            output='screen'
        ),
    ])
