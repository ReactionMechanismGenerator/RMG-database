#!/usr/bin/env python
# encoding: utf-8

name = "ketoenol/groups"
shortDesc = u""
longDesc = u"""
Sulfur was added to this family, and is treated the same as oxygen.
Ideally we would like to branch this into a new family "R=RSR <=> RRR=S"
once relevant kinetic data is available
"""

template(reactants=["Root"], products=["ketone"], ownReverse=False)

reverse = "Ketone_To_Enol"
reversible = True

reactantNum = 1
productNum = 1

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['CHANGE_BOND', '*2', 1, '*3'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*4', 1, '*1'],
])

boundaryAtoms = ["*2", "*3"]

entry(
    index = 0,
    label = "Root",
    group = 
"""
1 *2 R!H   u0 {2,S} {3,D}
2 *3 [O,S] u0 {1,S} {4,S}
3 *1 R!H   u0 {1,D}
4 *4 R     u0 {2,S}
""",
    kinetics = None,
)

tree(
"""
L1: Root
"""
)

