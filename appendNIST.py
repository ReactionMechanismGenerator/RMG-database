#!/usr/bin/env python
# encoding: utf-8

import os
import re
import subprocess
import sys
from datetime import datetime

from rmgpy import settings
from rmgpy.data.base import Entry
from rmgpy.data.kinetics import KineticsDatabase, saveEntry
from rmgpy.data.reference import Reference, Article, Book
from rmgpy.kinetics import Arrhenius
from rmgpy.quantity import Quantity

import urllib
import urllib2
import cookielib
from BeautifulSoup import BeautifulSoup
from ipdb import set_trace


###############################################################################


def main():

    if len(sys.argv) != 4:
        raise Exception('You must provide the reaction family, PrIMe index, '
                        'and squib as parameters.')

    family = sys.argv[1]
    try:
        primeIndex = int(sys.argv[2])
    except ValueError:
        raise Exception('You must provide an integer PrIMe index.')
    squib = sys.argv[3]

    primeDepo, nistDepo = loadDepositories(family)

    try:
        primeEntry = primeDepo.entries[primeIndex]
    except KeyError:
        raise Exception('No entry in {0}/PrIMe with index {1}.'.format(
                        family, primeIndex))

    nistEntries = nistDepo.entries.values()
    nistEntries.sort(key=lambda entry: entry.index)

    for entry in nistEntries:
        if entry.label == squib:
            print ('{0} already exists in '.format(squib) +
                   '{0}/NIST depository.\n'.format(family))
            remove = None
            while remove is None:
                ans = raw_input('Remove PrIMe entry? ')
                if ans.lower() == 'y':
                    remove = True
                elif ans.lower() == 'n':
                    remove = False
                else:
                    print 'please enter y or n\n'
            if remove:
                rewritePrIMe(primeDepo.entries.values(), family, primeIndex)
                gitCommit(family, primeIndex, entry.index, squib)
            else:
                print 'PrIMe to NIST conversion canceled.\n'
            return

    nistEntry = queryNIST(primeEntry, squib)

    if nistEntry is not None:
        nistEntry.index = nistEntries[-1].index + 1
        if match(nistEntry.data, primeEntry.data):
            appendToNIST(nistEntry, family)
            rewritePrIMe(primeDepo.entries.values(), family, primeIndex)
            gitCommit(family, primeIndex, nistEntry.index, squib)


###############################################################################


def loadDepositories(family):

    database = KineticsDatabase()
    database.loadFamilies(os.path.join(settings['database.directory'],
                                       'kinetics/families'),
                          families=[family])

    for depository in database.families[family].depositories:
        if depository.label == '{0}/PrIMe'.format(family):
            primeDepo = depository
            break
    else:
        raise Exception('Could\'t find PrIMe depository '
                        'in {0} family.'.format(family))

    for depository in database.families[family].depositories:
        if depository.label == '{0}/NIST'.format(family):
            nistDepo = depository
            break
    else:
        raise Exception('Couldn\'t find NIST depository '
                        'in {0} family.'.format(family))

    return primeDepo, nistDepo


###############################################################################


def queryNIST(entry, squib):

    cookiejar = cookielib.CookieJar()
    setNISTUnits(cookiejar)

    try:
        result = getKinetics(entry, squib, cookiejar)
        assert isinstance(result, Entry)
    except:
        print result
        return None

    return getReference(result, squib, cookiejar)


###############################################################################


def setNISTUnits(cookiejar):

    post = {
        'energyUnits': 'J',
        'evaluationTemperature': '300.0',
        'moleculeUnits': 'Mole',
        'pressureUnits': 'Pa',
        'referenceTemperature': '1.0',
        'temperatureUnits': 'K',
        'volumeUnits': 'cm',
    }

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    request = opener.open('http://kinetics.nist.gov/kinetics/'
                          'SetUnitsBean.jsp', data=urllib.urlencode(post))
    request.close()


###############################################################################


