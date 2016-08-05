#!/usr/bin/env python
# encoding: utf-8

name = "Polycyclic Ring Corrections"
shortDesc = u""
longDesc = u"""

"""
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
Properties of Liquids and Gases, Poling 5th Ed.
""",
)

entry(
    index = 0,
    label = "s1_3_3",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 * C u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "s1_3_3_ane",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2 * C u0 {1,S} {3,S}
3   C u0 {1,S} {2,S}
4   C u0 {1,S} {5,S}
5   C u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.93,-6.5,-6.24,-5.5,-4.4,-4.35,-2.38],'cal/(mol*K)'),
        H298 = (63.59,'kcal/mol'),
        S298 = (67.15,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Properties of Liquids and Gases, Poling 5th Ed. S, Cp from PM7 calculation
""",
)

entry(
    index = 2,
    label = "s1_3_3_ene",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2 * C u0 {1,S} {3,D}
3   C u0 {1,S} {2,D}
4   C u0 {1,S} {5,S}
5   C u0 {1,S} {4,S}
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
    index = 3,
    label = "s1_3_4_ane",
    group = 
"""
1 * C u0 {2,S} {3,S} {4,S} {5,S}
2   C u0 {1,S} {3,S}
3   C u0 {1,S} {2,S}
4   C u0 {1,S} {6,S}
5   C u0 {1,S} {6,S}
6   C u0 {4,S} {5,S}
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
    label = "s1_3_4_ene",
    group = 
"""
1 * C u0 {2,S} {3,S} {4,S} {5,S}
2   C u0 {1,S} {3,S}
3   C u0 {1,S} {2,S}
4   C u0 {1,S} {6,D}
5   C u0 {1,S} {6,S}
6   C u0 {4,D} {5,S}
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
    index = 0,
    label = "s1_3_5",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6 * C u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
7   C u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "s1_3_5_ane",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2   C u0 {1,S} {3,S}
3   C u0 {1,S} {2,S}
4   C u0 {1,S} {6,S}
5   C u0 {1,S} {7,S}
6 * C u0 {4,S} {7,S}
7   C u0 {5,S} {6,S}
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
    index = 6,
    label = "s1_3_5_ene_1",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2   C u0 {1,S} {3,S}
3   C u0 {1,S} {2,S}
4   C u0 {1,S} {7,S}
5   C u0 {1,S} {6,D}
6 * C u0 {5,D} {7,S}
7   C u0 {4,S} {6,S}
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
    label = "s1_3_5_ene_2",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2   C u0 {1,S} {3,S}
3   C u0 {1,S} {2,S}
4   C u0 {1,S} {7,S}
5   C u0 {1,S} {6,S}
6 * C u0 {5,S} {7,D}
7   C u0 {4,S} {6,D}
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
    index = 8,
    label = "s1_3_5_diene_1_3",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2   C u0 {1,S} {3,S}
3   C u0 {1,S} {2,S}
4   C u0 {1,S} {7,D}
5   C u0 {1,S} {6,D}
6 * C u0 {5,D} {7,S}
7   C u0 {4,D} {6,S}
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
    index = 0,
    label = "s1_3_6",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   C u0 {4,[S,D,T,B]} {8,[S,D,T,B]}
7   C u0 {5,[S,D,T,B]} {8,[S,D,T,B]}
8 * C u0 {6,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "s1_3_6_ane",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2   C u0 {1,S} {3,S}
3   C u0 {1,S} {2,S}
4   C u0 {1,S} {6,S}
5   C u0 {1,S} {7,S}
6   C u0 {4,S} {8,S}
7   C u0 {5,S} {8,S}
8 * C u0 {6,S} {7,S}
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
    index = 0,
    label = "s1_3_6_ene",
    group = "OR{s1_3_6_ene_1, s1_3_6_ene_2}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "s1_3_6_ene_1",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2   C u0 {1,S} {3,S}
3   C u0 {1,S} {2,S}
4   C u0 {1,S} {6,S}
5   C u0 {1,S} {7,D}
6   C u0 {4,S} {8,S}
7   C u0 {5,D} {8,S}
8 * C u0 {6,S} {7,S}
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
    label = "s1_3_6_ene_2",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2   C u0 {1,S} {3,S}
3   C u0 {1,S} {2,S}
4   C u0 {1,S} {6,S}
5   C u0 {1,S} {7,S}
6   C u0 {4,S} {8,D}
7   C u0 {5,S} {8,S}
8 * C u0 {6,D} {7,S}
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
    index = 0,
    label = "s1_3_6_diene",
    group = "OR{s1_3_6_diene_1_4, s1_3_6_diene_1_3}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "s1_3_6_diene_1_4",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2   C u0 {1,S} {3,S}
3   C u0 {1,S} {2,S}
4   C u0 {1,S} {7,D}
5   C u0 {1,S} {6,D}
6   C u0 {5,D} {8,S}
7   C u0 {4,D} {8,S}
8 * C u0 {6,S} {7,S}
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
    label = "s1_3_6_diene_1_3",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2   C u0 {1,S} {3,S}
3   C u0 {1,S} {2,S}
4   C u0 {1,S} {7,S}
5   C u0 {1,S} {6,D}
6   C u0 {5,D} {8,S}
7   C u0 {4,S} {8,D}
8 * C u0 {6,S} {7,D}
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
    index = 0,
    label = "s1_4_4",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 * C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6   C u0 {4,[S,D,T,B]} {5,[S,D,T,B]}
7   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "s1_4_4_ane",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2 * C u0 {1,S} {7,S}
3   C u0 {1,S} {7,S}
4   C u0 {1,S} {6,S}
5   C u0 {1,S} {6,S}
6   C u0 {4,S} {5,S}
7   C u0 {2,S} {3,S}
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
    index = 15,
    label = "s1_4_4_ene_1",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2 * C u0 {1,S} {7,S}
3   C u0 {1,S} {6,S}
4   C u0 {1,S} {7,D}
5   C u0 {1,S} {6,S}
6   C u0 {3,S} {5,S}
7   C u0 {2,S} {4,D}
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
    index = 16,
    label = "s1_4_4_diene_1_5",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2 * C u0 {1,S} {7,D}
3   C u0 {1,S} {6,S}
4   C u0 {1,S} {7,S}
5   C u0 {1,S} {6,D}
6   C u0 {3,S} {5,D}
7   C u0 {2,D} {4,S}
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
    index = 0,
    label = "s1_4_5",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 * C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6   C u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
7   C u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
8   C u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "s1_4_5_ane",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2 * C u0 {1,S} {7,S}
3   C u0 {1,S} {6,S}
4   C u0 {1,S} {8,S}
5   C u0 {1,S} {6,S}
6   C u0 {3,S} {5,S}
7   C u0 {2,S} {8,S}
8   C u0 {4,S} {7,S}
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
    index = 0,
    label = "s1_4_5_ene",
    group = "OR{s1_4_5_ene_1, s1_4_5_ene_2, s1_4_5_ene_6}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "s1_4_5_ene_1",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2 * C u0 {1,S} {7,S}
3   C u0 {1,S} {6,S}
4   C u0 {1,S} {8,D}
5   C u0 {1,S} {6,S}
6   C u0 {3,S} {5,S}
7   C u0 {2,S} {8,S}
8   C u0 {4,D} {7,S}
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
    label = "s1_4_5_ene_2",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2 * C u0 {1,S} {8,S}
3   C u0 {1,S} {7,S}
4   C u0 {1,S} {6,S}
5   C u0 {1,S} {6,S}
6   C u0 {4,S} {5,S}
7   C u0 {3,S} {8,D}
8   C u0 {2,S} {7,D}
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
    label = "s1_4_5_ene_6",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2 * C u0 {1,S} {8,S}
3   C u0 {1,S} {6,D}
4   C u0 {1,S} {6,S}
5   C u0 {1,S} {7,S}
6   C u0 {3,D} {4,S}
7   C u0 {5,S} {8,S}
8   C u0 {2,S} {7,S}
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
    index = 21,
    label = "s1_4_5_diene_1_3",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2   C u0 {1,S} {6,S}
3 * C u0 {1,S} {7,D}
4   C u0 {1,S} {8,D}
5   C u0 {1,S} {6,S}
6   C u0 {2,S} {5,S}
7   C u0 {3,D} {8,S}
8   C u0 {4,D} {7,S}
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
    label = "s1_4_5_diene_1_6",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2   C u0 {1,S} {6,D}
3 * C u0 {1,S} {7,S}
4   C u0 {1,S} {8,D}
5   C u0 {1,S} {6,S}
6   C u0 {2,D} {5,S}
7   C u0 {3,S} {8,S}
8   C u0 {4,D} {7,S}
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
    label = "s1_4_5_diene_2_6",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2 * C u0 {1,S} {8,S}
3   C u0 {1,S} {6,D}
4   C u0 {1,S} {7,S}
5   C u0 {1,S} {6,S}
6   C u0 {3,D} {5,S}
7   C u0 {4,S} {8,D}
8   C u0 {2,S} {7,D}
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
    index = 0,
    label = "s1_4_6",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
7 * C u0 {5,[S,D,T,B]} {9,[S,D,T,B]}
8   C u0 {3,[S,D,T,B]} {9,[S,D,T,B]}
9   C u0 {7,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "s1_4_6_ane",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2   C u0 {1,S} {6,S}
3   C u0 {1,S} {8,S}
4   C u0 {1,S} {6,S}
5   C u0 {1,S} {7,S}
6   C u0 {2,S} {4,S}
7 * C u0 {5,S} {9,S}
8   C u0 {3,S} {9,S}
9   C u0 {7,S} {8,S}
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
    index = 25,
    label = "s1_4_6_ene_1",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2   C u0 {1,S} {6,S}
3   C u0 {1,S} {8,D}
4   C u0 {1,S} {6,S}
5   C u0 {1,S} {7,S}
6   C u0 {2,S} {4,S}
7 * C u0 {5,S} {9,S}
8   C u0 {3,D} {9,S}
9   C u0 {7,S} {8,S}
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
    label = "s1_4_6_ene_2",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2   C u0 {1,S} {7,S}
3   C u0 {1,S} {6,S}
4   C u0 {1,S} {6,S}
5   C u0 {1,S} {8,S}
6   C u0 {3,S} {4,S}
7 * C u0 {2,S} {9,S}
8   C u0 {5,S} {9,D}
9   C u0 {7,S} {8,D}
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
    label = "s1_4_6_ene_7",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2   C u0 {1,S} {6,D}
3   C u0 {1,S} {8,S}
4   C u0 {1,S} {7,S}
5   C u0 {1,S} {6,S}
6   C u0 {2,D} {5,S}
7 * C u0 {4,S} {9,S}
8   C u0 {3,S} {9,S}
9   C u0 {7,S} {8,S}
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
    index = 28,
    label = "s1_4_6_diene_1_3",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2   C u0 {1,S} {8,S}
3   C u0 {1,S} {6,S}
4   C u0 {1,S} {7,D}
5   C u0 {1,S} {6,S}
6   C u0 {3,S} {5,S}
7 * C u0 {4,D} {9,S}
8   C u0 {2,S} {9,D}
9   C u0 {7,S} {8,D}
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
    label = "s1_4_6_diene_1_4",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2   C u0 {1,S} {8,D}
3   C u0 {1,S} {6,S}
4   C u0 {1,S} {6,S}
5   C u0 {1,S} {7,D}
6   C u0 {3,S} {4,S}
7 * C u0 {5,D} {9,S}
8   C u0 {2,D} {9,S}
9   C u0 {7,S} {8,S}
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
    label = "s1_4_6_diene_1_7",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2   C u0 {1,S} {6,D}
3   C u0 {1,S} {6,S}
4   C u0 {1,S} {8,D}
5   C u0 {1,S} {7,S}
6   C u0 {2,D} {3,S}
7 * C u0 {5,S} {9,S}
8   C u0 {4,D} {9,S}
9   C u0 {7,S} {8,S}
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
    label = "s1_4_6_diene_2_7",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2   C u0 {1,S} {6,D}
3   C u0 {1,S} {8,S}
4   C u0 {1,S} {6,S}
5   C u0 {1,S} {7,S}
6   C u0 {2,D} {4,S}
7 * C u0 {5,S} {9,D}
8   C u0 {3,S} {9,S}
9   C u0 {7,D} {8,S}
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
    index = 0,
    label = "s1_5_5",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 * C u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
6   C u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
7   C u0 {3,[S,D,T,B]} {6,[S,D,T,B]}
8   C u0 {5,[S,D,T,B]} {9,[S,D,T,B]}
9   C u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "s1_5_5_ane",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2 * C u0 {1,S} {9,S}
3   C u0 {1,S} {7,S}
4   C u0 {1,S} {6,S}
5   C u0 {1,S} {8,S}
6   C u0 {4,S} {7,S}
7   C u0 {3,S} {6,S}
8   C u0 {5,S} {9,S}
9   C u0 {2,S} {8,S}
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
    index = 33,
    label = "s1_5_5_ene_1",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2 * C u0 {1,S} {9,S}
3   C u0 {1,S} {6,D}
4   C u0 {1,S} {8,S}
5   C u0 {1,S} {7,S}
6   C u0 {3,D} {8,S}
7   C u0 {5,S} {9,S}
8   C u0 {4,S} {6,S}
9   C u0 {2,S} {7,S}
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
    label = "s1_5_5_ene_2",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2 * C u0 {1,S} {7,S}
3   C u0 {1,S} {6,S}
4   C u0 {1,S} {9,S}
5   C u0 {1,S} {8,S}
6   C u0 {3,S} {9,D}
7   C u0 {2,S} {8,S}
8   C u0 {5,S} {7,S}
9   C u0 {4,S} {6,D}
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
    index = 35,
    label = "s1_5_5_diene_1_3",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2 * C u0 {1,S} {7,D}
3   C u0 {1,S} {8,D}
4   C u0 {1,S} {9,S}
5   C u0 {1,S} {6,S}
6   C u0 {5,S} {9,S}
7   C u0 {2,D} {8,S}
8   C u0 {3,D} {7,S}
9   C u0 {4,S} {6,S}
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
    label = "s1_5_5_diene_1_6",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2 * C u0 {1,S} {6,S}
3   C u0 {1,S} {8,S}
4   C u0 {1,S} {9,D}
5   C u0 {1,S} {7,D}
6   C u0 {2,S} {7,S}
7   C u0 {5,D} {6,S}
8   C u0 {3,S} {9,S}
9   C u0 {4,D} {8,S}
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
    label = "s1_5_5_diene_1_7",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2 * C u0 {1,S} {7,D}
3   C u0 {1,S} {6,S}
4   C u0 {1,S} {9,S}
5   C u0 {1,S} {8,S}
6   C u0 {3,S} {9,D}
7   C u0 {2,D} {8,S}
8   C u0 {5,S} {7,S}
9   C u0 {4,S} {6,D}
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
    label = "s1_5_5_diene_2_7",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S} {5,S}
2 * C u0 {1,S} {9,S}
3   C u0 {1,S} {8,S}
4   C u0 {1,S} {7,S}
5   C u0 {1,S} {6,S}
6   C u0 {5,S} {8,D}
7   C u0 {4,S} {9,D}
8   C u0 {3,S} {6,D}
9   C u0 {2,S} {7,D}
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
    index = 0,
    label = "s1_5_6",
    group = 
"""
1    C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2    C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
3    C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
4    C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5    C u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
6  * C u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
7    C u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
8    C u0 {4,[S,D,T,B]} {10,[S,D,T,B]}
9    C u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
10   C u0 {8,[S,D,T,B]} {9,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "s1_5_6_ane",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {7,S}
3    C u0 {1,S} {6,S}
4    C u0 {1,S} {8,S}
5    C u0 {1,S} {9,S}
6  * C u0 {3,S} {7,S}
7    C u0 {2,S} {6,S}
8    C u0 {4,S} {10,S}
9    C u0 {5,S} {10,S}
10   C u0 {8,S} {9,S}
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
    index = 40,
    label = "s1_5_6_ene_1",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {6,S}
3    C u0 {1,S} {7,D}
4    C u0 {1,S} {8,S}
5    C u0 {1,S} {9,S}
6  * C u0 {2,S} {9,S}
7    C u0 {3,D} {10,S}
8    C u0 {4,S} {10,S}
9    C u0 {5,S} {6,S}
10   C u0 {7,S} {8,S}
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
    label = "s1_5_6_ene_2",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {6,S}
3    C u0 {1,S} {8,S}
4    C u0 {1,S} {7,S}
5    C u0 {1,S} {9,S}
6    C u0 {2,S} {10,S}
7  * C u0 {4,S} {9,S}
8    C u0 {3,S} {10,D}
9    C u0 {5,S} {7,S}
10   C u0 {6,S} {8,D}
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
    label = "s1_5_6_ene_7",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {7,S}
3    C u0 {1,S} {8,D}
4    C u0 {1,S} {6,S}
5    C u0 {1,S} {9,S}
6    C u0 {4,S} {10,S}
7    C u0 {2,S} {10,S}
8  * C u0 {3,D} {9,S}
9    C u0 {5,S} {8,S}
10   C u0 {6,S} {7,S}
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
    label = "s1_5_6_ene_8",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {7,S}
3    C u0 {1,S} {6,S}
4    C u0 {1,S} {9,S}
5    C u0 {1,S} {8,S}
6  * C u0 {3,S} {8,D}
7    C u0 {2,S} {10,S}
8    C u0 {5,S} {6,D}
9    C u0 {4,S} {10,S}
10   C u0 {7,S} {9,S}
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
    index = 44,
    label = "s1_5_6_diene_1_3",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {9,S}
3    C u0 {1,S} {8,S}
4    C u0 {1,S} {6,D}
5    C u0 {1,S} {7,S}
6    C u0 {4,D} {10,S}
7  * C u0 {5,S} {9,S}
8    C u0 {3,S} {10,D}
9    C u0 {2,S} {7,S}
10   C u0 {6,S} {8,D}
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
    label = "s1_5_6_diene_1_4",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {6,S}
3    C u0 {1,S} {8,D}
4    C u0 {1,S} {9,D}
5    C u0 {1,S} {7,S}
6  * C u0 {2,S} {7,S}
7    C u0 {5,S} {6,S}
8    C u0 {3,D} {10,S}
9    C u0 {4,D} {10,S}
10   C u0 {8,S} {9,S}
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
    label = "s1_5_6_diene_1_7",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {7,S}
3    C u0 {1,S} {6,S}
4    C u0 {1,S} {9,D}
5    C u0 {1,S} {8,D}
6    C u0 {3,S} {10,S}
7  * C u0 {2,S} {9,S}
8    C u0 {5,D} {10,S}
9    C u0 {4,D} {7,S}
10   C u0 {6,S} {8,S}
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
    label = "s1_5_6_diene_1_8",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {8,D}
3    C u0 {1,S} {6,S}
4    C u0 {1,S} {9,S}
5    C u0 {1,S} {7,S}
6  * C u0 {3,S} {9,D}
7    C u0 {5,S} {10,S}
8    C u0 {2,D} {10,S}
9    C u0 {4,S} {6,D}
10   C u0 {7,S} {8,S}
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
    label = "s1_5_6_diene_2_7",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {7,S}
3    C u0 {1,S} {9,D}
4    C u0 {1,S} {8,S}
5    C u0 {1,S} {6,S}
6  * C u0 {5,S} {9,S}
7    C u0 {2,S} {10,S}
8    C u0 {4,S} {10,D}
9    C u0 {3,D} {6,S}
10   C u0 {7,S} {8,D}
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
    label = "s1_5_6_diene_2_8",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {6,S}
3    C u0 {1,S} {9,S}
4    C u0 {1,S} {7,S}
5    C u0 {1,S} {8,S}
6  * C u0 {2,S} {7,D}
7    C u0 {4,S} {6,D}
8    C u0 {5,S} {10,D}
9    C u0 {3,S} {10,S}
10   C u0 {8,D} {9,S}
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
    label = "s1_5_6_diene_7_9",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {6,D}
3    C u0 {1,S} {7,S}
4    C u0 {1,S} {9,S}
5    C u0 {1,S} {8,D}
6  * C u0 {2,D} {8,S}
7    C u0 {3,S} {10,S}
8    C u0 {5,D} {6,S}
9    C u0 {4,S} {10,S}
10   C u0 {7,S} {9,S}
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
    index = 0,
    label = "s1_5_6_triene",
    group = "OR{s1_5_6_triene_1_3_7, s1_5_6_triene_1_3_8}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "s1_5_6_triene_1_3_7",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {8,S}
3    C u0 {1,S} {7,D}
4    C u0 {1,S} {6,D}
5    C u0 {1,S} {9,S}
6  * C u0 {4,D} {9,S}
7    C u0 {3,D} {10,S}
8    C u0 {2,S} {10,D}
9    C u0 {5,S} {6,S}
10   C u0 {7,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.72,-6.82,-6.48,-5.99,-5.19,-4.29,-2.12],'cal/(mol*K)'),
        H298 = (14.743,'kcal/mol'),
        S298 = (57.75,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt17 from C10H11 library.
""",
)

entry(
    index = 44,
    label = "s1_5_6_triene_1_3_8",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {8,S}
3    C u0 {1,S} {9,S}
4    C u0 {1,S} {7,S}
5    C u0 {1,S} {6,D}
6    C u0 {5,D} {10,S}
7  * C u0 {4,S} {8,D}
8    C u0 {2,S} {7,D}
9    C u0 {3,S} {10,D}
10   C u0 {6,S} {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.34,-6.73,-6.55,-6.13,-5.34,-4.43,-2.23],'cal/(mol*K)'),
        H298 = (14.573,'kcal/mol'),
        S298 = (57.37,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt17 from C10H11 library.
""",
)

entry(
    index = 0,
    label = "s1_5_6_tetraene",
    group = "OR{s1_5_6_tetraene_1_3_7_9, s1_5_6_tetraene_1_4_7_9}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "s1_5_6_tetraene_1_3_7_9",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {8,S}
3    C u0 {1,S} {6,D}
4    C u0 {1,S} {9,D}
5    C u0 {1,S} {7,D}
6    C u0 {3,D} {10,S}
7  * C u0 {5,D} {9,S}
8    C u0 {2,S} {10,D}
9    C u0 {4,D} {7,S}
10   C u0 {6,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.54,-7.38,-7.43,-7.04,-6.22,-5.38,-3.12],'cal/(mol*K)'),
        H298 = (3.583,'kcal/mol'),
        S298 = (59.28,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species prod2 from naphthalene_H library.
""",
)

entry(
    index = 44,
    label = "s1_5_6_tetraene_1_4_7_9",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {7,D}
3    C u0 {1,S} {9,D}
4    C u0 {1,S} {8,D}
5    C u0 {1,S} {6,D}
6  * C u0 {5,D} {8,S}
7    C u0 {2,D} {10,S}
8    C u0 {4,D} {6,S}
9    C u0 {3,D} {10,S}
10   C u0 {7,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.98,-5.93,-5.62,-5.32,-5,-4.36,-3.36],'cal/(mol*K)'),
        H298 = (11.133,'kcal/mol'),
        S298 = (57.08,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species prod2 from naphthalene_H library.
""",
)

entry(
    index = 0,
    label = "s1_6_6",
    group = 
"""
1    C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2    C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
3    C u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
4    C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
5    C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    C u0 {5,[S,D,T,B]} {11,[S,D,T,B]}
7    C u0 {4,[S,D,T,B]} {10,[S,D,T,B]}
8    C u0 {2,[S,D,T,B]} {11,[S,D,T,B]}
9    C u0 {3,[S,D,T,B]} {10,[S,D,T,B]}
10 * C u0 {7,[S,D,T,B]} {9,[S,D,T,B]}
11   C u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "s1_6_6_ane",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {8,S}
3    C u0 {1,S} {9,S}
4    C u0 {1,S} {7,S}
5    C u0 {1,S} {6,S}
6    C u0 {5,S} {11,S}
7    C u0 {4,S} {10,S}
8    C u0 {2,S} {11,S}
9    C u0 {3,S} {10,S}
10 * C u0 {7,S} {9,S}
11   C u0 {6,S} {8,S}
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
    index = 52,
    label = "s1_6_6_ene_1",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {9,S}
3    C u0 {1,S} {8,S}
4    C u0 {1,S} {7,S}
5    C u0 {1,S} {6,D}
6    C u0 {5,D} {11,S}
7    C u0 {4,S} {11,S}
8    C u0 {3,S} {10,S}
9    C u0 {2,S} {10,S}
10 * C u0 {8,S} {9,S}
11   C u0 {6,S} {7,S}
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
    label = "s1_6_6_ene_2",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {9,S}
3    C u0 {1,S} {8,S}
4    C u0 {1,S} {7,S}
5    C u0 {1,S} {6,S}
6    C u0 {5,S} {10,S}
7    C u0 {4,S} {11,S}
8    C u0 {3,S} {10,D}
9    C u0 {2,S} {11,S}
10 * C u0 {6,S} {8,D}
11   C u0 {7,S} {9,S}
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
    index = 54,
    label = "s1_6_6_diene_1_3",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {6,D}
3    C u0 {1,S} {9,S}
4    C u0 {1,S} {8,S}
5    C u0 {1,S} {7,S}
6    C u0 {2,D} {11,S}
7    C u0 {5,S} {10,S}
8    C u0 {4,S} {10,S}
9    C u0 {3,S} {11,D}
10 * C u0 {7,S} {8,S}
11   C u0 {6,S} {9,D}
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
    label = "s1_6_6_diene_1_4",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {9,D}
3    C u0 {1,S} {6,D}
4    C u0 {1,S} {7,S}
5    C u0 {1,S} {8,S}
6    C u0 {3,D} {10,S}
7    C u0 {4,S} {11,S}
8    C u0 {5,S} {11,S}
9    C u0 {2,D} {10,S}
10 * C u0 {6,S} {9,S}
11   C u0 {7,S} {8,S}
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
    label = "s1_6_6_diene_1_7",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {9,S}
3    C u0 {1,S} {7,D}
4    C u0 {1,S} {6,S}
5    C u0 {1,S} {8,D}
6    C u0 {4,S} {10,S}
7    C u0 {3,D} {11,S}
8    C u0 {5,D} {10,S}
9    C u0 {2,S} {11,S}
10 * C u0 {6,S} {8,S}
11   C u0 {7,S} {9,S}
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
    label = "s1_6_6_diene_1_8",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {6,S}
3    C u0 {1,S} {9,S}
4    C u0 {1,S} {7,S}
5    C u0 {1,S} {8,D}
6    C u0 {2,S} {10,S}
7    C u0 {4,S} {11,S}
8    C u0 {5,D} {10,S}
9    C u0 {3,S} {11,D}
10 * C u0 {6,S} {8,S}
11   C u0 {7,S} {9,D}
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
    label = "s1_6_6_diene_2_8",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S} {5,S}
2    C u0 {1,S} {6,S}
3    C u0 {1,S} {7,S}
4    C u0 {1,S} {8,S}
5    C u0 {1,S} {9,S}
6    C u0 {2,S} {10,S}
7    C u0 {3,S} {11,D}
8    C u0 {4,S} {11,S}
9    C u0 {5,S} {10,D}
10 * C u0 {6,S} {9,D}
11   C u0 {7,D} {8,S}
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
    index = 0,
    label = "s2_3_3",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3 * C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "s2_3_3_ane",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S}
