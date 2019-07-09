#!/usr/bin/env python
# encoding: utf-8

name = "CHON"
shortDesc = u"Yaws' Critical Property Data for C and N compounds"
longDesc = u"""
Yaws' Critical Property Data for Chemical Engineers and Chemists
Table 30. Heat Capacity of Gas - Organic Compounds
Table 38. Enthalpy of Formation of Gas - Organic Compounds
Table 46. Entropy of Gas - Organic Compounds

Contains only molecules with only carbon, hydrogen, oxygen, and nitrogen compounds
"""
entry(
    index = 0,
    label = "CH3NO",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 N u0 p1 c0 {1,S} {5,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.725,13.097,15.339,17.343,20.559,22.921,26.561],'cal/(mol*K)'),
        H298 = (-44.499,'kcal/mol'),
        S298 = (59.437,'cal/(mol*K)'),
    ),
    shortDesc = u"""formamide""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "CH3NO2a",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 N u0 p0 c+1 {1,S} {6,D} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 O u0 p3 c-1 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.732,16.74,19.508,21.875,25.457,28.016,31.788],'cal/(mol*K)'),
        H298 = (-17.852,'kcal/mol'),
        S298 = (65.794,'cal/(mol*K)'),
    ),
    shortDesc = u"""nitromethane""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "CH3NO2b",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u0 p1 c0 {2,S} {7,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.169,18.258,21.011,23.354,26.969,29.52,32.21],'cal/(mol*K)'),
        H298 = (-15.271,'kcal/mol'),
        S298 = (68.119,'cal/(mol*K)'),
    ),
    shortDesc = u"""methyl nitrite""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "CH3NO3",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {1,S} {6,S}
6 N u0 p0 c+1 {5,S} {7,D} {8,S}
7 O u0 p2 c0 {6,D}
8 O u0 p3 c-1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.347,21.87,24.95,27.539,31.47,34.19,37.305],'cal/(mol*K)'),
        H298 = (-28.775,'kcal/mol'),
        S298 = (72.272,'cal/(mol*K)'),
    ),
    shortDesc = u"""methyl nitrate""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "C2H3NO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 N u0 p1 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,D}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.433,17.131,19.541,21.66,25.141,27.701,30.225],'cal/(mol*K)'),
        H298 = (-13.809,'kcal/mol'),
        S298 = (64.871,'cal/(mol*K)'),
    ),
    shortDesc = u"""methyl isocyanate""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "C2H5NOa",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,D}
3 N u0 p1 c0 {2,S} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {2,D}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.191,19.972,23.511,26.602,31.451,35.069,40.681],'cal/(mol*K)'),
        H298 = (-56.953,'kcal/mol'),
        S298 = (68.03,'cal/(mol*K)'),
    ),
    shortDesc = u"""acetamide""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "C2H5NOb",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 N u0 p1 c0 {1,S} {3,S} {7,S}
3 C u0 p0 c0 {2,S} {8,S} {9,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 O u0 p2 c0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.279,20.084,23.671,26.829,31.809,35.49,41.08],'cal/(mol*K)'),
        H298 = (-44.078,'kcal/mol'),
        S298 = (67.148,'cal/(mol*K)'),
    ),
    shortDesc = u"""N-methylformamide""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "C2H5NO2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  H u0 p0 c0 {1,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6  H u0 p0 c0 {5,S}
7  H u0 p0 c0 {5,S}
8  N u0 p0 c+1 {5,S} {9,D} {10,S}
9  O u0 p2 c0 {8,D}
10 O u0 p3 c-1 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.012,23.615,27.746,31.243,36.537,40.363,46.056],'cal/(mol*K)'),
        H298 = (-24.377,'kcal/mol'),
        S298 = (75.711,'cal/(mol*K)'),
    ),
    shortDesc = u"""nitroethane""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "C2H5NO3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  H u0 p0 c0 {1,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6  H u0 p0 c0 {5,S}
7  H u0 p0 c0 {5,S}
8  O u0 p2 c0 {5,S} {9,S}
9  N u0 p0 c+1 {8,S} {10,D} {11,S}
10 O u0 p2 c0 {9,D}
11 O u0 p3 c-1 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.36,28.653,33.292,37.125,42.739,46.689,52.667],'cal/(mol*K)'),
        H298 = (-36.798,'kcal/mol'),
        S298 = (83.383,'cal/(mol*K)'),
    ),
    shortDesc = u"""ethyl nitrate""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "C2H7NOa",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  N u0 p1 c0 {1,S} {9,S} {10,S}
4  O u0 p2 c0 {2,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.464,24.989,29.228,32.747,37.917,41.996,48.225],'cal/(mol*K)'),
        H298 = (-50.235,'kcal/mol'),
        S298 = (76.647,'cal/(mol*K)'),
    ),
    shortDesc = u"""monoethanolamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "C2H7NOb",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  N u0 p1 c0 {1,S} {9,S} {10,S}
4  O u0 p2 c0 {1,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.464,24.989,29.228,32.747,37.917,41.996,48.225],'cal/(mol*K)'),
        H298 = (-50.235,'kcal/mol'),
        S298 = (76.643,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-aminoethanol""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "C3H5NOa",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,D}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {2,D} {7,S} {8,S}
4  N u0 p1 c0 {1,S} {9,S} {10,S}
5  O u0 p2 c0 {1,D}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.915,24.443,28.635,32.276,37.932,41.917,46.828],'cal/(mol*K)'),
        H298 = (-40.629,'kcal/mol'),
        S298 = (71.805,'cal/(mol*K)'),
    ),
    shortDesc = u"""acrylamide""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "C3H5NOb",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,T}
4  O u0 p2 c0 {2,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  N u0 p1 c0 {3,T}
10 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.302,24.676,28.586,31.869,36.768,40.193,44.902],'cal/(mol*K)'),
        H298 = (-23.493,'kcal/mol'),
        S298 = (79.18,'cal/(mol*K)'),
    ),
    shortDesc = u"""hydracrylonitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "C3H5NOc",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,T}
