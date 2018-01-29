#!/usr/bin/env python
# encoding: utf-8

name = "Bimolec_Hydroperoxide_Decomposition/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["ROOH", "ROOH"], products=["ROOrad", "ROrad", "H2O"], ownReverse=False)

reverse = "none"

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*2', 1, '*3'],
    ['GAIN_RADICAL', '*1', '1'],
    ['GAIN_RADICAL', '*4', '1'],
])

entry(
    index = 1,
    label = "ROOH",
    group = 
"""
1    R u0 {2,S}
2 *1 O u0 {1,S} {3,S}
3 *2 O u0 {2,S} {4,S}
4 *3 H u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "C_sec_OOH",
    group =
"""
1    C   u0 {2,S} {5,S} {6,S} {7,S}
2 *1 O   u0 {1,S} {3,S}
3 *2 O   u0 {2,S} {4,S}
4 *3 H   u0 {3,S}
5    R!H u0 {1,S}
6    R!H u0 {1,S}
7    H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "ringOOH",
    group =
"""
1     C   u0 {2,S} {5,S} {6,S} {10,S}
2  *1 O   u0 {1,S} {3,S}
3  *2 O   u0 {2,S} {4,S}
4  *3 H   u0 {3,S}
5     H   u0 {1,S}
6     R!H u0 {1,S} {7,S}
7     R!H u0 {6,S} {8,S}
8     R!H u0 {7,S} {9,S}
9     R!H u0 {8,S} {10,S}
10    R!H u0 {1,S} {9,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "C_ter_OOH",
    group =
"""
1    C   u0 {2,S} {5,S} {6,S} {7,S}
2 *1 O   u0 {1,S} {3,S}
3 *2 O   u0 {2,S} {4,S}
4 *3 H   u0 {3,S}
5    R!H u0 {1,S}
6    R!H u0 {1,S}
7    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "R/ringOOH",
    group =
"""
1     C   u0 {2,S} {5,S} {6,S} {10,S}
2  *1 O   u0 {1,S} {3,S}
3  *2 O   u0 {2,S} {4,S}
4  *3 H   u0 {3,S}
5     R!H u0 {1,S}
6     R!H u0 {1,S} {7,S}
7     R!H u0 {6,S} {8,S}
8     R!H u0 {7,S} {9,S}
9     R!H u0 {8,S} {10,S}
10    R!H u0 {1,S} {9,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "R2/R/R_OOH",
    group =
"""
1    C   u0 {2,S} {5,S} {6,S} {7,S}
2 *1 O   u0 {1,S} {3,S}
3 *2 O   u0 {2,S} {4,S}
4 *3 H   u0 {3,S}
5    R!H u0 {1,S}
6    R!H u0 {1,S}
7    R!H u0 {1,S} {8,S}
8    R!H u0 {7,S}
""",
    kinetics = None,
)

tree(
"""
L1: ROOH
    L2: C_sec_OOH
        L3: ringOOH
    L2: C_ter_OOH
        L3: R/ringOOH
        L3: R2/R/R_OOH
"""
)
