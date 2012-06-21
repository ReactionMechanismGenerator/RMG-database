#!/usr/bin/env python
# encoding: utf-8

import os
import re
import sys

from rmgpy.data.kinetics import KineticsDatabase
from rmgpy.data.rmg import RMGDatabase
from rmgpy.data.base import Entry
from rmgpy.data.reference import *
from rmgpy.kinetics import Arrhenius
from rmgpy.molecule import Molecule
from rmgpy.reaction import Reaction

import urllib
import urllib2
import cookielib
from BeautifulSoup import BeautifulSoup

################################################################################

def loadEntries(family):
    
    database = RMGDatabase()
    database.kinetics = KineticsDatabase()
    database.kinetics.loadFamilies('input/kinetics/families')
    database.loadForbiddenStructures('input/forbiddenStructures.py')
    
    for depository in database.kinetics.families[family].depositories:
        if depository.label == '{0}/PrIMe'.format(family):
            break
    else:
        raise Exception('Could not find PrIMe depository in {0} family.'.format(family))
    
    identifiedEntries = []
    unidentifiedEntries = []

    counter = 1
    
    print 'Found {0} entries in {1}.'.format(len(depository.entries), depository.label),
    for entry in depository.entries.values():
        speciesList = []
        for reactant in entry.item.reactants:
            speciesList.append(reactant)
        for product in entry.item.products:
            speciesList.append(product)
        
        found = 0
        notFound = 0
        
        print '\n   Getting CAS numbers for entry #{0}...'.format(counter),
        for species in speciesList:
            if not getCAS(species):
				notFound += 1
            else:
				found += 1
        
        print 'found {0} of {1} species.'.format(found, found + notFound),
        
        if notFound:
            unidentifiedEntries.append(entry)
        else:
            identifiedEntries.append(entry)
        
        counter += 1
    
    return identifiedEntries, unidentifiedEntries

################################################################################

def getCAS(species):
    
    inchi = species.toInChI()
    
    url = "http://webbook.nist.gov/cgi/inchi/{0}".format(urllib.quote(inchi))
    try:
        f = urllib2.urlopen(url, timeout=5)
    except urllib2.URLError, e:
        pass
    else:
        searcher = re.compile('<li><a href="/cgi/inchi\?GetInChI=C(\d+)')
        for line in f:
            m = searcher.match(line)
            if m:
                return m.group(1)
    
    url = "http://cactus.nci.nih.gov/chemical/structure/{0}/cas".format((inchi))
    try:
        f = urllib2.urlopen(url, timeout=5)
    except urllib2.URLError, e:
        pass
    else:
        searcher = re.compile('(\d+)-(\d+)-(\d+)')
        caslist = []
        for line in f:
            m = searcher.match(line)
            if m:
                caslist.append(int(m.group(0).replace('-', '')))
        if len(caslist) > 0:
            return str(min(caslist))
    
    return False

################################################################################

def savePrIMe(entries, family):
    
    filename = 'input/kinetics/families/{0}/PrIMe.py'.format(family)
    
    os.remove(filename)
    
    if entries:
        
        with open(filename, 'w') as f:
            
            f.write('#!/usr/bin/env python\n')
            f.write('# encoding: utf-8\n\n')
            f.write('name = "{0}/PrIMe"\n'.format(family))
            f.write('shortDesc = u""\n')
            f.write('longDesc = u"""\n\n')
            f.write('"""\n')
            f.write('recommended = False\n')
                
            for entry in entries:
                f.write('\nentry(\n')
                f.write('    index = {0},\n'.format(entry.index))
                f.write('    label = "{0}",\n'.format(entry.label))
                
                count = 1
                for reactant in entry.item.reactants:
                    f.write('    reactant{0} = \n"""\n{1}""",\n'.format(count, reactant.toAdjacencyList(removeH = True)))
                    count += 1
                
                count = 1
                for product in entry.item.products:
                    f.write('    product{0} = \n"""\n{1}""",\n'.format(count, product.toAdjacencyList(removeH = True)))
                    count += 1
                
                f.write('    degeneracy = {0},\n'.format(entry.item.degeneracy))
                f.write('    kinetics = Arrhenius(\n'.format(entry.data.toPrettyRepr()))
                f.write('        A = ({0},"{1}"),\n'.format(entry.data.A.value, entry.data.A.units))
                f.write('        n = ({0},""),\n'.format(entry.data.n.value))
                f.write('        Ea = ({0},"{1}"),\n'.format(entry.data.Ea.value, entry.data.Ea.units))
                f.write('        T0 = ({0},"{1}"),\n'.format(entry.data.T0.value, entry.data.T0.units))
                f.write('    ),\n')
                
                lines = entry.reference.toPrettyRepr().splitlines()
                f.write('    reference = {0}\n'.format(lines[0]))
                for line in lines[1:-1]:
                    f.write('    {0}\n'.format(line))
                f.write('    ),\n')
                
                f.write('    referenceType = "",\n')
                f.write('    shortDesc = u"""""",\n')
                f.write('    longDesc = \nu"""\n{0}\n""",\n'.format(entry.longDesc))
                f.write('    history = {0},\n'.format(entry.history))
                f.write(')\n')
            
            f.close()
                
    print '\n   ... saved {0} unidentified entries to {1}/PrIMe.'.format(len(entries), family)

