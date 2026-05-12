## subscriber
#### 1. my_subscriber
> ROS2에서 turtlesim 패키지의 pose 메시지 타입을 가져온다.
> turtlesim: ROS2의 예제 시뮬레이터 패키지 이름
> .msg: 메시지 타입들이 들어있는 폴더
> pose: 거북이의 위치/방향 정보를 담은 메시티 타입
```py
$ cd ~/ros_ws/src/my_pkg/my_pkg
$ nano my_subscriber.py
import rclpy as rp
from rclpy.node import Node
from turtlesim.msg import Pose

class Subscriber(Node):
    def __init__(self):
        super().__init__('turtlesim_subscriber')
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.callback,
            10
        )
        self.subscription

    def callback(self, msg):
        print("x: ", msg.x, "y: ", msg.y)
def main(args=None):
    rp.init(args=args)

    subscriber = Subscriber()
    rp.spin(subscriber)

    subscriber.destroy_node()
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
            'my_subscriber = my_pkg.my_subscriber:main'
        ],
    },
# 위와 같이 my_subscriber 를 추가한다.
```
#### 3. build
```py
$ cd ~/res2_ws
$ colcon build
```
#### 4. turtlesim_node 실행
```py
$ source install/setup.bash
$ ros2 run turtlesim turtlesim_node
```
#### 5. subscriber 실행
```py
$ source /opt/ros/jazzy/setup.bash
$ source ~/ros2_ws/install/setup.bash
$ ros2 run my_pkg my_subscriber
```
#### 5. rqt 실행
```py
$ source /opt/ros/jazzy/setup.bash
$ source ~/ros2_ws/install/setup.bash
$ rqt
```
