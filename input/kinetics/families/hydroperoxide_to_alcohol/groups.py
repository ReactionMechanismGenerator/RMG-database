#!/usr/bin/env python
# encoding: utf-8

name = "hydroperoxide_to_alcohol/groups"
shortDesc = u""
longDesc = u"""
This family describes solution-phase conversions of the sort:
ROOH + H2O <=> ROH + H2O2

atom labels:

R_O(*1)_O(*2)_H(*3) + H(*4)_O(*5)_H <=> R_O(*1)_H(*4) + H(*3)_O(*2)_O(*5)_H
"""

template(reactants=["ROOH", "H2O"], products=["ROH", "H2O2"], ownReverse=False)

reverse = "alcohol_to_hydroperoxide"

reversible = True

only_forward = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*4', 1, '*5'],
    ['FORM_BOND', '*1', 1, '*4'],
    ['FORM_BOND', '*2', 1, '*5'],
])

entry(
    index = 0,
    label = "ROOH",
    group =
"""
1    R!H ux px cx {2,S}
2 *1 O   u0 p2 c0 {1,S} {3,S}
3 *2 O   u0 p2 c0 {2,S} {4,S}
4 *3 H   u0 p0 c0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "H2O",
    group = 
"""
1 *5 O u0 p2 c0 {2,S} {3,S}
2 *4 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: ROOH
L1: H2O
"""
)
