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
1 * R u0
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
    rank = 10,
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
1 * Cs u0 {3,S} {4,S} {7,S}
2   Cs u0 {3,S} {5,S} {6,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {2,S} {4,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {1,S} {6,S}
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
1  * Cs u0 {3,S} {4,S} {7,S}
2    Cs u0 {3,S} {5,S} {6,S}
3    Cs u0 {1,S} {2,S}
4    Cs u0 {1,S} {5,S}
5    Cs u0 {2,S} {4,S}
6    Cs u0 {2,S} {7,S} {10,S}
7    Cs u0 {1,S} {6,S} {8,S}
8    Cs u0 {7,S} {9,S}
9    Cs u0 {8,S} {10,S}
10   Cs u0 {6,S} {9,S}
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
1  * Cs u0 {3,S} {4,S} {7,S}
2    Cs u0 {3,S} {5,S} {6,S}
3    Cs u0 {1,S} {2,S}
4    Cs u0 {1,S} {5,S}
5    Cs u0 {2,S} {4,S}
6    Cs u0 {2,S} {7,S} {10,S}
7    Cs u0 {1,S} {6,S} {8,S}
8    Cd u0 {7,S} {9,D}
9    Cd u0 {8,D} {10,S}
10   Cs u0 {6,S} {9,S}
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
1  * Cs u0 {2,S} {5,S} {9,S} {10,S}
2    Cs u0 {1,S} {3,S} {6,S}
3    Cs u0 {2,S} {4,S}
4    Cs u0 {3,S} {5,S}
5    Cs u0 {1,S} {4,S}
6    Cs u0 {2,S} {7,S}
7    Cs u0 {6,S} {8,S} {10,S}
8    Cs u0 {7,S} {9,S}
9    Cs u0 {1,S} {8,S}
10   Cs u0 {1,S} {7,S}
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
1  * Cs u0 {2,S} {9,S} {10,S}
2    Cs u0 {1,S} {3,S}
3    Cs u0 {2,S} {4,S} {8,S}
4    Cs u0 {3,S} {5,S} {10,S}
5    Cs u0 {4,S} {6,S}
6    Cs u0 {5,S} {7,S}
7    Cs u0 {6,S} {8,S}
8    Cs u0 {3,S} {7,S} {9,S}
9    Cs u0 {1,S} {8,S}
10   Cs u0 {1,S} {4,S}
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
1 * Cs u0 {3,S} {4,S} {7,S}
2   Cs u0 {3,S} {5,S} {6,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {2,S} {4,S}
6   C  u0 {2,S} {7,D}
7   C  u0 {1,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.51,-5.19333,-4.47333,-3.76,-3.44333,-2.94667,-2.47],'cal/(mol*K)','+|-',[2.72057,3.42407,4.84068,5.11681,5.13207,5.8757,8.29108]),
        H298 = (33.1097,'kcal/mol','+|-',24.8344),
        S298 = (53.2167,'cal/(mol*K)','+|-',9.77287),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species product6 from vinylCPD_H library.
Fitted from species product17 from vinylCPD_H library.
Fitted from species product23 from vinylCPD_H library.
""",
)

entry(
    index = 8,
    label = "exo-tricyclo[5.2.1.0(2.6)]dec-8-ene",
    group = 
"""
1  * Cs u0 {3,S} {4,S} {7,S}
2    Cs u0 {3,S} {5,S} {6,S}
3    Cs u0 {1,S} {2,S}
4    Cs u0 {1,S} {5,S} {8,S}
5    Cs u0 {2,S} {4,S} {10,S}
6    C  u0 {2,S} {7,D}
7    C  u0 {1,S} {6,D}
8    Cs u0 {4,S} {9,S}
9    Cs u0 {8,S} {10,S}
10   Cs u0 {5,S} {9,S}
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
1 * Cs u0 {3,S} {5,S} {6,S}
2   Cs u0 {3,S} {4,S} {7,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {5,S}
5   Cs u0 {1,S} {4,S}
6   Cs u0 {1,S} {8,S}
7   Cs u0 {2,S} {8,S}
8   Cs u0 {6,S} {7,S}
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
1  * Cs u0 {2,S} {6,S} {8,S}
2    Cs u0 {1,S} {3,S} {9,S}
3    Cs u0 {2,S} {4,S}
4    Cs u0 {3,S} {5,S} {10,S}
5    Cs u0 {4,S} {6,S} {7,S}
6    Cs u0 {1,S} {5,S}
7    Cs u0 {5,S} {8,S}
8    Cs u0 {1,S} {7,S}
9    Cs u0 {2,S} {10,S}
10   Cs u0 {4,S} {9,S}
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
1 * Cs u0 {3,S} {5,S} {6,S}
2   Cs u0 {3,S} {4,S} {7,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {5,S}
5   Cs u0 {1,S} {4,S}
6   C  u0 {1,S} {8,D}
7   Cs u0 {2,S} {8,S}
8   C  u0 {6,D} {7,S}
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
1   C  u0 {2,B} {3,S} {5,B}
2   C  u0 {1,B} {4,S} {6,B}
3   Cs u0 {1,S} {7,S}
4   Cs u0 {2,S} {7,S}
5   C  u0 {1,B} {8,B}
6   C  u0 {2,B} {9,B}
7 * Cs u0 {3,S} {4,S}
8   C  u0 {5,B} {9,B}
9   C  u0 {6,B} {8,B}
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
1   C  u0 {2,B} {3,S} {4,B}
2   C  u0 {1,B} {5,S} {6,B}
3 * Cs u0 {1,S} {7,S}
4   C  u0 {1,B} {8,B}
5   C  u0 {2,S} {7,D}
6   C  u0 {2,B} {9,B}
7   C  u0 {3,S} {5,D}
8   C  u0 {4,B} {9,B}
9   C  u0 {6,B} {8,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-3.07,-2.67,-2.42,-2.22,-2.2,-2.23,-2.04],'cal/(mol*K)'),
        H298 = (5.01,'kcal/mol'),
        S298 = (32.84,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species INDENE from C10H11 library.
""",
)

entry(
    index = 12,
    label = "cis-octahydro-1H-indene",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3   Cs u0 {1,S} {7,S}
4   Cs u0 {1,S} {8,S}
5   Cs u0 {2,S} {9,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   Cs u0 {4,S} {9,S}
9   Cs u0 {5,S} {8,S}
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
1  * Cs u0 {2,S} {3,S} {4,S}
2    Cs u0 {1,S} {5,S} {6,S}
3    Cs u0 {1,S} {9,S}
4    Cs u0 {1,S} {7,S}
5    Cs u0 {2,S} {8,S}
6    Cs u0 {2,S} {9,S} {10,S}
7    Cs u0 {4,S} {8,S} {10,S}
8    Cs u0 {5,S} {7,S}
9    Cs u0 {3,S} {6,S}
10   Cs u0 {6,S} {7,S}
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
1  * Cs u0 {2,S} {3,S} {4,S}
2    Cs u0 {1,S} {5,S} {6,S}
3    Cs u0 {1,S} {9,S}
4    Cs u0 {1,S} {7,S}
5    Cs u0 {2,S} {8,S}
6    Cs u0 {2,S} {9,S}
7    Cs u0 {4,S} {8,S} {10,S}
8    Cs u0 {5,S} {7,S}
9    Cs u0 {3,S} {6,S} {10,S}
10   Cs u0 {7,S} {9,S}
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
1   Cd u0 {2,S} {3,S} {4,D}
2   Cs u0 {1,S} {5,S} {6,S}
3 * Cs u0 {1,S} {7,S}
4   Cd u0 {1,D} {8,S}
5   Cs u0 {2,S} {9,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   Cs u0 {4,S} {9,S}
9   Cs u0 {5,S} {8,S}
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
1 * Cd u0 {2,S} {3,D} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cd u0 {1,D} {7,S}
4   Cs u0 {2,S} {7,S}
5   Cs u0 {2,S} {8,S}
6   Cs u0 {1,S} {9,S}
7   Cs u0 {3,S} {4,S}
8   Cs u0 {5,S} {9,S}
9   Cs u0 {6,S} {8,S}
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
1 * Cs u0 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {7,S}
4   Cs u0 {2,S} {7,S}
5   Cd u0 {2,S} {8,D}
6   Cs u0 {1,S} {9,S}
7   Cs u0 {3,S} {4,S}
8   Cd u0 {5,D} {9,S}
9   Cs u0 {6,S} {8,S}
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
1 * Cs u0 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {7,S}
4   Cs u0 {2,S} {7,S}
5   Cs u0 {2,S} {8,S}
6   Cs u0 {1,S} {9,S}
7   Cs u0 {3,S} {4,S}
8   Cd u0 {5,S} {9,D}
9   Cd u0 {6,S} {8,D}
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
1   Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D} {5,S} {6,S}
3 * Cs u0 {1,S} {7,S}
4   Cs u0 {1,S} {8,S}
5   Cs u0 {2,S} {9,S}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   Cs u0 {4,S} {9,S}
9   Cs u0 {5,S} {8,S}
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
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {5,S} {6,S}
3 * Cs u0 {1,S} {7,S}
4   Cs u0 {1,S} {8,S}
5   Cs u0 {2,S} {9,S}
6   Cd u0 {2,S} {7,D}
7   Cd u0 {3,S} {6,D}
8   Cs u0 {4,S} {9,S}
9   Cs u0 {5,S} {8,S}
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
1 * Cs u0 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {7,S}
4   Cs u0 {2,S} {7,S}
5   Cd u0 {2,S} {8,D}
6   Cd u0 {1,S} {9,D}
7   Cs u0 {3,S} {4,S}
8   Cd u0 {5,D} {9,S}
9   Cd u0 {6,D} {8,S}
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
1   Cd u0 {2,S} {3,S} {4,D}
2   Cs u0 {1,S} {5,S} {6,S}
3 * Cs u0 {1,S} {7,S}
4   Cd u0 {1,D} {8,S}
5   Cd u0 {2,S} {9,D}
6   Cs u0 {2,S} {7,S}
7   Cs u0 {3,S} {6,S}
8   Cs u0 {4,S} {9,S}
9   Cd u0 {5,D} {8,S}
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
1 * Cd u0 {2,D} {3,S} {6,S}
2   Cd u0 {1,D} {4,S} {5,S}
3   Cs u0 {1,S} {7,S}
4   Cs u0 {2,S} {7,S}
5   Cd u0 {2,S} {8,D}
6   Cs u0 {1,S} {9,S}
7   Cs u0 {3,S} {4,S}
8   Cd u0 {5,D} {9,S}
9   Cs u0 {6,S} {8,S}
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
1 * Cd u0 {2,D} {3,S} {6,S}
2   Cd u0 {1,D} {4,S} {5,S}
3   Cs u0 {1,S} {7,S}
4   Cs u0 {2,S} {7,S}
5   Cs u0 {2,S} {8,S}
6   Cs u0 {1,S} {9,S}
7   Cs u0 {3,S} {4,S}
8   Cd u0 {5,S} {9,D}
9   Cd u0 {6,S} {8,D}
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
1 * Cd u0 {2,S} {3,S} {6,D}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {7,S}
4   Cs u0 {2,S} {7,S}
5   Cs u0 {2,S} {8,S}
6   Cd u0 {1,D} {9,S}
7   Cs u0 {3,S} {4,S}
8   Cd u0 {5,S} {9,D}
9   Cd u0 {6,S} {8,D}
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
1 * Cd u0 {2,S} {3,S} {6,D}
2   Cd u0 {1,S} {4,S} {5,D}
3   Cs u0 {1,S} {7,S}
4   Cs u0 {2,S} {7,S}
5   Cd u0 {2,D} {8,S}
6   Cd u0 {1,D} {9,S}
7   Cs u0 {3,S} {4,S}
8   Cs u0 {5,S} {9,S}
9   Cs u0 {6,S} {8,S}
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
1 * Cs u0 {2,S} {3,S} {6,S}
2   Cd u0 {1,S} {4,D} {5,S}
3   Cs u0 {1,S} {7,S}
4   Cd u0 {2,D} {7,S}
5   Cd u0 {2,S} {8,D}
6   Cs u0 {1,S} {9,S}
7   Cs u0 {3,S} {4,S}
8   Cd u0 {5,D} {9,S}
9   Cs u0 {6,S} {8,S}
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
1 * Cs u0 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {7,S}
4   Cs u0 {2,S} {7,S}
5   Cs u0 {2,S} {8,S}
6   Cs u0 {1,S} {8,S}
7   Cs u0 {3,S} {4,S}
8   Cs u0 {5,S} {6,S}
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
1  * Cs u0 {2,S} {9,S} {10,S}
2    Cs u0 {1,S} {3,S}
3    Cs u0 {2,S} {4,S}
4    Cs u0 {3,S} {5,S} {10,S}
5    Cs u0 {4,S} {6,S}
6    Cs u0 {5,S} {7,S}
7    Cs u0 {6,S} {8,S} {10,S}
8    Cs u0 {7,S} {9,S}
9    Cs u0 {1,S} {8,S}
10   Cs u0 {1,S} {4,S} {7,S}
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
1    Cs u0 {2,S} {10,S}
2    Cs u0 {1,S} {3,S} {9,S}
3    Cs u0 {2,S} {4,S}
4  * Cs u0 {3,S} {5,S} {10,S}
5    Cs u0 {4,S} {6,S}
6    Cs u0 {5,S} {7,S}
7    Cs u0 {6,S} {8,S} {10,S}
8    Cs u0 {7,S} {9,S}
9    Cs u0 {2,S} {8,S}
10   Cs u0 {1,S} {4,S} {7,S}
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
1  * Cs u0 {2,S} {5,S} {8,S} {10,S}
2    Cs u0 {1,S} {3,S} {6,S}
3    Cs u0 {2,S} {4,S}
4    Cs u0 {3,S} {5,S}
5    Cs u0 {1,S} {4,S}
6    Cs u0 {2,S} {7,S} {9,S}
7    Cs u0 {6,S} {8,S}
8    Cs u0 {1,S} {7,S}
9    Cs u0 {6,S} {10,S}
10   Cs u0 {1,S} {9,S}
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
1  * Cs u0 {2,S} {5,S} {10,S}
2    Cs u0 {1,S} {3,S} {8,S}
3    Cs u0 {2,S} {4,S}
4    Cs u0 {3,S} {5,S}
5    Cs u0 {1,S} {4,S} {6,S}
6    Cs u0 {5,S} {7,S}
7    Cs u0 {6,S} {8,S}
8    Cs u0 {2,S} {7,S} {9,S}
9    Cs u0 {8,S} {10,S}
10   Cs u0 {1,S} {9,S}
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
1 * Cs u0 {2,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {5,S}
3   Cs u0 {2,S} {7,S}
4   Cd u0 {1,S} {7,D}
5   Cs u0 {2,S} {8,S}
6   Cs u0 {1,S} {8,S}
7   Cd u0 {3,S} {4,D}
8   Cs u0 {5,S} {6,S}
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
1 * Cs u0 {2,S} {4,S} {6,S}
2   Cd u0 {1,S} {3,D} {5,S}
3   Cd u0 {2,D} {7,S}
4   Cs u0 {1,S} {7,S}
5   Cs u0 {2,S} {8,S}
6   Cs u0 {1,S} {8,S}
7   Cs u0 {3,S} {4,S}
8   Cs u0 {5,S} {6,S}
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
1 * Cs u0 {2,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {5,S}
3   Cd u0 {2,S} {7,D}
4   Cs u0 {1,S} {7,S}
5   Cs u0 {2,S} {8,S}
6   Cd u0 {1,S} {8,D}
7   Cd u0 {3,D} {4,S}
8   Cd u0 {5,S} {6,D}
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
1 * Cs u0 {2,S} {4,S} {6,S}
2   Cs u0 {1,S} {3,S} {5,S}
3   Cd u0 {2,S} {7,D}
4   Cs u0 {1,S} {7,S}
5   Cd u0 {2,S} {8,D}
6   Cs u0 {1,S} {8,S}
7   Cd u0 {3,D} {4,S}
8   Cd u0 {5,D} {6,S}
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
1 * Cs u0 {2,S} {4,S} {6,S}
2   Cd u0 {1,S} {3,S} {5,D}
3   Cd u0 {2,S} {7,D}
4   Cs u0 {1,S} {7,S}
5   Cd u0 {2,D} {8,S}
6   Cs u0 {1,S} {8,S}
7   Cd u0 {3,D} {4,S}
8   Cs u0 {5,S} {6,S}
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
1 * Cd u0 {2,S} {4,S} {6,D}
2   Cs u0 {1,S} {3,S} {5,S}
3   Cd u0 {2,S} {7,D}
4   Cs u0 {1,S} {7,S}
5   Cs u0 {2,S} {8,S}
6   Cd u0 {1,D} {8,S}
7   Cd u0 {3,D} {4,S}
8   Cs u0 {5,S} {6,S}
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
1 * Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
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
1 * Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {5,S}
5   Cs u0 {1,S} {4,S}
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
1 * Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {4,S} {5,S}
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
1 * Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {6,[S,D]}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {4,[S,D]} {7,S}
7   Cs u0 {5,S} {6,S}
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
1 * Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {4,S} {7,S}
7   Cs u0 {5,S} {6,S}
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
1 * Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {6,D}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {4,D} {7,S}
7   Cs u0 {5,S} {6,S}
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
1  * Cs u0 {2,S} {3,S} {5,S}
2    Cs u0 {1,S} {3,S} {4,S}
3    Cs u0 {1,S} {2,S}
4    Cs u0 {2,S} {6,D}
5    Cs u0 {1,S} {7,S} {10,S}
6    Cs u0 {4,D} {7,S}
7    Cs u0 {5,S} {6,S} {8,S}
8    Cs u0 {7,S} {9,S}
9    Cs u0 {8,S} {10,S}
10   Cs u0 {5,S} {9,S}
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
1 * Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {4,S} {8,S}
7   Cs u0 {5,S} {8,S}
8   Cs u0 {6,S} {7,S}
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
1 * Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {7,S}
6   Cs u0 {4,S} {8,S}
7   Cs u0 {5,S} {9,S}
8   Cs u0 {6,S} {9,S}
9   Cs u0 {7,S} {8,S}
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
1 * C  u0 {3,S} {4,S} {7,S}
2   C  u0 {3,S} {5,S} {6,S}
3   Cs u0 {1,S} {2,S}
4   C  u0 {1,S} {5,D}
5   C  u0 {2,S} {4,D}
6   C  u0 {2,S} {7,D}
7   C  u0 {1,S} {6,D}
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
1  * C u0 {2,B} {4,S} {6,B}
2    C u0 {1,B} {3,S} {5,B}
3    C u0 {2,S} {4,B} {7,B}
4    C u0 {1,S} {3,B} {8,B}
5    C u0 {2,B} {9,B}
6    C u0 {1,B} {10,B}
7    C u0 {3,B} {11,B}
8    C u0 {4,B} {12,B}
9    C u0 {5,B} {10,B}
10   C u0 {6,B} {9,B}
11   C u0 {7,B} {12,B}
12   C u0 {8,B} {11,B}
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
1 * Cs u0 {2,S} {3,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {1,S} {4,S}
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
1 * Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
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
1 * Cs u0 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
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
1 * Cs u0 {3,S} {4,S} {5,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {1,S} {2,S}
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
1 * Cs u0 {3,S} {6,S} {8,S}
2   Cs u0 {4,S} {5,S} {7,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   Cs u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
7   Cs u0 {2,S} {8,S}
8   Cs u0 {1,S} {7,S}
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
1  * Cs u0 {2,S} {6,S} {10,S}
2    Cs u0 {1,S} {3,S}
3    Cs u0 {2,S} {4,S}
4    Cs u0 {3,S} {5,S} {9,S}
5    Cs u0 {4,S} {6,S}
6    Cs u0 {1,S} {5,S} {7,S}
7    Cs u0 {6,S} {8,S}
8    Cs u0 {7,S} {9,S}
9    Cs u0 {4,S} {8,S} {10,S}
10   Cs u0 {1,S} {9,S}
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
1 * Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {3,S} {4,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {2,S}
5   C  u0 {2,S} {6,D}
6   C  u0 {1,S} {5,D}
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
1 * Cs u0 {3,S} {4,S} {6,S}
2   Cs u0 {4,S} {5,S} {7,S}
3   Cd u0 {1,S} {5,S} {8,D}
4   Cs u0 {1,S} {2,S}
5   Cs u0 {2,S} {3,S}
6   Cs u0 {1,S} {7,S}
7   Cs u0 {2,S} {6,S}
8   Cd u0 {3,D}
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
1 * Cs u0 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {4,S}
4   Cs u0 {2,S} {3,S}
5   C  u0 {2,S} {6,D}
6   C  u0 {1,S} {5,D}
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
1   C  u0 {2,D} {4,S} {6,S}
2   C  u0 {1,D} {3,S} {5,S}
3 * Cs u0 {2,S} {4,S}
4   Cs u0 {1,S} {3,S}
5   Cs u0 {2,S} {6,S}
6   Cs u0 {1,S} {5,S}
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
1   C u0 {2,D} {3,S} {5,S}
2   C u0 {1,D} {3,S} {4,S}
3   C u0 {1,S} {2,S}
4 * C u0 {2,S} {5,S}
5   C u0 {1,S} {4,S}
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
1 * Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   C  u0 {2,S} {5,D}
5   C  u0 {1,S} {4,D}
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
1  * Cs u0 {4,S} {5,S} {6,S}
2    Cs u0 {3,S} {5,S} {7,S}
3    Cs u0 {2,S} {6,S} {10,S}
4    Cs u0 {1,S} {8,S} {9,S}
5    Cs u0 {1,S} {2,S}
6    Cs u0 {1,S} {3,S}
7    Cs u0 {2,S} {8,S}
8    Cs u0 {4,S} {7,S}
9    Cs u0 {4,S} {10,S}
10   Cs u0 {3,S} {9,S}
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

entry(
    index = 74,
    label = "product1",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {2,S} {6,D}
5   Cs u0 {1,S} {6,S}
6 * Cd u0 {4,D} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.53,-5.88833,-6.0675,-5.87167,-5.755,-5.22583,-3.91833],'cal/(mol*K)','+|-',[13.695,15.6123,16.4506,15.9745,14.9052,13.0715,9.23303]),
        H298 = (33.7772,'kcal/mol','+|-',4.36481),
        S298 = (75.9204,'cal/(mol*K)','+|-',29.7929),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species product1 from vinylCPD_H library.
Fitted from species product19 from vinylCPD_H library.
Fitted from species product19 from vinylCPD_H library.
Fitted from species product36 from vinylCPD_H library.
Fitted from species product39 from vinylCPD_H library.
Fitted from species pdt24 from C10H11 library.
Fitted from species pdt24 from C10H11 library.
Fitted from species pdt57 from C10H11 library.
Fitted from species biring1 from Fulvene_H library.
Fitted from species prod1 from naphthalene_H library.
Fitted from species prod3 from naphthalene_H library.
Fitted from species prod3 from naphthalene_H library.
""",
)

entry(
    index = 75,
    label = "product3",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S}
2   Cs u0 {1,S} {3,S} {6,S}
3 * Cs u0 {2,S} {4,S}
4   Cs u0 {1,S} {3,S}
5   Cs u0 {1,S} {7,S}
6   Cd u0 {2,S} {7,D}
7   Cd u0 {5,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.49,-5.912,-5.48,-4.912,-4.61,-4.122,-3.47],'cal/(mol*K)','+|-',[11.276,13.3805,14.1663,13.3764,12.968,11.469,9.42729]),
        H298 = (37.631,'kcal/mol','+|-',6.50583),
        S298 = (71.26,'cal/(mol*K)','+|-',32.7404),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species product3 from vinylCPD_H library.
Fitted from species product8 from vinylCPD_H library.
Fitted from species product25 from vinylCPD_H library.
Fitted from species pdt7 from C10H11 library.
Fitted from species pdt7 from C10H11 library.
""",
)

entry(
    index = 76,
    label = "product23",
    group = 
"""
1 * Cd u0 {3,S} {4,S} {6,D}
2   Cs u0 {3,S} {5,S} {7,S}
3   Cs u0 {1,S} {2,S}
4   Cs u0 {1,S} {5,S}
5   Cs u0 {2,S} {4,S}
6   Cd u0 {1,D} {7,S}
7   Cs u0 {2,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.785,-6.005,-5.34,-4.815,-4.35,-3.915,-3.05],'cal/(mol*K)','+|-',[8.69809,7.63302,6.62712,5.8579,4.61531,3.60941,2.13015]),
        H298 = (71.868,'kcal/mol','+|-',63.5123),
        S298 = (58.32,'cal/(mol*K)','+|-',1.69706),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species product23 from vinylCPD_H library.
Fitted from species product29 from vinylCPD_H library.
""",
)

entry(
    index = 77,
    label = "product25",
    group = 
"""
1 * Cd u0 {2,S} {4,S} {6,D}
2   Cs u0 {1,S} {3,S} {5,S}
3   Cs u0 {2,S} {4,S}
4   Cs u0 {1,S} {3,S}
5   Cs u0 {2,S} {7,S}
6   Cd u0 {1,D} {7,S}
7   Cs u0 {5,S} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.32,-5.85,-5.4,-4.81,-4.34,-3.92,-3.03],'cal/(mol*K)'),
        H298 = (45.173,'kcal/mol'),
        S298 = (60.95,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species product25 from vinylCPD_H library.
""",
)

entry(
    index = 78,
    label = "product29",
    group = 
"""
1 * Cd u0 {3,D} {5,S} {7,S}
2   Cs u0 {3,S} {4,S} {6,S}
3   Cd u0 {1,D} {2,S}
4   Cs u0 {2,S} {7,S}
5   Cs u0 {1,S} {6,S}
6   Cs u0 {2,S} {5,S}
7   Cs u0 {1,S} {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.05,-5.36,-4.88,-4.32,-3.96,-3.61,-2.87],'cal/(mol*K)'),
        H298 = (94.073,'kcal/mol'),
        S298 = (58.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species product29 from vinylCPD_H library.
""",
)

entry(
    index = 79,
    label = "product34",
    group = 
"""
1 * Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {3,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {1,S} {6,D}
5   Cd u0 {2,S} {7,D}
6   Cd u0 {4,D} {7,S}
7   Cd u0 {5,D} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.38,-4.49,-4.61,-4.23,-4.095,-3.75,-3.51],'cal/(mol*K)','+|-',[1.89346,4.02361,4.97034,5.32536,5.73956,5.79873,8.8756]),
        H298 = (41.913,'kcal/mol','+|-',20.8172),
        S298 = (62.305,'cal/(mol*K)','+|-',13.2229),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species product34 from vinylCPD_H library.
