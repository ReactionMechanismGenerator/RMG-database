#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_COm/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "CH3 + CO <=> C2H3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.634e+07, 'cm^3/(mol*s)'),
        n = 1.512,
        Ea = (6.013, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Senosiain, J. P.'", "'Klippenstein, S. J.'", "'Miller, J. A.'"],
        title = 'Pathways and Rate Coefficients for the Decomposition of Vinoxy and Acetyl Radicals',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'110 (17)'",
        pages = """'5772-5781'""",
        year = "'2006'",
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
RQCISD(T)/cc-pVinfZ //UQCISD/UB3LYP
""",
)

entry(
    index = 1,
    label = "C2H3O <=> CO + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.07e+12, 's^-1'), n=0.63, Ea=(70698, 'J/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["'Senosiain, J. P.'", "'Klippenstein, S. J.'", "'Miller, J. A.'"],
        title = 'Pathways and Rate Coefficients for the Decomposition of Vinoxy and Acetyl Radicals',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'110 (17)'",
        pages = """'5772-5781'""",
        year = "'2006'",
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
RQCISD(T)/cc-pVinfZ //UQCISD/UB3LYP
""",
)

entry(
    index = 2,
    label = "C3H5O <=> CO + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.417e+12, 's^-1'), n=0.428, Ea=(15.009, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["'Zador, J.'", "'Miller, J. A.'"],
        title = 'Adventures on the C3H5O potential energy surface: OH + propyne, OH + allene and related reactions',
        journal = "'Proceedings of the Combustion Institute'",
        volume = "'35 (1)'",
        pages = """'181-188'""",
        year = "'2015'",
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
UCCSD(T)-F12b/cc-pVQZ-F12//M06-2X/6-311++G(d,p)
""",
)

entry(
    index = 3,
    label = "C5H5O + CO <=> C6H5O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (14420, 'cm^3/(mol*s)'),
        n = 2.333,
        Ea = (18.929, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'I. V. Tokmakov'", "'G. Kim'", "'V. V. Kislov'", "'A. M. Mebel'", "'M. C. Lin'"],
        title = 'The Reaction of Phenyl Radical with Molecular Oxygen: A G2M Study of the Potential Energy Surface',
        journal = "'J. Phys. Chem. A'",
        volume = "'109 (27)'",
        pages = """'6114-6127'""",
        year = "'2005'",
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
Using CanTherm to calculate TST rates from the PES at the G2M(MP2)//B3LYP/6-311++G** level of theory
The rates have been validated by the rates reported in Proceedings of the Combustion Institute 35 (2015) 1861–1869,
where only 1500, 2000, 2500 K rates were reported.
""",
)

