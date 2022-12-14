from setuptools import setup
import os
from glob import glob

package_name = 'follow_waypoints'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='fulltimerobotics',
    maintainer_email='fulltimerobotics@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'nav2_follow_waypoints = follow_waypoints.nav2_follow_waypoints:main',
            'nav2_move_via_points = follow_waypoints.nav2_move_via_points:main'
        ],
    },
)