Fitted from species product46 from vinylCPD_H library.
""",
)

entry(
    index = 80,
    label = "product36",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4 * Cs u0 {2,S} {6,S}
5   Cs u0 {1,S} {6,S}
6   Cd u0 {4,S} {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.97,-4.68,-4.47,-4.27,-4.21,-3.94,-3.36],'cal/(mol*K)'),
        H298 = (32.543,'kcal/mol'),
        S298 = (65.1674,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species product36 from vinylCPD_H library.
""",
)

entry(
    index = 81,
    label = "product42",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cs u0 {1,S} {3,S} {5,S}
3 * Cd u0 {1,S} {2,S}
4   Cs u0 {1,S} {6,S}
5   Cd u0 {2,S} {6,D}
6   Cd u0 {4,S} {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.48,-3.9,-3.81,-3.6,-3.7,-3.68,-3.44],'cal/(mol*K)'),
        H298 = (47.323,'kcal/mol'),
        S298 = (66.8874,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species product42 from vinylCPD_H library.
""",
)

entry(
    index = 82,
    label = "product45",
    group = 
"""
1   Cs u0 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cd u0 {1,S} {4,D}
4   Cd u0 {2,S} {3,D}
5   Cd u0 {2,S} {7,D}
6   Cs u0 {1,S} {7,S}
7   Cd u0 {5,D} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.23,-4.36,-3.97,-3.6,-3.53,-3.44,-3.16],'cal/(mol*K)'),
        H298 = (39.483,'kcal/mol'),
        S298 = (62.16,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species product45 from vinylCPD_H library.
""",
)

entry(
    index = 83,
    label = "product46",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {4,D}
2   Cs u0 {1,S} {3,S} {5,S}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {1,D} {6,S}
5   Cs u0 {2,S} {7,S}
6   Cd u0 {4,S} {7,D}
7   Cd u0 {5,S} {6,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.31,-5.83,-5.92,-5.53,-5.17,-4.71,-3.89],'cal/(mol*K)'),
        H298 = (48.433,'kcal/mol'),
        S298 = (65.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species product46 from vinylCPD_H library.
""",
)

