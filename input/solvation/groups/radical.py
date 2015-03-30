#!/usr/bin/env python
# encoding: utf-8

name = "Radical Groups"
shortDesc = u"Radical corrections to A"
longDesc = u"""
H-bonding parameter A should be modified for when we saturate 
radical molecules with hydrogens and look up the saturated
structure.
"""
entry(
    index = 0,
    label = "R_rad",
    group = 
"""
1 * R u1
""",
    solute = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "O_rad",
    group = 
"""
1 * O u1 p2
""",
    solute = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "ROJ",
    group = 
"""
1 * O u1 p2 c0 {2,S}
2   R u0 {1,S}
""",
    solute = SoluteData(
        S = 0.0,
        B = 0.0,
        E = 0.0,
        L = 0.0,
        A = -0.345,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "ROOJ",
    group = 
"""
1 * O u1 p2 c0 {2,S}
2   O u0 p2 {1,S} {3,S}
3   R u0 {2,S}
""",
    solute = SoluteData(
        S = 0.0,
        B = 0.0,
        E = 0.0,
        L = 0.0,
        A = -0.345,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "RC(O)OJ",
    group = 
"""
1 * O u1 p2 c0 {2,S}
2   C u0 p0 {1,S} {3,D} {4,S}
3   O u0 p2 {2,D}
4   R u0 {2,S}
""",
    solute = SoluteData(
        S = 0.0,
        B = 0.0,
        E = 0.0,
        L = 0.0,
        A = -0.243,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: R_rad
    L2: O_rad
        L3: ROJ
            L4: RC(O)OJ
            L4: ROOJ
"""
)

