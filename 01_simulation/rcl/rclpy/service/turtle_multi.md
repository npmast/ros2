#### 1. degree & radian
> - 원의 한바퀴  
> degree: 360°  
> radian: 2π  
> - 1 라디안: 원주 호의 길이가 반지름과 같을 때(57.2958...)  
> - 반지름이 1일 때 반원의 둘레는 π radians = 180°
  2π rad = 360  
  rad: 각도 x (π / 180)  
  deg: rad X (180 / π)
> 원 반지름이 r 일 때
  x 좌표 = r x con(θ), y 좌표 = r x sin(θ)

#### 2. jypyter lab
```py
import numpy as np
to_degree = 180 / np.pi
to_radian = np.pi / 180

num_turtles = 3
angle_step = 2 * np.pi / num_turtles          # 터틀심 각도 간격 계산

angle_step                             # radians

angle_step * to_degree                # degree

theta = [angle_step * n for n in range(num_turtles)]     # 리스트 컴프리헨션
theta

'''
theta = []                                # 이것과 같다.
for n in range(num_turtles):
    theta.append(angle_step * n)
theta

num_turtles = 4
angle_step = 90

theta = []                                
for n in range(num_turtles):
    theta.append(angle_step * n)
theta
'''
[each * to_degree for each in theta]
'''
result = []                              # 같다.
for each in theta:
    result.append(each * to_degree)

import math
theta = [0, math.pi/2, math.pi]
to_degree = 180 / math.pi
degree_list = [each * to_degree for each in theta]
print(degree_list)
'''
r = 3.5
x = [r * np.cos(th) for th in theta]               # x 좌표 계산
y = [r * np.sin(th) for th in theta]               # y 좌표 계

x

y

import matplotlib.pyplot as plt

plt.scatter(x, y)
plt.axis('equal')
!pip install --upgrade matplotlib-inline ipython         # 커널 재 시작

def calc_position(n, r):
    angle_step = 2 * np.pi / n
    theta = [angle_step * n for n in range(n)]
    x = [r*np.cos(th) for th in theta]
    y = [r*np.sin(th) for th in theta]
    return x, y, theta

calc_position(4, 3)

def draw_pos(x, y):
    plt.scatter(x, y)
    plt.axis('equal')
    plt.show()

X, Y, theta = calc_position(15, 3)
draw_pos(X, Y)
```
#### 3. my_service_server.py
```py
$ ~/ros2_ws/src/my_pkg/my_pkg
$ nano my_service_server.py
from my_pkg_msgs.srv import MultiSpawn
import rclpy as rp
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute
from turtlesim.srv import Spawn
import numpy as np
import time

class MultiSpawning(Node):
    def __init__(self):
        super().__init__('multi_spawn')
        self.server = self.create_service(
            MultiSpawn,                         # 서비스 타입
            'multi_spawn',                      # 서비스 이름
            self.callback_service
        )
        self.teleport = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
        self.spawn = self.create_client(Spawn, '/spawn')
        self.req_teleport = TeleportAbsolute.Request()
        self.req_spawn = Spawn.Request()
        self.center_x = 5.54
        self.center_y = 5.54

    def calc_position(self, n, r):
        angle_step = 2. * np.pi / n
        theta = [angle_step * n for n in range(n)]
        x = [r * np.cos(th) for th in theta]
        y = [r * np.sin(th) for th in theta]
        return x, y, theta

    def callback_service(self, request, response):
        x, y, theta = self.calc_position(request.num, 3)
        for n in range(len(theta)):
            self.req_spawn.x = x[n] + self.center_x
            self.req_spawn.y = y[n] + self.center_y
            self.req_spawn.theta = theta[n]
            self.spawn.call_async(self.req_spawn)
        response.x = x
        response.y = y
        response.theta = theta
        return response

def main(args=None):
    rp.init(args=args)
    multi_spawn = MultiSpawning()
    rp.spin(multi_spawn)
    rp.shutdown()

if __name__ == "__main__":
    main()

```
#### 4. build 및 실행
```py
$ cd ~/ros2_ws
$ colcon build --s
$ source install/setup.bash
$ ros2 run turtlesim turtlesim_node
teminal 2
$ source install/setup.bash
$ ros2 run my_pkg my_service_server
teminal 3
$ source install/setup.bash
$ ros2 service call /multi_spawn my_pkg/srv/MultiSpawn "{num: 9}"
```
