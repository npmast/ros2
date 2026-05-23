### 서비스
> 서비스는 토픽의 발행자-구독자 모델 대신 호출-응답 모델을 기반으로 한다.  
> 서비스 서버(요청을 기다림 + 응답 반환)  
> 서비스 클라이언트(요청 전송 + 응답 수신)
> 서비스는 클라이언트가 특정적으로 호출할 때만 데이터를 제공한다.
#### turtlesim 서비스 테스트  
```py
$ ros2 run turtlesim turtlesim_node
$ ros2 run turtlesim turtle_teleop_key
$ ros2 service list
$ ros2 service list
/clear
/kill
/reset
/spawn
/teleop_turtle/describe_parameters
/teleop_turtle/get_parameter_types
/teleop_turtle/get_parameters
/teleop_turtle/list_parameters
/teleop_turtle/set_parameters
/teleop_turtle/set_parameters_atomically
/turtle1/set_pen
/turtle1/teleport_absolute
/turtle1/teleport_relative
/turtlesim/describe_parameters
/turtlesim/get_parameter_types
/turtlesim/get_parameters
/turtlesim/list_parameters
/turtlesim/set_parameters
/turtlesim/set_parameters_atomically
$ ros2 service type /clear              // clear 서비스 유형  
std_srvs/srv/Empty
$ ros2 service type /spawn
turtlesim/srv/Spawn
$ ros2 interface show turtlesim/srv/Spawn
float32 x
float32 y
float32 theta
string name                       # 선택적. 이 값이 비어 있으면 고유한 이름이 생성되고 반환됩니다.
---
string name
#### 서비스 호출
$ ros2 service call /spawn turtlesim/srv/Spawn "{x: 2, y: 2, theta: 0.2, name: ''}"
requester: making request: turtlesim.srv.Spawn_Request(x=2.0, y=2.0, theta=0.2, name='')

respon:
turtlesim.srv.Spawn_Response(name='turtle2')

$ ros2 service call /turtle1/teleport_absolute turtlesim/srv/TeleportAbsolute "{x: 5.0, y: 5.0, theta: 0.0}"
```
