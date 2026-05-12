#### 1. arduino
```c
/* DHT sensor library INSTALL */
#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT11   // DHT22면 DHT22로 변경

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (!isnan(h) && !isnan(t)) {
    Serial.print(t);
    Serial.print(",");
    Serial.println(h);
  }

  delay(1000);
}
```
#### 2. 패키지 생성
```c
$ ~/ros2_ws/src
$ ros2 pkg create dht_sensor_bridge --build-type ament_python --dependencies rclpy std_msgs
```
