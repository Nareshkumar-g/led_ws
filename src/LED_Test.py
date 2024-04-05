import serial
import time

# Setup serial connection
port1 = '/dev/ttyS0'
ser1 = serial.Serial(port1, baudrate=115200, timeout=1)

def setLEDColor(r, g, b, s):
    # Create command string
    command = "{} {} {} {}\n".format(r,g,b,s)
    # Encode command string
    encode_val = command.encode()
    print(encode_val)
    # Send encoded command over serial
    ser1.write(encode_val)
    #data_to_send = b'\x7E\x32\x30\x30\x31\x34\x36\x34\x32\x45\x30\x30\x32\x30\x31\x46\x44\x33\x35\x0D'
    
try:
    while True:
        # Set LED strip color to blue
        # for e in range(200,256):
        #     for i in range(204,256):  # Range goes from 0 to 255
        #         for b in range(256):  # Range goes from 0 to 255
        # for e in range(0,256):
        #     setLEDColor(225, e, 0, 1)
        #     time.sleep(1.0)
        #             #setLEDColor(0,0,57,1)
        #             # Wait for 1 second
        #setLEDColor(255,255,255)
        #setLEDColor(0,0,0)
        setLEDColor(225,5,0,1)
        time.sleep(0.05)
        # setLEDColor(0,0,4,1)                ## white
        # setLEDColor(0,0,7,1)                ## lite red
        # setLEDColor(0,0,1,1)                ## Red
        # setLEDColor(0,0,0) at baudrate 57600 ##Green
        # setLEDColor(0,0,0) at baudrate 38400 ##off
        # # Wait for 1 second
        # time.sleep(1)
        # setLEDColor(0,0,1,1)
        # # Wait for 1 second
        # time.sleep(1)
except KeyboardInterrupt:
    # Close serial connection when the script is stopped
    ser1.close()
    print("Script stopped.")
