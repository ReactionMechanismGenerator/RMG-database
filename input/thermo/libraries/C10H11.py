#!/usr/bin/env python
# encoding: utf-8

name = "C10H11"
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
    label = "adductd",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {8,S} {17,S}
5  C u0 p0 c0 {2,S} {9,D} {15,S}
6  C u0 p0 c0 {2,S} {10,D} {16,S}
7  C u0 p0 c0 {3,S} {8,D} {18,S}
8  C u0 p0 c0 {4,S} {7,D} {21,S}
9  C u0 p0 c0 {5,D} {10,S} {19,S}
10 C u0 p0 c0 {6,D} {9,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.72,49.69,60.6,69.31,82,90.78,103.75],'cal/(mol*K)'),
        H298 = (83.49,'kcal/mol'),
        S298 = (94.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "adducte",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {11,S}
3  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {3,S} {15,S}
5  C u0 p0 c0 {1,S} {8,D} {18,S}
6  C u0 p0 c0 {2,S} {9,D} {16,S}
7  C u0 p0 c0 {2,S} {10,D} {17,S}
8  C u0 p0 c0 {3,S} {5,D} {19,S}
9  C u0 p0 c0 {6,D} {10,S} {20,S}
10 C u0 p0 c0 {7,D} {9,S} {21,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([37.27,50.09,60.89,69.53,82.15,90.9,103.84],'cal/(mol*K)'),
        H298 = (97.04,'kcal/mol'),
        S298 = (94.95,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "pdt7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {13,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {14,S}
4  C u0 p0 c0 {2,S} {3,S} {7,S} {12,S}
5  C u0 p0 c0 {1,S} {9,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {9,D} {20,S}
7  C u0 p0 c0 {4,S} {10,D} {17,S}
8  C u1 p0 c0 {2,S} {10,S} {18,S}
9  C u0 p0 c0 {5,S} {6,D} {19,S}
10 C u0 p0 c0 {7,D} {8,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.78,48.21,59.54,68.55,81.61,90.58,103.73],'cal/(mol*K)'),
        H298 = (85.78,'kcal/mol'),
        S298 = (89.07,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "pdt8",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {7,D} {16,S}
5  C u0 p0 c0 {1,S} {9,D} {18,S}
6  C u1 p0 c0 {2,S} {8,S} {15,S}
7  C u0 p0 c0 {3,S} {4,D} {17,S}
8  C u0 p0 c0 {6,S} {10,D} {20,S}
9  C u0 p0 c0 {5,D} {10,S} {21,S}
10 C u0 p0 c0 {8,D} {9,S} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.78,48.52,59.38,68.18,81.16,90.2,103.52],'cal/(mol*K)'),
        H298 = (78.78,'kcal/mol'),
        S298 = (91.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "pdt9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u1 p0 c0 {1,S} {4,S} {13,S}
3  C u0 p0 c0 {1,S} {5,D} {14,S}
4  C u0 p0 c0 {2,S} {8,D} {18,S}
5  C u0 p0 c0 {3,D} {9,S} {19,S}
6  C u0 p0 c0 {7,D} {10,S} {15,S}
7  C u0 p0 c0 {6,D} {8,S} {16,S}
8  C u0 p0 c0 {4,D} {7,S} {17,S}
9  C u0 p0 c0 {5,S} {10,D} {20,S}
10 C u0 p0 c0 {6,S} {9,D} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.91,50.96,61.19,69.52,81.94,90.69,103.71],'cal/(mol*K)'),
        H298 = (98.89,'kcal/mol'),
        S298 = (93.05,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "pdt10bis",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {10,D} {18,S}
5  C u0 p0 c0 {2,S} {9,D} {15,S}
6  C u1 p0 c0 {2,S} {8,S} {16,S}
7  C u0 p0 c0 {3,S} {8,D} {17,S}
8  C u0 p0 c0 {6,S} {7,D} {20,S}
9  C u0 p0 c0 {5,D} {10,S} {19,S}
10 C u0 p0 c0 {4,D} {9,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.17,48.88,59.7,68.46,81.4,90.4,103.65],'cal/(mol*K)'),
        H298 = (76.28,'kcal/mol'),
        S298 = (89.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "pdt11",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {7,D}
4  C u0 p0 c0 {1,S} {9,D} {15,S}
5  C u0 p0 c0 {2,S} {8,D} {14,S}
6  C u0 p0 c0 {3,S} {10,D} {17,S}
7  C u0 p0 c0 {3,D} {8,S} {18,S}
8  C u0 p0 c0 {5,D} {7,S} {19,S}
9  C u0 p0 c0 {4,D} {10,S} {20,S}
10 C u0 p0 c0 {6,D} {9,S} {16,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.42,46.5,56.8,65.16,77.52,86.1,98.67],'cal/(mol*K)'),
        H298 = (63.19,'kcal/mol'),
        S298 = (87.27,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "pdt12",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,D} {12,S}
3  C u1 p0 c0 {1,S} {6,S} {13,S}
4  C u0 p0 c0 {1,S} {7,D} {14,S}
5  C u0 p0 c0 {2,D} {9,S} {16,S}
6  C u0 p0 c0 {3,S} {8,D} {17,S}
7  C u0 p0 c0 {4,D} {8,S} {19,S}
8  C u0 p0 c0 {6,D} {7,S} {18,S}
9  C u0 p0 c0 {5,S} {10,D} {15,S}
10 C u0 p0 c0 {9,D} {20,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.98,51.09,61.37,69.7,82.05,90.73,103.67],'cal/(mol*K)'),
        H298 = (91.54,'kcal/mol'),
        S298 = (99.44,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "pdt13",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,B} {4,B}
