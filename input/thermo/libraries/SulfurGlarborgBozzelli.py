#!/usr/bin/env python
# encoding: utf-8

name = "SulfurGlarborgBozzeli"
shortDesc = u""
longDesc = u"""
Contains: SOx, HSxOy, HxS, SOx-NOx

The effect of SO2 on moist CO oxidation with and without NO

Taken from:
Impact of SO2 and NO on CO oxidation under post-flame conditions
Peter Glarborg, Dorte Kubel, Kim Dam-Johansen, Hong-Ming Chiang, Joseph W. Bozzelli
International Journal of Chemical Kinetics, 28 (1996) 773-790
DOI: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
"""

entry(
    index = 1,
    label = "S",
    molecule = 
"""
multiplicity 3
1 S u2 p2 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([5.67,5.54,5.43,5.35,5.22,5.13,5.06],'cal/(mol*K)'),
        H298 = (66.2,'kcal/mol'),
        S298 = (40.09,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
from [34]
""",
)

entry(
    index = 2,
    label = "S2",
    molecule = 
"""
1 S u0 p2 c0 {2,D}
2 S u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.79,8.13,8.38,8.56,8.76,8.89,9.29],'cal/(mol*K)'),
        H298 = (30.7,'kcal/mol'),
        S298 = (54.50,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
from [34]
""",
)

entry(
    index = 3,
    label = "SH",
    molecule = 
"""
multiplicity 2
1 S u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.74,7.59,7.49,7.46,7.59,7.85,8.34],'cal/(mol*K)'),
        H298 = (33.3,'kcal/mol'),
        S298 = (46.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
from [34]
""",
)

entry(
    index = 4,
    label = "H2S",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.15,8.54,8.91,9.29,10.15,10.97,12.28],'cal/(mol*K)'),
        H298 = (-4.9,'kcal/mol'),
        S298 = (49.14,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
from [34]
""",
)

entry(
    index = 5,
    label = "SO",
    molecule = 
"""
1 S u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.22,7.55,7.84,8.08,8.43,8.62,8.95],'cal/(mol*K)'),
        H298 = (1.2,'kcal/mol'),
        S298 = (53.01,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
from [34]
""",
)

entry(
    index = 6,
    label = "SO2",
    molecule = 
"""
1 S u0 p1 c0 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.54,10.41,11.12,11.71,12.55,13.03,13.61],'cal/(mol*K)'),
        H298 = (-71.0,'kcal/mol'),
        S298 = (59.29,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
from [34] (AdjList currently doesn't work on website)
""",
)

entry(
    index = 7,
    label = "SO3",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 S u0 p0 c+2 {1,D} {3,S} {4,S}
3 O u0 p3 c-1 {2,S}
4 O u0 p3 c-1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.17,13.76,15.05,16.07,17.45,18.16,19.02],'cal/(mol*K)'),
        H298 = (-94.6,'kcal/mol'),
        S298 = (61.34,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
from [34]
""",
)

entry(
    index = 8,
    label = "HSO",
    molecule = 
"""
multiplicity 2
1 S u1 p1 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.02,9.93,10.73,11.36,12.22,12.73,13.34],'cal/(mol*K)'),
        H298 = (-5.4,'kcal/mol'),
        S298 = (57.80,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
from [35]
""",
)

entry(
    index = 9,
    label = "HOS",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 S u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.71,9.42,10.00,10.45,11.08,11.53,12.33],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (57.15,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
from [35]
""",
)

entry(
    index = 10,
    label = "HSOH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 S u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.83,12.22,13.47,14.46,15.82,16.62,17.60],'cal/(mol*K)'),
        H298 = (-28.5,'kcal/mol'),
        S298 = (58.66,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
from [35]
""",
)

entry(
    index = 11,
    label = "H2SO",
    molecule = 
"""
1 S u0 p1 c0 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.53,11.13,12.66,13.95,15.82,17.00,18.44],'cal/(mol*K)'),
        H298 = (-11.3,'kcal/mol'),
        S298 = (57.26,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
from [35]
""",
)

entry(
    index = 12,
    label = "HOSO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 S u1 p1 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.87,13.43,14.56,15.35,16.40,17.06,18.09],'cal/(mol*K)'),
        H298 = (-57.7,'kcal/mol'),
        S298 = (64.62,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
from [35]
""",
)

entry(
    index = 13,
    label = "HSO2",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 S u0 p1 c0 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.94,13.68,14.99,15.97,17.28,18.05,18.98],'cal/(mol*K)'),
        H298 = (-33.8,'kcal/mol'),
        S298 = (63.68,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
from [35]
""",
)

entry(
    index = 14,
    label = "HOSHO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 S u0 p1 c0 {1,S} {3,D} {5,S}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.58,15.84,17.65,19.01,20.82,21.95,23.54],'cal/(mol*K)'),
        H298 = (-64.5,'kcal/mol'),
        S298 = (64.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
from [35]
""",
)

entry(
    index = 15,
    label = "HOSO2",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 S u1 p0 c0 {1,D} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,S} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.74,18.76,20.13,21.07,22.22,22.94,24.02],'cal/(mol*K)'),
        H298 = (-93.5,'kcal/mol'),
        S298 = (70.72,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
from [35] (AdjList currently doesn't work on website)
""",
)

