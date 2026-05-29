### 일정 거리 이동 액션 서버
#### 1. dist_action_server.py
```py
$ ~/ros2_ws/src/my_pkg/my_pkg
$ nano dist_action_server.py
import rclpy as rp
from rclpy.action import ActionServer
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node
from my_pkg_msgs.action import DistTurtle
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from my_pkg.my_subscriber import TurtlesimSubscriber
import time
import math

class DistTurtleServer(Node):
    def __init__(self):
        super().__init__('dist_action_server')
        self.total_dist = 0.0
        self.is_first_time = True
        self.current_pose = Pose()
        self.previous_pose = Pose()
        self.publisher = self.create_publisher(
            Twist, '/turtle1/cmd_vel', 10
        )
        self.action_server = ActionServer(
            self, DistTurtle, 'dist_turtle', self.callback_service
		)
    def calc_diff_pose(self):
        if self.is_first_time:
            self.previous_pose.x = self.current_pose.x
            self.previous_pose.y = self.current_pose.y
            self.is_first_time = False
        diff_pose = math.sqrt((self.current_pose.x - self.previous_pose.x) ** 2 +\
                            (self.current_pose.y - self.previous_pose.y) ** 2)
        self.previous_pose = self.current_pose
        return diff_pose
    def callback_service(self, goal_handle):
        feedback_msg = DistTurtle.Feedback()
        msg = Twist()
        msg.linear.x = goal_handle.request.linear_x
        msg.angular.z = goal_handle.request.angular_z

        while True:
            self.total_dist += self.calc_diff_pose()
            feedback_msg.remained_dist = goal_handle.request.dist - self.total_dist
            goal_handle.publish_feedback(feedback_msg)
            self.publisher.publish(msg)
            time.sleep(0.1)
            if feedback_msg.remained_dist < 0.2:
                break
        goal_handle.succeed()
        result = DistTurtle.Result()
        result.pos_x = self.current_pose.x
        result.pos_y = self.current_pose.y
        result.pos_theta = self.current_pose_theta
        result.result_dist = self.total_dist
        self.total_dist = 0.0
        self.is_first_time = True
        return result

class TurtleSub_Action(TurtlesimSubscriber):
    def __init__(self, act_server):
        super().__init__()
        self.act_server = act_server
    def callback(self, msg):
        self.act_server.current_pose = msg

def main(args=None):
    rp.init(args=args)

    executor = MultiThreadedExecutor()
    act = DistTurtleServer()
    sub = TurtleSub_Action(act_server= act)

    executor.add_node(act)
    executor.add_node(sub)

    try:
        executor.spin()
    finally:
        executor.shutdown()
        act.destroy_node()
        sub.destroy_node()
        rp.shutdown()

if __name__ == '__main__':
	main()

```
#### 2. setup.py
```c
$ ~/ros2_ws/my_pkg/my_pkg
$ nano setpu.py
 entry_points={
        'console_scripts': [
            'my_node = my_pkg.my_node:main',
            'my_subscriber = my_pkg.my_subscriber:main',
            'my_publisher = my_pkg.my_publisher:main',
	      		'turtle_vel = my_pkg.turtle_vel:main',
            'my_service_server = my_pkg.my_service_server:main',
            'my_action_server = my_pkg.my_action_server:main',
            'my_thread = my_pkg.my_thread:main',
            'dist_action_server = my_pkg.dist_action_server:main'       <== 삽입
        ],
    },
```
#### 3. build
```c
$ cd ~/ros2_ws
$ python3 -m py_compile src/my_pkg/my_pkg/dist_action_server.py      # tab error
$ colcon build
```
#### 4. 실행
```c
terminal 1
$ cd ~/ros2_ws
$ source install/setup.bash
$ ros2 run turtlesim turtlesim_node
terminal 2
$ cd ~/ros2_ws
$ source install/setup.bash
$ ros2 run my_pkg dist_action_server
terminal 3
$ cd ~/ros2_ws
$ source install/setup.bash
$ ros2 action send_goal --feedback /dist_turtle my_pkg_msgs/action/DistTurtle "{linear_x: 0.8, angular_z: 0.4, dist: 20}"
terminal 4
$ cd ~/ros2_ws
$ source install/setup.bash
$ rqt
```
