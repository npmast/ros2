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

    
    
