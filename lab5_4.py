#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import math

a = float(input('Введіть перший член квадратного рівняння:'))
b = float(input('Введіть другий член квадратного рівняння:'))
c = float(input('Введіть третій член квадратного рівняння:'))

if a == 0 and b != 0:
    x1 = None
    x2 = -(c / b)
elif a == 0 and b == 0:
    x1 = x2 = None
else:
    discriminant = b ** 2 - 4 * a * c
    x1 = (-b + discriminant ** 0.5)/2 * a
    x2 = (-b - discriminant ** 0.5)/2 * a
print("x1=" + str(x1) + "\t" + "x2=" + str(x2))
