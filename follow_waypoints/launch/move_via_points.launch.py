from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='follow_waypoints',
            executable='nav2_move_via_points',
            name='nav2_move_via_points',
            output='screen'
        )
    ])
