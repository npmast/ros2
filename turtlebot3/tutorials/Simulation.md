#### 1. Gazebo Simulation
> 1. 설치하기
```C
$ cd ~/turtlebot3_ws/src/
$ git clone -b humble https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
$ cd ~/turtlebot3_ws && colcon build --symlink-install
```
> 2. 시뮬레이션 실행
```c
$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_gazebo empty_world.launch.py

$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_gazebo turtlebot3_house.launch.py
```
> 3. 조작
```c
- teleop 노드
$ ros2 run turtlebot3_teleop teleop_keyboard

- 충돌 방지 노드
$ ros2 run turtlebot3_gazebo turtlebot3_drive
```
> 4. RViz2
```c
$ ros2 launch turtlebot3_bringup rviz2.launch.py
```
#### 2. SLAM Simulation
> 1. gazebo 시작
```c
$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```
> 2. SLAM 노드 실행
```c
$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True
```
> 3. 원격 노드 실행
```c
$ export TURTLEBOT3_MODEL=burger
$ ros2 run turtlebot3_teleop teleop_keyboard

 Control Your TurtleBot3!
 ---------------------------
 Moving around:
        w
   a    s    d
        x

 w/x : increase/decrease linear velocity
 a/d : increase/decrease angular velocity
 space key, s : force stop

 CTRL-C to quit
```
> 4. 지도 저장
```c
$ ros2 run nav2_map_server map_saver_cli -f ~/map/map1
```
#### 3. Navigation Simulation
> 1. Gazebo 실행
```c
$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```
> 2. Navigation 노드 실행
```c
$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=$HOME/map/map1.yaml
```
