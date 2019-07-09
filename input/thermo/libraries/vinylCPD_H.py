#!/usr/bin/env python
# encoding: utf-8

name = "vinylCPD_H"
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
    label = "CH3",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "H",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "C2H4",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "C2H3",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {3,S}
2 C u0 p0 c0 {1,D} {4,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "vinylCPD",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,D} {10,S}
3  C u0 p0 c0 {1,S} {6,D} {11,S}
4  C u0 p0 c0 {1,S} {7,D} {9,S}
5  C u0 p0 c0 {2,D} {6,S} {12,S}
6  C u0 p0 c0 {3,D} {5,S} {13,S}
7  C u0 p0 c0 {4,D} {14,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.48,35.21,42.6,48.55,57.32,63.49,72.74],'cal/(mol*K)'),
        H298 = (54.52,'kcal/mol'),
        S298 = (79.29,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "addA",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u1 p0 c0 {1,S} {2,S} {12,S}
4  C u0 p0 c0 {1,S} {6,D} {13,S}
5  C u0 p0 c0 {1,S} {7,D} {14,S}
6  C u0 p0 c0 {4,D} {7,S} {15,S}
7  C u0 p0 c0 {5,D} {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.06,37.93,45.56,51.79,61.1,67.72,77.72],'cal/(mol*K)'),
        H298 = (71.36,'kcal/mol'),
        S298 = (87.55,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "addB",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {1,S} {6,D} {12,S}
5  C u0 p0 c0 {3,D} {6,S} {13,S}
6  C u0 p0 c0 {4,D} {5,S} {14,S}
7  C u1 p0 c0 {2,S} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.36,38.33,45.97,52.14,61.34,67.87,77.77],'cal/(mol*K)'),
        H298 = (73.9,'kcal/mol'),
        S298 = (86.07,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "addC",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,D} {13,S}
