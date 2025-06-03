#!/usr/bin/python3
""" writes an object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a file
    argument
        my_obj: the object to be written to the file
        filename: the name of the file or its relative path
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
