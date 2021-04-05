#!/usr/bin/env python
# encoding: utf-8

name = "Chlorination"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "1230xa",
    molecule =
"""
1 Cl u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3 C  u0 p0 c0 {2,S} {4,S} {5,D}
4 Cl u0 p3 c0 {3,S}
5 C  u0 p0 c0 {3,D} {6,S} {7,S}
6 Cl u0 p3 c0 {5,S}
7 Cl u0 p3 c0 {5,S}
8 H  u0 p0 c0 {2,S}
9 H  u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([28.046,31.867,34.851,37.2015,40.58,42.80,45.83],'cal/(mol*K)'),
        H298 = (-26.053,'kcal/mol'),
        S298 = (93.522,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)


entry(
    index = 2,
    label = "HCL",
    molecule =
"""
1 Cl u0 p3 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([ 6.945,6.9431,6.973,7.033,7.222,7.451,7.972],'cal/(mol*K)'),
        H298 = (-22.06,'kcal/mol'),
        S298 = (44.670,'cal/(mol*K)'),
    ),
    shortDesc = u"""NIST""",
    longDesc =
u"""

""",
)

entry(
    index = 3,
    label = "C3H3Cl3",
    molecule =
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 Cl u0 p3 c0 {2,S}
8 Cl u0 p3 c0 {3,S}
9 Cl u0 p3 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.67,20,22.74,25.63,27.60,29.77,30.58],'cal/(mol*K)'),
        H298 = (-15.2,'kcal/mol'),
        S298 = (85.33,'cal/(mol*K)'),
    ),
    shortDesc = u"""NIST""",
    longDesc =
u"""

""",
)

#entry(
#    index = 4,
#    label = "1,1,1,2,3-pentachloropropane",
#    molecule =
#"""
#1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
#2 C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
#3 C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
#4 H u0 p0 c0 {1,S}
#5 Cl u0 p3 c0 {1,S}
#6 Cl u0 p3 c0 {3,S}
#7 Cl u0 p3 c0 {2,S}
#8 H u0 p0 c0 {2,S}
#9 H u0 p0 c0 {2,S}
#10 Cl u0 p3 c0 {3,S}
#11 Cl u0 p3 c0 {3,S}
#""",
#    thermo = ThermoData(
#        Tdata = ([300,400,500,600,800,1000,1500],'K'),
#        Cpdata = ([34.04,38.44,41.68,44.31,47.85,50.47,53.21],'cal/(mol*K)'),
#        H298 = (-53.3,'kcal/mol'),
#        S298 = (105.15,'cal/(mol*K)'),
#    ),
#    shortDesc = u"""CBS-QB3 calcs""",
 #   longDesc =
#u"""
#
#""",
#)

entry(
    index = 5,
    label = "ClCC(Cl)(Cl)C(Cl)(Cl)Cl",
    molecule =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3 C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4 Cl u0 p3 c0 {1,S}
5 Cl u0 p3 c0 {1,S}
6 Cl u0 p3 c0 {3,S}
7 Cl u0 p3 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
10 Cl u0 p3 c0 {3,S}
11 Cl u0 p3 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([37.24,41.54,45.18,48.11,50.75,53.78,56.01],'cal/(mol*K)'),
        H298 = (-59.5,'kcal/mol'),
        S298 = (108.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)

entry(
    index = 6,
    label = "Cl",
    molecule =
"""
1 Cl u1 p3 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.968,4.968,4.968,4.968,4.968,4.968,4.968],'cal/(mol*K)'),
        H298 = (29.347,'kcal/mol'),
        S298 = (37.959,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)



entry(
    index = 7,
    label = "Cl2",
    molecule =
"""
1 Cl u0 p3 c0 {2,S}
2 Cl u0 p3 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.957,8.266,8.491,8.642,8.796,8.846,8.873],'cal/(mol*K)'),
        H298 = (-0.685,'kcal/mol'),
        S298 = (53.383,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)

