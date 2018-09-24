#!/usr/bin/env python3
#!-*- coding: utf-8 -*-

height = float(input('Height:'))
width = float(input('Width:'))

a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))

if height > a and width > b:
 print('Success')

elif height > a and width > c:
 print('Success')

elif height > b and width > a:
 print('Success')

elif height > b and width > c:
 print('Success')

elif height > c and width > a:
 print('Success')

elif height > c and width > b:
 print('Success')

else:
 print('Failure')
