#!/usr/bin/python3
"""a script that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """A function that reads and prints the content of a file to STDOUT
        Arguments
        filename:(string) the name of the file or its relative path
    """
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
