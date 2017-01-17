#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction/groups"
shortDesc = u""
longDesc = u"""
Two adsorbates react. One has a multiple bond to the surface, the other has a 
single-bond to the surface and some functional group. 
The functional group is transferred from the single
to the multiple-bonded species.

 *1   *4-*3             *1-*4  *3
 ||       |      ---->   |     ||
~*2~~ + ~*5~~          ~*2~ + ~*5~~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Abstracting", "Donating"], products=["Abstracting", "Donating"], ownReverse=True)

recipe(actions=[
    ['FORM_BOND', '*1', 'S', '*4'],
    ['BREAK_BOND', '*3', 'S', '*4'],
    ['CHANGE_BOND', '*1', '-1', '*2'],
    ['CHANGE_BOND', '*3', '1', '*5'],
])

entry(
    index = 1,
    label = "Abstracting",
    group = 
"""
1 *1 R  ux {2,[D,T,Q]}
2 *2 Xo u0 {1,[D,T,Q]}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="Donating",
    group = 
"""
1 *4 R  ux {2,S}
2 *3 R  ux {1,S} {3,[S,D,T]}
3 *5 Xo u0       {2,[S,D,T]}
""",
    kinetics = None,
)


tree(
"""
L1: Abstracting

L1: Donating
"""
)

