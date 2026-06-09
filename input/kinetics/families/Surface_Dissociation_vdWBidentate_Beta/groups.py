#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_vdWBidentate_Beta/groups"
shortDesc = u""
longDesc = u"""
Surface bond fission of a vdW bidentate adsorbate via beta-scission into a physisorbed species and an adsorbate with a single bond.
Example: [X]~OC(H)O[X] -> OCO.[X] + H[X]
The *1-*2 bond order (O-C) increases as *2 (C) releases *4 (R), 
and the *3 (O) vdW bond 'breaks', releasing the physisorbed species.
    *4
     |
 *1-*2=*3           *1=*2=*3  *4
  |     :     ---->            |
~*5~  ~*6~~           ~*5~ + ~*6~~


The rate, which should be in mol/m2/s,
will be given by k * (mol/m2)
so k should be in (1/s)
"""

template(reactants=["Combined"], products=["Adsorbate1", "Adsorbate2"], ownReverse=False)

reverse = "Surface_Association_vdWBidentate_Beta"

reactantNum=1
productNum=2

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*5'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*2', 1, '*4'],
    ['CHANGE_BOND', '*3', 1, '*6'],
    ['BREAK_BOND', '*3', 1, '*6'],
    ['FORM_BOND', '*4', 1, '*6'],
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
1 *1 O   u0 p2 {2,S} {5,S}
2 *2 R!H u0 {1,S} {3,D} {4,S}
3 *3 O   u0 p2 {2,D} {6,vdW}
4 *4 R u0 {2,S}
5 *5 X  u0 {1,S}
6 *6 X  u0 {3,vdW}
""",
    kinetics = None,
)

tree(
"""
L1: Combined
"""
)