entry(
    index = 8,
    label = "CH2Cl",
    molecule =
"""
1 C  u1 p0 c0 {2,S} {3,S} {4,S}
2 Cl u0 p3 c0 {1,S}
3 H  u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.987,11.160 ,12.171,13.025,14.364,15.361,16.996 ],'cal/(mol*K)'),
        H298 = (28.606,'kcal/mol'),
        S298 = (57.651,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)

entry(
    index = 9,
    label = "CHCl2",
    molecule =
"""
1 Cl u0 p3 c0 {2,S}
2 C  u1 p0 c0 {1,S} {3,S} {4,S}
3 Cl u0 p3 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.907,13.296,14.418,15.293,16.484,17.210,18.224],'cal/(mol*K)'),
        H298 = (20.597,'kcal/mol'),
        S298 = (65.728,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)

entry(
    index = 10,
    label = "rad1",
    molecule =
"""
1 C  u0 p0 c0 {2,D} {7,S} {8,S}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 Cl u0 p3 c0 {2,S}
4 C  u1 p0 c0 {2,S} {5,S} {6,S}
5 Cl u0 p3 c0 {4,S}
6 Cl u0 p3 c0 {4,S}
7 H  u0 p0 c0 {1,S}
8 H  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.735 ,28.138 ,30.686,32.652,35.457,37.330,39.985],'cal/(mol*K)'),
        H298 = (19.949,'kcal/mol'),
        S298 = (87.920,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)

entry(
    index = 11,
    label = "rad2",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  Cl u0 p3 c0 {1,S}
3  Cl u0 p3 c0 {1,S}
4  Cl u0 p3 c0 {1,S}
5  C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6  Cl u0 p3 c0 {5,S}
7  Cl u0 p3 c0 {5,S}
8  C  u1 p0 c0 {5,S} {9,S} {10,S}
9  Cl u0 p3 c0 {8,S}
10 H  u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([38.167 ,42.155 ,44.960,47.005,49.701,51.321,53.316],'cal/(mol*K)'),
        H298 = (-10.101,'kcal/mol'),
        S298 = (111.697,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)


entry(
    index = 12,
    label = "rad3",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  Cl u0 p3 c0 {1,S}
3  Cl u0 p3 c0 {1,S}
4  C  u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  Cl u0 p3 c0 {4,S}
6  Cl u0 p3 c0 {4,S}
7  C  u1 p0 c0 {4,S} {8,S} {10,S}
8  Cl u0 p3 c0 {7,S}
9  H  u0 p0 c0 {1,S}
10 H  u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.416 ,37.606 ,40.792,43.253,46.702,48.914,51.842],'cal/(mol*K)'),
        H298 = (-6.900,'kcal/mol'),
        S298 = (104.456,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)


entry(
    index = 13,
    label = "rad4",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  Cl u0 p3 c0 {1,S}
3  Cl u0 p3 c0 {1,S}
4  Cl u0 p3 c0 {1,S}
5  C  u0 p0 c0 {1,S} {6,S} {7,S} {9,S}
6  Cl u0 p3 c0 {5,S}
7  C  u1 p0 c0 {5,S} {8,S} {10,S}
8  Cl u0 p3 c0 {7,S}
9  H  u0 p0 c0 {5,S}
10 H  u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.355 ,37.552 ,40.741,43.204,46.660,48.879,51.823],'cal/(mol*K)'),
        H298 = (-5.818,'kcal/mol'),
        S298 = (103.998,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)




entry(
    index = 14,
    label = "rad5",
    molecule =
"""
1  C  u1 p0 c0 {2,S} {3,S} {4,S}
2  Cl u0 p3 c0 {1,S}
3  Cl u0 p3 c0 {1,S}
4  C  u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  Cl u0 p3 c0 {4,S}
6  Cl u0 p3 c0 {4,S}
7  C  u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  Cl u0 p3 c0 {7,S}
9  H  u0 p0 c0 {7,S}
10 H  u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([32.659 ,36.796 ,40.030,42.574,46.192,48.535,51.647],'cal/(mol*K)'),
        H298 = (-12.848,'kcal/mol'),
        S298 = (104.027,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)


entry(
    index = 15,
    label = "rad6",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  Cl u0 p3 c0 {1,S}
3  C  u1 p0 c0 {1,S} {4,S} {5,S}
4  Cl u0 p3 c0 {3,S}
5  C  u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
6  Cl u0 p3 c0 {5,S}
7  Cl u0 p3 c0 {5,S}
8  Cl u0 p3 c0 {5,S}
9  H  u0 p0 c0 {1,S}
10 H  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([32.837 ,36.982 ,40.212 ,42.744,46.332 ,48.646,51.703],'cal/(mol*K)'),
        H298 = (-8.758,'kcal/mol'),
        S298 = (105.970,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)

entry(
    index = 16,
    label = "1230xf",
    molecule =
"""
1 C  u0 p0 c0 {2,D} {8,S} {9,S}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 Cl u0 p3 c0 {2,S}
4 C  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 Cl u0 p3 c0 {4,S}
6 Cl u0 p3 c0 {4,S}
7 Cl u0 p3 c0 {4,S}
8 H  u0 p0 c0 {1,S}
9 H  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.148 ,33.230 ,36.160 ,38.345,41.360,43.317,46.044],'cal/(mol*K)'),
        H298 = (-20.637,'kcal/mol'),
        S298 = (90.801,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)

entry(
    index = 17,
    label = "240ab",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  Cl u0 p3 c0 {2,S}
4  Cl u0 p3 c0 {2,S}
5  C  u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  Cl u0 p3 c0 {5,S}
7  Cl u0 p3 c0 {5,S}
8  Cl u0 p3 c0 {5,S}
9  H  u0 p0 c0 {1,S}
10 H  u0 p0 c0 {1,S}
11 H  u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([34.381 ,38.923 ,42.375 ,45.109,49.149,51.939,55.980],'cal/(mol*K)'),
        H298 = (-58.083,'kcal/mol'),
        S298 = (98.307,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)

entry(
    index = 18,
    label = "240db",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  Cl u0 p3 c0 {1,S}
3  C  u0 p0 c0 {1,S} {4,S} {5,S} {11,S}
4  Cl u0 p3 c0 {3,S}
5  C  u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
6  Cl u0 p3 c0 {5,S}
7  Cl u0 p3 c0 {5,S}
8  Cl u0 p3 c0 {5,S}
9  H  u0 p0 c0 {1,S}
10 H  u0 p0 c0 {1,S}
11 H  u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([33.630  ,38.464 ,42.240  ,45.229,49.554,52.436,56.425],'cal/(mol*K)'),
        H298 = (-54.049,'kcal/mol'),
        S298 = (99.599,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)


entry(
    index = 19,
    label = "250fb",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  Cl u0 p3 c0 {1,S}
3  C  u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
4  C  u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5  Cl u0 p3 c0 {4,S}
6  Cl u0 p3 c0 {4,S}
7  Cl u0 p3 c0 {4,S}
8  H  u0 p0 c0 {1,S}
9  H  u0 p0 c0 {1,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([30.008,34.775,38.707,41.947,46.832,50.216,55.080],'cal/(mol*K)'),
        H298 = (-49.253,'kcal/mol'),
        S298 = (94.098,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)



entry(
    index = 20,
    label = "1240za",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,D}
2 Cl u0 p3 c0 {1,S}
3 Cl u0 p3 c0 {1,S}
4 C  u0 p0 c0 {1,D} {5,S} {7,S}
5 C  u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
6 Cl u0 p3 c0 {5,S}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {5,S}
9 H  u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.731,26.651,29.819,32.388,36.213,38.844,42.624 ],'cal/(mol*K)'),
        H298 = (-13.244,'kcal/mol'),
        S298 = (82.453,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)


entry(
    index = 21,
    label = "1240zf",
    molecule =
"""
1 C  u0 p0 c0 {2,D} {7,S} {8,S}
2 C  u0 p0 c0 {1,D} {3,S} {9,S}
3 C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 Cl u0 p3 c0 {3,S}
5 Cl u0 p3 c0 {3,S}
6 Cl u0 p3 c0 {3,S}
7 H  u0 p0 c0 {1,S}
8 H  u0 p0 c0 {1,S}
9 H  u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.729,27.813,30.918,33.325,36.797,39.189,42.773],'cal/(mol*K)'),
        H298 = (-7.364,'kcal/mol'),
        S298 = (81.149,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)


entry(
    index = 22,
    label = "CC(Cl)C",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C  u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3  Cl u0 p3 c0 {2,S}
4  C  u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  H  u0 p0 c0 {1,S}
6  H  u0 p0 c0 {1,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {4,S}
10 H  u0 p0 c0 {4,S}
11 H  u0 p0 c0 {4,S}
""",
    thermo = Wilhoit(
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (257.749, 'J/(mol*K)'),
        a0 = -2.74468,
        a1 = 3.80647,
        a2 = -8.18262,
        a3 = 5.18858,
        H0 = (-96.5735, 'kJ/mol'),
        S0 = (-1382.47, 'J/(mol*K)'),
        B = (685.282, 'K'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)


entry(
    index = 23,
    label = "C[C](Cl)C",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C  u1 p0 c0 {1,S} {3,S} {4,S}
3  Cl u0 p3 c0 {2,S}
4  C  u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
5  H  u0 p0 c0 {1,S}
6  H  u0 p0 c0 {1,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {4,S}
9  H  u0 p0 c0 {4,S}
10 H  u0 p0 c0 {4,S}
""",
    thermo = Wilhoit(
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (232.805, 'J/(mol*K)'),
        a0 = -3.59945,
        a1 = 13.6356,
        a2 = -21.6418,
        a3 = 9.46726,
        H0 = (-51.9955, 'kJ/mol'),
        S0 = (-1122.89, 'J/(mol*K)'),
        B = (432.452, 'K'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)


entry(
    index = 24,
    label = "CCC",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = Wilhoit(
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (257.749, 'J/(mol*K)'),
        a0 = -4.25899,
        a1 = -5.10272,
        a2 = 16.4936,
        a3 = -9.55006,
        H0 = (-968.741, 'kJ/mol'),
        S0 = (-1537.05, 'J/(mol*K)'),
        B = (1271.61, 'K'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)


entry(
    index = 25,
    label = "C[CH]C",
    molecule =
"""
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
    thermo = Wilhoit(
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (232.805, 'J/(mol*K)'),
        a0 = -2.29417,
        a1 = 10.502,
        a2 = -10.6501,
        a3 = 0.0593513,
        H0 = (-52.0716, 'kJ/mol'),
        S0 = (-1068.19, 'J/(mol*K)'),
        B = (300, 'K'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)



entry(
    index = 26,
    label = "CC=CCl",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C  u0 p0 c0 {1,S} {3,D} {8,S}
3 C  u0 p0 c0 {2,D} {4,S} {9,S}
4 Cl u0 p3 c0 {3,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {1,S}
8 H  u0 p0 c0 {2,S}
9 H  u0 p0 c0 {3,S}
""",
    thermo = Wilhoit(
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (199.547, 'J/(mol*K)'),
        a0 = 0.730089,
        a1 = -6.71949,
        a2 = 5.66936,
        a3 = -1.92764,
        H0 = (-166.516, 'kJ/mol'),
        S0 = (-963.145, 'J/(mol*K)'),
        B = (544.223, 'K'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)



entry(
    index = 27,
    label = "CC=[C]Cl",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C  u0 p0 c0 {1,S} {3,D} {8,S}
3 C  u1 p0 c0 {2,D} {4,S}
4 Cl u0 p3 c0 {3,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {1,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = Wilhoit(
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (174.604, 'J/(mol*K)'),
        a0 = -23.4455,
        a1 = 74.6316,
        a2 = -103.81,
        a3 = 55.3938,
        H0 = (10942.8, 'kJ/mol'),
        S0 = (-991.024, 'J/(mol*K)'),
        B = (2082.28, 'K'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)



entry(
    index = 28,
    label = "CC=C",
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
    thermo = Wilhoit(
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (199.547, 'J/(mol*K)'),
        a0 = 2.54589,
        a1 = -11.3365,
        a2 = 9.2321,
        a3 = -2.69286,
        H0 = (-137.342, 'kJ/mol'),
        S0 = (-995.616, 'J/(mol*K)'),
        B = (587.976, 'K'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)



entry(
    index = 29,
    label = "CC=[CH]",
    molecule =
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u1 p0 c0 {2,D} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = Wilhoit(
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (174.604, 'J/(mol*K)'),
        a0 = 2.32723,
        a1 = -8.05561,
        a2 = 6.47757,
        a3 = -3.14449,
        H0 = (110.742, 'kJ/mol'),
        S0 = (-795.629, 'J/(mol*K)'),
        B = (453.092, 'K'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)



entry(
    index = 30,
    label = "CCC(Cl)(Cl)",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C  u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C  u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
4  Cl u0 p3 c0 {3,S}
5  Cl u0 p3 c0 {3,S}
6  H  u0 p0 c0 {1,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {1,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {2,S}
11 H  u0 p0 c0 {3,S}
""",
    thermo = Wilhoit(
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (257.749, 'J/(mol*K)'),
        a0 = -2.50126,
        a1 = 8.29092,
        a2 = -12.7317,
        a3 = 4.74044,
        H0 = (-289.151, 'kJ/mol'),
        S0 = (-1236.11, 'J/(mol*K)'),
        B = (389.142, 'K'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)



entry(
    index = 31,
    label = "CC[C](Cl)(Cl)",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C  u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C  u1 p0 c0 {2,S} {4,S} {5,S}
4  Cl u0 p3 c0 {3,S}
5  Cl u0 p3 c0 {3,S}
6  H  u0 p0 c0 {1,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {1,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {2,S}
""",
    thermo = Wilhoit(
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (232.805, 'J/(mol*K)'),
        a0 = -2.9388,
        a1 = 9.53147,
        a2 = -12.0944,
        a3 = 3.26826,
        H0 = (-92.597, 'kJ/mol'),
        S0 = (-1056.06, 'J/(mol*K)'),
        B = (334.536, 'K'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)


entry(
    index = 32,
    label = "CCCCl",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C  u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C  u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  Cl u0 p3 c0 {3,S}
5  H  u0 p0 c0 {1,S}
6  H  u0 p0 c0 {1,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
""",
    thermo = Wilhoit(
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (257.749, 'J/(mol*K)'),
        a0 = -1.08769,
        a1 = 6.42838,
        a2 = -9.46155,
        a3 = 1.8086,
        H0 = (-287.142, 'kJ/mol'),
        S0 = (-1220.68, 'J/(mol*K)'),
        B = (334.178, 'K'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)


entry(
    index = 33,
    label = "CC[CH]Cl",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C  u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C  u1 p0 c0 {2,S} {4,S} {10,S}
4  Cl u0 p3 c0 {3,S}
5  H  u0 p0 c0 {1,S}
6  H  u0 p0 c0 {1,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {3,S}
""",
    thermo = Wilhoit(
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (232.805, 'J/(mol*K)'),
        a0 = -1.59909,
        a1 = 6.2616,
        a2 = -6.96961,
        a3 = 1.69161e-06,
        H0 = (-71.4289, 'kJ/mol'),
        S0 = (-1059.89, 'J/(mol*K)'),
        B = (318.456, 'K'),
    ),
    shortDesc = u"""CBS-QB3 calcs""",
    longDesc =
u"""

""",
)


#entry(
#    index = 34,
#    label = "CCC",
#    molecule =
#"""
#1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
#2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
#3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
#4  H u0 p0 c0 {1,S}
#5  H u0 p0 c0 {1,S}
#6  H u0 p0 c0 {1,S}
#7  H u0 p0 c0 {2,S}
#8  H u0 p0 c0 {2,S}
#9  H u0 p0 c0 {3,S}
#10 H u0 p0 c0 {3,S}
#11 H u0 p0 c0 {3,S}
#""",
#    thermo = Wilhoit(
#        Cp0 = (33.2579, 'J/(mol*K)'),
#        CpInf = (257.749, 'J/(mol*K)'),
#        a0 = -4.25899,
#        a1 = -5.10272,
#        a2 = 16.4936,
#        a3 = -9.55006,
#        H0 = (-968.741, 'kJ/mol'),
#        S0 = (-1537.05, 'J/(mol*K)'),
#        B = (1271.61, 'K'),
#    ),
#    shortDesc = u"""CBS-QB3 calcs""",
#    longDesc =
#u"""
#
#""",
#)
#
#
#
#entry(
#    index = 35,
#    label = "CC[CH2]",
#    molecule =
#"""
#1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
#2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
#3  C u1 p0 c0 {2,S} {9,S} {10,S}
#4  H u0 p0 c0 {1,S}
#5  H u0 p0 c0 {1,S}
#6  H u0 p0 c0 {1,S}
#7  H u0 p0 c0 {2,S}
#8  H u0 p0 c0 {2,S}
#9  H u0 p0 c0 {3,S}
#10 H u0 p0 c0 {3,S}
#""",
#    thermo = Wilhoit(
#        Cp0 = (33.2579, 'J/(mol*K)'),
#        CpInf = (232.805, 'J/(mol*K)'),
#        a0 = -1.48103,
#        a1 = 7.45716,
#        a2 = -8.32216,
#        a3 = -1.20369e-06,
#        H0 = (-33.5017, 'kJ/mol'),
#        S0 = (-1076.04, 'J/(mol*K)'),
#        B = (319.315, 'K'),
#    ),
#    shortDesc = u"""CBS-QB3 calcs""",
#    longDesc =
#u"""
#
#""",
#)


entry(
    index = 2,
    label = "CH3Cl",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 Cl u0 p3 c0 {1,S}
3 H  u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials=[
            NASAPolynomial(coeffs=[3.96612,-0.00505693,4.02006e-05,-4.82782e-08,1.86722e-11,-11073,5.70447],
            Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.97884,0.00791729,-2.81714e-06,4.51716e-10,-2.69086e-14,-11676.2,2.58273],
            Tmin=(1000,'K'), Tmax=(6000,'K'))],
        Tmin=(200,'K'), Tmax=(6000,'K'),
        comment="""tpis91"""),
    shortDesc = u"""Burcat/Ruscic """,
    longDesc =
u"""
See http://www.ipd.anl.gov/anlpubs/2005/07/53802.pdf
74-87-3
CH3CL	METHYL CHLORIDE  SIGMA=3  STATWT=1  IAIBIC=3039.28  Nu=2968,1356,731,
3039(2),1452(2),1017(2)  HF298=-81.87+/-0.6 kJ HF0=-73.94 kJ  REF=Gurvich 91
{HF298=-82.562+/-0.35 kJ  REF=ATcT A; HF298=-80. kJ   REF=Burcat G3B3 calc 2008;
HF298=-81.966 kJ REF=TRC 12/81;  HF298=-83.68 kJ  REF=Kromkin Khimicheskaya
Fizika 22,(2003),30}  Max Lst Sq Error Cp @ 6000 K 0.54%.

CH3CL             tpis91C  1.H  3.CL 1.   0.G   200.000  6000.000  B  50.48722 1
 3.97883949E+00 7.91729094E-03-2.81713927E-06 4.51715634E-10-2.69086155E-14    2
-1.16761879E+04 2.58272676E+00 3.96611858E+00-5.05692958E-03 4.02006413E-05    3
-4.82781901E-08 1.86721580E-11-1.10729538E+04 5.70446517E+00-9.84664159E+03    4
""",
)

entry(
    index = 34,
    label = "HOCl",
    molecule =
"""
1 Cl u0 p3 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials=[
            NASAPolynomial(coeffs=[3.54650,0.00233217,0.523315e-05,-0.973660e-08,0.446729e-11,-0.102996e+05,7.39746e+01],
            Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.36649,0.00205137,-0.670877E-06, 0.10131893E-09, -0.57791828E-14, -0.10576070E+05, 0.28049555E+01],
            Tmin=(1000,'K'), Tmax=(6000,'K'))],
        Tmin=(200,'K'), Tmax=(6000,'K')
        ),
    shortDesc = u"""Gurvich 89 """,
    longDesc =
u"""
See http://www.ipd.anl.gov/anlpubs/2005/07/53802.pdf
7790-92-3
HOCl  SIGMA=1   STATWT=1  IAIBIC=4.357   NU=3609.2,1240,725   HF0=-72.8 KJ
REF=Gurvich 89    Max Lst Sq Error Cp @ 400 K 0.25%
HOCL              RUS 89H   1O   1CL  1    0G   200.000  6000.000  B  52.46004 1
 0.43664934E+01 0.20513656E-02-0.67087650E-06 0.10131893E-09-0.57791828E-14    2
-0.10576070E+05 0.28049555E+01 0.35465037E+01 0.23321738E-02 0.52331522E-05    3
-0.97366010E-08 0.44672936E-11-0.10299629E+05 0.73974601E+01-0.91094784E+04    4
""",
)

entry(
    index = 35,
    label = "CH2ClOOH",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 Cl u0 p3 c0 {1,S}
3 O  u0 p2 c0 {1,S} {4,S}
4 O  u0 p2 c0 {3,S} {7,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.98,19.94,22.45,24.47,27.47,29.59,32.88],'cal/(mol*K)'),
        H298 = (-41.41,'kcal/mol'),
        S298 = (72.44,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBSQ//B3""",
    longDesc =
u"""
Sun, H. Y., Chen, C. J., & Bozzelli, J. W. (2000).
Structures, intramolecular rotation barriers, and thermodynamic properties
(enthalpies, entropies and heat capacities) of chlorinated methyl hydroperoxides
(CH2ClOOH, CHCl2OOH, and CCl3OOH). Journal of Physical Chemistry A, 104(35), 8270–8282.
https://doi.org/10.1021/jp0013917
""",
)

entry(
    index = 36,
    label = "CH2Cl2OOH",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 Cl u0 p3 c0 {1,S}
3 O  u0 p2 c0 {1,S} {4,S}
4 O  u0 p2 c0 {3,S} {7,S}
5 Cl u0 p3 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.47,23.52,25.88,27.66,30.13,31.77,34.21],'cal/(mol*K)'),
        H298 = (-44.74,'kcal/mol'),
        S298 = (79.05,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBSQ//B3""",
    longDesc =
u"""
Sun, H. Y., Chen, C. J., & Bozzelli, J. W. (2000).
Structures, intramolecular rotation barriers, and thermodynamic properties
(enthalpies, entropies and heat capacities) of chlorinated methyl hydroperoxides
(CH2ClOOH, CHCl2OOH, and CCl3OOH). Journal of Physical Chemistry A, 104(35), 8270–8282.
https://doi.org/10.1021/jp0013917
""",
)

entry(
    index = 7,
    label = "CH2Cl3OOH",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 Cl u0 p3 c0 {1,S}
3 O  u0 p2 c0 {1,S} {4,S}
4 O  u0 p2 c0 {3,S} {7,S}
5 Cl  u0 p3 c0 {1,S}
6 Cl  u0 p3 c0 {1,S}
7 H  u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.76,27.74,29.78,31.21,33.01,34.10,35.61],'cal/(mol*K)'),
        H298 = (-45.63,'kcal/mol'),
        S298 = (82.85,'cal/(mol*K)'),
    ),
    shortDesc = u"""CBSQ//B3""",
    longDesc =
u"""
Sun, H. Y., Chen, C. J., & Bozzelli, J. W. (2000).
Structures, intramolecular rotation barriers, and thermodynamic properties
(enthalpies, entropies and heat capacities) of chlorinated methyl hydroperoxides
(CH2ClOOH, CHCl2OOH, and CCl3OOH). Journal of Physical Chemistry A, 104(35), 8270–8282.
https://doi.org/10.1021/jp0013917
""",
)
