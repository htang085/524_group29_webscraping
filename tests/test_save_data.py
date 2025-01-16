import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from _524_group29_webscraping.save_data import save_data

def test_save_data_valid_csv(tmp_path):
    data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
    destination = tmp_path / "output.csv"
    result = save_data(data, format='csv', destination=str(destination))
    assert os.path.exists(result)

def test_save_data_valid_json(tmp_path):
    data = {"name": "Alice", "age": 25}
    destination = tmp_path / "output.json"
    result = save_data(data, format='json', destination=str(destination))
    assert os.path.exists(result)

def test_save_data_invalid_format():
    data = {"name": "Alice", "age": 25}
    with pytest.raises(ValueError):
        save_data(data, format='xml', destination='output.xml')

def test_save_data_invalid_structure_csv():
    data = {"name": "Alice", "age": 25}
    with pytest.raises(ValueError):
        save_data(data, format='csv', destination='output.csv')

def test_save_data_missing_directory():
    data = [{"name": "Alice", "age": 25}]
    with pytest.raises(FileNotFoundError):
        save_data(data, format='csv', destination='/nonexistent_dir/output.csv')
