#### 1. 패키지  
```c
/opt/ros/jazzy/share/example_interfaces/srv/AddTwoInts                        
$ ros2 interface show example_interfaces/srv/AddTwoInts
int64 a                // 요청
int64 b                
---
int64 sum              // 응답
```
#### 2. add_server.py
```py
import rclpy as rp
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AddServer(Node):
    def __init__(self):
        super().__init__('add_server')
        self.srv = self.create_service(                # 서비스 생성
            AddTwoInts,          # 서비스 타입
            'add_two_ints',      # 서비스 이름
            self.callback        # 요청 오면 실행될 함수
        )
        self.get_logger().info('service ready')

    def callback(self, request, response):
        self.get_logger().info(
            f'request: {request.a} + {request.b}'
        )
        response.sum = request.a + request.b
        return response

def main():
    rp.init()
    node = AddServer()
    rp.spin(node)
    rp.shutdown()

if __name__ == '__main__':
    main()
```
#### 3. add_client.py
```py
import rclpy as rp
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AddClient(Node):
    def __init__(self):
        super().__init__('add_client')
        self.client = self.create_client(               # 클라이언트 생성
            AddTwoInts,
            'add_two_ints'
        )
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('waiting service...')
    def send_request(self):
        req = AddTwoInts.Request()                      # 요청 데이터 생성
        req.a = 10
        req.b = 20
        future = self.client.call_async(req)            # 서비스 요청 전송
        return future

def main():
    rp.init()
    node = AddClient()
    future = node.send_request()
    while rp.ok():
        rp.spin_once(node)                               # 이벤트 처리(서비스 응답 수신, 토픽 수신, 타이머 처리)
        if future.done():                                # 서비스 응답이 도착했는가?
            try:
                response = future.result()
                print('sum =', response.sum)
            except Exception as e:
                print(e)
            break
    rp.shutdown()

if __name__ == '__main__':
    main()
```
#### 4. 실행 순서
```c
terminal 1
$ python3 add_server.py
service ready
terminal 2
python3 add_client.py
sum = 30
```
