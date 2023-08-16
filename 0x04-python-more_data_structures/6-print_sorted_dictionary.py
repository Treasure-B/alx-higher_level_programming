#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys."""
    sort_keys = sorted(a_dictionary.keys())
    for keys in sort_keys:
        print(keys + ": " + str(a_dictionary[keys]))
