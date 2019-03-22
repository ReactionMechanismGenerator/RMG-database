#!/usr/bin/env python
# encoding: utf-8

name = "pme"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44618,0.0474918,-6.62132e-05,1.03669e-07,-6.49171e-11,-30835.5,9.10621], Tmin=(10,'K'), Tmax=(574.1,'K')),
            NASAPolynomial(coeffs=[0.786644,0.0492491,-2.69818e-05,7.22382e-09,-7.58871e-13,-30835.5,22.8683], Tmin=(574.1,'K'), Tmax=(3000,'K')),
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
    index = 1,
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
    index = 2,
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
            NASAPolynomial(coeffs=[3.28174,0.0733203,-0.000166491,3.45406e-07,-2.85955e-10,-29738.9,10.6064], Tmin=(10,'K'), Tmax=(392.77,'K')),
            NASAPolynomial(coeffs=[3.22771,0.0564821,-3.57802e-05,1.0832e-08,-1.25715e-12,-29738.9,12.5239], Tmin=(392.77,'K'), Tmax=(3000,'K')),
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
    index = 3,
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
            NASAPolynomial(coeffs=[2.33891,0.11432,-0.000210611,1.88e-07,-6.24217e-11,-24442.7,15.2382], Tmin=(10,'K'), Tmax=(895.04,'K')),
            NASAPolynomial(coeffs=[15.0473,0.02726,-1.39855e-05,3.76396e-09,-4.08695e-13,-24442.7,-37.8911], Tmin=(895.04,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[2.6879,0.132662,-0.00047552,9.36747e-07,-6.79849e-10,-22777.5,11.311], Tmin=(10,'K'), Tmax=(426.1,'K')),
            NASAPolynomial(coeffs=[7.39266,0.047012,-2.79654e-05,8.02296e-09,-8.91373e-13,-22777.5,-2.95402], Tmin=(426.1,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[2.25565,0.154331,-0.000474281,7.03353e-07,-3.81704e-10,-21122.8,12.9621], Tmin=(10,'K'), Tmax=(555.25,'K')),
            NASAPolynomial(coeffs=[13.3669,0.0290044,-1.3386e-05,3.1023e-09,-2.88712e-13,-21122.8,-27.8206], Tmin=(555.25,'K'), Tmax=(3000,'K')),
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
    label = "propanal",
    molecule =
"""
1  O u0 p2 c0 {4,D}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {1,D} {2,S} {10,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84662,0.0144249,1.96059e-05,-2.7507e-08,9.456e-12,-23531.7,9.13571], Tmin=(10,'K'), Tmax=(1005.43,'K')),
            NASAPolynomial(coeffs=[2.10419,0.0296272,-1.54128e-05,3.89376e-09,-3.86041e-13,-23531.7,15.4725], Tmin=(1005.43,'K'), Tmax=(3000,'K')),
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
    label = "MPO1Star",
    molecule =
"""
1  O u0 p2 c0 {3,S} {5,S}
2  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {5,D} {12,S}
5  C u0 p0 c0 {1,S} {4,D} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.52225,0.0408649,-5.05522e-05,7.26698e-08,-4.48502e-11,-17021.3,9.2477], Tmin=(10,'K'), Tmax=(571.71,'K')),
            NASAPolynomial(coeffs=[1.7414,0.041958,-2.35976e-05,6.46222e-09,-6.91769e-13,-17021.3,18.4682], Tmin=(571.71,'K'), Tmax=(3000,'K')),
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
    index = 8,
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
            NASAPolynomial(coeffs=[3.80964,0.0287426,1.87539e-05,-3.39089e-08,1.19918e-11,-34682.8,10.718], Tmin=(10,'K'), Tmax=(1075.78,'K')),
            NASAPolynomial(coeffs=[5.57892,0.039324,-1.9927e-05,4.8895e-09,-4.70381e-13,-34682.8,-2.56211], Tmin=(1075.78,'K'), Tmax=(3000,'K')),
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
    index = 9,
    label = "MPO13OCYC",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {2,S} {3,S}
6  O u0 p2 c0 {2,S} {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82608,0.0236302,4.06527e-05,-6.50281e-08,2.58487e-11,-34827.4,9.64195], Tmin=(10,'K'), Tmax=(887.22,'K')),
            NASAPolynomial(coeffs=[3.13432,0.0445004,-2.46439e-05,6.58805e-09,-6.85845e-13,-34827.4,8.95923], Tmin=(887.22,'K'), Tmax=(3000,'K')),
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
    label = "CH3OCHO",
    molecule =
