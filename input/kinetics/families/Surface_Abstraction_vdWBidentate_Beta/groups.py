#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_vdWBidentate_Beta/groups"
shortDesc = u""
longDesc = u"""
Surface abstraction of the beta R!H-R atom of a vdW bidentate by a neighboring surface adsorbate. 
Example:  [X]~OC(H)O[X] + O=[X]-> OCO.[X] + O[X] + [X]
The bond fission occurs at the beta position: the R!H-H bond (*2-*4) breaks, and *4 (R) 
is transferred to the abstracting adsorbate *7, which weakens its own surface bond (*7-*8) upon 
gaining R. Simultaneously, the *1-*2 bond (O-R) strengthens and *3 (O) detaches from surface 
site *6, releasing CO2. A vacant site (*6) is produced as a product.

    *4
     |
 *1-*2=*3          *7            *1=*2=*3    *7-*4
  |     :          ||      ---->              |
~*5~ +~*6~  +     ~*8~~           ~*5~  +   ~*8~~  + ~*6~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s). 
"""

template(reactants=["Donating", "Abstracting"], products=["Adsorbate2","Adsorbate3", "VacantSite"], ownReverse=False)

reverse = "Surface_Abstraction_vdWBidentate_reverse_Beta"

reactantNum=2
productNum=3

recipe(actions=[
    ['FORM_BOND', '*4', 1, '*7'],
    ['CHANGE_BOND', '*7', -1, '*8'],
    ['CHANGE_BOND', '*1', -1, '*5'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*3', 1, '*6'],
    ['BREAK_BOND', '*3', 1, '*6'],
    ['BREAK_BOND', '*2', 1, '*4'],
])

entry(
    index = 1,
    label = "Donating",
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

entry(
    index = 2,
    label="Abstracting",
    group =
"""
1 *8 Xo  u0 {2,[D,T,Q]}
2 *7 R!H u0 px c0 {1,[D,T,Q]}	
""",
    kinetics = None,
)

tree(
"""
L1: Abstracting
L1: Donating
"""
)