#!/usr/bin/env python
# encoding: utf-8

name = "lone_electron_pair_bond/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["N3sRRR", "O_atom_singlet"], products=["N3sRRRO"], ownReverse=False)

reverse = "Bond_Dissociation"

recipe(actions=[
    ['FORM_BOND', '*1', 'S', '*2'],
    ['LOSE_RADICAL', '*2', '2'],
    ['LOSE_PAIR', '*1', '1'],
    ['GAIN_PAIR', '*2', '1'],
])

entry(
    index = 1,
    label = "N3sRRR",
    group = 
"""
1 *1 N3s 0 {2,S} {3,S} {4,S}
2    R 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "O_atom_singlet",
    group = 
"""
1 *2 O 2S
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: N3sRRR
L1: O_atom_singlet
"""
)





forbidden(
    label = "OJJH",
    group = 
"""
1    O 2T {2,S}
2    R 0  {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)
