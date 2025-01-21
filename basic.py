# Pandas dataframe to an excel file

import pandas as pd

file_name = r"C:\Users\subha\Documents\output.xlsx"

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Modify an entry in the DataFrame, for example, update Bob's age
df.loc[df['Name'] == 'Bob', 'Age'] = 32  # Change Bob's age to 30

# Write the DataFrame to an Excel file
df.to_excel(file_name, index=False)