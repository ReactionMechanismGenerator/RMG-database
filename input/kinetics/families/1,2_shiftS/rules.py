#!/usr/bin/env python
# encoding: utf-8

name = "1,2_shiftS/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 1,
    label = "XSYJ;YJ-Ss;X-Ss",
    group1 = 
"""
1 *1 C   0 {3,S}
2 *2 S   1 {3,S}
3 *3 R!H 0 {1,S} {2,S}
""",
    group2 = 
"""
1 *3 R!H 1
""",
    group3 = "OR{C-Ss}",
    kinetics = ArrheniusEP(
        A = (100000000.0, 's^-1'),
        n = 2,
        alpha = 0,
        E0 = (40, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 1,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

