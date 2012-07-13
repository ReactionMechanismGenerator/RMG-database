#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition_CCO/NIST"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    label = "1972BLA/DAV491:1",
    reactant1 = 
"""
1 *1 C 0 {2,D}
2 *2 C 0 {1,D} {3,D}
3    O 0 {2,D}
""",
    reactant2 = 
"""
1 *4 C 0 {2,D}
2 *3 C 0 {1,D} {3,D}
3    O 0 {2,D}
""",
    product1 = 
"""
1 *1 C 0 {3,S} {4,S}
2 *4 C 0 {3,S} {4,S}
3 *2 C 0 {1,S} {2,S} {5,D}
4 *3 C 0 {1,S} {2,S} {6,D}
5    O 0 {3,D}
6    O 0 {4,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (178.0,"m^3/(mol*s)"),
        n = (0.0,""),
        Ea = (73.999,"kJ/mol","+|-",0.74),
        T0 = (1.0,"K"),
        Tmin = (498.0,"K"),
        Tmax = (596.0,"K"),
        Pmin = (800.0,"Pa"),
        Pmax = (15300.0,"Pa"),
    ),
    reference = Article(
        authors = ["Blake, P.G.", "Davis, H.H."],
        title = u'Kinetics of Dimerisation of Gaseous Keten',
        journal = "J. Appl. Chem. Biotechnol.",
        volume = "22",
        pages = """491""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972BLA/DAV491:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00007002
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00007002/rk00000001.xml
Bath gas: H2C=C=O
Category: Experiment
Data type: Absolute value measured directly
Excitation technique: Thermal
Analytical technique: Vis-UV absorption
""",
    history = [('Fri Jul 13 08:21:49 2012', 'Sean Troiano <stroiano7@gmail.com>', 'action', 'Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1972BLA/DAV491:1')],
)

entry(
    index = 2,
    label = "1986VAL/BAI16:2",
    reactant1 = 
"""
1  *1 C 0 {3,S} {4,S} {7,S} {8,S}
2  *4 C 0 {5,S} {6,S} {7,S} {8,S}
3     C 0 {1,S}
4     C 0 {1,S}
5     C 0 {2,S}
6     C 0 {2,S}
7  *2 C 0 {1,S} {2,S} {9,D}
8  *3 C 0 {1,S} {2,S} {10,D}
9     O 0 {7,D}
10    O 0 {8,D}
""",
    product1 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *1 C 0 {1,S} {2,S} {4,D}
4 *2 C 0 {3,D} {5,D}
5    O 0 {4,D}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *4 C 0 {1,S} {2,S} {4,D}
4 *3 C 0 {3,D} {5,D}
5    O 0 {4,D}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.03e+13,"s^-1"),
        n = (0.0,""),
        Ea = (202.873,"kJ/mol"),
        T0 = (1.0,"K"),
        Tmin = (656.0,"K"),
        Tmax = (793.0,"K"),
    ),
    reference = Article(
        authors = ["Vala, M.", "Baiardo, J.", "Latham, D.", "Mukherjee, R.", "Pascyz, S."],
        title = u'Fourier transform infrared kinetic study of the thermal decomposition of tetramethyl-1-3-cyclobutanedione and dimethylketene',
        journal = "J. Indian Chem. Soc.",
        volume = "63",
        pages = """16""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986VAL/BAI16:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00009168
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00009168/rk00000001.xml
Category: Experiment
Data type: Absolute value measured directly
Excitation technique: Thermal
Analytical technique: Fourier transform (FTIR)
""",
    history = [('Fri Jul 13 08:21:51 2012', 'Sean Troiano <stroiano7@gmail.com>', 'action', 'Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1986VAL/BAI16:2')],
)
