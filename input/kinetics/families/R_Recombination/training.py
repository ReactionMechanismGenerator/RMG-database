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
1   C 0 {2,S} {4,S} {5,S} {6,S}
2   O 0 {1,S} {3,S}
3   O 1 {2,S}
4   H 0 {1,S}
5   H 0 {1,S}
6   H 0 {1,S}
""",
    product1 = 
"""
1 * O 1 {2,S}
2   O 1 {1,S}
""",
    product2 = 
"""
1 * C 1 {2,S} {3,S} {4,S}
2   H 0 {1,S}
3   H 0 {1,S}
4   H 0 {1,S}
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
1   C 0 {2,S} {3,S} {5,S} {6,S}
2   C 0 {1,S} {7,S} {8,S} {9,S}
3   O 0 {1,S} {4,S}
4   O 1 {3,S}
5   H 0 {1,S}
6   H 0 {1,S}
7   H 0 {2,S}
8   H 0 {2,S}
9   H 0 {2,S}
""",
    product1 = 
"""
1 * O 1 {2,S}
2   O 1 {1,S}
""",
    product2 = 
"""
1   C 0 {2,S} {3,S} {4,S} {5,S}
2 * C 1 {1,S} {6,S} {7,S}
3   H 0 {1,S}
4   H 0 {1,S}
5   H 0 {1,S}
6   H 0 {2,S}
7   H 0 {2,S}
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

entry(
    index = 3,
    reactant1 = 
"""
1   C 0 {3,S} {4,S} {6,S} {7,S}
2   C 0 {4,S} {8,S} {9,S} {10,S}
3   O 0 {1,S} {5,S}
4   C 0 {1,S} {2,S} {11,S} {12,S}
5   O 1 {3,S}
6   H 0 {1,S}
7   H 0 {1,S}
8   H 0 {2,S}
9   H 0 {2,S}
10  H 0 {2,S}
11  H 0 {4,S}
12  H 0 {4,S}
""",
    product1 = 
"""
1 * O 1 {2,S}
2   O 1 {1,S}
""",
    product2 = 
"""
1   C 0 {2,S} {3,S} {4,S} {5,S}
2   C 0 {1,S} {6,S} {7,S} {8,S}
3 * C 1 {1,S} {9,S} {10,S}
4   H 0 {1,S}
5   H 0 {1,S}
6   H 0 {2,S}
7   H 0 {2,S}
8   H 0 {2,S}
9   H 0 {3,S}
10  H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.52e+23, 's^-1'), n=-2.71, Ea=(36.4, 'kcal/mol'), T0=(1, 'K')),
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
        ("Sun Sep 22 11:59:44 2013","Shamel Merchant <shamel@mit.edu>","action","""New entry. Rate rule for CCCO[O] = C[CH2] + O2"""),
    ],
)



entry(
    index = 4,
    reactant1 = 
"""
1   C 0 {2,S} {3,S}
2   C 0 {1,S} {4,S}
3   C 0 {1,S}
4 * C 1 {2,S} {5,S}
5   O 0 {4,S}
""",
    reactant2 = 
"""
1 * O 1 {2,S}
2   O 1 {1,S}
""",
    product1 = 
"""
1 C 0 {2,S} {3,S}
2 C 0 {1,S} {4,S}
3 C 0 {1,S} {5,S} {6,S}
4 C 0 {2,S}
5 O 0 {3,S}
6 O 0 {3,S} {7,S}
7 O 1 {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8360000000000.0, 'cm^3/(mol*s)'),
        n = -0.085,
        Ea = (-567.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""CBS-QB3 w/ 1-d HR""",
    longDesc = 
u"""
Reference: Low-Temperature Combustion Chemistry of n-Butanol: Principal Oxidation Pathways of Hydroxybutyl Radicals 
DOI: 10.1021/jp403792t
""",
    history = [
        ("Mon Nov 18 15:16:03 2013","Connie Gao <connieg@mit.edu>","action","""New entry. Updated rate rule for CCC[C]O + O2 = CCCC(O[O])O"""),
        ("Tue Nov 19 13:18:37 2013","Connie Gao <connieg@mit.edu>","action","""Updated rate with atom starring in forward direction for CCC[C]O + O2 = CCCC(O[O])O"""),
    ],
)

