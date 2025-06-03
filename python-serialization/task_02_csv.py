#!/usr/bin/env python3
"""
Module to convert CSV data to JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to JSON and saves it as data.json.

    Args:
        csv_filename (str): The input CSV file path.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        with open(csv_filename, 'r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
