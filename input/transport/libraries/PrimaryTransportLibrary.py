#!/usr/bin/env python
# encoding: utf-8

name = "primaryTransportLibrary"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (496.376,'J/mol'),
        sigma = (2.8327,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""library value for H2""",
    longDesc = u"""""",
)

entry(
    index = 2,
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (887.157,'J/mol'),
        sigma = (3.467,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""library value for O2""",
    longDesc = u"""""",
)

entry(
    index = 3,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (6727.26,'J/mol'),
        sigma = (2.641,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (1.76,'angstroms^3'),
        rotrelaxcollnum = 4.0,
    ),
    shortDesc = u"""library value for H2O""",
    longDesc = u"""""",
)

entry(
    index = 4,
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
        epsilon = (2405.38,'J/mol'),
        sigma = (4.196,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""library value for H2O2""",
    longDesc = u"""""",
)

entry(
    index = 5,
    label = "CO2",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (1622.99,'J/mol'),
        sigma = (3.941,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""library value for CO2""",
    longDesc = u"""""",
)

entry(
    index = 6,
    label = "CO",
    molecule = 
"""
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = (762.44,'J/mol'),
        sigma = (3.69,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (1.76,'angstroms^3'),
        rotrelaxcollnum = 4.0,
    ),
    shortDesc = u"""library value for CO""",
    longDesc = u"""""",
)

entry(
    index = 7,
    label = "H2S",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = (1837.5,'J/mol'),
        sigma = (3.73,'angstroms'),
        dipoleMoment = (0,'C*m'),
        polarizability = (0,'angstroms^3'),
        rotrelaxcollnum = 0.0,
    ),
    shortDesc = u"""library value for H2S""",
    longDesc = u"""""",
)

entry(
    index = 8,
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
    index = 9,
    label = "C(S)",
    molecule = 
"""
1 C u0 p2 c0
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
    index = 10,
    label = "NH(S)",
    molecule = 
"""
1 N u0 p2 c0 {2,S}
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
    index = 11,
    label = "N(D)",
    molecule = 
"""
multiplicity 2
1 N u1 p2 c0
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

