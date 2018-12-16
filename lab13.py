#!/usr/bin/env python3

import abc
import random

class Employee(abc.ABC):
    @abc.abstractmethod
    def get_salary(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def get_physical_tax(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def get_military_tax(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def get_united_tax(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def get_social_tax(self) -> float:
        raise NotImplementedError

class HourlyEmployee(Employee):
    def __init__(self, name: str, rate: float):
        self.name = name
        self.rate = rate

    def get_name(self) -> str:
        return self.name

    def get_salary(self) -> float:
        return 20.8 * 8 * self.rate

    def get_physical_tax(self) -> float:
        return self.get_salary() * 0.18

    def get_military_tax(self) -> float:
        return self.get_salary() * 0.015

    def get_united_tax(self) -> float:
        return 0

    def get_social_tax(self) -> float:
        return 0

class MonthlyEmployee(Employee):
    def __init__(self, name: str, rate: float):
        self.name = name
        self.rate = rate

    def get_name(self) -> str:
        return self.name

    def get_salary(self) -> float:
        return self.rate

    def get_physical_tax(self) -> float:
        return self.get_salary() * 0.18

    def get_military_tax(self) -> float:
        return self.get_salary() * 0.015

    def get_united_tax(self) -> float:
        return 0

    def get_social_tax(self) -> float:
        return 0

class EntrepreneurEmployee(Employee):
    def __init__(self, name: str, rate: float):
        self.name = name
        self.rate = rate
        self.social_tax = 704

    def get_name(self) -> str:
        return self.name

    def get_salary(self) -> float:
        return 20.8 * 8 * 1.1 * self.rate

    def get_physical_tax(self) -> float:
        return 0

    def get_military_tax(self) -> float:
        return 0

    def get_united_tax(self) -> float:
        return self.get_salary() * 0.05

    def get_social_tax(self) -> float:
        return self.social_tax

class FreelancerEmployee(Employee):
    def __init__(self, name: str, rate: float, count_lines: int):
        self.name = name
        self.rate = rate
        self.count_lines = count_lines
        self.social_tax = 704

    def get_name(self) -> str:
        return self.name

    def get_salary(self) -> float:
        return self.rate * self.count_lines

    def get_physical_tax(self) -> float:
        return self.get_salary() * 0.18

    def get_military_tax(self) -> float:
        return self.get_salary() * 0.015

    def get_united_tax(self) -> float:
        return 0

    def get_social_tax(self) -> float:
        return self.social_tax

def input_data() -> list:
    names = ('Ivan', 'Mykola', 'Mykhailo', 'Taras', 'Yurii', 'Andrii', 'Serhii')
    employees = []
    for _ in range(random.randint(5, 10)):
        name = random.choice(names)
        employees.append(random.choice([
        HourlyEmployee(name, random.randint(100, 1000)),
        MonthlyEmployee(name, random.randint(10000, 30000)),
        EntrepreneurEmployee(name, random.randint(100, 1000)),
        FreelancerEmployee(name, 
        random.randint(30, 50), random.randint(100, 1000))]))
    return employees

def employee_sort(employees: list) -> list:
    return sorted(employees,
    key=lambda e: (e.get_salary(), e.get_name()), reverse=True)

def output(employees: list) -> None:
    for employee in employees:
        print("ID:", id(employee))
        print("Name:", employee.get_name())
        print("Salary:", employee.get_salary())
        full_tax = employee.get_military_tax() + employee.get_physical_tax() + \
                   employee.get_social_tax() + employee.get_united_tax()
        print("Full tax:", full_tax)
        print("\n")

output(employee_sort(input_data()))
