#!/usr/bin/env python
# encoding: utf-8

name = "intra_H_migration/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index        = 1,
    reactant1 = 
"""
multiplicity 2
1    O U0 L2 E0  {5,D}
2 *2 C U0 L0 E0  {3,S} {5,S} {7,S} {8,S}
3 *3 H U0 L0 E0  {2,S}
4 *4 O U0 L2 E0  {5,S} {6,S}
5 *5 C U0 L0 E0  {1,D} {2,S} {4,S}
6 *1 O U1 L2 E0  {4,S}
7    H U0 L0 E0  {2,S}
8    H U0 L0 E0  {2,S}
""",
    product1 = 
"""
multiplicity 2
1 *4 C U0 L0 E0  {2,S} {3,S} {5,D}
2 *1 C U1 L0 E0  {1,S} {7,S} {8,S}
3 *5 O U0 L2 E0  {1,S} {4,S}
4 *2 O U0 L2 E0  {3,S} {6,S}
5    O U0 L2 E0  {1,D}
6 *3 H U0 L0 E0  {4,S}
7    H U0 L0 E0  {2,S}
8    H U0 L0 E0  {2,S}
""",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2300000000.0, 's^-1', '*|/', 2.51189),
        n = 0.75,
        Ea = (23.2, 'kcal/mol'),
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
)