"""
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,D}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {2,D} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96529,0.00198331,6.4164e-05,-1.06369e-07,5.67671e-11,-25946.1,9.57726], Tmin=(10,'K'), Tmax=(484.13,'K')),
            NASAPolynomial(coeffs=[0.820986,0.0279625,-1.63287e-05,4.47319e-09,-4.71181e-13,-25946.1,22.4658], Tmin=(484.13,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[4.03062,-0.00252733,0.000128158,-1.86361e-07,8.71637e-11,-36672.3,11.2617], Tmin=(10,'K'), Tmax=(609.03,'K')),
            NASAPolynomial(coeffs=[-3.82255,0.0560851,-3.35254e-05,9.58787e-09,-1.05608e-12,-36672.3,44.1835], Tmin=(609.03,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[2.91574,0.115846,-0.00035112,8.23593e-07,-7.62759e-10,-42913,13.4872], Tmin=(10,'K'), Tmax=(332.65,'K')),
            NASAPolynomial(coeffs=[4.67696,0.0719594,-5.08301e-05,1.65677e-08,-2.02492e-12,-42913,8.8173], Tmin=(332.65,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[3.00324,0.107259,-0.000391806,9.61462e-07,-8.71064e-10,-67871.5,10.7997], Tmin=(10,'K'), Tmax=(357.59,'K')),
            NASAPolynomial(coeffs=[3.71846,0.0615013,-4.14788e-05,1.30453e-08,-1.5518e-12,-67871.5,11.4601], Tmin=(357.59,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[3.62664,0.0363321,4.34027e-05,-9.27254e-08,4.44225e-11,-30693.9,11.5305], Tmin=(10,'K'), Tmax=(751.2,'K')),
            NASAPolynomial(coeffs=[3.79827,0.0549092,-3.26116e-05,9.2746e-09,-1.01798e-12,-30693.9,7.0912], Tmin=(751.2,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[3.2518,0.0882431,-8.34614e-05,4.09341e-08,-8.32015e-12,-37183.5,11.5911], Tmin=(10,'K'), Tmax=(1077.52,'K')),
            NASAPolynomial(coeffs=[12.9683,0.0521733,-3.32493e-05,9.86768e-09,-1.11229e-12,-37183.5,-36.0107], Tmin=(1077.52,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[3.15812,0.071764,-6.94456e-05,3.768e-08,-8.73901e-12,-48456.3,9.79082], Tmin=(10,'K'), Tmax=(955.31,'K')),
            NASAPolynomial(coeffs=[9.76502,0.0441,-2.60084e-05,7.36718e-09,-8.06265e-13,-48456.3,-21.7816], Tmin=(955.31,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[3.1656,0.0877412,-0.000372232,9.10438e-07,-7.63069e-10,-51166.6,11.1074], Tmin=(10,'K'), Tmax=(410.66,'K')),
            NASAPolynomial(coeffs=[0.52515,0.0542629,-3.37147e-05,9.84632e-09,-1.09986e-12,-51166.6,27.5735], Tmin=(410.66,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[3.3454,0.064478,-0.000171941,3.66961e-07,-2.94518e-10,-70822.4,9.65601], Tmin=(10,'K'), Tmax=(418.93,'K')),
            NASAPolynomial(coeffs=[2.498,0.0489748,-3.19533e-05,9.75851e-09,-1.13293e-12,-70822.4,15.478], Tmin=(418.93,'K'), Tmax=(3000,'K')),
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
    label = "Propionic",
    molecule =
"""
1  O u0 p2 c0 {5,S} {11,S}
2  O u0 p2 c0 {5,D}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {1,S} {2,D} {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82289,0.0192901,2.08652e-05,-3.18432e-08,1.0933e-11,-47925.6,9.73308], Tmin=(10,'K'), Tmax=(1068.47,'K')),
            NASAPolynomial(coeffs=[3.88618,0.0330098,-1.79888e-05,4.6246e-09,-4.60062e-13,-47925.6,5.69549], Tmin=(1068.47,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[3.56462,0.0370009,9.89701e-05,-2.69132e-07,1.89284e-10,-64611.9,11.1498], Tmin=(10,'K'), Tmax=(493.57,'K')),
            NASAPolynomial(coeffs=[3.72512,0.0589523,-3.84091e-05,1.1878e-08,-1.39978e-12,-64611.9,7.61967], Tmin=(493.57,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[3.1772,0.0718492,0.000156206,-7.74098e-07,8.15342e-10,-40350.6,11.9998], Tmin=(10,'K'), Tmax=(373.44,'K')),
            NASAPolynomial(coeffs=[9.79049,0.0612786,-4.34018e-05,1.43735e-08,-1.78772e-12,-40350.6,-19.0179], Tmin=(373.44,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[3.06499,0.097313,-0.000244877,4.91591e-07,-4.10416e-10,-65350.5,9.9789], Tmin=(10,'K'), Tmax=(346.25,'K')),
            NASAPolynomial(coeffs=[5.27711,0.0611784,-4.2506e-05,1.37077e-08,-1.66409e-12,-65350.5,2.56869], Tmin=(346.25,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[3.72915,0.0284479,8.36406e-05,-1.56147e-07,7.71316e-11,-29981.1,11.1052], Tmin=(10,'K'), Tmax=(701.61,'K')),
            NASAPolynomial(coeffs=[3.11807,0.0581033,-3.57145e-05,1.04301e-08,-1.1685e-12,-29981.1,9.24615], Tmin=(701.61,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[2.91198,0.0935515,-0.000187252,2.339e-07,-1.17999e-10,-29395.5,12.1871], Tmin=(10,'K'), Tmax=(556.52,'K')),
            NASAPolynomial(coeffs=[8.10592,0.0453781,-2.81864e-05,8.34609e-09,-9.49511e-13,-29395.5,-8.31832], Tmin=(556.52,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[2.6381,0.144124,-0.000516694,1.15846e-06,-9.86819e-10,-33521.9,11.4262], Tmin=(10,'K'), Tmax=(357.6,'K')),
            NASAPolynomial(coeffs=[6.62556,0.0656252,-4.52409e-05,1.44781e-08,-1.74506e-12,-33521.9,-0.680208], Tmin=(357.6,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[2.98814,0.106241,-0.000361829,8.11169e-07,-6.78184e-10,-44721.1,11.5728], Tmin=(10,'K'), Tmax=(380.94,'K')),
            NASAPolynomial(coeffs=[4.44085,0.0573822,-3.71221e-05,1.13533e-08,-1.32441e-12,-44721.1,9.1667], Tmin=(380.94,'K'), Tmax=(3000,'K')),
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
    index = 27,
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
            NASAPolynomial(coeffs=[3.38576,0.0659346,-4.45748e-05,9.88458e-09,8.94308e-13,-42721.5,9.97381], Tmin=(10,'K'), Tmax=(1063.2,'K')),
            NASAPolynomial(coeffs=[14.2402,0.037064,-2.07254e-05,5.51606e-09,-5.67655e-13,-42721.5,-46.2384], Tmin=(1063.2,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[3.08165,0.0953311,-0.000407843,9.54467e-07,-7.67979e-10,-47868.4,10.784], Tmin=(10,'K'), Tmax=(423.1,'K')),
            NASAPolynomial(coeffs=[0.956071,0.0523092,-3.15537e-05,8.9782e-09,-9.80909e-13,-47868.4,25.8866], Tmin=(423.1,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[3.83567,0.0145233,7.81521e-05,-2.13934e-07,1.82674e-10,-28548.1,10.7744], Tmin=(10,'K'), Tmax=(300.05,'K')),
            NASAPolynomial(coeffs=[2.34933,0.0343378,-2.09033e-05,6.15085e-09,-6.99343e-13,-28548.1,16.1558], Tmin=(300.05,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[3.2758,0.0799826,-0.000357235,9.09099e-07,-7.94684e-10,-64061,11.7998], Tmin=(10,'K'), Tmax=(390.03,'K')),
            NASAPolynomial(coeffs=[1.64397,0.0454345,-2.71377e-05,7.75226e-09,-8.54154e-13,-64061,23.1365], Tmin=(390.03,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[3.47754,0.0460187,1.10417e-05,-5.5054e-08,2.94415e-11,-61108.2,11.7138], Tmin=(10,'K'), Tmax=(735.88,'K')),
            NASAPolynomial(coeffs=[4.74967,0.0529554,-3.13329e-05,8.91441e-09,-9.805e-13,-61108.2,3.41835], Tmin=(735.88,'K'), Tmax=(3000,'K')),
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
    label = "CC=COCOO",
    molecule =
"""
1  O u0 p2 c0 {4,S} {7,S}
2  O u0 p2 c0 {3,S} {4,S}
3  O u0 p2 c0 {2,S} {15,S}
4  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
5  C u0 p0 c0 {6,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {5,S} {7,D} {13,S}
7  C u0 p0 c0 {1,S} {6,D} {14,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38523,0.0540299,-3.6963e-05,1.30859e-08,-1.9124e-12,-32240.3,13.1257], Tmin=(10,'K'), Tmax=(1439.95,'K')),
            NASAPolynomial(coeffs=[9.5503,0.0369042,-1.91231e-05,4.82637e-09,-4.78418e-13,-34015.8,-18.865], Tmin=(1439.95,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-268.137,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (345.051,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Bond corrections: {'C-O': 3, 'H-O': 1, 'C=C': 1, 'C-H': 7, 'C-C': 1, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [1, 4], dihedral: [7, 1, 4, 2], invalidation reason: scan job crashed
pivots: [1, 7], dihedral: [3, 0, 6, 5], rotor symmetry: 1, max scan energy: 24.34 kJ/mol
* Invalidated! pivots: [2, 4], dihedral: [3, 2, 4, 1], invalidation reason: scan has a barrier larger than 40 kJ/mol
pivots: [2, 3], dihedral: [4, 2, 3, 15], rotor symmetry: 1, max scan energy: 32.50 kJ/mol
pivots: [5, 6], dihedral: [8, 5, 6, 7], rotor symmetry: 3, max scan energy: 8.15 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -0.01326700    0.22076000    1.18964900
O      -2.05167800   -0.00188200    0.03985300
O      -1.55146300   -0.73794900   -1.10906100
C      -1.03162000    0.86364100    0.46803700
C       3.02831900   -1.78758500    0.24782000
C       1.84127800   -1.22807500    0.97532700
C       1.02396400   -0.31413200    0.46146200
H       3.11467400   -1.37361900   -0.76026600
H       3.96147100   -1.56824300    0.77851000
H       2.96547900   -2.87767200    0.15810300
H      -0.62102500    1.40717600   -0.39046700
H      -1.53925000    1.53241700    1.16410700
H       1.64693400   -1.57592100    1.98602900
H       1.13900900    0.08505300   -0.54379800
H      -1.33646400   -1.58861200   -0.69960600
""",
)

entry(
    index = 33,
    label = "CC=COC[O]",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {6,S}
2  O u1 p2 c0 {4,S}
3  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {6,D} {12,S}
6  C u0 p0 c0 {1,S} {5,D} {13,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58236,0.0384791,3.46361e-06,-3.84443e-08,2.10014e-11,-15556.5,11.4682], Tmin=(10,'K'), Tmax=(769.478,'K')),
            NASAPolynomial(coeffs=[5.86068,0.0395038,-2.36188e-05,6.7528e-09,-7.43962e-13,-16288.1,-1.40178], Tmin=(769.478,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-129.38,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Bond corrections: {'C-O': 3, 'C=C': 1, 'C-C': 1, 'C-H': 7}
1D rotors:
pivots: [1, 6], dihedral: [3, 0, 5, 4], rotor symmetry: 1, max scan energy: 24.60 kJ/mol
pivots: [1, 4], dihedral: [5, 0, 3, 1], rotor symmetry: 1, max scan energy: 16.26 kJ/mol
pivots: [3, 5], dihedral: [7, 3, 5, 6], rotor symmetry: 3, max scan energy: 8.09 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       0.70188800   -0.77409700   -0.11062500
O       0.98833300    1.57587100    0.11237900
C      -2.96463100   -1.49849900    0.00445600
C       1.54015500    0.41611000   -0.03327100
C      -1.47754700   -1.63636300   -0.08588000
C      -0.63274000   -0.59495100   -0.02394900
H      -3.36597000   -2.06675800    0.85166700
H      -3.26664800   -0.45553500    0.12545300
H      -3.45564600   -1.89020800   -0.89400100
H       2.15364700    0.35563700   -0.96093700
H       2.24389900    0.17784900    0.79651900
H      -1.05865300   -2.63120300   -0.20801500
H      -0.96176500    0.43152400    0.09676300
""",
)

entry(
    index = 34,
    label = "COC([O])CC=O",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {5,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,D} {14,S}
5  O u0 p2 c0 {2,S} {3,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u1 p2 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77074,0.0306817,0.000689863,-6.00281e-06,1.51448e-08,-38548.9,9.61396], Tmin=(10,'K'), Tmax=(143.518,'K')),
            NASAPolynomial(coeffs=[5.28059,0.0438923,-2.61025e-05,7.40562e-09,-8.08841e-13,-38649.1,3.27704], Tmin=(143.518,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-315.136,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (315.95,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Bond corrections: {'C-O': 3, 'C=O': 1, 'C-C': 2, 'C-H': 7}
1D rotors:
pivots: [1, 6], dihedral: [5, 1, 6, 11], rotor symmetry: 3, max scan energy: 5.14 kJ/mol
pivots: [1, 5], dihedral: [6, 1, 5, 2], rotor symmetry: 1, max scan energy: 33.58 kJ/mol
pivots: [4, 5], dihedral: [7, 4, 5, 1], rotor symmetry: 1, max scan energy: 16.52 kJ/mol
pivots: [4, 7], dihedral: [5, 4, 7, 3], rotor symmetry: 1, max scan energy: 17.54 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.05118700   -0.76063500   -0.31267700
O       0.78778600    1.40425100    0.52731800
O      -2.62823300   -0.83847600    0.37376200
C      -0.94515800    0.41430700   -0.79454400
C       0.56155300    0.55164000   -0.47035100
C       2.41517500   -0.84174600    0.09279500
C      -1.67026900   -0.11920600    0.42662800
H      -1.34338900    1.40942200   -1.01720100
H      -1.10618300   -0.24306300   -1.64905500
H       1.04759200    1.02854400   -1.36087800
H       2.64515400   -1.90196200    0.18655100
H       3.07642900   -0.39620300   -0.66272800
H       2.57690900   -0.34171300    1.05050600
H      -1.25194300    0.23701300    1.39522800
""",
)

entry(
    index = 35,
    label = "OOCCCOO",
    molecule =
"""
1  O u0 p2 c0 {3,S} {6,S}
2  O u0 p2 c0 {4,S} {7,S}
3  O u0 p2 c0 {1,S} {14,S}
4  O u0 p2 c0 {2,S} {15,S}
5  C u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
6  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
7  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58204,0.0537249,0.000598969,-5.68157e-06,1.38203e-08,-36528.4,10.0076], Tmin=(10,'K'), Tmax=(158.246,'K')),
            NASAPolynomial(coeffs=[7.04071,0.0429254,-2.49917e-05,6.99113e-09,-7.56405e-13,-36733.9,-3.33345], Tmin=(158.246,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-300.106,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Bond corrections: {'C-O': 2, 'O-O': 2, 'H-O': 2, 'C-C': 2, 'C-H': 6}
1D rotors:
pivots: [1, 6], dihedral: [2, 0, 5, 4], rotor symmetry: 1, max scan energy: 27.30 kJ/mol
pivots: [1, 3], dihedral: [6, 1, 3, 14], rotor symmetry: 1, max scan energy: 31.01 kJ/mol
pivots: [2, 4], dihedral: [7, 2, 4, 15], rotor symmetry: 1, max scan energy: 26.19 kJ/mol
pivots: [2, 7], dihedral: [4, 2, 7, 5], rotor symmetry: 1, max scan energy: 23.64 kJ/mol
pivots: [5, 6], dihedral: [7, 5, 6, 1], rotor symmetry: 3, max scan energy: 30.84 kJ/mol
pivots: [5, 7], dihedral: [6, 5, 7, 2], rotor symmetry: 1, max scan energy: 20.19 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O      -2.25653500   -0.33174600   -0.29017000
O       1.29619300   -0.19869600    1.96750100
O      -3.28514200    0.65070700    0.02670100
O       2.55307400    0.36767600    2.42170400
C      -1.03673800    0.15702600    1.78688100
C      -1.03267100    0.14283500    0.25968900
C       0.26002300    0.69361300    2.37701500
H      -1.85740500    0.79118800    2.13189000
H      -1.22535000   -0.85465900    2.15746500
H      -0.29367400   -0.56376300   -0.12567400
H      -0.80575900    1.13895600   -0.14152100
H       0.48198200    1.70042100    2.00431000
H       0.21013500    0.73081100    3.47177600
H      -3.50198800    0.95558500   -0.86467300
H       2.82127500   -0.30216600    3.06556400
""",
)

entry(
    index = 36,
    label = "COC(CC=O)OO",
    molecule =
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,D} {15,S}
5  O u0 p2 c0 {1,S} {3,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46553,0.0528639,-1.59421e-05,-1.41243e-08,8.45112e-12,-57027.7,12.6916], Tmin=(10,'K'), Tmax=(965.94,'K')),
            NASAPolynomial(coeffs=[8.58604,0.0452048,-2.50824e-05,6.70135e-09,-6.96141e-13,-58648.8,-15.1054], Tmin=(965.94,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-474.172,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (374.151,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Bond corrections: {'C-O': 3, 'C=O': 1, 'H-O': 1, 'C-H': 7, 'C-C': 2, 'O-O': 1}
1D rotors:
pivots: [1, 7], dihedral: [5, 1, 7, 12], rotor symmetry: 3, max scan energy: 6.47 kJ/mol
* Invalidated! pivots: [1, 5], dihedral: [7, 1, 5, 2], invalidation reason: scan has a barrier larger than 40 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [5, 2, 3, 16], invalidation reason: scan has a barrier larger than 40 kJ/mol
* Invalidated! pivots: [2, 5], dihedral: [3, 2, 5, 1], invalidation reason: scan has a barrier larger than 40 kJ/mol
* Invalidated! pivots: [5, 6], dihedral: [1, 5, 6, 8], invalidation reason: scan has a barrier larger than 40 kJ/mol
pivots: [6, 8], dihedral: [5, 6, 8, 4], rotor symmetry: 1, max scan energy: 23.19 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.59861400   -0.86281100    0.09998400
O       0.23156500    0.88932000    0.71211600
O      -0.25309800    2.01181900   -0.06046700
O      -2.48136200    0.30449900   -0.22653600
C       0.37498000   -0.25151700   -0.14593500
C      -0.69723900   -1.28667100    0.17705100
C       2.72457200   -0.08006600   -0.29936700
C      -2.12078600   -0.82175000    0.02983800
H       0.29828900    0.12029200   -1.17566900
H      -0.56020100   -2.18280700   -0.43992300
H      -0.56177000   -1.61954100    1.21440300
H       2.73538600    0.88080500    0.21951500
H       2.71358500    0.09128600   -1.38324000
H       3.60968900   -0.65548000   -0.03236600
H      -2.87971900   -1.61722800    0.18002100
H      -1.20008000    1.78414800   -0.11591200
""",
)

entry(
    index = 37,
    label = "[O]CCCOO",
    molecule =
"""
multiplicity 2
1     O u0 p2 c0 {2,S} {5,S}
2     O u0 p2 c0 {1,S} {13,S}
3  *2 O u1 p2 c0 {6,S}
4     C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
6  *1 C u0 p0 c0 {3,S} {4,S} {11,S} {12,S}
7     H u0 p0 c0 {4,S}
8     H u0 p0 c0 {4,S}
9     H u0 p0 c0 {5,S}
10    H u0 p0 c0 {5,S}
11    H u0 p0 c0 {6,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88539,0.00649985,0.000162584,-2.95731e-07,1.62234e-10,-16677.4,12.7128], Tmin=(10,'K'), Tmax=(589.356,'K')),
            NASAPolynomial(coeffs=[-0.275942,0.0612592,-4.42741e-05,1.46034e-08,-1.7907e-12,-16647.4,26.6818], Tmin=(589.356,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-138.716,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Bond corrections: {'C-O': 2, 'C-C': 2, 'H-O': 1, 'O-O': 1, 'C-H': 6}
1D rotors:
* Invalidated! pivots: [1, 5], dihedral: [2, 1, 5, 4], invalidation reason: scan has a barrier larger than 40 kJ/mol
* Invalidated! pivots: [1, 2], dihedral: [5, 1, 2, 13], invalidation reason: scan has a barrier larger than 40 kJ/mol
pivots: [4, 5], dihedral: [6, 4, 5, 1], rotor symmetry: 1, max scan energy: 35.85 kJ/mol
pivots: [4, 6], dihedral: [5, 4, 6, 3], rotor symmetry: 1, max scan energy: 36.49 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       1.47983300   -0.04579700   -0.27987100
O       1.25785600    1.12580800    0.54591800
O      -1.25609000    1.12629100   -0.56758800
C      -0.73496700   -1.16676200   -0.23569400
C       0.71331300   -1.11607200    0.25106500
C      -1.63398100    0.04860000    0.18651900
H      -1.22112600   -2.05641700    0.17963600
H      -0.76536100   -1.24889200   -1.32471900
H       1.23086000   -2.01499600   -0.10205500
H       0.76913300   -1.08939400    1.34396300
H      -1.45392600    0.23016500    1.25765600
H      -2.68290400   -0.22303500    0.00793200
H       0.48056600    1.51219700    0.09814000
""",
)

entry(
    index = 38,
    label = "O=COC=O",
    molecule =
"""
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {4,D}
3 O u0 p2 c0 {5,D}
4 C u0 p0 c0 {1,S} {2,D} {6,S}
5 C u0 p0 c0 {1,S} {3,D} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91016,0.0057145,9.04633e-05,-2.03729e-07,1.35406e-10,-59318,9.72741], Tmin=(10,'K'), Tmax=(508.613,'K')),
            NASAPolynomial(coeffs=[3.6506,0.0251566,-1.81936e-05,5.95911e-09,-7.25779e-13,-59516.6,8.5916], Tmin=(508.613,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-493.223,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (149.66,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Bond corrections: {'C-O': 2, 'C=O': 2, 'C-H': 2}
1D rotors:
pivots: [1, 5], dihedral: [4, 1, 5, 3], rotor symmetry: 1, max scan energy: 20.56 kJ/mol
pivots: [1, 4], dihedral: [5, 1, 4, 2], rotor symmetry: 1, max scan energy: 35.70 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
O       0.03988900   -0.71659700    0.00000200
O      -1.77601100    0.67594500   -0.00001300
O       2.12511500    0.09812900   -0.00000400
C      -1.30119200   -0.41736600   -0.00000200
C       0.96245200    0.32949300   -0.00000600
H      -1.85863000   -1.36265500    0.00000600
H       0.48550900    1.31491900   -0.00001500
""",
)


entry(
    index = 39,
    label = "C1COOC1",
    molecule =
"""
1  O u0 p2 c0 {2,S} {4,S}
2  O u0 p2 c0 {1,S} {5,S}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
5  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06755,-0.00538559,0.000122796,-1.80708e-07,8.47594e-11,-14775.6,9.4667], Tmin=(10,'K'), Tmax=(655.799,'K')),
            NASAPolynomial(coeffs=[-1.63575,0.0448646,-2.751e-05,8.04396e-09,-9.02048e-13,-14360.1,32.0404], Tmin=(655.799,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-122.851,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Bond corrections: {'C-O': 2, 'O-O': 1, 'C-C': 2, 'C-H': 6}

External symmetry: 2, optical isomers: 2

Geometry:
O       0.71706500   -0.88015400   -0.58508900
O      -0.57025200   -1.04653100    0.07866400
C      -0.05021500    1.25402000    0.06283700
C       1.19265700    0.34343500   -0.02330400
C      -1.18498900    0.22571200   -0.12738300
H      -0.10375000    1.75797400    1.02888900
H      -0.06691300    2.00982700   -0.72365500
H       1.62640600    0.16061400    0.96544400
H       1.96197400    0.70705600   -0.70626900
H      -1.97864700    0.29863600    0.61780200
H      -1.61153700    0.27941000   -1.13453600
""",
)

entry(
    index = 40,
    label = "CCC(OO)OC=O",
    molecule =
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {14,D} {15,S}
5  O u0 p2 c0 {2,S} {4,S}
6  O u0 p2 c0 {2,S} {7,S}
7  O u0 p2 c0 {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.37058,0.0580624,-3.39272e-05,6.10713e-09,8.86814e-13,-67560.7,12.9982], Tmin=(10,'K'), Tmax=(1099.94,'K')),
            NASAPolynomial(coeffs=[10.4554,0.0406601,-2.15986e-05,5.54617e-09,-5.5652e-13,-69625.1,-24.156], Tmin=(1099.94,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-561.773,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (369.994,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Bond corrections: {'C-O': 3, 'C=O': 1, 'H-O': 1, 'C-H': 7, 'C-C': 2, 'O-O': 1}
1D rotors:
* Invalidated! pivots: [1, 8], dihedral: [6, 1, 8, 4], invalidation reason: scan has a barrier larger than 40 kJ/mol
pivots: [1, 6], dihedral: [8, 1, 6, 2], rotor symmetry: 1, max scan energy: 37.16 kJ/mol
* Invalidated! pivots: [2, 6], dihedral: [3, 2, 6, 1], invalidation reason: scan has a barrier larger than 40 kJ/mol
* Invalidated! pivots: [2, 3], dihedral: [6, 2, 3, 16], invalidation reason: scan has a barrier larger than 40 kJ/mol
pivots: [5, 7], dihedral: [6, 5, 7, 12], rotor symmetry: 3, max scan energy: 11.30 kJ/mol
pivots: [5, 6], dihedral: [7, 5, 6, 1], rotor symmetry: 1, max scan energy: 19.66 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.00692800    1.03757800    0.28560500
O      -0.39485600   -1.29014400    0.54415800
O      -1.48716100   -1.74646800   -0.29110500
O      -2.20457700    0.87035000   -0.22656300
C       1.82158200   -0.51404100    0.25138300
C       0.36165600   -0.33908700   -0.12835300
C       2.75926600    0.49317300   -0.41766000
C      -1.23807500    1.48526700    0.15484600
H       2.09055500   -1.53613400   -0.02712700
H       1.89300900   -0.44891800    1.34101700
H       0.17641100   -0.41514300   -1.20156500
H       3.79431200    0.29442800   -0.13137500
H       2.51629700    1.51557300   -0.12474400
H       2.69887600    0.42850500   -1.50824400
H      -1.27609900    2.54030100    0.45687900
H      -2.06987500   -0.95923700   -0.26960400
""",
)

entry(
    index = 41,
    label = "CCC([O])OC=O",
    molecule =
"""
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  *1 C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {5,S} {13,D} {14,S}
5     O u0 p2 c0 {2,S} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8  *2 O u1 p2 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    O u0 p2 c0 {4,D}
14    H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97593,0.0459198,-2.36724e-05,3.92051e-09,2.07859e-13,-49999.2,12.2244], Tmin=(10,'K'), Tmax=(1604.47,'K')),
            NASAPolynomial(coeffs=[26.4196,0.00381382,2.74668e-06,-1.67796e-09,2.42079e-13,-58983.5,-112.219], Tmin=(1604.47,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-415.706,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (315.95,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""
Bond corrections: {'C-O': 3, 'C=O': 1, 'C-C': 2, 'C-H': 7}
1D rotors:
pivots: [1, 7], dihedral: [4, 0, 6, 2], rotor symmetry: 1, max scan energy: 51.70 kJ/mol
pivots: [1, 5], dihedral: [7, 1, 5, 2], rotor symmetry: 1, max scan energy: 32.98 kJ/mol
pivots: [4, 6], dihedral: [5, 4, 6, 11], rotor symmetry: 3, max scan energy: 11.92 kJ/mol
pivots: [4, 5], dihedral: [6, 4, 5, 1], rotor symmetry: 1, max scan energy: 17.48 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
O       0.61738100    0.06565800   -0.51969300
O      -0.47673300    2.09348200   -0.30195000
O       1.68139600   -0.10573500    1.47869200
C      -1.81586400    0.11814100   -0.28095700
C      -0.48711500    0.83205500    0.08133800
C      -1.88138100   -1.32492900    0.21493900
C       1.62071100   -0.29847400    0.29446900
H      -1.91817400    0.16280100   -1.36809900
H      -2.61531500    0.72268600    0.15247800
H      -0.33535900    0.80576600    1.17854300
H      -2.84849200   -1.76297300   -0.04336200
H      -1.10311200   -1.93683700   -0.24402900
H      -1.76638200   -1.38240400    1.30062700
H       2.39138400   -0.81596800   -0.29440400
""",
)
