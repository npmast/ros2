##### service_client.ipynb
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
/turtle1/teleport_absolute [turtlesim/srv/TeleportAbsolute]    # /서비스명 [패키지명/srv/서비스타입] 
~
$ ros2 interface show turtlesim/srv/TeleportAbsulute
float32 x
float32 y
float32 theta
---
```
* jupyter
  1. 
* future = call_async(request): 비동기 서비스 요청
  rp.spin_future_complete(node, future)
