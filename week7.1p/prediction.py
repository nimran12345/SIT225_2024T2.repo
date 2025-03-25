# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the dataset
df = pd.read_csv("dht_data.csv", encoding="ISO-8859-1")  # Ensure correct file path and encoding

# Rename columns if necessary
df.columns = ["timestamp", "temperature", "humidity"]

# Drop missing values
df = df.dropna()

# Convert data to numeric format
df["temperature"] = pd.to_numeric(df["temperature"], errors="coerce")
df["humidity"] = pd.to_numeric(df["humidity"], errors="coerce")

# Remove extreme values (optional)
df = df[(df["temperature"] > -10) & (df["temperature"] < 50)]  # Temperature range
df = df[(df["humidity"] >= 0) & (df["humidity"] <= 100)]  # Humidity range

# Extract features (X) and labels (y)
X = df[['temperature']].values  # Convert to 2D array
y = df['humidity'].values  # Convert to 1D array

# Train the Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Find the minimum and maximum temperature values
min_temp = df["temperature"].min()
max_temp = df["temperature"].max()

print(f"Min Temperature: {min_temp:.2f}°C")
print(f"Max Temperature: {max_temp:.2f}°C")

# Generate 100 equally spaced test temperature values
test_temps = np.linspace(min_temp, max_temp, 100).reshape(-1, 1)  # Reshape to 2D array

print(f"\nGenerated test temperatures (first 5 values):\n{test_temps[:5]} ...")

# Predict humidity for the generated test temperature values
predicted_humidity = model.predict(test_temps)

# Print the first 5 predicted humidity values
print(f"\nPredicted humidity values (first 5 values):\n{predicted_humidity[:5]} ...")