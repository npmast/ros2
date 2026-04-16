# UBUNTU  
### ubuntu 버전  
ROS2 jazzy Jalisco 는 Ubuntu 24.04 LTS 버전을 공식적으로 지원하며, 이 환경에서 설치 및 동작하도록 설계되었다.
2024 년 5월에 릴리스된 Jazzy 는 Ubuntu 24.04 기반의 장기 지원(LTS) 버전으로 2029 년까지 업데이트가 제공되는 최신 추천 버전이다.  
Raspberry Pi Imager 에서 운영체제를 Ubuntu 24.04로 선택하여 설치한다. 
## 원격 PC에 ubuntu 설치하기
#### 1. VMWare 를 다운 받는다.
  VMWare가 브로드컴에 인수된 후 무료로 제공하고 있다. 다운로드를 위해서는 회원가입이 필수이다.  
  broadcom.com 접속 > 오른쪽 상단 Support Portal > Register 클릭하여 진행한다.  
  회원가입 후 Go To Portal 클릭 로그인 > Software > VMWare Cloud Foundation > My Downloads을 진행하여    다운로드 받는다.  (다소 까다로움)
#### 2. ubuntu 설치하기
  ubuntu.com 접속 > 오른쪽 상단 Menu > Download Ubuntu > Desktop 클릭
#### 3. 환경 설정하기(24.04)
  * bridged mode
    Edit > Virtual Network Editer > Change Settings > bridged > bridged to: 현재 랜카드 설정 > OK
    VM > Setting > Network Adgpter > bridged 로 설정
  * Open VM Tools 설치 - 화면 크기 조절    
    sudo atp update && sudo apt install open-vm-tools-desktop
  * Teminator 설치  
    sudo apt install terminator
    터미널창에서 우클릭 > Preferences 클릭하면 터미널 환경을 설정할 수 있다.
  
## raspberryPi5 에 ubuntu 설치하기  
#### 1. ssh 연결
  a. Monitor 연결하고 Pi에 전원을 공급한다.  
> 첫 화면이 켜지면 인터넷을 활성화시켜고 접속 IP 을 확인한다.(ip a or hsotname -I)    
> 터미널을 열어 update 와 ssh server 를 설치한다.
  ```c
  sudo apt update
  sudo apt install openssh-server
  ```
  b. 설치가 완료되면 HDMI 케이블을 제거하고 재부팅한다.  
