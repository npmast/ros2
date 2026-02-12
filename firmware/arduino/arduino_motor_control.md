# ARDUINO

1. arduino IDE 설치
> ubuntu 에서 브라우저로 arduino 사이트를 찾아간다.  
> arduino.cc/en/software > Legacy IDE(1.8.19) Linux ARM 64 bit 파일을 다운받는다.  
> Downloads 폴더로 가서 방금 다운받은 압축파일을 Extract 한다.  
> 그러면 arduino-1.8.19-Linuxaarch64 폴더가 만들어 지는데 폴더로 들어가서 다음을 실해한다.
> ```c
>  sudo ./install.sh
> ```

2. arduino 연결
   다음 명령어를 실행하면 arduino usb port 연결을 확인할 수 있다.
   ```c
    ls /dev/ttyACM*
   ```
   /dev/ttyACM0 가 나오면 포트가 잡힌 것이다.(혹은 /dev/ttyUSB 확인)
   
3. I2C Test
   ```c++
    #include <Wire.h>

    void setup() {
       Serial.begin(115200);
       Serial.println("\nI2C Test");
       Wire.begin();
    }

    void loop() {
      byte error, addr;
      int nDevices = 0;

      for(addr = 1: addr < 127; addr++) {
        Wire.beginTransmission(addr);
        error = Wire.endTransmission();

        if(error == 0) {
          Serial.print("I2C device found at 0x");
          if(addr < 16) Serial.print("0");
          Serial.println(addr. HEX);
          nDevices++;
        }
      }

      if(nDevices == 0) Serial.println("No I2C devices found");
      Serial.println("------");
      delay(2000);
   }
   ```
4. Adafruit MotorShield Test   
  Arduino IDE 좌측에 LIBRARY MANAGER 버튼을 클릭한다.   
  search창에 Adafruit Motor Shield V2 Library by Adafruit을 찾아 Library를 설치한다.
  > * Adafruit motor library Test
   ```c++
    #include <Wire.h>
    #include <Adafruit_MotorShield.h>

    Adafruit_MotorShield AFMS = Adafruit_MotorShield();

    void setup() {
      Serial.begin(115200);
      Serial.println("MotorShield begin...");
      if(!AFMS.begin()) {
        Serial.println("FAIL: AFMS.begin()-Shield not found");
        delay(100);
      }
      Serial.println("OK: Shield found");
    }

    void loop() {
      delay(1000);
    }
   ```
  > * Moter Test
```c++
    #include <Wire.h>
    #include <Adafruit_MotorShield.h>

    Adafruit_MotorShield AFMS = Adafruit_MotorShield();
    Adafruit_DCMotor *motor;

    void setup() {
      Serial.begin(115200);
      Serial.println("AFMS.begin...");
      if(!AFMS.begin()) {
        Serial.println("FAIL: Shield not found");
        delay(100);
      }
      Serial.println("OK: Shield ready");
  
      motor = AFMS.getMotor(1);
      if(!motor) {
        Serial.println("FAIL: getMotor(1)");
        delay(100);
      }
    }

    void loop() {
      Serial.println("Test: forward ramp");
      motor->run(FORWARD);
      for(int spd = 0: spd <= 255; spd += 25) {
        Serial.print("Speed= ");
        Serial.println(spd);
        motor->setSpeed(spd);
        delay(800);
      }

      Serial.println("Stop");
      motor->setSpeed(0);
      motor->run(RELEASE);
      delay(2000);

      Serial.println("Test: backward ramp");
      motor->run(BACKWARD);
      for(int spd = 0; spd <= 255; spd += 25) {
        Serial.print("Speed= ");
        Serial.println(spd);
        motor->setSpeed(spd);
        delay(800);
      }

      Serial.println("Stop");
      motor->setSpeed(0);
      motor->run(RELEASE);
      delay(4000);
    }
```
> * Serial Test
```c++
    String rxBus = "";

    void setup() {
      Serial.begin(115200);
      while(!Serial) { ; }
      Serial.println("Arduino ready!!");
    }

    void loop() {
      while(Serial.available()) {
        char c = Serial.read();
        if(c == '\n' || c == '\r') {
          if(rxBuf.length() > 0) {
            Serial.print("Rx: ");
            Serial.println(rxBuf);
            rxBuf = "";
          }
        } else {
          rxBuf += c;
        }
      }
    }
```
