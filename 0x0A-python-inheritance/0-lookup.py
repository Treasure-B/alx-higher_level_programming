#!/usr/bin/python3
"""This script defines an object attribute lookup function."""


def lookup(obj):
    """Returns a available attributes and methods of an object."""
    return dir(obj)
