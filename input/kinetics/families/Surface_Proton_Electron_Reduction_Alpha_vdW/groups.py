#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Proton_Electron_Reduction_Alpha_vdW/groups"
shortDesc = u""
longDesc = u"""

   *1                        *1-*3H
    |  + *3H+ + *e-  ---->    :
  ~*2~                      ~*2~~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m3) * 1
so k should be in (m3/mol/s).
"""

template(reactants=["Adsorbate", "Proton"], products=["Reduced"], ownReverse=False)

reverse = "Surface_Proton_Electron_Oxidation_Alpha_vdW"

reactantNum = 2
productNum = 1
allowChargedSpecies = True
electrons = -1

recipe(actions=[
    ['LOSE_CHARGE', '*3', 1],
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
])

entry(
    index = 1,
    label = "Adsorbate",
    group =
"""
1 *1 R u0 {2,S}
2 *2 X u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Proton",
    group =
"""
1 *3 H+ u0 p0 c+1
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "CX",
    group =
"""
1 *1 C u0 {2,S}
2 *2 X u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "OX",
    group =
"""
1 *1 O u0 {2,S}
2 *2 X u0 {1,S}
""",
    kinetics = None,
)


entry(
    index = 6,
    label = "NX",
    group =
"""
1 *1 N u0 {2,S}
2 *2 X u0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: Adsorbate
    L2: CX
    L2: OX
    L2: NX

L1: Proton
"""
)
