### 사용자 정의 서비스
> ROS2에서 사용자 정의 서비스(service)를 사용하려면, 패키지 루트 디렉토리 내에 srv라는 폴더를 생성하고
> 그 안에 확장자가 .srv인 파일을 작성해야 한다.
#### 1. 폴더 및 파일 생성
```py
$ cd ~/ros2_ws/srv/my_pkg_msgs

1. MultiSpawn.srv 파일 만들기
$ mkdir srv
$ MultiSpawn.srv
int 64 num
---
float64[] x
float64[] y
float64[] theta

2. CMakeLists.txt 수정
$ cd ~/ros2_ws/src/my_pkg_msgs
$ nano CMakeLists.txt
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
    "msg/MyCmdPoseVel.msg" 
    "srv/MultiSpawn.srv"                <== 삽입
)
```
#### 2. build
```c
$ cd ~/ros2_ws
$ colcon build --packages-select my_pkg_msgs
$ source install/setup.bash
$ ros2 interface show my_pkg_msgs/srv/MultiSpawn
```
