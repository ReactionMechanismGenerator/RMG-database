#!/usr/bin/env python
# encoding: utf-8

"""
This script will generate an Evans-Polanyi plot for a single kinetics family.
"""
import math
import numpy
import pylab

from rmgpy.reaction import Reaction
from rmgpy.kinetics import Arrhenius

################################################################################

def generate_thermo_data(species, database):
    """
    Return the thermodynamics data for a given `species` as generated from
    the specified `database`.
    """
    thermo_data = [database.thermo.get_thermo_data(species)]
    thermo_data.sort(key=lambda x: x.get_enthalpy(298))
    return thermo_data[0]

def get_reaction_for_entry(entry, database):
    """
    Return a Reaction object for a given entry that uses Species instead of
    Molecules (so that we can compute the reaction thermo).
    """
    reaction = Reaction(reactants=[], products=[])
    for reactant in entry.item.reactants:
        reactant.generate_resonance_structures()
        reactant.thermo = generate_thermo_data(reactant, database)
        reaction.reactants.append(reactant)
    for product in entry.item.products:
        product.generate_resonance_structures()
        product.thermo = generate_thermo_data(product, database)
        reaction.products.append(product)
    
    reaction.kinetics = entry.data
    reaction.degeneracy = entry.item.degeneracy
    
    return reaction

################################################################################

def fit_evans_polanyi(dHrxn, Ea):
    """
    Generate best-fit Evans-Polanyi parameters for the given set of enthalpy
    of reaction and activation energy data. This can be done using a simple
    linear least-squares optimization.
    """

    # Fit Evans-Polanyi parameters to the entire dataset
    N = len(dHrxn)
    A = numpy.zeros((N, 2), numpy.float64)
    b = numpy.zeros(N, numpy.float64)
    for index in range(N):
        A[index,0] = dHrxn[index]
        A[index,1] = 1
        b[index] = Ea[index]
    x, residues, rank, s = numpy.linalg.lstsq(A, b, rcond=None)

    # In the above fit, we probably included reactions with very negative or
    # very positive dHrxn, for which Ea = 0 and Ea = dHrxn, respectively
    # However, the Evans-Polanyi fit predicts very unphysical values of Ea in
    # these limits, since it's only linear
    # To improve the Evans-Polanyi fit, let's impose the condition 0 <= Ea <= dHrxn
    # When we do this, we can improve the fit over the linear region by
    # excluding the very negative and very positive dHrxn points from our
    # dataset and refitting using only the points in the linear region
    # This presumes that we will impose 0 <= Ea <= dHrxn where needed
    Hmin = -x[1] / x[0]
    Hmax = x[1] / (1 - x[0])
    A = []; b = []
    for index in range(N):
        if Hmin <= dHrxn[index] <= Hmax:
            A.append([dHrxn[index], 1])
            b.append(Ea[index])
    A = numpy.array(A, numpy.float64)
    b = numpy.array(b, numpy.float64)
    x, residues, rank, s = numpy.linalg.lstsq(A, b, rcond=None)
    Hmin = -x[1] / x[0]
    Hmax = x[1] / (1 - x[0])
    
    # Compute sample standard deviation and standard error
    stdev = 0.0; error = 0.0; count = 0
    for H, E in zip(dHrxn, Ea):
        if H < Hmin:
            stdev += (E - 0)**2
        elif H > Hmax:
            stdev += (E - H)**2
        else:
            E0 = x[0] * H + x[1]
            if E0 < 0 and H < 0: E0 = 0
            elif E0 < H and H > 0: E0 = H
            stdev += (E0 - E)**2
        count += 1
    stdev = math.sqrt(stdev / (count - 1))
    
    dHrxn1 = numpy.arange(min(dHrxn), max(dHrxn), 0.1, numpy.float64)
    Ea1 = []
    for H in dHrxn1:
        E = x[0] * H + x[1]
        if E < 0 and H < 0: E = 0
        elif E < H and H > 0: E = H
        Ea1.append(E)
    Ea1 = numpy.array(Ea1, numpy.float64)
    dHrxn1 = numpy.array(dHrxn1, numpy.float64)

    return x, stdev, dHrxn1, Ea1

