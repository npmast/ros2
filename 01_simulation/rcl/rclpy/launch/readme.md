### Launch
> 여러 노드 한 번에 실행  
> 이동 로봇는 센서 드라이버, 로봇 상태 발행기, 제어 노드, 위치 추정 노드, 지도 서버, Nav2 노드, RViz 등을 함께 실행해야 한다.  
> 이 문제를 해결하는 것이 launch 이다.  
#### launch  
```c
- launch 파일 실행: ros2 launch [패키지이름] [launch파일이름]
$ ros2 launch turtlesim multisim.launch.py
- 인자 확인: ro2 launch [패키지이름] [launch파일이름] --show-args
```
