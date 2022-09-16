#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_to_Bidentate/groups"
shortDesc = u""
longDesc = u"""
A monodentate species becomes bidentate as H dissociates from it and both form a new bond with the surface instead.

 *1--*2--*3                   *1--*2    *3 
  |                  ---->     |   |     |
~*4~ + ~*5~ + ~*6            ~*4~~*5 + ~*6~~ 

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2) * (mol/m2)
so k should be in (m4/mol2/s)
"""

template(reactants=["Combined", "VacantSite1", "VacantSite2"], products=["Adsorbate1", "Adsorbate2"], ownReverse=False)

reverse = "Surface_Bidentate_Association_to_Monodentate"

recipe(actions=[
    ['BREAK_BOND', '*2', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*5'],
    ['FORM_BOND', '*3', 1, '*6'],
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
1 *1 R!H u0 {2,[S,D,T]} {4,[S,D,T]}
2 *2 R!H u0 {1,[S,D,T]} {3,[S]}
3 *3 H   u0 {2,[S]}
4 *4 Xo  u0 {1,[S,D,T]}

""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite1",
    group =
"""
1 *5 Xv u0
""",
    kinetics = None,
)

entry(
    index = 3,
    label="VacantSite2",
    group =
"""
1 *6 Xv u0
""",
    kinetics = None,
)


tree(
"""
L1: Combined

L1: VacantSite1

L1: VacantSite2
"""
)
