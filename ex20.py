#!/usr/bin/env python

from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print '=' * 40

print "First let's print the whole file:\n"
print_all(current_file)

print '=' * 40

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"

current_line = 1

for i in range(1, 4):
    print_line(current_line, current_file)
    current_line += 1