def getKinetics(entry, squib, cookiejar):

    url = ('http://kinetics.nist.gov/kinetics/'
           'Detail?id={0}:0'.format(squib.split(':')[0]))
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    request = opener.open(url)
    soup = BeautifulSoup(request.read())
    request.close()

    try:
        form = soup.findAll(name='form', attrs={'name': 'KineticsResults'})[0]
    except IndexError:
        return 'No results found for {0}.'.format(squib)

    for tr in form.findAll(name='tr'):
        tdlist = tr.findAll(name='td')
        if len(tdlist) == 17 and tr.findAll(name='input', value=squib):
            break
    else:
        return 'No results found for {0}.'.format(squib)

    try:
        if 'Reference reaction' in tr.findNext(name='tr').text:
            return 'Result is a reference reaction.'
    except AttributeError:
        pass

    Trange = tdlist[6].text
    A = tdlist[8].text
    n = tdlist[10].text
    Ea = tdlist[12].text
    order = tdlist[16].text

    if ';' in A:
        print 'Invalid pre-exponential.'
        set_trace()
    if ';' in Ea:
        print 'Invalid activation energy.'
        set_trace()
    if ';' in order:
        print 'Invalid reaction order.'
        set_trace()
    if int(order) != len(entry.item.reactants):
        print 'Order does not match number of reactants.'
        set_trace()

    if n == '&nbsp;':
        n = 0.0

    Tmin = None
    Tmax = None
    if '-' in Trange:
        Tmin, Tmax = Trange.split('-')
    elif ';' in Trange:
        pass
    else:
        Tmin = Trange
        Tmax = Trange

    url = ('http://kinetics.nist.gov/kinetics/'
           'Detail?id={0}'.format(squib))

    return Entry(item=entry.item,
                 label=squib,
                 data=Arrhenius(A=((float(A) / 1.0e6, "m^3/(mol*s)")
                                   if len(entry.item.reactants) == 2
                                   else (float(A), "s^-1")),
                                n=(float(n), ""),
                                Ea=(float(Ea) / 1.0e3, "kJ/mol"),
                                T0=(1.0, "K"),
                                Tmin=((float(Tmin), "K") if Tmin else None),
                                Tmax=((float(Tmax), "K") if Tmax else None),
                                ),
                 longDesc='PrIMe Reaction: '
                          '{0}\n'.format(entry.reference.url.split('/')[6]) +
                          'PrIMe Kinetics: '
                          '{0}\n'.format(entry.reference.url),
                 history=[(datetime.now().strftime("%a %b %d %H:%M:%S %Y"),
                           'Sean Troiano <stroiano7@gmail.com>',
                           'action',
                           'Imported from NIST database at {0}'.format(url)
                           )
                          ],
                 )


###############################################################################


