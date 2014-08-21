#!/usr/bin/env python
# encoding: utf-8

name = "Cyclic_Ether_Formation/NIST"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "C5H11O2 <=> C5H10O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11, 's^-1'),
        n = 0,
        Ea = (73.001, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (653, 'K'),
        Tmax = (793, 'K'),
        Pmin = (66700, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Baldwin, R.R.", "Hisham, M.W.M.", "Walker, R.W."],
        title = u'Arrhenius parameters of elementary reactions involved in the oxidation of neopentane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "78",
        pages = """1615""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982BAL/HIS1615:8",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00016872
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016872/rk00000002.xml
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 2,
    label = "C5H11O2 <=> C5H10O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.05e+35, 's^-1'),
        n = -7.46,
        Ea = (100.362, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (900, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Sun, H.", "Bozzelli, J.W."],
        title = u'Thermochemical and kinetic analysis on the reactions of neopentyl and hydroperoxy-neopentyl radicals with oxygen: Part I.  OH and initial stable HC product formation',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """1694-1711""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004SUN/BOZ1694-1711:23",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00016872

Quantum calculations of energetics of pathways related to reaction between neopentyl radical and O2 (and subsequent reaction pathways). This includes primary reaction pathways as well as subsequent secondary reactions. Used ab initio CBS-Q method, as well as B3LYP/6-31G(d,p) for some molecules. Many reaction channels are discussed in paper, for some, rate expressions are provided at low pressure limit, high pressure limit, and a number of intermediate pressures. For some reaction channels, no rate expressions are given in paper, but are provided in auxillary information associated with the article in JPC.

Rate expressions reported are derived from ab initio transition states using QRRK analysis of the chemically activated reaction pathways. We have only abstracted rate expressions from the paper for 1 atm and 300-900 K. For other pressures and at higher temperatures see paper.
""",
)

entry(
    index = 3,
    label = "C5H11O2 <=> C5H10O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.78e+17, 's^-1'),
        n = -2.45,
        Ea = (48.103, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (900, 'K'),
        Tmax = (2500, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Sun, H.", "Bozzelli, J.W."],
        title = u'Thermochemical and kinetic analysis on the reactions of neopentyl and hydroperoxy-neopentyl radicals with oxygen: Part I.  OH and initial stable HC product formation',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """1694-1711""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004SUN/BOZ1694-1711:24",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00016872

Quantum calculations of energetics of pathways related to reaction between neopentyl radical and O2 (and subsequent reaction pathways). This includes primary reaction pathways as well as subsequent secondary reactions. Used ab initio CBS-Q method, as well as B3LYP/6-31G(d,p) for some molecules. Many reaction channels are discussed in paper, for some, rate expressions are provided at low pressure limit, high pressure limit, and a number of intermediate pressures. For some reaction channels, no rate expressions are given in paper, but are provided in auxillary information associated with the article in JPC.

Rate expressions reported are derived from ab initio transition states using QRRK analysis of the chemically activated reaction pathways. We have only abstracted rate expressions from the paper for 1 atm and 300-900 K. For other pressures and at higher temperatures see paper.
""",
)