> PC에서 명령프롬프트를 실행하고 ssh 접속 명령을 실행한다.  
> C:\Users\사용자>ssh 사용자@xxx.xxx.xxx.xxx  
> 비밀번호를 입력한다.  
> 접속이 되면 upgrade 를 실행한다.  
> (failed 가 뜨면 C:\Users\사용자\.ssh 폴더의 known_hosts 파일을 열어 내용을 지운다.(이전 접속 정보와 충돌))
> ```
> # 우분투 버전 확인
> lsb_release -a
> # 자동 업데이트 설정
> sudo nano /etc/apt/apt.conf/20auto-upgrades
>   APT::Periodic::Update-Package-List "0";     // 패키지 자동 업데이트 끄기
>   APT::Reriodic::Unattended-Upgrade "0";      // 보안 업데이트 자동 설치 끄기
> # 부팅 지연 방지
> systemctl mask systemd-networkd-wait-online.service
> # 절전 및 최대 절전 모드 비활성화
> sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target
#### 2. vnc server  
> realvnc server 검색 Download VNC Server by RealVNC 사이트 접속  
> wget 사용은 다음과 같다.
> ```c
> cd Downloads
> wget https://downloads.realvnc.com/download/file/vnc.files/VNC-Server-7.16.0-Linux-ARM64.deb
> chmod u+x VNC-Server-7.16.0-Linux-ARM64.deb
> sudo apt install ./VNC-Server-7.16.0-Linux-ARM64.deb
> ```
> * 설정
> ```c
> sudo nano /etc/gdm3/custom.conf 파일을 연다.
> #WaylandEnable=false   // 7행 주석 제거
> ```
> * xorg 가상 비디오 드라이버 설치
> ```c
> sudo apt install xserver-xorg-video-dummy xinit
> ```
> * sudo nano /etc/X11/xorg.conf 파일을 열어 다음을 복사한다.  
> ```c
>Section "Device"
>    Identifier "Configured Video Device"
>    Driver "dummy"
>EndSection
>
>Section "Monitor"
>    Identifier "Configured Monitor"
>    HorizSync 28-80
>    VertRefresh 48-75
>    Modeline "1920x1080" 172.80 1920 2040 2248 2576 1080 1081 1084 1118
>EndSection
>
>Section "Screen"
>    Identifier "Default Screen"
>    Device "Configured Video Device"
>    Monitor "Configured Monitor"
>    DefaultDepth 24
>    SubSection "Display"
>        Depth 24
>        Modes "1920x1080"
>    EndSubSection
>EndSection
> ```
> * 서비스 활성화 및 자동시작
> ```c
> sudo systemctl enable vncserver-x11-serviced.service 
> sudo systemctl start vncserver-x11-serviced.service
> sudo systemctl status vncserver-x11-serviced.service
> //sudo nano /boot/firmware/config.txt 파일을 열어 끝에 추가한다.
> //hdmi_force_hotplug=1
> //hdmi_group=2
> //hdmi_mode=82
> sudo reboot
> ```
> * 검은 화면이 나타나면 다음 명령을 실행한다.
> ```c
> sudo systemctl restart gdm3
> ```
#### 3. jupyter lab  
> jupyter 는 전역으로 설치하고 가상환경별로 커널을 만들어 사용한다.  
> * jupyter lab 설치
> ```c
> sudo apt update
> //sudo apt install -y python3-venv python3-pip pipx
> //pipx ensurepath                                                                  // 사용자 PATH에 자동 연결
> //source ~/.bashrc                                                                 // 현재 터미널 적용
> //pipx install jupyterlab                                                          // jupyterlab 설치
> python3 -m pip config set global.break-system-packages true                        // pip 전역 사용 설정
> sudo apt install jupyter-core                                                      // 핵심 패키지 설치  
> pip3 install jupyterlab                                                            // jupyterlab 설치
> sudo reboot                                                                        
> jupyter lab
> ```
> * 가상환경 생성 및 등록(가상환경별 실행)  
> 가상환경에서는 pip 사용을 한다.
> ```c
> mkdir -p ~/venvs
> python3 -m venv ~/venvs/{ros2:가상환경 명}                                        // 가상환경 생성
> source ~/venvs/ros2/bin/activate                                                  // 활성화
> python -m pip install --upgrade pip여
> python -m pip install ipykernel                                                   // ipykernel 패키지 설치
> python -m ipykernel install --user --name {ros2:가상환경} --display-name {"Python\(ros2\)": 커널이름} // 커널등록
> jupyter kernelspec list                                                            // 커널 확인
> 
> jupyter kernelspec uninstall {커널이름}                                            // 커널 삭제
> deactivate                                                                         // 비활성화
> ```
> 커널들이 저장되는 위치: /home/사용자/.local/share/jupyter/kernels/{커널이름}  
> * 가상환경을 \"python3 -m venv --system-site-packages {가상환경}\" 와 같이 "--system-site-packages" 옵션을 사용하여 생성하
> 시스템에 이미 설치된 파이션 패키지를 가상환경 내에서 사용할 수 있게 허용하는 옵션이다.
> * 외부접속 허용
> ```c
> jupyter lab --generate-config                  // 설정 파일 생성
> nano ~/.jupyter/jupyter_lab_config.py          // 설정 파일 열어 추가한다.
> c.ServerApp.ip = '0.0.0.0'                      // 모든 IP 허용(922)
> c.ServerApp.port = 8888                         // 접속 포트 설정(1038)
> c.ServerApp.open_browser = False                // 브라우저 자동 실행 비활성(1026)
> jupyter lab                                     // 실행
> 
> ```  
* PC 에서 서버ip:8888 로 접속  
  첫 화면에서 비밀번호 입력 및 생성이 나오는데 토큰을 넣어야 비밀번호 생성이 가능하다.  
  서버 터미널에서 다음 명령을 사용하여 알 수 있다.  
  $ jupyter server list 
#### 4. VSCode
> code.visualstdio.com/Download > Arm64 다운로드
> ```c
> cd Downloads
> sudo apt install ./code_1.113.0-1774364715_arm64.deb
> code                    // 실행
> Extensions > python     // 설치
> ```
> * PC VSCode 원격 접속
> PC에 python이 설치되어 있어야 한다.(python.org)
> 확장 설치: Extension > Remote - SSH 설치    
> 원격 연결: 좌측 하단 >< 버튼(Open a Remote Window) 클릭    
> SSH 연결: "Connect to Host... > +Add New SSH Host.. > ssh 사용자@IP주소 > 비밀번호 입력  
> EXTENSIONS: Python 설치  
> 작업 폴더 지정: File > Open Folder  
> 터미널 열기: ctrl + `  
    
