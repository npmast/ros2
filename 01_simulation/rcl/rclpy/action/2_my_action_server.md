### 액션 서버 만들기
#### 1. 
```c
$ cd ~/ros2_ws/src/my_pkg/my_pkg
$ naon my_action_server
import rclpy as rp
from rclpy.action import ActionServer
from rclpy.node import Node
from my_pkg_msgs.action import DistTurtle

class DistTurtleserver(Node):
	def __init__(self):
		super().__init__('action_server')
		self.action_server = ActionServer(
			self, DistTurtle, 'dist_turtle', self.callback_service
		)
	def callback_service(self, goal_handle):
		goal_handle.succeed()
		result = DistTurtle.Result()
		return result

def main(args=None):
	rp.init(args=args)
	action_server = DistTurtleserver()
	rp.spin(action_server)

if __name__ == '__main__':
	main()
```
#### 2. setup.py
```py
    entry_points={
        'console_scripts': [
            'my_node = my_pkg.my_node:main',
            'my_subscriber = my_pkg.my_subscriber:main',
            'my_publisher = my_pkg.my_publisher:main',
			      'turtle_vel = my_pkg.turtle_vel:main',
            'my_service_server = my_pkg.my_service_server:main',
            'my_action_server = my_pkg.my_action_server:main'        <== 삽입
        ],
    },
```
#### 3.
```c
terminal 1
$ source ~/ros2_ws/install/setup.bash
$ ros2 run my_pkg my_action_server
terminal 2
$ source ~/ros2_ws/install/setup.bash
$ ros2 action send_goal /dist_turtle my_pkg_msgs/action/DistTurtle "{linear_x: 0, angular_z; 0, dist: 0}"
Waiting for an action server to become available...
Sending goal:                                # 목표 전송(클라이언트)
     linear_x: 0.0
angular_z: 0.0
dist: 0.0

Goal accepted with ID: 6d28ff74f4804409b1f0dcbc4a5fa46e      # 서버 목표 수락

Result:                                      # 결과 수신
    pos_x: 0.0
pos_y: 0.0
pos_theta: 0.0
result_dist: 0.0

Goal finished with status: SUCCEEDED        # 작업 성공

```
#### 4. feedback
```py
$ cd ~/ros2_ws/src/my_pkg/my_pkg
$ naon my_action_server
import time

	def callback_service(self, goal_handle):
		feedback_msg = DistTurtle.Feedback()
		for n in range(0, 10):
			feedback_msg.remained_dist = float(n)
			goal_handle.publish_feedback(feedback_msg)
			time.sleep(0.5)
		goal_handle.succeed()
		result = DistTurtle.Result()
		return result
```

```c
terminal 1
$ source ~/ros2_ws/install/setup.bash
$ ros2 run my_pkg my_action_server
terminal 2
$ source ~/ros2_ws/install/setup.bash
$ ros2 action send_goal --feedback /dist_turtle my_pkg_msgs/action/DistTurtle "{linear_x: 0, angular_z; 0, dist: 0}"
Waiting for an action server to become available...
Sending goal:
     linear_x: 0.0
angular_z: 0.0
dist: 0.0

Goal accepted with ID: c2fc6bb6e76d4463871b115095a111db

Feedback:
    remained_dist: 0.0

Feedback:
    remained_dist: 1.0

Feedback:
    remained_dist: 2.0

Feedback:
    remained_dist: 3.0

```
