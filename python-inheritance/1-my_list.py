#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """a class which inherits a built in list class
    attribute: a public object method which sorts
    and prints the list object
    """
    def print_sorted(self):
        sort = sorted(self)
        print(sort)