################################################################################

def generate_evans_polanyi_plot(depository, database):
    """
    Generate an Evans-Polanyi plot for the entries in the given `depository`
    of the loaded `database`.
    """
    
    fig = pylab.figure(figsize=(6,5))
        
    Ea = []; dHrxn = []; reactions = []
    entries = list(depository.entries.values())
    
    for entry in entries:
        if isinstance(entry.data, Arrhenius):

            reaction = get_reaction_for_entry(entry, database)

            reactions.append(reaction)
            Ea.append(reaction.kinetics.Ea.value / 1000.)
            dHrxn.append(reaction.get_enthalpy_of_reaction(298) / 1000.)
            
    xEP, stdevEP, dHrxnEP, EaEP = fit_evans_polanyi(dHrxn, Ea)

    print()
    print('Summary')
    print('=======')
    print('Parameters:')
    print('    Evans-Polanyi = %s' % (xEP))
    print('Sample standard deviation:')
    print('    Evans-Polanyi = %g kJ/mol' % (stdevEP))
    print('95% confidence limit:')
    print('    Evans-Polanyi = %g kJ/mol' % (1.96 * stdevEP))

    pylab.plot(dHrxn,   Ea,   color='#B0B0B0', linestyle='None', marker='o', picker=5)
    pylab.plot(dHrxnEP, EaEP, color='red', linestyle='solid', linewidth=2)
    pylab.plot(dHrxnEP, EaEP + 1.96 * stdevEP, color='red', linestyle='dashed', linewidth=1)
    pylab.plot(dHrxnEP, EaEP - 1.96 * stdevEP, color='red', linestyle='dashed', linewidth=1)
    
    pylab.xlabel('Enthalpy of reaction at 298 K (kJ/mol)')
    pylab.ylabel('Arrhenius activation energy (kJ/mol)')
    pylab.xlim(-350,350)
    pylab.ylim(-100,350)
    pylab.minorticks_on()

    fig.subplots_adjust(left=0.14, bottom=0.1, top=0.95, right=0.95, wspace=0.20, hspace=0.20)
    
    def on_pick(event):
        print('Pick')
        thisline = event.artist
        dHrxn = thisline.get_xdata()
        Ea = thisline.get_ydata()
        for ind in event.ind:
            entry = entries[ind]
            reaction = reactions[ind]
            print('%i. %s' % (entry.index, entry.label))
            print(reaction)
            print('dHrxn    = %.2f kJ/mol' % (dHrxn[ind]))
            print('Ea       = %.2f kJ/mol' % (Ea[ind]))
            for reactant in reaction.reactants:
                print('%24s H298 = %g kcal/mol' % (reactant, reactant.thermo.get_enthalpy(300) / 4184.))
            for product in reaction.products:
                print('%24s H298 = %g kcal/mol' % (product, product.thermo.get_enthalpy(300) / 4184.))

    fig.canvas.mpl_connect('pick_event', on_pick)

    pylab.show()

################################################################################

if __name__ == '__main__':

    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('kinetics_family', metavar='<family>', type=str, nargs=1, help='the family to use')
    parser.add_argument('kinetics_depository', metavar='<kinetics_depository>', type=str, nargs='+',
                        help='the kineticsDepository to use, e.g., training, NIST')
    
    args = parser.parse_args()
    
    print('Loading RMG database...')
    from rmgpy.data.rmg import RMGDatabase
    from rmgpy import settings
    database = RMGDatabase()
    database.load(settings['database.directory'], kinetics_families=args.kinetics_family,
                  kinetics_depositories=args.kinetics_depository)

    family = database.kinetics.families.get(args.kinetics_family[0])

    print('Generating Evans-Polanyi data...')
    for depository in family.depositories:
        try:
            generate_evans_polanyi_plot(depository, database)
        except KeyError:
            print(e)
            print('The specified depository "{0}" was invalid.'.format(depository))
            quit()
