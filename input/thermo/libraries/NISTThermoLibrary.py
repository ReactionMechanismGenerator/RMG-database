#!/usr/bin/env python
# encoding: utf-8

name = "NIST"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "NO2",
    molecule = 
"""
1 N 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 O 0 3 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.85,9.6,10.33,10.95,11.88,12.47,12.85],'cal/(mol*K)'),
        H298 = (7.911,'kcal/mol'),
        S298 = (57.371,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "O",
    molecule = 
"""
1 O 2T 2
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.2338,5.1292,5.0777,5.0517,5.0156,5.0005,4.9819],'cal/(mol*K)'),
        H298 = (59.555,'kcal/mol'),
        S298 = (38.494,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "C(T)",
    molecule = 
"""
1 C 4T 0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.98,4.98,4.98,4.97,4.97,4.96,4.97],'cal/(mol*K)'),
        H298 = (171.29,'kcal/mol'),
        S298 = (37.787,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "HO2",
    molecule = 
"""
1 H 0 0 {2,S}
2 O 0 2 {1,S} {3,S}
3 O 1 2 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.34,8.95,9.48,9.96,10.76,11.39,12.45],'cal/(mol*K)'),
        H298 = (0.5,'kcal/mol'),
        S298 = (54.754,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "NH2",
    molecule = 
"""
1 H 0 0 {3,S}
2 H 0 0 {3,S}
3 N 1 1 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.03,8.22,8.49,8.81,9.49,10.18,11.56],'cal/(mol*K)'),
        H298 = (45.5,'kcal/mol'),
        S298 = (46.537,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "NH3",
    molecule = 
"""
1 H 0 0 {3,S}
2 H 0 0 {3,S}
3 N 0 1 {1,S} {2,S} {4,S}
4 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.53,9.26,10.05,10.82,12.25,13.5,15.91],'cal/(mol*K)'),
        H298 = (-10.98,'kcal/mol'),
        S298 = (46.07,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "NO",
    molecule = 
"""
1 N 1 1 {2,D}
2 O 0 2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.13,7.15,7.29,7.47,7.83,8.13,8.55],'cal/(mol*K)'),
        H298 = (21.58,'kcal/mol'),
        S298 = (50.373,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "HNO",
    molecule = 
"""
1 H 0 0 {2,S}
2 N 0 1 {1,S} {3,D}
3 O 0 2 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.29,8.79,9.34,9.87,10.77,12.52],'cal/(mol*K)'),
        H298 = (23.8,'kcal/mol'),
        S298 = (52.753,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "HONO",
    molecule = 
"""
1 H 0 0 {2,S}
2 O 0 2 {1,S} {3,S}
3 N 0 1 {2,S} {4,D}
4 O 0 2 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.87,12.28,13.4,14.31,15.65,16.54,17.93],'cal/(mol*K)'),
        H298 = (-18.34,'kcal/mol'),
        S298 = (59.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

