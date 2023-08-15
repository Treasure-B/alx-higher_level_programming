#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """ If tuple_a or tuple_b has less than 2 integers, append"""
    if len(tuple_a) < 2:
        tuple_a += (0,)

    if len(tuple_b) < 2:
        tuple_b += (0,)

    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]

    total_1 = tuple_a[0] + tuple_b[0]
    total_2 = tuple_a[1] + tuple_b[1]

    return (total_1, total_2)
