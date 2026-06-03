### SLAM
#### 1. TurtleBot3
> 1. bringup
```c
$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_bringup robot.launch.py
```
#### 2. 원격 PC
```c
$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_cartographer cartographer.launch.py
```
