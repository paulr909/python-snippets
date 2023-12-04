import pandas as pd


df = pd.read_csv("sample-data-v2/Inventory_v2.csv")

# Write to spreadsheet
df.to_excel("sample-data-v2/inventory-v3.xlsx", index=False)

excel_file = pd.read_excel("sample-data-v2/inventory-v3.xlsx")

print(excel_file)
