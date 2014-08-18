#!/usr/bin/env python
# encoding: utf-8

name = "Korcek_step2/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "C1(R)(H)(O[OC3(OH)(R')]C2)",
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

