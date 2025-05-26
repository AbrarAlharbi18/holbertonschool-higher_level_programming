#!/usr/bin/python3
"""creates a class that raises an exception"""


class BaseGeometry:
    """this class raises an exception"""
    def area(self):
        raise Exception("area() is not implemented")
