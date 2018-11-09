#!/usr/bin/env python
# encoding: utf-8

name = "naphthalene_H"
shortDesc = u"Cyclopentadiene pyrolysis in the presence of ethene"
longDesc = u"""
Calculated at the CBS-QB3 level

Citation:

Aaron G. Vandeputte, Shamel S. Merchant, Marko R. Djokic, Kevin M. Van Geem, 
Guy B. Marin, William H. Green, "Detailed study of cyclopentadiene pyrolysis in the 
presence of ethene: realistic pathways from C5H5 to naphthalene." (2016)
"""
entry(
    index = 0,
    label = "biCPD3ene",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {4,S}
2  C u0 p0 c0 {1,D} {5,S} {6,S}
3  C u0 p0 c0 {1,S} {7,D} {12,S}
4  C u0 p0 c0 {1,S} {8,D} {13,S}
5  C u0 p0 c0 {2,S} {9,D} {15,S}
6  C u0 p0 c0 {2,S} {10,D} {18,S}
7  C u0 p0 c0 {3,D} {8,S} {11,S}
8  C u0 p0 c0 {4,D} {7,S} {14,S}
9  C u0 p0 c0 {5,D} {10,S} {16,S}
10 C u0 p0 c0 {6,D} {9,S} {17,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.63,44.87,54.11,61.4,71.86,78.97,89.36],'cal/(mol*K)'),
        H298 = (93.37,'kcal/mol'),
        S298 = (87.33,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "adducta",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {6,D}
3  C u0 p0 c0 {1,S} {7,D} {12,S}
4  C u0 p0 c0 {1,S} {8,D} {13,S}
5  C u1 p0 c0 {2,S} {9,S} {14,S}
6  C u0 p0 c0 {2,D} {10,S} {17,S}
7  C u0 p0 c0 {3,D} {8,S} {18,S}
8  C u0 p0 c0 {4,D} {7,S} {19,S}
9  C u0 p0 c0 {5,S} {10,D} {15,S}
10 C u0 p0 c0 {6,S} {9,D} {16,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.43,47.36,57.15,64.83,75.84,83.35,94.38],'cal/(mol*K)'),
        H298 = (103.26,'kcal/mol'),
        S298 = (91.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "adductb",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {5,D}
3  C u0 p0 c0 {2,S} {6,D} {7,S}
4  C u0 p0 c0 {1,S} {8,D} {13,S}
5  C u0 p0 c0 {2,D} {8,S} {14,S}
6  C u0 p0 c0 {3,D} {9,S} {16,S}
7  C u1 p0 c0 {3,S} {10,S} {19,S}
8  C u0 p0 c0 {4,D} {5,S} {15,S}
9  C u0 p0 c0 {6,S} {10,D} {17,S}
10 C u0 p0 c0 {7,S} {9,D} {18,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.04,46.85,56.64,64.38,75.53,83.15,94.31],'cal/(mol*K)'),
        H298 = (87.79,'kcal/mol'),
        S298 = (90.05,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "adductc",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {4,D} {6,S}
3  C u0 p0 c0 {2,S} {7,D} {8,S}
4  C u0 p0 c0 {1,S} {2,D} {14,S}
5  C u0 p0 c0 {1,S} {6,D} {13,S}
6  C u0 p0 c0 {2,S} {5,D} {17,S}
7  C u0 p0 c0 {3,D} {9,S} {16,S}
8  C u0 p0 c0 {3,S} {10,D} {18,S}
9  C u1 p0 c0 {7,S} {10,S} {15,S}
10 C u0 p0 c0 {8,D} {9,S} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.28,47.09,56.84,64.54,75.64,83.23,94.35],'cal/(mol*K)'),
        H298 = (91.89,'kcal/mol'),
        S298 = (90.47,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "prod1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {7,S} {12,S}
4  C u0 p0 c0 {1,S} {9,D} {13,S}
5  C u0 p0 c0 {1,S} {10,D} {14,S}
6  C u0 p0 c0 {2,S} {8,D} {15,S}
7  C u1 p0 c0 {3,S} {8,S} {16,S}
8  C u0 p0 c0 {6,D} {7,S} {19,S}
9  C u0 p0 c0 {4,D} {10,S} {17,S}
10 C u0 p0 c0 {5,D} {9,S} {18,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.69,46.98,56.98,64.77,75.84,83.35,94.37],'cal/(mol*K)'),
        H298 = (110.21,'kcal/mol'),
        S298 = (87.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "prod2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,D} {11,S}
3  C u0 p0 c0 {1,S} {7,D} {12,S}
4  C u1 p0 c0 {1,S} {8,S} {13,S}
5  C u0 p0 c0 {1,S} {9,D} {14,S}
6  C u0 p0 c0 {2,D} {7,S} {15,S}
7  C u0 p0 c0 {3,D} {6,S} {16,S}
8  C u0 p0 c0 {4,S} {10,D} {17,S}
9  C u0 p0 c0 {5,D} {10,S} {19,S}
10 C u0 p0 c0 {8,D} {9,S} {18,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.84,46.8,56.62,64.35,75.47,83.08,94.24],'cal/(mol*K)'),
        H298 = (96.34,'kcal/mol'),
        S298 = (88.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "prod4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,D} {6,S}
3  C u1 p0 c0 {1,S} {7,S} {12,S}
4  C u0 p0 c0 {1,S} {8,D} {13,S}
5  C u0 p0 c0 {2,D} {9,S} {14,S}
6  C u0 p0 c0 {2,S} {10,D} {17,S}
7  C u0 p0 c0 {3,S} {9,D} {16,S}
8  C u0 p0 c0 {4,D} {10,S} {19,S}
9  C u0 p0 c0 {5,S} {7,D} {15,S}
10 C u0 p0 c0 {6,D} {8,S} {18,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.93,45.8,55.7,63.59,75.06,82.9,94.29],'cal/(mol*K)'),
        H298 = (81.64,'kcal/mol'),
        S298 = (86.42,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "prod5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {4,S}
2  C u0 p0 c0 {1,S} {8,D} {11,S}
3  C u0 p0 c0 {1,D} {5,S} {13,S}
4  C u0 p0 c0 {1,S} {7,D} {17,S}
5  C u0 p0 c0 {3,S} {6,D} {14,S}
6  C u0 p0 c0 {5,D} {7,S} {15,S}
7  C u0 p0 c0 {4,D} {6,S} {16,S}
8  C u0 p0 c0 {2,D} {9,S} {12,S}
9  C u0 p0 c0 {8,S} {10,D} {18,S}
10 C u1 p0 c0 {9,D} {19,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.53,47.63,56.92,64.39,75.35,82.96,94.2],'cal/(mol*K)'),
        H298 = (115.68,'kcal/mol'),
        S298 = (94.21,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "naphthalene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,D}
2  C u0 p0 c0 {1,S} {3,S} {6,D}
3  C u0 p0 c0 {2,S} {7,D} {11,S}
4  C u0 p0 c0 {1,S} {8,D} {14,S}
5  C u0 p0 c0 {1,D} {9,S} {15,S}
6  C u0 p0 c0 {2,D} {10,S} {18,S}
7  C u0 p0 c0 {3,D} {8,S} {12,S}
8  C u0 p0 c0 {4,D} {7,S} {13,S}
9  C u0 p0 c0 {5,S} {10,D} {16,S}
10 C u0 p0 c0 {6,S} {9,D} {17,S}
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
        Cpdata = ([31.94,42.88,52.08,59.62,70.72,78.68,90.24],'cal/(mol*K)'),
        H298 = (36,'kcal/mol'),
        S298 = (79.49,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "prod3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {6,S} {12,S}
4  C u1 p0 c0 {1,S} {8,S} {14,S}
5  C u0 p0 c0 {1,S} {10,D} {16,S}
6  C u0 p0 c0 {3,S} {8,D} {13,S}
7  C u0 p0 c0 {2,S} {9,D} {15,S}
8  C u0 p0 c0 {4,S} {6,D} {17,S}
9  C u0 p0 c0 {7,D} {10,S} {18,S}
10 C u0 p0 c0 {5,D} {9,S} {19,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.61,46.65,56.54,64.33,75.51,83.13,94.3],'cal/(mol*K)'),
        H298 = (104.32,'kcal/mol'),
        S298 = (85.86,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "biCPD_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {7,D} {13,S}
4  C u0 p0 c0 {1,S} {8,D} {14,S}
5  C u0 p0 c0 {2,S} {9,D} {15,S}
6  C u0 p0 c0 {2,S} {10,D} {16,S}
7  C u0 p0 c0 {3,D} {8,S} {17,S}
8  C u0 p0 c0 {4,D} {7,S} {18,S}
9  C u0 p0 c0 {5,D} {10,S} {19,S}
10 C u0 p0 c0 {6,D} {9,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.2,47.8,58.3,66.6,78.49,86.56,98.23],'cal/(mol*K)'),
        H298 = (76.66,'kcal/mol'),
        S298 = (91.52,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "biCPD_2",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {11,S}
2  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {2,S} {7,D}
4  C u0 p0 c0 {1,S} {8,D} {14,S}
5  C u0 p0 c0 {1,S} {9,D} {15,S}
6  C u0 p0 c0 {2,S} {10,D} {16,S}
7  C u0 p0 c0 {3,D} {10,S} {19,S}
8  C u0 p0 c0 {4,D} {9,S} {17,S}
9  C u0 p0 c0 {5,D} {8,S} {18,S}
10 C u0 p0 c0 {6,D} {7,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.93,48.52,58.35,66.27,77.92,86.02,98.04],'cal/(mol*K)'),
        H298 = (74.7,'kcal/mol'),
        S298 = (92.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "biCPD_3",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {11,S}
2  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {4,D} {8,S}
4  C u0 p0 c0 {2,S} {3,D} {16,S}
5  C u0 p0 c0 {1,S} {9,D} {14,S}
6  C u0 p0 c0 {1,S} {10,D} {15,S}
7  C u0 p0 c0 {2,S} {8,D} {17,S}
8  C u0 p0 c0 {3,S} {7,D} {20,S}
9  C u0 p0 c0 {5,D} {10,S} {18,S}
10 C u0 p0 c0 {6,D} {9,S} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([37.24,48.93,58.72,66.58,78.13,86.17,98.11],'cal/(mol*K)'),
        H298 = (74.12,'kcal/mol'),
        S298 = (92.04,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "biCPD_4",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,S} {7,D}
4  C u0 p0 c0 {2,S} {3,S} {8,D}
5  C u0 p0 c0 {1,S} {9,D} {15,S}
6  C u0 p0 c0 {2,S} {10,D} {16,S}
7  C u0 p0 c0 {3,D} {9,S} {18,S}
8  C u0 p0 c0 {4,D} {10,S} {19,S}
9  C u0 p0 c0 {5,D} {7,S} {17,S}
10 C u0 p0 c0 {6,D} {8,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.87,48.9,58.96,67.01,78.75,86.82,98.62],'cal/(mol*K)'),
        H298 = (66.94,'kcal/mol'),
        S298 = (87.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "biCPD_5",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
2  C u0 p0 c0 {5,S} {7,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,S} {8,D}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {2,S} {4,D} {16,S}
6  C u0 p0 c0 {1,S} {10,D} {15,S}
7  C u0 p0 c0 {2,S} {9,D} {17,S}
8  C u0 p0 c0 {3,D} {10,S} {19,S}
9  C u0 p0 c0 {4,S} {7,D} {20,S}
10 C u0 p0 c0 {6,D} {8,S} {18,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.97,48.98,58.99,66.98,78.62,86.65,98.46],'cal/(mol*K)'),
        H298 = (67.91,'kcal/mol'),
        S298 = (91.04,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "biCPD_6",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {7,S} {11,S} {12,S}
2  C u0 p0 c0 {6,S} {8,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {5,D} {9,S}
4  C u0 p0 c0 {3,S} {6,D} {10,S}
5  C u0 p0 c0 {1,S} {3,D} {16,S}
6  C u0 p0 c0 {2,S} {4,D} {17,S}
7  C u0 p0 c0 {1,S} {9,D} {15,S}
8  C u0 p0 c0 {2,S} {10,D} {18,S}
9  C u0 p0 c0 {3,S} {7,D} {19,S}
10 C u0 p0 c0 {4,S} {8,D} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([37.11,49.15,59.09,66.99,78.52,86.51,98.33],'cal/(mol*K)'),
        H298 = (68.7,'kcal/mol'),
        S298 = (89.76,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

