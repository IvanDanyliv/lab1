#!/usr/bin/env python3

import math

def revers_all_by_for(strings: list) -> list:
    reversed_strings = []
    for string in strings:
        string = string[::-1]
        reversed_strings.append(string)
    return reversed_strings

def revers_all_by_comprehension(strings: list) -> list:
    reversed_strings = []
    reversed_strings += [string[::-1] for string in strings]
    return reversed_strings

def revers_all_by_map(strings: list) -> list:
    return list(map(lambda x: x[::-1], strings))

def power_by_shift() -> int:
    return 2 << 99

def power_by_double_star() -> int:
    return 2 ** 100

def power_by_pow() -> int:
    return pow(2, 100)

def power_by_math_pow() -> int:
    return math.pow(2, 100)