4  C u0 p0 c0 {1,S} {7,D} {11,S}
5  C u1 p0 c0 {2,S} {6,S} {12,S}
6  C u0 p0 c0 {3,D} {5,S} {14,S}
7  C u0 p0 c0 {4,D} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.24,37.37,45.17,51.5,60.92,67.59,77.64],'cal/(mol*K)'),
        H298 = (61.34,'kcal/mol'),
        S298 = (85.03,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "addD",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {2,S} {11,S}
4  C u0 p0 c0 {1,S} {5,D} {14,S}
5  C u0 p0 c0 {2,S} {4,D} {13,S}
6  C u0 p0 c0 {1,S} {7,D} {12,S}
7  C u0 p0 c0 {6,D} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.74,37.72,45.42,51.69,61.06,67.71,77.73],'cal/(mol*K)'),
        H298 = (74.75,'kcal/mol'),
        S298 = (84.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "product1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {5,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  C u1 p0 c0 {3,S} {7,S} {14,S}
6  C u0 p0 c0 {2,S} {7,D} {15,S}
7  C u0 p0 c0 {5,S} {6,D} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.64,37.05,45.03,51.46,60.94,67.6,77.64],'cal/(mol*K)'),
        H298 = (62.21,'kcal/mol'),
        S298 = (79.16,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "product2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u1 p0 c0 {1,S} {6,S} {12,S}
4  C u0 p0 c0 {1,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {7,S} {14,S}
6  C u0 p0 c0 {3,S} {7,D} {16,S}
7  C u0 p0 c0 {5,S} {6,D} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.67,36.76,44.56,50.95,60.53,67.32,77.53],'cal/(mol*K)'),
        H298 = (44.25,'kcal/mol'),
        S298 = (80.51,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "product3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
5  C u1 p0 c0 {2,S} {7,S} {14,S}
6  C u0 p0 c0 {1,S} {7,D} {15,S}
7  C u0 p0 c0 {5,S} {6,D} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.94,35.75,44.09,50.77,60.58,67.43,77.61],'cal/(mol*K)'),
        H298 = (63.77,'kcal/mol'),
        S298 = (78.59,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "product4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u1 p0 c0 {1,S} {6,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {7,S} {14,S}
6  C u0 p0 c0 {3,S} {7,D} {16,S}
7  C u0 p0 c0 {5,S} {6,D} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.94,36.03,43.92,50.41,60.17,67.09,77.45],'cal/(mol*K)'),
        H298 = (50.64,'kcal/mol'),
        S298 = (78.23,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "product5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {2,S} {6,D} {12,S}
5  C u0 p0 c0 {3,D} {6,S} {13,S}
6  C u0 p0 c0 {4,D} {5,S} {14,S}
7  C u1 p0 c0 {1,S} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.08,37.92,45.49,51.67,60.97,67.61,77.65],'cal/(mol*K)'),
        H298 = (72.11,'kcal/mol'),
        S298 = (83.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "product6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
5  C u1 p0 c0 {2,S} {4,S} {14,S}
6  C u0 p0 c0 {1,S} {7,D} {15,S}
7  C u0 p0 c0 {2,S} {6,D} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.5,35.54,43.97,50.71,60.55,67.4,77.6],'cal/(mol*K)'),
        H298 = (68.14,'kcal/mol'),
        S298 = (76.39,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "product7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u1 p0 c0 {1,S} {4,S} {5,S}
4  C u0 p0 c0 {3,S} {6,D} {13,S}
5  C u0 p0 c0 {3,S} {7,D} {16,S}
6  C u0 p0 c0 {4,D} {7,S} {14,S}
7  C u0 p0 c0 {5,D} {6,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29,37.82,45.4,51.59,60.9,67.53,77.58],'cal/(mol*K)'),
        H298 = (50.68,'kcal/mol'),
        S298 = (85.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "product8",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
5  C u1 p0 c0 {2,S} {3,S} {14,S}
6  C u0 p0 c0 {2,S} {7,D} {16,S}
7  C u0 p0 c0 {4,S} {6,D} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.52,36.08,44.28,50.91,60.69,67.55,77.74],'cal/(mol*K)'),
        H298 = (79.77,'kcal/mol'),
        S298 = (80.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "product9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
3  C u1 p0 c0 {1,S} {2,S} {12,S}
4  C u0 p0 c0 {1,S} {6,D} {13,S}
5  C u0 p0 c0 {2,S} {7,D} {14,S}
6  C u0 p0 c0 {4,D} {7,S} {15,S}
7  C u0 p0 c0 {5,D} {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.26,35.04,42.7,49.02,58.58,65.4,75.63],'cal/(mol*K)'),
        H298 = (72.26,'kcal/mol'),
        S298 = (77.23,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "product10",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u1 p0 c0 {1,S} {5,S} {6,S}
4  C u0 p0 c0 {2,S} {5,D} {12,S}
5  C u0 p0 c0 {3,S} {4,D} {14,S}
6  C u0 p0 c0 {3,S} {7,D} {13,S}
7  C u0 p0 c0 {6,D} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.05,37.08,44.86,51.22,60.72,67.46,77.6],'cal/(mol*K)'),
        H298 = (48.83,'kcal/mol'),
        S298 = (82.25,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "product11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,D}
2  C u0 p0 c0 {1,S} {4,D} {10,S}
3  C u0 p0 c0 {1,S} {6,D} {8,S}
4  C u0 p0 c0 {2,D} {7,S} {9,S}
5  C u0 p0 c0 {1,D} {13,S} {14,S}
6  C u0 p0 c0 {3,D} {11,S} {12,S}
7  C u1 p0 c0 {4,S} {15,S} {16,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([31.38,39.87,47.02,52.84,61.62,67.95,77.69],'cal/(mol*K)'),
        H298 = (67.69,'kcal/mol'),
        S298 = (88.46,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "product12",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {6,S} {7,D}
4  C u1 p0 c0 {2,S} {3,S} {13,S}
5  C u0 p0 c0 {1,S} {6,D} {12,S}
6  C u0 p0 c0 {3,S} {5,D} {14,S}
7  C u0 p0 c0 {3,D} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.03,37.11,44.85,51.17,60.67,67.42,77.59],'cal/(mol*K)'),
        H298 = (53.97,'kcal/mol'),
        S298 = (81.31,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "product13",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {7,D}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,S} {6,D} {11,S}
5  C u0 p0 c0 {3,D} {6,S} {13,S}
6  C u0 p0 c0 {4,D} {5,S} {12,S}
7  C u0 p0 c0 {2,D} {14,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.18,34.75,42.05,48,56.91,63.21,72.65],'cal/(mol*K)'),
        H298 = (46.84,'kcal/mol'),
        S298 = (78.02,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "product14",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {5,S} {6,S} {7,D}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {1,S} {6,D} {11,S}
5  C u0 p0 c0 {2,S} {3,D} {12,S}
6  C u0 p0 c0 {2,S} {4,D} {13,S}
7  C u0 p0 c0 {2,D} {14,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.05,34.62,41.92,47.89,56.83,63.16,72.64],'cal/(mol*K)'),
        H298 = (42.9,'kcal/mol'),
        S298 = (75.6,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "product15",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,D} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {2,D} {7,S} {12,S}
