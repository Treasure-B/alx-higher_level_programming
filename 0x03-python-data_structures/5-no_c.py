#!/usr/bin/python3

def no_c(my_string):
    """Remove all characters c and C from a string."""
    rmv = [j for j in my_string
           if j != 'c' and j != 'C']
    return "".join(rmv)
