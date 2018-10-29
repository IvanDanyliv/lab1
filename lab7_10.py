#!/usr/bin/env python3

def smallest(sentence: str) -> str:
    return min(sentence.split())

print(smallest(input("Input your sentence: ")))
