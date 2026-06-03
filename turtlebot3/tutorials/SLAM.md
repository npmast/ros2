### SLAM(동시 위치 추정 및 지도 작성)
: 임의의 공간에서 현재 위치를 추정하여 지도를 그리는 기술
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
#### 3. 원격 조작
> SLAM 노드가 성공적으로 가동되면 TurtleBot3는 원격 조작을 사용하여 지도의 미지의 영역을 탐색한다. 이때 선형 속도외 각속도를 너무 빠르게 변경하는 등의 움직임은 피하며 지도의 구석구석을 스캔한다.
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
#### 4. 지도 저장
> 지도 데이터는 TurtleBot3가 이동하는 동안 RViz창에 표시된다.
> 원하는 영역의 전체 지도를 생성한 후, 나중에 사용할 수 있도독 지도 데이터를 저장한다.
> 1. nav2_map_server 패키지의 map_saver_cli 노드를 실행하여 지도 파일을 생성한다.
> 2. 생성된 지도 파일은 map_saver_cli 노드가 실행된 다렉토리에 저장된다.
> 3. 특정 파일 이름을 지정하지 않으면 map 기본 파일 이름이 사용되며, map.pgm 및 파일이 생성된다.
```c
$ ros2 run nav2_map_server map_saver_cli -f ~/map
```
