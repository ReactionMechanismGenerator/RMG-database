#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_vdWBidentate/groups"
shortDesc = u""
longDesc = u"""
Surface bond fission of a vdW bidentate (e.g., formate XOCHXO) into two adsorbates.
Example: [X]~OC(H)O[X] -> [X]O + O=C[X]H
The *1-*2 bond (C-O) breaks. Atom *1 (O) has a single bond to surface site *4 and 
increases to a double bond. Atom *3 (O) has a vdW bond to surface 
site *5. The vdW bond is broke and *2 (C) forms a new bond to *5.

 *1-*2=*3              *1     *2=*3
  |     :     ---->    ||      |
~*4~  ~*5~~           ~*4~ + ~*5~~


The rate, which should be in mol/m2/s,
will be given by k * (mol/m2)
so k should be in (1/s)
"""

template(reactants=["Combined"], products=["Adsorbate1", "Adsorbate2"], ownReverse=False)

reverse = "Surface_Association_vdWBidentate"

reactantNum=1
productNum=2

recipe(actions=[
    ['CHANGE_BOND', '*1', 1, '*4'],
    ['BREAK_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*3', 1, '*5'],
    ['BREAK_BOND', '*3', 1, '*5'],
    ['FORM_BOND', '*2', 1, '*5'],
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
1 *1 O   u0 p2 {2,S} {4,S}
2 *2 R!H u0 {1,S} {3,D}
3 *3 O   u0 p2 {2,D} {5,vdW}
4 *4 X  u0 {1,S}
5 *5 X  u0 {3,vdW}
""",
    kinetics = None,
)

tree(
"""
L1: Combined
"""
)
