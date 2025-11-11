#!/usr/bin/python3
"""add_item module
Adds all command-line arguments to a Python list
and saves them to a JSON file.
"""

import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

"""Load existing items from JSON file, if it exists."""

try:
    loaded_items = load_from_json_file("add_item.json")
except FileNotFoundError:
    loaded_items = []
"""Add command-line arguments to the list."""

for arg in sys.argv[1:]:
    loaded_items.append(arg)

save_to_json_file(loaded_items, "add_item.json")
