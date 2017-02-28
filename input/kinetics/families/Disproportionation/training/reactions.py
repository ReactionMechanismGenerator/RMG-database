#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "C2H + CH3O <=> C2H2 + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.61e+13, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [90] Literature review.""",
    longDesc = 
u"""
[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.
Literature review: C2H + CH2OH --> C2H2 + CH2O

pg. 504: Discussion on evaluated data

Entry 39,21 (a): CH2OH + C2H --> C2H2 + CH2O

Author suggest a disproportionation rate coefficient of 6.0x10^-11 cm3/molecule/s, due

to very exothermic rxn.  No data available at the time.
MRH 30-Aug-2009
""",
)



entry(
    index = 2,
    label = "H + C10H9 <=> H2 + C10H8",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.11e+09, 'cm^3/(mol*s)'),
        n = 1.081,
        Ea = (2011, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H8_HACA""",
    longDesc = 
u"""
Taken from entry: A5 + H <=> N1 + H2
""",
)



entry(
    index = 3,
    label = "H + C10H9-2 <=> H2 + C10H8-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.05e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3405, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H8_HACA""",
    longDesc = 
u"""
Taken from entry: A9 + H <=> N1 + H2
""",
)

