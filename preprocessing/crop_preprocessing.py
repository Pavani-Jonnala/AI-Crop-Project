import pandas as pd

# Load Crop Dataset
df = pd.read_csv("datasets/crop/Crop_recommendation.csv")

# Display first 5 rows
print("First 5 Rows")
print(df.head())

# Display dataset shape
print("\nDataset Shape")
print(df.shape)

# Display column names
print("\nColumns")
print(df.columns)

# Display dataset information
print("\nDataset Information")
print(df.info())