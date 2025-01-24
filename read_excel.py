import pandas as pd

#file name = 'D:\\sales_data.xlsx'
file_name = "C:\\excel\\data_py.xlsx"

# Step 1: Load your Excel data
try:
    data = pd.read_excel(file_name)

    print(data.head())
except FileNotFoundError:
    print("{} not found".format(file_name))