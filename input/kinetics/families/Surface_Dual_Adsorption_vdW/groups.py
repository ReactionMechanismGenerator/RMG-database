#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dual_Adsorption_vdW/groups"
shortDesc = u""
longDesc = u"""
Two vdW species reacting together and abstracting a functional group and then forming a single bond to the surface.

*2=*3  *4-*6           *2-*3-*4     *6
  :      :     ---->    |            |
~*1~ + ~*5~~          ~*1~       + ~*5~~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s).

"""

template(reactants=["Adsorbate1","Adsorbate2"], products=["Adsorbate3","Adsorbate4"], ownReverse=False)

reverse = "Surface_Dual_Desorption_vdW"

reactantNum=2
productNum=2

recipe(actions=[
    ['CHANGE_BOND','*2', -1, '*3'],
    ['FORM_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*4', 1, '*6'],
    ['FORM_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*5', 1, '*6'],
])

entry(
    index = 1,
    label = "Adsorbate1",
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
    label = "Adsorbate2",
    group =
"""
1 *5 Xv ux px cx
2 *4 R  ux px cx {3,S}
3 *6 R  ux px cx {2,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "CR",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *2 C   ux px cx {3,[D,T,Q]}
3 *3 R!H ux px cx {2,[D,T,Q]}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "O=R",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *2 O   ux px cx {3,D}
3 *3 R!H ux px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "C=O",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 C  u0 p0 c0 {3,D}
3 *3 O  u0 p2 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "O=C",
    group =
"""
1 *1 Xv u0 p0 c0
2 *2 O  u0 p2 c0 {3,D}
3 *3 C  ux px cx {2,D}
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
    label = "C$",
    group =
"""
1 *1 Xv  u0 p0 c0
2 *2 C   ux px cx {3,Q}
3 *3 R!H ux px cx {2,Q}
""",
    kinetics = None,
)

entry(
    index = 10,
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
    index = 11,
    label = "RR",
    group =
"""
1 *5 Xv  u0 p0 c0
2 *4 R!H ux px cx {3,S}
3 *6 R!H ux px cx {2,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "C-H",
    group =
"""
1 *5 Xv u0 p0 c0
2 *4 C  ux px cx {3,S}
3 *6 H  u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "O-H",
    group =
"""
1 *5 Xv u0 p0 c0
2 *4 O  u0 p2 c0 {3,S}
3 *6 H  u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "HH",
    group =
"""
1 *5 Xv u0 p0 c0
2 *4 H  u0 p0 c0 {3,S}
3 *6 H  u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "RH",
    group =
"""
1 *5 Xv  u0 p0 c0
2 *4 R!H ux px cx {3,S}
3 *6 H   u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "HR",
    group =
"""
1 *5 Xv  u0 p0 c0
2 *4 H   u0 p0 c0 {3,S}
3 *6 R!H ux px cx {2,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "H-C",
    group =
"""
1 *5 Xv u0 p0 c0
2 *4 H  u0 p0 c0 {3,S}
3 *6 C  ux px cx {2,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "H-O",
    group =
"""
1 *5 Xv u0 p0 c0
2 *4 H  u0 p0 c0 {3,S}
3 *6 O  u0 p2 c0 {2,S}
""",
    kinetics = None,
)

tree(
"""
L1: Adsorbate1
    L2: CR
        L3: C=
            L4: C=O
        L3: C#
        L3: C$
    L2: O=R
        L3: O=C
        L3: O=O
L1: Adsorbate2
    L2: RR
    L2: HH
    L2: RH
        L3: C-H
        L3: O-H
    L2: HR
        L3: H-C
        L3: H-O
"""
)
