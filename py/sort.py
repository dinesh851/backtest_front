import os
import pandas as pd

folder_path = "unsorted - Copy\market_data_2023"  # Replace with the actual path to your folder

def delete_files_with_conditions(folder_path):
    # Iterate through all files and subfolders in the given folder
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(".csv"):  # Check if the file is a CSV file
                 if "CE" in file_name or "PE" in file_name:
                    file_path = os.path.join(root, file_name)
                    
                    # Read the CSV file into a pandas DataFrame
                    df = pd.read_csv(file_path)
                    
                    # Check if the DataFrame meets the conditions
                    if (len(df) < 300 or 
                        df[:190][['close', 'open', 'high', 'low']].max().max() < 30 or
                        df[:190][['close', 'open', 'high', 'low']].min().min() > 300 ):
                        
                        # Delete the file
                        os.remove(file_path)
                        print(f"Deleted file: {file_path}")

# Call the function to delete files in the main folder and its subfolders
delete_files_with_conditions(folder_path)
