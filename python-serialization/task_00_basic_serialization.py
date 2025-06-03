# task_00_basic_serialization.py

import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a dictionary to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the file to save JSON to.
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)  # indent for readability


def load_and_deserialize(filename):
    """
    Loads JSON data from a file and deserializes it into a dictionary.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        dict: The deserialized data.
    """
    with open(filename, 'r') as file:
        return json.load(file)
