#!/usr/bin/env python
# encoding: utf-8

name = "ketoenol/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["R_ROR"], products=["keton"], ownReverse=False)

reverse = "none"

recipe(actions=[
    ['CHANGE_BOND', '*1', '-1', '*2'],
    ['CHANGE_BOND', '*2', '1', '*3'],
    ['BREAK_BOND', '*3', 'S', '*4'],
    ['FORM_BOND', '*4', 'S', '*1'],
])

entry(
    index = 1,
    label = "R_ROR",
    group = 
"""
1 *1 R 0 {2,D}
2 *2 R 0 {1,D} {3,S}
3 *3 O 0 {2,S} {4,S}
4 *4 R 0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "C_COH",
    group = 
"""
1 *1 C 0 {2,D}
2 *2 C 0 {1,D} {3,S}
3 *3 O 0 {2,S} {4,S}
4 *4 H 0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "Cds/H2_Cds/ROH",
    group = 
"""
1 *1 C 0 {2,D} {5,S} {6,S}
2 *2 C 0 {1,D} {3,S} {7,S}
3 *3 O 0 {2,S} {4,S}
4 *4 H 0 {3,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    R 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "Cds/H2_Cds/HOH",
    group = 
"""
1 *1 C 0 {2,D} {5,S} {6,S}
2 *2 C 0 {1,D} {3,S} {7,S}
3 *3 O 0 {2,S} {4,S}
4 *4 H 0 {3,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "Cds/H2_Cds/CsOH",
    group = 
"""
1 *1 C  0 {2,D} {5,S} {6,S}
2 *2 C  0 {1,D} {3,S} {7,S}
3 *3 O  0 {2,S} {4,S}
4 *4 H  0 {3,S}
5    H  0 {1,S}
6    H  0 {1,S}
7    Cs 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "Cds/CsH_Cds/ROH",
    group = 
"""
1 *1 C  0 {2,D} {5,S} {6,S}
2 *2 C  0 {1,D} {3,S} {7,S}
3 *3 O  0 {2,S} {4,S}
4 *4 H  0 {3,S}
5    Cs 0 {1,S}
6    H  0 {1,S}
7    R  0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "Cds/CsH_Cds/HOH",
    group = 
"""
1 *1 C  0 {2,D} {5,S} {6,S}
2 *2 C  0 {1,D} {3,S} {7,S}
3 *3 O  0 {2,S} {4,S}
4 *4 H  0 {3,S}
5    Cs 0 {1,S}
6    H  0 {1,S}
7    H  0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "Cds/CsH_Cds/CsOH",
    group = 
"""
1 *1 C  0 {2,D} {5,S} {6,S}
2 *2 C  0 {1,D} {3,S} {7,S}
3 *3 O  0 {2,S} {4,S}
4 *4 H  0 {3,S}
5    Cs 0 {1,S}
6    H  0 {1,S}
7    Cs 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "Cds/CsCs_Cds/ROH",
    group = 
"""
1 *1 C  0 {2,D} {5,S} {6,S}
2 *2 C  0 {1,D} {3,S} {7,S}
3 *3 O  0 {2,S} {4,S}
4 *4 H  0 {3,S}
5    Cs 0 {1,S}
6    Cs 0 {1,S}
7    R  0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "Cds/CsCs_Cds/HOH",
    group = 
"""
1 *1 C  0 {2,D} {5,S} {6,S}
2 *2 C  0 {1,D} {3,S} {7,S}
3 *3 O  0 {2,S} {4,S}
4 *4 H  0 {3,S}
5    Cs 0 {1,S}
6    Cs 0 {1,S}
7    H  0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "Cds/CsCs_Cds/CsOH",
    group = 
"""
1 *1 C  0 {2,D} {5,S} {6,S}
2 *2 C  0 {1,D} {3,S} {7,S}
3 *3 O  0 {2,S} {4,S}
4 *4 H  0 {3,S}
5    Cs 0 {1,S}
6    Cs 0 {1,S}
7    Cs 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "C_COC",
    group = 
"""
1 *1 C 0 {2,D}
2 *2 C 0 {1,D} {3,S}
3 *3 O 0 {2,S} {4,S}
4 *4 C 0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "S_COH",
    group = 
"""
1 *1 S 0 {2,D}
2 *2 C 0 {1,D} {3,S}
3 *3 O 0 {2,S} {4,S}
4 *4 H 0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "S_Cds/HOH",
    group = 
"""
1 *1 S 0 {2,D}
2 *2 C 0 {1,D} {3,S} {5,S}
3 *3 O 0 {2,S} {4,S}
4 *4 H 0 {3,S}
5    H 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "S_Cds/CsOH",
    group = 
"""
1 *1 S  0 {2,D}
2 *2 C  0 {1,D} {3,S} {5,S}
3 *3 O  0 {2,S} {4,S}
4 *4 H  0 {3,S}
5    Cs 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "S_Cds/CH3OH",
    group = 
"""
1 *1 S  0 {2,D}
2 *2 C  0 {1,D} {3,S} {5,S}
3 *3 O  0 {2,S} {4,S}
4 *4 H  0 {3,S}
5    Cs 0 {2,S} {6,S} {7,S} {8,S}
6    H  0 {5,S}
7    H  0 {5,S}
8    H  0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "S_Cds/CH2CH3OH",
    group = 
"""
1  *1 S  0 {2,D}
2  *2 C  0 {1,D} {3,S} {5,S}
3  *3 O  0 {2,S} {4,S}
4  *4 H  0 {3,S}
5     Cs 0 {2,S} {6,S} {7,S} {8,S}
6     Cs 0 {5,S} {9,S} {10,S} {11,S}
7     H  0 {5,S}
8     H  0 {5,S}
9     H  0 {6,S}
10    H  0 {6,S}
11    H  0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "S_COC",
    group = 
"""
1 *1 S 0 {2,D}
2 *2 C 0 {1,D} {3,S}
3 *3 O 0 {2,S} {4,S}
4 *4 C 0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: R_ROR
    L2: C_COH
        L3: Cds/H2_Cds/ROH
            L4: Cds/H2_Cds/HOH
            L4: Cds/H2_Cds/CsOH
        L3: Cds/CsH_Cds/ROH
            L4: Cds/CsH_Cds/HOH
            L4: Cds/CsH_Cds/CsOH
        L3: Cds/CsCs_Cds/ROH
            L4: Cds/CsCs_Cds/HOH
            L4: Cds/CsCs_Cds/CsOH
    L2: C_COC
    L2: S_COH
        L3: S_Cds/HOH
        L3: S_Cds/CsOH
            L4: S_Cds/CH3OH
            L4: S_Cds/CH2CH3OH
    L2: S_COC
"""
)

