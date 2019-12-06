#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_vdW/groups"
shortDesc = u""
longDesc = u"""
A vdW species splitting, adsorbing to the surface, and transferring a functional group to a double, triple, or
quadruple bonded surface species.

 *2-*3  *4             *2     *4-*3
  :     ||     ---->    |      |
~*1~ + ~*5~~          ~*1~ + ~*5~~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s).

"""

template(reactants=["AdsorbateVdW","Adsorbate1"], products=["Adsorbate2","Adsorbate3"], ownReverse=False)

reverse = "Surface_Reverse_Abstraction_vdW"  # maybe needs a better name?

reactantNum=2
productNum=2

recipe(actions=[
    ['BREAK_BOND', '*2', 1, '*3'],
    ['FORM_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*4', -1, '*5'],
    ['FORM_BOND', '*3', 1, '*4'],
])

entry(
    index = 1,
    label = "AdsorbateVdW",
    group =
"""
1 *1 Xv ux px cx
2 *2 R  ux px cx {3,S}
3 *3 R  ux px cx {2,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Adsorbate1",
    group =
"""
1 *5 X   ux px cx {2,[D,T,Q]}
2 *4 R!H ux px cx {1,[D,T,Q]}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "O-R",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 O  ux p2 cx {3,S}
3 *3 R  ux px cx {2,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "C-R",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 C  ux px cx {3,S}
3 *3 R  ux px cx {2,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "O=*",
    group =
"""
1 *5 X u0 p0 c0 {2,D}
2 *4 O u0 p2 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "C=*",
    group =
"""
1 *5 X u0 p0 c0 {2,[D,T,Q]}
2 *4 C ux px cx {1,[D,T,Q]}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "H-H",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 H  u0 p0 c0 {3,S}
3 *3 R  ux px cx {2,S}
""",
    kinetics = None,
)

tree(
"""
L1: AdsorbateVdW
    L2: H-H
    L2: O-R
    L2: C-R
L1: Adsorbate1
    L2: O=*
    L2: C=*
"""
)
