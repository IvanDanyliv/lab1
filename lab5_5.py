#!/usr/bin/env python3
#!-*- coding: utf-8 -*-

num = int(input('Введіть число:'))

if num > 1:
    a = 2
    while a != num:
        if (num % a) == 0:
            print('Число не просте')
            break
        a += 1
    else:
        print('Число просте')
else:
    print('Число не просте')
