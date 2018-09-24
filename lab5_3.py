#!/usr/bin/env python3
#!-*- coding: utf-8 -*-

import random

print('Камінь, ножниці, папір')
s = ('камінь', 'ножниці', 'папір')
knb = int(input('камінь(1), ножниці(2) або папір(3)? ')) - 1
comp = random.randint(0, 2)
print("Ви вибрали {}, комп'ютер вибрав {}.\n{}".format(
    s[knb], s[comp],
    ('Ви програли!', 'Нічия!', 'Ви виграли!')[((comp+1) % 3) - knb]))
