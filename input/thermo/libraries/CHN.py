#!/usr/bin/env python
# encoding: utf-8

name = "CHN"
shortDesc = u"Yaws' Critical Property Data for C, H and N compounds"
longDesc = u"""
Yaws' Critical Property Data for Chemical Engineers and Chemists
Table 30. Heat Capacity of Gas - Organic Compounds
Table 38. Enthalpy of Formation of Gas - Organic Compounds
Table 46. Entropy of Gas - Organic Compounds

Contains only compounds with carbon hydrogen and nitrogen
"""
entry(
    index = 0,
    label = "1  N 0 {2,T}",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {6,S} {12,S}
5  C u0 p0 c0 {2,S} {13,T}
6  C u0 p0 c0 {4,S} {14,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 N u0 p1 c0 {5,T}
14 N u0 p1 c0 {6,T}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "C4H5Nf",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {1,S} {4,D} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "C5H5N",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,B} {11,B}
2  H u0 p0 c0 {1,S}
3  C u0 p0 c0 {1,B} {4,S} {5,B}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,B} {6,S} {7,B}
6  H u0 p0 c0 {5,S}
7  C u0 p0 c0 {5,B} {8,S} {9,B}
8  H u0 p0 c0 {7,S}
9  C u0 p0 c0 {7,B} {10,S} {11,B}
10 H u0 p0 c0 {9,S}
11 N u0 p1 c0 {1,B} {9,B}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "C6H7Nb",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {7,B}
3  C u0 p0 c0 {2,B} {4,B} {13,S}
4  C u0 p0 c0 {3,B} {5,B} {12,S}
5  C u0 p0 c0 {4,B} {6,B} {11,S}
6  C u0 p0 c0 {5,B} {7,B} {14,S}
7  N u0 p1 c0 {2,B} {6,B}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "C6H7Nc",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {5,B}
3  C u0 p0 c0 {2,B} {4,B} {12,S}
4  C u0 p0 c0 {3,B} {6,B} {11,S}
5  C u0 p0 c0 {2,B} {7,B} {13,S}
6  C u0 p0 c0 {4,B} {7,B} {14,S}
7  N u0 p1 c0 {5,B} {6,B}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "C6H7Nd",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {11,S}
4  C u0 p0 c0 {2,B} {6,B} {12,S}
5  C u0 p0 c0 {3,B} {7,B} {13,S}
6  C u0 p0 c0 {4,B} {7,B} {14,S}
7  N u0 p1 c0 {5,B} {6,B}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "C7H5N",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,T}
2  C u0 p0 c0 {1,S} {3,B} {7,B}
3  C u0 p0 c0 {2,B} {4,B} {9,S}
4  C u0 p0 c0 {3,B} {5,B} {10,S}
5  C u0 p0 c0 {4,B} {6,B} {11,S}
6  C u0 p0 c0 {5,B} {7,B} {12,S}
7  C u0 p0 c0 {2,B} {6,B} {13,S}
8  N u0 p1 c0 {1,T}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "C7H9N",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {7,B}
3  C u0 p0 c0 {2,B} {4,B} {11,S}
4  C u0 p0 c0 {3,B} {5,B} {12,S}
5  C u0 p0 c0 {4,B} {6,B} {13,S}
6  C u0 p0 c0 {5,B} {7,B} {14,S}
7  C u0 p0 c0 {2,B} {6,B} {15,S}
8  N u0 p1 c0 {1,S} {16,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "HCN",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 N u0 p1 c0 {2,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.586,9.343,9.974,10.491,11.31,12.005,13.217],'cal/(mol*K)'),
        H298 = (31.095,'kcal/mol'),
        S298 = (48.139,'cal/(mol*K)'),
    ),
    shortDesc = u"""hydrogen cyanide""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "CH5N",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 N u0 p1 c0 {1,S} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.004,14.388,16.745,18.878,22.359,25.069,29.484],'cal/(mol*K)'),
        H298 = (-5.376,'kcal/mol'),
        S298 = (58.097,'cal/(mol*K)'),
    ),
    shortDesc = u"""methylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "C2H3Na",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 C u0 p0 c0 {1,S} {6,T}
6 N u0 p1 c0 {5,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.53,14.684,16.618,18.359,21.288,23.518,27.008],'cal/(mol*K)'),
        H298 = (15.393,'kcal/mol'),
        S298 = (57.976,'cal/(mol*K)'),
    ),
    shortDesc = u"""acetonitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "C2H5N",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 N u0 p1 c0 {1,S} {2,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.311,16.357,20.16,23.314,27.88,31.24,34.88],'cal/(mol*K)'),
        H298 = (29.502,'kcal/mol'),
        S298 = (59.981,'cal/(mol*K)'),
    ),
    shortDesc = u"""ethyleneimine""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "C2H7Na",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  N u0 p1 c0 {1,S} {9,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.172,21.182,24.9,28.096,33.052,36.876,43.303],'cal/(mol*K)'),
        H298 = (-11.351,'kcal/mol'),
        S298 = (67.773,'cal/(mol*K)'),
    ),
    shortDesc = u"""ethylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "C2H7Nb",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  N u0 p1 c0 {1,S} {2,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.918,21.241,25.38,29.039,34.849,39.271,46.159],'cal/(mol*K)'),
        H298 = (-4.443,'kcal/mol'),
        S298 = (64.646,'cal/(mol*K)'),
    ),
    shortDesc = u"""dimethylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "C2H8N2",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  H u0 p0 c0 {4,S}
6  H u0 p0 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  H u0 p0 c0 {7,S}
9  H u0 p0 c0 {7,S}
10 N u0 p1 c0 {7,S} {11,S} {12,S}
11 H u0 p0 c0 {10,S}
12 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.892,26.763,31.19,35.017,41.081,45.663,51.821],'cal/(mol*K)'),
        H298 = (-4.137,'kcal/mol'),
        S298 = (76.833,'cal/(mol*K)'),
    ),
    shortDesc = u"""ethylenediamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "C3H2N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 C u0 p0 c0 {3,S} {7,T}
7 N u0 p1 c0 {6,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.176,20.093,22.62,24.785,28.023,30.059,34.113],'cal/(mol*K)'),
        H298 = (63.456,'kcal/mol'),
        S298 = (68.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""malononitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "C3H3N",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,D}
4 H u0 p0 c0 {3,S}
5 C u0 p0 c0 {3,D} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.34,18.352,20.973,23.157,26.46,28.905,32.651],'cal/(mol*K)'),
        H298 = (43.165,'kcal/mol'),
        S298 = (65.438,'cal/(mol*K)'),
    ),
    shortDesc = u"""acrylonitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "C3H5Na",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
