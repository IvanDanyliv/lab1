#!/usr/bin/env python3

def is_valid_email(email: str) -> bool:
    splited = email.split('@')[1].split('.')
    return len(splited[-1]) > 1 and email.count('@') < 2 and len(splited) > 1

print(is_valid_email(input("Input your email: ")))
