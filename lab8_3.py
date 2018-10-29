#!/usr/bin/env python3

import functools
import random

def gen_list(size: int) -> list:
    return [random.randint(0, 10) for _ in range(size)]

def average(source: list) -> float:
    return functools.reduce((lambda x, y: x + y), source) / len(source)

def median(source: list) -> float:
    number = len(source)
    if len(source) % 2 == 1: return sorted(source)[number//2]
    else: return sum(sorted(source)[number//2-1:number//2+1])/2

lst = gen_list(10)
print(lst)
print(average(lst))
print(median(lst))
