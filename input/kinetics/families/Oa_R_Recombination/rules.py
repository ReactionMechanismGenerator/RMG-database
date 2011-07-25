#!/usr/bin/env python
# encoding: utf-8

name = "Oa_R_Recombination/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1000,
    label = "Y_rad;Oa",
    group1 = 
"""
1  *1 R 1
""",
    group2 = 
"""
1  *2 O 2T
""",
    kinetics = ArrheniusEP(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

