#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in a list"""
    return [result % 2 == 0 for result in my_list]
