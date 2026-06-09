#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_vdW_to_vdWBidentate/groups"
shortDesc = u""
longDesc = u"""
Dissociation of a physisorbed species (e.g., formic acid HCOOH) into a vdW bidentate (e.g., formate XOCHXO)
Example: HOC(H)O.[X] + [X] + [X] -> [X]~OC(H)O[X] + [X]H
and an adsorbate with a single bond to the surface (e.g., XH). The formic acid is initially physisorbed via a vdW 
interaction through the carbonyl oxygen (*3). Upon dissociation, the R!H-R bond (*1-*4) breaks, 
the R!H (*1) forms a single bond to the surface site (*5), the carbonyl oxygen (*3) 
retains a vdW interaction with a neighboring vacant site (*6), and the R (*4) adsorbs 
onto a second vacant site (*7), yielding bidentate formate.

 *4-*1--*2=*3                                *1-*2=*3      *4
     :                             ---->      |     :       |
   ~*5~    +   ~*6~~    +   ~*7~~           ~*5~  ~*6~ +  ~*7~


The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)* (mol/m2)
so k should be in (m4/mol2/s)
"""

template(reactants=["Combined", "VacantSite1", "VacantSite2"], products=["Adsorbate1", "Adsorbate2"], ownReverse=False)

reverse = "Surface_Association_vdWBidentate_to_vdW"

reactantNum=3
productNum=2

recipe(actions=[
    ['CHANGE_BOND', '*1', 1, '*5'],
    ['BREAK_BOND', '*1', 1, '*4'],
    ['FORM_BOND', '*4', 1, '*7'],
    ['FORM_BOND', '*3', 1, '*6'],
    ['CHANGE_BOND', '*3', -1, '*6'],
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
multiplicity [1]
1 *1 R!H u0 px c0 {2,S} {4,S}
2 *2 R!H u0 px c0 {1,S} {3,D}
3 *3 O  u0 p2 c0 {2,D}
4 *4 R   u0 px c0 {1,S}
5 *5 Xv  u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite1",
    group =
"""
1 *6 Xv u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 3,
    label="VacantSite2",
    group =
"""
1 *7 Xv u0 p0 c0
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

