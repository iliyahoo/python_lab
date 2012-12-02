#!/usr/bin/env python

from sys import argv

arg1, arg2, arg3 = argv

def print_two (*args):
    print "arg1=%r, arg2=%r" % args
print_two(arg2, arg3)
