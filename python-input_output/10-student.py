#!/usr/bin/python3
"""Student module
"""


class Student:
    """Represents a student with basic attributes."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student.
        
        If `attrs` is a list of strings, only those attributes
        will be included in the returned dictionary.
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__

        temp = {}
        for elem in attrs:
            if not isinstance(elem, str):
                return self.__dict__
            if elem in self.__dict__:
                temp[elem] = self.__dict__[elem]
        return temp
