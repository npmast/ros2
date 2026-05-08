#### subscription.ipynb
* jupyter lab
```c
$ mkdir -p Work/py
$ source /opt/ros/jazzyi/setup.bash or jazzy
$ jupyter lab
- other terminal
$ jazzy
$ ros2 run turtlesim turtlesim_node
$ ros2 topic list
```
외부에서 접속한다(IP:PORT)  
* topic_sub.ipynb
1. 패키지 import
```py
import rclpy import rp
from turtlesim.msg import Pose
import time
```
2. 초기화
```py
if not rp.ok():
    rp.init()
```
3. 노드 생성
```py
node = rp.create_node('subscriber')
```
4. 콜백함수
```py
def pose_callback(msg):
    print(f"x={msg.x: .2f}, y={msg.y: .2f}, theta={msg.theta: .2f}")
```
5. subscriber 객체 생성
```py
sub = node.create_subscription(Pose, '/turtle1/pose', pose_callback, 10)
```
6. 콜백처리
```py
rp.spin_once(node, timeout_sec=0.1)              # 한 번만 콜백 큐 처리
time.sleep(0.1)
```
* rcl 는 ROS2 Client Library  
* rp.init() 는 초기화로 ROS2 네트워크 통신 환경을 설정한다.  
* rp.create_node('pose_subscriber') 는 노드 생성  
* node.create_subscription(Pose, '/turtle1/pose', pose_callback, 10) 은 subscription 객체 생성  
* rp.spin_once(node) 가 DDS 통신, subscriber 이벤트 처리, callback 실행을 수행된다.
```c
$ ros2 node list
/pose_subscriber
/turtlesim
```
