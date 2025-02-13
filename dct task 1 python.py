import serial
import random
import time
from datetime import datetime

# Set up serial connection (make sure to replace with your correct port)
ser = serial.Serial('COM10', 9600)  # Replace 'COM3' with your actual port
time.sleep(2)  # Wait for the serial connection to initialize

while True:
    random_number = random.randint(1, 10)  # Generate a random number
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get current timestamp
    ser.write(str(random_number).encode())  # Send the random number to Arduino
    print(f"{timestamp} - Sent: {random_number}")  # Log the sending event
    response = ser.readline().decode().strip()  # Wait for response from Arduino
    print(f"{timestamp} - Received: {response}")  # Log the response
    time.sleep(int(response))  # Wait for the number of seconds received
    print(f"{timestamp} - Sleeping for {response} seconds")