#!/usr/bin/python3
"""
Module that returns Pascal's Triangle up to n rows.
"""

def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to n rows.

    Args:
        n (int): Number of rows

    Returns:
        List[List[int]]: Pascal's Triangle as a list of lists
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for row_num in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for i in range(1, row_num):
            new_row.append(prev_row[i - 1] + prev_row[i])

        new_row.append(1)
        triangle.append(new_row)

    return triangle
