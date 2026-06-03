### SLAM
: ~/.bashrc 에 저장
```c
$ nano ~/.bashrc
export TURTLEBOT3_MODEL=burger
```
#### 1. TurtleBot3 Bringup 실행
> 1. bringup
```c
$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_bringup robot.launch.py
```
#### 2. 원격 PC SLAM 노드 실행
```c
$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_cartographer cartographer.launch.py
```