7 H u0 p0 c0 {6,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.705,21.461,24.847,27.755,32.349,35.827,40.001],'cal/(mol*K)'),
        H298 = (12.31,'kcal/mol'),
        S298 = (68.213,'cal/(mol*K)'),
    ),
    shortDesc = u"""propionitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "C3H7Na",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  N u0 p1 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.905,25.181,29.354,32.999,38.647,42.967,49.356],'cal/(mol*K)'),
        H298 = (13.912,'kcal/mol'),
        S298 = (74.754,'cal/(mol*K)'),
    ),
    shortDesc = u"""allylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "C3H7Nb",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  N u0 p1 c0 {1,S} {2,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.131,23.952,29.296,33.625,39.704,44.217,50.181],'cal/(mol*K)'),
        H298 = (21.226,'kcal/mol'),
        S298 = (68.823,'cal/(mol*K)'),
    ),
    shortDesc = u"""propyleneimine""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "C3H9Na",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  N u0 p1 c0 {2,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.896,27.632,32.988,37.658,45.002,50.559,59.273],'cal/(mol*K)'),
        H298 = (-16.752,'kcal/mol'),
        S298 = (77.769,'cal/(mol*K)'),
    ),
    shortDesc = u"""propylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "C3H9Nb",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  N u0 p1 c0 {1,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.422,29.082,34.185,38.555,45.37,50.55,58.772],'cal/(mol*K)'),
        H298 = (-20.002,'kcal/mol'),
        S298 = (74.642,'cal/(mol*K)'),
    ),
    shortDesc = u"""isopropylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "C3H9Nc",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  N u0 p1 c0 {1,S} {3,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.089,27.747,33.185,37.89,45.072,50.428,58.413],'cal/(mol*K)'),
        H298 = (-10.8,'kcal/mol'),
        S298 = (80.198,'cal/(mol*K)'),
    ),
    shortDesc = u"""methylethylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "C3H9Nd",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  N u0 p1 c0 {1,S} {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.04,28.033,33.63,38.39,45.619,50.98,56.919],'cal/(mol*K)'),
        H298 = (-5.662,'kcal/mol'),
        S298 = (69.272,'cal/(mol*K)'),
    ),
    shortDesc = u"""trimethylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "C3H10N2a",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  N u0 p1 c0 {1,S} {14,S} {15,S}
5  N u0 p1 c0 {2,S} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.508,33.968,39.851,44.87,52.574,58.297,66.709],'cal/(mol*K)'),
        H298 = (-12.827,'kcal/mol'),
        S298 = (86.212,'cal/(mol*K)'),
    ),
    shortDesc = u"""1,2-propanediamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "C3H10N2c",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  N u0 p1 c0 {2,S} {12,S} {13,S}
5  N u0 p1 c0 {3,S} {14,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.501,33.461,39.521,44.925,53.297,59.443,68.265],'cal/(mol*K)'),
        H298 = (-12.827,'kcal/mol'),
        S298 = (86.211,'cal/(mol*K)'),
    ),
    shortDesc = u"""1,3-propanediamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "C4H4N2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,T}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {5,T}
5  N u0 p1 c0 {4,T}
6  N u0 p1 c0 {1,T}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.562,27.064,30.961,34.191,39.01,42.517,48.251],'cal/(mol*K)'),
        H298 = (50.12,'kcal/mol'),
        S298 = (78.218,'cal/(mol*K)'),
    ),
    shortDesc = u"""succinonitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "C4H5Nc",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {10,T}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 N u0 p1 c0 {4,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.882,25.991,29.745,33.026,38.221,41.968,47.078],'cal/(mol*K)'),
        H298 = (23.431,'kcal/mol'),
        S298 = (53.574,'cal/(mol*K)'),
    ),
    shortDesc = u"""methacrylonitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "C4H5Nd",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {10,T}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 N u0 p1 c0 {4,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.844,24.948,28.709,31.977,37.111,40.838,45.811],'cal/(mol*K)'),
        H298 = (37.716,'kcal/mol'),
        S298 = (72.629,'cal/(mol*K)'),
    ),
    shortDesc = u"""vinylacetonitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "C4H5Ne",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {10,T}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 N u0 p1 c0 {4,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.119,24.291,28.109,31.442,36.718,40.641,46.606],'cal/(mol*K)'),
        H298 = (33.837,'kcal/mol'),
        S298 = (75.511,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-butenenitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "C4H7Na",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,T}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 N u0 p1 c0 {4,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.639,28.949,33.733,37.76,43.874,48.518,55.712],'cal/(mol*K)'),
        H298 = (8.008,'kcal/mol'),
        S298 = (77.888,'cal/(mol*K)'),
    ),
    shortDesc = u"""butyronitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "C4H7Nb",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,T}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 N u0 p1 c0 {4,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.812,29.17,33.999,38.056,44.18,48.781,55.88],'cal/(mol*K)'),
        H298 = (5.762,'kcal/mol'),
        S298 = (74.922,'cal/(mol*K)'),
    ),
    shortDesc = u"""isobutyronitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "C4H9N",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.521,27.096,34.391,40.493,49.35,55.839,62.344],'cal/(mol*K)'),
        H298 = (-0.833,'kcal/mol'),
        S298 = (74.172,'cal/(mol*K)'),
    ),
    shortDesc = u"""pyrrolidine""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "C4H10N2",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  N u0 p1 c0 {3,S} {5,S} {12,S}
5  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.681,38.019,46.529,53.227,61.535,66.474,75.644],'cal/(mol*K)'),
        H298 = (5.333,'kcal/mol'),
        S298 = (77.009,'cal/(mol*K)'),
    ),
    shortDesc = u"""piperazine""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "C4H11Na",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  N u0 p1 c0 {3,S} {15,S} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.051,35.149,41.224,46.816,56.031,62.846,72.535],'cal/(mol*K)'),
        H298 = (-21.986,'kcal/mol'),
        S298 = (87.123,'cal/(mol*K)'),
    ),
    shortDesc = u"""butylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "C4H11Nb",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  N u0 p1 c0 {2,S} {15,S} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.894,34.862,41.554,47.288,55.927,62.392,72.012],'cal/(mol*K)'),
        H298 = (-23.551,'kcal/mol'),
        S298 = (84.198,'cal/(mol*K)'),
    ),
    shortDesc = u"""isobutylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "C4H11Nc",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  N u0 p1 c0 {1,S} {15,S} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.471,35.2,41.791,47.592,56.458,62.749,72.424],'cal/(mol*K)'),
        H298 = (-25.009,'kcal/mol'),
        S298 = (85.32,'cal/(mol*K)'),
    ),
    shortDesc = u"""sec-butylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "C4H11Nd",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  N u0 p1 c0 {1,S} {15,S} {16,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.039,36.161,42.424,47.802,56.329,62.782,72.992],'cal/(mol*K)'),
        H298 = (-28.845,'kcal/mol'),
        S298 = (78.386,'cal/(mol*K)'),
    ),
    shortDesc = u"""tert-butylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "C4H11Nf",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  N u0 p1 c0 {2,S} {4,S} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.586,34.649,41.426,47.273,56.155,62.759,72.696],'cal/(mol*K)'),
        H298 = (-15.771,'kcal/mol'),
        S298 = (89.377,'cal/(mol*K)'),
    ),
    shortDesc = u"""methyl-propylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "C4H11Ng",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  N u0 p1 c0 {1,S} {4,S} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.536,34.67,41.525,47.429,56.334,62.887,72.845],'cal/(mol*K)'),
        H298 = (-18.831,'kcal/mol'),
        S298 = (81.072,'cal/(mol*K)'),
    ),
    shortDesc = u"""methylisopropylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "C4H11Nh",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  N u0 p1 c0 {1,S} {2,S} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.602,34.897,41.137,46.87,56.267,63.14,73.138],'cal/(mol*K)'),
        H298 = (-17.134,'kcal/mol'),
        S298 = (84.158,'cal/(mol*K)'),
    ),
    shortDesc = u"""diethylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "C4H11Ni",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
5  N u0 p1 c0 {1,S} {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.537,34.884,41.842,47.739,56.515,63.031,72.338],'cal/(mol*K)'),
        H298 = (-11.947,'kcal/mol'),
        S298 = (85.056,'cal/(mol*K)'),
    ),
    shortDesc = u"""dimethylethylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "C4H13N3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  N u0 p1 c0 {1,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
