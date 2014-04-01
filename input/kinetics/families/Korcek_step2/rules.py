#!/usr/bin/env python
# encoding: utf-8

name = "Korcek_step2/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "C1(R)(H)(O[OC3(OH)(R')]C2)",
    group1 = 
"""
1  *1 C 0 {2,S} {4,S} {7,S} {9,S}
2  *2 C 0 {1,S} {3,S} {11,S} {12,S}
3  *3 C 0 {2,S} {5,S} {6,S} {8,S}
4  *5 O 0 {1,S} {5,S}
5  *4 O 0 {3,S} {4,S}
6     O 0 {3,S} {10,S}
7     R 0 {1,S}
8     R 0 {3,S}
9  *6 H 0 {1,S}
10    H 0 {6,S}
11    H 0 {2,S}
12    H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (3000000000.0, 's^-1'),
        n = 1.38,
        alpha = 0,
        E0 = (34.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""CanTherm calculations using F12-QZ energies for reactants and TS. OH rotor potentials for cyclic peroxide obtained at th3 b3lyp/cbsb7 level of theory""",
    longDesc = 
u"""

""",
)

