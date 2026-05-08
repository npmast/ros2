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
<img width="754" height="484" alt="Image" src="https://github.com/user-attachments/assets/98744bd4-ff93-4b95-992b-e83dba1a3b8c" />

  - future: 응답 결과를 저장하는 객체  
