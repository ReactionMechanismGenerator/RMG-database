#!/usr/bin/env python
# encoding: utf-8

name = "PriSec_Peroxyl_Disproportionation/groups"
shortDesc = u""
longDesc = u"""
This family assumes that the disproportionation reaction results exclusively
in ketone, alcohol, and oxygen. In reality, the termination proceeds through a
series of more complex steps, which also involves the production of hydrogen
peroxide.
"""

template(reactants=["R2CHOO_rad", "R2CHOO_rad"], products=["R2CO", "R2CHOH", "O2"], ownReverse=False)

reverse = "none"

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*4'],
    ['BREAK_BOND', '*2', 1, '*3'],
    ['BREAK_BOND', '*5', 1, '*6'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*3', 1, '*6'],
    ['FORM_BOND', '*4', 1, '*5'],
])

entry(
    index = 1,
    label = "R2CHOO_rad",
    group = 
"""
1 *1 C u0 {2,S} {4,S} {5,S} {6,S}
2 *2 O u0 {1,S} {3,S}
3 *3 O u1 {2,S}
4 *4 H u0 {1,S}
5    R u0 {1,S}
6    R u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "C_methyl_OO_rad",
    group =
"""
1 *1 C u0 {2,S} {4,S} {5,S} {6,S}
2 *2 O u0 {1,S} {3,S}
3 *3 O u1 {2,S}
4 *4 H u0 {1,S}
5    H u0 {1,S}
6    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "C_pri_OO_rad",
    group =
"""
1 *1 C   u0 {2,S} {4,S} {5,S} {6,S}
2 *2 O   u0 {1,S} {3,S}
3 *3 O   u1 {2,S}
4 *4 H   u0 {1,S}
5    H   u0 {1,S}
6    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "C_sec_OO_rad",
    group =
"""
1 *1 C   u0 {2,S} {4,S} {5,S} {6,S}
2 *2 O   u0 {1,S} {3,S}
3 *3 O   u1 {2,S}
4 *4 H   u0 {1,S}
5    R!H u0 {1,S}
6    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "ring_OO_rad",
    group =
"""
1 *1 C   u0 {2,S} {4,S} {5,S} {9,S}
2 *2 O   u0 {1,S} {3,S}
3 *3 O   u1 {2,S}
4 *4 H   u0 {1,S}
5    R!H u0 {1,S} {6,S}
6    R!H u0 {5,S} {7,S}
7    R!H u0 {6,S} {8,S}
8    R!H u0 {7,S} {9,S}
9    R!H u0 {1,S} {8,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "R4/R_OO_rad",
    group =
"""
1 *1 C   u0 {2,S} {4,S} {5,S} {9,S}
2 *2 O   u0 {1,S} {3,S}
3 *3 O   u1 {2,S}
4 *4 H   u0 {1,S}
5    R!H u0 {1,S} {6,S}
6    R!H u0 {5,S} {7,S}
7    R!H u0 {6,S} {8,S}
8    R!H u0 {7,S}
9    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "R3/R_OO_rad",
    group =
"""
1 *1 C   u0 {2,S} {4,S} {5,S} {8,S}
2 *2 O   u0 {1,S} {3,S}
3 *3 O   u1 {2,S}
4 *4 H   u0 {1,S}
5    R!H u0 {1,S} {6,S}
6    R!H u0 {5,S} {7,S}
7    R!H u0 {6,S}
8    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "R2/R_OO_rad",
    group =
"""
1 *1 C   u0 {2,S} {4,S} {5,S} {7,S}
2 *2 O   u0 {1,S} {3,S}
3 *3 O   u1 {2,S}
4 *4 H   u0 {1,S}
5    R!H u0 {1,S} {6,S}
6    R!H u0 {5,S}
7    R!H u0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: R2CHOO_rad
    L2: C_methyl_OO_rad
    L2: C_pri_OO_rad
    L2: C_sec_OO_rad
        L3: ring_OO_rad
        L3: R4/R_OO_rad
        L3: R3/R_OO_rad
        L3: R2/R_OO_rad
"""
)