def getReference(entry, squib, cookiejar):

    url = 'http://kinetics.nist.gov/kinetics/Detail?id={0}'.format(squib)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    request = opener.open(url)
    html = request.read()
    soup = BeautifulSoup(html)
    request.close()

    try:
        category = soup.table.findAll(text='Category:')[0].parent
        category = category.nextSibling[7:].lower()
    except IndexError:
        category = ''

    try:
        datatype = soup.table.findAll(text='Data type:')[0].parent
        datatype = datatype.nextSibling[13:]
    except IndexError:
        datatype = ''

    reftype = soup.table.findAll(text='Reference type:')[0].parent
    reftype = reftype.nextSibling[13:].lower()
    if reftype == 'technical report':
        reftype = 'journal article'
    if reftype == 'book':
        reftype = 'book chapter'
    try:
        assert reftype in ['journal article', 'book chapter']
    except AssertionError:
        raise Exception('Unexpected reference type '
                        '"{0}" from squib "{1}".'.format(reftype,
                                                         squib))

    if reftype in ['journal article', 'book chapter']:
        authors0 = soup.table.findAll(text='Author(s):')[0].parent
        authors0 = authors0.nextSibling[13:]
        authors = []
        for author0 in authors0.split(';'):
            authors.append(author0.strip())

    if reftype == 'journal article':
        title = soup.table.findAll(text='Title:')[0].parent.nextSibling[13:]
        gen = soup.table.findAll(text='Title:')[0].parent.nextSibling
        gen = gen.nextSiblingGenerator()
        output = []
        foundTitle = False
        while not foundTitle:
            item = gen.next()
            try:
                foundTitle = 'br' in item.name
            except AttributeError:
                foundTitle = False
            if foundTitle:
                break
            try:
                text = item.text
            except AttributeError:
                text = item
            output.append(text)
        title += ''.join(output)

        journal = soup.table.findAll(text='Journal:')[0].parent
        journal = journal.nextSibling[13:]
        try:
            volume = soup.table.findAll(text='Volume:')[0].parent
            volume = volume.nextSibling[13:]
        except IndexError:
            volume = ''
        pages = soup.table.findAll(text='Page(s):')[0].parent.nextSibling[13:]
        if not pages:
            if '/' in squib:
                pages = squib[11:]
                pages = pages.split(':')[0]
            else:
                pages = squib[7:]
                pages = pages.split(':')[0]
        year = soup.table.findAll(text='Year:')[0].parent.nextSibling[13:]
        entry.reference = Article(
            authors=authors,
            title=title,
            journal=journal,
            volume=volume,
            pages=re.sub(' - ', '-', pages),
            year=year,
        )

    elif reftype == 'book chapter':
        title = soup.table.findAll(text='Title:')[0].parent.nextSibling[13:]
        gen = soup.table.findAll(text='Title:')[0].parent.nextSibling
        gen = gen.nextSiblingGenerator()
        output = []
        foundTitle = False
        while not foundTitle:
            item = gen.next()
            try:
                foundTitle = 'br' in item.name
            except AttributeError:
                foundTitle = False
            if foundTitle:
                break
            try:
                text = item.text
            except AttributeError:
                text = item
            output.append(text)
        title += ''.join(output)

        publisher = soup.table.findAll(text='Publisher address:')[0].parent
        publisher = publisher.nextSibling[13:]
        year = soup.table.findAll(text='Year:')[0].parent.nextSibling[13:]
        entry.reference = Book(
            authors=authors,
            title=title,
            publisher=publisher,
            year=year,
        )

    for item in soup('sup'):
        if 'J/mole]/RT' in item.text:
            break
    else:
        set_trace()
    entry.data.Ea.value = -float(item.text.split(' ')[0])

    if not '[J/mole]/RT' in item.text and '[&plusmn;' in item.text:
        error = item.text.split('&plusmn;')[1]
        entry.data.Ea.uncertainty = float(error.split(' ')[0])
        entry.data.Ea.uncertaintyType = '+|-'

    for item in soup('sup'):
        if '(' in item.text and ')' and '&plusmn;' in item.text:
            try:
                error = item.text.split('&plusmn;')[1].split(')')[0]
                entry.data.n.uncertainty = float(error)
            except ValueError:
                set_trace()
            entry.data.n.uncertaintyType = '+|-'

    entry.data.A.uncertainty = False
    entry.data.A.uncertaintyType = ''
    try:
        start = soup.table.findAll(text='Rate expression:')[0].parent
    except IndexError:
        start = None

    if start:
        item = start
        text = ''
        while not '[' in text:
            item = item.nextSibling
            try:
                text = item.text
            except AttributeError:
                text = item
        if '&plusmn;' in text:
            text = text.split('&plusmn;')[1].split(' ')[0]
            entry.data.A.uncertaintyType = '+|-'
            if text.isdigit():
                entry.data.A.uncertainty = float(text)
            elif 'x' in text:
                entry.data.A.uncertainty = float(text.split('x')[0] + 'e' +
                                                 item.nextSibling.text)
            if len(entry.item.reactants) == 2:
                entry.data.A.uncertainty /= 1.0e6

    try:
        miscellaneous = soup.table.findAll(text='Rate expression:')[0].parent
    except IndexError:
        set_trace()

    gen = miscellaneous.nextSiblingGenerator()
    output = []
    item = gen.next()
    foundMisc = False
    while not foundMisc:
        item = gen.next()
        try:
            foundMisc = 'br' in item.name
        except AttributeError:
            foundMisc = False
    while item:
        try:
            text = item.text
        except AttributeError:
            text = item
        output.append(text)
        item = gen.next()

    longDesc = ''.join(output)
    longDesc = longDesc.replace('&nbsp;&nbsp;\n', ' ')
    longDesc = longDesc.replace('&nbsp;', ' ')
    longDesc = longDesc.replace('Category:  ', 'Category: ')
    longDesc = longDesc.replace('Estimated:  ', 'Estimated: ')

    for line in longDesc.splitlines():
        if 'Uncertainty:' in line and entry.data.A.uncertainty == 0.0:
            entry.data.A.uncertainty = float(line.split(' ')[1])
            entry.data.A.uncertaintyType = '*|/'

    entry.reference.url = url
    entry.referenceType = category
    entry.shortDesc = datatype.replace('Estimated:  ', 'Estimated: ')
    entry.longDesc += longDesc.strip().encode('utf-8')

    if entry.data.A.uncertaintyType is '+|-':
        if abs(entry.data.A.uncertainty) > abs(entry.data.A.value):
            u = entry.data.A.uncertainty
            entry.longDesc += ('\nNote: Invalid A value uncertainty '
                               '({0}) found and ignored'.format(u))
            entry.data.A.uncertainty = 0.0
    if entry.data.n.uncertaintyType is '+|-':
        if abs(entry.data.n.uncertainty) > abs(entry.data.n.value):
            u = entry.data.n.uncertainty
            entry.longDesc += ('\nNote: Invalid n value uncertainty '
                               '({0}) found and ignored'.format(u))
            entry.data.n.uncertainty = 0.0
    if entry.data.Ea.uncertaintyType is '+|-':
        if abs(entry.data.Ea.uncertainty) > abs(entry.data.Ea.value):
            u = entry.data.Ea.uncertainty
            entry.longDesc += ('\nNote: Invalid Ea value uncertainty '
                               '({0}) found and ignored'.format(u))
            entry.data.Ea.uncertainty = 0.0

    try:
        Prange = soup.table.findAll(text='Pressure:')[0].parent
        Prange = Prange.nextSibling[12:]
    except IndexError:
        Prange = ''

    Pmin = None
    Pmax = None
    if Prange:
        if ' - ' in Prange:
            Pmin = Prange.split(' ')[0]
            Pmax = Prange.split(' ')[2]
        else:
            Pmin = Prange.split(' ')[0]
            Pmax = Prange.split(' ')[0]
            if Pmax < 10:
                set_trace()

    if Pmin:
        entry.data.Pmin = Quantity(float(Pmin), "Pa")
    if Pmax:
        entry.data.Pmax = Quantity(float(Pmax), "Pa")

    html2 = html.replace('<P>', '<BR><BR>')
    html2 = html2.replace('<p>', '<BR><BR>')

    soup2 = BeautifulSoup(html2)

    if len(soup2.table.findAll(text='Comments:')) == 1:
        comm = soup2.table.findAll(text='Comments:')[0].parent
        gen = comm.nextSiblingGenerator()
        item = ''
        text = ''
        output = []
        foundEnd = False

        while not foundEnd:
            try:
                item = gen.next()
            except:
                output.pop()
                output.pop()
                output.pop()
                break
            try:
                foundEnd = 'hr' in item.name
            except AttributeError:
                pass
            if not foundEnd:
                try:
                    if 'br' in item.name:
                        text = '\n'
                    else:
                        text = item.text.strip()
                except AttributeError:
                    try:
                        text = item.strip()
                    except:
                        text = item
                output.append(text)

        comments = ('Comments:' +
                    ''.join(output[:-4]).replace('&nbsp;&nbsp;\n', ' '))

        newLongDesc = ''
        for line in entry.longDesc.splitlines():
            if 'Comments: ' not in line:
                newLongDesc += line + '\n'
            else:
                newLongDesc += comments + '\n'

        entry.longDesc = newLongDesc.replace('  ', ' ').strip()
        entry.longDesc = entry.longDesc.replace('Comments: ', '\n')
    elif len(soup2.table.findAll(text='Comments:')) > 1:
        set_trace()
    else:
        pass

    return entry


