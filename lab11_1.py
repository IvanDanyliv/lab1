#!/usr/bin/env python3

def parse(filename: str) -> int:
    f_name = open(filename, 'rt')
    for line in f_name:
        size = line.split()[9]
        yield int(size)

def calculate_bytes(bytes: list) -> int:
    b_size = 0
    for byte in bytes:
        b_size += byte
    print(b_size)

calculate_bytes(parse("2017_05_07_nginx.txt"))
