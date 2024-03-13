#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a Python object.

    Args:
        my_obj: The object to be converted to a JSON-formatted string.

    Returns:
        str: The JSON representation of the input object.
    """
    return json.dumps(my_obj)