2   C u0 {1,S} {3,S} {4,S}
3 * C u0 {1,S} {2,S}
4   C u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.74,-5.18,-4.85,-4.17,-3.61,-4.01,-3.22],'cal/(mol*K)'),
        H298 = (65.52,'kcal/mol'),
        S298 = (69.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Modified to match experimental data from NIST, S and cp from PM7 calculation
""",
)

entry(
    index = 60,
    label = "s2_3_3_ene",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S}
2   C u0 {1,S} {3,S} {4,D}
3 * C u0 {1,S} {2,S}
4   C u0 {1,S} {2,D}
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
    index = 0,
    label = "s2_3_4",
    group = 
"""
1 * C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
5   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "s2_3_4_ane",
    group = 
"""
1 * C u0 {2,S} {3,S} {4,S}
2   C u0 {1,S} {3,S} {5,S}
3   C u0 {1,S} {2,S}
4   C u0 {1,S} {5,S}
5   C u0 {2,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.7,-6.66,-5.78,-4.57,-3.31,-3.56,-2.35],'cal/(mol*K)'),
        H298 = (55.38,'kcal/mol'),
        S298 = (64.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Properties of Liquids and Gases, Poling 5th Ed. S, Cp from PM7 calculation
""",
)

entry(
    index = 0,
    label = "s2_3_4_ene",
    group = "OR{s2_3_4_ene_1, s2_3_4_ene_m}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "s2_3_4_ene_1",
    group = 
"""
1 * C u0 {2,S} {3,S} {5,S}
2   C u0 {1,S} {3,S} {4,S}
3   C u0 {1,S} {2,S}
4   C u0 {2,S} {5,D}
5   C u0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.56,-5.1,-4.92,-3.97,-3.38,-3.81,-2.92],'cal/(mol*K)'),
        H298 = (67.9,'kcal/mol'),
        S298 = (65.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Wiberg, K. Angew. Chem., Int. Ed. Engl. 1986, 25, 312 1986 experimental S, Cp from PM7 calculation
""",
)

entry(
    index = 63,
    label = "s2_3_4_ene_m",
    group = 
"""
1 * C u0 {2,D} {3,S} {5,S}
2   C u0 {1,D} {3,S} {4,S}
3   C u0 {1,S} {2,S}
4   C u0 {2,S} {5,S}
5   C u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.52,-5.35,-5.15,-4.39,-3.54,-3.73,-2.7],'cal/(mol*K)'),
        H298 = (126,'kcal/mol'),
        S298 = (66.41,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Wiberg, K. Angew. Chem., Int. Ed. Engl. 1986, 25, 312 1986 ab initio, S, Cp from PM7 calculation
""",
)

entry(
    index = 0,
    label = "s2_3_5",
    group = 
"""
1 * C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
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
    index = 64,
    label = "s2_3_5_ane",
    group = 
"""
1 * C u0 {2,S} {3,S} {5,S}
2   C u0 {1,S} {3,S} {4,S}
3   C u0 {1,S} {2,S}
4   C u0 {2,S} {6,S}
5   C u0 {1,S} {6,S}
6   C u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.27,-8.01,-6.85,-5.27,-3.32,-3.2,-1.6],'cal/(mol*K)'),
        H298 = (32.75,'kcal/mol'),
        S298 = (61.25,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Properties of Liquids and Gases, Poling 5th Ed. S, Cp from PM7 calculation
""",
)

entry(
    index = 0,
    label = "s2_3_5_ene",
    group = "OR{s2_3_5_ene_1, s2_3_5_ene_side, s2_3_5_ene_1_side}",
    thermo = None,
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
1 * C u0 {2,S} {3,S} {5,S}
2   C u0 {1,S} {3,S} {4,S}
3   C u0 {1,S} {2,S}
4   C u0 {2,S} {6,D}
5   C u0 {1,S} {6,S}
6   C u0 {4,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.53,-5.88833,-6.0675,-5.87167,-5.755,-5.22583,-3.91833],'cal/(mol*K)','+|-',[13.695,15.6123,16.4506,15.9745,14.9052,13.0715,9.23303]),
        H298 = (33.7772,'kcal/mol','+|-',4.36481),
        S298 = (75.9204,'cal/(mol*K)','+|-',29.7929),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species product1 from vinylCPD_H library.
Fitted from species product19 from vinylCPD_H library.
Fitted from species product19 from vinylCPD_H library.
Fitted from species product36 from vinylCPD_H library.
Fitted from species product39 from vinylCPD_H library.
Fitted from species pdt24 from C10H11 library.
Fitted from species pdt24 from C10H11 library.
Fitted from species pdt57 from C10H11 library.
Fitted from species biring1 from Fulvene_H library.
Fitted from species prod1 from naphthalene_H library.
Fitted from species prod3 from naphthalene_H library.
Fitted from species prod3 from naphthalene_H library.
""",
)

entry(
    index = 65,
    label = "s2_3_5_ene_side",
    group = 
"""
1 * C u0 {2,S} {4,S} {6,S}
2   C u0 {1,S} {4,S} {5,S}
3   C u0 {5,S} {6,S} {7,D}
4   C u0 {1,S} {2,S}
5   C u0 {2,S} {3,S}
6   C u0 {1,S} {3,S}
7   R ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.97,-4.68,-4.47,-4.27,-4.21,-3.94,-3.36],'cal/(mol*K)'),
        H298 = (32.543,'kcal/mol'),
        S298 = (65.1674,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species product36 from vinylCPD_H library.
""",
)

entry(
    index = 65,
    label = "s2_3_5_ene_1_side",
    group = 
"""
1 * C u0 {2,S} {3,S} {4,S}
2   C u0 {1,S} {3,S} {5,S}
3   C u0 {1,S} {2,S} {7,D}
4   C u0 {1,S} {6,S}
5   C u0 {2,S} {6,D}
6   C u0 {4,S} {5,D}
7   R ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.48,-3.9,-3.81,-3.6,-3.7,-3.68,-3.44],'cal/(mol*K)'),
        H298 = (47.323,'kcal/mol'),
        S298 = (66.8874,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species product42 from vinylCPD_H library.
""",
)

entry(
    index = 0,
    label = "s2_3_6",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6 * C u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
7   C u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = None,
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
1   C u0 {2,S} {3,S} {5,S}
2   C u0 {1,S} {3,S} {4,S}
3   C u0 {1,S} {2,S}
4   C u0 {2,S} {6,S}
5   C u0 {1,S} {7,S}
6 * C u0 {4,S} {7,S}
7   C u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.33,-8.86,-7.46,-5.59,-3.08,-2.67,-0.76],'cal/(mol*K)'),
        H298 = (28.95,'kcal/mol'),
        S298 = (57.69,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Properties of Liquids and Gases, Poling 5th Ed. S, Cp from PM7 calculation
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
    index = 67,
    label = "s2_3_6_ene_1",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S}
2   C u0 {1,S} {3,S} {5,S}
3   C u0 {1,S} {2,S}
4   C u0 {1,S} {6,D}
5   C u0 {2,S} {7,S}
6 * C u0 {4,D} {7,S}
7   C u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.33,-8.86,-7.46,-5.59,-3.08,-2.67,-0.76],'cal/(mol*K)'),
        H298 = (28.95,'kcal/mol'),
        S298 = (57.69,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Copied from entry: bicyclo-(4.1.0)-heptane
""",
)

entry(
    index = 68,
    label = "s2_3_6_ene_2",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S}
2   C u0 {1,S} {3,S} {5,S}
3   C u0 {1,S} {2,S}
4   C u0 {1,S} {7,S}
5   C u0 {2,S} {6,S}
6 * C u0 {5,S} {7,D}
7   C u0 {4,S} {6,D}
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
    index = 0,
    label = "s2_3_6_diene",
    group = "OR{s2_3_6_diene_0_2, s2_3_6_diene_0_3, s2_3_6_diene_1_3}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "s2_3_6_diene_0_2",
    group = 
"""
1   C u0 {2,S} {3,S} {4,D}
2   C u0 {1,S} {3,S} {5,S}
3   C u0 {1,S} {2,S}
4   C u0 {1,D} {6,S}
5   C u0 {2,S} {7,S}
6 * C u0 {4,S} {7,D}
7   C u0 {5,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.31,-5.83,-5.92,-5.53,-5.17,-4.71,-3.89],'cal/(mol*K)'),
        H298 = (48.433,'kcal/mol'),
        S298 = (65.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species product46 from vinylCPD_H library.
""",
)

entry(
    index = 69,
    label = "s2_3_6_diene_0_3",
    group = 
"""
1   C u0 {2,S} {3,S} {5,D}
2   C u0 {1,S} {3,S} {4,S}
3   C u0 {1,S} {2,S}
4   C u0 {2,S} {7,D}
5   C u0 {1,D} {6,S}
6 * C u0 {5,S} {7,S}
7   C u0 {4,D} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.82,-4.74,-4.65,-4.52,-4.39,-4.28,-4.42],'cal/(mol*K)'),
        H298 = (53.563,'kcal/mol'),
        S298 = (63.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species product46 from vinylCPD_H library.
""",
)

entry(
    index = 69,
    label = "s2_3_6_diene_1_3",
    group = 
"""
1   C u0 {2,S} {3,S} {5,S}
2   C u0 {1,S} {3,S} {4,S}
3   C u0 {1,S} {2,S}
4   C u0 {2,S} {6,D}
5   C u0 {1,S} {7,D}
6 * C u0 {4,D} {7,S}
7   C u0 {5,D} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.38,-4.49,-4.61,-4.23,-4.095,-3.75,-3.51],'cal/(mol*K)','+|-',[1.89346,4.02361,4.97034,5.32536,5.73956,5.79873,8.8756]),
        H298 = (41.913,'kcal/mol','+|-',20.8172),
        S298 = (62.305,'cal/(mol*K)','+|-',13.2229),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species product34 from vinylCPD_H library.
