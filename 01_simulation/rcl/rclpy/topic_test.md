### NODE 구조와 통신 방식  
1. 패키지 생성
```c
$ cd ~/ros2_ws/src
$ ros2 pkg create test_pkg --build-type ament_python --dependencies rclpy std_msgs
```
2. 단일 노드 생성
```c
$ cd ~/ros2_ws/src/test_pkg
$ nano test_pkg.py

import rclpy
from rclpy.node import Node

class TestNode(Node):                            # Node 를 상속받는다
    def __init__(self):
        super().__init__('test_node')
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Hello ROS2")

def main(args=None):
    rclpy.init(args=args)
    node = TestNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```
3. Publisher 만들기  
```c
$ cd ~/ros2_ws/src/test_pkg/test_pkg
$ nano publisher_node.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(
            String,                                // 데이터 타입
            'chatter',                             // topic 이름(기본 문자열 토픽)                  
            10                                     // QoS
        )
        self.timer = self.create_timer(
            1.0,
            self.publish_message
        )
        self.count = 0

    def publish_message(self):
        msg = String()
        msg.data = f'Hello ROS2 {self.count}'            // f-string
        self.publisher_.publish(msg)
        self.get_logger().info(msg.data)
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```
4. subscriber 만들기
```c
$ nano subscriber.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.listener_callback,
            10
        )
    def listener_callback(self, msg):
        self.get_logger().info(
            f'Received: {msg.data}'
        )

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```
5. setup.py 등록
```c
$ cd ~/ros2_ws/src/test_pkg/setup.py
아래 부분을 찾아 수정한다.
entry_points={
    'console_scripts': [
        'publisher_node = test_pkg.publisher_node:main',
        'subscriber_node = test_pkg.subscriber_node:main',
    ],
},
```
6. build
```c
$ cd ~/ros2_ws
$ colcon build
```
7. subscriber 실행
```c
$ cd ~/ros2_ws
$ source install/setup.bash
$ ros2 run test_pkg subscriber_node
```
8. publisher 실행
```c
$ cd ~/ros2_ws
$ source install/setup.bash
$ ros2 run test_pkg publisher_node
```
9. other teminal  
실행 중일 때 확인
```C
$ ros2 topic list
$ ros2 topic echo /chatter
$ ros2 node list
```
### Launch
#### 1. launch 폴더 생성 및 launch 파일 생성
```c
$ cd ~/ros2_ws/src/test_pkg
$ mkdir launch
$ nano test.launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([                        // 실행할 노드 목록
        Node(
            package='test_pkg',                        // 패키지 이름
            executable='publisher_node',               // setup.py에 등록한 실행 이름
            name='publisher_node'                      // ROS2 노드 이름
        ),
        Node(
            package='test_pkg',
            executable='subscriber_node',
            name='subscriber_node'
        ),
    ])
```
#### 2. setup.py 수정
```c
a. 헤더 추가
from glob import glob
import os
b. data_files 에 추가
   data_files=[
       ('share/ament_index/resource_index/packages',
           ['resource/' + package_name]),
       ('share/' + package_name, ['package.xml']),
       (os.path.join('share', package_name, 'launch'),
       glob('launch/*.launch.py')),
   ],
```
#### 3. build
```c
cd ~/ros2_ws
colcon build
source install/setup.bash
```
#### 4. launch 실행
```c
ros2 launch test_pkg test.launch.py            // 동시에 실행된다.
[publisher_node] Hello ROS2 0
[subscriber_node] Received: Hello ROS2 0
```