4  N u0 p1 c0 {3,S} {5,S} {14,S}
5  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {5,S} {7,S} {17,S} {18,S}
7  N u0 p1 c0 {6,S} {19,S} {20,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.569,45.568,53.741,60.623,71.04,78.827,89.457],'cal/(mol*K)'),
        H298 = (-1.397,'kcal/mol'),
        S298 = (106.311,'cal/(mol*K)'),
    ),
    shortDesc = u"""diethylene triamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "C5H6N2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,T}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {12,S} {13,S}
5  C u0 p0 c0 {4,S} {6,T}
6  N u0 p1 c0 {5,T}
7  N u0 p1 c0 {1,T}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.121,33.936,39.13,43.543,50.17,54.734,62.115],'cal/(mol*K)'),
        H298 = (40.632,'kcal/mol'),
        S298 = (87.821,'cal/(mol*K)'),
    ),
    shortDesc = u"""glutaronitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "C5H9Na",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,T}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 N u0 p1 c0 {5,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.248,35.622,41.593,46.796,54.949,61.006,69.908],'cal/(mol*K)'),
        H298 = (2.741,'kcal/mol'),
        S298 = (87.499,'cal/(mol*K)'),
    ),
    shortDesc = u"""valeronitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "C5H9Nb",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,T}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 N u0 p1 c0 {5,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.86,35.371,41.472,46.745,54.848,60.779,69.648],'cal/(mol*K)'),
        H298 = (1.102,'kcal/mol'),
        S298 = (86.121,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-methylbutanenitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "C5H9Nc",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {15,T}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 N u0 p1 c0 {5,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.86,35.371,41.472,46.745,54.848,60.779,69.648],'cal/(mol*K)'),
        H298 = (1.054,'kcal/mol'),
        S298 = (84.838,'cal/(mol*K)'),
    ),
    shortDesc = u"""3-methylbutanenitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "C5H9Nd",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,T}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 N u0 p1 c0 {5,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.893,36.811,43.038,48.224,55.932,61.687,70.507],'cal/(mol*K)'),
        H298 = (-0.595,'kcal/mol'),
        S298 = (79.146,'cal/(mol*K)'),
    ),
    shortDesc = u"""2,2-dimethylpropanenitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "C5H11Na",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
6  N u0 p1 c0 {3,S} {4,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.861,34.175,42.999,50.35,60.97,68.656,77.447],'cal/(mol*K)'),
        H298 = (-1.937,'kcal/mol'),
        S298 = (78.782,'cal/(mol*K)'),
    ),
    shortDesc = u"""N-methylpyrrolidine""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "C5H11Nb",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
6  N u0 p1 c0 {4,S} {5,S} {17,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.291,39.783,48.601,55.631,64.638,70.074,75.825],'cal/(mol*K)'),
        H298 = (-11.685,'kcal/mol'),
        S298 = (80.558,'cal/(mol*K)'),
    ),
    shortDesc = u"""piperidine""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "C5H11Nc",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
6  N u0 p1 c0 {1,S} {4,S} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.373,34.279,42.579,50.435,62.979,70.663,79.303],'cal/(mol*K)'),
        H298 = (-1.937,'kcal/mol'),
        S298 = (78.781,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-methylpyrrolidine""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "C5H11Nd",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
6  N u0 p1 c0 {3,S} {4,S} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.855,32.307,40.129,47.533,59.355,66.597,74.739],'cal/(mol*K)'),
        H298 = (-1.937,'kcal/mol'),
        S298 = (78.782,'cal/(mol*K)'),
    ),
    shortDesc = u"""3-methylpyrrolidine""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "C5H13Na",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  N u0 p1 c0 {4,S} {18,S} {19,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.626,41.798,49.687,56.527,67.032,74.939,86.493],'cal/(mol*K)'),
        H298 = (-26.933,'kcal/mol'),
        S298 = (96.559,'cal/(mol*K)'),
    ),
    shortDesc = u"""pentylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "C5H13Nb",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  N u0 p1 c0 {1,S} {18,S} {19,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.962,42.253,50.22,57.067,67.375,74.998,86.561],'cal/(mol*K)'),
        H298 = (-29.323,'kcal/mol'),
        S298 = (94.715,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-methylbutylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "C5H13Nc",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6  N u0 p1 c0 {3,S} {18,S} {19,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.962,42.253,50.22,57.067,67.375,74.998,86.561],'cal/(mol*K)'),
        H298 = (-29.323,'kcal/mol'),
        S298 = (90.122,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-methylbutylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "C5H13Nd",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  N u0 p1 c0 {3,S} {18,S} {19,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.962,42.253,50.22,57.067,67.375,74.998,86.561],'cal/(mol*K)'),
        H298 = (-26.933,'kcal/mol'),
        S298 = (98.138,'cal/(mol*K)'),
    ),
    shortDesc = u"""3-methylbutylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "C5H13Ne",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
6  N u0 p1 c0 {1,S} {18,S} {19,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.947,42.832,51.193,58.099,67.927,75.22,86.817],'cal/(mol*K)'),
        H298 = (-26.933,'kcal/mol'),
        S298 = (93.905,'cal/(mol*K)'),
    ),
    shortDesc = u"""1,1-dimethylpropylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "C5H13Nf",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
6  N u0 p1 c0 {2,S} {18,S} {19,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.912,42.274,50.32,57.223,67.554,75.127,86.71],'cal/(mol*K)'),
        H298 = (-26.933,'kcal/mol'),
        S298 = (100.094,'cal/(mol*K)'),
    ),
    shortDesc = u"""1,2-dimethylpropylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "C5H13Ng",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  N u0 p1 c0 {2,S} {18,S} {19,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.947,42.832,51.193,58.099,67.927,75.22,86.817],'cal/(mol*K)'),
        H298 = (-26.933,'kcal/mol'),
        S298 = (93.905,'cal/(mol*K)'),
    ),
    shortDesc = u"""2,2-dimethylpropylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "C5H13Nh",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  N u0 p1 c0 {1,S} {18,S} {19,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.947,42.832,51.193,58.099,67.927,75.22,86.817],'cal/(mol*K)'),
        H298 = (-27.615,'kcal/mol'),
        S298 = (95.349,'cal/(mol*K)'),
    ),
    shortDesc = u"""3-pentanamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "C5H13Ni",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