5  C u0 p0 c0 {3,D} {6,S} {13,S}
6  C u0 p0 c0 {5,S} {7,D} {14,S}
7  C u0 p0 c0 {4,S} {6,D} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.35,33.99,41.43,47.51,56.61,63.02,72.57],'cal/(mol*K)'),
        H298 = (47.08,'kcal/mol'),
        S298 = (75.54,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "product16",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {4,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {5,D} {11,S}
4  C u0 p0 c0 {1,S} {6,D} {8,S}
5  C u0 p0 c0 {3,D} {7,S} {12,S}
6  C u0 p0 c0 {4,D} {13,S} {14,S}
7  C u1 p0 c0 {5,S} {15,S} {16,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.9,39.28,46.51,52.43,61.39,67.82,77.67],'cal/(mol*K)'),
        H298 = (60.02,'kcal/mol'),
        S298 = (85.55,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "product17",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
5  C u1 p0 c0 {1,S} {2,S} {14,S}
6  C u0 p0 c0 {2,S} {7,D} {15,S}
7  C u0 p0 c0 {1,S} {6,D} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.2,35.3,43.7,50.5,60.4,67.3,77.5],'cal/(mol*K)'),
        H298 = (74.29,'kcal/mol'),
        S298 = (75.05,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "product18",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {1,S} {6,D} {12,S}
5  C u0 p0 c0 {3,D} {6,S} {13,S}
6  C u0 p0 c0 {4,D} {5,S} {14,S}
7  C u1 p0 c0 {1,S} {15,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.3,39.2,46.6,52.6,61.5,67.9,77.7],'cal/(mol*K)'),
        H298 = (71.9,'kcal/mol'),
        S298 = (83.07,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "product19",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  C u1 p0 c0 {1,S} {7,S} {14,S}
6  C u0 p0 c0 {2,S} {7,D} {15,S}
7  C u0 p0 c0 {5,S} {6,D} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28,37.4,45.3,51.7,61.1,67.7,77.7],'cal/(mol*K)'),
        H298 = (61.77,'kcal/mol'),
        S298 = (80.32,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "product20",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {5,D}
4  C u1 p0 c0 {1,S} {6,S} {13,S}
5  C u0 p0 c0 {3,D} {7,S} {14,S}
6  C u0 p0 c0 {4,S} {7,D} {16,S}
7  C u0 p0 c0 {5,S} {6,D} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28,36.8,44.5,50.9,60.5,67.4,77.6],'cal/(mol*K)'),
        H298 = (41.34,'kcal/mol'),
        S298 = (81.16,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "product21",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {5,D}
4  C u0 p0 c0 {1,S} {6,D} {12,S}
5  C u0 p0 c0 {3,D} {6,S} {13,S}
6  C u0 p0 c0 {4,D} {5,S} {14,S}
7  C u1 p0 c0 {2,S} {15,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.6,38.4,46,52.1,61.3,67.9,77.8],'cal/(mol*K)'),
        H298 = (71.79,'kcal/mol'),
        S298 = (86.1,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "product22",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  C u0 p0 c0 {2,S} {6,D} {13,S}
6  C u0 p0 c0 {3,S} {5,D} {14,S}
7  C u1 p0 c0 {1,S} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.7,38.5,46,52.2,61.4,67.9,77.8],'cal/(mol*K)'),
        H298 = (71.24,'kcal/mol'),
        S298 = (86.35,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "product23",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
5  C u1 p0 c0 {3,S} {4,S} {7,S}
6  C u0 p0 c0 {1,S} {7,D} {15,S}
7  C u0 p0 c0 {5,S} {6,D} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.6,34.7,43.2,50,60,67,77.4],'cal/(mol*K)'),
        H298 = (77.43,'kcal/mol'),
        S298 = (75.93,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "product24",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {7,D}
4  C u0 p0 c0 {2,S} {6,D} {12,S}
5  C u1 p0 c0 {3,S} {6,S} {13,S}
6  C u0 p0 c0 {4,D} {5,S} {14,S}
7  C u0 p0 c0 {3,D} {15,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.6,36.8,44.6,51,60.6,67.3,77.5],'cal/(mol*K)'),
        H298 = (46.96,'kcal/mol'),
        S298 = (80.83,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "product25",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
5  C u1 p0 c0 {1,S} {3,S} {7,S}
6  C u0 p0 c0 {4,S} {7,D} {15,S}
7  C u0 p0 c0 {5,S} {6,D} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.8,35.5,43.8,50.5,60.4,67.3,77.6],'cal/(mol*K)'),
        H298 = (73.44,'kcal/mol'),
        S298 = (79.16,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "product26",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {5,D}
4  C u1 p0 c0 {2,S} {3,S} {12,S}
5  C u0 p0 c0 {3,D} {6,S} {14,S}
6  C u0 p0 c0 {5,S} {7,D} {13,S}
7  C u0 p0 c0 {6,D} {15,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.13,38,45.64,51.86,61.16,67.77,77.75],'cal/(mol*K)'),
        H298 = (74.69,'kcal/mol'),
        S298 = (84.15,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "product29",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {6,S} {7,D}
6  C u1 p0 c0 {1,S} {5,S} {16,S}
7  C u0 p0 c0 {4,S} {5,D} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.07,35.99,44.32,50.99,60.78,67.61,77.76],'cal/(mol*K)'),
        H298 = (122.34,'kcal/mol'),
        S298 = (77.13,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "product31",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {6,S} {7,D}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  C u0 p0 c0 {1,S} {6,D} {12,S}
6  C u0 p0 c0 {3,S} {5,D} {14,S}
7  C u0 p0 c0 {3,D} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.14,38.13,45.73,51.9,61.13,67.7,77.67],'cal/(mol*K)'),
        H298 = (54.72,'kcal/mol'),
        S298 = (82.84,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "product32",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {7,D}
4  C u1 p0 c0 {1,S} {6,S} {12,S}
5  C u0 p0 c0 {3,S} {6,D} {13,S}
6  C u0 p0 c0 {4,S} {5,D} {14,S}
7  C u0 p0 c0 {3,D} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.77,37.83,45.5,51.72,61.01,67.62,77.63],'cal/(mol*K)'),
        H298 = (48.57,'kcal/mol'),
        S298 = (82.58,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "product33",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {5,S} {11,S}
5  C u1 p0 c0 {4,S} {6,S} {12,S}
6  C u0 p0 c0 {5,S} {7,D} {13,S}
7  C u0 p0 c0 {1,S} {6,D} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.61,34.52,41.14,46.48,54.37,59.92,68.21],'cal/(mol*K)'),
        H298 = (68.17,'kcal/mol'),
        S298 = (75.14,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "product34",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  C u0 p0 c0 {1,S} {6,D} {11,S}
5  C u0 p0 c0 {2,S} {7,D} {12,S}
6  C u0 p0 c0 {4,D} {7,S} {13,S}
7  C u0 p0 c0 {5,D} {6,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.54,33.9,40.84,46.35,54.4,59.98,68.26],'cal/(mol*K)'),
        H298 = (111.3,'kcal/mol'),
        S298 = (76.88,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "product35",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {7,D}
4  C u0 p0 c0 {1,S} {5,D} {11,S}
5  C u0 p0 c0 {3,S} {4,D} {12,S}
6  C u1 p0 c0 {1,S} {13,S} {14,S}
7  C u0 p0 c0 {3,D} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.83,38.66,46.12,52.19,61.28,67.79,77.69],'cal/(mol*K)'),
        H298 = (72.51,'kcal/mol'),
        S298 = (87.52,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "product36",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
5  C u0 p0 c0 {4,S} {6,S} {7,D}
6  C u1 p0 c0 {2,S} {5,S} {14,S}
7  C u0 p0 c0 {5,D} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.51,37.14,45.18,51.6,61.04,67.67,77.65],'cal/(mol*K)'),
        H298 = (64.39,'kcal/mol'),
        S298 = (79.77,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "product37",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {7,D}
4  C u1 p0 c0 {1,S} {2,S} {12,S}
5  C u0 p0 c0 {2,S} {6,D} {13,S}
6  C u0 p0 c0 {3,S} {5,D} {14,S}
7  C u0 p0 c0 {3,D} {15,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.36,37.27,44.93,51.21,60.71,67.49,77.66],'cal/(mol*K)'),
        H298 = (67.12,'kcal/mol'),
        S298 = (83.09,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "product38",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {7,D}
4  C u0 p0 c0 {2,S} {5,D} {11,S}
5  C u0 p0 c0 {3,S} {4,D} {12,S}
6  C u1 p0 c0 {1,S} {13,S} {14,S}
7  C u0 p0 c0 {3,D} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.71,38.57,46.06,52.14,61.27,67.78,77.7],'cal/(mol*K)'),
        H298 = (72.35,'kcal/mol'),
        S298 = (85.54,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "product39",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {6,D} {13,S}
6  C u0 p0 c0 {4,S} {5,D} {14,S}
7  C u1 p0 c0 {1,S} {15,S} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.89,38.17,45.92,52.14,61.34,67.86,77.74],'cal/(mol*K)'),
        H298 = (76.86,'kcal/mol'),
        S298 = (80.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "product41",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,D} {5,S} {11,S}
