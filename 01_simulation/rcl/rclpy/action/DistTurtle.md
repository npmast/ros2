### 액션 정의 만들기
#### 1. DistTurtle.action
```c
$ cd ~/ros2_ws/src/my_pkg_msgs
$ mkdir action
$ nano action/DistTurtle.action
# Request
float32 linear_x
float32 angular_z
float32 dist
---
# Result
float32 pos_x
float32 pos_y
float32 pos_theta
float32 result_dist
---
# Feedback
float32 remained_dist
```
#### 2. CMakeLists.txt & package.xml
```c
$ cd ros2_ws/src/my_pkg_msgs/
$ nano CMakeList.txt
 rosidl_generate_interfaces(${PROJECT_NAME}
    "msg/MyCmdPoseVel.msg"
    "srv/MultiSpawn.srv"
    "action/DistTurtle.aciton"             <== 추가
 )
$ nano package.xml
...
<member_of_group>rosidl_interface_packages</member_of_group>
<depend>action_msgs</depend>              <== 추가
...
```
### 3. build
```c
$ cd ~/ros2_ws
$ colcon build --packages-select my_pkg_msgs
$ source install/setup.bash
$ ros2 interface show my_pkg_msgs/action/DistTurtle
```