Fitted from species product46 from vinylCPD_H library.
""",
)

entry(
    index = 69,
    label = "s2_3_6_ben",
    group = 
"""
1   C u0 {2,B} {3,S} {4,B}
2   C u0 {1,B} {3,S} {5,B}
3   C u0 {1,S} {2,S}
4   C u0 {1,B} {6,B}
5   C u0 {2,B} {7,B}
6 * C u0 {4,B} {7,B}
7   C u0 {5,B} {6,B}
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
    index = 0,
    label = "s2_3_7",
    group = 
"""
1 * C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   C u0 {4,[S,D,T,B]} {8,[S,D,T,B]}
7   C u0 {5,[S,D,T,B]} {8,[S,D,T,B]}
8   C u0 {6,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "s2_3_7_ane",
    group = 
"""
1 * C u0 {2,S} {3,S} {5,S}
2   C u0 {1,S} {3,S} {4,S}
3   C u0 {1,S} {2,S}
4   C u0 {2,S} {6,S}
5   C u0 {1,S} {7,S}
6   C u0 {4,S} {8,S}
7   C u0 {5,S} {8,S}
8   C u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.29,-9.54,-7.86,-5.68,-2.67,-2.04,0.13],'cal/(mol*K)'),
        H298 = (29.64,'kcal/mol'),
        S298 = (51.29,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Properties of Liquids and Gases, Poling 5th Ed. S, Cp from PM7 calculation
""",
)

entry(
    index = 0,
    label = "s2_3_8",
    group = 
"""
1 * C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {4,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   C u0 {4,[S,D,T,B]} {8,[S,D,T,B]}
7   C u0 {5,[S,D,T,B]} {9,[S,D,T,B]}
8   C u0 {6,[S,D,T,B]} {9,[S,D,T,B]}
9   C u0 {7,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "s2_3_8_ane",
    group = 
"""
1 * C u0 {2,S} {3,S} {5,S}
2   C u0 {1,S} {3,S} {4,S}
3   C u0 {1,S} {2,S}
4   C u0 {2,S} {6,S}
5   C u0 {1,S} {7,S}
6   C u0 {4,S} {8,S}
7   C u0 {5,S} {9,S}
8   C u0 {6,S} {9,S}
9   C u0 {7,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.04,-10.02,-8.09,-5.64,-2.16,-1.32,1.06],'cal/(mol*K)'),
        H298 = (31.14,'kcal/mol'),
        S298 = (48.46,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Properties of Liquids and Gases, Poling 5th Ed. S, Cp from PM7 calculation
""",
)

entry(
    index = 0,
    label = "s2_4_4",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3 * C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6   C u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "s2_4_4_ane",
    group = 
"""
1   C u0 {2,S} {4,S} {5,S}
2   C u0 {1,S} {3,S} {6,S}
3 * C u0 {2,S} {4,S}
4   C u0 {1,S} {3,S}
5   C u0 {1,S} {6,S}
6   C u0 {2,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.54,-8.07,-6.7,-4.98,-3.04,-3.1,-1.48],'cal/(mol*K)'),
        H298 = (51.8,'kcal/mol'),
        S298 = (59.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Wiberg, K. Angew. Chem., Int. Ed. Engl. 1986, 25, 312 1986 experimental S, Cp from PM7 calculation
""",
)

entry(
    index = 0,
    label = "s2_4_4_ene",
    group = "OR{s2_4_4_ene_1, s2_4_4_ene_m}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "s2_4_4_ene_1",
    group = 
"""
1   C u0 {2,S} {3,S} {5,S}
2   C u0 {1,S} {4,S} {6,S}
3 * C u0 {1,S} {4,S}
4   C u0 {2,S} {3,S}
5   C u0 {1,S} {6,D}
6   C u0 {2,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.35,-6.47,-5.81,-4.36,-3.1,-3.34,-2.05],'cal/(mol*K)'),
        H298 = (55.7,'kcal/mol'),
        S298 = (60.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Wiberg, K. Angew. Chem., Int. Ed. Engl. 1986, 25, 312 1986 experimental S, Cp from PM7 calculation
""",
)

entry(
    index = 74,
    label = "s2_4_4_ene_m",
    group = 
"""
1   C u0 {2,D} {4,S} {6,S}
2   C u0 {1,D} {3,S} {5,S}
3 * C u0 {2,S} {4,S}
4   C u0 {1,S} {3,S}
5   C u0 {2,S} {6,S}
6   C u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.4,-6.61,-5.83,-4.57,-3.17,-3.27,-1.87],'cal/(mol*K)'),
        H298 = (87,'kcal/mol'),
        S298 = (58.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Wiberg, K. Angew. Chem., Int. Ed. Engl. 1986, 25, 312 1986 ab initio S, Cp from PM7 calculation
""",
)

entry(
    index = 0,
    label = "s2_4_5",
    group = 
"""
1 * C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   C u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   C u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "s2_4_5_ane",
    group = 
"""
1 * C u0 {2,S} {3,S} {5,S}
2   C u0 {1,S} {4,S} {6,S}
3   C u0 {1,S} {4,S}
4   C u0 {2,S} {3,S}
5   C u0 {1,S} {7,S}
6   C u0 {2,S} {7,S}
7   C u0 {5,S} {6,S}
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
    index = 0,
    label = "s2_4_5_ene",
    group = "OR{s2_4_5_ene_0, s2_4_5_ene_1}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "s2_4_5_ene_0",
    group = 
"""
1 * C u0 {2,S} {4,S} {6,D}
2   C u0 {1,S} {3,S} {5,S}
3   C u0 {2,S} {4,S}
4   C u0 {1,S} {3,S}
5   C u0 {2,S} {7,S}
6   C u0 {1,D} {7,S}
7   C u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.32,-5.85,-5.4,-4.81,-4.34,-3.92,-3.03],'cal/(mol*K)'),
        H298 = (45.173,'kcal/mol'),
        S298 = (60.95,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species product25 from vinylCPD_H library.
""",
)

entry(
    index = 76,
    label = "s2_4_5_ene_1",
    group = 
"""
1 * C u0 {2,S} {3,S} {6,S}
2   C u0 {1,S} {4,S} {5,S}
3   C u0 {1,S} {4,S}
4   C u0 {2,S} {3,S}
5   C u0 {2,S} {7,S}
6   C u0 {1,S} {7,D}
7   C u0 {5,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.49,-5.912,-5.48,-4.912,-4.61,-4.122,-3.47],'cal/(mol*K)','+|-',[11.276,13.3805,14.1663,13.3764,12.968,11.469,9.42729]),
        H298 = (37.631,'kcal/mol','+|-',6.50583),
        S298 = (71.26,'cal/(mol*K)','+|-',32.7404),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species product3 from vinylCPD_H library.
Fitted from species product8 from vinylCPD_H library.
Fitted from species product25 from vinylCPD_H library.
Fitted from species pdt7 from C10H11 library.
Fitted from species pdt7 from C10H11 library.
""",
)

entry(
    index = 0,
    label = "s2_4_5_diene",
    group = "OR{s2_4_5_diene_0_3, s2_4_5_diene_1_5, s2_4_5_diene_4_6}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "s2_4_5_diene_0_3",
    group = 
"""
1 * C u0 {2,S} {3,S} {5,D}
2   C u0 {1,S} {4,S} {6,D}
3   C u0 {1,S} {4,S}
4   C u0 {2,S} {3,S}
5   C u0 {1,D} {7,S}
6   C u0 {2,D} {7,S}
7   C u0 {5,S} {6,S}
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
    label = "s2_4_5_diene_1_5",
    group = 
"""
1 * C u0 {2,S} {3,S} {6,S}
2   C u0 {1,S} {4,S} {5,S}
3   C u0 {1,S} {4,D}
4   C u0 {2,S} {3,D}
5   C u0 {2,S} {7,D}
6   C u0 {1,S} {7,S}
7   C u0 {5,D} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.23,-4.36,-3.97,-3.6,-3.53,-3.44,-3.16],'cal/(mol*K)'),
        H298 = (39.483,'kcal/mol'),
        S298 = (62.16,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species product45 from vinylCPD_H library.
""",
)

entry(
    index = 76,
    label = "s2_4_5_diene_4_6",
    group = 
"""
1 * C u0 {2,S} {3,D} {6,S}
2   C u0 {1,S} {4,D} {5,S}
3   C u0 {1,D} {4,S}
4   C u0 {2,D} {3,S}
5   C u0 {2,S} {7,S}
6   C u0 {1,S} {7,S}
7   C u0 {5,S} {6,S}
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
    index = 0,
    label = "s2_4_6",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   C u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
7 * C u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8   C u0 {5,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "s2_4_6_ane",
    group = 
"""
1   C u0 {2,S} {3,S} {6,S}
2   C u0 {1,S} {4,S} {5,S}
3   C u0 {1,S} {4,S}
4   C u0 {2,S} {3,S}
5   C u0 {2,S} {8,S}
6   C u0 {1,S} {7,S}
7 * C u0 {6,S} {8,S}
8   C u0 {5,S} {7,S}
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
    index = 0,
    label = "s2_4_6_ene",
    group = "OR{s2_4_6_ene_1, s2_4_6_ene_2, s2_4_6_ene_6}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "s2_4_6_ene_1",
    group = 
"""
1   C u0 {2,S} {3,S} {5,S}
2   C u0 {1,S} {4,S} {6,S}
3   C u0 {1,S} {4,S}
4   C u0 {2,S} {3,S}
5   C u0 {1,S} {7,S}
6   C u0 {2,S} {8,D}
7 * C u0 {5,S} {8,S}
8   C u0 {6,D} {7,S}
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
    label = "s2_4_6_ene_2",
    group = 
"""
1   C u0 {2,S} {4,S} {6,S}
2   C u0 {1,S} {3,S} {5,S}
3   C u0 {2,S} {4,S}
4   C u0 {1,S} {3,S}
5   C u0 {2,S} {7,S}
6   C u0 {1,S} {8,S}
7 * C u0 {5,S} {8,D}
8   C u0 {6,S} {7,D}
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
    label = "s2_4_6_ene_6",
    group = 
"""
1   C u0 {2,S} {4,S} {5,S}
2   C u0 {1,S} {3,S} {6,S}
3   C u0 {2,S} {4,D}
4   C u0 {1,S} {3,D}
5   C u0 {1,S} {7,S}
6   C u0 {2,S} {8,S}
7 * C u0 {5,S} {8,S}
8   C u0 {6,S} {7,S}
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
    index = 0,
    label = "s2_4_6_diene",
    group = "OR{s2_4_6_diene_1_3, s2_4_6_diene_1_6, s2_4_6_diene_2_6, s2_4_6_diene_5_7}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 180,
    label = "s2_4_6_diene_1_3",
    group = 
"""
1   C u0 {2,S} {3,S} {6,S}
2   C u0 {1,S} {4,S} {5,S}
3   C u0 {1,S} {4,S}
4   C u0 {2,S} {3,S}
5   C u0 {2,S} {8,D}
6   C u0 {1,S} {7,D}
7 * C u0 {6,D} {8,S}
8   C u0 {5,D} {7,S}
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
    index = 181,
    label = "s2_4_6_diene_1_6",
    group = 
"""
1   C u0 {2,S} {4,S} {6,S}
2   C u0 {1,S} {3,S} {5,S}
3   C u0 {2,S} {4,D}
4   C u0 {1,S} {3,D}
5   C u0 {2,S} {8,S}
6   C u0 {1,S} {7,D}
7 * C u0 {6,D} {8,S}
8   C u0 {5,S} {7,S}
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
    index = 182,
    label = "s2_4_6_diene_2_6",
    group = 
"""
1   C u0 {2,S} {4,S} {5,S}
2   C u0 {1,S} {3,S} {6,S}
3   C u0 {2,S} {4,D}
4   C u0 {1,S} {3,D}
5   C u0 {1,S} {7,S}
6   C u0 {2,S} {8,S}
7 * C u0 {5,S} {8,D}
8   C u0 {6,S} {7,D}
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
    index = 182,
    label = "s2_4_6_diene_5_7",
    group = 
"""
1   C u0 {2,S} {4,D} {6,S}
2   C u0 {1,S} {3,D} {5,S}
3   C u0 {2,D} {4,S}
4   C u0 {1,D} {3,S}
5   C u0 {2,S} {7,S}
6   C u0 {1,S} {8,S}
7 * C u0 {5,S} {8,S}
8   C u0 {6,S} {7,S}
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
    index = 183,
    label = "s2_4_6_ben",
    group = 
"""
1   C u0 {2,B} {4,S} {5,B}
2   C u0 {1,B} {3,S} {6,B}
3   C u0 {2,S} {4,S}
4   C u0 {1,S} {3,S}
5   C u0 {1,B} {7,B}
6   C u0 {2,B} {8,B}
7 * C u0 {5,B} {8,B}
8   C u0 {6,B} {7,B}
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
    index = 0,
    label = "s2_5_5",
    group = 
"""
1   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
3 * C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
6   C u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
7   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]}
8   C u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "s2_5_5_ane",
    group = 
"""
1   C u0 {2,S} {3,S} {5,S}
2   C u0 {1,S} {4,S} {6,S}
3 * C u0 {1,S} {7,S}
4   C u0 {2,S} {7,S}
5   C u0 {1,S} {8,S}
6   C u0 {2,S} {8,S}
7   C u0 {3,S} {4,S}
8   C u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.52,-10.59,-8.62,-6.18,-2.88,-2.26,0.09],'cal/(mol*K)'),
        H298 = (10.3,'kcal/mol'),
        S298 = (54.09,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Automated Estimation of Ring Strain Energies, Gasteiger, 1978, S, Cp from PM7
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
    index = 81,
    label = "s2_5_5_ene_0",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S}
2   C u0 {1,S} {5,D} {6,S}
3 * C u0 {1,S} {8,S}
4   C u0 {1,S} {7,S}
5   C u0 {2,D} {7,S}
6   C u0 {2,S} {8,S}
7   C u0 {4,S} {5,S}
8   C u0 {3,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.85,-8.16,-7.22,-6.08,-4.66,-3.57,-1.84],'cal/(mol*K)'),
        H298 = (13.8,'kcal/mol'),
        S298 = (50.57,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
A.G. Vandeputte isodesmic reactions + B3LYP/cbsb7 S and cp
""",
)

entry(
    index = 82,
    label = "s2_5_5_ene_1",
    group = 
"""
1   C u0 {2,S} {4,S} {5,S}
2   C u0 {1,S} {3,S} {6,S}
3 * C u0 {2,S} {7,D}
4   C u0 {1,S} {8,S}
5   C u0 {1,S} {7,S}
6   C u0 {2,S} {8,S}
7   C u0 {3,D} {5,S}
8   C u0 {4,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.84,-8,-7.03,-5.94,-4.62,-3.53,-1.94],'cal/(mol*K)'),
        H298 = (9.76,'kcal/mol'),
        S298 = (51.17,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
A.G. Vandeputte isodesmic reactions + B3LYP/cbsb7 S and cp
""",
)

entry(
    index = 83,
    label = "s2_5_5_ene_m",
    group = 
"""
1   C u0 {2,D} {3,S} {5,S}
2   C u0 {1,D} {4,S} {6,S}
3 * C u0 {1,S} {8,S}
4   C u0 {2,S} {7,S}
5   C u0 {1,S} {7,S}
6   C u0 {2,S} {8,S}
7   C u0 {4,S} {5,S}
8   C u0 {3,S} {6,S}
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
    index = 84,
    label = "s2_5_5_diene_0_2",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S}
2   C u0 {1,S} {5,S} {6,D}
3 * C u0 {1,S} {8,S}
4   C u0 {1,S} {7,D}
5   C u0 {2,S} {8,S}
6   C u0 {2,D} {7,S}
7   C u0 {4,D} {6,S}
8   C u0 {3,S} {5,S}
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
    label = "s2_5_5_diene_0_3",
    group = 
"""
1   C u0 {2,S} {4,D} {5,S}
2   C u0 {1,S} {3,D} {6,S}
3 * C u0 {2,D} {7,S}
4   C u0 {1,D} {7,S}
5   C u0 {1,S} {8,S}
6   C u0 {2,S} {8,S}
7   C u0 {3,S} {4,S}
8   C u0 {5,S} {6,S}
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
    label = "s2_5_5_diene_m_2",
    group = 
"""
1   C u0 {2,D} {3,S} {5,S}
2   C u0 {1,D} {4,S} {6,S}
3 * C u0 {1,S} {7,S}
4   C u0 {2,S} {8,D}
5   C u0 {1,S} {8,S}
6   C u0 {2,S} {7,S}
7   C u0 {3,S} {6,S}
8   C u0 {4,D} {5,S}
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
    label = "s2_5_5_diene_0_4",
    group = 
"""
1   C u0 {2,S} {3,D} {4,S}
2   C u0 {1,S} {5,D} {6,S}
3 * C u0 {1,D} {7,S}
4   C u0 {1,S} {8,S}
5   C u0 {2,D} {8,S}
6   C u0 {2,S} {7,S}
7   C u0 {3,S} {6,S}
8   C u0 {4,S} {5,S}
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
    label = "s2_5_5_diene_0_5",
    group = 
"""
1   C u0 {2,S} {3,S} {6,S}
2   C u0 {1,S} {4,D} {5,S}
3 * C u0 {1,S} {7,D}
4   C u0 {2,D} {8,S}
5   C u0 {2,S} {7,S}
6   C u0 {1,S} {8,S}
7   C u0 {3,D} {5,S}
8   C u0 {4,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.57,-7.46,-6.33,-5.3,-4.01,-3.25,-1.79],'cal/(mol*K)'),
        H298 = (14.2,'kcal/mol'),
        S298 = (51.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
A. G. Vandeputte CBS-QB3 isodesmic reaction, C12CCC=C1CC=C2 + 3 ethane -> cyclopentene + isobutane + 2-methyl-2-butene, experimental data from the NIST Chemical Webbook
""",
)

entry(
    index = 89,
    label = "s2_5_5_diene_0_6",
    group = 
"""
1   C u0 {2,S} {4,S} {6,S}
2   C u0 {1,S} {3,S} {5,D}
3 * C u0 {2,S} {7,D}
4   C u0 {1,S} {8,S}
5   C u0 {2,D} {8,S}
6   C u0 {1,S} {7,S}
7   C u0 {3,D} {6,S}
8   C u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.57,-7.46,-6.33,-5.3,-4.01,-3.25,-1.79],'cal/(mol*K)'),
        H298 = (14.2,'kcal/mol'),
        S298 = (51.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Copied from entry: C12CCC=C1CC=C2
""",
)

