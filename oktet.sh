#!/usr/bin/env python

oktet = [1]

for i in xrange(1, 8):
    x = len(oktet)
    y = oktet[x-1] * 2
    oktet.append(y)
print oktet
