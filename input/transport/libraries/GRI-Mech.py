#!/usr/bin/env python
# encoding: utf-8



entry(
    index = 1,
    label = "AR",
    molecule =
"""
1 Ar 0 4
""",
    transport = TransportData(
        shapeIndex = 0,
        epsilon = (136.500 * 8.3145, 'J/mol'),
        sigma = (3.330, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 0.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for AR""",
    longDesc = 
u"""

""",
)


entry(
    index = 2,
    label = "C(T)",
    molecule =
"""
1 C 4T 0
""",
    transport = TransportData(
        shapeIndex = 0,
        epsilon = (71.400 * 8.3145, 'J/mol'),
        sigma = (3.298, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 0.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "C2",
    molecule =
"""
1 C 1 0 {2,T}
2 C 1 0 {1,T}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (97.530 * 8.3145, 'J/mol'),
        sigma = (3.621, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (1.760, 'angstroms^3'),
        rotrelaxcollnum = 4.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C2""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "C2O",
    molecule =
"""
1 C 2 0 {2,D}
2 C 0 0 {1,D} {3,D}
3 O 0 2 {2,D}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (232.400 * 8.3145, 'J/mol'),
        sigma = (3.828, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C2O""",
    longDesc = 
u"""

""",
)

'''
entry(
    index = 5,
    label = "CN2",
    molecule =
"""

""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (232.400 * 8.3145, 'J/mol'),
        sigma = (3.828, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CN2""",
    longDesc = 
u"""

""",
)
'''

entry(
    index = 6,
    label = "C2H",
    molecule =
"""
1 H 0 0 {2,S}
2 C 0 0 {1,S} {3,T}
3 C 1 0 {2,T}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (209.000 * 8.3145, 'J/mol'),
        sigma = (4.100, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 2.500,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C2H""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "C2H2",
    molecule =
"""
1 H 0 0 {2,S}
2 C 0 0 {1,S} {3,T}
3 C 0 0 {2,T} {4,S}
4 H 0 0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (209.000 * 8.3145, 'J/mol'),
        sigma = (4.100, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 2.500,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C2H2""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "C2H2OH",
    molecule =
"""
1 C 1 0 {2,D} {4,S}
2 C 0 0 {1,D} {3,S} {5,S}
3 O 0 2 {2,S} {6,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (224.700 * 8.3145, 'J/mol'),
        sigma = (4.162, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C2H2OH""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "C2H3",
    molecule =
"""
1 H 0 0 {2,S}
2 C 1 0 {1,S} {3,D}
3 C 0 0 {2,D} {4,S} {5,S}
4 H 0 0 {3,S}
5 H 0 0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (209.000 * 8.3145, 'J/mol'),
        sigma = (4.100, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C2H3""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "C2H4",
    molecule =
"""
1 H 0 0 {3,S}
2 H 0 0 {3,S}
3 C 0 0 {1,S} {2,S} {4,D}
4 C 0 0 {3,D} {5,S} {6,S}
5 H 0 0 {4,S}
6 H 0 0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (280.800 * 8.3145, 'J/mol'),
        sigma = (3.971, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.500,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C2H4""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "C2H5",
    molecule =
"""
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 C 0 0 {1,S} {5,S} {6,S} {7,S}
5 H 0 0 {4,S}
6 H 0 0 {4,S}
7 H 0 0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (252.300 * 8.3145, 'J/mol'),
        sigma = (4.302, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.500,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C2H5""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "C2H6",
    molecule =
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 C 0 0 {1,S} {6,S} {7,S} {8,S}
6 H 0 0 {5,S}
7 H 0 0 {5,S}
8 H 0 0 {5,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (252.300 * 8.3145, 'J/mol'),
        sigma = (4.302, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.500,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C2H6""",
    longDesc = 
u"""

""",
)

'''
entry(
    index = 13,
    label = "C2N",
    molecule =
"""

""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (232.400 * 8.3145, 'J/mol'),
        sigma = (3.828, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C2N""",
    longDesc = 
u"""

""",
)
'''


entry(
    index = 14,
    label = "C2N2",
    molecule =
"""
1 N 0 1 {2,T}
2 C 0 0 {1,T} {3,S}
3 C 0 0 {2,S} {4,T}
4 N 0 1 {3,T}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (349.000 * 8.3145, 'J/mol'),
        sigma = (4.361, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C2N2""",
    longDesc = 
u"""

""",
)


entry(
    index = 15,
    label = "C3H2",
    molecule =
"""
1 C 1 0 {2,D} {4,S}
2 C 0 0 {1,D} {3,D}
3 C 1 0 {2,D} {5,S}
4 H 0 0 {1,S}
5 H 0 0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (209.000 * 8.3145, 'J/mol'),
        sigma = (4.100, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C3H2""",
    longDesc = 
u"""

""",
)


entry(
    index = 16,
    label = "C3H4",
    molecule =
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 0 {1,S} {3,D} {6,S}
3 C 0 0 {1,S} {2,D} {7,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (252.000 * 8.3145, 'J/mol'),
        sigma = (4.760, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for 'C3H4'; cyclic structure guessed""",
    longDesc = 
u"""

""",
)


entry(
    index = 17,
    label = "C3H6",
    molecule =
"""
1 C 0 0 {2,D} {4,S} {5,S}
2 C 0 0 {1,D} {3,S} {6,S}
3 C 0 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {3,S}
8 H 0 0 {3,S}
9 H 0 0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (266.800 * 8.3145, 'J/mol'),
        sigma = (4.982, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C3H6""",
    longDesc = 
u"""

""",
)

'''
entry(
    index = 18,
    label = "C3H7",
    molecule =
"""
1  C 0 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 0 {1,S} {3,S} {7,S}
3  C 0 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 0 {1,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {3,S}

""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (266.800 * 8.3145, 'J/mol'),
        sigma = (4.982, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for BOTH C3H7""",
    longDesc = 
u"""

""",
)
'''


entry(
    index = 19,
    label = "C4H6",
    molecule =
"""
1  C 0 0 {2,D} {5,S} {6,S}
2  C 0 0 {1,D} {3,S} {7,S}
3  C 0 0 {2,S} {4,D} {8,S}
4  C 0 0 {3,D} {9,S} {10,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {3,S}
9  H 0 0 {4,S}
10 H 0 0 {4,S}

""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (357.000 * 8.3145, 'J/mol'),
        sigma = (5.180, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C4H6""",
    longDesc = 
u"""

""",
)


entry(
    index = 20,
    label = "I*C3H7",
    molecule =
"""
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 0 {1,S} {3,S} {7,S}
3 C 0 0 {2,S} {8,S} {9,S} {10,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
9 H 0 0 {3,S}
10 H 0 0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (266.800 * 8.3145, 'J/mol'),
        sigma = (4.982, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for I*C3H7""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "N*C3H7",
    molecule =
"""
1 C 1 0 {2,S} {4,S} {5,S}
2 C 0 0 {1,S} {3,S} {6,S} {7,S}
3 C 0 0 {2,S} {8,S} {9,S} {10,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
9 H 0 0 {3,S}
10 H 0 0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (266.800 * 8.3145, 'J/mol'),
        sigma = (4.982, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for N*C3H7""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "C3H8",
    molecule =
"""
1  C 0 0 {2,S} {3,S} {4,S} {5,S}
2  H 0 0 {1,S}
3  H 0 0 {1,S}
4  H 0 0 {1,S}
5  C 0 0 {1,S} {6,S} {7,S} {8,S}
6  H 0 0 {5,S}
7  H 0 0 {5,S}
8  C 0 0 {5,S} {9,S} {10,S} {11,S}
9  H 0 0 {8,S}
10 H 0 0 {8,S}
11 H 0 0 {8,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (266.800 * 8.3145, 'J/mol'),
        sigma = (4.982, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C3H8""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "C4H",
    molecule =
"""
1 C 1 0 {2,T}
2 C 0 0 {1,T} {3,S}
3 C 0 0 {2,S} {4,T}
4 C 0 0 {3,T} {5,S}
5 H 0 0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (357.000 * 8.3145, 'J/mol'),
        sigma = (5.180, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C4H""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "C4H2",
    molecule =
"""
1 C 0 0 {2,T} {5,S}
2 C 0 0 {1,T} {3,S}
3 C 0 0 {2,S} {4,T}
4 C 0 0 {3,T} {6,S}
5 H 0 0 {1,S}
6 H 0 0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (357.000 * 8.3145, 'J/mol'),
        sigma = (5.180, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C4H2""",
    longDesc = 
u"""

""",
)

'''
entry(
    index = 25,
    label = "C4H2OH",
    molecule =
"""

""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (224.700 * 8.3145, 'J/mol'),
        sigma = (4.162, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C4H2OH""",
    longDesc = 
u"""

""",
)
'''


entry(
    index = 26,
    label = "C4H8",
    molecule =
"""
1  C 0 0 {2,D} {5,S} {6,S}
2  C 0 0 {1,D} {3,S} {7,S}
3  C 0 0 {2,S} {4,S} {8,S} {9,S}
4  C 0 0 {3,S} {10,S} {11,S} {12,S}
5  H 0 0 {1,S}
6  H 0 0 {1,S}
7  H 0 0 {2,S}
8  H 0 0 {3,S}
9  H 0 0 {3,S}
10 H 0 0 {4,S}
11 H 0 0 {4,S}
12 H 0 0 {4,S}

""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (357.000 * 8.3145, 'J/mol'),
        sigma = (5.176, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for 'C4H8'. 1-butune structure guessed""",
    longDesc = 
u"""

""",
)


entry(
    index = 27,
    label = "C4H9",
    molecule =
"""
1 C 1 0 {2,S} {5,S} {6,S}
2 C 0 0 {1,S} {3,S} {7,S} {8,S}
3 C 0 0 {2,S} {4,S} {9,S} {10,S}
4 C 0 0 {3,S} {11,S} {12,S} {13,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
9 H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (357.000 * 8.3145, 'J/mol'),
        sigma = (5.176, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C4H9""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "I*C4H9",
    molecule =
"""
1 C 0 0 {2,S} {5,S} {6,S} {7,S}
2 C 1 0 {1,S} {3,S} {8,S}
3 C 0 0 {2,S} {4,S} {9,S} {10,S}
4 C 0 0 {3,S} {11,S} {12,S} {13,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {2,S}
9 H 0 0 {3,S}
10 H 0 0 {3,S}
11 H 0 0 {4,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (357.000 * 8.3145, 'J/mol'),
        sigma = (5.176, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for I*C4H9""",
    longDesc = 
u"""

""",
)

'''
entry(
    index = 29,
    label = "C5H2",
    molecule =
"""

""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (357.000 * 8.3145, 'J/mol'),
        sigma = (5.180, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C5H2""",
    longDesc = 
u"""

""",
)
'''

'''
entry(
    index = 30,
    label = "C5H3",
    molecule =
"""

""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (357.000 * 8.3145, 'J/mol'),
        sigma = (5.180, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C5H3""",
    longDesc = 
u"""

""",
)
'''

'''
entry(
    index = 31,
    label = "C6H2",
    molecule =
"""

""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (357.000 * 8.3145, 'J/mol'),
        sigma = (5.180, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C6H2""",
    longDesc = 
u"""

""",
)
'''

'''
entry(
    index = 32,
    label = "C6H5",
    molecule =
"""

""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (412.300 * 8.3145, 'J/mol'),
        sigma = (5.349, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C6H5""",
    longDesc = 
u"""

""",
)
'''

'''
entry(
    index = 33,
    label = "C6H5O",
    molecule =
"""

""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (450.000 * 8.3145, 'J/mol'),
        sigma = (5.500, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C6H5O""",
    longDesc = 
u"""

""",
)
'''

'''
entry(
    index = 34,
    label = "C5H5OH",
    molecule =
"""

""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (450.000 * 8.3145, 'J/mol'),
        sigma = (5.500, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C5H5OH""",
    longDesc = 
u"""

""",
)
'''

'''
entry(
    index = 35,
    label = "C6H6",
    molecule =
"""

""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (412.300 * 8.3145, 'J/mol'),
        sigma = (5.349, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C6H6""",
    longDesc = 
u"""

""",
)
'''

'''
entry(
    index = 36,
    label = "C6H7",
    molecule =
"""

""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (412.300 * 8.3145, 'J/mol'),
        sigma = (5.349, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for C6H7""",
    longDesc = 
u"""

""",
)
'''

entry(
    index = 37,
    label = "CH(D)",
    molecule =
"""
1 C 3D 0 {2,S}
2 H 0  0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (80.000 * 8.3145, 'J/mol'),
        sigma = (2.750, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 0.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "CH2",
    molecule =
"""
1 C 2T 0 {2,S} {3,S}
2 H 0  0 {1,S}
3 H 0  0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (144.000 * 8.3145, 'J/mol'),
        sigma = (3.800, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 0.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "CH2(S)",
    molecule =
"""
1 C 2S 0 {2,S} {3,S}
2 H 0  0 {1,S}
3 H 0  0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (144.000 * 8.3145, 'J/mol'),
        sigma = (3.800, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 0.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2(S)""",
    longDesc = 
u"""

""",
)

'''
entry(
    index = 40,
    label = "CH2*",
    molecule =
"""

""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (144.000 * 8.3145, 'J/mol'),
        sigma = (3.800, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 0.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2*""",
    longDesc = 
u"""

""",
)
'''

entry(
    index = 41,
    label = "CH2CHCCH",
    molecule =
"""
1 C 0 0 {2,D} {5,S} {6,S}
2 C 0 0 {1,D} {3,S} {7,S}
3 C 0 0 {2,S} {4,T}
4 C 0 0 {3,T} {8,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (357.000 * 8.3145, 'J/mol'),
        sigma = (5.180, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2CHCCH""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "CH2CHCCH2",
    molecule =
"""
1 C 0 0 {2,D} {5,S} {6,S}
2 C 0 0 {1,D} {3,S} {7,S}
3 C 1 0 {2,S} {4,D}
4 C 0 0 {3,D} {8,S} {9,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {4,S}
9 H 0 0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (357.000 * 8.3145, 'J/mol'),
        sigma = (5.180, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2CHCCH2""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "CH2CHCH2",
    molecule =
"""
1 C 1 0 {2,S} {4,S} {5,S}
2 C 0 0 {1,S} {3,D} {6,S}
3 C 0 0 {2,D} {7,S} {8,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {3,S}
8 H 0 0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (260.000 * 8.3145, 'J/mol'),
        sigma = (4.850, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2CHCH2""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "CH2CHCHCH",
    molecule =
"""
1 C 0 0 {2,D} {5,S} {6,S}
2 C 0 0 {1,D} {3,S} {7,S}
3 C 0 0 {2,S} {4,D} {8,S}
4 C 1 0 {3,D} {9,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
9 H 0 0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (357.000 * 8.3145, 'J/mol'),
        sigma = (5.180, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2CHCHCH""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "CH2CHCHCH2",
    molecule =
"""
1 C 0 0 {2,D} {5,S} {6,S}
2 C 0 0 {1,D} {3,S} {7,S}
3 C 0 0 {2,S} {4,D} {8,S}
4 C 0 0 {3,D} {9,S} {10,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
9 H 0 0 {4,S}
10 H 0 0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (357.000 * 8.3145, 'J/mol'),
        sigma = (5.180, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2CHCHCH2""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "CH2CO",
    molecule =
"""
1 C 0 0 {2,S} {3,S} {4,D}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 C 0 0 {1,D} {5,D}
5 O 0 2 {4,D}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (436.000 * 8.3145, 'J/mol'),
        sigma = (3.970, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 2.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2CO""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "CH2O",
    molecule =
"""
1 C 0 0 {2,S} {3,S} {4,D}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 O 0 2 {1,D}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (498.000 * 8.3145, 'J/mol'),
        sigma = (3.590, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 2.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2O""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "CH2OH",
    molecule =
"""
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 O 0 2 {1,S} {5,S}
5 H 0 0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (417.000 * 8.3145, 'J/mol'),
        sigma = (3.690, 'angstroms'),
        dipoleMoment = (1.700, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 2.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2OH""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "CH3",
    molecule =
"""
1 C 1 0 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (144.000 * 8.3145, 'J/mol'),
        sigma = (3.800, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 0.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH3""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "CH3CC",
    molecule =
"""
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 0 {1,S} {3,T}
3 C 1 0 {2,T}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (252.000 * 8.3145, 'J/mol'),
        sigma = (4.760, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH3CC""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "CH3CCCH2",
    molecule =
"""
1 C 0 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 0 {1,S} {3,T}
3 C 0 0 {2,T} {4,S}
4 C 1 0 {3,S} {8,S} {9,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {4,S}
9 H 0 0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (357.000 * 8.3145, 'J/mol'),
        sigma = (5.180, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH3CCCH2""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "CH3CCCH3",
    molecule =
"""
1 C 0 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 0 {1,S} {3,T}
3 C 0 0 {2,T} {4,S}
4 C 0 0 {3,S} {8,S} {9,S} {10,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {4,S}
9 H 0 0 {4,S}
10 H 0 0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (357.000 * 8.3145, 'J/mol'),
        sigma = (5.180, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH3CCCH3""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "CH3CCH2",
    molecule =
"""
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 0 {1,S} {3,D}
3 C 0 0 {2,D} {7,S} {8,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {3,S}
8 H 0 0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (260.000 * 8.3145, 'J/mol'),
        sigma = (4.850, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH3CCH2""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "CH3CHCH",
    molecule =
"""
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 0 {1,S} {3,D} {7,S}
3 C 1 0 {2,D} {8,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (260.000 * 8.3145, 'J/mol'),
        sigma = (4.850, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH3CHCH""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "CH3CH2CCH",
    molecule =
"""
1 C 0 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 0 {1,S} {3,S} {8,S} {9,S}
3 C 0 0 {2,S} {4,T}
4 C 0 0 {3,T} {10,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {1,S}
8 H 0 0 {2,S}
9 H 0 0 {2,S}
10 H 0 0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (357.000 * 8.3145, 'J/mol'),
        sigma = (5.180, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH3CH2CCH""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "CH3CHO",
    molecule =
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 C 0 0 {1,S} {6,S} {7,D}
6 H 0 0 {5,S}
7 O 0 2 {5,D}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (436.000 * 8.3145, 'J/mol'),
        sigma = (3.970, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 2.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH3CHO""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "CH2CHO",
    molecule =
"""
1 C 1 0 {2,S} {4,S} {5,S}
2 C 0 0 {1,S} {3,D} {6,S}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (436.000 * 8.3145, 'J/mol'),
        sigma = (3.970, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 2.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH2CHO""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "CH3CO",
    molecule =
"""
1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 0 {1,S} {3,D}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (436.000 * 8.3145, 'J/mol'),
        sigma = (3.970, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 2.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH3CO""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "CH3O",
    molecule =
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (417.000 * 8.3145, 'J/mol'),
        sigma = (3.690, 'angstroms'),
        dipoleMoment = (1.700, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 2.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH3O""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "CH3OH",
    molecule =
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 2 {1,S} {6,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (481.800 * 8.3145, 'J/mol'),
        sigma = (3.626, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH3OH""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "CH4",
    molecule =
"""
1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (141.400 * 8.3145, 'J/mol'),
        sigma = (3.746, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (2.600, 'angstroms^3'),
        rotrelaxcollnum = 13.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH4""",
    longDesc = 
u"""

""",
)

'''
entry(
    index = 62,
    label = "CH4O",
    molecule =
"""

""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (417.000 * 8.3145, 'J/mol'),
        sigma = (3.690, 'angstroms'),
        dipoleMoment = (1.700, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 2.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CH4O""",
    longDesc = 
u"""

""",
)
'''

entry(
    index = 63,
    label = "CN",
    molecule =
"""
1 C 1 0 {2,T}
2 N 0 0 {1,T}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (75.000 * 8.3145, 'J/mol'),
        sigma = (3.856, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CN""",
    longDesc = 
u"""

""",
)

'''
entry(
    index = 64,
    label = "CNC",
    molecule =
"""

""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (232.400 * 8.3145, 'J/mol'),
        sigma = (3.828, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CNC""",
    longDesc = 
u"""

""",
)
'''

'''
entry(
    index = 65,
    label = "CNN",
    molecule =
"""

""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (232.400 * 8.3145, 'J/mol'),
        sigma = (3.828, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CNN""",
    longDesc = 
u"""

""",
)
'''

entry(
    index = 66,
    label = "CO",
    molecule =
"""
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (98.100 * 8.3145, 'J/mol'),
        sigma = (3.650, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (1.950, 'angstroms^3'),
        rotrelaxcollnum = 1.800,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CO""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "CO2",
    molecule =
"""
1 C 0 0 {2,D} {3,D}
2 O 0 2 {1,D}
3 O 0 2 {1,D}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (244.000 * 8.3145, 'J/mol'),
        sigma = (3.763, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (2.650, 'angstroms^3'),
        rotrelaxcollnum = 2.100,
    ),
    shortDesc = u"""GRI-Mech3.0 value for CO2""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "H",
    molecule =
"""
1 H 1 0
""",
    transport = TransportData(
        shapeIndex = 0,
        epsilon = (145.000 * 8.3145, 'J/mol'),
        sigma = (2.050, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 0.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for H""",
    longDesc = 
u"""

""",
)

'''
entry(
    index = 69,
    label = "H2C4O",
    molecule =
"""

""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (357.000 * 8.3145, 'J/mol'),
        sigma = (5.180, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for H2C4O""",
    longDesc = 
u"""

""",
)
'''

entry(
    index = 70,
    label = "H2",
    molecule =
"""
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (38.000 * 8.3145, 'J/mol'),
        sigma = (2.920, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.790, 'angstroms^3'),
        rotrelaxcollnum = 280.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for H2""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "H2CCCCH",
    molecule =
"""
1 C 1 0 {2,S} {5,S} {6,S}
2 C 0 0 {1,S} {3,S}
3 C 0 0 {2,S} {4,T}
4 C 0 0 {3,T} {7,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (357.000 * 8.3145, 'J/mol'),
        sigma = (5.180, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for H2CCCCH""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "H2CCCCH2",
    molecule =
"""
1 C 0 0 {2,D} {4,S} {5,S}
2 C 0 0 {1,D} {3,D}
3 C 0 0 {2,D} {6,S} {7,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {3,S}
7 H 0 0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (357.000 * 8.3145, 'J/mol'),
        sigma = (5.180, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for H2CCCCH2""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "H2CCCH",
    molecule =
"""
1 C 1 0 {2,S} {4,S} {5,S}
2 C 0 0 {1,S} {3,T}
3 C 0 0 {2,T} {6,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (252.000 * 8.3145, 'J/mol'),
        sigma = (4.760, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for H2CCCH""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "H2CN",
    molecule =
"""
1 C 0 0 {2,D} {3,S} {4,S}
2 N 1 1 {1,D}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (569.000 * 8.3145, 'J/mol'),
        sigma = (3.630, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for H2CN""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "H2NO",
    molecule =
"""
1 N 0 1 {2,S} {3,S} {4,S}
2 O 1 2 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (116.700 * 8.3145, 'J/mol'),
        sigma = (3.492, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for H2NO""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "H2O",
    molecule =
"""
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (572.400 * 8.3145, 'J/mol'),
        sigma = (2.605, 'angstroms'),
        dipoleMoment = (1.844, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 4.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for H2O""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "H2O2",
    molecule =
"""
1 H 0 0 {2,S}
2 O 0 2 {1,S} {3,S}
3 O 0 2 {2,S} {4,S}
4 H 0 0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (107.400 * 8.3145, 'J/mol'),
        sigma = (3.458, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 3.800,
    ),
    shortDesc = u"""GRI-Mech3.0 value for H2O2""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "HC2N2",
    molecule =
"""
1 H 0 0 {2,S}
2 C 0 0 {1,S} {3,T}
3 C 0 0 {2,T} {4,S}
4 N 0 1 {3,S} {5,D}
5 N 1 1 {4,D}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (349.000 * 8.3145, 'J/mol'),
        sigma = (4.361, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HC2N2""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "HCCHCCH",
    molecule =
"""
1 C 1 0 {2,D} {5,S}
2 C 0 0 {1,D} {3,S} {6,S}
3 C 0 0 {2,S} {4,T}
4 C 0 0 {3,T} {7,S}
5 H 0 0 {1,S}
6 H 0 0 {2,S}
7 H 0 0 {4,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (357.000 * 8.3145, 'J/mol'),
        sigma = (5.180, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HCCHCCH""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "HCCO",
    molecule =
"""
1 C 1 0 {2,D} {4,S}
2 C 0 0 {1,D} {3,D}
3 O 0 2 {2,D}
4 H 0 0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (150.000 * 8.3145, 'J/mol'),
        sigma = (2.500, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HCCO""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "HCNN",
    molecule =
"""
1 C 0 0 {2,T} {4,S}
2 N 0 0 {1,T} {3,S}
3 N 1 2 {2,S}
4 H 0 0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (150.000 * 8.3145, 'J/mol'),
        sigma = (2.500, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HCNN""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "HCCOH",
    molecule =
"""
1 C 0 0 {2,T} {4,S}
2 C 0 0 {1,T} {3,S}
3 O 0 2 {2,S} {5,S}
4 H 0 0 {1,S}
5 H 0 0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (436.000 * 8.3145, 'J/mol'),
        sigma = (3.970, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 2.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HCCOH""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "HCN",
    molecule =
"""
1 H 0 0 {2,S}
2 C 0 0 {1,S} {3,T}
3 N 0 1 {2,T}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (569.000 * 8.3145, 'J/mol'),
        sigma = (3.630, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HCN""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "HCO",
    molecule =
"""
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (498.000 * 8.3145, 'J/mol'),
        sigma = (3.590, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 0.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HCO""",
    longDesc = 
u"""

""",
)

'''
entry(
    index = 85,
    label = "HE",
    molecule =
"""

""",
    transport = TransportData(
        shapeIndex = 0,
        epsilon = (10.200 * 8.3145, 'J/mol'),
        sigma = (2.576, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 0.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HE""",
    longDesc = 
u"""

""",
)
'''

entry(
    index = 86,
    label = "HCNO",
    molecule =
"""
1 H 0 0 {2,S}
2 C 0 0 {1,S} {3,T}
3 N 0 0 {2,T} {4,S}
4 O 0 3 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (232.400 * 8.3145, 'J/mol'),
        sigma = (3.828, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HCNO""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "HOCN",
    molecule =
"""
1 H 0 0 {2,S}
2 O 0 2 {1,S} {3,S}
3 C 0 0 {2,S} {4,T}
4 N 0 1 {3,T}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (232.400 * 8.3145, 'J/mol'),
        sigma = (3.828, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HOCN""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "HNCO",
    molecule =
"""
1 H 0 0 {2,S}
2 N 0 1 {1,S} {3,D}
3 C 0 0 {2,D} {4,D}
4 O 0 2 {3,D}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (232.400 * 8.3145, 'J/mol'),
        sigma = (3.828, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HNCO""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "HNNO",
    molecule =
"""
1 H 0 0 {2,S}
2 N 0 1 {1,S} {3,D}
3 N 0 1 {2,D} {4,S}
4 O 1 2 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (232.400 * 8.3145, 'J/mol'),
        sigma = (3.828, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HNNO""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "HNO",
    molecule =
"""
1 H 0 0 {2,S}
2 N 0 1 {1,S} {3,D}
3 O 0 2 {2,D}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (116.700 * 8.3145, 'J/mol'),
        sigma = (3.492, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HNO""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "HNOH",
    molecule =
"""
1 H 0 0 {2,S}
2 N 1 1 {1,S} {3,S}
3 O 0 2 {2,S} {4,S}
4 H 0 0 {3,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (116.700 * 8.3145, 'J/mol'),
        sigma = (3.492, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HNOH""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "HO2",
    molecule =
"""
1 O 1 2 {2,S}
2 O 0 2 {1,S} {3,S}
3 H 0 0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (107.400 * 8.3145, 'J/mol'),
        sigma = (3.458, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for HO2""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "N(Q)",
    molecule =
"""
1 N 3Q 1 
""",
    transport = TransportData(
        shapeIndex = 0,
        epsilon = (71.400 * 8.3145, 'J/mol'),
        sigma = (3.298, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 0.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for N""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "N2",
    molecule =
"""
1 N 0 1 {2,T}
2 N 0 1 {1,T}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (97.530 * 8.3145, 'J/mol'),
        sigma = (3.621, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (1.760, 'angstroms^3'),
        rotrelaxcollnum = 4.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for N2""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "N2H2",
    molecule =
"""
1 N 0 1 {2,D} {3,S}
2 N 0 1 {1,D} {4,S}
3 H 0 0 {1,S}
4 H 0 0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (71.400 * 8.3145, 'J/mol'),
        sigma = (3.798, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for N2H2""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "N2H3",
    molecule =
"""
1 N 0 1 {2,S} {3,S} {4,S}
2 N 1 1 {1,S} {5,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (200.000 * 8.3145, 'J/mol'),
        sigma = (3.900, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for N2H3""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "N2H4",
    molecule =
"""
1 N 0 1 {2,S} {3,S} {4,S}
2 N 0 1 {1,S} {5,S} {6,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
6 H 0 0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (205.000 * 8.3145, 'J/mol'),
        sigma = (4.230, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (4.260, 'angstroms^3'),
        rotrelaxcollnum = 1.500,
    ),
    shortDesc = u"""GRI-Mech3.0 value for N2H4""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "N2O",
    molecule =
"""
1 N 0 2 {2,D}
2 N 0 0 {1,D} {3,D}
3 O 0 2 {2,D}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (232.400 * 8.3145, 'J/mol'),
        sigma = (3.828, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for N2O""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "NCN",
    molecule =
"""
1 N 1 1 {2,D}
2 C 0 0 {1,D} {3,D}
3 N 1 1 {2,D}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (232.400 * 8.3145, 'J/mol'),
        sigma = (3.828, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for NCN""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "NCO",
    molecule =
"""
1 N 0 1 {2,T}
2 C 0 0 {1,T} {3,S}
3 O 1 2 {2,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (232.400 * 8.3145, 'J/mol'),
        sigma = (3.828, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for NCO""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "NH(T)",
    molecule =
"""
1 N 2T 1 {2,S}
2 H 0  0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (80.000 * 8.3145, 'J/mol'),
        sigma = (2.650, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 4.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for NH""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "NH2",
    molecule =
"""
1 N 1 1 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (80.000 * 8.3145, 'J/mol'),
        sigma = (2.650, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (2.260, 'angstroms^3'),
        rotrelaxcollnum = 4.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for NH2""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "NH3",
    molecule =
"""
1 N 0 1 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (481.000 * 8.3145, 'J/mol'),
        sigma = (2.920, 'angstroms'),
        dipoleMoment = (1.470, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 10.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for NH3""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "NNH",
    molecule =
"""
1 N 1 1 {2,D}
2 N 0 1 {1,D} {3,S}
3 H 0 0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (71.400 * 8.3145, 'J/mol'),
        sigma = (3.798, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for NNH""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "NO",
    molecule =
"""
1 N 1 1 {2,D}
2 O 0 2 {1,D}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (97.530 * 8.3145, 'J/mol'),
        sigma = (3.621, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (1.760, 'angstroms^3'),
        rotrelaxcollnum = 4.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for NO""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "NCNO",
    molecule =
"""
1 N 0 1 {2,T}
2 C 0 0 {1,T} {3,S}
3 N 0 1 {2,S} {4,D}
4 O 0 2 {3,D}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (232.400 * 8.3145, 'J/mol'),
        sigma = (3.828, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for NCNO""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "NO2",
    molecule =
"""
1 N 1 0 {2,S} {3,D}
2 O 0 3 {1,S}
3 O 0 2 {1,D}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (200.000 * 8.3145, 'J/mol'),
        sigma = (3.500, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 1.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for NO2""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "O(T)",
    molecule =
"""
1 O 2T 2
""",
    transport = TransportData(
        shapeIndex = 0,
        epsilon = (80.000 * 8.3145, 'J/mol'),
        sigma = (2.750, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 0.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for O""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "O2",
    molecule =
"""
1 O 1 2 {2,S}
2 O 1 2 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (107.400 * 8.3145, 'J/mol'),
        sigma = (3.458, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (1.600, 'angstroms^3'),
        rotrelaxcollnum = 3.800,
    ),
    shortDesc = u"""GRI-Mech3.0 value for O2""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "OH",
    molecule =
"""
1 O 1 2 {2,S}
2 H 0 0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (80.000 * 8.3145, 'J/mol'),
        sigma = (2.750, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 0.000,
    ),
    shortDesc = u"""GRI-Mech3.0 value for OH""",
    longDesc = 
u"""

""",
)