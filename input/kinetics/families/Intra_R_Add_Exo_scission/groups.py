#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Exo_scission/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Rn-Cs-Cb"], products=["Rn-Cs-Cb"], ownReverse=True)

recipe(actions=[
    ['BREAK_BOND', '*2', 'S', '*3'],
    ['FORM_BOND', '*1', 'S', '*2'],
    ['LOSE_RADICAL', '*1', '1'],
    ['GAIN_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "Rn-Cs-Cb",
    group = 
"""
1 *1 C 	 u1 {2,S}
2 *3 C   u0 {1,S} {3,S}
3 *2 Cb  u0 {2,S}
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

entry(
    index = 5,
    label = "Cs-Cb",
    group =
"""
2 *3 C   u0 {3,S}
3 *2 Cb  u0 {2,S}
""",
    kinetics = None,
)

tree(
"""
L1: Rn-Cs-Cb

L1: rad
   L2: rad-Ct
   L2: rad-HH
    
L1: Cs-Cb
"""
)
