#!/usr/bin/python3

def uniq_add(my_list=[]):
    """adds all unique integers in a list"""
    uniq_set = set(my_list)
    sum = 0

    for element in uniq_set:
        sum += element
        return (sum)
