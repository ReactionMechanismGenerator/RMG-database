#!/usr/bin/env python
# encoding: utf-8

name = ""
shortDesc = u""
longDesc = u"""

"""

entry(
    label = "Ods",
    multiplicity = [1,2,3,4,5],
    group = 
"""
1 O {0,1,2,3,4} {2,D} {3,S}
2 R {0,1,2,3,4} {1,D}
3 R {0,1,2,3,4} {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "Od_rad",
    multiplicity = [1,2,3,4,5],
    group = 
"""
1 O 1           {2,D}
2 R {0,1,2,3,4} {1,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "N_birad_RsRsRs",
    multiplicity = [1,2,3,4,5],
    group = 
"""
1 N 1         {2,S} {3,S} {4,S}
2 R {0,1,2,3} {1,S}
3 R {0,1,2,3} {1,S}
4 R {0,1,2,3} {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "N_birad_RsRs",
    multiplicity = [1,2,3,4,5],
    group = 
"""
1 N 2         {2,S} {3,S}
2 R {0,1,2,3} {1,S}
3 R {0,1,2,3} {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "C_(V)",
    multiplicity = [5],
    group = 
"""
1 C 4
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "CH_(D)",
    multiplicity = [2],
    group = 
"""
1 C 3 {2,S}
2 H 0 {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "C8H7S2J",
    multiplicity = [1,2,3,4,5],
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
    multiplicity = [1,2,3,4,5],
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
    label = "Carbene_D",
    multiplicity = [1,3],
    group = 
"""
1 C 2 {2,D}
2 C 0 {1,D}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "Carbene_S",
    multiplicity = [1,3],
    group = 
"""
1 C   2 {2,S}
2 R!H 0 {1,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    label = "O3",
    multiplicity = [1,2,3,4,5],
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
    multiplicity = [1,2,3,4,5],
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
    multiplicity = [1,2,3,4,5],
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
    multiplicity = [1,2,3,4,5],
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
    multiplicity = [1,2,3,4,5],
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
    multiplicity = [1,2,3,4,5],
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
    multiplicity = [1,2,3,4,5],
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
    multiplicity = [1,2,3,4,5],
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
    multiplicity = [1,2,3,4,5],
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
    multiplicity = [1],
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

