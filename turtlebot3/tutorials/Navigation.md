### Navigation
: 경로 계산, 장애물 회피, /cmd_vel 생성
#### 1. TurtleBot 3
```c
$ ssh ubuntu@{IP_ADDRESS_OF_RASPBERRY_IP}
$ export TURTLEBOT3_MODEL=${TB3_MODEL}
$ ros2 launch turtlebot3_bringup robot.launch.py
```
#### 2. 원격 PC
```c
$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_navigation2 navigation2.launch.py map:=$HOME/map.yaml
```
