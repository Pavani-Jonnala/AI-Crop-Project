import pandas as pd
import os

base = "datasets"

folders = ["crop", "climate", "soil", "flood", "fertilizer"]

for folder in folders:

    folder_path = os.path.join(base, folder)

    print("\n==============================")
    print("FOLDER:", folder)
    print("==============================")

    if not os.path.exists(folder_path):
        print("Folder not found")
        continue

    files = os.listdir(folder_path)

    for file in files:

        if file.endswith(".csv"):

            path = os.path.join(folder_path, file)

            print("\nFILE:", file)

            try:
                df = pd.read_csv(path)

                print("Shape:", df.shape)

                print("Columns:")
                print(list(df.columns))

                print("\nFirst 3 rows:")
                print(df.head(3))

            except Exception as e:
                print("Error:", e)