### 토픽 사용자 정의 자료형 만들기
> 사용자 지정 메시지를 만들려면 기존 ROS2 패키지 내부(또는 새로운 인터페이스 전용 패키지)에 진입하여
> msg폴더를 생성해야 한다.
#### 1. pakage 만들기  
> 패키지명_msgs 이름으로 만든다.
> anent_python 에는 메시지를 빌드할 수 없다.
```c
$ cd ~/ros2_ws/src
$ ros2 pkg create --build-type ament_cmake my_pkg_msgs
```
#### 2. MyCmdPoseVel.msg
> my_pkg_msgs 폴더안에 msg 폴더를 만든다.  
> msg 폴더는 사용자 지정 메시지(.msg)파일들 저장하는 디렉토리  
```c
$ cd ~/ros2_ws/src/my_pkg_msgs
$ mkdir msg
$ nano MyCmdPoseVel.msg                      # 6가지의 자료형을 만든다.
float32 cmd_vel_linear
float32 cmd_vel_angular

float32 pose_x
float32 pose_y
float32 linear_vel
float32 angular_vel
```
#### 2. CMakeList.txt
```c
$ cd ~/ros2_ws/src/my_pkg_msgs/CMakeLists.txt
# find_package(<dependency> REQUIRED)
----------------------------------------------------- 수정
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/MyCmdPoseVel.msg")
------------------------------------------------------  
if(BUILD_TESTING)
```
#### 3. package.xml
```c
  <test_depend>ament_lint_auto</test_depend>
  <test_depend>ament_lint_common</test_depend>
-------------------------------------------------------- 수정
  <build_depend>rosidl_default_generators</build_depend>
  <exec_depend>rosidl_default_runtime</exec_depend>
  <member_of_group>rosidl_interface_packages</member_of_group>
  -------------------------------------------------------------
  <export>
    <build_type>ament_cmake</build_type>
  </export>
```
#### 4. build
```c
$ cd ~/ros2_ws
$ jazzy
$ colcon build
$ source install/setup.bash
$ ros2 interface show my_pkg_msgs/msg/MyCmdPoseVel        // ros2_ws 폴더에서 확인
float32 cmd_vel_linear
float32 cmd_vel_angular

float32 pose_x
float32 pose_y
float32 linear_vel
float32 angular_vel
```

