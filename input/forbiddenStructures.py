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
    label = "N_monorad_3singleBonds",
    group = 
"""
1 N u1 p0 {2,S} {3,S} {4,S}
2 R ux {1,S}
3 R ux {1,S}
4 R ux {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "N_birad_singlet_2singleBonds",
    group = 
"""
1 N u0 p1 {2,S} {3,S}
2 R ux {1,S}
3 R ux {1,S}
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
    label = "CH_doublet",
    group = 
"""
1 C u1 p1 {2,S}
2 H u0 {1,S}
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

