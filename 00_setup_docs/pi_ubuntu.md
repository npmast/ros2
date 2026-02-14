# UBUNTU  

raspberryPi5 에 ubuntu 설치하기  
### ubuntu 버전  
ROS2 jazzy Jalisco 는 Ubuntu 24.04 LTS 버전을 공식적으로 지원하며, 이 환경에서 설치 및 동작하도록 설계되었다.
2024 년 5월에 릴리스된 Jazzy 는 Ubuntu 24.04 기반의 장기 지원(LTS) 버전으로 2029 년까지 업데이트가 제공되는 최신 추천 버전이다.  
Raspberry Pi Imager 에서 운영체제를 Ubuntu 24.04로 선택하여 설치한다.  

#### 1. ssh 연결
  a. Monitor 연결하고 Pi에 전원을 공급한다.  
> 첫 화면이 켜지면 인터넷을 활성화시켜고 접속 IP 을 확인한다.(ip addr or hsotname -I)    
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
> failed 가 뜨면 C:\Users\사용자\.ssh 폴더의 known_hosts 파일을 열어 내용을 지운다.(이전 접속 정보와 충돌)
#### 2. vnc server  
> realvnc server 검색 Download VNC Server by RealVNC 사이트 접속  
> wget 사용은 다음과 같다.
> ```c
> cd Downloads
> wget https://downloads.realvnc.com/download/file/vnc.files/VNC-Server-7.16.0-Linux-ARM64.deb
> chmod u+x VNC-Server-7.16.0-Linux-ARM64.deb
> sudo apt install ./VNC-Server-7.16.0-Linux-ARM64.deb
> ```
#### 3. jupyter lab  
> jupyter 는 전역으로 설치하고 가상환경별로 커널을 만들어 사용한다.  
> * jupyter lab 설치
> ```c
> sudo apt update
> sudo apt install -y python3-pip                                                    // pip 설치
> pip3 install japyterlab
> jupyter lab
> ```
> * 가상환경 생성 및 등록
> ```c
> python3 -m vnev {가상환경 명}                                                      // 가상환경 생성
> pip install ipykernel                                                              // ipykernel 설치
> python3 -m ipykernel install --user --name {가상환경} --display-name {커널이름}    // 커널등록
> jupyter kernelspec list                                                            // 커널 확인
> 
> jupyter kernelspec uninstall {커널이름}                                            // 커널 삭제
> ```
> 커널들이 저장되는 위치: /home/사용자/.local/share/jupyter/kernels/{커널이름}  
> 가상환경을 \"python3 -m venv --system-site-packages {커널이름}\" 와 같이 "\--system-site-packages"\ 옵션을 사용하면
> 시스템에 이미 설치된 파이션 패키지를 가상환경 내에서 사용할 수 있게 허용하는 옵션이다.
    
    