###############################################################################


def match(nist, prime):

    if not nist.A.equals(prime.A):
        print ('\nMismatch in A: PrIMe - {0}\n'.format(prime.A) +
               '                NIST - {0}'.format(nist.A))
    if not nist.n.equals(prime.n):
        print ('\nMismatch in n: PrIMe - {0}\n'.format(prime.n) +
               '                NIST - {0}'.format(nist.n))
    if not nist.Ea.equals(prime.Ea):
        print ('\nMismatch in Ea: PrIMe - {0}\n'.format(prime.Ea) +
               '                 NIST - {0}'.format(nist.Ea))

    while True:
        ans = raw_input('\nContinue? ')
        if ans.lower() == 'y':
            return True
        elif ans.lower() == 'n':
            print 'PrIMe to NIST conversion canceled.\n'
            return False
        else:
            print 'please enter y or n'


###############################################################################


def appendToNIST(entry, family):

    file = os.path.join(settings['database.directory'], 'kinetics/families',
                        family, 'NIST.py')

    saveEntry(open(file, 'a'), entry)


###############################################################################


def rewritePrIMe(entries, family, index):

    file = os.path.join(settings['database.directory'], 'kinetics/families',
                        family, 'PrIMe.py')

    open(file, 'w').write('#!/usr/bin/env python\n'
                          '# encoding: utf-8\n\n'
                          'name = "{0}/PrIMe"\n'.format(family) +
                          'shortDesc = u""\n'
                          'longDesc = u"""\n\n"""\n'
                          'recommended = False\n\n')

    entries.sort(key=lambda entry: entry.index)
    for entry in entries:
        if entry.index != index:
            saveEntry(open(file, 'a'), entry)


