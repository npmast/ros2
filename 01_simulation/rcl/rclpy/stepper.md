#### 1. Arduino  
```c
#include <Stepper.h>

const int STEPS_PER_REV = 2048;

// 28BYJ-48 + ULN2003은 핀 순서가 중요합니다.
// IN1, IN3, IN2, IN4 순서로 넣는 경우가 많습니다.
Stepper stepper(STEPS_PER_REV, 8, 10, 9, 11);

void setup() {
  Serial.begin(115200);
  stepper.setSpeed(10);  // RPM
  Serial.println("READY");
}

void loop() {
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();

    if (cmd.startsWith("M")) {
      int spaceIndex = cmd.indexOf(' ');
      int steps = cmd.substring(spaceIndex + 1).toInt();

      stepper.step(steps);

      Serial.println("OK");
    }
  }
}
```
