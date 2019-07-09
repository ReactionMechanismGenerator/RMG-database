#!/usr/bin/env python
# encoding: utf-8

name = "Peroxyl_Termination/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["RHOO_rad", "ROO_rad"], products=["R=O", "ROH", "O2"], ownReverse=False)

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
    label = "RHOO_rad",
    group =
"""
1 *1 R!H u0 {2,S} {4,S}
2 *2 O   u0 {1,S} {3,S}
3 *3 O   u1 {2,S}
4 *4 H   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "ROO_rad",
    group =
"""
1    R u0 {2,S}
2 *5 O u0 {1,S} {3,S}
3 *6 O u1 {2,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "CH_methyl_OO_rad",
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
    index = 4,
    label = "CH_pri_OO_rad",
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
    index = 5,
    label = "CH_sec_OO_rad",
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
    index = 6,
    label = "HOO_rad",
    group =
"""
1    H u0 {2,S}
2 *5 O u0 {1,S} {3,S}
3 *6 O u1 {2,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "C_methyl_OO_rad",
    group =
"""
1    C u0 {2,S} {4,S} {5,S} {6,S}
2 *5 O u0 {1,S} {3,S}
3 *6 O u1 {2,S}
4    H u0 {1,S}
5    H u0 {1,S}
6    H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "C_pri_OO_rad",
    group =
"""
1    C   u0 {2,S} {4,S} {5,S} {6,S}
2 *5 O   u0 {1,S} {3,S}
3 *6 O   u1 {2,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
6    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "C_sec_OO_rad",
    group =
"""
1    C   u0 {2,S} {4,S} {5,S} {6,S}
2 *5 O   u0 {1,S} {3,S}
3 *6 O   u1 {2,S}
4    H   u0 {1,S}
5    R!H u0 {1,S}
6    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "C_ter_OO_rad",
    group =
"""
1    C   u0 {2,S} {4,S} {5,S} {6,S}
2 *5 O   u0 {1,S} {3,S}
3 *6 O   u1 {2,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
6    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "O=COO_rad",
    group =
"""
1    C u0 {2,S} {4,D}
2 *5 O u0 {1,S} {3,S}
3 *6 O u1 {2,S}
4    O u0 {1,D}
""",
    kinetics = None,
)

tree(
"""
L1: RHOO_rad
    L2: CH_methyl_OO_rad
    L2: CH_pri_OO_rad
    L2: CH_sec_OO_rad
L1: ROO_rad
    L2: HOO_rad
    L2: C_methyl_OO_rad
    L2: C_pri_OO_rad
    L2: C_sec_OO_rad
    L2: C_ter_OO_rad
    L2: O=COO_rad
"""
)
