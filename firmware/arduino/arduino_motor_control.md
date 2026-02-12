# ARDUINO

### 1. arduino IDE 설치  
ubuntu 에서 브라우저로 arduino 사이트를 찾아간다.  
arduino.cc/en/software > Legacy IDE(1.8.19) Linux ARM 64 bit 파일을 다운받는다.  
Downloads 폴더로 가서 방금 다운받은 압축파일을 Extract 한다.  
그러면 arduino-1.8.19-Linuxaarch64 폴더가 만들어 지는데 폴더로 들어가서 다음을 실행한다.
 ```c
  sudo ./install.sh
 ```

### 2. arduino 연결  
다음 명령어를 실행하면 arduino usb port 연결을 확인할 수 있다.
   ```c
    ls /dev/ttyACM*
   ```
   /dev/ttyACM0 가 나오면 포트가 잡힌 것이다.(혹은 /dev/ttyUSB 확인)
   
### 3. I2C Test
  * I2C_test.ino
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
### 4. Adafruit MotorShield Test   
  Arduino IDE 좌측에 LIBRARY MANAGER 버튼을 클릭한다.   
  search창에 Adafruit Motor Shield V2 Library by Adafruit을 찾아 Library를 설치한다.
   * Adafruit_shield_test.ino
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
   * Moter_shield_test.ino
```c++
    #include <Wire.h>
    #include <Adafruit_MotorShield.h>

    #define motor m2                                                 // left motor: m1, right motor: m2

    Adafruit_MotorShield AFMS = Adafruit_MotorShield();              // I2C 주소: 0x60
    Adafruit_DCMotor *motor;

    void setup() {
      Serial.begin(115200);
      Serial.println("AFMS.begin...");
      if(!AFMS.begin()) {
        Serial.println("FAIL: Shield not found");
        delay(100);
      }
      Serial.println("OK: Shield ready");
  
      motor = AFMS.getMotor(2);                                      // M1
      if(!motor) {
        Serial.println("FAIL: getMotor(2)");
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
 * Serial_test.ino
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
### 5. Motor control  
 * Motor_control.ino
```c++
#include <Wire.h>
#include <Adafruit_MotorShield.h>

Adafruit_MotorShield AFMS = Adafruit_MotorShield();                     // Motor Shield 객체 (기본 I2C 주소 0x60)

Adafruit_DCMotor *motorL = nullptr;                                     // M1
Adafruit_DCMotor *motorR = nullptr;                                     // M2

// 속도 제한
static int clampSpeed(int v) {
  if (v > 255) return 255;
  if (v < -255) return -255;
  return v;
}

static void setMotor(Adafruit_DCMotor *m, int spd) {
  spd = clampSpeed(spd);
  if (spd > 0) {
    m->run(FORWARD);
    m->setSpeed((uint8_t)spd);
  } else if (spd < 0) {
    m->run(BACKWARD);
    m->setSpeed((uint8_t)(-spd));
  } else {
    m->setSpeed(0);
    m->run(RELEASE);                                                      // 관성/프리휠
  }
}

// 간단 라인 파서: "V left right\n" (예: "V 120 -120\n")
String lineBuf;

void setup() {
  Serial.begin(115200);
  while (!Serial) { ; }

  if (!AFMS.begin()) {
    Serial.println("ERR: MotorShield not found. Check I2C wiring/address.");
    while (1) { delay(100); }
  }

  motorL = AFMS.getMotor(1);                                              // M1
  motorR = AFMS.getMotor(2);                                              // M2
  if (!motorL || !motorR) {
    Serial.println("ERR: Motor ports not available.");
    while (1) { delay(100); }
  }

  // 초기 정지
  setMotor(motorL, 0);
  setMotor(motorR, 0);

  Serial.println("OK: Ready. Send: V <left> <right>\\n (range -255..255)");
}

