import os
import json
import csv

def save_data(data, format='csv', destination='output.csv'):
    """
    Saves the extracted data into the specified format at the given destination.

    Parameters:
    data (list or dict): The data to be saved. For CSV, it must be a list of dictionaries.
    format (str): The file format to save the data ('csv', 'json').
    destination (str): The file path where the data will be saved.

    Returns:
    str: The absolute path to the saved file.

    Raises:
    ValueError: If the format is unsupported or the data structure is incompatible.
    FileNotFoundError: If the destination directory does not exist.
    """
    # Validate the destination directory
    dir_path = os.path.dirname(destination)
    if dir_path and not os.path.exists(dir_path):
        raise FileNotFoundError(f"The directory {dir_path} does not exist.")

    # Save as CSV
    if format == 'csv':
        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            raise ValueError("For CSV, data must be a list of dictionaries.")
        try:
            with open(destination, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
        except Exception as e:
            raise Exception(f"Failed to save CSV data: {e}")

    # Save as JSON
    elif format == 'json':
        if not isinstance(data, (list, dict)):
            raise ValueError("For JSON, data must be a list or a dictionary.")
        try:
            with open(destination, mode='w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            raise Exception(f"Failed to save JSON data: {e}")

    else:
        raise ValueError("Unsupported format. Use 'csv' or 'json'.")

    return os.path.abspath(destination)
