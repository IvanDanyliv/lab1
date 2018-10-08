#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

a = float(input("Введіть невід'ємне число: "))
b = float(input("Введіть додатнє число: "))

x=(math.sqrt(a*b))/((math.e**a)*b)+(a*math.e**((2*a)/b))

print(x)
