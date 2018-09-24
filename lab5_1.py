#!/usr/bin/env python3

n = int(input("Введіть ціле додатнє число:"))

print(n != 0 and ((n & (n - 1)) == 0))