6  N u0 p1 c0 {3,S} {5,S} {19,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.083,41.551,49.666,56.655,67.237,75.089,86.979],'cal/(mol*K)'),
        H298 = (-20.742,'kcal/mol'),
        S298 = (98.555,'cal/(mol*K)'),
    ),
    shortDesc = u"""methyl-butylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "C5H13Nj",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
6  N u0 p1 c0 {2,S} {5,S} {19,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.033,41.572,49.765,56.811,67.416,75.218,87.128],'cal/(mol*K)'),
        H298 = (-22.344,'kcal/mol'),
        S298 = (95.14,'cal/(mol*K)'),
    ),
    shortDesc = u"""methylisobutylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "C5H13Nk",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
6  N u0 p1 c0 {1,S} {5,S} {19,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.033,41.572,49.765,56.811,67.416,75.218,87.128],'cal/(mol*K)'),
        H298 = (-23.323,'kcal/mol'),
        S298 = (91.854,'cal/(mol*K)'),
    ),
    shortDesc = u"""methyl-sec-butylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "C5H13Nl",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
6  N u0 p1 c0 {1,S} {5,S} {19,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.018,42.152,50.738,57.844,67.968,75.44,87.385],'cal/(mol*K)'),
        H298 = (-25.881,'kcal/mol'),
        S298 = (79.044,'cal/(mol*K)'),
    ),
    shortDesc = u"""methyl-tert-butylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "C5H13Nm",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  N u0 p1 c0 {2,S} {3,S} {19,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.083,41.551,49.666,56.655,67.237,75.089,86.979],'cal/(mol*K)'),
        H298 = (-22.105,'kcal/mol'),
        S298 = (93.986,'cal/(mol*K)'),
    ),
    shortDesc = u"""ethylpropylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "C5H13Nn",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
6  N u0 p1 c0 {1,S} {2,S} {19,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.033,41.572,49.765,56.811,67.416,75.218,87.128],'cal/(mol*K)'),
        H298 = (-25.164,'kcal/mol'),
        S298 = (85.681,'cal/(mol*K)'),
    ),
    shortDesc = u"""ethylisopropylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "C5H13No",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
6  N u0 p1 c0 {1,S} {2,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.034,41.789,50.082,57.118,67.597,75.361,86.489],'cal/(mol*K)'),
        H298 = (-18.28,'kcal/mol'),
        S298 = (89.665,'cal/(mol*K)'),
    ),
    shortDesc = u"""methyldiethylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "C5H13Np",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
6  N u0 p1 c0 {2,S} {4,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.034,41.789,50.082,57.118,67.597,75.361,86.489],'cal/(mol*K)'),
        H298 = (-16.918,'kcal/mol'),
        S298 = (94.234,'cal/(mol*K)'),
    ),
    shortDesc = u"""dimethyl-propylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "C5H13Nq",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
6  N u0 p1 c0 {1,S} {4,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([32.984,41.811,50.182,57.274,67.776,75.49,86.637],'cal/(mol*K)'),
        H298 = (-19.977,'kcal/mol'),
        S298 = (85.93,'cal/(mol*K)'),
    ),
    shortDesc = u"""dimethylisopropylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "C6H6N2c",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  C u0 p0 c0 {1,S} {13,T}
6  C u0 p0 c0 {2,S} {14,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 N u0 p1 c0 {5,T}
14 N u0 p1 c0 {6,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.367,36.725,42.46,47.356,54.637,59.462,67.481],'cal/(mol*K)'),
        H298 = (62.382,'kcal/mol'),
        S298 = (94.002,'cal/(mol*K)'),
    ),
    shortDesc = u"""trans-1,4-dicyano-2-butene""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "C6H7Na",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {8,S}
3  C u0 p0 c0 {1,B} {6,B} {12,S}
4  C u0 p0 c0 {2,B} {5,B} {9,S}
5  C u0 p0 c0 {4,B} {6,B} {10,S}
6  C u0 p0 c0 {3,B} {5,B} {11,S}
7  N u0 p1 c0 {1,S} {13,S} {14,S}
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
        Cpdata = ([25.945,33.954,40.75,46.187,53.848,59.178,67.041],'cal/(mol*K)'),
        H298 = (20.762,'kcal/mol'),
        S298 = (76.439,'cal/(mol*K)'),
    ),
    shortDesc = u"""aniline""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "C6H8N2a",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {16,T}
6  C u0 p0 c0 {4,S} {15,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 N u0 p1 c0 {6,T}
16 N u0 p1 c0 {5,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.472,41.351,48.212,53.702,61.442,67.168,76.227],'cal/(mol*K)'),
        H298 = (35.733,'kcal/mol'),
        S298 = (95.726,'cal/(mol*K)'),
    ),
    shortDesc = u"""adiponitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "C6H8N2b",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,T}
6  C u0 p0 c0 {3,S} {16,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 N u0 p1 c0 {5,T}
16 N u0 p1 c0 {6,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.231,41.062,47.176,52.47,60.795,66.818,75.829],'cal/(mol*K)'),
        H298 = (33.941,'kcal/mol'),
        S298 = (93.168,'cal/(mol*K)'),
    ),
    shortDesc = u"""methylglutaronitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "C6H8N2c",
    molecule = 
"""
1  C u0 p0 c0 {3,B} {5,B} {8,S}
2  C u0 p0 c0 {3,B} {4,B} {7,S}
3  C u0 p0 c0 {1,B} {2,B} {9,S}
4  C u0 p0 c0 {2,B} {6,B} {10,S}
5  C u0 p0 c0 {1,B} {6,B} {12,S}
6  C u0 p0 c0 {4,B} {5,B} {11,S}
7  N u0 p1 c0 {2,S} {13,S} {14,S}
8  N u0 p1 c0 {1,S} {15,S} {16,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([32.227,40.716,48.253,54.234,62.198,67.609,76.726],'cal/(mol*K)'),
        H298 = (21.799,'kcal/mol'),
        S298 = (86.115,'cal/(mol*K)'),
    ),
    shortDesc = u"""m-phenylenediamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "C6H8N2d",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {4,B} {8,S}
2  C u0 p0 c0 {1,B} {3,B} {7,S}
3  C u0 p0 c0 {2,B} {5,B} {9,S}
4  C u0 p0 c0 {1,B} {6,B} {12,S}
5  C u0 p0 c0 {3,B} {6,B} {10,S}
6  C u0 p0 c0 {4,B} {5,B} {11,S}
7  N u0 p1 c0 {2,S} {13,S} {14,S}
8  N u0 p1 c0 {1,S} {15,S} {16,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([32.227,40.716,48.253,54.234,62.198,67.609,76.726],'cal/(mol*K)'),
        H298 = (21.799,'kcal/mol'),
        S298 = (86.115,'cal/(mol*K)'),
    ),
    shortDesc = u"""o-phenylenediamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "C6H8N2e",
    molecule = 
