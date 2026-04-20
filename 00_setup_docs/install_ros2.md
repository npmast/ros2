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
#### bash 환경 적용 및 버전 확인
> ```c
> source /opt/ros/jazzy/setup.bash
> echo $ROS_DISTRO
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
####  bashrc  설정하기  
새로운 터미널 세션이 시작될 때마다 실행되는 스크립터 파일로  bash 환경을 제공한다.  
- .bashrc: 터미널이 열릴 때마다 실행되는 스크립트 파일로 설정 파일이다.  
- source: 현재 셸 환경에서 즉시 다시 불러와 적용하는 명령어  
> $ echo &SHELL  
> $ cp ~/.bashrc ~/.bashrc.backup  
bashrc 파일을 열고 마지막 줄에 아래 내용을 추가하고 저장한다.  
> $ nano ~/.bashrc 
> echo "ROS Jazzy is now active."  
> source /opt/ros/jazzy/setup.bash  
> $ source ~/.bashrc        // 현재 쉘에 적용하는 명령
- alias 적용  
> $ nano /.bashrc  
> alias jazzy="source /opt/ros/jazzy/setup.bash; echo \"ROS Jazzy is now active.\""
> $ soruce ~/.bashrc  
> 이제부터는 터미널이 열리고 jazzy 를 입력하면 ros2 가 활성화 된다.  
#### Domain
> DDS 도메인을 식별하는데 사용된다. ID 값은 0 ~ 232 범위의 값을 가지며 같은 ROS_DOMAIN_ID 값을 가진 노드들은
> 서로 통신을 할 수 있다.  
> .bashrc 파일을 열고 추가한 코드를 삭제하고 새로 작성한다.  
> $ nano /.bashrc  
> alias domain="export ROS_DIMAIN_ID=10; echo \"ROS_DOMAIN_ID=10\""  
> alias jazzy="source /opt/ros/jazzy/setup.bash; domain; echo \"ROS jazzy is now active.\""  
저장하고 빠져나온다.  
> $ source ~/.bashrc  
> $ jazzy  
> ROS_DOMAIN_ID=10  
> ROS2 jazzy is now active.    
