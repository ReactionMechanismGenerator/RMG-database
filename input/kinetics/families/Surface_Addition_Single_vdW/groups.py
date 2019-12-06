#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Addition_Single_vdW/groups"
shortDesc = u""
longDesc = u"""
A single bonded surface species adding to a vdW double, triple, or quadruple bonded species and adsorbing to a surface.

*2=*3       *4              *2-*3-*4
  :     +    |     ---->    |         +
~*1~       ~*5~           ~*1~            ~*5~  

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s).

"""

template(reactants=["AdsorbateVdW","Adsorbate1"], products=["VacantSite","Adsorbate2"], ownReverse=False)

reverse = "Surface_Deletion_Single_vdW"

reactantNum=2
productNum=2

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*2', -1, '*3'],
    ['FORM_BOND', '*3', 1, '*4'],
    ['BREAK_BOND', '*4', 1, '*5'],
])

entry(
    index = 1,
    label = "AdsorbateVdW",
    group =
"""
1 *1 Xv  ux px cx
2 *2 R!H ux px cx {3,[D,T,Q]}
3 *3 R!H ux px cx {2,[D,T,Q]}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Adsorbate1",
    group =
"""
1 *5 X ux px cx {2,S}
2 *4 R ux px cx {1,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "O=R",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *2 O   ux p2 cx {3,D}
3 *3 R!H ux px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "C=R",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *2 C   ux px cx {3,[D,T,Q]}
3 *3 R!H ux px cx {2,[D,T,Q]}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "O=C=O",
    group =
"""
1    O  u0 p2 c0 {3,D}
2 *2 O  u0 p2 c0 {3,D}
3 *3 C  u0 p0 c0 {1,D} {2,D}
4 *1 Xv u0 p0 c0
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "H",
    group =
"""
1 *5 X  u0 p0 c0 {2,S}
2 *4 H  u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "O=C",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 O  ux p2 cx {3,D}
3 *3 C  ux px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "O",
    group =
"""
1 *5 X  u0 p0 c0 {2,S}
2 *4 O  u0 px c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "OH",
    group =
"""
1 *5 X  u0 p0 c0 {2,S}
2 *4 O  u0 p2 c0 {1,S} {3,S}
3    H  u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "C=O",
    group =
"""
1 *1 Xv u0 p0 c0
2 *3 O  ux p2 cx {3,D}
3 *2 C  ux px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "CO2",
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
    L2: C=R
        L3: C=O
            L4: CO2
    L2: O=R
        L3: O=C
            L4: O=C=O
L1: Adsorbate1
    L2: H
    L2: O
        L3: OH
"""
)

# forbidden(
#     label = "O=C",
#     group =
# """
# 1 *1 Xv ux px cx
# 2 *2 O  ux px cx {3,D}
# 3 *3 C  ux px cx {2,D}
# """,
#     shortDesc = u"""""",
#     longDesc =u"""
# Any O=C should not match *2 and *3 respectively because of duplicate reactions
# """,
# )

