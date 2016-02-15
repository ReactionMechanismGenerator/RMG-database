#!/usr/bin/env python
# encoding: utf-8

name = "Silylene_to_Silene/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["SiRSiH"], products=["SiRH=Si"], ownReverse=False)

reverse = "Silene_to_Silylene"

recipe(actions=[
    ['BREAK_BOND', '*2', 'S', '*3'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['CHANGE_BOND', '*1', '1', '*2'],
    ['LOSE_PAIR', '*1', '1']
])

entry(
    index = 1,
    label = "SiRSiH",
    group = 
"""
1 *1 Si u0 p1 c0 {2,S}
2 *2 Si u0 px c0 {1,S} {3,S}
3 *3  H u0 p0 c0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "SiHSiH",
    group = 
"""
1 *1 Si u0 p1 c0 {2,S} {4,S}
2 *2 Si u0 px c0 {1,S} {3,S}
3 *3  H u0 p0 c0 {2,S}
4     H u0 p0 c0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "SiHSiH3",
    group = 
"""
1 *1 Si u0 p1 c0 {2,S} {4,S}
2 *2 Si u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 *3  H u0 p0 c0 {2,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {2,S}
6     H u0 p0 c0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "SiHSiH2",
    group = 
"""
1 *1 Si u0 p1 c0 {2,S} {4,S}
2 *2 Si u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 *3  H u0 p0 c0 {2,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {2,S}
6    Si ux px c0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "SiHSiH(Si2)",
    group = 
"""
1 *1 Si u0 p1 c0 {2,S} {4,S}
2 *2 Si u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 *3  H u0 p0 c0 {2,S}
4     H u0 p0 c0 {1,S}
5    Si ux px c0 {2,S}
6    Si ux px c0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "SiSiSiH",
    group = 
"""
1 *1 Si u0 p1 c0 {2,S} {4,S}
2 *2 Si u0 px c0 {1,S} {3,S}
3 *3  H u0 p0 c0 {2,S}
4    Si ux px c0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "SiSiSiH3",
    group = 
"""
1 *1 Si u0 p1 c0 {2,S} {4,S}
2 *2 Si u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 *3  H u0 p0 c0 {2,S}
4    Si ux px c0 {1,S}
5     H u0 p0 c0 {2,S}
6     H u0 p0 c0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "SiSiSiH2",
    group = 
"""
1 *1 Si u0 p1 c0 {2,S} {4,S}
2 *2 Si u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 *3  H u0 p0 c0 {2,S}
4    Si ux px c0 {1,S}
5     H u0 p0 c0 {2,S}
6    Si ux px c0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "SiSiSiH(Si2)",
    group = 
"""
1 *1 Si u0 p1 c0 {2,S} {4,S}
2 *2 Si u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 *3  H u0 p0 c0 {2,S}
4    Si ux px c0 {1,S}
5    Si ux px c0 {2,S}
6    Si ux px c0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)


tree(
"""
L1: SiRSiH
    L2: SiHSiH
        L3: SiHSiH3
        L3: SiHSiH2
        L3: SiHSiH(Si2)
    L2: SiSiSiH
        L3: SiSiSiH3
        L3: SiSiSiH2
        L3: SiSiSiH(Si2)
"""
)