"""
1  C u0 p0 c0 {3,B} {6,B} {8,S}
2  C u0 p0 c0 {4,B} {5,B} {7,S}
3  C u0 p0 c0 {1,B} {4,B} {9,S}
4  C u0 p0 c0 {2,B} {3,B} {10,S}
5  C u0 p0 c0 {2,B} {6,B} {11,S}
6  C u0 p0 c0 {1,B} {5,B} {12,S}
7  N u0 p1 c0 {2,S} {13,S} {14,S}
8  N u0 p1 c0 {1,S} {15,S} {16,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([32.227,40.716,48.253,54.234,62.198,67.609,76.726],'cal/(mol*K)'),
        H298 = (21.799,'kcal/mol'),
        S298 = (83.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""p-phenylenediamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "C6H8N2f",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {9,S}
3  C u0 p0 c0 {1,B} {6,B} {13,S}
4  C u0 p0 c0 {2,B} {5,B} {10,S}
5  C u0 p0 c0 {4,B} {6,B} {11,S}
6  C u0 p0 c0 {3,B} {5,B} {12,S}
7  N u0 p1 c0 {1,S} {8,S} {14,S}
8  N u0 p1 c0 {7,S} {15,S} {16,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.646,38.426,46.342,52.629,61.019,66.867,75.884],'cal/(mol*K)'),
        H298 = (48.64,'kcal/mol'),
        S298 = (84.008,'cal/(mol*K)'),
    ),
    shortDesc = u"""phenylhydrazine""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "C6H11Na",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,T}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 N u0 p1 c0 {6,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.828,42.57,49.859,56.222,66.174,73.527,84.256],'cal/(mol*K)'),
        H298 = (-2.208,'kcal/mol'),
        S298 = (96.798,'cal/(mol*K)'),
    ),
    shortDesc = u"""hexanenitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "C6H11Nb",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {18,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 N u0 p1 c0 {6,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.358,42.278,49.712,56.122,65.93,73.11,83.778],'cal/(mol*K)'),
        H298 = (-4.137,'kcal/mol'),
        S298 = (94.097,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-methylpentanenitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "C6H11Nc",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {18,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 N u0 p1 c0 {6,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.358,42.278,49.712,56.122,65.93,73.11,83.778],'cal/(mol*K)'),
        H298 = (-4.137,'kcal/mol'),
        S298 = (91.131,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-ethylbutanenitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "C6H11Nd",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {18,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 N u0 p1 c0 {6,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.358,42.278,49.712,56.122,65.93,73.11,83.778],'cal/(mol*K)'),
        H298 = (-3.907,'kcal/mol'),
        S298 = (93.664,'cal/(mol*K)'),
    ),
    shortDesc = u"""3-methylpentanenitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "C6H11Ne",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {18,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 N u0 p1 c0 {6,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.358,42.278,49.712,56.122,65.93,73.11,83.778],'cal/(mol*K)'),
        H298 = (-3.907,'kcal/mol'),
        S298 = (93.744,'cal/(mol*K)'),
    ),
    shortDesc = u"""4-methylpentanenitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "C6H11Nf",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {18,T}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 N u0 p1 c0 {6,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.343,42.858,50.685,57.154,66.482,73.332,84.033],'cal/(mol*K)'),
        H298 = (-4.947,'kcal/mol'),
        S298 = (95.147,'cal/(mol*K)'),
    ),
    shortDesc = u"""2,2-dimethylbutanenitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "C6H11Ng",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {2,S} {18,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 N u0 p1 c0 {6,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.307,42.3,49.812,56.278,66.11,73.239,83.925],'cal/(mol*K)'),
        H298 = (-5.836,'kcal/mol'),
        S298 = (88.638,'cal/(mol*K)'),
    ),
    shortDesc = u"""2,3-dimethylbutanenitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "C6H11Nh",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {18,T}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 N u0 p1 c0 {6,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.343,42.858,50.685,57.154,66.482,73.332,84.033],'cal/(mol*K)'),
        H298 = (-7.528,'kcal/mol'),
        S298 = (83.203,'cal/(mol*K)'),
    ),
    shortDesc = u"""3,3-dimethylbutanenitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "C6H12N2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
2  N u0 p1 c0 {1,S} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
5  N u0 p1 c0 {4,S} {6,S} {7,S}
6  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {8,S} {17,S} {18,S}
8  C u0 p0 c0 {2,S} {7,S} {19,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.584,41.307,53.451,63.284,76.49,85.657,97.208],'cal/(mol*K)'),
        H298 = (12.6,'kcal/mol'),
        S298 = (85.655,'cal/(mol*K)'),
    ),
    shortDesc = u"""triethylenediamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "C6H13Na",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {3,S} {5,S} {15,S} {16,S}
7  N u0 p1 c0 {1,S} {19,S} {20,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([32.032,42.884,53.391,62.339,75.432,84.66,96.56],'cal/(mol*K)'),
        H298 = (-25.068,'kcal/mol'),
        S298 = (84.055,'cal/(mol*K)'),
    ),
    shortDesc = u"""cyclohexylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "C6H13Nb",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
