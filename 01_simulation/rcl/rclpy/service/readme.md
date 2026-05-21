### 서비스
> 서비스 서버(요청을 기다림 + 응답 반환)    
> 서비스 클라이언트(요청 전송 + 응답 수신)  
#### turtlesim 서비스 테스트  
```py
$ ros2 run turtlesim turtlesim_node
$ ros2 service list
/turtle1/teleport_absolute
/clear
/reset
$ ros2 service call /turtle1/teleport_absolute turtlesim/srv/TeleportAbsolute "{x: 5.0, y: 5.0, theta: 0.0}"
```
