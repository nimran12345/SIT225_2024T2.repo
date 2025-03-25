import serial
import csv
import time

# Define serial port and baud rate
SERIAL_PORT = "COM2"  # Change this to match your port (e.g., "/dev/ttyUSB0" for Linux/Mac)
BAUD_RATE = 9600
CSV_FILE = "dht_data.csv"

# Open serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)  # Allow time for Arduino to reset

# Open CSV file in append mode
with open(CSV_FILE, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Temperature (°C)", "Humidity (%)"])  # Write header if new file

    while True:
        try:
            # Read data from serial port
            line = ser.readline().decode('utf-8').strip()
            if line and "Error" not in line:  # Ignore error messages
                data = line.split(",")
                if len(data) == 2:
                    temp, hum = data
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                    writer.writerow([timestamp, temp, hum])
                    print(f"{timestamp} - Temperature: {temp}°C, Humidity: {hum}%")
            
            time.sleep(2)  # Match Arduino delay
        except KeyboardInterrupt:
            print("Data collection stopped.")
            break
        except Exception as e:
            print(f"Error: {e}")

# Close serial connection
ser.close()