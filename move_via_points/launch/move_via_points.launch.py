from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='move_via_points',
            executable='nav2_move_via_points',
            name='nav2_move_via_points',
            output='screen'
        )
    ])