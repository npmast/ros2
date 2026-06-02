### 일정 거리 이동 후 남은 거리 피드백을 보내는 액션 서버
> trutlesimSubscriber --> 현재 Pose 수신 --> DistTurtleServer(거리 계산, cmd_vel 발행, Feedback 전송, Result 반환
#### 1. dist_action_server.py
```py
$ ~/ros2_ws/src/my_pkg/my_pkg
$ nano dist_action_server.py
import rclpy as rp
from rclpy.action import ActionServer
from rclpy.executors import MultiThreadedExecutor					# 여러 노드 동시 실행
from rclpy.node import Node
from my_pkg_msgs.action import DistTurtle							# Action 메시지
from geometry_msgs.msg import Twist									# 속도 명령
from turtlesim.msg import Pose										# 터틀 현재 위치
from my_pkg.my_subscriber import Subscriber							# MY_구독자 클래스
import time
import math

class DistTurtleServer(Node):										# 액션 서버 노드
    def __init__(self):
        super().__init__('dist_action_server')
        self.total_dist = 0.0										# 터틀 이동한 거리
        self.is_first_time = True									# 최초 실행 수신
        self.current_pose = Pose()									# 현재 위치
        self.previous_pose = Pose()									# 이전 위치
        self.publisher = self.create_publisher(						# 터틀 이동 명령 발행
            Twist, '/turtle1/cmd_vel', 10
        )
        self.action_server = ActionServer(							# Action Server 생성
            self, DistTurtle, 'dist_turtle', self.callback_service
		)
    def calc_diff_pose(self):										# 현재와 이전 위치 거래 계산
        if self.is_first_time:
            self.previous_pose.x = self.current_pose.x
            self.previous_pose.y = self.current_pose.y
            self.is_first_time = False
		# 거리 공식: d = √(x2-x1)² + (y2-y1)²
		# sqrt(): Square Root(제곱근) 구하는 함수, **2 는 거듭제곱(2**2 = 4)
		# 이전(5, 5) 현재(6, 5) 면 이동 거리: 1
        diff_pose = math.sqrt((self.current_pose.x - self.previous_pose.x) ** 2 +\
                            (self.current_pose.y - self.previous_pose.y) ** 2)
        self.previous_pose.x = self.current_pose.x
		self.previous_pose.y = self.current_pose.y
        return diff_pose
    def callback_service(self, goal_handle):						# Goal이 들어오면 실행
        feedback_msg = DistTurtle.Feedback()						# Feedback 객체 생성
        msg = Twist()												# Twist 생성
        msg.linear.x = goal_handle.request.linear_x					# Goal 값 가져오기
        msg.angular.z = goal_handle.request.angular_z

        while True:
            self.total_dist += self.calc_diff_pose()				# 이동 거리 누적
            feedback_msg.remained_dist = goal_handle.request.dist - self.total_dist		# 남은 거리 계산
            goal_handle.publish_feedback(feedback_msg)				# Feedback 전송
            self.publisher.publish(msg)								# 이동 명령 발생
            time.sleep(0.1)
            if feedback_msg.remained_dist < 0.2:					# 목표 도달 0.2 이하 종료
                break
        goal_handle.succeed()										# 액션 성공
        result = DistTurtle.Result()								# 결과 생성
        result.pos_x = self.current_pose.x							# 현재 위치 저장
        result.pos_y = self.current_pose.y
        result.pos_theta = self.current_pose.theta
        result.result_dist = self.total_dist						# 총 이동 거리
        self.total_dist = 0.0										# 초기화
        self.is_first_time = True
        return result

class TurtleSub_Action(TurtlesimSubscriber):						# Pose 구독용 클래스
    def __init__(self, act_server):	
        super().__init__()
        self.act_server = act_server								# 액션 서버 객체
    def callback(self, msg):										# Pose 수신
        self.act_server.current_pose = msg							# 현재 위치 전달

def main(args=None):
    rp.init(args=args)

    executor = MultiThreadedExecutor()								# Executor 생성
    act = DistTurtleServer()										# 액션 서버 생성
    sub = TurtleSub_Action(act_server= act)							# Pose 구독자 생성

    executor.add_node(act)											# Executor 등록
    executor.add_node(sub)

    try:
        executor.spin()												# 동시 실행
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
> 클라이언트가 Goal 전송 --> 서버 /cmd_vel 발행 --> 터틀 이동 --> 수신: 이동 거리 계산 --> Feedbach 전송 --> 이동 완료 --> Result 반환
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
