#!/usr/bin/env python3

import sys

def steganoraph_encrypt(img_name: str, message: str) -> None:
    if sys.getsizeof(message) > 160: raise ValueError('Not support message')
    message = ''.join(message.split())

    (result, msg_bytes) = ([], [])
    pointer = 1000
    img = open(img_name, 'rb+')
    for word in message: msg_bytes += list(format(ord(word), 'b'))
    img.seek(pointer)
    img_bytes = list(img.read(7 * len(message)))
    result += [img_bytes[_] - int(msg_bytes[_]) for _ in range(0, len(img_bytes))]
    img.seek(pointer)
    for _ in result: img.write(chr(_).encode('ISO-8859-1'))
    img.flush()
    img.close()

steganoraph_encrypt(input("Input filename: "), input("Input your message: "))
