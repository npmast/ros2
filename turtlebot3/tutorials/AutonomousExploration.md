### Autonomous Exploration
> Frontier 탐색 알고리즘
> 가장 가까운 Frontier 1개를 찾아 Nab2 Goal로 보낸다.
> 즉 Free(백색) 격자와 Unknown(회색) 격자가 맞닿는 경계점(Frontier)들을 찾아 목표점을 설정하고 목적지로 이동, 스캔하여 지도를 업데이트 한다.
> ```c
> 100 : 장애물
> 0 : 빈 공간
> -1 : 미 탐색
> ```
#### 1. 패키지 만들기
```c
$ ~/ros2_ws/src
$ ros2 pkg create --build-type ament_python frontier_explorer
```
#### 1. SBC bringup
```c
$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_bringup robot.launch.py
```
#### 2. remote PC 
#### 1. SLAM
```c
$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=false
```
#### 2. RViz
```c
$ rviz2
fixed Frame: map
Map
LaserScan
TF
RobotModel
Odometry
```
#### 3. 자동 탐색 노드
```c
$ ros2 run my_explorer frontier_explorer
```
