#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = int(input('Перша сторона трникутника: '))
b = int(input('Друга сторона трникутника: '))
c = int(input('Третя сторона трникутника: '))

if a <= 0 or b <= 0 or c <= 0:
    print('Трикутник не існує')
else:
    if a + b > c and a + c > b and b + c > a:
        print('Трикутник існує')
    else:
        print('Трикутник не існує')
 
