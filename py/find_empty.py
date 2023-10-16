import os
import pandas as pd

# Define the main folder path containing four subfolders
main_folder_path = 'test_sort'

# Function to check if the CSV is empty
def is_csv_empty(file_path):
    try:
        df = pd.read_csv(file_path)
        return df.empty
    except (pd.errors.EmptyDataError, pd.errors.ParserError):
        return True

# Function to traverse through all subfolders recursively
def process_subfolders(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                if is_csv_empty(file_path):
                    print(f"Empty CSV: {file_path}")

# Traverse through all four subfolders in the main folder
for subfolder_name in os.listdir(main_folder_path):
    subfolder_path = os.path.join(main_folder_path, subfolder_name)
    process_subfolders(subfolder_path)
