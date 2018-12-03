#!/usr/bin/env python3

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, point) -> float:
        return ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5

class Triangle:
    def __init__(self, a_point, b_point, c_point):
        self.a_point = a_point
        self.b_point = b_point
        self.c_point = c_point
        self.a_side = self.a_point.distance_to(self.b_point)
        self.b_side = self.b_point.distance_to(self.c_point)
        self.c_side = self.c_point.distance_to(self.a_point)

    def is_exist(self) -> bool:
        hypotenuse = max(self.a_side, self.b_side, self.c_side)
        catheti_sum = sum(self.a_side, self.b_side, self.c_side) - hypotenuse
        return catheti_sum > hypotenuse

    def get_perimeter(self) -> float:
        if not(self.is_exist): raise Exception("Triangle not exists")
        return self.a_side + self.b_side + self.c_side

    def get_square(self) -> float:
        if not(self.is_exist): raise Exception("Triangle not exists")
        p = self.get_perimeter() / 2
        return (p * (p - self.a_side) * (p - self.b_side) * (p - self.c_side)) ** 0.5

def input_data() -> Triangle:
    a_point = Point(float(input("Input xa: ")), float(input("Input ya: ")))
    b_point = Point(float(input("Input xb: ")), float(input("Input yb: ")))
    c_point = Point(float(input("Input xc: ")), float(input("Input yc: ")))
    return Triangle(a_point, b_point, c_point)

def output(triangle) -> None:
    try:
        print("Perimeter of triangle:", triangle.get_perimeter())
        print("Perimeter of square:", triangle.get_square())
    except:
        print("Triangle exists:", triangle.is_exist())

output(input_data())
