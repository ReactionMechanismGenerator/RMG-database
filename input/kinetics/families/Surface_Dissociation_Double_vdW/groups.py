#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_Double_vdW/groups"
shortDesc = u""
longDesc = u"""
A vdW double bonded species dissociatively adsorbing to the surface with double
bonds.

*2=*3                      *2          *3
  :     +          ---->   ||    +     ||
~*1~        ~*4~          ~*1~        ~*4~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s).

"""

template(reactants=["AdsorbateVdW","VacantSite"], products=["Adsorbate1","Adsorbate2"], ownReverse=False)

reverse = "Surface_Association_Double_vdW"

reactantNum=2
productNum=2

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*2', -1, '*3'],
    ['BREAK_BOND', '*2', 1, '*3'],
    ['FORM_BOND', '*3', 1, '*4'],
    ['CHANGE_BOND', '*3', 1, '*4'],
])

entry(
    index = 1,
    label = "AdsorbateVdW",
    group =
"""
1 *1 Xv  ux px cx
2 *2 R!H ux px cx {3,D}
3 *3 R!H ux px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "VacantSite",
    group =
"""
1 *4 Xv u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "C=C",
    group =
"""
1 *1 Xv ux px cx
2 *2 C  ux px cx {3,D}
3 *3 C  ux px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "C=O",
    group =
"""
1 *1 Xv ux px cx
2 *2 C  ux px cx {3,D}
3 *3 O  ux px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "O=C=O",
    group =
"""
1    O  u0 p2 c0 {3,D}
2 *3 O  u0 p2 c0 {3,D}
3 *2 C  u0 p0 c0 {1,D} {2,D}
4 *1 Xv u0 p0 c0
""",
    kinetics = None,
)

tree(
"""
L1: AdsorbateVdW
    L2: C=C
    L2: C=O
        L3: O=C=O
L1: VacantSite
"""
)

forbidden(
    label = "O=C",
    group =
"""
1 *1 Xv ux px cx
2 *2 O  ux px cx {3,D}
3 *3 C  ux px cx {2,D}
""",
    shortDesc = u"""""",
    longDesc =u"""
Any O=C should not match *2 and *3 respectively because of duplicate reactions
""",
)
