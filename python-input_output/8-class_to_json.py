#!/usr/bin/python3
"""serialises the dictionary of the attributes in an object"""


def class_to_json(obj):
    """serialises the dictionary of all attributes in an object
            arguments:obj - the object to be serialised
            return: a dictionary is returned
    """
    attribute = obj.__dict__
    return attribute
