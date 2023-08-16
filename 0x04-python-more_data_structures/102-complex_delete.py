#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """deletes keys with a specific value in a dictionary."""
    keys_del = []
    for k, val in a_dictionary.items():
        if val == value:
            keys_del.append(k)
    for k in keys_del:
        del a_dictionary[k]
    return a_dictionary
