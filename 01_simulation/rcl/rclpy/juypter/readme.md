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
  > * node.create_subscription(msg_type, topic, callback, qos_profile): 새로운 구독자 생성  
  > * node.create_publishers(msg_type, topic, gos_profile, callback, events_callbacks): 새로은 게시자 생성  
  > * node.create_client(srv_type, srv_name): 새로운 클라이언트 생성
  > * node.create_service(src_type, srv_name, callback, qos_profile): 새 서비스 서버 생성  
* rp.spin_once(node) 가 DDS 통신, subscriber 이벤트 처리, callback 실행을 수행된다.  
  node를 실행한다.  
* 자동완성 설정  
Settings → Settings Editor → Code Completion  
Enable autocompletion 체크
python3 -m pip install -U jedi ipykernel jupyterlab
