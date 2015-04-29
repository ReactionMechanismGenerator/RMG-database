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
        p=subprocess.Popen('git config --get user.name'.split(),
                stdout=subprocess.PIPE)
        name = p.stdout.read()
    except OSError:
        pass
    if name:
        name = name.strip()
    else:
        raise Exception("Couldn't find user.name from git. Please add user info to git or fill user info manually.")
    
    try:
        p=subprocess.Popen('git config --get user.email'.split(),
                stdout=subprocess.PIPE)
        email = p.stdout.read()
    except OSError:
        pass
    if email:
        email = email.strip()
    else:
        raise Exception("Couldn't find user.email from git. Please add email to git or fill email info manually.")
    
    return '{0} <{1}>'.format(name,email)


from cStringIO import StringIO
def compare(entry1,entry2,saver):
    """Compare entries entry1 and entry2 according to the saveEntry function saver"""
    history1, history2 = entry1.history, entry2.history
    entry1.history = []
    entry2.history = []
    s1 = StringIO()
    saver(s1,entry1)
    s2 = StringIO()
    saver(s2,entry2)
    equal = False
    if s1.getvalue() == s2.getvalue():
        equal = True
    s1.close()
    s2.close()
    entry1.history, entry2.history = history1, history2
    return equal
    
def setHistory(database, current_database, user):
    """
    For each entry in each component of the database, add a note to the history
    indicating the import event and its time, if it's different than what's in the current_database
    """
    # Add history item to each entry in each database
    event = [time.asctime(),user,'action','{0} updated this entry by importing the old RMG database.'.format(user)]
    event_new = [time.asctime(),user,'action','{0} added this entry by importing the old RMG database.'.format(user)]
    
    for depository in database.thermo.depository.values():
        for label, entry in depository.entries.iteritems():
            raise NotImplementedError("Wasn't expecting depositories in the old database, so haven't implemented change detection")
            entry.history.append(event)
    
    for key, library in database.thermo.libraries.iteritems():
        try:
            old_library = current_database.thermo.libraries[key].entries
        except KeyError:
            old_library = {}
        for label, entry in library.entries.iteritems():
            try:
                old_entry = old_library[label]
            except KeyError:
                entry.history.append(event_new)
                continue # next in for loop
            entry.history.extend(old_entry.history)
            if compare(old_entry, entry, library.saveEntry):
                print key, label, "has not changed."
            else:
                entry.history.append(event)
                
    for key, groups in database.thermo.groups.iteritems():
        try:
            old_groups = current_database.thermo.groups[key].entries
        except KeyError:
            old_groups = {}
        for label, entry in groups.entries.iteritems():
            try:
                old_entry = old_groups[label]
            except KeyError:
                entry.history.append(event_new)
                continue # next in for loop
            entry.history.extend(old_entry.history)
            if compare(old_entry, entry, groups.saveEntry):
                print key, label, "has not changed."
            else:
                entry.history.append(event)
    
    for key, family in database.kinetics.families.iteritems():
        try:
            old_groups = current_database.kinetics.families[key].groups.entries
        except KeyError:
            old_groups = {}
        for label, entry in family.groups.entries.iteritems():
            try:
                old_entry = old_groups[label]
            except KeyError:
                entry.history.append(event_new)
                continue # next in for loop
            entry.history.extend(old_entry.history)
            if compare(old_entry, entry, family.rules.saveEntry): # family.groups has no .saveEntry?
                print key, label, "has not changed."
            else:
                entry.history.append(event)
        try:
            old_rules = current_database.kinetics.families[key].rules.entries
        except KeyError:
            old_rules = {}
        for label, entry in family.rules.entries.iteritems():
            try:
                old_entry = old_rules[label]
            except KeyError:
                for item in entry:
                    item.history.append(event_new)
                continue # next in for loop
            for item in entry:
                for old_item in old_entry:
                    if old_item.index == item.index:
                        print "Found what's meant to be the same thing"
                        item.history.extend(old_item.history)
                        if compare(old_item, item, family.rules.saveEntry):
                            print key, label, "has not changed."
                        else:
                            item.history.append(event)
                        break
                else:
                    "Couldn't find corresponding item with same index."
                    item.history.append(event_new)
                    
        for depository in family.depositories.values():
            for label, entry in depository.entries.iteritems():
                raise NotImplementedError("Wasn't expecting depositories in the old database, so haven't implemented change detection")
                entry.history.append(event)
        
    for key, library in database.kinetics.libraries.iteritems():
        try:
            old_library = current_database.kinetics.libraries[key].entries
        except KeyError:
            old_library = {}
        for label, entry in library.entries.iteritems():
            #print "What is the label?",label
            # is this useful for looking things up?
            try:
                old_entry = old_library[label]
            except KeyError:
                entry.history.append(event_new)
                continue # next in for loop
            entry.history.extend(old_entry.history)
            if compare(old_entry, entry, library.saveEntry):
                print key, label, "has not changed."
            else:
                entry.history.append(event)
    
    
    groups = database.statmech.groups
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
      
    print 'Saving the new RMG-Py database...'
    database.save(newPath)
    print "Done!"
