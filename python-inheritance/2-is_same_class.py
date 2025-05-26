#!/usr/bin/python3
"""checks if an object belongs to a class"""


def is_same_class(obj, a_class):
    """a function that checks for the instance of a class
    arguments: obj(object): the object to be inspected
                a_class(class): the class whose instance is to be
                inspected
    """
    if type(obj) is a_class:
        return True
    else:
        return False
