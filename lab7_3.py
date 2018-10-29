#!/usr/bin/env python3

sentence = input("Input your string: ")
open = tuple('({[')
close = tuple(')}]')
mapping = dict(zip(open, close))
queue = []

for letter in sentence:
    if letter in open:
        queue.append(mapping[letter])
    elif letter in close:
        if not queue or letter != queue.pop():
            print(False)
print(not queue)
