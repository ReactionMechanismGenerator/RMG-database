#!/usr/bin/env python
# encoding: utf-8

name = "HO2_Elimination_from_PeroxyRadical/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
recommended = True

entry(
    index = 1,
    reactant1 = 
"""
acetylperoxy
1 *1 C 0 {2,S} {4,S} {7,S} {8,S}
2 *2 C 0 {1,S} {3,S} {5,D}
3 *3 O 0 {2,S} {6,S}
4 *5 H 0 {1,S}
5    O 0 {2,D}
6 *4 O 1 {3,S}
7    H 0 {1,S}
8    H 0 {1,S}
""",
    product1 = 
"""
ketene
1 *1 C 0 {2,D} {4,S} {5,S}
2 *2 C 0 {1,D} {3,D}
3    O 0 {2,D}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    product2 = 
"""
HO2
1 *4 O 0 {2,S} {3,S}
2 *5 H 0 {1,S}
3 *3 O 1 {1,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2600000000.0, 's^-1', '*|/', 2.51189),
        n = 1.2,
        Ea = (34.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["J. W. Allen", "C. F. Goldsmith", "W. H. Green"],
        title = u'Automatic Estimation of Pressure-Dependent Rate Coefficients',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "???",
        pages = """???-???""",
        year = "2011 (accepted)",
    ),
    referenceType = "theory",
    shortDesc = u"""CFG VTST calculations at RQCISD(T)/CBS//B3LYP/6-311++G(d,p) level""",
    longDesc = 
u"""
Quantum chemistry calculations at the RQCISD(T)/CBS//B3LYP/6-311++G(d,p) level
using Gaussian 03 and MOLPRO. High-pressure-limit rate coefficient computed
using Variflex.
""",
    history = [
    ],
)