entry(
    index = 84,
    label = "product46-1",
    group = 
"""
1 * Cd u0 {2,S} {3,S} {5,D}
2   Cs u0 {1,S} {3,S} {4,S}
3   Cs u0 {1,S} {2,S}
4   Cd u0 {2,S} {7,D}
5   Cd u0 {1,D} {6,S}
6   Cs u0 {5,S} {7,S}
7   Cd u0 {4,D} {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.82,-4.74,-4.65,-4.52,-4.39,-4.28,-4.42],'cal/(mol*K)'),
        H298 = (53.563,'kcal/mol'),
        S298 = (63.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species product46 from vinylCPD_H library.
""",
)

entry(
    index = 85,
    label = "pdt8",
    group = 
"""
1  * Cs u0 {2,S} {3,S} {4,S}
2    Cs u0 {1,S} {5,S} {6,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {1,S} {9,S}
5    Cs u0 {2,S} {7,S}
6    Cd u0 {2,S} {8,D}
7    Cd u0 {3,D} {5,S}
8    Cd u0 {6,D} {10,S}
9    Cd u0 {4,S} {10,D}
10   Cd u0 {8,S} {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.535,-6.635,-6.36,-5.495,-4.605,-3.68,-2.31],'cal/(mol*K)','+|-',[3.13605,3.13605,2.84019,2.426,1.71595,1.18341,0.473366]),
        H298 = (13.728,'kcal/mol','+|-',10.9884),
        S298 = (54.235,'cal/(mol*K)','+|-',0.296985),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt8 from C10H11 library.
Fitted from species pdt23 from C10H11 library.
""",
)

