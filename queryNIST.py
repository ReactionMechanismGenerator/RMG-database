#!/usr/bin/env python
# encoding: utf-8

"""
This script queries the NIST Chemical Kinetics Database 
(<http://kinetics.nist.gov>) for a given gas-phase reaction, parses the HTML
output, and creates a new file in the RMG database for that reaction and all
the matching kinetics.
"""

import os
import os.path
import sys
import re

from rmgpy.data.base import Entry
from rmgpy.data.reference import *
from rmgpy.kinetics import Arrhenius
from rmgpy.species import Species
from rmgpy.reaction import Reaction

import urllib
import urllib2
import cookielib
from BeautifulSoup import BeautifulSoup

################################################################################

forwardReaction = None
reverseReaction = None
reactionIndex = None
reactionLabel = None

def reaction(index, label, reactant1, product1, forwardDegeneracy, reverseDegeneracy, reactant2=None, product2=None):
    global forwardReaction, reverseReaction, reactionIndex, reactionLabel
    
    reactants = []
    reactants.append(Species().fromAdjacencyList(reactant1))
    if reactant2: reactants.append(Species().fromAdjacencyList(reactant2))
    for reactant in reactants:
        if reactant.label == '':
            reactant.label = reactant.molecule[0].toSMILES()
            
    products = []
    products.append(Species().fromAdjacencyList(product1))
    if product2: products.append(Species().fromAdjacencyList(product2))
    for product in products:
        if product.label == '':
            product.label = product.molecule[0].toSMILES()
    
    reactionIndex = index
    reactionLabel = label
    forwardReaction = Reaction(reactants=reactants, products=products, degeneracy=forwardDegeneracy)
    reverseReaction = Reaction(reactants=products, products=reactants, degeneracy=reverseDegeneracy)

def entry(forward, kinetics, reference, referenceType, shortDesc, longDesc):
    pass

def loadReaction(path):
    """
    
    """
    print 'Loading reaction from {0}...'.format(os.path.relpath(path))
    
    # Set up global and local context
    global_context = {
        '__builtins__': None,
        'True': True,
        'False': False,
        'reactionIndex': None,
        'reactionLabel': None,
        'forwardReaction': None,
        'reverseReaction': None,
    }
    local_context = {
        '__builtins__': None,
        'reaction': reaction,
        'entry': entry,
        'Arrhenius': Arrhenius,
        'Article': Article,
        'Book': Book,
        'Thesis': Thesis,
        'Reference': Reference,
    }    
    
    # Process the file
    f = open(path, 'r')
    exec f in global_context, local_context
    f.close()
    
    return reactionIndex, reactionLabel, forwardReaction, reverseReaction

################################################################################

def getNISTIdentifier(species):
    """
    For a given `species`, return a string identifier that NIST is likely to
    associate with the same species in its database. In general the lowest
    available CAS number seems to work. We query the NIST Chemical Identifier 
    Resolver to convert an InChI to a CAS number; if this fails we return the
    chemical formula.
    """
    
    inchi = species.molecule[0].toInChI()
    smiles = species.molecule[0].toSMILES()
    formula = species.molecule[0].getFormula()
    
    # When this works, it is more likely to give a CAS number that NIST knows about
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
    
    # When the above does not work, the below sometimes gives at least one CAS number
    # It could also give multiple CAS numbers, in which case we keep the lowest
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
    
    # If nothing else works, just use the chemical formula
    return formula

################################################################################

def queryNIST(reactants, products):
    """
    Query the NIST website for the gas-phase reaction consisting of the given
    lists of `reactants` and `products`, which should already be in a form that
    NIST understands (e.g. CAS number).    
    """
    
    # Create a session cookie (so that the units set below persist)
    cookiejar = cookielib.CookieJar()
    
    # Set the units to use for this session
    setNISTUnits(reactants, products, cookiejar)
    
    # Now search for the reaction
    entries = queryNISTKinetics(reactants, products, cookiejar)
    
    # Also extract reference information for each reference
    # (This information is also available within the kinetics search results,
    # but is much easier to extract from its details page)
    for entry in entries:
        queryNISTReference(entry, entry.reference, cookiejar)
        
    # Clear the cookies we used for these queries
    cookiejar.clear_session_cookies()
    
    # Return the resulting entries
    return entries
      
