#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints x elements of a list."""

    num = 0
    try:
        for j in range(x):
            print("{}".format(my_list[j]), end=" ")
            num += 1
    except IndexError:
        print("Error: Index out of range")
        print("")
        return (num)