entry(
    index = 86,
    label = "pdt8-1",
    group = 
"""
1    Cs u0 {2,S} {4,S} {6,S}
2    Cs u0 {1,S} {3,S} {5,S}
3  * Cs u0 {2,S} {7,S}
4    Cd u0 {1,S} {7,D}
5    Cd u0 {2,S} {8,D}
6    Cd u0 {1,S} {9,D}
7    Cd u0 {3,S} {4,D}
8    Cd u0 {5,D} {10,S}
9    Cd u0 {6,D} {10,S}
10   Cs u0 {8,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.31,-5.81,-5.33,-4.69,-3.97,-3.35,-2.88],'cal/(mol*K)'),
        H298 = (14.973,'kcal/mol'),
        S298 = (52.13,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt8 from C10H11 library.
""",
)

entry(
    index = 87,
    label = "pdt8-2",
    group = 
"""
1    Cs u0 {2,S} {3,S} {6,S}
2  * Cs u0 {1,S} {4,S} {5,S}
3    Cd u0 {1,S} {7,D}
4    Cs u0 {2,S} {9,S}
5    Cs u0 {2,S} {7,S}
6    Cd u0 {1,S} {8,D}
7    Cd u0 {3,D} {5,S}
8    Cd u0 {6,D} {10,S}
9    Cd u0 {4,S} {10,D}
10   Cd u0 {8,S} {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.3425,-7.0575,-5.85,-4.7975,-3.47,-2.58,-1.35],'cal/(mol*K)','+|-',[4.00405,3.66182,6.7465,8.34184,9.49513,9.23012,7.85553]),
        H298 = (6.758,'kcal/mol','+|-',29.8859),
        S298 = (51.8325,'cal/(mol*K)','+|-',9.6992),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt8 from C10H11 library.
Fitted from species pdt23 from C10H11 library.
Fitted from species pdt28 from C10H11 library.
Fitted from species pdt29 from C10H11 library.
""",
)

