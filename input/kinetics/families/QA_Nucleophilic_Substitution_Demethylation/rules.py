#!/usr/bin/env python
# encoding: utf-8

name = "QA_Nucleophilic_Substitution_Demethylation"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 0,
    label = "R-CH2-(N)R2-CH3",
    kinetics = ArrheniusEP(
        A = (100000, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = 
u"""

""",
)