#!/usr/bin/env python
# encoding: utf-8

"""
This script imports an RMG-Java database from the output directory and saves
it in the input directory.
"""

import math
import os.path
import sys
import time
import subprocess
import os

from rmgpy.data.rmg import RMGDatabase
from rmgpy.kinetics import KineticsData
from rmgpy.data.kinetics import KineticsDatabase, KineticsGroups

from importOldDatabase import getUsername
user = getUsername()

################################################################################

import re
def fix_prime_urls(database):
    rxn_search = re.compile('^r\d+$')
    kin_search = re.compile('(rk\d+\.xml)$')
    for label, depository in database.kinetics.depository.iteritems():
        for entry in depository.entries.values():
            if rxn_search.match(entry.label):
                match = kin_search.search(entry.reference.url)
                if match:
                    rk = match.group()
                    url = "http://warehouse.primekinetics.org/depository/reactions/data/{0}/{1}".format(entry.label,rk)
                    entry.reference.url = url
                    entry.longDesc = "Imported from PrIMe database at {0}\n{1}".format(url,entry.longDesc.strip())
                    
                    entry.history[0] = ( entry.history[0][0],entry.history[0][1],entry.history[0][2],
                                    "Imported from PrIMe database at {0}".format(url) )
                else:
                    print "couldn't find prime id in {0}".format(entry.reference.url)
            else:
                print "{0} is not a prime label".format(entry.label)
            
################################################################################

if __name__ == '__main__':
    
    #figure out the username
    user = getUsername()

    print 'Loading RMG database...'
    from rmgpy.data.rmg import RMGDatabase
    database = RMGDatabase()
    database.load('input')
    
    fix_prime_urls(database)

    print 'Saving the RMG-Py database...'
    #database.save('input')
    database.kinetics.saveDepository(os.path.join('input', 'kinetics'))