entry(
    index = 90,
    label = "s2_5_5_diene_1_5",
    group = 
"""
1   C u0 {2,S} {3,S} {5,S}
2   C u0 {1,S} {4,S} {6,S}
3 * C u0 {1,S} {7,D}
4   C u0 {2,S} {8,D}
5   C u0 {1,S} {8,S}
6   C u0 {2,S} {7,S}
7   C u0 {3,D} {6,S}
8   C u0 {4,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.57,-7.46,-6.33,-5.3,-4.01,-3.25,-1.79],'cal/(mol*K)'),
        H298 = (10,'kcal/mol'),
        S298 = (51.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
ring strain N. Vandewiele, S and cp taken from C12CCC=C1CC=C2
""",
)

entry(
    index = 91,
    label = "s2_5_5_diene_1_6",
    group = 
"""
1   C u0 {2,S} {3,S} {4,S}
2   C u0 {1,S} {5,S} {6,S}
3 * C u0 {1,S} {7,D}
4   C u0 {1,S} {8,D}
5   C u0 {2,S} {7,S}
6   C u0 {2,S} {8,S}
7   C u0 {3,D} {5,S}
8   C u0 {4,D} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.57,-7.46,-6.33,-5.3,-4.01,-3.25,-1.79],'cal/(mol*K)'),
        H298 = (14.2,'kcal/mol'),
        S298 = (51.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Copied from entry: C12CCC=C1CC=C2
""",
)

entry(
    index = 0,
    label = "s2_5_5_tetraene",
    group = "OR{s2_5_5_tetraene_0_2_4_6}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "s2_5_5_tetraene_0_2_4_6",
    group = 
"""
1   C u0 {2,S} {3,S} {4,D}
2   C u0 {1,S} {5,D} {6,S}
3 * C u0 {1,S} {8,D}
4   C u0 {1,D} {7,S}
5   C u0 {2,D} {8,S}
6   C u0 {2,S} {7,D}
7   C u0 {4,S} {6,D}
8   C u0 {3,D} {5,S}
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
    index = 0,
    label = "s2_5_6",
    group = 
"""
1 * C u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3   C u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   C u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7   C u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
8   C u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
9   C u0 {3,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "s2_5_6_ane",
    group = 
"""
1 * C u0 {2,S} {4,S} {5,S}
2   C u0 {1,S} {3,S} {6,S}
3   C u0 {2,S} {9,S}
4   C u0 {1,S} {8,S}
5   C u0 {1,S} {7,S}
6   C u0 {2,S} {7,S}
7   C u0 {5,S} {6,S}
8   C u0 {4,S} {9,S}
9   C u0 {3,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.91,-10.762,-9.241,-7.769,-5.56,-3.888,-1.388],'cal/(mol*K)'),
        H298 = (8.21,'kcal/mol'),
        S298 = (47.72,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
ring strain N. Vandewiele, S and cp modified by A. G. Vandeputte to match BMK/6-311G(2d,d,p) data
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
    index = 93,
    label = "s2_5_6_ene_0",
    group = 
"""
1 * C u0 {2,S} {3,S} {5,S}
2   C u0 {1,S} {4,D} {6,S}
3   C u0 {1,S} {7,S}
4   C u0 {2,D} {8,S}
5   C u0 {1,S} {9,S}
6   C u0 {2,S} {7,S}
7   C u0 {3,S} {6,S}
8   C u0 {4,S} {9,S}
9   C u0 {5,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.8,-9,-7.9,-6.5,-4.7,-3.4,-1.3],'cal/(mol*K)'),
        H298 = (9,'kcal/mol'),
        S298 = (47.04,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
A. G. Vandeputte CBS-QB3 isodesmic reaction, S and cp match B3LYP/cbsb7 data
""",
)

entry(
    index = 94,
    label = "s2_5_6_ene_1",
    group = 
"""
1 * C u0 {2,S} {4,S} {6,S}
2   C u0 {1,S} {3,S} {5,S}
3   C u0 {2,S} {8,D}
4   C u0 {1,S} {7,S}
5   C u0 {2,S} {7,S}
6   C u0 {1,S} {9,S}
7   C u0 {4,S} {5,S}
8   C u0 {3,D} {9,S}
9   C u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8,-7.6,-6.8,-5.7,-4.3,-3.3,-2.1],'cal/(mol*K)'),
        H298 = (9,'kcal/mol'),
        S298 = (45.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Copied from entry: 2.4.5.6.7.7a-hexahydro-1H-indene
""",
)

entry(
    index = 95,
    label = "s2_5_6_ene_m",
    group = 
"""
1 * C u0 {2,D} {5,S} {6,S}
2   C u0 {1,D} {3,S} {4,S}
3   C u0 {2,S} {8,S}
4   C u0 {2,S} {7,S}
5   C u0 {1,S} {7,S}
6   C u0 {1,S} {9,S}
7   C u0 {4,S} {5,S}
8   C u0 {3,S} {9,S}
9   C u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8,-7.6,-6.8,-5.7,-4.3,-3.3,-2.1],'cal/(mol*K)'),
        H298 = (9,'kcal/mol'),
        S298 = (45.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Copied from entry: 2.4.5.6.7.7a-hexahydro-1H-indene
""",
)

entry(
    index = 96,
    label = "s2_5_6_ene_2",
    group = 
"""
1 * C u0 {2,S} {5,S} {6,S}
2   C u0 {1,S} {3,S} {4,S}
3   C u0 {2,S} {7,S}
4   C u0 {2,S} {8,S}
5   C u0 {1,S} {7,S}
6   C u0 {1,S} {9,S}
7   C u0 {3,S} {5,S}
8   C u0 {4,S} {9,D}
9   C u0 {6,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8,-7.6,-6.8,-5.7,-4.3,-3.3,-2.1],'cal/(mol*K)'),
        H298 = (9,'kcal/mol'),
        S298 = (45.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Copied from entry: 2.4.5.6.7.7a-hexahydro-1H-indene
""",
)

entry(
    index = 97,
    label = "s2_5_6_ene_5",
    group = 
"""
1 * C u0 {2,S} {3,D} {6,S}
2   C u0 {1,S} {4,S} {5,S}
3   C u0 {1,D} {7,S}
4   C u0 {2,S} {9,S}
5   C u0 {2,S} {7,S}
6   C u0 {1,S} {8,S}
7   C u0 {3,S} {5,S}
8   C u0 {6,S} {9,S}
9   C u0 {4,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8,-7.6,-6.8,-5.7,-4.3,-3.3,-2.1],'cal/(mol*K)'),
        H298 = (9,'kcal/mol'),
        S298 = (45.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
ring strain 2.3.3a.4.5.6-hexahydro-1H-indene, S and cp modified by A. G. Vandeputte to match BMK/6-311G(2d,p) data
""",
)

entry(
    index = 98,
    label = "s2_5_6_ene_6",
    group = 
"""
1 * C u0 {2,S} {4,S} {6,S}
2   C u0 {1,S} {3,S} {5,S}
3   C u0 {2,S} {8,S}
4   C u0 {1,S} {7,S}
5   C u0 {2,S} {7,D}
6   C u0 {1,S} {9,S}
7   C u0 {4,S} {5,D}
8   C u0 {3,S} {9,S}
9   C u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8,-7.6,-6.8,-5.7,-4.3,-3.3,-2.1],'cal/(mol*K)'),
        H298 = (9,'kcal/mol'),
        S298 = (45.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Copied from entry: 2.4.5.6.7.7a-hexahydro-1H-indene
""",
)

entry(
    index = 0,
    label = "s2_5_6_diene",
    group = "OR{s2_5_6_diene_m_1, s2_5_6_diene_m_2, s2_5_6_diene_m_7, s2_5_6_diene_0_2, s2_5_6_diene_0_3, s2_5_6_diene_0_4, s2_5_6_diene_0_5, s2_5_6_diene_0_6, s2_5_6_diene_0_7, s2_5_6_diene_1_3, s2_5_6_diene_1_5, s2_5_6_diene_1_6, s2_5_6_diene_1_7, s2_5_6_diene_1_8, s2_5_6_diene_2_5, s2_5_6_diene_2_6, s2_5_6_diene_5_7, s2_5_6_diene_5_8}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "s2_5_6_diene_m_1",
    group = 
"""
1 * C u0 {2,D} {4,S} {6,S}
2   C u0 {1,D} {3,S} {5,S}
3   C u0 {2,S} {8,D}
4   C u0 {1,S} {7,S}
5   C u0 {2,S} {7,S}
6   C u0 {1,S} {9,S}
7   C u0 {4,S} {5,S}
8   C u0 {3,D} {9,S}
9   C u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8,-7.6,-6.8,-5.7,-4.3,-3.3,-2.1],'cal/(mol*K)'),
        H298 = (10.1,'kcal/mol'),
        S298 = (45.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Copied from entry: 2.3.3a.7a-tetrahydro-1H-indene
""",
)

entry(
    index = 100,
    label = "s2_5_6_diene_m_2",
    group = 
"""
1 * C u0 {2,D} {3,S} {6,S}
2   C u0 {1,D} {4,S} {5,S}
3   C u0 {1,S} {9,S}
4   C u0 {2,S} {8,S}
5   C u0 {2,S} {7,S}
6   C u0 {1,S} {7,S}
7   C u0 {5,S} {6,S}
8   C u0 {4,S} {9,D}
9   C u0 {3,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8,-7.6,-6.8,-5.7,-4.3,-3.3,-2.1],'cal/(mol*K)'),
        H298 = (10.1,'kcal/mol'),
        S298 = (45.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Copied from entry: 2.3.3a.7a-tetrahydro-1H-indene
""",
)

entry(
    index = 101,
    label = "s2_5_6_diene_m_7",
    group = 
"""
1 * C u0 {2,D} {3,S} {5,S}
2   C u0 {1,D} {4,S} {6,S}
3   C u0 {1,S} {8,S}
4   C u0 {2,S} {7,S}
5   C u0 {1,S} {7,D}
6   C u0 {2,S} {9,S}
7   C u0 {4,S} {5,D}
8   C u0 {3,S} {9,S}
9   C u0 {6,S} {8,S}
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
    label = "s2_5_6_diene_0_2",
    group = 
"""
1 * C u0 {2,S} {4,S} {6,D}
2   C u0 {1,S} {3,S} {5,S}
3   C u0 {2,S} {7,S}
4   C u0 {1,S} {7,S}
5   C u0 {2,S} {9,S}
6   C u0 {1,D} {8,S}
7   C u0 {3,S} {4,S}
8   C u0 {6,S} {9,D}
9   C u0 {5,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8,-7.6,-6.8,-5.7,-4.3,-3.3,-2.1],'cal/(mol*K)'),
        H298 = (10.1,'kcal/mol'),
        S298 = (45.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Copied from entry: 2.3.3a.7a-tetrahydro-1H-indene
""",
)

entry(
    index = 103,
    label = "s2_5_6_diene_0_3",
    group = 
"""
1 * C u0 {2,S} {3,S} {6,S}
2   C u0 {1,S} {4,D} {5,S}
3   C u0 {1,S} {8,D}
4   C u0 {2,D} {9,S}
5   C u0 {2,S} {7,S}
6   C u0 {1,S} {7,S}
7   C u0 {5,S} {6,S}
8   C u0 {3,D} {9,S}
9   C u0 {4,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8,-7.6,-6.8,-5.7,-4.3,-3.3,-2.1],'cal/(mol*K)'),
        H298 = (6.8,'kcal/mol'),
        S298 = (45.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
ring strain N. Vandewiele, S and cp taken from 2.4.5.6.7.7a-hexahydro-1H-indene
""",
)

entry(
    index = 104,
    label = "s2_5_6_diene_0_4",
    group = 
"""
1 * C u0 {2,S} {4,D} {5,S}
2   C u0 {1,S} {3,D} {6,S}
3   C u0 {2,D} {9,S}
4   C u0 {1,D} {8,S}
5   C u0 {1,S} {7,S}
6   C u0 {2,S} {7,S}
7   C u0 {5,S} {6,S}
8   C u0 {4,S} {9,S}
9   C u0 {3,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8,-7.6,-6.8,-5.7,-4.3,-3.3,-2.1],'cal/(mol*K)'),
        H298 = (10.1,'kcal/mol'),
        S298 = (45.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Copied from entry: 2.3.3a.7a-tetrahydro-1H-indene
""",
)

entry(
    index = 105,
    label = "s2_5_6_diene_0_5",
    group = 
"""
1 * C u0 {2,S} {4,S} {5,D}
2   C u0 {1,S} {3,D} {6,S}
3   C u0 {2,D} {8,S}
4   C u0 {1,S} {9,S}
5   C u0 {1,D} {7,S}
6   C u0 {2,S} {7,S}
7   C u0 {5,S} {6,S}
8   C u0 {3,S} {9,S}
9   C u0 {4,S} {8,S}
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
    label = "s2_5_6_diene_0_6",
    group = 
"""
1 * C u0 {2,S} {4,S} {6,S}
2   C u0 {1,S} {3,D} {5,S}
3   C u0 {2,D} {9,S}
4   C u0 {1,S} {8,S}
5   C u0 {2,S} {7,S}
6   C u0 {1,S} {7,D}
7   C u0 {5,S} {6,D}
8   C u0 {4,S} {9,S}
9   C u0 {3,S} {8,S}
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
    label = "s2_5_6_diene_0_7",
    group = 
"""
1 * C u0 {2,S} {3,S} {6,S}
2   C u0 {1,S} {4,S} {5,D}
3   C u0 {1,S} {7,S}
4   C u0 {2,S} {7,D}
5   C u0 {2,D} {8,S}
6   C u0 {1,S} {9,S}
7   C u0 {3,S} {4,D}
8   C u0 {5,S} {9,S}
9   C u0 {6,S} {8,S}
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
    label = "s2_5_6_diene_1_3",
    group = 
"""
1 * C u0 {2,S} {5,S} {6,S}
2   C u0 {1,S} {3,S} {4,S}
3   C u0 {2,S} {9,D}
4   C u0 {2,S} {7,S}
5   C u0 {1,S} {8,D}
6   C u0 {1,S} {7,S}
7   C u0 {4,S} {6,S}
8   C u0 {5,D} {9,S}
9   C u0 {3,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8,-7.6,-6.8,-5.7,-4.3,-3.3,-2.1],'cal/(mol*K)'),
        H298 = (10.1,'kcal/mol'),
        S298 = (45.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
ring strain N. Vandewiele, S and cp taken from 2.4.5.6.7.7a-hexahydro-1H-indene
""",
)

entry(
    index = 109,
    label = "s2_5_6_diene_1_5",
    group = 
"""
1 * C u0 {2,S} {4,S} {5,S}
2   C u0 {1,S} {3,D} {6,S}
3   C u0 {2,D} {7,S}
4   C u0 {1,S} {9,D}
5   C u0 {1,S} {7,S}
6   C u0 {2,S} {8,S}
7   C u0 {3,S} {5,S}
8   C u0 {6,S} {9,S}
9   C u0 {4,D} {8,S}
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
    label = "s2_5_6_diene_1_6",
    group = 
"""
1 * C u0 {2,S} {4,S} {6,S}
2   C u0 {1,S} {3,S} {5,S}
3   C u0 {2,S} {7,S}
4   C u0 {1,S} {7,D}
5   C u0 {2,S} {8,D}
6   C u0 {1,S} {9,S}
7   C u0 {3,S} {4,D}
8   C u0 {5,D} {9,S}
9   C u0 {6,S} {8,S}
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
    label = "s2_5_6_diene_1_7",
    group = 
"""
1 * C u0 {2,S} {4,S} {5,S}
2   C u0 {1,S} {3,S} {6,S}
3   C u0 {2,S} {8,S}
4   C u0 {1,S} {9,D}
5   C u0 {1,S} {7,D}
6   C u0 {2,S} {7,S}
7   C u0 {5,D} {6,S}
8   C u0 {3,S} {9,S}
9   C u0 {4,D} {8,S}
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
    label = "s2_5_6_diene_1_8",
    group = 
"""
1 * C u0 {2,S} {3,S} {6,S}
2   C u0 {1,S} {4,D} {5,S}
3   C u0 {1,S} {7,S}
4   C u0 {2,D} {7,S}
5   C u0 {2,S} {8,D}
6   C u0 {1,S} {9,S}
7   C u0 {3,S} {4,S}
8   C u0 {5,D} {9,S}
9   C u0 {6,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8,-7.6,-6.8,-5.7,-4.3,-3.3,-2.1],'cal/(mol*K)'),
        H298 = (10.1,'kcal/mol'),
        S298 = (45.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Copied from entry: 2.3.3a.7a-tetrahydro-1H-indene
""",
)

entry(
    index = 113,
    label = "s2_5_6_diene_2_5",
    group = 
"""
1 * C u0 {2,S} {5,S} {6,S}
2   C u0 {1,S} {3,S} {4,D}
3   C u0 {2,S} {9,S}
4   C u0 {2,D} {7,S}
5   C u0 {1,S} {8,S}
6   C u0 {1,S} {7,S}
7   C u0 {4,S} {6,S}
8   C u0 {5,S} {9,D}
9   C u0 {3,S} {8,D}
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
    label = "s2_5_6_diene_2_6",
    group = 
"""
1 * C u0 {2,S} {4,S} {5,S}
2   C u0 {1,S} {3,S} {6,S}
3   C u0 {2,S} {8,S}
4   C u0 {1,S} {7,S}
5   C u0 {1,S} {9,S}
6   C u0 {2,S} {7,D}
7   C u0 {4,S} {6,D}
8   C u0 {3,S} {9,D}
9   C u0 {5,S} {8,D}
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
    label = "s2_5_6_diene_5_7",
    group = 
"""
1 * C u0 {2,S} {3,S} {4,S}
2   C u0 {1,S} {5,S} {6,D}
3   C u0 {1,S} {7,D}
4   C u0 {1,S} {9,S}
5   C u0 {2,S} {8,S}
6   C u0 {2,D} {7,S}
7   C u0 {3,D} {6,S}
8   C u0 {5,S} {9,S}
9   C u0 {4,S} {8,S}
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
    label = "s2_5_6_diene_5_8",
    group = 
"""
1 * C u0 {2,S} {3,D} {5,S}
2   C u0 {1,S} {4,D} {6,S}
3   C u0 {1,D} {7,S}
4   C u0 {2,D} {7,S}
5   C u0 {1,S} {9,S}
6   C u0 {2,S} {8,S}
7   C u0 {3,S} {4,S}
8   C u0 {6,S} {9,S}
9   C u0 {5,S} {8,S}
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
    index = 0,
    label = "s2_5_6_triene",
    group = "OR{s2_5_6_triene_0_2_6, s2_5_6_triene_0_2_7, s2_5_6_triene_0_3_7, s2_5_6_triene_1_3_5, s2_5_6_triene_1_3_6, s2_5_6_triene_1_6_8, s2_5_6_triene_2_5_7, s2_5_6_triene_m_1_7, s2_5_6_triene_m_2_6}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "s2_5_6_triene_0_2_6",
    group = 
"""
1 * C u0 {2,S} {3,S} {6,D}
2   C u0 {1,S} {4,S} {5,S}
3   C u0 {1,S} {7,S}
4   C u0 {2,S} {8,S}
5   C u0 {2,S} {7,D}
6   C u0 {1,D} {9,S}
7   C u0 {3,S} {5,D}
8   C u0 {4,S} {9,D}
9   C u0 {6,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.68,-6.81,-6.56,-5.84,-4.8,-3.99,-3.4],'cal/(mol*K)'),
        H298 = (6.863,'kcal/mol'),
        S298 = (57.6932,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt21 from C10H11 library.
""",
)

