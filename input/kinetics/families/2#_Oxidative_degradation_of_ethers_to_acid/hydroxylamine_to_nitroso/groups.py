#!/usr/bin/env python
# encoding: utf-8

name = "hydroxylamine_to_nitroso/groups"
shortDesc = u""
longDesc = u"""
This family describes solution-phase hydrolysis of amine groups:
 HN(OH)R' <=> N(=O)R' +H2
 atom labels:
 H[*1]N[*2](O[*3]H[*4])R' <=> N[*2](=O[#])R' +H[*1]H[*4]
"""

template(reactants=["hydroxylamine"], products=["nitroso", "H2O"], ownReverse=False)

reverse = "NULL"

reversible = True

only_forward = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*1', 1, '*4'],
    ['CHANGE_BOND', '*2', +1, '*3'],


])

entry(
    index=0,
    label="hydroxylamine",
    group=
"""
1 R ux px cx {2,S} 
2 *2 N u0 p1 c0 {1,S} {3,S} {4,S}
3 *3 O u0 p2 c0 {2,S} {5,S}
4 *1 H u0 p0 c0 {2,S}
5 *4 H u0 p0 c0 {3,S}

""",
    kinetics=None,
)


tree(
"""
L1: hydroxylamine
"""
)
