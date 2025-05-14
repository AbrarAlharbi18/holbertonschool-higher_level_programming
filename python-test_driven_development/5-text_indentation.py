#!/usr/bin/python3
"""function that prints a text with 2 new lines after each ., ? and : """


def text_indentation(text):
    """args:
            text:(string) the string to be printed
        raise:
            TypeErrror:text must be a string is raised if the argument
            passed to the function is not a string
    """
    new_line = (".", "?", ":")
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i in new_line:
            print(i, end="")
            print()
            print()
        else:
            print(i, end="")
