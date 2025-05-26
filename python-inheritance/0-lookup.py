#!/usr/bin/python3
"""a function that returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """ this function returns the attribute of an object
    arguments:obj(object)
    Return:A list of attributes is returned
    """
    return dir(obj)
