import serial
import firebase_admin
from firebase_admin import credentials, db
import json

#  Setup Serial Communication (Update COM port accordingly)
SERIAL_PORT = "COM10"  # Change this based on Arduino's port
BAUD_RATE = 115200

# Initialize Firebase
cred = credentials.Certificate(r"C:\Users\engha\Downloads\sit225gyrodata-firebase-adminsdk-fbsvc-dc40692ab1.json")  # Your downloaded Firebase key
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://sit225gyrodata-default-rtdb.firebaseio.com/"  # Replace with your Firebase DB URL
})
ref = db.reference("gyroscope_data")  # Database node where data is stored

# Read data from Arduino and upload to Firebase
def read_and_upload():
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            print("Connected to Arduino. Reading and uploading data...")

            while True:
                line = ser.readline().decode('utf-8').strip()  # Read and clean Serial input
                if line:
                    try:
                        timestamp, x, y, z = line.split(",")  # Split received data
                        data = {
                            "timestamp": int(timestamp),
                            "x": float(x),
                            "y": float(y),
                            "z": float(z)
                        }
                        ref.push(data)  # Upload data to Firebase
                        print("Uploaded:", json.dumps(data))

                    except ValueError:
                        print("Invalid data format:", line)  # Handle data errors

    except serial.SerialException as e:
        print(f"Error: {e}. Check if Arduino is connected.")

# Run the function
read_and_upload()
