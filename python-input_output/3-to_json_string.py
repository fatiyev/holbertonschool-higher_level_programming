#!/usr/bin/python3
"""to_json_string module
"""

import json


def to_json_string(my_obj):
    """Return JSON representation of my_obj."""
    return json.dumps(my_obj)
