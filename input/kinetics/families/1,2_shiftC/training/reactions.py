#!/usr/bin/env python
# encoding: utf-8

name = "1,2_shiftC/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C7H9 <=> C7H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.53e+06, 's^-1'), n=1.73, Ea=(58.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product7 <=> product18
""",
)

entry(
    index = 1,
    label = "C7H9-3 <=> C7H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.59e+09, 's^-1'), n=0.99, Ea=(43.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product31 <=> product32
""",
)

entry(
    index = 2,
    label = "C7H9-5 <=> C7H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.33e+08, 's^-1'), n=1.36, Ea=(37.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product18 <=> product7
""",
)

entry(
    index = 3,
    label = "C7H9-7 <=> C7H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.745e+09, 's^-1'), n=1.06, Ea=(49.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product32 <=> product31
""",
)

entry(
    index = 4,
    label = "C6H5O2 <=> C6H5O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.889e+11, 's^-1'), n=0.232, Ea=(29.338, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['I. V. Tokmakov', 'G. Kim', 'V. V. Kislov', 'A. M. Mebel', 'M. C. Lin'],
        title = 'The Reaction of Phenyl Radical with Molecular Oxygen: A G2M Study of the Potential Energy Surface',
        journal = 'J. Phys. Chem. A',
        volume = '109 (27)',
        pages = '6114-6127',
        year = '2005',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Using CanTherm to calculate TST rates from the PES at the G2M(MP2)//B3LYP/6-311++G** level of theory
The rates have been validated by the rates reported in Proceedings of the Combustion Institute 35 (2015) 1861–1869,
where only 1500, 2000, 2500 K rates were reported.
""",
)


entry(
    index = 5,
    label = "C7H5 <=> C7H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.66e+11, 's^-1'), n=0.438, Ea=(22.58, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Gabriel da Silva', 'Adam J. Trevittb'],
        title = 'Chemically activated reactions on the C7H5 energy surface: propargyl+diacetylene, i-C5H3+acetylene, and n-C5H3+acetylene',
        journal = 'Phys. Chem. Chem. Phys.',
        volume = '13 (19)',
        pages = '8940-8952',
        year = '2011',
    ),
    referenceType = "theory",   
    rank = 5,
    longDesc = 
u"""
All species reported here are studied using the G3SX composite theoretical methodology. This method uses B3LYP/6-31G(2df,p) optimized geometries, vibrational
frequencies and scaled zero point energies, with higher-level wavefunction theory calculations for accurate energies (along with empirical scaling corrections).
1D-Hinder rotor is considered.
""",
)

entry(
    index = 6,
    label = "C7H5-2 <=> C7H5",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(7.13e+12, 's^-1'), n=0.254, Ea=(68.75, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Gabriel da Silva', 'Adam J. Trevittb'],
        title = 'Chemically activated reactions on the C7H5 energy surface: propargyl+diacetylene, i-C5H3+acetylene, and n-C5H3+acetylene',
        journal = 'Phys. Chem. Chem. Phys.',
        volume = '13 (19)',
        pages = '8940-8952',
        year = '2011',
    ),
    referenceType = "theory",   
    rank = 5,
    longDesc = 
u"""
All species reported here are studied using the G3SX composite theoretical methodology. This method uses B3LYP/6-31G(2df,p) optimized geometries, vibrational
frequencies and scaled zero point energies, with higher-level wavefunction theory calculations for accurate energies (along with empirical scaling corrections).
1D-Hinder rotor is considered.
""",
)

