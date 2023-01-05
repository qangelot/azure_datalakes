import pandas as pd
import glob

# Find all CSV files in the directory
csv_files = glob.glob('*.csv')

# Create an empty list to store the dataframes
df_list = []

# Iterate through the list of CSV files and read each one into a dataframe
for file in csv_files:
    df = pd.read_csv(file)
    df_list.append(df)

# Merge all the dataframes into a single dataframe
df_merged = pd.concat(df_list)

# Rename the 'company_name' column to 'stock_name'
df_merged.rename(columns={'company_name': 'stock_name'}, inplace=True)
