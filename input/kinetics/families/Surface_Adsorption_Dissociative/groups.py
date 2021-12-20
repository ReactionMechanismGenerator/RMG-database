#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Dissociative/groups"
shortDesc = u""
longDesc = u"""
Dissociative adsorption of a gas-phase species onto the surface. The single-bond
in the gas-phase species is split; the resulting fragments each are singled
bonded to the surface.

 *1-*2               *1      *2
             ---->    |       |
~*3~ + ~*4~         ~*3~~ + ~*4~~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2) * (mol/m3)
so k should be in (m5/mol2/s). We will use sticking coefficients.

For now, so there aren't duplicate reactions, the heavy atom will match *1
"""

template(reactants=["Adsorbate", "VacantSite1", "VacantSite2"],
         products=["Adsorbed1", "Adsorbed2"], ownReverse=False)

reverse = "Surface_Desorption_Associative"

reactantNum=3
productNum=2

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4']
])

entry(
    index = 1,
    label = "Adsorbate",
    group =
"""
multiplicity [1]
1 *1 R u0 px cx {2,S}
2 *2 R u0 px cx {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="VacantSite1",
    group =
"""
1 *3 Xv u0
""",
    kinetics = None,
)

entry(
    index = 3,
    label="VacantSite2",
    group =
"""
1 *4 Xv u0
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "H2",
    group =
"""
multiplicity [1]
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    kinetics = None,
)


entry(
    index = 5,
    label = "CH4",
    group =
"""
multiplicity [1]
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "C2H6",
    group =
"""
multiplicity [1]
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "C3H8",
    group =
"""
multiplicity [1]
1  *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3     C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    kinetics = None,
)

#entry(
#    index = 5,
#    label = "O",
#    group =
#"""
#multiplicity [1]
#1 *1 O u0 p2 c0 {2,S}
#2 *2 R u0 {1,S}
#""",
#    kinetics = None,
#)

#entry(
#    index = 6,
#    label = "O-H",
#    group =
#"""
#multiplicity [1]
#1 *1 O u0 p2 c0 {2,S}
#2 *2 H u0 p0 c0 {1,S}
#""",
#    kinetics = None,
#)

#entry(
#    index = 7,
#    label = "H2O",
#    group =
#"""
#multiplicity [1]
#1 *1 O u0 p2 c0 {2,S} {3,S}
#2 *2 H u0 p0 c0 {1,S}
#3    H u0 p0 c0 {1,S}
#""",
#    kinetics = None,
#)

# entry(
#     index = 8,
#     label = "O-O",
#     group =
# """
# 1 *1 O u0 {2,S}
# 2 *2 O u0 {1,S}
# """,
#     kinetics = None,
# )

#entry(
#    index = 9,
#    label = "O-N",
#    group =
#"""
#multiplicity [1]
#1 *1 O u0 p2 c0 {2,S}
#2 *2 N u0 p1 c0 {1,S}
#""",
#    kinetics = None,
#)

#entry(
#    index = 10,
#    label = "O-C",
#    group =
#"""
#multiplicity [1]
#1 *1 O u0 p2 c0 {2,S}
#2 *2 C u0 p0 c0 {1,S}
#""",
#    kinetics = None,
#)

#entry(
#    index = 11,
#    label = "N",
#    group =
#"""
#multiplicity [1]
#1 *1 N u0 px cx {2,S}
#2 *2 R u0 {1,S}
#""",
#    kinetics = None,
#)

#entry(
#    index = 12,
#    label = "N-C",
#    group =
#"""
#multiplicity [1]
#1 *1 N u0 p2 c0 {2,S}
#2 *2 C u0 p0 c0 {1,S}
#""",
#    kinetics = None,
#)

#entry(
#    index = 13,
#    label = "N-H",
#    group =
#"""
#multiplicity [1]
#1 *1 N u0 p2 c0 {2,S}
#2 *2 H u0 p0 c0 {1,S}
#""",
#    kinetics = None,
#)

