#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionCS_isomerization/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index        = 1,
    label        = "XSYJ;C;YJ",
    group1 = "OR{XSR3J, XSR4J, XSR5J, XSR6J, XSR7J}",
    group2 = "OR{C-RRR, Cds-R, Ct}",
    group3 = "OR{CJ, SJ, CJ-3, SJ-3}",
    kinetics = ArrheniusEP(
        A = (1000000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (50, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index        = 2,
    label        = "XSR3J_S;C-HHH;CsJ-3-SsHH",
    group1 = 
"""
1 *3 R!H U1 {2,S}
2 *2 Ss  U0 {1,S} {3,S}
3 *1 C   U0 {2,S}
""",
    group2 = 
"""
1 *1 C U0 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    H U0 {1,S}
4    H U0 {1,S}
""",
    group3 = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *2 Ss U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1030000000.0, 's^-1'),
        n = 1.057,
        alpha = 0,
        E0 = (45.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index        = 3,
    label        = "XSR4J_SS;C-HHH;CsJ-CsHH",
    group1 = 
"""
1 *3 R!H U1 {2,S}
2 *4 R!H U0 {1,S} {3,S}
3 *2 Ss  U0 {2,S} {4,S}
4 *1 C   U0 {3,S}
""",
    group2 = 
"""
1 *1 C U0 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    H U0 {1,S}
4    H U0 {1,S}
""",
    group3 = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Cs U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (67600000000.0, 's^-1'),
        n = 0.394,
        alpha = 0,
        E0 = (45.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index        = 4,
    label        = "XSR4J_SS;C-HHH;CsJ-SsHH",
    group1 = 
"""
1 *3 R!H U1 {2,S}
2 *4 R!H U0 {1,S} {3,S}
3 *2 Ss  U0 {2,S} {4,S}
4 *1 C   U0 {3,S}
""",
    group2 = 
"""
1 *1 C U0 {2,S} {3,S} {4,S}
2    H U0 {1,S}
3    H U0 {1,S}
4    H U0 {1,S}
""",
    group3 = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Ss U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (151000000000.0, 's^-1'),
        n = 0.327,
        alpha = 0,
        E0 = (55.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

