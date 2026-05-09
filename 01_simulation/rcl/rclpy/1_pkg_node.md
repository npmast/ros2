## pakage 만들기
: colcon build 실행하여 src 폴더가 있어야 한다.(readme.md)
#### 1. pakage & node
```py
$ source /opt/ros/jazzy/setup.bash
$ cd ~/ros2_ws/src
$ $ ros2 pkg create --build-type ament_python --node-name my_node my_pkg --dependencies rclpy std_msgs
# --node-name 옵션을 사용하면 기본 실행 파일(노드)이 자동으로 만들어진다.
$ sudo apt install tree
$ tree                # 폴더의 계층구조 확인
```
#### 2. build
```c
$ cd ~/ros2_ws
$ colcon build

```
#### 3. 환경 적용 및 실행
```py
$ source /install/setup.bash
$ ros2 run my_pkg my_node
Hi from my_pkg
$ ros2 pkg list | grep my_pkg
my_pkg
alias 
```
#### 4. Node
1. main_test.py  
   다음 코드를 작성하고 실행하면 'Hi from my_pkg' 가 출력된다.
```py
def main():
    print('Hi from my_pkg.')

if __name__ == '__main__':
    main()
```
2. my_node.py
```py

```
