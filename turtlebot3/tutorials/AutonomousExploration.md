### Autonomous Exploration
> __Frontier 탐색 알고리즘__  
> 가장 가까운 Frontier 1개를 찾아 Nav2 Goal로 보낸다.  
> 즉 Free(백색) 격자와 Unknown(회색) 격자가 맞닿는 경계점(Frontier)들을 찾아 목표점을 설정하고 목적지로 이동, 스캔하여 지도를 업데이트 한다.
> ```c
> 100 : 장애물
> 0 : 빈 공간
> -1 : 미 탐색
>
> 예를 들어 OccupancyGrid 값이 
> 0  0  0  0  0
> 0  0  0 -1 -1
> 0  0  0 -1 -1
> 같을 때 여기서 0 옆에 -1 이 있는 지점이 Frontier 이다.
> ```
> Nav2 --> cmd_vel --> TurtleBot3  
> | 구성요소          | 역할          | 필수 여부 |  
  | --                | --           | --        |  
  | SLAM              | 지도 생성     | 필수     |  
  | Nav2              | 목표까지 이동  | 필수    |  
  | Frontier Explorer | 탐색 목표 선정 | 필수    |  
  | RViz              | 상태 확인      | 선택    |  

#### 1. 패키지 만들기
```c
$ ~/ros2_ws/src
$ ros2 pkg create --build-type ament_python frontier_explorer --dependcies rclpy nav_msgs geometry_msgs nav2_msgs
```
> * 또는 기존 my_pkg 에 작성하고 나중에 독립 패키지로 분리한다.  
> $ nano ~/ros2_ws/src/my_pkg/frontier_explorer.py 에 작성한다.
#### 2. frontier_explorer_node
> 1. 코드 작성
```py
$ cd ~/ros2_ws/src/frontier_explorer/frontier_explorer
$ nano frontier_explorer_node.py
import rclpy
from rclpy.node import Node

from nav_msgs.msg import OccupancyGrid
from nav2_msgs.action import NavigateToPose
from rclpy.action import ActionClient


class FrontierExplorer(Node):
    def __init__(self):
        super().__init__('frontier_explorer')

        self.map_sub = self.create_subscription(
            OccupancyGrid,
            '/map',
            self.map_callback,
            10
        )

        self.nav_client = ActionClient(
            self,
            NavigateToPose,
            'navigate_to_pose'
        )

        self.goal_sent = False

        self.get_logger().info('Frontier Explorer started')

    def map_callback(self, msg):
        self.get_logger().info('Map received')
        if self.goal_sent:
            return

        frontier = self.find_frontier(msg)

        if frontier is None:
            self.get_logger().info('No frontier found')
            return

        world_x, world_y = frontier
        self.send_goal(world_x, world_y)

    def find_frontier(self, map_msg):
        width = map_msg.info.width
        height = map_msg.info.height
        resolution = map_msg.info.resolution

        origin_x = map_msg.info.origin.position.x
        origin_y = map_msg.info.origin.position.y

        data = map_msg.data

        for y in range(1, height - 1):
            for x in range(1, width - 1):
                idx = y * width + x

                # 0 : 이동 가능한 공간
                if data[idx] != 0:
                    continue

                neighbors = [
                    (x + 1, y),
                    (x - 1, y),
                    (x, y + 1),
                    (x, y - 1)
                ]

                for nx, ny in neighbors:
                    nidx = ny * width + nx

                    # -1 : 아직 모르는 공간
                    if data[nidx] == -1:
                        world_x = origin_x + x * resolution
                        world_y = origin_y + y * resolution

                        return world_x, world_y

        return None

    def send_goal(self, x, y):
        self.get_logger().info(f'Sending goal: x={x:.2f}, y={y:.2f}')

        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.header.frame_id = 'map'
        goal_msg.pose.header.stamp = self.get_clock().now().to_msg()

        goal_msg.pose.pose.position.x = x
        goal_msg.pose.pose.position.y = y
        goal_msg.pose.pose.orientation.w = 1.0

        self.nav_client.wait_for_server()

        self.goal_sent = True
        self.nav_client.send_goal_async(goal_msg)


def main(args=None):
    rclpy.init(args=args)

    node = FrontierExplorer()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```
> 2. setup.py 수정
```c
$ cd ~/ros2_ws/src/frontier_explorer
$ nano setup.py
entry_points={
    'console_scripts': [
        'frontier_explorer_node = frontier_explorer.frontier_explorer_node:main',
    ],
},
```
> 3. build
```c
$ cd ~/ros2_ws
$ colcon build --packages-select frontier_explorer
$ source install/setup.bash
```
#### 3. SBC bringup
```c
$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_bringup robot.launch.py
```
#### 4. remote PC 
##### 1. SLAM
```c
$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=false
```
##### 2. Nav2 실행
```c
$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=false
$ ros2 action list
/navigate_to_pose 가 있어야 한다.
```
##### 3. RViz
```c
$ rviz2
fixed Frame: map
Map
LaserScan
TF
RobotModel
Odometry
```
##### 4. 자동 탐색 노드
```c
$ cd ~/ros2_ws
$ source install/setup.bash
$ ros2 run frontier_explorer frontier_explorer_node
```
