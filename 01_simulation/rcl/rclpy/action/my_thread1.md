### thread
#### 1.
```py
$ cd ~/ros2_ws/src/my_pkg/my_pkg
$ nano my_thread.py
import rclpy as rp
from rclpy.executors import MultiThreadedExecutor           # 이그젝큐터: 실행기
from rclpy.node import Node
from my_pkg.my_publisher import Publisher          # 클래스를 불러온다.
from my_pkg.my_subscriber import Subscriber

def main(args=None):
    rp.init(args=args)

    pub = Publisher()
    sub = Subscriber()

    executor = MultiThreadedExecutor()

    executor.add_node(pub)
    executor.add_node(sub)

    try:
        executor.spin()                  # rclpy.spin(): SingleThreadedExecutor 처럼 동작한다.
    finally:
        executor.shutdown()
        pub.destroy_node()
        sub.destroy_node()
        rp.shutdown()

if __name__ == "__main__":
    main()
```
#### 2.
```C
   'my_action_server = my_pkg.my_action_server:main',
   'my_thread = my_pkg.my_thread:main'                      <== 추가
```
#### 3.
```c
terminal 1
$ run2 run turtlesim turtlesim_node
terminal 2
$ cd ~/ros2_ws
$ colcon build
$ source install/setup.bash
$ run2 run my_pkg my_thread
```
