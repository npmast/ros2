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

class TestNode(Node):
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
3. Publisher
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
            String,
            'chatter',
            10
        )
        self.timer = self.create_timer(
            1.0,
            self.publish_message
        )
        self.count = 0

    def publish_message(self):
        msg = String()
        msg.data = f'Hello ROS2 {self.count}'
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
4. subscriber
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
