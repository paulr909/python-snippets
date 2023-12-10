import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("../../sample-data/Inventory_v2.csv")

# df.plot(kind="scatter", x="quantity", y="value")
# plt.show()

# print(df.info())

# print(df.describe())

# df["segment"].fillna("INDUSTRIAL", inplace=True)

# print(df.tail())

# df.to_csv("sample-data-v2/inventory-v3.csv", index=False)

print(df["value"].max())
print(df["value"].min())
# Average
print(df["value"].mean())
# Overview of numerical data
print(df.describe())

# print(df.duplicated())

# for x in df.index:
#     if df.loc[x, "segment"] == "INDUSTRIAL":
#         df.loc[x, "segment"] = "IND"

# Error, not all values are numbers or floats
# print(df.corr())

# df.to_csv("sample-data-v2/inventory-v3.csv", index=False)