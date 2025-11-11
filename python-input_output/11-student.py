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

        filtered = {}
        for attr in attrs:
            if not isinstance(attr, str):
                return self.__dict__
            if attr in self.__dict__:
                filtered[attr] = self.__dict__[attr]
        return filtered

    def reload_from_json(self, json):
        """Replace all attributes of the Student using a JSON dictionary."""
        for key, value in json.items():
            self.__dict__[key] = value