void loop() {
  while (Serial.available()) {
    char c = (char)Serial.read();
    if (c == '\n') {
      lineBuf.trim();                                                    // 한 줄 완성
      if (lineBuf.length() > 0) {
        // 예상 포맷: V left right
        char cmd;
        int left, right;
        int n = sscanf(lineBuf.c_str(), " %c %d %d", &cmd, &left, &right);
        if (n == 3 && (cmd == 'V' || cmd == 'v')) {
          setMotor(motorL, left);
          setMotor(motorR, right);
          // 간단 ACK
          Serial.print("ACK V ");
          Serial.print(left);
          Serial.print(" ");
          Serial.println(right);
        } else if (lineBuf == "S" || lineBuf == "s") {
          setMotor(motorL, 0);
          setMotor(motorR, 0);
          Serial.println("ACK S");
        } else {
          Serial.print("ERR: bad cmd: ");
          Serial.println(lineBuf);
        }
      }
      lineBuf = "";
    } else {
      if (lineBuf.length() < 64) lineBuf += c;                          // 버퍼 누적 (너무 길면 리셋)
      else lineBuf = "";
    }
  }
}
```
### 6. SCREEN  
 ROS screen 은 일반적으로 ROS 환경에서 노드나 프로그램의 실행 화면을 분리하거나 터미널 출력을 확인하는 Linux의 도구이다.  
 ```c
 ls /dev/ttyACM* (or /dev/ttyUSB*)                                   // ttyACM* or ttyUSB* 확인
 sudo apt install screen                                             // screen 설치
 screen /dev/ttyACM0 115200                                          // 115200 속도로 Serial 연결(ubuntu <-> arduino)

 // 스크린 종료
 Ctrl + A
 -> K
 -> Y
 ```
* Motor.ino
```c++
/* moter test (screen) */
#include <Wire.h>
#include <Adafruit_MotorShield.h>

/* ================== Motor Shield ================== */
Adafruit_MotorShield AFMS = Adafruit_MotorShield();                   // 기본 I2C: 0x60
Adafruit_DCMotor *motorL;
Adafruit_DCMotor *motorR;

/* ================== Serial RX ================== */
char rxBuf[32];
uint8_t rxIdx = 0;

/* ================== Watchdog ================== */
unsigned long lastCmdTime = 0;
const unsigned long CMD_TIMEOUT_MS = 500;                             // 0.5초 명령 없으면 정지

/* ================== Utils ================== */
int clamp(int v) {
  if (v > 255) return 255;
  if (v < -255) return -255;
  return v;
}

void setMotor(Adafruit_DCMotor *m, int pwm) {
  pwm = clamp(pwm);
  if (pwm > 0) {
    m->run(FORWARD);
    m->setSpeed(pwm);
  } else if (pwm < 0) {
    m->run(BACKWARD);
    m->setSpeed(-pwm);
  } else {
    m->setSpeed(0);
    m->run(RELEASE);
  }
}

void stopAll() {
  setMotor(motorL, 0);
  setMotor(motorR, 0);
}

/* ================== Command Handler ================== */
void handleCommand(char *cmd) {
  lastCmdTime = millis();

  if (cmd[0] == 'S') {
    stopAll();
    Serial.println("ACK S");
    return;
  }

  if (cmd[0] == 'V') {
    int l, r;
    if (sscanf(cmd, "V %d %d", &l, &r) == 2) {
      setMotor(motorL, l);
      setMotor(motorR, r);
      Serial.print("ACK V ");
      Serial.print(l);
      Serial.print(" ");
      Serial.println(r);
    } else {
      Serial.println("ERR V format");
    }
    return;
  }

  Serial.print("ERR unknown: ");
  Serial.println(cmd);
}

/* ================== Setup ================== */
void setup() {
  Serial.begin(115200);
  //while (!Serial) {}

  Serial.println("Motor controller booting...");

  if (!AFMS.begin()) {
    Serial.println("FATAL: MotorShield not found");
    while (1);
  }

  motorL = AFMS.getMotor(1);                                                // M1
  motorR = AFMS.getMotor(2);                                                // M2

  if (!motorL || !motorR) {
    Serial.println("FATAL: motor port error");
    while (1);
  }

  stopAll();
  Serial.println("OK: Ready");
}

/* ================== Loop ================== */
void loop() {
  /* ---- Serial RX (non-blocking) ---- */
  while (Serial.available()) {
    char c = Serial.read();

    if (c == '\n' || c == '\r') {
      if (rxIdx > 0) {
        rxBuf[rxIdx] = '\0';
        handleCommand(rxBuf);
        rxIdx = 0;
      }
    } else if (rxIdx < sizeof(rxBuf) - 1) {
      rxBuf[rxIdx++] = c;
    }
  }

  /* ---- Watchdog ---- */
  if (millis() - lastCmdTime > CMD_TIMEOUT_MS) {
    stopAll();
  }
}
```