4  O u0 p2 c0 {1,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  N u0 p1 c0 {3,T}
10 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.006,26.061,29.693,32.928,38.403,42.625,47.619],'cal/(mol*K)'),
        H298 = (-15.271,'kcal/mol'),
        S298 = (97.617,'cal/(mol*K)'),
    ),
    shortDesc = u"""lactonitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "C3H7NOa",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  N u0 p1 c0 {1,S} {2,S} {4,S}
4  C u0 p0 c0 {3,S} {11,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.032,28.049,33.079,37.542,44.287,48.737,55.086],'cal/(mol*K)'),
        H298 = (-45.815,'kcal/mol'),
        S298 = (78.034,'cal/(mol*K)'),
    ),
    shortDesc = u"""N,N-dimethylformamide""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "C3H7NOb",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  N u0 p1 c0 {1,S} {4,S} {12,S}
4  C u0 p0 c0 {2,S} {3,S} {11,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.262,23.422,28.393,32.802,39.881,45.227,51.992],'cal/(mol*K)'),
        H298 = (-57.359,'kcal/mol'),
        S298 = (76.666,'cal/(mol*K)'),
    ),
    shortDesc = u"""N-methylacetamide""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "C3H7NO2a",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  N u0 p0 c+1 {2,S} {12,D} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 O u0 p3 c-1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.557,30.784,36.295,40.909,47.83,52.844,60.277],'cal/(mol*K)'),
        H298 = (-29.993,'kcal/mol'),
        S298 = (83.783,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-nitropropane""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "C3H7NO2b",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  N u0 p0 c+1 {1,S} {12,D} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 O u0 p3 c-1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.758,31.08,36.654,41.306,48.241,53.203,60.492],'cal/(mol*K)'),
        H298 = (-33.219,'kcal/mol'),
        S298 = (82.26,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-nitropropane""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "C3H7NO3a",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  N u0 p0 c+1 {5,S} {13,D} {14,S}
5  O u0 p2 c0 {2,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 O u0 p3 c-1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.095,35.724,41.605,46.538,53.898,59.07,66.633],'cal/(mol*K)'),
        H298 = (-41.597,'kcal/mol'),
        S298 = (92.241,'cal/(mol*K)'),
    ),
    shortDesc = u"""propyl nitrate""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "C3H7NO3b",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  N u0 p0 c+1 {5,S} {13,D} {14,S}
5  O u0 p2 c0 {1,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 O u0 p3 c-1 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.954,35.829,41.896,46.894,54.154,59.263,66.85],'cal/(mol*K)'),
        H298 = (-45.648,'kcal/mol'),
        S298 = (89.355,'cal/(mol*K)'),
    ),
    shortDesc = u"""isopropyl nitrate""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "C3H9NOb",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  N u0 p1 c0 {2,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.664,31.433,36.984,41.718,48.769,54.049,62.066],'cal/(mol*K)'),
        H298 = (-52.818,'kcal/mol'),
        S298 = (87.854,'cal/(mol*K)'),
    ),
    shortDesc = u"""3-amino-1-propanol""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "C3H9NOd",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  N u0 p1 c0 {1,S} {12,S} {13,S}
5  O u0 p2 c0 {2,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.797,30.989,36.931,41.915,49.197,54.741,62.861],'cal/(mol*K)'),
        H298 = (-52.419,'kcal/mol'),
        S298 = (85.742,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-amino-1-propanol, ()""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "C4H5NO2",
    molecule = 
"""
1  C u0 p0 c0 {2,T} {3,S}
2  N u0 p1 c0 {1,T}
3  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {7,S}
7  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.006,31.235,36.497,40.482,45.867,50.238,56.124],'cal/(mol*K)'),
        H298 = (-56.643,'kcal/mol'),
        S298 = (91.358,'cal/(mol*K)'),
    ),
    shortDesc = u"""methyl cyanoacetate""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "C4H7NOa",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,T}
5  O u0 p2 c0 {1,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 N u0 p1 c0 {4,T}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([27.373,33.012,37.993,42.175,48.522,53.112,59.335],'cal/(mol*K)'),
        H298 = (-31.786,'kcal/mol'),
        S298 = (80.414,'cal/(mol*K)'),
    ),
    shortDesc = u"""acetone cyanohydrin""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "C4H7NOb",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u0 p0 c0 {2,S} {5,S} {9,D}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  N u0 p1 c0 {3,S} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.34,32.697,38.37,43.104,50.558,56.672,63.312],'cal/(mol*K)'),
        H298 = (-44.214,'kcal/mol'),
        S298 = (86.37,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-methacrylamide""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "C4H7NOc",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {1,S} {3,S}
5  C u0 p0 c0 {2,S} {13,T}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 N u0 p1 c0 {5,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.673,31.504,36.815,41.338,48.204,53.061,59.277],'cal/(mol*K)'),
        H298 = (-18.88,'kcal/mol'),
        S298 = (87.092,'cal/(mol*K)'),
    ),
    shortDesc = u"""3-methoxypropionitrile""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "C4H7NOd",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  N u0 p1 c0 {2,S} {5,S} {13,S}
