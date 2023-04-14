### PDE4430_mobile_robotics_CW-2-ROBO

Objective:

To create a mobile robot that can operate in either autonomous or teleoperator modes to move three distinct spheres inside the "pen" created by two walls.The robot must be able to move and interact with objects in the simulation and have a URDF file loaded into Gazebo with all the essential parameters established in order to perform the job or demonstrate that it could be achieved.

## Model of Robot
A robot with two wheels and a connected body with two hands is created.

## How to use this Repository
* Move into your workspace/src folder
```
 cd path/to/workspace/src/
 Example: cd ~/catkin_ws/src/
```

* Cloning the complete project in the workspace- This will help to extract all files related to your local machine
```
git clone https://github.com/MEGHA-MURALI/PDE4430_mobile_robotics_CW-2-ROBO
```

* Perform make and build through catkin
 ```
 catkin_make
 ```
 
 * Whenever you open a terminal, source your workspace. Run files from this workspace 
```
source /path/to/catkin-ws/devel/setup.bash
```

* Launch robo(URDF file) in Gazebo world and using teleop script we can move the robot
```
roslaunch robo robo.launch
```

```
roslaunch robo robo_gazebo.launch 
```
```
roslaunch robo robo_gazebo_teleop.launch 
```
## Demo Link

https://www.youtube.com/watch?v=47zv0VHdHwc

## Reference:

http://wiki.ros.org/urdf/Tutorials
