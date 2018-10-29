#!/usr/bin/env python3

def frame(sentence: str) -> None:
    print('*' * len(sentence) + "****")
    print("*", sentence, "*")
    print('*' * len(sentence) + "****")

frame(input("Input your string: "))
