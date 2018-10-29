#!/usr/bin/env python3

def is_can_create(string: str, checking_string: str) -> bool:
    return not[0 for _ in string if string.count(_) > checking_string.count(_)]

print(is_can_create(input("Input string: "), input("Input checking string: ")))
