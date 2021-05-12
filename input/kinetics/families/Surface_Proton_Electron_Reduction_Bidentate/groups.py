#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Proton_Electron_Reduction_Bidentate/groups"
shortDesc = u""
longDesc = u"""

 *1                                   *6H-*1
 ||                                        |
 *2   +   *4   + *6H+ + *e-  <--->        *2 -- *4
 ||       ||                              ||     |
~*3~     ~*5~                            ~*3~  ~*5~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m3) * 1
so k should be in (m3/mol/s).
"""

template(reactants=["Adsorbate1","Adsorbate2","Proton"], products=["Reduced"], ownReverse=False)

reverse = "Surface_Proton_Electron_Oxidation_Bidentate"

reactantNum = 3
productNum = 1
allowChargedSpecies = True
electrons = -1

recipe(actions=[
    ['LOSE_CHARGE', '*6', 1],
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['FORM_BOND', '*1', 1, '*6'],
    ['CHANGE_BOND', '*4', -1, '*5'],
    ['FORM_BOND', '*4', 1, '*2'],
])


entry(
    index = 1,
    label = "Adsorbate1",
    group =
"""
1 *1 R!H u0 {2,[D,T]}
2 *2 R!H u0 {1,[D,T]} {3,[S,D]}
3 *3 X u0 {2,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Adsorbate2",
    group =
"""
1 *4 R!H u0 {2,[D,T,Q]}
2 *5 X u0 {1,[D,T,Q]}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "Proton",
    group =
"""
1 *6 H+ u0 p0 c+1
""",
    kinetics = None,
)

tree(
"""
L1: Adsorbate1

L1: Adsorbate2

L1: Proton
"""
)