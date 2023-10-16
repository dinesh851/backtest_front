import os
import pandas as pd

# Define the folder path containing CSV files
main_folder_path = 'test_sort'

# Function to handle missing values in 'oi' and 'VWAP' columns and replace with 0
def handle_missing_data(file_path):
    try:
        df = pd.read_csv(file_path)

        # Fill missing values in 'oi' column with 0
        df['oi'].fillna(0, inplace=True)

        # Fill missing values in 'VWAP' column with 0
        df['VWAP'].fillna(0, inplace=True)

        # Convert 'oi' and 'VWAP' columns to integers
        df['oi'] = df['oi'].astype(int)
        df['VWAP'] = df['VWAP'].astype(int)

        # Save the DataFrame back to the CSV file
        df.to_csv(file_path, index=False)

    except (pd.errors.EmptyDataError, pd.errors.ParserError) as e:
        # Handle any file reading or parsing errors and print the error message
        print(f"Error occurred while processing '{file_path}': {e}")

# Function to traverse through all subfolders recursively
def process_subfolders(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                handle_missing_data(file_path)

# Traverse through all four subfolders in the main folder
for subfolder_name in os.listdir(main_folder_path):
    subfolder_path = os.path.join(main_folder_path, subfolder_name)
    process_subfolders(subfolder_path)