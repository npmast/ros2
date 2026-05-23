### Parameters
> 파라미터는 노드의 설정 값이다.
> 노드는 자신의 설정된 파라미터를 유지한다.
#### 1. 
```c
terminal 1
$ jazzy
$ ros2 run turtlesim turtlesim_node
terminal 2
$jazzy
$ ros2 run turtlesim turtle_teleop_key
terminal 3
$ jazzy
$ ros2 param list
/teleop_turtle:
  qos_overrides./parameter_events.publisher.depth
  qos_overrides./parameter_events.publisher.durability
  qos_overrides./parameter_events.publisher.history
  qos_overrides./parameter_events.publisher.reliability
  scale_angular
  scale_linear
  use_sim_time
/turtlesim:
  background_b
  background_g
  background_r
  qos_overrides./parameter_events.publisher.depth
  qos_overrides./parameter_events.publisher.durability
  qos_overrides./parameter_events.publisher.history
  qos_overrides./parameter_events.publisher.reliability
  use_sim_time
```
#### 2. param get
```c
$ ros2 param get /turtlesim backgrount_g
Integer value is: 86
$ ros2 param get /turtlesim backgrount_r
Integer value is: 69
```
#### 3. param set
```c
$ ros2 param set /turtlesim backgrount_r 150
Set parameter successful              # 터틀심 창의 배경색이 변경된다.
```
