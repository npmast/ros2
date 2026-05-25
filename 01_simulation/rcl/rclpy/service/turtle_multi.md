#### 1. degree & radian
> - 원의 한바퀴  
> degree: 360°  
> radian: 2π  
> - 1 라디안: 원주 호의 길이가 반지름과 같을 때(57.2958...)  
> - 반지름이 1일 때 반원의 둘레는 π(3.141592...) radians == 180°  
  1° degree: π / 180(1° x 180 = π)  
  1 radians: 180 / π(1rad x π = 180)  
```py
import numpy as np
to_degree = 180 / np.pi
to_radian = np.pi / 180

angle_step = 2 * np.pi / num_turtles          # 터틀심 각도 간격 계산
```
