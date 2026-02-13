# ROS2 Python 노드  

### 1. ROS2 패키지 생성  
```c
sudo apt update
sudo apt install python3-serial -y
mkdir -p ~/ros2_ws/src                                                                            // WS 생성
cd ~/ros2_ws/src
ros2 pkg create motor_serial_bridge --build-type ament_python --dependencies rclpy geometry_msgs  // motor_serial_bridge 이름의 ROS2 패키지 생성
```
ament_python 빌드타입을 쓰는 motor_serial_bridge 이름의 패키지 구조가 src 폴더 안에 생성된다.(~/ros2_ws/src/motor_serial_bridge)  
~/ros2_ws/src/motor_serial_bridge 폴더안에는  
motor_serial_bride 폴더, resource 폴더, test 폴더, package.xml 파일, setup.cfg 파일, setup.py 파일이 자동 생성된다.  
motor_serial_bride 폴더안에는 \_\_init\_\_.py 파일이 생성되어 있다.(디렉토리를 하나의 패키지로 패스킹하고 초기화하는 역활)  
의존성 rclpy와 geometry_msgs 는 ROS2 설치 시에 함께 설치가 되는 핵심 패키지이다.  
### 2. 노드 코드 생성  
moter_serial_bridge 폴더안에 motor_serial_bridge.py 를 작성하여 노드를 추가한다.  
nano ~/ros2_ws/src/motor_serial_bridge/motor_serial_bridge/motor_serial_bridge_node.py  
### 3. setup.py 파일에 실행 엔트리 등록  
nano ~/ros2_ws/src/motor_serial_bridge/setup.py 를 열고 entry_points를 다음과 같이 수정한다.  
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
jazzy                                                                  // source /opt/ros/jazzy/setup.bash
colcon build                                                           // 워크스페이스 내의 모든 패키지 빌드
source ~/ros2_ws/install/setup.bash                                    // setup.bash 적용   
```
* 실행  
```c
ros2 run motor_serial_bridge motor_serial_bridge --ros-args -p port:=/dev/ttyACM0
```
### 5. 동작 테스트  
* 새로운 터미널에서  
```c
jazzy
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
