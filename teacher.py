#!/usr/bin/env python

Lloyd = {
    "name":"Lloyd",
    "homework": [90, 97, 75, 92],
    "quizzes": [88, 40, 94],
    "tests": [75, 90]
    }

Alice = {
    "name":"Alice",
    "homework": [100,92,98,100],
    "quizzes": [82,83,91],
    "tests": [89,97]
    }

Tyler = {
    "name":"Tyler",
    "homework": [0,87,75,22],
    "quizzes": [0,75,78],
    "tests": [100,100]
    }

students = (Lloyd, Alice, Tyler)

for nnm in Lloyd, Alice, Tyler:
	print nnm['name'], '#', 'name'
	print nnm['homework'], '#', 'homework'
	print nnm['quizzes'], '#', 'guizzes'
	print nnm['tests'], '#', 'tests' 
	print "\n"

def average(X):
	print "sum(X['tests']) / len(X['tests'])"
average(Lloyd)
