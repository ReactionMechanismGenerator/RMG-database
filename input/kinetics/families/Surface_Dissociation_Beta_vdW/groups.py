#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_Beta_vdW/groups"
shortDesc = u""
longDesc = u"""
Surface bond fission of one species into two adsorbates. The bond fission occurs not at the binding atom, but in the beta position of the adsorbate, that is the bond between Atom *2 and *3 is broken. Molecule *1-2 forms a vdW bond to the surface (*4). The bond between *2 and *3 must be single.


 *1-*2--*3              *1=*2  *3
  |             ---->    :      |
~*4~ + ~*5~~           ~*4~ + ~*5~~

The rate should be in mol/m2/s, so k should be in (m2/mol/s). 
"""

template(reactants=["Combined", "VacantSite"], products=["Adsorbate1","Adsorbate2"], ownReverse=False)

reverse = "Surface_Association_Beta_vdW"

reactantNum=2
productNum=2

recipe(actions=[
    ['FORM_BOND', '*3', 1, '*5'],
    ['BREAK_BOND', '*1', 1, '*4'],
    ['FORM_BOND', '*1', 0, '*4'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*2', 1, '*3']
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
1 *1 R!H u0 px cx {2,S} {4,S}
2 *2 R!H u0 px cx {1,S} {3,S}
3 *3 R   u0 {2,S}
4 *4 Xo  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite",
    group =
"""
1 *5 Xv u0
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "R-H",
    group =
"""
1 *1 R!H u0 {2,S} {4,S}
2 *2 R!H u0 {1,S} {3,S}
3 *3 H   u0 {2,S}
4 *4 Xo  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "C-H",
    group =
"""
1 *1 R!H u0 {2,S} {4,S}
2 *2 C   u0 {1,S} {3,S}
3 *3 H   u0 {2,S}
4 *4 Xo  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "CH3",
    group =
"""
1 *1 R!H u0 px cx {2,S} {6,S}
2 *2 C   u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 *3 H   u0 p0 c0 {2,S}
4    H   u0 p0 c0 {2,S}
5    H   u0 p0 c0 {2,S}
6 *4 Xo  u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "O-H",
    group =
"""
1 *1 R!H u0 {2,S} {4,S}
2 *2 O   u0 px {1,S} {3,S}
3 *3 H   u0 {2,S}
4 *4 Xo  u0 {1,S}
""",
    kinetics = None,
)


tree(
"""
L1: Combined
	L2: R-H
	   L3: C-H
		L4: CH3
	   L3: O-H
L1: VacantSite
"""
)

forbidden(
    label = "Bidentate",
    group =
"""
1 *1 R!H u0 px cx {2,S} {4,S}
2 *2 R!H u0 px cx {1,S} {3,S}
3 *3 R   u0 {2,S}
4 *4 Xo  u0 {1,S}
5    Xo  u0
""",
)

