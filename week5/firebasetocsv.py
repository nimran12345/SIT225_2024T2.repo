import firebase_admin
from firebase_admin import credentials, db
import pandas as pd

#Initialize Firebase
cred = credentials.Certificate(r"C:\Users\engha\Downloads\sit225gyrodata-firebase-adminsdk-fbsvc-dc40692ab1.json")  # Update with your Firebase credentials file
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://sit225gyrodata-default-rtdb.firebaseio.com/"  # Replace with your Firebase DB URL
})

#Reference the "gyroscope_data" node in Firebase
ref = db.reference("gyroscope_data")

# Retrieve all data from Firebase
data = ref.get()

# Process data into a Pandas DataFrame
if data:
    records = []
    for key, value in data.items():
        records.append(value)  # Extract values (timestamp, x, y, z)

    # Convert to DataFrame
    df = pd.DataFrame(records)
    
    # Sort by timestamp
    df = df.sort_values(by="timestamp")

    # Save data to CSV file
    df.to_csv("gyroscope_data.csv", index=False)

    print("Data successfully saved to gyroscope_data.csv")
else:
    print("No data found in Firebase.")