5  C u0 p0 c0 {3,S} {4,S} {12,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.217,28.291,34.962,40.489,48.401,54.097,60.399],'cal/(mol*K)'),
        H298 = (-47.117,'kcal/mol'),
        S298 = (72.088,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-pyrrolidone""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "C4H9NOa",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
4  N u0 p1 c0 {1,S} {2,S} {5,S}
5  C u0 p0 c0 {3,S} {4,S} {15,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 O u0 p2 c0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.493,33.898,40.759,46.57,55.465,62.332,71.655],'cal/(mol*K)'),
        H298 = (-53.774,'kcal/mol'),
        S298 = (84.015,'cal/(mol*K)'),
    ),
    shortDesc = u"""N,N-dimethylacetamide""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "C4H9NOb",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  N u0 p1 c0 {1,S} {2,S} {15,S}
6  O u0 p2 c0 {3,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.04,35.85,42.905,48.611,56.669,62.553,69.881],'cal/(mol*K)'),
        H298 = (-37.282,'kcal/mol'),
        S298 = (55.556,'cal/(mol*K)'),
    ),
    shortDesc = u"""morpholine""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "C4H9NO2a",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  N u0 p0 c+1 {3,S} {15,D} {16,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u0 p2 c0 {5,D}
16 O u0 p3 c-1 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.748,37.59,44.548,50.38,59.113,65.392,74.546],'cal/(mol*K)'),
        H298 = (-34.39,'kcal/mol'),
        S298 = (90.574,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-nitrobutane""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "C4H9NO2b",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  N u0 p0 c+1 {1,S} {15,D} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {5,D}
16 O u0 p3 c-1 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.645,37.807,44.933,50.796,59.386,65.535,74.57],'cal/(mol*K)'),
        H298 = (-39.098,'kcal/mol'),
        S298 = (87.928,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-nitrobutane""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "C4H9NO2c",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  N u0 p0 c+1 {2,S} {15,D} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u0 p2 c0 {5,D}
16 O u0 p3 c-1 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.222,37.589,44.389,50.189,58.94,65.12,73.924],'cal/(mol*K)'),
        H298 = (-33.919,'kcal/mol'),
        S298 = (91.423,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-nitro-2-methylpropane""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "C4H9NO2d",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  N u0 p0 c+1 {1,S} {15,D} {16,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u0 p2 c0 {5,D}
16 O u0 p3 c-1 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.455,38.428,45.423,51.276,60.024,66.181,75],'cal/(mol*K)'),
        H298 = (-41.847,'kcal/mol'),
        S298 = (86.565,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-nitro-2-methylpropane""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "C4H11NOa",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  N u0 p1 c0 {2,S} {15,S} {16,S}
6  O u0 p2 c0 {1,S} {17,S}
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
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.213,38.076,45.611,51.866,60.761,67.377,77.371],'cal/(mol*K)'),
        H298 = (-48.276,'kcal/mol'),
        S298 = (91.919,'cal/(mol*K)'),
    ),
    shortDesc = u"""dimethylethanolamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "C4H11NOb",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  N u0 p1 c0 {1,S} {15,S} {16,S}
6  O u0 p2 c0 {3,S} {17,S}
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
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.213,38.076,45.611,51.866,60.761,67.377,77.371],'cal/(mol*K)'),
        H298 = (-48.276,'kcal/mol'),
        S298 = (91.921,'cal/(mol*K)'),
    ),
    shortDesc = u"""3-amino-1-butanol""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "C4H11NOc",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  N u0 p1 c0 {1,S} {15,S} {16,S}
6  O u0 p2 c0 {2,S} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.213,38.076,45.611,51.866,60.761,67.377,77.371],'cal/(mol*K)'),
        H298 = (-48.276,'kcal/mol'),
        S298 = (91.921,'cal/(mol*K)'),
    ),
    shortDesc = u"""3-amino-2-butanol""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "C4H11NOd",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  N u0 p1 c0 {3,S} {15,S} {16,S}
6  O u0 p2 c0 {4,S} {17,S}
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
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.213,38.076,45.611,51.866,60.761,67.377,77.371],'cal/(mol*K)'),
        H298 = (-48.276,'kcal/mol'),
        S298 = (91.918,'cal/(mol*K)'),
    ),
    shortDesc = u"""4-amino-1-butanol""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "C4H11NOe",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  N u0 p1 c0 {1,S} {15,S} {16,S}
