#!/usr/bin/env python3
#!-*- coding: utf-8 -*-

import math

def ui_input() -> list:
    #Input of argument
    a = float(input("Available amount "))
    b = float(input("Required amount "))
    c = float(input("Interest rate "))
    return[a, b, c]

def ui_output(years: float):
    #Output of result
    print (years)

def calculate_area_triangle(year: list) -> float:
    #Calculate number of years
    years = math.log(year[1]/year[0], (1+year[2])/100) 
    return years

ui_output(calculate_area_triangle(ui_input()))
