#!/usr/bin/python3
def pow(a, b):
    r = 1
    p = b
    if b < 0:
        p = -b
    for i in range(p):
        r = r * a
    if b < 0:
        r = 1 / r
    return r