6  O u0 p2 c0 {3,S} {17,S}
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
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.213,38.076,45.611,51.866,60.761,67.377,77.371],'cal/(mol*K)'),
        H298 = (-48.276,'kcal/mol'),
        S298 = (91.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-amino-1-butanol, ()-""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "C4H11NOf",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  N u0 p1 c0 {1,S} {15,S} {16,S}
6  O u0 p2 c0 {2,S} {17,S}
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
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.213,38.076,45.611,51.866,60.761,67.377,77.371],'cal/(mol*K)'),
        H298 = (-48.276,'kcal/mol'),
        S298 = (91.921,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-amino-2-methyl-1-propanol""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "C4H11NOg",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  N u0 p1 c0 {1,S} {2,S} {16,S}
6  O u0 p2 c0 {3,S} {17,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.213,38.076,45.611,51.866,60.761,67.377,77.371],'cal/(mol*K)'),
        H298 = (-48.276,'kcal/mol'),
        S298 = (91.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-(ethylamino)ethanol""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "C4H11NOh",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  N u0 p1 c0 {3,S} {15,S} {16,S}
6  O u0 p2 c0 {1,S} {17,S}
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
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.213,38.076,45.611,51.866,60.761,67.377,77.371],'cal/(mol*K)'),
        H298 = (-48.276,'kcal/mol'),
        S298 = (91.921,'cal/(mol*K)'),
    ),
    shortDesc = u"""4-amino-2-butanol""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "C4H11NOi",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  N u0 p1 c0 {3,S} {15,S} {16,S}
6  O u0 p2 c0 {1,S} {17,S}
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
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.213,38.076,45.611,51.866,60.761,67.377,77.371],'cal/(mol*K)'),
        H298 = (-48.276,'kcal/mol'),
        S298 = (91.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-amino-2-butanol""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "C4H11NO2a",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  N u0 p1 c0 {1,S} {2,S} {16,S}
6  O u0 p2 c0 {3,S} {17,S}
7  O u0 p2 c0 {4,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.79,41.643,49.072,55.249,64.214,71.099,81.775],'cal/(mol*K)'),
        H298 = (-94.853,'kcal/mol'),
        S298 = (102.645,'cal/(mol*K)'),
    ),
    shortDesc = u"""diethanolamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "C4H11NO2b",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {6,S} {7,S} {10,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  N u0 p1 c0 {2,S} {16,S} {17,S}
6  O u0 p2 c0 {1,S} {3,S}
7  O u0 p2 c0 {1,S} {18,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.757,41.744,48.961,55.023,64.211,71.016,79.336],'cal/(mol*K)'),
        H298 = (-87.234,'kcal/mol'),
        S298 = (106.493,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-aminoethoxyethanol""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "C4H11NO2c",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  N u0 p1 c0 {1,S} {15,S} {16,S}
6  O u0 p2 c0 {2,S} {17,S}
7  O u0 p2 c0 {3,S} {18,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.79,41.643,49.072,55.249,64.214,71.099,81.775],'cal/(mol*K)'),
        H298 = (-94.853,'kcal/mol'),
        S298 = (102.642,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-amino-2-methyl-1,3-propanediol""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "C4H11NO2d",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  N u0 p1 c0 {2,S} {4,S} {16,S}
6  O u0 p2 c0 {1,S} {18,S}
7  O u0 p2 c0 {3,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.79,41.643,49.072,55.249,64.214,71.099,81.775],'cal/(mol*K)'),
        H298 = (-94.853,'kcal/mol'),
        S298 = (102.643,'cal/(mol*K)'),
    ),
    shortDesc = u"""3-methylamino-1,2-propanediol""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "C4H12N2O",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  N u0 p1 c0 {3,S} {5,S} {14,S}
5  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {5,S} {7,S} {17,S} {18,S}
7  O u0 p2 c0 {6,S} {19,S}
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
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.816,43.502,51.364,57.91,67.711,75.026,83.816],'cal/(mol*K)'),
        H298 = (-45.647,'kcal/mol'),
        S298 = (107.016,'cal/(mol*K)'),
    ),
    shortDesc = u"""N-aminoethyl ethanolamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "C5H7NO2",
    molecule = 
"""
1  C u0 p0 c0 {2,T} {3,S}
2  N u0 p1 c0 {1,T}
3  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {7,S}
7  C u0 p0 c0 {6,S} {8,S} {11,S} {12,S}
8  C u0 p0 c0 {7,S} {13,S} {14,S} {15,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.194,37.848,44.596,49.943,57.211,62.321,69.623],'cal/(mol*K)'),
        H298 = (-75.557,'kcal/mol'),
        S298 = (98.813,'cal/(mol*K)'),
    ),
    shortDesc = u"""ethyl cyanoacetate""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "C5H9NOa",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  N u0 p1 c0 {3,S} {6,D}
6  C u0 p0 c0 {5,D} {16,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u0 p2 c0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.705,35.606,42.105,47.97,57.401,64.093,76.444],'cal/(mol*K)'),
        H298 = (-30.351,'kcal/mol'),
        S298 = (91.43,'cal/(mol*K)'),
    ),
    shortDesc = u"""butyl isocyanate""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "C5H9NOb",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  N u0 p1 c0 {2,S} {4,S} {6,S}
6  C u0 p0 c0 {3,S} {5,S} {16,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u0 p2 c0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.721,33.864,42.505,49.635,59.924,67.609,75.53],'cal/(mol*K)'),
        H298 = (-46.696,'kcal/mol'),
        S298 = (81.003,'cal/(mol*K)'),
    ),
    shortDesc = u"""N-methyl-2-pyrrolidone""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "C5H9NOc",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  N u0 p1 c0 {2,S} {6,D}
6  C u0 p0 c0 {5,D} {16,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u0 p2 c0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([26.405,33.066,38.472,42.497,48.434,54.344,62.039],'cal/(mol*K)'),
        H298 = (-30.351,'kcal/mol'),
        S298 = (91.432,'cal/(mol*K)'),
    ),
    shortDesc = u"""isobutyl isocyanate""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "C5H9NOd",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  N u0 p1 c0 {1,S} {6,D}
6  C u0 p0 c0 {5,D} {16,D}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u0 p2 c0 {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([44.194,55.344,64.391,71.128,81.064,90.955,103.835],'cal/(mol*K)'),
        H298 = (-30.353,'kcal/mol'),
        S298 = (91.422,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-isocyanato-2-methylpropane""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "C5H9NO4",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,S} {16,S} {17,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {18,S}
8  C u0 p0 c0 {2,S} {9,D} {10,S}
9  O u0 p2 c0 {8,D}
10 O u0 p2 c0 {8,S} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([41.794,50.443,58.008,64.231,73.277,79.559,88.88],'cal/(mol*K)'),
        H298 = (-196.938,'kcal/mol'),
        S298 = (117.644,'cal/(mol*K)'),
    ),
    shortDesc = u"""L-glutamic acid""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "C5H11NO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  N u0 p1 c0 {1,S} {6,S} {17,S}
