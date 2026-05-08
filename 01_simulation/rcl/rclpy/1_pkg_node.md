#### 1. pakage 만들기  
```py
$ source /opt/ros/jazzy/setup.bash
$ cd ~/ros2_ws/src
$ $ ros2 pkg create --build-type ament_python --node-name my_node my pkg --dependencies rclpy std_msgs
# --node-name 옵션을 사용하면 기본 실행 파일(노드)이 자동으로 만들어진다.
```
