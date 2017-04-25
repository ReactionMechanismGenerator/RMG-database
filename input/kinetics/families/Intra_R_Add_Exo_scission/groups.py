#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Exo_scission/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["R4-Cs-Cb"], products=["R4-Cs-Cb"], ownReverse=True)

recipe(actions=[
    ['BREAK_BOND', '*2', 1, '*4'],
    ['FORM_BOND', '*1', 1, '*2'],
    ['LOSE_RADICAL', '*1', '1'],
    ['GAIN_RADICAL', '*4', '1'],
])

entry(
    index = 1,
    label = "R4-Cs-Cb",
    group = 
"""
1 *1 C 	 u1 {2,S}
2 *4 C   u0 {1,S} {3,S}
3 *2 Cb  u0 {2,S} {4,B}
4 *3 Cb	 u0 {3,B}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "rad",
    group = 
"""
1 *1 C  u1
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "rad-Ct",
    group = 
"""
1 *1 C  u1 {2,S}
2    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "rad-HH",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: R4-Cs-Cb

L1: rad
   L2: rad-Ct
   L2: rad-HH
    
"""
)

forbidden(
    label = "Benzofulvenyl_1",
    group =
"""
1  *1 C u1 {4,S}
4  *4 Cs u0 {1,S} {5,S} {12,S}
5  Cd u0 {4,S} {6,D}
6  Cd u0 {5,D} {7,S}
7  *3 Cb u0 {6,S} {8,B} {12,B}
8  Cb u0 {7,B} {9,B}
9  Cb u0 {8,B} {10,B}
10 Cb u0 {9,B} {11,B}
11 Cb u0 {10,B} {12,B}
12 *2 Cb u0 {4,S} {7,B} {11,B}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a benzofulvenyl radical  from isomerizing to 1H_naphthalene in one step using this family. No transition state was
found for such a reaction.
""",
)

forbidden(
    label = "Benzofulvenyl_2",
    group =
"""
1  *1 C u1 {4,S}
4  *4 Cs u0 {1,S} {5,S} {12,S}
5  Cd u0 {4,S} {6,D}
6  Cd u0 {5,D} {7,S}
7  Cb u0 {6,S} {8,B} {12,B}
8  Cb u0 {7,B} {9,B}
9  Cb u0 {8,B} {10,B}
10 Cb u0 {9,B} {11,B}
11 *3 Cb u0 {10,B} {12,B}
12 *2 Cb u0 {4,S} {7,B} {11,B}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a benzofulvenyl radical  from isomerizing to 1H_naphthalene in one step using this family. No transition state was
found for such a reaction.
""",
)