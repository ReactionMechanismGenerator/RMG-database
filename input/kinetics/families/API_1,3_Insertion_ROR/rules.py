#!/usr/bin/env python
# encoding: utf-8

name = "API_1,3_Insertion_ROR/rules"
shortDesc = u""
longDesc = u"""
561 - 570 Some of the tortional motions in the alkyl part of the 

transition states are treated as free rotations as they are relatively loose TSs.
"""
entry(
    index = 560,
    label = "doublebond;R_OR",
    kinetics = ArrheniusEP(
        A = (100, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)

entry(
    index = 712,
    label = "doublebond;R_OH",
    kinetics = ArrheniusEP(
        A = (1e-05, 'cm^3/(mol*s)'),
        n = 4,
        alpha = 0,
        E0 = (80, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)

