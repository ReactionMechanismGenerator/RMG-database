#!/usr/bin/env python
# encoding: utf-8

name = "1,2-Birad_to_alkene/groups"
shortDesc = u""
longDesc = u"""
"""

template(reactants=["Y_12birad"], products=["Y_multiple_bond"], ownReverse=False)

reverse = None
reversible = False

recipe(actions=[
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*2', '1'],
])

entry(
    index = 1,
    label = "Y_12birad",
    group = "OR{CsCs, NOS}",
    kinetics = None,
)

entry(
    index = 17,
    label = "CsCs",
    group = "OR{Y_12_00, Y_12_10, Y_12_20, Y_12_30, Y_12_40, Y_12_01, Y_12_02, Y_12_03, Y_12_04, Y_12_11, Y_12_12,Y_12_21, Y_12_22, Y_12_13, Y_12_31}",
    kinetics = None,
)

entry(
    index = 2,
    label = "Y_12_00",
    group =
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 Cs u1 {1,S} {5,S} {6,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {2,S}
6    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "Y_12_10",
    group =
"""
1 *1 Cs      u1 {2,S} {3,S} {4,S}
2 *2 Cs      u1 {1,S} {5,S} {6,S}
3    [Cs,O2s] u0 {1,S}
4    H       u0 {1,S}
5    H       u0 {2,S}
6    H       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "Y_12_20",
    group = "OR{Y_12_20a, Y_12_20b}",
    kinetics = None,
)

entry(
    index = -1,
    label = "Y_12_20a",
    group =
"""
1 *1 Cs          u1 {2,S} {3,S} {4,S}
2 *2 Cs          u1 {1,S} {5,S} {6,S}
3    [Cs,O2s,S2s] u0 px c0 {1,S}
4    [Cs,O2s,S2s] u0 px c0 {1,S}
5    H           u0 {2,S}
6    H           u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = -1,
    label = "Y_12_20b",
    group =
"""
1 *1 Cs          u1 {2,S} {3,S} {4,S}
2 *2 Cs          u1 {1,S} {5,S} {6,S}
3    [Cs,O2s,S2s] u0 px c0 {1,S}
4    H           u0 {1,S}
5    [Cs,O2s,S2s] u0 px c0 {2,S}
6    H           u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "Y_12_30",
    group =
"""
1 *1 Cs          u1 {2,S} {3,S} {4,S}
2 *2 Cs          u1 {1,S} {5,S} {6,S}
3    [Cs,O2s,S2s] u0 px c0 {1,S}
4    [Cs,O2s,S2s] u0 px c0 {1,S}
5    [Cs,O2s,S2s] u0 px c0 {2,S}
6    H           u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "Y_12_40",
    group =
"""
1 *1 Cs          u1 {2,S} {3,S} {4,S}
2 *2 Cs          u1 {1,S} {5,S} {6,S}
3    [Cs,O2s,S2s] u0 px c0 {1,S}
4    [Cs,O2s,S2s] u0 px c0 {1,S}
5    [Cs,O2s,S2s] u0 px c0 {2,S}
6    [Cs,O2s,S2s] u0 px c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "Y_12_01",
    group =
"""
1 *1 Cs               u1 {2,S} {3,S} {4,S}
2 *2 Cs               u1 {1,S} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {1,S}
5    H                u0 {2,S}
6    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "Y_12_02",
    group = "OR{Y_12_02a, Y_12_02b}",
    kinetics = None,
)

entry(
    index = -1,
    label = "Y_12_02a",
    group =
"""
1 *1 Cs               u1 {2,S} {3,S} {4,S}
2 *2 Cs               u1 {1,S} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    H                u0 {2,S}
6    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = -1,
    label = "Y_12_02b",
    group =
"""
1 *1 Cs               u1 {2,S} {3,S} {4,S}
2 *2 Cs               u1 {1,S} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
6    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "Y_12_03",
    group =
"""
1 *1 Cs               u1 {2,S} {3,S} {4,S}
2 *2 Cs               u1 {1,S} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
6    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "Y_12_04",
    group =
"""
1 *1 Cs               u1 {2,S} {3,S} {4,S}
2 *2 Cs               u1 {1,S} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "Y_12_11",
    group = "OR{Y_12_11a, Y_12_11b}",
    kinetics = None,
)

entry(
    index = -1,
    label = "Y_12_11a",
    group =
"""
1 *1 Cs               u1 {2,S} {3,S} {4,S}
2 *2 Cs               u1 {1,S} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O2s,S2s]     u0 px c0 {1,S}
5    H                u0 {2,S}
6    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = -1,
    label = "Y_12_11b",
    group =
"""
1 *1 Cs               u1 {2,S} {3,S} {4,S}
2 *2 Cs               u1 {1,S} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    H                u0 {1,S}
5    [Cs,O2s,S2s]     u0 px c0 {2,S}
6    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "Y_12_12",
    group = "OR{Y_12_12a, Y_12_12b}",
    kinetics = None,
)

entry(
    index = -1,
    label = "Y_12_12a",
    group =
"""
1 *1 Cs               u1 {2,S} {3,S} {4,S}
2 *2 Cs               u1 {1,S} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cs,O2s,S2s]     u0 px c0 {2,S}
6    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = -1,
    label = "Y_12_12b",
    group =
"""
1 *1 Cs               u1 {2,S} {3,S} {4,S}
2 *2 Cs               u1 {1,S} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O2s,S2s]     u0 px c0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
6    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "Y_12_21",
    group = "OR{Y_12_21a, Y_12_21b}",
    kinetics = None,
)

