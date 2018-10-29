#!/usr/bin/env python3

def del_gap(sentence: str) -> str:
    return ' '.join(sentence.split())

print(del_gap(input("Input your sentence: ")))
