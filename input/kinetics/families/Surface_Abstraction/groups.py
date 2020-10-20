#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction/groups"
shortDesc = u""
longDesc = u"""
Two adsorbates react. One has a multiple bond to the surface, the other has a
single-bond to the surface and some functional group.
The functional group is transferred from the single
to the multiple-bonded species.
 *1   *4-*3             *1-*4  *3
 ||       |      ---->   |     ||
~*2~~ + ~*5~~          ~*2~ + ~*5~~
The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m2)
so k should be in (m2/mol/s)
"""

template(reactants=["Abstracting", "Donating"], products=["Abstracting", "Donating"], ownReverse=True)

reactantNum=2
productNum=2

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*4'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['CHANGE_BOND', '*3', +1, '*5'],
])

entry(
    index = 1,
    label = "Abstracting",
    group =
"""
1 *1 R!H ux px cx {2,[D,T,Q]}
2 *2 Xo  u0 p0 c0 {1,[D,T,Q]}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="Donating",
    group =
"""
1 *4 R   ux px cx {2,S}
2 *3 R!H ux px cx {1,S} {3,[S,D,T]}
3 *5 Xo  u0 p0 c0 {2,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 3,
    label="*R-H",
    group =
"""
1 *4 H   u0 p0 c0 {2,S}
2 *3 R!H ux px cx {1,S} {3,[S,D,T]}
3 *5 Xo  u0 p0 c0 {2,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 4,
    label="*R-O",
    group =
"""
1 *4 O   u0 p2 c0 {2,S}
2 *3 R!H ux px cx {1,S} {3,[S,D,T]}
3 *5 Xo  u0 p0 c0 {2,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 5,
    label="*R-OH",
    group =
"""
1 *4 O   u0 p2 c0 {2,S} {4,S}
2 *3 R!H ux px cx {1,S} {3,[S,D,T]}
3 *5 Xo  u0 p0 c0 {2,[S,D,T]}
4    H   u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label="*R-C",
    group =
"""
1 *4 C   ux px cx {2,S}
2 *3 R!H ux px cx {1,S} {3,[S,D,T]}
3 *5 Xo  u0 p0 c0 {2,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "C",
    group =
"""
1 *1 C  ux px cx {2,[D,T,Q]}
2 *2 Xo u0 p0 c0 {1,[D,T,Q]}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "N",
    group =
"""
1 *1 N  ux px cx {2,[D,T]}
2 *2 Xo u0 p0 c0 {1,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "O",
    group =
"""
1 *1 O  u0 p2 c0 {2,D}
2 *2 Xo u0 p0 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 10,
    label="*R-N",
    group =
"""
1 *4 N   ux px cx {2,S}
2 *3 R!H ux px cx {1,S} {3,[S,D,T]}
3 *5 Xo  u0 p0 c0 {2,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 11,
    label="*C-H",
    group =
"""
1 *4 H  u0 p0 c0 {2,S}
2 *3 C  u0 p0 c0 {1,S} {3,[S,D,T]}
3 *5 Xo u0 p0 c0 {2,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 12,
    label="*N-H",
    group =
"""
1 *4 H  u0 p0 c0 {2,S}
2 *3 N  u0 p1 c0 {1,S} {3,[S,D]}
3 *5 Xo u0 p0 c0 {2,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 13,
    label="*OH",
    group =
"""
1 *4 H  u0 p0 c0 {2,S}
2 *3 O  u0 p2 c0 {1,S} {3,S}
3 *5 Xo u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label="*-N-H",
    group =
"""
1 *4 H  u0 p0 c0 {2,S}
2 *3 N  u0 p1 c0 {1,S} {3,S} {4,S}
3 *5 Xo u0 p0 c0 {2,S}
4    R  ux px c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label="*=N-H",
    group =
"""
1 *4 H  u0 p0 c0 {2,S}
2 *3 N  u0 p1 c0 {1,S} {3,D}
3 *5 Xo u0 p0 c0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 16,
    label="*-C-H",
    group =
"""
1 *4 H  u0 p0 c0 {2,S}
2 *3 C  u0 p0 c0 {1,S} {3,S} {4,[S,D]}
3 *5 Xo u0 p0 c0 {2,S}
4    R  u0 px c0 {2,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 17,
    label="*=C-H",
    group =
"""
1 *4 H  u0 p0 c0 {2,S}
2 *3 C  u0 p0 c0 {1,S} {3,D} {4,S}
3 *5 Xo u0 p0 c0 {2,D}
4    R  u0 px c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label="*#C-H",
    group =
"""
1 *4 H  u0 p0 c0 {2,S}
2 *3 C  u0 p0 c0 {1,S} {3,T}
3 *5 Xo u0 p0 c0 {2,T}
""",
    kinetics = None,
)

entry(
    index = 19,
    label="*C-OH",
    group =
"""
1 *4 O   u0 p2 c0 {2,S} {4,S}
2 *3 C   u0 p0 c0 {1,S} {3,[S,D,T]}
3 *5 Xo  u0 p0 c0 {2,[S,D,T]}
4    H   u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label="*=N-OH",
    group =
"""
1 *4 O  u0 p2 c0 {2,S} {4,S}
2 *3 N  u0 p1 c0 {1,S} {3,D}
3 *5 Xo u0 p0 c0 {2,D}
4    H  u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label="*O-OH",
    group =
"""
1 *4 O  u0 p2 c0 {2,S} {4,S}
2 *3 O  u0 p2 c0 {1,S} {3,S}
3 *5 Xo u0 p0 c0 {2,S}
4    H  u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label="*-C-OH",
    group =
"""
1 *4 O  u0 p2 c0 {2,S} {4,S}
2 *3 C  u0 p0 c0 {1,S} {3,S} {5,[S,D]}
3 *5 Xo u0 p0 c0 {2,S}
4    H  u0 p0 c0 {1,S}
5    R  u0 p0 c0 {2,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 23,
    label="*=C-OH",
    group =
"""
1 *4 O  u0 p2 c0 {2,S} {4,S}
2 *3 C  u0 p0 c0 {1,S} {3,D} {5,S}
3 *5 Xo u0 p0 c0 {2,D}
4    H  u0 p0 c0 {1,S}
5    R  ux px c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label="*#C-OH",
    group =
"""
1 *4 O  u0 p2 c0 {2,S} {4,S}
2 *3 C  u0 p0 c0 {1,S} {3,T}
3 *5 Xo u0 p0 c0 {2,T}
4    H  u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "C=*",
    group =
"""
1 *1 C  u0 p0 c0 {2,D}
2 *2 Xo u0 p0 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "C#*",
    group =
"""
1 *1 C  u0 p0 c0 {2,T}
2 *2 Xo u0 p0 c0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "C$*",
    group =
"""
1 *1 C  u0 p0 c0 {2,Q}
2 *2 Xo u0 p0 c0 {1,Q}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "N=*",
    group =
"""
1 *1 N  u0 px cx {2,D} {3,[S,D]}
2 *2 Xo u0 p0 c0 {1,D}
3    R  ux px cx {1,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "N#*",
    group =
"""
1 *1 N  u0 px cx {2,T}
2 *2 Xo u0 p0 c0 {1,T}
""",
    kinetics = None,
)

# entry(
#     index = 30,
#     label = "R=N=*",
#     group =
# """
# 1 *1 N   u0 p0 c+1 {2,D} {3,D}
# 2 *2 Xo  u0 p0 c0  {1,D}
# 3    R!H u0 px c-1 {1,D}
# """,
#     kinetics = None,
# )

entry(
    index = 31,
    label = "R-N=*",
    group =
"""
1 *1 N  u0 p1 c0 {2,D} {3,S}
2 *2 Xo u0 p0 c0 {1,D}
3    R  u0 p0 c0 {1,S}
""",
    kinetics = None,
)

# entry(
#     index = 32,
#     label = "R-N#*",
#     group =
# """
# 1 *1 N   u0 p0 c+1 {2,T} {3,S}
# 2 *2 Xo  u0 p0 c0  {1,T}
# 3    R!H u0 px c-1 {1,S}
# """,
#     kinetics = None,
# )

entry(
    index = 33,
    label = ":N#*",
    group =
"""
1 *1 N   u0 p1 c0 {2,T}
2 *2 Xo  u0 p0 c0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 34,
    label="*N-OH",
    group =
"""
1 *4 O  u0 p2 c0 {2,S} {4,S}
2 *3 N  ux px cx {1,S} {3,[S,D]}
3 *5 Xo u0 p0 c0 {2,[S,D]}
4    H  u0 p0 c0 {1,S}
""",
    kinetics = None,
)

# entry(
#     index = 35,
#     label="*-N-OH",
#     group =
# """
# 1 *4 O   u0 p2 c0  {2,S} {4,S}
# 2 *3 N   u0 p1 c+1 {1,S} {3,S} {5,[S,D]}
# 3 *5 Xo  u0 p0 c0  {2,S}
# 4    H   u0 p0 c0  {1,S}
# 5    R!H u0 px c-1 {2,[S,D]}
# """,
#     kinetics = None,
# )

entry(
    index = 36,
    label="*C-C",
    group =
"""
1 *4 C  u0 p0 c0 {2,S}
2 *3 C  u0 p0 c0 {1,S} {3,[S,D,T]}
3 *5 Xo u0 p0 c0 {2,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 37,
    label="*-O-C",
    group =
"""
1 *4 C  u0 p0 c0 {2,S}
2 *3 O  u0 p2 c0 {1,S} {3,S}
3 *5 Xo u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label="*N-C",
    group =
"""
1 *4 C  u0 p0 c0 {2,S}
2 *3 N  u0 px cx {1,S} {3,[S,D]}
3 *5 Xo u0 p0 c0 {2,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 39,
    label="*C-N",
    group =
"""
1 *4 N  ux px cx {2,S}
2 *3 C  u0 p0 c0 {1,S} {3,[S,D,T]}
3 *5 Xo u0 p0 c0 {2,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 40,
    label="*-O-N",
    group =
"""
1 *4 N  ux px cx {2,S}
2 *3 O  u0 p2 c0 {1,S} {3,S}
3 *5 Xo u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label="*N-N",
    group =
"""
1 *4 N  ux px cx {2,S}
2 *3 N  ux px cx {1,S} {3,[S,D,T]}
3 *5 Xo u0 p0 c0 {2,[S,D,T]}
""",
    kinetics = None,
)

tree(
"""
L1: Abstracting
    L2: C
        L3: C=*
        L3: C#*
        L3: C$*
    L2: N
        L3: N=*
            L4: R-N=*
        L3: N#*
            L4: :N#*
    L2: O

L1: Donating
    L2: *R-H
        L3: *C-H
            L4: *-C-H
            L4: *=C-H
            L4: *#C-H
        L3: *N-H
            L4: *-N-H
            L4: *=N-H
        L3: *OH
    L2: *R-O
        L3: *R-OH
            L4: *C-OH
                L5: *-C-OH
                L5: *=C-OH
                L5: *#C-OH
            L4: *N-OH
                L5: *=N-OH
            L4: *O-OH
    L2: *R-C
        L3: *C-C
        L3: *-O-C
        L3: *N-C
    L2: *R-N
        L3: *C-N
        L3: *N-N
        L3: *-O-N
"""
)
