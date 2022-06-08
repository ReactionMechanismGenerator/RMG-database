#!/usr/bin/env python
# encoding: utf-8

name = "nitroso_to_oxime/groups"
shortDesc = u""
longDesc = u"""
This family describes solution-phase hydrolysis of amine groups:
N(=O)RH <=> N(OH)=R
*ONLY HAPPEN WHEN R HAS AT LEAST ONE H*
atom labels:
N[*1](=O[*2])C[*3]H[*4] <=> N[*1](O[*2]H[*4])=C[*3]
"""

template(reactants=["nitroso"], products=["oxime"], ownReverse=False)

reverse = "NULL"

reversible = True

only_forward = True

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*2', 1, '*4'],
    ['CHANGE_BOND', '*1', +1, '*3'],


])

entry(
    index=0,
    label="nitroso",
    group=
"""
1 *1 N u0 p1 c0 {2,D} {3,S}
2 *2 O u0 p2 c0 {1,D}
3 *3 C u0 p0 c0 {4,S} {5,S} {6,S} {1,S}
4 *4 H u0 p0 c0 {3,S}
5    R!H ux px cx {3,S}
6    R ux px cx {3,S}



""",
    kinetics=None,
)


tree(
"""
L1: nitroso
"""
)