6  C u0 p0 c0 {5,S} {7,D} {18,S}
7  O u0 p2 c0 {6,D}
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
18 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.394,38.782,46.901,53.623,62.993,69.508,78.562],'cal/(mol*K)'),
        H298 = (-67.874,'kcal/mol'),
        S298 = (89.763,'cal/(mol*K)'),
    ),
    shortDesc = u"""tert-butylformamide""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "C5H11NO2a",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  N u0 p0 c+1 {4,S} {18,D} {19,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 O u0 p2 c0 {6,D}
19 O u0 p3 c-1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.77,44.487,52.53,59.4,69.843,77.322,87.776],'cal/(mol*K)'),
        H298 = (-37.59,'kcal/mol'),
        S298 = (103.006,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-nitropentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "C5H11NO2b",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
6  N u0 p0 c+1 {1,S} {18,D} {19,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u0 p2 c0 {6,D}
19 O u0 p3 c-1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.72,44.509,52.63,59.556,70.022,77.45,87.922],'cal/(mol*K)'),
        H298 = (-38.852,'kcal/mol'),
        S298 = (100.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-nitropentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "C5H11NO2c",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  N u0 p0 c+1 {1,S} {18,D} {19,S}
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
18 O u0 p2 c0 {6,D}
19 O u0 p3 c-1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.72,44.509,52.63,59.556,70.022,77.45,87.922],'cal/(mol*K)'),
        H298 = (-38.852,'kcal/mol'),
        S298 = (100.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""3-nitropentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "C5H11NO2d",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6  N u0 p0 c+1 {3,S} {18,D} {19,S}
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
18 O u0 p2 c0 {6,D}
19 O u0 p3 c-1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.72,44.509,52.63,59.556,70.022,77.45,87.922],'cal/(mol*K)'),
        H298 = (-38.852,'kcal/mol'),
        S298 = (100.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-nitro-2-methylbutane""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "C5H11NO2e",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  N u0 p0 c+1 {3,S} {18,D} {19,S}
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
18 O u0 p2 c0 {6,D}
19 O u0 p3 c-1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.72,44.509,52.63,59.556,70.022,77.45,87.922],'cal/(mol*K)'),
        H298 = (-38.852,'kcal/mol'),
        S298 = (100.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-nitro-3-methylbutane""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "C5H11NO2f",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
6  N u0 p0 c+1 {1,S} {18,D} {19,S}
7  H u0 p0 c0 {2,S}
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
18 O u0 p2 c0 {6,D}
19 O u0 p3 c-1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.705,45.088,53.602,60.588,70.574,77.672,88.174],'cal/(mol*K)'),
        H298 = (-41.847,'kcal/mol'),
        S298 = (119.167,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-nitro-2-methylbutane""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "C5H11NO2g",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6  N u0 p0 c+1 {2,S} {18,D} {19,S}
7  H u0 p0 c0 {1,S}
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
18 O u0 p2 c0 {6,D}
19 O u0 p3 c-1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.67,44.53,52.729,59.712,70.201,77.579,88.068],'cal/(mol*K)'),
        H298 = (-40.114,'kcal/mol'),
        S298 = (98.453,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-nitro-3-methylbutane""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "C5H11NO2h",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  N u0 p0 c+1 {2,S} {18,D} {19,S}
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
18 O u0 p2 c0 {6,D}
19 O u0 p3 c-1 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.705,45.088,53.602,60.588,70.574,77.672,88.174],'cal/(mol*K)'),
        H298 = (-39.681,'kcal/mol'),
        S298 = (93.715,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-nitro-2,2-dimethylpropane""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "C5H13NO2a",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
6  N u0 p1 c0 {1,S} {2,S} {5,S}
7  O u0 p2 c0 {3,S} {20,S}
8  O u0 p2 c0 {4,S} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.451,46.303,53.733,59.909,68.874,75.76,86.435],'cal/(mol*K)'),
        H298 = (-90.819,'kcal/mol'),
        S298 = (112.641,'cal/(mol*K)'),
    ),
    shortDesc = u"""methyl diethanolamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "C5H13NO2b",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {8,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6  N u0 p1 c0 {1,S} {18,S} {19,S}
7  O u0 p2 c0 {3,S} {20,S}
8  O u0 p2 c0 {4,S} {21,S}
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
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.451,46.303,53.733,59.909,68.874,75.76,86.435],'cal/(mol*K)'),
        H298 = (-90.816,'kcal/mol'),
        S298 = (112.649,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-amino-2-ethyl-1,3-propanediol""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "C6H4N2O4a",
    molecule = 
"""
1  C u0 p0 c0 {3,B} {5,B} {7,S}
2  C u0 p0 c0 {3,B} {4,B} {8,S}
3  C u0 p0 c0 {1,B} {2,B} {9,S}
4  C u0 p0 c0 {2,B} {6,B} {10,S}
5  C u0 p0 c0 {1,B} {6,B} {12,S}
6  C u0 p0 c0 {4,B} {5,B} {11,S}
7  N u0 p0 c+1 {1,S} {13,D} {14,S}
8  N u0 p0 c+1 {2,S} {15,D} {16,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {5,S}
13 O u0 p2 c0 {7,D}
14 O u0 p3 c-1 {7,S}
15 O u0 p2 c0 {8,D}
16 O u0 p3 c-1 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.508,45.963,54.199,60.693,69.149,74.78,87.717],'cal/(mol*K)'),
        H298 = (12.86,'kcal/mol'),
        S298 = (89.966,'cal/(mol*K)'),
    ),
    shortDesc = u"""m-dinitrobenzene""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "C6H4N2O4b",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {4,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {8,S}
3  C u0 p0 c0 {2,B} {5,B} {9,S}
4  C u0 p0 c0 {1,B} {6,B} {12,S}
5  C u0 p0 c0 {3,B} {6,B} {10,S}
6  C u0 p0 c0 {4,B} {5,B} {11,S}
7  N u0 p0 c+1 {1,S} {13,D} {14,S}
8  N u0 p0 c+1 {2,S} {15,D} {16,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {4,S}
13 O u0 p2 c0 {7,D}
14 O u0 p3 c-1 {7,S}
15 O u0 p2 c0 {8,D}
16 O u0 p3 c-1 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.04,45.547,53.86,60.419,68.96,74.651,87.566],'cal/(mol*K)'),
        H298 = (6.646,'kcal/mol'),
        S298 = (77.141,'cal/(mol*K)'),
    ),
    shortDesc = u"""o-dinitrobenzene""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "C6H4N2O4c",
    molecule = 
"""
1  C u0 p0 c0 {3,B} {6,B} {7,S}
2  C u0 p0 c0 {4,B} {5,B} {8,S}
3  C u0 p0 c0 {1,B} {4,B} {9,S}
4  C u0 p0 c0 {2,B} {3,B} {10,S}
5  C u0 p0 c0 {2,B} {6,B} {11,S}
6  C u0 p0 c0 {1,B} {5,B} {12,S}
7  N u0 p0 c+1 {1,S} {13,D} {14,S}
8  N u0 p0 c+1 {2,S} {15,D} {16,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 O u0 p2 c0 {7,D}
14 O u0 p3 c-1 {7,S}
15 O u0 p2 c0 {8,D}
16 O u0 p3 c-1 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.422,46.012,54.35,60.878,69.271,74.859,87.81],'cal/(mol*K)'),
        H298 = (12.143,'kcal/mol'),
        S298 = (89.967,'cal/(mol*K)'),
    ),
    shortDesc = u"""p-dinitrobenzene""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "C6H5NO2",
    molecule = 
"""
1  N u0 p0 c+1 {2,D} {3,S} {4,S}
2  O u0 p2 c0 {1,D}
3  O u0 p3 c-1 {1,S}
4  C u0 p0 c0 {1,S} {5,B} {13,B}
5  C u0 p0 c0 {4,B} {6,S} {7,B}
6  H u0 p0 c0 {5,S}
7  C u0 p0 c0 {5,B} {8,S} {9,B}
8  H u0 p0 c0 {7,S}
9  C u0 p0 c0 {7,B} {10,S} {11,B}
10 H u0 p0 c0 {9,S}
11 C u0 p0 c0 {9,B} {12,S} {13,B}
12 H u0 p0 c0 {11,S}
13 C u0 p0 c0 {4,B} {11,B} {14,S}
14 H u0 p0 c0 {13,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.583,36.015,42.765,48.244,55.602,60.182,67.234],'cal/(mol*K)'),
        H298 = (16.158,'kcal/mol'),
        S298 = (85.763,'cal/(mol*K)'),
    ),
    shortDesc = u"""nitrobenzene""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "C6H6N2O2a",
    molecule = 
"""
1  C u0 p0 c0 {3,B} {5,B} {7,S}
2  C u0 p0 c0 {3,B} {4,B} {8,S}
3  C u0 p0 c0 {1,B} {2,B} {9,S}
4  C u0 p0 c0 {2,B} {6,B} {10,S}
5  C u0 p0 c0 {1,B} {6,B} {12,S}
6  C u0 p0 c0 {4,B} {5,B} {11,S}
7  N u0 p0 c+1 {1,S} {13,D} {14,S}
8  N u0 p1 c0 {2,S} {15,S} {16,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {5,S}
13 O u0 p2 c0 {7,D}
14 O u0 p3 c-1 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.334,42.781,49.204,54.504,62.297,67.672,75.583],'cal/(mol*K)'),
        H298 = (13.984,'kcal/mol'),
        S298 = (91.327,'cal/(mol*K)'),
    ),
    shortDesc = u"""m-nitroaniline""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "C6H6N2O2b",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {4,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {8,S}
3  C u0 p0 c0 {2,B} {5,B} {9,S}
4  C u0 p0 c0 {1,B} {6,B} {12,S}
5  C u0 p0 c0 {3,B} {6,B} {10,S}
6  C u0 p0 c0 {4,B} {5,B} {11,S}
7  N u0 p0 c+1 {1,S} {13,D} {14,S}
8  N u0 p1 c0 {2,S} {15,S} {16,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {4,S}
13 O u0 p2 c0 {7,D}
14 O u0 p3 c-1 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.334,42.781,49.204,54.504,62.297,67.672,75.583],'cal/(mol*K)'),
        H298 = (15.25,'kcal/mol'),
        S298 = (91.567,'cal/(mol*K)'),
    ),
    shortDesc = u"""o-nitroaniline""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "C6H6N2O2c",
    molecule = 
