#!/usr/bin/env python
# encoding: utf-8

name = "bio_oil"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "BENZENE",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {6,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {8,S}
3  C u0 p0 c0 {2,B} {4,B} {9,S}
4  C u0 p0 c0 {3,B} {5,B} {10,S}
5  C u0 p0 c0 {4,B} {6,B} {11,S}
6  C u0 p0 c0 {1,B} {5,B} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.72,26.74,33.02,38.24,45.41,50.53,57.61],'cal/(mol*K)'),
        H298 = (19.81,'kcal/mol'),
        S298 = (64.32,'cal/(mol*K)'),
    ),
    shortDesc = u"""Burcat Third Millenium Database""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "FULVENE",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,D}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,D} {5,S} {8,S}
5  C u0 p0 c0 {3,D} {4,S} {9,S}
6  C u0 p0 c0 {1,D} {11,S} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.73,28.59,34.55,39.45,46.22,51.09,57.91],'cal/(mol*K)'),
        H298 = (56.6,'kcal/mol'),
        S298 = (70.29,'cal/(mol*K)'),
    ),
    shortDesc = u"""Burcat Third Millenium Database""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "FURAN",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 C u0 p0 c0 {2,S} {4,D} {8,S}
4 C u0 p0 c0 {3,D} {5,S} {9,S}
5 O u0 p2 c0 {1,S} {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.73,21.02,25.69,29.48,34.47,37.99,42.8],'cal/(mol*K)'),
        H298 = (-8.29,'kcal/mol'),
        S298 = (63.87,'cal/(mol*K)'),
    ),
    shortDesc = u"""Burcat Third Millenium Database""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "Benzaldehyde",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,D} {9,S}
2  C u0 p0 c0 {1,S} {3,B} {7,B}
3  C u0 p0 c0 {2,B} {4,B} {10,S}
4  C u0 p0 c0 {3,B} {5,B} {11,S}
5  C u0 p0 c0 {4,B} {6,B} {12,S}
6  C u0 p0 c0 {5,B} {7,B} {13,S}
7  C u0 p0 c0 {2,B} {6,B} {14,S}
8  O u0 p2 c0 {1,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.86,35.04,41.86,47.45,55.52,60.95,68.54],'cal/(mol*K)'),
        H298 = (-8.8,'kcal/mol'),
        S298 = (80.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""Burcat Third Millenium Database""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "styrene",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,B} {8,B}
4  C u0 p0 c0 {3,B} {5,B} {12,S}
5  C u0 p0 c0 {4,B} {6,B} {13,S}
6  C u0 p0 c0 {5,B} {7,B} {14,S}
7  C u0 p0 c0 {6,B} {8,B} {15,S}
8  C u0 p0 c0 {3,B} {7,B} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.9,37.94,45.92,52.52,61.7,68.27,77.71],'cal/(mol*K)'),
        H298 = (35.44,'kcal/mol'),
        S298 = (82.39,'cal/(mol*K)'),
    ),
    shortDesc = u"""Burcat Third Millenium Database""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "phenol",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {6,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {8,S}
3  C u0 p0 c0 {2,B} {4,B} {9,S}
4  C u0 p0 c0 {3,B} {5,B} {10,S}
5  C u0 p0 c0 {4,B} {6,B} {11,S}
6  C u0 p0 c0 {1,B} {5,B} {12,S}
7  O u0 p2 c0 {1,S} {13,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.85,32.29,38.63,43.75,50.73,55.64,62.53],'cal/(mol*K)'),
        H298 = (-23.04,'kcal/mol'),
        S298 = (75.33,'cal/(mol*K)'),
    ),
    shortDesc = u"""Burcat Third Millenium Database""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "Phenoxy",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,B} {7,B}
3  C u0 p0 c0 {2,B} {4,B} {8,S}
4  C u0 p0 c0 {3,B} {5,B} {9,S}
5  C u0 p0 c0 {4,B} {6,B} {10,S}
6  C u0 p0 c0 {5,B} {7,B} {11,S}
7  C u0 p0 c0 {2,B} {6,B} {12,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.48,30.34,36.1,40.72,46.94,51.29,57.24],'cal/(mol*K)'),
        H298 = (12.91,'kcal/mol'),
        S298 = (74.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""Burcat Third Millenium Database""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "TOLUENE",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {6,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {8,S}
3  C u0 p0 c0 {2,B} {4,B} {9,S}
4  C u0 p0 c0 {3,B} {5,B} {10,S}
5  C u0 p0 c0 {4,B} {6,B} {11,S}
6  C u0 p0 c0 {1,B} {5,B} {12,S}
7  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.84,33.1,40.59,46.93,55.94,62.45,71.58],'cal/(mol*K)'),
        H298 = (11.99,'kcal/mol'),
        S298 = (76.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Burcat Third Millenium Database""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "PHENYL",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {8,S}
2  C u0 p0 c0 {1,B} {4,B} {7,S}
3  C u0 p0 c0 {1,B} {5,B} {9,S}
4  C u0 p0 c0 {2,B} {6,B} {10,S}
5  C u0 p0 c0 {3,B} {6,B} {11,S}
6  C u1 p0 c0 {4,B} {5,B}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.44,24.81,30.39,34.95,41.06,45.38,51.29],'cal/(mol*K)'),
        H298 = (81.2,'kcal/mol'),
        S298 = (68.36,'cal/(mol*K)'),
    ),
    shortDesc = u"""Burcat Third Millenium Database""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "FULVENYL",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,D}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,D} {5,S} {8,S}
