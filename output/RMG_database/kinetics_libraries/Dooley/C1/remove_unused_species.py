#!/usr/bin/env python
# encoding: utf-8
"""
remove_unused_species.py

Created by Richard West on 2011-03-10.
Copyright (c) 2011 MIT. All rights reserved.
"""

import sys
import os
import re
import fileinput

species = set()
for line in fileinput.input(('reactions.txt','pdepreactions.txt')):
    if (line.find(' = ') == -1):
        continue
    if (line.strip().startswith('//')):
        continue
    line = line.replace("(+M)","")
    reactants, products = line.split(' = ')
    products, junk = products.split(None, 1)
    combined = "%s+%s"%(reactants,products)
    for s in combined.split('+'):
        species.add(s.strip())
    
print "These %d species listed in reactions.txt and pdepreactions.txt" % len(species)
for s in species:
    print s
    
print "Copying the species.txt file, removing redundant species"

outfile = file('species.new.txt','w')
infile = file('species.txt')
for line in infile:
    if (line.strip().startswith('//')):
        continue
    if (line.strip()==''):
        continue
    s = line.strip()
    try:
        if (s in species):
            while (line.strip()!=''):
                outfile.write(line.strip()+'\n')
                line = infile.next()
            outfile.write('\n')
        else:
            print "Skipping %s"%s
            while (line.strip()!=''):
                line = infile.next()
    except StopIteration:
        break
outfile.close()