7  N u0 p1 c0 {5,S} {6,S} {20,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.162,39.657,50.825,60.235,73.861,83.65,94.931],'cal/(mol*K)'),
        H298 = (-8.165,'kcal/mol'),
        S298 = (85.38,'cal/(mol*K)'),
    ),
    shortDesc = u"""hexamethyleneimine""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "C6H15Na",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  N u0 p1 c0 {5,S} {21,S} {22,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([40.184,48.722,57.278,65.18,78.179,87.679,101.198],'cal/(mol*K)'),
        H298 = (-31.856,'kcal/mol'),
        S298 = (105.913,'cal/(mol*K)'),
    ),
    shortDesc = u"""hexylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "C6H15Nb",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  N u0 p1 c0 {1,S} {21,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.459,49.149,58.461,66.452,78.457,87.329,100.793],'cal/(mol*K)'),
        H298 = (-34.365,'kcal/mol'),
        S298 = (99.06,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-aminohexane""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "C6H15Nc",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  N u0 p1 c0 {1,S} {21,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.459,49.149,58.461,66.452,78.457,87.329,100.793],'cal/(mol*K)'),
        H298 = (-33.887,'kcal/mol'),
        S298 = (100.663,'cal/(mol*K)'),
    ),
    shortDesc = u"""3-aminohexane""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "C6H15Nd",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
7  N u0 p1 c0 {4,S} {21,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.459,49.149,58.461,66.452,78.457,87.329,100.793],'cal/(mol*K)'),
        H298 = (-32.907,'kcal/mol'),
        S298 = (103.95,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-amino-2-methylpentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "C6H15Ne",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
7  N u0 p1 c0 {4,S} {21,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.459,49.149,58.461,66.452,78.457,87.329,100.793],'cal/(mol*K)'),
        H298 = (-32.907,'kcal/mol'),
        S298 = (103.95,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-amino-3-methylpentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "C6H15Nf",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
7  N u0 p1 c0 {4,S} {21,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.459,49.149,58.461,66.452,78.457,87.329,100.793],'cal/(mol*K)'),
        H298 = (-33.385,'kcal/mol'),
        S298 = (102.346,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-amino-4-methylpentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "C6H15Ng",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
7  N u0 p1 c0 {1,S} {21,S} {22,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.444,49.729,59.433,67.485,79.009,87.551,101.049],'cal/(mol*K)'),
        H298 = (-37.544,'kcal/mol'),
        S298 = (84.165,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-amino-2-methylpentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "C6H15Nh",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
6  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
7  N u0 p1 c0 {2,S} {21,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.408,49.171,58.56,66.609,78.637,87.457,100.941],'cal/(mol*K)'),
        H298 = (-34.771,'kcal/mol'),
        S298 = (99.653,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-amino-3-methylpentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "C6H15Ni",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
7  N u0 p1 c0 {2,S} {21,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.408,49.171,58.56,66.609,78.637,87.457,100.941],'cal/(mol*K)'),
        H298 = (-35.728,'kcal/mol'),
        S298 = (96.446,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-amino-4-methylpentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "C6H15Nj",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
7  N u0 p1 c0 {2,S} {21,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.408,49.171,58.56,66.609,78.637,87.457,100.941],'cal/(mol*K)'),
        H298 = (-34.771,'kcal/mol'),
        S298 = (99.653,'cal/(mol*K)'),
    ),
    shortDesc = u"""3-amino-2-methylpentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "C6H15Nk",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
6  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
7  N u0 p1 c0 {1,S} {21,S} {22,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.444,49.729,59.433,67.485,79.009,87.551,101.049],'cal/(mol*K)'),
        H298 = (-36.349,'kcal/mol'),
        S298 = (88.174,'cal/(mol*K)'),
    ),
    shortDesc = u"""3-amino-3-methylpentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "C6H15Nl",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
7  N u0 p1 c0 {3,S} {21,S} {22,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.444,49.729,59.433,67.485,79.009,87.551,101.049],'cal/(mol*K)'),
        H298 = (-34.604,'kcal/mol'),
        S298 = (94.025,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-amino-2,2-dimethylbutane""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "C6H15Nm",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
3  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
7  N u0 p1 c0 {3,S} {21,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.408,49.171,58.56,66.609,78.637,87.457,100.941],'cal/(mol*K)'),
        H298 = (-33.792,'kcal/mol'),
        S298 = (102.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-amino-2,3-dimethylbutane""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "C6H15Nn",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {7,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
7  N u0 p1 c0 {3,S} {21,S} {22,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.444,49.729,59.433,67.485,79.009,87.551,101.049],'cal/(mol*K)'),
        H298 = (-35.799,'kcal/mol'),
        S298 = (90.017,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-amino-3,3-dimethylbutane""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "C6H15No",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
6  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
7  N u0 p1 c0 {1,S} {21,S} {22,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.394,49.751,59.533,67.641,79.189,87.679,101.198],'cal/(mol*K)'),
        H298 = (-37.353,'kcal/mol'),
        S298 = (86.763,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-amino-2,3-dimethylbutane""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "C6H15Np",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
7  N u0 p1 c0 {2,S} {21,S} {22,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.394,49.751,59.533,67.641,79.189,87.679,101.198],'cal/(mol*K)'),
        H298 = (-36.588,'kcal/mol'),
        S298 = (89.328,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-amino-3,3-dimethyl butane""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "C6H15Nq",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
7  N u0 p1 c0 {4,S} {21,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.459,49.149,58.461,66.452,78.457,87.329,100.793],'cal/(mol*K)'),
        H298 = (-32.429,'kcal/mol'),
        S298 = (105.553,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-amino-2-ethylbutane""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "C6H15Ns",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
7  N u0 p1 c0 {4,S} {6,S} {22,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.58,48.453,57.907,66.037,78.319,87.42,101.262],'cal/(mol*K)'),
        H298 = (-25.689,'kcal/mol'),
        S298 = (107.814,'cal/(mol*K)'),
    ),
    shortDesc = u"""methylpentylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "C6H15Nt",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
7  N u0 p1 c0 {1,S} {6,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.53,48.475,58.006,66.194,78.498,87.548,101.411],'cal/(mol*K)'),
        H298 = (-28.27,'kcal/mol'),
        S298 = (101.112,'cal/(mol*K)'),
    ),
    shortDesc = u"""methyl-1-methylbutylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "C6H15Nu",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
7  N u0 p1 c0 {3,S} {6,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.53,48.475,58.006,66.194,78.498,87.548,101.411],'cal/(mol*K)'),
        H298 = (-26.812,'kcal/mol'),
        S298 = (106.002,'cal/(mol*K)'),
    ),
    shortDesc = u"""methyl-2-methylbutylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "C6H15Nv",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
7  N u0 p1 c0 {3,S} {6,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.53,48.475,58.006,66.194,78.498,87.548,101.411],'cal/(mol*K)'),
        H298 = (-27.29,'kcal/mol'),
        S298 = (104.399,'cal/(mol*K)'),
    ),
    shortDesc = u"""methyl-3-methylbutylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "C6H15Nw",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
7  N u0 p1 c0 {1,S} {6,S} {22,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.515,49.054,58.978,67.226,79.05,87.77,101.668],'cal/(mol*K)'),
        H298 = (-29.633,'kcal/mol'),
        S298 = (92.31,'cal/(mol*K)'),
    ),
    shortDesc = u"""methyl-1,1-dimethylpropylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "C6H15Nx",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
7  N u0 p1 c0 {2,S} {6,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.53,48.475,58.006,66.194,78.498,87.548,101.411],'cal/(mol*K)'),
        H298 = (-29.155,'kcal/mol'),
        S298 = (98.146,'cal/(mol*K)'),
    ),
    shortDesc = u"""methyl-1,2-dimethylpropylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "C6H15Ny",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
7  N u0 p1 c0 {2,S} {6,S} {22,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.515,49.054,58.978,67.226,79.05,87.77,101.668],'cal/(mol*K)'),
        H298 = (-29.704,'kcal/mol'),
        S298 = (92.07,'cal/(mol*K)'),
    ),
    shortDesc = u"""methyl-2,2-dimethylpropylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "C6H15Nz",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