################################################################################

def sortIdentified(entries0):
    
    entries = []
    
    print '\nSorting {0} identified entries...'.format(len(entries0)),
    for entry0 in entries0:
        for entry in entries:
            if entry.item.isIsomorphic(entry0.item):
                break
        else:
            entries.append(entry0)
    print 'found {0} unique reactions.'.format(len(entries)),
    
    entries.sort(key=lambda entry: sum([1 for r in entry.item.reactants for a in r.atoms if a.isNonHydrogen()]))
    
    return entries

################################################################################

def saveNIST(entries, family):
    
    if entries:
        
        filename = 'input/kinetics/families/{0}/NIST.py'.format(family)
        
        with open(filename, 'w') as f:
            
            f.write('#!/usr/bin/env python\n')
            f.write('# encoding: utf-8\n\n')
            f.write('name = "{0}/NIST"\n'.format(family))
            f.write('shortDesc = u""\n')
            f.write('longDesc = u"""\n\n')
            f.write('"""\n')
            f.write('recommended = False\n')
            
            index = 1
            
            for entry in entries:
                f.write('\nentry(\n')
                f.write('    index = {0},\n'.format(index))
                f.write('    label = "{0}",\n'.format(entry.label))
                
                count = 1
                for reactant in entry.item.reactants:
                    f.write('    reactant{0} = \n"""\n{1}""",\n'.format(count, reactant.toAdjacencyList(removeH = True)))
                    count += 1
                
                count = 1
                for product in entry.item.products:
                    f.write('    product{0} = \n"""\n{1}""",\n'.format(count, product.toAdjacencyList(removeH = True)))
                    count += 1
                
                f.write('    degeneracy = {0},\n'.format(entry.item.degeneracy))
                f.write('    kinetics = Arrhenius(\n'.format(entry.data.toPrettyRepr()))
                f.write('        A = ({0},"{1}"),\n'.format(entry.data.A.value, entry.data.A.units))
                f.write('        n = ({0},""),\n'.format(entry.data.n.value))
                f.write('        Ea = ({0},"{1}"),\n'.format(entry.data.Ea.value, entry.data.Ea.units))
                f.write('        T0 = ({0},"{1}"),\n'.format(entry.data.T0.value, entry.data.T0.units))
                f.write('        Tmin = ({0},"{1}"),\n'.format(entry.data.Tmin.value, entry.data.Tmin.units))
                f.write('        Tmax = ({0},"{1}"),\n'.format(entry.data.Tmax.value, entry.data.Tmax.units))
                if entry.data.Pmax.value > 0:
                    f.write('        Pmin = ({0},"{1}"),\n'.format(entry.data.Pmin.value, entry.data.Pmin.units))
                    f.write('        Pmax = ({0},"{1}"),\n'.format(entry.data.Pmax.value, entry.data.Pmax.units))
                f.write('    ),\n')
                
                lines = entry.reference.toPrettyRepr().splitlines()
                f.write('    reference = {0}\n'.format(lines[0]))
                for line in lines[1:-1]:
                    f.write('    {0}\n'.format(line))
                f.write('    ),\n')
                
                f.write('    referenceType = "{0}",\n'.format(entry.referenceType))
                f.write('    shortDesc = u"""{0}""",\n'.format(entry.shortDesc))
                f.write('    longDesc = \nu"""\n{0}\n""",\n'.format(entry.longDesc))
                f.write('    history = {0},\n'.format(entry.history))
                f.write(')\n')
                
                index += 1
    
        print '\n   ... saved {0} identified entries to {1}/NIST.'.format(len(entries), family)

