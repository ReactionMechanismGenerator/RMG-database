#!/usr/bin/env python
# encoding: utf-8

name = "1,5-Interaction Corrections"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "CsOsSs",
    group = 
"""
1 * [Cs,Os,S2s] u0 {2,S} {3,S}
2   Cs         u0 {1,S} {4,S} {5,S} {6,S}
3   Cs         u0 {1,S} {7,S} {8,S}
4   Cs         u0 {2,S}
5   Cs         u0 {2,S}
6   Cs         u0 {2,S}
7   Cs         u0 {3,S}
8   Cs         u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "Cs(Cs(CsCsCs)Cs(CsCsR)RR)",
    group = 
"""
1 * Cs u0 {2,S} {3,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3   Cs u0 {1,S} {7,S} {8,S}
4   Cs u0 {2,S}
5   Cs u0 {2,S}
6   Cs u0 {2,S}
7   Cs u0 {3,S}
8   Cs u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.5,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "Cs(Cs(CsCsCs)Cs(CsCsCs)RR)",
    group = 
"""
1 * Cs u0 {2,S} {3,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3   Cs u0 {1,S} {7,S} {8,S} {9,S}
4   Cs u0 {2,S}
5   Cs u0 {2,S}
6   Cs u0 {2,S}
7   Cs u0 {3,S}
8   Cs u0 {3,S}
9   Cs u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (3,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "Os(Cs(CsCsCs)Cs(CsCsR))",
    group = 
"""
1 * Os u0 {2,S} {3,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3   Cs u0 {1,S} {7,S} {8,S}
4   Cs u0 {2,S}
5   Cs u0 {2,S}
6   Cs u0 {2,S}
7   Cs u0 {3,S}
8   Cs u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (3.5,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "Os(Cs(CsCsCs)Cs(CsCsCs))",
    group = 
"""
1 * Os u0 {2,S} {3,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3   Cs u0 {1,S} {7,S} {8,S} {9,S}
4   Cs u0 {2,S}
5   Cs u0 {2,S}
6   Cs u0 {2,S}
7   Cs u0 {3,S}
8   Cs u0 {3,S}
9   Cs u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (7,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "S2s(Cs(CsCsCs)Cs(CsCsR))",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3   Cs u0 {1,S} {7,S} {8,S}
4   Cs u0 {2,S}
5   Cs u0 {2,S}
6   Cs u0 {2,S}
7   Cs u0 {3,S}
8   Cs u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.1,-0.2,-0.1,0,0.2,0.1,-0.2],'cal/(mol*K)'),
        H298 = (3.1,'kcal/mol'),
        S298 = (-1.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "S2s(Cs(CsCsCs)Cs(CsCsCs))",
    group = 
"""
1 * S2s u0 {2,S} {3,S}
2   Cs u0 {1,S} {4,S} {5,S} {6,S}
3   Cs u0 {1,S} {7,S} {8,S} {9,S}
4   Cs u0 {2,S}
5   Cs u0 {2,S}
6   Cs u0 {2,S}
7   Cs u0 {3,S}
8   Cs u0 {3,S}
9   Cs u0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1,-1,-0.8,-0.7,-0.6,-0.7,-1],'cal/(mol*K)'),
        H298 = (5.7,'kcal/mol'),
        S298 = (-1.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: CsOsSs
    L2: Cs(Cs(CsCsCs)Cs(CsCsR)RR)
        L3: Cs(Cs(CsCsCs)Cs(CsCsCs)RR)
    L2: Os(Cs(CsCsCs)Cs(CsCsR))
        L3: Os(Cs(CsCsCs)Cs(CsCsCs))
    L2: S2s(Cs(CsCsCs)Cs(CsCsR))
        L3: S2s(Cs(CsCsCs)Cs(CsCsCs))
"""
)

