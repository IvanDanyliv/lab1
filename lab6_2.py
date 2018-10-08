#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def ui_input() -> list:
    #Input of argument
    a = float(input("Available amount "))
    b = float(input("Interest rate "))
    c = float(input("Duration of the deposit "))
    return[a, b, c]

def ui_output(money: float):
    #Output of result
    print (money)

def calculate_area_triangle(deposit: list) -> float:
    #Calculate final amout of money deposit
    final_money = deposit[0]*(1+deposit[1]/100)**deposit[2]
    return final_money

ui_output(calculate_area_triangle(ui_input()))
