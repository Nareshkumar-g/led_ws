import serial
import time

# Setup serial connection parameters
port1 = '/dev/ttyS0'
start_baudrate = 4800  # Starting baud rate
max_baudrate = 150000  # Maximum baud rate to test up to
increment = 4800       # Increment the baud rate by 4800 each time

def setLEDColor(r, g, b, ser):
    # Create command string
    command = f"{r} {g} {b}\n"
    # Encode command string to bytes
    encode_val = command.encode()
    # Send encoded command over serial
    ser.write(encode_val)
    # Optionally, add a delay or wait for a response if necessary

# Iterate through baud rates
for baudrate in range(start_baudrate, max_baudrate + 1, increment):
    try:
        # Attempt to open serial port with the current baud rate
        with serial.Serial(port1, baudrate, timeout=1) as ser1:
            print(f"Testing with baud rate: {baudrate}")
            # Example operation: Set LED color
            setLEDColor(200, 10, 200, ser1)
            time.sleep(0.3)  # Short delay to observe LED change or wait for device response

            # Here you can add any other operations or checks you need to perform
            # For example, checking if the device responded correctly

    except serial.SerialException as e:
        print(f"Failed to open serial port at baud rate {baudrate}: {e}")
    except Exception as e:
        print(f"An error occurred at baud rate {baudrate}: {e}")

    # Delay before next iteration, if needed, to allow hardware to reset, etc.
    time.sleep(1)
