#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import decimal

def ui_input() -> list:
    #Input of argument
    a = decimal.Decimal(input("Available amount "))
    b = decimal.Decimal(input("Required amount "))
    c = decimal.Decimal(input("Interest rate "))
    return[a, b, c]

def ui_output(d: float):
    #Output of result
    print (d)

def deposit_duration_calculate(deposit: list) -> float:
    #Calculate duration of deposit
    duration = math.log(deposit[1]/deposit[0], (1+deposit[2]/100))
    return duration

ui_output(deposit_duration_calculate(ui_input()))
