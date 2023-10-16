import os
import pandas as pd

# Define the folder path containing CSV files
folder_path = 'dummy'

# Function to handle missing values in 'oi' and 'VWAP' columns and replace with zeros
def handle_missing_data(file_path):
    try:
        df = pd.read_csv(file_path)

        # Fill missing values in 'oi' column with 0
        df['oi'].fillna(0, inplace=True)

        # Fill missing values in 'VWAP' column with 0
        df['VWAP'].fillna(0, inplace=True)

        # Save the DataFrame back to the CSV file
        df.to_csv(file_path, index=False)

    except (pd.errors.EmptyDataError, pd.errors.ParserError) as e:
        # Handle any file reading or parsing errors and print the error message
        print(f"Error occurred while processing '{file_path}': {e}")

# Process all CSV files in the specified folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)
        handle_missing_data(file_path)
