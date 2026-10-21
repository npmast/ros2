1. ros2 실행
> ```
> ros2 run <package_name> <executable_name>
> $ ros2 run turtlesim turtlesim_node        #
2. ros2 노드 목록
> ```
> $ ros2 node list                            # 실행 중인 모든 노드의 목록
> /turtlesim
> $ ros2 run turtlesim turtle_teleop_key
> $ ros2 node list
> /turtlesim
> /teleop_turtle
> ```
> 2.1 리매핑
> - 기본 노드 속성 다시 할당
> ```
> # 새로운 터미널을 열고 명령어를 실행한다.
> $ ros2 run turtlesim turtlesim_node --ros-args --remap __node:=my_turtle
> $ ros2 run ros2 node list
> /my_turtle
> /turtlesim
> /teleop_turtle
> ```
> - 노드 정보 확인
> ```
> ros2 node info <node_name>
> $ ros2 node info /my_turtle
> ```
