#!/usr/bin/env python
# encoding: utf-8

name = "Polycyclic Ring Corrections"
shortDesc = u""
longDesc = u"""

"""
# L1
entry(
    index = 0,
    label = "PolycyclicRing",
    group = 
"""
1 * R u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)
# L2
entry(
    index = 0,
    label = "s1_3_3",
    group = 
"""
1 * C u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
4   C u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_3_4",
    group = 
"""
1 * C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6   C u0 {4,[S,D,T,B]} {5,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_3_5",
    group = 
"""
1 * C u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
2   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]}
3   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   C u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
7   C u0 {4,[S,D,T,B]} {5,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_3_6",
    group = 
"""
1 * C u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4   C u0 {3,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]} {8,[S,D,T,B]}
5   C u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6   C u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
7   C u0 {4,[S,D,T,B]} {8,[S,D,T,B]}
8   C u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_4_4",
    group = 
"""
1 * C u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
3   C u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
5   C u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6   C u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
7   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_4_5",
    group = 
"""
1 * C u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {5,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
4   C u0 {5,[S,D,T,B]} {7,[S,D,T,B]}
5   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]}
6   C u0 {3,[S,D,T,B]} {8,[S,D,T,B]}
7   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]}
8   C u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_4_6",
    group = 
"""
1 * C u0 {3,[S,D,T,B]} {9,[S,D,T,B]}
2   C u0 {5,[S,D,T,B]} {7,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
4   C u0 {5,[S,D,T,B]} {8,[S,D,T,B]}
5   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]} {9,[S,D,T,B]}
6   C u0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7   C u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
8   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]}
9   C u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_5_5",
    group = 
"""
1 * C u0 {8,[S,D,T,B]} {9,[S,D,T,B]}
2   C u0 {4,[S,D,T,B]} {5,[S,D,T,B]}
3   C u0 {5,[S,D,T,B]} {9,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
5   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
6   C u0 {7,[S,D,T,B]} {9,[S,D,T,B]}
7   C u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
9   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_5_6",
    group = 
"""
1  * C u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
2    C u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3    C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4    C u0 {3,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]} {10,[S,D,T,B]}
5    C u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
6    C u0 {8,[S,D,T,B]} {9,[S,D,T,B]}
7    C u0 {4,[S,D,T,B]} {8,[S,D,T,B]}
8    C u0 {6,[S,D,T,B]} {7,[S,D,T,B]}
9    C u0 {6,[S,D,T,B]} {10,[S,D,T,B]}
10   C u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_6_6",
    group = 
