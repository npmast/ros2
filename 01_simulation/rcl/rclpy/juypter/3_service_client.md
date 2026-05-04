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
/turtle1/teleport_absolute [turtlesim/srv/TeleportAbsolute]
~
$ ros2 interface show turtlesim/srv/TeleportAbsulute
float32 x
float32 y
float32 theta
---
```
<img width="965" height="876" alt="Image" src="https://github.com/user-attachments/assets/3169d44d-f23c-4441-877f-341adda44720" />
