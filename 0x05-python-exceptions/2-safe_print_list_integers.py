#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers."""
    num = 0
    for k in range(x):
        try:
            if type(my_list[k]) == int:
                print("{:d}".format(my_list[k]), end="")
                num += 1
        except IndexError:
            break
    print("")
    return (num)
