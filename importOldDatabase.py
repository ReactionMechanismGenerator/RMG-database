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

from rmgpy.kinetics import KineticsData
from rmgpy.data.kinetics import KineticsDatabase, KineticsGroups
from rmgpy.data.rmg import RMGDatabase

################################################################################


if __name__ == '__main__':
    

    # Set the import and export paths
    oldPath = 'output/RMG_database'
    newPath = 'input'
    
    print 'Loading old RMG-Java database...'
    database = RMGDatabase()
    database.loadOld(oldPath)
      
    print 'Saving the new RMG-Py database...'
    database.save(newPath)
    print "Done!"
