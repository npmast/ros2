### 토픽 구독  
#### 1. turtle_vel.py
> 일단 MyVel 노드에 구독 객체를 생성한다.
```c
$ cd ~/ros2_ws/src/my_pkg/my_pkg
$ nano turtle_vel.py
import rclpy as rp
from rclpy.node import Node
from turtlesim.msg import Pose
  
class MyVel(Node):
    def __init__(self):
        super().__init__('turtle_vel')
        self.sub_pose = self.create_subscription(
            Pose, 
            '/turtle1/pose', 
            self.callback_pose, 
            10)
 
    def callback_pose(self, msg):
        print("x: ", msg.x, "y: ", msg.y)

def main(args=None):
    rp.init(args=args)
     
    my_vel_node = MyVel()
    rp.spin(my_vel_node)

    my_vel_node.destroy_node()
    rp.shutdown()

if __name__ == '__main__':
    main()
```
#### 2. setup.py
```c
$ cd ~/ros2_ws/src/my_pkg
$ nano setup.py
entry_points={
    'console_scripts': [
        'my_node = my_pkg.my_node:main',
        'my_subscriber = my_pkg.my_subscriber:main',
        'turtle_vel = my_pkg.turtle_vel:main'
    ],
```
#### 3. build
```c
$ cd ~/ros2_ws
$ colcon build
$ source install/setup.bash
```
#### 4. 실행
```c
$ ros2 run turtlesim turtlesim_node
다른 터미널을 연다.
$ source install/setup.bash
$ ros2 run my_pkg turtle_vel
```
