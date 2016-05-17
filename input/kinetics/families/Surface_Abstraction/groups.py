#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction/groups"
shortDesc = u""
longDesc = u"""
Two adsorbates react. One has a double bond, the other has a single-bond and some functional group. The functional group is transferred to from the single to the double-bonded species.

 *1      *3-*4          *1-*4  *3
 ||       |      ---->   |     ||
~*2~~ + ~*5~~          ~*2~ + ~*5~~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Adsorbate1", "Adsorbate2"], products=["Combined", "VacantSite"], ownReverse=True)

recipe(actions=[
    ['FORM_BOND', '*1', 'S', '*4'],
    ['BREAK_BOND', '*3', 'S', '*4'],
    ['CHANGE_BOND', '*1', '-1', '*2'],
    ['CHANGE_BOND', '*3', '1', '*5'],
])

entry(
    index = 1,
    label = "Adsorbate1",
    group = 
"""
1 *1 R  ux {2,[D,T]}
2 *2 Xo u0 {1,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="Adsorbate2",
    group = 
"""
1 *4 R  ux {2,S}
2 *3 R  ux {1,S} {3,[S,D,T]}
3 *5 Xo u0 {2,[S,D,T]}
""",
    kinetics = None,
)


tree(
"""
L1: Adsorbate1

L1: Adsorbate2
"""
)

