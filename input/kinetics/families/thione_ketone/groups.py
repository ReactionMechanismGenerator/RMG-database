#!/usr/bin/env python
# encoding: utf-8

name = "thione_ketone/groups"
shortDesc = u""
longDesc = u"""
This family describes solution-phase hydrolysis of a thione:
C=S + H2O <=> C=O + H2S

atom labels:

C[*1]_=S[*2] + H[*3]_O[*4]_H[*5] <=> C[*1]_=O[*4] + H[*3]_S[*2]_H[*5]
"""

template(reactants=["thione", "H2O"], products=["ketone", "H2S"], ownReverse=False)

reverse = "ketone_thione"

reversible = True

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['BREAK_BOND', '*4', 1, '*5'],
    ['FORM_BOND', '*1', 1, '*4'],
    ['CHANGE_BOND', '*1', 1, '*4'],
    ['FORM_BOND', '*2', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*5'],
])

entry(
    index=0,
    label="thione",
    group=
"""
1 *1 C u0 p0 c0 {2,D}
2 *2 S u0 p2 c0 {1,D}
""",
    kinetics=None,
)

entry(
    index=1,
    label="H2O",
    group=
"""
1 *4 O u0 p2 c0 {2,S} {3,S}
2 *3 H u0 p0 c0 {1,S}
3 *5 H u0 p0 c0 {1,S}
""",
    kinetics=None,
)

tree(
"""
L1: thione
L1: H2O
"""
)