7  N u0 p1 c0 {3,S} {4,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.58,48.453,57.907,66.037,78.319,87.42,101.262],'cal/(mol*K)'),
        H298 = (-27.051,'kcal/mol'),
        S298 = (103.245,'cal/(mol*K)'),
    ),
    shortDesc = u"""ethylbutylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "C6H15Naa",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {6,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
7  N u0 p1 c0 {1,S} {3,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.53,48.475,58.006,66.194,78.498,87.548,101.411],'cal/(mol*K)'),
        H298 = (-29.633,'kcal/mol'),
        S298 = (96.543,'cal/(mol*K)'),
    ),
    shortDesc = u"""ethyl-sec-butylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "C6H15Nbb",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {6,S} {7,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
7  N u0 p1 c0 {2,S} {3,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.53,48.475,58.006,66.194,78.498,87.548,101.411],'cal/(mol*K)'),
        H298 = (-28.653,'kcal/mol'),
        S298 = (99.83,'cal/(mol*K)'),
    ),
    shortDesc = u"""ethylisobutylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "C6H15Ncc",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
7  N u0 p1 c0 {1,S} {2,S} {22,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.515,49.054,58.978,67.226,79.05,87.77,101.668],'cal/(mol*K)'),
        H298 = (-32.19,'kcal/mol'),
        S298 = (83.733,'cal/(mol*K)'),
    ),
    shortDesc = u"""ethyl-tert-butylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "C6H15Ndd",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  N u0 p1 c0 {3,S} {4,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([37.798,48.194,57.99,66.177,78.226,87.489,101.342],'cal/(mol*K)'),
        H298 = (-27.721,'kcal/mol'),
        S298 = (102.788,'cal/(mol*K)'),
    ),
    shortDesc = u"""di-propylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "C6H15Nee",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  N u0 p1 c0 {1,S} {2,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.154,48.772,58.789,67.126,79.164,88.158,102.117],'cal/(mol*K)'),
        H298 = (-33.17,'kcal/mol'),
        S298 = (107.678,'cal/(mol*K)'),
    ),
    shortDesc = u"""diisopropylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "C6H15Nff",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
7  N u0 p1 c0 {1,S} {3,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.53,48.475,58.006,66.194,78.498,87.548,101.411],'cal/(mol*K)'),
        H298 = (-30.111,'kcal/mol'),
        S298 = (94.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""propylisopropylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "C6H15Nhh",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {7,S} {20,S} {21,S} {22,S}
7  N u0 p1 c0 {2,S} {3,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.531,48.694,58.323,66.497,78.679,87.692,100.64],'cal/(mol*K)'),
        H298 = (-23.251,'kcal/mol'),
        S298 = (98.844,'cal/(mol*K)'),
    ),
    shortDesc = u"""methylethylpropylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    label = "C6H15Nii",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {5,S} {7,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {7,S} {20,S} {21,S} {22,S}
7  N u0 p1 c0 {1,S} {2,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.481,48.716,58.422,66.653,78.859,87.821,100.788],'cal/(mol*K)'),
        H298 = (-26.311,'kcal/mol'),
        S298 = (90.539,'cal/(mol*K)'),
    ),
    shortDesc = u"""methylethylisopropylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "C6H15Njj",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {7,S} {20,S} {21,S} {22,S}
7  N u0 p1 c0 {3,S} {5,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.531,48.694,58.323,66.497,78.679,87.692,100.64],'cal/(mol*K)'),
        H298 = (-21.889,'kcal/mol'),
        S298 = (103.413,'cal/(mol*K)'),
    ),
    shortDesc = u"""dimethylbutylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    label = "C6H15Nkk",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {7,S} {20,S} {21,S} {22,S}
7  N u0 p1 c0 {1,S} {5,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.481,48.716,58.422,66.653,78.859,87.821,100.788],'cal/(mol*K)'),
        H298 = (-24.47,'kcal/mol'),
        S298 = (96.712,'cal/(mol*K)'),
    ),
    shortDesc = u"""dimethyl-sec-butylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "C6H15Nll",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {7,S} {20,S} {21,S} {22,S}