entry(
    index = 88,
    label = "pdt10bis",
    group = 
"""
1  * Cs u0 {2,S} {4,S} {6,S}
2    Cs u0 {1,S} {3,S} {5,S}
3    Cs u0 {2,S} {7,S}
4    Cs u0 {1,S} {8,S}
5    Cd u0 {2,S} {10,D}
6    Cd u0 {1,S} {9,D}
7    Cd u0 {3,S} {8,D}
8    Cd u0 {4,S} {7,D}
9    Cd u0 {6,D} {10,S}
10   Cd u0 {5,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.455,-6.46,-6.15,-5.28,-4.38,-3.47,-2.41],'cal/(mol*K)','+|-',[0.532536,0.946731,1.53844,1.65678,1.53844,1.30176,2.24849]),
        H298 = (3.073,'kcal/mol','+|-',13.7744),
        S298 = (52.44,'cal/(mol*K)','+|-',1.21622),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt10bis from C10H11 library.
Fitted from species pdt37 from C10H11 library.
""",
)

entry(
    index = 89,
    label = "pdt10bis-1",
    group = 
"""
1  * Cs u0 {2,S} {3,S} {4,S}
2    Cs u0 {1,S} {5,S} {6,S}
3    Cs u0 {1,S} {9,S}
4    Cd u0 {1,S} {10,D}
5    Cd u0 {2,S} {8,D}
6    Cd u0 {2,S} {7,D}
7    Cd u0 {6,D} {9,S}
8    Cd u0 {5,D} {10,S}
9    Cs u0 {3,S} {7,S}
10   Cd u0 {4,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.91,-7.26,-6.54,-5.57,-4.35,-3.43,-2.07],'cal/(mol*K)'),
        H298 = (7.733,'kcal/mol'),
        S298 = (54.59,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt10bis from C10H11 library.
""",
)

entry(
    index = 90,
    label = "pdt11",
    group = 
"""
1    Cs u0 {2,S} {3,S} {6,S}
2    Cd u0 {1,S} {4,D} {5,S}
3    Cd u0 {1,S} {8,D}
4    Cd u0 {2,D} {7,S}
5    Cd u0 {2,S} {10,D}
6    Cs u0 {1,S} {9,S}
7    Cd u0 {4,S} {9,D}
8    Cd u0 {3,D} {10,S}
9  * Cd u0 {6,S} {7,D}
10   Cd u0 {5,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.475,-10.72,-10,-8.715,-6.555,-5.06,-3.055],'cal/(mol*K)','+|-',[6.21292,6.62712,5.79873,4.4378,1.71595,0.355024,3.13605]),
        H298 = (1.5665,'kcal/mol','+|-',21.2797),
        S298 = (58.74,'cal/(mol*K)','+|-',4.18607),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt11 from C10H11 library.
Fitted from species prod4 from naphthalene_H library.
""",
)

entry(
    index = 91,
    label = "pdt17",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2  * Cs u0 {1,S} {8,S}
3    Cs u0 {1,S} {9,S}
4    Cs u0 {1,S} {7,S}
5    Cd u0 {1,S} {6,D}
6    Cd u0 {5,D} {10,S}
7    Cd u0 {4,S} {8,D}
8    Cd u0 {2,S} {7,D}
9    Cd u0 {3,S} {10,D}
10   Cd u0 {6,S} {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.34,-6.73,-6.55,-6.13,-5.34,-4.43,-2.23],'cal/(mol*K)'),
        H298 = (14.573,'kcal/mol'),
        S298 = (57.37,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt17 from C10H11 library.
""",
)

entry(
    index = 92,
    label = "pdt17-1",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2    Cs u0 {1,S} {8,S}
3    Cd u0 {1,S} {7,D}
4    Cd u0 {1,S} {6,D}
5    Cs u0 {1,S} {9,S}
6  * Cd u0 {4,D} {9,S}
7    Cd u0 {3,D} {10,S}
8    Cd u0 {2,S} {10,D}
9    Cs u0 {5,S} {6,S}
10   Cd u0 {7,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.72,-6.82,-6.48,-5.99,-5.19,-4.29,-2.12],'cal/(mol*K)'),
        H298 = (14.743,'kcal/mol'),
        S298 = (57.75,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt17 from C10H11 library.
""",
)

entry(
    index = 93,
    label = "pdt19",
    group = 
"""
1    Cs u0 {2,S} {4,S} {6,S}
2    Cd u0 {1,S} {3,D} {5,S}
3  * Cd u0 {2,D} {7,S}
4    Cs u0 {1,S} {9,S}
5    Cs u0 {2,S} {8,S}
6    Cs u0 {1,S} {10,S}
7    Cd u0 {3,S} {9,D}
8    Cd u0 {5,S} {10,D}
9    Cd u0 {4,S} {7,D}
10   Cd u0 {6,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.98,-7.21,-6.77,-5.84,-4.695,-3.755,-2.135],'cal/(mol*K)','+|-',[2.95853,2.36683,1.77512,1.4201,0.88756,0.650878,0.295853]),
        H298 = (2.333,'kcal/mol','+|-',14.9058),
        S298 = (51.955,'cal/(mol*K)','+|-',2.95571),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt19 from C10H11 library.
Fitted from species pdt37 from C10H11 library.
""",
)

entry(
    index = 94,
    label = "pdt19-1",
    group = 
"""
1    Cs u0 {2,S} {4,S} {6,S}
2    Cd u0 {1,S} {3,S} {5,D}
3    Cs u0 {2,S} {10,S}
4    Cd u0 {1,S} {7,D}
5    Cd u0 {2,D} {8,S}
6    Cs u0 {1,S} {9,S}
7  * Cd u0 {4,D} {10,S}
8    Cd u0 {5,S} {9,D}
9    Cd u0 {6,S} {8,D}
10   Cs u0 {3,S} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.27,-7.7,-6.87,-5.9,-4.53,-3.57,-2.03],'cal/(mol*K)'),
        H298 = (7.693,'kcal/mol'),
        S298 = (54.74,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt19 from C10H11 library.
""",
)

entry(
    index = 95,
    label = "pdt21",
    group = 
"""
1   Cs u0 {2,S} {4,S} {5,S}
2   Cd u0 {1,S} {3,D} {6,S}
3   Cd u0 {2,D} {8,S}
4   Cs u0 {1,S} {9,S}
5   Cs u0 {1,S} {7,S}
6   Cd u0 {2,S} {7,D}
7 * Cd u0 {5,S} {6,D}
8   Cd u0 {3,S} {9,D}
9   Cd u0 {4,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.07,-7.77333,-7.70333,-6.73333,-5.47333,-4.32333,-2.97333],'cal/(mol*K)','+|-',[3.26137,4.03866,3.95722,3.57416,2.7068,2.08753,1.35534]),
        H298 = (2.643,'kcal/mol','+|-',4.3516),
        S298 = (60.4632,'cal/(mol*K)','+|-',1.24756),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt21 from C10H11 library.
Fitted from species pdt27 from C10H11 library.
Fitted from species pdt32 from C10H11 library.
""",
)

entry(
    index = 96,
    label = "pdt21-1",
    group = 
"""
1   Cd u0 {2,S} {3,S} {6,D}
2   Cs u0 {1,S} {4,S} {5,S}
3 * Cs u0 {1,S} {7,S}
4   Cs u0 {2,S} {8,S}
5   Cd u0 {2,S} {7,D}
6   Cd u0 {1,D} {9,S}
7   Cd u0 {3,S} {5,D}
8   Cd u0 {4,S} {9,D}
9   Cd u0 {6,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.68,-6.81,-6.56,-5.84,-4.8,-3.99,-3.4],'cal/(mol*K)'),
        H298 = (6.863,'kcal/mol'),
        S298 = (57.6932,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt21 from C10H11 library.
""",
)

entry(
    index = 97,
    label = "pdt21-2",
    group = 
"""
1   Cs u0 {2,S} {3,S} {4,S}
2   Cd u0 {1,S} {5,D} {6,S}
3   Cs u0 {1,S} {9,S}
4   Cd u0 {1,S} {7,D}
5   Cd u0 {2,D} {7,S}
6   Cs u0 {2,S} {8,S}
7 * Cd u0 {4,D} {5,S}
8   Cd u0 {6,S} {9,D}
9   Cd u0 {3,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.68,-6.81,-6.56,-5.84,-4.8,-3.99,-3.4],'cal/(mol*K)'),
        H298 = (6.863,'kcal/mol'),
        S298 = (57.6932,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt21 from C10H11 library.
""",
)

