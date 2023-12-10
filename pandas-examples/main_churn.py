import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# import matplotlib.pyplot as plt


df = pd.read_csv("../sample-data/Churn_Modelling.csv")

# print(df.shape)
# print(df.columns)

# Drop columns with axis=1
# df.drop(["RowNumber", "CustomerId", "Surname", "CreditScore"], axis=1, inplace=True)
# print(df.shape)

# Select columns with usecols=["X", "Y", "Z"]
df_spec = pd.read_csv(
    "../sample-data/Churn_Modelling.csv",
    usecols=["Gender", "Age", "Tenure", "Balance"],
)
# print(df_spec.head())

# Select columns with usecols=[*range(0, 10)]
df_range = pd.read_csv("../sample-data/Churn_Modelling.csv", usecols=[*range(0, 10)])
# print(df_range.head())

# Select 500 rows
df_partial = pd.read_csv("../sample-data/Churn_Modelling.csv", nrows=500)
# print(df_partial.shape)

# Skip first 500 rows
df_skip = pd.read_csv("../sample-data/Churn_Modelling.csv", skiprows=500)
# print(df_skip.shape)

# Select sample data
df_sample = df.sample(n=1000)
# print(df_sample.shape)

df_sample2 = df.sample(frac=0.1)
# print(df_sample2.shape)

# Check for missing values
# print(df.isna().sum())

# Adding missing values using loc and iloc
missing_index = np.random.randint(10000, size=20)
df.loc[missing_index, ["Balance", "Geography"]] = np.nan
df.iloc[missing_index, -1] = np.nan
# print(df.isna().sum())

df_geography = df["Geography"].value_counts()
# print(df_geography)

mode = df["Geography"].value_counts().index[0]
df["Geography"].fillna(value=mode, inplace=True)

df_geography2 = df["Geography"].value_counts()
# print(df_geography2)

avg = df["Balance"].mean()
df["Balance"].fillna(value=avg, inplace=True)

avg = df["Balance"].mean()
# print(avg)

# Drop missing values
df.dropna(axis=0, how="any", inplace=True)
# print(df)

# print(df.isna().sum().sum())

# Selecting rows based on condition
france_churn = df[(df.Geography == "France") & (df.Exited == 1)]
# print(france_churn.Geography.value_counts())

# Use query function
df2 = df.query("80000 < Balance < 100000")

df2["Balance"].plot(kind="hist", figsize=(8, 5))
# plt.show()

# Describing the conditions with isin
isin_tenure = df[df["Tenure"].isin([4, 6, 9, 10])][:3]

# print(isin_tenure)

# groupby function
group_by_gender = (
    df[["Geography", "Gender", "Exited"]].groupby(["Geography", "Gender"]).mean()
)
# print(group_by_gender)

# Multiple aggregate functions with groupby
multiple = (
    df[["Geography", "Gender", "Exited"]]
    .groupby(["Geography", "Gender"])
    .agg(["mean", "count"])
)
# print(multiple)

# Applying different aggregate functions to different groups
df_summary = (
    df[["Geography", "Exited", "Balance"]]
    .groupby("Geography")
    .agg({"Exited": "sum", "Balance": "mean"})
)
df_summary.rename(
    columns={
        "Exited": "Number of churned customers",
        "Balance": "Average balance of customers",
    },
    inplace=True,
)
# print(df_summary)

# Reset the index
df_new = (
    df[["Geography", "Exited", "Balance"]]
    .groupby(["Geography", "Exited"])
    .mean()
    .reset_index()
)
# print(df_new)

# Reset the index with a drop
reset = df[["Geography", "Exited", "Balance"]].sample(n=6).reset_index()
# print(reset)

# The index is reset but the original is kept as a new column. We can drop it while
# resetting the index
reset2 = df[["Geography", "Exited", "Balance"]].sample(n=6).reset_index(drop=True)
# print(reset2)

# Set a particular column as the index
df_geography_index = df_new.set_index("Geography")
# print(df_geography_index)

# Inserting a new column
group = np.random.randint(10, size=6)
# df_new["Group"] = group
# print(df_new)

# Insert at particular column
df_new.insert(0, "Group", group)
# print(df_new)

# Where function
# df_new["Balance"] = df_new["Balance"].where(df_new["Group"] >= 6, 0)
# print(df_new)

# Rank function
# df_new["rank"] = df_new["Balance"].rank(method="first", ascending=False).astype("int")
# print(df_new)

# Number of unique values in a column
# print(df.Geography.value_counts().size)

# Number of unique values in a column
# print(df.Geography.nunique())

# Check memory usage
# print(df.memory_usage(deep=True))

# Category data type
data = df["Geography"] = df["Geography"].astype("category")
# print(data)

# Replacing values
df_new["Group"].replace(0, "B1")
# print(df_new)

# Replacing values with a dictionary
df_new["Group"].replace({0: "B1", 1: "B2"}, inplace=True)
# print(df_new)

# Draw a histogram
df["Balance"].plot(kind="hist", figsize=(10, 6), title="Customer Balance")
# plt.show()

# Reducing the decimal points of floats
# df_new.round(2)
# print(df_new)

# Changing the display options
pd.set_option("display.precision", 2)
# print(df_new)

# Calculating the percentage change through a column
ser = pd.Series([4, 5, 2, 5, 6, 10, 12])
# print(ser.pct_change())

# Filtering based on strings
start = df_new[df_new.Geography.str.startswith("Fr")]
# print(start)

# Styling a dataframe
df_new.style.highlight_max(axis=0, color="darkgreen")
print(df_new)
