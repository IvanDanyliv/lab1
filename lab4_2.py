#!/usr/bin/env python3
#!-*- coding: utf-8 -*-

import math

a = float(input("Введіть дійсне число: "))
b = float(input("Введіть дійсне число: "))
c = float(input("Введіть дійсне число: "))

f=1/(c*math.sqrt(2*math.pi))*math.exp(-((a-b)**2)/(2*c**2))

print(f)
