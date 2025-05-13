#!/usr/bin/python3
"""
This module contains the function add_integer(a, b=98)
which adds two integers or floats after casting them to integers.
"""

def add_integer(a, b=98):
    """Add two integers or floats, casting floats to integers.

    Args:
        a: first number (int or float).
        b: second number (int or float), default is 98.

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: if a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
