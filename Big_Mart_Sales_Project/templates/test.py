import pandas as pd

df = pd.read_csv("Train.csv")
print("Columns:", df.columns.tolist())

if "Item_Fat_Content" in df.columns:
    print("\nUnique values in Item_Fat_Content:")
    print(df["Item_Fat_Content"].unique())
else:
    print("\nNo column named 'Item_Fat_Content'. Check actual name.")
