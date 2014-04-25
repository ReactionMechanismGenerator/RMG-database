#!/usr/bin/env python
# encoding: utf-8

name = "lone_electron_pair_bond/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["N3sRRR", "O_(S)"], products=["N3sRRRO"], ownReverse=False)

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
1 *1 N3s 0 1 {2,S} {3,S} {4,S}
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
    label = "O_(S)",
    multiplicity = [1],
    group = 
"""
1 *2 O 2
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
L1: O_(S)
"""
)


forbidden(
    label = "OJJH",
    multiplicity = [3],
    group = 
"""
1    O 2 {2,S}
2    R 0 {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)
