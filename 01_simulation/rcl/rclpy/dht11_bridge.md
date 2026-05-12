#### 1. arduino
```c
/* DHT sensor library INSTALL */
#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT11   // DHT22면 DHT22로 변경

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (!isnan(h) && !isnan(t)) {
    Serial.print(t);
    Serial.print(",");
    Serial.println(h);
  }

  delay(1000);
}
```
#### 2. 패키지 생성
```c
$ ~/ros2_ws/src
$ ros2 pkg create dht_sensor_bridge --build-type ament_python --dependencies rclpy std_msgs
```
#### 3. pyserial 설치
```c
sudo apt install python3-serial
```
##### 4. 노드 작성
```c
$ cd ~/ros2_ws/src/dht_sensor_bridge/dht_sensor_bridge
$ nano dht_node.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import serial

class DHTNode(Node):
    def __init__(self):
        super().__init__('dht_node')

        self.temp_pub = self.create_publisher(Float32, 'temperature', 10)
        self.humi_pub = self.create_publisher(Float32, 'humidity', 10)

        self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

        self.timer = self.create_timer(1.0, self.read_sensor)

    def read_sensor(self):
        line = self.ser.readline().decode().strip()

        try:
            temp_str, humi_str = line.split(',')
            temp = float(temp_str)
            humi = float(humi_str)

            temp_msg = Float32()
            humi_msg = Float32()

            temp_msg.data = temp
            humi_msg.data = humi

            self.temp_pub.publish(temp_msg)
            self.humi_pub.publish(humi_msg)

            self.get_logger().info(f'Temp: {temp} C, Humidity: {humi} %')

        except Exception:
            pass

def main(args=None):
    rclpy.init(args=args)
    node = DHTNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
```
#### 5. setup.py 수정
```c
$ cd ~/ros2_ws/src/dht_sensor_bridge
$ nano setup.py
entry_points={
    'console_scripts': [
        'dht_node = dht_sensor_bridge.dht_node:main',
    ],
},
```
#### 6. 빌드
```c
$ cd ~/ros2_ws
$ colcon build --packages-select dht_sensor_bridge
$ source install/setup.bash
```
#### 7. 실행
```c
$ ls /dev/ttyACM*
/dev/ttyACM0
$ ros2 run dht_sensor_bridge dht_node
$ ros2 topic list
$ ros2 topic echo /temperature
$ ros2 topic echo /humidity
==> 권한 문제 시 dialout 그룹에 추가: sudo usermod -aG dialout $USER
```
