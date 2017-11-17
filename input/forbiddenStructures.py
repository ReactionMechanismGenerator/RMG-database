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

# entry(
#     label = "cyclopropyne",
#     group =
# """
# 1 C u0 {2,T} {3,S}
# 2 C u0 {1,T} {3,S}
# 3 C u0 {1,S} {2,S} {4,S} {5,S}
# 4 H u0 {3,S}
# 5 H u0 {3,S}
# """,
#     shortDesc = u"""""",
#     longDesc =
# u"""
#
# """,
# )

entry(
    label = "cyclobutyne",
    group =
"""
1   R!H ux {2,T} {4,[S,D,T]}
2   R!H ux {1,T} {3,[S,D,T]}
3   R!H ux {2,[S,D,T]} {4,[S,D,T]}
4   R!H ux {1,[S,D,T]} {3,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
""",
)

entry(
    label = "s2_3_4_yne_1",
    group =
"""
1   R!H ux {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
2   R!H ux {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
3   R!H ux {1,[S,D,T,B]} {2,[S,D,T,B]}
4   R!H ux {1,[S,D,T,B]} {5,T}
5   R!H ux {2,[S,D,T,B]} {4,T}
""",
    shortDesc = u"""""",
    longDesc =
u"""
""",
)

entry(
    label = "s2_4_4_yne_1",
    group =
"""
1   R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H ux {1,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3   R!H ux {2,[S,D,T,B]} {4,T}
4   R!H ux {1,[S,D,T,B]} {3,T}
5   R!H ux {1,[S,D,T,B]} {6,[S,D,T,B]}
6   R!H ux {2,[S,D,T,B]} {5,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
""",
)

entry(
    label = "s2_4_5_yne_5",
    group =
"""
1   R!H ux {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
3   R!H ux {1,[S,D,T,B]} {4,T}
4   R!H ux {2,[S,D,T,B]} {3,T}
5   R!H ux {1,[S,D,T,B]} {7,[S,D,T,B]}
6   R!H ux {2,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H ux {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
""",
)

entry(
    label = "s2_4_6_yne_6",
    group =
"""
1   R!H ux {2,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
2   R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3   R!H ux {1,[S,D,T,B]} {4,T}
4   R!H ux {2,[S,D,T,B]} {3,T}
5   R!H ux {2,[S,D,T,B]} {8,[S,D,T,B]}
6   R!H ux {1,[S,D,T,B]} {7,[S,D,T,B]}
7   R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8   R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
""",
)

entry(
    label = "strained_tetracyclic_1",
    group =
"""
1  R!H ux {2,[S,D,T,B]} {9,[S,D,T,B]}
2  R!H ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3  R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]} {10,[S,D,T,B]}
4  R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]} {9,[S,D,T,B]}
5  R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]} {10,[S,D,T,B]}
8  R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]} {10,[S,D,T,B]}
9  R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]} {8,[S,D,T,B]}
10 R!H ux {3,[S,D,T,B]} {7,[S,D,T,B]} {8,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
For certain unsaturated versions of this strained tetracyclic, RMG finds multiple reverse H-abstraction reactions, causing RMG
to crash.
""",
)

entry(
    label = "strained_tricyclic_1",
    group =
"""
2  R!H ux {3,[S,D,T,B]} {10,[S,D,T,B]}
3  R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]} {9,[S,D,T,B]}
6  R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]} {10,[S,D,T,B]}
7  R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9  R!H ux {5,[S,D,T,B]} {8,[S,D,T,B]} {10,[S,D,T,B]}
10 R!H ux {2,[S,D,T,B]} {6,[S,D,T,B]} {9,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
For certain unsaturated versions of this strained tricyclic, RMG's Clar optimization fails, causing RMG
to crash.
""",
)

entry(
    label = "strained_tricyclic_2",
    group =
"""
1  R!H ux {2,[S,D,T,B]} {10,[S,D,T,B]}
2  R!H ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3  R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]} {8,[S,D,T,B]}
4  R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]} {10,[S,D,T,B]}
6  R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  R!H ux {3,[S,D,T,B]} {7,[S,D,T,B]} {9,[S,D,T,B]}
9  R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 R!H ux {1,[S,D,T,B]} {5,[S,D,T,B]} {9,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Certain unsaturated versions of this strained tricyclic cause RMG
to crash.
""",
)

entry(
    label = "strained_tricyclic_3",
    group =
"""
1  R!H ux {3,[S,D,T,B]} {7,[S,D,T,B]}
3  R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]} {10,[S,D,T,B]}
4  R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]} {10,[S,D,T,B]}
6  R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  R!H ux {1,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
8  R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9  R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]} {9,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Certain unsaturated versions of this strained tricyclic cause RMG
to crash.
""",
)

entry(
    label = "CO_birad",
    group =
"""
multiplicity [3]
1 C u2 p0 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbidden after discussion with whgreen.
This species should quickly transform into a closed shell [C-]#[O+].
We don't need it as a resonance structure of carbon monoxide for reactivity since carbon monoxide has its designated
reaction families (CO_Disprop, R_Add_COm).
""",
)

entry(
    label = "CS_birad",
    group =
"""
multiplicity [3]
1 C u2 p0 c0 {2,D}
2 S u0 p2 c0 {1,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbidden after discussion with whgreen.
This species should quickly transform into a closed shell [C-]#[S+] similar to the carbon monoxide case above.
We don't need it as a resonance structure of carbon monsulfide for reactivity since carbon monsulfide has its designated
reaction families (CO_Disprop [also deals with CS], R_Add_CSm).
""",
)
