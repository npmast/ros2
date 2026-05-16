### Pose 토픽과 Twist 토픽 구독하기

```c
cd ~/ros2_ws/src/my_mkg/my_mkg
nano turtle_vel.py
import rclpy as rp
from rclpy.node import Node
from turtlesim.msg import Pose
from my_pkg_msgs.msg import MyCmdPoseVel

class MyVel(Node):
	def __init__(self):
		super().__init__('turtle_vel')
		self.sub_pose = self.create_subscription(Pose, '/turtle1/pose', self.callback_pose, 10)
		self.sub_cmdvel = self.create_subscription(Twist, '/turtle1/cmd_vel', self.callback_cmd, 10)
		self.cmd_pose = MyCmdPoseVel()

	def callback_pose(self, msg):
		self.cmd_pose.pose_x = msg.x
		self.cmf_pose.pose_y = msg.y
		self.cmd_pose.linear_vel = msg.linear_velocity
		self.cmd_pose.angular_vel = msg.angular_velocity

	def callback_cmd(self, msg):
		self.cmd_pose.cmd_vel_liner = msg.linear.x
		self.cmd_pose.cmd_vel_angular = msg.angular.z
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
