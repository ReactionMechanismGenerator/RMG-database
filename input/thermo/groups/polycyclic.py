#!/usr/bin/env python
# encoding: utf-8

name = "Polycyclic Ring Corrections"
shortDesc = u""
longDesc = u"""

"""
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
)

entry(
    index = 1,
    label = "norborn{a/e}ne",
    group = "OR{norbornane, norbornene}",
    thermo = u'norbornane',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "norbornane",
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
        H298 = (16.14,'kcal/mol'),
        S298 = (53.47,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "exo-tricyclo[5.2.1.0(2.6)]decane",
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
        Cpdata = ([-15.018,-13.783,-12.193,-10.63,-8.502,-6.688,-4.111],'cal/(mol*K)'),
        H298 = (17.68,'kcal/mol'),
        S298 = (78.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "exo-tricyclo[5.2.1.0(2.6)]decene",
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
        Cpdata = ([-15.018,-13.783,-12.193,-10.63,-8.502,-6.688,-4.111],'cal/(mol*K)'),
        H298 = (22.65,'kcal/mol'),
        S298 = (78.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "exo-tricyclo[5.2.1.0(1.5)]decane",
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
        Cpdata = ([-15.018,-13.783,-12.193,-10.63,-8.502,-6.688,-4.111],'cal/(mol*K)'),
        H298 = (23.86,'kcal/mol'),
        S298 = (78.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "tricyclo[5.2.1.0(3.8)]decane",
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
        Cpdata = ([-15.018,-13.783,-12.193,-10.63,-8.502,-6.688,-4.111],'cal/(mol*K)'),
        H298 = (19.26,'kcal/mol'),
        S298 = (78.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
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
        Cpdata = ([-8.29,-7.302,-6.501,-5.499,-4.58,-3.778,-2.608],'cal/(mol*K)'),
        H298 = (17.8,'kcal/mol'),
        S298 = (53.75,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "exo-tricyclo[5.2.1.0(2.6)]dec-8-ene",
    group = 
"""
1  * Cs 0 {3,S} {4,S} {7,S}
2    Cs 0 {3,S} {5,S} {6,S}
3    Cs 0 {1,S} {2,S}
4    Cs 0 {1,S} {5,S} {8,S}
5    Cs 0 {2,S} {4,S} {10,S}
6    C  0 {2,S} {7,D}
7    C  0 {1,S} {6,D}
8    Cs 0 {4,S} {9,S}
9    Cs 0 {8,S} {10,S}
10   Cs 0 {5,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-12.29,-11.16,-10.04,-8.64,-7.12,-5.72,-3.81],'cal/(mol*K)'),
        H298 = (22.83,'kcal/mol'),
        S298 = (79.45,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "bicyclo[3.2.1]oct{a/e}ne",
    group = "OR{bicyclo[3.2.1]octane, bicyclo[3.2.1]octene}",
    thermo = u'bicyclo[3.2.1]octane',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "bicyclo[3.2.1]octane",
    group = 
"""
1 * Cs 0 {2,S} {6,S} {8,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {4,S} {6,S} {7,S}
6   Cs 0 {1,S} {5,S}
7   Cs 0 {5,S} {8,S}
8   Cs 0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-11.2,-9.9,-8.4,-7.1,-5.2,-3.8,-1.7],'cal/(mol*K)'),
        H298 = (8.5,'kcal/mol'),
        S298 = (48.66,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "tricyclo[4.2.1.1(2.5)]decane",
    group = 
"""
1  * Cs 0 {2,S} {6,S} {8,S}
2    Cs 0 {1,S} {3,S} {9,S}
3    Cs 0 {2,S} {4,S}
4    Cs 0 {3,S} {5,S} {10,S}
5    Cs 0 {4,S} {6,S} {7,S}
6    Cs 0 {1,S} {5,S}
7    Cs 0 {5,S} {8,S}
8    Cs 0 {1,S} {7,S}
9    Cs 0 {2,S} {10,S}
10   Cs 0 {4,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-15.1,-13.4,-11.6,-10,-7.8,-6.1,-3.7],'cal/(mol*K)'),
        H298 = (22.5,'kcal/mol'),
        S298 = (77.13,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "bicyclo[3.2.1]octene",
    group = 
"""
1 * Cs 0 {2,S} {6,S} {8,S}
2   C  0 {1,S} {3,D}
3   C  0 {2,D} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {4,S} {6,S} {7,S}
6   Cs 0 {1,S} {5,S}
7   Cs 0 {5,S} {8,S}
8   Cs 0 {1,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.3,-8.3,-7.2,-6.1,-4.8,-3.6,-2],'cal/(mol*K)'),
        H298 = (8.5,'kcal/mol'),
        S298 = (48.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "ind{a/e}ne",
    group = "OR{indane, indene, cis-octahydro-1H-indene, hexahydro-1H-indene, tetrahydro-1H-indene}",
    thermo = u'indane',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
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
        Cpdata = ([-5.23,-5.21,-4.3,-2.86,-0.88,-0.71,1.4],'cal/(mol*K)'),
        H298 = (5.54,'kcal/mol'),
        S298 = (25.35,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
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
        Cpdata = ([-3.88,-4.29,-3.89,-2.96,-1.83,-2.2,-1.31],'cal/(mol*K)'),
        H298 = (2.1,'kcal/mol'),
        S298 = (33.08,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
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
        Cpdata = ([-11.91,-10.762,-9.241,-7.769,-5.56,-3.888,-1.388],'cal/(mol*K)'),
        H298 = (8.21,'kcal/mol'),
        S298 = (47.72,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "tricyclo[4.3.1.0(3.7)]decane",
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
        Cpdata = ([-15.58,-14.7,-12.37,-9.37,-5.42,-4.64,-1.58],'cal/(mol*K)'),
        H298 = (20.77,'kcal/mol'),
        S298 = (78.58,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "tricyclo[4.3.1.0(3.8)]decane",
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
        Cpdata = ([-16.03,-15.03,-12.57,-9.46,-5.47,-4.74,-1.59],'cal/(mol*K)'),
        H298 = (18.29,'kcal/mol'),
        S298 = (75.75,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "hexahydro-1H-indene",
    group = "OR{2.3.3a.4.5.6-hexahydro-1H-indene, 2.4.5.6.7.7a-hexahydro-1H-indene, 2.3.3a.4.5.7a-hexahydro-1H-indene, 2.3.3a.4.7.7a-hexahydro-1H-indene, 3a.4.5.6.7.7a-hexahydro-1H-indene, 2.3.4.5.6.7-hexahydro-1H-indene}",
    thermo = u'2.4.5.6.7.7a-hexahydro-1H-indene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "2.3.3a.4.5.6-hexahydro-1H-indene",
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
        Cpdata = ([-9.8,-9,-7.9,-6.5,-4.7,-3.4,-1.3],'cal/(mol*K)'),
        H298 = (9,'kcal/mol'),
        S298 = (47.04,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "2.4.5.6.7.7a-hexahydro-1H-indene",
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
        Cpdata = ([-8,-7.6,-6.8,-5.7,-4.3,-3.3,-2.1],'cal/(mol*K)'),
        H298 = (9,'kcal/mol'),
        S298 = (45.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "2.3.3a.4.5.7a-hexahydro-1H-indene",
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
    thermo = u'2.4.5.6.7.7a-hexahydro-1H-indene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "2.3.3a.4.7.7a-hexahydro-1H-indene",
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
    thermo = u'2.4.5.6.7.7a-hexahydro-1H-indene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "2.3.4.5.6.7-hexahydro-1H-indene",
    group = 
"""
1 * Cs 0 {2,S} {9,S}
2   Cd 0 {1,S} {3,S} {7,D}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {4,S} {6,S}
6   Cs 0 {5,S} {7,S}
7   Cd 0 {2,D} {6,S} {8,S}
8   Cs 0 {7,S} {9,S}
9   Cs 0 {1,S} {8,S}
""",
    thermo = u'2.4.5.6.7.7a-hexahydro-1H-indene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "3a.4.5.6.7.7a-hexahydro-1H-indene",
    group = 
"""
1 * Cs 0 {2,S} {9,S}
2   Cs 0 {1,S} {3,S} {7,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {4,S} {6,S}
6   Cs 0 {5,S} {7,S}
7   Cs 0 {2,S} {6,S} {8,S}
8   Cd 0 {7,S} {9,D}
9   Cd 0 {1,S} {8,D}
""",
    thermo = u'2.4.5.6.7.7a-hexahydro-1H-indene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "tetrahydro-1H-indene",
    group = "OR{2.3.4.5-tetrahydro-1H-indene, 2.3.4.7-tetrahydro-1H-indene, 2.3.3a.7a-tetrahydro-1H-indene, C12CCCC1=CCC=C2, 2.3.3a.4-tetrahydro-1H-indene, 2.3.5.6-tetrahydro-1H-indene, 2.6.7.7a-tetrahydro-1H-indene}",
    thermo = u'2.3.3a.7a-tetrahydro-1H-indene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "2.3.3a.7a-tetrahydro-1H-indene",
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
        Cpdata = ([-8,-7.6,-6.8,-5.7,-4.3,-3.3,-2.1],'cal/(mol*K)'),
        H298 = (10.1,'kcal/mol'),
        S298 = (45.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
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
        Cpdata = ([-8,-7.6,-6.8,-5.7,-4.3,-3.3,-2.1],'cal/(mol*K)'),
        H298 = (6.8,'kcal/mol'),
        S298 = (45.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "2.3.4.5-tetrahydro-1H-indene",
    group = 
"""
1 * Cd 0 {2,S} {5,D} {9,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cd 0 {1,D} {4,S} {6,S}
6   Cd 0 {5,S} {7,D}
7   Cd 0 {6,D} {8,S}
8   Cs 0 {7,S} {9,S}
9   Cs 0 {1,S} {8,S}
""",
    thermo = u'2.3.3a.7a-tetrahydro-1H-indene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "2.3.4.7-tetrahydro-1H-indene",
    group = 
"""
1 * Cd 0 {2,S} {5,D} {9,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cd 0 {1,D} {4,S} {6,S}
6   Cs 0 {5,S} {7,S}
7   Cd 0 {6,S} {8,D}
8   Cd 0 {7,D} {9,S}
9   Cs 0 {1,S} {8,S}
""",
    thermo = u'2.3.3a.7a-tetrahydro-1H-indene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "2.3.3a.4-tetrahydro-1H-indene",
    group = 
"""
1 * Cd 0 {2,S} {5,S} {9,D}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cs 0 {1,S} {4,S} {6,S}
6   Cs 0 {5,S} {7,S}
7   Cd 0 {6,S} {8,D}
8   Cd 0 {7,D} {9,S}
9   Cd 0 {1,D} {8,S}
""",
    thermo = u'2.3.3a.7a-tetrahydro-1H-indene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "2.3.5.6-tetrahydro-1H-indene",
    group = 
"""
1 * Cd 0 {2,S} {5,S} {9,D}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cs 0 {3,S} {5,S}
5   Cd 0 {1,S} {4,S} {6,D}
6   Cd 0 {5,D} {7,S}
7   Cs 0 {6,S} {8,S}
8   Cs 0 {7,S} {9,S}
9   Cd 0 {1,D} {8,S}
""",
    thermo = u'2.3.3a.7a-tetrahydro-1H-indene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "2.6.7.7a-tetrahydro-1H-indene",
    group = 
"""
1 * Cs 0 {2,S} {5,S} {9,S}
2   Cs 0 {1,S} {3,S}
3   Cs 0 {2,S} {4,S}
4   Cd 0 {3,S} {5,D}
5   Cd 0 {1,S} {4,D} {6,S}
6   Cd 0 {5,S} {7,D}
7   Cd 0 {6,D} {8,S}
8   Cs 0 {7,S} {9,S}
9   Cs 0 {1,S} {8,S}
""",
    thermo = u'2.3.3a.7a-tetrahydro-1H-indene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "pental{a/e}ne",
    group = "OR{octahydropentalene, hexahydropentalene, tetrahydropentalene}",
    thermo = u'octahydropentalene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
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
        Cpdata = ([-11.52,-10.59,-8.62,-6.18,-2.88,-2.26,0.09],'cal/(mol*K)'),
        H298 = (10.3,'kcal/mol'),
        S298 = (54.09,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "tricyclo[5.2.1.0(4.10)]decane",
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
        Cpdata = ([-15.018,-13.783,-12.193,-10.63,-8.502,-6.688,-4.111],'cal/(mol*K)'),
        H298 = (15.68,'kcal/mol'),
        S298 = (78.53,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "tricyclo[5.2.1.0(4.8)]decane",
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
        Cpdata = ([-15.6,-14.69,-12.36,-9.34,-5.4,-4.64,-1.58],'cal/(mol*K)'),
        H298 = (21.48,'kcal/mol'),
        S298 = (78.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "tricyclo[4.2.2.0(1.5)]decane",
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
        Cpdata = ([-15.15,-14.51,-12.47,-9.72,-5.97,-5.19,-1.39],'cal/(mol*K)'),
        H298 = (29.65,'kcal/mol'),
        S298 = (82.23,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "tricyclo[5.3.0.0(4.10)]decane",
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
        Cpdata = ([-15.5,-14.55,-12.19,-9.17,-5.28,-4.57,-1.53],'cal/(mol*K)'),
        H298 = (20.74,'kcal/mol'),
        S298 = (77.45,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "hexahydropentalene",
    group = "OR{1.2.3.3a.4.6a-hexahydropentalene, 1.2.3.3a.4.5-hexahydropentalene}",
    thermo = u'1.2.3.3a.4.6a-hexahydropentalene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "1.2.3.3a.4.6a-hexahydropentalene",
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
        Cpdata = ([-8.84,-8,-7.03,-5.94,-4.62,-3.53,-1.94],'cal/(mol*K)'),
        H298 = (9.76,'kcal/mol'),
        S298 = (51.17,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "1.2.3.3a.4.5-hexahydropentalene",
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
        Cpdata = ([-8.85,-8.16,-7.22,-6.08,-4.66,-3.57,-1.84],'cal/(mol*K)'),
        H298 = (13.8,'kcal/mol'),
        S298 = (50.57,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "tetrahydropentalene",
    group = "OR{1.3a.4.6a-tetrahydropentalene, 1.3a.6.6a-tetrahydropentalene, 1.2.6.6a-tetrahydropentalene, C12CCC=C1CC=C2}",
    thermo = u'1.3a.4.6a-tetrahydropentalene',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "1.3a.4.6a-tetrahydropentalene",
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
        Cpdata = ([-8.57,-7.46,-6.33,-5.3,-4.01,-3.25,-1.79],'cal/(mol*K)'),
        H298 = (10,'kcal/mol'),
        S298 = (51.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "1.3a.6.6a-tetrahydropentalene",
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
    thermo = u'C12CCC=C1CC=C2',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "1.2.6.6a-tetrahydropentalene",
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
    thermo = u'C12CCC=C1CC=C2',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
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
        Cpdata = ([-8.57,-7.46,-6.33,-5.3,-4.01,-3.25,-1.79],'cal/(mol*K)'),
        H298 = (14.2,'kcal/mol'),
        S298 = (51.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "sided3memberedring",
    group = "OR{bicyclo-(1.1.0)-butane, bicyclo-(2.1.0)-pentane, bicyclo-(3.1.0)-hexane, bicyclo-(4.1.0)-hept{a/e}ne, bicyclo-(5.1.0)-octane, bicyclo-(6.1.0)-nonane}",
    thermo = u'bicyclo-(1.1.0)-butane',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
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
        Cpdata = ([-4.74,-5.18,-4.85,-4.17,-3.61,-4.01,-3.22],'cal/(mol*K)'),
        H298 = (65.52,'kcal/mol'),
        S298 = (69.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
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
        Cpdata = ([-6.7,-6.66,-5.78,-4.57,-3.31,-3.56,-2.35],'cal/(mol*K)'),
        H298 = (55.38,'kcal/mol'),
        S298 = (64.73,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
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
        Cpdata = ([-8.27,-8.01,-6.85,-5.27,-3.32,-3.2,-1.6],'cal/(mol*K)'),
        H298 = (32.75,'kcal/mol'),
        S298 = (61.25,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "bicyclo-(4.1.0)-hept{a/e}ne",
    group = 
"""
1 * Cs 0 {2,S} {3,S} {5,S}
2   Cs 0 {1,S} {3,S} {4,S}
3   Cs 0 {1,S} {2,S}
4   Cs 0 {2,S} {6,{S,D}}
5   Cs 0 {1,S} {7,S}
6   Cs 0 {4,{S,D}} {7,S}
7   Cs 0 {5,S} {6,S}
""",
    thermo = u'bicyclo-(4.1.0)-heptane',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
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
        Cpdata = ([-9.33,-8.86,-7.46,-5.59,-3.08,-2.67,-0.76],'cal/(mol*K)'),
        H298 = (28.95,'kcal/mol'),
        S298 = (57.69,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "bicyclo-(4.1.0)-hept-2-ene",
    group = 
"""
1 * Cs 0 {2,S} {3,S} {5,S}
2   Cs 0 {1,S} {3,S} {4,S}
3   Cs 0 {1,S} {2,S}
4   Cs 0 {2,S} {6,D}
5   Cs 0 {1,S} {7,S}
6   Cs 0 {4,D} {7,S}
7   Cs 0 {5,S} {6,S}
""",
    thermo = u'bicyclo-(4.1.0)-heptane',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "1.1a.3a.4.5.6.6a.6b-octahydrocyclopropa[e]indene",
    group = 
"""
1  * Cs 0 {2,S} {3,S} {5,S}
2    Cs 0 {1,S} {3,S} {4,S}
3    Cs 0 {1,S} {2,S}
4    Cs 0 {2,S} {6,D}
5    Cs 0 {1,S} {7,S} {10,S}
6    Cs 0 {4,D} {7,S}
7    Cs 0 {5,S} {6,S} {8,S}
8    Cs 0 {7,S} {9,S}
9    Cs 0 {8,S} {10,S}
10   Cs 0 {5,S} {9,S}
""",
    thermo = u'bicyclo-(4.1.0)-heptane',
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
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
        Cpdata = ([-10.29,-9.54,-7.86,-5.68,-2.67,-2.04,0.13],'cal/(mol*K)'),
        H298 = (29.64,'kcal/mol'),
        S298 = (51.29,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
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
        Cpdata = ([-11.04,-10.02,-8.09,-5.64,-2.16,-1.32,1.06],'cal/(mol*K)'),
        H298 = (31.14,'kcal/mol'),
        S298 = (48.46,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "bicyclo(2.2.1)hepta-2.5-diene",
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
        Cpdata = ([-9.88,-8.43,-6.65,-4.77,-2.79,-3.1,-1.54],'cal/(mol*K)'),
        H298 = (31.64,'kcal/mol'),
        S298 = (57.61,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
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
        Cpdata = ([-3.33,-4.84,-5.11,-4.26,-2.86,-2.67,-1.23],'cal/(mol*K)'),
        H298 = (58.88,'kcal/mol'),
        S298 = (31.69,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
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
        Cpdata = ([-5.93,-6.5,-6.24,-5.5,-4.4,-4.35,-2.38],'cal/(mol*K)'),
        H298 = (63.59,'kcal/mol'),
        S298 = (67.15,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
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
        Cpdata = ([-8.92,-8.22,-6.65,-4.79,-2.85,-3.09,-1.39],'cal/(mol*K)'),
        H298 = (37,'kcal/mol'),
        S298 = (57.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "bicyclo[2.2.0]hexane",
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
        Cpdata = ([-8.54,-8.07,-6.7,-4.98,-3.04,-3.1,-1.48],'cal/(mol*K)'),
        H298 = (51.8,'kcal/mol'),
        S298 = (59.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "bicyclo[1.1.1]pentane",
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
        Cpdata = ([-6.64,-6.32,-5.24,-3.91,-2.78,-3.31,-2.12],'cal/(mol*K)'),
        H298 = (68,'kcal/mol'),
        S298 = (62.36,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
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
        Cpdata = ([-12,-11.01,-8.96,-6.42,-3.03,-2.4,0.05],'cal/(mol*K)'),
        H298 = (7.4,'kcal/mol'),
        S298 = (48.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "tricyclo[4.4.0.0(3.8)]decane",
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
        Cpdata = ([-16.13,-15.02,-12.47,-9.29,-5.32,-4.7,-1.53],'cal/(mol*K)'),
        H298 = (26.12,'kcal/mol'),
        S298 = (75.25,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
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
        Cpdata = ([-6.86,-6.73,-5.82,-4.2,-2.93,-3.36,-1.97],'cal/(mol*K)'),
        H298 = (51,'kcal/mol'),
        S298 = (58.93,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "methylidenebicyclo[2.2.1]heptane",
    group = 
"""
1 * Cs 0 {3,S} {4,S} {7,S}
2   Cs 0 {3,S} {5,S} {6,S}
3   Cs 0 {1,S} {2,S}
4   Cs 0 {1,S} {5,S}
5   Cs 0 {2,S} {4,S}
6   Cs 0 {2,S} {7,S}
7   Cd 0 {1,S} {6,S} {8,D}
8   Cd 0 {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.27,-8.28,-7.29,-6.18,-4.88,-3.81,-2.22],'cal/(mol*K)'),
        H298 = (14.6,'kcal/mol'),
        S298 = (50.85,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
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
        Cpdata = ([-6.35,-6.47,-5.81,-4.36,-3.1,-3.34,-2.05],'cal/(mol*K)'),
        H298 = (55.7,'kcal/mol'),
        S298 = (60.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "bicyclo[2.2.0]hex-1(4)-ene",
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
        Cpdata = ([-6.4,-6.61,-5.83,-4.57,-3.17,-3.27,-1.87],'cal/(mol*K)'),
        H298 = (87,'kcal/mol'),
        S298 = (58.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
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
        Cpdata = ([-4.52,-5.35,-5.15,-4.39,-3.54,-3.73,-2.7],'cal/(mol*K)'),
        H298 = (126,'kcal/mol'),
        S298 = (66.41,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "bicyclo[2.1.0]pent-2-ene",
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
        Cpdata = ([-4.56,-5.1,-4.92,-3.97,-3.38,-3.81,-2.92],'cal/(mol*K)'),
        H298 = (67.9,'kcal/mol'),
        S298 = (65.71,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "tricyclo[4.4.0.0(3.9)]decane",
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
        Cpdata = ([-16.09,-14.97,-12.4,-9.23,-5.27,-4.66,-1.5],'cal/(mol*K)'),
        H298 = (30.9,'kcal/mol'),
        S298 = (75.36,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: PolycyclicRing
    L2: norborn{a/e}ne
        L3: norbornane
            L4: exo-tricyclo[5.2.1.0(2.6)]decane
            L4: exo-tricyclo[5.2.1.0(2.6)]decene
            L4: exo-tricyclo[5.2.1.0(1.5)]decane
            L4: tricyclo[5.2.1.0(3.8)]decane
        L3: norbornene
            L4: exo-tricyclo[5.2.1.0(2.6)]dec-8-ene
    L2: bicyclo[3.2.1]oct{a/e}ne
        L3: bicyclo[3.2.1]octane
            L4: tricyclo[4.2.1.1(2.5)]decane
        L3: bicyclo[3.2.1]octene
    L2: ind{a/e}ne
        L3: indane
        L3: indene
        L3: cis-octahydro-1H-indene
            L4: tricyclo[4.3.1.0(3.7)]decane
            L4: tricyclo[4.3.1.0(3.8)]decane
        L3: hexahydro-1H-indene
            L4: 2.3.3a.4.5.6-hexahydro-1H-indene
            L4: 2.4.5.6.7.7a-hexahydro-1H-indene
            L4: 2.3.3a.4.5.7a-hexahydro-1H-indene
            L4: 2.3.3a.4.7.7a-hexahydro-1H-indene
            L4: 2.3.4.5.6.7-hexahydro-1H-indene
            L4: 3a.4.5.6.7.7a-hexahydro-1H-indene
        L3: tetrahydro-1H-indene
            L4: 2.3.3a.7a-tetrahydro-1H-indene
            L4: C12CCCC1=CCC=C2
            L4: 2.3.4.5-tetrahydro-1H-indene
            L4: 2.3.4.7-tetrahydro-1H-indene
            L4: 2.3.3a.4-tetrahydro-1H-indene
            L4: 2.3.5.6-tetrahydro-1H-indene
            L4: 2.6.7.7a-tetrahydro-1H-indene
    L2: pental{a/e}ne
        L3: octahydropentalene
            L4: tricyclo[5.2.1.0(4.10)]decane
            L4: tricyclo[5.2.1.0(4.8)]decane
            L4: tricyclo[4.2.2.0(1.5)]decane
            L4: tricyclo[5.3.0.0(4.10)]decane
        L3: hexahydropentalene
            L4: 1.2.3.3a.4.6a-hexahydropentalene
            L4: 1.2.3.3a.4.5-hexahydropentalene
        L3: tetrahydropentalene
            L4: 1.3a.4.6a-tetrahydropentalene
            L4: 1.3a.6.6a-tetrahydropentalene
            L4: 1.2.6.6a-tetrahydropentalene
            L4: C12CCC=C1CC=C2
    L2: sided3memberedring
        L3: bicyclo-(1.1.0)-butane
        L3: bicyclo-(2.1.0)-pentane
        L3: bicyclo-(3.1.0)-hexane
        L3: bicyclo-(4.1.0)-hept{a/e}ne
            L4: bicyclo-(4.1.0)-heptane
            L4: bicyclo-(4.1.0)-hept-2-ene
                L5: 1.1a.3a.4.5.6.6a.6b-octahydrocyclopropa[e]indene
        L3: bicyclo-(5.1.0)-octane
        L3: bicyclo-(6.1.0)-nonane
    L2: bicyclo(2.2.1)hepta-2.5-diene
    L2: biphenylene
    L2: spiropentane
    L2: bicyclo[2.1.1]hexane
    L2: bicyclo[2.2.0]hexane
    L2: bicyclo[1.1.1]pentane
    L2: bicyclo[2.2.2]octane
        L3: tricyclo[4.4.0.0(3.8)]decane
    L2: bicyclo[2.1.1]hex-2-ene
    L2: methylidenebicyclo[2.2.1]heptane
    L2: bicyclo[2.2.0]hex-2-ene
    L2: bicyclo[2.2.0]hex-1(4)-ene
    L2: bicyclo[2.1.0]pent-1(4)-ene
    L2: bicyclo[2.1.0]pent-2-ene
    L2: tricyclo[4.4.0.0(3.9)]decane
"""
)

