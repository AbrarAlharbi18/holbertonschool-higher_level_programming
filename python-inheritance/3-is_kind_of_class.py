#!/usr/bin/python3
"""this script checks if a object is an istance of a class
    or its subclass
"""


def is_kind_of_class(obj, a_class):
    """a function that checks the istance of a class
    arguments
        obj:(object) to be inspected
        a_class:(class) the classs whose instance is to be checked
        Return: True if the object is an istance of the class or its subclass
        or False if not
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
