#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Intra_Elimination_LiR/groups"
shortDesc = ""
longDesc = """
"""

template(reactants=["Root"], products=["YJ"], ownReverse=False)

reversible = True

reactantNum = 1

productNum = 1

autoGenerated = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*4'],
    ['BREAK_BOND', '*2', 1, '*3'],
    ['FORM_BOND', '*3', 1, '*4'],
    ['CHANGE_BOND', '*1', 1, '*2'],
])

entry(
    index = 0,
    label = "Root",
    group =
"""
1 *1 R!H u[0,1] {2,[S,D,B]} {4,S}
2 *2 R!H u[0,1] r1 {1,[S,D,B]} {3,S}
3 *3 R u[0,1] r1 {2,S}
4 *4 Li u0 {1,S}
""",
    kinetics = None,
)



tree(
"""
L1: Root
"""
)