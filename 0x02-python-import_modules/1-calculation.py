#!/usr/bin/python3

if __name__ == "__main__":
    """imports functions from the file calculator_1.py"""
    from calculator_1 import add, su, mul, div

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, subt(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
