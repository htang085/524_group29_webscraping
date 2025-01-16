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
    pass