entry(
    index = 98,
    label = "pdt21-3",
    group = 
"""
1   Cs u0 {2,S} {3,S} {5,S}
2   Cd u0 {1,S} {4,D} {6,S}
3   Cs u0 {1,S} {8,S}
4   Cd u0 {2,D} {7,S}
5   Cd u0 {1,S} {7,D}
6   Cd u0 {2,S} {9,D}
7   Cd u0 {4,S} {5,D}
8 * Cs u0 {3,S} {9,S}
9   Cd u0 {6,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.67,-8.62,-7.99,-7,-5.42,-4.27,-2.72],'cal/(mol*K)'),
        H298 = (2.023,'kcal/mol'),
        S298 = (61.7232,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt21 from C10H11 library.
""",
)

entry(
    index = 99,
    label = "pdt22",
    group = 
"""
1   Cd u0 {2,S} {4,S} {5,D}
2   Cs u0 {1,S} {3,S} {6,S}
3   Cd u0 {2,S} {8,D}
4   Cd u0 {1,S} {9,D}
5   Cd u0 {1,D} {7,S}
6   Cd u0 {2,S} {7,D}
7   Cd u0 {5,S} {6,D}
8 * Cd u0 {3,D} {9,S}
9   Cd u0 {4,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.63,-9.81,-9.04,-7.82,-5.95,-4.71,-3.23],'cal/(mol*K)'),
        H298 = (14.05,'kcal/mol'),
        S298 = (60.39,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt22 from C10H11 library.
""",
)

entry(
    index = 100,
    label = "pdt26",
    group = 
"""
1    Cd u0 {2,S} {3,D} {5,S}
2    Cd u0 {1,S} {4,S} {6,D}
3  * Cd u0 {1,D} {8,S}
4    Cs u0 {2,S} {10,S}
5    Cs u0 {1,S} {9,S}
6    Cd u0 {2,D} {7,S}
7    Cd u0 {6,S} {9,D}
8    Cd u0 {3,S} {10,D}
9    Cd u0 {5,S} {7,D}
10   Cd u0 {4,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-9.51,-10.83,-10.38,-9.04,-6.78,-5.2,-2.72],'cal/(mol*K)'),
        H298 = (10.33,'kcal/mol'),
        S298 = (53.47,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt26 from C10H11 library.
""",
)

entry(
    index = 101,
    label = "pdt27",
    group = 
"""
1   Cd u0 {2,D} {3,S} {5,S}
2   Cd u0 {1,D} {4,S} {6,S}
3 * Cd u0 {1,S} {7,D}
4   Cs u0 {2,S} {8,S}
5   Cs u0 {1,S} {9,S}
6   Cs u0 {2,S} {7,S}
7   Cd u0 {3,D} {6,S}
8   Cd u0 {4,S} {9,D}
9   Cd u0 {5,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.88,-7.18,-6.81,-6.07,-4.85,-4.06,-3.25],'cal/(mol*K)'),
        H298 = (6.883,'kcal/mol'),
        S298 = (58.0732,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt27 from C10H11 library.
""",
)

entry(
    index = 102,
    label = "pdt27-1",
    group = 
"""
1   Cd u0 {2,D} {3,S} {6,S}
2   Cd u0 {1,D} {4,S} {5,S}
3   Cd u0 {1,S} {9,D}
4   Cs u0 {2,S} {8,S}
5   Cs u0 {2,S} {7,S}
6   Cd u0 {1,S} {7,D}
7 * Cd u0 {5,S} {6,D}
8   Cs u0 {4,S} {9,S}
9   Cd u0 {3,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.57,-4.83,-4.71,-4.26,-4,-3.54,-3.01],'cal/(mol*K)'),
        H298 = (-2.777,'kcal/mol'),
        S298 = (59.5532,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt27 from C10H11 library.
""",
)

entry(
    index = 103,
    label = "pdt29",
    group = 
"""
1  * Cd u0 {2,S} {4,D} {6,S}
2    Cs u0 {1,S} {3,S} {5,S}
3    Cs u0 {2,S} {7,S}
4    Cd u0 {1,D} {8,S}
5    Cs u0 {2,S} {9,S}
6    Cd u0 {1,S} {7,D}
7    Cd u0 {3,S} {6,D}
8    Cd u0 {4,S} {10,D}
9    Cs u0 {5,S} {10,S}
10   Cd u0 {8,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.56,-9.04,-8.6,-7.5,-5.91,-4.62,-2.75],'cal/(mol*K)'),
        H298 = (0.693,'kcal/mol'),
        S298 = (56.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt29 from C10H11 library.
""",
)

entry(
    index = 104,
    label = "pdt29-1",
    group = 
"""
1    Cs u0 {2,S} {5,S} {6,S}
2    Cd u0 {1,S} {3,D} {4,S}
3    Cd u0 {2,D} {8,S}
4    Cd u0 {2,S} {7,D}
5    Cs u0 {1,S} {9,S}
6    Cs u0 {1,S} {7,S}
7    Cd u0 {4,D} {6,S}
8  * Cs u0 {3,S} {10,S}
9    Cd u0 {5,S} {10,D}
10   Cd u0 {8,S} {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.57,-7.23,-7.07,-6.34,-5.29,-4.34,-3.43],'cal/(mol*K)'),
        H298 = (6.033,'kcal/mol'),
        S298 = (53.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt29 from C10H11 library.
""",
)

entry(
    index = 105,
    label = "pdt29-2",
    group = 
"""
1  * Cs u0 {2,S} {3,S} {6,S}
2    Cd u0 {1,S} {4,S} {5,D}
3    Cs u0 {1,S} {8,S}
4    Cd u0 {2,S} {9,D}
5    Cd u0 {2,D} {7,S}
6    Cs u0 {1,S} {7,S}
7    Cs u0 {5,S} {6,S}
8    Cd u0 {3,S} {10,D}
9    Cd u0 {4,D} {10,S}
10   Cd u0 {8,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.56,-9.04,-8.6,-7.5,-5.91,-4.62,-2.75],'cal/(mol*K)'),
        H298 = (3.993,'kcal/mol'),
        S298 = (56.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt29 from C10H11 library.
""",
)

entry(
    index = 106,
    label = "pdt30",
    group = 
"""
1    Cs u0 {2,S} {3,S} {5,S}
2    Cd u0 {1,S} {4,S} {6,D}
3    Cs u0 {1,S} {8,S}
4    Cd u0 {2,S} {9,D}
5    Cd u0 {1,S} {7,D}
6    Cd u0 {2,D} {7,S}
7    Cd u0 {5,D} {6,S}
8  * Cd u0 {3,S} {10,D}
9    Cd u0 {4,D} {10,S}
10   Cd u0 {8,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.84,-11.12,-10.33,-8.95,-6.62,-4.99,-2.8],'cal/(mol*K)'),
        H298 = (14.29,'kcal/mol'),
        S298 = (58.23,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt30 from C10H11 library.
""",
)

entry(
    index = 107,
    label = "pdt31",
    group = 
"""
1    Cs u0 {2,S} {4,S} {6,S}
2    Cd u0 {1,S} {3,D} {5,S}
3  * Cd u0 {2,D} {9,S}
4    Cd u0 {1,S} {8,D}
5    Cd u0 {2,S} {7,D}
6    Cs u0 {1,S} {7,S}
7    Cd u0 {5,D} {6,S}
8    Cd u0 {4,D} {10,S}
9    Cd u0 {3,S} {10,D}
10   Cd u0 {8,S} {9,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.94,-11.19,-10.38,-8.99,-6.63,-5,-2.79],'cal/(mol*K)'),
        H298 = (11.73,'kcal/mol'),
        S298 = (57.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt31 from C10H11 library.
""",
)

entry(
    index = 108,
    label = "pdt32",
    group = 
"""
1   Cd u0 {2,S} {4,D} {5,S}
2   Cs u0 {1,S} {3,S} {6,S}
3   Cs u0 {2,S} {7,S}
4   Cd u0 {1,D} {8,S}
5   Cd u0 {1,S} {7,D}
6   Cd u0 {2,S} {9,D}
7 * Cd u0 {3,S} {5,D}
8   Cs u0 {4,S} {9,S}
9   Cd u0 {6,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.91,-7.09,-6.83,-6.08,-4.95,-4.08,-3.42],'cal/(mol*K)'),
        H298 = (5.483,'kcal/mol'),
        S298 = (58.2132,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt32 from C10H11 library.
""",
)