5  C u0 p0 c0 {3,D} {4,S} {9,S}
6  C u1 p0 c0 {1,D} {11,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.38,28.84,34.21,38.46,44.16,48.18,53.75],'cal/(mol*K)'),
        H298 = (117.2,'kcal/mol'),
        S298 = (73.39,'cal/(mol*K)'),
    ),
    shortDesc = u"""Burcat Third Millenium Database""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "BENZYL",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {6,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {8,S}
3  C u0 p0 c0 {2,B} {4,B} {9,S}
4  C u0 p0 c0 {3,B} {5,B} {10,S}
5  C u0 p0 c0 {4,B} {6,B} {11,S}
6  C u0 p0 c0 {1,B} {5,B} {12,S}
7  C u1 p0 c0 {1,S} {13,S} {14,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.38,34.53,41.47,47.12,55.04,60.77,68.47],'cal/(mol*K)'),
        H298 = (49.71,'kcal/mol'),
        S298 = (76.05,'cal/(mol*K)'),
    ),
    shortDesc = u"""Burcat Third Millenium Database""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "EthBenzene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {4,B} {8,B}
4  C u0 p0 c0 {3,B} {5,B} {14,S}
5  C u0 p0 c0 {4,B} {6,B} {15,S}
6  C u0 p0 c0 {5,B} {7,B} {16,S}
7  C u0 p0 c0 {6,B} {8,B} {17,S}
8  C u0 p0 c0 {3,B} {7,B} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([31.21,41.14,49.99,57.43,68.06,75.81,86.94],'cal/(mol*K)'),
        H298 = (7.12,'kcal/mol'),
        S298 = (84.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""Burcat Third Millenium Database""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "Naphthalene",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {4,B} {5,B}
2  C u0 p0 c0 {1,B} {3,B} {6,B}
3  C u0 p0 c0 {2,B} {7,B} {11,S}
4  C u0 p0 c0 {1,B} {8,B} {14,S}
5  C u0 p0 c0 {1,B} {9,B} {15,S}
6  C u0 p0 c0 {2,B} {10,B} {18,S}
7  C u0 p0 c0 {3,B} {8,B} {12,S}
8  C u0 p0 c0 {4,B} {7,B} {13,S}
9  C u0 p0 c0 {5,B} {10,B} {16,S}
10 C u0 p0 c0 {6,B} {9,B} {17,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([31.74,42.77,52.39,60.31,71.19,78.79,89.1],'cal/(mol*K)'),
        H298 = (35.99,'kcal/mol'),
        S298 = (79.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""Burcat Third Millenium Database""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "CPD",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {5,S} {6,S}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {5,S} {9,S}
5  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.13,24.46,30.13,34.82,41.23,45.87,52.36],'cal/(mol*K)'),
        H298 = (32.1,'kcal/mol'),
        S298 = (65.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""Burcat Third Millenium Database""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "CPDYL",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {5,S} {6,S}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {5,S} {9,S}
5  C u1 p0 c0 {1,S} {4,S} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.43,24.47,29.58,33.63,38.96,42.77,48.06],'cal/(mol*K)'),
        H298 = (63.6,'kcal/mol'),
        S298 = (66.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""Burcat Third Millenium Database""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "StyreneRad",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,D} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,B} {8,B}
