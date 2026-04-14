#### 노드(Node)
: 연산을 수행하는 최소 단위의 프로세스로 수 많은 노드들의 집합으로 하나의 로봇 시스템이 만들어 진다.  
즉 로붓 시스템의 구성은 노드들로 이루어진다. 모터 제어 노드, 라이다(LiDAR) 노드, 카메라 노드, 네비게이션 노드, 센서 융함 노드 등이 하나의 기능을 담당하고  서로 필요한 정보를 통신으로 주고 받는다. 노드는 실제 실행 파일이다.  
* 실행 명령: ros2 run [PKG] [NODE]
```c
ros2 run turtlesim turtlesim_node
```
#### 패키지(Package)
: 노드들과 설정 파일들의 폴더 또는 컨테이너 
#### 노드 통신
1. 토픽(Topic)
   노드 간에 데이터를 주고 받는 단방향 통신으로 일대일, 다대일, 다대다 통신이 가능하다.
   * Publisher(발행자): 특정 주제(Topic)에 메시지를 발행하는 노드
   * Subscriber(구독자): 특정 주제(Topic)에 메시지를 받는 노드
   * 실행  
     $ ros2 run turtlesim turtlesim_node  
     다른 터미널을 연다.  
     $ ros2 node list -t // t: 데이터 타입도 출력한다. v: 구분 정보 출력  
     $ ros2 node info /turtlesim
2. 서비스(service)
   클라이언트 노드와 서버 노드간에 요청(request)과 응답(response)으로 이루어지는 통신 방식 요청과  
   응답 메시지에는 데이터 타입이 존재한다.
   * 실행  
     $ ros2 run turtlesim turtlesim_node  
     - 새로운 터미널을 연다.  
     $ ros2 service list                                                  // 서비스 목록 확인. info 를 이용해도 된다.  
     $ ros2 service type /turtle1/teleport_absolute                                            // 서비스 타입 확인  
     $ ros2 interface show turtlesim/srv/TeleportAbsolute                                      // 타입 확인  
     $ ros2 service call /turtle2/teleport_absolute turtlesim/srv/TeleportAbsolute "{x: 3, y: 7, theta: 0}"     // 이동  
     $ ros2 service call /spawn turtlesim/srv/Spawn "{x: 2, y: 5, theta: 0, name: ''}"                  // 터틀2 생성  
     $ ros2 service list           // turtlesim2가 보인다.
     $ ros2 service call /turtle2/teleport_absolute turtlesim/srv/TeleportAbsolute "{x: 5, y: 5, theta: 0}"
4. 액션(Action)
   * 실행
     $ ros2 action list
     $ ros2 action list -t
     $ ros2 interface show turtlesim/action/RotateAbsolute
     $ ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 3.14}"

     
