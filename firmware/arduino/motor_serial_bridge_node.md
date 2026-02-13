# ROS2 Python 노드  

### 1. ROS2 패키지 생성  
```c
sudo apt update
sudo apt install -y python3-serial
mkdir -p ~/ros2_ws/src                                                                                  // WS 생성
cd ~/ros2_ws/src
ros2 pkg create motor_serial_bridge --build-type ament_python --dependencies rclpy geometry_msgs        // ROS2 패키지 생성
```
### 2. 노드 코드 생성
~/ros2_ws/src/motor_serial_bridge/motor_serial_bridge/motor_serial_bridge_node.py  
### 3. setup.py 파일에 실행 엔트리 등록  
~/ros2_ws/src/motor_serial_bridge/setup.py를 열고 entry_points를 작성한다.  
```c
entry_points={
    'console_scripts': [
        'motor_serial_bridge = motor_serial_bridge.motor_serial_bridge_node:main',
    ],
},
```
실행권한 설정  
```c
chmod +x ~/ros2_ws/src/motor_serial_bridge/motor_serial_bridge/motor_serial_bridge_node.py
```
### 4. 빌드 및 실행  
* 빌드
```c
cd ~/ros2_ws
source /opt/ros/jazzy/setup.bash
colcon build
source ~/ros2_ws/install/setup.bash
```
* 실행  
```c
ros2 run motor_serial_bridge motor_serial_bridge --ros-args -p port:=/dev/ttyACM0
```
### 5. 동작 테스트  
* 새로운 터미널에서  
```c
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
// 직진
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.2}, angular: {z: 0.0}}"
// 제자리 회전
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.0}, angular: {z: 1.0}}"
// 정
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.0}, angular: {z: 0.0}}"
```
* 옵션
```c
// 좌/우 방항 반대일 때
ros2 run motor_serial_bridge motor_serial_bridge --ros-args -p invert_left:=true
// 속도가 세거나 약할 때
// max_v가 작으면: 같은 cmd_vel에서 PWM 이 큼(민감), max_v 가 크면: PWM 이 작음(둔감)
ros2 run motor_serial_bridge motor_serial_bridge --ros-args -p max_v:=0.3
```
* 주의: screen 이 동작하면 포드를 사용할 수 없다. ROS 노드 실행 중 screen 을 종료해야 한다.(CTRL+A -> K -> Y)
