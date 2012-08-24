#!/usr/bin/env python
# encoding: utf-8

import os

from rmgpy import settings
from rmgpy.data.kinetics import KineticsDatabase, saveEntry


###############################################################################


def main():

    db = KineticsDatabase()
    db.loadFamilies(os.path.join(settings['database.directory'],
                                 'kinetics/families'))

    for family in db.families.values():
        for depository in family.depositories:
            if 'NIST' in depository.name:
                entries = depository.entries.values()
                entries.sort(key=lambda entry: sum([1 for r in entry.item.reactants for a in r.atoms if a.isNonHydrogen()]))
                print 'Rewriting {0}...'.format(depository.name),
                rewrite(entries, depository.name)
                print 'done.'


###############################################################################


def rewrite(entries, name):

    file = os.path.join(settings['database.directory'], 'kinetics/families',
                        '{0}.py'.format(name))

    open(file, 'w').write('#!/usr/bin/env python\n'
                          '# encoding: utf-8\n\n'
                          'name = "{0}"\n'.format(name) +
                          'shortDesc = u""\n'
                          'longDesc = u"""\n\n"""\n'
                          'recommended = False\n\n')

    index = 0
    for entry in entries:
        index += 1
        entry.index = index
        saveEntry(open(file, 'a'), entry)


###############################################################################


if __name__ == '__main__':

    main()