entry(
    index = 109,
    label = "pdt32-1",
    group = 
"""
1   Cs u0 {2,S} {3,S} {6,S}
2   Cs u0 {1,S} {4,S} {5,S}
3   Cs u0 {1,S} {7,S}
4   Cd u0 {2,S} {8,D}
5   Cd u0 {2,S} {7,D}
6   Cd u0 {1,S} {9,D}
7 * Cd u0 {3,S} {5,D}
8   Cd u0 {4,D} {9,S}
9   Cd u0 {6,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.78,-6.1,-4.92,-3.65,-2.41,-1.62,-0.77],'cal/(mol*K)'),
        H298 = (-15.727,'kcal/mol'),
        S298 = (49.8332,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt32 from C10H11 library.
""",
)

entry(
    index = 110,
    label = "pdt32-2",
    group = 
"""
1   Cs u0 {2,S} {4,S} {6,S}
2   Cd u0 {1,S} {3,D} {5,S}
3   Cd u0 {2,D} {7,S}
4   Cs u0 {1,S} {7,S}
5   Cd u0 {2,S} {9,D}
6   Cd u0 {1,S} {8,D}
7   Cs u0 {3,S} {4,S}
8 * Cd u0 {6,D} {9,S}
9   Cd u0 {5,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.9,-8.9,-8.26,-7.24,-5.57,-4.36,-2.74],'cal/(mol*K)'),
        H298 = (3.693,'kcal/mol'),
        S298 = (61.9332,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt32 from C10H11 library.
""",
)

entry(
    index = 111,
    label = "pdt35",
    group = 
"""
1    Cd u0 {2,D} {3,S} {6,S}
2    Cd u0 {1,D} {4,S} {5,S}
3  * Cs u0 {1,S} {8,S}
4    Cd u0 {2,S} {9,D}
5    Cd u0 {2,S} {7,D}
6    Cs u0 {1,S} {7,S}
7    Cd u0 {5,D} {6,S}
8    Cd u0 {3,S} {10,D}
9    Cd u0 {4,D} {10,S}
10   Cd u0 {8,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.52,-7.11,-6.7,-5.92,-4.93,-4.1,-2.95],'cal/(mol*K)'),
        H298 = (8.12,'kcal/mol'),
        S298 = (54.6,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt35 from C10H11 library.
""",
)

entry(
    index = 112,
    label = "pdt37",
    group = 
"""
1    Cd u0 {2,S} {4,D} {6,S}
2    Cs u0 {1,S} {3,S} {5,S}
3  * Cd u0 {2,S} {10,D}
4    Cd u0 {1,D} {7,S}
5    Cs u0 {2,S} {8,S}
6    Cs u0 {1,S} {9,S}
7    Cs u0 {4,S} {10,S}
8    Cd u0 {5,S} {9,D}
9    Cd u0 {6,S} {8,D}
10   Cd u0 {3,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.74,-6.32,-5.65,-4.95,-3.99,-3.38,-2.69],'cal/(mol*K)'),
        H298 = (2.193,'kcal/mol'),
        S298 = (48.91,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt37 from C10H11 library.
""",
)

entry(
    index = 113,
    label = "pdt38",
    group = 
"""
1  * Cd u0 {2,S} {3,S} {4,D}
2    Cd u0 {1,S} {5,D} {6,S}
3    Cs u0 {1,S} {8,S}
4    Cd u0 {1,D} {7,S}
5    Cd u0 {2,D} {10,S}
6    Cs u0 {2,S} {9,S}
7    Cd u0 {4,S} {10,D}
8    Cd u0 {3,S} {9,D}
9    Cd u0 {6,S} {8,D}
10   Cd u0 {5,S} {7,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.4,-11.67,-11.09,-9.63,-7.17,-5.47,-2.85],'cal/(mol*K)'),
        H298 = (-17.82,'kcal/mol'),
        S298 = (53.93,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt38 from C10H11 library.
""",
)

entry(
    index = 114,
    label = "pdt38-1",
    group = 
"""
1    Cb u0 {2,B} {4,B} {5,S}
2    Cb u0 {1,B} {3,S} {6,B}
3  * Cs u0 {2,S} {8,S}
4    Cb u0 {1,B} {10,B}
5    Cs u0 {1,S} {7,S}
6    Cb u0 {2,B} {9,B}
7    Cd u0 {5,S} {8,D}
8    Cd u0 {3,S} {7,D}
9    Cb u0 {6,B} {10,B}
10   Cb u0 {4,B} {9,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-1.68,-1.73,-1.85,-1.91,-2.19,-2.39,-2.51],'cal/(mol*K)'),
        H298 = (2.84,'kcal/mol'),
        S298 = (35.91,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species pdt38 from C10H11 library.
""",
)

entry(
    index = 115,
    label = "INDENE",
    group = 
"""
1   Cd u0 {2,S} {4,S} {5,D}
2   Cd u0 {1,S} {3,D} {6,S}
3 * Cd u0 {2,D} {9,S}
4   Cd u0 {1,S} {7,D}
5   Cd u0 {1,D} {8,S}
6   Cs u0 {2,S} {7,S}
7   Cd u0 {4,D} {6,S}
8   Cd u0 {5,S} {9,D}
9   Cd u0 {3,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.18,-9.06,-8.74,-7.88,-6.6,-5.53,-4.33],'cal/(mol*K)'),
        H298 = (-18.19,'kcal/mol'),
        S298 = (60.02,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species INDENE from C10H11 library.
""",
)

entry(
    index = 116,
    label = "INDENE-1",
    group = 
"""
1   Cd u0 {2,D} {3,S} {5,S}
2   Cd u0 {1,D} {4,S} {6,S}
3 * Cd u0 {1,S} {8,D}
4   Cd u0 {2,S} {9,D}
5   Cs u0 {1,S} {7,S}
6   Cd u0 {2,S} {7,D}
7   Cd u0 {5,S} {6,D}
8   Cd u0 {3,D} {9,S}
9   Cd u0 {4,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-8.18,-9.06,-8.74,-7.88,-6.6,-5.53,-4.33],'cal/(mol*K)'),
        H298 = (-18.19,'kcal/mol'),
        S298 = (60.02,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species INDENE from C10H11 library.
""",
)

entry(
    index = 117,
    label = "2HINDENE",
    group = 
"""
1   Cd u0 {2,S} {5,S} {6,D}
2   Cd u0 {1,S} {3,S} {4,D}
3 * Cd u0 {2,S} {8,D}
4   Cd u0 {2,D} {7,S}
5   Cd u0 {1,S} {9,D}
6   Cd u0 {1,D} {7,S}
7   Cs u0 {4,S} {6,S}
8   Cd u0 {3,D} {9,S}
9   Cd u0 {5,D} {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-4.49,-4.75,-4.62,-4.45,-4.55,-4.28,-4.48],'cal/(mol*K)'),
        H298 = (-0.61,'kcal/mol'),
        S298 = (58.88,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species 2HINDENE from C10H11 library.
""",
)

