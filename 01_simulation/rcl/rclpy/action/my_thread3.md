### my_thread3
#### 1. 
> timere 1 은 중복 실행을 막고, timer 2는 따로 돌리려고 하면 그룹을 분리한다.
```py
import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup, MutuallyExclusiveCallbackGroup
import time


class ThreadTestNode(Node):
    def __init__(self):
        super().__init__('thread_test_node')

        self.timer1_group = MutuallyExclusiveCallbackGroup()
        self.timer2_group = ReentrantCallbackGroup()

        self.timer1 = self.create_timer(
            1.0,
            self.timer_callback_1,
            callback_group=self.timer1_group
        )

        self.timer2 = self.create_timer(
            1.0,
            self.timer_callback_2,
            callback_group=self.timer2_group
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

    executor = MultiThreadedExecutor(num_threads=3)         # 내부에 작업 스레드가 2개 생성
    executor.add_node(node)                         

    try:
        executor.spin()                                     # 멀티스레드 실행
    finally:
        executor.shutdown()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
```
