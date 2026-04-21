## 워크스페이스와 패키지
ros2 패키지를 포함하는 디렉터리로 터미널에서 워크스페이스를 소싱해야 ros2 패키지를 사용할 수 있다.
### ROS2 기본 개발 순서
1. 워크스페이스 생성
2. 패키지 생성
3. 노드(코드) 작성
4. setup.py / package.xml 설정
5. 빌드(colcon)
6. 환경 적용(source)
7. 실행(ros2 run)  
#### 1. 워크스페이스 만들기  
ROS2 패키지는 src 디렉토리 안에서 생성하는 것이 기본이다.  
$ madir -p ~/ros2_ws/src    
$ cd ~/ros2_ws/src    
#### 2. 패키지 만들기  
코드를 설치하거나 배포하려면 패키지를 만들어야 한다.  
* CMake 구조  
  my_package/  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CMakeLists.txt  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include/my_package/  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;package.xml  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;src/  
  - CMakeLists.txt: 패키지 내부 코드를 빌드하는 방법을 설명한 파일
  - include/..: 패키지의 공용 헤더를 포함하는 디렉터리
  - package.xml: 패키지에 대한 메타 정보를 포함하는 파일
  - src: 패키지의 소스 코드를 포함하는 파일
* Python 구조  
  my_package/  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;package.xml  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;resource/my_package  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;setup.cfg  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;setup.py  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;my_package/
  - package.xml: 패키지에 대한 메터 정보를 포함하는 파일
  - resource/: 패키지 마커 파일
  - setup.cfg: 패키지가 실행 파일을 포함할 경우 ros2 run을 찾는 파일
  - setup.py: 패키지가 설치하는 방법을 설명하는 파일
##### 패키지 생성
* CMake  
  $ ros2 pkg create --build-type ament_cmake --node-name my_node my_package  
* Python  
  $ ros2 pkg create --build-type ament_python --node-name my_node my_package  
src 디렉터리 내에 my_package 폴더가 생성된다.
### 3. 패키지 빌드  
$ cd ~/ros2_ws  
$ colcon build  
$ colcon build --package-select my_package &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// my_package 패키지만 빌드  
$ sudo apt install tree  
$ tree          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;// 폴더 구조를 확인한다.
### 4. 패키지 사용  
$ source install/local_setup.bash  
$ ros2 run my_package my_node
$ ros2 pkg create test_package --build-type ament_python --dependencies rclpy std_msgs  
  * test_package: 패키지 이름
  * --build-type ament_python: 빌드 Python 패키지 타입
  * --dependencies crlpy std_msgs: ROS2 Python 노드와 문자열 메시지 사용
