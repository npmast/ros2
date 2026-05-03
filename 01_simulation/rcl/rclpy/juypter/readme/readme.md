#### jupyter lab  
```c
$ jazzy
$ mkdir -p Work/py
$ source /opt/ros/jazzyi/setup.bash or jazzy
$ jupyter lab
```
외부에서 접속한다(IP:PORT)  
rclpy 와 Pose 를 import 하고 실행해 본다.
<img width="1211" height="714" alt="Image" src="https://github.com/user-attachments/assets/350d4d63-1d34-4424-aee2-4221e4d1986f" />
* rcl 는 ROS2 Client Library  
* rp.init() 는 초기화로 ROS2 네트워크 통신 환경을 설정한다.  
* rp.create_node('my_node') 는 노드 생성  
* node.create_subscription(Pose, '/turtle1/pose', pose_callback, 10) 은 subscription 노드 생성  
* rp.spin_once(node) 가 DDS 통신, subscriber 이벤트 처리, callback 실행을 수행된다.  
