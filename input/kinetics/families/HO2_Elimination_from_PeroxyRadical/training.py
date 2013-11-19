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
1 *1 C 0 {2,S} {4,S}
2 *2 C 0 {1,S} {3,S} {5,D}
3 *3 O 0 {2,S} {6,S}
4 *5 H 0 {1,S}
5    O 0 {2,D}
6 *4 O 1 {3,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D}
2 *2 C 0 {1,D} {3,D}
3    O 0 {2,D}
""",
    product2 = 
"""
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

entry(
    index = 2,
    reactant1 = 
"""
1 C 0 {2,S} {3,S}
2 C 0 {1,S} {4,S}
3 C 0 {1,S} {5,S} {6,S}
4 C 0 {2,S}
5 O 0 {3,S}
6 O 0 {3,S} {7,S}
7 O 1 {6,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *2 C 0 {2,S} {5,D}
5 *1 O 0 {4,D}
""",
    product2 = 
"""
1 *4 O 0 {2,S} {3,S}
2 *3 O 1 {1,S}
3 *5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2900000000.0, 's^-1'),
        n = 0.843,
        Ea = (10.653, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""CBS-QB3 w/ 1d-HR""",
    longDesc = 
u"""
Reference: Low-Temperature Combustion Chemistry of n-Butanol: Principal Oxidation Pathways of Hydroxybutyl Radicals 
DOI: 10.1021/jp403792t
""",
    history = [
        ("Tue Nov 19 12:46:54 2013","Connie Gao <connieg@mit.edu>","action","""New entry. Updated rate rule for CCCC(O[O])O = CCCC=O + HO2"""),
    ],
)

entry(
    index = 3,
    reactant1 = 
"""
1 C 0 {2,S} {3,S}
2 C 0 {1,S} {4,S}
3 C 0 {1,S} {5,S} {6,S}
4 C 0 {2,S}
5 O 0 {3,S}
6 O 0 {3,S} {7,S}
7 O 1 {6,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *1 C 0 {1,S} {4,D}
4 *2 C 0 {3,D} {5,S}
5    O 0 {4,S}
""",
    product2 = 
"""
1 *4 O 0 {2,S} {3,S}
2 *3 O 1 {1,S}
3 *5 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(A=(72900000.0, 's^-1'), n=1.408, Ea=(30.456, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""CBS-QB3 w/ 1d-HR""",
    longDesc = 
u"""
Reference: Low-Temperature Combustion Chemistry of n-Butanol: Principal Oxidation Pathways of Hydroxybutyl Radicals 
DOI: 10.1021/jp403792t
""",
    history = [
        ("Tue Nov 19 13:08:18 2013","Connie Gao <connieg@mit.edu>","action","""New entry. Updated rate rule for CCCC(O[O])O = CCC=CO + HO2"""),
    ],
)