#entry(
#    index = 14,
#    label = "C-H",
#    group =
#"""
#multiplicity [1]
#1 *1 C u0 p0 c0 {2,S}
#2 *2 H u0 p0 c0 {1,S}
#""",
#    kinetics = None,
#)

tree(
"""
L1: Adsorbate
    L2: H2
    L2: CH4
    L2: C2H6
    L2: C3H8
L1: VacantSite1
L1: VacantSite2
"""
)

forbidden(
    label = "H2O",
    group =
"""
multiplicity [1]
1 *1 O u0 p2 c0 {2,S} {3,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
"""
)

forbidden(
    label = "adjacentradical1",
    group =
"""
1 *1 R u0 {2,[S,D,T]}
2    R u1 {1,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The adsorbing atom should not be adjacent to a radical.
e.g. this is not allowed:

CH2.-CH3    -->   CH2.-CH2   +   H
                       |         |
     X X               X         X
""",
)

forbidden(
    label = "adjacentradical2",
    group =
"""
1 *2 R u0 {2,[S,D,T]}
2    R u1 {1,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Neither adsorbing atom should be adjacent to a radical
e.g. this is not allowed:

CH2.-CH3    -->   CH2.-CH2   +   H
                       |         |
     X X               X         X
""",
)

forbidden(
    label = "disigma1",
    group =
"""
1 *1 R u0 {2,[S,D,T]}
2    R u0 {1,[S,D,T]} {3,[S,D,T]}
3    X u0 {2,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The adsorbing atom should not be adjacent to an atom that is already adsorbed.
e.g. this is not allowed:

H  O=C-O   <-->  O=CH-O
|    | |              |
X    X X         X X  X
""",
)

forbidden(
    label = "disigma2",
    group =
"""
1 *2 R u0 {2,[S,D,T]}
2    R u0 {1,[S,D,T]} {3,[S,D,T]}
3    X u0 {2,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The adsorbing atom should not be adjacent to an atom that is already adsorbed.
e.g. this is not allowed:

H  O=C-O   <-->  O=CH-O
|    | |              |
X    X X         X X  X
""",
)

forbidden(
    label = "disigma3",
    group =
"""
1 *1 R u0 {2,[S,D,T]}
2    R u0 {1,[S,D,T]} {3,[S,D,T]}
3    R u0 {2,[S,D,T]} {4,[S,D,T]}
4    X u0 {3,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The adsorbing atom should not be next-nearest neighbor to an atom that is already adsorbed.
""",
)

forbidden(
    label = "disigma4",
    group =
"""
1 *2 R u0 {2,[S,D,T]}
2    R u0 {1,[S,D,T]} {3,[S,D,T]}
3    R u0 {2,[S,D,T]} {4,[S,D,T]}
4    X u0 {3,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The adsorbing atom should not be next-nearest neighbor to an atom that is already adsorbed.
""",
)

forbidden(
    label = "N-O",
    group =
"""
1 *2 O u0 {2,S}
2 *1 N u0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
O should not match to *2 with a less heavy atom
""",
)

forbidden(
    label = "C-O",
    group =
"""
1 *2 O u0 {2,S}
2 *1 C u0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
O should not match to *2 with a less heavy atom
""",
)

forbidden(
    label = "H-O",
    group =
"""
1 *2 O u0 {2,S}
2 *1 H u0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
O should not match to *2 with a less heavy atom
""",
)

forbidden(
    label = "C-N",
    group =
"""
1 *2 N u0 {2,S}
2 *1 C u0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
N should not match to *2 with a less heavy atom
""",
)

forbidden(
    label = "H-N",
    group =
"""
1 *2 N u0 {2,S}
2 *1 H u0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
N should not match to *2 with a less heavy atom
""",
)

forbidden(
    label = "H-C",
    group =
"""
1 *2 C u0 {2,S}
2 *1 H u0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
C should not match to *2 with a less heavy atom
""",
)

forbidden(
    label = "chargedBond",
    group =
"""
1 *1 R!H ux c[+1,-1] {2,[S,D,T]}
2 *2 R!H ux c[+1,-1] {1,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The adsorbing molecule should not have a charge on the surface.
""",
)
