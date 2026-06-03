# TURTLEBOT3  
### e-Manual
### 1. SBC 설정
##### 1. 우분투 이미지 받기(22.04 LTS)  
>https://cdimage.ubuntu.com/releases/jammy/release/ 접속하여 
>ubuntu-22.04.5-preinstalled-server-arm64+raspi.img.xz 파일을 다운로드 한다.
#### 2. 이미지 굽기  
>Raspberry Pi Imager
>hostname: 장치에 부여하는 이름  
#### 3. 설정하기  
>부팅하면 나타나는 사용자와 비밀번호는 ubuntu 이다. 입력하면 새 비밀번호를 설정할 수 있다.
#### 4. 인터넷 설정하기(무선 고정 IP)
>다음 파일을 백업하고 수정한다.  
>이때 들여쓰기에 주의하고 비밀번호는 8자 이상이어야 한다.
```c
sudo nano /etc/netplan/50-cloud-init.yaml
network:
  version: 2
  wifis:
    wlan0:
      addresses:
        - 192.168.0.110/24
      routes:
        - to: default
          via: 192.168.0.1
      nameservers:
        addresses:
          - 8.8.8.8
      access-points:
          WiFi이름:
              password: 비밀번호
      dhcp4: true
      optional: true
      regulatory-domain: KR
```
>sudo netplan apply 명령을 실행하여 변경사항 적용
#### 5. 기타 설정
* ssh 설정
>sudo apt update  
>sudo apt install openssh-server  
>sudo systemctl status ssh  
>원격 PC의 cmd 창: ssh 사용자@IP
* 자동 업데이트 설정
>$ sudo nano /etc/apt/apt.conf.d/20auto-upgrades 파일을 열어  
>슷자를 두 개 모두 "0"으로 변경한다.
* 부팅 지연 방지
>$ systemctl mask systemd-networkd-wait-online.service
* 절전 및 최대 절전 모드 비활성화
>$ sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target  
>$ sudo reboot
* TurtleBot3 2GB인 경우 패키지 빌드를 위해 스왑 메모리 생성
>```c
>$ sudo fallocate -l 2G /swapfile
>$ sudo chmod 600 /swapfile
>$ sudo mkswap /swapfile
>$ sudo swapon /swapfile
>$ echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab    // 스왑파일 자동 활성화
>$ free -f                                                       // 메모리 확인
>```
#### 6. ROS2 설치: 원격 PC와 SBC 둘 다 설치
>ROS2 문서: Humble편에 우분투(deb 패키지)설치를 따라 설치한다.  
>ROS2 설치는 ROS-Base 설치(최소 기능)으로 설치한다.  
>개발도구는 설치하지 않는다.
>몇 가지 예를 들어보세요는 서버용은 실행되지 않는다.
#### 7. 패키지 설치 및 환경 구성
>시간이 오래 소요된다. 하나씩 천천히 따라한다.  
* ROS 패키지 설치하기  
>$ sudo apt install python3-argcomplete python3-colcon-common-extensions libboost-system-dev build-essential  
$ sudo apt install ros-humble-hls-lfcd-lds-driver  
$ sudo apt install ros-humble-turtlebot3-msgs  
$ sudo apt install ros-humble-dynamixel-sdk  
$ sudo apt install ros-humble-xacro  
$ sudo apt install libudev-dev  
$ mkdir -p ~/turtlebot3_ws/src && cd ~/turtlebot3_ws/src  
$ git clone -b humble https://github.com/ROBOTIS-GIT/turtlebot3.git  
$ git clone -b humble https://github.com/ROBOTIS-GIT/ld08_driver.git  
$ git clone -b humble https://github.com/ROBOTIS-GIT/coin_d4_driver  
$ cd ~/turtlebot3_ws/src/turtlebot3  
$ rm -r turtlebot3_cartographer turtlebot3_navigation2  
$ cd ~/turtlebot3_ws/  
$ echo 'source /opt/ros/humble/setup.bash' >> ~/.bashrc  
$ source ~/.bashrc  
$ colcon build --symlink-install --parallel-workers 1  
$ echo 'source ~/turtlebot3_ws/install/setup.bash' >> ~/.bashrc
$ source ~/.bashrc  
+업데이트 후 마이크로코드의 최신 여부에 대한 안내 문구가 출력되면 다음 파일을 열고     
$ sudo nano /etc/needrestart/needrestart.conf  
&nbsp;&nbsp;#$nrconf{ucodehints} = 0; 줄의 주석을 제거한다.  
* OpenCR용 USB 포트 설정  
>$ sudo cp `ros2 pkg prefix turtlebot3_bringup`/share/turtlebot3_bringup/script/99-turtlebot3-cdc.rules /etc/udev/rules.d/  
$ sudo udevadm control --reload-rules  
$ sudo udevadm trigger  
* ROS DDS 도메인 설정
>- 현재 설정된 DDS 도메인을 확인한다.  
>$ echo $ROS_DOMAIN_ID    
>- DDS 도메인을 30으로 설정한다.(설정 범위: 0 ~ 232)        
>$ echo 'export ROS_DOMAIN_ID=30 #TURTLEBOT3' >> ~/.bashrc    
$ source ~/.bashrc
#### 8. LDS 구성  
>사용하는 LDS 모델에 따라 다음과 같다.  
>$ echo 'export LDS_MODEL=LDS-01' >> ~/.bashrc # If you are using LDS-01  
$ echo 'export LDS_MODEL=LDS-02' >> ~/.bashrc # If you are using LDS-02  
$ echo 'export LDS_MODEL=LDS-03' >> ~/.bashrc # If you are using LDS-03  
>$ source ~/.bashrc
#### 9. Bringup
#### * 원격PC 네트워크 설정(VMware): TURTLEBOT3와 VMWare의 네트워크를 동일하게 맞춘다.
1. bridge mode 설정
  Edit > Virtual Network Editor > 하단의 Change Setting > VMnet0 (Bridbe) 선택
  Bridge to 항목에서 Automatic 대신 연결된 실제 컴퓨터의 랜카드 선택 > Apply 및 OK
