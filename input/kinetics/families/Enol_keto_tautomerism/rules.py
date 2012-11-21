#!/usr/bin/env python
# encoding: utf-8

name = "Enol_keto_tautomerism/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 1,
    label = "enol;ene",
    group1 = 
"""
1 *2 {Cd,Cdd} {0,1,2} {2,D}
2 *3 Cd       {0,1}   {1,D} {3,S}
3 *4 Os       0       {2,S} {4,S}
4 *1 H        0       {3,S}
""",
    group2 = 
"""
1 *2 {Cd,Cdd} {0,1,2} {2,D}
2 *3 Cd       {0,1}   {1,D}
""",
    kinetics = ArrheniusEP(
        A = (8.590e11,"s^-1"),
        n = 0.32,
        alpha = 0,
        E0 = (55.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""default""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov  1 13:04:03 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen added this entry to the database."""),
    ],
)
