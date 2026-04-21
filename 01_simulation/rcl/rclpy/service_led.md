##### 1. 인터페이스 정의  
* srv 폴더 생성
```py
cd ~/ros2_ws/src/arduino_led_bridge
mkdir srv
```
* SetLed.srv 파일 생성
```py
touch srv/SetLed.srv
파일의 내용은 
bool on
---
bool success
string message
- 요청: 켜기/끄기
- 응답: 성공 여부 + 메시지
```
##### 2. package.xml 수정
```c
<build_depend>rosidl_default_generators</build_depend>
<exec_depend>rosidl_default_runtime</exec_depend>

<member_of_group>rosidl_interface_packages</member_of_group>
```
##### 3. CMakeLists.txt 수정
```c
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/SetLed.srv"
)

ament_export_dependencies(rosidl_default_runtime)
```
##### 4. Python 서비스 노드 작성
```c
$ cd ~/ros2_ws/src/arduino_led_bridge/arduino_led_bridge
$ nano led_service_node.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import serial
import time

from arduino_led_bridge.srv import SetLed


class LedServiceNode(Node):

    def __init__(self):
        super().__init__('led_service_node')

        # 시리얼 연결
        try:
            self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
            time.sleep(2)
            self.get_logger().info('Serial connected')
        except Exception as e:
            self.get_logger().error(f'Serial error: {e}')
            self.ser = None

        # 상태 변수
        self.led_state = False

        # Service 생성
        self.srv = self.create_service(
            SetLed,
            'set_led',
            self.handle_set_led
        )

        # 상태 publish
        self.pub = self.create_publisher(Bool, 'led_state', 10)

        self.get_logger().info('LED Service Node Ready')

    def handle_set_led(self, request, response):

        if self.ser is None:
            response.success = False
            response.message = 'Serial not connected'
            return response

        try:
            if request.on:
                self.ser.write(b'ON\n')
                self.led_state = True
                self.get_logger().info('LED ON')
            else:
                self.ser.write(b'OFF\n')
                self.led_state = False
                self.get_logger().info('LED OFF')

            # 상태 publish
            msg = Bool()
            msg.data = self.led_state
            self.pub.publish(msg)

            response.success = True
            response.message = 'OK'

        except Exception as e:
            response.success = False
            response.message = str(e)

        return response


def main(args=None):
    rclpy.init(args=args)
    node = LedServiceNode()

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
```c
entry_points={
    'console_scripts': [
        'led_service_node = arduino_led_bridge.led_service_node:main',
    ],
},
```
##### 6. 빌드
```c
$ cd ~/ros2_ws
$ colcon build
$ source install/setup.bash
```
##### 7. 실행
* 터미널 1: 서비스 서버 실행
```c
$ cd ~/ros2_ws
$ source .venv/bin/activate
$ source /opt/ros/humble/setup.bash
$ source install/setup.bash
$ ros2 run arduino_led_bridge led_service_node
Serial connected
LED Service Node Ready
```
* 터미널 2: 서비스 호출
  LED 켜기
  ```
$ ros2 service call /set_led arduino_led_bridge/srv/SetLed "{on: true}"
  ```
  LED 끄기
```
$ ros2 service call /set_led arduino_led_bridge/srv/SetLed "{on: false}"
```
##### 8. 상태 확인
```
$ ros2 topic echo /led_state
```