2. 가상 머신 네트워크 어댑터 설정(VM Settings)
  VM > Setting > HardWare에서 Network Adapter > Network connection에 Bridged~ 와 Replicate~ 선택사항 선택 > OK
3. 가상 머신 재부팅 > 터미널에서 ip a 로 ip를 확인한다.(VM과 SBC가 동일한 네트워크로 잡혀있어야 한다.)
4. 확인
   1.  __TurtleBot3 bringup 실행: 원격 PC에서 SBC 사용하려면 먼저 실행되어야 한다.__   
   $ echo $ROS_DIMAIN_ID               // DOMAIN_ID 가 원격 Pc와 같아야 한다.
   $ echo $ROS_LOCALHOST_ONLY          // 반드시 0이 나와야 한다.     
   $ __ros2 launch turtlebot3_bringup robot.launch.py__  
   2. 원격 PC 에서 Topic 확인  
   $ ros2 topic list  
   $ ros2 topic echo /scan              // topic 데이터 확인(LiDAR)  
   $ ros2 topic info /scan              // topic 타입 확인  
==> 동일한 네트워크에 ROS_DOMAIN_ID 가 같으면 노드들이 자동으로 연결된다.  
==> ROS2의 기본 미들웨어인 DDS는 멀티캐스트와 검색 메커니즘을 사용하여 같은 도메인ID를 가진 노드를 스스로 찾아내고 통신 채널을 형성한다.
### 2. OpenCR 설정
#### 1. 패키지 설치
>$ sudo dpkg --add-architecture armhf  
>$ sudo apt-get update  
>$sudo apt-get install libc6:armhf  
>$ export OPENCR_PORT=/dev/ttyACM0  
>$ export OPENCR_MODEL=burger  
$ rm -rf ./opencr_update.tar.bz2  
>$ wget https://github.com/ROBOTIS-GIT/OpenCR-Binaries/raw/master/turtlebot3/ROS2/latest/opencr_update.tar.bz2     
$ tar -xvf opencr_update.tar.bz2
#### # 2. 업로드
>$ cd ./opencr_update  
$ ./update.sh $OPENCR_PORT $OPENCR_MODEL.opencr
#### 3. 자주 사용하는 메시지 타입  
> std_msgs/msg/String  
> geometry_msgs/msg/Twist  
> sensor_msgs/msg/Image  
> sensor_msgs/msg/LaserScan
### 3. 기본 작동
#### 1. TurtleBot3
```c
$ ssh ubuntu@&#123;IP_ADDRESS_OF_RASPBERRY_PI&#125;
$ export TURTLEBOT3_MODEL=burger
$ ros2 launch turtlebot3_bringup robot.launch.py
[INFO] [launch]: All log files can be found below /home/ubuntu/.ros/log/2019-08-19-01-24-19-009803-ubuntu-15310
[INFO] [launch]: Default logging verbosity is set to INFO
urdf_file_name : turtlebot3_burger.urdf
[INFO] [robot_state_publisher-1]: process started with pid [15320]
[INFO] [hlds_laser_publisher-2]: process started with pid [15321]
[INFO] [turtlebot3_ros-3]: process started with pid [15322]
[robot_state_publisher-1] Initialize urdf model from file: /home/ubuntu/turtlebot_ws/install/turtlebot3_description/share/turtlebot3_description/urdf/turtlebot3_burger.urdf
[robot_state_publisher-1] Parsing robot urdf xml string.
[robot_state_publisher-1] Link base_link had 5 children
[robot_state_publisher-1] Link caster_back_link had 0 children
[robot_state_publisher-1] Link imu_link had 0 children
[robot_state_publisher-1] Link base_scan had 0 children
[robot_state_publisher-1] Link wheel_left_link had 0 children
[robot_state_publisher-1] Link wheel_right_link had 0 children
[robot_state_publisher-1] got segment base_footprint
[robot_state_publisher-1] got segment base_link
[robot_state_publisher-1] got segment base_scan
[robot_state_publisher-1] got segment caster_back_link
[robot_state_publisher-1] got segment imu_link
[robot_state_publisher-1] got segment wheel_left_link
[robot_state_publisher-1] got segment wheel_right_link
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Init TurtleBot3 Node Main
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Init DynamixelSDKWrapper
[turtlebot3_ros-3] [INFO] [DynamixelSDKWrapper]: Succeeded to open the port(/dev/ttyACM0)!
[turtlebot3_ros-3] [INFO] [DynamixelSDKWrapper]: Succeeded to change the baudrate!
[robot_state_publisher-1] Adding fixed segment from base_footprint to base_link
[robot_state_publisher-1] Adding fixed segment from base_link to caster_back_link
[robot_state_publisher-1] Adding fixed segment from base_link to imu_link
[robot_state_publisher-1] Adding fixed segment from base_link to base_scan
[robot_state_publisher-1] Adding moving segment from base_link to wheel_left_link
[robot_state_publisher-1] Adding moving segment from base_link to wheel_right_link
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Start Calibration of Gyro
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Calibration End
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Add Motors
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Add Wheels
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Add Sensors
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create battery state publisher
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create imu publisher
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create sensor state publisher
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create joint state publisher
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Add Devices
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create motor power server
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create reset server
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Succeeded to create sound server
[turtlebot3_ros-3] [INFO] [turtlebot3_node]: Run!
[turtlebot3_ros-3] [INFO] [diff_drive_controller]: Init Odometry
[turtlebot3_ros-3] [INFO] [diff_drive_controller]: Run!
```
#### 2. 원격 PC
> 원격 PC의 터미널을 연다.
> * 주제 목록
```c
$ ros2 topic list
/battery_state
/cmd_vel
/imu
/joint_states
/magnetic_field
/odom
/parameter_events
/robot_description
/rosout
/scan
/sensor_state
/tf
/tf_static
```
> * 서비스 목록
```c
$ ros2 service list
/diff_drive_controller/describe_parameters
/diff_drive_controller/get_parameter_types
/diff_drive_controller/get_parameters
/diff_drive_controller/list_parameters
/diff_drive_controller/set_parameters
/diff_drive_controller/set_parameters_atomically
/hlds_laser_publisher/describe_parameters
/hlds_laser_publisher/get_parameter_types
/hlds_laser_publisher/get_parameters
/hlds_laser_publisher/list_parameters
/hlds_laser_publisher/set_parameters
/hlds_laser_publisher/set_parameters_atomically
/launch_ros/describe_parameters
/launch_ros/get_parameter_types
/launch_ros/get_parameters
/launch_ros/list_parameters
/launch_ros/set_parameters
/launch_ros/set_parameters_atomically
/motor_power
/reset
/sound
/turtlebot3_node/describe_parameters
/turtlebot3_node/get_parameter_types
/turtlebot3_node/get_parameters
/turtlebot3_node/list_parameters
/turtlebot3_node/set_parameters
/turtlebot3_node/set_parameters_atomically
```
> * 원격 조작
```c
$ export TURTLEBOT3_MODEL=${TB3_MODEL}
$ ros2 run turtlebot3_teleop teleop_keyboard
Control Your Turtlebot3
Moving around
        w
    a   s   d
        x
w/x : increase/decrease linear velocity (Burger : ~ 0.22, Waffle and Waffle Pi : ~ 0.26)
a/d : increase/decrease angular velocity (Burger : ~ 2.84, Waffle and Waffle Pi : ~ 1.82)
space key, s : force stop
CTRL-C to quit
```
> * rqt
```c
$ rqt
```
