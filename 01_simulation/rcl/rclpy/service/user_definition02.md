### service server 만들기
#### 1. 
```py
$ cd ~/ros_ws/src/my_pkg/my_pkg
$ nano my_service_server.py
from my_pkg_msgs.srv import MultiSpawn
import rclpy as rp
from rclpy.node import Node

class MultiSpawning(Node):
	def __init__(self):
		super().__init__('multi_spawn')
		self.server = self.create_service(
			MultiSpawn,
			'multi_spawn',
			self.callback_service
		)

	def callback_service(self, request, response):
		print('Request: ', request)

		response.x = [1., 2., 3.]
		response.y = [10., 20., 30.]
		response.theta = [100., 200., 300.]
		return response
		
def main(args=None):
	rp.init(args=args)
	multi_spawn = MultiSpawning()
	rp.spin(multi_spawn)
	rp.shutdown()

if __name__ == "__main__":
	main()
```
#### 2.
```c
nano ~/ros2_ws/src/my_pkg/setup.py
    entry_points={
        'console_scripts': [
            'my_node = my_pkg.my_node:main',
            'my_subscriber = my_pkg.my_subscriber:main',
            'my_publisher = my_pkg.my_publisher:main',
			'turtle_vel = my_pkg.turtle_vel:main',
            'my_service_server = my_pkg.my_service_server:main'    <== 수정
        ],
    },
```
#### 3. build
```c
$ colcon build --packages-select my_pkg
```
#### 4. 실행
```c
terminal 1
$ source ~/ros2_ws/install/setup.bash
$ ros2 run my_pkg my_service_server
terminal 2
$ source ~/ros2_ws/install/setup.bash
$ ros2 service call /multi_spawn my_pkg_msgs/srv/MultiSpawn "{num: 1}"
```
