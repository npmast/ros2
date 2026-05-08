## VMware
##### 1. 워크스페이스 폴더 생성
```c
$ mkdir -p ~/ros2_ws/src  
$ cd ~/ros2_ws
```  
##### 2. 빌드 테스트
```c
$ colcon build  
$ ls  
// build/ install/ log/ 폴더가 추가로 만들어 진다.  
```
##### 3. 환경 등록  
```c
$ ls install  
// install 폴더안에 setup.bash 파일이 들어 있다.  
$ source install/setup.bash
```
##### 4. 패키지 생성  
```c
$ cd src  
$ ros2 pkg create robot_control --build-type ament_python --dependencies rclpy std_msgs  
// 패키지 이름은 robot_control, 빌드 타입은 ament_python 의존성은 rclpy 라이브러리와 표준 데이터 형식으로 설정한다.  
$ ls  
// 성공적으로 실행되면 robot_control 폴더가 생성되고 그 폴더안에  
// package.xml resource robot_control setup.cfg setup.py test 가 만들어 진다.  
// ros2_ws/src 폴더에서 tree 실행하면 계층적으로 보여준다.  
```
##### 5. 노드 생성  
$ cd ~/ros2_ws/src/robot_control/robot_control  
$ nano led_commander.py
``` py
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class LedCommander(Node):
    def __init__(self):
        super().__init__('led_commander')

        self.publisher_ = self.create_publisher(String, 'led_cmd', 10)
        self.timer = self.create_timer(2.0, self.timer_callback)

        self.state = False

    def timer_callback(self):
        msg = String()
        msg.data = 'ON' if self.state else 'OFF'

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publish: {msg.data}')

        self.state = not self.state


def main(args=None):
    rclpy.init(args=args)
    node = LedCommander()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```
##### 6. 실행 등록  
$ cd ~/ros2_ws/src/robot>control  
$ nano setup.py  
entry_points 부분 찾아서 수정한다.  
```py
entry_points={
    'console_scripts': [
        'led_commander = robot_control.led_commander:main',
    ],
},
```
##### 7. 빌드  
$ cd ~/ros2_ws  
$ colcon build  
Starting >>> robot_control  
Finished <<< robot_control  
##### 8. 환경 적용 및 실행  
$ source install/setup.bash  
$ ros2 run robot_control led_commander   
``` py
[INFO] [~~] : Publisc: ON  
[INFO] [~~] : Publisc: OFF  
```
##### 9. 토픽 확인  
새로운 터미널을 연다.   
$ jazzy  
$ source ~/ros2_ws/install/setup.bash  
$ ros2 topic list   
``` py
/led_cmd  
/paraeter_events  
/rosout
```
$ ros2 topic echo /let_cmd  
``` py
data: 'ON'  
---  
daga: 'OFF'  
---
```

