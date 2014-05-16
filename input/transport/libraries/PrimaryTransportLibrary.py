#!/usr/bin/env python
# encoding: utf-8


name = "primaryTransportLibrary"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "H2",
    multiplicity = 1,
    molecule = 
"""
1 H U0 L0 {2,S}
2 H U0 L0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (59.700 * 8.3145, 'J/mol'),
        sigma = (2.8327, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 0.000
    ),
    shortDesc = u"""library value for H2""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "O2_(T)",
    multiplicity = 3,
    molecule = 
"""
1 O U1 L2 {2,S}
2 O U1 L2 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (106.700 * 8.3145, 'J/mol'),
        sigma = (3.467, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 0.000
    ),
    shortDesc = u"""library value for O2""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "H2O",
    multiplicity = 1,
    molecule = 
"""
1 O U0 L2 {2,S} {3,S}
2 H U0 L0 {1,S}
3 H U0 L0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (809.100 * 8.3145, 'J/mol'),
        sigma = (2.641, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (1.760, 'angstroms^3'),
        rotrelaxcollnum = 4.000
    ),
    shortDesc = u"""library value for H2O""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "H2O2",
    multiplicity = 1,
    molecule = 
"""
1 O U0 L2 {2,S} {3,S}
2 O U0 L2 {1,S} {4,S}
3 H U0 L0 {1,S}
4 H U0 L0 {2,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (289.300 * 8.3145, 'J/mol'),
        sigma = (4.196, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 0.000 
    ),
    shortDesc = u"""library value for H2O2""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "CO2",
    multiplicity = 1,
    molecule = 
"""
1 O U0 L2 {2,D}
2 C U0 L0 {1,D} {3,D}
3 O U0 L2 {2,D}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (195.200 * 8.3145, 'J/mol'),
        sigma = (3.941, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 0.000 
    ),
    shortDesc = u"""library value for CO2""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "CO",
    multiplicity = 1,
    molecule = 
"""
1 C U0 L1 {2,T}
2 O U0 L1 {1,T}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (91.700 * 8.3145, 'J/mol'),
        sigma = (3.690, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (1.760, 'angstroms^3'),
        rotrelaxcollnum = 4.000 
    ),
    shortDesc = u"""library value for CO""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "H2S",
    multiplicity = 1,
    molecule = 
"""
1 S U0 L2 {2,S} {3,S}
2 H U0 L0 {1,S}
3 H U0 L0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (221.000 * 8.3145, 'J/mol'),
        sigma = (3.730, 'angstroms'),
        dipoleMoment = (0.000, 'C*m'),
        polarizability = (0.000, 'angstroms^3'),
        rotrelaxcollnum = 0.000 
    ),
    shortDesc = u"""library value for H2S""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "N2",
    multiplicity = 1,
    molecule = 
"""
1 N U0 L1 {2,T}
2 N U0 L1 {1,T}
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
    index = 9,
    label = "C(S)",
    multiplicity = 1,
    molecule =
"""
1 C U4 L0
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
    index = 10,
    label = "NH(S)",
    multiplicity = 1,
    molecule =
"""
1 N U2 L1 {2,S}
2 H U0 L0 {1,S}
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
    index = 11,
    label = "N(D)",
    multiplicity = 2,
    molecule =
"""
1 N U3 L1
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