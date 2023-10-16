import os
import json

def get_folder_names(directory):
    folder_names = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
    return folder_names

def save_to_json(folder_names, json_file):
    with open(json_file, 'w') as file:
        json.dump(folder_names, file, indent=4)

if __name__ == "__main__":
    target_directory = "test_sort\market_data_2023"  # Replace with the path to your target folder
    json_file_path = "2023.json"  # Replace with the desired path for the JSON file

    folders = get_folder_names(target_directory)
    save_to_json(folders, json_file_path)
