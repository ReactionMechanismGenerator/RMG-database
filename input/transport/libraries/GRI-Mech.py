#!/usr/bin/env python
# encoding: utf-8

name = ""
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "AR",
    molecule = 
"""
1 Ar u0 p4 c0
""",
    transport = TransportData(
        shapeIndex = 0,
        epsilon = (1134.93,'J/mol'),
        sigma = (3.33,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for AR""",
    longDesc = u"""""",
)

entry(
    index = 2,
    label = "C(T)",
    molecule = 
"""
multiplicity 3
1 C u2 p1 c0
""",
    transport = TransportData(
        shapeIndex = 0,
        epsilon = (593.655,'J/mol'),
        sigma = (3.298,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C""",
    longDesc = u"""""",
)

entry(
    index = 3,
    label = "C2",
    molecule = 
"""
multiplicity 3
1 C u1 p0 c0 {2,T}
2 C u1 p0 c0 {1,T}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (810.913,'J/mol'),
        sigma = (3.621,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (1.76,'angstroms^3'),
        rotrelaxcollnum = 4.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C2""",
    longDesc = u"""""",
)

entry(
    index = 4,
    label = "C2O(T)",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (1932.29,'J/mol'),
        sigma = (3.828,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C2O""",
    longDesc = 
u"""
Same value as C2O(S).
""",
)

entry(
    index = 5,
    label = "C2O(S)",
    molecule = 
"""
1 C u0 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (1932.29,'J/mol'),
        sigma = (3.828,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C2O""",
    longDesc = 
u"""
Same Value as C2O(T).
""",
)

entry(
    index = 6,
    label = "C2H",
    molecule = 
"""
multiplicity 2
1 H u0 p0 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u1 p0 c0 {2,T}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (1737.73,'J/mol'),
        sigma = (4.1,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 2.5,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C2H""",
    longDesc = u"""""",
)

entry(
    index = 7,
    label = "C2H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (1737.73,'J/mol'),
        sigma = (4.1,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 2.5,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C2H2""",
    longDesc = u"""""",
)

entry(
    index = 8,
    label = "C2H2OH",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {4,S}
2 C u0 p0 c0 {1,D} {3,S} {5,S}
3 O u0 p2 c0 {2,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1868.27,'J/mol'),
        sigma = (4.162,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C2H2OH""",
    longDesc = u"""""",
)

entry(
    index = 9,
    label = "C2H3",
    molecule = 
"""
multiplicity 2
1 H u0 p0 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1737.73,'J/mol'),
        sigma = (4.1,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C2H3""",
    longDesc = u"""""",
)

entry(
    index = 10,
    label = "C2H4",
    molecule = 
"""
1 H u0 p0 c0 {3,S}
2 H u0 p0 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2334.71,'J/mol'),
        sigma = (3.971,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.5,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C2H4""",
    longDesc = u"""""",
)

entry(
    index = 11,
    label = "C2H5",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2097.75,'J/mol'),
        sigma = (4.302,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.5,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C2H5""",
    longDesc = u"""""",
)

entry(
    index = 12,
    label = "C2H6",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2097.75,'J/mol'),
        sigma = (4.302,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.5,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C2H6""",
    longDesc = u"""""",
)

entry(
    index = 14,
    label = "C2N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 N u0 p1 c0 {3,T}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (2901.76,'J/mol'),
        sigma = (4.361,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C2N2""",
    longDesc = u"""""",
)

entry(
    index = 15,
    label = "C3H2",
    molecule = 
"""
multiplicity 3
1 C u1 p0 c0 {2,D} {4,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u1 p0 c0 {2,D} {5,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1737.73,'J/mol'),
        sigma = (4.1,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C3H2""",
    longDesc = u"""""",
)

entry(
    index = 16,
    label = "C3H4",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {1,S} {2,D} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (2095.25,'J/mol'),
        sigma = (4.76,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for 'C3H4'; cyclic structure guessed""",
    longDesc = u"""""",
)

entry(
    index = 17,
    label = "C3H6",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2218.31,'J/mol'),
        sigma = (4.982,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C3H6""",
    longDesc = u"""""",
)

entry(
    index = 19,
    label = "C4H6",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {5,S} {6,S}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2968.28,'J/mol'),
        sigma = (5.18,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C4H6""",
    longDesc = u"""""",
)

entry(
    index = 20,
    label = "I*C3H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u1 p0 c0 {1,S} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2218.31,'J/mol'),
        sigma = (4.982,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for I*C3H7""",
    longDesc = u"""""",
)

entry(
    index = 21,
    label = "N*C3H7",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2218.31,'J/mol'),
        sigma = (4.982,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for N*C3H7""",
    longDesc = u"""""",
)

entry(
    index = 22,
    label = "C3H8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  H u0 p0 c0 {1,S}
5  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6  H u0 p0 c0 {5,S}
7  H u0 p0 c0 {5,S}
8  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {8,S}
11 H u0 p0 c0 {8,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2218.31,'J/mol'),
        sigma = (4.982,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C3H8""",
    longDesc = u"""""",
)

entry(
    index = 23,
    label = "C4H",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {5,S}
5 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (2968.28,'J/mol'),
        sigma = (5.18,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C4H""",
    longDesc = u"""""",
)

entry(
    index = 24,
    label = "C4H2",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {5,S}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {6,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (2968.28,'J/mol'),
        sigma = (5.18,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C4H2""",
    longDesc = u"""""",
)

entry(
    index = 26,
    label = "C4H8",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {5,S} {6,S}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2968.28,'J/mol'),
        sigma = (5.176,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for 'C4H8'. 1-butune structure guessed""",
    longDesc = u"""""",
)

entry(
    index = 27,
    label = "C4H9",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2968.28,'J/mol'),
        sigma = (5.176,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C4H9""",
    longDesc = u"""""",
)

entry(
    index = 28,
    label = "I*C4H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2968.28,'J/mol'),
        sigma = (5.176,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for I*C4H9""",
    longDesc = u"""""",
)

entry(
    index = 37,
    label = "CH(D)",
    molecule = 
"""
multiplicity 2
1 C u1 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (665.16,'J/mol'),
        sigma = (2.75,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH""",
    longDesc = u"""""",
)

entry(
    index = 38,
    label = "CH2",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1197.29,'J/mol'),
        sigma = (3.8,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2""",
    longDesc = u"""""",
)

entry(
    index = 39,
    label = "CH2(S)",
    molecule = 
"""
1 C u0 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1197.29,'J/mol'),
        sigma = (3.8,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2(S)""",
    longDesc = u"""""",
)

entry(
    index = 41,
    label = "CH2CHCCH",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2968.28,'J/mol'),
        sigma = (5.18,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2CHCCH""",
    longDesc = u"""""",
)

entry(
    index = 42,
    label = "CH2CHCCH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 C u1 p0 c0 {2,S} {4,D}
4 C u0 p0 c0 {3,D} {8,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2968.28,'J/mol'),
        sigma = (5.18,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2CHCCH2""",
    longDesc = u"""""",
)

entry(
    index = 43,
    label = "CH2CHCH2",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {2,D} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2161.77,'J/mol'),
        sigma = (4.85,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2CHCH2""",
    longDesc = u"""""",
)

entry(
    index = 44,
    label = "CH2CHCHCH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 C u0 p0 c0 {2,S} {4,D} {8,S}
4 C u1 p0 c0 {3,D} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2968.28,'J/mol'),
        sigma = (5.18,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2CHCHCH""",
    longDesc = u"""""",
)

entry(
    index = 45,
    label = "CH2CHCHCH2",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {5,S} {6,S}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2968.28,'J/mol'),
        sigma = (5.18,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2CHCHCH2""",
    longDesc = u"""""",
)

entry(
    index = 46,
    label = "CH2CO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,D} {5,D}
5 O u0 p2 c0 {4,D}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (3625.12,'J/mol'),
        sigma = (3.97,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 2.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2CO""",
    longDesc = u"""""",
)

entry(
    index = 47,
    label = "CH2O",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,D}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 O u0 p2 c0 {1,D}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (4140.62,'J/mol'),
        sigma = (3.59,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 2.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2O""",
    longDesc = u"""""",
)

entry(
    index = 48,
    label = "CH2OH",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 O u0 p2 c0 {1,S} {5,S}
5 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (3467.15,'J/mol'),
        sigma = (3.69,'angstroms'),
        dipoleMoment = (1.7,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 2.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2OH""",
    longDesc = u"""""",
)

entry(
    index = 49,
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
        shapeIndex = 2,
        epsilon = (1197.29,'J/mol'),
        sigma = (3.8,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH3""",
    longDesc = u"""""",
)

entry(
    index = 50,
    label = "CH3CC",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u1 p0 c0 {2,T}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2095.25,'J/mol'),
        sigma = (4.76,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH3CC""",
    longDesc = u"""""",
)

entry(
    index = 51,
    label = "CH3CCCH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 C u1 p0 c0 {3,S} {8,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2968.28,'J/mol'),
        sigma = (5.18,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH3CCCH2""",
    longDesc = u"""""",
)

entry(
    index = 52,
    label = "CH3CCCH3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,T}
3  C u0 p0 c0 {2,T} {4,S}
4  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2968.28,'J/mol'),
        sigma = (5.18,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH3CCCH3""",
    longDesc = u"""""",
)

entry(
    index = 53,
    label = "CH3CCH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2161.77,'J/mol'),
        sigma = (4.85,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH3CCH2""",
    longDesc = u"""""",
)

entry(
    index = 54,
    label = "CH3CHCH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u1 p0 c0 {2,D} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2161.77,'J/mol'),
        sigma = (4.85,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH3CHCH""",
    longDesc = u"""""",
)

entry(
    index = 55,
    label = "CH3CH2CCH",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,T}
4  C u0 p0 c0 {3,T} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2968.28,'J/mol'),
        sigma = (5.18,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH3CH2CCH""",
    longDesc = u"""""",
)

entry(
    index = 56,
    label = "CH3CHO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 C u0 p0 c0 {1,S} {6,S} {7,D}
6 H u0 p0 c0 {5,S}
7 O u0 p2 c0 {5,D}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (3625.12,'J/mol'),
        sigma = (3.97,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 2.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH3CHO""",
    longDesc = u"""""",
)

entry(
    index = 57,
    label = "CH2CHO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (3625.12,'J/mol'),
        sigma = (3.97,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 2.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2CHO""",
    longDesc = u"""""",
)

entry(
    index = 58,
    label = "CH3CO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (3625.12,'J/mol'),
        sigma = (3.97,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 2.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH3CO""",
    longDesc = u"""""",
)

entry(
    index = 59,
    label = "CH3O",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (3467.15,'J/mol'),
        sigma = (3.69,'angstroms'),
        dipoleMoment = (1.7,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 2.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH3O""",
    longDesc = u"""""",
)

entry(
    index = 60,
    label = "CH3OH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (4005.93,'J/mol'),
        sigma = (3.626,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH3OH""",
    longDesc = u"""""",
)

entry(
    index = 61,
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
        dipoleMoment = (0,'C*m'),
        polarizability = (2.6,'angstroms^3'),
        rotrelaxcollnum = 13.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH4""",
    longDesc = u"""""",
)

entry(
    index = 66,
    label = "CO",
    molecule = 
"""
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (815.652,'J/mol'),
        sigma = (3.65,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (1.95,'angstroms^3'),
        rotrelaxcollnum = 1.8,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CO""",
    longDesc = u"""""",
)

entry(
    index = 67,
    label = "CO2",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (2028.74,'J/mol'),
        sigma = (3.763,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (2.65,'angstroms^3'),
        rotrelaxcollnum = 2.1,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CO2""",
    longDesc = u"""""",
)

entry(
    index = 68,
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
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for H""",
    longDesc = u"""""",
)

entry(
    index = 70,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (315.951,'J/mol'),
        sigma = (2.92,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0.79,'angstroms^3'),
        rotrelaxcollnum = 280.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for H2""",
    longDesc = u"""""",
)

entry(
    index = 71,
    label = "H2CCCCH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {4,D}
4 C u1 p0 c0 {3,D} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2968.28,'J/mol'),
        sigma = (5.18,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for H2CCCCH""",
    longDesc = u"""""",
)

entry(
    index = 72,
    label = "H2CCCCH2",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u0 p0 c0 {2,D} {4,D}
4 C u0 p0 c0 {3,D} {7,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2968.28,'J/mol'),
        sigma = (5.18,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for H2CCCCH2""",
    longDesc = u"""""",
)

entry(
    index = 73,
    label = "H2CCCH",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2095.25,'J/mol'),
        sigma = (4.76,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for H2CCCH""",
    longDesc = u"""""",
)

entry(
    index = 74,
    label = "H2CN",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 N u1 p1 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (4730.95,'J/mol'),
        sigma = (3.63,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for H2CN""",
    longDesc = u"""""",
)

entry(
    index = 75,
    label = "H2NO",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (970.302,'J/mol'),
        sigma = (3.492,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for H2NO""",
    longDesc = u"""""",
)

entry(
    index = 76,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (4759.22,'J/mol'),
        sigma = (2.605,'angstroms'),
        dipoleMoment = (1.844,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 4.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for H2O""",
    longDesc = u"""""",
)

entry(
    index = 77,
    label = "H2O2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (892.977,'J/mol'),
        sigma = (3.458,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 3.8,
    ),
    shortDesc = u"""GRI-Mech3.0 value for H2O2""",
    longDesc = u"""""",
)

entry(
    index = 78,
    label = "HC2N2",
    molecule = 
"""
multiplicity 2
1 H u0 p0 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 N u0 p1 c0 {3,S} {5,D}
5 N u1 p1 c0 {4,D}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (2901.76,'J/mol'),
        sigma = (4.361,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HC2N2""",
    longDesc = u"""""",
)

entry(
    index = 79,
    label = "HCCHCCH",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (2968.28,'J/mol'),
        sigma = (5.18,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HCCHCCH""",
    longDesc = u"""""",
)

entry(
    index = 80,
    label = "HCCO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {4,S}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1247.18,'J/mol'),
        sigma = (2.5,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HCCO""",
    longDesc = u"""""",
)

entry(
    index = 81,
    label = "HCNN",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {4,S}
2 N u0 p0 c+1 {1,T} {3,S}
3 N u1 p2 c-1 {2,S}
4 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1247.18,'J/mol'),
        sigma = (2.5,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HCNN""",
    longDesc = u"""""",
)

entry(
    index = 82,
    label = "HCCOH",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {4,S}
2 C u0 p0 c0 {1,T} {3,S}
3 O u0 p2 c0 {2,S} {5,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (3625.12,'J/mol'),
        sigma = (3.97,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 2.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HCCOH""",
    longDesc = u"""""",
)

entry(
    index = 83,
    label = "HCN",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 N u0 p1 c0 {2,T}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (4730.95,'J/mol'),
        sigma = (3.63,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HCN""",
    longDesc = u"""""",
)

entry(
    index = 84,
    label = "HCO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (4140.62,'J/mol'),
        sigma = (3.59,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HCO""",
    longDesc = u"""""",
)

entry(
    index = 86,
    label = "HCNO",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 N u0 p0 c+1 {2,T} {4,S}
4 O u0 p3 c-1 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1932.29,'J/mol'),
        sigma = (3.828,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HCNO""",
    longDesc = u"""""",
)

entry(
    index = 87,
    label = "HOCN",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 N u0 p1 c0 {3,T}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1932.29,'J/mol'),
        sigma = (3.828,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HOCN""",
    longDesc = u"""""",
)

entry(
    index = 88,
    label = "HNCO",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 N u0 p1 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,D}
4 O u0 p2 c0 {3,D}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1932.29,'J/mol'),
        sigma = (3.828,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HNCO""",
    longDesc = u"""""",
)

entry(
    index = 89,
    label = "HNNO",
    molecule = 
"""
multiplicity 2
1 H u0 p0 c0 {2,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {2,D} {4,S}
4 O u1 p2 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1932.29,'J/mol'),
        sigma = (3.828,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HNNO""",
    longDesc = u"""""",
)

entry(
    index = 90,
    label = "HNO",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 N u0 p1 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (970.302,'J/mol'),
        sigma = (3.492,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HNO""",
    longDesc = u"""""",
)

entry(
    index = 91,
    label = "HNOH",
    molecule = 
"""
multiplicity 2
1 H u0 p0 c0 {2,S}
2 N u1 p1 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 H u0 p0 c0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (970.302,'J/mol'),
        sigma = (3.492,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HNOH""",
    longDesc = u"""""",
)

entry(
    index = 92,
    label = "HO2",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (892.977,'J/mol'),
        sigma = (3.458,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HO2""",
    longDesc = u"""""",
)

entry(
    index = 93,
    label = "N(Q)",
    molecule = 
"""
multiplicity 4
1 N u3 p1 c0
""",
    transport = TransportData(
        shapeIndex = 0,
        epsilon = (593.655,'J/mol'),
        sigma = (3.298,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for N""",
    longDesc = u"""""",
)

entry(
    index = 94,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (810.913,'J/mol'),
        sigma = (3.621,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (1.76,'angstroms^3'),
        rotrelaxcollnum = 4.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for N2""",
    longDesc = u"""""",
)

entry(
    index = 95,
    label = "N2H2",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (593.655,'J/mol'),
        sigma = (3.798,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for N2H2""",
    longDesc = u"""""",
)

entry(
    index = 96,
    label = "N2H3",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u1 p1 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1662.9,'J/mol'),
        sigma = (3.9,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for N2H3""",
    longDesc = u"""""",
)

entry(
    index = 97,
    label = "N2H4",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1704.47,'J/mol'),
        sigma = (4.23,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (4.26,'angstroms^3'),
        rotrelaxcollnum = 1.5,
    ),
    shortDesc = u"""GRI-Mech3.0 value for N2H4""",
    longDesc = u"""""",
)

entry(
    index = 98,
    label = "N2O",
    molecule = 
"""
1 N u0 p2 c-1 {2,D}
2 N u0 p0 c+1 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (1932.29,'J/mol'),
        sigma = (3.828,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for N2O""",
    longDesc = u"""""",
)

entry(
    index = 99,
    label = "NCN",
    molecule = 
"""
multiplicity 3
1 N u1 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 N u1 p1 c0 {2,D}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (1932.29,'J/mol'),
        sigma = (3.828,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for NCN""",
    longDesc = u"""""",
)

entry(
    index = 100,
    label = "NCO",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 O u1 p2 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (1932.29,'J/mol'),
        sigma = (3.828,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for NCO""",
    longDesc = u"""""",
)

entry(
    index = 101,
    label = "NH(T)",
    molecule = 
"""
multiplicity 3
1 N u2 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (665.16,'J/mol'),
        sigma = (2.65,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 4.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for NH""",
    longDesc = u"""""",
)

entry(
    index = 102,
    label = "NH2",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (665.16,'J/mol'),
        sigma = (2.65,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (2.26,'angstroms^3'),
        rotrelaxcollnum = 4.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for NH2""",
    longDesc = u"""""",
)

entry(
    index = 103,
    label = "NH3",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (3999.27,'J/mol'),
        sigma = (2.92,'angstroms'),
        dipoleMoment = (1.47,'De'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 10.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for NH3""",
    longDesc = u"""""",
)

entry(
    index = 104,
    label = "NNH",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (593.655,'J/mol'),
        sigma = (3.798,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for NNH""",
    longDesc = u"""""",
)

entry(
    index = 105,
    label = "NO",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (810.913,'J/mol'),
        sigma = (3.621,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (1.76,'angstroms^3'),
        rotrelaxcollnum = 4.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for NO""",
    longDesc = u"""""",
)

entry(
    index = 106,
    label = "NCNO",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 N u0 p1 c0 {2,S} {4,D}
4 O u0 p2 c0 {3,D}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1932.29,'J/mol'),
        sigma = (3.828,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for NCNO""",
    longDesc = u"""""",
)

entry(
    index = 107,
    label = "NO2",
    molecule = 
"""
multiplicity 2
1 N u1 p0 c+1 {2,S} {3,D}
2 O u0 p3 c-1 {1,S}
3 O u0 p2 c0 {1,D}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1662.9,'J/mol'),
        sigma = (3.5,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 1.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for NO2""",
    longDesc = u"""""",
)

entry(
    index = 108,
    label = "O(T)",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    transport = TransportData(
        shapeIndex = 0,
        epsilon = (665.16,'J/mol'),
        sigma = (2.75,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for O""",
    longDesc = u"""""",
)

entry(
    index = 109,
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (892.977,'J/mol'),
        sigma = (3.458,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (1.6,'angstroms^3'),
        rotrelaxcollnum = 3.8,
    ),
    shortDesc = u"""GRI-Mech3.0 value for O2""",
    longDesc = u"""""",
)

entry(
    index = 110,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (665.16,'J/mol'),
        sigma = (2.75,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""GRI-Mech3.0 value for OH""",
    longDesc = u"""""",
)

