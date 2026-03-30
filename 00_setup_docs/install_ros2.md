### ROS2 문서: Jazzy
#### 1. 시스템 설정
##### 로케일 설정
> ```c
> locale  # check for UTF-8
>
> sudo apt update && sudo apt install locales
> sudo locale-gen en_US en_US.UTF-8
> sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
> export LANG=en_US.UTF-8
> 
> locale  # verify settings
> ```
##### 저장소 활성화
> ```c
> sudo apt install software-properties-common
> sudo add-apt-repository universe
> ```
#### ros-apt-source 패키지 설치
> ```c
> sudo apt update && sudo apt install curl -y
> export ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F'"' '{print $4}')
> curl -L -o /tmp/ros2-apt-source.deb "https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt->source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo ${UBUNTU_CODENAME:-${VERSION_CODENAME}})_all.deb"
> sudo dpkg -i /tmp/ros2-apt-source.deb
> ```
#### 개발도구 설치
> ```c
> sudo apt update && sudo apt install ros-dev-tools
> ```
#### ROS2 설치
> ```c
> sudo apt update
> sudo apt upgrade
> sudo apt insall ros-jazzy-desktop
> ```
#### 환경설정
> ```c
> source /opt/ros/jazzy/setup.bash
> ```
##### 예제 실행
터미널에서 C++ talker 실행
> ```c
> source /opt/ros/jazzy/setup.bash
> ros2 run demo_nodes_cpp talker
> ```
다른 터미널에서 Python listener 실행
> ```c
> source /opt/ros/jazzy/setup.bash
> ros2 run demo_nodes_py listener
> ```