entry(
    index = 99,
    label = "s2_5_6_triene_0_2_7",
    group = 
"""
1 * C u0 {2,S} {4,S} {5,S}
2   C u0 {1,S} {3,D} {6,S}
3   C u0 {2,D} {8,S}
4   C u0 {1,S} {9,S}
5   C u0 {1,S} {7,S}
6   C u0 {2,S} {7,D}
7   C u0 {5,S} {6,D}
8   C u0 {3,S} {9,D}
9   C u0 {4,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.07,-7.77333,-7.70333,-6.73333,-5.47333,-4.32333,-2.97333],'cal/(mol*K)','+|-',[3.26137,4.03866,3.95722,3.57416,2.7068,2.08753,1.35534]),
        H298 = (2.643,'kcal/mol','+|-',4.3516),
        S298 = (60.4632,'cal/(mol*K)','+|-',1.24756),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt21 from C10H11 library.
Fitted from species pdt27 from C10H11 library.
Fitted from species pdt32 from C10H11 library.
""",
)

entry(
    index = 99,
    label = "s2_5_6_triene_0_3_7",
    group = 
"""
1 * C u0 {2,S} {4,D} {5,S}
2   C u0 {1,S} {3,S} {6,S}
3   C u0 {2,S} {7,S}
4   C u0 {1,D} {8,S}
5   C u0 {1,S} {7,D}
6   C u0 {2,S} {9,D}
7   C u0 {3,S} {5,D}
8   C u0 {4,S} {9,S}
9   C u0 {6,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.91,-7.09,-6.83,-6.08,-4.95,-4.08,-3.42],'cal/(mol*K)'),
        H298 = (5.483,'kcal/mol'),
        S298 = (58.2132,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt32 from C10H11 library.
""",
)

entry(
    index = 99,
    label = "s2_5_6_triene_1_3_5",
    group = 
"""
1 * C u0 {2,S} {4,S} {6,S}
2   C u0 {1,S} {3,D} {5,S}
3   C u0 {2,D} {7,S}
4   C u0 {1,S} {7,S}
5   C u0 {2,S} {9,D}
6   C u0 {1,S} {8,D}
7   C u0 {3,S} {4,S}
8   C u0 {6,D} {9,S}
9   C u0 {5,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.9,-8.9,-8.26,-7.24,-5.57,-4.36,-2.74],'cal/(mol*K)'),
        H298 = (3.693,'kcal/mol'),
        S298 = (61.9332,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt32 from C10H11 library.
""",
)

entry(
    index = 99,
    label = "s2_5_6_triene_1_3_6",
    group = 
"""
1 * C u0 {2,S} {3,S} {6,S}
2   C u0 {1,S} {4,S} {5,S}
3   C u0 {1,S} {7,S}
4   C u0 {2,S} {8,D}
5   C u0 {2,S} {7,D}
6   C u0 {1,S} {9,D}
7   C u0 {3,S} {5,D}
8   C u0 {4,D} {9,S}
9   C u0 {6,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.78,-6.1,-4.92,-3.65,-2.41,-1.62,-0.77],'cal/(mol*K)'),
        H298 = (-15.727,'kcal/mol'),
        S298 = (49.8332,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt32 from C10H11 library.
""",
)

entry(
    index = 99,
    label = "s2_5_6_triene_1_6_8",
    group = 
"""
1 * C u0 {2,S} {3,S} {5,S}
2   C u0 {1,S} {4,D} {6,S}
3   C u0 {1,S} {8,S}
4   C u0 {2,D} {7,S}
5   C u0 {1,S} {7,D}
6   C u0 {2,S} {9,D}
7   C u0 {4,S} {5,D}
8   C u0 {3,S} {9,S}
9   C u0 {6,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.67,-8.62,-7.99,-7,-5.42,-4.27,-2.72],'cal/(mol*K)'),
        H298 = (2.023,'kcal/mol'),
        S298 = (61.7232,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt21 from C10H11 library.
""",
)

entry(
    index = 99,
    label = "s2_5_6_triene_2_5_7",
    group = 
"""
1 * C u0 {2,S} {3,S} {4,S}
2   C u0 {1,S} {5,D} {6,S}
3   C u0 {1,S} {9,S}
4   C u0 {1,S} {7,D}
5   C u0 {2,D} {7,S}
6   C u0 {2,S} {8,S}
7   C u0 {4,D} {5,S}
8   C u0 {6,S} {9,D}
9   C u0 {3,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.68,-6.81,-6.56,-5.84,-4.8,-3.99,-3.4],'cal/(mol*K)'),
        H298 = (6.863,'kcal/mol'),
        S298 = (57.6932,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt21 from C10H11 library.
""",
)

entry(
    index = 99,
    label = "s2_5_6_triene_m_1_7",
    group = 
"""
1 * C u0 {2,D} {3,S} {6,S}
2   C u0 {1,D} {4,S} {5,S}
3   C u0 {1,S} {9,D}
4   C u0 {2,S} {8,S}
5   C u0 {2,S} {7,S}
6   C u0 {1,S} {7,D}
7   C u0 {5,S} {6,D}
8   C u0 {4,S} {9,S}
9   C u0 {3,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.57,-4.83,-4.71,-4.26,-4,-3.54,-3.01],'cal/(mol*K)'),
        H298 = (-2.777,'kcal/mol'),
        S298 = (59.5532,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt27 from C10H11 library.
""",
)

entry(
    index = 99,
    label = "s2_5_6_triene_m_2_6",
    group = 
"""
1 * C u0 {2,D} {3,S} {5,S}
2   C u0 {1,D} {4,S} {6,S}
3   C u0 {1,S} {7,D}
4   C u0 {2,S} {8,S}
5   C u0 {1,S} {9,S}
6   C u0 {2,S} {7,S}
7   C u0 {3,D} {6,S}
8   C u0 {4,S} {9,D}
9   C u0 {5,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.88,-7.18,-6.81,-6.07,-4.85,-4.06,-3.25],'cal/(mol*K)'),
        H298 = (6.883,'kcal/mol'),
        S298 = (58.0732,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt27 from C10H11 library.
""",
)

entry(
    index = 0,
    label = "s2_5_6_tetraene",
    group = "OR{s2_5_6_tetraene_1_3_5_7, s2_5_6_tetraene_1_3_5_8}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "s2_5_6_tetraene_1_3_5_7",
    group = 
"""
1 * C u0 {2,S} {4,S} {5,D}
2   C u0 {1,S} {3,S} {6,S}
3   C u0 {2,S} {8,D}
4   C u0 {1,S} {9,D}
5   C u0 {1,D} {7,S}
6   C u0 {2,S} {7,D}
7   C u0 {5,S} {6,D}
8   C u0 {3,D} {9,S}
9   C u0 {4,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.63,-9.81,-9.04,-7.82,-5.95,-4.71,-3.23],'cal/(mol*K)'),
        H298 = (14.05,'kcal/mol'),
        S298 = (60.39,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt22 from C10H11 library.
""",
)

entry(
    index = 99,
    label = "s2_5_6_tetraene_1_3_5_8",
    group = 
"""
1 * C u0 {2,S} {5,S} {6,D}
2   C u0 {1,S} {3,S} {4,D}
3   C u0 {2,S} {8,D}
4   C u0 {2,D} {7,S}
5   C u0 {1,S} {9,D}
6   C u0 {1,D} {7,S}
7   C u0 {4,S} {6,S}
8   C u0 {3,D} {9,S}
9   C u0 {5,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.49,-4.75,-4.62,-4.45,-4.55,-4.28,-4.48],'cal/(mol*K)'),
        H298 = (-0.61,'kcal/mol'),
        S298 = (58.88,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species 2HINDENE from C10H11 library.
""",
)

entry(
    index = 184,
    label = "s2_5_6_ben",
    group = 
"""
1 * C u0 {2,B} {3,S} {5,B}
2   C u0 {1,B} {4,S} {6,B}
3   C u0 {1,S} {7,S}
4   C u0 {2,S} {7,S}
5   C u0 {1,B} {9,B}
6   C u0 {2,B} {8,B}
7   C u0 {3,S} {4,S}
8   C u0 {6,B} {9,B}
9   C u0 {5,B} {8,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.23,-5.21,-4.3,-2.86,-0.88,-0.71,1.4],'cal/(mol*K)'),
        H298 = (5.54,'kcal/mol'),
        S298 = (25.35,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Verevkin (2011), experimental, S and cp from PM7
""",
)

entry(
    index = 117,
    label = "s2_5_6_indene",
    group = 
"""
1 * C u0 {2,B} {3,S} {4,B}
2   C u0 {1,B} {5,S} {6,B}
3   C u0 {1,S} {7,S}
4   C u0 {1,B} {8,B}
5   C u0 {2,S} {7,D}
6   C u0 {2,B} {9,B}
7   C u0 {3,S} {5,D}
8   C u0 {4,B} {9,B}
9   C u0 {6,B} {8,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.88,-4.29,-3.89,-2.96,-1.83,-2.2,-1.31],'cal/(mol*K)'),
        H298 = (2.1,'kcal/mol'),
        S298 = (33.08,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Verevkin (2011), experimental, S and cp from PM7
""",
)

entry(
    index = 0,
    label = "s2_5_7",
    group = 
"""
1  * C u0 {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2    C u0 {1,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
3    C u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
4    C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
5    C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6    C u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
7    C u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
8    C u0 {4,[S,D,T,B]} {10,[S,D,T,B]}
9    C u0 {3,[S,D,T,B]} {10,[S,D,T,B]}
10   C u0 {8,[S,D,T,B]} {9,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 0,
    label = "s2_5_7_triene",
    group = "OR{s2_5_7_triene_0_2_8, s2_5_7_triene_0_3_8, s2_5_7_triene_1_3_7, s2_5_7_triene_1_3_8, s2_5_7_triene_1_3_9, s2_5_7_triene_1_4_7}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "s2_5_7_triene_0_2_8",
    group = 
"""
1  * C u0 {2,S} {4,D} {6,S}
2    C u0 {1,S} {3,S} {5,S}
3    C u0 {2,S} {7,S}
4    C u0 {1,D} {8,S}
5    C u0 {2,S} {9,S}
6    C u0 {1,S} {7,D}
7    C u0 {3,S} {6,D}
8    C u0 {4,S} {10,D}
9    C u0 {5,S} {10,S}
10   C u0 {8,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.56,-9.04,-8.6,-7.5,-5.91,-4.62,-2.75],'cal/(mol*K)'),
        H298 = (0.693,'kcal/mol'),
        S298 = (56.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt29 from C10H11 library.
""",
)

entry(
    index = 118,
    label = "s2_5_7_triene_0_3_8",
    group = 
"""
1  * C u0 {2,S} {5,S} {6,S}
2    C u0 {1,S} {3,D} {4,S}
3    C u0 {2,D} {8,S}
4    C u0 {2,S} {7,D}
5    C u0 {1,S} {9,S}
6    C u0 {1,S} {7,S}
7    C u0 {4,D} {6,S}
8    C u0 {3,S} {10,S}
9    C u0 {5,S} {10,D}
10   C u0 {8,S} {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.57,-7.23,-7.07,-6.34,-5.29,-4.34,-3.43],'cal/(mol*K)'),
        H298 = (6.033,'kcal/mol'),
        S298 = (53.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt29 from C10H11 library.
""",
)

entry(
    index = 118,
    label = "s2_5_7_triene_1_3_7",
    group = 
"""
1  * C u0 {2,S} {3,S} {4,S}
2    C u0 {1,S} {5,S} {6,S}
3    C u0 {1,S} {7,D}
4    C u0 {1,S} {9,S}
5    C u0 {2,S} {7,S}
6    C u0 {2,S} {8,D}
7    C u0 {3,D} {5,S}
8    C u0 {6,D} {10,S}
9    C u0 {4,S} {10,D}
10   C u0 {8,S} {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.535,-6.635,-6.36,-5.495,-4.605,-3.68,-2.31],'cal/(mol*K)','+|-',[3.13605,3.13605,2.84019,2.426,1.71595,1.18341,0.473366]),
        H298 = (13.728,'kcal/mol','+|-',10.9884),
        S298 = (54.235,'cal/(mol*K)','+|-',0.296985),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt8 from C10H11 library.
Fitted from species pdt23 from C10H11 library.
""",
)

entry(
    index = 118,
    label = "s2_5_7_triene_1_3_8",
    group = 
"""
1  * C u0 {2,S} {3,S} {6,S}
2    C u0 {1,S} {4,S} {5,S}
3    C u0 {1,S} {7,D}
4    C u0 {2,S} {9,S}
5    C u0 {2,S} {7,S}
6    C u0 {1,S} {8,D}
7    C u0 {3,D} {5,S}
8    C u0 {6,D} {10,S}
9    C u0 {4,S} {10,D}
10   C u0 {8,S} {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.3425,-7.0575,-5.85,-4.7975,-3.47,-2.58,-1.35],'cal/(mol*K)','+|-',[4.00405,3.66182,6.7465,8.34184,9.49513,9.23012,7.85553]),
        H298 = (6.758,'kcal/mol','+|-',29.8859),
        S298 = (51.8325,'cal/(mol*K)','+|-',9.6992),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt8 from C10H11 library.