7  N u0 p1 c0 {2,S} {5,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.481,48.716,58.422,66.653,78.859,87.821,100.788],'cal/(mol*K)'),
        H298 = (-23.49,'kcal/mol'),
        S298 = (99.998,'cal/(mol*K)'),
    ),
    shortDesc = u"""dimethylisobutylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    label = "C6H15Nmm",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {7,S} {20,S} {21,S} {22,S}
7  N u0 p1 c0 {1,S} {5,S} {6,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.466,49.296,59.395,67.686,79.411,88.043,101.043],'cal/(mol*K)'),
        H298 = (-25.211,'kcal/mol'),
        S298 = (89.994,'cal/(mol*K)'),
    ),
    shortDesc = u"""dimethyl-tert-butylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    label = "C6H15Nnn",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {6,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {20,S} {21,S} {22,S}
7  N u0 p1 c0 {1,S} {2,S} {3,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([39.931,48.795,57.545,65.572,78.698,88.168,101.186],'cal/(mol*K)'),
        H298 = (-22.152,'kcal/mol'),
        S298 = (96.454,'cal/(mol*K)'),
    ),
    shortDesc = u"""triethylamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
    label = "C6H15N3",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  H u0 p0 c0 {4,S}
6  H u0 p0 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  H u0 p0 c0 {7,S}
9  H u0 p0 c0 {7,S}
10 N u0 p1 c0 {7,S} {11,S} {22,S}
11 C u0 p0 c0 {10,S} {12,S} {13,S} {14,S}
12 H u0 p0 c0 {11,S}
13 H u0 p0 c0 {11,S}
14 C u0 p0 c0 {11,S} {15,S} {16,S} {17,S}
15 H u0 p0 c0 {14,S}
16 H u0 p0 c0 {14,S}
17 N u0 p1 c0 {14,S} {18,S} {19,S}
18 H u0 p0 c0 {17,S}
19 C u0 p0 c0 {17,S} {20,S} {21,S} {22,S}
20 H u0 p0 c0 {19,S}
21 H u0 p0 c0 {19,S}
22 C u0 p0 c0 {10,S} {19,S} {23,S} {24,S}
23 H u0 p0 c0 {22,S}
24 H u0 p0 c0 {22,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([42.9,54.447,65.186,74.309,88.016,97.955,111.165],'cal/(mol*K)'),
        H298 = (6.003,'kcal/mol'),
        S298 = (107.618,'cal/(mol*K)'),
    ),
    shortDesc = u"""N-aminoethyl piperazine""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
    label = "C6H16N2a",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {8,S} {19,S} {20,S}
7  N u0 p1 c0 {5,S} {21,S} {22,S}
8  N u0 p1 c0 {6,S} {23,S} {24,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([44.227,54.679,64.382,72.81,85.814,95.104,108.828],'cal/(mol*K)'),
        H298 = (-23.617,'kcal/mol'),
        S298 = (113.611,'cal/(mol*K)'),
    ),
    shortDesc = u"""hexamethylenediamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 128,
    label = "C6H16N2b",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
2  C u0 p0 c0 {5,S} {7,S} {9,S} {10,S}
3  C u0 p0 c0 {6,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {20,S} {21,S} {22,S}
7  N u0 p1 c0 {1,S} {2,S} {3,S}
8  N u0 p1 c0 {4,S} {23,S} {24,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([44.227,54.679,64.382,72.81,85.814,95.104,108.828],'cal/(mol*K)'),
        H298 = (-23.617,'kcal/mol'),
        S298 = (113.618,'cal/(mol*K)'),
    ),
    shortDesc = u"""N,N-diethyl-1,2-ethanediamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
    label = "C6H16N2c",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {8,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {7,S} {9,S} {10,S}
4  C u0 p0 c0 {6,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {20,S} {21,S} {22,S}
7  N u0 p1 c0 {1,S} {3,S} {23,S}
8  N u0 p1 c0 {2,S} {4,S} {24,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([44.227,54.679,64.382,72.81,85.814,95.104,108.828],'cal/(mol*K)'),
        H298 = (-23.617,'kcal/mol'),
        S298 = (113.618,'cal/(mol*K)'),
    ),
    shortDesc = u"""N,N'-diethyl-1,2-ethanediamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 130,
    label = "C6H16N2d",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {7,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {7,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {8,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {8,S} {22,S} {23,S} {24,S}
7  N u0 p1 c0 {1,S} {3,S} {4,S}
8  N u0 p1 c0 {2,S} {5,S} {6,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([44.227,54.679,64.382,72.81,85.814,95.104,108.828],'cal/(mol*K)'),
        H298 = (-23.617,'kcal/mol'),
        S298 = (113.612,'cal/(mol*K)'),
    ),
    shortDesc = u"""N,N,N',N'-tetramethyl-1,2-ethanediamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 131,
    label = "C6H16N2e",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {8,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  N u0 p1 c0 {3,S} {4,S} {22,S}
8  N u0 p1 c0 {5,S} {23,S} {24,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([44.227,54.679,64.382,72.81,85.814,95.104,108.828],'cal/(mol*K)'),
        H298 = (-23.617,'kcal/mol'),
        S298 = (113.617,'cal/(mol*K)'),
    ),
    shortDesc = u"""N-butylethylenediamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 132,
    label = "C6H16N2f",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {8,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
7  N u0 p1 c0 {4,S} {21,S} {22,S}
8  N u0 p1 c0 {5,S} {23,S} {24,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([44.227,54.679,64.382,72.81,85.814,95.104,108.828],'cal/(mol*K)'),
        H298 = (-23.617,'kcal/mol'),
        S298 = (113.613,'cal/(mol*K)'),
    ),
    shortDesc = u"""1,5-diamino-2-methylpentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 133,
    label = "C6H16N2g",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
2  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
7  N u0 p1 c0 {1,S} {3,S} {22,S}
8  N u0 p1 c0 {4,S} {23,S} {24,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([44.227,54.679,64.382,72.81,85.814,95.104,108.828],'cal/(mol*K)'),
        H298 = (-23.617,'kcal/mol'),
        S298 = (113.616,'cal/(mol*K)'),
    ),
    shortDesc = u"""N-isopropyl-1,3-propanediamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 134,
    label = "C6H16N2h",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {8,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  N u0 p1 c0 {3,S} {4,S} {22,S}
8  N u0 p1 c0 {5,S} {23,S} {24,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([44.227,54.679,64.382,72.81,85.814,95.104,108.828],'cal/(mol*K)'),
        H298 = (-23.617,'kcal/mol'),
        S298 = (113.615,'cal/(mol*K)'),
    ),
    shortDesc = u"""N-propyl-1,3-propanediamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "C6H16N2i",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
4  C u0 p0 c0 {7,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {7,S} {21,S} {22,S} {23,S}
6  C u0 p0 c0 {8,S} {15,S} {16,S} {17,S}
7  N u0 p1 c0 {2,S} {4,S} {5,S}
8  N u0 p1 c0 {3,S} {6,S} {24,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([44.227,54.679,64.382,72.81,85.814,95.104,108.828],'cal/(mol*K)'),
        H298 = (-23.617,'kcal/mol'),
        S298 = (113.618,'cal/(mol*K)'),
    ),
    shortDesc = u"""N,N,N'-trimethyl-1,3-propanediamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "C6H16N2j",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {18,S} {19,S} {20,S}
7  N u0 p1 c0 {1,S} {21,S} {22,S}
8  N u0 p1 c0 {2,S} {23,S} {24,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([44.227,54.679,64.382,72.81,85.814,95.104,108.828],'cal/(mol*K)'),
        H298 = (-23.617,'kcal/mol'),
        S298 = (113.617,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-methyl-2,4-pentanediamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "C6H18N4",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  H u0 p0 c0 {4,S}
6  H u0 p0 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  H u0 p0 c0 {7,S}
9  H u0 p0 c0 {7,S}
10 N u0 p1 c0 {7,S} {11,S} {12,S}
11 H u0 p0 c0 {10,S}
12 C u0 p0 c0 {10,S} {13,S} {14,S} {15,S}
13 H u0 p0 c0 {12,S}
14 H u0 p0 c0 {12,S}
15 C u0 p0 c0 {12,S} {16,S} {17,S} {18,S}
16 H u0 p0 c0 {15,S}
17 H u0 p0 c0 {15,S}
18 N u0 p1 c0 {15,S} {19,S} {20,S}
19 H u0 p0 c0 {18,S}
20 C u0 p0 c0 {18,S} {21,S} {22,S} {23,S}
21 H u0 p0 c0 {20,S}
22 H u0 p0 c0 {20,S}
23 C u0 p0 c0 {20,S} {24,S} {25,S} {26,S}
24 H u0 p0 c0 {23,S}
25 H u0 p0 c0 {23,S}
26 N u0 p1 c0 {23,S} {27,S} {28,S}
27 H u0 p0 c0 {26,S}
28 H u0 p0 c0 {26,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([51.283,64.415,76.341,86.296,101.166,112.306,127.451],'cal/(mol*K)'),
        H298 = (0.806,'kcal/mol'),
        S298 = (135.076,'cal/(mol*K)'),
    ),
    shortDesc = u"""triethylene tetramine""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "CH3CHNH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {7,S}
3 N u0 p1 c0 {2,S} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.4185,20.6221,23.6417,26.2968,30.6212,33.9675,39.4489],'cal/(mol*K)'),
        H298 = (28.75,'kcal/mol'),
        S298 = (70.02,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-Aminoeth-1-yl radical, C[CH]N""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "CH2=CHNH2",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 N u0 p1 c0 {1,S} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.05,18.62,21.69,24.24,28.21,31.21,36.12],'cal/(mol*K)'),
        H298 = (14.17,'kcal/mol'),
        S298 = (62.17,'cal/(mol*K)'),
    ),
    shortDesc = u"""C=CN""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    label = "CH3CH=NH2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 N u0 p1 c0 {2,D} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.98,17.32,20.49,23.26,27.71,31.05,36.29],'cal/(mol*K)'),
        H298 = (10.65,'kcal/mol'),
        S298 = (62.65,'cal/(mol*K)'),
    ),
    shortDesc = u"""C=CN""",
    longDesc = 
u"""

""",
)

