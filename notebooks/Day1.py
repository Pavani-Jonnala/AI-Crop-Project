import pandas as pd

# Read Dataset
df = pd.read_csv("datasets/crop/Crop_recommendation.csv")

# First 5 Rows
print("===== First 5 Rows =====")
print(df.head())

# Last 5 Rows
print("\n===== Last 5 Rows =====")
print(df.tail())

# Shape
print("\n===== Shape =====")
print(df.shape)

# Column Names
print("\n===== Column Names =====")
print(df.columns)