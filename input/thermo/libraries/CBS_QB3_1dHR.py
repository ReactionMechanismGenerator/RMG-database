#!/usr/bin/env python
# encoding: utf-8

name = "CBS_QB3_1dHR"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    label = "sBuOH",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 0 {1,S} {3,S} {5,S} {9,S}
3  C 0 0 {2,S} {4,S} {10,S} {11,S}
4  C 0 0 {3,S} {12,S} {13,S} {14,S}
5  O 0 2 {2,S} {15,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
14 H 0 0 {4,S}
15 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.21,34.5,40.21,45.08,52.8,58.62,67.9],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-70.51,'kcal/mol','+|-',2),
        S298 = (83.05,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "CH2CH[OH]C2H5",
    molecule = 
"""
1  C 1 0 {2,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {5,S} {8,S}
3  C 0 0 {2,S} {4,S} {9,S} {10,S}
4  C 0 0 {3,S} {11,S} {12,S} {13,S}
5  O 0 2 {2,S} {14,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
14 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.32,34.19,39.3,43.58,50.27,55.31,63.42],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-20.29,'kcal/mol','+|-',2),
        S298 = (85.12,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "CH3C[OH]C2H5",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 1 0 {1,S} {3,S} {5,S}
3  C 0 0 {2,S} {4,S} {9,S} {10,S}
4  C 0 0 {3,S} {11,S} {12,S} {13,S}
5  O 0 2 {2,S} {14,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
14 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.09,32.67,37.82,42.25,49.33,54.67,63.16],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-28.11,'kcal/mol','+|-',2),
        S298 = (85.48,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "CH3CH[O]C2H5",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 0 {1,S} {3,S} {5,S} {9,S}
3  C 0 0 {2,S} {4,S} {10,S} {11,S}
4  C 0 0 {3,S} {12,S} {13,S} {14,S}
5  O 1 2 {2,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
14 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.15,33.15,38.5,43.06,50.3,55.76,64.36],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-16.68,'kcal/mol','+|-',2),
        S298 = (81.26,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    label = "CH3CH[OH]CHCH3",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 0 {1,S} {3,S} {5,S} {9,S}
3  C 1 0 {2,S} {4,S} {10,S}
4  C 0 0 {3,S} {11,S} {12,S} {13,S}
5  O 0 2 {2,S} {14,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
14 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.6,34.49,38.99,42.99,49.61,54.76,63.12],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-22.93,'kcal/mol','+|-',2),
        S298 = (85.73,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    label = "CH3CH[OH]CH2CH2",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 0 {1,S} {3,S} {5,S} {9,S}
3  C 0 0 {2,S} {4,S} {10,S} {11,S}
4  C 1 0 {3,S} {12,S} {13,S}
5  O 0 2 {2,S} {14,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
14 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.95,34.38,39.34,43.58,50.3,55.39,63.54],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-21.44,'kcal/mol','+|-',2),
        S298 = (85.19,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    label = "HOCHC2H5",
    molecule = 
"""
1  O 0 2 {2,S} {5,S}
2  C 1 0 {1,S} {3,S} {6,S}
3  C 0 0 {2,S} {4,S} {7,S} {8,S}
4  C 0 0 {3,S} {9,S} {10,S} {11,S}
5  H 0 0 {1,S}
6  H 0 0 {2,S}
7  H 0 0 {3,S}
8  H 0 0 {3,S}
9  H 0 0 {4,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.59,25.27,29.45,32.98,38.48,42.6,49.12],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-18.03,'kcal/mol','+|-',2),
        S298 = (77.53,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    label = "HOCHCH3",
    molecule = 
"""
1 O 0 2 {2,S} {4,S}
2 C 1 0 {1,S} {3,S} {5,S}
3 C 0 0 {2,S} {6,S} {7,S} {8,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {3,S}
7 H 0 0 {3,S}
8 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.6,18.61,21.4,23.78,27.55,30.37,34.91],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-13.27,'kcal/mol','+|-',2),
        S298 = (68.07,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    label = "CH3CH[OH]CH2",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {4,S} {8,S}
3  C 1 0 {2,S} {9,S} {10,S}
4  O 0 2 {2,S} {11,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.88,27.27,31.04,34.18,39.13,42.92,49.13],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-15.05,'kcal/mol','+|-',2),
        S298 = (76.17,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    label = "tBuOH",
    molecule = 
"""
1  O 0 2 {2,S} {6,S}
2  C 0 0 {1,S} {3,S} {4,S} {5,S}
3  C 0 0 {2,S} {7,S} {8,S} {9,S}
4  C 0 0 {2,S} {10,S} {11,S} {12,S}
5  C 0 0 {2,S} {13,S} {14,S} {15,S}
6  H 0 0 {1,S}
7  H 0 0 {3,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
12 H 0 0 {4,S}
13 H 0 0 {5,S}
14 H 0 0 {5,S}
15 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.26,35.02,40.83,45.65,53.18,58.85,67.96],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-75.87,'kcal/mol','+|-',2),
        S298 = (78.3,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    label = "OC[CH3]3",
    molecule = 
"""
1  O 1 2 {2,S}
2  C 0 0 {1,S} {3,S} {4,S} {5,S}
3  C 0 0 {2,S} {6,S} {7,S} {8,S}
4  C 0 0 {2,S} {9,S} {10,S} {11,S}
5  C 0 0 {2,S} {12,S} {13,S} {14,S}
6  H 0 0 {3,S}
7  H 0 0 {3,S}
8  H 0 0 {3,S}
9  H 0 0 {4,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
12 H 0 0 {5,S}
13 H 0 0 {5,S}
14 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.25,33.57,38.95,43.42,50.47,55.8,64.28],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-21.12,'kcal/mol','+|-',2),
        S298 = (76.85,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    label = "HOC[CH2][CH3]2",
    molecule = 
"""
1  O 0 2 {2,S} {6,S}
2  C 0 0 {1,S} {3,S} {4,S} {5,S}
3  C 1 0 {2,S} {7,S} {8,S}
4  C 0 0 {2,S} {9,S} {10,S} {11,S}
5  C 0 0 {2,S} {12,S} {13,S} {14,S}
6  H 0 0 {1,S}
7  H 0 0 {3,S}
8  H 0 0 {3,S}
9  H 0 0 {4,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
12 H 0 0 {5,S}
13 H 0 0 {5,S}
14 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.21,35.23,40.22,44.31,50.69,55.53,63.46],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-24.74,'kcal/mol','+|-',2),
        S298 = (81.5,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    label = "tC4H9",
    molecule = 
"""
1  C 1 0 {2,S} {3,S} {4,S}
2  C 0 0 {1,S} {5,S} {6,S} {7,S}
3  C 0 0 {1,S} {8,S} {9,S} {10,S}
4  C 0 0 {1,S} {11,S} {12,S} {13,S}
5  H 0 0 {2,S}
6  H 0 0 {2,S}
7  H 0 0 {2,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.47,26.48,31.51,36.05,43.52,49.21,58.13],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (12.48,'kcal/mol','+|-',2),
        S298 = (76.49,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    label = "HOC[CH3]2",
    molecule = 
"""
1  O 0 2 {2,S} {5,S}
2  C 1 0 {1,S} {3,S} {4,S}
3  C 0 0 {2,S} {6,S} {7,S} {8,S}
4  C 0 0 {2,S} {9,S} {10,S} {11,S}
5  H 0 0 {1,S}
6  H 0 0 {3,S}
7  H 0 0 {3,S}
8  H 0 0 {3,S}
9  H 0 0 {4,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.59,25.81,29.71,33.1,38.53,42.63,49.16],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-23.5,'kcal/mol','+|-',2),
        S298 = (74.7,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 15,
    label = "C3H5OJ(17)",
    molecule = 
"""
1 C 0 0 {2,S} {5,S} {6,S} {7,S}
2 C 1 0 {1,S} {3,D}
3 C 0 0 {2,D} {4,S} {8,S}
4 O 0 2 {3,S} {9,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {3,S}
9 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.21,23.32,26.93,29.77,33.8,36.58,40.96],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (22.25,'kcal/mol','+|-',2),
        S298 = (72.17,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    label = "C4H7O_1_2",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 1 0 {1,S} {3,S} {9,S}
3  C 0 0 {2,S} {4,D} {10,S}
4  C 0 0 {3,D} {5,S} {11,S}
5  O 0 2 {4,S} {12,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
12 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.48,30.4,34.84,38.6,44.45,48.8,55.64],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-8.11,'kcal/mol','+|-',2),
        S298 = (80.56,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    label = "C4H7O-13",
    molecule = 
"""
1  C 0 0 {2,D} {6,S} {7,S}
2  C 0 0 {1,D} {3,S} {8,S}
3  C 1 0 {2,S} {4,S} {9,S}
4  C 0 0 {3,S} {5,S} {10,S} {11,S}
5  O 0 2 {4,S} {12,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
12 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.06,31.99,36.04,39.42,44.8,48.92,55.62],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-2.41,'kcal/mol','+|-',2),
        S298 = (79.66,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 18,
    label = "C4H7OJ(13)",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 1 0 {1,S} {3,S} {9,S}
3  C 0 0 {2,S} {4,S} {10,S} {11,S}
4  C 0 0 {3,S} {5,D} {12,S}
5  O 0 2 {4,D}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.05,27.77,32.28,36.23,42.54,47.26,54.54],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-2.61,'kcal/mol','+|-',2),
        S298 = (86.64,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    label = "CH2CHCCHOH",
    molecule = 
"""
1  C 0 0 {2,D} {6,S} {7,S}
2  C 0 0 {1,D} {3,S} {8,S}
3  C 1 0 {2,S} {4,D}
4  C 0 0 {3,D} {5,S} {9,S}
5  O 0 2 {4,S} {10,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {4,S}
10 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.22,28.44,32.51,35.55,39.78,42.75,47.48],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (38.05,'kcal/mol','+|-',2),
        S298 = (76.08,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    label = "CH3CHCHCO",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 0 {1,S} {3,D} {9,S}
3  C 0 0 {2,D} {4,S} {10,S}
4  C 1 0 {3,S} {5,D}
5  O 0 2 {4,D}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.13,26.48,30.11,33.1,37.72,41.11,46.34],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (14.06,'kcal/mol','+|-',2),
        S298 = (75.12,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    label = "CHCCHCHOH",
    molecule = 
"""
1 C 0 0 {2,T} {6,S}
2 C 0 0 {1,T} {3,S}
3 C 0 0 {2,S} {4,D} {7,S}
4 C 0 0 {3,D} {5,S} {8,S}
5 O 0 2 {4,S} {9,S}
6 H 0 0 {1,S}
7 H 0 0 {3,S}
8 H 0 0 {4,S}
9 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.23,26.36,29.54,32.03,35.69,38.3,42.41],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (28.19,'kcal/mol','+|-',2),
        S298 = (73.91,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    label = "iC4H5OJ(14)",
    molecule = 
"""
1  C 0 0 {2,D} {6,S} {7,S}
2  C 0 0 {1,D} {3,S} {5,S}
3  C 1 0 {2,S} {4,D}
4  O 0 2 {3,D}
5  C 0 0 {2,S} {8,S} {9,S} {10,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {5,S}
9  H 0 0 {5,S}
10 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.34,26.71,30.14,32.93,37.32,40.67,46],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (14.08,'kcal/mol','+|-',2),
        S298 = (76.7,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    label = "iC4H5OJ(15)",
    molecule = 
"""
1  C 0 0 {2,D} {6,S} {7,S}
2  C 0 0 {1,D} {3,S} {5,S}
3  C 0 0 {2,S} {4,D} {8,S}
4  O 0 2 {3,D}
5  C 1 0 {2,S} {9,S} {10,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {3,S}
9  H 0 0 {5,S}
10 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.08,26.8,30.77,34.04,39.05,42.66,48.02],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (12.77,'kcal/mol','+|-',2),
        S298 = (74.84,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    label = "iC4H7OJ(17)",
    molecule = 
"""
1  C 0 0 {2,D} {6,S} {7,S}
2  C 0 0 {1,D} {3,S} {5,S}
3  C 0 0 {2,S} {4,S} {8,S} {9,S}
4  O 0 2 {3,S} {10,S}
5  C 1 0 {2,S} {11,S} {12,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
11 H 0 0 {5,S}
12 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.6,30.87,35.26,38.89,44.56,48.86,55.75],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-1.97,'kcal/mol','+|-',2),
        S298 = (78.93,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    label = "iC4H7OJ(48)",
    molecule = 
"""
1  C 1 0 {2,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {5,S} {8,S}
3  C 0 0 {2,S} {4,D} {9,S}
4  O 0 2 {3,D}
5  C 0 0 {2,S} {10,S} {11,S} {12,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {5,S}
11 H 0 0 {5,S}
12 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.44,29.81,33.87,37.43,43.22,47.64,54.64],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-0.88,'kcal/mol','+|-',2),
        S298 = (82.81,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    label = "iC4H7OJ(51)",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 0 {1,S} {3,S} {5,S} {9,S}
3  C 1 0 {2,S} {4,D}
4  O 0 2 {3,D}
5  C 0 0 {2,S} {10,S} {11,S} {12,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {5,S}
11 H 0 0 {5,S}
12 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.27,27.89,32.25,36.12,42.42,47.16,54.56],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-14.49,'kcal/mol','+|-',2),
        S298 = (80.22,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
    label = "tSPC(1286)",
    molecule = 
"""
1 O 0 2 {2,S} {6,S}
2 O 1 2 {1,S}
3 O 0 2 {6,D}
4 C 0 0 {5,D} {8,S} {9,S}
5 C 0 0 {4,D} {6,S} {7,S}
6 C 0 0 {1,S} {3,D} {5,S}
7 H 0 0 {5,S}
8 H 0 0 {4,S}
9 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.68,26.88,30.42,33.26,37.32,39.96,43.51],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-11,'kcal/mol','+|-',2),
        S298 = (79.85,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("Thu Feb  6 13:58:32 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> updated this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 28,
    label = "tSPC(1553)",
    molecule = 
"""
1 O 1 2 {5,S}
2 O 0 2 {5,D}
3 C 0 0 {4,D} {7,S} {8,S}
4 C 0 0 {3,D} {5,S} {6,S}
5 C 0 0 {1,S} {2,D} {4,S}
6 H 0 0 {4,S}
7 H 0 0 {3,S}
8 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.28,22.22,25.51,28.12,31.86,34.37,37.97],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-19.27,'kcal/mol','+|-',2),
        S298 = (73.08,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
        ("Thu Feb  6 13:58:32 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> updated this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 29,
    label = "tSPC(343)",
    molecule = 
"""
1  O 1 2 {6,S}
2  O 0 2 {5,D}
3  C 0 0 {4,D} {7,S} {8,S}
4  C 0 0 {3,D} {5,S} {6,S}
5  C 0 0 {2,D} {4,S} {9,S}
6  C 0 0 {1,S} {4,S} {10,S} {11,S}
7  H 0 0 {3,S}
8  H 0 0 {3,S}
9  H 0 0 {5,S}
10 H 0 0 {6,S}
11 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.61,31.29,35.94,39.68,45.17,48.86,53.87],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-6.43,'kcal/mol','+|-',2),
        S298 = (80.94,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
    label = "nC4H10O",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 0 {2,S} {4,S} {11,S} {12,S}
4  C 0 0 {3,S} {5,S} {13,S} {14,S}
5  O 0 2 {4,S} {15,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 H 0 0 {3,S}
12 H 0 0 {3,S}
13 H 0 0 {4,S}
14 H 0 0 {4,S}
15 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.32,33.59,39.43,44.44,52.4,58.38,67.83],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-66.09,'kcal/mol','+|-',2),
        S298 = (85.9,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 31,
    label = "C4H9O-1",
    molecule = 
"""
1  C 1 0 {2,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 0 {2,S} {4,S} {10,S} {11,S}
4  C 0 0 {3,S} {5,S} {12,S} {13,S}
5  O 0 2 {4,S} {14,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
14 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.95,32.82,38.15,42.65,49.68,54.93,63.28],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-16.27,'kcal/mol','+|-',2),
        S298 = (88.99,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 32,
    label = "C4H9O-2",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 1 0 {1,S} {3,S} {9,S}
3  C 0 0 {2,S} {4,S} {10,S} {11,S}
4  C 0 0 {3,S} {5,S} {12,S} {13,S}
5  O 0 2 {4,S} {14,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
14 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.35,32.64,37.79,42.3,49.47,54.84,63.3],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-19.7,'kcal/mol','+|-',2),
        S298 = (88.4,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
    label = "C4H9O-3",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 0 {1,S} {3,S} {9,S} {10,S}
3  C 1 0 {2,S} {4,S} {11,S}
4  C 0 0 {3,S} {5,S} {12,S} {13,S}
5  O 0 2 {4,S} {14,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
14 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.25,33.57,38.32,42.48,49.29,54.55,63.04],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-18.5,'kcal/mol','+|-',2),
        S298 = (88.73,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 34,
    label = "C4H9O-4",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 0 {2,S} {4,S} {11,S} {12,S}
4  C 1 0 {3,S} {5,S} {13,S}
5  O 0 2 {4,S} {14,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 H 0 0 {3,S}
12 H 0 0 {3,S}
13 H 0 0 {4,S}
14 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.57,32.71,38.13,42.67,49.73,54.99,63.34],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-23.13,'kcal/mol','+|-',2),
        S298 = (86.3,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 35,
    label = "C4H9O-5",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 0 {2,S} {4,S} {11,S} {12,S}
4  C 0 0 {3,S} {5,S} {13,S} {14,S}
5  O 1 2 {4,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 H 0 0 {3,S}
12 H 0 0 {3,S}
13 H 0 0 {4,S}
14 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.61,32.68,38.16,42.84,50.26,55.81,64.46],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-13.43,'kcal/mol','+|-',2),
        S298 = (82.96,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 36,
    label = "iBuOH",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 0 {1,S} {3,S} {5,S} {9,S}
3  C 0 0 {2,S} {4,S} {10,S} {11,S}
4  O 0 2 {3,S} {12,S}
5  C 0 0 {2,S} {13,S} {14,S} {15,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
13 H 0 0 {5,S}
14 H 0 0 {5,S}
15 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.21,33.74,39.68,44.72,52.64,58.55,67.9],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-68.34,'kcal/mol','+|-',2),
        S298 = (83.38,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 37,
    label = "C4H9Oi1",
    molecule = 
"""
1  C 1 0 {2,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {5,S} {8,S}
3  C 0 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 2 {3,S} {11,S}
5  C 0 0 {2,S} {12,S} {13,S} {14,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
12 H 0 0 {5,S}
13 H 0 0 {5,S}
14 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.03,33.68,38.81,43.16,49.99,55.12,63.33],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-18.28,'kcal/mol','+|-',2),
        S298 = (86.11,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 38,
    label = "C4H9Oi2",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 1 0 {1,S} {3,S} {5,S}
3  C 0 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 2 {3,S} {11,S}
5  C 0 0 {2,S} {12,S} {13,S} {14,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
12 H 0 0 {5,S}
13 H 0 0 {5,S}
14 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.11,32.27,37.18,41.54,48.7,54.18,62.91],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-22.94,'kcal/mol','+|-',2),
        S298 = (84.64,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 39,
    label = "C4H9Oi3",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 0 {1,S} {3,S} {5,S} {9,S}
3  C 1 0 {2,S} {4,S} {10,S}
4  O 0 2 {3,S} {11,S}
5  C 0 0 {2,S} {12,S} {13,S} {14,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
12 H 0 0 {5,S}
13 H 0 0 {5,S}
14 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.12,33.12,38.42,42.88,49.87,55.11,63.43],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-24.24,'kcal/mol','+|-',2),
        S298 = (84.93,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 40,
    label = "C4H9Oi4",
    molecule = 
"""
1  C 0 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 0 {1,S} {3,S} {5,S} {9,S}
3  C 0 0 {2,S} {4,S} {10,S} {11,S}
4  O 1 2 {3,S}
5  C 0 0 {2,S} {12,S} {13,S} {14,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {1,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {5,S}
13 H 0 0 {5,S}
14 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.32,32.81,38.45,43.15,50.5,55.97,64.52],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (-15.78,'kcal/mol','+|-',2),
        S298 = (80.19,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 41,
    label = "C4H7OJ(9)",
    molecule = 
"""
1  C 1 0 {2,S} {6,S} {7,S}
2  C 0 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 0 {2,S} {4,D} {10,S}
4  C 0 0 {3,D} {5,S} {11,S}
5  O 0 2 {4,S} {12,S}
6  H 0 0 {1,S}
7  H 0 0 {1,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
12 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.26,31.38,35.64,39.11,44.43,48.41,54.85],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (9.68,'kcal/mol','+|-',2),
        S298 = (81,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 42,
    label = "fulvalene",
    molecule = 
"""
1  C 0 0 {2,S} {5,S} {6,D}
2  C 0 0 {1,S} {3,D} {11,S}
3  C 0 0 {2,D} {4,S} {12,S}
4  C 0 0 {3,S} {5,D} {13,S}
5  C 0 0 {1,S} {4,D} {14,S}
6  C 0 0 {1,D} {7,S} {10,S}
7  C 0 0 {6,S} {8,D} {15,S}
8  C 0 0 {7,D} {9,S} {16,S}
9  C 0 0 {8,S} {10,D} {17,S}
10 C 0 0 {6,S} {9,D} {18,S}
11 H 0 0 {2,S}
12 H 0 0 {3,S}
13 H 0 0 {4,S}
14 H 0 0 {5,S}
15 H 0 0 {7,S}
16 H 0 0 {8,S}
17 H 0 0 {9,S}
18 H 0 0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.71,44.95,54.19,61.46,71.89,78.98,89.33],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (90.89,'kcal/mol','+|-',2),
        S298 = (84.6,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 43,
    label = "C5H4C5H5",
    molecule = 
"""
1  C 1 0 {2,S} {5,S} {6,S}
2  C 0 0 {1,S} {3,D} {11,S}
3  C 0 0 {2,D} {4,S} {12,S}
4  C 0 0 {3,S} {5,D} {13,S}
5  C 0 0 {1,S} {4,D} {14,S}
6  C 0 0 {1,S} {7,S} {10,S} {15,S}
7  C 0 0 {6,S} {8,D} {16,S}
8  C 0 0 {7,D} {9,S} {17,S}
9  C 0 0 {8,S} {10,D} {18,S}
10 C 0 0 {6,S} {9,D} {19,S}
11 H 0 0 {2,S}
12 H 0 0 {3,S}
13 H 0 0 {4,S}
14 H 0 0 {5,S}
15 H 0 0 {6,S}
16 H 0 0 {7,S}
17 H 0 0 {8,S}
18 H 0 0 {9,S}
19 H 0 0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.24,47.77,57.22,64.69,75.48,82.89,93.75],'cal/(mol*K)','+|-',[1,1,1,1,1,1,1]),
        H298 = (100.63,'kcal/mol','+|-',2),
        S298 = (93.09,'cal/(mol*K)','+|-',1),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 12:27:50 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