################################################################################

def processUniqueEntries(entries):
    
    cookiejar = cookielib.CookieJar()
    
    processedEntries = []
    
    count = 1
    
    for entry in entries:
        
        forwardReaction = entry.item
        reverseReaction = Reaction(
                            reactants = entry.item.products,
                            products = entry.item.reactants,
                            degeneracy = entry.item.degeneracy
                          )
        
        setNISTUnits(cookiejar)
        
        print '\n   Searching NIST for reaction #{0} ({1} -> {2})...'.format(count, ' + '.join([str(getCAS(r)) for r in forwardReaction.reactants]), ' + '.join([str(getCAS(p)) for p in forwardReaction.products])),
        forwardEntries = queryNIST(forwardReaction, cookiejar)
        cookiejar.clear_session_cookies()
        reverseEntries = queryNIST(reverseReaction, cookiejar)
        setNISTUnits(cookiejar)
        cookiejar.clear_session_cookies()
        print '{0} forward, {1} reverse results found.'.format(len(forwardEntries), len(reverseEntries)),
        
        count += 1
    
        for entry in forwardEntries:
            queryReference(entry, cookiejar)
            processedEntries.append(entry)
        
        for entry in reverseEntries:
            queryReference(entry, cookiejar)
            processedEntries.append(entry)
    
    return processedEntries

################################################################################

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
    request = opener.open('http://kinetics.nist.gov/kinetics/SetUnitsBean.jsp', data=urllib.urlencode(post))
    unitsHTML = request.read()
    request.close()

################################################################################

def queryNIST(reaction, cookiejar):
    
    entries = []
    
    post = {
        'boolean1': '',
        'boolean2': 'and',
        'boolean3': 'and',
        'boolean4': 'and',
        'category': '0',
        'database': 'kinetics',
        'doc': 'SearchForm',
        'lp1': ' ',
        'lp2': ' ',
        'lp3': ' ',
        'lp4': ' ',
        'relate1': '=',
        'relate2': '=',
        'relate3': '=',
        'relate4': '=',
        'rp1': ' ',
        'rp2': ' ',
        'rp3': ' ',
        'rp4': ' ',
        'type': 'java',
        'Units': '',
    }
    count = 0
    for reactant in reaction.reactants:
        count += 1
        post['field{0:d}'.format(count)] = 'reactants'
        post['text{0:d}'.format(count)] = getCAS(reactant)
    for product in reaction.products:
        count += 1
        post['field{0:d}'.format(count)] = 'products'
        post['text{0:d}'.format(count)] = getCAS(product)
    post['numberOfFields'] = str(count)
    
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    request = opener.open('http://kinetics.nist.gov/kinetics/Search.jsp', data=urllib.urlencode(post))
    searchHTML = request.read()
    request.close()
    
    if "No records found" in searchHTML:
        return []
    elif "There was no match in the database for the following input" in searchHTML:
        return []
    elif "Click on a link in the table below to see detail on the selected reaction" in searchHTML:
        return []
    
    soup = BeautifulSoup(searchHTML)
    
    form = soup.findAll(name='form', attrs={'name': 'KineticsResults'})[0]
    for tr in form.findAll(name='tr'):
        tdlist = tr.findAll(name='td')
        if len(tdlist) == 17:
            
            # Some extra effort is needed to extract the squib from the BeautifulSoup DOM tree
            
            squib = re.search('\d\d\d\d\w\w\w?(/\w\w\w?)?\w+(-\w+)?:\d+', unicode(tdlist[2].a))
            url = 'http://kinetics.nist.gov/kinetics/Detail?id={0}'.format(squib.group()).encode()
            
            # Assume the result is of modified Arrhenius form
            Trange = tdlist[6].text
            A = tdlist[8].text
            n = tdlist[10].text
            Ea = tdlist[12].text
            k300 = tdlist[14].text
            order = tdlist[16].text
            
            # Reject results that don't have a valid preexponential or activation energy
            if ';' in A or ';' in Ea:
                continue
            # Reject results whose reaction order does not match the number of reactants
            if int(order) != len(reaction.reactants):
                continue
            
            # Many times n is not given, so set it to zero if that happens
            if n == '&nbsp;':
                n = 0.0
                
            # Convert the temperature range to separate minimum and maximum valies
            if '-' in Trange:
                Tmin, Tmax = Trange.split('-')
            else:
                Tmin = Trange; Tmax = Trange
            
            # Create an entry for this result and append it to the list of entries
            entry = Entry(
                item = reaction,
                label = squib.group(),
                data = Arrhenius(
                    A = (float(A) / 1.0e6,"m^3/(mol*s)") if len(reaction.reactants) == 2 else (float(A),"s^-1"),
                    n = (float(n),""),
                    Ea = (float(Ea),"J/mol"),
                    T0 = (1.0,"K"),
                    Tmin = (float(Tmin),"K"),
                    Tmax = (float(Tmax),"K"),
                    Pmin = (0,"Pa"),
                    Pmax = (0,"Pa"),
                ),
                reference = url,
            )
            entries.append(entry)
    
    return entries

