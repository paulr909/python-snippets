import pandas as pd

import matplotlib.pyplot as plt


df = pd.read_csv("../../sample-data/Inventory_v2.csv")

# df.plot(kind="scatter", x="quantity", y="value")
# plt.show()

# print(df.info())

# print(df.describe())

# Drop rows with NaN
# df.dropna(inplace=True)

# Replace NaN with values
# df.fillna(130, inplace=True)

# print(df.tail())

# df.to_csv("sample-data-v2/inventory-v3.csv", index=False)

print(df["value"].max())
print(df["value"].min())

# Mean = the average value
print(df["value"].mean())
# Median = the value in the middle
print(df["value"].median())
# Mode = the value that appears most frequently
print(df["value"].mode())

# Convert into correct datetime
# df["Date"] = pd.to_datetime(df["Date"])
# Drop rows with NaT
# df.dropna(subset=["Date"], inplace=True)

# Overview of numerical data
# print(df.describe())

# print(df.duplicated())
# df.drop_duplicates(inplace=True)

# Replace values
# df.loc[7, 'Duration'] = 45

# Replace empty value with values
# df["segment"].fillna("INDUSTRIAL", inplace=True)

for x in df.index:
    if df.loc[x, "segment"] == "INDUSTRIAL":
        df.loc[x, "segment"] = "IND"

# Remove the rows that contain wrong data
# for x in df.index:
#     if df.loc[x, "Duration"] > 120:
#         df.drop(x, inplace=True)

# Error, not all values are numbers or floats
# print(df.corr())

# df.to_csv("sample-data-v2/inventory-v3.csv", index=False)
