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

def getUsername():
    """
    Figure out what the current username is in the form "Richard West <rwest@mit.edu>"
    
    It should be in the format "Richard West <rwest@mit.edu>". We do this by
    interrogating git, if possible
    """
    name = ''
    email = ''
    try:
        login = os.getlogin()
    except OSError:
        try:
            import pwd
            login = pwd.getpwuid(os.geteuid()).pw_name
        except:
            login = "unknown"
    try:
        p=subprocess.Popen('git config --get user.name'.split(),
                stdout=subprocess.PIPE)
        name = p.stdout.read()
    except OSError:
        pass
    if name:
        name = name.strip()
    else:
        print "Couldn't find user.name from git."
        name = login

    try:
        p=subprocess.Popen('git config --get user.email'.split(),
                stdout=subprocess.PIPE)
        email = p.stdout.read()
    except OSError:
        pass
    if email:
        email = email.strip()
    else:
        print "Couldn't find user.email from git."
        email = login + "@" + os.uname()[1]
    
    return '{0} <{1}>'.format(name,email)

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
    
    for family in database.kinetics.families.values():
        for label, entry in family.groups.entries.iteritems():
            entry.history.append(event)
        for label, entry in family.rules.entries.iteritems():
            for item in entry:
                item.history.append(event)
        for depository in family.depositories.values():
            for label, entry in depository.entries.iteritems():
                entry.history.append(event)
    for library in database.kinetics.libraries.values():
        for label, entry in library.entries.iteritems():
            entry.history.append(event)
    
    groups = database.statmech.groups
    for label, entry in groups.entries.iteritems():
        entry.history.append(event)
    
    for label, entry in database.forbiddenStructures.entries.iteritems():
        entry.history.append(event)
    
################################################################################

if __name__ == '__main__':
    
    #figure out the username
    user = getUsername()

    # Set the import and export paths
    oldPath = 'output/RMG_database'
    newPath = 'input'
    
    print 'Loading old RMG-Java database...'
    database = RMGDatabase()
    database.loadOld(oldPath)
    
    print 'Setting history of all entries in database...'
    setHistory(database, user=user)
      
    print 'Saving the new RMG-Py database...'
    database.save(newPath)
