#!/usr/bin/env python
# encoding: utf-8

name = "Surface_vdW_to_Bidentate/groups"
shortDesc = u""
longDesc = u"""
If a vdW adsorbate has an internal double or a triple bond, reduce the bond order and make it bidentate. 

 *1#*2                   *1==*2
   :            ---->     |  |
 ~*3~ + ~*4~~           ~*3~~*4~~


The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Combined", "VacantSite"], products=["Adsorbate"], ownReverse=False)

reverse = "Surface_Bidentate_to_vdW"

recipe(actions=[
    ['CHANGE_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4'],
    ['CHANGE_BOND', '*1', -1, '*2'],
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
1 *1 R!H  u0 {2,[D,T]}
2 *2 R!H  u0 {1,[D,T]}
3 *3 Xv   u0
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite",
    group =
"""
1 *4 Xv u0
""",
    kinetics = None,
)


tree(
"""
L1: Combined

L1: VacantSite
"""
)
