#!/usr/bin/python3
"""a class that is a subclass and initialises an object"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
    Instantiation with width and height: def __init__(self, width, height)
    width and height must be private. No getter or setter
    width and height must be positive integers, validated by integer_validator
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
