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
1   C 0 0 {2,S} {4,S} {5,S} {6,S}
2   O 0 2 {1,S} {3,S}
3   O 1 2 {2,S}
4   H 0 0 {1,S}
5   H 0 0 {1,S}
6   H 0 0 {1,S}
""",
    product1 = 
"""
1 * O 1 2 {2,S}
2   O 1 2 {1,S}
""",
    product2 = 
"""
1 * C 1 0 {2,S} {3,S} {4,S}
2   H 0 0 {1,S}
3   H 0 0 {1,S}
4   H 0 0 {1,S}
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
1   C 0 0 {2,S} {3,S} {5,S} {6,S}
2   C 0 0 {1,S} {7,S} {8,S} {9,S}
3   O 0 2 {1,S} {4,S}
4   O 1 2 {3,S}
5   H 0 0 {1,S}
6   H 0 0 {1,S}
7   H 0 0 {2,S}
8   H 0 0 {2,S}
9   H 0 0 {2,S}
""",
    product1 = 
"""
1 * O 1 2 {2,S}
2   O 1 2 {1,S}
""",
    product2 = 
"""
1   C 0 0 {2,S} {3,S} {4,S} {5,S}
2 * C 1 0 {1,S} {6,S} {7,S}
3   H 0 0 {1,S}
4   H 0 0 {1,S}
5   H 0 0 {1,S}
6   H 0 0 {2,S}
7   H 0 0 {2,S}
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
1   C 0 0 {3,S} {4,S} {6,S} {7,S}
2   C 0 0 {4,S} {8,S} {9,S} {10,S}
3   O 0 2 {1,S} {5,S}
4   C 0 0 {1,S} {2,S} {11,S} {12,S}
5   O 1 2 {3,S}
6   H 0 0 {1,S}
7   H 0 0 {1,S}
8   H 0 0 {2,S}
9   H 0 0 {2,S}
10  H 0 0 {2,S}
11  H 0 0 {4,S}
12  H 0 0 {4,S}
""",
    product1 = 
"""
1 * O 1 2 {2,S}
2   O 1 2 {1,S}
""",
    product2 = 
"""
1   C 0 0 {2,S} {3,S} {4,S} {5,S}
2   C 0 0 {1,S} {6,S} {7,S} {8,S}
3 * C 1 0 {1,S} {9,S} {10,S}
4   H 0 0 {1,S}
5   H 0 0 {1,S}
6   H 0 0 {2,S}
7   H 0 0 {2,S}
8   H 0 0 {2,S}
9   H 0 0 {3,S}
10  H 0 0 {3,S}
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
1   C 0 0 {2,S} {3,S}
2   C 0 0 {1,S} {4,S}
3   C 0 0 {1,S}
4 * C 1 0 {2,S} {5,S}
5   O 0 2 {4,S}
""",
    reactant2 = 
"""
1 * O 1 2 {2,S}
2   O 1 2 {1,S}
""",
    product1 = 
"""
1 C 0 0 {2,S} {3,S}
2 C 0 0 {1,S} {4,S}
3 C 0 0 {1,S} {5,S} {6,S}
4 C 0 0 {2,S}
5 O 0 0 {3,S}
6 O 0 0 {3,S} {7,S}
7 O 1 0 {6,S}
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

entry(
    index = 5,
    label = "1988BOR/COB4377-4384:1",
    reactant1 = 
"""
1 * N 1 0 {2,S} {3,D}
2   O 0 3 {1,S}
3   O 0 2 {1,D}
""",
    reactant2 = 
"""
NO2
1 * N 1 0 {2,D} {3,S}
2   O 0 2 {1,D}
3   O 0 3 {1,S}
""",
    product1 = 
"""
NO2NO2
1 N 0 0 {2,S} {3,S} {4,D}
2 N 0 0 {1,S} {5,D} {6,S}
3 O 0 3 {1,S}
4 O 0 2 {1,D}
5 O 0 2 {2,D}
6 O 0 3 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (263000000.0, 'm^3/(mol*s)', '+|-', 31600000.0),
        n = -1.1,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (600, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (20900000.0, 'Pa'),
    ),
    reference = Article(
        authors = ["Borrell, P.", "Cobos, C.J.", "Luther, K."],
        title = u'Falloff curve and specific rate constants for the reaction NO2 + NO2 N2O4',
        journal = "J. Phys. Chem.",
        volume = "92",
        pages = """4377-4384""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988BOR/COB4377-4384:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
Bath gas: N2
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Vis-UV absorption
""",
    history = [
        ("Wed Dec 18 10:24:30 2013","Beat Buesser <bbuesser@mit.edu>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988BOR/COB4377-4384:1"""),
    ],
)

entry(
    index = 6,
    label = "1962ASH/BUR253:5",
    reactant1 = 
"""
1 * N 1 1 {2,D}
2   O 0 2 {1,D}
""",
    reactant2 = 
"""
1 * O 1 2 {2,S}
2   O 1 2 {1,S}
""",
    product1 = 
"""
1 N 0 1 {2,S} {3,D}
2 O 0 2 {1,S} {4,S}
3 O 0 2 {1,D}
4 O 1 2 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (117000, 'm^3/(mol*s)', '*|/', -1),
        n = 0,
        Ea = (13.386, 'kJ/mol', '+|-', -0.001),
        T0 = (1, 'K'),
        Tmin = (473, 'K'),
        Tmax = (703, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (33600, 'Pa'),
    ),
    reference = Article(
        authors = ["Ashmore, P.G.", "Burnett, M.G."],
        title = u'Concurrent molecular and free radical mechanisms in the thermal decomposition of nitrogen dioxide',
        journal = "J. Chem. Soc. Faraday Trans. 2",
        volume = "58",
        pages = """253""",
        year = "1962",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962ASH/BUR253:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
Uncertainty: 3.0
Bath gas: NO2
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
    history = [
        ("Wed Dec 18 12:01:41 2013","Beat Buesser <bbuesser@mit.edu>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1962ASH/BUR253:5"""),
    ],
)

