#!/usr/bin/env python
# encoding: utf-8

name = "halocarbene_recombination/groups"
shortDesc = u""
longDesc = u"""

              R           R
              |           |
*1R. +    Y-*2C:  <-->  *2C.-*1R
                          |
                          Y
Y = F,Cl,Br,I
"""

template(reactants=["carbene"], products=["radical"], ownReverse=False)

reverse = "Bond_Dissociation"

reversible = True
reactantNum = 2
productNum = 1

recipe(actions=[
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_PAIR', '*2', '1'],
    ['GAIN_RADICAL', '*2', '1'],
    ['FORM_BOND', '*1', 1, '*2'],
])

entry(
    index = 0,
    label = "carbene",
    group = 
"""
1 *1 R    u1 px
2 *2 C2s  u0 p1 {3,S}
3    Val7 u0 p3 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "CF",
    group = 
"""
1 *1 R    u1 px
2 *2 C2s  u0 p1 {3,S}
3    F1s  u0 p3 {2,S}
""",
    kinetics = None,
)


entry(
    index = 2,
    label = "CF2",
    group = 
"""
1 *1 R    u1 px
2 *2 C2s  u0 p1 {3,S} {4,S}
3    F1s  u0 p3 {2,S}
4    F1s  u0 p3 {2,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "CCl",
    group = 
"""
1 *1 R    u1 px
2 *2 C2s  u0 p1 {3,S}
3    Cl1s  u0 p3 {2,S}
""",
    kinetics = None,
)


entry(
    index = 4,
    label = "CCl2",
    group = 
"""
1 *1 R    u1 px
2 *2 C2s  u0 p1 {3,S} {4,S}
3    Cl1s u0 p3 {2,S}
4    Cl1s u0 p3 {2,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "CBr",
    group = 
"""
1 *1 R    u1 px
2 *2 C2s  u0 p1 {3,S}
3    Br1s u0 p3 {2,S}
""",
    kinetics = None,
)


entry(
    index = 6,
    label = "CBr2",
    group = 
"""
1 *1 R    u1 px
2 *2 C2s  u0 p1 {3,S} {4,S}
3    Br1s u0 p3 {2,S}
4    Br1s u0 p3 {2,S}
""",
    kinetics = None,
)


tree(
"""
L1: carbene
    L2: CF
        L3: CF2
    L2: CCl
        L3: CCl2
    L2: CBr
        L3: CBr2
"""
)

