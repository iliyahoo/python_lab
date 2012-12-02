#!/usr/bin/env python

def by_three(n):
    if n % 3 == 0:
        return cube(n)
    else:
        return False

def cube(n):
    return  n ** 3
		
by_three(11)
by_three(12)
by_three(13)
by_three(9)

