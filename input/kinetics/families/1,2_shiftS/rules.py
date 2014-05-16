#!/usr/bin/env python
# encoding: utf-8

name = "1,2_shiftS/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index        = 1,
    label        = "XSYJ;YJ-Ss;X-Ss",
    group1 = 
"""
1 *1 C   U0 {3,S}
2 *2 S   U1 {3,S}
3 *3 R!H U0 {1,S} {2,S}
""",
    group2 = 
"""
1 *3 R!H U1
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
    rank = 1,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
u"""

""",
)

