#### action
> 액션은 목표, 피드백, 결과로 구성이 된다.  
> 액션은 클라이언트-서버 모델을 사용하며, 퍼블리셔-서브스크라이버 모델과 유사하다.  
> 액션 클라이언트 노드는 액션 서버 노드에 목표를 보내고 액션 서버는 목표를 확인하고 피드백 스트림과 결과를 반환한다.
#### 1. 액션 
```c
terminal 1
$ jazzy
$ ros2 run turtlesim turtlesim_node
terminal 2
$ jazzy
$ ros2 run turtlesim turtle_teleop_key
g|b|v|c|d|e|r|t ==> 3시를 기준으로 45도씩 회전하는 방향키를 누를 때마다 액션 서버에 목표를 보낸다.
```
#### 2. 노드 정보
```c
$ ros2 node info /turtlesim
/turtlesim
  Subscribers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /turtle1/cmd_vel: geometry_msgs/msg/Twist
  Publishers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
    /turtle1/color_sensor: turtlesim/msg/Color
    /turtle1/pose: turtlesim/msg/Pose
  Service Servers:
    /clear: std_srvs/srv/Empty
    /kill: turtlesim/srv/Kill
    /reset: std_srvs/srv/Empty
    /spawn: turtlesim/srv/Spawn
    /turtle1/set_pen: turtlesim/srv/SetPen
    /turtle1/teleport_absolute: turtlesim/srv/TeleportAbsolute
    /turtle1/teleport_relative: turtlesim/srv/TeleportRelative
    /turtlesim/describe_parameters: rcl_interfaces/srv/DescribeParameters
    /turtlesim/get_parameter_types: rcl_interfaces/srv/GetParameterTypes
    /turtlesim/get_parameters: rcl_interfaces/srv/GetParameters
    /turtlesim/list_parameters: rcl_interfaces/srv/ListParameters
    /turtlesim/set_parameters: rcl_interfaces/srv/SetParameters
    /turtlesim/set_parameters_atomically: rcl_interfaces/srv/SetParametersAtomically
  Service Clients:
  Action Servers:
    /turtle1/rotate_absolute: turtlesim/action/RotateAbsolute
  Action Clients:
```
> Action Servers 에 trutle1/rotate_absolute 액션은 turtlesim이 /turtle1/rotate_absolute 액션에 응답하고 피드백을 제공한다.
```c
$ ros2 node info /teleop_turtle
/teleop_turtle
  Subscribers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
  Publishers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
    /turtle1/cmd_vel: geometry_msgs/msg/Twist
  Service Servers:
    /teleop_turtle/describe_parameters: rcl_interfaces/srv/DescribeParameters
    /teleop_turtle/get_parameter_types: rcl_interfaces/srv/GetParameterTypes
    /teleop_turtle/get_parameters: rcl_interfaces/srv/GetParameters
    /teleop_turtle/list_parameters: rcl_interfaces/srv/ListParameters
    /teleop_turtle/set_parameters: rcl_interfaces/srv/SetParameters
    /teleop_turtle/set_parameters_atomically: rcl_interfaces/srv/SetParametersAtomically
  Service Clients:
  Action Servers:
  Action Clients:
    /turtle1/rotate_absolute: turtlesim/action/RotateAbsolute
```
> /teleop_turtle 노드는 액션 클라이언트 아래에 /turtle1/rotate_absolute 액션을 가지고 있다.
> 이는 이 액션 이름에 대한 목표를 액션 서버에 보낸다.
```c
$ ros2 action list -t
/turtle1/rotate_absolute [turtlesim/action/RotateAbsolute]
$ ros2 action info /turtle1/rotate_absolute
Action: /turtle1/rotate_absolute
Action clients: 1
    /teleop_turtle
Action servers:  1
    /turtlesim
$ ros2 interface show turtlesim/action/RotateAbsolute
# The desired heading in radians                # 원하는 각도
float32 theta
---
# The angular displacement in radians to the starting position    # 시작 위치로의 각도 이동량
float32 delta
---
# The reamining rotation in radians            # 남은 회전량(피드백)
float32 remaining
```
#### 3. 액션 실행
> 1.57 라디안(약 90도 회전) 회전 목표
```c
$ ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 1.57}"
Waiting for an action server to become available...
Sending goal:                                                # 서버로 전송
   theta: 1.57

Goal accepted with ID: f8db8f44410849eaa93d3feb747dd444      # 고유 ID 부여하고 작업 시작

Result:                                                      # 최종 결과 반환
  delta: -1.568000316619873                                  # 처음 위치에서 얼마나 회전했는지 결과 반환

Goal finished with status: SUCCEEDED                         # 작업 종료 상태

```
