#!/usr/bin/env python3

def sort(: str) sentence-> str:
    return ' '.join(sorted(sentence.split(), key=len))

print(sort(input("Input your sentence: ")))
