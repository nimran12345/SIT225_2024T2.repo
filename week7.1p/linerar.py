# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import chardet

# Detect the correct file encoding
with open("dht_data.csv", "rb") as f:
    result = chardet.detect(f.read())
    detected_encoding = result["encoding"]  # Get encoding type

# Load the sensor data from CSV with detected encoding
try:
    df = pd.read_csv("dht_data.csv", encoding=detected_encoding)
except UnicodeDecodeError:
    df = pd.read_csv("dht_data.csv", encoding="ISO-8859-1", errors="replace")  # Fallback encoding

# Display first few rows to verify data
print("First few rows of the dataset:")
print(df.head())

# Rename columns properly
df.columns = ["timestamp", "temperature", "humidity"]

# Drop missing values
df = df.dropna()

# Convert to numeric values (ensuring correct data types)
df["temperature"] = pd.to_numeric(df["temperature"], errors="coerce")
df["humidity"] = pd.to_numeric(df["humidity"], errors="coerce")

# Remove extreme values (optional)
df = df[(df["temperature"] > -10) & (df["temperature"] < 50)]  # Temperature range
df = df[(df["humidity"] >= 0) & (df["humidity"] <= 100)]  # Humidity range

# Extract independent (X) and dependent (y) variables
X = df[['temperature']].values  # Convert to 2D array
y = df['humidity'].values  # Convert to 1D array

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Print model parameters
print(f"\nModel Coefficient (Slope): {model.coef_[0]:.4f}")
print(f"Model Intercept: {model.intercept_:.4f}")

# Evaluate model performance
r2_score = model.score(X, y)
print(f"Model R² Score: {r2_score:.4f}")