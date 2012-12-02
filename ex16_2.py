#!/usr/bin/env python
from sys import argv
script, filename = argv
target = open(filename, 'w')

Str = str("bla\nbale\nbrt\n")
print Str

#target.truncate()
target.write('iliya\nmake\nit'.upper())
target.close()

target = open(filename, 'r')
print target.read()

