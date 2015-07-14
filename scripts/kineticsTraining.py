#!/usr/bin/env python
# encoding: utf-8

"""
This script can be used to generate the "best fit" high-pressure limit kinetics
to a set of input kinetics.

To simply generate the best-fit kinetics, use the command ::

$ python kineticsTraining.py generate <family> <index>

where <family> is the name of the reaction family and <index> is the index of
the reaction to generate the recommended kinetics for. To also generate a plot
of the best-fit kinetics, use the command ::

$ python kineticsTraining.py evaluate <family> <index>

"""

import os.path
import math
import numpy
import matplotlib
matplotlib.rc('mathtext', fontset='stixsans', default='regular')
import pylab

from rmgpy.quantity import Quantity, constants
from rmgpy.thermo import *
from rmgpy.kinetics import *
from rmgpy.data.reference import *
from rmgpy.data.base import Entry
from rmgpy.data.thermo import ThermoDatabase
from rmgpy.data.kinetics import saveEntry
from rmgpy.molecule import Molecule
from rmgpy.species import Species
from rmgpy.reaction import Reaction

################################################################################

class ArgumentError(Exception):
    """
    An exception raised when the command-line arguments given to the script are
    invalid. Pass a string describing why the arguments are invalid.
    """
    pass

################################################################################

forwardKinetics = []
reverseKinetics = []
forwardReaction = None
reverseReaction = None
forwardWeights = []
reverseWeights = []

def loadSpecies(adjlist):
    species = Species().fromAdjacencyList(adjlist)
    species.molecule = species.molecule[0].generateResonanceIsomers()
    species.thermo = getThermoData(species)
    species.molecule = [Molecule().fromAdjacencyList(adjlist)]
    return species

def reaction(index, label, reactant1, product1, forwardDegeneracy=1, reverseDegeneracy=1, reactant2=None, product2=None, product3=None):
    global forwardReaction, reverseReaction
    reactants = [loadSpecies(reactant1)]
    if reactant2:
        reactants.append(loadSpecies(reactant2))
    products = [loadSpecies(product1)]
    if product2:
        products.append(loadSpecies(product2))
    if product3:
        reactants.append(loadSpecies(product3))
    forwardReaction = Reaction(reactants=reactants, products=products, degeneracy=forwardDegeneracy)
    reverseReaction = Reaction(reactants=products, products=reactants, degeneracy=reverseDegeneracy)
    
def entry(forward, kinetics, reference, referenceType, shortDesc, longDesc, weight=1.0):
    global forwardKinetics, reverseKinetics
    referenceTypes = {'theory': 'T', 'experiment': 'E', 'review': 'R'}
    try:
        comment = referenceTypes[referenceType] + '/'
    except KeyError:
        comment = ''
    author = reference.authors[0].split()
    if author[-1] == 'Jr.':
        author = author[-2][:-1]
    else:
        author = author[-1]
    comment += '{0!s}/{1!s}'.format(reference.year, author)
    kinetics.comment = comment
    if forward:
        forwardKinetics.append(kinetics)
        forwardWeights.append(weight)
    else:
        reverseKinetics.append(kinetics)
        reverseWeights.append(weight)
    
