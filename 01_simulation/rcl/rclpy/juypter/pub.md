#### publisher

<img width="1206" height="908" alt="Image" src="https://github.com/user-attachments/assets/cc328921-34de-4d16-8394-6790aeb59e98" />
<img width="1199" height="689" alt="Image" src="https://github.com/user-attachments/assets/4a7c21cb-7de5-482a-a5fa-d2261db071a4" />  

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
