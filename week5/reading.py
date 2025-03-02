import serial

# Change this to the correct port (check Arduino IDE > Tools > Port)
SERIAL_PORT = "COM10"  # For Windows (use "COMx")
# SERIAL_PORT = "/dev/ttyUSB0"  # For Linux/Mac

BAUD_RATE = 115200  # Same as Arduino's Serial.begin(115200)

def read_serial():
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            print("Connected to Arduino. Reading data...")
            
            while True:
                line = ser.readline().decode('utf-8').strip()  # Read and clean line
                if line:
                    print("Received:", line)  # Debugging output
                    # Further processing (e.g., storing data) will be done in Step 3

    except serial.SerialException as e:
        print(f"Error: {e}. Check if Arduino is connected.")

# Run the function to start reading data
read_serial()