def loadKinetics(path):
    """
    Load a set of kinetics data from the file located at `path` on disk.
    """
    global forwardKinetics, reverseKinetics
    global forwardReaction, reverseReaction
    global forwardWeights, reverseWeights
    
    print 'Loading kinetics from {0}...'.format(os.path.relpath(path))
    
    forwardKinetics = []
    reverseKinetics = []
    forwardReaction = None
    reverseReaction = None
    forwardWeights = []
    reverseWeights = []

    # Set up global and local context
    global_context = {
        '__builtins__': None,
        'True': True,
        'False': False,
        'forwardKinetics': [],
        'reverseKinetics': [],
        'forwardWeights': [],
        'reverseWeights': [],
        'forwardReaction': None,
        'reverseReaction': None,
    }
    local_context = {
        '__builtins__': None,
        # Function prototypes
        'reaction': reaction,
        'entry': entry,
        # Constants
        'R': constants.R,
        'kB': constants.kB,
        # Kinetics types
        'KineticsData': KineticsData,
        'Arrhenius': Arrhenius,
        'ArrheniusEP': ArrheniusEP,
        'MultiKinetics': MultiKinetics,
        'PDepArrhenius': PDepArrhenius,
        'Chebyshev': Chebyshev,
        'ThirdBody': ThirdBody,
        'Lindemann': Lindemann,
        'Troe': Troe,
        # Reference types
        'Reference': Reference,
        'Article': Article,
        'Book': Book,
        'Thesis': Thesis,
    }    
    
    # Process the file
    f = open(path, 'r')
    exec f in global_context, local_context
    f.close()
    
    # For each kinetics entry in reverseKinetics, fit the reverse kinetics and
    # append it to forwardKinetics
    for kinetics0, weight in zip(reverseKinetics, reverseWeights):
        reverseReaction.kinetics = kinetics0
        try:
            kinetics = reverseReaction.generateReverseRateCoefficient()
        except IndexError:
            continue
        kinetics.Tmin = kinetics0.Tmin
        kinetics.Tmax = kinetics0.Tmax
        kinetics.comment = kinetics0.comment + '*'
        forwardKinetics.append(kinetics)
        forwardWeights.append(weight)
        
    return forwardKinetics, reverseKinetics, forwardWeights, reverseWeights
    
################################################################################

thermoDatabase = None

def loadThermoDatabase(path):
    """
    Load the RMG thermodynamics database from `path`.
    """
    global thermoDatabase
    print 'Loading thermodynamics database...'
    thermoDatabase = ThermoDatabase()
    thermoDatabase.load(path)

def getThermoData(species):
    global thermoDatabase
    
    # Ensure molecules are using explicit hydrogens
    implicitH = [mol.implicitHydrogens for mol in species.molecule]
    for molecule in species.molecule:
        molecule.makeHydrogensExplicit()
    
    thermo = []
    for molecule in species.molecule:
        molecule.clearLabeledAtoms()
        molecule.updateAtomTypes()
        thermo.append(thermoDatabase.getThermoData(species))

    H298 = numpy.array([t.getEnthalpy(298.) for t in thermo])
    indices = H298.argsort()

    # If multiple resonance isomers are present, use the thermo data of
    # the most stable isomer (i.e. one with lowest enthalpy of formation)
    # as the thermo data of the species
    thermo0 = thermo[indices[0]]

    # Sort the structures in order of decreasing stability
    species.molecule = [species.molecule[ind] for ind in indices]
    implicitH = [implicitH[ind] for ind in indices]

    # Convert to Wilhoit
    if isinstance(thermo0, Wilhoit):
        wilhoit = thermo0
    else:
        linear = species.molecule[0].isLinear()
        nRotors = species.molecule[0].countInternalRotors()
        nFreq = 3 * len(species.molecule[0].atoms) - (5 if linear else 6) - nRotors
        wilhoit = convertThermoModel(thermo0, Wilhoit, linear=linear, nFreq=nFreq, nRotors=nRotors)
    
    # Restore implicit hydrogens if necessary
    for implicit, molecule in zip(implicitH, species.molecule):
        if implicit: molecule.makeHydrogensImplicit()

    return wilhoit

################################################################################

def fitArrhenius(kineticsList, weights, Tlist, Tmin, Tmax):
    """
    Fit a modified Arrhenius expression to the set of loaded kinetics 
    `kineticsList` using the given array of temperatures `Tlist` in K. The
    `Tmin` and `Tmax` parameters specify the limits in K at which the fitted
    kinetics should be said to be valid. Returns the best-fit kinetics and the
    confidence interval (on a log scale).
    """
    import scipy.stats
    
    Tdata = []; kdata = []; wdata = []
    
    print 'Fitting modified Arrhenius kinetics...'
    
    for kinetics, weight in zip(kineticsList, weights):
        for n in range(len(Tlist)):
            if kinetics.isTemperatureValid(Tlist[n]):
                Tdata.append(Tlist[n])
                kdata.append(kinetics.getRateCoefficient(Tlist[n]))
                wdata.append(weight)
                
    Tdata = numpy.array(Tdata, numpy.float)
    kdata = numpy.array(kdata, numpy.float)
    wdata = numpy.array(wdata, numpy.float)
    arrhenius = Arrhenius().fitToData(Tdata, kdata, kunits='m^3/(mol*s)', T0=300, weights=wdata)
    
    # Compute RMS error and confidence interval
    count = len(kdata)
    rmsError = 0
    for T, k in zip(Tdata, kdata):
        rmsError += (math.log10(k) - math.log10(arrhenius.getRateCoefficient(T)))**2
    rmsError = math.sqrt(rmsError / (count - 3))
    ci = scipy.stats.t.ppf(0.975, count - 3) * rmsError
    
    # Adjust units of best-fit Arrhenius expression
    arrhenius.A.units = 'cm^3/(mol*s)' if len(forwardReaction.reactants) == 2 else 's^-1'
    arrhenius.Ea.units = 'kJ/mol'
    
    # Set Tmin and Tmax of best-fit Arrhenius expression
    arrhenius.Tmin = Quantity(Tmin,"K")
    arrhenius.Tmax = Quantity(Tmax,"K")
    
    return arrhenius, ci
       
