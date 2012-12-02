#!/usr/bin/env python

from sys import argv
from os.path import exists

script, outfile, infile = argv

output = open(outfile)
outdata = output.read()

print "The output file %r is %r bytes length." % (outfile, len(outdata))
print "Does the input file exists? %r" % exists(infile)

print "Ready, hit RETURN to continue, CTRL_C to abort."
raw_input("> ")

input = open(infile, 'w')
input.write(outdata)

input.close()
output.close()