2  C u0 p0 c0 {1,S} {5,D} {13,S}
3  C u0 p0 c0 {1,B} {6,B} {14,S}
4  C u0 p0 c0 {1,B} {8,B} {18,S}
5  C u0 p0 c0 {2,D} {9,S} {12,S}
6  C u0 p0 c0 {3,B} {7,B} {15,S}
7  C u0 p0 c0 {6,B} {8,B} {16,S}
8  C u0 p0 c0 {4,B} {7,B} {17,S}
9  C u0 p0 c0 {5,S} {10,D} {11,S}
10 C u0 p0 c0 {9,D} {19,S} {20,S}
11 H u0 p0 c0 {9,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.82,48.28,58.1,66.1,77.96,86.27,98.6],'cal/(mol*K)'),
        H298 = (51.71,'kcal/mol'),
        S298 = (94.14,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "pdt14",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u1 p0 c0 {1,S} {5,S} {12,S}
3  C u0 p0 c0 {1,S} {6,D} {13,S}
4  C u0 p0 c0 {1,S} {7,D} {14,S}
5  C u0 p0 c0 {2,S} {8,D} {17,S}
6  C u0 p0 c0 {3,D} {7,S} {18,S}
7  C u0 p0 c0 {4,D} {6,S} {19,S}
8  C u0 p0 c0 {5,D} {9,S} {16,S}
9  C u0 p0 c0 {8,S} {10,D} {15,S}
10 C u0 p0 c0 {9,D} {20,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.53,51.71,62.01,70.29,82.48,91.01,103.78],'cal/(mol*K)'),
        H298 = (90.38,'kcal/mol'),
        S298 = (99.22,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "pdt15",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {3,S} {8,D}
5  C u1 p0 c0 {1,S} {9,S} {17,S}
6  C u0 p0 c0 {2,S} {9,D} {16,S}
7  C u0 p0 c0 {3,S} {10,D} {18,S}
8  C u0 p0 c0 {4,D} {10,S} {20,S}
9  C u0 p0 c0 {5,S} {6,D} {19,S}
10 C u0 p0 c0 {7,D} {8,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([37.05,49.82,60.62,69.28,81.98,90.78,103.78],'cal/(mol*K)'),
        H298 = (81.47,'kcal/mol'),
        S298 = (95.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "pdt16",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,D} {5,S}
3  C u0 p0 c0 {1,S} {6,D} {13,S}
4  C u0 p0 c0 {2,D} {8,S} {17,S}
5  C u1 p0 c0 {2,S} {6,S} {18,S}
6  C u0 p0 c0 {3,D} {5,S} {19,S}
7  C u0 p0 c0 {8,D} {9,S} {15,S}
8  C u0 p0 c0 {4,S} {7,D} {16,S}
9  C u0 p0 c0 {7,S} {10,D} {14,S}
10 C u0 p0 c0 {9,D} {20,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.63,51.67,61.91,70.18,82.4,90.98,103.79],'cal/(mol*K)'),
        H298 = (76.88,'kcal/mol'),
        S298 = (98.02,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "pdt17",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {10,D} {16,S}
5  C u1 p0 c0 {1,S} {8,S} {17,S}
6  C u0 p0 c0 {2,S} {9,D} {15,S}
7  C u0 p0 c0 {3,S} {8,D} {18,S}
8  C u0 p0 c0 {5,S} {7,D} {21,S}
9  C u0 p0 c0 {6,D} {10,S} {19,S}
10 C u0 p0 c0 {4,D} {9,S} {20,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([37.03,49.77,60.5,69.12,81.79,90.61,103.67],'cal/(mol*K)'),
        H298 = (80.09,'kcal/mol'),
        S298 = (92.88,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "pdt18",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {5,D}
3  C u1 p0 c0 {1,S} {6,S} {13,S}
4  C u0 p0 c0 {2,S} {7,D} {16,S}
5  C u0 p0 c0 {2,D} {8,S} {17,S}
6  C u0 p0 c0 {3,S} {8,D} {19,S}
7  C u0 p0 c0 {4,D} {9,S} {15,S}
8  C u0 p0 c0 {5,S} {6,D} {18,S}
9  C u0 p0 c0 {7,S} {10,D} {14,S}
10 C u0 p0 c0 {9,D} {20,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.95,50.96,61.22,69.56,81.97,90.7,103.69],'cal/(mol*K)'),
        H298 = (72.87,'kcal/mol'),
        S298 = (96.29,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "pdt19",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {3,S} {8,D}
5  C u1 p0 c0 {1,S} {9,S} {18,S}
6  C u0 p0 c0 {2,S} {10,D} {17,S}
7  C u0 p0 c0 {3,S} {9,D} {16,S}
8  C u0 p0 c0 {4,D} {10,S} {20,S}
9  C u0 p0 c0 {5,S} {7,D} {19,S}
10 C u0 p0 c0 {6,D} {8,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.33,48.88,59.6,68.33,81.28,90.32,103.62],'cal/(mol*K)'),
        H298 = (74.88,'kcal/mol'),
        S298 = (91.27,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "pdt20",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
2  C u0 p0 c0 {4,S} {5,D} {6,S}
3  C u0 p0 c0 {1,S} {7,D} {14,S}
4  C u0 p0 c0 {2,S} {8,D} {17,S}
5  C u0 p0 c0 {2,D} {9,S} {18,S}
6  C u1 p0 c0 {2,S} {10,S} {21,S}
7  C u0 p0 c0 {3,D} {8,S} {15,S}
8  C u0 p0 c0 {4,D} {7,S} {16,S}
9  C u0 p0 c0 {5,S} {10,D} {19,S}
10 C u0 p0 c0 {6,S} {9,D} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.84,51.62,61.72,69.94,82.18,90.8,103.69],'cal/(mol*K)'),
        H298 = (75.75,'kcal/mol'),
        S298 = (99.31,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "pdt21",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {7,D} {8,S}
5  C u0 p0 c0 {1,S} {9,D} {16,S}
6  C u1 p0 c0 {2,S} {10,S} {17,S}
7  C u0 p0 c0 {4,D} {9,S} {19,S}
8  C u0 p0 c0 {4,S} {10,D} {20,S}
9  C u0 p0 c0 {5,D} {7,S} {18,S}
10 C u0 p0 c0 {6,S} {8,D} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([37.02,49.6,60.29,68.93,81.68,90.56,103.68],'cal/(mol*K)'),
        H298 = (63.36,'kcal/mol'),
        S298 = (91.32,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "pdt22",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {5,D} {6,S}
3  C u0 p0 c0 {1,S} {7,D} {11,S}
4  C u0 p0 c0 {1,S} {8,D} {12,S}
5  C u0 p0 c0 {2,D} {8,S} {15,S}
6  C u0 p0 c0 {2,S} {9,D} {16,S}
7  C u0 p0 c0 {3,D} {9,S} {13,S}
8  C u0 p0 c0 {4,D} {5,S} {14,S}
9  C u0 p0 c0 {6,D} {7,S} {17,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.9,40.53,49.39,56.44,66.66,73.66,83.86],'cal/(mol*K)'),
        H298 = (74.42,'kcal/mol'),
        S298 = (81.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "pdt23",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {8,S} {16,S}
5  C u0 p0 c0 {2,S} {8,D} {17,S}
6  C u0 p0 c0 {2,S} {10,D} {18,S}
7  C u0 p0 c0 {3,S} {9,D} {15,S}
8  C u0 p0 c0 {4,S} {5,D} {20,S}
9  C u0 p0 c0 {7,D} {10,S} {19,S}
10 C u0 p0 c0 {6,D} {9,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.31,49.05,59.86,68.59,81.45,90.4,103.6],'cal/(mol*K)'),
        H298 = (83.25,'kcal/mol'),
        S298 = (91.39,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "pdt24",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {7,S} {12,S}
4  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {8,S} {15,S} {16,S}
6  C u0 p0 c0 {2,S} {8,D} {19,S}
7  C u1 p0 c0 {3,S} {10,S} {20,S}
8  C u0 p0 c0 {5,S} {6,D} {18,S}
9  C u0 p0 c0 {4,S} {10,D} {17,S}
10 C u0 p0 c0 {7,S} {9,D} {21,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.9,48.9,59.87,68.68,81.59,90.53,103.69],'cal/(mol*K)'),
        H298 = (82.04,'kcal/mol'),
        S298 = (88.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "pdt25",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
2  C u0 p0 c0 {4,S} {5,B} {6,B}
3  C u0 p0 c0 {1,S} {7,D} {14,S}
4  C u1 p0 c0 {2,S} {7,S} {16,S}
5  C u0 p0 c0 {2,B} {8,B} {17,S}
6  C u0 p0 c0 {2,B} {10,B} {21,S}
7  C u0 p0 c0 {3,D} {4,S} {15,S}
8  C u0 p0 c0 {5,B} {9,B} {18,S}
9  C u0 p0 c0 {8,B} {10,B} {19,S}
10 C u0 p0 c0 {6,B} {9,B} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.73,50.54,60.75,69.11,81.61,90.41,103.53],'cal/(mol*K)'),
        H298 = (53.96,'kcal/mol'),
        S298 = (97.19,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "pdt26",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,S} {7,D}
4  C u0 p0 c0 {2,S} {3,S} {8,D}
5  C u0 p0 c0 {1,S} {9,D} {15,S}
6  C u0 p0 c0 {2,S} {10,D} {16,S}
7  C u0 p0 c0 {3,D} {10,S} {18,S}
8  C u0 p0 c0 {4,D} {9,S} {20,S}
9  C u0 p0 c0 {5,D} {8,S} {17,S}
10 C u0 p0 c0 {6,D} {7,S} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.85,46.73,56.9,65.2,77.52,86.1,98.68],'cal/(mol*K)'),
        H298 = (63.81,'kcal/mol'),
        S298 = (86.13,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "pdt27",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {11,S}
2  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u1 p0 c0 {1,S} {2,S} {5,S}
5  C u0 p0 c0 {4,S} {8,S} {9,D}
6  C u0 p0 c0 {1,S} {10,D} {17,S}
7  C u0 p0 c0 {2,S} {8,D} {18,S}
8  C u0 p0 c0 {5,S} {7,D} {21,S}
9  C u0 p0 c0 {5,D} {10,S} {20,S}
10 C u0 p0 c0 {6,D} {9,S} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([37.3,49.7,60.28,68.87,81.62,90.53,103.69],'cal/(mol*K)'),
        H298 = (62.67,'kcal/mol'),
        S298 = (92.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "pdt28",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {11,S}
2  C u0 p0 c0 {4,S} {8,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  C u0 p0 c0 {1,S} {7,D} {18,S}
6  C u0 p0 c0 {1,S} {10,D} {19,S}
7  C u0 p0 c0 {3,S} {5,D} {17,S}
8  C u0 p0 c0 {2,S} {9,D} {16,S}
9  C u0 p0 c0 {8,D} {10,S} {20,S}
10 C u0 p0 c0 {6,D} {9,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.48,48.92,59.63,68.36,81.35,90.42,103.73],'cal/(mol*K)'),
        H298 = (94.43,'kcal/mol'),
        S298 = (93.22,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "pdt29",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {7,S} {8,D}
5  C u0 p0 c0 {2,S} {7,D} {16,S}
6  C u1 p0 c0 {3,S} {9,S} {17,S}
7  C u0 p0 c0 {4,S} {5,D} {21,S}
8  C u0 p0 c0 {4,D} {10,S} {20,S}
9  C u0 p0 c0 {6,S} {10,D} {18,S}
10 C u0 p0 c0 {8,S} {9,D} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.9,48.52,59.35,68.14,81.16,90.22,103.55],'cal/(mol*K)'),
        H298 = (64.66,'kcal/mol'),
        S298 = (90.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "pdt30",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,D} {7,S}
4  C u0 p0 c0 {1,S} {9,D} {15,S}
5  C u0 p0 c0 {2,S} {8,D} {14,S}
6  C u0 p0 c0 {3,D} {9,S} {18,S}
7  C u0 p0 c0 {3,S} {10,D} {19,S}
8  C u0 p0 c0 {5,D} {10,S} {16,S}
9  C u0 p0 c0 {4,D} {6,S} {17,S}
10 C u0 p0 c0 {7,D} {8,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.58,46.66,56.96,65.3,77.6,86.14,98.66],'cal/(mol*K)'),
        H298 = (68.39,'kcal/mol'),
        S298 = (88.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "pdt31",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {7,D}
4  C u0 p0 c0 {1,S} {8,D} {15,S}
5  C u0 p0 c0 {2,S} {6,D} {14,S}
6  C u0 p0 c0 {3,S} {5,D} {19,S}
7  C u0 p0 c0 {3,D} {10,S} {18,S}
8  C u0 p0 c0 {4,D} {9,S} {20,S}
9  C u0 p0 c0 {8,S} {10,D} {16,S}
10 C u0 p0 c0 {7,S} {9,D} {17,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.48,46.59,56.91,65.26,77.59,86.13,98.67],'cal/(mol*K)'),
        H298 = (65.83,'kcal/mol'),
        S298 = (87.99,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "pdt32",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {7,S} {8,D}
5  C u0 p0 c0 {1,S} {7,D} {16,S}
6  C u1 p0 c0 {2,S} {9,S} {17,S}
7  C u0 p0 c0 {4,S} {5,D} {18,S}
8  C u0 p0 c0 {4,D} {10,S} {19,S}
9  C u0 p0 c0 {6,S} {10,D} {21,S}
10 C u0 p0 c0 {8,S} {9,D} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.79,49.32,60.02,68.69,81.53,90.47,103.66],'cal/(mol*K)'),
        H298 = (62.33,'kcal/mol'),
        S298 = (91.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "pdt33",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {5,S} {6,D}
3  C u1 p0 c0 {1,S} {2,S} {14,S}
4  C u0 p0 c0 {1,S} {5,D} {13,S}
5  C u0 p0 c0 {2,S} {4,D} {19,S}
6  C u0 p0 c0 {2,D} {8,S} {18,S}
7  C u0 p0 c0 {8,D} {9,S} {16,S}
8  C u0 p0 c0 {6,S} {7,D} {17,S}
9  C u0 p0 c0 {7,S} {10,D} {15,S}
10 C u0 p0 c0 {9,D} {20,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.82,51.85,62.06,70.3,82.49,91.05,103.83],'cal/(mol*K)'),
        H298 = (81.27,'kcal/mol'),
        S298 = (98.78,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "pdt35",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {9,D} {15,S}
6  C u0 p0 c0 {2,S} {7,D} {16,S}
7  C u0 p0 c0 {4,S} {6,D} {20,S}
8  C u0 p0 c0 {4,S} {10,D} {18,S}
9  C u0 p0 c0 {5,D} {10,S} {17,S}
10 C u0 p0 c0 {8,D} {9,S} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.04,47.01,57.21,65.5,77.74,86.25,98.74],'cal/(mol*K)'),
        H298 = (65.78,'kcal/mol'),
        S298 = (88.09,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "pdt37",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {3,S} {8,D}
5  C u1 p0 c0 {1,S} {9,S} {18,S}
6  C u0 p0 c0 {2,S} {7,D} {17,S}
7  C u0 p0 c0 {3,S} {6,D} {16,S}
8  C u0 p0 c0 {4,D} {10,S} {21,S}
9  C u0 p0 c0 {5,S} {10,D} {19,S}
10 C u0 p0 c0 {8,S} {9,D} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.83,48.48,59.3,68.09,81.13,90.21,103.57],'cal/(mol*K)'),
        H298 = (64.94,'kcal/mol'),
        S298 = (89.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "pdt38",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,B} {7,B}
