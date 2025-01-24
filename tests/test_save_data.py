# test_save_data.py
# author: Hui Tang
# date: 2025-01-16

import pytest
import os
from unittest.mock import patch, mock_open

from dsci524_group29_webscraping.save_data import save_data


def test_save_data_valid_csv(tmp_path):
    """
    Test saving valid data to a CSV file.
    Ensures the file is created at the specified destination.
    """
    data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
    destination = tmp_path / "output.csv"
    result = save_data(data, format='csv', destination=str(destination))
    assert os.path.exists(result)


def test_save_data_valid_json(tmp_path):
    """
    Test saving valid data to a JSON file.
    Ensures the file is created at the specified destination.
    """
    data = {"name": "Alice", "age": 25}
    destination = tmp_path / "output.json"
    result = save_data(data, format='json', destination=str(destination))
    assert os.path.exists(result)


def test_save_data_invalid_format():
    """
    Test saving data with an unsupported file format.
    Expects a ValueError to be raised.
    """
    data = {"name": "Alice", "age": 25}
    with pytest.raises(ValueError, match="Unsupported format. Use 'csv' or 'json'."):
        save_data(data, format='xml', destination='output.xml')


def test_save_data_invalid_structure_csv():
    """
    Test saving data with an invalid structure for CSV.
    Expects a ValueError to be raised.
    """
    data = {"name": "Alice", "age": 25}
    with pytest.raises(ValueError, match="For CSV, data must be a list of dictionaries."):
        save_data(data, format='csv', destination='output.csv')


def test_save_data_invalid_structure_json():
    """
    Test saving data with an invalid structure for JSON.
    Expects a ValueError to be raised.
    """
    data = 12345  # Not a list or dictionary
    with pytest.raises(ValueError, match="For JSON, data must be a list or a dictionary."):
        save_data(data, format='json', destination='output.json')


def test_save_data_missing_directory():
    """
    Test saving data to a nonexistent directory.
    Expects a FileNotFoundError to be raised.
    """
    data = [{"name": "Alice", "age": 25}]
    with pytest.raises(FileNotFoundError, match="The directory .* does not exist."):
        save_data(data, format='csv', destination='/nonexistent_dir/output.csv')


@patch("builtins.open", side_effect=OSError("File write error"))
def test_save_data_csv_write_failure(mock_open):
    """
    Test a failure during CSV file writing.
    Expects an Exception to be raised.
    """
    data = [{"name": "Alice", "age": 25}]
    with pytest.raises(Exception, match="Failed to save CSV data: File write error"):
        save_data(data, format='csv', destination='output.csv')


@patch("builtins.open", side_effect=OSError("File write error"))
def test_save_data_json_write_failure(mock_open):
    """
    Test a failure during JSON file writing.
    Expects an Exception to be raised.
    """
    data = {"name": "Alice", "age": 25}
    with pytest.raises(Exception, match="Failed to save JSON data: File write error"):
        save_data(data, format='json', destination='output.json')