Fitted from species pdt23 from C10H11 library.
Fitted from species pdt28 from C10H11 library.
Fitted from species pdt29 from C10H11 library.
""",
)

entry(
    index = 118,
    label = "s2_5_7_triene_1_3_9",
    group = 
"""
1  * C u0 {2,S} {3,S} {6,S}
2    C u0 {1,S} {4,S} {5,D}
3    C u0 {1,S} {8,S}
4    C u0 {2,S} {9,D}
5    C u0 {2,D} {7,S}
6    C u0 {1,S} {7,S}
7    C u0 {5,S} {6,S}
8    C u0 {3,S} {10,D}
9    C u0 {4,D} {10,S}
10   C u0 {8,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.56,-9.04,-8.6,-7.5,-5.91,-4.62,-2.75],'cal/(mol*K)'),
        H298 = (3.993,'kcal/mol'),
        S298 = (56.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt29 from C10H11 library.
""",
)

entry(
    index = 118,
    label = "s2_5_7_triene_1_4_7",
    group = 
"""
1  * C u0 {2,S} {4,S} {6,S}
2    C u0 {1,S} {3,S} {5,S}
3    C u0 {2,S} {7,S}
4    C u0 {1,S} {7,D}
5    C u0 {2,S} {8,D}
6    C u0 {1,S} {9,D}
7    C u0 {3,S} {4,D}
8    C u0 {5,D} {10,S}
9    C u0 {6,D} {10,S}
10   C u0 {8,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.31,-5.81,-5.33,-4.69,-3.97,-3.35,-2.88],'cal/(mol*K)'),
        H298 = (14.973,'kcal/mol'),
        S298 = (52.13,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt8 from C10H11 library.
""",
)

entry(
    index = 0,
    label = "s2_5_7_tetraene",
    group = "OR{s2_5_7_tetraene_0_2_4_8, s2_5_7_tetraene_1_3_7_9, s2_5_7_tetraene_m_1_3_8}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "s2_5_7_tetraene_0_2_4_8",
    group = 
"""
1  * C u0 {2,S} {4,S} {6,S}
2    C u0 {1,S} {3,D} {5,S}
3    C u0 {2,D} {9,S}
4    C u0 {1,S} {8,D}
5    C u0 {2,S} {7,D}
6    C u0 {1,S} {7,S}
7    C u0 {5,D} {6,S}
8    C u0 {4,D} {10,S}
9    C u0 {3,S} {10,D}
10   C u0 {8,S} {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.94,-11.19,-10.38,-8.99,-6.63,-5,-2.79],'cal/(mol*K)'),
        H298 = (11.73,'kcal/mol'),
        S298 = (57.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt31 from C10H11 library.
""",
)

entry(
    index = 118,
    label = "s2_5_7_tetraene_1_3_7_9",
    group = 
"""
1  * C u0 {2,S} {3,S} {5,S}
2    C u0 {1,S} {4,S} {6,D}
3    C u0 {1,S} {8,S}
4    C u0 {2,S} {9,D}
5    C u0 {1,S} {7,D}
6    C u0 {2,D} {7,S}
7    C u0 {5,D} {6,S}
8    C u0 {3,S} {10,D}
9    C u0 {4,D} {10,S}
10   C u0 {8,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.84,-11.12,-10.33,-8.95,-6.62,-4.99,-2.8],'cal/(mol*K)'),
        H298 = (14.29,'kcal/mol'),
        S298 = (58.23,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt30 from C10H11 library.
""",
)

entry(
    index = 118,
    label = "s2_5_7_tetraene_m_1_3_8",
    group = 
"""
1  * C u0 {2,D} {3,S} {6,S}
2    C u0 {1,D} {4,S} {5,S}
3    C u0 {1,S} {8,S}
4    C u0 {2,S} {9,D}
5    C u0 {2,S} {7,D}
6    C u0 {1,S} {7,S}
7    C u0 {5,D} {6,S}
8    C u0 {3,S} {10,D}
9    C u0 {4,D} {10,S}
10   C u0 {8,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.52,-7.11,-6.7,-5.92,-4.93,-4.1,-2.95],'cal/(mol*K)'),
        H298 = (8.12,'kcal/mol'),
        S298 = (54.6,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt35 from C10H11 library.
""",
)

entry(
    index = 0,
    label = "s2_6_6",
    group = 
"""
1    C u0 {2,[S,D,T,B]} {3,[S,D,T,B]} {6,[S,D,T,B]}
2    C u0 {1,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3    C u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
4    C u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
5    C u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6    C u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
7  * C u0 {4,[S,D,T,B]} {9,[S,D,T,B]}
8    C u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
9    C u0 {3,[S,D,T,B]} {7,[S,D,T,B]}
10   C u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "s2_6_6_ane",
    group = 
"""
1    C u0 {2,S} {3,S} {6,S}
2    C u0 {1,S} {4,S} {5,S}
3    C u0 {1,S} {9,S}
4    C u0 {2,S} {7,S}
5    C u0 {2,S} {8,S}
6    C u0 {1,S} {10,S}
7  * C u0 {4,S} {9,S}
8    C u0 {5,S} {10,S}
9    C u0 {3,S} {7,S}
10   C u0 {6,S} {8,S}
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
    index = 119,
    label = "s2_6_6_ene_0",
    group = 
"""
1    C u0 {2,S} {3,S} {5,S}
2    C u0 {1,S} {4,D} {6,S}
3    C u0 {1,S} {7,S}
4    C u0 {2,D} {8,S}
5    C u0 {1,S} {10,S}
6    C u0 {2,S} {9,S}
7  * C u0 {3,S} {8,S}
8    C u0 {4,S} {7,S}
9    C u0 {6,S} {10,S}
10   C u0 {5,S} {9,S}
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
    label = "s2_6_6_ene_1",
    group = 
"""
1    C u0 {2,S} {3,S} {5,S}
2    C u0 {1,S} {4,S} {6,S}
3    C u0 {1,S} {9,D}
4    C u0 {2,S} {7,S}
5    C u0 {1,S} {10,S}
6    C u0 {2,S} {8,S}
7  * C u0 {4,S} {10,S}
8    C u0 {6,S} {9,S}
9    C u0 {3,D} {8,S}
10   C u0 {5,S} {7,S}
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
    label = "s2_6_6_ene_2",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S}
2    C u0 {1,S} {5,S} {6,S}
3    C u0 {1,S} {10,S}
4    C u0 {1,S} {7,S}
5    C u0 {2,S} {8,S}
6    C u0 {2,S} {9,S}
7  * C u0 {4,S} {8,S}
8    C u0 {5,S} {7,S}
9    C u0 {6,S} {10,D}
10   C u0 {3,S} {9,D}
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
    label = "s2_6_6_ene_m",
    group = 
"""
1    C u0 {2,D} {5,S} {6,S}
2    C u0 {1,D} {3,S} {4,S}
3    C u0 {2,S} {7,S}
4    C u0 {2,S} {8,S}
5    C u0 {1,S} {10,S}
6    C u0 {1,S} {9,S}
7  * C u0 {3,S} {9,S}
8    C u0 {4,S} {10,S}
9    C u0 {6,S} {7,S}
10   C u0 {5,S} {8,S}
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
    index = 0,
    label = "s2_6_6_diene",
    group = "OR{s2_6_6_diene_m_1, s2_6_6_diene_m_2, s2_6_6_diene_0_2, s2_6_6_diene_0_3, s2_6_6_diene_0_4, s2_6_6_diene_0_5, s2_6_6_diene_0_6, s2_6_6_diene_0_7, s2_6_6_diene_0_8, s2_6_6_diene_1_3, s2_6_6_diene_1_6, s2_6_6_diene_1_7, s2_6_6_diene_1_8, s2_6_6_diene_2_7}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "s2_6_6_diene_m_1",
    group = 
"""
1    C u0 {2,D} {4,S} {6,S}
2    C u0 {1,D} {3,S} {5,S}
3    C u0 {2,S} {9,S}
4    C u0 {1,S} {8,S}
5    C u0 {2,S} {7,D}
6    C u0 {1,S} {10,S}
7  * C u0 {5,D} {8,S}
8    C u0 {4,S} {7,S}
9    C u0 {3,S} {10,S}
10   C u0 {6,S} {9,S}
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
    label = "s2_6_6_diene_m_2",
    group = 
"""
1    C u0 {2,D} {5,S} {6,S}
2    C u0 {1,D} {3,S} {4,S}
3    C u0 {2,S} {8,S}
4    C u0 {2,S} {10,S}
5    C u0 {1,S} {9,S}
6    C u0 {1,S} {7,S}
7  * C u0 {6,S} {10,S}
8    C u0 {3,S} {9,D}
9    C u0 {5,S} {8,D}
10   C u0 {4,S} {7,S}
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
    label = "s2_6_6_diene_0_2",
    group = 
"""
1    C u0 {2,S} {3,S} {5,S}
2    C u0 {1,S} {4,S} {6,D}
3    C u0 {1,S} {8,S}
4    C u0 {2,S} {10,S}
5    C u0 {1,S} {9,S}
6    C u0 {2,D} {7,S}
7  * C u0 {6,S} {8,D}
8    C u0 {3,S} {7,D}
9    C u0 {5,S} {10,S}
10   C u0 {4,S} {9,S}
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
    label = "s2_6_6_diene_0_3",
    group = 
"""
1    C u0 {2,S} {4,S} {6,D}
2    C u0 {1,S} {3,S} {5,S}
3    C u0 {2,S} {10,S}
4    C u0 {1,S} {9,S}
5    C u0 {2,S} {7,D}
6    C u0 {1,D} {8,S}
7  * C u0 {5,D} {8,S}
8    C u0 {6,S} {7,S}
9    C u0 {4,S} {10,S}
10   C u0 {3,S} {9,S}
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
    label = "s2_6_6_diene_0_4",
    group = 
"""
1    C u0 {2,S} {3,S} {5,D}
2    C u0 {1,S} {4,D} {6,S}
3    C u0 {1,S} {10,S}
4    C u0 {2,D} {8,S}
5    C u0 {1,D} {7,S}
6    C u0 {2,S} {9,S}
7  * C u0 {5,S} {8,S}
8    C u0 {4,S} {7,S}
9    C u0 {6,S} {10,S}
10   C u0 {3,S} {9,S}
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
    label = "s2_6_6_diene_0_5",
    group = 
"""
1    C u0 {2,S} {3,S} {5,D}
2    C u0 {1,S} {4,D} {6,S}
3    C u0 {1,S} {9,S}
4    C u0 {2,D} {7,S}
5    C u0 {1,D} {10,S}
6    C u0 {2,S} {8,S}
7  * C u0 {4,S} {9,S}
8    C u0 {6,S} {10,S}
9    C u0 {3,S} {7,S}
10   C u0 {5,S} {8,S}
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
    label = "s2_6_6_diene_0_6",
    group = 
"""
1    C u0 {2,S} {5,S} {6,D}
2    C u0 {1,S} {3,S} {4,S}
3    C u0 {2,S} {10,S}
4    C u0 {2,S} {9,D}
5    C u0 {1,S} {8,S}
6    C u0 {1,D} {7,S}
7  * C u0 {6,S} {10,S}
8    C u0 {5,S} {9,S}
9    C u0 {4,D} {8,S}
10   C u0 {3,S} {7,S}
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
    label = "s2_6_6_diene_0_7",
    group = 
"""
1    C u0 {2,S} {4,S} {6,D}
2    C u0 {1,S} {3,S} {5,S}
3    C u0 {2,S} {8,S}
4    C u0 {1,S} {9,S}
5    C u0 {2,S} {10,S}
6    C u0 {1,D} {7,S}
7  * C u0 {6,S} {10,S}
8    C u0 {3,S} {9,D}
9    C u0 {4,S} {8,D}
10   C u0 {5,S} {7,S}
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
    label = "s2_6_6_diene_0_8",
    group = 
"""
1    C u0 {2,S} {4,S} {6,D}
2    C u0 {1,S} {3,S} {5,S}
3    C u0 {2,S} {9,S}
4    C u0 {1,S} {10,D}
5    C u0 {2,S} {8,S}
6    C u0 {1,D} {7,S}
7  * C u0 {6,S} {8,S}
8    C u0 {5,S} {7,S}
9    C u0 {3,S} {10,S}
10   C u0 {4,D} {9,S}
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
    label = "s2_6_6_diene_1_3",
    group = 
"""
1    C u0 {2,S} {5,S} {6,S}
2    C u0 {1,S} {3,S} {4,S}
3    C u0 {2,S} {7,D}
4    C u0 {2,S} {8,S}
5    C u0 {1,S} {10,S}
6    C u0 {1,S} {9,D}
7  * C u0 {3,D} {9,S}
8    C u0 {4,S} {10,S}
9    C u0 {6,D} {7,S}
10   C u0 {5,S} {8,S}
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
    label = "s2_6_6_diene_1_6",
    group = 
"""
1    C u0 {2,S} {5,S} {6,S}
2    C u0 {1,S} {3,S} {4,S}
3    C u0 {2,S} {10,S}
4    C u0 {2,S} {8,D}
5    C u0 {1,S} {9,S}
6    C u0 {1,S} {7,D}
7  * C u0 {6,D} {10,S}
8    C u0 {4,D} {9,S}
9    C u0 {5,S} {8,S}
10   C u0 {3,S} {7,S}
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
    label = "s2_6_6_diene_1_7",
    group = 
"""
1    C u0 {2,S} {4,S} {6,S}
2    C u0 {1,S} {3,S} {5,S}
3    C u0 {2,S} {10,S}
4    C u0 {1,S} {7,S}
5    C u0 {2,S} {8,D}
6    C u0 {1,S} {9,S}
7  * C u0 {4,S} {10,D}
8    C u0 {5,D} {9,S}
9    C u0 {6,S} {8,S}
10   C u0 {3,S} {7,D}
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
    label = "s2_6_6_diene_1_8",
    group = 
"""
1    C u0 {2,S} {4,S} {5,S}
2    C u0 {1,S} {3,S} {6,S}
3    C u0 {2,S} {7,S}
4    C u0 {1,S} {10,D}
5    C u0 {1,S} {8,D}
6    C u0 {2,S} {9,S}
7  * C u0 {3,S} {8,S}
8    C u0 {5,D} {7,S}
9    C u0 {6,S} {10,S}
10   C u0 {4,D} {9,S}
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
    label = "s2_6_6_diene_2_7",
    group = 
"""
1    C u0 {2,S} {4,S} {6,S}
2    C u0 {1,S} {3,S} {5,S}
3    C u0 {2,S} {8,S}
4    C u0 {1,S} {9,S}
5    C u0 {2,S} {7,S}
6    C u0 {1,S} {10,S}
7  * C u0 {5,S} {9,D}
8    C u0 {3,S} {10,D}
9    C u0 {4,S} {7,D}
10   C u0 {6,S} {8,D}
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
    index = 0,
    label = "s2_6_6_triene",
    group = "OR{s2_6_6_triene_0_2_6, s2_6_6_triene_0_2_7, s2_6_6_triene_0_3_7, s2_6_6_triene_1_3_6, s2_6_6_triene_1_3_7}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "s2_6_6_triene_0_2_6",
    group = 
"""
1    C u0 {2,S} {4,S} {6,S}
2    C u0 {1,S} {3,S} {5,D}
3    C u0 {2,S} {10,S}
4    C u0 {1,S} {7,D}
5    C u0 {2,D} {8,S}
6    C u0 {1,S} {9,S}
7  * C u0 {4,D} {10,S}
8    C u0 {5,S} {9,D}
9    C u0 {6,S} {8,D}
10   C u0 {3,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.27,-7.7,-6.87,-5.9,-4.53,-3.57,-2.03],'cal/(mol*K)'),
        H298 = (7.693,'kcal/mol'),
        S298 = (54.74,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt19 from C10H11 library.
""",
)

entry(
    index = 123,
    label = "s2_6_6_triene_0_2_7",
    group = 
"""
1    C u0 {2,S} {4,S} {6,S}
2    C u0 {1,S} {3,D} {5,S}
3    C u0 {2,D} {7,S}
4    C u0 {1,S} {9,S}
5    C u0 {2,S} {8,S}
6    C u0 {1,S} {10,S}
7  * C u0 {3,S} {9,D}
8    C u0 {5,S} {10,D}
9    C u0 {4,S} {7,D}
10   C u0 {6,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.98,-7.21,-6.77,-5.84,-4.695,-3.755,-2.135],'cal/(mol*K)','+|-',[2.95853,2.36683,1.77512,1.4201,0.88756,0.650878,0.295853]),
        H298 = (2.333,'kcal/mol','+|-',14.9058),
        S298 = (51.955,'cal/(mol*K)','+|-',2.95571),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt19 from C10H11 library.
Fitted from species pdt37 from C10H11 library.
""",
)

entry(
    index = 123,
    label = "s2_6_6_triene_0_3_7",
    group = 
"""
1    C u0 {2,S} {4,D} {6,S}
2    C u0 {1,S} {3,S} {5,S}
3    C u0 {2,S} {10,D}
4    C u0 {1,D} {7,S}
5    C u0 {2,S} {8,S}
6    C u0 {1,S} {9,S}
7  * C u0 {4,S} {10,S}
8    C u0 {5,S} {9,D}
9    C u0 {6,S} {8,D}
10   C u0 {3,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.74,-6.32,-5.65,-4.95,-3.99,-3.38,-2.69],'cal/(mol*K)'),
        H298 = (2.193,'kcal/mol'),
        S298 = (48.91,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt37 from C10H11 library.
""",
)

entry(
    index = 123,
    label = "s2_6_6_triene_1_3_6",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S}
2    C u0 {1,S} {5,S} {6,S}
3    C u0 {1,S} {9,S}
4    C u0 {1,S} {10,D}
5    C u0 {2,S} {8,D}
6    C u0 {2,S} {7,D}
7  * C u0 {6,D} {9,S}
8    C u0 {5,D} {10,S}
9    C u0 {3,S} {7,S}
10   C u0 {4,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.91,-7.26,-6.54,-5.57,-4.35,-3.43,-2.07],'cal/(mol*K)'),
        H298 = (7.733,'kcal/mol'),
        S298 = (54.59,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt10bis from C10H11 library.
""",
)

entry(
    index = 123,
    label = "s2_6_6_triene_1_3_7",
    group = 
"""
1    C u0 {2,S} {4,S} {6,S}
2    C u0 {1,S} {3,S} {5,S}
3    C u0 {2,S} {7,S}
4    C u0 {1,S} {8,S}
5    C u0 {2,S} {10,D}
6    C u0 {1,S} {9,D}
7  * C u0 {3,S} {8,D}
8    C u0 {4,S} {7,D}
9    C u0 {6,D} {10,S}
10   C u0 {5,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.455,-6.46,-6.15,-5.28,-4.38,-3.47,-2.41],'cal/(mol*K)','+|-',[0.532536,0.946731,1.53844,1.65678,1.53844,1.30176,2.24849]),
        H298 = (3.073,'kcal/mol','+|-',13.7744),
        S298 = (52.44,'cal/(mol*K)','+|-',1.21622),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt10bis from C10H11 library.
Fitted from species pdt37 from C10H11 library.
""",
)

entry(
    index = 0,
    label = "s2_6_6_tetraene",
    group = "OR{s2_6_6_tetraene_0_2_4_7, s2_6_6_tetraene_0_2_5_7, s2_6_6_tetraene_0_2_6_8, s2_6_6_tetraene_0_3_6_8, s2_6_6_tetraene_1_3_6_8}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "s2_6_6_tetraene_0_2_4_7",
    group = 
"""
1    C u0 {2,S} {3,S} {4,D}
2    C u0 {1,S} {5,D} {6,S}
3    C u0 {1,S} {8,S}
4    C u0 {1,D} {7,S}
5    C u0 {2,D} {10,S}
6    C u0 {2,S} {9,S}
7  * C u0 {4,S} {10,D}
8    C u0 {3,S} {9,D}
9    C u0 {6,S} {8,D}
10   C u0 {5,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.4,-11.67,-11.09,-9.63,-7.17,-5.47,-2.85],'cal/(mol*K)'),
        H298 = (-17.82,'kcal/mol'),
        S298 = (53.93,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt38 from C10H11 library.
""",
)

entry(
    index = 123,
    label = "s2_6_6_tetraene_0_2_5_7",
    group = 
"""
1    C u0 {2,S} {3,D} {5,S}
2    C u0 {1,S} {4,S} {6,D}
3    C u0 {1,D} {8,S}
4    C u0 {2,S} {10,S}
5    C u0 {1,S} {9,S}
6    C u0 {2,D} {7,S}
7  * C u0 {6,S} {9,D}
8    C u0 {3,S} {10,D}
9    C u0 {5,S} {7,D}
10   C u0 {4,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.51,-10.83,-10.38,-9.04,-6.78,-5.2,-2.72],'cal/(mol*K)'),
        H298 = (10.33,'kcal/mol'),
        S298 = (53.47,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt26 from C10H11 library.
""",
)

entry(
    index = 123,
    label = "s2_6_6_tetraene_0_2_6_8",
    group = 
"""
1    C u0 {2,S} {3,S} {6,S}
2    C u0 {1,S} {4,D} {5,S}
3    C u0 {1,S} {8,D}
4    C u0 {2,D} {7,S}
5    C u0 {2,S} {10,D}
6    C u0 {1,S} {9,S}
7  * C u0 {4,S} {9,D}
8    C u0 {3,D} {10,S}
9    C u0 {6,S} {7,D}
10   C u0 {5,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.475,-10.72,-10,-8.715,-6.555,-5.06,-3.055],'cal/(mol*K)','+|-',[6.21292,6.62712,5.79873,4.4378,1.71595,0.355024,3.13605]),
        H298 = (1.5665,'kcal/mol','+|-',21.2797),
        S298 = (58.74,'cal/(mol*K)','+|-',4.18607),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt11 from C10H11 library.
