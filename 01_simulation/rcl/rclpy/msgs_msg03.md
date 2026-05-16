### 정의한 자료형에 데이터 출력
> trutlesim 의 토픽(/turtle1/pose)을 구독하여 정의한 자료형으로 위치정보를 출력한다.
#### 1. turtle_vel.py
```c
$ cd ~/ros2_ws/src/my_pkg/my_pkg
$ nano turtle_vel.py
import rclpy as rp
from rclpy.node import Node
from turtlesim.msg import Pose
from my_pkg_msgs.msg import MyCmdPoseVel

class MyVel(Node):
	def __init__(self):
		super().__init__('turtle_vel')
		self.sub_pose = self.create_subscription(Pose, '/turtle1/pose', self.callback_pose, 10)
		self.cmd_pose = MyCmdPoseVel()

	def callback_pose(self, msg):						# Pose 데이터 타입을 메시지 정의타입으로 바꿈
		self.cmd_pose.pose_x = msg.x
		self.cmd_pose.pose_y = msg.y
		self.cmd_pose.linear_vel = msg.linear_velocity
		self.cmd_pose.angular_vel = msg.angular_velocity
		print(self.cmd_pose)
		
def main(args=None):
	rp.init(args=args)

	my_vel_node = MyVel()
	rp.spin(my_vel_node)

	my_vel_node.destroy_node()
	rp.shutdown()

if __name__ == '__main__':
	main()
```
#### 2. build
```c
$ cd ~/rosw_ws/
$ colcon build --packages-select my_pkg
```
#### 3. 실행
```c
$ source install/setup.bash
$ ros2 run turtlesim turtlesim_node
다른 터이널
$ source install/setup.bash
$ ros2 run my_pkg turtle_vel
```
