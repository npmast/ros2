#### 1. 우분투 이미지 받기(22.04 LTS)  
>https://cdimage.ubuntu.com/releases/jammy/release/ 접속하여 
>ubuntu-22.04.5-preinstalled-server-arm64+raspi.img.xz 파일을 다운로드 한다.
#### 2. 이미지 굽기  
>Raspberry Pi Imager  
#### 3. 설정하기  
>부팅하면 나타나는 사용자와 비밀번호는 ubuntu 이다. 입력하면 새 비밀번호를 설정할 수 있다.
#### 4. 인터넷 설정하기(무선 고정 IP)
>다음 파일을 백업하고 수정한다.  
>이때 들여쓰기에 주의하고 비밀번호는 8자 이상이어야 한다.
```c
sudo nano /etc/netplan/50-cloud-init.yaml
network:
  version: 2
  renderer: networkd
  wifis:
    wlan0:
      dhcp4: no
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
```
>sudo netplan apply 명령을 실행하여 변경사항 적용
#### 5. 기타 설정
* ssh 설정
>sudo apt update  
>sudo apt install openssh-server  
>sudo systemctl status ssh
>원격 PC의 cmd 창에서 ssh 사용자@IP 명령어로 접속한다.  
 
