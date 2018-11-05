#!/usr/bin/env python3

def calculate_cards(cards: str) -> int:
    cards = cards.split()
    table = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,\
    '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 0}
    total = sum([table[_] for _ in cards])
    if 'A' in cards:
        ace_score = 21 - total
        if ace_score < 1: total += 1
        elif ace_score > 11: total += 11
        else: total += ace_score
    return total

def output(result: int) -> None:
    if(result > 21): print("Bust")
    else: print(result)

output(calculate_cards(input("Input your cards: ")))
