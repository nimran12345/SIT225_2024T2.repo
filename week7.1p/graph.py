# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the dataset (Ensure correct encoding)
df = pd.read_csv("dht_data.csv", encoding="ISO-8859-1")

# Rename columns (if needed)
df.columns = ["timestamp", "temperature", "humidity"]

# Drop missing values
df = df.dropna()

# Convert to numeric format
df["temperature"] = pd.to_numeric(df["temperature"], errors="coerce")
df["humidity"] = pd.to_numeric(df["humidity"], errors="coerce")

# Remove extreme values (optional)
df = df[(df["temperature"] > -10) & (df["temperature"] < 50)]  # Valid temperature range
df = df[(df["humidity"] >= 0) & (df["humidity"] <= 100)]  # Valid humidity range

# Extract independent (X) and dependent (y) variables
X = df[['temperature']].values  # Convert to 2D array
y = df['humidity'].values  # Convert to 1D array

# Train the Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Generate 100 equally spaced test temperature values
min_temp = df["temperature"].min()
max_temp = df["temperature"].max()
test_temps = np.linspace(min_temp, max_temp, 100).reshape(-1, 1)  # Reshape for model

# Predict humidity for test temperatures
predicted_humidity = model.predict(test_temps)

# Scatter plot of actual temperature vs humidity
plt.scatter(df["temperature"], df["humidity"], color="blue", label="Actual Data", alpha=0.6)

# Plot the regression trend line
plt.plot(test_temps, predicted_humidity, color="red", linewidth=2, label="Trend Line")

# Add labels, title, and legend
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.title("Temperature vs Humidity (with Linear Regression)")
plt.legend()

# Show the plot
plt.show()