#!/usr/bin/env python3

def sort(expression: str) -> str:
    return ' '.join(sorted(expression.split(), key=len))

print(sort(input("Input your expression: ")))
