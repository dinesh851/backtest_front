import os
import pandas as pd

# Define the main folder path containing four subfolders
main_folder_path = 'test_sort'

# Function to calculate VWAP and update CSV file
def calculate_and_update_vwap(file_path):
    try:
        df = pd.read_csv(file_path)

        # Check if 'volume' column exists in the DataFrame
        if 'volume' in df.columns:
            # Calculate VWAP for each row
            df['VWAP'] = (df['close'] * df['volume']).cumsum() / df['volume'].cumsum()

            # Round VWAP to 2 decimal places
            df['VWAP'] = df['VWAP'].round(4)

            # Save the DataFrame back to the CSV file
            df.to_csv(file_path, index=False)
        else:
            # If 'volume' column is missing, do not add or delete VWAP column
            if 'VWAP' in df.columns:
                # Delete 'VWAP' column if it exists with a value of 0
                if df['VWAP'].sum() == 0:
                    df.drop(columns=['VWAP'], inplace=True)
                    df.to_csv(file_path, index=False)
    except (pd.errors.EmptyDataError, pd.errors.ParserError) as e:
        # Handle any file reading or parsing errors and print the error message
        print(f"Error occurred while processing '{file_path}': {e}")

# Function to traverse through all subfolders recursively
def process_subfolders(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            print(file)
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                calculate_and_update_vwap(file_path)

# Traverse through all four subfolders in the main folder
for subfolder_name in os.listdir(main_folder_path):
    subfolder_path = os.path.join(main_folder_path, subfolder_name)
    process_subfolders(subfolder_path)