entry(
    index = -1,
    label = "Y_12_21a",
    group =
"""
1 *1 Cs               u1 {2,S} {3,S} {4,S}
2 *2 Cs               u1 {1,S} {5,S} {6,S}
3    [Cs,O2s,S2s]     u0 px c0 {1,S}
4    [Cs,O2s,S2s]     u0 px c0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
6    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = -1,
    label = "Y_12_21b",
    group =
"""
1 *1 Cs               u1 {2,S} {3,S} {4,S}
2 *2 Cs               u1 {1,S} {5,S} {6,S}
3    [Cs,O2s,S2s]     u0 px c0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cs,O2s,S2s]     u0 px c0 {2,S}
6    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "Y_12_22",
    group = "OR{Y_12_22a, Y_12_22b}",
    kinetics = None,
)

entry(
    index = -1,
    label = "Y_12_22a",
    group =
"""
1 *1 Cs               u1 {2,S} {3,S} {4,S}
2 *2 Cs               u1 {1,S} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cs,O2s,S2s]     u0 px c0 {2,S}
6    [Cs,O2s,S2s]     u0 px c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = -1,
    label = "Y_12_22b",
    group =
"""
1 *1 Cs               u1 {2,S} {3,S} {4,S}
2 *2 Cs               u1 {1,S} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cs,O2s,S2s]     u0 px c0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
6    [Cs,O2s,S2s]     u0 px c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "Y_12_13",
    group =
"""
1 *1 Cs               u1 {2,S} {3,S} {4,S}
2 *2 Cs               u1 {1,S} {5,S} {6,S}
3    [Cd,Ct,Cb,CO,CS] u0 {1,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {2,S}
6    [Cs,O2s,S2s]     u0 px c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "Y_12_31",
    group =
"""
1 *1 Cs               u1 {2,S} {3,S} {4,S}
2 *2 Cs               u1 {1,S} {5,S} {6,S}
3    [Cs,O2s,S2s]     u0 px c0 {1,S}
4    [Cs,O2s,S2s]     u0 px c0 {1,S}
5    [Cs,O2s,S2s]     u0 px c0 {2,S}
6    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "NOS",
    group =
"""
1 *1 [N,O,S]   u1 px c0 {2,[S,D]}
2 *2 [N,O,S,C] u1 px c0 {1,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "N",
    group =
"""
1 *1 N u1 px c0 {2,[S,D]}
2 *2 N u1 px c0 {1,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "N3s",
    group =
"""
1 *1 N3s u1 p1 c0 {2,S}
2 *2 N3s u1 p1 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "N3d",
    group =
"""
1 *1 N3d u1 p1 c0 {2,D}
2 *2 N3d u1 p1 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "S",
    group =
"""
1 *1 S     u1 px c0 {2,[S,D]}
2 *2 [S,O] u1 px c0 {1,[S,D]}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "SX2",
    group =
"""
1 *1 S4d                        u1 p1 c0 {2,S} {3,D}
2 *2 [S2s,O2s]                  u1 p2 c0 {1,S}
3    [O2d,S2d,N3d,Cd,CO,CS,Cdd] u0 p2 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "SO2",
    group =
"""
1 *1 S4d u1 p1 c0 {2,S} {3,D}
2 *2 O2s u1 p2 c0 {1,S}
3    O2d u0 p2 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "SX3",
    group =
"""
1 *1 S6dd                       u1 p0 c0 {2,S} {3,D} {4,D}
2 *2 [S2s,O2s]                  u1 p2 c0 {1,S}
3    [O2d,S2d,N3d,Cd,CO,CS,Cdd] u0 p2 c0 {1,D}
4    [O2d,S2d,N3d,Cd,CO,CS,Cdd] u0 p2 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "SO3",
    group =
"""
1 *1 S6dd u1 p0 c0 {2,S} {3,D} {4,D}
2 *2 O2s  u1 p2 c0 {1,S}
3    O2d  u0 p2 c0 {1,D}
4    O2d  u0 p2 c0 {1,D}
""",
    kinetics = None,
)

tree(
"""
L1: Y_12birad
    L2: CsCs
        L3: Y_12_00
        L3: Y_12_10
        L3: Y_12_20
            L4: Y_12_20a
            L4: Y_12_20b
        L3: Y_12_30
        L3: Y_12_40
        L3: Y_12_01
        L3: Y_12_02
            L4: Y_12_02a
            L4: Y_12_02b
        L3: Y_12_03
        L3: Y_12_04
        L3: Y_12_11
            L4: Y_12_11a
            L4: Y_12_11b
        L3: Y_12_12
            L4: Y_12_12a
            L4: Y_12_12b
        L3: Y_12_21
            L4: Y_12_21a
            L4: Y_12_21b
        L3: Y_12_22
            L4: Y_12_22a
            L4: Y_12_22b
        L3: Y_12_13
        L3: Y_12_31
    L2: NOS
        L3: N
            L4: N3s
            L4: N3d
        L3: S
            L4: SX2
                L5: SO2
            L4: SX3
                L5: SO3
"""
)

forbidden(
    label = "O2",
    group =
"""
1 *1 O2s u1 p2 c0 {2,S}
2 *2 O2s u1 p2 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
The ground state of these three isoelectrinic structures (O2, S2, SO) is the triplet form,
hence they behave differently than this family
""",
)

forbidden(
    label = "S2",
    group =
"""
1 *1 S2s u1 p2 c0 {2,S}
2 *2 S2s u1 p2 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
""",
)

forbidden(
    label = "SO",
    group =
"""
1 *1 S2s u1 p2 c0 {2,S}
2 *2 O2s u1 p2 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
""",
)
