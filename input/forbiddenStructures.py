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
1 O X {2,D} {3,S}
2 R X {1,D}
3 R X {1,S}
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
1 O 1           {2,D}
2 R X {1,D}
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
1 N 1 0 {2,S} {3,S} {4,S}
2 R X {1,S}
3 R X {1,S}
4 R X {1,S}
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
1 N 2S 0 {2,S} {3,S}
2 R X {1,S}
3 R X {1,S}
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
1 N 2T 0 {2,S} {3,S}
2 R X {1,S}
3 R X {1,S}
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
1 C 4V 0
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
1 C 3D 0 {2,S}
2 H 0  {1,S}
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
1  S 0 {5,S} {11,S}
2  C 0 {3,D} {6,S} {18,S}
3  C 0 {2,D} {4,S} {13,S}
4  C 0 {3,S} {5,D} {7,S}
5  C 0 {1,S} {4,D} {8,S}
6  H 0 {2,S}
7  H 0 {4,S}
8  H 0 {5,S}
9  S 0 {10,S} {13,S}
10 C 0 {9,S} {11,S} {14,S} {15,S}
11 C 0 {1,S} {10,S} {12,S} {16,S}
12 C 0 {11,S} {13,D} {17,S}
13 C 0 {3,S} {9,S} {12,D}
14 H 0 {10,S}
15 H 0 {10,S}
16 H 0 {11,S}
17 H 0 {12,S}
18 H 0 {2,S}
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
1  S 0 {5,S} {11,S}
2  C 0 {3,D} {6,S} {18,S}
3  C 0 {2,D} {4,S} {13,S}
4  C 0 {3,S} {5,D} {7,S}
5  C 0 {1,S} {4,D} {8,S}
6  H 0 {2,S}
7  H 0 {4,S}
8  H 0 {5,S}
9  S 0 {10,S} {13,S}
10 C 0 {9,S} {11,S} {14,S} {15,S}
11 C 0 {1,S} {10,S} {12,S} {16,S}
12 C 0 {11,S} {13,D} {17,S}
13 C 0 {3,S} {9,S} {12,D}
14 H 0 {10,S}
15 H 0 {10,S}
16 H 0 {11,S}
17 H 0 {12,S}
18 H 0 {2,S}
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
1 C 2T 0 {2,D}
2 C 0       {1,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "Carbene_D_singlet",
    group = 
"""
1 C 2S 0 {2,D}
2 C 0       {1,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "Carbene_S_triplet",
    group = 
"""
1 C   2T 0 {2,S}
2 R!H 0       {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "Carbene_S_singlet",
    group = 
"""
1 C 2S 0 {2,S}
2 R!H 0       {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "O3",
    group = 
"""
1 O 0 {2,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S}
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
1 O 0 {2,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
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
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
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
1 O 0 {2,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {4,S}
4 O 0 {3,S}
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
1 O 0 {2,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {4,S}
4 O 1 {3,S}
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
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {4,S}
4 O 1 {3,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "S3",
    group = 
"""
1 S 0 {2,S}
2 S 0 {1,S} {3,S}
3 S 0 {2,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "S3..",
    group = 
"""
1 S 1 {2,S}
2 S 0 {1,S} {3,S}
3 S 1 {2,S}
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
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 C 0 {1,S} {4,T}
4 C 0 {1,S} {3,T}
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
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {3,S}
3 C 0 {1,S} {2,S} {4,S} {5,S}
4 H 0 {3,S}
5 H 0 {3,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

