#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionS_isomerization/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index        = 1,
    label        = "XSYJ;YJ;S-RR",
    group1 = "OR{XSR3J, XSR4J, XSR5J, XSR6J, XSR7J}",
    group2 = "OR{CJ, SJ, CJ-3, SJ-3}",
    group3 = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    R  U0 {1,S}
3 *2 R  U0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1000000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (20, 'kcal/mol'),
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
    label        = "XSR3J_S;CsJ-3-SsHH;S-Cs(HHH)Ss",
    group1 = 
"""
1 *3 R!H U1 {2,S}
2 *2 R!H U0 {1,S} {3,S}
3 *1 Ss  U0 {2,S} {4,S}
4    R   U0 {3,S}
""",
    group2 = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *2 Ss U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
""",
    group3 = 
"""
1 *1 Ss U0 {2,S} {3,S}
2 *2 Ss U0 {1,S}
3    Cs U0 {1,S} {4,S} {5,S} {6,S}
4    H  U0 {3,S}
5    H  U0 {3,S}
6    H  U0 {3,S}
""",
    kinetics = ArrheniusEP(
        A = (329000000000.0, 's^-1'),
        n = 0.211,
        alpha = 0,
        E0 = (31.9, 'kcal/mol'),
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
    label        = "XSR4J_SS;CsJ-CsHH;S-HSs",
    group1 = 
"""
1 *3 R!H U1 {2,S}
2 *4 R!H U0 {1,S} {3,S}
3 *2 R!H U0 {2,S} {4,S}
4 *1 Ss  U0 {3,S} {5,S}
5    R   U0 {4,S}
""",
    group2 = 
"""
1 *3 C  U1 {2,S} {3,S} {4,S}
2 *4 Cs U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
""",
    group3 = 
"""
1 *1 Ss U0 {2,S} {3,S}
2    H  U0 {1,S}
3 *2 Ss U0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (288000000000.0, 's^-1'),
        n = 0.108,
        alpha = 0,
        E0 = (21.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

