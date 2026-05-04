##### 서비스 클라이언트  
* 터미널 1
```c
$ jazzy
$ ros2 run turtlesim turtlesim_node
```
* 터미널 2
```c
$ jazzy
$ source ~/venvs/.venv/bin/activate
$ jupyter lab
```
* 터미널 3
```c
$ jazzy
$ ros2 service list -t
~
/turtle1/teleport_absolute [turtlesim/srv/TeleportAbsolute]
~
$ ros2 interface show turtlesim/srv/TeleportAbsulute
float32 x
float32 y
float32 theta
---
```
