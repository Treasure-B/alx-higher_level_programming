#!/usr/bin/python3

def uniq_add(my_list=[]):
    """adds all unique integers in a list"""
    uniq_set = set(my_list)
    result = 0

    for element in uniq_set:
        result += element
