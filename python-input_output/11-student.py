#!/usr/bin/python3
"""a script that creates a class"""


class Student:
    """a class called student that has the following atttributes
        Attributes:
            first_name
            last_name
            age
            _json: retrieves a dictionary of the instance attributes
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, lis=[]):
        if isinstance(lis, list):
            if len(lis) == 0:
                return self.__dict__
            dic = self.__dict__
            new = {}
            for i in lis:
                if i in dic:
                    value = dic[i]
                    new[i] = value
        return new

    def reload_from_json(self, json):
        if len(json) != 0:
            for i in json.keys():
                if i in self.__dict__:
                    self.__dict__[i] = json[i]
        return self.__dict__
