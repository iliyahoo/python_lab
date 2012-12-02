#!/usr/bin/env python

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s." % (from_file, to_file)

#input = open(from_file)
indata = open(from_file).read()

print "The %s is %s bytes long." % (from_file, len(indata))
print "Does the %s file exist? %s" % (to_file, exists(to_file)) 
raw_input()

open(to_file, 'w').write(indata)

print "All done."

open(from_file).close()
open(to_file).close()