def setNISTUnits(reactants, products, cookiejar):
    """
    Query the NIST website for the gas-phase reaction consisting of the given
    lists of `reactants` and `products`, which should already be in a form that
    NIST understands (e.g. CAS number).    
    """
    
    # Set the POST data to contain the units to use for this session
    post = {
        'energyUnits': 'kJ',
        'evaluationTemperature': '300.0',
        'moleculeUnits': 'Mole',
        'pressureUnits': 'bar',
        'referenceTemperature': '1.0',
        'temperatureUnits': 'K',
        'volumeUnits': 'cm',
    }
    
    # Make an HTML query to NIST to POST the units we want to use
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    request = opener.open('http://kinetics.nist.gov/kinetics/SetUnitsBean.jsp', data=urllib.urlencode(post))
    unitsHTML = request.read()
    request.close()
    
def queryNISTKinetics(reactants, products, cookiejar):
    """
    Query the NIST website for the gas-phase reaction consisting of the given
    lists of `reactants` and `products`, which should already be in a form that
    NIST understands (e.g. CAS number).    
    """
    
    entries = []
    
    # Set the POST data to contain the parameters for our reaction kinetics query
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
    for reactant in reactants:
        count += 1
        post['field{0:d}'.format(count)] = 'reactants'
        post['text{0:d}'.format(count)] = reactant
    for product in products:
        count += 1
        post['field{0:d}'.format(count)] = 'products'
        post['text{0:d}'.format(count)] = product
    post['numberOfFields'] = str(count)
    
    # Formally query the NIST kinetics database
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    request = opener.open('http://kinetics.nist.gov/kinetics/Search.jsp', data=urllib.urlencode(post))
    searchHTML = request.read()
    request.close()
    
    # Some checks to ensure that the search was successful
    if "No records found" in searchHTML:
        return []
    elif "There was no match in the database for the following input" in searchHTML:
        return []
    elif "Click on a link in the table below to see detail on the selected reaction" in searchHTML:
        return []
    
    # Parse the returned HTML to extract the kinetics information
    # We use the BeautifulSoup package because the returned HTML is probably
    # not valid XML, so DOM and SAX parsers would choke
    soup = BeautifulSoup(searchHTML)
    
    form = soup.findAll(name='form', attrs={'name': 'KineticsResults'})[0]
    for tr in form.findAll(name='tr'):
        tdlist = tr.findAll(name='td')
        if len(tdlist) == 17:
            
            # Some extra effort is needed to extract the squib from the BeautifulSoup DOM tree
            squib = re.search('\d\d\d\d\w\w\w?(/\w\w\w?)?\w+(-\w+)?:\d+', unicode(tdlist[2].a))
            squib = squib.group()
            
            # Assume the result is of modified Arrhenius form
            Trange = tdlist[6].text
            A = tdlist[8].text
            n = tdlist[10].text
            Ea = tdlist[12].text
            k300 = tdlist[14].text
            order = tdlist[16].text
            
            # Reject results that don't have a valid preexponential or activation energy
            if A == '&nbsp;' or Ea == '&nbsp;':
                continue
            # Reject results whose reaction order does not match the number of reactants
            if int(order) != len(reactants):
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
                data = Arrhenius(
                    A = (float(A.split(';')[-1]),"cm^3/(mol*s)" if len(reactants) == 2 else "s^-1"),
                    n = float(n),
                    Ea = (float(Ea),"kJ/mol"),
                    T0 = (1.0,"K"),
                    Tmin = (float(Tmin),"K"),
                    Tmax = (float(Tmax),"K"),
                ),
                reference = squib, # Just save the squib for now; we'll get the actual reference later
            )
            entries.append(entry)
    
    return entries
    
