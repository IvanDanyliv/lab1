#!/usr/bin/env python3

sentence = input("Input your string : ")

sum_vowel = sentence.count('a') + sentence.count('o') + sentence.count('u') \
+ sentence.count('i') + sentence.count('e') + sentence.count("y")

print(sum_vowel)
