#!/usr/bin/env python
# encoding: utf-8

name = "Silylene_Insertion/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "SiH2 + H2 <=> SiH4",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.74E-18, 'cm^3/(mol*s)'),
        n = 1.97,
        Ea = (-1.9, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (400, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ["Walch, S.P.", "Dateo, C.E."],
        title = "Thermal decomposition pathways and rates for silane, chlorosilane, dichlorosilane, and trichlorosilane",
        journal = "J. Phys. Chem. A",
        pages = """2015-2022""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001WAL/DAT2015-2022:2",
    ),
    longDesc = 
u"""
Calculations using CASSCF/cc-pVDZ for geometries and vibrational frequencies. Energies of reactats, products and TS computed with CCSD(T)/aug-cc-pVTZ extrapolated to complete basis set using MP2/aug-cc-pVnZ(n=2,3,4). Rate founded with conventional TST. Error in barrier at most 2 kcal/mol, likely about 1 kcal/mol.
""",
)