def queryNISTReference(entry, squib0, cookiejar):    
    
    # The NIST database stores its authors as last name first (e.g. 
    # "Allen, J.W."), which leads to comma overload in many-author references
    # I prefer having the last name last (e.g. "J. W. Allen") to make things
    # easier to read
    # These regular expressions handle various forms for authors
    author_regexes = [
        (r'([\w-]+), (\w+\.)(\w+\.)(\w+\.), Jr.', r'\2 \3 \4 \1, Jr.'),
        (r'([\w-]+), (\w+\.)(\w+\.), Jr.',        r'\2 \3 \1, Jr.'),
        (r'([\w-]+), (\w+\.)-(\w+\.), Jr.',       r'\2-\3 \1, Jr.'),
        (r'([\w-]+), (\w+-\w+\.), Jr.',           r'\2 \1, Jr.'),
        (r'([\w-]+), (\w+\.), Jr.',               r'\2 \1, Jr.'),
        (r'([\w-]+), (\w+\.)(\w+\.)(\w+\.)',      r'\2 \3 \4 \1'),
        (r'([\w-]+), (\w+\.)(\w+\.)',             r'\2 \3 \1'),
        (r'([\w-]+), (\w+\.)-(\w+\.)',            r'\2-\3 \1'),
        (r'([\w-]+), (\w+-\w+\.)',                r'\2 \1'),
        (r'([\w-]+), (\w+\.)',                    r'\2 \1'),
    ]
    
    # Fetch the HTML page for the reference and kinetics
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    request = opener.open('http://kinetics.nist.gov/kinetics/Detail?id={0}'.format(squib0))
    referenceHTML = request.read()
    request.close()
    
    # Parse the returned HTML to extract the reference information
    # We use the BeautifulSoup package because the returned HTML is probably
    # not valid XML, so DOM and SAX parsers would choke
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
            author0 = author0.strip()
            for pattern, repl in author_regexes:
                author = re.sub(pattern, repl, author0)
                if author != author0:
                    break
            authors.append(author)
        
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
    entry.reference.url = 'http://kinetics.nist.gov/kinetics/Detail?id={0}'.format(squib)
    entry.referenceType = category
    entry.shortDesc = datatype
    entry.longDesc = """Imported from http://kinetics.nist.gov/kinetics/Detail?id={0}""".format(squib0)
    
    return entry
    
################################################################################

def saveEntry(f, entry, forward):

    f.write('entry(\n')
    f.write('    forward = {0},\n'.format(forward))
    
    # Write kinetics
    kinetics = entry.data.toPrettyRepr()
    lines = kinetics.splitlines()
    f.write('    kinetics = {0}\n'.format(lines[0]))
    for line in lines[1:-1]:
        f.write('    {0}\n'.format(line))
    f.write('    ),\n'.format(lines[0]))

    # Write reference
    reference = entry.reference.toPrettyRepr()
    lines = reference.splitlines()
    f.write('    reference = {0}\n'.format(lines[0]))
    for line in lines[1:-1]:
        f.write('    {0}\n'.format(line))
    f.write('    ),\n'.format(lines[0]))
        
    f.write('    referenceType = "{0}",\n'.format(entry.referenceType))
    f.write('    shortDesc = u"""{0}""",\n'.format(entry.shortDesc))
    f.write('    longDesc = \n')
    f.write('u"""\n')
    f.write(entry.longDesc.strip() + "\n")
    f.write('""",\n')
    f.write(')\n\n')

def save(reactionIndex, reactionLabel, forwardReaction, reverseReaction, forwardEntries, reverseEntries, filename):
    """
    Save the results of a query to the NIST kinetics database to `filename` on
    disk.
    """
    
    with open(filename, 'w') as f:

        f.write('#!/usr/bin/env python\n')
        f.write('# encoding: utf-8\n\n')
        
        f.write('reaction(\n')
        f.write('    index = {0:d},\n'.format(reactionIndex))
        f.write('    label = "{0!s}",\n'.format(reactionLabel))

        for index in range(len(forwardReaction.reactants)):
            f.write('    reactant{0} = \n'.format(index+1))
            f.write('"""\n')
            f.write(forwardReaction.reactants[index].toAdjacencyList())
            f.write('""",\n')

        for index in range(len(forwardReaction.products)):
            f.write('    product{0} = \n'.format(index+1))
            f.write('"""\n')
            f.write(forwardReaction.products[index].toAdjacencyList())
            f.write('""",\n')

        f.write('    forwardDegeneracy = {0:d},\n'.format(forwardReaction.degeneracy))
        f.write('    reverseDegeneracy = {0:d},\n'.format(reverseReaction.degeneracy))
        f.write(')\n\n')
        
        f.write('################################################################################\n\n')
  
        for entry in forwardEntries:
            saveEntry(f, entry, True)
        for entry in reverseEntries:
            saveEntry(f, entry, False)
        
