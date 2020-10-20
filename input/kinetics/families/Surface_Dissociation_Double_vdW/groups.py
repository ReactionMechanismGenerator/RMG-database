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
multiplicity [1]
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

# entry(
#     index = 3,
#     label = "CC",
#     group =
# """
# 1 *1 Xv u0 p0 c0
# 2 *2 C  u0 p0 c0 {3,D}
# 3 *3 C  u0 p0 c0 {2,D}
# """,
#     kinetics = None,
# )

entry(
    index = 4,
    label = "OC",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *3 C  u0 p0 c0 {3,D}
3 *2 O  u0 p2 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "CO2",
    group =
"""
multiplicity [1]
1    O  u0 p2 c0 {3,D}
2 *2 O  u0 p2 c0 {3,D}
3 *3 C  u0 p0 c0 {1,D} {2,D}
4 *1 Xv u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "NC",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *2 N  u0 p1 c0 {3,D}
3 *3 C  u0 p0 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "ON",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *3 N  u0 px cx {3,D}
3 *2 O  u0 p2 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "ONR",
    group =
"""
multiplicity [1]
1 *1 Xv u0 p0 c0
2 *3 N  u0 p1 c0 {3,D} {4,S}
3 *2 O  u0 p2 c0 {2,D}
4    R  u0 px c0 {2,S}
""",
    kinetics = None,
)

tree(
"""
L1: AdsorbateVdW
    L2: OC
        L3: CO2
    L2: ON
        L3: ONR
    L2: NC
L1: VacantSite
"""
)

forbidden(
    label = "CO",
    group =
"""
1 *1 Xv ux
2 *3 O  ux {3,D}
3 *2 C  ux {2,D}
""",
    shortDesc = u"""""",
    longDesc =u"""
Any CO should not match *2 and *3 respectively because of duplicate reactions
""",
)

forbidden(
    label = "NO",
    group =
"""
1 *1 Xv ux
2 *3 O  ux {3,D}
3 *2 N  ux {2,D}
""",
    shortDesc = u"""""",
    longDesc =u"""
Any NO should not match *2 and *3 respectively because of duplicate reactions
""",
)

forbidden(
    label = "CN",
    group =
"""
1 *1 Xv ux
2 *3 N  ux {3,D}
3 *2 C  ux {2,D}
""",
    shortDesc = u"""""",
    longDesc =u"""
Any CN should not match *2 and *3 respectively because of duplicate reactions
""",
)

forbidden(
    label = "chargedBond",
    group =
"""
1 *2 R!H ux c[+1,-1] {2,[S,D,T]}
2 *3 R!H ux c[+1,-1] {1,[S,D,T]}
3 *1 Xv  u0 p0 c0
""",
    shortDesc = u"""""",
    longDesc =
u"""
The adsorbing molecule should not have a charge on the surface.
""",
)
