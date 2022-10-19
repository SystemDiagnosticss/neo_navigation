# neo_navigation

This repository contains the ROS packages for navigate TurtleBot3 in a figure-8 pattern with Simple Commander API in two scenarios follow waypoints and move through poses. This is used to demonstrate different robotic behavior in these two cases.

## Prerequisites
1. Ubuntu 20.04
2. Python 3.8
3. ROS Galactic

### Required ROS packages
- ros-galactic-navigation2
- ros-galactic-nav2-bringup
- ros-galactic-turtlebot3*

## Development

### Setup
neo_navigation packages use colcon for building code. So first of all you need to prepare colcon workspace:

```
$ mkdir -p ros2_ws/src
$ cd ros2_ws/src
$ cd ..
$ colcon build
```

Now you need to source the `setup.bash` by previous build.

```
$ source ~/ros2_ws/install/setup.bash
```

It is recommended to add a corresponding line to .bashrc to source required environment automatically.
Also export turtlebot3 model and add Gazebo models path for simulation. 

```
export TURTLEBOT3_MODEL=waffle
$ export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/<ros2-distro>/share/turtlebot3_gazebo/models
```

### Build

Clone `neo_navigation` repository into catkin_ws/src directory and execute `colcon build` in the root of catkin workspace:

```
$ cd ros2_ws/src
$ git clone https://github.com/SystemDiagnosticss/neo_navigation
$ cd ..
$ colcon build
```

### Run Gazebo simulation 

Run Turtlebot3 simulation in Gazebosim in headless mode

```
$ ros2 launch nav2_bringup tb3_simulation_launch.py headless:=True
```

Scenario 1: Launch follow_waipoints for moving via points with pause in every points

```
$ ros2 launch follow_waypoints follow_waypoints.launch.py
```

Scenario 2: Launch follow_waipoints for moving via points without pause and path smoothing.

```
$ ros2 launch follow_waypoints move_via_points.launch.py
```