################################################################################

def searchReaction(reactionIndex, reactionLabel, forwardReaction, reverseReaction, filename):
    """
    For a given chemical reaction defined by a list of one or two `reactant`
    species and a list of one or two `product` species, search the literature
    (via the NIST Chemical Kinetics Database at <http://kinetics.nist.gov/> for
    kinetic models for that reaction. The `forwardDegeneracy` and 
    `reverseDegeneracy` parameters are used to specify the forward and reverse
    reaction-path degeneracies, respectively. The results of the search are
    saved to the given `filename` on disk.
    """
    
    reactants = forwardReaction.reactants
    products = forwardReaction.products
    forwardDegeneracy = forwardReaction.degeneracy
    reverseDegeneracy = reverseReaction.degeneracy
    
    # For each species, determine an identifier that the NIST database is likely to understand
    print 'Determining NIST species identifiers...'
    reactantIdentifiers = []; productIdentifiers = []
    for species in reactants:
        identifier = getNISTIdentifier(species)
        reactantIdentifiers.append(identifier)
        print '    Identifier for {0!s} is "{1}"'.format(species, identifier)
    for species in products:
        identifier = getNISTIdentifier(species)
        productIdentifiers.append(identifier)
        print '    Identifier for {0!s} is "{1}"'.format(species, identifier)
    
    # Query the NIST database for kinetics in both directions
    print 'Searching NIST for reaction {0} -> {1}...'.format(' + '.join([str(r) for r in reactants]), ' + '.join([str(p) for p in products]))
    forwardEntries = queryNIST(reactantIdentifiers, productIdentifiers)
    print '{0} results found.'.format(len(forwardEntries))
    print 'Searching NIST for reaction {0} -> {1}...'.format(' + '.join([str(p) for p in products]), ' + '.join([str(r) for r in reactants]))
    reverseEntries = queryNIST(productIdentifiers, reactantIdentifiers)
    print '{0} results found.'.format(len(reverseEntries))
    
    # Swap the reaction direction if there are more matches in the reverse
    # direction than in the forward direction
    if len(reverseEntries) > len(forwardEntries):
        forwardReaction, reverseReaction = reverseReaction, forwardReaction
        reactantIdentifiers, productIdentifiers = productIdentifiers, reactantIdentifiers
        forwardEntries, reverseEntries = reverseEntries, forwardEntries
        forwardDegeneracy, reverseDegeneracy = reverseDegeneracy, forwardDegeneracy
    
    # Save the matching results in both directions to the specified file
    print 'Saving {0} results to {1}...'.format(len(forwardEntries) + len(reverseEntries), filename)
    save(reactionIndex, reactionLabel, forwardReaction, reverseReaction, forwardEntries, reverseEntries, filename)

################################################################################

if __name__ == '__main__':
    
    if len(sys.argv) < 3:
        raise Exception('You must pass the family name and reaction index (or multiple indices) as command-line parameters.')
        
    family = str(sys.argv[1])
    for index in sys.argv[2:]:
        index = int(index)
        filename = 'input/kinetics/families/{0!s}/training/{1:d}.py'.format(family, index)
        reactionIndex, reactionLabel, forwardReaction, reverseReaction = loadReaction(filename)
        filename = 'input/kinetics/families/{0!s}/training/{1:d}.py'.format(family, index)
        searchReaction(reactionIndex, reactionLabel, forwardReaction, reverseReaction, filename)
