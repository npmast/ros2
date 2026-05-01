### turtlesim  
#### 개념
> 1. turtlesim:              ROS2 패키지
> 2. turtlesim_node:         실행 노드 프로그램
> 3. /turtlesim:             실행된 노드 이름
> 4. turtle1:                시뮬레이터 내부 거북이 객체
> 5. /turtle1/pose:          turtle1 상태 토픽
> 6. /turtle1/cmd_vel:       속도 명령 토픽
> 7. *turtlesim 패키지 안에 있는 turtlesim_node가 실행되면 /turtlesim 노드 생성, turtle1 객체 생성, topic 생성, service 생성*
```c
$ ros2 pkg executables turtlesim  
turutlsim turtlesim_node                             // 시뮬레이터 창을 띄우는 실행 파일
turtlesim turtle_teleop_key                          // 화살표 키를 사용하는 실행 파일
turtlesim draw_square                                // 거북이가 사각형을 그리는 실행 파일
turtlesim mimic
```
  
#### 1. turtlesim_node  
- terminal open
```c
$ source /opt/ros/jazzy/setup.bash    
$ ros2 run turtlesim turtlesim_node        // 노드 이름, 패키지, 그리고 위치 정보가 나타난다.
```
- other terminal open
```c
$ source /opt/ros/jazzy/setup.bash  
$ ros2 node list                
/turtlesim
$ ros2 node info /turtlesim                // 현재 실행 중인 /turtlesim 노드 상세 목록
$ echo $ROS_DOMAIN_ID  
```
#### 2. teleop_key  
```c
$ ros2 run turtlesim turtle_teleop_key
```
#### 3. rqt  
그래픽 사용자 인터페이스 프레임워크  
- other terminal open
```c
$ source /opt/ros/jazzy/setup.bash 
$ rqt                                      // QThread 
Plugins > Introspection > Node Graph
```
/telep_turtle 노드와 /turtlesim 노드의 통신관계를 보여 준다.
