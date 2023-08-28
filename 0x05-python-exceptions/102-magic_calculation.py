#!/usr/bin/python3

def magic_calculation(a, b):
    output = 0

    for j in range(1, 4):
        try:
            if j > a:
                raise Exception('Too far')
            output += (a ** b) / i
        except ValueError as e:
            output += a + b
            break

    return (output)
