#!/usr/bin/env python
# encoding: utf-8

name = ""
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "AR",
    molecule = 
"""
1 Ar u0 p4 c0
""",
    transport = TransportData(
        shapeIndex = 0,
        epsilon = (1134.93,'J/mol'),
        sigma = (3.33,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 1,
    label = "C",
    molecule = 
"""
1 C u0 p2 c0
""",
    transport = TransportData(
        shapeIndex = 0,
        epsilon = (593.653,'J/mol'),
        sigma = (3.298,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 2,
    label = "C2H",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {3,S}
2 C u1 p0 c0 {1,T}
3 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (1737.72,'J/mol'),
        sigma = (4.1,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 2.5,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 3,
    label = "C2H2",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (1737.72,'J/mol'),
        sigma = (4.1,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 2.5,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 4,
    label = "C2H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u1 p0 c0 {1,D} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1737.72,'J/mol'),
        sigma = (4.1,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 5,
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
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2334.7,'J/mol'),
        sigma = (3.971,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.5,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 6,
    label = "C2H5",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2097.74,'J/mol'),
        sigma = (4.302,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.5,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 7,
    label = "C2H6",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2097.74,'J/mol'),
        sigma = (4.302,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.5,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 8,
    label = "C3H6",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2218.3,'J/mol'),
        sigma = (4.982,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 9,
    label = "C3H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2218.3,'J/mol'),
        sigma = (4.982,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 10,
    label = "C3H8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2218.3,'J/mol'),
        sigma = (4.982,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 11,
    label = "CH",
    molecule = 
"""
multiplicity 2
1 C u1 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (665.158,'J/mol'),
        sigma = (2.75,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 12,
    label = "CH2",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (1197.28,'J/mol'),
        sigma = (3.8,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 13,
    label = "CH2(S)",
    molecule = 
"""
1 C u0 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (1197.28,'J/mol'),
        sigma = (3.8,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 14,
    label = "CH2CO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (3625.11,'J/mol'),
        sigma = (3.97,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 2.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 15,
    label = "CH2O",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (4140.61,'J/mol'),
        sigma = (3.59,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 2.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 16,
    label = "CH2OH",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (3467.14,'J/mol'),
        sigma = (3.69,'angstroms'),
        dipoleMoment = (1.7,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 2.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 17,
    label = "CH3",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (1197.28,'J/mol'),
        sigma = (3.8,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 18,
    label = "CH3CCH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,D} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2161.76,'J/mol'),
        sigma = (4.85,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 19,
    label = "CH3CHO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (3625.11,'J/mol'),
        sigma = (3.97,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 2.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 20,
    label = "CH2CHO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 C u1 p0 c0 {3,S} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (3625.11,'J/mol'),
        sigma = (3.97,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 2.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 21,
    label = "CH3CO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u1 p0 c0 {1,D} {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (3625.11,'J/mol'),
        sigma = (3.97,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 2.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 22,
    label = "CH3O",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (3467.14,'J/mol'),
        sigma = (3.69,'angstroms'),
        dipoleMoment = (1.7,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 2.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 23,
    label = "CH3OH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (4005.91,'J/mol'),
        sigma = (3.626,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 24,
    label = "CH4",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1175.67,'J/mol'),
        sigma = (3.746,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (2.6,'angstroms^3'),
        rotrelaxcollnum = 13.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 25,
    label = "CO",
    molecule = 
"""
1 O u0 p1 c+1 {2,T}
2 C u0 p1 c-1 {1,T}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (815.65,'J/mol'),
        sigma = (3.65,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (1.95,'angstroms^3'),
        rotrelaxcollnum = 1.8,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 26,
    label = "CO2",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (2028.73,'J/mol'),
        sigma = (3.763,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (2.65,'angstroms^3'),
        rotrelaxcollnum = 2.1,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 27,
    label = "H",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    transport = TransportData(
        shapeIndex = 0,
        epsilon = (1205.6,'J/mol'),
        sigma = (2.05,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 28,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (315.95,'J/mol'),
        sigma = (2.92,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0.79,'angstroms^3'),
        rotrelaxcollnum = 280.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 29,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (4759.2,'J/mol'),
        sigma = (2.605,'angstroms'),
        dipoleMoment = (1.844,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 4.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 30,
    label = "H2O2",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (892.974,'J/mol'),
        sigma = (3.458,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 3.8,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 31,
    label = "HCCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 C u1 p0 c0 {3,D} {4,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1247.17,'J/mol'),
        sigma = (2.5,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 32,
    label = "HCCOH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (3625.11,'J/mol'),
        sigma = (3.97,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 2.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 33,
    label = "HCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (4140.61,'J/mol'),
        sigma = (3.59,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 34,
    label = "HO2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (892.974,'J/mol'),
        sigma = (3.458,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 35,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (810.911,'J/mol'),
        sigma = (3.621,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (1.76,'angstroms^3'),
        rotrelaxcollnum = 4.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 36,
    label = "O",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    transport = TransportData(
        shapeIndex = 0,
        epsilon = (665.158,'J/mol'),
        sigma = (2.75,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 37,
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (892.974,'J/mol'),
        sigma = (3.458,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (1.6,'angstroms^3'),
        rotrelaxcollnum = 3.8,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 38,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (665.158,'J/mol'),
        sigma = (2.75,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 39,
    label = "F",
    molecule = 
"""
multiplicity 2
1 F u1 p3 c0
""",
    transport = TransportData(
        shapeIndex = 0,
        epsilon = (665.158,'J/mol'),
        sigma = (2.75,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 40,
    label = "F2",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 F u0 p3 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (1045.13,'J/mol'),
        sigma = (3.301,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (1.6,'angstroms^3'),
        rotrelaxcollnum = 3.8,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 41,
    label = "HF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (2743.78,'J/mol'),
        sigma = (3.148,'angstroms'),
        dipoleMoment = (1.92,'De'),
        polarizability = (2.46,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 42,
    label = "CH3F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2178.39,'J/mol'),
        sigma = (4.123,'angstroms'),
        dipoleMoment = (1.8,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 43,
    label = "CH2F2",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2178.39,'J/mol'),
        sigma = (4.123,'angstroms'),
        dipoleMoment = (1.8,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 44,
    label = "CHF3",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2178.39,'J/mol'),
        sigma = (4.123,'angstroms'),
        dipoleMoment = (1.8,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 45,
    label = "CF4",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {5,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1114.14,'J/mol'),
        sigma = (4.662,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 46,
    label = "CH2F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2178.39,'J/mol'),
        sigma = (4.123,'angstroms'),
        dipoleMoment = (1.8,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 47,
    label = "CHF2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u1 p0 c0 {1,S} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2178.39,'J/mol'),
        sigma = (4.123,'angstroms'),
        dipoleMoment = (1.8,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 48,
    label = "CF3",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u1 p0 c0 {1,S} {2,S} {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1006.05,'J/mol'),
        sigma = (4.32,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 49,
    label = "CHF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p1 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2178.39,'J/mol'),
        sigma = (4.123,'angstroms'),
        dipoleMoment = (1.8,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 50,
    label = "CF2",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p1 c0 {1,S} {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (897.963,'J/mol'),
        sigma = (3.977,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 51,
    label = "CF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p1 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (783.223,'J/mol'),
        sigma = (3.635,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 52,
    label = "CF3O",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 O u1 p2 c0 {5,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2914.22,'J/mol'),
        sigma = (4.906,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 53,
    label = "CHFO",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2914.22,'J/mol'),
        sigma = (4.906,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 54,
    label = "CF2O",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2914.22,'J/mol'),
        sigma = (4.906,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 55,
    label = "CFO",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {3,D}
3 C u1 p0 c0 {1,S} {2,D}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (7150.45,'J/mol'),
        sigma = (4,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 56,
    label = "CH3-CH2F",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2595.78,'J/mol'),
        sigma = (4.583,'angstroms'),
        dipoleMoment = (2,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 57,
    label = "CH3-CHF2",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2688.9,'J/mol'),
        sigma = (4.798,'angstroms'),
        dipoleMoment = (2.3,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 58,
    label = "CH2F-CH2F",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2595.78,'J/mol'),
        sigma = (4.583,'angstroms'),
        dipoleMoment = (2,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 59,
    label = "CH3-CF3",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2403.71,'J/mol'),
        sigma = (4.911,'angstroms'),
        dipoleMoment = (2.3,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 60,
    label = "CH2F-CHF2",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2688.9,'J/mol'),
        sigma = (4.798,'angstroms'),
        dipoleMoment = (2.3,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 61,
    label = "CH2F-CF3",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {6,S}
3 F u0 p3 c0 {6,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2688.9,'J/mol'),
        sigma = (4.85,'angstroms'),
        dipoleMoment = (2.3,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 62,
    label = "CHF2-CHF2",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {6,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
6 C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {6,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2688.9,'J/mol'),
        sigma = (4.85,'angstroms'),
        dipoleMoment = (2,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 63,
    label = "CHF2-CF3",
    molecule = 
"""
1 F u0 p3 c0 {6,S}
2 F u0 p3 c0 {6,S}
3 F u0 p3 c0 {7,S}
4 F u0 p3 c0 {7,S}
5 F u0 p3 c0 {7,S}
6 C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
7 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
8 H u0 p0 c0 {6,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2688.9,'J/mol'),
        sigma = (4.9,'angstroms'),
        dipoleMoment = (1.5,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 64,
    label = "CF3-CF3",
    molecule = 
"""
1 F u0 p3 c0 {7,S}
2 F u0 p3 c0 {7,S}
3 F u0 p3 c0 {7,S}
4 F u0 p3 c0 {8,S}
5 F u0 p3 c0 {8,S}
6 F u0 p3 c0 {8,S}
7 C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
8 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1927.29,'J/mol'),
        sigma = (4.969,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 65,
    label = "CH3-CHF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u1 p0 c0 {1,S} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2595.78,'J/mol'),
        sigma = (4.583,'angstroms'),
        dipoleMoment = (2,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 66,
    label = "CH2F-CH2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u1 p0 c0 {2,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2595.78,'J/mol'),
        sigma = (4.583,'angstroms'),
        dipoleMoment = (2,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 67,
    label = "CH3-CF2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u1 p0 c0 {1,S} {2,S} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2688.9,'J/mol'),
        sigma = (4.798,'angstroms'),
        dipoleMoment = (2.3,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 68,
    label = "CH2F-CHF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u1 p0 c0 {2,S} {3,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2595.78,'J/mol'),
        sigma = (4.583,'angstroms'),
        dipoleMoment = (2,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 69,
    label = "CHF2-CH2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 C u1 p0 c0 {3,S} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2688.9,'J/mol'),
        sigma = (4.798,'angstroms'),
        dipoleMoment = (2.3,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 70,
    label = "CH2F-CF2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 C u1 p0 c0 {2,S} {3,S} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2688.9,'J/mol'),
        sigma = (4.798,'angstroms'),
        dipoleMoment = (2.3,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 71,
    label = "CHF2-CHF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 C u1 p0 c0 {3,S} {4,S} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2688.9,'J/mol'),
        sigma = (4.798,'angstroms'),
        dipoleMoment = (2.3,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 72,
    label = "CHF2-CF2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {6,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
6 C u1 p0 c0 {3,S} {4,S} {5,S}
7 H u0 p0 c0 {5,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2688.9,'J/mol'),
        sigma = (4.85,'angstroms'),
        dipoleMoment = (2,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 73,
    label = "CF3-CH2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 C u1 p0 c0 {4,S} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2403.71,'J/mol'),
        sigma = (4.911,'angstroms'),
        dipoleMoment = (2.3,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 74,
    label = "CF3-CHF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u1 p0 c0 {4,S} {5,S} {7,S}
7 H u0 p0 c0 {6,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2688.9,'J/mol'),
        sigma = (4.85,'angstroms'),
        dipoleMoment = (2.3,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 75,
    label = "CF3-CF2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {6,S}
2 F u0 p3 c0 {6,S}
3 F u0 p3 c0 {6,S}
4 F u0 p3 c0 {7,S}
5 F u0 p3 c0 {7,S}
6 C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
7 C u1 p0 c0 {4,S} {5,S} {6,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2688.9,'J/mol'),
        sigma = (4.9,'angstroms'),
        dipoleMoment = (1.5,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 76,
    label = "CH2CHF",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,S} {2,D} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2263.2,'J/mol'),
        sigma = (4.322,'angstroms'),
        dipoleMoment = (1.4,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 77,
    label = "CH2CF2",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {4,D} {5,S} {6,S}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2091.09,'J/mol'),
        sigma = (4.442,'angstroms'),
        dipoleMoment = (1.4,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 78,
    label = "CHFCHF[Z]",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {2,S} {3,D} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2091.09,'J/mol'),
        sigma = (4.442,'angstroms'),
        dipoleMoment = (1.4,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 79,
    label = "CHFCF2",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {5,D} {6,S}
5 C u0 p0 c0 {2,S} {3,S} {4,D}
6 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2091.09,'J/mol'),
        sigma = (4.442,'angstroms'),
        dipoleMoment = (1.4,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 80,
    label = "CF2CF2",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {6,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {6,D}
6 C u0 p0 c0 {3,S} {4,S} {5,D}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2113.54,'J/mol'),
        sigma = (4.647,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 81,
    label = "CH2CF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2263.2,'J/mol'),
        sigma = (4.322,'angstroms'),
        dipoleMoment = (1.4,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 82,
    label = "CHFCH[Z]",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u1 p0 c0 {2,D} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2263.2,'J/mol'),
        sigma = (4.322,'angstroms'),
        dipoleMoment = (1.4,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 83,
    label = "CHFCF[Z]",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u1 p0 c0 {2,S} {3,D}
5 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2091.09,'J/mol'),
        sigma = (4.442,'angstroms'),
        dipoleMoment = (1.4,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 84,
    label = "CF2CH",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,D}
4 C u1 p0 c0 {3,D} {5,S}
5 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2091.09,'J/mol'),
        sigma = (4.442,'angstroms'),
        dipoleMoment = (1.4,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 85,
    label = "CF2CF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {2,S} {5,D}
5 C u1 p0 c0 {3,S} {4,D}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2091.09,'J/mol'),
        sigma = (4.442,'angstroms'),
        dipoleMoment = (1.4,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 86,
    label = "C2HF",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,T} {4,S}
3 C u0 p0 c0 {1,S} {2,T}
4 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (1870.76,'J/mol'),
        sigma = (4.25,'angstroms'),
        dipoleMoment = (1,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 87,
    label = "C2F2",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {2,S} {3,T}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (1995.47,'J/mol'),
        sigma = (4.4,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 88,
    label = "CHFCO",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {4,D}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2914.22,'J/mol'),
        sigma = (4.906,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 89,
    label = "CF2CO",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 O u0 p2 c0 {5,D}
4 C u0 p0 c0 {1,S} {2,S} {5,D}
5 C u0 p0 c0 {3,D} {4,D}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2914.22,'J/mol'),
        sigma = (4.906,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 90,
    label = "CFCO",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {4,D}
3 C u1 p0 c0 {1,S} {4,D}
4 C u0 p0 c0 {2,D} {3,D}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2914.22,'J/mol'),
        sigma = (4.906,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 91,
    label = "CF3CO",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 O u0 p2 c0 {6,D}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u1 p0 c0 {4,D} {5,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2914.22,'J/mol'),
        sigma = (4.906,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 92,
    label = "CF3CHO",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 O u0 p2 c0 {6,D}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u0 p0 c0 {4,D} {5,S} {7,S}
7 H u0 p0 c0 {6,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2914.22,'J/mol'),
        sigma = (4.906,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 93,
    label = "CF3COF",
    molecule = 
"""
1 F u0 p3 c0 {6,S}
2 F u0 p3 c0 {6,S}
3 F u0 p3 c0 {6,S}
4 F u0 p3 c0 {7,S}
5 O u0 p2 c0 {7,D}
6 C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
7 C u0 p0 c0 {4,S} {5,D} {6,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2914.22,'J/mol'),
        sigma = (4.906,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 94,
    label = "CF3CHCH2",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 C u0 p0 c0 {4,S} {6,D} {7,S}
6 C u0 p0 c0 {5,D} {8,S} {9,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {6,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2785.35,'J/mol'),
        sigma = (4.7,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 95,
    label = "CF3CCH2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
5 C u0 p0 c0 {6,D} {7,S} {8,S}
6 C u1 p0 c0 {4,S} {5,D}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2768.72,'J/mol'),
        sigma = (4.7,'angstroms'),
        dipoleMoment = (2.444,'De'),
        polarizability = (6.006,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 96,
    label = "CF3CCH",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 C u0 p0 c0 {4,S} {6,T}
6 C u0 p0 c0 {5,T} {7,S}
7 H u0 p0 c0 {6,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2752.09,'J/mol'),
        sigma = (4.7,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 97,
    label = "CF3COCH3",
    molecule = 
"""
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {6,S}
3  F u0 p3 c0 {6,S}
4  O u0 p2 c0 {7,D}
5  C u0 p0 c0 {7,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
7  C u0 p0 c0 {4,D} {5,S} {6,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (3051.41,'J/mol'),
        sigma = (5,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 98,
    label = "CH2CFCF3",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u0 p0 c0 {4,S} {5,S} {7,D}
7 C u0 p0 c0 {6,D} {8,S} {9,S}
8 H u0 p0 c0 {7,S}
9 H u0 p0 c0 {7,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (3084.67,'J/mol'),
        sigma = (4.9,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 99,
    label = "CFCCF3",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {7,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u0 p0 c0 {5,S} {7,T}
7 C u0 p0 c0 {4,S} {6,T}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (3001.52,'J/mol'),
        sigma = (4.8,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 100,
    label = "CH-CFCF3",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u0 p0 c0 {4,S} {5,S} {7,D}
7 C u1 p0 c0 {6,D} {8,S}
8 H u0 p0 c0 {7,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (3051.41,'J/mol'),
        sigma = (4.9,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 101,
    label = "CHFCHCF3",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {7,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u0 p0 c0 {5,S} {7,D} {8,S}
7 C u0 p0 c0 {4,S} {6,D} {9,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {7,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (3084.67,'J/mol'),
        sigma = (4.9,'angstroms'),
        dipoleMoment = (0,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 102,
    label = "CFCHCF3",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {7,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u0 p0 c0 {5,S} {7,D} {8,S}
7 C u1 p0 c0 {4,S} {6,D}
8 H u0 p0 c0 {6,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2785.35,'J/mol'),
        sigma = (4.7,'angstroms'),
        dipoleMoment = (2.722,'De'),
        polarizability = (4.631,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 103,
    label = "CHFCCF3",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
6 C u0 p0 c0 {4,S} {7,D} {8,S}
7 C u1 p0 c0 {5,S} {6,D}
8 H u0 p0 c0 {6,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2785.35,'J/mol'),
        sigma = (4.7,'angstroms'),
        dipoleMoment = (2.722,'De'),
        polarizability = (4.631,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

entry(
    index = 104,
    label = "CH2CFO",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 O u0 p2 c0 {4,D}
3 C u1 p0 c0 {4,S} {5,S} {6,S}
4 C u0 p0 c0 {1,S} {2,D} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2595.78,'J/mol'),
        sigma = (4.583,'angstroms'),
        dipoleMoment = (3.302,'De'),
        polarizability = (3.442,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""From NIST CH2F2 model""",
    longDesc = u"""""",
)

