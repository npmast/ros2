#### 1. 직진성 확인
##### 1. turtlebot3
```c
$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_bringup robot.launch.py
```
##### 2. 원격 PC
> * 1m 이동:
> 거리 = 속도 x 시간 = 0.1 m/s x 10sec = 1m  
> * x: 0.1 은 1초에 10cm 이동을 나타낸다.
```c
- 10cm 이동
ros2 topic pub --once /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.1}, angular: {z: 0.0}}"
- 1m 이동
ros2 topic pub -r 10 /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.1}, angular: {z: 0.0}}"
- stop
ros2 topic pub --once /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.0}, angular: {z: 0.0}}"
```
#### 2. 오도메트리 튜닝
##### 1. 1m 이동
```c
ros2 topic pub --once /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.1}, angular: {z: 0.0}}"
```