entry(
    index = 7,
    label = "2000HAH/LUT5098-5104:4",
    reactant1 = 
"""
1 * N 1 0 {2,D} {3,S}
2   O 0 2 {1,D}
3   O 0 3 {1,S}
""",
    reactant2 = 
"""
1   N 0 0 {2,D} {3,S} {4,S}
2   O 0 2 {1,D}
3 * O 1 2 {1,S}
4   O 0 3 {1,S}
""",
    product1 = 
"""
1 N 0 0 {3,S} {4,D} {5,S}
2 N 0 0 {3,S} {6,D} {7,S}
3 O 0 2 {1,S} {2,S}
4 O 0 2 {1,D}
5 O 0 3 {1,S}
6 O 0 2 {2,D}
7 O 0 3 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (366000, 'm^3/(mol*s)', '+|-', 57700),
        n = 0.2,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (400, 'K'),
        Pmin = (100000, 'Pa'),
        Pmax = (90000000.0, 'Pa'),
    ),
    reference = Article(
        authors = ["Hahn, J.", "Luther, K.", "Troe, J."],
        title = u'Experimental and Theoretical Study of the Temperature and Pressure Dependences of the Recombination Reactions O+NO2(+M)\u2192\x92NO3(+M) and NO2+NO3(+M)\u2192\x92N-2O5(+M)',
        journal = "Phys. Chem. Chem. Phys.",
        pages = """5098-5104""",
        year = "2000",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2000HAH/LUT5098-5104:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
Pressure dependence: Rate constant is high pressure limit
Experimental procedure: Static or low flow - Data taken vs time
Excitation technique: Flash photolysis (laser or conventional)
Time resolution: In real time
Analytical technique: Vis-UV absorption

Theoretical modeling of k0, k∞ and Fc=0.38 exp(-T/4900K) led to consistency with the experimental data.
""",
    history = [
        ("Wed Dec 18 14:36:16 2013","Beat Buesser <bbuesser@mit.edu>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2000HAH/LUT5098-5104:4"""),
    ],
)

entry(
    index = 8,
    label = "2007WIL/POG154321:2",
    reactant1 = 
"""
1 * N 1 0 {2,D} {3,S}
2   O 0 2 {1,D}
3   O 0 3 {1,S}
""",
    reactant2 = 
"""
1 * O 1 2 {2,S}
2   H 0 0 {1,S}
""",
    product1 = 
"""
1 N 0 0 {2,S} {3,D} {4,S}
2 O 0 2 {1,S} {5,S}
3 O 0 2 {1,D}
4 O 0 3 {1,S}
5 H 0 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24100000.0, 'm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (400, 'K'),
    ),
    reference = Article(
        authors = ["Williams, C.F.", "Pogrebnya, S.K.", "Clary, D.C."],
        title = u'Quantum study on the branching ratio of the reaction NO2+OH',
        journal = "J. Chem. Phys.",
        volume = "126",
        pages = """154321""",
        year = "2007",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2007WIL/POG154321:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Other theoretical""",
    longDesc = 
u"""
Pressure dependence: Rate constant is high pressure limit

Quantum dynamics calculations. Reaction potential energy suraface was studied using quantum chemistry.
""",
    history = [
        ("Fri Dec 20 17:45:27 2013","Beat Buesser <bbuesser@mit.edu>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2007WIL/POG154321:2"""),
    ],
)

entry(
    index = 9,
    label = "2007WIL/POG154321:4",
    reactant1 = 
"""
1   N 0 1 {2,D} {3,S}
2   O 0 2 {1,D}
3 * O 1 2 {1,S}
""",
    reactant2 = 
"""
1 * O 1 2 {2,S}
2   H 0 0 {1,S}
""",
    product1 = 
"""
1 N 0 0 {2,S} {3,D} {4,S}
2 O 0 2 {1,S} {5,S}
3 O 0 2 {1,D}
4 O 0 3 {1,S}
5 H 0 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1205000.0, 'm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (400, 'K'),
    ),
    reference = Article(
        authors = ["Williams, C.F.", "Pogrebnya, S.K.", "Clary, D.C."],
        title = u'Quantum study on the branching ratio of the reaction NO2+OH',
        journal = "J. Chem. Phys.",
        volume = "126",
        pages = """154321""",
        year = "2007",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2007WIL/POG154321:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Other theoretical""",
    longDesc = 
u"""
Pressure dependence: Rate constant is high pressure limit
Reference reaction: 2007WIL/POG154321:4
Branching ration: 0.05
Quantum dynamics calculations. Reaction potential energy suraface was studied using quantum chemistry.
""",
    history = [
        ("Fri Dec 20 17:45:27 2013","Beat Buesser <bbuesser@mit.edu>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2007WIL/POG154321:2"""),
    ],
)

