#### publisher.ipynb  
1. 패키지 import
```py
import rclpy as rp
from geometry_msgs.msg import Twist         # 속도
import time
```
2. 초기화
```pr
if not rp.ok():
    rp.init()
```
3. Twist 객체 생성
```py
msg = Twist()                                 # Twist 객체 생성
print(msg)                                    # turtlesim1의 속도 정보가 들어있다.
```
4. 속도 변경
```py
msg.linear.x = 2.5
msg.angular.z = 2.5
msg
```
5. 노드 생성
```py
node = rp.create_node('publisher')            # publisher 이름 속성의 node 생성
```
6. 퍼블리셔 객체 생성
```py
# 메시지 타입, 토픽명, QoS
pub = node.create_publisher(Twist, '/turtle1/cmd_vel', 10)      # 퍼블리셔 객체 생성
```
7. 전진/회전/곡선/반복
```py
msg.linear.x = 2.0
msg.angular.z = 0.0
pub.publish(msg)
print('Forward')

msg.linear.x = 2.0
msg.angular.z = 0.0
pub.publish(msg)
print('Forward')

msg.linear.x = 2.0
msg.angular.z = 1.0
pub.publish(msg)
print('Curve')

msg.linear.x = 0.5
msg.angular.z = 1.0
for _ in range(10):
    pub.publish(msg)
    time.sleep(0.5)
print('Repeat')
```
* node = ROS2 프로세서의 기본 컨테이너  
* 'publisher': 노드 이름  
* __생성한 node 안에 publisher 기능을 추가한 객체 pub 생성__    
  ROS2는 DDS 기반 분산 시스템이라 누가 요청하는지, 어떤 QoS인지, 어떤 namespace 인지가 Node에 등록되어야 한다.  
  - _노드를 먼저 생성하고 기능을 담당할 객체를 생성한다._  
* Node 소속 기능 객체 생성  
  - Publisher  
  pub = node.create_publisher(...)  
  - Subcriber  
  sub = node.create_subscription(...)  
