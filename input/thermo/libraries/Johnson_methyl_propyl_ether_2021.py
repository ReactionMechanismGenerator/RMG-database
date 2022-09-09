#!/usr/bin/env python
# encoding: utf-8

name = "Johnson_methyl_propyl_ether_2021"
shortDesc = u""
longDesc = u"""
Calculations from Johnson et al. 2021
G4 calculations were done by Bu Lintao and Mark Nimlos
CBS-QB3 calculations were done by Matthew Johnson
"""

entry(
    index = 1,
    label = "CH2COOCH3",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {4,D}
3  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {2,D} {5,S}
5  C u1 p0 c0 {4,S} {9,S} {10,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83567,0.0145233,7.81521e-05,-2.13934e-07,1.82674e-10,-18731.2,10.7744], Tmin=(10,'K'), Tmax=(300.05,'K')),
            NASAPolynomial(coeffs=[2.34933,0.0343378,-2.09033e-05,6.15085e-09,-6.99343e-13,-18731.2,16.1558], Tmin=(300.05,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 2,
    label = "MPO",
    molecule =
"""
1  O u0 p2 c0 {3,S} {5,S}
2  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
            Tdata = ([300,400,500,600,800,1000,1500],'K'),
            Cpdata = ([26.967,32.955,38.762,43.963,52.3,58.468,67.264],'cal/(mol*K)'),
            H298 = (-56.857,'kcal/mol'),
            S298 = (84.269,'cal/(mol*K)'),
        ),
    shortDesc = u"""""",
    longDesc =
u"""
experimental value, same as in CHO library
""",
)

entry(
    index = 3,
    label = "MPO1J",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {5,S}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  C u1 p0 c0 {1,S} {2,S} {14,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45234,0.05365,-0.000126472,2.5448e-07,-1.88294e-10,-9816.9,10.2227], Tmin=(10,'K'), Tmax=(466.89,'K')),
            NASAPolynomial(coeffs=[1.9197,0.044409,-2.49072e-05,6.82697e-09,-7.32144e-13,-9816.9,19.0608], Tmin=(466.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 4,
    label = "MPO1QJ",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {2,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28174,0.0733203,-0.000166491,3.45406e-07,-2.85955e-10,-19922,10.6064], Tmin=(10,'K'), Tmax=(392.77,'K')),
            NASAPolynomial(coeffs=[3.22771,0.0564821,-3.57802e-05,1.0832e-08,-1.25715e-12,-19922,12.5239], Tmin=(392.77,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 5,
    label = "MPO1Q-1J",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {5,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.33891,0.11432,-0.000210611,1.88e-07,-6.24217e-11,-14625.8,15.2382], Tmin=(10,'K'), Tmax=(895.04,'K')),
            NASAPolynomial(coeffs=[15.0473,0.02726,-1.39855e-05,3.76396e-09,-4.08695e-13,-14625.8,-37.8911], Tmin=(895.04,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 6,
    label = "MPO1Q2J",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {2,S} {15,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.6879,0.132662,-0.00047552,9.36747e-07,-6.79849e-10,-12960.6,11.311], Tmin=(10,'K'), Tmax=(426.1,'K')),
            NASAPolynomial(coeffs=[7.39266,0.047012,-2.79654e-05,8.02296e-09,-8.91373e-13,-12960.6,-2.95402], Tmin=(426.1,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 7,
    label = "MPO1Q3J",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {2,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.25565,0.154331,-0.000474281,7.03353e-07,-3.81704e-10,-11305.9,12.9621], Tmin=(10,'K'), Tmax=(555.25,'K')),
            NASAPolynomial(coeffs=[13.3669,0.0290044,-1.3386e-05,3.1023e-09,-2.88712e-13,-11305.9,-27.8206], Tmin=(555.25,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

#entry(
#    index = 8,
#    label = "MPO1Star",
#    molecule =
#"""
#1  O u0 p2 c0 {3,S} {5,S}
#2  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
#3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
#4  C u0 p0 c0 {2,S} {5,D} {12,S}
#5  C u0 p0 c0 {1,S} {4,D} {13,S}
#6  H u0 p0 c0 {2,S}
#7  H u0 p0 c0 {2,S}
#8  H u0 p0 c0 {2,S}
#9  H u0 p0 c0 {3,S}
#10 H u0 p0 c0 {3,S}
#11 H u0 p0 c0 {3,S}
#12 H u0 p0 c0 {4,S}
#13 H u0 p0 c0 {5,S}
#""",
#    thermo = NASA(
#        polynomials = [
#            NASAPolynomial(coeffs=[3.52225,0.0408649,-5.05522e-05,7.26698e-08,-4.48502e-11,-7204.43,9.2477], Tmin=(10,'K'), Tmax=(571.71,'K')),
#            NASAPolynomial(coeffs=[1.7414,0.041958,-2.35976e-05,6.46222e-09,-6.91769e-13,-7204.43,18.4682], Tmin=(571.71,'K'), Tmax=(3000,'K')),
#        ],
#        Tmin = (10,'K'),
#        Tmax = (3000,'K'),
#    ),
#    shortDesc = u"""""",
#    longDesc =
#u"""
#
#""",
#)

entry(
    index = 9,
    label = "MPO1-1OCYC",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {6,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {2,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03062,-0.00252733,0.000128158,-1.86361e-07,8.71637e-11,-26855.4,11.2617], Tmin=(10,'K'), Tmax=(609.03,'K')),
            NASAPolynomial(coeffs=[-3.82255,0.0560851,-3.35254e-05,9.58787e-09,-1.05608e-12,-26855.4,44.1835], Tmin=(609.03,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 10,
    label = "MPO12OCYC",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {2,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80964,0.0287426,1.87539e-05,-3.39089e-08,1.19918e-11,-24865.9,10.718], Tmin=(10,'K'), Tmax=(1075.78,'K')),
            NASAPolynomial(coeffs=[5.57892,0.039324,-1.9927e-05,4.8895e-09,-4.70381e-13,-24865.9,-2.56211], Tmin=(1075.78,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 11,
    label = "MPO1Q-1QJ",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {4,S} {17,S}
8  O u0 p2 c0 {6,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u1 p2 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.91574,0.115846,-0.00035112,8.23593e-07,-7.62759e-10,-33096.1,13.4872], Tmin=(10,'K'), Tmax=(332.65,'K')),
            NASAPolynomial(coeffs=[4.67696,0.0719594,-5.08301e-05,1.65677e-08,-2.02492e-12,-33096.1,8.8173], Tmin=(332.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 12,
    label = "MPO1Q3QJ",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {3,S} {17,S}
8  O u0 p2 c0 {6,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u1 p2 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1772,0.0718492,0.000156206,-7.74098e-07,8.15342e-10,-30533.7,11.9998], Tmin=(10,'K'), Tmax=(373.44,'K')),
            NASAPolynomial(coeffs=[9.79049,0.0612786,-4.34018e-05,1.43735e-08,-1.78772e-12,-30533.7,-19.0179], Tmin=(373.44,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 13,
    label = "MPO1O-1Q",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {5,S} {15,D}
5  O u0 p2 c0 {3,S} {4,S}
6  O u0 p2 c0 {3,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.00324,0.107259,-0.000391806,9.61462e-07,-8.71064e-10,-58054.6,10.7997], Tmin=(10,'K'), Tmax=(357.59,'K')),
            NASAPolynomial(coeffs=[3.71846,0.0615013,-4.14788e-05,1.30453e-08,-1.5518e-12,-58054.6,11.4601], Tmin=(357.59,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 14,
    label = "MPO1Q2J-1Q",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {5,S} {7,S} {14,S} {15,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {16,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {2,S} {9,S}
8  O u0 p2 c0 {6,S} {17,S}
9  O u0 p2 c0 {7,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2518,0.0882431,-8.34614e-05,4.09341e-08,-8.32015e-12,-27366.6,11.5911], Tmin=(10,'K'), Tmax=(1077.52,'K')),
            NASAPolynomial(coeffs=[12.9683,0.0521733,-3.32493e-05,9.86768e-09,-1.11229e-12,-27366.6,-36.0107], Tmin=(1077.52,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 15,
    label = "MPO-1Q12OCYC",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {6,S} {7,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {4,S} {8,S}
8  O u0 p2 c0 {7,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.15812,0.071764,-6.94456e-05,3.768e-08,-8.73901e-12,-38639.4,9.79082], Tmin=(10,'K'), Tmax=(955.31,'K')),
            NASAPolynomial(coeffs=[9.76502,0.0441,-2.60084e-05,7.36718e-09,-8.06265e-13,-38639.4,-21.7816], Tmin=(955.31,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 16,
    label = "Ozoind1-1",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {4,S} {8,S}
8  O u0 p2 c0 {6,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62664,0.0363321,4.34027e-05,-9.27254e-08,4.44225e-11,-20877,11.5305], Tmin=(10,'K'), Tmax=(751.2,'K')),
            NASAPolynomial(coeffs=[3.79827,0.0549092,-3.26116e-05,9.2746e-09,-1.01798e-12,-20877,7.0912], Tmin=(751.2,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 17,
    label = "MPO1O3Q",
    molecule =
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {5,S} {15,D}
5  O u0 p2 c0 {3,S} {4,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u0 p2 c0 {4,D}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.06499,0.097313,-0.000244877,4.91591e-07,-4.10416e-10,-55533.6,9.9789], Tmin=(10,'K'), Tmax=(346.25,'K')),
            NASAPolynomial(coeffs=[5.27711,0.0611784,-4.2506e-05,1.37077e-08,-1.66409e-12,-55533.6,2.56869], Tmin=(346.25,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 18,
    label = "MPO1Q2J3Q",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
4  C u1 p0 c0 {1,S} {2,S} {16,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {1,S} {9,S}
7  O u0 p2 c0 {2,S} {8,S}
8  O u0 p2 c0 {7,S} {17,S}
9  O u0 p2 c0 {6,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.6381,0.144124,-0.000516694,1.15846e-06,-9.86819e-10,-23705,11.4262], Tmin=(10,'K'), Tmax=(357.6,'K')),
            NASAPolynomial(coeffs=[6.62556,0.0656252,-4.52409e-05,1.44781e-08,-1.74506e-12,-23705,-0.680208], Tmin=(357.6,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 19,
    label = "MPO1Q2Star",
    molecule =
"""
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {3,S} {4,S}
3  O u0 p2 c0 {2,S} {15,S}
4  C u0 p0 c0 {1,S} {2,S} {6,S} {8,S}
5  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {4,S} {7,D} {12,S}
7  C u0 p0 c0 {6,D} {13,S} {14,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.91198,0.0935515,-0.000187252,2.339e-07,-1.17999e-10,-19578.6,12.1871], Tmin=(10,'K'), Tmax=(556.52,'K')),
            NASAPolynomial(coeffs=[8.10592,0.0453781,-2.81864e-05,8.34609e-09,-9.49511e-13,-19578.6,-8.31832], Tmin=(556.52,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 20,
    label = "Ozoind13",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {2,S} {8,S}
7  O u0 p2 c0 {3,S} {8,S}
8  O u0 p2 c0 {6,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72915,0.0284479,8.36406e-05,-1.56147e-07,7.71316e-11,-20164.2,11.1052], Tmin=(10,'K'), Tmax=(701.61,'K')),
            NASAPolynomial(coeffs=[3.11807,0.0581033,-3.57145e-05,1.04301e-08,-1.1685e-12,-20164.2,9.24615], Tmin=(701.61,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 21,
    label = "MPO1Q2-1OCYC",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {6,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {2,S} {8,S}
8  O u0 p2 c0 {7,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59505,0.042073,2.30238e-05,-6.33518e-08,2.95334e-11,-48801.9,10.8848], Tmin=(10,'K'), Tmax=(826.6,'K')),
            NASAPolynomial(coeffs=[5.68604,0.0516792,-3.02021e-05,8.44419e-09,-9.12027e-13,-48801.9,-2.88099], Tmin=(826.6,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 22,
    label = "MPO1Q23OCYC",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {2,S} {8,S}
8  O u0 p2 c0 {7,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38576,0.0659346,-4.45748e-05,9.88458e-09,8.94308e-13,-32904.6,9.97381], Tmin=(10,'K'), Tmax=(1063.2,'K')),
            NASAPolynomial(coeffs=[14.2402,0.037064,-2.07254e-05,5.51606e-09,-5.67655e-13,-32904.6,-46.2384], Tmin=(1063.2,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 23,
    label = "MPO3Q12OCYC",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {2,S}
6  O u0 p2 c0 {2,S} {4,S}
7  O u0 p2 c0 {3,S} {8,S}
8  O u0 p2 c0 {7,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.98814,0.106241,-0.000361829,8.11169e-07,-6.78184e-10,-34904.2,11.5728], Tmin=(10,'K'), Tmax=(380.94,'K')),
            NASAPolynomial(coeffs=[4.44085,0.0573822,-3.71221e-05,1.13533e-08,-1.32441e-12,-34904.2,9.1667], Tmin=(380.94,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 24,
    label = "MPO1O-1OJ",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {5,S} {14,D}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u1 p2 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1656,0.0877412,-0.000372232,9.10438e-07,-7.63069e-10,-41349.7,11.1074], Tmin=(10,'K'), Tmax=(410.66,'K')),
            NASAPolynomial(coeffs=[0.52515,0.0542629,-3.37147e-05,9.84632e-09,-1.09986e-12,-41349.7,27.5735], Tmin=(410.66,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 25,
    label = "MPO1O3OJ",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {5,S} {14,D}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.08165,0.0953311,-0.000407843,9.54467e-07,-7.67979e-10,-38051.5,10.784], Tmin=(10,'K'), Tmax=(423.1,'K')),
            NASAPolynomial(coeffs=[0.956071,0.0523092,-3.15537e-05,8.9782e-09,-9.80909e-13,-38051.5,25.8866], Tmin=(423.1,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 26,
    label = "MPO_CP1-1",
    molecule =
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {7,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {4,S} {6,S}
8  O u0 p2 c0 {1,S} {16,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56462,0.0370009,9.89701e-05,-2.69132e-07,1.89284e-10,-54795,11.1498], Tmin=(10,'K'), Tmax=(493.57,'K')),
            NASAPolynomial(coeffs=[3.72512,0.0589523,-3.84091e-05,1.1878e-08,-1.39978e-12,-54795,7.61967], Tmin=(493.57,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 28,
    label = "MPO1O-1O",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,D}
4  C u0 p0 c0 {5,S} {12,D} {13,S}
5  O u0 p2 c0 {3,S} {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.3454,0.064478,-0.000171941,3.66961e-07,-2.94518e-10,-61005.5,9.65601], Tmin=(10,'K'), Tmax=(418.93,'K')),
            NASAPolynomial(coeffs=[2.498,0.0489748,-3.19533e-05,9.75851e-09,-1.13293e-12,-61005.5,15.478], Tmin=(418.93,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 29,
    label = "MPO_CP13",
    molecule =
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {4,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {3,S} {6,S}
8  O u0 p2 c0 {1,S} {16,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47754,0.0460187,1.10417e-05,-5.5054e-08,2.94415e-11,-51291.3,11.7138], Tmin=(10,'K'), Tmax=(735.88,'K')),
            NASAPolynomial(coeffs=[4.74967,0.0529554,-3.13329e-05,8.91441e-09,-9.805e-13,-51291.3,3.41835], Tmin=(735.88,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 33,
    label = "MPrO3J",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
5  C u1 p0 c0 {4,S} {6,S} {7,S}
6  H u0 p0 c0 {5,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49493250E+00, 4.17889180E-02,-3.88555340E-05,4.66742860E-08,-2.73187110E-11,-5.80307080E+03, 9.92730340E+00  ], Tmin=(10,'K'), Tmax=(735.88,'K')),
            NASAPolynomial(coeffs=[ 1.44485470E+00, 4.58000180E-02,-2.55892160E-05, 6.96686990E-09,-7.42219890E-13,-5.80307085E+03, 2.02447660E+01], Tmin=(735.88,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)


entry(
    index = 32,
    label = "MPrO-1J",
    molecule =
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  O u0 p2 c0 {1,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
6  C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
7  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.34587030E+00, 6.61255180E-02,-1.79440500E-04, 3.72842960E-07,-2.89118990E-10,-9.13205590E+03, 9.32395340E+00], Tmin=(10,'K'), Tmax=(735.88,'K')),
            NASAPolynomial(coeffs=[2.97039610E+00, 4.62276120E-02, -2.75102030E-05, 7.91162030E-09,-8.81711200E-13,-9.13205595E+03, 1.33188590E+01], Tmin=(735.88,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)


entry(
    index = 30,
    label = "MPO1O3O",
    molecule =
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,D}
4  C u0 p0 c0 {1,S} {12,D} {13,S}
5  O u0 p2 c0 {2,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {3,D}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2758,0.0799826,-0.000357235,9.09099e-07,-7.94684e-10,-54244.1,11.7998], Tmin=(10,'K'), Tmax=(390.03,'K')),
            NASAPolynomial(coeffs=[1.64397,0.0454345,-2.71377e-05,7.75226e-09,-8.54154e-13,-54244.1,23.1365], Tmin=(390.03,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 31,
    label = "1CH2OC1CH3",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.9969, -7.40169e-05, 7.92687e-05, -1.27441e-07, 6.66791e-11, 12210.8, 9.15832],
                Tmin = (10, 'K'),
                Tmax = (493.926, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-0.00815379, 0.0323599, -1.92281e-05, 5.50083e-09, -6.08155e-13, 12606.4, 25.6554],
                Tmin = (493.926, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (101.519, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (203.705, 'J/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 calculation with methyl treated as Free Rotor by Matt Johnson""",
    longDesc =
u"""
CBS-QB3 calculation with methyl treated as Free Rotor by Matt Johnson
""",
)

entry(
    index = 32,
    label = "C=CC=O",
    molecule =
"""
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {2,D} {6,S} {7,S}
4 C u0 p0 c0 {1,D} {2,S} {8,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97189,0.0017228,7.21085e-05,-1.30404e-07,7.68479e-11,-9675.26,8.14288], Tmin=(10,'K'), Tmax=(436.87,'K')),
            NASAPolynomial(coeffs=[1.15917,0.0274898,-1.64096e-05,4.74608e-09,-5.3304e-13,-9675.26,19.3819], Tmin=(436.87,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G4 calculation with rotors""",
    longDesc =
u"""

""",
)

entry(
    index = 33,
    label = "C[CH]COC",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
5  C u1 p0 c0 {2,S} {3,S} {14,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.42776,0.0628232,-0.000255428,6.52327e-07,-5.56444e-10,-7172.78,11.396], Tmin=(10,'K'), Tmax=(414.98,'K')),
            NASAPolynomial(coeffs=[0.09724,0.0471886,-2.63617e-05,7.1241e-09,-7.49618e-13,-7172.78,29.487], Tmin=(414.98,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G4 calculation with rotors""",
    longDesc =
u"""

""",
)

entry(
    index = 34,
    label = "C=C[CH]OC",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {4,S} {5,D} {9,S}
4  C u1 p0 c0 {1,S} {3,S} {10,S}
5  C u0 p0 c0 {3,D} {11,S} {12,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77704,0.027474,3.96935e-06,-1.72148e-08,6.5149e-12,-1587.54,10.3494], Tmin=(10,'K'), Tmax=(1099.48,'K')),
            NASAPolynomial(coeffs=[6.06737,0.0303602,-1.52736e-05,3.73352e-09,-3.58526e-13,-1587.54,-4.00103], Tmin=(1099.48,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G4 calculation with rotors""",
    longDesc =
u"""

""",
)

entry(
    index = 35,
    label = "C=COC",
    molecule =
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {9,S} {10,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98063,0.0130311,2.41624e-05,-3.21285e-08,1.08256e-11,-14003.1,8.48602], Tmin=(10,'K'), Tmax=(1062.24,'K')),
            NASAPolynomial(coeffs=[4.2279,0.0256603,-1.282e-05,3.0997e-09,-2.93806e-13,-14003.1,3.67704], Tmin=(1062.24,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G4 calculation with rotors""",
    longDesc =
u"""

""",
)

# entry(
#     index = 36,
#     label = "CCC(OC)OO",
#     molecule =
# """
# 1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
# 2  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
# 3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
# 4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
# 5  O u0 p2 c0 {2,S} {4,S}
# 6  O u0 p2 c0 {2,S} {7,S}
# 7  O u0 p2 c0 {6,S} {17,S}
# 8  H u0 p0 c0 {1,S}
# 9  H u0 p0 c0 {1,S}
# 10 H u0 p0 c0 {2,S}
# 11 H u0 p0 c0 {3,S}
# 12 H u0 p0 c0 {3,S}
# 13 H u0 p0 c0 {3,S}
# 14 H u0 p0 c0 {4,S}
# 15 H u0 p0 c0 {4,S}
# 16 H u0 p0 c0 {4,S}
# 17 H u0 p0 c0 {7,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[3.78519,0.0524187,-2.80435e-05,5.48266e-09,-1.21483e-15,-106546,10.4081], Tmin=(10,'K'), Tmax=(1553.74,'K')),
#             NASAPolynomial(coeffs=[23.0335,0.0150004,-3.63473e-06,3.63327e-11,6.62874e-14,-113993,-95.6495], Tmin=(1553.74,'K'), Tmax=(3000,'K')),
#         ],
#         Tmin = (10,'K'),
#         Tmax = (3000,'K'),
#     ),
#     shortDesc = u"""G4 calculation with rotors""",
#     longDesc =
# u"""
#
# """,
# )

entry(
    index = 37,
    label = "[CH2]OCCCOO",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u1 p0 c0 {5,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {3,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29485,0.0721047,-0.000180079,3.95924e-07,-3.25101e-10,-19358.4,13.6815], Tmin=(10,'K'), Tmax=(416.32,'K')),
            NASAPolynomial(coeffs=[1.92939,0.0585696,-3.5274e-05,1.02522e-08,-1.15241e-12,-19358.4,21.8466], Tmin=(416.32,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G4 calculation with rotors""",
    longDesc =
u"""

""",
)

entry(
    index = 38,
    label = "C=CC(OC)OOC",
    molecule =
"""
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {3,S} {4,S}
3  O u0 p2 c0 {2,S} {6,S}
4  C u0 p0 c0 {1,S} {2,S} {7,S} {9,S}
5  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
7  C u0 p0 c0 {4,S} {8,D} {16,S}
8  C u0 p0 c0 {7,D} {17,S} {18,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.21396,0.0824352,-0.000231769,5.55924e-07,-4.80178e-10,-28138.6,13.8935], Tmin=(10,'K'), Tmax=(404.06,'K')),
            NASAPolynomial(coeffs=[0.798547,0.0687809,-4.16266e-05,1.21226e-08,-1.3634e-12,-28138.6,27.1524], Tmin=(404.06,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G4 calculation with rotors""",
    longDesc =
u"""

""",
)

entry(
    index = 39,
    label = "CC[CH]OCOO",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {6,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {5,S} {15,S}
5  O u0 p2 c0 {3,S} {4,S}
6  O u0 p2 c0 {3,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75816,0.049909,-2.21363e-05,2.13057e-09,6.23884e-13,-28220.6,13.1551], Tmin=(10,'K'), Tmax=(1574.77,'K')),
            NASAPolynomial(coeffs=[22.5449,0.0161572,-3.29148e-06,-2.14861e-10,1.0207e-13,-28220.6,-91.5104], Tmin=(1574.77,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G4 calculation with rotors""",
    longDesc =
u"""

""",
)

entry(
    index = 40,
    label = "COCCCO[O]",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {3,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.3664,0.0693859,-0.000237993,6.42379e-07,-5.86743e-10,-25017.9,13.454], Tmin=(10,'K'), Tmax=(394.54,'K')),
            NASAPolynomial(coeffs=[-0.405766,0.0621074,-3.725e-05,1.07348e-08,-1.19505e-12,-25017.9,32.6343], Tmin=(394.54,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G4 calculation with rotors""",
    longDesc =
u"""

""",
)

entry(
    index = 41,
    label = "COCC(C)OO",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.32245,0.0656447,-0.000123799,2.48751e-07,-1.92414e-10,-42437.8,12.4935], Tmin=(10,'K'), Tmax=(456.72,'K')),
            NASAPolynomial(coeffs=[1.05921,0.06229,-3.66643e-05,1.04547e-08,-1.1574e-12,-42437.8,24.2849], Tmin=(456.72,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G4 calculation with rotors""",
    longDesc =
u"""

""",
)

entry(
    index = 42,
    label = "COCC(C)[O]",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {6,S}
2  O u1 p2 c0 {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
6  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.52652,0.0462887,-7.2103e-05,1.72233e-07,-1.48775e-10,-20365.5,12.1872], Tmin=(10,'K'), Tmax=(454.16,'K')),
            NASAPolynomial(coeffs=[-0.0767802,0.0562516,-3.30959e-05,9.41199e-09,-1.03849e-12,-20365.5,29.199], Tmin=(454.16,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G4 calculation with rotors""",
    longDesc =
u"""

""",
)

entry(
    index = 43,
    label = "CO[CH]CCOO",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {5,S} {15,S}
5  O u0 p2 c0 {3,S} {4,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.20184,0.0831785,-0.000261387,5.95504e-07,-4.88823e-10,-19976.8,13.7072], Tmin=(10,'K'), Tmax=(412.31,'K')),
            NASAPolynomial(coeffs=[1.96131,0.0580181,-3.45369e-05,9.9203e-09,-1.10325e-12,-19976.8,22.427], Tmin=(412.31,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""G4 calculation with rotors""",
    longDesc =
u"""

""",
)

entry(
    index = 44,
    label = "CCCOCO[O]",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
6  O u0 p2 c0 {5,S} {7,S}
7  O u1 p2 c0 {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [2.96964, 0.109831, -0.000442634, 1.0282e-06, -8.47585e-10, -28094.9, 12.4821],
                Tmin = (10, 'K'),
                Tmax = (399.694, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.21382, 0.053943, -3.23227e-05, 9.28696e-09, -1.03009e-12, -27687.6, 16.8684],
                Tmin = (399.694, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-233.627, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (361.68, 'J/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 Duminda""",
    longDesc =
u"""
CBS-QB3 Duminda
""",
)

entry(
    index = 45,
    label = "C=CCOC",
    molecule =
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.40165, 0.062284, -0.00022576, 5.19989e-07, -4.12815e-10, -15527.8, 8.78137],
                Tmin = (10, 'K'),
                Tmax = (435.134, 'K'),
            ),
            NASAPolynomial(
                coeffs = [1.39539, 0.0421595, -2.3437e-05, 6.31842e-09, -6.64461e-13, -14988.1, 20.9865],
                Tmin = (435.134, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-129.118, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (295.164, 'J/(mol*K)'),
    ),
    shortDesc = u"""CBS-QB3 Duminda""",
    longDesc =
u"""
CBS-QB3 Duminda
""",
)

entry(
    index = 46,
    label = "CH2CC(OO)OCOO",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {7,S} {13,S} {14,S}
4  C u1 p0 c0 {2,S} {15,S} {16,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {3,S} {9,S}
8  O u0 p2 c0 {6,S} {17,S}
9  O u0 p2 c0 {7,S} {18,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.08475,0.0779582,-6.90646e-05,3.48901e-08,-7.71317e-12,-37941.4,15.7197], Tmin=(10,'K'), Tmax=(966.571,'K')),
            NASAPolynomial(coeffs=[8.98673,0.053534,-3.11613e-05,8.74742e-09,-9.51515e-13,-39082.3,-12.5533], Tmin=(966.571,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-315.572,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (419.881,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Matt Johnson CBS-QB3 with rotors at b3lyp/6-311+g(d,p)
Pivots of considered rotors: [3, 5] ,[6, 7] ,[7, 9]


Geometry:
O      -0.72163000   -4.62411200    9.81479600
O       1.18995200   -3.25196500    9.72336500
O      -0.44656300   -4.41730700    7.49501100
O       0.96571300   -2.33167400    8.62612900
O       0.15280700   -5.72941300    7.39039700
C      -0.03335200   -3.50883800   10.37876400
C       0.31584000   -3.87037500   11.82045900
C      -1.35814000   -4.43669300    8.58413600
C      -0.86931000   -4.20552300   12.65598400
H       1.01761300   -4.71951500   11.77075700
H       0.87806300   -3.03423700   12.24304000
H      -0.65916800   -2.61332200   10.30677600
H      -2.05102500   -5.26834400    8.46008200
H      -1.86030600   -3.46499800    8.51250500
H      -1.67079100   -4.80563500   12.24716100
H      -0.87073900   -3.98707400   13.71557200
H       0.74627500   -2.95337400    7.90672000
H       0.76601300   -5.71725400    8.14370400
""",
)

entry(
    index = 47,
    label = "CH2OC(CCOO)OO",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u1 p0 c0 {5,S} {15,S} {16,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {2,S} {9,S}
7  O u0 p2 c0 {3,S} {8,S}
8  O u0 p2 c0 {7,S} {17,S}
9  O u0 p2 c0 {6,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.95965,0.0939149,-0.000129205,1.17079e-07,-4.68225e-11,-35790.9,16.1904], Tmin=(10,'K'), Tmax=(581.833,'K')),
            NASAPolynomial(coeffs=[8.1782,0.0580384,-3.6714e-05,1.11027e-08,-1.28714e-12,-36398.2,-6.15989], Tmin=(581.833,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-297.654,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (411.566,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Matt Johnson CBS-QB3 with rotors at b3lyp/6-311+g(d,p)
Pivots of considered rotors: [1, 9] ,[2, 5] ,[3, 4] ,[3, 8] ,[6, 8]


Geometry:
O      -1.61276200    0.75311100   -0.60332200
O      -1.09710600   -0.75339300    1.11280800
O       2.34330300    0.15757600    0.87174200
O       2.93406700    1.13554400   -0.03249700
O      -1.55615400   -1.91223500    0.36606000
C       0.50938400   -0.30523300   -0.70562100
C      -0.58325200    0.21399800    0.21192100
C       1.70926300   -0.83686400    0.06799200
C      -2.55993100    1.49442200    0.04282200
H       0.09519100   -1.09947100   -1.32943100
H       0.82447000    0.51033800   -1.35839000
H      -0.20492000    0.97365900    0.90452900
H       2.44104700   -1.28507400   -0.61265900
H       1.40052900   -1.58419000    0.80386200
H      -2.70008900    1.34433500    1.10615100
H      -3.34860500    1.84569400   -0.60541300
H       3.87063700    0.99832900    0.16416800
H      -2.46507200   -1.65054500    0.15825700
""",
)

entry(
    index = 48,
    label = "COC(CCOO)OOd",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {3,S} {8,S}
7  O u0 p2 c0 {2,S} {17,S}
8  O u0 p2 c0 {6,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u1 p2 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55987,0.0641994,-2.86259e-05,-3.38579e-09,4.10237e-12,-39022.4,14.4891], Tmin=(10,'K'), Tmax=(1171.3,'K')),
            NASAPolynomial(coeffs=[15.996,0.0396939,-2.02485e-05,4.93972e-09,-4.69286e-13,-43167.9,-52.7345], Tmin=(1171.3,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-324.4,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (415.724,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Matt Johnson CBS-QB3 with rotors at b3lyp/6-311+g(d,p)
Pivots of considered rotors: [1, 7] ,[1, 9] ,[2, 4] ,[3, 7]


Geometry:
O       1.12268400   -0.25401700    2.83734700
O       4.90589000   -2.10730600    1.30011700
O       1.74868100   -2.41380600    3.30680800
O       5.15549700   -1.95043100    2.72222900
O       2.74343900   -3.21979500    3.59437200
C       2.56012000   -1.28215400    1.24505700
C       2.19912600   -1.09154800    2.71921000
C       4.03318400   -1.06614000    0.88580300
C       0.82434300    0.16375600    4.17508700
H       1.95478600   -0.56475400    0.68445900
H       2.25685300   -2.28256700    0.92696000
H       3.04493600   -0.79740800    3.34800600
H       4.40416900   -0.10641500    1.26225300
H       4.13778300   -1.07140200   -0.20326100
H       1.70059600    0.63423700    4.63559400
H       0.01990500    0.89218000    4.09409600
H       0.49620800   -0.67995000    4.78637000
H       4.51524700   -2.58634600    3.09367900
""",
)

entry(
    index = 49,
    label = "OOC1CCOCO1",
    molecule =
"""
1  O u0 p2 c0 {6,S} {8,S}
2  O u0 p2 c0 {7,S} {8,S}
3  O u0 p2 c0 {4,S} {6,S}
4  O u0 p2 c0 {3,S} {16,S}
5  C u0 p0 c0 {6,S} {7,S} {9,S} {10,S}
6  C u0 p0 c0 {1,S} {3,S} {5,S} {11,S}
7  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
8  C u0 p0 c0 {1,S} {2,S} {14,S} {15,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88165,0.00777667,0.000219933,-4.65719e-07,3.1083e-10,-59218,12.8602], Tmin=(10,'K'), Tmax=(460.652,'K')),
            NASAPolynomial(coeffs=[-0.786153,0.0687175,-4.49622e-05,1.38199e-08,-1.61593e-12,-59004.4,29.4113], Tmin=(460.652,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-492.387,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (374.151,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Matt Johnson CBS-QB3 with rotors at b3lyp/6-311+g(d,p)
Pivots of considered rotors: [3, 6] ,[3, 4]


Geometry:
O       0.26915100    1.10779400    0.43212200
O      -1.82679000    0.42856100   -0.38913500
O       1.59485500   -0.21989800   -0.96047800
O       2.74926300    0.63873700   -0.80025200
C      -0.20297700   -1.27739900    0.15568600
C       0.85274600   -0.17339900    0.24437000
C      -1.34052800   -0.86036300   -0.77517000
C      -0.80633500    1.37976500   -0.46514800
H      -0.59971300   -1.43083300    1.16219300
H       0.26676400   -2.20528400   -0.17805300
H       1.53328900   -0.30305300    1.08688900
H      -2.18603600   -1.54440400   -0.70379300
H      -1.00075900   -0.83062600   -1.81904000
H      -1.22183900    2.33487600   -0.15190900
H      -0.41911100    1.43830700   -1.49389500
H       2.33802200    1.51721800   -0.80220900
""",
)

entry(
    index = 50,
    label = "dOC1CCOCO1",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {6,S} {7,S}
2  O u0 p2 c0 {5,S} {7,S}
3  O u1 p2 c0 {5,S}
4  C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
6  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
7  C u0 p0 c0 {1,S} {2,S} {13,S} {14,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94834,0.00319194,0.000160992,-2.91893e-07,1.70655e-10,-39967.8,11.9341], Tmin=(10,'K'), Tmax=(443.969,'K')),
            NASAPolynomial(coeffs=[-2.65248,0.062863,-4.12897e-05,1.28702e-08,-1.52958e-12,-39383.6,38.3971], Tmin=(443.969,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-332.328,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Matt Johnson CBS-QB3 with rotors at b3lyp/6-311+g(d,p)
Bond corrections: {'C-O': 5, 'C-C': 2, 'C-H': 7}


Geometry:
O       0.65889900    1.18407900   -0.22133600
O      -1.37128600    0.02117600   -0.23203100
O      -1.42028100   -2.27058400   -0.25910700
C       0.70409400   -1.25165200   -0.24103800
C      -0.79956700   -1.20921500    0.20861400
C       1.38381900    0.04393400    0.21495900
C      -0.66621300    1.14272000    0.24803600
H       1.18457600   -2.13306900    0.18641600
H       0.70878300   -1.32390300   -1.32926900
H      -0.81136500   -1.23283400    1.32345300
H       2.38372400    0.12383900   -0.21385400
H       1.47367500    0.05478000    1.31239800
H      -1.17278600    2.02496900   -0.13561600
H      -0.66870500    1.14541200    1.35334400
""",
)

entry(
    index = 51,
    label = "CCC(OOd)OCOO",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {5,S} {6,S} {15,S} {16,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {4,S} {8,S}
7  O u0 p2 c0 {2,S} {17,S}
8  O u0 p2 c0 {6,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u1 p2 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16178,0.0828927,-0.000129954,1.9831e-07,-1.42392e-10,-43442.1,15.3698], Tmin=(10,'K'), Tmax=(396.605,'K')),
            NASAPolynomial(coeffs=[4.26279,0.0657773,-4.2487e-05,1.3069e-08,-1.53623e-12,-43482.1,11.6723], Tmin=(396.605,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-361.21,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (415.724,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Matt Johnson CBS-QB3 with rotors at b3lyp/6-311+g(d,p)
Pivots of considered rotors: [2, 4] ,[3, 7] ,[6, 8] ,[6, 7]


Geometry:
O       2.95310000   -1.14941700   -2.84267400
O       1.68134200    0.76348300   -3.46134800
O       3.69491900   -0.44669100   -0.72554900
O       2.56625100    1.84886900   -3.07658400
O       3.04082100    0.68147500   -0.58278600
C       5.05459400   -1.91680300   -1.98348500
C       4.07837800   -0.76561100   -2.13414800
C       5.65358900   -2.34706400   -3.32414400
C       2.46293500   -0.30409100   -3.88470300
H       4.51531700   -2.74737400   -1.51916100
H       5.84137300   -1.60887400   -1.28915700
H       4.52898200    0.14594100   -2.53701200
H       4.87274600   -2.67559100   -4.01281100
H       6.34789000   -3.17753800   -3.18218800
H       6.20680200   -1.53025000   -3.79759400
H       3.29441700    0.05983500   -4.49593100
H       1.78495900   -0.93828700   -4.45580900
H       2.64554800    1.67344500   -2.11816400
""",
)

entry(
    index = 52,
    label = "O=C1CCOCO1",
    molecule =
"""
1  O u0 p2 c0 {5,S} {6,S}
2  O u0 p2 c0 {6,S} {7,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
6  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
7  C u0 p0 c0 {2,S} {3,D} {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95192,0.00304664,0.000150899,-2.83236e-07,1.72566e-10,-62454.3,11.962], Tmin=(10,'K'), Tmax=(423.438,'K')),
            NASAPolynomial(coeffs=[-1.61526,0.0556879,-3.57593e-05,1.09263e-08,-1.27742e-12,-61983.3,34.0309], Tmin=(423.438,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-519.287,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Matt Johnson CBS-QB3 with rotors at b3lyp/6-311+g(d,p)
Bond corrections: {'C-O': 4, 'C=O': 1, 'C-C': 2, 'C-H': 6}


Geometry:
O       1.15758800   -0.61783100   -0.63389100
O       0.58245300    1.44602700    0.38356300
O      -1.53476500    2.06589400    0.59068800
C      -1.17325300   -0.11000100   -0.35402600
C      -0.09698200   -1.18831700   -0.26216800
C       1.52700400    0.35904500    0.27710100
C      -0.75494800    1.21423600    0.27193600
H      -2.11331200   -0.41724700    0.10698600
H      -1.38131500    0.11042000   -1.40608300
H      -0.28643400   -2.01255400   -0.94878800
H      -0.02890800   -1.59385400    0.75741700
H       1.64733100   -0.06345200    1.28498300
H       2.45554000    0.80763300   -0.06771900
""",
)

entry(
    index = 53,
    label = "propanal",
    molecule =
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {10,S}
4  O u0 p2 c0 {3,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.84662,0.0144249,1.96059e-05,-2.7507e-08,9.456e-12,-24137.9,9.13571], Tmin=(10,'K'), Tmax=(1005.43,'K')),
                               NASAPolynomial(coeffs=[2.10419,0.0296272,-1.54128e-05,3.89376e-09,-3.86041e-13,-24137.9,15.4725], Tmin=(1005.43,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
    shortDesc = u"""""",
    longDesc =
u"""
Mark Nimlos G4 HR
""",
)

entry(
    index = 54,
    label = "CC[C]=O",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3 C u1 p0 c0 {2,S} {4,D}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.7518,0.0206031,-9.89069e-06,9.41636e-09,-7.00204e-12,-5645,9.63608], Tmin=(10,'K'), Tmax=(613.11,'K')), NASAPolynomial(coeffs=[2.21082,0.0266276,-1.4773e-05,4.00709e-09,-4.26016e-13,-5645,16.9341], Tmin=(613.11,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
    shortDesc = u"""""",
    longDesc =
u"""
Mark Nimlos G4 HR
""",
)

entry(
    index = 55,
    label = "CCC(O[O])=O",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {6,D}
4  O u0 p2 c0 {3,S} {5,S}
5  O u1 p2 c0 {4,S}
6  O u0 p2 c0 {3,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.55965,0.044902,-9.00498e-05,1.8475e-07,-1.56569e-10,-23981,11.6303], Tmin=(10,'K'), Tmax=(386.77,'K')), NASAPolynomial(coeffs=[3.37288,0.0373409,-2.39119e-05,7.2952e-09,-8.51574e-13,-23981,13.2718], Tmin=(386.77,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
    shortDesc = u"""""",
    longDesc =
u"""
Mark Nimlos G4 HR
""",
)

entry(
    index = 56,
    label = "[CH2]CC(OO)=O",
    molecule =
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {6,S} {8,D}
6  O u0 p2 c0 {5,S} {7,S}
7  O u0 p2 c0 {6,S} {11,S}
8  O u0 p2 c0 {5,D}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {7,S}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[4.04193,0.0365306,-2.12342e-05,5.04567e-09,-3.04573e-13,-21618.9,10.593], Tmin=(10,'K'), Tmax=(1700.74,'K')), NASAPolynomial(coeffs=[25.4144,-0.00407759,6.0626e-06,-2.31521e-09,2.86607e-13,-21618.9,-107.974], Tmin=(1700.74,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
    shortDesc = u"""""",
    longDesc =
u"""
Mark Nimlos G4 HR
""",
)

entry(
    index = 57,
    label = "C1CC(O1)=O",
    molecule =
"""
1 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3 C u0 p0 c0 {2,S} {4,S} {5,D}
4 O u0 p2 c0 {1,S} {3,S}
5 O u0 p2 c0 {3,D}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[4.13406,-0.0126456,0.000168036,-2.9975e-07,1.75203e-10,-36142.4,9.7856], Tmin=(10,'K'), Tmax=(531.79,'K')), NASAPolynomial(coeffs=[0.286175,0.0355236,-2.20632e-05,6.546e-09,-7.48634e-13,-36142.4,23.3634], Tmin=(531.79,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
    shortDesc = u"""""",
    longDesc =
u"""
Mark Nimlos G4 HR
""",
)

entry(
    index = 58,
    label = "C[CH]C=O",
    molecule =
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,D} {9,S}
5 O u0 p2 c0 {4,D}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.85171,0.0147221,1.3238e-05,-2.11228e-08,7.41516e-12,-4930.68,9.60676], Tmin=(10,'K'), Tmax=(1026.98,'K')), NASAPolynomial(coeffs=[3.26193,0.0248262,-1.2923e-05,3.26187e-09,-3.22772e-13,-4930.68,10.4634], Tmin=(1026.98,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
    shortDesc = u"""""",
    longDesc =
u"""
Mark Nimlos G4 HR
""",
)

entry(
    index = 59,
    label = "CC(O[O])C=O",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {10,S}
3  O u0 p2 c0 {2,S} {4,S}
4  O u1 p2 c0 {3,S}
5  C u0 p0 c0 {2,S} {6,D} {11,S}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.54731,0.0418059,-4.06703e-05,2.83842e-08,-1.01304e-11,-17879.9,10.8834], Tmin=(10,'K'), Tmax=(585.15,'K')), NASAPolynomial(coeffs=[4.64872,0.0342769,-2.13701e-05,6.3954e-09,-7.35945e-13,-17879.9,6.15996], Tmin=(585.15,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
    shortDesc = u"""""",
    longDesc =
u"""
Mark Nimlos G4 HR
""",
)

entry(
    index = 60,
    label = "CC(OO)[C]=O",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {10,S}
3  O u0 p2 c0 {2,S} {4,S}
4  O u0 p2 c0 {3,S} {11,S}
5  C u1 p0 c0 {2,S} {6,D}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.67984,0.0249734,0.000152248,-5.09623e-07,4.57595e-10,-17077.5,9.69054], Tmin=(10,'K'), Tmax=(405.77,'K')), NASAPolynomial(coeffs=[6.37662,0.0356748,-2.51471e-05,8.29315e-09,-1.02761e-12,-17077.5,-4.66975], Tmin=(405.77,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
    shortDesc = u"""""",
    longDesc =
u"""
Mark Nimlos G4 HR
""",
)

entry(
    index = 61,
    label = "CC1OC1=O",
    molecule =
"""
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {9,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,D}
5 O u0 p2 c0 {4,D}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.92341,0.00609324,9.38552e-05,-2.2345e-07,1.73852e-10,-28653.1,9.95759], Tmin=(10,'K'), Tmax=(328.14,'K')), NASAPolynomial(coeffs=[1.90036,0.0307539,-1.88738e-05,5.57537e-09,-6.35394e-13,-28653.1,17.4633], Tmin=(328.14,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
    shortDesc = u"""""",
    longDesc =
u"""
Mark Nimlos G4 HR
""",
)

entry(
    index = 62,
    label = "[CH2]CC=O",
    molecule =
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
5 C u0 p0 c0 {4,S} {6,D} {9,S}
6 O u0 p2 c0 {5,D}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.72883,0.025842,-4.00264e-05,7.65806e-08,-5.76543e-11,711.906,9.43674], Tmin=(10,'K'), Tmax=(482.46,'K')), NASAPolynomial(coeffs=[2.55964,0.0266889,-1.51543e-05,4.20487e-09,-4.56006e-13,711.906,15.2923], Tmin=(482.46,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
    shortDesc = u"""""",
    longDesc =
u"""
Mark Nimlos G4 HR
""",
)

entry(
    index = 63,
    label = "C(O[O])CC=O",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  O u0 p2 c0 {1,S} {3,S}
3  O u1 p2 c0 {2,S}
4  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.49613,0.0516235,-0.000147151,3.1836e-07,-2.56322e-10,-16311.4,10.8236], Tmin=(10,'K'), Tmax=(411.68,'K')), NASAPolynomial(coeffs=[3.23876,0.0356656,-2.17507e-05,6.37329e-09,-7.20405e-13,-16311.4,13.7366], Tmin=(411.68,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
    shortDesc = u"""""",
    longDesc =
u"""
Mark Nimlos G4 HR
""",
)

entry(
    index = 64,
    label = "C(OO)C[C]=O",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  O u0 p2 c0 {1,S} {3,S}
3  O u0 p2 c0 {2,S} {9,S}
4  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
5  C u1 p0 c0 {4,S} {6,D}
6  O u0 p2 c0 {5,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.27172,0.0744293,-0.000260752,5.33847e-07,-4.02674e-10,-15244.3,10.2478], Tmin=(10,'K'), Tmax=(416.82,'K')), NASAPolynomial(coeffs=[5.11855,0.0320213,-1.93076e-05,5.59964e-09,-6.27455e-13,-15244.3,5.52633], Tmin=(416.82,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
    shortDesc = u"""""",
    longDesc =
u"""
Mark Nimlos G4 HR
""",
)

entry(
    index = 65,
    label = "CCC1OC1C",
    molecule =
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {12,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {3,S} {4,S} {6,S} {13,S}
6  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.27172,0.0744293,-0.000260752,5.33847e-07,-4.02674e-10,-15244.3,10.2478], Tmin=(10,'K'), Tmax=(416.82,'K')), NASAPolynomial(coeffs=[5.11855,0.0320213,-1.93076e-05,5.59964e-09,-6.27455e-13,-15244.3,5.52633], Tmin=(416.82,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
    shortDesc = u"""""",
    longDesc =
u"""
Mark Nimlos G4 HR
""",
)

entry(
index = 66,
label = 'CC1OC1O[O]',
molecule ="""multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {10,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {2,S} {3,S} {5,S} {11,S}
5  O u0 p2 c0 {4,S} {6,S}
6  O u1 p2 c0 {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.45875,0.056116,-0.000122748,2.8579e-07,-2.56273e-10,-11381.6,11.5526], Tmin=(10,'K'), Tmax=(388.53,'K')), NASAPolynomial(coeffs=[2.21298,0.0507691,-3.19481e-05,9.61191e-09,-1.10976e-12,-11147.6,18.1501], Tmin=(388.53,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = "",
longDesc =  "Mark Nimlos Calculation")
entry(
index = 67,
label = 'CC(O[O])COC',
molecule ="""multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {11,S}
3  O u0 p2 c0 {2,S} {4,S}
4  O u1 p2 c0 {3,S}
5  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
6  O u0 p2 c0 {5,S} {7,S}
7  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.18552,0.0782675,-0.000188156,3.39307e-07,-2.3537e-10,-26620,10.701], Tmin=(10,'K'), Tmax=(463.11,'K')), NASAPolynomial(coeffs=[3.67832,0.0517932,-3.04421e-05,8.67493e-09,-9.60411e-13,-26427.4,11.2751], Tmin=(463.11,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = "",
longDesc =  "Mark Nimlos Calculation")
entry(
index = 68,
label = 'CC(COC=O)OO',
molecule ="""1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {6,D} {15,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {2,S} {8,S}
8  O u0 p2 c0 {7,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {8,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.95002,0.0976102,-0.000197672,2.64423e-07,-1.46712e-10,-63178.2,11.8309], Tmin=(10,'K'), Tmax=(474.34,'K')), NASAPolynomial(coeffs=[8.04185,0.0498662,-3.14944e-05,9.50682e-09,-1.10139e-12,-63607.2,-8.36671], Tmin=(474.34,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = "",
longDesc =  "Mark Nimlos Calculation")
entry(
index = 69,
label = 'CCC1(O)OC1C',
molecule ="""1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  O u0 p2 c0 {3,S} {13,S}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {3,S} {5,S} {7,S} {14,S}
7  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.2771,0.0683556,-0.000105338,1.61122e-07,-1.08457e-10,-45521.9,10.6673], Tmin=(10,'K'), Tmax=(468.01,'K')), NASAPolynomial(coeffs=[3.33125,0.0570042,-3.4058e-05,9.87459e-09,-1.11013e-12,-45407.7,11.7212], Tmin=(468.01,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = "",
longDesc =  "Mark Nimlos Calculation")
entry(
index = 70,
label = 'CC1[CH]CO1',
molecule ="""multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {10,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
6  O u0 p2 c0 {2,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.95085,0.00338687,0.000143779,-3.05473e-07,2.14446e-10,8294.74,10.8278], Tmin=(10,'K'), Tmax=(363.95,'K')), NASAPolynomial(coeffs=[0.172127,0.0449167,-2.73828e-05,8.05208e-09,-9.14751e-13,8569.79,25.2387], Tmin=(363.95,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = "",
longDesc =  "Mark Nimlos Calculation")
entry(
index = 71,
label = 'CC([O])COC=O',
molecule ="""multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {11,S}
3  O u1 p2 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
5  O u0 p2 c0 {4,S} {6,S}
6  C u0 p0 c0 {5,S} {7,D} {14,S}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.67655,0.0301542,0.000182109,-7.16756e-07,8.05267e-10,-43452.4,10.5368], Tmin=(10,'K'), Tmax=(305.2,'K')), NASAPolynomial(coeffs=[3.99806,0.049923,-3.29175e-05,1.03945e-08,-1.25312e-12,-43583.7,7.53733], Tmin=(305.2,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = "",
longDesc =  "Mark Nimlos Calculation")
entry(
index = 72,
label = 'CC1[CH]O1',
molecule ="""multiplicity 2
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {9,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 O u0 p2 c0 {2,S} {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {2,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.9699,0.00184736,8.27805e-05,-1.49318e-07,8.7645e-11,13245.2,9.50815], Tmin=(10,'K'), Tmax=(438.92,'K')), NASAPolynomial(coeffs=[0.694627,0.0316998,-1.92531e-05,5.67989e-09,-6.50123e-13,13532.7,22.612], Tmin=(438.92,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = "",
longDesc =  "Mark Nimlos Calculation")
entry(
index = 73,
label = 'O=[C]OCOO',
molecule ="""multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
5 O u0 p2 c0 {4,S} {6,S}
6 O u0 p2 c0 {5,S} {9,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {6,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.30619,0.0731828,-0.0002965,6.56411e-07,-5.3151e-10,-34177.7,13.4194], Tmin=(10,'K'), Tmax=(385.96,'K')), NASAPolynomial(coeffs=[5.40693,0.0263298,-1.69325e-05,5.14058e-09,-5.95281e-13,-34153,7.70454], Tmin=(385.96,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = "",
longDesc =  "Mark Nimlos Calculation")
entry(
index = 74,
label = 'O=CC(=O)O',
molecule ="""1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 O u0 p2 c0 {3,D}
5 O u0 p2 c0 {3,S} {7,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {5,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.91546,0.00619706,9.63217e-05,-2.61075e-07,2.1472e-10,-59297.4,9.23579], Tmin=(10,'K'), Tmax=(404.41,'K')), NASAPolynomial(coeffs=[3.62328,0.0226011,-1.46476e-05,4.48784e-09,-5.27052e-13,-59384.2,9.01455], Tmin=(404.41,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = "",
longDesc =  "Mark Nimlos Calculation")
entry(
index = 76,
label = 'CC(OO)C(=O)O.',
molecule ="""1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {11,S}
3  O u0 p2 c0 {2,S} {4,S}
4  O u0 p2 c0 {3,S} {12,S}
5  C u0 p0 c0 {2,S} {6,D} {7,S}
6  O u0 p2 c0 {5,D}
7  O u0 p2 c0 {5,S} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.6085,0.0315605,9.02661e-05,-2.31943e-07,1.50737e-10,-68974.9,9.59664], Tmin=(10,'K'), Tmax=(550.22,'K')), NASAPolynomial(coeffs=[4.93975,0.049631,-3.46459e-05,1.10648e-08,-1.32433e-12,-69541.4,0.152577], Tmin=(550.22,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = "",
longDesc =  "Mark Nimlos Calculation")
entry(
index = 77,
label = 'O=COCOO',
molecule ="""1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5  O u0 p2 c0 {4,S} {6,S}
6  O u0 p2 c0 {5,S} {10,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.68092,0.0262052,0.000146232,-5.61387e-07,5.64665e-10,-58847,8.03678], Tmin=(10,'K'), Tmax=(367.19,'K')), NASAPolynomial(coeffs=[6.35882,0.0323274,-2.29582e-05,7.56836e-09,-9.36848e-13,-59281.6,-5.43951], Tmin=(367.19,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = "",
longDesc =  "Mark Nimlos Calculation")
entry(
index = 78,
label = 'C[CH]C(=O)O',
molecule ="""multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {10,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {6,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.85541,0.017514,2.41351e-05,-3.85096e-08,1.441e-11,-35700.3,10.2901], Tmin=(10,'K'), Tmax=(971.85,'K')), NASAPolynomial(coeffs=[4.10979,0.0303936,-1.72392e-05,4.6175e-09,-4.77212e-13,-36407.5,5.68642], Tmin=(971.85,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = "",
longDesc =  "Mark Nimlos Calculation")
entry(
index = 79,
label = 'OCCOO',
molecule ="""1  O u0 p2 c0 {2,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u0 p2 c0 {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.66538,0.0330289,0.000123078,-6.83737e-07,9.29233e-10,-47193.8,7.73276], Tmin=(10,'K'), Tmax=(277.53,'K')), NASAPolynomial(coeffs=[5.45183,0.0336007,-2.22615e-05,7.08769e-09,-8.61466e-13,-47394.3,-0.422042], Tmin=(277.53,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = "",
longDesc =  "Mark Nimlos Calculation")
entry(
index = 80,
label = 'C[CH]COCOO',
molecule ="""multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
5  O u0 p2 c0 {4,S} {6,S}
6  C u0 p0 c0 {5,S} {7,S} {14,S} {15,S}
7  O u0 p2 c0 {6,S} {8,S}
8  O u0 p2 c0 {7,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.78924,0.12477,-0.000460644,9.61859e-07,-7.35724e-10,-22130,10.295], Tmin=(10,'K'), Tmax=(411.09,'K')), NASAPolynomial(coeffs=[6.04946,0.0499343,-3.0271e-05,8.80567e-09,-9.88286e-13,-22033.8,1.89525], Tmin=(411.09,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = "",
longDesc =  "Mark Nimlos Calculation")
entry(
index = 81,
label = 'CC(OO)CO[CH2]',
molecule ="""multiplicity 2
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {13,S}
3  O u0 p2 c0 {2,S} {4,S}
4  O u0 p2 c0 {3,S} {14,S}
5  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
6  O u0 p2 c0 {5,S} {7,S}
7  C u1 p0 c0 {6,S} {8,S} {9,S}
8  H u0 p0 c0 {7,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.84212,0.117017,-0.000378968,7.37819e-07,-5.42958e-10,-21681.7,11.1129], Tmin=(10,'K'), Tmax=(413.16,'K')), NASAPolynomial(coeffs=[6.85664,0.0496484,-3.09036e-05,9.21927e-09,-1.05745e-12,-21770.2,-1.7623], Tmin=(413.16,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = "",
longDesc =  "Mark Nimlos Calculation")
entry(
index = 83,
label = 'CC([O])C(=O)O',
molecule ="""multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {10,S}
3  O u1 p2 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {11,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {6,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.68933,0.0288607,6.3491e-06,-3.03374e-08,1.49005e-11,-47325.9,12.0232], Tmin=(10,'K'), Tmax=(816.21,'K')), NASAPolynomial(coeffs=[4.89095,0.032861,-1.91761e-05,5.35493e-09,-5.78341e-13,-47851.4,4.45224], Tmin=(816.21,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = "",
longDesc =  "Mark Nimlos Calculation")
entry(
index = 84,
label = 'CC(COCOO)O[O]',
molecule ="""multiplicity 2
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
6  O u0 p2 c0 {5,S} {7,S}
7  O u0 p2 c0 {6,S} {18,S}
8  O u0 p2 c0 {2,S} {9,S}
9  O u1 p2 c0 {8,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.64642,0.142747,-0.000512305,1.14003e-06,-9.57497e-10,-40824,15.4395], Tmin=(10,'K'), Tmax=(365.93,'K')), NASAPolynomial(coeffs=[6.41194,0.065042,-4.39752e-05,1.38843e-08,-1.6575e-12,-40854.9,4.40172], Tmin=(365.93,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = "",
longDesc =  "Mark Nimlos Calculation")

entry(
index=85,
label = '[CH2]OC(C)=O',
molecule ="""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  O u0 p2 c0 {1,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {7,D}
6  C u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
7  O u0 p2 c0 {5,D}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.59714,0.0385117,-8.94709e-05,1.94286e-07,-1.54366e-10,-28456.1,10.7777], Tmin=(10,'K'), Tmax=(451.02,'K')), NASAPolynomial(coeffs=[1.71581,0.0369355,-2.34969e-05,6.9996e-09,-7.95449e-13,-28100.7,20.415], Tmin=(451.02,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = u"""Mark Nimlos Calculation""",
longDesc = u"""Mark Nimlos Calculation"""
)

entry(
index=86,
label = 'CCC(=O)O',
molecule ="""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  O u0 p2 c0 {3,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.63208,0.0343579,-6.34669e-05,1.39403e-07,-1.09894e-10,-57174.5,9.05022], Tmin=(10,'K'), Tmax=(482.26,'K')), NASAPolynomial(coeffs=[0.78462,0.0398301,-2.40499e-05,6.89656e-09,-7.61602e-13,-56688.8,22.8987], Tmin=(482.26,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = u"""Mark Nimlos Calculation""",
longDesc = u"""Mark Nimlos Calculation"""
)

entry(
index=87,
label = 'CCCOO',
molecule ="""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.67856,0.0334599,-8.58867e-06,-5.27235e-09,2.55714e-12,-25043,10.7549], Tmin=(10,'K'), Tmax=(1241.26,'K')), NASAPolynomial(coeffs=[7.82652,0.0288714,-1.36522e-05,3.14488e-09,-2.85717e-13,-26749,-12.8772], Tmin=(1241.26,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = u"""Mark Nimlos Calculation""",
longDesc = u"""Mark Nimlos Calculation"""
)

entry(
index=88,
label = 'CCCO[O]',
molecule ="""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u1 p2 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.6102,0.0400182,-9.31781e-05,2.21576e-07,-1.8716e-10,-7862.48,10.4098], Tmin=(10,'K'), Tmax=(431.59,'K')), NASAPolynomial(coeffs=[1.4926,0.0397489,-2.30957e-05,6.51255e-09,-7.14212e-13,-7494.4,20.9933], Tmin=(431.59,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = u"""Mark Nimlos Calculation""",
longDesc = u"""Mark Nimlos Calculation"""
)


entry(
index=89,
label = 'CC(COCOO)OO',
molecule ="""
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
6  O u0 p2 c0 {5,S} {7,S}
7  O u0 p2 c0 {6,S} {18,S}
8  O u0 p2 c0 {2,S} {9,S}
9  O u0 p2 c0 {8,S} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.47115,0.179611,-0.00105197,3.34182e-06,-3.61124e-09,-60233.3,11.9861], Tmin=(10,'K'), Tmax=(317.72,'K')), NASAPolynomial(coeffs=[-1.47062,0.101111,-7.64618e-05,2.56606e-08,-3.17693e-12,-59336.2,36.6603], Tmin=(317.72,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = u"""Mark Nimlos Calculation""",
longDesc = u"""Mark Nimlos Calculation"""
)

entry(
index=90,
label = 'CC(COCO[O])OO',
molecule ="""
multiplicity 2
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
6  O u0 p2 c0 {5,S} {7,S}
7  O u1 p2 c0 {6,S}
8  O u0 p2 c0 {2,S} {9,S}
9  O u0 p2 c0 {8,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {9,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.93207,0.116001,-0.000354827,8.81928e-07,-8.75849e-10,-40192.6,14.6937], Tmin=(10,'K'), Tmax=(309.15,'K')), NASAPolynomial(coeffs=[4.51029,0.0748746,-5.48143e-05,1.83171e-08,-2.27812e-12,-40191.2,10.5327], Tmin=(309.15,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = u"""Mark Nimlos Calculation""",
longDesc = u"""Mark Nimlos Calculation"""
)

entry(
index=91,
label = 'CC([CH]OCOO)OO',
molecule ="""
multiplicity 2
1  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {14,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
7  O u0 p2 c0 {6,S} {8,S}
8  O u0 p2 c0 {7,S} {17,S}
9  O u0 p2 c0 {2,S} {10,S}
10 O u0 p2 c0 {9,S} {18,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {10,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.36755,0.181142,-0.000852575,2.25161e-06,-2.14698e-09,-37907.4,13.7228], Tmin=(10,'K'), Tmax=(336.81,'K')), NASAPolynomial(coeffs=[4.89533,0.0766825,-5.58393e-05,1.83727e-08,-2.24864e-12,-37655.5,10.5464], Tmin=(336.81,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = u"""Mark Nimlos Calculation""",
longDesc = u"""Mark Nimlos Calculation"""
)

entry(
index=92,
label = 'O=[C]C(O)COO',
molecule ="""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u1 p0 c0 {1,D} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4  O u0 p2 c0 {3,S} {9,S}
5  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
6  O u0 p2 c0 {5,S} {7,S}
7  O u0 p2 c0 {6,S} {12,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {7,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.26091,0.07735,2.58783e-05,-8.94286e-07,1.60958e-09,-34794.8,10.5252], Tmin=(10,'K'), Tmax=(260.5,'K')), NASAPolynomial(coeffs=[9.56614,0.0332106,-2.32765e-05,7.72297e-09,-9.6682e-13,-35302,-14.8431], Tmin=(260.5,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = u"""Mark Nimlos Calculation""",
longDesc = u"""Mark Nimlos Calculation"""
)

entry(
index=94,
label = 'CC(COO)OO',
molecule ="""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u0 p2 c0 {4,S} {14,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.68218,0.128623,-0.000406535,7.07372e-07,-4.66292e-10,-37651,10.7017], Tmin=(10,'K'), Tmax=(444.7,'K')), NASAPolynomial(coeffs=[9.63602,0.0407785,-2.49023e-05,7.33455e-09,-8.34245e-13,-38019.4,-14.3991], Tmin=(444.7,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = u"""Mark Nimlos Calculation""",
longDesc = u"""Mark Nimlos Calculation"""
)

entry(
index=95,
label = 'CCCOCOO',
molecule ="""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
6  O u0 p2 c0 {5,S} {7,S}
7  O u0 p2 c0 {6,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.1478,0.0867657,-0.00023272,4.80858e-07,-3.80454e-10,-46197.9,9.14624], Tmin=(10,'K'), Tmax=(407.63,'K')), NASAPolynomial(coeffs=[3.58644,0.0578508,-3.57562e-05,1.06145e-08,-1.21324e-12,-46029.2,9.93168], Tmin=(407.63,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = u"""Mark Nimlos Calculation""",
longDesc = u"""Mark Nimlos Calculation"""
)

entry(
index=96,
label = 'CCC(OO)OCOO',
molecule ="""
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {15,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u0 p2 c0 {4,S} {16,S}
6  O u0 p2 c0 {3,S} {7,S}
7  C u0 p0 c0 {6,S} {8,S} {17,S} {18,S}
8  O u0 p2 c0 {7,S} {9,S}
9  O u0 p2 c0 {8,S} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.84174,0.127824,-0.000452091,1.25145e-06,-1.31459e-09,-63620.4,9.28405], Tmin=(10,'K'), Tmax=(308.69,'K')), NASAPolynomial(coeffs=[3.2966,0.0848112,-6.27173e-05,2.10076e-08,-2.61284e-12,-63471.7,10.4888], Tmin=(308.69,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = u"""Mark Nimlos Calculation""",
longDesc = u"""Mark Nimlos Calculation"""
)

entry(
index=97,
label = 'CC(COO)O[O]',
molecule ="""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u0 p2 c0 {4,S} {14,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u1 p2 c0 {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.67182,0.0200615,0.000236753,-5.57945e-07,3.67183e-10,-20457.2,11.8426], Tmin=(10,'K'), Tmax=(547.3,'K')), NASAPolynomial(coeffs=[9.29179,0.0497365,-3.84824e-05,1.3514e-08,-1.74388e-12,-22132,-21.5632], Tmin=(547.3,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = u"""Mark Nimlos Calculation""",
longDesc = u"""Mark Nimlos Calculation"""
)

entry(
index=98,
label = 'O=C(OO)C(O)COO',
molecule ="""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {5,S}
3  O u0 p2 c0 {2,S} {4,S}
4  O u0 p2 c0 {3,S} {10,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {11,S}
6  O u0 p2 c0 {5,S} {12,S}
7  C u0 p0 c0 {5,S} {8,S} {13,S} {14,S}
8  O u0 p2 c0 {7,S} {9,S}
9  O u0 p2 c0 {8,S} {15,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {9,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.29645,0.081543,0.000123264,-1.65472e-06,3.41943e-09,-75799.1,12.383], Tmin=(10,'K'), Tmax=(204.39,'K')), NASAPolynomial(coeffs=[6.9539,0.0570692,-4.28324e-05,1.46938e-08,-1.87061e-12,-76047,-1.86193], Tmin=(204.39,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = u"""Mark Nimlos Calculation""",
longDesc = u"""Mark Nimlos Calculation"""
)

entry(
index=99,
label = '[O]OC(=O)C(O)COO',
molecule ="""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,S} {7,S} {10,S}
6  O u0 p2 c0 {5,S} {11,S}
7  C u0 p0 c0 {5,S} {8,S} {12,S} {13,S}
8  O u0 p2 c0 {7,S} {9,S}
9  O u0 p2 c0 {8,S} {14,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {9,S}
""",
thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.05841,0.0907347,-0.000118229,7.8647e-08,-2.10866e-11,-54824.4,11.1728], Tmin=(10,'K'), Tmax=(877.22,'K')), NASAPolynomial(coeffs=[14.991,0.0363236,-2.51889e-05,7.93844e-09,-9.35246e-13,-56917.9,-44.8319], Tmin=(877.22,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K')),
shortDesc = u"""Mark Nimlos Calculation""",
longDesc = u"""Mark Nimlos Calculation"""
)

entry(
index=100,
label = 'C[CH]C(=O)OCO',
molecule ="""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  H u0 p0 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p2 c0 {4,S} {7,S}
7  C u0 p0 c0 {6,S} {8,S} {12,S} {13,S}
8  O u0 p2 c0 {7,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
""",
thermo =  NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.51772, 0.0498199, -0.000105415, 2.75467e-07, -2.57358e-10, -56993, 12.0235],
                Tmin = (10, 'K'),
                Tmax = (402.554, 'K'),
            ),
            NASAPolynomial(
                coeffs = [0.642818, 0.0545317, -3.4085e-05, 1.01312e-08, -1.15589e-12, -56568.2, 25.678],
                Tmin = (402.554, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (
            -473.88,
            'kJ/mol',
        ),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (320.107, 'J/(mol*K)'),
    ),
shortDesc = u"""Mark Nimlos CBS-QB3 Calculation""",
longDesc = u"""Mark Nimlos CBS-QB3 Calculation"""
)

entry(
index=101,
label = 'CCC(OO)OC',
molecule ="""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {13,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u0 p2 c0 {4,S} {14,S}
6  O u0 p2 c0 {3,S} {7,S}
7  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
""",
thermo =  NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.23246, 0.0761536, -0.000143498, 2.55555e-07, -1.93599e-10, -47889.4, 8.97972],
                Tmin = (10, 'K'),
                Tmax = (411.218, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.72851, 0.0591624, -3.71406e-05, 1.11831e-08, -1.29359e-12, -47827.3, 8.27814],
                Tmin = (411.218, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (
            -398.192,
            'kJ/mol',
        ),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (386.623, 'J/(mol*K)'),
    ),
shortDesc = u"""Mark Nimlos CBS-QB3 Calculation""",
longDesc = u"""Mark Nimlos CBS-QB3 Calculation"""
)

entry(
index=102,
label = 'CC1OC1OC[O]',
molecule ="""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {11,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {2,S} {3,S} {5,S} {12,S}
5  O u0 p2 c0 {4,S} {6,S}
6  C u0 p0 c0 {5,S} {7,S} {13,S} {14,S}
7  O u1 p2 c0 {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
thermo =  NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.70972, 0.0248565, 0.000198801, -6.90643e-07, 6.96693e-10, -30341.6, 10.7186],
                Tmin = (10, 'K'),
                Tmax = (340.731, 'K'),
            ),
            NASAPolynomial(
                coeffs = [4.22582, 0.047918, -3.09186e-05, 9.64624e-09, -1.15481e-12, -30545.8, 6.30381],
                Tmin = (340.731, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (
            -252.236,
            'kJ/mol',
        ),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (320.107, 'J/(mol*K)'),
    ),
shortDesc = u"""Mark Nimlos CBS-QB3 Calculation""",
longDesc = u"""Mark Nimlos CBS-QB3 Calculation"""
)