################################################################################

def plotKinetics(kineticsList, Tlist, filename=None, bestKinetics=None):
    """
    Plot the set of loaded kinetics `kineticsList` at the array of temperatures
    `Tlist` in K. Different symbols denote the various reference types, while
    different linespecs denote individual kinetics within each reference type. 
    If given, the `bestKinetics` will also be plotted, using a thicker line to
    make it stand out.
    """
    
    sm = pylab.cm.ScalarMappable(
        norm = matplotlib.colors.Normalize(vmin=0, vmax=len(kineticsList)-1), 
        cmap = pylab.get_cmap('jet'),
    )

    if len(forwardReaction.reactants) == 2:
        kfactor = 1e6; kunits = '$cm^3/mol*s$'
    else:
        kfactor = 1; kunits = '$s^-1$'

    fig = pylab.figure(figsize=(8,6))
    legend = []; lines = []
    for index, kinetics in enumerate(kineticsList):
        klist = numpy.zeros_like(Tlist)
        for n in range(len(Tlist)):
            if kinetics.isTemperatureValid(Tlist[n]):
                klist[n] = kinetics.getRateCoefficient(Tlist[n])
        try:
            if kinetics.comment[0] == 'R':
                linespec = '-'
            elif kinetics.comment[0] == 'E':
                linespec = ':'
            elif kinetics.comment[0] == 'T':
                linespec = '--'
            else:
                linespec = '-.'
        except IndexError:
            continue
        color = sm.to_rgba(index)
        if numpy.any(klist):
            lines.append(pylab.semilogy(1000. / Tlist, klist * kfactor, linespec, color=color, picker=5)[0])
            legend.append(kinetics.comment)
        
    if bestKinetics:
        klist = numpy.zeros_like(Tlist)
        for n in range(len(Tlist)):
            if bestKinetics.isTemperatureValid(Tlist[n]):
                klist[n] = bestKinetics.getRateCoefficient(Tlist[n])
        if numpy.any(klist):
            pylab.semilogy(1000. / Tlist, klist * kfactor, '-k', linewidth=3)
            legend.append(bestKinetics.comment)
        
    pylab.xlabel('1000 / (Temperature (K))')
    pylab.ylabel('Rate coefficient ({0})'.format(kunits))
    pylab.xlim(0.0,4.0)
    pylab.legend(legend, loc=1)
    
    pylab.title('{0} $\\rightarrow$ {1}'.format(
        ' + '.join([spec.label for spec in forwardReaction.reactants]),
        ' + '.join([spec.label for spec in forwardReaction.products]),
    ))
    
    if filename:
        pylab.savefig(filename)
    
    def onpick(event):
        index = lines.index(event.artist)
        kinetics = kineticsList[index]
        print kinetics.comment
        print kinetics
            
    connection_id = fig.canvas.mpl_connect('pick_event', onpick)
    
    pylab.show()
    
################################################################################

def generateEntry(reaction, kinetics, index, ci):
    """
    Return a string containing the reaction and its recommended kinetics in a
    format suitable for putting in the training set.
    """
    import StringIO
    
    longDesc = ""
    
    entry = Entry(
        index = index,
        item = forwardReaction,
        data = kinetics,
        reference = None,
        referenceType = "review",
        shortDesc = "Recommended value based on evaluation of {0:d} kinetics entries. log(CI) = {1:.3f}".format(len(forwardKinetics), ci),
        longDesc = longDesc,
    )
    
    f = StringIO.StringIO()
    saveEntry(f, entry)
    string = f.getvalue()
    f.close()
    
    return string

