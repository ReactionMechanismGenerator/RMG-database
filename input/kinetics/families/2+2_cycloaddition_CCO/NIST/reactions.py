#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition_CCO/NIST"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "C2H2O + C2H2O-2 <=> C4H4O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (178, 'm^3/(mol*s)'),
        n = 0,
        Ea = (73.999, 'kJ/mol', '+|-', 0.74),
        T0 = (1, 'K'),
        Tmin = (498, 'K'),
        Tmax = (596, 'K'),
        Pmin = (800, 'Pa'),
        Pmax = (15300, 'Pa'),
    ),
    reference = Article(
        authors = ["Blake, P.G.", "Davis, H.H."],
        title = u'Kinetics of Dimerisation of Gaseous Keten',
        journal = "J. Appl. Chem. Biotechnol.",
        volume = "22",
        pages = """491""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972BLA/DAV491:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00007002
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007002/rk00000001.xml
Bath gas: H2C=C=O
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 2,
    label = "C8H12O2 <=> C4H6O + C4H6O-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.03e+13, 's^-1'),
        n = 0,
        Ea = (202.873, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (656, 'K'),
        Tmax = (793, 'K'),
    ),
    reference = Article(
        authors = ["Vala, M.", "Baiardo, J.", "Latham, D.", "Mukherjee, R.", "Pascyz, S."],
        title = u'Fourier transform infrared kinetic study of the thermal decomposition of tetramethyl-1-3-cyclobutanedione and dimethylketene',
        journal = "J. Indian Chem. Soc.",
        volume = "63",
        pages = """16""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986VAL/BAI16:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009168
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009168/rk00000001.xml
Excitation technique: Thermal
Analytical technique: Fourier transform (FTIR)
""",
)

