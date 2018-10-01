#!/usr/bin/env python3
#!-*- coding: utf-8 -*-

import math

def ui_input() -> list:
    #Input of argument
    a = float(input("Input first side of triangle"))
    b = float(input("Input second side of triangle"))
    c = float(input("Input third side of triangle"))
    return[a, b, c]

def ui_output(area: float):
    #Output of result
    print (area)

def calculate_area_triangle(sides_triangle: list) -> float:
    #Calculates the area of the triangle
    p = (sides_triangle[0]+sides_triangle[1]+sides_triangle[2])/2
    s = math.sqrt(p*(p-sides_triangle[0])+(p-sides_triangle[1])*(p-sides_triangle[2]))

    return s

ui_output(calculate_area_triangle(ui_input()))
