# CREATING DATA FRAME

# Import pandas library
import pandas as pd

# Define file paths
file_name = r"C:\Users\subha\Documents\data.xlsx"
csv_path = r"C:\Users\subha\Documents\data.csv"

# Create DataFrame from dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 31, 32],
    'Salary': [50000, 60000, 70000]
}
df = pd.DataFrame(data)

# Save DataFrame to Excel
df.to_excel(file_name, index=False)
# Save DataFrame to CSV
df.to_csv(csv_path)

# Load DataFrame from CSV
df = pd.read_csv(csv_path)

# Print first 5 rows
print(df.head())

# Load DataFrame from Excel
df = pd.read_excel(file_name)

# Print first 5 rows
print(df.head())
