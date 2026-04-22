#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_Charge_Single/groups"
shortDesc = u""
longDesc = u"""
Surface bond fission of one species into two distinct adsorbates.
Atom *1 is bonded to the surface (*3). The bond between *1 and *2
must be single, and the bond between *4 and *1 must have
charge separation across it.

*4[-]--*1[+]--*2               *4 --*1      *2
        ||            ---->          |       |
       ~*3~ + ~*5~~                ~*3~  + ~*5~~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Combined", "VacantSite"], products=["Adsorbate1", "Adsorbate2"], ownReverse=False)

reverse = "Surface_Association_Charge_Single"

reactantNum=2
productNum=2

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*2', 1, '*5'],
    ['LOSE_PAIR','*4','1'],
    ['GAIN_PAIR', '*1', '1'],
    ['CHANGE_BOND', '*1', -1, '*3'],
    ['CHANGE_BOND', '*1', 1, '*4'],
    ['LOSE_CHARGE','*1','1'],
    ['GAIN_CHARGE', '*4', '1'],
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
1 *1 Val5 u0 p0 c+1 {2,S} {3,D} {4,S}
2 *2 R u0 px c0 {1,S}
3 *3 Xo u0 p0 c0 {1,D}
4 *4 R!H u0 p[1,2,3] c-1 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite",
    group =
"""
1 *5 Xv u0 p0 c0
""",
    kinetics = None,
)

tree(
"""
L1: Combined
L1: VacantSite
"""
)

forbidden(
    label = "Surf",
    group =
"""
1 *1 Val5 u0 p0 c+1 {2,S} {3,D} {4,S}
2 *2 R u0 px c0 {1,S} {5,[S,D,T]}
3 *3 Xo u0 p0 c0 {1,D}
4 *4 R!H u0 px c-1 {1,S}
5 Xo u0 c0 {2,[S,D,T]}
""",
)
