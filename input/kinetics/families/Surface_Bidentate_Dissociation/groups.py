#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Bidentate_Dissociation/groups"
shortDesc = u""
longDesc = u"""
Surface bond fission of one species with a double bond into two distinct adsorbates, in which one of the new adsorbates is bidentate:

 *1=*2-*3                        *1--*2   +  *3
  |                     ---->     |   |       |
~*4~ + ~*5~~  + ~*6~~           ~*4~~*5~~ + ~*6~~


The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)  * (mol/m2)
so k should be in (m4/mol2/s)
"""

template(reactants=["Combined", "VacantSite1", "VacantSite2"], products=["Adsorbate1", "Adsorbate2"], ownReverse=False)

reverse = "Surface_Bidentate_Association"

recipe(actions=[
    ['FORM_BOND', '*2', 1, '*5'],
    ['FORM_BOND', '*3', 1, '*6'],
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['BREAK_BOND', '*2', 1, '*3'],
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
1 *1 R!H u0 {2,[D,T]} {4,[S,D]}
2 *2 R!H u0 {1,[D,T]} {3,S}
3 *3 R   u0 {2,S}
4 *4 Xo  u0 {1,[S,D]}
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
    index = 2,
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
