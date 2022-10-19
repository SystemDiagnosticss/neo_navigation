from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    return LaunchDescription([
        Node(
            package='follow_waypoints',
            executable='nav2_follow_waypoints',
            name='nav2_follow_waypoints',
            output='screen'        )
    ])
