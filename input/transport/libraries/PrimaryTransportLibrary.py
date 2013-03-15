#!/usr/bin/env python
# encoding: utf-8

name = "primaryTransportLibrary"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 1,
    label = "H2",
    molecule = 
"""
1 H 0 {2,S}
2 H 0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = 59.700,
        sigma = 2.8327,
        dipoleMoment = 0.000,
        polarizability = 0.000,
        rotrelaxcollnum = 0.000
    ),
    shortDesc = u"""library value for H2""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 25 2:00:00 2013","Jake Barlow <barlow.ja@husky.neu.edu>","action",""
        "Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "O2",
    molecule = 
"""
1 O 1 {2,S}
2 O 1 {1,S}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = 106.700,
        sigma = 3.467,
        dipoleMoment = 0.000,
        polarizability = 0.000,
        rotrelaxcollnum = 0.000
    ),
    shortDesc = u"""library value for O2""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 25 2:00:00 2013","Jake Barlow <barlow.ja@husky.neu.edu>","action",""
        "Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "H2O",
    molecule = 
"""
1 O 0
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = 809.100,
        sigma = 2.641,
        dipoleMoment = 0.000,
        polarizability = 1.760,
        rotrelaxcollnum = 4.000
    ),
    shortDesc = u"""library value for H2O""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 25 2:00:00 2013","Jake Barlow <barlow.ja@husky.neu.edu>","action",""
        "Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "H2O2",
    molecule = 
"""
1 O 0 {2,S}
2 O 0 {1,S}
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = 289.300,
        sigma = 4.196,
        dipoleMoment = 0.000,
        polarizability = 0.000,
        rotrelaxcollnum = 0.000 
    ),
    shortDesc = u"""library value for H2O2""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 25 2:00:00 2013","Jake Barlow <barlow.ja@husky.neu.edu>","action",""
        "Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    label = "CO2",
    molecule = 
"""
1 O 0 {2,D}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = 195.200,
        sigma = 3.941,
        dipoleMoment = 0.000,
        polarizability = 0.000,
        rotrelaxcollnum = 0.000 
    ),
    shortDesc = u"""library value for CO2""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 25 2:00:00 2013","Jake Barlow <barlow.ja@husky.neu.edu>","action",""
        "Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    label = "CO",
    molecule = 
"""
1 C 2T {2,D}
2 O 0 {1,D}
""",
    transport = TransportData(
        shapeIndex = 1,
        epsilon = 91.700,
        sigma = 3.690,
        dipoleMoment = 0.000,
        polarizability = 1.760,
        rotrelaxcollnum = 4.000 
    ),
    shortDesc = u"""library value for CO""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 25 2:00:00 2013","Jake Barlow <barlow.ja@husky.neu.edu>","action",""
        "Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    label = "H2S",
    molecule = 
"""
1 S 0
""",
    transport = TransportData(
        shapeIndex = 2,
        epsilon = 221.000,
        sigma = 3.730,
        dipoleMoment = 0.000,
        polarizability = 0.000,
        rotrelaxcollnum = 0.000 
    ),
    shortDesc = u"""library value for H2S""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 25 2:00:00 2013","Jake Barlow <barlow.ja@husky.neu.edu>","action",""
        "Jake Barlow <barlow.ja@husky.neu.edu> imported this entry from the old RMG database."""),
    ],
)
