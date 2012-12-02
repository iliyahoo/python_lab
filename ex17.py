#!/usr/bin/env python

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

indata = open(from_file).read()

print "The input file is %d bytes long." % len(indata)
print "Does the output file exist. %r" % exists(to_file)
print "Hit return to continue, CTRL-C to abort."
raw_input()

open(to_file, 'w').write(indata)

print "All done."

#indata.close()
#input.close()
