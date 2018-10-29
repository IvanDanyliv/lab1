#!/usr/bin/env python3

import re

def camel_case(sentence: str) -> str:
    words = sentence.split('_')
    camel_name = words[0] + ''.join(list(map(str.capitalize, words[1:])))
    return camel_name

def snake_case(sentence: str) -> str:
    words = re.sub(r'([A-Z])', r" \1", sentence).split()
    snake_name = '_'.join(list(map(str.lower, words)))
    return snake_name

print(camel_case(input("Input your variable in snake case: ")))
print(snake_case(input("Input your variable in camel case: ")))
