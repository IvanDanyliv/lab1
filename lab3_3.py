#!/usr/bin/env python3

height = input('Зріст у метрах: ')
weight = input('Вага у кілограмах: ')

BMI = float(weight) / float(height) ** 2

print('Індекс маси тіла: ' + str(BMI))