entry(
    index = 118,
    label = "prod2",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2  * Cs u0 {1,S} {8,S}
3    Cd u0 {1,S} {6,D}
4    Cd u0 {1,S} {9,D}
5    Cd u0 {1,S} {7,D}
6    Cd u0 {3,D} {10,S}
7    Cd u0 {5,D} {9,S}
8    Cd u0 {2,S} {10,D}
9    Cd u0 {4,D} {7,S}
10   Cd u0 {6,S} {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.54,-7.38,-7.43,-7.04,-6.22,-5.38,-3.12],'cal/(mol*K)'),
        H298 = (3.583,'kcal/mol'),
        S298 = (59.28,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species prod2 from naphthalene_H library.
""",
)

entry(
    index = 119,
    label = "prod2-1",
    group = 
"""
1    Cs u0 {2,S} {3,S} {4,S} {5,S}
2    Cd u0 {1,S} {7,D}
3    Cd u0 {1,S} {9,D}
4    Cd u0 {1,S} {8,D}
5    Cd u0 {1,S} {6,D}
6  * Cd u0 {5,D} {8,S}
7    Cd u0 {2,D} {10,S}
8    Cd u0 {4,D} {6,S}
9    Cd u0 {3,D} {10,S}
10   Cs u0 {7,S} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-5.98,-5.93,-5.62,-5.32,-5,-4.36,-3.36],'cal/(mol*K)'),
        H298 = (11.133,'kcal/mol'),
        S298 = (57.08,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species prod2 from naphthalene_H library.
""",
)

entry(
    index = 120,
    label = "prod4",
    group = 
"""
1    Cd u0 {2,S} {5,D} {6,S}
2    Cs u0 {1,S} {3,S} {4,S}
3  * Cd u0 {2,S} {8,D}
4    Cd u0 {2,S} {10,D}
5    Cd u0 {1,D} {7,S}
6    Cd u0 {1,S} {9,D}
7    Cs u0 {5,S} {8,S}
8    Cd u0 {3,D} {7,S}
9    Cd u0 {6,D} {10,S}
10   Cd u0 {4,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.57,-7.86,-7.37,-6.54,-5.25,-4.39,-3.88],'cal/(mol*K)'),
        H298 = (-1.957,'kcal/mol'),
        S298 = (55.67,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species prod4 from naphthalene_H library.
""",
)

entry(
    index = 121,
    label = "prod4-1",
    group = 
"""
1  * Cs u0 {2,S} {3,S} {4,S}
2    Cs u0 {1,S} {5,S} {6,S}
3    Cd u0 {1,S} {8,D}
4    Cd u0 {1,S} {9,D}
5    Cd u0 {2,S} {10,D}
6    Cd u0 {2,S} {7,D}
7    Cd u0 {6,D} {8,S}
8    Cd u0 {3,D} {7,S}
9    Cd u0 {4,D} {10,S}
10   Cd u0 {5,D} {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-10.33,-8.08,-6.33,-4.9,-3.09,-2.2,-1.2],'cal/(mol*K)'),
        H298 = (-22.037,'kcal/mol'),
        S298 = (49.84,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species prod4 from naphthalene_H library.
""",
)

entry(
    index = 122,
    label = "naphthalene",
    group = 
"""
1    Cd u0 {2,S} {4,D} {6,S}
2    Cd u0 {1,S} {3,S} {5,D}
3    Cd u0 {2,S} {7,D}
4    Cd u0 {1,D} {9,S}
5    Cd u0 {2,D} {8,S}
6    Cd u0 {1,S} {10,D}
7  * Cd u0 {3,D} {10,S}
8    Cd u0 {5,S} {9,D}
9    Cd u0 {4,S} {8,D}
10   Cd u0 {6,D} {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-7.54,-8.82,-8.92,-8.3,-7.22,-5.66,-4.34],'cal/(mol*K)'),
        H298 = (-41.44,'kcal/mol'),
        S298 = (59.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species naphthalene from naphthalene_H library.
""",
)

entry(
    index = 123,
    label = "naphthalene-1",
    group = 
"""
1    Cbf u0 {2,B} {3,B} {4,B}
2    Cbf u0 {1,B} {5,B} {6,B}
3    Cb  u0 {1,B} {9,B}
4    Cb  u0 {1,B} {8,B}
5    Cb  u0 {2,B} {10,B}
6  * Cb  u0 {2,B} {7,B}
7    Cb  u0 {6,B} {8,B}
8    Cb  u0 {4,B} {7,B}
9    Cb  u0 {3,B} {10,B}
10   Cb  u0 {5,B} {9,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-6.79295e-15,0,-1.35859e-14,-6.79295e-15,0,1.35859e-14,-1.35859e-14],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (-2.75,'cal/(mol*K)'),
    ),
    shortDesc = u"""Fitted from thermo library values""",
    longDesc = 
u"""
Fitted from species naphthalene from naphthalene_H library.
""",
)

entry(
    index = 124,
    label = "s1_3_6",
    group = 
"""
1 * C u0 {2,[S,D,T,B]} {6,[S,D,T,B]}
2   C u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3   C u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4   C u0 {3,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]} {8,[S,D,T,B]}
5   C u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6   C u0 {1,[S,D,T,B]} {5,[S,D,T,B]}
7   C u0 {4,[S,D,T,B]} {8,[S,D,T,B]}
8   C u0 {4,[S,D,T,B]} {7,[S,D,T,B]}
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 125,
    label = "s1_3_6_ane",
    group = 
"""
1 * C 0 {2,S} {6,S}
2   C 0 {1,S} {3,S}
3   C 0 {2,S} {4,S}
4   C 0 {3,S} {5,S} {7,S} {8,S}
5   C 0 {4,S} {6,S}
6   C 0 {1,S} {5,S}
7   C 0 {4,S} {8,S}
8   C 0 {4,S} {7,S}
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
    index = 126,
    label = "s1_3_6_ene",
    group = "OR{s1_3_6_ene_1, s1_3_6_ene_2}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 127,
    label = "s1_3_6_diene",
    group = "OR{s1_3_6_diene_1_4, s1_3_6_diene_1_3}",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 128,
    label = "s1_3_6_ene_1",
    group = 
"""
1 * C 0 {2,S} {6,S}
2   C 0 {1,S} {3,D}
3   C 0 {2,D} {4,S}
4   C 0 {3,S} {5,S} {7,S} {8,S}
5   C 0 {4,S} {6,S}
6   C 0 {1,S} {5,S}
7   C 0 {4,S} {8,S}
8   C 0 {4,S} {7,S}
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
    index = 129,
    label = "s1_3_6_ene_2",
    group =  
"""
1 * C 0 {2,D} {6,S}
2   C 0 {1,D} {3,S}
3   C 0 {2,S} {4,S}
4   C 0 {3,S} {5,S} {7,S} {8,S}
5   C 0 {4,S} {6,S}
6   C 0 {1,S} {5,S}
7   C 0 {4,S} {8,S}
8   C 0 {4,S} {7,S}
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
    index = 130,
    label = "s1_3_6_diene_1_4",
    group =   
"""
1 * C 0 {2,S} {6,S}
2   C 0 {1,S} {3,D}
3   C 0 {2,D} {4,S}
4   C 0 {3,S} {5,S} {7,S} {8,S}
5   C 0 {4,S} {6,D}
6   C 0 {1,S} {5,D}
7   C 0 {4,S} {8,S}
8   C 0 {4,S} {7,S}
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
    index = 131,
    label = "s1_3_6_diene_1_3",
    group =    
"""
1 * C 0 {2,S} {6,D}
2   C 0 {1,S} {3,D}
3   C 0 {2,D} {4,S}
4   C 0 {3,S} {5,S} {7,S} {8,S}
5   C 0 {4,S} {6,S}
6   C 0 {1,D} {5,S}
7   C 0 {4,S} {8,S}
8   C 0 {4,S} {7,S}
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
    L2: product1
    L2: product3
    L2: product23
    L2: product25
    L2: product29
    L2: product34
    L2: product36
    L2: product42
    L2: product45
    L2: product46
    L2: product46-1
    L2: pdt8
    L2: pdt8-1
    L2: pdt8-2
    L2: pdt10bis
    L2: pdt10bis-1
    L2: pdt11
    L2: pdt17
    L2: pdt17-1
    L2: pdt19
    L2: pdt19-1
    L2: pdt21
    L2: pdt21-1
    L2: pdt21-2
    L2: pdt21-3
    L2: pdt22
    L2: pdt26
    L2: pdt27
    L2: pdt27-1
    L2: pdt29
    L2: pdt29-1
    L2: pdt29-2
    L2: pdt30
    L2: pdt31
    L2: pdt32
    L2: pdt32-1
    L2: pdt32-2
    L2: pdt35
    L2: pdt37
    L2: pdt38
    L2: pdt38-1
    L2: INDENE
    L2: INDENE-1
    L2: 2HINDENE
    L2: prod2
    L2: prod2-1
    L2: prod4
    L2: prod4-1
    L2: naphthalene
    L2: naphthalene-1
    L2: s1_3_6
        L3: s1_3_6_ane
        L3: s1_3_6_ene
            L4: s1_3_6_ene_1
            L4: s1_3_6_ene_2
        L3: s1_3_6_diene
            L4: s1_3_6_diene_1_4
            L4: s1_3_6_diene_1_3
"""
)

