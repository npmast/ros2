## Publisher
#### 1. my_publisher
```py
$ cd ~/ros_ws/src/my_pkg/my_pkg
$ nano my_publisher.py
import rclpy as rp
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Publisher(Node):
   def __init__(self):
      super().__init__('turtlesim_publisher')
      self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
      timer_period = 0.5
      self.timer = self.create_timer(timer_period, self.timer_callback)
   def timer_callback(self):
      msg = Twist()
      msg.linear.x = 2.0
      msg.angular.z = 2.0
      self.publisher.publish(msg)

def main(args=None):
    rp.init(args=args)

    publisher = Publisher()
    rp.spin(publisher)

    publisher.destroy_node()
    rp.shutdowm()

if __name__ == '__main__':
    main()

```
#### 2. setup.py
entry_point 수정(시작점 지정)
```py
$ cd ~/ros2_ws/src/my_pkg
$ nano setup.py
entry_points={
        'console_scripts': [
            'my_node = my_pkg.my_node:main',
            'my_subscriber = my_pkg.my_subscriber:main',
            'my_publisher = my_pkg.my_publisher:main'
        ],
    },
# 위와 같이 my_publisher 를 추가한다.
```
#### 3. build
```py
$ cd ~/res2_ws
$ colcon build
```
#### 4. 실행
```py
terminal 1
$ source /opt/ros/jazzy/setup.bash
$ source install/setup.bash
& ros2 run my_pkg my_publisher
terminal 2
$ source /opt/ros/jazzy/setup.bash
$ source install/setup.bash
& ros2 run my_pkg my_subscriber
terminal 3
$ source /opt/ros/jazzy/setup.bash
$ source install/setup.bash
& ros2 run turtlesim turtlesim_node
terminal 4
$ source /opt/ros/jazzy/setup.bash
$ source install/setup.bash
& rqt_graph

```
