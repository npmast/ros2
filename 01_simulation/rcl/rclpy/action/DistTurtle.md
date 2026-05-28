### 액션 정의 만들기
#### 1.
```c
$ cd ~/ros2_ws/src/my_pkg_msgs
$ mkdir action
$ nano action/DistTurtle.action
# Request
float32 linear_x
float32 angular_z
float32 dist
---
# Result
float32 pos_x
float32 pos_y
float32 pos_theta
float32 result_dist
---
# Feedback
float32 remained_dist
```
