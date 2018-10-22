#!/usr/bin/env python3
# -*- coding: utf-8 -*-

string = input('Input string: ')
num = int(input('Input number: '))

first = string[0 : num]
second = string[num:]
shifted_string = second + first

print(shifted_string)