4  C u0 p0 c0 {3,B} {5,B} {11,S}
5  C u0 p0 c0 {4,B} {6,B} {12,S}
6  C u0 p0 c0 {5,B} {7,B} {13,S}
7  C u0 p0 c0 {6,B} {8,B} {14,S}
8  C u0 p0 c0 {3,B} {7,B} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.64,39.54,46.98,52.89,60.81,66.32,73.88],'cal/(mol*K)'),
        H298 = (93,'kcal/mol'),
        S298 = (82.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""Burcat Third Millenium Database""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "EthBenzRad",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u1 p0 c0 {1,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,B} {8,B}
4  C u0 p0 c0 {3,B} {5,B} {13,S}
5  C u0 p0 c0 {4,B} {6,B} {14,S}
6  C u0 p0 c0 {5,B} {7,B} {15,S}
7  C u0 p0 c0 {6,B} {8,B} {16,S}
8  C u0 p0 c0 {3,B} {7,B} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([31.38,40.53,48.48,55.05,64.36,71.12,80.89],'cal/(mol*K)'),
        H298 = (56.81,'kcal/mol'),
        S298 = (87.15,'cal/(mol*K)'),
    ),
    shortDesc = u"""Burcat Third Millenium Database""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "Anisole",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {6,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {9,S}
3  C u0 p0 c0 {2,B} {4,B} {10,S}
4  C u0 p0 c0 {3,B} {5,B} {11,S}
5  C u0 p0 c0 {4,B} {6,B} {12,S}
6  C u0 p0 c0 {1,B} {5,B} {13,S}
7  O u0 p2 c0 {1,S} {8,S}
8  C u0 p0 c0 {7,S} {14,S} {15,S} {16,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.67,38.91,46.53,52.77,62.06,68.33,77.22],'cal/(mol*K)'),
        H298 = (-17.1,'kcal/mol'),
        S298 = (84.01,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated using Group additivity methods""",
    longDesc = 
u"""
Pecullan, M. Brezinsky, K. Glassman, I. "Pyrolysis and Oxidation of Anisole near 100K". J Phys Chem A. 1997 101, 3305-3316
""",
)

entry(
    index = 18,
    label = "C6H5OCH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {6,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {9,S}
3  C u0 p0 c0 {2,B} {4,B} {10,S}
4  C u0 p0 c0 {3,B} {5,B} {11,S}
5  C u0 p0 c0 {4,B} {6,B} {12,S}
6  C u0 p0 c0 {1,B} {5,B} {13,S}
7  O u0 p2 c0 {1,S} {8,S}
8  C u1 p0 c0 {7,S} {14,S} {15,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.35,37.07,43.97,49.42,57.08,62.04,69.8],'cal/(mol*K)'),
        H298 = (79.99,'kcal/mol'),
        S298 = (88.28,'cal/(mol*K)'),
    ),
    shortDesc = u"""Estimated using Group additivity methods""",
    longDesc = 
u"""
Pecullan, M. Brezinsky, K. Glassman, I. "Pyrolysis and Oxidation of Anisole near 100K". J Phys Chem A. 1997 101, 3305-3316
""",
)

