#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def encryption(expression: str) -> str:
    lst = list(map(lambda x: chr(ord(x) + 1), expression))
    return ''.join(lst)

print(encryption(input("Input your string: ")))
