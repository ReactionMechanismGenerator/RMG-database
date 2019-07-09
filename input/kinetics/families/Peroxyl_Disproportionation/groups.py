#!/usr/bin/env python
# encoding: utf-8

name = "Peroxyl_Disproportionation/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["ROO_rad", "ROO_rad"], products=["RO_rad", "RO_rad", "O2"], ownReverse=False)

reverse = "none"

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*2', 1, '*4'],
    ['GAIN_RADICAL', '*1', '1'],
    ['GAIN_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "ROO_rad",
    group =
"""
1    R u0 {2,S}
2 *1 O u0 {1,S} {3,S}
3 *2 O u1 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "HOO_rad",
    group =
"""
1    H u0 {2,S}
2 *1 O u0 {1,S} {3,S}
3 *2 O u1 {2,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "C_methyl_OO_rad",
    group =
"""
1    C u0 {2,S} {4,S} {5,S} {6,S}
2 *1 O u0 {1,S} {3,S}
3 *2 O u1 {2,S}
4    H u0 {1,S}
5    H u0 {1,S}
6    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "C_pri_OO_rad",
    group =
"""
1    C   u0 {2,S} {4,S} {5,S} {6,S}
2 *1 O   u0 {1,S} {3,S}
3 *2 O   u1 {2,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "C_sec_OO_rad",
    group =
"""
1    C   u0 {2,S} {4,S} {5,S} {6,S}
2 *1 O   u0 {1,S} {3,S}
3 *2 O   u1 {2,S}
4    H   u0 {1,S}
5    R!H u0 {1,S}
6    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "C_ter_OO_rad",
    group =
"""
1    C   u0 {2,S} {4,S} {5,S} {6,S}
2 *1 O   u0 {1,S} {3,S}
3 *2 O   u1 {2,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
6    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "O=COO_rad",
    group =
"""
1    C u0 {2,S} {4,D}
2 *1 O u0 {1,S} {3,S}
3 *2 O u1 {2,S}
4    O u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "CCOO_rad",
    group =
"""
1    C u0 {2,S} {4,S} {5,S} {6,S}
2 *1 O u0 {1,S} {3,S}
3 *2 O u1 {2,S}
4    C u0 {1,S}
5    H u0 {1,S}
6    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "OCOO_rad",
    group =
"""
1    C u0 {2,S} {4,S} {5,S} {6,S}
2 *1 O u0 {1,S} {3,S}
3 *2 O u1 {2,S}
4    O u0 {1,S}
5    H u0 {1,S}
6    H u0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: ROO_rad
    L2: HOO_rad
    L2: C_methyl_OO_rad
    L2: C_pri_OO_rad
        L3: CCOO_rad
        L3: OCOO_rad
    L2: C_sec_OO_rad
    L2: C_ter_OO_rad
    L2: O=COO_rad
"""
)
