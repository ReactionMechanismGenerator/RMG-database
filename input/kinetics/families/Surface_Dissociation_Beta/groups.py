#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_Beta/groups"
shortDesc = u""
longDesc = u"""
Surface bond fission of one species into two distinct adsorbates. The bond fission occurs not at the binding atom, but in the beta position of the adsorbate, that is the bond between Atom *2 and *3 is broken. Atom *1 binds to the surface (*4). The image below shows a double bond, but a triple bond is also possible. What matters is that the bond between *2 and *3 must be single.


 *1-*2--*3              *1=*2  *3
  ||            ---->    |      |
~*4~ + ~*5~~           ~*4~ + ~*5~~

The rate, which should be in mol/m2/s, so k should be in (m2/mol/s).
"""

template(reactants=["Combined", "VacantSite"], products=["Adsorbate1","Adsorbate2"], ownReverse=False)

reverse = "Surface_Association_Beta"

reactantNum=2
productNum=2

recipe(actions=[
    ['FORM_BOND', '*3', 1, '*5'],
    ['CHANGE_BOND', '*1', -1, '*4'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*2', 1, '*3']
])

entry(
    index = 1,
    label = "Combined",
    group =
"""
1 *1 R!H u0 {2,S} {4,[D,T]}
2 *2 R!H u0 {1,S} {3,S}
3 *3 R   u0 {2,S}
4 *4 Xo  u0 {1,[D,T]}
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
    label = "C-H",
    group =
"""
1 *1 R!H u0 {2,S} {4,[D,T]}
2 *2 C   u0 {1,S} {3,S}
3 *3 H   u0 {2,S}
4 *4 Xo  u0 {1,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "O-H",
    group =
"""
1 *1 R!H u0 {2,S} {4,[D,T]}
2 *2 O   u0 {1,S} {3,S}
3 *3 H   u0 {2,S}
4 *4 Xo  u0 {1,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "R-H",
    group =
"""
1 *1 R!H u0 {2,S} {4,[D,T]}
2 *2 R!H u0 {1,S} {3,S}
3 *3 H   u0 {2,S}
4 *4 Xo  u0 {1,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "CH3",
    group =
"""
1 *1 R!H u0 px cx {2,S} {6,[D,T]}
2 *2 C   u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 *3 H   u0 p0 c0 {2,S}
4    H   u0 p0 c0 {2,S}
5    H   u0 p0 c0 {2,S}
6 *4 Xo  u0 p0 c0 {1,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "CR-H",
    group =
"""
1 *1 R!H u0 {2,S} {4,D}
2 *2 C   u0 {1,S} {3,S} {5,S}
3 *3 H   u0 {2,S}
4 *4 Xo  u0 {1,D}
5    R!H u0 {2,S}  
""",
    kinetics = None,
)

tree(
"""
L1: Combined
    L2: R-H
      L3: CR-H
      L3: C-H
	L4: CH3
      L3: O-H
L1: VacantSite
"""
)

forbidden(
    label = "R-C",
    group =
"""
1 *1 R!H u0 {2,S} {4,[D,T]}
2 *2 R!H u0 {1,S} {3,S}
3 *3 C   u0 px cx {2,S}
4 *4 Xo  u0 {1,[D,T]}
""",
)

forbidden(
    label = "Bidentate",
    group =
"""
1 *1 R!H u0 {2,S} {4,[D,T]}
2 *2 R!H u0 {1,S} {3,S}
3 *3 R   u0 {2,S}
4 *4 Xo  u0 {1,[D,T]}
5    Xo  u0
"""
)
