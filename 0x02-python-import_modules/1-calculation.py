#!/usr/bin/python3

if __name__ == "__main__":
    """imports functions from the file calculator_1.py"""
    from calculator_1 import add, subtraction, multiple, divide

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, subtraction(a, b)))
    print("{} * {} = {}".format(a, b, multiple(a, b)))
    print("{} / {} = {}".format(a, b, divide(a, b)))
