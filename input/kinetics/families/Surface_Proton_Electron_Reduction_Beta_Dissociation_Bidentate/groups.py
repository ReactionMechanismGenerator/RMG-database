#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Proton_Electron_Reduction_Beta_Dissociation_Bidentate/groups"
shortDesc = u""
longDesc = u"""

   *1                       
    |                        
   *2 -- *4  + *6H+ + *e-  ---->  *2 = *4 + *1-*6 + ~*5~
    |     |                        |
  ~*3~  ~*5~                     ~*3~   

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m3) * 1
so k should be in (m3/mol/s).
"""

template(reactants=["Adsorbate", "Proton"], products=["Reduced", "Adsorbate1","P3"], ownReverse=False)

reverse = "Surface_Proton_Electron_Oxidation_Beta_Association_Bidentate"

reactantNum = 2
productNum = 3
allowChargedSpecies = True
electrons = -1

recipe(actions=[
    ['LOSE_CHARGE', '*6', 1],
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*1', 1, '*6'],
    ['BREAK_BOND', '*4', 1, '*5'],
    ['CHANGE_BOND', '*2', 1, '*4'],
])

entry(
    index = 1,
    label = "Adsorbate",
    group =
"""
1 *1 R!H u0 {2,S}
2 *2 R!H u0 {1,S} {3,[S,D]} {4,[S,D]}
3 *3 X u0 {2,[S,D]}
4 *4 R!H u0 {2,[S,D]} {5,S}
5 *5 X u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Proton",
    group =
"""
1 *6 H+ u0 p0 c+1
""",
    kinetics = None,
)

tree(
"""
L1: Adsorbate

L1: Proton
"""
)

forbidden(
    label = "Xo",
    group =
"""
1 *5 Xo u0
""",
    shortDesc = u"""""",
    longDesc =
u"""
""",
)