"""
1  C u0 p0 c0 {3,B} {6,B} {7,S}
2  C u0 p0 c0 {4,B} {5,B} {8,S}
3  C u0 p0 c0 {1,B} {4,B} {9,S}
4  C u0 p0 c0 {2,B} {3,B} {10,S}
5  C u0 p0 c0 {2,B} {6,B} {11,S}
6  C u0 p0 c0 {1,B} {5,B} {12,S}
7  N u0 p0 c+1 {1,S} {13,D} {14,S}
8  N u0 p1 c0 {2,S} {15,S} {16,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 O u0 p2 c0 {7,D}
14 O u0 p3 c-1 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([35.334,42.781,49.204,54.504,62.297,67.672,75.583],'cal/(mol*K)'),
        H298 = (14.223,'kcal/mol'),
        S298 = (90.525,'cal/(mol*K)'),
    ),
    shortDesc = u"""p-nitroaniline""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "C6H8N2O",
    molecule = 
"""
1  C u0 p0 c0 {2,T} {3,S}
2  N u0 p1 c0 {1,T}
3  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {12,S} {13,S}
5  O u0 p2 c0 {4,S} {6,S}
6  C u0 p0 c0 {5,S} {7,S} {14,S} {15,S}
7  C u0 p0 c0 {6,S} {8,S} {16,S} {17,S}
8  C u0 p0 c0 {7,S} {9,T}
9  N u0 p1 c0 {8,T}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([36.661,44.199,50.979,56.772,65.568,71.597,79.985],'cal/(mol*K)'),
        H298 = (4.878,'kcal/mol'),
        S298 = (100.368,'cal/(mol*K)'),
    ),
    shortDesc = u"""bis(cyanoethyl) ether""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "C6H11NOa",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {6,S} {16,S} {17,S}