################################################################################

Tlist_fit = 1000.0/numpy.arange(0.5, 3.34, 0.01, numpy.float)
Tlist_plot = 1000.0/numpy.arange(0.5, 3.34, 0.1, numpy.float)
Tmin = 300
Tmax = 2000

def getPath(family, index):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input', 'kinetics', 'families', family, 'training', '{0}.py'.format(index))

def generate(args):
    """
    Generate the recommended kinetics for a reaction.
    """
    family = str(args.family[0])
    
    for index in args.index:
        index = int(index)
    
        path = getPath(args.family[0], str(index))
        forwardKinetics, reverseKinetics, forwardWeights, reverseWeights = loadKinetics(path)
        kinetics, ci = fitArrhenius(forwardKinetics, forwardWeights, Tlist_fit, Tmin, Tmax)
        kinetics.comment = 'Best fit'
        
        print 
        print generateEntry(forwardReaction, kinetics, index, ci)

def evaluate(args):
    """
    Evaluate the collected kinetics for a given reaction.
    """
    family = str(args.family[0])
    
    for index in args.index:
        index = int(index)
    
        path = getPath(args.family[0], str(index))
        forwardKinetics, reverseKinetics, forwardWeights, reverseWeights = loadKinetics(path)
        
        done = False
        while not done:
            kinetics, ci = fitArrhenius(forwardKinetics, forwardWeights, Tlist_fit, Tmin, Tmax)
            kinetics.comment = 'Best fit'
            
            Tlist = Tlist_fit
            klist = numpy.zeros_like(Tlist)
            for n in range(len(Tlist)):
                if kinetics.isTemperatureValid(Tlist[n]):
                    klist[n] = kinetics.getRateCoefficient(Tlist[n])
                    
            done = True; outlier = None; outlierRMS = 0
            for kinetics0 in forwardKinetics:
                klist0 = numpy.zeros_like(Tlist)
                rms = 0; count = 0
                for n in range(len(Tlist)):
                    if kinetics0.isTemperatureValid(Tlist[n]):
                        klist0[n] = kinetics0.getRateCoefficient(Tlist[n])
                        error = math.log10(klist0[n]) - math.log10(klist[n])
                        rms += error * error
                        count += 1
                if count == 0: continue
                rms = math.sqrt(rms / count)
                if rms > 3.0 and rms > outlierRMS:
                    outlier = kinetics0
                    outlierRMS = rms
            if outlier is not None:
                forwardKinetics.remove(outlier)
                print 'Identified kinetics "{0}" as outlier (RMS = {1:g}). Removing it from Arrhenius fit.'.format(outlier.comment, outlierRMS)
                done = False
                    
        plotKinetics(forwardKinetics, Tlist_plot, filename='{0}.pdf'.format(path[:-3]), bestKinetics=kinetics)
        
        print 
        print generateEntry(forwardReaction, kinetics, index, ci)

################################################################################

if __name__ == '__main__':

    import argparse
    
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command', help='')
    
    # generate <index> - generate the recommended kinetics for a given reaction
    generateParser = subparsers.add_parser('generate', help='generate the recommended kinetics for a given reaction')
    generateParser.add_argument('family', type=str, nargs=1, help='the reaction family containing the reaction')
    generateParser.add_argument('index', type=str, nargs='+', help='the index of the reaction')
    generateParser.set_defaults(run=generate)
    
    # evaluate <index> - evaluate the collected kinetics for a given reaction
    evaluateParser = subparsers.add_parser('evaluate', help='evaluate the collected kinetics for a given reaction')
    evaluateParser.add_argument('family', type=str, nargs=1, help='the reaction family containing the reaction')
    evaluateParser.add_argument('index', metavar='<index>', type=str, nargs='+', help='the index of the reaction')
    evaluateParser.set_defaults(run=evaluate)
    
    args = parser.parse_args()
    
    loadThermoDatabase(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input', 'thermo'))
    
    try:
        args.run(args)
    except ArgumentError, e:
        for choice, subparser in subparsers.choices.iteritems():
            if args.command == choice:
                subparser.print_help()
                break
        else:
            parser.print_help()
        print 'ArgumentError: {0}'.format(e)
