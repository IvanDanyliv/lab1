#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_palindrome(string):
    symbols = ['!',',','\'',' ','.']
    for symbol in symbols:
        if symbol in string:
            string = string.lower().replace(symbol,'')
    rev_string = string[::-1]

    return string == rev_string

my_str =  input('Input string: ')
print('YES' if is_palindrome(my_str) else 'NO')
