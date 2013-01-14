#!/usr/bin/env python
# encoding: utf-8

name = "Polycyclic Ring Corrections"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 0,
    label = "PolycyclicRing",
    group = 
"""
1 * R 0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 1,
    label = "bicyclo-(1.1.0)-butane",
    group = 
"""
1 * Cs 0 {2,S} {3,S} {4,S}
2   Cs 0 {1,S} {3,S} {4,S}
3   Cs 0 {1,S} {2,S}
4   Cs 0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.227,-2.849,-2.536,-2.35,-2.191,-2.111,-1.76],'cal/(mol*K)'),
        H298 = (57.0789,'kcal/mol'),
        S298 = (69.2967,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "bicyclo-(2.1.0)-pentane",
    group = 
"""
1 * Cs 0 {2,S} {3,S} {5,S}
2   Cs 0 {1,S} {3,S} {4,S}
3   Cs 0 {1,S} {2,S}
4   Cs 0 {2,S} {5,S}
5   Cs 0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.227,-2.849,-2.536,-2.35,-2.191,-2.111,-1.76],'cal/(mol*K)'),
        H298 = (55.378,'kcal/mol'),
        S298 = (64.7895,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    label = "spiropentane",
    group = 
"""
1 * Cs 0 {2,S} {3,S} {4,S} {5,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {1,S} {2,S}
4   Cs 0 {1,S} {5,S}
5   Cs 0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.227,-2.849,-2.536,-2.35,-2.191,-2.111,-1],'cal/(mol*K)'),
        H298 = (63.5885,'kcal/mol'),
        S298 = (67.6938,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    label = "Bicyclo[1.1.1]pentane",
    group = 
"""
1 * Cs 0 {3,S} {4,S} {5,S}
2   Cs 0 {3,S} {4,S} {5,S}
3   Cs 0 {1,S} {2,S}
4   Cs 0 {1,S} {2,S}
5   Cs 0 {1,S} {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.61,-3.89,-3.14,-2.64,-1.88,-1.38,-0.67],'cal/(mol*K)'),
        H298 = (68,'kcal/mol'),
        S298 = (29.8,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    label = "bicyclo[2.1.0]pent-1(4)-ene",
    group = 
"""
1 * C 0 {2,S} {5,S}
2   C 0 {1,S} {4,S}
3   C 0 {4,S} {5,S}
4   C 0 {2,S} {3,S} {5,D}
5   C 0 {1,S} {3,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.469,-0.789,-0.953,-1.107,-1.45,-1.696,-1.716],'cal/(mol*K)'),
        H298 = (126,'kcal/mol'),
        S298 = (33.3257,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    label = "Bicyclo[2.1.0]pent-2-ene",
    group = 
"""
1 * Cs 0 {2,S} {3,S} {5,S}
2   Cs 0 {1,S} {3,S} {4,S}
3   Cs 0 {1,S} {2,S}
4   C  0 {2,S} {5,D}
5   C  0 {1,S} {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.038,-2.783,-2.423,-2.153,-1.888,-1.694,-1.258],'cal/(mol*K)'),
        H298 = (67.9,'kcal/mol'),
        S298 = (29.8677,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "bicyclo-(3.1.0)-hexane",
    group = 
"""
1 * Cs 0 {2,S} {3,S} {5,S}
2   Cs 0 {1,S} {3,S} {4,S}
3   Cs 0 {1,S} {2,S}
4   Cs 0 {2,S} {6,S}
5   Cs 0 {1,S} {6,S}
6   Cs 0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.227,-2.849,-2.536,-2.35,-2.191,-2.111,-1.76],'cal/(mol*K)'),
        H298 = (32.7464,'kcal/mol'),
        S298 = (60.9856,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    label = "bicyclo[2.1.1]hexane",
    group = 
"""
1 * Cs 0 {3,S} {4,S} {6,S}
2   Cs 0 {3,S} {4,S} {5,S}
3   Cs 0 {1,S} {2,S}
4   Cs 0 {1,S} {2,S}
5   Cs 0 {2,S} {6,S}
6   Cs 0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.61,-3.89,-3.14,-2.64,-1.88,-1.38,-0.67],'cal/(mol*K)'),
        H298 = (37,'kcal/mol'),
        S298 = (29.8,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    label = "Bicyclo[2.2.0]hexane",
    group = 
"""
1 * Cs 0 {2,S} {3,S} {6,S}
2   Cs 0 {1,S} {4,S} {5,S}
3   Cs 0 {1,S} {4,S}
4   Cs 0 {2,S} {3,S}
5   Cs 0 {2,S} {6,S}
6   Cs 0 {1,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.61,-3.89,-3.14,-2.64,-1.88,-1.38,-0.67],'cal/(mol*K)'),
        H298 = (51.8,'kcal/mol'),
        S298 = (29.8,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    label = "bicyclo[2.1.1]hex-2-ene",
    group = 
"""
1 * Cs 0 {3,S} {4,S} {6,S}
2   Cs 0 {3,S} {4,S} {5,S}
3   Cs 0 {1,S} {2,S}
4   Cs 0 {1,S} {2,S}
5   C  0 {2,S} {6,D}
6   C  0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.61,-3.89,-3.14,-2.64,-1.88,-1.38,-0.67],'cal/(mol*K)'),
        H298 = (51,'kcal/mol'),
        S298 = (29.8,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 18,
    label = "bicyclo[2.2.0]hex-2-ene",
    group = 
"""
1 * Cs 0 {2,S} {3,S} {6,S}
2   Cs 0 {1,S} {4,S} {5,S}
3   Cs 0 {1,S} {4,S}
4   Cs 0 {2,S} {3,S}
5   C  0 {2,S} {6,D}
6   C  0 {1,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.038,-2.783,-2.423,-2.153,-1.888,-1.694,-1.258],'cal/(mol*K)'),
        H298 = (55.7,'kcal/mol'),
        S298 = (29.8677,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    label = "Bicyclo[2.2.0]hex-1(4)-ene",
    group = 
"""
1 * Cs 0 {2,S} {6,S}
2   Cs 0 {1,S} {5,S}
3   Cs 0 {4,S} {6,S}
4   Cs 0 {3,S} {5,S}
5   C  0 {2,S} {4,S} {6,D}
6   C  0 {1,S} {3,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.038,-2.783,-2.423,-2.153,-1.888,-1.694,-1.258],'cal/(mol*K)'),
        H298 = (87,'kcal/mol'),
        S298 = (29.8677,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "bicyclo-(2.2.1)-heptane",
    group = 
"""
1 * Cs 0 {3,S} {4,S} {7,S}
2   Cs 0 {3,S} {5,S} {6,S}
3   Cs 0 {1,S} {2,S}
4   Cs 0 {1,S} {5,S}
5   Cs 0 {2,S} {4,S}
6   Cs 0 {2,S} {7,S}
7   Cs 0 {1,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (16.1435,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 38,
    label = "Exo-tricyclo[5.2.1.0(2.6)]decane",
    group = 
"""
1  * Cs 0 {3,S} {4,S} {7,S}
2    Cs 0 {3,S} {5,S} {6,S}
3    Cs 0 {1,S} {2,S}
4    Cs 0 {1,S} {5,S}
5    Cs 0 {2,S} {4,S}
6    Cs 0 {2,S} {7,S} {10,S}
7    Cs 0 {1,S} {6,S} {8,S}
8    Cs 0 {7,S} {9,S}
9    Cs 0 {8,S} {10,S}
10   Cs 0 {6,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (22.65,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978 S, Cp copied from cyclopentane""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 39,
    label = "Exo-tricyclo[5.2.1.0(2.6)]decene",
    group = 
"""
1  * Cs 0 {3,S} {4,S} {7,S}
2    Cs 0 {3,S} {5,S} {6,S}
3    Cs 0 {1,S} {2,S}
4    Cs 0 {1,S} {5,S}
5    Cs 0 {2,S} {4,S}
6    Cs 0 {2,S} {7,S} {10,S}
7    Cs 0 {1,S} {6,S} {8,S}
8    Cd 0 {7,S} {9,D}
9    Cd 0 {8,D} {10,S}
10   Cs 0 {6,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (22.65,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978 S, Cp copied from cyclopentane""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 40,
    label = "Exo-tricyclo[5.2.1.0(1,5)]decane",
    group = 
"""
1  * Cs 0 {2,S} {5,S} {9,S} {10,S}
2    Cs 0 {1,S} {3,S} {6,S}
3    Cs 0 {2,S} {4,S}
4    Cs 0 {3,S} {5,S}
5    Cs 0 {1,S} {4,S}
6    Cs 0 {2,S} {7,S}
7    Cs 0 {6,S} {8,S} {10,S}
8    Cs 0 {7,S} {9,S}
9    Cs 0 {1,S} {8,S}
10   Cs 0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (23.86,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978 S, Cp copied from cyclopentane""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 49,
    label = "tricyclo[5.2.1.0(3,8)]decane",
    group = 
"""
1  * Cs 0 {2,S} {9,S} {10,S}
2    Cs 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S} {8,S}
4    Cs 0 {3,S} {5,S} {10,S}
5    Cs 0 {4,S} {6,S}
6    Cs 0 {5,S} {7,S}
7    Cs 0 {6,S} {8,S}
8    Cs 0 {3,S} {7,S} {9,S}
9    Cs 0 {1,S} {8,S}
10   Cs 0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (19.26,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978 S, Cp copied from cyclopentane""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    label = "bicyclo-(4.1.0)-heptane",
    group = 
"""
1 * Cs 0 {2,S} {3,S} {5,S}
2   Cs 0 {1,S} {3,S} {4,S}
3   Cs 0 {1,S} {2,S}
4   Cs 0 {2,S} {6,S}
5   Cs 0 {1,S} {7,S}
6   Cs 0 {4,S} {7,S}
7   Cs 0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.227,-2.849,-2.536,-2.35,-2.191,-2.111,-1.76],'cal/(mol*K)'),
        H298 = (28.9498,'kcal/mol'),
        S298 = (55.5766,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    label = "bicyclo(2.2.1)hepta-2,5-diene",
    group = 
"""
1 * C  0 {3,S} {4,S} {7,S}
2   C  0 {3,S} {5,S} {6,S}
3   Cs 0 {1,S} {2,S}
4   C  0 {1,S} {5,D}
5   C  0 {2,S} {4,D}
6   C  0 {2,S} {7,D}
7   C  0 {1,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (31.6435,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    label = "norbornene",
    group = 
"""
1 * Cs 0 {3,S} {4,S} {7,S}
2   Cs 0 {3,S} {5,S} {6,S}
3   Cs 0 {1,S} {2,S}
4   Cs 0 {1,S} {5,S}
5   Cs 0 {2,S} {4,S}
6   C  0 {2,S} {7,D}
7   C  0 {1,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (19.2,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    label = "bicyclo-(5.1.0)-octane",
    group = 
"""
1 * Cs 0 {2,S} {3,S} {5,S}
2   Cs 0 {1,S} {3,S} {4,S}
3   Cs 0 {1,S} {2,S}
4   Cs 0 {2,S} {6,S}
5   Cs 0 {1,S} {8,S}
6   Cs 0 {4,S} {7,S}
7   Cs 0 {6,S} {8,S}
8   Cs 0 {5,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.227,-2.849,-2.536,-2.35,-2.191,-2.111,-1.76],'cal/(mol*K)'),
        H298 = (29.6411,'kcal/mol'),
        S298 = (50.6699,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 15,
    label = "bicyclo[2.2.2]octane",
    group = 
"""
1 * Cs 0 {3,S} {6,S} {8,S}
2   Cs 0 {4,S} {5,S} {7,S}
3   Cs 0 {1,S} {4,S}
4   Cs 0 {2,S} {3,S}
5   Cs 0 {2,S} {6,S}
6   Cs 0 {1,S} {5,S}
7   Cs 0 {2,S} {8,S}
8   Cs 0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.8,-4.1,-2.9,-1.3,1.08,2.16,3],'cal/(mol*K)'),
        H298 = (7.4,'kcal/mol'),
        S298 = (18.1277,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 45,
    label = "tricyclo[4.4.0.0(3,8)]decane",
    group = 
"""
1  * Cs 0 {2,S} {6,S} {10,S}
2    Cs 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S}
4    Cs 0 {3,S} {5,S} {9,S}
5    Cs 0 {4,S} {6,S}
6    Cs 0 {1,S} {5,S} {7,S}
7    Cs 0 {6,S} {8,S}
8    Cs 0 {7,S} {9,S}
9    Cs 0 {4,S} {8,S} {10,S}
10   Cs 0 {1,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.8,-4.1,-2.9,-1.3,1.08,2.16,3],'cal/(mol*K)'),
        H298 = (26.12,'kcal/mol'),
        S298 = (18.1277,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978 S, Cp copied from Cyclohexane""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    label = "octahydropentalene",
    group = 
"""
1 * Cs 0 {2,S} {5,S} {8,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {1,S} {4,S} {6,S}
6   Cs 0 {5,S} {7,S}
7   Cs 0 {6,S} {8,S}
8   Cs 0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.5,-5.5,-4.5,-3.8,-2.8,-1.93,-0.37],'cal/(mol*K)'),
        H298 = (10.3,'kcal/mol'),
        S298 = (27.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978, S, Cp from Cyclopentane""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 37,
    label = "tricyclo[5.2.1.0(4,10)]decane",
    group = 
"""
1  * Cs 0 {2,S} {9,S} {10,S}
2    Cs 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S}
4    Cs 0 {3,S} {5,S} {10,S}
5    Cs 0 {4,S} {6,S}
6    Cs 0 {5,S} {7,S}
7    Cs 0 {6,S} {8,S} {10,S}
8    Cs 0 {7,S} {9,S}
9    Cs 0 {1,S} {8,S}
10   Cs 0 {1,S} {4,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.5,-5.5,-4.5,-3.8,-2.8,-1.93,-0.37],'cal/(mol*K)'),
        H298 = (15.68,'kcal/mol'),
        S298 = (27.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978, S, Cp from Cyclopentane""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 44,
    label = "tricyclo[5.2.1.0(4,8)]decane",
    group = 
"""
1    Cs 0 {2,S} {10,S}
2    Cs 0 {1,S} {3,S} {9,S}
3    Cs 0 {2,S} {4,S}
4  * Cs 0 {3,S} {5,S} {10,S}
5    Cs 0 {4,S} {6,S}
6    Cs 0 {5,S} {7,S}
7    Cs 0 {6,S} {8,S} {10,S}
8    Cs 0 {7,S} {9,S}
9    Cs 0 {2,S} {8,S}
10   Cs 0 {1,S} {4,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (21.48,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978 S, Cp copied from cyclopentane""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 46,
    label = "tricyclo[4.2.2.0(1,5)]decane",
    group = 
"""
1  * Cs 0 {2,S} {5,S} {8,S} {10,S}
2    Cs 0 {1,S} {3,S} {6,S}
3    Cs 0 {2,S} {4,S}
4    Cs 0 {3,S} {5,S}
5    Cs 0 {1,S} {4,S}
6    Cs 0 {2,S} {7,S} {9,S}
7    Cs 0 {6,S} {8,S}
8    Cs 0 {1,S} {7,S}
9    Cs 0 {6,S} {10,S}
10   Cs 0 {1,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (29.65,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978 S, Cp copied from cyclopentane""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 47,
    label = "tricyclo[5.3.0.0(4,10)]decane",
    group = 
"""
1  * Cs 0 {2,S} {5,S} {10,S}
2    Cs 0 {1,S} {3,S} {8,S}
3    Cs 0 {2,S} {4,S}
4    Cs 0 {3,S} {5,S}
5    Cs 0 {1,S} {4,S} {6,S}
6    Cs 0 {5,S} {7,S}
7    Cs 0 {6,S} {8,S}
8    Cs 0 {2,S} {7,S} {9,S}
9    Cs 0 {8,S} {10,S}
10   Cs 0 {1,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (20.74,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978 S, Cp copied from cyclopentane""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 31,
    label = "1,2,3,3a,4,6a-Hexahydropentalene",
    group = 
"""
1 * Cs 0 {2,S} {5,S} {8,S}
2   Cs 0 {1,S} {3,S} {6,S}
3   Cs 0 {2,S} {4,S}
4   Cd 0 {3,S} {5,D}
5   Cd 0 {1,S} {4,D}
6   Cs 0 {2,S} {7,S}
7   Cs 0 {6,S} {8,S}
8   Cs 0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.5,-5.5,-4.5,-3.8,-2.8,-1.93,-0.37],'cal/(mol*K)'),
        H298 = (10.3,'kcal/mol'),
        S298 = (27.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978, S, Cp from Cyclopentane""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 32,
    label = "1,2,3,3a,4,5-hexahydropentalene",
    group = 
"""
1 * Cs 0 {2,S} {5,S} {8,S}
2   Cd 0 {1,S} {3,D} {6,S}
3   Cd 0 {2,D} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {1,S} {4,S}
6   Cs 0 {2,S} {7,S}
7   Cs 0 {6,S} {8,S}
8   Cs 0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.5,-5.5,-4.5,-3.8,-2.8,-1.93,-0.37],'cal/(mol*K)'),
        H298 = (10.3,'kcal/mol'),
        S298 = (27.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978, S, Cp from Cyclopentane""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
    label = "1,3a,4,6a-tetrahydropentalene",
    group = 
"""
1 * Cs 0 {2,S} {5,S} {8,S}
2   Cs 0 {1,S} {3,S} {6,S}
3   Cd 0 {2,S} {4,D}
4   Cd 0 {3,D} {5,S}
5   Cs 0 {1,S} {4,S}
6   Cs 0 {2,S} {7,S}
7   Cd 0 {6,S} {8,D}
8   Cd 0 {1,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (10,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978, S, Cp from Cyclopentene""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 34,
    label = "1,3a,6,6a-tetrahydropentalene",
    group = 
"""
1 * Cs 0 {2,S} {5,S} {8,S}
2   Cs 0 {1,S} {3,S} {6,S}
3   Cd 0 {2,S} {4,D}
4   Cd 0 {3,D} {5,S}
5   Cs 0 {1,S} {4,S}
6   Cd 0 {2,S} {7,D}
7   Cd 0 {6,D} {8,S}
8   Cs 0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (10,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978, S, Cp from Cyclopentene""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 35,
    label = "1,2,6,6a-tetrahydropentalene",
    group = 
"""
1 * Cs 0 {2,S} {5,S} {8,S}
2   Cd 0 {1,S} {3,S} {6,D}
3   Cd 0 {2,S} {4,D}
4   Cd 0 {3,D} {5,S}
5   Cs 0 {1,S} {4,S}
6   Cd 0 {2,D} {7,S}
7   Cs 0 {6,S} {8,S}
8   Cs 0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (10,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978, S, Cp from Cyclopentene""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 36,
    label = "C12CCC=C1CC=C2",
    group = 
"""
1 * Cd 0 {2,S} {5,S} {8,D}
2   Cs 0 {1,S} {3,S} {6,S}
3   Cd 0 {2,S} {4,D}
4   Cd 0 {3,D} {5,S}
5   Cs 0 {1,S} {4,S}
6   Cs 0 {2,S} {7,S}
7   Cs 0 {6,S} {8,S}
8   Cd 0 {1,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (10,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978, S, Cp from Cyclopentene""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    label = "bicyclo-(6.1.0)-nonane",
    group = 
"""
1 * Cs 0 {2,S} {3,S} {5,S}
2   Cs 0 {1,S} {3,S} {4,S}
3   Cs 0 {1,S} {2,S}
4   Cs 0 {2,S} {6,S}
5   Cs 0 {1,S} {9,S}
6   Cs 0 {4,S} {7,S}
7   Cs 0 {6,S} {8,S}
8   Cs 0 {7,S} {9,S}
9   Cs 0 {5,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.227,-2.849,-2.536,-2.35,-2.191,-2.111,-1.76],'cal/(mol*K)'),
        H298 = (31.1435,'kcal/mol'),
        S298 = (49.2679,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    label = "cis-octahydro-1H-indene",
    group = 
"""
1 * Cs 0 {2,S} {3,S} {4,S}
2   Cs 0 {1,S} {5,S} {6,S}
3   Cs 0 {1,S} {9,S}
4   Cs 0 {1,S} {7,S}
5   Cs 0 {2,S} {8,S}
6   Cs 0 {2,S} {9,S}
7   Cs 0 {4,S} {8,S}
8   Cs 0 {5,S} {7,S}
9   Cs 0 {3,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (8.21053,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 41,
    label = "tricyclo[4.3.1.0(3,7)]decane",
    group = 
"""
1  * Cs 0 {2,S} {3,S} {4,S}
2    Cs 0 {1,S} {5,S} {6,S}
3    Cs 0 {1,S} {9,S}
4    Cs 0 {1,S} {7,S}
5    Cs 0 {2,S} {8,S}
6    Cs 0 {2,S} {9,S} {10,S}
7    Cs 0 {4,S} {8,S} {10,S}
8    Cs 0 {5,S} {7,S}
9    Cs 0 {3,S} {6,S}
10   Cs 0 {6,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (20.77,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978 S, Cp copied from cyclopentane""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 42,
    label = "tricyclo[4.3.1.0(3,8)]decane",
    group = 
"""
1  * Cs 0 {2,S} {3,S} {4,S}
2    Cs 0 {1,S} {5,S} {6,S}
3    Cs 0 {1,S} {9,S}
4    Cs 0 {1,S} {7,S}
5    Cs 0 {2,S} {8,S}
6    Cs 0 {2,S} {9,S}
7    Cs 0 {4,S} {8,S} {10,S}
8    Cs 0 {5,S} {7,S}
9    Cs 0 {3,S} {6,S} {10,S}
10   Cs 0 {7,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (18.29,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978 S, Cp copied from cyclopentane""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    label = "indane",
    group = 
"""
1 * Cs 0 {2,S} {3,S}
2   Cs 0 {1,S} {4,S}
3   Cs 0 {1,S} {5,S}
4   C  0 {2,S} {5,B} {6,B}
5   C  0 {3,S} {4,B} {7,B}
6   C  0 {4,B} {8,B}
7   C  0 {5,B} {9,B}
8   C  0 {6,B} {9,B}
9   C  0 {7,B} {8,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.5,-5.5,-4.5,-3.8,-2.8,-1.93,-0.37],'cal/(mol*K)'),
        H298 = (5.54,'kcal/mol'),
        S298 = (27.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    label = "indene",
    group = 
"""
1 * Cs 0 {2,S} {4,S}
2   C  0 {1,S} {3,B} {5,B}
3   C  0 {2,B} {6,S} {7,B}
4   C  0 {1,S} {6,D}
5   C  0 {2,B} {8,B}
6   C  0 {3,S} {4,D}
7   C  0 {3,B} {9,B}
8   C  0 {5,B} {9,B}
9   C  0 {7,B} {8,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (2.1,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    label = "2,3,3a,4,5,6-hexahydro-1H-indene",
    group = 
"""
1 * Cs 0 {2,S} {9,S}
2   Cd 0 {1,S} {3,D} {7,S}
3   Cd 0 {2,D} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {4,S} {6,S}
6   Cs 0 {5,S} {7,S}
7   Cs 0 {2,S} {6,S} {8,S}
8   Cs 0 {7,S} {9,S}
9   Cs 0 {1,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.5,-5.5,-4.5,-3.8,-2.8,-1.93,-0.37],'cal/(mol*K)'),
        H298 = (7.5,'kcal/mol'),
        S298 = (27.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978, S, Cp from Cyclopentane""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    label = "C12CCCC1=CCC=C2",
    group = 
"""
1 * Cs 0 {2,S} {9,S}
2   Cd 0 {1,S} {3,D} {7,S}
3   Cd 0 {2,D} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cd 0 {4,S} {6,D}
6   Cd 0 {5,D} {7,S}
7   Cs 0 {2,S} {6,S} {8,S}
8   Cs 0 {7,S} {9,S}
9   Cs 0 {1,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.5,-5.5,-4.5,-3.8,-2.8,-1.93,-0.37],'cal/(mol*K)'),
        H298 = (6.8,'kcal/mol'),
        S298 = (27.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978, S, Cp from Cyclopentane""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
    label = "2,4,5,6,7,7a-Hexahydro-1H-indene",
    group = 
"""
1 * Cd 0 {2,D} {5,S} {9,S}
2   Cd 0 {1,D} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {1,S} {4,S} {6,S}
6   Cs 0 {5,S} {7,S}
7   Cs 0 {6,S} {8,S}
8   Cs 0 {7,S} {9,S}
9   Cs 0 {1,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (5.97,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978, S, Cp from Cyclopentene""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 28,
    label = "2,3,3a,4,5,7a-hexahydro-1H-indene",
    group = 
"""
1 * Cs 0 {2,S} {5,S} {9,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {1,S} {4,S} {6,S}
6   Cd 0 {5,S} {7,D}
7   Cd 0 {6,D} {8,S}
8   Cs 0 {7,S} {9,S}
9   Cs 0 {1,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.5,-5.5,-4.5,-3.8,-2.8,-1.93,-0.37],'cal/(mol*K)'),
        H298 = (7.5,'kcal/mol'),
        S298 = (27.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978, S, Cp from Cyclopentane""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 29,
    label = "2,3,3a,4,7,7a-Hexahydro-1H-indene",
    group = 
"""
1 * Cs 0 {2,S} {5,S} {9,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {1,S} {4,S} {6,S}
6   Cs 0 {5,S} {7,S}
7   Cd 0 {6,S} {8,D}
8   Cd 0 {7,D} {9,S}
9   Cs 0 {1,S} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.5,-5.5,-4.5,-3.8,-2.8,-1.93,-0.37],'cal/(mol*K)'),
        H298 = (7.5,'kcal/mol'),
        S298 = (27.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978, S, Cp from Cyclopentane""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
    label = "2,3,3a,7a-tetrahydro-1H-indene",
    group = 
"""
1 * Cs 0 {2,S} {5,S} {9,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {1,S} {4,S} {6,S}
6   Cd 0 {5,S} {7,D}
7   Cd 0 {6,D} {8,S}
8   Cd 0 {7,S} {9,D}
9   Cd 0 {1,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.5,-5.5,-4.5,-3.8,-2.8,-1.93,-0.37],'cal/(mol*K)'),
        H298 = (10.1,'kcal/mol'),
        S298 = (27.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978, S, Cp from Cyclopentane""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 43,
    label = "tricyclo[4.4.0.0(3,9)]decane",
    group = 
"""
1  * Cs 0 {2,S} {6,S} {10,S}
2    Cs 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S} {9,S}
4    Cs 0 {3,S} {5,S}
5    Cs 0 {4,S} {6,S}
6    Cs 0 {1,S} {5,S} {7,S}
7    Cs 0 {6,S} {8,S}
8    Cs 0 {7,S} {9,S}
9    Cs 0 {3,S} {8,S} {10,S}
10   Cs 0 {1,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (30.9,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978 S, Cp copied from cyclopentane""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 48,
    label = "anti-tricyclo[4.2.1.1(2,5)]decane",
    group = 
"""
1  * Cs 0 {2,S} {8,S} {10,S}
2    Cs 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S}
4    Cs 0 {3,S} {5,S} {10,S}
5    Cs 0 {4,S} {6,S} {9,S}
6    Cs 0 {5,S} {7,S}
7    Cs 0 {6,S} {8,S}
8    Cs 0 {1,S} {7,S} {9,S}
9    Cs 0 {5,S} {8,S}
10   Cs 0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.5,-3.942,-3.291,-2.759,-2.08,-1.628,-0.898],'cal/(mol*K)'),
        H298 = (30.66,'kcal/mol'),
        S298 = (25.8284,'cal/(mol*K)'),
    ),
    shortDesc = u"""Automated Estimation of Ring Strain Energies, Gasteiger, 1978 S, Cp copied from cyclopentane""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    label = "biphenylene",
    group = 
"""
1  * C 0 {2,B} {4,S} {6,B}
2    C 0 {1,B} {3,S} {5,B}
3    C 0 {2,S} {4,B} {7,B}
4    C 0 {1,S} {3,B} {8,B}
5    C 0 {2,B} {9,B}
6    C 0 {1,B} {10,B}
7    C 0 {3,B} {11,B}
8    C 0 {4,B} {12,B}
9    C 0 {5,B} {10,B}
10   C 0 {6,B} {9,B}
11   C 0 {7,B} {12,B}
12   C 0 {8,B} {11,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.61,-3.89,-3.14,-2.64,-1.88,-1.38,-0.67],'cal/(mol*K)'),
        H298 = (58.8828,'kcal/mol'),
        S298 = (29.8,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 14 11:29:30 2013","connieg <connieg@mit.edu>","action","""connieg <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

tree(
"""
L1: PolycyclicRing
    L2: bicyclo-(1.1.0)-butane
    L2: bicyclo-(2.1.0)-pentane
    L2: spiropentane
    L2: Bicyclo[1.1.1]pentane
    L2: bicyclo[2.1.0]pent-1(4)-ene
    L2: Bicyclo[2.1.0]pent-2-ene
    L2: bicyclo-(3.1.0)-hexane
    L2: bicyclo[2.1.1]hexane
    L2: Bicyclo[2.2.0]hexane
    L2: bicyclo[2.1.1]hex-2-ene
    L2: bicyclo[2.2.0]hex-2-ene
    L2: Bicyclo[2.2.0]hex-1(4)-ene
    L2: bicyclo-(2.2.1)-heptane
        L3: Exo-tricyclo[5.2.1.0(2.6)]decane
        L3: Exo-tricyclo[5.2.1.0(2.6)]decene
        L3: Exo-tricyclo[5.2.1.0(1,5)]decane
        L3: tricyclo[5.2.1.0(3,8)]decane
    L2: bicyclo-(4.1.0)-heptane
    L2: bicyclo(2.2.1)hepta-2,5-diene
    L2: norbornene
    L2: bicyclo-(5.1.0)-octane
    L2: bicyclo[2.2.2]octane
        L3: tricyclo[4.4.0.0(3,8)]decane
    L2: octahydropentalene
        L3: tricyclo[5.2.1.0(4,10)]decane
        L3: tricyclo[5.2.1.0(4,8)]decane
        L3: tricyclo[4.2.2.0(1,5)]decane
        L3: tricyclo[5.3.0.0(4,10)]decane
    L2: 1,2,3,3a,4,6a-Hexahydropentalene
    L2: 1,2,3,3a,4,5-hexahydropentalene
    L2: 1,3a,4,6a-tetrahydropentalene
    L2: 1,3a,6,6a-tetrahydropentalene
    L2: 1,2,6,6a-tetrahydropentalene
    L2: C12CCC=C1CC=C2
    L2: bicyclo-(6.1.0)-nonane
    L2: cis-octahydro-1H-indene
        L3: tricyclo[4.3.1.0(3,7)]decane
        L3: tricyclo[4.3.1.0(3,8)]decane
    L2: indane
    L2: indene
    L2: 2,3,3a,4,5,6-hexahydro-1H-indene
    L2: C12CCCC1=CCC=C2
    L2: 2,4,5,6,7,7a-Hexahydro-1H-indene
    L2: 2,3,3a,4,5,7a-hexahydro-1H-indene
    L2: 2,3,3a,4,7,7a-Hexahydro-1H-indene
    L2: 2,3,3a,7a-tetrahydro-1H-indene
    L2: tricyclo[4.4.0.0(3,9)]decane
    L2: anti-tricyclo[4.2.1.1(2,5)]decane
    L2: biphenylene
"""
)

