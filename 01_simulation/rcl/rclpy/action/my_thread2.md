### MultiThread
#### 1. 
```py
$ nano ~/ros2_wn/src/my_pkg/my_pkg/my_thread2.py

import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup               # 콜백 그룹안에 동시 실행
import time

class ThreadTestNode(Node):
    def __init__(self):
        super().__init__('thread_test_node')

        self.callback_group = ReentrantCallbackGroup()

        self.timer1 = self.create_timer(
            1.0,
            self.timer_callback_1,
            callback_group=self.callback_group
        )

        self.timer2 = self.create_timer(
            1.0,
            self.timer_callback_2,
            callback_group=self.callback_group
        )

    def timer_callback_1(self):
        self.get_logger().info('Timer 1 시작')
        time.sleep(3)
        self.get_logger().info('Timer 1 끝')

    def timer_callback_2(self):
        self.get_logger().info('Timer 2 실행')


def main(args=None):
    rclpy.init(args=args)

    node = ThreadTestNode()

    executor = MultiThreadedExecutor(num_threads=2)         # 내부에 작업 스레드가 2개 생성
    executor.add_node(node)                         

    try:
        executor.spin()                                     # 멀티스레드 실행
    finally:
        executor.shutdown()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

# 1. create_time(1.0, callback): 1초마다 콜백 준비
# 2. MultiThreadedExecutor(num_threads=2): 빈 스레드가 있으면 실행
# 3. ReentrantCallbackGroup: 같은 콜백이 끝나기 전에도 다시 실행 허용
0초: thread-1 → Timer1 시작, 3초 sleep
0초: thread-2 → Timer2 실행

1초: thread-2 → Timer1 또 시작, 3초 sleep
2초: Timer2도 실행 준비됨
     하지만 thread-1, thread-2 모두 Timer1 실행 중
     → Timer2 대기

3초: thread-1 → Timer1 끝
     그제야 Timer2 실행 가능
```
#### 2. 
```c
$ python3 ~/ros2_wn/src/my_pkg/my_pkg/my_thread2.py
[INFO] [1780047294.979675158] [thread_test_node]: Timer 2 실행
[INFO] [1780047294.980191419] [thread_test_node]: Timer 1 시작
[INFO] [1780047295.961870779] [thread_test_node]: Timer 1 시작
[INFO] [1780047297.980941176] [thread_test_node]: Timer 1 끝
[INFO] [1780047297.982079457] [thread_test_node]: Timer 2 실행
[INFO] [1780047297.982642065] [thread_test_node]: Timer 1 시작
[INFO] [1780047298.963491432] [thread_test_node]: Timer 1 끝
[INFO] [1780047298.963885313] [thread_test_node]: Timer 1 시작
[INFO] [1780047300.983817271] [thread_test_node]: Timer 1 끝
[INFO] [1780047300.984892413] [thread_test_node]: Timer 2 실행
[INFO] [1780047300.985504555] [thread_test_node]: Timer 1 시작
[INFO] [1780047301.964814070] [thread_test_node]: Timer 1 끝

```
