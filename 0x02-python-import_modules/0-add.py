#!/usr/bin/python3

if __name__ == "__main__":
  """Prints the sum of 1 and 2"""
# imports the function def add(a, b): from the file add_0.py

from add_0 import add

a = 1
b = 2
print("{} + {} = {}".format(a, b, add(a, b)))
