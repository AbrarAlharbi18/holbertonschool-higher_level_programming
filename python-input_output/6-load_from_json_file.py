#!/usr/bin/python3
"""creates an object from a file containing JSON string"""
import json


def load_from_json_file(filename):
    """a function that creates an object from a file"""
    with open(filename, "r") as f:
        return json.load(f)
