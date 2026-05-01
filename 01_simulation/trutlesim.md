### turtlesim  
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
