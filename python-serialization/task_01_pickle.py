#!/usr/bin/env python3
"""
Module to pickle and unpickle a custom class.
"""

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the object's attributes in a specific format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the object and saves it to a file.

        Args:
            filename (str): File to save the object to.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            pass  # Silent fail, per instruction (you may log or print if allowed)

    @classmethod
    def deserialize(cls, filename):
        """
        Loads a serialized object from a file.

        Args:
            filename (str): File to load the object from.

        Returns:
            CustomObject | None: The deserialized object or None on failure.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
