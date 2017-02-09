#!/usr/bin/env python
# encoding: utf-8

name = "lone_electron_pair_bond/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["N3sRRR", "O_atom_singlet"], products=["N3sRRRO"], ownReverse=False)

reverse = "Bond_Dissociation"

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*2'],
    ['LOSE_PAIR', '*1', '1'],
])

entry(
    index = 1,
    label = "N3sRRR",
    group = 
"""
1 *1 N3s u0 {2,S} {3,S} {4,S}
2    R   u0 {1,S}
3    R   u0 {1,S}
4    R   u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "O_atom_singlet",
    group = 
"""
1 *2 O u0 p3
""",
    kinetics = None,
)

tree(
"""
L1: N3sRRR
L1: O_atom_singlet
"""
)
