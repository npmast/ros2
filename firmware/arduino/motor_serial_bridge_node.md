# ROS2 Python 노드  

### ROS2 패키지 생성  
```c
sudo apt update
sudo apt install -y python3-serial
mkdir -p ~/ros2_ws/src                                                                                  // WS 생성
cd ~/ros2_ws/src
ros2 pkg create motor_serial_bridge --build-type ament_python --dependencies rclpy geometry_msgs        // ROS2 패키지 생성
```
### 노드 코드 생성
~/ros2_ws/src/motor_serial_bridge/motor_serial_bridge/motor_serial_bridge_node.py  
### setup.py 파일에 실행 엔트리 등록  
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
