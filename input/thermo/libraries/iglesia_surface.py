#!/usr/bin/env python
# encoding: utf-8

name = "iglesia_surface"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 0,
    label = "NO",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.97,7.06,7.2,7.37,7.72,8,8.46],'cal/(mol*K)'),
        # H298 = (21.85,'kcal/mol'),
        H298 = (0.0,'kcal/mol'),
        S298 = (49.02,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
From thermo_DFT_CCSDTF12_BAC:
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.97,7.06,7.2,7.37,7.72,8,8.46],'cal/(mol*K)'),
        H298 = (21.85,'kcal/mol'),
        S298 = (49.02,'cal/(mol*K)'),
    ),
""",
)

entry(
    index = 1,
    label = "HNO",
    molecule =
"""
1 N u0 p1 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.09,8.42,8.87,9.37,10.34,11.11,12.35],'cal/(mol*K)'),
        H298 = (32.10, 'kcal/mol'),
        S298 = (52.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
From thermo_DFT_CCSDTF12_BAC:
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.09,8.42,8.87,9.37,10.34,11.11,12.35],'cal/(mol*K)'),
        H298 = (25.34,'kcal/mol'),
        S298 = (52.71,'cal/(mol*K)'),
    ),
""",
)

entry(
    index = 2,
    label = "CH3NO",
    molecule =
"""
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.18,15.06,16.8,18.35,20.93,22.93,26.1],'cal/(mol*K)'),
        H298 = (23.69, 'kcal/mol'),
        S298 = (62.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
From thermo_DFT_CCSDTF12_BAC:
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.18,15.06,16.8,18.35,20.93,22.93,26.1],'cal/(mol*K)'),
        H298 = (16.93,'kcal/mol'),
        S298 = (62.7,'cal/(mol*K)'),
    ),
""",
)

entry(
    index = 3,
    label = "C2H5NO",
    molecule =
"""
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.3,21.3,24.8,28.0,32.9,36.5,42.1],'cal/(mol*K)'),
        H298 = (16.84, 'kcal/mol'),
        S298 = (70.44,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
From NOx2018
""",
)

entry(
    index = 4,
    label = "IC3H7NO",
    molecule =
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {9,S}
3  N u0 p1 c0 {2,S} {4,D}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.58,28.38,32.80,36.68,42.84,47.44,54.66],'cal/(mol*K)'),
        H298 = (30.34, 'kcal/mol'),
        S298 = (79.55,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
From GAV
""",
)

entry(
    index = 5,
    label = "NC3H7NO",
    molecule =
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  N u0 p1 c0 {3,S} {5,D}
5  O u0 p2 c0 {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.49,28.39,32.85,36.84,42.99,47.61,54.83],'cal/(mol*K)'),
        H298 = (13.08, 'kcal/mol'),
        S298 = (81.95,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
From GAV
""",
)
