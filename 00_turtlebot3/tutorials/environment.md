#### 1. 설치 파일 불러오기
```c
$ source /opt/ros/humble/setup.bash
또는 Run commands 설정
$ echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc      // 셸에 소스 추가
```
#### 2. 환경 변수
```c
$ printenv | grep -i ROS
ROS_VERSION=2
ROS_PYTHON_VERSION=3
ROS_DISTRO=humble
...
$ echo "export ROS_LOCALHOST_ONLY=1" >> ~/.bashrc        // localhost 로 제한  
```
#### 3. turtlesim  
> 1. turtlesim packages 
```c
$ ros2 pkg executables turtlesim
turtlesim doaw_square
turtlesim mimic
turtlesim turtle_teleop_key
turtlesim turtlesim_node
```
> 2. turtlesim 실행
```c
$ ros2 run turtlesim turtlesim_node
```
> 다른 터미널을 연다
```c
$ ros2 run turtlesim turtle_teleop_keky
```
> 3. 통신 확인
```c
$ ros2 node list
$ ros2 topic list
$ ros2 service list
$ ros2 action list
```
> 4. rqt
```c
$ rqt
```
