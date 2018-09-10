#!/usr/bin/env python3

h = input('Your height in m: ')
w = input('Your weight in kg: ')

s = float(w) / float(h) ** 2

print('Your Body Mass Index: ' + str(s))
