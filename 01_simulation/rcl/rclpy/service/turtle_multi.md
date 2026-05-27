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

#### jypyter lab
```py
import numpy as np
to_degree = 180 / np.pi
to_radian = np.pi / 180

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

