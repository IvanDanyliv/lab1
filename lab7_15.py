#!/usr/bin/env python3

import random
import string

def gen_password() -> str:
    password = ''
    chars = string.ascii_letters + string.digits + string.punctuation 
    while not set(string.digits).intersection(set(password)) or \
    not set(string.punctuation).intersection(set(password)):
        password = ''.join(random.choice(chars) for i in range(random.randint(8, 16)))
    return password

print(gen_password())
