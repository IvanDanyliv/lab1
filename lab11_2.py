#!/usr/bin/env python3

def get_random(seed: str) -> int:
    if len(seed) < 6: seed = '0' * (6 - len(seed)) + seed
    elif len(seed) > 6: raise ValueError('Not supported seed')
    else: pass

    while True:
        seed = str(seed)
        raw_number = list(str(int(seed[3:] + seed[0:3]) * int(seed)))
        while len(raw_number) > 7: raw_number.pop(0);raw_number.pop(-1)
        if len(raw_number) > 6: del raw_number[-1]
        seed = int(''.join(raw_number))
        yield seed

a = get_random(input("Input seed: "))
print(a.__next__())
print(a.__next__())
print(a.__next__())
