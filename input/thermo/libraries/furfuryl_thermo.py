#!/usr/bin/env python
# encoding: utf-8

name = "Thermo Library Furfuryl 2023"
shortDesc = "The reactions of 2-furfuryl alcohol with hydrogen atom: A theoretical calculation and kinetic modeling analysis"
longDesc = """
https://www.sciencedirect.com/science/article/pii/S0010218023000123?via%3Dihub#cebibl1
"""
entry(
    index = 0,
    label = "OCC1[CH]C=CO1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {7,S} {11,S}
4  C u1 p0 c0 {3,S} {5,S} {12,S}
5  C u0 p0 c0 {4,S} {6,D} {13,S}
6  C u0 p0 c0 {5,D} {7,S} {14,S}
7  O u0 p2 c0 {3,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([298,400,600,800,1000,1200,1400,1800,2000,2500],'K'),
        Cpdata = ([26.67,34.7,46.72,54.54,59.96,63.92,66.89,70.89,72.24,74.55],'cal/(mol*K)'),
        H298 = (74.91,'kcal/mol'),
        S298 = (82.98,'cal/(mol*K)'),
    ),
    shortDesc = """W1""",
    longDesc = 
"""

""",
)

entry(
    index = 1,
    label = "OC[C]1CC=CO1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u1 p0 c0 {2,S} {4,S} {7,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {6,D} {13,S}
6  C u0 p0 c0 {5,D} {7,S} {14,S}
7  O u0 p2 c0 {3,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([298,400,600,800,1000,1200,1400,1800,2000,2500],'K'),
        Cpdata = ([26.66,34.39,46.33,54.28,59.82,63.86,66.87,70.91,72.27,74.58],'cal/(mol*K)'),
        H298 = (75.01,'kcal/mol'),
        S298 = (85.32,'cal/(mol*K)'),
    ),
    shortDesc = """W2""",
    longDesc = 
"""

""",
)

entry(
    index = 2,
    label = "OCC1=CC[CH]O1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,D} {7,S}
4  C u0 p0 c0 {3,D} {5,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
6  C u1 p0 c0 {5,S} {7,S} {14,S}
7  O u0 p2 c0 {3,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([298,400,600,800,1000,1200,1400,1800,2000,2500],'K'),
        Cpdata = ([27.16,34.85,46.6,54.41,59.89,63.9,66.89,70.91,72.27,74.57],'cal/(mol*K)'),
        H298 = (74.84,'kcal/mol'),
        S298 = (84.41,'cal/(mol*K)'),
    ),
    shortDesc = """W3""",
    longDesc = 
"""

""",
)

entry(
    index = 3,
    label = "OCC1=C[CH]CO1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,D} {7,S}
4  C u0 p0 c0 {3,D} {5,S} {11,S}
5  C u1 p0 c0 {4,S} {6,S} {12,S}
6  C u0 p0 c0 {5,S} {7,S} {13,S} {14,S}
7  O u0 p2 c0 {3,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([298,400,600,800,1000,1200,1400,1800,2000,2500],'K'),
        Cpdata = ([26.85,34.57,46.46,54.35,59.85,63.87,66.87,70.89,72.26,74.57],'cal/(mol*K)'),
        H298 = (74.98,'kcal/mol'),
        S298 = (84.91,'cal/(mol*K)'),
    ),
    shortDesc = """W4""",
    longDesc = 
"""

""",
)

entry(
    index = 4,
    label = "O=C[CH]C=CCO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u1 p0 c0 {2,S} {4,S} {9,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {4,D} {6,S} {11,S}
6  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
7  O u0 p2 c0 {6,S} {14,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([298,400,600,800,1000,1200,1400,1800,2000,2500],'K'),
        Cpdata = ([29.19,36.11,47.13,54.68,60.05,64.01,66.97,70.96,72.31,74.6],'cal/(mol*K)'),
        H298 = (74.2,'kcal/mol'),
        S298 = (91.28,'cal/(mol*K)'),
    ),
    shortDesc = """W5""",
    longDesc = 
"""

""",
)

entry(
    index = 5,
    label = "O=CCC=C[CH]O",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {6,S} {12,S}
6  C u1 p0 c0 {5,S} {7,S} {13,S}
7  O u0 p2 c0 {6,S} {14,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([298,400,600,800,1000,1200,1400,1800,2000,2500],'K'),
        Cpdata = ([30.07,36.95,47.68,55.04,60.3,64.19,67.11,71.05,72.39,74.65],'cal/(mol*K)'),
        H298 = (73.53,'kcal/mol'),
        S298 = (92.41,'cal/(mol*K)'),
    ),
    shortDesc = """W6""",
    longDesc = 
"""

""",
)

