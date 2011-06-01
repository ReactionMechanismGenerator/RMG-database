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

from rmgpy.data.rmg import RMGDatabase
from rmgpy.kinetics import KineticsData
from rmgpy.data.kinetics import KineticsDatabase, KineticsGroups

################################################################################

def setHistory(database, user):
    """
    For each entry in each component of the database, add a note to the history
    indicating the import event and its time.
    """
    # Add history item to each entry in each database
    event = [time.asctime(),user,'action','{0} imported this entry from the old RMG database.'.format(user)]
    
    for depository in database.thermo.depository.values():
        for label, entry in depository.entries.iteritems():
            entry.history.append(event)
    for library in database.thermo.libraries.values():
        for label, entry in library.entries.iteritems():
            entry.history.append(event)
    for groups in database.thermo.groups.values():
        for label, entry in groups.entries.iteritems():
            entry.history.append(event)
    
    for depository in database.kinetics.depository.values():
        for label, entry in depository.entries.iteritems():
            entry.history.append(event)
    for library in database.kinetics.libraries.values():
        for label, entry in library.entries.iteritems():
            entry.history.append(event)
    for groups in database.kinetics.groups.values():
        for label, entry in groups.entries.iteritems():
            entry.history.append(event)
    
    groups = database.states.groups
    for label, entry in groups.entries.iteritems():
        entry.history.append(event)
    
    for label, entry in database.forbiddenStructures.entries.iteritems():
        entry.history.append(event)
    
################################################################################

if __name__ == '__main__':

    # Set the import and export paths
    oldPath = 'output/RMG_database'
    newPath = 'input'
    
    print 'Loading old RMG-Java database...'
    database = RMGDatabase()
    database.loadOld(oldPath)
    
    print 'Setting history of all entries in database...'
    setHistory(database, user='jwallen')
      
    print 'Saving the new RMG-Py database...'
    database.save(newPath)
