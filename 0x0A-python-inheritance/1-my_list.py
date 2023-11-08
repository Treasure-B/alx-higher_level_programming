#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """An inherited list class that provides a method for sorted printing."""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