################################################################################

def queryReference(entry, cookiejar):
    
    setNISTUnits(cookiejar)
    
    # Fetch the HTML page for the reference and kinetics
    url = entry.reference
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    request = opener.open(url)
    referenceHTML = request.read()
    request.close()
    
    soup = BeautifulSoup(referenceHTML)
    
    squib = soup.table.findAll(text='Squib:')[0].parent.nextSibling[13:]
    category = soup.table.findAll(text='Category:')[0].parent.nextSibling[7:].lower()
    datatype = soup.table.findAll(text='Data type:')[0].parent.nextSibling[13:]
    
    reftype = soup.table.findAll(text='Reference type:')[0].parent.nextSibling[13:].lower()
    if reftype == 'technical report': reftype = 'journal article'
    assert reftype in ['journal article', 'book chapter'], 'Unexpected reference type "{0}" from squib "{1}".'.format(reftype, squib)
    
    # Extract the authors and process each author name to the preferred format
    if reftype in ['journal article', 'book chapter']:
        authors0 = soup.table.findAll(text='Author(s):')[0].parent.nextSibling[13:]
        authors = []
        for author0 in authors0.split(';'):
            authors.append(author0.strip())
        
    # Create a reference object describing the reference based on the type in reftype
    if reftype == 'journal article':
        title   = soup.table.findAll(text='Title:')[0].parent.nextSibling[13:]
        journal = soup.table.findAll(text='Journal:')[0].parent.nextSibling[13:]
        try:
            volume  = soup.table.findAll(text='Volume:')[0].parent.nextSibling[13:]
        except IndexError:
            volume = ''
        pages   = soup.table.findAll(text='Page(s):')[0].parent.nextSibling[13:]
        year    = soup.table.findAll(text='Year:')[0].parent.nextSibling[13:]
        entry.reference = Article(
            authors = authors,
            title = title,
            journal = journal,
            volume = volume,
            pages = re.sub(' - ', '-', pages),
            year = year,
        )
    
    elif reftype == 'book chapter':
        title   = soup.table.findAll(text='Title:')[0].parent.nextSibling[13:]
        publisher = soup.table.findAll(text='Publisher address:')[0].parent.nextSibling[13:]
        year    = soup.table.findAll(text='Year:')[0].parent.nextSibling[13:]
        entry.reference = Book(
            authors = authors,
            title = title,
            publisher = publisher,
            year = year,
        )
        
    # Reference metadata common to all reference types
    entry.reference.url = url
    entry.referenceType = category
    entry.shortDesc = datatype
    entry.longDesc = """Imported from {0}""".format(url)

    try:
        Prange = soup.table.findAll(text='Pressure:')[0].parent.nextSibling[13:]
    except IndexError:
        Prange = ''
    
    if Prange is not '':
        if ' - ' in Prange:
            Pmin = Prange.split(' ')[0]
            Pmax = Prange.split(' ')[2]
        else:
            Pmin = Prange.split(' ')[0]
            Pmax = Prange.split(' ')[0]
    else:
        Pmin = False
        Pmax = False
    
    if Pmin:
        entry.data.Pmin.value = float(Pmin)
    if Pmax:
        entry.data.Pmax.value = float(Pmax)
    
    return entry

################################################################################

if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        raise Exception('You must provide the name of the reaction family as the lone command-line argument.')
    
    family = sys.argv[1]
    
    identifiedEntries, unidentifiedEntries = loadEntries(family)
	
    savePrIMe(unidentifiedEntries, family)
    
    if identifiedEntries:
        uniqueEntries = sortIdentified(identifiedEntries)
        saveNIST(processUniqueEntries(uniqueEntries), family)
