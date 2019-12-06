#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Abstraction_vdW/groups"
shortDesc = u""
longDesc = u"""
Adsorbtion of a vdw species to the surface with a surface species.

*2=*3    *4-*5        *2-*3-*5    *4
  :   +   |    ---->   |       +  ||
~*1~    ~*6~         ~*1~~       ~*6~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m3)
so k should be in (m3/mol/s). We will use sticking coefficients.
"""

template(reactants=["AdsorbateVdW", "Adsorbate1"], products=["Adsorbate2","Adsorbate3"], ownReverse=False)

reverse = "Surface_Desorption_Abstraction_vdW"

reactantNum=2
productNum=2

recipe(actions=[
    ['CHANGE_BOND', '*2', -1, '*3'],
    ['FORM_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*4', 1, '*5'],
    ['FORM_BOND', '*3', 1, '*5'],
    ['CHANGE_BOND', '*4', 1, '*6'],
])

entry(
    index = 1,
    label = "AdsorbateVdW",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *2 R!H ux px cx {3,[D,T]}
3 *3 R!H ux px cx {2,[D,T]}

""",
    kinetics = None,
)

entry(
    index = 2,
    label="Adsorbate1",
    group =
"""
1 *6 Xo  ux px cx {2,S}
2 *4 R!H ux px cx {1,S} {3,S}
3 *5 R   ux px cx {2,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "O=",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *2 O   ux px cx {3,D}
3 *3 R!H ux px cx {2,D}

""",
    kinetics = None,
)

entry(
    index = 4,
    label = "C",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *2 C   ux px cx {3,[D,T]}
3 *3 R!H ux px cx {2,[D,T]}

""",
    kinetics = None,
)

entry(
    index = 5,
    label = "O=C",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 O  ux px cx {3,D}
3 *3 C  ux px cx {2,D}

""",
    kinetics = None,
)

entry(
    index = 6,
    label = "O=O",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0 {3,D}
3 *3 O  u0 p2 c0 {2,D}

""",
    kinetics = None,
)

entry(
    index = 7,
    label = "C=",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *2 C   ux px cx {3,D}
3 *3 R!H ux px cx {2,D}

""",
    kinetics = None,
)

entry(
    index = 8,
    label = "C#",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *2 C   ux px cx {3,T}
3 *3 R!H ux px cx {2,T}

""",
    kinetics = None,
)

entry(
    index = 9,
    label="C-R",
    group =
"""
1 *6 Xo u0 p0 c0 {2,S}
2 *4 C  ux px cx {1,S} {3,S}
3 *5 R  ux px cx {2,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label="O-R",
    group =
"""
1 *6 Xo u0 p0 c0 {2,S}
2 *4 O  u0 p2 c0 {1,S} {3,S}
3 *5 R  ux px cx {2,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label="C-H",
    group =
"""
1 *6 Xo u0 p0 c0 {2,S}
2 *4 C  u0 p0 c0 {1,S} {3,S}
3 *5 H  u0 p0 c0 {2,S}
""",
    kinetics = None,
)

tree(
"""
L1: AdsorbateVdW
    L2: O=
        L3: O=C
        L3: O=O
    L2: C
        L3: C=
        L3: C#
L1: Adsorbate1
    L2: C-R
        L3: C-H
    L2: O-R
"""
)
