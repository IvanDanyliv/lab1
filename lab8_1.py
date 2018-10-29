#!/usr/bin/env python3

import itertools

def war(number: int, step: int) -> int:
    lst = list(range(1, number + 1))
    count = 1
    while len(lst) > 1:
        first = lst.pop(0)
        if count != step:
            lst.append(first)
            count += 1
        else: count = 1
    return lst[0]

print(war(int(input("Input amount: ")), int(input("Input step: "))))
