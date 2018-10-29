#!/usr/bin/env python3

def lucky_ticket(sentence: str) -> bool:
    number = int(len(sentence) / 2)
    first_half = list(map(int, sentence[0 : number]))
    second_half = list(map(int, sentence[-number :]))
    return sum(first_half) == sum(second_half)

print(lucky_ticket(input("Input your ticket number: ")))
