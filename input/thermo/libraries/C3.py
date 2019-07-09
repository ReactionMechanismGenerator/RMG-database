#!/usr/bin/env python
# encoding: utf-8

name = "C3"
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
    label = "prod_31",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  C u1 p0 c0 {2,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {6,T}
6  C u0 p0 c0 {5,T} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "prod_32",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {5,D}
4  C u0 p0 c0 {1,S} {6,D} {11,S}
5  C u0 p0 c0 {3,D} {12,S} {13,S}
6  C u1 p0 c0 {2,S} {4,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "prod_1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {5,S}
3  C u0 p0 c0 {1,S} {6,D} {9,S}
4  C u0 p0 c0 {2,D} {12,S} {13,S}
5  C u1 p0 c0 {2,S} {14,S} {15,S}
6  C u0 p0 c0 {3,D} {10,S} {11,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.41,36.27,42.93,48.38,56.69,62.74,72.15],'cal/(mol*K)'),
        H298 = (55.11,'kcal/mol'),
        S298 = (86,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "prod_2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {6,D}
5  C u1 p0 c0 {2,S} {3,S} {13,S}
6  C u0 p0 c0 {4,D} {14,S} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.5,33.78,40.98,46.91,55.91,62.37,72.15],'cal/(mol*K)'),
        H298 = (50.95,'kcal/mol'),
        S298 = (79.74,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "prod_3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {6,D}
4  C u0 p0 c0 {2,S} {5,D} {11,S}
5  C u0 p0 c0 {3,S} {4,D} {12,S}
6  C u0 p0 c0 {3,D} {13,S} {14,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.23,31.12,37.95,43.55,51.99,58.01,67.09],'cal/(mol*K)'),
        H298 = (28.98,'kcal/mol'),
        S298 = (75.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "prod_4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {5,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {1,S} {3,S} {4,S}
6  C u0 p0 c0 {2,S} {3,S} {7,D}
7  C u0 p0 c0 {6,D} {17,S} {18,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.97,40.49,48.99,56.14,67.14,75.1,87.13],'cal/(mol*K)'),
        H298 = (42.25,'kcal/mol'),
        S298 = (92.36,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "prod_5",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {3,S} {6,D}
5  C u0 p0 c0 {2,S} {6,S} {7,D}
6  C u0 p0 c0 {4,D} {5,S} {15,S}
7  C u0 p0 c0 {5,D} {16,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.21,38.33,46.37,53.09,63.38,70.81,82.06],'cal/(mol*K)'),
        H298 = (19.43,'kcal/mol'),
        S298 = (84,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "prod_6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {5,D}
4  C u0 p0 c0 {1,S} {6,D} {7,S}
5  C u0 p0 c0 {3,D} {17,S} {18,S}
6  C u0 p0 c0 {4,D} {13,S} {14,S}
7  C u1 p0 c0 {4,S} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.91,43.3,51.32,57.95,68.12,75.56,87.11],'cal/(mol*K)'),
        H298 = (46.11,'kcal/mol'),
        S298 = (92.82,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "prod_7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,D} {12,S}
4  C u0 p0 c0 {1,S} {6,D} {13,S}
5  C u0 p0 c0 {3,D} {14,S} {15,S}
6  C u1 p0 c0 {2,S} {4,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.34,35.5,41.98,47.47,56.07,62.39,72.1],'cal/(mol*K)'),
        H298 = (76.21,'kcal/mol'),
        S298 = (87.95,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "prod_8",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {6,D}
5  C u1 p0 c0 {1,S} {2,S} {14,S}
6  C u0 p0 c0 {2,S} {4,D} {15,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.07,33.99,41.02,46.89,55.88,62.38,72.19],'cal/(mol*K)'),
        H298 = (46.36,'kcal/mol'),
        S298 = (78.86,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "prod_9",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {5,D}
4  C u0 p0 c0 {1,S} {6,D} {12,S}
5  C u0 p0 c0 {3,D} {6,S} {13,S}
6  C u0 p0 c0 {4,D} {5,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.94,31.59,38.29,43.81,52.18,58.16,67.19],'cal/(mol*K)'),
        H298 = (26.03,'kcal/mol'),
        S298 = (75.03,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "prod_10",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {7,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {2,S} {6,D}
5  C u0 p0 c0 {1,S} {7,D} {16,S}
6  C u0 p0 c0 {4,D} {17,S} {18,S}
7  C u1 p0 c0 {3,S} {5,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.86,42.55,50.38,57.05,67.51,75.21,87.06],'cal/(mol*K)'),
        H298 = (67.42,'kcal/mol'),
        S298 = (95.42,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "prod_11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
2  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
5  C u1 p0 c0 {1,S} {2,S} {3,S}
6  C u0 p0 c0 {1,S} {4,S} {7,D}
7  C u0 p0 c0 {2,S} {6,D} {18,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([31.44,40.64,48.99,56.08,67.09,75.09,87.16],'cal/(mol*K)'),
        H298 = (37.76,'kcal/mol'),
        S298 = (88.44,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "prod_12",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {2,S} {6,D}
5  C u0 p0 c0 {1,S} {3,S} {7,D}
6  C u0 p0 c0 {4,D} {7,S} {16,S}
7  C u0 p0 c0 {5,D} {6,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.93,38.74,46.63,53.28,63.52,70.93,82.15],'cal/(mol*K)'),
        H298 = (17.76,'kcal/mol'),
        S298 = (81.84,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "prod_13",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,D}
2  C u0 p0 c0 {1,S} {5,D} {6,S}
3  C u0 p0 c0 {1,S} {7,D} {8,S}
4  C u0 p0 c0 {1,D} {11,S} {12,S}
5  C u0 p0 c0 {2,D} {13,S} {14,S}
6  C u1 p0 c0 {2,S} {15,S} {16,S}
7  C u0 p0 c0 {3,D} {9,S} {10,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([31.93,40.53,47.61,53.32,61.91,68.12,77.75],'cal/(mol*K)'),
        H298 = (74.57,'kcal/mol'),
        S298 = (88.38,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "prod_14",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {6,D}
4  C u0 p0 c0 {3,S} {5,S} {7,D}
5  C u1 p0 c0 {2,S} {4,S} {12,S}
6  C u0 p0 c0 {3,D} {15,S} {16,S}
7  C u0 p0 c0 {4,D} {13,S} {14,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.9,37.97,45.6,51.79,61.06,67.66,77.67],'cal/(mol*K)'),
        H298 = (56.55,'kcal/mol'),
        S298 = (81.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "prod_15",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {6,D}
3  C u0 p0 c0 {2,S} {5,S} {7,D}
4  C u0 p0 c0 {1,S} {5,D} {10,S}
5  C u0 p0 c0 {3,S} {4,D} {11,S}
6  C u0 p0 c0 {2,D} {14,S} {15,S}
7  C u0 p0 c0 {3,D} {12,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.03,35.61,42.8,48.62,57.3,63.46,72.74],'cal/(mol*K)'),
        H298 = (49.78,'kcal/mol'),
        S298 = (78.99,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "prod_16",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {7,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {4,S} {5,D}
3  C u0 p0 c0 {2,S} {6,D} {11,S}
4  C u0 p0 c0 {2,S} {7,D} {12,S}
5  C u0 p0 c0 {2,D} {13,S} {14,S}
6  C u0 p0 c0 {3,D} {15,S} {16,S}
7  C u1 p0 c0 {1,S} {4,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([31.98,39.86,46.74,52.48,61.35,67.82,77.73],'cal/(mol*K)'),
        H298 = (96.68,'kcal/mol'),
        S298 = (92.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "prod_17",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u1 p0 c0 {1,S} {2,S} {5,S}
4  C u0 p0 c0 {1,S} {6,S} {7,D}
5  C u0 p0 c0 {3,S} {6,D} {14,S}
6  C u0 p0 c0 {4,S} {5,D} {13,S}
7  C u0 p0 c0 {4,D} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.53,38.29,45.76,51.87,61.11,67.72,77.72],'cal/(mol*K)'),
        H298 = (51.79,'kcal/mol'),
        S298 = (82.26,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "prod_18",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,D} {5,S}
3  C u0 p0 c0 {4,S} {6,S} {7,D}
4  C u0 p0 c0 {2,D} {3,S} {13,S}
5  C u0 p0 c0 {2,S} {6,D} {12,S}
6  C u0 p0 c0 {3,S} {5,D} {11,S}
7  C u0 p0 c0 {3,D} {14,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.53,35.79,42.83,48.59,57.25,63.41,72.71],'cal/(mol*K)'),
        H298 = (45.09,'kcal/mol'),
        S298 = (79.52,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "prod_19",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {12,S} {13,S}
5  C u0 p0 c0 {6,D} {14,S} {15,S}
6  C u1 p0 c0 {2,S} {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.57,35.97,41.79,46.76,54.62,60.48,69.62],'cal/(mol*K)'),
        H298 = (78.33,'kcal/mol'),
        S298 = (92.15,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "prod_20",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {3,S} {5,D}
5  C u0 p0 c0 {4,D} {15,S} {16,S}
6  C u0 p0 c0 {7,D} {17,S} {18,S}
7  C u1 p0 c0 {2,S} {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.91,42.72,49.74,55.76,65.32,72.47,83.55],'cal/(mol*K)'),
        H298 = (70.04,'kcal/mol'),
        S298 = (100.36,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "prod_21",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  C u1 p0 c0 {3,D} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.56,29.52,33.99,37.81,43.83,48.34,55.46],'cal/(mol*K)'),
        H298 = (87.29,'kcal/mol'),
        S298 = (82.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "prod_22",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  C u0 p0 c0 {2,S} {5,D} {11,S}
5  C u0 p0 c0 {1,S} {4,D} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.09,26.8,32.61,37.36,44.5,49.58,57.22],'cal/(mol*K)'),
        H298 = (55.36,'kcal/mol'),
        S298 = (70.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "prod_23",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {5,T}
4  C u1 p0 c0 {2,D} {9,S}
5  C u0 p0 c0 {3,T} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.59,27.1,30.74,33.69,38.23,41.61,46.96],'cal/(mol*K)'),
        H298 = (128.11,'kcal/mol'),
        S298 = (78.08,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "prod_24",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u1 p0 c0 {1,S} {4,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.51,23.31,28.2,32.11,37.82,41.78,47.67],'cal/(mol*K)'),
        H298 = (98.11,'kcal/mol'),
        S298 = (68.17,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "prod_25",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {12,S}
4  C u1 p0 c0 {2,S} {3,D}
5  C u0 p0 c0 {1,S} {6,T}
6  C u0 p0 c0 {5,T} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.55,33.55,38.74,43.1,49.9,54.93,62.71],'cal/(mol*K)'),
        H298 = (117.33,'kcal/mol'),
        S298 = (86.34,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "prod_26",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  C u0 p0 c0 {1,S} {3,D} {12,S}
5  C u0 p0 c0 {3,S} {6,D} {13,S}
6  C u1 p0 c0 {1,S} {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.48,30.51,36.62,41.63,49.19,54.57,62.63],'cal/(mol*K)'),
        H298 = (89.08,'kcal/mol'),
        S298 = (76.12,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "prod_27",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {5,D}
4  C u0 p0 c0 {1,S} {6,T}
5  C u1 p0 c0 {3,D} {12,S}
6  C u0 p0 c0 {4,T} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.79,34.01,39.22,43.51,50.16,55.08,62.73],'cal/(mol*K)'),
        H298 = (120.58,'kcal/mol'),
        S298 = (83.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "prod_28",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {5,S} {12,S}
5  C u0 p0 c0 {4,S} {6,D} {13,S}
6  C u1 p0 c0 {1,S} {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.45,30.44,36.53,41.56,49.15,54.54,62.62],'cal/(mol*K)'),
        H298 = (89.67,'kcal/mol'),
        S298 = (76.34,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "prod_29",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {4,D} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,D}
5  C u0 p0 c0 {2,S} {6,T}
6  C u0 p0 c0 {5,T} {13,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.19,33.48,38.8,43.2,50.01,55.01,62.75],'cal/(mol*K)'),
        H298 = (119.21,'kcal/mol'),
        S298 = (85.4,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "prod_30",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {5,D}
4  C u0 p0 c0 {3,S} {6,D} {11,S}
5  C u0 p0 c0 {3,D} {12,S} {13,S}
6  C u1 p0 c0 {2,S} {4,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.83,30.11,36.35,41.44,49.05,54.45,62.54],'cal/(mol*K)'),
        H298 = (90.51,'kcal/mol'),
        S298 = (77.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "prod_33",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {6,D}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u1 p0 c0 {2,S} {5,S} {10,S}
5  C u0 p0 c0 {3,D} {4,S} {11,S}
6  C u0 p0 c0 {2,D} {12,S} {13,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.26,30.87,37.19,42.24,49.66,54.87,62.72],'cal/(mol*K)'),
        H298 = (54.93,'kcal/mol'),
        S298 = (74.21,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