6  C u0 p0 c0 {5,S} {7,S} {18,D}
7  N u0 p1 c0 {4,S} {6,S} {19,S}
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
18 O u0 p2 c0 {6,D}
19 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.076,43.448,52.959,60.785,71.917,80.103,93.961],'cal/(mol*K)'),
        H298 = (-58.84,'kcal/mol'),
        S298 = (87.054,'cal/(mol*K)'),
    ),
    shortDesc = u"""epsiloN-caprolactam""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "C6H11NOb",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {6,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {5,S} {7,D}
7  N u0 p1 c0 {6,D} {8,S}
8  O u0 p2 c0 {7,S} {19,S}
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
19 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([32.928,42.828,52.065,59.906,71.539,80.024,93.868],'cal/(mol*K)'),
        H298 = (-46.364,'kcal/mol'),
        S298 = (90.252,'cal/(mol*K)'),
    ),
    shortDesc = u"""cyclohexanone oxime""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "C6H13NO2a",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  N u0 p0 c+1 {5,S} {21,D} {22,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 O u0 p2 c0 {7,D}
22 O u0 p3 c-1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([41.268,51.407,60.771,68.767,80.925,89.652,101.773],'cal/(mol*K)'),
        H298 = (-42.523,'kcal/mol'),
        S298 = (112.313,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-nitrohexane""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "C6H13NO2b",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
7  N u0 p0 c+1 {1,S} {21,D} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {7,D}
22 O u0 p3 c-1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([41.218,51.428,60.87,68.923,81.104,89.781,101.919],'cal/(mol*K)'),
        H298 = (-43.785,'kcal/mol'),
        S298 = (110.037,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-nitrohexane""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "C6H13NO2c",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
7  N u0 p0 c+1 {1,S} {21,D} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 O u0 p2 c0 {7,D}
22 O u0 p3 c-1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([41.218,51.428,60.87,68.923,81.104,89.781,101.919],'cal/(mol*K)'),
        H298 = (-43.785,'kcal/mol'),
        S298 = (110.037,'cal/(mol*K)'),
    ),
    shortDesc = u"""3-nitrohexane""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "C6H13NO2d",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
7  N u0 p0 c+1 {4,S} {21,D} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {7,D}
22 O u0 p3 c-1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([41.218,51.428,60.87,68.923,81.104,89.781,101.919],'cal/(mol*K)'),
        H298 = (-43.785,'kcal/mol'),
        S298 = (110.037,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-nitro-2-methylpentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "C6H13NO2e",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
7  N u0 p0 c+1 {4,S} {21,D} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {7,D}
22 O u0 p3 c-1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([41.218,51.428,60.87,68.923,81.104,89.781,101.919],'cal/(mol*K)'),
        H298 = (-43.785,'kcal/mol'),
        S298 = (110.037,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-nitro-3-methylpentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "C6H13NO2f",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
7  N u0 p0 c+1 {4,S} {21,D} {22,S}
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
21 O u0 p2 c0 {7,D}
22 O u0 p3 c-1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([41.218,51.428,60.87,68.923,81.104,89.781,101.919],'cal/(mol*K)'),
        H298 = (-43.785,'kcal/mol'),
        S298 = (110.037,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-nitro-4-methyl pentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "C6H13NO2g",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
7  N u0 p0 c+1 {1,S} {21,D} {22,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u0 p2 c0 {7,D}
22 O u0 p3 c-1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([41.203,52.008,61.843,69.956,81.656,90.003,102.171],'cal/(mol*K)'),
        H298 = (-44.614,'kcal/mol'),
        S298 = (103.022,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-nitro-2-methylpentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "C6H13NO2h",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
7  N u0 p0 c+1 {2,S} {21,D} {22,S}
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
21 O u0 p2 c0 {7,D}
22 O u0 p3 c-1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([41.168,51.45,60.969,69.08,81.283,89.909,102.065],'cal/(mol*K)'),
        H298 = (-45.046,'kcal/mol'),
        S298 = (107.76,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-nitro-3-methylpentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "C6H13NO2i",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {18,S} {19,S} {20,S}
7  N u0 p0 c+1 {2,S} {21,D} {22,S}
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
21 O u0 p2 c0 {7,D}
22 O u0 p3 c-1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([41.168,51.45,60.969,69.08,81.283,89.909,102.065],'cal/(mol*K)'),
        H298 = (-45.046,'kcal/mol'),
        S298 = (107.76,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-nitro-4-methylpentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "C6H13NO2j",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {9,S}
3  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
7  N u0 p0 c+1 {2,S} {21,D} {22,S}
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
21 O u0 p2 c0 {7,D}
22 O u0 p3 c-1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([41.168,51.45,60.969,69.08,81.283,89.909,102.065],'cal/(mol*K)'),
        H298 = (-45.046,'kcal/mol'),
        S298 = (107.76,'cal/(mol*K)'),
    ),
    shortDesc = u"""3-nitro-2-methylpentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "C6H13NO2k",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
6  C u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
7  N u0 p0 c+1 {1,S} {21,D} {22,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
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
20 H u0 p0 c0 {6,S}
21 O u0 p2 c0 {7,D}
22 O u0 p3 c-1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([41.203,52.008,61.843,69.956,81.656,90.003,102.171],'cal/(mol*K)'),
        H298 = (-44.614,'kcal/mol'),
        S298 = (103.022,'cal/(mol*K)'),
    ),
    shortDesc = u"""3-nitro-3-methylpentane""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "C6H13NO2l",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
7  N u0 p0 c+1 {3,S} {21,D} {22,S}
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
21 O u0 p2 c0 {7,D}
22 O u0 p3 c-1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([41.203,52.008,61.843,69.956,81.656,90.003,102.171],'cal/(mol*K)'),
        H298 = (-44.614,'kcal/mol'),
        S298 = (103.022,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-nitro-2,2-dimethylbutane""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "C6H13NO2m",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {8,S}
3  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
7  N u0 p0 c+1 {3,S} {21,D} {22,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
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
21 O u0 p2 c0 {7,D}
22 O u0 p3 c-1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([41.168,51.45,60.969,69.08,81.283,89.909,102.065],'cal/(mol*K)'),
        H298 = (-45.046,'kcal/mol'),
        S298 = (107.76,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-nitro-2,3-dimethylbutane""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "C6H13NO2n",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {7,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
7  N u0 p0 c+1 {3,S} {21,D} {22,S}
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
21 O u0 p2 c0 {7,D}
22 O u0 p3 c-1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([41.203,52.008,61.843,69.956,81.656,90.003,102.171],'cal/(mol*K)'),
        H298 = (-44.614,'kcal/mol'),
        S298 = (103.022,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-nitro-3,3-dimethylbutane""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "C6H13NO2o",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
7  N u0 p0 c+1 {1,S} {21,D} {22,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 O u0 p2 c0 {7,D}
22 O u0 p3 c-1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([41.153,52.03,61.942,70.112,81.835,90.131,102.317],'cal/(mol*K)'),
        H298 = (-45.876,'kcal/mol'),
        S298 = (100.746,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-nitro-2,3-dimethylbutane""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "C6H13NO2p",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {18,S} {19,S} {20,S}
7  N u0 p0 c+1 {2,S} {21,D} {22,S}
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
20 H u0 p0 c0 {6,S}
21 O u0 p2 c0 {7,D}
22 O u0 p3 c-1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([41.153,52.03,61.942,70.112,81.835,90.131,102.317],'cal/(mol*K)'),
        H298 = (-45.876,'kcal/mol'),
        S298 = (100.746,'cal/(mol*K)'),
    ),
    shortDesc = u"""2-nitro-3,3-dimethylbutane""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "C6H13NO2q",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
7  N u0 p0 c+1 {4,S} {21,D} {22,S}
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
21 O u0 p2 c0 {7,D}
22 O u0 p3 c-1 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([41.218,51.428,60.87,68.923,81.104,89.781,101.919],'cal/(mol*K)'),
        H298 = (-43.785,'kcal/mol'),
        S298 = (110.037,'cal/(mol*K)'),
    ),
    shortDesc = u"""1-nitro-2-ethylbutane""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "C6H14N2O2",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,S} {16,S} {17,S}
5  C u0 p0 c0 {4,S} {6,S} {18,S} {19,S}
6  C u0 p0 c0 {5,S} {7,S} {20,S} {21,S}
7  N u0 p1 c0 {6,S} {22,S} {23,S}
8  C u0 p0 c0 {2,S} {9,D} {10,S}
9  O u0 p2 c0 {8,D}
10 O u0 p2 c0 {8,S} {24,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([47.577,58.453,68.234,76.436,88.756,97.674,109.118],'cal/(mol*K)'),
        H298 = (-110.178,'kcal/mol'),
        S298 = (126.872,'cal/(mol*K)'),
    ),
    shortDesc = u"""lysine""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "C6H15NO2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {12,S}
3  O u0 p2 c0 {2,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  N u0 p1 c0 {1,S} {6,S} {17,S}
6  C u0 p0 c0 {5,S} {7,S} {18,S} {19,S}
7  C u0 p0 c0 {6,S} {8,S} {9,S} {20,S}
8  O u0 p2 c0 {7,S} {21,S}
9  C u0 p0 c0 {7,S} {22,S} {23,S} {24,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([45.157,56.428,67.029,75.658,87.682,96.788,111.32],'cal/(mol*K)'),
        H298 = (-108.505,'kcal/mol'),
        S298 = (122.798,'cal/(mol*K)'),
    ),
    shortDesc = u"""diisopropanolamine""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "C6H15NO3",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  O u0 p2 c0 {3,S} {15,S}
5  C u0 p0 c0 {1,S} {6,S} {16,S} {17,S}
6  C u0 p0 c0 {5,S} {7,S} {18,S} {19,S}
7  O u0 p2 c0 {6,S} {20,S}
8  C u0 p0 c0 {1,S} {9,S} {21,S} {22,S}
9  C u0 p0 c0 {8,S} {10,S} {23,S} {24,S}
10 O u0 p2 c0 {9,S} {25,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([47.355,59.118,69.941,79.004,91.932,100.304,112.056],'cal/(mol*K)'),
        H298 = (-134.336,'kcal/mol'),
        S298 = (128.756,'cal/(mol*K)'),
    ),
    shortDesc = u"""triethanolamine""",
    longDesc = 
u"""

""",
)

