### Topic LED ON/OFF  
/led_cmd 토픽에 "ON" 또는 "OFF"를 발행하면 ros2 노드가 시리얼로 ARDUINO 로 보냄.  
=> ARDUINO는 받은 문자열에 따라 LED 제어  
> 1. ROS2 토픽 발행
> 2. ROS2 Python subscriber 노드가 메시지 수신
> 3. 시리얼 포트로 아두이노에 ON\n 또는 OFF\n 전송
> 4. 아두이노 수신 후 LED 제어  
##### 1. 아두이노 코드  
```c++
String cmd = "";
const int LED_PIN = LED_BUILTIN;   // 보통 Uno는 13번

void setup() {
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);

  Serial.begin(115200);
}

void loop() {
  while (Serial.available() > 0) {
    cmd = Serial.readStringUntil('\');
      if (cmd == "ON") {
        digitalWrite(LED_PIN, HIGH);
        Serial.println("LED ON");
      }
      else if (cmd == "OFF") {
        digitalWrite(LED_PIN, LOW);
        Serial.println("LED OFF");
      }
  }
}
```
##### 2. 패키지 생성  
```c
$ mkdir -p ~/ros2_ws/src
$ cd ~/ros2_ws/src
$ ros2 pkg create arduino_led_bridge --build-type ament_python --dependencies rclpy std_msgs
```
패키지 구조는 다음과 같다.  
arduino_led_bridge/  
├── arduino_led_bridge  
│&nbsp;&nbsp;&nbsp;&nbsp; └── __init__.py  
├── package.xml  
├── setup.py  
└── setup.cfg  
##### 3. pyserial 설치  
```c
/*
$ cd ~/ros2_ws
$ python3 -m venv .venv
$ source .venv/bin/activate
$ python -m pip install --upgrade pip
$ python -m pip install pyserial
$ python -c "import serial; print(serial.__version__)"
*/
$ sudo apt update
$ sudo apt install python3-serial
$ python -c "import serial; print(serial.__version__)"
3.5      
```
##### 4. subscriber 노드 작성  
$ cd ~/ros2_ws/src/arduino_led_bridge/arduino_led_bridge  
$ nano led_serial_subscriber.py
```py
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import time

class LedSerialSubscriber(Node):
    def __init__(self):
        super().__init__('led_serial_subscriber')

        # 아두이노 포트 확인 후 수정
        port = '/dev/ttyACM0'
        baudrate = 115200

        try:
            self.ser = serial.Serial(port, baudrate, timeout=1)
            time.sleep(2)  # 아두이노 리셋 대기
            self.get_logger().info(f'Serial connected: {port}')
        except Exception as e:
            self.get_logger().error(f'Failed to open serial port: {e}')
            self.ser = None

        self.subscription = self.create_subscription(
            String,
            'led_cmd',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        if self.ser is None:
            self.get_logger().error('Serial not available')
            return

        data = msg.data.strip().lower()

        if data == 'on':
            self.ser.write(b'ON\n')
            self.get_logger().info('Sent: ON')
        elif data == 'off':
            self.ser.write(b'OFF\n')
            self.get_logger().info('Sent: OFF')
        else:
            self.get_logger().warn(f'Unknown command: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = LedSerialSubscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    if node.ser is not None:
        node.ser.close()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```
##### 5. setup.py 수정  
$ cd ~/ros2_ws/src/arduino_led_bridge  
$ nano setup.py
setup.py에 실행 엔트리를 추가해야 ros2 run 으로 실행할 수 있다.  
```py
from setuptools import setup

package_name = 'arduino_led_bridge'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@example.com',
    description='ROS2 Arduino LED bridge',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'led_serial_subscriber = arduino_led_bridge.led_serial_subscriber:main',
        ],
    },
)
```
##### 6. 빌드  
```c
$ cd ~/ros2_ws
$ colcon build --packages-select arduino_led_bridge
$ source install/setup.bash
```
##### 7. port 확인  
```c
$  ls /dev/ttyACM* or ls /dev/ttyUSB*
* 권한 문제로 에러가 뜨면
$ sudo usermod -a -G dialout $USER
$ newgrp dialout
$ groups
$ ls -l /dev/ttyACM0
```
##### 8. 실행  
  * 터미널 1: ROS2 subscriber 실행
```c
$ cd ~/ros2_ws
$ source install/setup.bash
$ ros2 run arduino_led_bridge led_serial_subscriber
```
  * 터미널 2: 토픽 발행
```c
cd ~/ros2_ws
source /opt/ros/jazzy/setup.bash
source install/setup.bash
source .venv/bin/activate
* LED ON 명령 실행
ros2 topic pub /led_cmd std_msgs/msg/String "{data: 'on'}" --once
* LED OFF 명령 실행
ros2 topic pub /led_cmd std_msgs/msg/String "{data: 'off'}" --once
```
