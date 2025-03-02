import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("gyroscope_data.csv")

# Clean the data
# Convert all columns to numeric (forcing errors='coerce' will replace non-numeric values with NaN)
df = df.apply(pd.to_numeric, errors='coerce')

# Remove rows with NaN values (i.e., corrupted or missing data)
df = df.dropna()

# Sort by timestamp
df = df.sort_values(by="timestamp")

# Save cleaned data (optional)
df.to_csv("gyroscope_data_cleaned.csv", index=False)

print("✅ Data cleaned and saved as gyroscope_data_cleaned.csv")

#Plot individual X, Y, Z graphs
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(df["timestamp"], df["x"], label="X-axis", color='r')
plt.xlabel("Timestamp (ms)")
plt.ylabel("X (°/s)")
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(df["timestamp"], df["y"], label="Y-axis", color='g')
plt.xlabel("Timestamp (ms)")
plt.ylabel("Y (°/s)")
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(df["timestamp"], df["z"], label="Z-axis", color='b')
plt.xlabel("Timestamp (ms)")
plt.ylabel("Z (°/s)")
plt.legend()

plt.tight_layout()
plt.savefig("gyro_xyz_separate.png")  # Save the individual plots
plt.show()

# Plot combined graph of X, Y, and Z
plt.figure(figsize=(10, 5))
plt.plot(df["timestamp"], df["x"], label="X-axis", color='r')
plt.plot(df["timestamp"], df["y"], label="Y-axis", color='g')
plt.plot(df["timestamp"], df["z"], label="Z-axis", color='b')
plt.xlabel("Timestamp (ms)")
plt.ylabel("Angular Velocity (°/s)")
plt.title("Gyroscope Data (X, Y, Z)")
plt.legend()
plt.grid()
plt.savefig("gyro_xyz_combined.png")  # Save the combined plot
plt.show()
