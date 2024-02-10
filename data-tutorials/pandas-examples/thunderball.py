import pandas as pd

# Data upto 02-Jan-2024
df = pd.read_csv("../../sample-data/thunderball-draw-history.csv")

# print(df.head())
# print(df.shape)

print("Ball 1 most common (mode):", df["Ball 1"].mode()[0])
print("Ball 2 most common (mode):", df["Ball 2"].mode()[0])
print("Ball 3 most common (mode):", df["Ball 3"].mode()[0])
print("Ball 4 most common (mode):", df["Ball 4"].mode()[0])
print("Ball 5 most common (mode):", df["Ball 5"].mode()[0])
print("Thunderball most common (mode):", df["Thunderball"].mode()[0])

# print(df.mode())

# print("Ball 1 middle (median):", df["Ball 1"].median())
# print("Ball 2 middle (median):", df["Ball 2"].median())
# print("Ball 3 middle (median):", df["Ball 3"].median())
# print("Ball 4 middle (median):", df["Ball 4"].median())
# print("Ball 5 middle (median):", df["Ball 5"].median())
# print("Thunderball middle (median):", df["Thunderball"].median())

print(df["Ball 1"].value_counts().to_frame())
print(df["Ball 2"].value_counts().to_frame())
print(df["Ball 3"].value_counts().to_frame())
print(df["Ball 4"].value_counts().to_frame())
print(df["Ball 5"].value_counts().to_frame())
print(df["Thunderball"].value_counts().to_frame())
