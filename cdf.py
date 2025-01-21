# Creating a DataFrame

import pandas as pd

file_name = r"C:\Users\subha\Documents\data.xlsx"
csv_path = r"C:\Users\subha\Documents\data.csv"

# From dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}
df = pd.DataFrame(data)

# df.to_excel(file_name, index=False)
# df.to_csv(csv_path)

# From CSV
df = pd.read_csv(csv_path)

print(df.head())

# From Excel
df = pd.read_excel(file_name)

print(df.head())