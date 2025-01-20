import pandas as pd

file_name = r"C:\Users\subha\Documents\data_py.xlsx"

try:
    # Create a sample DataFrame (the previous code)
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [24, 27, 20],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
    df = pd.DataFrame(data)

    # Write the DataFrame to an Excel file (the previous code)
    df.to_excel(file_name, index=False)

    # Read the Excel file into a DataFrame (new code to modify)
    df_read = pd.read_excel(file_name)

    # Modify an entry in the DataFrame, for example, update Bob's age
    df_read.loc[df_read['Name'] == 'Bob', 'Age'] = 31  # Change Bob's age to 30

    # Write the updated DataFrame back to the Excel file
    df_read.to_excel(file_name, index=False)

    print(df_read)

    print("File updated successfully.")

except FileNotFoundError:
    print(f"{file_name} not found")
except PermissionError:
    print(f"Permission denied: {file_name}. Make sure the directory exists and is writable.")
