#!/usr/bin/env python3
#!-*- coding: utf-8 -*-

n = int(input("Введіть ціле додатнє число:"))

print(n != 0 and ((n & (n - 1)) == 0))
