#!/usr/bin/python3

def roman_to_int(roman_string):
    """converts a Roman numeral to an integer."""
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_fig = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    val_list = [1, 5, 10, 50, 100, 500, 1000]

    roman_dictionary = dict(zip(roman_fig, val_list))

    total = 0
    prev_value = 0

    for char in roman_string[::-1]:
        value = roman_dictionary[char]

        if value >= prev_value:
            total += value
        else:
            total -= value

        prev_value = value

    return total
