import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import time
import threading

class LEDController(Node):
    def __init__(self):
        super().__init__('led_controller')
        self.port = '/dev/ttyS0'  # Define the serial port
        self.blink_active = False  # Flag to control the blink loop
        self.get_logger().info('LED Controller Node started')
        self.subscription = self.create_subscription(
            String,
            'led_color',
            self.led_color_callback,
            10)
        self.blink_thread = None  # Reference to the blink thread

    def setLEDColor(self, r, g, b, s, baudrate):
        with serial.Serial(self.port, baudrate, timeout=1) as serial_port:
            command = f"{r} {g} {b} {s}\n"
            encode_val = command.encode()
            serial_port.write(encode_val)

    def blink_led(self):
        # Toggle the LED on and off with a 0.5-second interval
        while self.blink_active:
            self.setLEDColor(225, 5, 0, 1, 115200)  # Example values for "on" state
            time.sleep(0.05)
            # self.setLEDColor(0, 0, 0, 0, 115200)  # Assuming these values turn the LED "off"
            # time.sleep(0.5)

    def led_color_callback(self, msg):
        color = msg.data.lower()
        if color == 'red':
            self.blink_active = False  # Ensure blinking stops
            self.setLEDColor(0, 0, 1, 1, 115200)
            print("Red is publishing")
        elif color == 'white':
            self.blink_active = False  # Ensure blinking stops
            self.setLEDColor(0, 0, 4, 1, 115200)
            print("White is publishing")
        elif color == 'blink':
            if not self.blink_active:
                self.blink_active = True
                if self.blink_thread is None or not self.blink_thread.is_alive():
                    self.blink_thread = threading.Thread(target=self.blink_led)
                    self.blink_thread.start()
            print("Blink is publishing")
        elif color == 'green':
            self.blink_active = False  # Ensure blinking stops
            self.setLEDColor(0, 0, 0, 0, 57600)
            print("Green is publishing")
        else:
            self.blink_active = False  # Ensure blinking stops
            self.get_logger().error(f"Received an unknown color specification: {color}")

def main(args=None):
    rclpy.init(args=args)
    led_controller = LEDController()

    try:
        rclpy.spin(led_controller)
    except KeyboardInterrupt:
        pass
    finally:
        # The serial port is automatically closed when exiting the with statement
        led_controller.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
