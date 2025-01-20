import pandas as pd

file_name = r"C:\Users\subha\Documents\data_py.xlsx"

try:
    # Read the Excel file into a DataFrame
    df_read = pd.read_excel(file_name)

    # Display the contents of the DataFrame
    print(df_read)

except FileNotFoundError:
    print(f"{file_name} not found")
except PermissionError:
    print(f"Permission denied: {file_name}. Make sure the directory exists and is accessible.")
