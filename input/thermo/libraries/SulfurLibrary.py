#!/usr/bin/env python
# encoding: utf-8

name = "SulfurLibrary"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "CS2",
    molecule = 
"""
1 C 0 0 {2,D} {3,D}
2 S 0 2 {1,D}
3 S 0 2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.93,11.87,12.55,13.05,13.74,14.17,14.72],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (27.95,'kcal/mol','+|-',1),
        S298 = (56.88,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""All from [10]""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "CH2CS",
    molecule = 
"""
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 S 0 2 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.05,14.81,16.24,17.42,19.26,20.64,22.79],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (46.77,'kcal/mol','+|-',1),
        S298 = (60.69,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "H2S",
    molecule = 
"""
1 S 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.18,8.49,8.89,9.31,10.16,10.93,12.3],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-4.9,'kcal/mol','+|-',1),
        S298 = (49.18,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""All from [10]""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "H2S2",
    molecule = 
"""
1 S 0 2 {2,S} {3,S}
2 S 0 2 {1,S} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.86,13.23,14.22,14.99,16.1,16.86,17.86],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (3.4,'kcal/mol','+|-',1),
        S298 = (60.38,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "H2S3",
    molecule = 
"""
1 S 0 2 {2,S} {3,S}
2 S 0 2 {1,S} {4,S}
3 S 0 2 {1,S} {5,S}
4 H 0 0 {2,S}
5 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.13,18.9,20.16,21.12,22.42,23.17,23.85],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (6.41,'kcal/mol','+|-',1),
        S298 = (74.73,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "CH3SH",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 S 0 2 {1,S} {6,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.34,14.53,16.51,18.22,21.02,23.2,26.71],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-5.46,'kcal/mol','+|-',0.14),
        S298 = (60.55,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""H298 from [1]""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "CH3SCH3",
    molecule = 
"""
1 C 0 0 {3,S} {4,S} {5,S} {6,S}
2 C 0 0 {3,S} {7,S} {8,S} {9,S}
3 S 0 2 {1,S} {2,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
9 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.91,21.13,24.08,26.61,30.7,33.9,39.27],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-8.96,'kcal/mol','+|-',0.48),
        S298 = (69.68,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""H298 from [5]""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "C2H3SC2H3",
    molecule = 
"""
1  C 0 0 {3,D} {5,S} {6,S}
2  C 0 0 {4,D} {5,S} {7,S}
3  C 0 0 {1,D} {8,S} {9,S}
4  C 0 0 {2,D} {10,S} {11,S}
5  S 0 2 {1,S} {2,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.45,30.48,34.38,37.45,42.1,45.58,51.21],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (25.33,'kcal/mol','+|-',0.96),
        S298 = (81.43,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""H298 from [5], strong disagreement w/ QM""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "C2H3SC2H",
    molecule = 
"""
1 C 0 0 {2,D} {3,S} {6,S}
2 C 0 0 {1,D} {7,S} {8,S}
3 S 0 2 {1,S} {4,S}
4 C 0 0 {3,S} {5,T}
5 C 0 0 {4,T} {9,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
9 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.45,29.27,31.82,33.75,36.7,38.99,42.86],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (83.7,'kcal/mol','+|-',1),
        S298 = (77.79,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "C2H3SH",
    molecule = 
"""
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,S} {6,S}
3 S 0 2 {1,S} {7,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
7 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.09,18.96,21.25,23.08,25.89,28.01,31.48],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (19.24,'kcal/mol','+|-',1),
        S298 = (68.45,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "CH3SC2H3",
    molecule = 
"""
1  C 0 0 {4,S} {5,S} {6,S} {7,S}
2  C 0 0 {3,D} {4,S} {8,S}
3  C 0 0 {2,D} {9,S} {10,S}
4  S 0 2 {1,S} {2,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.3,26.11,29.41,32.19,36.61,40,45.51],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (14.77,'kcal/mol','+|-',1),
        S298 = (75.19,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "CH3SC2H",
    molecule = 
"""
1 C 0 0 {2,S} {5,S} {6,S} {7,S}
2 S 0 2 {1,S} {3,S}
3 C 0 0 {2,S} {4,T}
4 C 0 0 {3,T} {8,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.53,22.56,25,27.02,30.22,32.69,36.71],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (57.5,'kcal/mol','+|-',1),
        S298 = (72.66,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "HCSSH",
    molecule = 
"""
1 C 0 0 {2,D} {3,S} {4,S}
2 S 0 2 {1,D}
3 S 0 2 {1,S} {5,S}
4 H 0 0 {1,S}
5 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.42,16.28,17.71,18.84,20.54,21.76,23.52],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (25.68,'kcal/mol','+|-',1),
        S298 = (66.82,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "HCSSCH3",
    molecule = 
"""
1 C 0 0 {3,S} {4,S} {5,S} {6,S}
2 C 0 0 {3,S} {7,D} {8,S}
3 S 0 2 {1,S} {2,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 S 0 2 {2,D}
8 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.86,22.55,25.61,28.01,31.47,33.9,37.6],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (18.46,'kcal/mol','+|-',1),
        S298 = (75.46,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "HCSSC2H3",
    molecule = 
"""
1 C 0 0 {2,D} {4,S} {5,S}
2 C 0 0 {1,D} {6,S} {7,S}
3 C 0 0 {4,S} {8,D} {9,S}
4 S 0 2 {1,S} {3,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 S 0 2 {3,D}
9 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.07,27.64,31.09,33.65,37.2,39.65,43.38],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (45.24,'kcal/mol','+|-',1),
        S298 = (80.54,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "HCSSC2H",
    molecule = 
"""
1 C 0 0 {2,D} {3,S} {6,S}
2 S 0 2 {1,D}
3 S 0 2 {1,S} {4,S}
4 C 0 0 {3,S} {5,T}
5 C 0 0 {4,T} {7,S}
6 H 0 0 {1,S}
7 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.31,24.22,26.36,27.98,30.34,32.02,34.46],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (91.12,'kcal/mol','+|-',1),
        S298 = (78.43,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "HCSSCSH",
    molecule = 
"""
1 C 0 0 {2,D} {3,S} {6,S}
2 S 0 2 {1,D}
3 S 0 2 {1,S} {4,S}
4 C 0 0 {3,S} {5,D} {7,S}
5 S 0 2 {4,D}
6 H 0 0 {1,S}
7 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.18,24.14,26.51,28.36,31,32.71,34.8],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (56.89,'kcal/mol','+|-',1),
        S298 = (77.85,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "HCSSSH",
    molecule = 
"""
1 C 0 0 {2,D} {3,S} {5,S}
2 S 0 2 {1,D}
3 S 0 2 {1,S} {4,S}
4 S 0 2 {3,S} {6,S}
5 H 0 0 {1,S}
6 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.72,21.93,23.62,24.92,26.73,27.88,29.28],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (30.78,'kcal/mol','+|-',1),
        S298 = (76.99,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "C2H5SH",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 0 {1,S} {6,S} {7,S} {8,S}
3 S 0 2 {1,S} {9,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
9 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.04,21.64,24.88,27.66,32.05,35.34,40.47],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-11.03,'kcal/mol','+|-',1),
        S298 = (69.63,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""H298 from [2]""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "allylthiol",
    molecule = 
"""
1  C 0 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 0 {1,S} {3,D} {7,S}
3  C 0 0 {2,D} {8,S} {9,S}
4  S 0 2 {1,S} {10,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.35,26.88,29.92,32.54,36.85,40.22,45.68],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (14.42,'kcal/mol','+|-',1),
        S298 = (75.8,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "prop2yne1thiol",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {5,S} {6,S}
2 C 0 0 {1,S} {4,T}
3 S 0 2 {1,S} {7,S}
4 C 0 0 {2,T} {8,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {3,S}
8 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.48,22.62,25.16,27.25,30.52,33.01,36.98],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (56.45,'kcal/mol','+|-',1),
        S298 = (72.76,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "SHCH2SH",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 S 0 2 {1,S} {6,S}
3 S 0 2 {1,S} {7,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.68,21.08,22.49,23.82,26.16,28.08,31.22],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (4.18,'kcal/mol','+|-',1),
        S298 = (74.42,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "HCSCH2SH",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 0 {1,S} {6,D} {7,S}
3 S 0 2 {1,S} {8,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 S 0 2 {2,D}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.25,25.58,27.8,29.43,31.89,33.8,36.97],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (25.55,'kcal/mol','+|-',1),
        S298 = (75.82,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "propane2thiol",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {4,S} {5,S}
2  C 0 0 {1,S} {6,S} {7,S} {8,S}
3  C 0 0 {1,S} {9,S} {10,S} {11,S}
4  S 0 2 {1,S} {12,S}
5  H 0 0 {1,S}
6  H 0 0 {2,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.08,29.15,33.49,37.06,42.58,46.79,53.77],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-18.39,'kcal/mol','+|-',0.15),
        S298 = (77.9,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""H298 from [3]""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "but1ene3thiol",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {5,S} {6,S}
2  C 0 0 {1,S} {7,S} {8,S} {9,S}
3  C 0 0 {1,S} {4,D} {10,S}
4  C 0 0 {3,D} {11,S} {12,S}
5  S 0 2 {1,S} {13,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
12 H 0 0 {4,S}
13 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.04,34.68,39.19,42.82,48.5,52.89,60.03],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (6.8,'kcal/mol','+|-',1),
        S298 = (82.42,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "but1yne3thiol",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {4,S} {6,S}
2  C 0 0 {1,S} {7,S} {8,S} {9,S}
3  C 0 0 {1,S} {5,T}
4  S 0 2 {1,S} {10,S}
5  C 0 0 {3,T} {11,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {4,S}
11 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.26,29.98,33.83,36.96,41.81,45.46,51.25],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (49.14,'kcal/mol','+|-',1),
        S298 = (81.2,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "ethane11dithiol",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {4,S} {5,S}
2  C 0 0 {1,S} {6,S} {7,S} {8,S}
3  S 0 2 {1,S} {9,S}
4  S 0 2 {1,S} {10,S}
5  H 0 0 {1,S}
6  H 0 0 {2,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.11,28.27,31.06,33.47,37.42,40.51,45.5],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-3.68,'kcal/mol','+|-',1),
        S298 = (81.62,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "HCSCHCH3SH",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {4,S} {5,S}
2  C 0 0 {1,S} {6,S} {7,S} {8,S}
3  C 0 0 {1,S} {9,D} {10,S}
4  S 0 2 {1,S} {11,S}
5  H 0 0 {1,S}
6  H 0 0 {2,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  S 0 2 {3,D}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.83,32.92,36.65,39.41,43.42,46.41,51.3],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (17.58,'kcal/mol','+|-',1),
        S298 = (82.71,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "t_butanethiol",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {4,S} {5,S}
2  C 0 0 {1,S} {6,S} {7,S} {8,S}
3  C 0 0 {1,S} {9,S} {10,S} {11,S}
4  C 0 0 {1,S} {12,S} {13,S} {14,S}
5  S 0 2 {1,S} {15,S}
6  H 0 0 {2,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
14 H 0 0 {4,S}
15 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.64,37.33,42.97,47.52,54.44,59.63,68.19],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-25.99,'kcal/mol','+|-',0.21),
        S298 = (83.68,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""H298 from [4]""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "CH3CHS",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 0 {1,S} {6,D} {7,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 S 0 2 {2,D}
7 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.6,17.16,19.51,21.51,24.67,27.07,30.94],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (16.41,'kcal/mol','+|-',1),
        S298 = (65.91,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""Expt available [9]""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "HCSC2H5",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {4,S} {5,S}
2  C 0 0 {1,S} {6,S} {7,S} {8,S}
3  C 0 0 {1,S} {9,D} {10,S}
4  H 0 0 {1,S}
5  H 0 0 {1,S}
6  H 0 0 {2,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  S 0 2 {3,D}
10 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.98,24.09,27.73,30.78,35.55,39.14,44.94],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (11,'kcal/mol','+|-',1),
        S298 = (76.13,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "propanethial2methyl",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {4,S} {5,S}
2  C 0 0 {1,S} {6,S} {7,S} {8,S}
3  C 0 0 {1,S} {9,S} {10,S} {11,S}
4  C 0 0 {1,S} {12,D} {13,S}
5  H 0 0 {1,S}
6  H 0 0 {2,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 S 0 2 {4,D}
13 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.35,31.94,36.75,40.72,46.88,51.52,59.07],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (4.58,'kcal/mol','+|-',1),
        S298 = (82.97,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "propanethial22dimethyl",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {4,S} {5,S}
2  C 0 0 {1,S} {6,S} {7,S} {8,S}
3  C 0 0 {1,S} {9,S} {10,S} {11,S}
4  C 0 0 {1,S} {12,S} {13,S} {14,S}
5  C 0 0 {1,S} {15,D} {16,S}
6  H 0 0 {2,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
14 H 0 0 {4,S}
15 S 0 2 {5,D}
16 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([32.7,39.9,45.97,50.91,58.46,64.12,73.34],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-3.84,'kcal/mol','+|-',1),
        S298 = (87.27,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "propene2thiol",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,D} {4,S}
3  C 0 0 {2,D} {8,S} {9,S}
4  S 0 2 {2,S} {10,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.1,25.32,28.85,31.79,36.47,40.01,45.63],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (9.82,'kcal/mol','+|-',1),
        S298 = (73.9,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "propenethial",
    molecule = 
"""
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {6,S} {7,S}
3 C 0 0 {1,S} {5,D} {8,S}
4 H 0 0 {1,S}
5 S 0 2 {3,D}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.18,21.4,24.94,27.7,31.59,34.2,37.93],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (38.39,'kcal/mol','+|-',1),
        S298 = (68.35,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "propynethial",
    molecule = 
"""
1 C 0 0 {2,T} {5,S}
2 C 0 0 {1,T} {3,S}
3 C 0 0 {2,S} {4,D} {6,S}
4 S 0 2 {3,D}
5 H 0 0 {1,S}
6 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.92,18.49,20.44,21.95,24.18,25.77,28.24],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (84.36,'kcal/mol','+|-',1),
        S298 = (68.07,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "ethanedithial",
    molecule = 
"""
1 C 0 0 {2,S} {3,D} {5,S}
2 C 0 0 {1,S} {4,D} {6,S}
3 S 0 2 {1,D}
4 S 0 2 {2,D}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.69,18.59,21.14,23.21,26.01,27.54,29.1],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (53.07,'kcal/mol','+|-',1),
        S298 = (68.42,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "propane2thione",
    molecule = 
"""
1  C 0 0 {3,S} {4,S} {5,S} {6,S}
2  C 0 0 {3,S} {7,S} {8,S} {9,S}
3  C 0 0 {1,S} {2,S} {10,D}
4  H 0 0 {1,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 S 0 2 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19,22.89,26.6,29.85,35.06,38.97,45.08],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (5.5,'kcal/mol','+|-',1),
        S298 = (72.92,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "but3ene2thione",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {8,D}
3  C 0 0 {2,S} {4,D} {9,S}
4  C 0 0 {3,D} {10,S} {11,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  S 0 2 {2,D}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.55,28.42,32.62,36.13,41.5,45.38,51.32],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (29.02,'kcal/mol','+|-',1),
        S298 = (77.86,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "but3yne2thione",
    molecule = 
"""
1 C 0 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 0 {1,S} {3,S} {8,D}
3 C 0 0 {2,S} {4,T}
4 C 0 0 {3,T} {9,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 S 0 2 {2,D}
9 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.65,25.66,28.92,31.58,35.64,38.6,43.18],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (73.2,'kcal/mol','+|-',1),
        S298 = (76.39,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "HCSCSCH3",
    molecule = 
"""
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 0 {1,S} {3,S} {7,D}
3 C 0 0 {2,S} {8,D} {9,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 S 0 2 {2,D}
8 S 0 2 {3,D}
9 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.25,25.42,29.09,32.02,36.11,38.75,42.5],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (42.24,'kcal/mol','+|-',1),
        S298 = (79.42,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "C2HSC2H",
    molecule = 
"""
1 C 0 0 {2,T} {6,S}
2 C 0 0 {1,T} {3,S}
3 S 0 2 {2,S} {4,S}
4 C 0 0 {3,S} {5,T}
5 C 0 0 {4,T} {7,S}
6 H 0 0 {1,S}
7 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.8,24.53,26.41,27.83,29.94,31.49,33.98],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (129.08,'kcal/mol','+|-',1),
        S298 = (78.06,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "C2HSH",
    molecule = 
"""
1 C 0 0 {2,T} {3,S}
2 C 0 0 {1,T} {4,S}
3 S 0 2 {1,S} {5,S}
4 H 0 0 {2,S}
5 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.41,16.16,17.39,18.35,19.86,21.03,22.96],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (61.82,'kcal/mol','+|-',1),
        S298 = (63.03,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "C2H3SSH",
    molecule = 
"""
1 C 0 0 {2,D} {3,S} {5,S}
2 C 0 0 {1,D} {6,S} {7,S}
3 S 0 2 {1,S} {4,S}
4 S 0 2 {3,S} {8,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.38,24.76,27.55,29.79,33.03,35.19,38.17],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (24.15,'kcal/mol','+|-',1),
        S298 = (78.68,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "CH3SSH",
    molecule = 
"""
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 S 0 2 {1,S} {3,S}
3 S 0 2 {2,S} {7,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.27,19.74,21.86,23.64,26.43,28.47,31.59],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-1.25,'kcal/mol','+|-',1),
        S298 = (71.12,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "C2HSSH",
    molecule = 
"""
1 C 0 0 {2,S} {3,T}
2 S 0 2 {1,S} {4,S}
3 C 0 0 {1,T} {5,S}
4 S 0 2 {2,S} {6,S}
5 H 0 0 {3,S}
6 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.47,21.83,23.37,24.47,25.97,27,28.55],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (67.79,'kcal/mol','+|-',1),
        S298 = (73.72,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "CH3SC2H5",
    molecule = 
"""
1  C 0 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 0 {1,S} {7,S} {8,S} {9,S}
3  C 0 0 {4,S} {10,S} {11,S} {12,S}
4  S 0 2 {1,S} {3,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.83,27.53,31.85,35.6,41.68,46.35,53.82],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-14.41,'kcal/mol','+|-',0.26),
        S298 = (79.71,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""H298 from [3]""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "isopropyl_methyl_sulfide",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {5,S} {6,S}
2  C 0 0 {1,S} {7,S} {8,S} {9,S}
3  C 0 0 {1,S} {10,S} {11,S} {12,S}
4  C 0 0 {5,S} {13,S} {14,S} {15,S}
5  S 0 2 {1,S} {4,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {3,S}
13 H 0 0 {4,S}
14 H 0 0 {4,S}
15 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.07,35.22,40.76,45.49,53.07,58.86,68.12],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-21.43,'kcal/mol','+|-',0.18),
        S298 = (85.25,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""H298 from [4]""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "tertbutyl_methyl_sulfide",
    molecule = 
"""
1  C 0 0 {2,S} {7,S} {8,S} {9,S}
2  S 0 2 {1,S} {3,S}
3  C 0 0 {2,S} {4,S} {5,S} {6,S}
4  C 0 0 {3,S} {10,S} {11,S} {12,S}
5  C 0 0 {3,S} {13,S} {14,S} {15,S}
6  C 0 0 {3,S} {16,S} {17,S} {18,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {1,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
12 H 0 0 {4,S}
13 H 0 0 {5,S}
14 H 0 0 {5,S}
15 H 0 0 {5,S}
16 H 0 0 {6,S}
17 H 0 0 {6,S}
18 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.35,43.35,50.22,55.94,64.92,71.72,82.59],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-28.92,'kcal/mol','+|-',0.18),
        S298 = (90.14,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""H298 from [6]""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "allyl_methyl_sulfide",
    molecule = 
"""
1  C 0 0 {3,S} {5,S} {6,S} {7,S}
2  C 0 0 {5,S} {8,S} {9,S} {10,S}
3  C 0 0 {1,S} {4,D} {11,S}
4  C 0 0 {3,D} {12,S} {13,S}
5  S 0 2 {1,S} {2,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.37,34.55,38.7,42.18,47.85,52.31,59.65],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (10.61,'kcal/mol','+|-',1),
        S298 = (84.06,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "but1ene3thiomethyl",
    molecule = 
"""
1  C 0 0 {2,S} {4,S} {6,S} {7,S}
2  C 0 0 {1,S} {8,S} {9,S} {10,S}
3  C 0 0 {6,S} {11,S} {12,S} {13,S}
4  C 0 0 {1,S} {5,D} {14,S}
5  C 0 0 {4,D} {15,S} {16,S}
6  S 0 2 {1,S} {3,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 H 0 0 {3,S}
12 H 0 0 {3,S}
13 H 0 0 {3,S}
14 H 0 0 {4,S}
15 H 0 0 {5,S}
16 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.61,42.59,48.63,53.23,60.14,65.43,74.19],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (2.75,'kcal/mol','+|-',1),
        S298 = (89.92,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "methyl_propargyl_sulfide",
    molecule = 
"""
1  C 0 0 {3,S} {4,S} {6,S} {7,S}
2  C 0 0 {3,S} {8,S} {9,S} {10,S}
3  S 0 2 {1,S} {2,S}
4  C 0 0 {1,S} {5,T}
5  C 0 0 {4,T} {11,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.47,29.87,33.48,36.49,41.27,44.94,50.87],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (52.4,'kcal/mol','+|-',1),
        S298 = (81.12,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "but1yne3thiomethyl",
    molecule = 
"""
1  C 0 0 {2,S} {4,S} {5,S} {7,S}
2  C 0 0 {1,S} {8,S} {9,S} {10,S}
3  C 0 0 {4,S} {11,S} {12,S} {13,S}
4  S 0 2 {1,S} {3,S}
5  C 0 0 {1,S} {6,T}
6  C 0 0 {5,T} {14,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 H 0 0 {3,S}
12 H 0 0 {3,S}
13 H 0 0 {3,S}
14 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([31.76,37.47,42.26,46.25,52.57,57.39,65.15],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (45.19,'kcal/mol','+|-',1),
        S298 = (89.44,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "propene2thiomethyl",
    molecule = 
"""
1  C 0 0 {3,S} {6,S} {7,S} {8,S}
2  C 0 0 {5,S} {9,S} {10,S} {11,S}
3  C 0 0 {1,S} {4,D} {5,S}
4  C 0 0 {3,D} {12,S} {13,S}
5  S 0 2 {2,S} {3,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 H 0 0 {2,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.59,33.7,37.87,41.43,47.3,51.92,59.46],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (7.71,'kcal/mol','+|-',1),
        S298 = (82.87,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "CH3SSCH3",
    molecule = 
"""
1  C 0 0 {3,S} {5,S} {6,S} {7,S}
2  C 0 0 {4,S} {8,S} {9,S} {10,S}
3  S 0 2 {1,S} {4,S}
4  S 0 2 {2,S} {3,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.41,26.04,29.34,32.18,36.69,40.08,45.38],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-5.76,'kcal/mol','+|-',0.55),
        S298 = (80.48,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""H298 from [5]""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "CH3SSC2H3",
    molecule = 
"""
1  C 0 0 {4,S} {6,S} {7,S} {8,S}
2  C 0 0 {3,D} {5,S} {9,S}
3  C 0 0 {2,D} {10,S} {11,S}
4  S 0 2 {1,S} {5,S}
5  S 0 2 {2,S} {4,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.41,30.72,34.45,37.55,42.33,45.82,51.21],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (19.7,'kcal/mol','+|-',1),
        S298 = (85.74,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "CH3SSC2H",
    molecule = 
"""
1 C 0 0 {2,S} {6,S} {7,S} {8,S}
2 S 0 2 {1,S} {3,S}
3 S 0 2 {2,S} {4,S}
4 C 0 0 {3,S} {5,T}
5 C 0 0 {4,T} {9,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {1,S}
9 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.85,28.33,31.03,33.18,36.42,38.77,42.42],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (62.37,'kcal/mol','+|-',1),
        S298 = (82.66,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "CH3SSSH",
    molecule = 
"""
1 C 0 0 {2,S} {5,S} {6,S} {7,S}
2 S 0 2 {1,S} {3,S}
3 S 0 2 {2,S} {4,S}
4 S 0 2 {3,S} {8,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.84,25.56,27.87,29.8,32.73,34.76,37.58],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (1.05,'kcal/mol','+|-',1),
        S298 = (83.69,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "CH3SSSCH3",
    molecule = 
"""
1  C 0 0 {3,S} {6,S} {7,S} {8,S}
2  C 0 0 {4,S} {9,S} {10,S} {11,S}
3  S 0 2 {1,S} {5,S}
4  S 0 2 {2,S} {5,S}
5  S 0 2 {3,S} {4,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.67,33.35,36.55,39.27,43.56,46.69,51.4],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-4.49,'kcal/mol','+|-',1),
        S298 = (91.63,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "CH2S",
    molecule = 
"""
1 C 0 0 {2,D} {3,S} {4,S}
2 S 0 2 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.09,10.35,11.52,12.51,14.08,15.26,17.14],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (27.28,'kcal/mol','+|-',1),
        S298 = (56.45,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""Expts available [7] and [8]""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "CH3CSSH",
    molecule = 
"""
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 0 {1,S} {3,S} {7,D}
3 S 0 2 {2,S} {8,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 S 0 2 {2,D}
8 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.72,22.75,25.39,27.63,31.13,33.71,37.49],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (15.93,'kcal/mol','+|-',1),
        S298 = (75.41,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "C2H3SC2H5",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {8,S} {9,S} {10,S}
3  C 0 0 {4,D} {5,S} {11,S}
4  C 0 0 {3,D} {12,S} {13,S}
5  S 0 2 {1,S} {3,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.36,32.53,37.19,41.17,47.5,52.29,59.87],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (9.51,'kcal/mol','+|-',1),
        S298 = (85.05,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "pent1ene3thia4methyl",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {6,S} {7,S}
2  C 0 0 {1,S} {8,S} {9,S} {10,S}
3  C 0 0 {1,S} {11,S} {12,S} {13,S}
4  C 0 0 {5,D} {6,S} {14,S}
5  C 0 0 {4,D} {15,S} {16,S}
6  S 0 2 {1,S} {4,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 H 0 0 {3,S}
12 H 0 0 {3,S}
13 H 0 0 {3,S}
14 H 0 0 {4,S}
15 H 0 0 {5,S}
16 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([32.71,39.82,45.88,50.89,58.7,64.57,73.91],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (3.04,'kcal/mol','+|-',1),
        S298 = (90.5,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "pent1ene3thia24dimethyl",
    molecule = 
"""
1  C 0 0 {2,D} {8,S} {9,S}
2  C 0 0 {1,D} {3,S} {7,S}
3  S 0 2 {2,S} {4,S}
4  C 0 0 {3,S} {5,S} {6,S} {10,S}
5  C 0 0 {4,S} {11,S} {12,S} {13,S}
6  C 0 0 {4,S} {14,S} {15,S} {16,S}
7  C 0 0 {2,S} {17,S} {18,S} {19,S}
8  H 0 0 {1,S}
9  H 0 0 {1,S}
10 H 0 0 {4,S}
11 H 0 0 {5,S}
12 H 0 0 {5,S}
13 H 0 0 {5,S}
14 H 0 0 {6,S}
15 H 0 0 {6,S}
16 H 0 0 {6,S}
17 H 0 0 {7,S}
18 H 0 0 {7,S}
19 H 0 0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.8,47.27,54.54,60.65,70.27,77.47,88.69],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-6.89,'kcal/mol','+|-',1),
        S298 = (97.04,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "C2H3SC2CH3",
    molecule = 
"""
1  C 0 0 {4,S} {7,S} {8,S} {9,S}
2  C 0 0 {3,D} {5,S} {10,S}
3  C 0 0 {2,D} {11,S} {12,S}
4  C 0 0 {1,S} {6,T}
5  S 0 2 {2,S} {6,S}
6  C 0 0 {4,T} {5,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {1,S}
10 H 0 0 {2,S}
11 H 0 0 {3,S}
12 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.5,33.42,37.68,41.25,46.82,50.95,57.42],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (71.85,'kcal/mol','+|-',1),
        S298 = (89.41,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "CH3SC2SH",
    molecule = 
"""
1 C 0 0 {2,S} {6,S} {7,S} {8,S}
2 S 0 2 {1,S} {3,S}
3 C 0 0 {2,S} {4,T}
4 C 0 0 {3,T} {5,S}
5 S 0 2 {4,S} {9,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {1,S}
9 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.44,27.9,30.77,33.16,36.92,39.71,43.95],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (62,'kcal/mol','+|-',1),
        S298 = (83.62,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "penta14diene3thia24dimethyl",
    molecule = 
"""
1  C 0 0 {3,S} {8,S} {9,S} {10,S}
2  C 0 0 {4,S} {11,S} {12,S} {13,S}
3  C 0 0 {1,S} {5,D} {7,S}
4  C 0 0 {2,S} {6,D} {7,S}
5  C 0 0 {3,D} {14,S} {15,S}
6  C 0 0 {4,D} {16,S} {17,S}
7  S 0 2 {3,S} {4,S}
8  H 0 0 {1,S}
9  H 0 0 {1,S}
10 H 0 0 {1,S}
11 H 0 0 {2,S}
12 H 0 0 {2,S}
13 H 0 0 {2,S}
14 H 0 0 {5,S}
15 H 0 0 {5,S}
16 H 0 0 {6,S}
17 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.16,43.38,49.6,54.83,63.09,69.33,79.21],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (22.68,'kcal/mol','+|-',1),
        S298 = (98.26,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "HCSSC2H2SCH3",
    molecule = 
"""
1  S 0 2 {2,D}
2  C 0 0 {1,D} {3,S} {8,S}
3  S 0 2 {2,S} {4,S}
4  C 0 0 {3,S} {5,D} {9,S}
5  C 0 0 {4,D} {6,S} {10,S}
6  S 0 2 {5,S} {7,S}
7  C 0 0 {6,S} {11,S} {12,S} {13,S}
8  H 0 0 {2,S}
9  H 0 0 {4,S}
10 H 0 0 {5,S}
11 H 0 0 {7,S}
12 H 0 0 {7,S}
13 H 0 0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.25,41.93,46.2,49.47,54.23,57.67,63],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (46.36,'kcal/mol','+|-',1),
        S298 = (103.09,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "HCSSC2H5",
    molecule = 
"""
1  C 0 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 0 {1,S} {7,S} {8,S} {9,S}
3  C 0 0 {4,S} {10,D} {11,S}
4  S 0 2 {1,S} {3,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 S 0 2 {3,D}
11 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.33,29.56,33.9,37.37,42.54,46.28,51.98],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (13.06,'kcal/mol','+|-',1),
        S298 = (84.86,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "CH3CSSC2H5",
    molecule = 
"""
1  C 0 0 {2,S} {7,S} {8,S} {9,S}
2  C 0 0 {1,S} {3,D} {4,S}
3  S 0 2 {2,D}
4  S 0 2 {2,S} {5,S}
5  C 0 0 {4,S} {6,S} {10,S} {11,S}
6  C 0 0 {5,S} {12,S} {13,S} {14,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {1,S}
10 H 0 0 {5,S}
11 H 0 0 {5,S}
12 H 0 0 {6,S}
13 H 0 0 {6,S}
14 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.97,35.47,41.2,45.98,53.27,58.5,66.26],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (2.39,'kcal/mol','+|-',1),
        S298 = (93.04,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "SHCSC2H5",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {5,S} {6,S}
2  C 0 0 {1,S} {7,S} {8,S} {9,S}
3  C 0 0 {1,S} {4,S} {10,D}
4  S 0 2 {3,S} {11,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 S 0 2 {3,D}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.69,29.39,33.41,36.76,41.97,45.79,51.52],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (9.7,'kcal/mol','+|-',1),
        S298 = (83.73,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "pent1ene4methyl3thione",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {4,S} {7,S}
2  C 0 0 {1,S} {8,S} {9,S} {10,S}
3  C 0 0 {1,S} {11,S} {12,S} {13,S}
4  C 0 0 {1,S} {5,S} {14,D}
5  C 0 0 {4,S} {6,D} {15,S}
6  C 0 0 {5,D} {16,S} {17,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 H 0 0 {3,S}
12 H 0 0 {3,S}
13 H 0 0 {3,S}
14 S 0 2 {4,D}
15 H 0 0 {5,S}
16 H 0 0 {6,S}
17 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.97,42.21,49.39,55.33,64.31,70.72,80.35],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (17.87,'kcal/mol','+|-',1),
        S298 = (93.81,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "but-3-ene-2-thione-3-methyl",
    molecule = 
"""
1  C 0 0 {3,S} {6,S} {7,S} {8,S}
2  C 0 0 {4,S} {9,S} {10,S} {11,S}
3  C 0 0 {1,S} {4,S} {5,D}
4  C 0 0 {2,S} {3,S} {12,D}
5  C 0 0 {3,D} {13,S} {14,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 H 0 0 {2,S}
12 S 0 2 {4,D}
13 H 0 0 {5,S}
14 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.46,36.08,41.49,45.84,52.46,57.38,65.18],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (20.77,'kcal/mol','+|-',1),
        S298 = (85.09,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "prop-2-enethial-2-methyl",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,D} {4,S}
3  C 0 0 {2,D} {9,S} {10,S}
4  C 0 0 {2,S} {8,D} {11,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  S 0 2 {4,D}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.57,28.02,32.83,36.76,42.5,46.4,52.02],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (28.99,'kcal/mol','+|-',1),
        S298 = (76.76,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "pent-1-yne-3-thione",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {6,S} {7,S}
2  C 0 0 {1,S} {8,S} {9,S} {10,S}
3  C 0 0 {1,S} {4,S} {11,D}
4  C 0 0 {3,S} {5,T}
5  C 0 0 {4,T} {12,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 S 0 2 {3,D}
12 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.97,32.26,36.7,40.36,46.04,50.2,56.62],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (68.05,'kcal/mol','+|-',1),
        S298 = (88.13,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "C2HSSCSH",
    molecule = 
"""
1 C 0 0 {2,T} {7,S}
2 C 0 0 {1,T} {3,S}
3 S 0 2 {2,S} {4,S}
4 S 0 2 {3,S} {5,S}
5 C 0 0 {4,S} {6,D} {8,S}
6 S 0 2 {5,D}
7 H 0 0 {1,S}
8 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.44,30.81,33.05,34.63,36.73,38.1,39.96],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (95.39,'kcal/mol','+|-',1),
        S298 = (87.92,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "butane-23-dithione",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {4,D}
2  C 0 0 {1,S} {5,S} {6,D}
3  C 0 0 {1,S} {7,S} {8,S} {9,S}
4  S 0 2 {1,D}
5  C 0 0 {2,S} {10,S} {11,S} {12,S}
6  S 0 2 {2,D}
7  H 0 0 {3,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {5,S}
11 H 0 0 {5,S}
12 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26,31.13,35.73,39.58,45.48,49.7,56.05],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (33.1,'kcal/mol','+|-',1),
        S298 = (89.07,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "tertbutyl_hydrodisulfide",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {4,S} {5,S}
2  C 0 0 {1,S} {7,S} {8,S} {9,S}
3  C 0 0 {1,S} {10,S} {11,S} {12,S}
4  C 0 0 {1,S} {13,S} {14,S} {15,S}
5  S 0 2 {1,S} {6,S}
6  S 0 2 {5,S} {16,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {3,S}
13 H 0 0 {4,S}
14 H 0 0 {4,S}
15 H 0 0 {4,S}
16 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.08,42.44,48.49,53.39,60.86,66.35,74.82],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-24.77,'kcal/mol','+|-',1),
        S298 = (90.45,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "methanetrithiol",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 S 0 2 {1,S} {6,S}
3 S 0 2 {1,S} {7,S}
4 S 0 2 {1,S} {8,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {3,S}
8 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.19,27.38,28.99,30.26,32.36,34.04,36.79],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (12.93,'kcal/mol','+|-',1),
        S298 = (85.86,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "ethane-111-trithiol",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {4,S} {5,S}
2  C 0 0 {1,S} {6,S} {7,S} {8,S}
3  S 0 2 {1,S} {9,S}
4  S 0 2 {1,S} {10,S}
5  S 0 2 {1,S} {11,S}
6  H 0 0 {2,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
11 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([32.56,36.14,38.85,41.01,44.43,47.08,51.38],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (3.78,'kcal/mol','+|-',1),
        S298 = (91.05,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "propane-22-dithiol",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {4,S} {5,S}
2  C 0 0 {1,S} {6,S} {7,S} {8,S}
3  C 0 0 {1,S} {9,S} {10,S} {11,S}
4  S 0 2 {1,S} {12,S}
5  S 0 2 {1,S} {13,S}
6  H 0 0 {2,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
13 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([31.08,36.22,40.46,43.96,49.44,53.57,60.14],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-12.47,'kcal/mol','+|-',1),
        S298 = (85.85,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "butane-22-dithiol",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {5,S} {6,S}
2  C 0 0 {1,S} {4,S} {7,S} {8,S}
3  C 0 0 {1,S} {9,S} {10,S} {11,S}
4  C 0 0 {2,S} {12,S} {13,S} {14,S}
5  S 0 2 {1,S} {15,S}
6  S 0 2 {1,S} {16,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
14 H 0 0 {4,S}
15 H 0 0 {5,S}
16 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.68,43.28,48.84,53.45,60.64,66.01,74.46],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-17.29,'kcal/mol','+|-',1),
        S298 = (96.07,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "ethane-11-dithiol-1thiomethyl",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {4,S} {5,S}
2  C 0 0 {1,S} {7,S} {8,S} {9,S}
3  S 0 2 {1,S} {10,S}
4  S 0 2 {1,S} {11,S}
5  S 0 2 {1,S} {6,S}
6  C 0 0 {5,S} {12,S} {13,S} {14,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
12 H 0 0 {6,S}
13 H 0 0 {6,S}
14 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([37.76,42.85,46.98,50.29,55.36,59.19,65.39],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-1.15,'kcal/mol','+|-',1),
        S298 = (99.23,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "mercapto_rad",
    molecule = 
"""
1 S 1 2 {2,S}
2 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.75,7.57,7.48,7.47,7.6,7.85,8.35],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (33.3,'kcal/mol','+|-',1),
        S298 = (46.76,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""All from [10]""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "CH3Sj",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 S 1 2 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.8,12.57,14.13,15.44,17.57,19.22,21.92],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (29.88,'kcal/mol','+|-',0.48),
        S298 = (57.6,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""H298, S298 from [11]""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "C2H3Sj",
    molecule = 
"""
1 C 0 0 {2,D} {3,S} {4,S}
2 C 0 0 {1,D} {5,S} {6,S}
3 S 1 2 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.1,15.73,17.91,19.68,22.36,24.32,27.39],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (55.7,'kcal/mol','+|-',1),
        S298 = (64.5,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "C2HSj",
    molecule = 
"""
1 S 1 2 {2,S}
2 C 0 0 {1,S} {3,T}
3 C 0 0 {2,T} {4,S}
4 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.41,15.48,16.21,16.77,17.6,18.22,19.24],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (87.39,'kcal/mol','+|-',1),
        S298 = (93.95,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "HCSSj",
    molecule = 
"""
1 S 1 2 {2,S}
2 C 0 0 {1,S} {3,D} {4,S}
3 S 0 2 {2,D}
4 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.48,13.04,14.24,15.13,16.35,17.15,18.31],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (53.92,'kcal/mol','+|-',1),
        S298 = (65.88,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "SHSj",
    molecule = 
"""
1 S 1 2 {2,S}
2 S 0 2 {1,S} {3,S}
3 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.59,10.3,10.8,11.19,11.8,12.26,12.97],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (25.23,'kcal/mol','+|-',1),
        S298 = (60.88,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""Expt available [11]""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "CH3SSj",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 S 0 2 {1,S} {6,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 S 1 2 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.32,16.36,18.15,19.65,22.01,23.8,26.66],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (17.3,'kcal/mol','+|-',1),
        S298 = (70.82,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""Expts available [11]""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "SHSSj",
    molecule = 
"""
1 S 1 2 {2,S}
2 S 0 2 {1,S} {3,S}
3 S 0 2 {2,S} {4,S}
4 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.38,15.21,15.76,16.16,16.76,17.22,17.92],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (27.09,'kcal/mol','+|-',1),
        S298 = (73.78,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "CH2jSH",
    molecule = 
"""
1 C 1 0 {2,S} {3,S} {4,S}
2 S 0 2 {1,S} {5,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.92,14.45,15.71,16.75,18.39,19.66,21.74],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (38.04,'kcal/mol','+|-',1),
        S298 = (62.58,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "CH3CHjSH",
    molecule = 
"""
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 0 {1,S} {3,S} {7,S}
3 S 0 2 {2,S} {8,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.02,19.93,22.57,24.83,28.44,31.19,35.55],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (30.63,'kcal/mol','+|-',1),
        S298 = (71.55,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "C2H3CHjSH",
    molecule = 
"""
1 C 0 0 {2,S} {3,D} {5,S}
2 C 1 0 {1,S} {4,S} {6,S}
3 C 0 0 {1,D} {7,S} {8,S}
4 S 0 2 {2,S} {9,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {3,S}
8 H 0 0 {3,S}
9 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.46,24.55,27.89,30.57,34.61,37.57,42.21],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (44.65,'kcal/mol','+|-',1),
        S298 = (76.63,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "C2HCHjSH",
    molecule = 
"""
1 S 0 2 {2,S} {5,S}
2 C 1 0 {1,S} {3,S} {6,S}
3 C 0 0 {2,S} {4,T}
4 C 0 0 {3,T} {7,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.96,22.67,24.68,26.23,28.53,30.21,32.87],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (87.74,'kcal/mol','+|-',1),
        S298 = (74.46,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "HCSCHjSH",
    molecule = 
"""
1 S 0 2 {2,S} {5,S}
2 C 1 0 {1,S} {3,S} {6,S}
3 C 0 0 {2,S} {4,D} {7,S}
4 S 0 2 {3,D}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.24,21.29,23.78,25.76,28.65,30.63,33.43],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (48.63,'kcal/mol','+|-',1),
        S298 = (75.43,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "SHCHjSH",
    molecule = 
"""
1 C 1 0 {2,S} {3,S} {4,S}
2 S 0 2 {1,S} {5,S}
3 S 0 2 {1,S} {6,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.18,18.14,19.67,20.91,22.85,24.31,26.6],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (41.95,'kcal/mol','+|-',1),
        S298 = (74.81,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "isopropyl-2-thiol",
    molecule = 
"""
1  C 0 0 {3,S} {5,S} {6,S} {7,S}
2  C 0 0 {3,S} {8,S} {9,S} {10,S}
3  C 1 0 {1,S} {2,S} {4,S}
4  S 0 2 {3,S} {11,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.51,26.39,30.09,33.41,38.81,42.97,49.52],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (22.8,'kcal/mol','+|-',1),
        S298 = (82.05,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "but-1-en-3-yl-3-thiol",
    molecule = 
"""
1  C 1 0 {2,S} {3,S} {4,S}
2  S 0 2 {1,S} {6,S}
3  C 0 0 {1,S} {7,S} {8,S} {9,S}
4  C 0 0 {1,S} {5,D} {10,S}
5  C 0 0 {4,D} {11,S} {12,S}
6  H 0 0 {2,S}
7  H 0 0 {3,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
11 H 0 0 {5,S}
12 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.37,31.49,35.96,39.74,45.69,50.09,56.72],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (34.95,'kcal/mol','+|-',1),
        S298 = (86.56,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "but-1-yn-3-yl-3-thiol",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 1 0 {1,S} {3,S} {4,S}
3  C 0 0 {2,S} {5,T}
4  S 0 2 {2,S} {9,S}
5  C 0 0 {3,T} {10,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {4,S}
10 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.55,28.53,31.81,34.51,38.71,41.84,46.72],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (78.81,'kcal/mol','+|-',1),
        S298 = (84.1,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "propanethial-2-yl-2-thiol",
    molecule = 
"""
1  C 1 0 {2,S} {3,S} {4,S}
2  S 0 2 {1,S} {6,S}
3  C 0 0 {1,S} {7,S} {8,S} {9,S}
4  C 0 0 {1,S} {5,D} {10,S}
5  S 0 2 {4,D}
6  H 0 0 {2,S}
7  H 0 0 {3,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.92,29.09,33.25,36.47,41.13,44.34,48.95],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (35.68,'kcal/mol','+|-',1),
        S298 = (81.62,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "ethanyl-11-dithiol",
    molecule = 
"""
1 C 0 0 {2,S} {5,S} {6,S} {7,S}
2 C 1 0 {1,S} {3,S} {4,S}
3 S 0 2 {2,S} {8,S}
4 S 0 2 {2,S} {9,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {3,S}
9 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.75,25.1,27.51,29.71,33.37,36.19,40.61],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (34.44,'kcal/mol','+|-',1),
        S298 = (86.47,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "ethenyl-1-thiol",
    molecule = 
"""
1 C 0 0 {2,D} {4,S} {5,S}
2 C 1 0 {1,D} {3,S}
3 S 0 2 {2,S} {6,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.75,19.74,21.26,22.51,24.5,25.95,28.09],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (72.21,'kcal/mol','+|-',1),
        S298 = (69.43,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "thioacetyl",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 0 {1,S} {6,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 S 0 2 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.69,14.77,16.75,18.5,21.25,23.3,26.46],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (56.91,'kcal/mol','+|-',1),
        S298 = (66.09,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "Sjj",
    molecule = 
"""
1 S 2S 2
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.97,4.97,4.97,4.97,4.97,5.13,5.06],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (66.2,'kcal/mol','+|-',1),
        S298 = (40.11,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""H298, S298, Cp1000, Cp1500 from [10], rest from AGV""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "ethylthio",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 0 {1,S} {6,S} {7,S} {8,S}
3 S 1 2 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.99,19.18,22.02,24.45,28.36,31.33,36.04],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (23.44,'kcal/mol','+|-',1),
        S298 = (68.11,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "propyl-2-thio",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {4,S} {5,S}
2  C 0 0 {1,S} {6,S} {7,S} {8,S}
3  C 0 0 {1,S} {9,S} {10,S} {11,S}
4  S 1 2 {1,S}
5  H 0 0 {1,S}
6  H 0 0 {2,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.15,26.05,30.33,33.91,39.51,43.69,50.26],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (17.69,'kcal/mol','+|-',1),
        S298 = (74.74,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "tert-butylthio",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {4,S} {5,S}
2  C 0 0 {1,S} {6,S} {7,S} {8,S}
3  C 0 0 {1,S} {9,S} {10,S} {11,S}
4  C 0 0 {1,S} {12,S} {13,S} {14,S}
5  S 1 2 {1,S}
6  H 0 0 {2,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
14 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.39,33.82,39.39,44.02,51.15,56.41,64.72],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (9.73,'kcal/mol','+|-',1),
        S298 = (80.98,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "CH3SCH2Sj",
    molecule = 
"""
1 C 0 0 {3,S} {4,S} {5,S} {6,S}
2 C 0 0 {3,S} {7,S} {8,S} {9,S}
3 S 0 2 {1,S} {2,S}
4 S 1 2 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
9 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.36,24.36,27.74,30.4,34.27,37.02,41.33],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (33.73,'kcal/mol','+|-',1),
        S298 = (78.49,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "C2H3CH2Sj",
    molecule = 
"""
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 0 {1,S} {3,D} {7,S}
3 C 0 0 {2,D} {8,S} {9,S}
4 S 1 2 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
9 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.85,22.86,26.25,29.04,33.35,36.54,41.55],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (49.53,'kcal/mol','+|-',1),
        S298 = (73.16,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "C2H3C2H2Sj",
    molecule = 
"""
1  C 0 0 {2,S} {3,D} {5,S}
2  C 0 0 {1,S} {4,D} {6,S}
3  C 0 0 {1,D} {7,S} {8,S}
4  C 0 0 {2,D} {9,S} {10,S}
5  H 0 0 {1,S}
6  H 0 0 {2,S}
7  S 1 2 {3,S}
8  H 0 0 {3,S}
9  H 0 0 {4,S}
10 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.59,26.9,31.38,34.92,39.99,43.43,48.4],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (56.26,'kcal/mol','+|-',1),
        S298 = (79.5,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "propen-2-thio",
    molecule = 
"""
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 0 {1,S} {3,D} {7,S}
3 C 0 0 {2,D} {8,S} {9,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 S 1 2 {2,S}
8 H 0 0 {3,S}
9 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.62,22.47,25.86,28.68,33.1,36.35,41.47],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (38.65,'kcal/mol','+|-',1),
        S298 = (73.35,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "propen-1-thio",
    molecule = 
"""
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 0 {1,S} {3,D} {7,S}
3 C 0 0 {2,D} {8,S} {9,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 S 1 2 {3,S}
9 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.85,21.76,25.27,28.23,32.83,36.21,41.42],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (37.66,'kcal/mol','+|-',1),
        S298 = (73.01,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""Values for cis only""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "CH3SSSj",
    molecule = 
"""
1 S 1 2 {2,S}
2 S 0 2 {1,S} {3,S}
3 S 0 2 {2,S} {4,S}
4 C 0 0 {3,S} {5,S} {6,S} {7,S}
5 H 0 0 {4,S}
6 H 0 0 {4,S}
7 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19,21.2,23.04,24.56,26.95,28.75,31.62],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (21.23,'kcal/mol','+|-',1),
        S298 = (83.42,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "CH3SCH2j",
    molecule = 
"""
1 C 0 0 {3,S} {4,S} {5,S} {6,S}
2 C 1 0 {3,S} {7,S} {8,S}
3 S 0 2 {1,S} {2,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.66,20.57,23.11,25.26,28.69,31.32,35.56],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (33.53,'kcal/mol','+|-',1),
        S298 = (71.55,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "CH3SSCH2j",
    molecule = 
"""
1 C 0 0 {3,S} {5,S} {6,S} {7,S}
2 C 1 0 {4,S} {8,S} {9,S}
3 S 0 2 {1,S} {4,S}
4 S 0 2 {2,S} {3,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {2,S}
9 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.36,26.58,29.22,31.33,34.51,36.9,40.79],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (38.45,'kcal/mol','+|-',1),
        S298 = (83.91,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "SHCH2SCH2j",
    molecule = 
"""
1 C 0 0 {3,S} {4,S} {5,S} {6,S}
2 C 1 0 {3,S} {7,S} {8,S}
3 S 0 2 {1,S} {2,S}
4 S 0 2 {1,S} {9,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
9 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.44,27.29,29.67,31.66,34.81,37.23,41.12],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (43.2,'kcal/mol','+|-',1),
        S298 = (84.92,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "CH3SCHjCH3",
    molecule = 
"""
1  C 0 0 {3,S} {5,S} {6,S} {7,S}
2  C 0 0 {4,S} {8,S} {9,S} {10,S}
3  C 1 0 {1,S} {4,S} {11,S}
4  S 0 2 {2,S} {3,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.94,26.12,29.99,33.33,38.7,42.78,49.28],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (26.49,'kcal/mol','+|-',1),
        S298 = (82.05,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "C2H5SCHjCH3",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {8,S} {9,S} {10,S}
3  C 0 0 {4,S} {11,S} {12,S} {13,S}
4  C 1 0 {3,S} {5,S} {14,S}
5  S 0 2 {1,S} {4,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 H 0 0 {3,S}
12 H 0 0 {3,S}
13 H 0 0 {3,S}
14 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.94,33.65,38.76,43.11,50.03,55.27,63.6],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (20.69,'kcal/mol','+|-',1),
        S298 = (91,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    label = "pentan-2-yl-2-methyl-3-thia",
    molecule = 
"""
1  C 0 0 {2,S} {7,S} {8,S} {9,S}
2  C 0 0 {1,S} {3,S} {10,S} {11,S}
3  S 0 2 {2,S} {4,S}
4  C 1 0 {3,S} {5,S} {6,S}
5  C 0 0 {4,S} {12,S} {13,S} {14,S}
6  C 0 0 {4,S} {15,S} {16,S} {17,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {1,S}
10 H 0 0 {2,S}
11 H 0 0 {2,S}
12 H 0 0 {5,S}
13 H 0 0 {5,S}
14 H 0 0 {5,S}
15 H 0 0 {6,S}
16 H 0 0 {6,S}
17 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.48,40.03,46.19,51.6,60.35,67.02,77.54],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (12.94,'kcal/mol','+|-',1),
        S298 = (98.08,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "hex-2-yn-4-yl-4-methyl-5-thia",
    molecule = 
"""
1  C 0 0 {2,S} {8,S} {9,S} {10,S}
2  S 0 2 {1,S} {3,S}
3  C 1 0 {2,S} {4,S} {5,S}
4  C 0 0 {3,S} {11,S} {12,S} {13,S}
5  C 0 0 {3,S} {6,T}
6  C 0 0 {5,T} {7,S}
7  C 0 0 {6,S} {14,S} {15,S} {16,S}
8  H 0 0 {1,S}
9  H 0 0 {1,S}
10 H 0 0 {1,S}
11 H 0 0 {4,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
14 H 0 0 {7,S}
15 H 0 0 {7,S}
16 H 0 0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.43,40.98,46.69,51.53,59.27,65.13,74.37],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (63.56,'kcal/mol','+|-',1),
        S298 = (102.15,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    label = "propan-1-yl-1-thione",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 0 {1,S} {6,S} {7,S} {8,S}
3 C 1 0 {1,S} {9,D}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
9 S 0 2 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.15,21.58,24.82,27.62,32.07,35.39,40.53],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (50.85,'kcal/mol','+|-',1),
        S298 = (77.4,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "CS",
    molecule = 
"""
1 C 2S 0 {2,D}
2 S 0  2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.13,7.4,7.69,7.94,8.3,8.51,8.78],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (67,'kcal/mol','+|-',1),
        S298 = (50.32,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""All from [10]""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    label = "C2H5SC2H5",
    molecule = 
"""
1  C 0 0 {3,S} {5,S} {6,S} {7,S}
2  C 0 0 {4,S} {5,S} {8,S} {9,S}
3  C 0 0 {1,S} {10,S} {11,S} {12,S}
4  C 0 0 {2,S} {13,S} {14,S} {15,S}
5  S 0 2 {1,S} {2,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {3,S}
13 H 0 0 {4,S}
14 H 0 0 {4,S}
15 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.96,34.23,39.93,44.84,52.67,58.62,68.04],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-19.88,'kcal/mol','+|-',1),
        S298 = (87.79,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    label = "CH2JCH2SC2H5",
    molecule = 
"""
1  C 0 0 {3,S} {5,S} {6,S} {7,S}
2  C 0 0 {4,S} {5,S} {8,S} {9,S}
3  C 0 0 {1,S} {10,S} {11,S} {12,S}
4  C 1 0 {2,S} {13,S} {14,S}
5  S 0 2 {1,S} {2,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {3,S}
13 H 0 0 {4,S}
14 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.46,34.9,39.74,43.88,50.49,55.56,63.71],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (29.36,'kcal/mol','+|-',1),
        S298 = (91.95,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
    label = "CH2OHSH",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 2 {1,S} {6,S}
3 S 0 2 {1,S} {7,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.79,21.16,22.86,24.19,26.31,28,30.96],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-42.8,'kcal/mol','+|-',1),
        S298 = (68.52,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 128,
    label = "CHCH3OHSH",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {4,S} {5,S}
2  C 0 0 {1,S} {6,S} {7,S} {8,S}
3  O 0 2 {1,S} {9,S}
4  S 0 2 {1,S} {10,S}
5  H 0 0 {1,S}
6  H 0 0 {2,S}
7  H 0 0 {2,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.96,28.75,31.6,33.87,37.49,40.34,45.15],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-52.2,'kcal/mol','+|-',1),
        S298 = (75.71,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
    label = "CH2OHSJ",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 2 {1,S} {6,S}
3 S 1 2 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.89,16.4,18.45,20.05,22.39,24.06,26.71],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-7.88,'kcal/mol','+|-',1),
        S298 = (66.38,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 130,
    label = "CHCH3OHSJ",
    molecule = 
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 0 {1,S} {6,S} {7,S} {8,S}
3 O 0 2 {1,S} {9,S}
4 S 1 2 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
9 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.84,23.81,27.11,29.75,33.66,36.49,40.97],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-16.74,'kcal/mol','+|-',1),
        S298 = (75.02,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 131,
    label = "CHOHS",
    molecule = 
"""
1 C 0 0 {2,S} {3,D} {4,S}
2 O 0 2 {1,S} {5,S}
3 S 0 2 {1,D}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.77,13.96,15.89,17.5,19.92,21.57,23.72],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-27.46,'kcal/mol','+|-',1),
        S298 = (62.24,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 132,
    label = "CHOSH",
    molecule = 
"""
1 C 0 0 {2,S} {3,D} {4,S}
2 S 0 2 {1,S} {5,S}
3 O 0 2 {1,D}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.56,15.27,16.71,17.95,19.92,21.33,23.24],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-29.91,'kcal/mol','+|-',1),
        S298 = (64.42,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 133,
    label = "CHOSJ",
    molecule = 
"""
1 C 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 S 1 2 {1,S}
4 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.23,12.45,13.51,14.4,15.76,16.72,18.11],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (7.85,'kcal/mol','+|-',1),
        S298 = (64.12,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 134,
    label = "COS",
    molecule = 
"""
1 C 0 0 {2,D} {3,D}
2 S 0 2 {1,D}
3 O 0 2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.94,10.96,11.69,12.25,13.07,13.62,14.39],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-33.21,'kcal/mol','+|-',0.25),
        S298 = (55.35,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "thiophene",
    molecule = 
"""
1 C 0 0 {2,S} {3,D} {6,S}
2 C 0 0 {1,S} {4,D} {7,S}
3 C 0 0 {1,D} {5,S} {8,S}
4 C 0 0 {2,D} {5,S} {9,S}
5 S 0 2 {3,S} {4,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
9 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.5,22.92,27.23,30.54,35.23,38.42,43.14],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (27.49,'kcal/mol','+|-',0.24),
        S298 = (67.92,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "DHTP-2-ol",
    molecule = 
"""
1  C 0 0 {2,D} {5,S} {6,S}
2  C 0 0 {1,D} {3,S} {7,S}
3  C 0 0 {2,S} {4,D} {8,S}
4  C 0 0 {3,D} {5,S} {9,S}
5  S 0 2 {1,S} {4,S}
6  O 0 2 {1,S} {10,S}
7  H 0 0 {2,S}
8  H 0 0 {3,S}
9  H 0 0 {4,S}
10 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.92,31.33,36.65,40.86,46.94,51.15,57.51],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-22.43,'kcal/mol','+|-',1),
        S298 = (78.06,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "DHTP-3-ol",
    molecule = 
"""
1  C 0 0 {2,S} {3,D} {6,S}
2  C 0 0 {1,S} {4,D} {7,S}
3  C 0 0 {1,D} {5,S} {8,S}
4  C 0 0 {2,D} {5,S} {9,S}
5  S 0 2 {3,S} {4,S}
6  O 0 2 {1,S} {10,S}
7  H 0 0 {2,S}
8  H 0 0 {3,S}
9  H 0 0 {4,S}
10 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.6,32.36,37.58,41.56,47.31,51.36,57.59],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-21.68,'kcal/mol','+|-',1),
        S298 = (77.71,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "benzaldehyde",
    molecule = 
"""
1  C 0 0 {2,B} {6,B} {9,S}
2  C 0 0 {1,B} {3,B} {10,S}
3  C 0 0 {2,B} {4,B} {11,S}
4  C 0 0 {3,B} {5,B} {12,S}
5  C 0 0 {4,B} {6,B} {13,S}
6  C 0 0 {1,B} {5,B} {7,S}
7  C 0 0 {6,S} {8,D} {14,S}
8  O 0 2 {7,D}
9  H 0 0 {1,S}
10 H 0 0 {2,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
13 H 0 0 {5,S}
14 H 0 0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.37,34.38,41.26,46.87,55.14,60.79,68.78],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-10.03,'kcal/mol','+|-',1),
        S298 = (79.67,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "benzenethial",
    molecule = 
"""
1  C 0 0 {2,B} {6,B} {9,S}
2  C 0 0 {1,B} {3,B} {10,S}
3  C 0 0 {2,B} {4,B} {11,S}
4  C 0 0 {3,B} {5,B} {12,S}
5  C 0 0 {4,B} {6,B} {13,S}
6  C 0 0 {1,B} {5,B} {7,S}
7  C 0 0 {6,S} {8,D} {14,S}
8  S 0 2 {7,D}
9  H 0 0 {1,S}
10 H 0 0 {2,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
13 H 0 0 {5,S}
14 H 0 0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.26,35.41,42.29,47.81,55.83,61.26,68.97],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (43.95,'kcal/mol','+|-',1),
        S298 = (82.19,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    label = "PhCHOHSH",
    molecule = 
"""
1  C 0 0 {2,B} {6,B} {10,S}
2  C 0 0 {1,B} {3,B} {11,S}
3  C 0 0 {2,B} {4,B} {12,S}
4  C 0 0 {3,B} {5,B} {13,S}
5  C 0 0 {4,B} {6,B} {14,S}
6  C 0 0 {1,B} {5,B} {7,S}
7  C 0 0 {6,S} {8,S} {9,S} {15,S}
8  S 0 2 {7,S} {16,S}
9  O 0 2 {7,S} {17,S}
10 H 0 0 {1,S}
11 H 0 0 {2,S}
12 H 0 0 {3,S}
13 H 0 0 {4,S}
14 H 0 0 {5,S}
15 H 0 0 {7,S}
16 H 0 0 {8,S}
17 H 0 0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.16,47.24,54.31,59.84,67.91,73.59,82.2],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-20.54,'kcal/mol','+|-',1),
        S298 = (93.55,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "cyc-C6H10",
    molecule = 
"""
1  C 0 0 {2,D} {6,S} {7,S}
2  C 0 0 {1,D} {3,S} {8,S}
3  C 0 0 {2,S} {4,S} {9,S} {10,S}
4  C 0 0 {3,S} {5,S} {11,S} {12,S}
5  C 0 0 {4,S} {6,S} {13,S} {14,S}
6  C 0 0 {1,S} {5,S} {15,S} {16,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
12 H 0 0 {4,S}
13 H 0 0 {5,S}
14 H 0 0 {5,S}
15 H 0 0 {6,S}
16 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.42,33.39,41.41,48.14,58.47,65.88,76.91],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-1.03,'kcal/mol','+|-',0.23),
        S298 = (74.2,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""see NIST webbook""",
    longDesc = 
u"""

""",
)

entry(
    index = 142,
    label = "cyc-C6H9J-3",
    molecule = 
"""
1  C 0 0 {2,S} {3,S} {7,S} {8,S}
2  C 0 0 {1,S} {5,S} {9,S} {10,S}
3  C 0 0 {1,S} {4,S} {11,S} {12,S}
4  C 0 0 {3,S} {6,D} {13,S}
5  C 1 0 {2,S} {6,S} {14,S}
6  C 0 0 {4,D} {5,S} {15,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 H 0 0 {3,S}
12 H 0 0 {3,S}
13 H 0 0 {4,S}
14 H 0 0 {5,S}
15 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.28,32.36,39.58,45.76,55.33,62.07,71.91],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (30.04,'kcal/mol','+|-',1),
        S298 = (73.79,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""CAC CBS-QB3""",
    longDesc = 
u"""

""",
)

entry(
    index = 143,
    label = "cyc-C6H9J-4",
    molecule = 
"""
1  C 0 0 {2,S} {4,S} {7,S} {8,S}
2  C 0 0 {1,S} {5,S} {9,S} {10,S}
3  C 0 0 {4,S} {6,S} {11,S} {12,S}
4  C 1 0 {1,S} {3,S} {13,S}
5  C 0 0 {2,S} {6,D} {14,S}
6  C 0 0 {3,S} {5,D} {15,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 H 0 0 {3,S}
12 H 0 0 {3,S}
13 H 0 0 {4,S}
14 H 0 0 {5,S}
15 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.02,32.86,39.89,45.96,55.45,62.19,72.03],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (45.73,'kcal/mol','+|-',1),
        S298 = (75.45,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""CAC CBS-QB3""",
    longDesc = 
u"""

""",
)

entry(
    index = 144,
    label = "cyc-C6H8",
    molecule = 
"""
1  C 0 0 {2,D} {6,S} {7,S}
2  C 0 0 {1,D} {3,S} {8,S}
3  C 0 0 {2,S} {4,D} {9,S}
4  C 0 0 {3,D} {5,S} {10,S}
5  C 0 0 {4,S} {6,S} {11,S} {12,S}
6  C 0 0 {1,S} {5,S} {13,S} {14,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
11 H 0 0 {5,S}
12 H 0 0 {5,S}
13 H 0 0 {6,S}
14 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.66,30.72,37.76,43.56,52.27,58.42,67.52],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (25,'kcal/mol','+|-',0.15),
        S298 = (72.52,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""see NIST webbook""",
    longDesc = 
u"""

""",
)

entry(
    index = 145,
    label = "cyc-C6H7J",
    molecule = 
"""
1  C 0 0 {2,D} {6,S} {7,S}
2  C 0 0 {1,D} {3,S} {8,S}
3  C 0 0 {2,S} {4,D} {9,S}
4  C 0 0 {3,D} {5,S} {10,S}
5  C 1 0 {4,S} {6,S} {11,S}
6  C 0 0 {1,S} {5,S} {12,S} {13,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
11 H 0 0 {5,S}
12 H 0 0 {6,S}
13 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.3,29.55,35.87,41.17,49.18,54.69,62.6],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (48.64,'kcal/mol','+|-',1),
        S298 = (70.6,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""CAC CBS-QB3""",
    longDesc = 
u"""

""",
)

entry(
    index = 146,
    label = "benzene",
    molecule = 
"""
1  C 0 0 {2,B} {6,B} {7,S}
2  C 0 0 {1,B} {3,B} {8,S}
3  C 0 0 {2,B} {4,B} {9,S}
4  C 0 0 {3,B} {5,B} {10,S}
5  C 0 0 {4,B} {6,B} {11,S}
6  C 0 0 {1,B} {5,B} {12,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
11 H 0 0 {5,S}
12 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.84,27.13,33.3,38.26,45.52,50.53,57.87],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (19.8,'kcal/mol','+|-',0.2),
        S298 = (64.36,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""H from [12], rest from TRC""",
    longDesc = 
u"""

""",
)

entry(
    index = 147,
    label = "toluene",
    molecule = 
"""
1  C 0 0 {2,B} {6,B} {8,S}
2  C 0 0 {1,B} {3,B} {9,S}
3  C 0 0 {2,B} {4,B} {10,S}
4  C 0 0 {3,B} {5,B} {11,S}
5  C 0 0 {4,B} {6,B} {12,S}
6  C 0 0 {1,B} {5,B} {7,S}
7  C 0 0 {6,S} {13,S} {14,S} {15,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
12 H 0 0 {5,S}
13 H 0 0 {7,S}
14 H 0 0 {7,S}
15 H 0 0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.95,33.44,40.82,46.89,56,62.43,71.94],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (12,'kcal/mol','+|-',0.26),
        S298 = (80.74,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""see NIST webbook, used G3B3 calc for entropy""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "benzyl",
    molecule = 
"""
1  C 0 0 {2,B} {6,B} {8,S}
2  C 0 0 {1,B} {3,B} {9,S}
3  C 0 0 {2,B} {4,B} {10,S}
4  C 0 0 {3,B} {5,B} {11,S}
5  C 0 0 {4,B} {6,B} {12,S}
6  C 0 0 {1,B} {5,B} {7,S}
7  C 1 0 {6,S} {13,S} {14,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
12 H 0 0 {5,S}
13 H 0 0 {7,S}
14 H 0 0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.48,34.85,41.67,47.06,54.92,60.39,68.52],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (49.5,'kcal/mol','+|-',1),
        S298 = (76.31,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""see NIST, used QCISD/cc-pVDZ for Cp""",
    longDesc = 
u"""

""",
)

