#### 노드(Node)
: 연산을 수행하는 최소 단위의 프로세스로 수 많은 노드들의 집합으로 하나의 로봇 시스템이 만들어 진다.  
즉 로붓 시스템의 구성은 노드들로 이루어진다. 모터 제어 노드, 라이다(LiDAR) 노드, 카메라 노드, 네비게이션 노드, 센서 융합 노드 등이 하나의 기능을 담당하고  서로 필요한 정보를 통신으로 주고 받는다. 노드는 실제 실행 파일이다.  
* 실행 명령: ros2 run [PKG] [NODE]
```c
ros2 run turtlesim turtlesim_node
```
#### 패키지(Package)
: 노드들과 설정 파일들의 폴더 또는 컨테이너 
#### 노드 통신
1. **토픽**(Topic) : 기본적인 통신 방식
   노드 간에 데이터를 주고 받는 단방향 통신으로 일대일, 다대일, 다대다 통신이 가능하다.
   특정 채널(토픽)에 데이터를 지속적으로 흘려보내면 그 채널을 구독하여 데이터를 받는다.  
   * Publisher(발행자): 특정 주제(Topic)에 메시지를 발행하는 노드
   * Subscriber(구독자): 특정 주제(Topic)에 메시지를 받는 노드
   * 인터페이스: msg
   * 실행
```c
   $ ros2 run turtlesim turtlesim_node  
   - other terminal open
   $ ros2 node list -t                   // t: 데이터 타입도 출력한다. v: 구분 정보 출력  
   $ ros2 node info /turtlesim
```
   * 카메라 스트리밍/라이다 포인트 클라우드/ IMU 센서 데이터/로봇 속도  
3. **서비스**(service)
   클라이언트 노드와 서버 노드간에 **요청**(request)과 **응답**(response)으로 이루어지는 통신 방식.
   요청과 응답 메시지에는 각 데이터 타입이 존재한다.
   * 인터페이스: srv
   * 실행: *service list - service type - interface show - service call*
```c
   $ ros2 run turtlesim turtlesim_node

   * other terminal open 
   $ ros2 service list                                                // 서비스 목록 확인. info 를 이용해도 된다.  
   $ ros2 service type /turtle1/teleport_absolute                     // 해당 서비스 타입 확인
   turtlesim/srv/TeleportAbsolute
   $ ros2 interface show turtlesim/srv/TeleportAbsolute/              // 해당 서비스 타입의 데이터 타입
   float32 x
   float32 y
   float32 theta
   ---  
   $ ros2 service call /turtle2/teleport_absolute turtlesim/srv/TeleportAbsolute "{x: 3, y: 7, theta: 0}"                  // 서비스 콜: 이동

   * reset service
   $ ros2 service list
   $ ros2 service type /reset
   std_srvs/srv/Empty
   $ ros2 interface show std/srvs/srv/Empty
   ---
   $ ros2 service call /reset std_srvs/srv/Empty {}
   $ ros2 service call /spawn turtlesim/srv/Spawn "{x: 2, y: 5, theta: 0, name: ''}"      // 터틀2 생성  
   $ ros2 service list                                                // turtlesim2가 보인다.
   $ ros2 service call /turtle2/teleport_absolute turtlesim/srv/TeleportAbsolute "{x: 5, y: 5, theta: 0}"
```
   * 모터 활성화/좌표 변환/파라미터 변경  
5. **액션**(Action)
   토픽과 서비스의 장점을 결합한 통신이다. 클라이언트가 목표를 보내면, 서버는 작업을 수행하면서 중간에 피드백을 전송하고, 완료 시 결과를 반환한다.
   취소가 가능하며 작업을 안전하게 관리할 수 있다.
   * 인터페이스: action
   * 실행
```c
     $ ros2 action list
     $ ros2 action list -t
     $ ros2 interface show turtlesim/action/RotateAbsolute
     $ ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 3.14}"
```
   * 내비게이션 이동/로봇 팔 궤적/맵 빌딩/음성 인식 및 응답  

     
