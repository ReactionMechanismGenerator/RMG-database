#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_Charge_Separation/groups"
shortDesc = u""
longDesc = u"""
Two adsorbates react. One has multiple bonds to the surface, the other has a
bond to the surface and to some functional group with charge separation
across the bond. The functional group is transferred to the multiple-bonded
species.

 *1   *4[-]-*3[+]          *1=*4  *3
 |||          |      ---->  |      |
~*2~~ +    ~*5~~          ~*2~ + ~*5~~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Abstracting", "Donating"], products=["Abstracted", "Donated"], ownReverse=False)

reactantNum=2
productNum=2

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*4'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['CHANGE_BOND', '*1', 1, '*4'],
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['LOSE_PAIR','*4','1'],
    ['GAIN_PAIR', '*3', '1'],
    ['LOSE_CHARGE','*3','1'],
    ['GAIN_CHARGE', '*4', '1'],
])

entry(
    index = 1,
    label = "Abstracting",
    group =
"""
1 *1 R!H u0 px c0 {2,[T,Q]}
2 *2 Xo  u0 p0 c0 {1,[T,Q]}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="Donating",
    group =
"""
1 *4 R!H u0 p[1,2,3] c-1 {2,S}
2 *3 N u0 p0 c+1 {1,S} {3,[S,D]} {4,[S,D]}
3 *5 Xo u0 p0 c0 {2,[S,D]}
4 R u0 px c0 {2,[S,D]}
""",
    kinetics = None,
)


tree(
"""
L1: Abstracting
L1: Donating
"""
)

forbidden(
    label = "Surf",
    group =
"""
1 *4 R!H u0 p[1,2,3] c-1 {2,S} {5,[S,D,T]}
2 *3 N u0 p0 c+1 {1,S} {3,[S,D]} {4,[S,D]}
3 *5 Xo u0 p0 c0 {2,[S,D]}
4 R u0 px c0 {2,[S,D]}
5 Xo u0 c0 {1,[S,D,T]}
""",
)
