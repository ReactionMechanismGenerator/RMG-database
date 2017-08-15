#!/usr/bin/env python
# encoding: utf-8

name = ""
shortDesc = u""
longDesc = u"""

"""
entry(
    label = "Ods",
    group = 
"""
1 O ux {2,D} {3,S}
2 R ux {1,D}
3 R ux {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "Od_rad",
    group = 
"""
1 O u1 {2,D}
2 R ux {1,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

#entry(
#    label = "N_monorad_3singleBonds",
#    group = 
#"""
#1 N u1 p0 {2,S} {3,S} {4,S}
#2 R ux {1,S}
#3 R ux {1,S}
#4 R ux {1,S}
#""",
#    shortDesc = u"""""",
#    longDesc = 
#u"""
#restricts H2NO, see RMG-Py issue #514
#""",
#)

#entry(
#    label = "N_birad_singlet_2singleBonds",
#    group = 
#"""
#1 N u0 p1 {2,S} {3,S}
#2 R ux {1,S}
#3 R ux {1,S}
#""",
#    shortDesc = u"""""",
#    longDesc = 
#u"""
#restricts NH3, see RMG-Py issue #514
#""",
#)

entry(
    label = "N_birad_triplet_2singleBonds",
    group = 
"""
1 N u2 p0 {2,S} {3,S}
2 R ux {1,S}
3 R ux {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "C_quintet",
    group = 
"""
1 C u4 p0
""",
    shortDesc = u"""""",
    longDesc = 
u"""
restricts [C], see RMG-Py issue #514
""",
)

entry(
    label = "C8H7S2J",
    group = 
"""
1  S u0 {5,S} {11,S}
2  C u0 {3,D} {6,S} {18,S}
3  C u0 {2,D} {4,S} {13,S}
4  C u0 {3,S} {5,D} {7,S}
5  C u0 {1,S} {4,D} {8,S}
6  H u0 {2,S}
7  H u0 {4,S}
8  H u0 {5,S}
9  S u0 {10,S} {13,S}
10 C u0 {9,S} {11,S} {14,S} {15,S}
11 C u0 {1,S} {10,S} {12,S} {16,S}
12 C u0 {11,S} {13,D} {17,S}
13 C u0 {3,S} {9,S} {12,D}
14 H u0 {10,S}
15 H u0 {10,S}
16 H u0 {11,S}
17 H u0 {12,S}
18 H u0 {2,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "C8H7S2J(2)",
    group = 
"""
1  S u0 {5,S} {11,S}
2  C u0 {3,D} {6,S} {18,S}
3  C u0 {2,D} {4,S} {13,S}
4  C u0 {3,S} {5,D} {7,S}
5  C u0 {1,S} {4,D} {8,S}
6  H u0 {2,S}
7  H u0 {4,S}
8  H u0 {5,S}
9  S u0 {10,S} {13,S}
10 C u0 {9,S} {11,S} {14,S} {15,S}
11 C u0 {1,S} {10,S} {12,S} {16,S}
12 C u0 {11,S} {13,D} {17,S}
13 C u0 {3,S} {9,S} {12,D}
14 H u0 {10,S}
15 H u0 {10,S}
16 H u0 {11,S}
17 H u0 {12,S}
18 H u0 {2,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "Carbene_D_triplet",
    group =
"""
1 C u2 p0 {2,D}
2 C u0 {1,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
restricts C2O, see RMG-Py issue #514
""",
)

# entry(
#     label = "Carbene_D_singlet",
#     group =
# """
# 1 C u0 p1 {2,D}
# 2 C u0 {1,D}
# """,
#     shortDesc = u"""""",
#     longDesc =
# u"""
#
# """,
# )

entry(
    label = "Carbene_S_triplet",
    group =
"""
1 C   u2 p0 {2,S}
2 R!H u0 {1,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

# entry(
#     label = "Carbene_S_singlet",
#     group =
# """
# 1 C   u0 p1 {2,S}
# 2 R!H u0 {1,S}
# """,
#     shortDesc = u"""""",
#     longDesc =
# u"""
#
# """,
# )

entry(
    label = "O3",
    group = 
"""
1 O u0 {2,S}
2 O u0 {1,S} {3,S}
3 O u0 {2,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "O3.",
    group = 
"""
1 O u0 {2,S}
2 O u0 {1,S} {3,S}
3 O u1 {2,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "O3..",
    group = 
"""
1 O u1 {2,S}
2 O u0 {1,S} {3,S}
3 O u1 {2,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "O4",
    group = 
"""
1 O u0 {2,S}
2 O u0 {1,S} {3,S}
3 O u0 {2,S} {4,S}
4 O u0 {3,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "O4.",
    group = 
"""
1 O u0 {2,S}
2 O u0 {1,S} {3,S}
3 O u0 {2,S} {4,S}
4 O u1 {3,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "O4..",
    group = 
"""
1 O u1 {2,S}
2 O u0 {1,S} {3,S}
3 O u0 {2,S} {4,S}
4 O u1 {3,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "cyclic-C3O",
    group = 
"""
1 C u0 {2,D} {3,S} {4,S}
2 O u0 {1,D}
3 C u0 {1,S} {4,T}
4 C u0 {1,S} {3,T}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "cyclopropyne",
    group = 
"""
1 C u0 {2,T} {3,S}
2 C u0 {1,T} {3,S}
3 C u0 {1,S} {2,S} {4,S} {5,S}
4 H u0 {3,S}
5 H u0 {3,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "3H-Pyrazol",
    group = 
"""
multiplicity [2,3,4,5]
1 C ux {2,[S,D]} {5,[S,D]}
2 C ux {1,[S,D]} {3,[S,D]}
3 C ux {2,[S,D]} {4,[S,D]}
4 N ux {3,[S,D]} {5,[S,D]}
5 N ux {1,[S,D]} {4,[S,D]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
EA sims (xa1450 & xa1451) crashed with error: Invalid k(E) values computed for path reaction "C(=[CH])[N]N=C(1479) <=> C1[CH]C=N[N]1(1659)"
EA sims (xa1452 & xa1453) crashed with error: Invalid k(E) values computed for path reaction "C(=[CH])[N]N=C(1478) <=> C1C=C[N][N]1(1824)"
See RMG-Py issue #253
""",
)

entry(
    label = "C=N[N]C#[C]",
    group = 
"""
multiplicity [3]
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 N u0 p1 c0 {1,D} {3,S}
3 N u1 p1 c0 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,T}
5 C u1 p0 c0 {4,T}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
EA sims (xa1456-xa1459) crashed with error:
Did not find reverse reaction in reaction family H_Abstraction for reaction <Molecule "N(=C=[CH])N=[CH]"> + <Molecule "C=N[N]C#[C]"> <=> <Molecule "C=N[N]C#C"> + <Molecule "N(=C=[C])N=[CH]">.
See RMG-Py issue #806
""",
)

entry(
    label = "C1=CO[N][N]1",
    group = 
"""
multiplicity [3]
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 O u0 p2 c0 {2,S} {4,S}
4 N u1 p1 c0 {3,S} {5,S}
5 N u1 p1 c0 {1,S} {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
EA sims (xa1462-xa1465) crashed with error:
Invalid k(E) values computed for path reaction "C(=[CH])N=[N+][O-](2989) <=> C1=CO[N][N]1(3358)".
""",
)

entry(
    label = "C1N[C](N1)[O]",
    group = 
"""
multiplicity [3]
1 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2 N u0 p1 c0 {1,S} {3,S} {8,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 N u0 p1 c0 {1,S} {3,S} {9,S}
5 O u1 p2 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
EA sim (xa1467) crashed with error:
Mcoll = numpy.zeros((Nisom,Ngrains,NJ,Ngrains,NJ), numpy.float64)
""",
)

entry(
    label = "C(=[CH])[O-][N+]#N",
    group = 
"""
multiplicity [2]
1 C u0 p0 c0 {2,D} {4,S} {7,S}
2 C u1 p0 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
4 O u0 p2 c-1 {1,S} {5,S}
5 N u0 p0 c+1 {4,S} {6,T}
6 N u0 p1 c0 {5,T}
7 H u0 p0 c0 {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
EA sim (xa1479) crashed with error:
Invalid k(E) values computed for path reaction "C(=[CH])[O-][N+]#N(6454) <=> c1cn[n+][o-]1(6594)".
""",
)

entry(
    label = "Double_Carbene_neighbor",
    group =
"""
1 C   u0 p1 {2,[S,D,T,B]}
2 C   u0 p1 {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid two singlet carbene groups in the same molecule from being direct neighbors
""",
)

entry(
    label = "Double_Carbene_sep_1",
    group =
"""
1 C   u0 p1 {3,[S,D,T,B]}
2 C   u0 p1 {3,[S,D,T,B]}
3 R!H ux {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid two singlet carbene groups in the same molecule from being separated by one atom
""",
)

entry(
    label = "Double_Carbene_sep_2",
    group =
"""
1 C   u0 p1 {3,[S,D,T,B]}
2 C   u0 p1 {4,[S,D,T,B]}
3 R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]}
4 R!H ux {3,[S,D,T,B]} {2,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid two singlet carbene groups in the same molecule from being separated by 2 atoms
""",
)

entry(
    label = "Double_Carbene_sep_3",
    group =
"""
1 C   u0 p1 {3,[S,D,T,B]}
2 C   u0 p1 {5,[S,D,T,B]}
3 R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]}
4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 R!H ux {4,[S,D,T,B]} {2,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid two singlet carbene groups in the same molecule from being separated by 3 atoms
""",
)

entry(
    label = "Double_Carbene_sep_4",
    group =
"""
1 C   u0 p1 {3,[S,D,T,B]}
2 C   u0 p1 {6,[S,D,T,B]}
3 R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]}
4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 R!H ux {5,[S,D,T,B]} {2,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid two singlet carbene groups in the same molecule from being separated by 4 atoms
""",
)

entry(
    label = "Double_Carbene_sep_5",
    group =
"""
1 C   u0 p1 {3,[S,D,T,B]}
2 C   u0 p1 {7,[S,D,T,B]}
3 R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]}
4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 R!H ux {6,[S,D,T,B]} {2,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid two singlet carbene groups in the same molecule from being separated by 5 atoms
""",
)

entry(
    label = "Double_Carbene_sep_6",
    group =
"""
1 C   u0 p1 {3,[S,D,T,B]}
2 C   u0 p1 {8,[S,D,T,B]}
3 R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]}
4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 R!H ux {7,[S,D,T,B]} {2,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid two singlet carbene groups in the same molecule from being separated by 6 atoms
""",
)

entry(
    label = "Double_Carbene_sep_7",
    group =
"""
1 C   u0 p1 {3,[S,D,T,B]}
2 C   u0 p1 {9,[S,D,T,B]}
3 R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]}
4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9 R!H ux {8,[S,D,T,B]} {2,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid two singlet carbene groups in the same molecule from being separated by 7 atoms
""",
)

entry(
    label = "Double_Carbene_sep_8",
    group =
"""
1 C   u0 p1 {3,[S,D,T,B]}
2 C   u0 p1 {10,[S,D,T,B]}
3 R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]}
4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9 R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 R!H ux {9,[S,D,T,B]} {2,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid two singlet carbene groups in the same molecule from being separated by 8 atoms
""",
)

entry(
    label = "Carbene_Radical_neighbor",
    group =
"""
1 C   u0 p1 {2,[S,D,T,B]}
2 R!H u1 {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a singlet carbene and a radical group in the same molecule from being direct neighbors
""",
)

entry(
    label = "Carbene_Radical_sep_1",
    group =
"""
1 C   u0 p1 {3,[S,D,T,B]}
2 R!H u1 {3,[S,D,T,B]}
3 R!H ux {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a singlet carbene and a radical group in the same molecule from being separated by one atom
""",
)

entry(
    label = "Carbene_Radical_sep_2",
    group =
"""
1 C   u0 p1 {3,[S,D,T,B]}
2 R!H u1 {4,[S,D,T,B]}
3 R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]}
4 R!H ux {3,[S,D,T,B]} {2,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a singlet carbene and a radical group in the same molecule from being separated by 2 atoms
""",
)

entry(
    label = "Carbene_Radical_sep_3",
    group =
"""
1 C   u0 p1 {3,[S,D,T,B]}
2 R!H u1 {5,[S,D,T,B]}
3 R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]}
4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 R!H ux {4,[S,D,T,B]} {2,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a singlet carbene and a radical group in the same molecule from being separated by 3 atoms
""",
)

entry(
    label = "Carbene_Radical_sep_4",
    group =
"""
1 C   u0 p1 {3,[S,D,T,B]}
2 R!H u1 {6,[S,D,T,B]}
3 R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]}
4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 R!H ux {5,[S,D,T,B]} {2,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a singlet carbene and a radical group in the same molecule from being separated by 4 atoms
""",
)

entry(
    label = "Carbene_Radical_sep_5",
    group =
"""
1 C   u0 p1 {3,[S,D,T,B]}
2 R!H u1 {7,[S,D,T,B]}
3 R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]}
4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 R!H ux {6,[S,D,T,B]} {2,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a singlet carbene and a radical group in the same molecule from being separated by 5 atoms
""",
)

entry(
    label = "Carbene_Radical_sep_6",
    group =
"""
1 C   u0 p1 {3,[S,D,T,B]}
2 R!H u1 {8,[S,D,T,B]}
3 R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]}
4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 R!H ux {7,[S,D,T,B]} {2,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a singlet carbene and a radical group in the same molecule from being separated by 6 atoms
""",
)

entry(
    label = "Carbene_Radical_sep_7",
    group =
"""
1 C   u0 p1 {3,[S,D,T,B]}
2 R!H u1 {9,[S,D,T,B]}
3 R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]}
4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9 R!H ux {8,[S,D,T,B]} {2,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a singlet carbene and a radical group in the same molecule from being separated by 7 atoms
""",
)

entry(
    label = "Carbene_Radical_sep_8",
    group =
"""
1 C   u0 p1 {3,[S,D,T,B]}
2 R!H u1 {10,[S,D,T,B]}
3 R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]}
4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9 R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 R!H ux {9,[S,D,T,B]} {2,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a singlet carbene and a radical group in the same molecule from being separated by 8 atoms
""",
)

