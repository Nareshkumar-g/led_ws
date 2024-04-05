import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import time

class LEDController(Node):
    def __init__(self):
        super().__init__('led_controller')
        self.port = '/dev/ttyS0'  # Define the serial port
        self.get_logger().info('LED Controller Node started')
        self.subscription = self.create_subscription(
            String,
            'led_color',
            self.led_color_callback,
            10)
        self.subscription

    def setLEDColor(self, r, g, b, s, baudrate):
        # Adjust the serial port with the given baud rate
        with serial.Serial(self.port, baudrate, timeout=1) as serial_port:
            command = f"{r} {g} {b} {s}\n"
            encode_val = command.encode()
            serial_port.write(encode_val)

    def led_color_callback(self, msg):
        color = msg.data.lower()
        if color == 'red':
            self.setLEDColor(0, 0, 1, 1, 115200)
            time.sleep(0.3)
            print("Red is publishing")
        elif color == 'white':
            self.setLEDColor(0, 0, 4, 1, 115200)
            time.sleep(0.3)
            print("White is publishing")
        elif color == 'blink':
            while True:
                self.setLEDColor(225, 5, 0, 1, 115200)
                time.sleep(0.05)
                print("Blink is publishing")
        elif color == 'green':
            self.setLEDColor(0, 0, 0, 0, 57600)
            #time.sleep(0.3)
            print("Green is publishing")
        else:
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


    