5  C u0 p0 c0 {3,D} {4,S} {12,S}
6  C u0 p0 c0 {7,D} {13,S} {14,S}
7  C u1 p0 c0 {1,S} {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.73,34.78,41.48,46.83,54.69,60.18,68.37],'cal/(mol*K)'),
        H298 = (111.59,'kcal/mol'),
        S298 = (81.4,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "product42",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {7,D}
4  C u0 p0 c0 {1,S} {6,D} {10,S}
5  C u1 p0 c0 {2,S} {6,S} {11,S}
6  C u0 p0 c0 {4,D} {5,S} {12,S}
7  C u0 p0 c0 {3,D} {13,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.06,34.62,41.56,47,54.85,60.28,68.38],'cal/(mol*K)'),
        H298 = (103.96,'kcal/mol'),
        S298 = (77.63,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "BENZYL",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {8,S}
3  C u0 p0 c0 {1,B} {6,B} {12,S}
4  C u0 p0 c0 {2,B} {5,B} {9,S}
5  C u0 p0 c0 {4,B} {6,B} {10,S}
6  C u0 p0 c0 {3,B} {5,B} {11,S}
7  C u1 p0 c0 {1,S} {13,S} {14,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.42,33.72,40.6,46.09,54.13,59.74,68.09],'cal/(mol*K)'),
        H298 = (52.26,'kcal/mol'),
        S298 = (75.21,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "product44",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,D} {5,S} {12,S}
