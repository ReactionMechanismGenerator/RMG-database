#!/usr/bin/env python
# encoding: utf-8

import os

import rmgpy
from rmgpy.data.kinetics import KineticsDatabase

if __name__ == '__main__':

    print 'Loading kinetics families...'
    db = KineticsDatabase()
    db.loadFamilies(os.path.join(rmgpy.settings['database.directory'],
                                 'kinetics/families'))
    print '    ...done.'

    f = open('checkP.html', 'w')
    f.write('<html>\n'
            '<title>Low Pressure Check</title>\n'
            '<body>\n')

    finished = True

    for key in sorted(db.families.keys()):
        lowP = []
        for depository in db.families[key].depositories:
            if 'NIST' in depository.name:
                print '\nChecking {0}...'.format(key)
                for entry in depository.entries.values():
                    try:
                        if entry.data.Pmax.value < 10:
                            lowP.append({'index': entry.index,
                                         'url': entry.reference.url,
                                         'value': entry.data.Pmax.value})
                            print '    {0:3}  {1:25}  {2:.2e}'.format(
                                entry.index,
                                entry.reference.url.split('=')[1],
                                entry.data.Pmax.value)
                    except:
                        pass
                if lowP:
                    finished = False
                    f.write('\n<b>{0}</b>\n\t<br>\n\t<table>\n'.format(key))
                    for item in lowP:
                        f.write('\t\t<tr>\n'
                                '\t\t\t<td align="right" width="50px">'
                                '{0}</td>\n'.format(item['index']) +
                                '\t\t\t<td align="center" width="275px">'
                                '<a href="{0}">{1}</a></td>\n'.format(
                                    item['url'],
                                    item['url'].split('=')[1]) +
                                '\t\t\t<td width="50px">'
                                '{0:.2e}</td>\n\t\t</tr>'.format(
                                    item['value']))
                    f.write('\n\t</table>\n\t<br>\n')
                else:
                    print '    ...none found.'

    if finished:
        f.write('\n<b>No invalid pressure ranges found.</b>\n')
    f.write('\n</body>\n</html>')
    f.close()