Fitted from species prod4 from naphthalene_H library.
""",
)

entry(
    index = 123,
    label = "s2_6_6_tetraene_0_3_6_8",
    group = 
"""
1    C u0 {2,S} {5,D} {6,S}
2    C u0 {1,S} {3,S} {4,S}
3    C u0 {2,S} {8,D}
4    C u0 {2,S} {10,D}
5    C u0 {1,D} {7,S}
6    C u0 {1,S} {9,D}
7  * C u0 {5,S} {8,S}
8    C u0 {3,D} {7,S}
9    C u0 {6,D} {10,S}
10   C u0 {4,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.57,-7.86,-7.37,-6.54,-5.25,-4.39,-3.88],'cal/(mol*K)'),
        H298 = (-1.957,'kcal/mol'),
        S298 = (55.67,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species prod4 from naphthalene_H library.
""",
)

entry(
    index = 123,
    label = "s2_6_6_tetraene_1_3_6_8",
    group = 
"""
1    C u0 {2,S} {3,S} {4,S}
2    C u0 {1,S} {5,S} {6,S}
3    C u0 {1,S} {8,D}
4    C u0 {1,S} {9,D}
5    C u0 {2,S} {10,D}
6    C u0 {2,S} {7,D}
7  * C u0 {6,D} {8,S}
8    C u0 {3,D} {7,S}
9    C u0 {4,D} {10,S}
10   C u0 {5,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.33,-8.08,-6.33,-4.9,-3.09,-2.2,-1.2],'cal/(mol*K)'),
        H298 = (-22.037,'kcal/mol'),
        S298 = (49.84,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species prod4 from naphthalene_H library.
""",
)

entry(
    index = 185,
    label = "s2_6_6_ben",
    group = 
"""
1    C u0 {2,B} {3,B} {5,S}
2    C u0 {1,B} {4,B} {6,S}
3    C u0 {1,B} {7,B}
4    C u0 {2,B} {9,B}
5    C u0 {1,S} {10,S}
6    C u0 {2,S} {8,S}
7  * C u0 {3,B} {9,B}
8    C u0 {6,S} {10,S}
9    C u0 {4,B} {7,B}
10   C u0 {5,S} {8,S}
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
    index = 0,
    label = "s2_6_6_ben_ene",
    group = "OR{s2_6_6_ben_ene_1, s2_6_6_ben_ene_2}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "s2_6_6_ben_ene_1",
    group = 
"""
1    C u0 {2,B} {3,S} {4,B}
2    C u0 {1,B} {5,B} {6,S}
3    C u0 {1,S} {7,D}
4    C u0 {1,B} {8,B}
5    C u0 {2,B} {9,B}
6    C u0 {2,S} {10,S}
7  * C u0 {3,D} {10,S}
8    C u0 {4,B} {9,B}
9    C u0 {5,B} {8,B}
10   C u0 {6,S} {7,S}
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
    label = "s2_6_6_ben_ene_2",
    group = 
"""
1    C u0 {2,B} {4,B} {5,S}
2    C u0 {1,B} {3,S} {6,B}
3    C u0 {2,S} {8,S}
4    C u0 {1,B} {10,B}
5    C u0 {1,S} {7,S}
6    C u0 {2,B} {9,B}
7  * C u0 {5,S} {8,D}
8    C u0 {3,S} {7,D}
9    C u0 {6,B} {10,B}
10   C u0 {4,B} {9,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.68,-1.73,-1.85,-1.91,-2.19,-2.39,-2.51],'cal/(mol*K)'),
        H298 = (2.84,'kcal/mol'),
        S298 = (35.91,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species pdt38 from C10H11 library.
""",
)

entry(
    index = 185,
    label = "s2_6_6_naphthalene",
    group = 
"""
1    C u0 {2,B} {3,B} {4,B}
2    C u0 {1,B} {5,B} {6,B}
3    C u0 {1,B} {9,B}
4    C u0 {1,B} {8,B}
5    C u0 {2,B} {10,B}
6    C u0 {2,B} {7,B}
7  * C u0 {6,B} {8,B}
8    C u0 {4,B} {7,B}
9    C u0 {3,B} {10,B}
10   C u0 {5,B} {9,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.79295e-15,0,-1.35859e-14,-6.79295e-15,0,1.35859e-14,-1.35859e-14],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (-2.75,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species naphthalene from naphthalene_H library.
""",
)

entry(
    index = 0,
    label = "s3_4_4",
    group = 
"""
1   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 * C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "s3_4_4_ane",
    group = 
"""
1   C u0 {3,S} {4,S} {5,S}
2   C u0 {3,S} {4,S} {5,S}
3 * C u0 {1,S} {2,S}
4   C u0 {1,S} {2,S}
5   C u0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.64,-6.32,-5.24,-3.91,-2.78,-3.31,-2.12],'cal/(mol*K)'),
        H298 = (68,'kcal/mol'),
        S298 = (62.36,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Wiberg, K. Angew. Chem., Int. Ed. Engl. 1986, 25, 312 1986 ab initio S, Cp from PM7 calculation
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
    index = 138,
    label = "s3_4_4_ene_0",
    group = 
"""
1   C u0 {3,S} {4,S} {5,D}
2   C u0 {3,S} {4,S} {5,S}
3 * C u0 {1,S} {2,S}
4   C u0 {1,S} {2,S}
5   C u0 {1,D} {2,S}
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
    index = 139,
    label = "s3_4_4_diene_0_2",
    group = 
"""
1   C u0 {3,S} {4,S} {5,D}
2   C u0 {3,D} {4,S} {5,S}
3 * C u0 {1,S} {2,D}
4   C u0 {1,S} {2,S}
5   C u0 {1,D} {2,S}
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
    index = 0,
    label = "s3_4_5",
    group = 
"""
1   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
2   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 * C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
5   C u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
6   C u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    label = "s3_4_5_ane",
    group = 
"""
1   C u0 {3,S} {4,S} {6,S}
2   C u0 {3,S} {4,S} {5,S}
3 * C u0 {1,S} {2,S}
4   C u0 {1,S} {2,S}
5   C u0 {2,S} {6,S}
6   C u0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.92,-8.22,-6.65,-4.79,-2.85,-3.09,-1.39],'cal/(mol*K)'),
        H298 = (37,'kcal/mol'),
        S298 = (57.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Wiberg, K. Angew. Chem., Int. Ed. Engl. 1986, 25, 312 1986 ab initio, S, Cp from PM7 calculation
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
    index = 141,
    label = "s3_4_5_ene_0",
    group = 
"""
1   C u0 {3,S} {4,S} {6,D}
2   C u0 {3,S} {4,S} {5,S}
3 * C u0 {1,S} {2,S}
4   C u0 {1,S} {2,S}
5   C u0 {2,S} {6,S}
6   C u0 {1,D} {5,S}
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
    label = "s3_4_5_ene_1",
    group = 
"""
1   C u0 {3,S} {4,S} {5,S}
2   C u0 {3,S} {4,S} {6,S}
3 * C u0 {1,S} {2,S}
4   C u0 {1,S} {2,S}
5   C u0 {1,S} {6,D}
6   C u0 {2,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.86,-6.73,-5.82,-4.2,-2.93,-3.36,-1.97],'cal/(mol*K)'),
        H298 = (51,'kcal/mol'),
        S298 = (58.93,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Wiberg, K. Angew. Chem., Int. Ed. Engl. 1986, 25, 312 1986 ab initio S, Cp from PM7 calculations
""",
)

entry(
    index = 143,
    label = "s3_4_5_ene_3",
    group = 
"""
1   C u0 {3,D} {4,S} {6,S}
2   C u0 {3,S} {4,S} {5,S}
3 * C u0 {1,D} {2,S}
4   C u0 {1,S} {2,S}
5   C u0 {2,S} {6,S}
6   C u0 {1,S} {5,S}
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
    index = 144,
    label = "s3_4_5_diene_0_2",
    group = 
"""
1   C u0 {3,S} {4,S} {6,D}
2   C u0 {3,S} {4,S} {5,D}
3 * C u0 {1,S} {2,S}
4   C u0 {1,S} {2,S}
5   C u0 {2,D} {6,S}
6   C u0 {1,D} {5,S}
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
    label = "s3_4_5_diene_0_3",
    group = 
"""
1   C u0 {3,S} {4,S} {6,D}
2   C u0 {3,S} {4,D} {5,S}
3 * C u0 {1,S} {2,S}
4   C u0 {1,S} {2,D}
5   C u0 {2,S} {6,S}
6   C u0 {1,D} {5,S}
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
    label = "s3_4_5_diene_1_3",
    group = 
"""
1   C u0 {3,S} {4,S} {5,S}
2   C u0 {3,D} {4,S} {6,S}
3 * C u0 {1,S} {2,D}
4   C u0 {1,S} {2,S}
5   C u0 {1,S} {6,D}
6   C u0 {2,S} {5,D}
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
    label = "s3_4_5_diene_3_4",
    group = 
"""
1   C u0 {3,D} {4,S} {5,S}
2   C u0 {3,S} {4,D} {6,S}
3 * C u0 {1,D} {2,S}
4   C u0 {1,S} {2,D}
5   C u0 {1,S} {6,S}
6   C u0 {2,S} {5,S}
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
    index = 0,
    label = "s3_4_6",
    group = 
"""
1   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
2   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3 * C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
5   C u0 {2,[S,D,T,B]} {7,[S,D,T,B]}
6   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
7   C u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "s3_4_6_ane",
    group = 
"""
1   C u0 {3,S} {4,S} {6,S}
2   C u0 {3,S} {4,S} {5,S}
3 * C u0 {1,S} {2,S}
4   C u0 {1,S} {2,S}
5   C u0 {2,S} {7,S}
6   C u0 {1,S} {7,S}
7   C u0 {5,S} {6,S}
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
    index = 149,
    label = "s3_4_6_ene_0",
    group = 
"""
1   C u0 {3,S} {4,S} {6,D}
2   C u0 {3,S} {4,S} {5,S}
3 * C u0 {1,S} {2,S}
4   C u0 {1,S} {2,S}
5   C u0 {2,S} {7,S}
6   C u0 {1,D} {7,S}
7   C u0 {5,S} {6,S}
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
    label = "s3_4_6_ene_1",
    group = 
"""
1   C u0 {3,S} {4,S} {6,S}
2   C u0 {3,S} {4,S} {5,S}
3 * C u0 {1,S} {2,S}
4   C u0 {1,S} {2,S}
5   C u0 {2,S} {7,S}
6   C u0 {1,S} {7,D}
7   C u0 {5,S} {6,D}
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
    label = "s3_4_6_ene_4",
    group = 
"""
1   C u0 {3,S} {4,S} {5,S}
2   C u0 {3,D} {4,S} {6,S}
3 * C u0 {1,S} {2,D}
4   C u0 {1,S} {2,S}
5   C u0 {1,S} {7,S}
6   C u0 {2,S} {7,S}
7   C u0 {5,S} {6,S}
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
    index = 152,
    label = "s3_4_6_diene_0_2",
    group = 
"""
1   C u0 {3,S} {4,S} {6,S}
2   C u0 {3,S} {4,S} {5,D}
3 * C u0 {1,S} {2,S}
4   C u0 {1,S} {2,S}
5   C u0 {2,D} {7,S}
6   C u0 {1,S} {7,D}
7   C u0 {5,S} {6,D}
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
    index = 153,
    label = "s3_4_6_diene_0_3",
    group = 
"""
1   C u0 {3,S} {4,S} {5,D}
2   C u0 {3,S} {4,S} {6,D}
3 * C u0 {1,S} {2,S}
4   C u0 {1,S} {2,S}
5   C u0 {1,D} {7,S}
6   C u0 {2,D} {7,S}
7   C u0 {5,S} {6,S}
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
    index = 154,
    label = "s3_4_6_diene_0_4",
    group = 
"""
1   C u0 {3,S} {4,D} {5,S}
2   C u0 {3,S} {4,S} {6,D}
3 * C u0 {1,S} {2,S}
4   C u0 {1,D} {2,S}
5   C u0 {1,S} {7,S}
6   C u0 {2,D} {7,S}
7   C u0 {5,S} {6,S}
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
    label = "s3_4_6_diene_1_4",
    group = 
"""
1   C u0 {3,S} {4,S} {5,S}
2   C u0 {3,D} {4,S} {6,S}
3 * C u0 {1,S} {2,D}
4   C u0 {1,S} {2,S}
5   C u0 {1,S} {7,D}
6   C u0 {2,S} {7,S}
7   C u0 {5,D} {6,S}
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
    index = 156,
    label = "s3_4_6_diene_1_5",
    group = 
"""
1   C u0 {3,S} {4,S} {5,S}
2   C u0 {3,D} {4,S} {6,S}
3 * C u0 {1,S} {2,D}
4   C u0 {1,S} {2,S}
5   C u0 {1,S} {7,S}
6   C u0 {2,S} {7,D}
7   C u0 {5,S} {6,D}
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
    index = 0,
    label = "s3_5_5",
    group = 
"""
1   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
2   C u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4 * C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
6   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
7   C u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 157,
    label = "s3_5_5_ane",
    group = 
"""
1   C u0 {3,S} {4,S} {5,S}
2   C u0 {3,S} {6,S} {7,S}
3   C u0 {1,S} {2,S}
4 * C u0 {1,S} {6,S}
5   C u0 {1,S} {7,S}
6   C u0 {2,S} {4,S}
7   C u0 {2,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (16.14,'kcal/mol'),
        S298 = (53.47,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
ring strain N. Vandewiele, S and cp modified by A. G. Vandeputte to match BMK/6-311G(2d,d,p) data
""",
)

entry(
    index = 0,
    label = "s3_5_5_ene",
    group = "OR{s3_5_5_ene_0, s3_5_5_ene_1, s3_5_5_ene_side, s3_5_5_ene_m}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 158,
    label = "s3_5_5_ene_0",
    group = 
"""
1   C u0 {3,S} {4,S} {6,D}
2   C u0 {3,S} {5,S} {7,S}
3   C u0 {1,S} {2,S}
4 * C u0 {1,S} {5,S}
5   C u0 {2,S} {4,S}
6   C u0 {1,D} {7,S}
7   C u0 {2,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.785,-6.005,-5.34,-4.815,-4.35,-3.915,-3.05],'cal/(mol*K)','+|-',[8.69809,7.63302,6.62712,5.8579,4.61531,3.60941,2.13015]),
        H298 = (71.868,'kcal/mol','+|-',63.5123),
        S298 = (58.32,'cal/(mol*K)','+|-',1.69706),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species product23 from vinylCPD_H library.
Fitted from species product29 from vinylCPD_H library.
""",
)

entry(
    index = 158,
    label = "s3_5_5_ene_1",
    group = 
"""
1   C u0 {3,S} {5,S} {6,S}
2   C u0 {3,S} {4,S} {7,S}
3   C u0 {1,S} {2,S}
4 * C u0 {2,S} {5,S}
5   C u0 {1,S} {4,S}
6   C u0 {1,S} {7,D}
7   C u0 {2,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.29,-7.302,-6.501,-5.499,-4.58,-3.778,-2.608],'cal/(mol*K)'),
        H298 = (17.8,'kcal/mol'),
        S298 = (53.75,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
A. G. Vandeputte CBS-QB3 isodesmic reaction, norbornene + 7 ethane -> 2-butene + 2 isobutane + 3 propane, experimental data from the NIST Chemical Webbook
""",
)

entry(
    index = 159,
    label = "s3_5_5_ene_side",
    group = 
"""
1   C u0 {3,S} {4,S} {6,S}
2   C u0 {4,S} {5,S} {7,S}
3 * C u0 {1,S} {5,S} {8,D}
4   C u0 {1,S} {2,S}
5   C u0 {2,S} {3,S}
6   C u0 {1,S} {7,S}
7   C u0 {2,S} {6,S}
8   R ux {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.27,-8.28,-7.29,-6.18,-4.88,-3.81,-2.22],'cal/(mol*K)'),
        H298 = (14.6,'kcal/mol'),
        S298 = (50.85,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
A.G. Vandeputte isodesmic reactions + B3LYP/cbsb7 S and cp, CHECK!
""",
)

entry(
    index = 159,
    label = "s3_5_5_ene_m",
    group = 
"""
1   C u0 {3,D} {5,S} {7,S}
2   C u0 {3,S} {4,S} {6,S}
3   C u0 {1,D} {2,S}
4 * C u0 {2,S} {7,S}
5   C u0 {1,S} {6,S}
6   C u0 {2,S} {5,S}
7   C u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.05,-5.36,-4.88,-4.32,-3.96,-3.61,-2.87],'cal/(mol*K)'),
        H298 = (94.073,'kcal/mol'),
        S298 = (58.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Fitted from species product29 from vinylCPD_H library.
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
    index = 160,
    label = "s3_5_5_diene_1_4",
    group = 
"""
1   C u0 {3,S} {6,S} {7,S}
2   C u0 {3,S} {4,S} {5,S}
3   C u0 {1,S} {2,S}
4 * C u0 {2,S} {6,D}
5   C u0 {2,S} {7,D}
6   C u0 {1,S} {4,D}
7   C u0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.88,-8.43,-6.65,-4.77,-2.79,-3.1,-1.54],'cal/(mol*K)'),
        H298 = (31.64,'kcal/mol'),
        S298 = (57.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Properties of Liquids and Gases, Poling 5th Ed. S, Cp from PM7 calculation
""",
)

entry(
    index = 0,
    label = "s3_5_6",
    group = 
"""
1   C u0 {3,[S,D,T,B]} {5,[S,D,T,B]} {6,[S,D,T,B]}
2   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {7,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
5   C u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
6   C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
7   C u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
8 * C u0 {6,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 161,
    label = "s3_5_6_ane",
    group = 
"""
1   C u0 {3,S} {5,S} {6,S}
2   C u0 {3,S} {4,S} {7,S}
3   C u0 {1,S} {2,S}
4   C u0 {2,S} {5,S}
5   C u0 {1,S} {4,S}
6   C u0 {1,S} {8,S}
7   C u0 {2,S} {8,S}
8 * C u0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.2,-9.9,-8.4,-7.1,-5.2,-3.8,-1.7],'cal/(mol*K)'),
        H298 = (8.5,'kcal/mol'),
        S298 = (48.66,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
A.G Vandeputte CBS-QB3, isodesmic reactions approach
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
    index = 162,
    label = "s3_5_6_ene_1",
    group = 
"""
1   C u0 {3,S} {4,S} {7,S}
2   C u0 {3,S} {5,S} {6,S}
3   C u0 {1,S} {2,S}
4   C u0 {1,S} {5,S}
5   C u0 {2,S} {4,S}
6   C u0 {2,S} {8,S}
7   C u0 {1,S} {8,D}
8 * C u0 {6,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.3,-8.3,-7.2,-6.1,-4.8,-3.6,-2],'cal/(mol*K)'),
        H298 = (8.5,'kcal/mol'),
        S298 = (48.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
A.G Vandeputte CBS-QB3, isodesmic reactions approach
""",
)

entry(
    index = 163,
    label = "s3_5_6_ene_5",
    group = 
"""
1   C u0 {3,S} {4,S} {7,S}
2   C u0 {3,S} {5,S} {6,S}
3   C u0 {1,S} {2,S}
4   C u0 {1,S} {5,D}
5   C u0 {2,S} {4,D}
6   C u0 {2,S} {8,S}
7   C u0 {1,S} {8,S}
8 * C u0 {6,S} {7,S}
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
    index = 164,
    label = "s3_5_6_diene_1_5",
    group = 
"""
1   C u0 {3,S} {4,S} {6,S}
2   C u0 {3,S} {5,S} {7,S}
3   C u0 {1,S} {2,S}
4   C u0 {1,S} {5,D}
5   C u0 {2,S} {4,D}
6   C u0 {1,S} {8,D}
7   C u0 {2,S} {8,S}
8 * C u0 {6,D} {7,S}
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
    index = 0,
    label = "s3_6_6",
    group = 
"""
1   C u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
2   C u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4 * C u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
5   C u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
6   C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
7   C u0 {1,[S,D,T,B]} {9,[S,D,T,B]}
8   C u0 {5,[S,D,T,B]} {6,[S,D,T,B]}
9   C u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 165,
    label = "s3_6_6_ane",
    group = 
"""
1   C u0 {3,S} {6,S} {7,S}
2   C u0 {3,S} {4,S} {5,S}
3   C u0 {1,S} {2,S}
4 * C u0 {2,S} {9,S}
5   C u0 {2,S} {8,S}
6   C u0 {1,S} {8,S}
7   C u0 {1,S} {9,S}
8   C u0 {5,S} {6,S}
9   C u0 {4,S} {7,S}
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
    index = 166,
    label = "s3_6_6_ene_0",
    group = 
"""
1   C u0 {3,S} {4,S} {7,S}
2   C u0 {3,S} {5,S} {6,D}
3   C u0 {1,S} {2,S}
4 * C u0 {1,S} {8,S}
5   C u0 {2,S} {8,S}
6   C u0 {2,D} {9,S}
7   C u0 {1,S} {9,S}
8   C u0 {4,S} {5,S}
9   C u0 {6,S} {7,S}
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
    label = "s3_6_6_ene_1",
    group = 
"""
1   C u0 {3,S} {4,S} {6,S}
2   C u0 {3,S} {5,S} {7,S}
3   C u0 {1,S} {2,S}
4 * C u0 {1,S} {9,S}
5   C u0 {2,S} {8,S}
6   C u0 {1,S} {8,D}
7   C u0 {2,S} {9,S}
8   C u0 {5,S} {6,D}
9   C u0 {4,S} {7,S}
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
    label = "s3_6_6_ene_4",
    group = 
"""
1   C u0 {3,D} {4,S} {6,S}
2   C u0 {3,S} {5,S} {7,S}
3   C u0 {1,D} {2,S}
4 * C u0 {1,S} {8,S}
5   C u0 {2,S} {9,S}
6   C u0 {1,S} {9,S}
7   C u0 {2,S} {8,S}
8   C u0 {4,S} {7,S}
9   C u0 {5,S} {6,S}
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
    index = 0,
    label = "s3_6_6_diene",
    group = "OR{s3_6_6_diene_0_m, s3_6_6_diene_0_2, s3_6_6_diene_0_3, s3_6_6_diene_0_4, s3_6_6_diene_0_5, s3_6_6_diene_0_6, s3_6_6_diene_1_m, s3_6_6_diene_1_5, s3_6_6_diene_1_6, s3_6_6_diene_1_8}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 169,
    label = "s3_6_6_diene_0_m",
    group = 
"""
1   C u0 {3,S} {4,D} {5,S}
2   C u0 {3,D} {6,S} {7,S}
3   C u0 {1,S} {2,D}
4 * C u0 {1,D} {9,S}
5   C u0 {1,S} {8,S}
6   C u0 {2,S} {9,S}
7   C u0 {2,S} {8,S}
8   C u0 {5,S} {7,S}
9   C u0 {4,S} {6,S}
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
    label = "s3_6_6_diene_0_2",
    group = 
"""
1   C u0 {3,S} {6,S} {7,S}
2   C u0 {3,S} {4,S} {5,D}
3   C u0 {1,S} {2,S}
4 * C u0 {2,S} {9,S}
5   C u0 {2,D} {8,S}
6   C u0 {1,S} {8,D}
7   C u0 {1,S} {9,S}
8   C u0 {5,S} {6,D}
9   C u0 {4,S} {7,S}
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
    label = "s3_6_6_diene_0_3",
    group = 
"""
1   C u0 {3,S} {6,S} {7,D}
2   C u0 {3,S} {4,D} {5,S}
3   C u0 {1,S} {2,S}
4 * C u0 {2,D} {9,S}
5   C u0 {2,S} {8,S}
6   C u0 {1,S} {8,S}
7   C u0 {1,D} {9,S}
8   C u0 {5,S} {6,S}
9   C u0 {4,S} {7,S}
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
    label = "s3_6_6_diene_0_4",
    group = 
"""
1   C u0 {3,S} {5,S} {7,D}
2   C u0 {3,S} {4,S} {6,D}
3   C u0 {1,S} {2,S}
4 * C u0 {2,S} {9,S}
5   C u0 {1,S} {8,S}
6   C u0 {2,D} {8,S}
7   C u0 {1,D} {9,S}
8   C u0 {5,S} {6,S}
9   C u0 {4,S} {7,S}
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
    index = 173,
    label = "s3_6_6_diene_0_5",
    group = 
"""
1   C u0 {3,S} {4,S} {7,S}
2   C u0 {3,S} {5,D} {6,S}
3   C u0 {1,S} {2,S}
4 * C u0 {1,S} {9,S}
5   C u0 {2,D} {9,S}
6   C u0 {2,S} {8,S}
7   C u0 {1,S} {8,D}
8   C u0 {6,S} {7,D}
9   C u0 {4,S} {5,S}
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
    index = 174,
    label = "s3_6_6_diene_0_6",
    group = 
"""
1   C u0 {3,S} {6,S} {7,S}
2   C u0 {3,S} {4,D} {5,S}
3   C u0 {1,S} {2,S}
4 * C u0 {2,D} {8,S}
5   C u0 {2,S} {9,D}
6   C u0 {1,S} {8,S}
7   C u0 {1,S} {9,S}
8   C u0 {4,S} {6,S}
9   C u0 {5,D} {7,S}
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
    index = 175,
    label = "s3_6_6_diene_1_m",
    group = 
"""
1   C u0 {3,D} {6,S} {7,S}
2   C u0 {3,S} {4,S} {5,S}
3   C u0 {1,D} {2,S}
4 * C u0 {2,S} {9,D}
5   C u0 {2,S} {8,S}
6   C u0 {1,S} {8,S}
7   C u0 {1,S} {9,S}
8   C u0 {5,S} {6,S}
9   C u0 {4,D} {7,S}
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
    index = 176,
    label = "s3_6_6_diene_1_5",
    group = 
"""
1   C u0 {3,S} {4,S} {6,S}
2   C u0 {3,S} {5,S} {7,S}
3   C u0 {1,S} {2,S}
4 * C u0 {1,S} {9,S}
5   C u0 {2,S} {9,D}
6   C u0 {1,S} {8,D}
7   C u0 {2,S} {8,S}
8   C u0 {6,D} {7,S}
9   C u0 {4,S} {5,D}
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
    index = 177,
    label = "s3_6_6_diene_1_6",
    group = 
"""
1   C u0 {3,S} {5,S} {6,S}
2   C u0 {3,S} {4,S} {7,S}
3   C u0 {1,S} {2,S}
4 * C u0 {2,S} {9,S}
5   C u0 {1,S} {9,D}
6   C u0 {1,S} {8,D}
7   C u0 {2,S} {8,S}
8   C u0 {6,D} {7,S}
9   C u0 {4,S} {5,D}
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
    index = 178,
    label = "s3_6_6_diene_1_8",
    group = 
"""
1   C u0 {3,S} {4,S} {6,S}
2   C u0 {3,D} {5,S} {7,S}
3   C u0 {1,S} {2,D}
4 * C u0 {1,S} {8,S}
5   C u0 {2,S} {8,D}
6   C u0 {1,S} {9,S}
7   C u0 {2,S} {9,S}
8   C u0 {4,S} {5,D}
9   C u0 {6,S} {7,S}
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
    index = 0,
    label = "s3_6_7",
    group = 
"""
1    C u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
2    C u0 {3,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
3    C u0 {1,[S,D,T,B]} {2,[S,D,T,B]}
4  * C u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
5    C u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
6    C u0 {1,[S,D,T,B]} {8,[S,D,T,B]}
7    C u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
8    C u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
9    C u0 {5,[S,D,T,B]} {10,[S,D,T,B]}
10   C u0 {7,[S,D,T,B]} {9,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 186,
    label = "s3_6_7_ane",
    group = 
"""
1    C u0 {3,S} {6,S} {7,S}
2    C u0 {3,S} {4,S} {5,S}
3    C u0 {1,S} {2,S}
4  * C u0 {2,S} {8,S}
5    C u0 {2,S} {9,S}
6    C u0 {1,S} {8,S}
7    C u0 {1,S} {10,S}
8    C u0 {4,S} {6,S}
9    C u0 {5,S} {10,S}
10   C u0 {7,S} {9,S}
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
    index = 0,
    label = "s3_6_7_ene",
    group = "OR{s3_6_7_ene_6}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 187,
    label = "s3_6_7_ene_6",
    group = 
"""
1    C u0 {3,S} {6,S} {7,S}
2    C u0 {3,S} {4,S} {5,S}
3    C u0 {1,S} {2,S}
4    C u0 {2,S} {9,S}
5  * C u0 {2,S} {8,D}
6    C u0 {1,S} {10,S}
7    C u0 {1,S} {8,S}
8    C u0 {5,D} {7,S}
9    C u0 {4,S} {10,S}
10   C u0 {6,S} {9,S}
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
    index = 0,
    label = "s3_6_7_diene",
    group = "OR{s3_6_7_diene_6_9-0}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 188,
    label = "s3_6_7_diene_6_9-0",
    group = 
"""
1    C u0 {3,D} {4,S} {7,S}
2    C u0 {3,S} {5,S} {6,S}
3    C u0 {1,D} {2,S}
4    C u0 {1,S} {10,S}
5  * C u0 {2,S} {8,D}
6    C u0 {2,S} {9,S}
7    C u0 {1,S} {8,S}
8    C u0 {5,D} {7,S}
9    C u0 {6,S} {10,S}
10   C u0 {4,S} {9,S}
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
    index = 0,
    label = "s4_6_6",
    group = 
"""
1 * C u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
2   C u0 {4,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
3   C u0 {1,[S,D,T,B]} {4,[S,D,T,B]}
4   C u0 {2,[S,D,T,B]} {3,[S,D,T,B]}
5   C u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
6   C u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
7   C u0 {2,[S,D,T,B]} {8,[S,D,T,B]}
8   C u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 179,
    label = "s4_6_6_ane",
    group = 
"""
1 * C u0 {3,S} {6,S} {8,S}
2   C u0 {4,S} {5,S} {7,S}
3   C u0 {1,S} {4,S}
4   C u0 {2,S} {3,S}
5   C u0 {2,S} {6,S}
6   C u0 {1,S} {5,S}
7   C u0 {2,S} {8,S}
8   C u0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-12,-11.01,-8.96,-6.42,-3.03,-2.4,0.05],'cal/(mol*K)'),
        H298 = (7.4,'kcal/mol'),
        S298 = (48.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Wiberg, K. Angew. Chem., Int. Ed. Engl. 1986, 25, 312 1986 experimental S, Cp from PM7 calculation
""",
)

entry(
    index = 0,
    label = "s4_6_8",
    group = 
"""
1    C u0 {4,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
2    C u0 {3,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
3  * C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4    C u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
5    C u0 {1,[S,D,T,B]} {6,[S,D,T,B]}
6    C u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
7    C u0 {1,[S,D,T,B]} {10,[S,D,T,B]}
8    C u0 {2,[S,D,T,B]} {9,[S,D,T,B]}
9    C u0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10   C u0 {7,[S,D,T,B]} {9,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 189,
    label = "s4_6_8_ane",
    group = 
"""
1    C u0 {4,S} {5,S} {7,S}
2    C u0 {3,S} {6,S} {8,S}
3  * C u0 {2,S} {4,S}
4    C u0 {1,S} {3,S}
5    C u0 {1,S} {6,S}
6    C u0 {2,S} {5,S}
7    C u0 {1,S} {10,S}
8    C u0 {2,S} {9,S}
9    C u0 {8,S} {10,S}
10   C u0 {7,S} {9,S}
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
    index = 0,
    label = "s4_6_8_ene",
    group = "OR{s4_6_8_ene_7}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 190,
    label = "s4_6_8_ene_7",
    group = 
"""
1    C u0 {3,S} {4,S} {8,S}
2    C u0 {5,D} {6,S} {7,S}
3  * C u0 {1,S} {5,S}
4    C u0 {1,S} {6,S}
5    C u0 {2,D} {3,S}
6    C u0 {2,S} {4,S}
7    C u0 {2,S} {9,S}
8    C u0 {1,S} {10,S}
9    C u0 {7,S} {10,S}
10   C u0 {8,S} {9,S}
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
    index = 0,
    label = "s4_6_8_diene",
    group = "OR{s4_6_8_diene_7_9}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 191,
    label = "s4_6_8_diene_7_9",
    group = 
"""
1    C u0 {3,D} {5,S} {7,S}
2    C u0 {4,S} {6,S} {8,S}
3  * C u0 {1,D} {4,S}
4    C u0 {2,S} {3,S}
5    C u0 {1,S} {6,D}
6    C u0 {2,S} {5,D}
7    C u0 {1,S} {10,S}
8    C u0 {2,S} {9,S}
9    C u0 {8,S} {10,S}
10   C u0 {7,S} {9,S}
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
        L3: s1_5_6_triene
            L4: s1_5_6_triene_1_3_7
            L4: s1_5_6_triene_1_3_8
        L3: s1_5_6_tetraene
            L4: s1_5_6_tetraene_1_3_7_9
            L4: s1_5_6_tetraene_1_4_7_9
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
            L4: s2_3_4_ene_m
    L2: s2_3_5
        L3: s2_3_5_ane
        L3: s2_3_5_ene
            L4: s2_3_5_ene_1
            L4: s2_3_5_ene_side
            L4: s2_3_5_ene_1_side
    L2: s2_3_6
        L3: s2_3_6_ane
        L3: s2_3_6_ene
            L4: s2_3_6_ene_1
            L4: s2_3_6_ene_2
        L3: s2_3_6_diene
            L4: s2_3_6_diene_0_2
            L4: s2_3_6_diene_0_3
            L4: s2_3_6_diene_1_3
        L3: s2_3_6_ben
    L2: s2_3_7
        L3: s2_3_7_ane
    L2: s2_3_8
        L3: s2_3_8_ane
    L2: s2_4_4
        L3: s2_4_4_ane
        L3: s2_4_4_ene
            L4: s2_4_4_ene_1
            L4: s2_4_4_ene_m
    L2: s2_4_5
        L3: s2_4_5_ane
        L3: s2_4_5_ene
            L4: s2_4_5_ene_0
            L4: s2_4_5_ene_1
        L3: s2_4_5_diene
            L4: s2_4_5_diene_0_3
            L4: s2_4_5_diene_1_5
            L4: s2_4_5_diene_4_6
    L2: s2_4_6
        L3: s2_4_6_ane
        L3: s2_4_6_ene
            L4: s2_4_6_ene_1
            L4: s2_4_6_ene_2
            L4: s2_4_6_ene_6
        L3: s2_4_6_diene
            L4: s2_4_6_diene_1_3
            L4: s2_4_6_diene_1_6
            L4: s2_4_6_diene_2_6
            L4: s2_4_6_diene_5_7
        L3: s2_4_6_ben
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
        L3: s2_5_5_tetraene
            L4: s2_5_5_tetraene_0_2_4_6
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
            L4: s2_5_6_diene_1_8
            L4: s2_5_6_diene_2_5
            L4: s2_5_6_diene_2_6
            L4: s2_5_6_diene_5_7
            L4: s2_5_6_diene_5_8
        L3: s2_5_6_triene
            L4: s2_5_6_triene_0_2_6
            L4: s2_5_6_triene_0_2_7
            L4: s2_5_6_triene_0_3_7
            L4: s2_5_6_triene_1_3_5
            L4: s2_5_6_triene_1_3_6
            L4: s2_5_6_triene_1_6_8
            L4: s2_5_6_triene_2_5_7
            L4: s2_5_6_triene_m_1_7
            L4: s2_5_6_triene_m_2_6
        L3: s2_5_6_tetraene
            L4: s2_5_6_tetraene_1_3_5_7
            L4: s2_5_6_tetraene_1_3_5_8
        L3: s2_5_6_ben
        L3: s2_5_6_indene
    L2: s2_5_7
        L3: s2_5_7_triene
            L4: s2_5_7_triene_0_2_8
            L4: s2_5_7_triene_0_3_8
            L4: s2_5_7_triene_1_3_7
            L4: s2_5_7_triene_1_3_8
            L4: s2_5_7_triene_1_3_9
            L4: s2_5_7_triene_1_4_7
        L3: s2_5_7_tetraene
            L4: s2_5_7_tetraene_0_2_4_8
            L4: s2_5_7_tetraene_1_3_7_9
            L4: s2_5_7_tetraene_m_1_3_8
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
        L3: s2_6_6_triene
            L4: s2_6_6_triene_0_2_6
            L4: s2_6_6_triene_0_2_7
            L4: s2_6_6_triene_0_3_7
            L4: s2_6_6_triene_1_3_6
            L4: s2_6_6_triene_1_3_7
        L3: s2_6_6_tetraene
            L4: s2_6_6_tetraene_0_2_4_7
            L4: s2_6_6_tetraene_0_2_5_7
            L4: s2_6_6_tetraene_0_2_6_8
            L4: s2_6_6_tetraene_0_3_6_8
            L4: s2_6_6_tetraene_1_3_6_8
        L3: s2_6_6_ben
        L3: s2_6_6_ben_ene
            L4: s2_6_6_ben_ene_1
            L4: s2_6_6_ben_ene_2
        L3: s2_6_6_naphthalene
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
            L4: s3_5_5_ene_0
            L4: s3_5_5_ene_1
            L4: s3_5_5_ene_side
            L4: s3_5_5_ene_m
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
    L2: s3_6_7
        L3: s3_6_7_ane
        L3: s3_6_7_ene
            L4: s3_6_7_ene_6
        L3: s3_6_7_diene
            L4: s3_6_7_diene_6_9-0
    L2: s4_6_6
        L3: s4_6_6_ane
    L2: s4_6_8
        L3: s4_6_8_ane
        L3: s4_6_8_ene
            L4: s4_6_8_ene_7
        L3: s4_6_8_diene
            L4: s4_6_8_diene_7_9
"""
)

