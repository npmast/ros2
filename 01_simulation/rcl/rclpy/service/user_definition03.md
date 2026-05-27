#### 1. teleport_absolute 클라이언트
> 주석 처리 후 다음 코드 작성
```
$ nano ~/ros2_ws/src/my_pkg/my_pkg/my_service_server.py

from my_pkg_msgs.srv import MultiSpawn
import rclpy as rp
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute

class MultiSpawning(Node):
	def __init__(self):
		super().__init__('multi_spawn')
		self.server = self.create_service(
			MultiSpawn,							  # 서비스 타입
			'multi_spawn',						# 서비스 이름
			self.callback_service
		)
		self.teleport = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
		self.req_teleport = TeleportAbsolute.Request()

	def callback_service(self, request, response):
		self.req_teleport.x = 1.
		self.req_teleport.y = 1.
		self.teleport.call_async(self.req_teleport)
		return response
		
def main(args=None):
	rp.init(args=args)
	multi_spawn = MultiSpawning()
	rp.spin(multi_spawn)
	rp.shutdown()

if __name__ == "__main__":
	main()
```
#### 2. 실행
```c
terminal 1
$ cd ~/ros2_ws
$ colcon build --packages-select my_pkg
$ source install/setup.bash
$ ros2 run turtlesim turtlesim_node
terminal 2
$ cd ~/ros2_ws
$ source install/setup.bash
$ ros2 run my_pkg my_service_server
terminal 3
$ cd ~/ros2_ws
$ source install/setup.bash
$ ros2 service call /multi_spawn my_pkg_msgs/srv/MultiSpawm "{num: 1}"
```