4  C u0 p0 c0 {2,S} {3,B} {8,B}
5  C u0 p0 c0 {1,S} {6,D} {15,S}
6  C u0 p0 c0 {2,S} {5,D} {16,S}
7  C u0 p0 c0 {3,B} {10,B} {19,S}
8  C u0 p0 c0 {4,B} {9,B} {20,S}
9  C u0 p0 c0 {8,B} {10,B} {17,S}
10 C u0 p0 c0 {7,B} {9,B} {18,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.96,45.89,56.19,64.61,77.13,85.83,98.55],'cal/(mol*K)'),
        H298 = (35.66,'kcal/mol'),
        S298 = (86.59,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "pdt39",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {6,S} {8,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,D} {9,S}
5  C u1 p0 c0 {1,S} {10,S} {17,S}
6  C u0 p0 c0 {3,S} {4,D} {18,S}
7  C u0 p0 c0 {2,S} {10,D} {16,S}
8  C u0 p0 c0 {3,S} {9,D} {19,S}
9  C u0 p0 c0 {4,S} {8,D} {21,S}
10 C u0 p0 c0 {5,S} {7,D} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([37.07,49.88,60.68,69.33,82,90.79,103.78],'cal/(mol*K)'),
        H298 = (80.61,'kcal/mol'),
        S298 = (94.59,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "INDENE",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,B} {5,B}
3  C u0 p0 c0 {2,B} {6,S} {7,B}
4  C u0 p0 c0 {1,S} {6,D} {12,S}
5  C u0 p0 c0 {2,B} {9,B} {15,S}
6  C u0 p0 c0 {3,S} {4,D} {16,S}
7  C u0 p0 c0 {3,B} {8,B} {17,S}
8  C u0 p0 c0 {7,B} {9,B} {13,S}
9  C u0 p0 c0 {5,B} {8,B} {14,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.28,39.78,48.65,55.78,66.17,73.3,83.68],'cal/(mol*K)'),
        H298 = (40.49,'kcal/mol'),
        S298 = (79.82,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "pdt55",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {7,S} {8,D}
5  C u0 p0 c0 {2,S} {6,D} {16,S}
6  C u0 p0 c0 {3,S} {5,D} {17,S}
7  C u1 p0 c0 {4,S} {10,S} {20,S}
8  C u0 p0 c0 {4,D} {9,S} {21,S}
9  C u0 p0 c0 {8,S} {10,D} {18,S}
10 C u0 p0 c0 {7,S} {9,D} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([37.13,49.83,60.56,69.18,81.83,90.63,103.66],'cal/(mol*K)'),
        H298 = (78.24,'kcal/mol'),
        S298 = (94.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "pdt57",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {6,S} {13,S}
4  C u0 p0 c0 {1,S} {8,D} {14,S}
5  C u0 p0 c0 {2,S} {7,D} {15,S}
6  C u1 p0 c0 {3,S} {7,S} {16,S}
7  C u0 p0 c0 {5,D} {6,S} {19,S}
8  C u0 p0 c0 {4,D} {9,S} {18,S}
9  C u0 p0 c0 {8,S} {10,D} {17,S}
10 C u0 p0 c0 {9,D} {20,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.02,51.51,61.97,70.32,82.53,91.05,103.78],'cal/(mol*K)'),
        H298 = (100.54,'kcal/mol'),
        S298 = (95.99,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "pdt58",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {3,D} {5,S} {6,S}
3  C u0 p0 c0 {1,S} {2,D} {14,S}
4  C u1 p0 c0 {1,S} {9,S} {13,S}
5  C u0 p0 c0 {2,S} {7,D} {16,S}
6  C u0 p0 c0 {2,S} {8,D} {19,S}
7  C u0 p0 c0 {5,D} {8,S} {17,S}
8  C u0 p0 c0 {6,D} {7,S} {18,S}
9  C u0 p0 c0 {4,S} {10,D} {15,S}
10 C u0 p0 c0 {9,D} {20,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.62,51.66,61.84,70.06,82.22,90.76,103.59],'cal/(mol*K)'),
        H298 = (96.71,'kcal/mol'),
        S298 = (103.4,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "2HINDENE",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {4,D} {7,S}
3  C u0 p0 c0 {2,S} {5,D} {6,S}
4  C u0 p0 c0 {1,S} {2,D} {12,S}
5  C u0 p0 c0 {1,S} {3,D} {13,S}
6  C u0 p0 c0 {3,S} {8,D} {14,S}
7  C u0 p0 c0 {2,S} {9,D} {17,S}
8  C u0 p0 c0 {6,D} {9,S} {15,S}
9  C u0 p0 c0 {7,D} {8,S} {16,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.17,40.65,49.4,56.39,66.59,73.6,83.82],'cal/(mol*K)'),
        H298 = (62.6,'kcal/mol'),
        S298 = (79.2,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