"""
1  * C u0 {5,[S,D,T,B]} {9,[S,D,T,B]}
2    C u0 {10,[S,D,T,B]} {11,[S,D,T,B]}
3    C u0 {4,[S,D,T,B]} {7,[S,D,T,B]} {8,[S,D,T,B]} {11,[S,D,T,B]}
4    C u0 {3,[S,D,T,B]} {6,[S,D,T,B]}
5    C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
6    C u0 {4,[S,D,T,B]} {10,[S,D,T,B]}
7    C u0 {3,[S,D,T,B]} {9,[S,D,T,B]}
8    C u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
9    C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
10   C u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
11   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s2_3_3",
    group = 
"""
1 * C u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]} {4,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s2_3_4",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
2 * C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
3   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4   C u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]} {4,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s2_3_5",
    group = 
"""
1 * C u0 {4,[S,D,T,B]} {5,[S,D,T,B]} {6,[S,D,T,B]}
2   C u0 {3,[S,D,T,B]} {6,[S,D,T,B]}
3   C u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
6   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s2_3_6",
    group = 
"""
1 * C u0 {3,[S,D,T,B]} {6,[S,D,T,B]}
2   C u0 {4,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
5   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
6   C u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
7   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s2_4_4",
    group = 
"""
1 * C u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
4   C u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5   C u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s2_4_5",
    group = 
"""
1 * C u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
6   C u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
7   C u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s2_4_6",
    group = 
"""
1 * C u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
2   C u0 {5,[S,D,T,B]} {7,[S,D,T,B]}
3   C u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
5   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {8,[S,D,T,B]}
6   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
7   C u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
8   C u0 {3,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s2_5_5",
    group = 
"""
1 * C u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {5,[S,D,T,B]} {7,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {7,[S,D,T,B]}
4   C u0 {3,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
6   C u0 {4,[S,D,T,B]} {8,[S,D,T,B]}
7   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {8,[S,D,T,B]}
8   C u0 {6,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s2_5_6",
    group = 
"""
1 * C u0 {3,[S,D,T,B]} {7,[S,D,T,B]} {8,[S,D,T,B]}
2   C u0 {5,[S,D,T,B]} {7,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   C u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
6   C u0 {8,[S,D,T,B]} {9,[S,D,T,B]}
7   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]} {9,[S,D,T,B]}
8   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
9   C u0 {6,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s2_6_6",
    group = 
"""
1  * C u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
2    C u0 {7,[S,D,T,B]} {9,[S,D,T,B]}
3    C u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
4    C u0 {3,[S,D,T,B]} {8,[S,D,T,B]} {10,[S,D,T,B]}
5    C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
6    C u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
7    C u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
8    C u0 {4,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
9    C u0 {2,[S,D,T,B]} {10,[S,D,T,B]}
10   C u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s3_4_4",
    group = 
"""
1 * C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
3   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
5   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s3_4_5",
    group = 
"""
1 * C u0 {4,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {4,[S,D,T,B]} {5,[S,D,T,B]}
3   C u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]} {3,[S,D,T,B]}
6   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s3_4_6",
    group = 
"""
1 * C u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
2   C u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
3   C u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
5   C u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
7   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s3_5_5",
    group = 
"""
1 * C u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {4,[S,D,T,B]} {5,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]} {6,[S,D,T,B]}
6   C u0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s3_5_6",
    group = 
"""
1 * C u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
2   C u0 {5,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
3   C u0 {4,[S,D,T,B]} {7,[S,D,T,B]} {8,[S,D,T,B]}
4   C u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
6   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
7   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
8   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s3_6_6",
    group = 
"""
1 * C u0 {5,[S,D,T,B]} {7,[S,D,T,B]}
2   C u0 {4,[S,D,T,B]} {8,[S,D,T,B]} {9,[S,D,T,B]}
3   C u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
6   C u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
7   C u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
8   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
9   C u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

# L3 non-leaves
entry(
    index = 0,
    label = "s1_3_5_ene",
    group = "OR{s1_3_5_ene_1, s1_3_5_ene_2}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_3_5_diene",
    group = "OR{s1_3_5_diene_1_3}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_3_6_ene",
    group = "OR{s1_3_6_ene_1,s1_3_6_ene_2}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_3_6_diene",
    group = "OR{s1_3_6_diene_1_4,s1_3_6_diene_1_3}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_4_4_ene",
    group = "OR{s1_4_4_ene_1}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_4_4_diene",
    group = "OR{s1_4_4_diene_1_5}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)


entry(
    index = 0,
    label = "s1_4_5_ene",
    group = "OR{s1_4_5_ene_1,s1_4_5_ene_2, s1_4_5_ene_6}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_4_5_diene",
    group = "OR{s1_4_5_diene_1_3, s1_4_5_diene_1_6, s1_4_5_diene_2_6}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_4_6_ene",
    group = "OR{s1_4_6_ene_1, s1_4_6_ene_2, s1_4_6_ene_7}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_4_6_diene",
    group = "OR{s1_4_6_diene_1_3, s1_4_6_diene_1_4, s1_4_6_diene_1_7, s1_4_6_diene_2_7}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_5_5_ene",
    group = "OR{s1_5_5_ene_1, s1_5_5_ene_2}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_5_5_diene",
    group = "OR{s1_5_5_diene_1_3, s1_5_5_diene_1_6, s1_5_5_diene_1_7, s1_5_5_diene_2_7}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_5_6_ene",
    group = "OR{s1_5_6_ene_1, s1_5_6_ene_2, s1_5_6_ene_7, s1_5_6_ene_8}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_5_6_diene",
    group = "OR{s1_5_6_diene_1_3, s1_5_6_diene_1_4, s1_5_6_diene_1_7, s1_5_6_diene_1_8, s1_5_6_diene_2_7, s1_5_6_diene_2_8, s1_5_6_diene_7_9}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_6_6_ene",
    group = "OR{s1_6_6_ene_1, s1_6_6_ene_2}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s1_6_6_diene",
    group = "OR{s1_6_6_diene_1_3, s1_6_6_diene_1_4, s1_6_6_diene_1_7, s1_6_6_diene_1_8, s1_6_6_diene_2_8}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s2_3_4_ene",
    group = "OR{s2_3_4_ene_1}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)
entry(
    index = 0,
    label = "s2_3_5_ene",
    group = "OR{s2_3_5_ene_1}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)
entry(
    index = 0,
    label = "s2_3_6_ene",
    group = "OR{s2_3_6_ene_1, s2_3_6_ene_2}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)
entry(
    index = 0,
    label = "s2_3_6_diene",
    group = "OR{s2_3_6_diene_1_3}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)
entry(
    index = 0,
    label = "s2_4_4_ene",
    group = "OR{s2_4_4_ene_1}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)
entry(
    index = 0,
    label = "s2_4_5_ene",
    group = "OR{s2_4_5_ene_1}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)
entry(
    index = 0,
    label = "s2_4_6_ene",
    group = "OR{s2_4_6_ene_1, s2_4_6_ene_2}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)
entry(
    index = 0,
    label = "s2_5_5_ene",
    group = "OR{s2_5_5_ene_0, s2_5_5_ene_1, s2_5_5_ene_m}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)
entry(
    index = 0,
    label = "s2_5_5_diene",
    group = "OR{s2_5_5_diene_0_2, s2_5_5_diene_0_3, s2_5_5_diene_m_2, s2_5_5_diene_0_4, s2_5_5_diene_0_5, s2_5_5_diene_0_6, s2_5_5_diene_1_5, s2_5_5_diene_1_6}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)
entry(
    index = 0,
    label = "s2_5_6_ene",
    group = "OR{s2_5_6_ene_0, s2_5_6_ene_1, s2_5_6_ene_m, s2_5_6_ene_2, s2_5_6_ene_5, s2_5_6_ene_6}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)
entry(
    index = 0,
    label = "s2_5_6_diene",
    group = "OR{s2_5_6_diene_m_1, s2_5_6_diene_m_2, s2_5_6_diene_m_7, s2_5_6_diene_0_2, s2_5_6_diene_0_3,s2_5_6_diene_0_4,s2_5_6_diene_0_5, s2_5_6_diene_0_6,s2_5_6_diene_0_7,s2_5_6_diene_1_3,s2_5_6_diene_1_5, s2_5_6_diene_1_6, s2_5_6_diene_1_7,s2_5_6_diene_2_5,s2_5_6_diene_2_6,s2_5_6_diene_5_7,s2_5_6_diene_5_8}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)
entry(
    index = 0,
    label = "s2_6_6_ene",
    group = "OR{s2_6_6_ene_0, s2_6_6_ene_1, s2_6_6_ene_2, s2_6_6_ene_m}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)
entry(
    index = 0,
    label = "s2_6_6_diene",
    group = "OR{s2_6_6_diene_m_1, s2_6_6_diene_m_2, s2_6_6_diene_0_2, s2_6_6_diene_0_3, s2_6_6_diene_0_4,s2_6_6_diene_0_5,s2_6_6_diene_0_6,s2_6_6_diene_0_7,s2_6_6_diene_0_8,s2_6_6_diene_1_3,s2_6_6_diene_1_6,s2_6_6_diene_1_7,s2_6_6_diene_1_8,s2_6_6_diene_2_7}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)
entry(
    index = 0,
    label = "s3_4_4_ene",
    group = "OR{s3_4_4_ene_0}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)
entry(
    index = 0,
    label = "s3_4_4_diene",
    group = "OR{s3_4_4_diene_0_2}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)
entry(
    index = 0,
    label = "s3_4_5_ene",
    group = "OR{s3_4_5_ene_0, s3_4_5_ene_1, s3_4_5_ene_3}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)
entry(
    index = 0,
    label = "s3_4_5_diene",
    group = "OR{s3_4_5_diene_0_2, s3_4_5_diene_0_3, s3_4_5_diene_1_3, s3_4_5_diene_3_4}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)
entry(
    index = 0,
    label = "s3_4_6_ene",
    group = "OR{s3_4_6_ene_0, s3_4_6_ene_1, s3_4_6_ene_4}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s3_4_6_diene",
    group = "OR{s3_4_6_diene_0_2, s3_4_6_diene_0_3, s3_4_6_diene_0_4, s3_4_6_diene_1_4, s3_4_6_diene_1_5}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s3_5_5_ene",
    group = "OR{s3_5_5_ene_1}", 
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s3_5_5_diene",
    group = "OR{s3_5_5_diene_1_4}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s3_5_6_ene",
    group = "OR{s3_5_6_ene_1, s3_5_6_ene_5}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s3_5_6_diene",
    group = "OR{s3_5_6_diene_1_5}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s3_6_6_ene",
    group = "OR{s3_6_6_ene_0, s3_6_6_ene_1, s3_6_6_ene_4}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "s3_6_6_diene",
    group = "OR{s3_6_6_diene_0_m, s3_6_6_diene_0_2, s3_6_6_diene_0_3, s3_6_6_diene_0_4, s3_6_6_diene_0_5, s3_6_6_diene_0_6, s3_6_6_diene_1_m, s3_6_6_diene_1_5, s3_6_6_diene_1_6, s3_6_6_diene_1_8}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)
# leaves

entry(
    index = 2,
    label = "s1_3_3_ane",
    group = 
"""
1 * Cs u0 {2,S} {3,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S} {4,S} {5,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {3,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "s1_3_3_ene",
    group = 
"""
1 * Cd u0 {2,D} {4,S}
2   Cd u0 {1,D} {4,S}
3   Cs u0 {4,S} {5,S}
4   Cs u0 {1,S} {2,S} {3,S} {5,S}
5   Cs u0 {3,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "s1_3_4_ane",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {6,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "s1_3_4_ene",
    group = 
"""
1 * Cd u0 {5,D} {6,S}
2   Cs u0 {5,S} {6,S}
3   Cs u0 {4,S} {6,S}
4   Cs u0 {3,S} {6,S}
5   Cd u0 {1,D} {2,S}
6   Cs u0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "s1_3_5_ane",
    group = 
"""
1 * Cs u0 {5,S} {6,S}
2   Cs u0 {3,S} {4,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {2,S} {3,S} {6,S} {7,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {1,S} {4,S}
7   Cs u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "s1_3_5_ene_1",
    group = 
"""
1 * Cs u0 {5,S} {7,S}
2   Cs u0 {3,S} {5,S}
3   Cs u0 {2,S} {5,S}
4   Cd u0 {5,S} {6,D}
5   Cs u0 {1,S} {2,S} {3,S} {4,S}
6   Cd u0 {4,D} {7,S}
7   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "s1_3_5_ene_2",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S} {6,S}
2   Cs u0 {1,S} {7,S}
3   Cs u0 {1,S} {6,S}
4   Cs u0 {1,S} {5,S}
5   Cd u0 {4,S} {7,D}
6   Cs u0 {1,S} {3,S}
7   Cd u0 {2,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "s1_3_5_diene_1_3",
    group = 
"""
1 * Cd u0 {4,D} {6,S}
2   Cd u0 {3,D} {4,S}
3   Cd u0 {2,D} {6,S}
4   Cd u0 {1,D} {2,S}
5   Cs u0 {6,S} {7,S}
6   Cs u0 {1,S} {3,S} {5,S} {7,S}
7   Cs u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "s1_3_6_ane",
    group = 
"""
1 * Cs u0 {3,S} {5,S}
2   Cs u0 {4,S} {6,S} {7,S} {8,S}
3   Cs u0 {1,S} {6,S}
4   Cs u0 {2,S} {7,S}
5   Cs u0 {1,S} {8,S}
6   Cs u0 {2,S} {3,S}
7   Cs u0 {2,S} {4,S}
8   Cs u0 {2,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "s1_3_6_ene_1",
    group = 
"""
1 * Cs u0 {3,S} {6,S}
2   Cs u0 {5,S} {7,S}
3   Cs u0 {1,S} {6,S}
4   Cd u0 {5,S} {8,D}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {1,S} {3,S} {7,S} {8,S}
7   Cs u0 {2,S} {6,S}
8   Cd u0 {4,D} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "s1_3_6_ene_2",
    group = 
"""
1 * Cs u0 {4,S} {7,S}
2   Cd u0 {3,S} {5,D}
3   Cs u0 {2,S} {7,S}
4   Cs u0 {1,S} {7,S}
5   Cd u0 {2,D} {8,S}
6   Cs u0 {7,S} {8,S}
7   Cs u0 {1,S} {3,S} {4,S} {6,S}
8   Cs u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "s1_3_6_diene_1_4",
    group = 
"""
1 * Cd u0 {6,D} {7,S}
2   Cs u0 {4,S} {6,S}
3   Cd u0 {4,D} {7,S}
4   Cd u0 {2,S} {3,D}
5   Cs u0 {7,S} {8,S}
6   Cd u0 {1,D} {2,S}
7   Cs u0 {1,S} {3,S} {5,S} {8,S}
8   Cs u0 {5,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "s1_3_6_diene_1_3",
    group = 
"""
1 * Cs u0 {4,S} {6,S}
2   Cd u0 {5,S} {7,D}
3   Cs u0 {4,S} {7,S}
4   Cs u0 {1,S} {3,S} {6,S} {8,S}
5   Cd u0 {2,S} {8,D}
6   Cs u0 {1,S} {4,S}
7   Cd u0 {2,D} {3,S}
8   Cd u0 {4,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "s1_4_4_ane",
    group = 
"""
1 * Cs u0 {2,S} {7,S}
2   Cs u0 {1,S} {3,S} {4,S} {6,S}
3   Cs u0 {2,S} {7,S}
4   Cs u0 {2,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {2,S} {5,S}
7   Cs u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "s1_4_4_ene_1",
    group = 
"""
1 * Cs u0 {3,S} {5,S}
2   Cs u0 {4,S} {7,S}
3   Cs u0 {1,S} {4,S} {6,S} {7,S}
4   Cs u0 {2,S} {3,S}
5   Cd u0 {1,S} {6,D}
6   Cd u0 {3,S} {5,D}
7   Cs u0 {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "s1_4_4_diene_1_5",
    group = 
"""
1 * Cd u0 {3,D} {5,S}
2   Cd u0 {4,S} {7,D}
3   Cd u0 {1,D} {6,S}
4   Cs u0 {2,S} {5,S}
5   Cs u0 {1,S} {4,S} {6,S} {7,S}
6   Cs u0 {3,S} {5,S}
7   Cd u0 {2,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "s1_4_5_ane",
    group = 
"""
1 * Cs u0 {2,S} {3,S}
2   Cs u0 {1,S} {8,S}
3   Cs u0 {1,S} {5,S} {6,S} {7,S}
4   Cs u0 {5,S} {7,S}
5   Cs u0 {3,S} {4,S}
6   Cs u0 {3,S} {8,S}
7   Cs u0 {3,S} {4,S}
8   Cs u0 {2,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "s1_4_5_ene_1",
    group = 
"""
1 * Cs u0 {5,S} {6,S}
2   Cs u0 {4,S} {5,S}
3   Cd u0 {5,S} {8,D}
4   Cs u0 {2,S} {7,S}
5   Cs u0 {1,S} {2,S} {3,S} {7,S}
6   Cs u0 {1,S} {8,S}
7   Cs u0 {4,S} {5,S}
8   Cd u0 {3,D} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "s1_4_5_ene_2",
    group = 
"""
1 * Cd u0 {3,D} {5,S}
2   Cs u0 {4,S} {5,S} {6,S} {7,S}
3   Cd u0 {1,D} {4,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {1,S} {2,S}
6   Cs u0 {2,S} {8,S}
7   Cs u0 {2,S} {8,S}
8   Cs u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "s1_4_5_ene_6",
    group = 
"""
1 * Cd u0 {3,D} {5,S}
2   Cs u0 {7,S} {8,S}
3   Cd u0 {1,D} {8,S}
4   Cs u0 {6,S} {7,S}
5   Cs u0 {1,S} {8,S}
6   Cs u0 {4,S} {8,S}
7   Cs u0 {2,S} {4,S}
8   Cs u0 {2,S} {3,S} {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "s1_4_5_diene_1_3",
    group = 
"""
1 * Cs u0 {4,S} {8,S}
2   Cd u0 {5,D} {6,S}
3   Cs u0 {4,S} {5,S} {7,S} {8,S}
4   Cs u0 {1,S} {3,S}
5   Cd u0 {2,D} {3,S}
6   Cd u0 {2,S} {7,D}
7   Cd u0 {3,S} {6,D}
8   Cs u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "s1_4_5_diene_1_6",
    group = 
"""
1 * Cs u0 {2,S} {5,S}
2   Cd u0 {1,S} {6,D}
3   Cs u0 {4,S} {5,S} {6,S} {7,S}
4   Cd u0 {3,S} {8,D}
5   Cs u0 {1,S} {3,S}
6   Cd u0 {2,D} {3,S}
7   Cs u0 {3,S} {8,S}
8   Cd u0 {4,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "s1_4_5_diene_2_6",
    group = 
"""
1 * Cs u0 {3,S} {6,S}
2   Cd u0 {3,D} {7,S}
3   Cd u0 {1,S} {2,D}
4   Cd u0 {5,D} {6,S}
5   Cd u0 {4,D} {8,S}
6   Cs u0 {1,S} {4,S} {7,S} {8,S}
7   Cs u0 {2,S} {6,S}
8   Cs u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "s1_4_6_ane",
    group = 
"""
1 * Cs u0 {3,S} {9,S}
2   Cs u0 {5,S} {7,S}
3   Cs u0 {1,S} {8,S}
4   Cs u0 {5,S} {8,S}
5   Cs u0 {2,S} {4,S} {6,S} {9,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {2,S} {6,S}
8   Cs u0 {3,S} {4,S}
9   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "s1_4_6_ene_1",
    group = 
"""
1 * Cs u0 {4,S} {6,S}
2   Cs u0 {4,S} {5,S} {6,S} {9,S}
3   Cs u0 {7,S} {8,S}
4   Cs u0 {1,S} {2,S}
5   Cd u0 {2,S} {8,D}
6   Cs u0 {1,S} {2,S}
7   Cs u0 {3,S} {9,S}
8   Cd u0 {3,S} {5,D}
9   Cs u0 {2,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "s1_4_6_ene_2",
    group = 
"""
1 * Cs u0 {3,S} {4,S} {5,S} {6,S}
2   Cd u0 {7,S} {9,D}
3   Cs u0 {1,S} {7,S}
4   Cs u0 {1,S} {8,S}
5   Cs u0 {1,S} {8,S}
6   Cs u0 {1,S} {9,S}
7   Cs u0 {2,S} {3,S}
8   Cs u0 {4,S} {5,S}
9   Cd u0 {2,D} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "s1_4_6_ene_7",
    group = 
"""
1 * Cd u0 {2,D} {7,S}
2   Cd u0 {1,D} {6,S}
3   Cs u0 {6,S} {8,S}
4   Cs u0 {5,S} {6,S}
5   Cs u0 {4,S} {9,S}
6   Cs u0 {2,S} {3,S} {4,S} {7,S}
7   Cs u0 {1,S} {6,S}
8   Cs u0 {3,S} {9,S}
9   Cs u0 {5,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "s1_4_6_diene_1_3",
    group = 
"""
1 * Cs u0 {2,S} {5,S} {8,S} {9,S}
2   Cs u0 {1,S} {6,S}
3   Cs u0 {5,S} {9,S}
4   Cd u0 {7,S} {8,D}
5   Cs u0 {1,S} {3,S}
6   Cd u0 {2,S} {7,D}
7   Cd u0 {4,S} {6,D}
8   Cd u0 {1,S} {4,D}
9   Cs u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "s1_4_6_diene_1_4",
    group = 
"""
1 * Cs u0 {2,S} {4,S} {5,S} {6,S}
2   Cd u0 {1,S} {8,D}
3   Cd u0 {6,D} {7,S}
4   Cs u0 {1,S} {9,S}
5   Cs u0 {1,S} {9,S}
6   Cd u0 {1,S} {3,D}
7   Cs u0 {3,S} {8,S}
8   Cd u0 {2,D} {7,S}
9   Cs u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "s1_4_6_diene_1_7",
    group = 
"""
1 * Cs u0 {6,S} {8,S}
2   Cs u0 {4,S} {5,S} {7,S} {8,S}
3   Cd u0 {4,D} {5,S}
4   Cd u0 {2,S} {3,D}
5   Cs u0 {2,S} {3,S}
6   Cs u0 {1,S} {9,S}
7   Cd u0 {2,S} {9,D}
8   Cs u0 {1,S} {2,S}
9   Cd u0 {6,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "s1_4_6_diene_2_7",
    group = 
"""
1 * Cd u0 {8,S} {9,D}
2   Cs u0 {4,S} {8,S}
3   Cd u0 {6,D} {7,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {8,S} {9,S}
6   Cd u0 {3,D} {4,S}
7   Cs u0 {3,S} {8,S}
8   Cs u0 {1,S} {2,S} {5,S} {7,S}
9   Cd u0 {1,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "s1_5_5_ane",
    group = 
"""
1 * Cs u0 {8,S} {9,S}
2   Cs u0 {4,S} {5,S}
3   Cs u0 {5,S} {9,S}
4   Cs u0 {2,S} {9,S}
5   Cs u0 {2,S} {3,S}
6   Cs u0 {7,S} {9,S}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {1,S} {7,S}
9   Cs u0 {1,S} {3,S} {4,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "s1_5_5_ene_1",
    group = 
"""
1 * Cd u0 {4,D} {5,S}
2   Cs u0 {6,S} {8,S}
3   Cs u0 {6,S} {9,S}
4   Cd u0 {1,D} {8,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {2,S} {3,S}
7   Cs u0 {5,S} {8,S}
8   Cs u0 {2,S} {4,S} {7,S} {9,S}
9   Cs u0 {3,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "s1_5_5_ene_2",
    group = 
"""
1 * Cs u0 {5,S} {6,S}
2   Cs u0 {3,S} {6,S}
3   Cd u0 {2,S} {8,D}
4   Cs u0 {6,S} {8,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {1,S} {2,S} {4,S} {9,S}
7   Cs u0 {5,S} {9,S}
8   Cd u0 {3,D} {4,S}
9   Cs u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "s1_5_5_diene_1_3",
    group = 
"""
1 * Cs u0 {7,S} {9,S}
2   Cs u0 {3,S} {5,S} {8,S} {9,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {6,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {4,S} {5,D}
7   Cs u0 {1,S} {8,S}
8   Cs u0 {2,S} {7,S}
9   Cs u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "s1_5_5_diene_1_6",
    group = 
"""
1 * Cs u0 {2,S} {4,S}
2   Cs u0 {1,S} {5,S}
3   Cs u0 {4,S} {6,S}
4   Cs u0 {1,S} {3,S} {7,S} {8,S}
5   Cd u0 {2,S} {8,D}
6   Cs u0 {3,S} {9,S}
7   Cd u0 {4,S} {9,D}
8   Cd u0 {4,S} {5,D}
9   Cd u0 {6,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "s1_5_5_diene_1_7",
    group = 
"""
1 * Cd u0 {6,S} {9,D}
2   Cs u0 {4,S} {6,S} {7,S} {8,S}
3   Cd u0 {4,D} {5,S}
4   Cd u0 {2,S} {3,D}
5   Cs u0 {3,S} {8,S}
6   Cs u0 {1,S} {2,S}
7   Cs u0 {2,S} {9,S}
8   Cs u0 {2,S} {5,S}
9   Cd u0 {1,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "s1_5_5_diene_2_7",
    group = 
"""
1 * Cs u0 {4,S} {9,S}
2   Cs u0 {4,S} {7,S}
3   Cd u0 {7,D} {8,S}
4   Cs u0 {1,S} {2,S} {5,S} {8,S}
5   Cs u0 {4,S} {6,S}
6   Cd u0 {5,S} {9,D}
7   Cd u0 {2,S} {3,D}
8   Cs u0 {3,S} {4,S}
9   Cd u0 {1,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "s1_5_6_ane",
    group = 
"""
1  * Cs u0 {2,S} {5,S}
2    Cs u0 {1,S} {3,S}
3    Cs u0 {2,S} {4,S}
4    Cs u0 {3,S} {5,S} {7,S} {10,S}
5    Cs u0 {1,S} {4,S}
6    Cs u0 {8,S} {9,S}
7    Cs u0 {4,S} {8,S}
8    Cs u0 {6,S} {7,S}
9    Cs u0 {6,S} {10,S}
10   Cs u0 {4,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "s1_5_6_ene_1",
    group = 
"""
1  * Cs u0 {3,S} {7,S}
2    Cs u0 {3,S} {8,S} {9,S} {10,S}
3    Cs u0 {1,S} {2,S}
4    Cd u0 {5,S} {8,D}
5    Cs u0 {4,S} {6,S}
6    Cs u0 {5,S} {9,S}
7    Cs u0 {1,S} {10,S}
8    Cd u0 {2,S} {4,D}
9    Cs u0 {2,S} {6,S}
10   Cs u0 {2,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "s1_5_6_ene_2",
    group = 
"""
1  * Cd u0 {3,S} {8,D}
2    Cs u0 {3,S} {10,S}
3    Cs u0 {1,S} {2,S}
4    Cs u0 {8,S} {10,S}
5    Cs u0 {6,S} {9,S}
6    Cs u0 {5,S} {10,S}
7    Cs u0 {9,S} {10,S}
8    Cd u0 {1,D} {4,S}
9    Cs u0 {5,S} {7,S}
10   Cs u0 {2,S} {4,S} {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "s1_5_6_ene_7",
    group = 
"""
1  * Cs u0 {4,S} {8,S}
2    Cd u0 {4,S} {9,D}
3    Cs u0 {5,S} {6,S}
4    Cs u0 {1,S} {2,S} {6,S} {7,S}
5    Cs u0 {3,S} {8,S}
6    Cs u0 {3,S} {4,S}
7    Cs u0 {4,S} {10,S}
8    Cs u0 {1,S} {5,S}
9    Cd u0 {2,D} {10,S}
10   Cs u0 {7,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "s1_5_6_ene_8",
    group = 
"""
1  * Cs u0 {5,S} {6,S}
2    Cs u0 {4,S} {5,S}
3    Cs u0 {6,S} {10,S}
4    Cd u0 {2,S} {8,D}
5    Cs u0 {1,S} {2,S} {7,S} {9,S}
6    Cs u0 {1,S} {3,S}
7    Cs u0 {5,S} {10,S}
8    Cd u0 {4,D} {9,S}
9    Cs u0 {5,S} {8,S}
10   Cs u0 {3,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "s1_5_6_diene_1_3",
    group = 
"""
1  * Cd u0 {6,S} {8,D}
2    Cs u0 {4,S} {10,S}
3    Cs u0 {9,S} {10,S}
4    Cs u0 {2,S} {5,S} {8,S} {9,S}
5    Cs u0 {4,S} {7,S}
6    Cd u0 {1,S} {7,D}
7    Cd u0 {5,S} {6,D}
8    Cd u0 {1,D} {4,S}
9    Cs u0 {3,S} {4,S}
10   Cs u0 {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "s1_5_6_diene_1_4",
    group = 
"""
1  * Cs u0 {2,S} {6,S} {8,S} {10,S}
2    Cs u0 {1,S} {3,S}
3    Cs u0 {2,S} {4,S}
4    Cs u0 {3,S} {10,S}
5    Cs u0 {7,S} {9,S}
6    Cd u0 {1,S} {7,D}
7    Cd u0 {5,S} {6,D}
8    Cd u0 {1,S} {9,D}
9    Cd u0 {5,S} {8,D}
10   Cs u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "s1_5_6_diene_1_7",
    group = 
"""
1  * Cs u0 {3,S} {6,S}
2    Cs u0 {5,S} {8,S}
3    Cs u0 {1,S} {8,S}
4    Cd u0 {8,S} {9,D}
5    Cs u0 {2,S} {9,S}
6    Cs u0 {1,S} {7,S}
7    Cd u0 {6,S} {10,D}
8    Cs u0 {2,S} {3,S} {4,S} {10,S}
9    Cd u0 {4,D} {5,S}
10   Cd u0 {7,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "s1_5_6_diene_1_8",
    group = 
"""
1  * Cd u0 {5,S} {10,D}
2    Cs u0 {6,S} {9,S}
3    Cd u0 {4,D} {8,S}
4    Cd u0 {3,D} {6,S}
5    Cs u0 {1,S} {8,S}
6    Cs u0 {2,S} {4,S}
7    Cs u0 {8,S} {10,S}
8    Cs u0 {3,S} {5,S} {7,S} {9,S}
9    Cs u0 {2,S} {8,S}
10   Cd u0 {1,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "s1_5_6_diene_2_7",
    group = 
"""
1  * Cs u0 {2,S} {4,S} {5,S} {10,S}
2    Cs u0 {1,S} {6,S}
3    Cs u0 {9,S} {10,S}
4    Cd u0 {1,S} {9,D}
5    Cs u0 {1,S} {8,S}
6    Cs u0 {2,S} {7,S}
7    Cd u0 {6,S} {8,D}
8    Cd u0 {5,S} {7,D}
9    Cd u0 {3,S} {4,D}
10   Cs u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "s1_5_6_diene_2_8",
    group = 
"""
1  * Cs u0 {2,S} {5,S}
2    Cs u0 {1,S} {4,S} {6,S} {10,S}
3    Cd u0 {8,D} {9,S}
4    Cs u0 {2,S} {9,S}
5    Cd u0 {1,S} {7,D}
6    Cs u0 {2,S} {7,S}
7    Cd u0 {5,D} {6,S}
8    Cd u0 {3,D} {10,S}
9    Cs u0 {3,S} {4,S}
10   Cs u0 {2,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "s1_5_6_diene_7_9",
    group = 
"""
1  * Cd u0 {2,D} {6,S}
2    Cd u0 {1,D} {5,S}
3    Cs u0 {4,S} {9,S}
4    Cs u0 {3,S} {7,S}
5    Cd u0 {2,S} {10,D}
6    Cs u0 {1,S} {7,S} {8,S} {10,S}
7    Cs u0 {4,S} {6,S}
8    Cs u0 {6,S} {9,S}
9    Cs u0 {3,S} {8,S}
10   Cd u0 {5,D} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "s1_6_6_ane",
    group = 
"""
1  * Cs u0 {5,S} {9,S}
2    Cs u0 {10,S} {11,S}
3    Cs u0 {4,S} {7,S} {8,S} {11,S}
4    Cs u0 {3,S} {6,S}
5    Cs u0 {1,S} {8,S}
6    Cs u0 {4,S} {10,S}
7    Cs u0 {3,S} {9,S}
8    Cs u0 {3,S} {5,S}
9    Cs u0 {1,S} {7,S}
10   Cs u0 {2,S} {6,S}
11   Cs u0 {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "s1_6_6_ene_1",
    group = 
"""
1  * Cs u0 {8,S} {11,S}
2    Cs u0 {3,S} {11,S}
3    Cs u0 {2,S} {6,S} {9,S} {10,S}
4    Cs u0 {5,S} {7,S}
5    Cd u0 {4,S} {10,D}
6    Cs u0 {3,S} {8,S}
7    Cs u0 {4,S} {9,S}
8    Cs u0 {1,S} {6,S}
9    Cs u0 {3,S} {7,S}
10   Cd u0 {3,S} {5,D}
11   Cs u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "s1_6_6_ene_2",
    group = 
"""
1  * Cs u0 {2,S} {11,S}
2    Cd u0 {1,S} {7,D}
3    Cs u0 {4,S} {9,S}
4    Cs u0 {3,S} {10,S}
5    Cs u0 {6,S} {9,S}
6    Cs u0 {5,S} {8,S} {10,S} {11,S}
7    Cd u0 {2,D} {8,S}
8    Cs u0 {6,S} {7,S}
9    Cs u0 {3,S} {5,S}
10   Cs u0 {4,S} {6,S}
11   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "s1_6_6_diene_1_3",
    group = 
"""
1  * Cd u0 {2,D} {8,S}
2    Cd u0 {1,D} {4,S}
3    Cs u0 {6,S} {11,S}
4    Cs u0 {2,S} {5,S} {7,S} {11,S}
5    Cs u0 {4,S} {10,S}
6    Cs u0 {3,S} {9,S}
7    Cs u0 {4,S} {9,S}
8    Cd u0 {1,S} {10,D}
9    Cs u0 {6,S} {7,S}
10   Cd u0 {5,S} {8,D}
11   Cs u0 {3,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "s1_6_6_diene_1_4",
    group = 
"""
1  * Cs u0 {3,S} {10,S}
2    Cs u0 {5,S} {7,S} {8,S} {11,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {6,S} {9,S}
5    Cd u0 {2,S} {10,D}
6    Cs u0 {4,S} {8,S}
7    Cd u0 {2,S} {3,D}
8    Cs u0 {2,S} {6,S}
9    Cs u0 {4,S} {11,S}
10   Cd u0 {1,S} {5,D}
11   Cs u0 {2,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "s1_6_6_diene_1_7",
    group = 
"""
1  * Cs u0 {2,S} {6,S} {8,S} {11,S}
2    Cs u0 {1,S} {10,S}
3    Cs u0 {5,S} {9,S}
4    Cs u0 {7,S} {10,S}
5    Cs u0 {3,S} {8,S}
6    Cd u0 {1,S} {7,D}
7    Cd u0 {4,S} {6,D}
8    Cs u0 {1,S} {5,S}
9    Cd u0 {3,S} {11,D}
10   Cs u0 {2,S} {4,S}
11   Cd u0 {1,S} {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "s1_6_6_diene_1_8",
    group = 
"""
1  * Cs u0 {7,S} {10,S}
2    Cs u0 {6,S} {7,S}
3    Cd u0 {8,S} {11,D}
4    Cs u0 {6,S} {11,S}
5    Cs u0 {6,S} {8,S}
6    Cs u0 {2,S} {4,S} {5,S} {9,S}
7    Cs u0 {1,S} {2,S}
8    Cs u0 {3,S} {5,S}
9    Cd u0 {6,S} {10,D}
10   Cd u0 {1,S} {9,D}
11   Cd u0 {3,D} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "s1_6_6_diene_2_8",
    group = 
"""
1  * Cd u0 {5,S} {10,D}
2    Cs u0 {5,S} {11,S}
3    Cd u0 {6,D} {8,S}
4    Cs u0 {6,S} {11,S}
5    Cs u0 {1,S} {2,S}
6    Cd u0 {3,D} {4,S}
7    Cs u0 {8,S} {11,S}
8    Cs u0 {3,S} {7,S}
9    Cs u0 {10,S} {11,S}
10   Cd u0 {1,D} {9,S}
11   Cs u0 {2,S} {4,S} {7,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "s2_3_3_ane",
    group = 
"""
1 * Cs u0 {2,S} {3,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S} {4,S}
4   Cs u0 {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "s2_3_3_ene",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {3,S} {4,D}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {1,S} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "s2_3_4_ane",
    group = 
"""
1   Cs u0 {2,S} {5,S}
2 * Cs u0 {1,S} {3,S} {5,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {1,S} {2,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "s2_3_4_ene_1",
    group = 
"""
1 * Cs u0 {4,S} {5,S}
2   Cd u0 {3,D} {5,S}
3   Cd u0 {2,D} {4,S}
4   Cs u0 {1,S} {3,S} {5,S}
5   Cs u0 {1,S} {2,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "s2_3_5_ane",
    group = 
"""
1 * Cs u0 {4,S} {5,S} {6,S}
2   Cs u0 {3,S} {6,S}
3   Cs u0 {2,S} {5,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {1,S} {3,S} {4,S}
6   Cs u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "s2_3_5_ene_1",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S} {4,S}
4   Cd u0 {3,S} {6,D}
5   Cs u0 {1,S} {6,S}
6   Cd u0 {4,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "s2_3_6_ane",
    group = 
"""
1 * Cs u0 {3,S} {6,S}
2   Cs u0 {4,S} {5,S} {7,S}
3   Cs u0 {1,S} {7,S}
4   Cs u0 {2,S} {5,S}
5   Cs u0 {2,S} {4,S} {6,S}
6   Cs u0 {1,S} {5,S}
7   Cs u0 {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "s2_3_6_ene_1",
    group = 
"""
1 * Cd u0 {2,S} {5,D}
2   Cs u0 {1,S} {3,S} {6,S}
3   Cs u0 {2,S} {6,S}
4   Cs u0 {6,S} {7,S}
5   Cd u0 {1,D} {7,S}
6   Cs u0 {2,S} {3,S} {4,S}
7   Cs u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "s2_3_6_ene_2",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {4,S}
3   Cs u0 {1,S} {7,S}
4   Cs u0 {1,S} {2,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cd u0 {5,S} {7,D}
7   Cd u0 {3,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "s2_3_6_diene_1_3",
    group = 
"""
1 * Cd u0 {3,D} {7,S}
2   Cs u0 {4,S} {5,S} {6,S}
3   Cd u0 {1,D} {4,S}
4   Cs u0 {2,S} {3,S} {6,S}
5   Cd u0 {2,S} {7,D}
6   Cs u0 {2,S} {4,S}
7   Cd u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "s2_4_4_ane",
    group = 
"""
1 * Cs u0 {2,S} {6,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {2,S} {4,S} {6,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {1,S} {3,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "s2_4_4_ene_1",
    group = 
"""
1 * Cs u0 {2,S} {5,S}
2   Cs u0 {1,S} {6,S}
3   Cd u0 {4,D} {5,S}
4   Cd u0 {3,D} {6,S}
5   Cs u0 {1,S} {3,S} {6,S}
6   Cs u0 {2,S} {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "s2_4_5_ane",
    group = 
"""
1 * Cs u0 {3,S} {4,S} {5,S}
2   Cs u0 {4,S} {7,S}
3   Cs u0 {1,S} {6,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {1,S} {6,S} {7,S}
6   Cs u0 {3,S} {5,S}
7   Cs u0 {2,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "s2_4_5_ene_1",
    group = 
"""
1 * Cs u0 {4,S} {7,S}
2   Cs u0 {3,S} {6,S}
3   Cs u0 {2,S} {5,S} {7,S}
4   Cd u0 {1,S} {5,D}
5   Cd u0 {3,S} {4,D}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {1,S} {3,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "s2_4_6_ane",
    group = 
"""
1 * Cs u0 {4,S} {6,S}
2   Cs u0 {5,S} {7,S}
3   Cs u0 {6,S} {8,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {2,S} {4,S} {8,S}
6   Cs u0 {1,S} {3,S}
7   Cs u0 {2,S} {8,S}
8   Cs u0 {3,S} {5,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "s2_4_6_ene_1",
    group = 
"""
1 * Cs u0 {3,S} {4,S} {7,S}
2   Cs u0 {4,S} {6,S}
3   Cs u0 {1,S} {5,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {3,S} {7,S}
6   Cd u0 {2,S} {8,D}
7   Cs u0 {1,S} {5,S} {8,S}
8   Cd u0 {6,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "s2_4_6_ene_2",
    group = 
"""
1 * Cs u0 {5,S} {7,S}
2   Cs u0 {4,S} {8,S}
3   Cs u0 {6,S} {7,S}
4   Cs u0 {2,S} {6,S} {7,S}
5   Cd u0 {1,S} {8,D}
6   Cs u0 {3,S} {4,S}
7   Cs u0 {1,S} {3,S} {4,S}
8   Cd u0 {2,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "s2_5_5_ane",
    group = 
"""
1 * Cs u0 {3,S} {5,S}
2   Cs u0 {5,S} {7,S}
3   Cs u0 {1,S} {4,S} {7,S}
4   Cs u0 {3,S} {6,S}
5   Cs u0 {1,S} {2,S}
6   Cs u0 {4,S} {8,S}
7   Cs u0 {2,S} {3,S} {8,S}
8   Cs u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "s2_5_5_ene_0",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {7,S}
3   Cd u0 {1,S} {5,D} {8,S}
4   Cs u0 {1,S} {6,S}
5   Cd u0 {3,D} {6,S}
6   Cs u0 {4,S} {5,S}
7   Cs u0 {2,S} {8,S}
8   Cs u0 {3,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "s2_5_5_ene_1",
    group = 
"""
1 * Cd u0 {5,D} {8,S}
2   Cs u0 {3,S} {4,S} {8,S}
3   Cs u0 {2,S} {7,S}
4   Cs u0 {2,S} {5,S}
5   Cd u0 {1,D} {4,S}
6   Cs u0 {7,S} {8,S}
7   Cs u0 {3,S} {6,S}
8   Cs u0 {1,S} {2,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "s2_5_5_ene_m",
    group = 
"""
1 * Cd u0 {2,D} {3,S} {7,S}
2   Cd u0 {1,D} {6,S} {8,S}
3   Cs u0 {1,S} {5,S}
4   Cs u0 {6,S} {7,S}
5   Cs u0 {3,S} {8,S}
6   Cs u0 {2,S} {4,S}
7   Cs u0 {1,S} {4,S}
8   Cs u0 {2,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "s2_5_5_diene_0_2",
    group = 
"""
1 * Cs u0 {2,S} {8,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cd u0 {2,S} {7,D}
4   Cd u0 {2,S} {5,S} {6,D}
5   Cs u0 {4,S} {8,S}
6   Cd u0 {4,D} {7,S}
7   Cd u0 {3,D} {6,S}
8   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "s2_5_5_diene_0_3",
    group = 
"""
1 * Cs u0 {4,S} {5,S}
2   Cs u0 {6,S} {8,S}
3   Cd u0 {5,D} {6,S} {7,S}
4   Cd u0 {1,S} {7,D}
5   Cd u0 {1,S} {3,D}
6   Cs u0 {2,S} {3,S}
7   Cd u0 {3,S} {4,D} {8,S}
8   Cs u0 {2,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "s2_5_5_diene_m_2",
    group = 
"""
1 * Cs u0 {2,S} {7,S}
2   Cd u0 {1,S} {4,S} {6,D}
3   Cd u0 {6,S} {8,D}
4   Cs u0 {2,S} {8,S}
5   Cs u0 {6,S} {7,S}
6   Cd u0 {2,D} {3,S} {5,S}
7   Cs u0 {1,S} {5,S}
8   Cd u0 {3,D} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "s2_5_5_diene_0_4",
    group = 
"""
1 * Cd u0 {3,S} {7,D}
2   Cs u0 {5,S} {7,S}
3   Cs u0 {1,S} {6,S}
4   Cd u0 {5,S} {8,D}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {3,S} {8,S}
7   Cd u0 {1,D} {2,S} {8,S}
8   Cd u0 {4,D} {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "s2_5_5_diene_0_5",
    group = 
"""
1 * Cd u0 {3,S} {4,D}
2   Cd u0 {5,D} {7,S}
3   Cs u0 {1,S} {5,S} {8,S}
4   Cd u0 {1,D} {6,S}
5   Cd u0 {2,D} {3,S} {6,S}
6   Cs u0 {4,S} {5,S}
7   Cs u0 {2,S} {8,S}
8   Cs u0 {3,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "s2_5_5_diene_0_6",
    group = 
"""
1 * Cs u0 {2,S} {6,S} {8,S}
2   Cd u0 {1,S} {3,S} {7,D}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {3,D} {8,S}
5   Cs u0 {6,S} {7,S}
6   Cs u0 {1,S} {5,S}
7   Cd u0 {2,D} {5,S}
8   Cs u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "s2_5_5_diene_1_5",
    group = 
"""
1 * Cd u0 {2,S} {4,D}
2   Cs u0 {1,S} {6,S} {7,S}
3   Cd u0 {5,D} {6,S}
4   Cd u0 {1,D} {8,S}
5   Cd u0 {3,D} {7,S}
6   Cs u0 {2,S} {3,S} {8,S}
7   Cs u0 {2,S} {5,S}
8   Cs u0 {4,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "s2_5_5_diene_1_6",
    group = 
"""
1 * Cd u0 {2,D} {3,S}
2   Cd u0 {1,D} {7,S}
3   Cs u0 {1,S} {5,S} {6,S}
4   Cd u0 {6,D} {8,S}
5   Cs u0 {3,S} {7,S} {8,S}
6   Cd u0 {3,S} {4,D}
7   Cs u0 {2,S} {5,S}
8   Cs u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "s2_5_6_ane",
    group = 
"""
1 * Cs u0 {3,S} {7,S} {8,S}
2   Cs u0 {5,S} {7,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {8,S} {9,S}
7   Cs u0 {1,S} {2,S} {9,S}
8   Cs u0 {1,S} {6,S}
9   Cs u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "s2_5_6_ene_0",
    group = 
"""
1 * Cs u0 {4,S} {9,S}
2   Cs u0 {3,S} {5,S} {7,S}
3   Cs u0 {2,S} {6,S}
4   Cd u0 {1,S} {7,D}
5   Cs u0 {2,S} {9,S}
6   Cs u0 {3,S} {8,S}
7   Cd u0 {2,S} {4,D} {8,S}
8   Cs u0 {6,S} {7,S}
9   Cs u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "s2_5_6_ene_1",
    group = 
"""
1 * Cd u0 {2,D} {4,S}
2   Cd u0 {1,D} {9,S}
3   Cs u0 {5,S} {7,S}
4   Cs u0 {1,S} {8,S}
5   Cs u0 {3,S} {6,S}
6   Cs u0 {5,S} {8,S} {9,S}
7   Cs u0 {3,S} {9,S}
8   Cs u0 {4,S} {6,S}
9   Cs u0 {2,S} {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "s2_5_6_ene_m",
    group = 
"""
1 * Cs u0 {6,S} {7,S}
2   Cd u0 {3,D} {7,S} {9,S}
3   Cd u0 {2,D} {4,S} {6,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {4,S} {8,S}
6   Cs u0 {1,S} {3,S}
7   Cs u0 {1,S} {2,S}
8   Cs u0 {5,S} {9,S}
9   Cs u0 {2,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "s2_5_6_ene_2",
    group = 
"""
1 * Cs u0 {2,S} {7,S} {8,S}
2   Cs u0 {1,S} {4,S} {6,S}
3   Cd u0 {6,S} {9,D}
4   Cs u0 {2,S} {5,S}
5   Cs u0 {4,S} {7,S}
6   Cs u0 {2,S} {3,S}
7   Cs u0 {1,S} {5,S}
8   Cs u0 {1,S} {9,S}
9   Cd u0 {3,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "s2_5_6_ene_5",
    group = 
"""
1 * Cd u0 {3,D} {9,S}
2   Cs u0 {5,S} {7,S}
3   Cd u0 {1,D} {7,S} {8,S}
4   Cs u0 {5,S} {8,S}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {8,S} {9,S}
7   Cs u0 {2,S} {3,S}
8   Cs u0 {3,S} {4,S} {6,S}
9   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "s2_5_6_ene_6",
    group = 
"""
1 * Cs u0 {3,S} {4,S}
2   Cs u0 {4,S} {6,S} {8,S}
3   Cs u0 {1,S} {5,S}
4   Cs u0 {1,S} {2,S} {7,S}
5   Cs u0 {3,S} {8,S}
6   Cs u0 {2,S} {9,S}
7   Cd u0 {4,S} {9,D}
8   Cs u0 {2,S} {5,S}
9   Cd u0 {6,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "s2_5_6_diene_m_1",
    group = 
"""
1 * Cs u0 {4,S} {7,S}
2   Cd u0 {5,S} {6,D}
3   Cd u0 {4,S} {5,D} {9,S}
4   Cs u0 {1,S} {3,S}
5   Cd u0 {2,S} {3,D} {7,S}
6   Cd u0 {2,D} {8,S}
7   Cs u0 {1,S} {5,S}
8   Cs u0 {6,S} {9,S}
9   Cs u0 {3,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "s2_5_6_diene_m_2",
    group = 
"""
1 * Cd u0 {3,S} {7,S} {9,D}
2   Cd u0 {5,S} {8,D}
3   Cs u0 {1,S} {8,S}
4   Cs u0 {6,S} {7,S}
5   Cs u0 {2,S} {9,S}
6   Cs u0 {4,S} {9,S}
7   Cs u0 {1,S} {4,S}
8   Cd u0 {2,D} {3,S}
9   Cd u0 {1,D} {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "s2_5_6_diene_m_7",
    group = 
"""
1 * Cs u0 {2,S} {4,S}
2   Cd u0 {1,S} {6,S} {8,D}
3   Cd u0 {5,S} {6,D}
4   Cs u0 {1,S} {9,S}
5   Cs u0 {3,S} {8,S}
6   Cd u0 {2,S} {3,D}
7   Cs u0 {8,S} {9,S}
8   Cd u0 {2,D} {5,S} {7,S}
9   Cs u0 {4,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "s2_5_6_diene_0_2",
    group = 
"""
1 * Cs u0 {2,S} {8,S}
2   Cs u0 {1,S} {6,S}
3   Cd u0 {6,S} {8,S} {9,D}
4   Cd u0 {5,D} {9,S}
5   Cd u0 {4,D} {7,S}
6   Cs u0 {2,S} {3,S}
7   Cs u0 {5,S} {8,S}
8   Cs u0 {1,S} {3,S} {7,S}
9   Cd u0 {3,D} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "s2_5_6_diene_0_3",
    group = 
"""
1 * Cd u0 {2,D} {4,S}
2   Cd u0 {1,D} {5,S}
3   Cs u0 {7,S} {9,S}
4   Cs u0 {1,S} {8,S} {9,S}
5   Cs u0 {2,S} {6,S}
6   Cd u0 {5,S} {8,D}
7   Cs u0 {3,S} {8,S}
8   Cd u0 {4,S} {6,D} {7,S}
9   Cs u0 {3,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "s2_5_6_diene_0_4",
    group = 
"""
1 * Cd u0 {4,D} {9,S}
2   Cd u0 {4,S} {5,D} {6,S}
3   Cs u0 {5,S} {9,S}
4   Cd u0 {1,D} {2,S} {7,S}
5   Cd u0 {2,D} {3,S}
6   Cs u0 {2,S} {8,S}
7   Cs u0 {4,S} {8,S}
8   Cs u0 {6,S} {7,S}
9   Cs u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "s2_5_6_diene_0_5",
    group = 
"""
1 * Cs u0 {4,S} {5,S}
2   Cs u0 {8,S} {9,S}
3   Cd u0 {6,S} {7,S} {8,D}
4   Cs u0 {1,S} {7,S}
5   Cd u0 {1,S} {6,D}
6   Cd u0 {3,S} {5,D} {9,S}
7   Cs u0 {3,S} {4,S}
8   Cd u0 {2,S} {3,D}
9   Cs u0 {2,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "s2_5_6_diene_0_6",
    group = 
"""
1 * Cs u0 {4,S} {8,S}
2   Cd u0 {8,S} {9,D}
3   Cd u0 {5,S} {6,D}
4   Cs u0 {1,S} {7,S}
5   Cs u0 {3,S} {9,S}
6   Cd u0 {3,D} {7,S}
7   Cs u0 {4,S} {6,S} {9,S}
8   Cs u0 {1,S} {2,S}
9   Cd u0 {2,D} {5,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "s2_5_6_diene_0_7",
    group = 
"""
1 * Cs u0 {4,S} {5,S}
2   Cd u0 {4,D} {8,S}
3   Cs u0 {6,S} {7,S}
4   Cd u0 {1,S} {2,D}
5   Cs u0 {1,S} {8,S} {9,S}
6   Cd u0 {3,S} {8,D}
7   Cs u0 {3,S} {9,S}
8   Cd u0 {2,S} {5,S} {6,D}
9   Cs u0 {5,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "s2_5_6_diene_1_3",
    group = 
"""
1 * Cd u0 {7,D} {8,S}
2   Cs u0 {3,S} {8,S}
3   Cs u0 {2,S} {9,S}
4   Cd u0 {5,S} {6,D}
5   Cs u0 {4,S} {8,S} {9,S}
6   Cd u0 {4,D} {7,S}
7   Cd u0 {1,D} {6,S}
8   Cs u0 {1,S} {2,S} {5,S}
9   Cs u0 {3,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "s2_5_6_diene_1_5",
    group = 
"""
1 * Cd u0 {8,S} {9,D}
2   Cs u0 {3,S} {7,S}
3   Cd u0 {2,S} {5,D}
4   Cs u0 {5,S} {6,S} {9,S}
5   Cd u0 {3,D} {4,S}
6   Cs u0 {4,S} {8,S}
7   Cs u0 {2,S} {9,S}
8   Cs u0 {1,S} {6,S}
9   Cd u0 {1,D} {4,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "s2_5_6_diene_1_6",
    group = 
"""
1 * Cs u0 {4,S} {9,S}
2   Cd u0 {6,D} {8,S}
3   Cs u0 {5,S} {7,S} {9,S}
4   Cd u0 {1,S} {5,D}
5   Cd u0 {3,S} {4,D}
6   Cd u0 {2,D} {9,S}
7   Cs u0 {3,S} {8,S}
8   Cs u0 {2,S} {7,S}
9   Cs u0 {1,S} {3,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "s2_5_6_diene_1_7",
    group = 
"""
1 * Cs u0 {3,S} {7,S}
2   Cd u0 {8,D} {9,S}
3   Cs u0 {1,S} {6,S}
4   Cd u0 {5,S} {6,D}
5   Cs u0 {4,S} {7,S} {8,S}
6   Cd u0 {3,S} {4,D}
7   Cs u0 {1,S} {5,S} {9,S}
8   Cd u0 {2,D} {5,S}
9   Cs u0 {2,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "s2_5_6_diene_2_5",
    group = 
"""
1 * Cd u0 {5,D} {7,S}
2   Cs u0 {6,S} {8,S}
3   Cs u0 {7,S} {8,S} {9,S}
4   Cs u0 {5,S} {9,S}
5   Cd u0 {1,D} {4,S}
6   Cd u0 {2,S} {9,D}
7   Cs u0 {1,S} {3,S}
8   Cs u0 {2,S} {3,S}
9   Cd u0 {3,S} {4,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "s2_5_6_diene_2_6",
    group = 
"""
1 * Cs u0 {6,S} {8,S}
2   Cd u0 {3,S} {5,D}
3   Cs u0 {2,S} {7,S}
4   Cs u0 {7,S} {9,S}
5   Cd u0 {2,D} {8,S}
6   Cd u0 {1,S} {9,D}
7   Cs u0 {3,S} {4,S} {8,S}
8   Cs u0 {1,S} {5,S} {7,S}
9   Cd u0 {4,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "s2_5_6_diene_5_7",
    group = 
"""
1 * Cs u0 {3,S} {8,S}
2   Cd u0 {4,D} {9,S}
3   Cs u0 {1,S} {6,S}
4   Cd u0 {2,D} {5,S}
5   Cs u0 {4,S} {6,S} {7,S}
6   Cs u0 {3,S} {5,S}
7   Cd u0 {5,S} {8,S} {9,D}
8   Cs u0 {1,S} {7,S}
9   Cd u0 {2,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "s2_5_6_diene_5_8",
    group = 
"""
1 * Cs u0 {8,S} {9,S}
2   Cs u0 {3,S} {4,S}
3   Cd u0 {2,S} {5,D}
4   Cd u0 {2,S} {6,D}
5   Cd u0 {3,D} {6,S} {7,S}
6   Cd u0 {4,D} {5,S} {9,S}
7   Cs u0 {5,S} {8,S}
8   Cs u0 {1,S} {7,S}
9   Cs u0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "s2_6_6_ane",
    group = 
"""
1  * Cs u0 {5,S} {6,S}
2    Cs u0 {7,S} {9,S}
3    Cs u0 {4,S} {6,S}
4    Cs u0 {3,S} {8,S} {10,S}
5    Cs u0 {1,S} {8,S}
6    Cs u0 {1,S} {3,S}
7    Cs u0 {2,S} {8,S}
8    Cs u0 {4,S} {5,S} {7,S}
9    Cs u0 {2,S} {10,S}
10   Cs u0 {4,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "s2_6_6_ene_0",
    group = 
"""
1  * Cs u0 {2,S} {5,S}
2    Cs u0 {1,S} {6,S}
3    Cd u0 {6,S} {10,D}
4    Cs u0 {5,S} {9,S}
5    Cs u0 {1,S} {4,S} {10,S}
6    Cs u0 {2,S} {3,S}
7    Cs u0 {8,S} {9,S}
8    Cs u0 {7,S} {10,S}
9    Cs u0 {4,S} {7,S}
10   Cd u0 {3,D} {5,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "s2_6_6_ene_1",
    group = 
"""
1  * Cd u0 {4,S} {9,D}
2    Cs u0 {3,S} {10,S}
3    Cs u0 {2,S} {5,S}
4    Cs u0 {1,S} {5,S} {6,S}
5    Cs u0 {3,S} {4,S} {8,S}
6    Cs u0 {4,S} {10,S}
7    Cs u0 {8,S} {9,S}
8    Cs u0 {5,S} {7,S}
9    Cd u0 {1,D} {7,S}
10   Cs u0 {2,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "s2_6_6_ene_2",
    group = 
"""
1  * Cs u0 {2,S} {6,S}
2    Cs u0 {1,S} {8,S}
3    Cd u0 {9,D} {10,S}
4    Cs u0 {5,S} {9,S}
5    Cs u0 {4,S} {6,S} {7,S}
6    Cs u0 {1,S} {5,S}
7    Cs u0 {5,S} {8,S} {10,S}
8    Cs u0 {2,S} {7,S}
9    Cd u0 {3,D} {4,S}
10   Cs u0 {3,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "s2_6_6_ene_m",
    group = 
"""
1  * Cs u0 {2,S} {7,S}
2    Cs u0 {1,S} {6,S}
3    Cd u0 {6,D} {8,S} {10,S}
4    Cs u0 {5,S} {6,S}
5    Cs u0 {4,S} {9,S}
6    Cd u0 {2,S} {3,D} {4,S}
7    Cs u0 {1,S} {10,S}
8    Cs u0 {3,S} {9,S}
9    Cs u0 {5,S} {8,S}
10   Cs u0 {3,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "s2_6_6_diene_m_1",
    group = 
"""
1  * Cd u0 {2,S} {8,D}
2    Cs u0 {1,S} {7,S}
3    Cs u0 {4,S} {6,S}
4    Cs u0 {3,S} {10,S}
5    Cd u0 {7,S} {9,D} {10,S}
6    Cs u0 {3,S} {9,S}
7    Cs u0 {2,S} {5,S}
8    Cd u0 {1,D} {9,S}
9    Cd u0 {5,D} {6,S} {8,S}
10   Cs u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "s2_6_6_diene_m_2",
    group = 
"""
1  * Cs u0 {3,S} {7,S}
2    Cd u0 {3,D} {6,S} {9,S}
3    Cd u0 {1,S} {2,D} {5,S}
4    Cs u0 {9,S} {10,S}
5    Cs u0 {3,S} {10,S}
6    Cs u0 {2,S} {8,S}
7    Cd u0 {1,S} {8,D}
8    Cd u0 {6,S} {7,D}
9    Cs u0 {2,S} {4,S}
10   Cs u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    label = "s2_6_6_diene_0_2",
    group = 
"""
1  * Cd u0 {3,D} {8,S}
2    Cs u0 {3,S} {6,S}
3    Cd u0 {1,D} {2,S}
4    Cs u0 {9,S} {10,S}
5    Cs u0 {6,S} {7,S}
6    Cs u0 {2,S} {5,S} {9,S}
7    Cs u0 {5,S} {10,S}
8    Cd u0 {1,S} {9,D}
9    Cd u0 {4,S} {6,S} {8,D}
10   Cs u0 {4,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "s2_6_6_diene_0_3",
    group = 
"""
1    Cd u0 {3,S} {5,S} {10,D}
2    Cs u0 {5,S} {9,S}
3    Cs u0 {1,S} {8,S}
4  * Cd u0 {6,D} {7,S}
5    Cs u0 {1,S} {2,S} {6,S}
6    Cd u0 {4,D} {5,S}
7    Cs u0 {4,S} {10,S}
8    Cs u0 {3,S} {9,S}
9    Cs u0 {2,S} {8,S}
10   Cd u0 {1,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    label = "s2_6_6_diene_0_4",
    group = 
"""
1  * Cd u0 {3,S} {5,S} {8,D}
2    Cs u0 {4,S} {8,S}
3    Cs u0 {1,S} {10,S}
4    Cs u0 {2,S} {6,S}
5    Cd u0 {1,S} {6,D} {9,S}
6    Cd u0 {4,S} {5,D}
7    Cs u0 {9,S} {10,S}
8    Cd u0 {1,D} {2,S}
9    Cs u0 {5,S} {7,S}
10   Cs u0 {3,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "s2_6_6_diene_0_5",
    group = 
"""
1  * Cs u0 {4,S} {7,S}
2    Cs u0 {3,S} {7,S}
3    Cd u0 {2,S} {6,D} {10,S}
4    Cd u0 {1,S} {10,D}
5    Cs u0 {8,S} {9,S}
6    Cd u0 {3,D} {8,S}
7    Cs u0 {1,S} {2,S}
8    Cs u0 {5,S} {6,S}
9    Cs u0 {5,S} {10,S}
10   Cd u0 {3,S} {4,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    label = "s2_6_6_diene_0_6",
    group = 
"""
1  * Cs u0 {8,S} {9,S}
2    Cd u0 {7,D} {9,S}
3    Cs u0 {8,S} {10,S}
4    Cd u0 {5,S} {9,S} {10,D}
5    Cs u0 {4,S} {6,S}
6    Cs u0 {5,S} {7,S}
7    Cd u0 {2,D} {6,S}
8    Cs u0 {1,S} {3,S}
9    Cs u0 {1,S} {2,S} {4,S}
10   Cd u0 {3,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    label = "s2_6_6_diene_0_7",
    group = 
"""
1  * Cs u0 {5,S} {8,S}
2    Cd u0 {3,S} {8,S} {10,D}
3    Cs u0 {2,S} {6,S}
4    Cs u0 {9,S} {10,S}
5    Cd u0 {1,S} {6,D}
6    Cd u0 {3,S} {5,D}
7    Cs u0 {8,S} {9,S}
8    Cs u0 {1,S} {2,S} {7,S}
9    Cs u0 {4,S} {7,S}
10   Cd u0 {2,D} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
    label = "s2_6_6_diene_0_8",
    group = 
"""
1  * Cs u0 {2,S} {9,S}
2    Cs u0 {1,S} {7,S}
3    Cd u0 {5,S} {6,S} {9,D}
4    Cs u0 {6,S} {8,S}
5    Cd u0 {3,S} {10,D}
6    Cs u0 {3,S} {4,S} {7,S}
7    Cs u0 {2,S} {6,S}
8    Cs u0 {4,S} {10,S}
9    Cd u0 {1,S} {3,D}
10   Cd u0 {5,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
    label = "s2_6_6_diene_1_3",
    group = 
"""
1  * Cd u0 {2,D} {6,S}
2    Cd u0 {1,D} {10,S}
3    Cs u0 {4,S} {8,S}
4    Cs u0 {3,S} {10,S}
5    Cs u0 {7,S} {9,S} {10,S}
6    Cd u0 {1,S} {9,D}
7    Cs u0 {5,S} {8,S}
8    Cs u0 {3,S} {7,S}
9    Cd u0 {5,S} {6,D}
10   Cs u0 {2,S} {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 128,
    label = "s2_6_6_diene_1_6",
    group = 
"""
1  * Cs u0 {4,S} {10,S}
2    Cs u0 {4,S} {8,S} {9,S}
3    Cd u0 {9,D} {10,S}
4    Cs u0 {1,S} {2,S} {7,S}
5    Cd u0 {6,S} {7,D}
6    Cs u0 {5,S} {8,S}
7    Cd u0 {4,S} {5,D}
8    Cs u0 {2,S} {6,S}
9    Cd u0 {2,S} {3,D}
10   Cs u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
    label = "s2_6_6_diene_1_7",
    group = 
"""
1  * Cs u0 {3,S} {9,S}
2    Cs u0 {3,S} {4,S} {10,S}
3    Cs u0 {1,S} {2,S} {6,S}
4    Cs u0 {2,S} {5,S}
5    Cd u0 {4,S} {9,D}
6    Cd u0 {3,S} {7,D}
7    Cd u0 {6,D} {8,S}
8    Cs u0 {7,S} {10,S}
9    Cd u0 {1,S} {5,D}
10   Cs u0 {2,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 130,
    label = "s2_6_6_diene_1_8",
    group = 
"""
1  * Cs u0 {4,S} {5,S} {6,S}
2    Cs u0 {3,S} {7,S}
3    Cs u0 {2,S} {4,S}
4    Cs u0 {1,S} {3,S} {9,S}
5    Cd u0 {1,S} {10,D}
6    Cd u0 {1,S} {7,D}
7    Cd u0 {2,S} {6,D}
8    Cs u0 {9,S} {10,S}
9    Cs u0 {4,S} {8,S}
10   Cd u0 {5,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 131,
    label = "s2_6_6_diene_2_7",
    group = 
"""
1  * Cd u0 {4,D} {8,S}
2    Cs u0 {3,S} {6,S}
3    Cd u0 {2,S} {10,D}
4    Cd u0 {1,D} {7,S}
5    Cs u0 {6,S} {7,S} {9,S}
6    Cs u0 {2,S} {5,S} {8,S}
7    Cs u0 {4,S} {5,S}
8    Cs u0 {1,S} {6,S}
9    Cs u0 {5,S} {10,S}
10   Cd u0 {3,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 132,
    label = "s3_4_4_ane",
    group = 
"""
1 * Cs u0 {2,S} {4,S}
2   Cs u0 {1,S} {3,S} {5,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {1,S} {3,S} {5,S}
5   Cs u0 {2,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 133,
    label = "s3_4_4_ene_0",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   Cs u0 {1,S} {5,S}
3   Cs u0 {1,S} {5,S}
4   Cd u0 {1,D} {5,S}
5   Cs u0 {2,S} {3,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 134,
    label = "s3_4_4_diene_0_2",
    group = 
"""
1 * Cd u0 {2,S} {4,D}
2   Cd u0 {1,S} {3,S} {5,D}
3   Cs u0 {2,S} {4,S}
4   Cd u0 {1,D} {3,S} {5,S}
5   Cd u0 {2,D} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "s3_4_5_ane",
    group = 
"""
1 * Cs u0 {4,S} {5,S}
2   Cs u0 {4,S} {5,S}
3   Cs u0 {5,S} {6,S}
4   Cs u0 {1,S} {2,S} {6,S}
5   Cs u0 {1,S} {2,S} {3,S}
6   Cs u0 {3,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "s3_4_5_ene_0",
    group = 
"""
1 * Cd u0 {2,S} {4,D} {5,S}
2   Cs u0 {1,S} {6,S}
3   Cs u0 {4,S} {6,S}
4   Cd u0 {1,D} {3,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {2,S} {3,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "s3_4_5_ene_1",
    group = 
"""
1 * Cd u0 {2,S} {4,D}
2   Cs u0 {1,S} {5,S} {6,S}
3   Cs u0 {4,S} {5,S} {6,S}
4   Cd u0 {1,D} {3,S}
5   Cs u0 {2,S} {3,S}
6   Cs u0 {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "s3_4_5_ene_3",
    group = 
"""
1 * Cs u0 {2,S} {4,S}
2   Cs u0 {1,S} {3,S}
3   Cd u0 {2,S} {5,D} {6,S}
4   Cs u0 {1,S} {5,S} {6,S}
5   Cd u0 {3,D} {4,S}
6   Cs u0 {3,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "s3_4_5_diene_0_2",
    group = 
"""
1 * Cd u0 {4,S} {5,D}
2   Cs u0 {3,S} {5,S}
3   Cd u0 {2,S} {4,D} {6,S}
4   Cd u0 {1,S} {3,D}
5   Cd u0 {1,D} {2,S} {6,S}
6   Cs u0 {3,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    label = "s3_4_5_diene_0_3",
    group = 
"""
1 * Cs u0 {2,S} {6,S}
2   Cd u0 {1,S} {3,D}
3   Cd u0 {2,D} {4,S} {5,S}
4   Cs u0 {3,S} {6,S}
5   Cd u0 {3,S} {6,D}
6   Cd u0 {1,S} {4,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "s3_4_5_diene_1_3",
    group = 
"""
1 * Cd u0 {2,S} {5,D}
2   Cs u0 {1,S} {4,S} {6,S}
3   Cd u0 {4,D} {5,S} {6,S}
4   Cd u0 {2,S} {3,D}
5   Cd u0 {1,D} {3,S}
6   Cs u0 {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 142,
    label = "s3_4_5_diene_3_4",
    group = 
"""
1 * Cd u0 {2,D} {4,S}
2   Cd u0 {1,D} {3,S} {5,S}
3   Cd u0 {2,S} {4,D}
4   Cd u0 {1,S} {3,D} {6,S}
5   Cs u0 {2,S} {6,S}
6   Cs u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 143,
    label = "s3_4_6_ane",
    group = 
"""
1 * Cs u0 {4,S} {6,S}
2   Cs u0 {3,S} {7,S}
3   Cs u0 {2,S} {6,S}
4   Cs u0 {1,S} {5,S} {7,S}
5   Cs u0 {4,S} {6,S}
6   Cs u0 {1,S} {3,S} {5,S}
7   Cs u0 {2,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 144,
    label = "s3_4_6_ene_0",
    group = 
"""
1 * Cd u0 {3,S} {5,D} {6,S}
2   Cs u0 {4,S} {7,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S} {6,S}
5   Cd u0 {1,D} {7,S}
6   Cs u0 {1,S} {4,S}
7   Cs u0 {2,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 145,
    label = "s3_4_6_ene_1",
    group = 
"""
1 * Cs u0 {5,S} {7,S}
2   Cs u0 {4,S} {7,S}
3   Cs u0 {5,S} {7,S}
4   Cd u0 {2,S} {6,D}
5   Cs u0 {1,S} {3,S} {6,S}
6   Cd u0 {4,D} {5,S}
7   Cs u0 {1,S} {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 146,
    label = "s3_4_6_ene_4",
    group = 
"""
1 * Cs u0 {2,S} {3,S}
2   Cs u0 {1,S} {5,S}
3   Cs u0 {1,S} {4,S} {6,S}
4   Cd u0 {3,S} {7,D}
5   Cs u0 {2,S} {7,S}
6   Cs u0 {3,S} {7,S}
7   Cd u0 {4,D} {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 147,
    label = "s3_4_6_diene_0_2",
    group = 
"""
1 * Cs u0 {4,S} {7,S}
2   Cd u0 {3,S} {6,D}
3   Cd u0 {2,S} {7,D}
4   Cs u0 {1,S} {5,S} {6,S}
5   Cs u0 {4,S} {7,S}
6   Cd u0 {2,D} {4,S}
7   Cd u0 {1,S} {3,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "s3_4_6_diene_0_3",
    group = 
"""
1 * Cs u0 {2,S} {6,S}
2   Cd u0 {1,S} {3,S} {4,D}
3   Cs u0 {2,S} {6,S}
4   Cd u0 {2,D} {7,S}
5   Cd u0 {6,D} {7,S}
6   Cd u0 {1,S} {3,S} {5,D}
7   Cs u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 149,
    label = "s3_4_6_diene_0_4",
    group = 
"""
1 * Cs u0 {3,S} {5,S}
2   Cd u0 {3,D} {5,S}
3   Cd u0 {1,S} {2,D} {4,S}
4   Cs u0 {3,S} {6,S}
5   Cd u0 {1,S} {2,S} {7,D}
6   Cs u0 {4,S} {7,S}
7   Cd u0 {5,D} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 150,
    label = "s3_4_6_diene_1_4",
    group = 
"""
1 * Cd u0 {5,S} {7,D}
2   Cs u0 {6,S} {7,S}
3   Cd u0 {5,S} {6,D}
4   Cs u0 {5,S} {6,S}
5   Cs u0 {1,S} {3,S} {4,S}
6   Cd u0 {2,S} {3,D} {4,S}
7   Cd u0 {1,D} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 151,
    label = "s3_4_6_diene_1_5",
    group = 
"""
1 * Cd u0 {3,S} {5,D}
2   Cs u0 {3,S} {4,S} {7,S}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {2,S} {6,D}
5   Cd u0 {1,D} {6,S}
6   Cd u0 {4,D} {5,S} {7,S}
7   Cs u0 {2,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 152,
    label = "s3_5_5_ane",
    group = 
"""
1 * Cs u0 {3,S} {5,S}
2   Cs u0 {4,S} {5,S}
3   Cs u0 {1,S} {7,S}
4   Cs u0 {2,S} {7,S}
5   Cs u0 {1,S} {2,S} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cs u0 {3,S} {4,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (16.14,'kcal/mol'),
        S298 = (53.47,'cal/(mol*K)'),
    ),
    shortDesc = u"""norbornane""",
    longDesc = 
u"""

""",
)

entry(
    index = 153,
    label = "s3_5_5_ene_1",
    group = 
"""
1 * Cs u0 {3,S} {7,S}
2   Cs u0 {5,S} {7,S}
3   Cs u0 {1,S} {5,S}
4   Cd u0 {5,S} {6,D}
5   Cs u0 {2,S} {3,S} {4,S}
6   Cd u0 {4,D} {7,S}
7   Cs u0 {1,S} {2,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.29,-7.302,-6.501,-5.499,-4.58,-3.778,-2.608],'cal/(mol*K)'),
        H298 = (17.8,'kcal/mol'),
        S298 = (53.75,'cal/(mol*K)'),
    ),
    shortDesc = u"""norbornene""",
    longDesc = 
u"""

""",
)

entry(
    index = 154,
    label = "s3_5_5_diene_1_4",
    group = 
"""
1 * Cd u0 {4,S} {6,D}
2   Cs u0 {3,S} {6,S} {7,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {1,S} {3,S} {5,S}
5   Cd u0 {4,S} {7,D}
6   Cd u0 {1,D} {2,S}
7   Cd u0 {2,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 155,
    label = "s3_5_6_ane",
    group = 
"""
1 * Cs u0 {6,S} {8,S}
2   Cs u0 {5,S} {6,S} {7,S}
3   Cs u0 {4,S} {7,S} {8,S}
4   Cs u0 {3,S} {5,S}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {1,S} {2,S}
7   Cs u0 {2,S} {3,S}
8   Cs u0 {1,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.2,-9.9,-8.4,-7.1,-5.2,-3.8,-1.7],'cal/(mol*K)'),
        H298 = (8.5,'kcal/mol'),
        S298 = (48.66,'cal/(mol*K)'),
    ),
    shortDesc = u"""bicyclo[3.2.1]octane""",
    longDesc = 
u"""

""",
)

entry(
    index = 156,
    label = "s3_5_6_ene_1",
    group = 
"""
1 * Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {5,S} {7,S}
3   Cs u0 {1,S} {8,S}
4   Cd u0 {1,S} {5,D}
5   Cd u0 {2,S} {4,D}
6   Cs u0 {1,S} {7,S}
7   Cs u0 {2,S} {6,S} {8,S}
8   Cs u0 {3,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.3,-8.3,-7.2,-6.1,-4.8,-3.6,-2],'cal/(mol*K)'),
        H298 = (8.5,'kcal/mol'),
        S298 = (48.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""bicyclo[3.2.1]octene""",
    longDesc = 
u"""

""",
)

entry(
    index = 157,
    label = "s3_5_6_ene_5",
    group = 
"""
1 * Cs u0 {3,S} {8,S}
2   Cs u0 {4,S} {6,S} {7,S}
3   Cs u0 {1,S} {5,S} {6,S}
4   Cd u0 {2,S} {5,D}
5   Cd u0 {3,S} {4,D}
6   Cs u0 {2,S} {3,S}
7   Cs u0 {2,S} {8,S}
8   Cs u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 158,
    label = "s3_5_6_diene_1_5",
    group = 
"""
1 * Cs u0 {2,S} {4,S} {5,S}
2   Cd u0 {1,S} {7,D}
3   Cs u0 {7,S} {8,S}
4   Cs u0 {1,S} {8,S}
5   Cd u0 {1,S} {6,D}
6   Cd u0 {5,D} {8,S}
7   Cd u0 {2,D} {3,S}
8   Cs u0 {3,S} {4,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 159,
    label = "s3_6_6_ane",
    group = 
"""
1 * Cs u0 {5,S} {7,S}
2   Cs u0 {4,S} {8,S} {9,S}
3   Cs u0 {6,S} {8,S}
4   Cs u0 {2,S} {7,S}
5   Cs u0 {1,S} {9,S}
6   Cs u0 {3,S} {7,S}
7   Cs u0 {1,S} {4,S} {6,S}
8   Cs u0 {2,S} {3,S}
9   Cs u0 {2,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 160,
    label = "s3_6_6_ene_0",
    group = 
"""
1 * Cs u0 {3,S} {8,S}
2   Cs u0 {7,S} {8,S}
3   Cs u0 {1,S} {4,S} {6,S}
4   Cs u0 {3,S} {7,S}
5   Cd u0 {7,D} {9,S}
6   Cs u0 {3,S} {9,S}
7   Cd u0 {2,S} {4,S} {5,D}
8   Cs u0 {1,S} {2,S}
9   Cs u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 161,
    label = "s3_6_6_ene_1",
    group = 
"""
1 * Cs u0 {3,S} {4,S}
2   Cd u0 {6,S} {7,D}
3   Cs u0 {1,S} {5,S} {7,S}
4   Cs u0 {1,S} {6,S} {9,S}
5   Cs u0 {3,S} {8,S}
6   Cs u0 {2,S} {4,S}
7   Cd u0 {2,D} {3,S}
8   Cs u0 {5,S} {9,S}
9   Cs u0 {4,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 162,
    label = "s3_6_6_ene_4",
    group = 
"""
1 * Cd u0 {3,D} {4,S} {8,S}
2   Cs u0 {3,S} {5,S} {9,S}
3   Cd u0 {1,D} {2,S}
4   Cs u0 {1,S} {6,S}
5   Cs u0 {2,S} {7,S}
6   Cs u0 {4,S} {9,S}
7   Cs u0 {5,S} {8,S}
8   Cs u0 {1,S} {7,S}
9   Cs u0 {2,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 163,
    label = "s3_6_6_diene_0_m",
    group = 
"""
1 * Cd u0 {3,D} {8,S}
2   Cs u0 {3,S} {6,S}
3   Cd u0 {1,D} {2,S} {9,S}
4   Cs u0 {5,S} {8,S}
5   Cd u0 {4,S} {7,S} {9,D}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {5,S} {6,S}
8   Cs u0 {1,S} {4,S}
9   Cd u0 {3,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 164,
    label = "s3_6_6_diene_0_2",
    group = 
"""
1 * Cs u0 {4,S} {6,S}
2   Cd u0 {4,D} {5,S}
3   Cs u0 {7,S} {8,S} {9,S}
4   Cd u0 {1,S} {2,D} {8,S}
5   Cd u0 {2,S} {7,D}
6   Cs u0 {1,S} {9,S}
7   Cd u0 {3,S} {5,D}
8   Cs u0 {3,S} {4,S}
9   Cs u0 {3,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 165,
    label = "s3_6_6_diene_0_3",
    group = 
"""
1 * Cs u0 {4,S} {6,S}
2   Cd u0 {3,S} {7,D}
3   Cs u0 {2,S} {8,S}
4   Cs u0 {1,S} {7,S}
5   Cd u0 {6,S} {8,D} {9,S}
6   Cs u0 {1,S} {5,S}
7   Cd u0 {2,D} {4,S} {9,S}
8   Cd u0 {3,S} {5,D}
9   Cs u0 {5,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 166,
    label = "s3_6_6_diene_0_4",
    group = 
"""
1 * Cs u0 {7,S} {9,S}
2   Cs u0 {5,S} {6,S}
3   Cd u0 {6,S} {9,D}
4   Cd u0 {5,D} {7,S}
5   Cd u0 {2,S} {4,D} {8,S}
6   Cs u0 {2,S} {3,S}
7   Cs u0 {1,S} {4,S}
8   Cs u0 {5,S} {9,S}
9   Cd u0 {1,S} {3,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 167,
    label = "s3_6_6_diene_0_5",
    group = 
"""
1 * Cs u0 {2,S} {5,S} {7,S}
2   Cs u0 {1,S} {9,S}
3   Cd u0 {6,D} {9,S}
4   Cs u0 {6,S} {8,S}
5   Cs u0 {1,S} {6,S}
6   Cd u0 {3,D} {4,S} {5,S}
7   Cd u0 {1,S} {8,D}
8   Cd u0 {4,S} {7,D}
9   Cs u0 {2,S} {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 168,
    label = "s3_6_6_diene_0_6",
    group = 
"""
1 * Cs u0 {2,S} {8,S}
2   Cd u0 {1,S} {7,D}
3   Cs u0 {5,S} {7,S}
4   Cd u0 {6,D} {7,S}
5   Cs u0 {3,S} {8,S} {9,S}
6   Cd u0 {4,D} {9,S}
7   Cd u0 {2,D} {3,S} {4,S}
8   Cs u0 {1,S} {5,S}
9   Cs u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 169,
    label = "s3_6_6_diene_1_m",
    group = 
"""
1 * Cd u0 {4,D} {6,S} {9,S}
2   Cd u0 {7,D} {8,S}
3   Cs u0 {5,S} {6,S}
4   Cd u0 {1,D} {8,S}
5   Cs u0 {3,S} {8,S}
6   Cs u0 {1,S} {3,S}
7   Cd u0 {2,D} {9,S}
8   Cs u0 {2,S} {4,S} {5,S}
9   Cs u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 170,
    label = "s3_6_6_diene_1_5",
    group = 
"""
1 * Cs u0 {5,S} {8,S}
2   Cd u0 {8,D} {9,S}
3   Cd u0 {5,S} {7,D}
4   Cs u0 {5,S} {9,S}
5   Cs u0 {1,S} {3,S} {4,S}
6   Cs u0 {7,S} {9,S}
7   Cd u0 {3,D} {6,S}
8   Cd u0 {1,S} {2,D}
9   Cs u0 {2,S} {4,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 171,
    label = "s3_6_6_diene_1_6",
    group = 
"""
1 * Cs u0 {8,S} {9,S}
2   Cd u0 {5,S} {9,D}
3   Cd u0 {5,S} {7,D}
4   Cs u0 {5,S} {8,S}
5   Cs u0 {2,S} {3,S} {4,S}
6   Cs u0 {7,S} {8,S}
7   Cd u0 {3,D} {6,S}
8   Cs u0 {1,S} {4,S} {6,S}
9   Cd u0 {1,S} {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 172,
    label = "s3_6_6_diene_1_8",
    group = 
"""
1 * Cs u0 {3,S} {4,S}
2   Cd u0 {3,D} {6,S}
3   Cd u0 {1,S} {2,D}
4   Cs u0 {1,S} {5,S} {9,S}
5   Cs u0 {4,S} {8,S}
6   Cd u0 {2,S} {7,S} {9,D}
7   Cs u0 {6,S} {8,S}
8   Cs u0 {5,S} {7,S}
9   Cd u0 {4,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: PolycyclicRing
    L2: s1_3_3
        L3: s1_3_3_ane
        L3: s1_3_3_ene
    L2: s1_3_4
        L3: s1_3_4_ane
        L3: s1_3_4_ene
    L2: s1_3_5
        L3: s1_3_5_ane
        L3: s1_3_5_ene
            L4: s1_3_5_ene_1
            L4: s1_3_5_ene_2
        L3: s1_3_5_diene
            L4: s1_3_5_diene_1_3
    L2: s1_3_6
        L3: s1_3_6_ane
        L3: s1_3_6_ene
            L4: s1_3_6_ene_1
            L4: s1_3_6_ene_2
        L3: s1_3_6_diene
            L4: s1_3_6_diene_1_4
            L4: s1_3_6_diene_1_3
    L2: s1_4_4
        L3: s1_4_4_ane
        L3: s1_4_4_ene
            L4: s1_4_4_ene_1
        L3: s1_4_4_diene
            L4: s1_4_4_diene_1_5
    L2: s1_4_5
        L3: s1_4_5_ane
        L3: s1_4_5_ene
            L4: s1_4_5_ene_1
            L4: s1_4_5_ene_2
            L4: s1_4_5_ene_6
        L3: s1_4_5_diene
            L4: s1_4_5_diene_1_3
            L4: s1_4_5_diene_1_6
            L4: s1_4_5_diene_2_6
    L2: s1_4_6
        L3: s1_4_6_ane
        L3: s1_4_6_ene
            L4: s1_4_6_ene_1
            L4: s1_4_6_ene_2
            L4: s1_4_6_ene_7
        L3: s1_4_6_diene
            L4: s1_4_6_diene_1_3
            L4: s1_4_6_diene_1_4
            L4: s1_4_6_diene_1_7
            L4: s1_4_6_diene_2_7
    L2: s1_5_5
        L3: s1_5_5_ane
        L3: s1_5_5_ene
            L4: s1_5_5_ene_1
            L4: s1_5_5_ene_2
        L3: s1_5_5_diene
            L4: s1_5_5_diene_1_3
            L4: s1_5_5_diene_1_6
            L4: s1_5_5_diene_1_7
            L4: s1_5_5_diene_2_7
    L2: s1_5_6
        L3: s1_5_6_ane
        L3: s1_5_6_ene
            L4: s1_5_6_ene_1
            L4: s1_5_6_ene_2
            L4: s1_5_6_ene_7
            L4: s1_5_6_ene_8
        L3: s1_5_6_diene
            L4: s1_5_6_diene_1_3
            L4: s1_5_6_diene_1_4
            L4: s1_5_6_diene_1_7
            L4: s1_5_6_diene_1_8
            L4: s1_5_6_diene_2_7
            L4: s1_5_6_diene_2_8
            L4: s1_5_6_diene_7_9
    L2: s1_6_6
        L3: s1_6_6_ane
        L3: s1_6_6_ene
            L4: s1_6_6_ene_1
            L4: s1_6_6_ene_2
        L3: s1_6_6_diene
            L4: s1_6_6_diene_1_3
            L4: s1_6_6_diene_1_4
            L4: s1_6_6_diene_1_7
            L4: s1_6_6_diene_1_8
            L4: s1_6_6_diene_2_8
    L2: s2_3_3
        L3: s2_3_3_ane
        L3: s2_3_3_ene
    L2: s2_3_4
        L3: s2_3_4_ane
        L3: s2_3_4_ene
            L4: s2_3_4_ene_1
    L2: s2_3_5
        L3: s2_3_5_ane
        L3: s2_3_5_ene
            L4: s2_3_5_ene_1
    L2: s2_3_6 
        L3: s2_3_6_ane
        L3: s2_3_6_ene
            L4: s2_3_6_ene_1
            L4: s2_3_6_ene_2
        L3: s2_3_6_diene
            L4: s2_3_6_diene_1_3
    L2: s2_4_4
        L3: s2_4_4_ane
        L3: s2_4_4_ene
            L4: s2_4_4_ene_1
    L2: s2_4_5
        L3: s2_4_5_ane
        L3: s2_4_5_ene
            L4: s2_4_5_ene_1
    L2: s2_4_6
        L3: s2_4_6_ane
        L3: s2_4_6_ene
            L4: s2_4_6_ene_1
            L4: s2_4_6_ene_2
    L2: s2_5_5
        L3: s2_5_5_ane
        L3: s2_5_5_ene
            L4: s2_5_5_ene_0
            L4: s2_5_5_ene_1
            L4: s2_5_5_ene_m
        L3: s2_5_5_diene
            L4: s2_5_5_diene_0_2
            L4: s2_5_5_diene_0_3
            L4: s2_5_5_diene_m_2
            L4: s2_5_5_diene_0_4
            L4: s2_5_5_diene_0_5
            L4: s2_5_5_diene_0_6
            L4: s2_5_5_diene_1_5
            L4: s2_5_5_diene_1_6
    L2: s2_5_6
        L3: s2_5_6_ane
        L3: s2_5_6_ene
            L4: s2_5_6_ene_0
            L4: s2_5_6_ene_1
            L4: s2_5_6_ene_m
            L4: s2_5_6_ene_2
            L4: s2_5_6_ene_5
            L4: s2_5_6_ene_6
        L3: s2_5_6_diene
            L4: s2_5_6_diene_m_1
            L4: s2_5_6_diene_m_2
            L4: s2_5_6_diene_m_7
            L4: s2_5_6_diene_0_2
            L4: s2_5_6_diene_0_3
            L4: s2_5_6_diene_0_4
            L4: s2_5_6_diene_0_5
            L4: s2_5_6_diene_0_6
            L4: s2_5_6_diene_0_7
            L4: s2_5_6_diene_1_3
            L4: s2_5_6_diene_1_5
            L4: s2_5_6_diene_1_6
            L4: s2_5_6_diene_1_7
            L4: s2_5_6_diene_2_5
            L4: s2_5_6_diene_2_6
            L4: s2_5_6_diene_5_7
            L4: s2_5_6_diene_5_8
    L2: s2_6_6
        L3: s2_6_6_ane
        L3: s2_6_6_ene
            L4: s2_6_6_ene_0
            L4: s2_6_6_ene_1
            L4: s2_6_6_ene_2
            L4: s2_6_6_ene_m
        L3: s2_6_6_diene
            L4: s2_6_6_diene_m_1
            L4: s2_6_6_diene_m_2
            L4: s2_6_6_diene_0_2
            L4: s2_6_6_diene_0_3
            L4: s2_6_6_diene_0_4
            L4: s2_6_6_diene_0_5
            L4: s2_6_6_diene_0_6
            L4: s2_6_6_diene_0_7
            L4: s2_6_6_diene_0_8
            L4: s2_6_6_diene_1_3
            L4: s2_6_6_diene_1_6
            L4: s2_6_6_diene_1_7
            L4: s2_6_6_diene_1_8
            L4: s2_6_6_diene_2_7
    L2: s3_4_4
        L3: s3_4_4_ane
        L3: s3_4_4_ene
            L4: s3_4_4_ene_0
        L3: s3_4_4_diene
            L4: s3_4_4_diene_0_2
    L2: s3_4_5
        L3: s3_4_5_ane
        L3: s3_4_5_ene
            L4: s3_4_5_ene_0
            L4: s3_4_5_ene_1
            L4: s3_4_5_ene_3
        L3: s3_4_5_diene
            L4: s3_4_5_diene_0_2
            L4: s3_4_5_diene_0_3
            L4: s3_4_5_diene_1_3
            L4: s3_4_5_diene_3_4
    L2: s3_4_6
        L3: s3_4_6_ane
        L3: s3_4_6_ene
            L4: s3_4_6_ene_0
            L4: s3_4_6_ene_1
            L4: s3_4_6_ene_4
        L3: s3_4_6_diene
            L4: s3_4_6_diene_0_2
            L4: s3_4_6_diene_0_3
            L4: s3_4_6_diene_0_4
            L4: s3_4_6_diene_1_4
            L4: s3_4_6_diene_1_5
    L2: s3_5_5
        L3: s3_5_5_ane
        L3: s3_5_5_ene
            L4: s3_5_5_ene_1
        L3: s3_5_5_diene
            L4: s3_5_5_diene_1_4
    L2: s3_5_6
        L3: s3_5_6_ane
        L3: s3_5_6_ene
            L4: s3_5_6_ene_1
            L4: s3_5_6_ene_5
        L3: s3_5_6_diene
            L4: s3_5_6_diene_1_5
    L2: s3_6_6
        L3: s3_6_6_ane
        L3: s3_6_6_ene
            L4: s3_6_6_ene_0
            L4: s3_6_6_ene_1
            L4: s3_6_6_ene_4
        L3: s3_6_6_diene
            L4: s3_6_6_diene_0_m
            L4: s3_6_6_diene_0_2
            L4: s3_6_6_diene_0_3
            L4: s3_6_6_diene_0_4
            L4: s3_6_6_diene_0_5
            L4: s3_6_6_diene_0_6
            L4: s3_6_6_diene_1_m
            L4: s3_6_6_diene_1_5
            L4: s3_6_6_diene_1_6
            L4: s3_6_6_diene_1_8
"""
)

