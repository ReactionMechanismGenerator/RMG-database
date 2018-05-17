#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_COm/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "CH3 + CO <=> C2H3O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.634e+07, 'cm^3/(mol*s)'),
        n = 1.512,
        Ea = (6.013, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ['Senosiain, J. P.', 'Klippenstein, S. J.', 'Miller, J. A.'],
        title = u'Pathways and Rate Coefficients for the Decomposition of Vinoxy and Acetyl Radicals',
        journal = 'The Journal of Physical Chemistry A',
        volume = '110 (17)',
        pages = '5772-5781',
        year = '2006',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
RQCISD(T)/cc-pV∞Z //UQCISD/UB3LYP
""",
)

entry(
    index = 2,
    label = "C2H3O <=> CO + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.07e+12, 's^-1'), n=0.63, Ea=(70698, 'J/mol'), T0=(1, 'K')),
    rank = 3,
    reference = Article(
        authors = ['Senosiain, J. P.', 'Klippenstein, S. J.', 'Miller, J. A.'],
        title = u'Pathways and Rate Coefficients for the Decomposition of Vinoxy and Acetyl Radicals',
        journal = 'The Journal of Physical Chemistry A',
        volume = '110 (17)',
        pages = '5772-5781',
        year = '2006',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
RQCISD(T)/cc-pV∞Z //UQCISD/UB3LYP
""",
)

entry(
    index = 3,
    label = "C3H5O <=> CO + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.417e+12, 's^-1'), n=0.428, Ea=(15.009, 'kcal/mol'), T0=(1, 'K')),
    rank = 2,
    reference = Article(
        authors = ['Zádor, J.', 'Miller, J. A.'],
        title = u'Adventures on the C3H5O potential energy surface: OH + propyne, OH + allene and related reactions',
        journal = 'Proceedings of the Combustion Institute',
        volume = '35 (1)',
        pages = '181-188',
        year = '2015',
    ),
    referenceType = 'theory',
    shortDesc = u"""""",
    longDesc = 
u"""
UCCSD(T)-F12b/cc-pVQZ-F12//M06-2X/6-311++G(d,p)
""",
)

