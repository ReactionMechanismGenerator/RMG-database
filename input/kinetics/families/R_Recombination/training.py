#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/training"
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
1   C 0 {2,S}
2   O 0 {1,S} {3,S}
3 * O 1 {2,S}
""",
    product1 = 
"""
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product2 = 
"""
1 C 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (109000000000000.0, 's^-1'),
        n = 0.25,
        Ea = (33.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "Quantum Calculation",
    shortDesc = u"""Method CBS-QB3 w/ 1-d Hindered rotor corrections""",
    longDesc = 
u"""
High-Pressure Rate Rules for Alkyl + O2 Reactions. 1. The Dissociation, Concerted Elimination, and Isomerization Channels of the Alkyl Peroxy Radical
Stephanie M. Villano, Lam K. Huynh, Hans-Heinrich Carstensen, and Anthony M. Dean
The Journal of Physical Chemistry A 2011 115 (46), 13425-13442
dx.doi.org/10.1021/jp2079204

Method CBS-QB3 w/ 1-d Hindered rotor corrections
""",
    history = [
        ("Sun Sep 22 11:35:10 2013","Shamel Merchant <shamel@mit.edu>","action","""New entry. Rate rule for CO[O] = [CH3] + O2"""),
    ],
)

entry(
    index = 2,
    reactant1 = 
"""
1   C 0 {3,S}
2   O 0 {3,S} {4,S}
3   C 0 {1,S} {2,S}
4 * O 1 {2,S}
""",
    product1 = 
"""
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product2 = 
"""
1 C 0 {2,S}
2 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.49e+21, 's^-1'), n=-2.41, Ea=(35.8, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "Quantum Calculation",
    shortDesc = u"""Method CBS-QB3 w/ 1-d Hindered rotor corrections""",
    longDesc = 
u"""
High-Pressure Rate Rules for Alkyl + O2 Reactions. 1. The Dissociation, Concerted Elimination, and Isomerization Channels of the Alkyl Peroxy Radical
Stephanie M. Villano, Lam K. Huynh, Hans-Heinrich Carstensen, and Anthony M. Dean
The Journal of Physical Chemistry A 2011 115 (46), 13425-13442
dx.doi.org/10.1021/jp2079204

Method CBS-QB3 w/ 1-d Hindered rotor corrections
""",
    history = [
        ("Sun Sep 22 11:45:54 2013","Shamel Merchant <shamel@mit.edu>","action","""New entry. Rate rule for CCO[O] = C[CH2] + O2"""),
    ],
)

