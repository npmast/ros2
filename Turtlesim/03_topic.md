1. 실행
- 터미널 열고
```
$ ros2 run turtlesim turtlesim_node
```
- 다른 터미널 열고
```
$ ros2 run tutlesim turtle_teleop_key
```
2. rqt
- 새 터미널 열고 실행
```
$ ros2 run rqt
```
> Plugins > Introspection > Node Graph  
> 이 그래프는 /trutlesim 노드와 /teleop_turtle 노드가 토픽을 통신하는 방법을 보여준다.  
> /teleop_turtle 노드는 토픽에 데이터를 게시하고 /turtle1/cmd_vel, /turtlesim 노드는 해당 토픽을 구독하여 데이터를 수신한다.  
3. ros2 토픽 목록
새로운 터미널에 실행한다.
```
$ ros2 topic list
$ ros2 topic list -t                      # data의 type을 알려준다.
```
rgt 의 hiden 을 선택 해제한다.  
4. ros2 Topic 에코
```
ros2 topic echo <topic_name>
$ ros2 topic echo /turtle1/cmd_vel
```
turtle_teleop_key 화살표 키를 사용해 거북이를 움직이면 위치 데이터가 표시된다.  
rqt의 debug 체크를 해제한다.  
5. ros2 topic info
```
$ ros2 topic info /turtle1/cmd_vel
```
5-1. ros2 topic 정보 - 상세 표시 플래그 사용(--verbose)
```
$ ros2 topic info /turtle11/cmd_vel --verbose
```
6. ros2 interface
```
$ ros2 topic list -t cmd_vel
geometry_msgs/msg/Twist
$ ros2 interface show geometry_msgs/msg/Twist
# This expresses velocity in free space broken into its linear and angular parts.
    Vector3  linear
            float64 x
            float64 y
            float64 z
    Vector3  angular
            float64 x
            float64 y
            float64 z
# 
