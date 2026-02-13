# ROS2 패키지 생성
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
ros2 pkg create motor_serial_bridge --build-type ament_python --dependencies rclpy geometry_msgs
# 노드 코드
~/ros2_ws/src/motor_serial_bridge/motor_serial_bridge/motor_serial_bridge_node.py
#!/usr/bin/env python3
import time
import serial

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


def clamp(v: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, v))


class MotorSerialBridge(Node):
    """
    Subscribes:
      - /cmd_vel (geometry_msgs/Twist)

    Sends to Arduino over serial:
      - "V <left_pwm> <right_pwm>\\n"
      - "S\\n" on timeout
    """

    def __init__(self):
        super().__init__("motor_serial_bridge")

        # ---- Parameters ----
        self.declare_parameter("port", "/dev/ttyACM0")
        self.declare_parameter("baud", 115200)
        self.declare_parameter("wheel_base", 0.20)   # meters (left-right distance)
        self.declare_parameter("max_v", 0.50)         # m/s => PWM 255 mapping
        self.declare_parameter("invert_left", False)
        self.declare_parameter("invert_right", False)
        self.declare_parameter("cmd_timeout_s", 0.5)  # seconds
        self.declare_parameter("send_rate_hz", 30.0)  # periodic send for stability

        self.port = self.get_parameter("port").value
        self.baud = int(self.get_parameter("baud").value)
        self.wheel_base = float(self.get_parameter("wheel_base").value)
        self.max_v = float(self.get_parameter("max_v").value)
        self.invert_left = bool(self.get_parameter("invert_left").value)
        self.invert_right = bool(self.get_parameter("invert_right").value)
        self.cmd_timeout_s = float(self.get_parameter("cmd_timeout_s").value)
        self.send_rate_hz = float(self.get_parameter("send_rate_hz").value)

        # ---- State ----
        self.target_left_pwm = 0
        self.target_right_pwm = 0
        self.last_cmd_time = time.monotonic()
        self.last_sent = (None, None)

        # ---- Serial ----
        try:
            self.ser = serial.Serial(self.port, self.baud, timeout=0.02)
        except Exception as e:
            raise RuntimeError(f"Failed to open serial port {self.port}: {e}")

        # Arduino는 포트 오픈 시 리셋될 수 있으므로 약간 대기
        time.sleep(2.0)
        self.get_logger().info(f"Opened {self.port} @ {self.baud}")

        # ---- ROS ----
        self.sub = self.create_subscription(Twist, "/cmd_vel", self.on_cmd_vel, 10)

        period = 1.0 / self.send_rate_hz if self.send_rate_hz > 0 else 0.033
        self.timer = self.create_timer(period, self.on_timer)

    def on_cmd_vel(self, msg: Twist):
        self.last_cmd_time = time.monotonic()

        v = float(msg.linear.x)    # m/s
        w = float(msg.angular.z)   # rad/s

        # Differential drive:
        # v_left  = v - w*L/2
        # v_right = v + w*L/2
        v_left = v - (w * self.wheel_base / 2.0)
        v_right = v + (w * self.wheel_base / 2.0)

        # Map m/s to PWM
        if self.max_v <= 0.0:
            self.get_logger().warn("max_v must be > 0. Using 0.5 as fallback.")
            max_v = 0.5
        else:
            max_v = self.max_v

        left_pwm = int(clamp((v_left / max_v) * 255.0, -255.0, 255.0))
        right_pwm = int(clamp((v_right / max_v) * 255.0, -255.0, 255.0))

        if self.invert_left:
            left_pwm = -left_pwm
        if self.invert_right:
            right_pwm = -right_pwm

        self.target_left_pwm = left_pwm
        self.target_right_pwm = right_pwm

    def on_timer(self):
        # Timeout이면 정지
        age = time.monotonic() - self.last_cmd_time
        if age > self.cmd_timeout_s:
            self.send_stop()
            return

        # 주기적으로 명령 송신 (연속 제어 안정화)
        self.send_velocity(self.target_left_pwm, self.target_right_pwm)

    def send_velocity(self, left_pwm: int, right_pwm: int):
        # 변경 없으면 송신 생략해도 되지만, 주기 송신이 더 안정적인 경우가 많음
        cmd = f"V {left_pwm} {right_pwm}\n"
        try:
            self.ser.write(cmd.encode("ascii"))
        except Exception as e:
            self.get_logger().error(f"Serial write failed: {e}")

    def send_stop(self):
        # 이미 정지 명령을 보낸 상태면 중복 전송 최소화
        if self.last_sent == (0, 0):
            return
        try:
            self.ser.write(b"S\n")
            self.last_sent = (0, 0)
        except Exception as e:
            self.get_logger().error(f"Serial stop failed: {e}")

    def destroy_node(self):
        try:
            self.ser.close()
        except Exception:
            pass
        super().destroy_node()


def main():
    rclpy.init()
    node = MotorSerialBridge()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