5  C u0 p0 c0 {3,D} {4,S} {13,S}
6  C u0 p0 c0 {1,S} {7,D} {11,S}
7  C u1 p0 c0 {6,D} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.53,34.76,41.55,46.93,54.76,60.21,68.35],'cal/(mol*K)'),
        H298 = (113.94,'kcal/mol'),
        S298 = (80.55,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "product45",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  C u0 p0 c0 {1,S} {7,D} {10,S}
6  C u1 p0 c0 {2,S} {7,S} {13,S}
7  C u0 p0 c0 {5,D} {6,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.43,33.25,40.52,46.24,54.45,60.07,68.35],'cal/(mol*K)'),
        H298 = (96.7,'kcal/mol'),
        S298 = (75.31,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "product46",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {5,D}
4  C u1 p0 c0 {1,S} {6,S} {11,S}
5  C u0 p0 c0 {3,D} {7,S} {14,S}
6  C u0 p0 c0 {4,S} {7,D} {12,S}
7  C u0 p0 c0 {5,S} {6,D} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.73,33.2,40.28,45.92,54.13,59.81,68.2],'cal/(mol*K)'),
        H298 = (103.42,'kcal/mol'),
        S298 = (78.03,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "CPDyl",
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
        Cpdata = ([18.91,24.67,29.39,33.1,38.45,42.17,47.78],'cal/(mol*K)'),
        H298 = (62.5,'kcal/mol'),
        S298 = (64.84,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
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
        Cpdata = ([21.48,28.53,34.38,39.04,45.85,50.61,57.74],'cal/(mol*K)'),
        H298 = (54.04,'kcal/mol'),
        S298 = (70.03,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
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
        Cpdata = ([17.94,24.42,29.92,34.33,40.83,45.39,52.23],'cal/(mol*K)'),
        H298 = (32.6,'kcal/mol'),
        S298 = (65.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
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
        Cpdata = ([19.56,26.74,32.86,37.8,45.05,50.08,57.51],'cal/(mol*K)'),
        H298 = (21.33,'kcal/mol'),
        S298 = (64.22,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "TOLUENE",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {11,S}
4  C u0 p0 c0 {2,B} {7,B} {15,S}
5  C u0 p0 c0 {3,B} {6,B} {12,S}
6  C u0 p0 c0 {5,B} {7,B} {13,S}
7  C u0 p0 c0 {4,B} {6,B} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.68,34.08,41.4,47.44,56.51,62.93,72.51],'cal/(mol*K)'),
        H298 = (13.72,'kcal/mol'),
        S298 = (80.65,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "vinylCPDyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {4,S}
2  C u0 p0 c0 {1,D} {5,S} {9,S}
3  C u1 p0 c0 {1,S} {6,S} {12,S}
4  C u0 p0 c0 {1,S} {7,D} {8,S}
5  C u0 p0 c0 {2,S} {6,D} {10,S}
6  C u0 p0 c0 {3,S} {5,D} {11,S}
7  C u0 p0 c0 {4,D} {13,S} {14,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.46,34.66,41.43,46.8,54.63,60.07,68.23],'cal/(mol*K)'),
        H298 = (73.21,'kcal/mol'),
        S298 = (79.4,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

