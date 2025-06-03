#!/usr/bin/python3
"""A script that writes into a text file"""


def write_file(filename="", text=""):
    """A function that writes into a text file
        Arguments:
            filename:(string) the name of the file or its relative path
            text:(string) the string content to be written into the file
        Return: the number of characters written is returned
    """
    with open(filename, "w") as File:
        File.write(text)
        return len(text)
