#!/usr/bin/env python
# encoding: utf-8

name = "Cyclic_Ether_Formation/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Root"], products=["RO", "OR"], ownReverse=False)

reverse = "OH+CyclicEther_Form_Alkyl-hydroperoxyl"
reversible = True

reactantNum = 1
productNum = 2

recipe(actions=[
    ['BREAK_BOND', '*2', 1, '*3'],
    ['FORM_BOND', '*1', 1, '*2'],
    ['GAIN_RADICAL', '*3', '1'],
    ['LOSE_RADICAL', '*1', '1'],
])

boundaryAtoms = ["*1", "*2"]

entry(
    index = 0,
    label = "Root",
    group =
"""
1 *1 R!H      u1
2 *2 O2s      u0  {3,S}
3 *3 [O2s,S]  ux  {2,S}
""",
    kinetics = None,
)

tree(
"""
L1: Root
"""
)
