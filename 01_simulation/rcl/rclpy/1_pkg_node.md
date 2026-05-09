## pakage 만들기
#### 1. pakage
```py
$ source /opt/ros/jazzy/setup.bash
$ cd ~/ros2_ws/src
$ $ ros2 pkg create --build-type ament_python --node-name my_node my_pkg --dependencies rclpy std_msgs
# --node-name 옵션을 사용하면 기본 실행 파일(노드)이 자동으로 만들어진다.
$ sudo apt install tree
$ tree                # 폴더의 계층구조 확인
```
#### 2. build
```c
$ cd ~/ros2_ws
$ colcon build

```
#### 3. 환경 적용 및 실행
```py
$ source /install/setup.bash
$ ros2 run my_pkg my_node
Hi from my_pkg
$ ros2 pkg list | grep my_pkg
my_pkg
alias 
```