###############################################################################


def gitCommit(family, primeIndex, nistIndex, squib):

    diff = subprocess.check_output(['git', 'diff'])
    if not diff:
        return

    print ('\n========================================'
           '========================================\n'
           '+                                  '
           ' GIT DIFF '
           '                                  +\n'
           '========================================'
           '========================================\n\n' + diff)

    cancel = None
    while cancel is None:
        ans = raw_input('Generate Git Commit? ')
        if ans.lower() == 'y':
            cancel = False
        elif ans.lower() == 'n':
            dir = os.path.join(settings['database.directory'],
                               'kinetics/families/{0}'.format(family))
            subprocess.Popen(['git', 'checkout', '--',
                              'PrIMe.py', 'NIST.py'],
                             cwd=dir)
            print 'PrIMe to NIST conversion canceled.'
            cancel = True
        else:
            print 'please enter y or n\n'
    if cancel:
        return

    print ('========================================'
           '========================================\n'
           '+                                 '
           ' GIT COMMIT '
           '                                 +\n'
           '========================================'
           '========================================\n')

    name = None
    try:
        name = subprocess.check_output(['git', 'config', '--get',
                                        'user.name']).strip()
        assert name
    except:
        name = raw_input('Name: ')

    email = None
    try:
        email = subprocess.check_output(['git', 'config', '--get',
                                         'user.email']).strip()
        assert email
    except:
        email = raw_input('Email Address: ')

    author = '{0} <{1}>'.format(name, email)

    path = os.path.join('kinetics/families', family)
    prime = os.path.join(path, 'PrIMe.py')
    nist = os.path.join(path, 'NIST.py')

    message = ('NIST Conversion: '
               '{0}/PrIMe/{1}\n\n'.format(family, primeIndex) +
               'New Entry: NIST/{0} ({1})'.format(nistIndex, squib))

    result = subprocess.check_output(['git', 'commit',
                                      '-m', message,
                                      '--author', author,
                                      prime, nist,
                                      ],
                                     cwd=settings['database.directory'])

    repo = subprocess.check_output(['git', 'config', '--get',
                                    'remote.origin.url'])
    repo = repo.split(':')[1].split('.git')[0]

    branch = subprocess.check_output(['git', 'branch'])
    branch = branch.split('* ')[1].split('\n')[0]

    commit = subprocess.check_output(['git', 'rev-parse', branch]).strip()

    time = subprocess.check_output(['date']).strip()

    print ' Branch: {0}/{1}'.format(repo, branch)
    print ' Commit: {0}'.format(commit)
    print ' Author: {0}'.format(author)
    print '   Date: {0}'.format(time)
    print '   Diff: {0}'.format(result.splitlines()[1].strip())
    print 'Message: {0}'.format(message.splitlines()[0])
    print '         {0}'.format(message.splitlines()[2])


###############################################################################


if __name__ == '__main__':

    main()
