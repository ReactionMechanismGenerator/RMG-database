#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition_CCO/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 588,
    label = "CCO;doublebond",
    group1 = 
"""
1 *1 Cd  0 {2,D}
2 *2 Cdd 0 {1,D} {3,D}
3    Od  0 {2,D}
""",
    group2 = "OR{mb_CCO, mb_COC}",
    kinetics = ArrheniusEP(
        A = (69200000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (43.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""Quick et al. [107]""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

