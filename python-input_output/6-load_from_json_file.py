#!/usr/bin/python3
"""load_from_json_file module
"""
import json


def load_from_json_file(filename):
    """Return a Python object created from a JSON file."""
    with open(filename, mode="r", encoding="UTF-8") as readFile:
        return json.load(readFile)
