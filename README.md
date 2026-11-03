## wsl
#### 1. 설치
* Windows 기능 켜기/끄기
  Hyper-v, Linux용 Windows 하위 시스템 그리고 가상 머신 플랫폼 이렇게 3개를 체크 확인하여 필요 파일을 다운로드 받는다.
* PowerShell 또는 명령 프롬프트를 관리자 권한으로 실행한다.
> ```
> $ wsl --list --online                      # 설치 가능한 리눅스 배포판을 확인한다.  
> $ wsl --install -d Ubuntu-24.04            #24.04를 설치한다.  
>  사용자가 표시되고(PC 사용자) 바꾸지 않으면 엔터를 치고 비번을 입력한다.
> $ wsl -l -v                                # wsl 버전 확인한다.
* 명령 프롬프트 실행
> ```
> > wsl                                      # wsl 실행
> **@***:/mnt/c/Users/NPtr$ cd               # 사용자 디렉터리로 이동
> ~$ pwd
> ~$ sudo apt update
> ~$ sudo apt upgrade -y
> ~$ python3 --version
> ~$ ls
> ~$ mkdir -p ~/venvs
> ~$ python3 -m venv --system-site-package ~/venvs/.venv
> ~$ sudo apt install python3.12-venv
> ~$ python3 -m venv --system-site-package ~/venvs/.venv
> ~$ source ~/venvs/.venv/bin/activate
> ~$ pip --version
> ~$ pip install --upgrade pip
> ~$ pip install jupyterlab
> ~$ jupyter lab --version
> ~$ jupyter lab
> ~$ python -m ipykernel install --user --name .venv --display-name "base"        # 커널생성
> ~$ jupyter kernelspec list
> ~$ jupyter kernelspec uninstall base(ros)                                       # 커널삭제
> ~$ cd ~/ros2_ws
> +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
> # 폴더 구성
> WSL2 / Ubuntu 24.04
>│
>├── ROS2 Jazzy (apt로 시스템에 설치)
>│
>└── /home/사용자명/
>    │
>    ├── venvs/
>    │   ├── .venv/        # 일반 Python + Jupyter
>    │   ├── ros_env/      # ROS2 + Python + rclpy
>    │   └── ml_env/       # 머신러닝/딥러닝 (선택)
>    │
>    ├── ros2_ws/          # ROS2 패키지 개발
>    │   └── src/
>    │
>    ├── projects/         # 일반 Python 개발
>    │
>    └── notebooks/        # Jupyter 노트북
> ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
> ```
### 00. Setup_Docs (0단계: 환경설정)  
  * install_guide.md (Ubuntu 및 ROS 설치)
  * network_config.txt(ip 설정 및 ssh 접속 정보)
### 01. simulation (1단계: 학습단계)   
  * 학습단계
### 02. hardware_design (2단계: 하드웨어)  
  * parts_list.xls (부품 목록 및 구매 링크)
  * circuit_diagram.pdf (회로도 및 핀 맵)
### 03. Firmware (3단계: 하드웨어 제어)  
  * arduino_motor_control (모더 드라이버 제어)
### 04. ROS_Workspace (4단계: ROS 패키지)  



