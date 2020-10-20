#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_Beta/groups"
shortDesc = u""
longDesc = u"""
Surface bond fission of one species into two distinct adsorbates. The bond fission occurs not at the binding atom, but in the beta position of the adsorbate, that is the bond between Atom *2 and *3 is broken. Atom *1 is bonded to the surface (*4). The image below shows a double bond, but a triple bond is also possible. What matters is that the bond between *2 and *3 must be single.


 *2=*3      *4           *2-*3-*4
  |     +    |   ---->   ||       +
~*1~       ~*5~         ~*1~        ~*5~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2) * (mol/m3)
so k should be in (m5/mol2/s). We will use sticking coefficients.
"""

template(reactants=["Adsorbate1", "Adsorbate2"], products=["Adsorbate3","VacantSite"], ownReverse=False)

reverse = "Surface_Association_Beta"

reactantNum=2
productNum=2

recipe(actions=[
    ['CHANGE_BOND', '*2', -1, '*3'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*4', 1, '*5'],
    ['FORM_BOND', '*3', 1, '*4'],
])

entry(
    index = 1,
    label = "Adsorbate1",
    group =
"""
1 *1 Xo   ux p0 c0 {2,[S,D]}
2 *2 R!H ux px cx {1,[S,D]} {3,[D,T]}
3 *3 R!H ux px cx {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="Adsorbate2",
    group =
"""
1 *5 Xo ux px cx {2,S}
2 *4 R ux px cx {1,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "*C",
    group =
"""
1 *1 Xo   ux p0 c0 {2,[S,D]}
2 *2 C   ux px cx {1,[S,D]} {3,[D,T]}
3 *3 R!H ux px cx {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "*-C=",
    group =
"""
1 *1 Xo   ux p0 c0 {2,S}
2 *2 C   u0 p0 c0 {1,S} {3,D}
3 *3 R!H ux px cx {2,D}
""",
    kinetics = None,
)


entry(
    index = 5,
    label = "*-C=O",
    group =
"""
1 *1 Xo ux p0 c0 {2,S}
2 *2 C u0 p0 c0 {1,S} {3,D}
3 *3 O ux px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "*-C=C",
    group =
"""
1 *1 Xo ux p0 c0 {2,S}
2 *2 C u0 p0 c0 {1,S} {3,D}
3 *3 C u0 p0 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "*-C#",
    group =
"""
1 *1 Xo ux p0 c0 {2,S}
2 *2 C u0 p0 c0 {1,S} {3,T}
3 *3 C ux px cx {2,T}
""",
    kinetics = None,
)

entry(
    index = 8,
    label="H-*",
    group =
"""
1 *5 Xo u0 p0 c0 {2,S}
2 *4 H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label="O-*",
    group =
"""
1 *5 Xo u0 p0 c0 {2,S}
2 *4 O u0 p2 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label="C-*",
    group =
"""
1 *5 Xo u0 p0 c0 {2,S}
2 *4 C u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "*-C",
    group =
"""
1 *1 Xo  ux p0 c0 {2,S}
2 *2 C   ux px cx {1,S} {3,[D,T]}
3 *3 R!H ux px cx {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "*=C",
    group =
"""
1 *1 Xo  ux p0 c0 {2,D}
2 *2 C   ux px cx {1,D} {3,D}
3 *3 R!H ux px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "*=C=C",
    group =
"""
1 *1 Xo ux p0 c0 {2,D}
2 *2 C  ux px cx {1,D} {3,D}
3 *3 C  ux px cx {2,D}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "*=C=O",
    group =
"""
1 *1 Xo u0 p0 c0 {2,D}
2 *2 C  u0 px c0 {1,D} {3,D}
3 *3 O  u0 p2 c0 {2,D}
""",
    kinetics = None,
)

tree(
"""
L1: Adsorbate1
    L2: *C
        L3: *-C
            L4: *-C=
                L5: *-C=O
                L5: *-C=C
            L4: *-C#
        L3: *=C
            L4: *=C=C
            L4: *=C=O
L1: Adsorbate2
    L2: H-*
    L2: O-*
    L2: C-*
"""
)
