#!/usr/bin/env python
# encoding: utf-8

name = "SABIC_aromatics"
shortDesc = u"Species relevant to aromatics formation, up to Benzo[a]pyrene (C20H12)"
longDesc = u"""
This library includes species from C6H5+O2 PES, 
10 first_to_second_ring pathways (Mebel 2017), naphthyl+acetylene HACA surfaces,
biphenyl decomposition, and other large PAHs up to Benzo[a]pyrene (C20H12).
Calculations done by Dr. Istvan Lengyel at CBS-QB3 level using Gaussian09 
(except for biphenyl C12H10 calculated by Max Liu using Gaussian03).
The calculations were done for the lowest energy conformer, but rotor scans 
were not performed. Thermo properties were evaluated with Cantherm, using 
bond additivity corrections from Petersson et al. 1998, because their training 
set included aromatic species (https://doi.org/10.1063/1.477794).
"""
entry(
    index = 0,
    label = "C4H3O2_6",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {5,S} {6,S}
2 O u0 p2 c0 {6,D}
3 C u0 p0 c0 {4,D} {6,S} {7,S}
4 C u0 p0 c0 {3,D} {5,S} {8,S}
5 C u1 p0 c0 {1,S} {4,S} {9,S}
6 C u0 p0 c0 {1,S} {2,D} {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.67401,0.0278533,1.78922e-06,-2.00655e-08,8.73312e-12,-19258,18.07], Tmin=(200,'K'), Tmax=(1029.77,'K')),
            NASAPolynomial(coeffs=[6.24477,0.0245704,-1.45088e-05,4.13287e-09,-4.54732e-13,-20966.6,-7.84094], Tmin=(1029.77,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "C4H5_1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,D} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 C u1 p0 c0 {2,D} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.03117,0.0250846,-9.41179e-07,-1.40302e-08,6.50388e-12,42100.2,15.6454], Tmin=(200,'K'), Tmax=(977.8,'K')),
            NASAPolynomial(coeffs=[4.75008,0.0231085,-1.19408e-05,3.03579e-09,-3.05378e-13,41131.3,0.35337], Tmin=(977.8,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "C5H5_2",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {1,S} {4,D} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.46619,0.0438111,-2.13798e-05,-6.21693e-09,6.50358e-12,30712,33.7787], Tmin=(200,'K'), Tmax=(902.09,'K')),
            NASAPolynomial(coeffs=[3.75767,0.0281847,-1.53019e-05,4.00234e-09,-4.05487e-13,29102,1.69376], Tmin=(902.09,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "C5H5O_6",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,S} {6,S}
2  C u0 p0 c0 {3,D} {4,S} {8,S}
3  C u0 p0 c0 {2,D} {5,S} {7,S}
4  C u0 p0 c0 {2,S} {6,D} {9,S}
5  C u1 p0 c0 {1,S} {3,S} {10,S}
6  C u0 p0 c0 {1,S} {4,D} {11,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.69692,0.0538189,-3.40177e-05,3.18292e-09,3.40275e-12,8300.45,36.3742], Tmin=(200,'K'), Tmax=(942.89,'K')),
            NASAPolynomial(coeffs=[5.37959,0.0313491,-1.70326e-05,4.43877e-09,-4.47387e-13,6253.18,-4.89519], Tmin=(942.89,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "C5H6_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,D} {8,S}
3  C u0 p0 c0 {1,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  C u0 p0 c0 {2,D} {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.03539,0.0394984,2.6981e-07,-3.00895e-08,1.52501e-11,15482.2,32.9681], Tmin=(200,'K'), Tmax=(880.57,'K')),
            NASAPolynomial(coeffs=[2.40632,0.0351284,-1.9212e-05,5.04515e-09,-5.12411e-13,14087.1,8.62464], Tmin=(880.57,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "C6H4_2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,D} {6,S} {9,S}
4  C u0 p0 c0 {2,D} {5,S} {10,S}
5  C u0 p0 c0 {4,S} {6,T}
6  C u0 p0 c0 {3,S} {5,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.55025,0.0437789,-2.01484e-05,-6.88498e-09,6.3568e-12,54058.4,30.767], Tmin=(200,'K'), Tmax=(926.47,'K')),
            NASAPolynomial(coeffs=[4.6105,0.0292253,-1.60874e-05,4.22611e-09,-4.28219e-13,52399.9,-1.27448], Tmin=(926.47,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "C6H4O_5",
    molecule = 
"""
1  O u0 p2 c0 {3,D}
2  C u0 p0 c0 {3,S} {4,D} {9,S}
3  C u0 p0 c0 {1,D} {2,S} {5,S}
4  C u0 p0 c0 {2,D} {6,S} {8,S}
5  C u0 p0 c0 {3,S} {7,D} {10,S}
6  C u0 p0 c0 {4,S} {7,D} {11,S}
7  C u0 p0 c0 {5,D} {6,D}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.595248,0.0435748,-1.65113e-05,-9.84546e-09,6.69511e-12,33949.5,22.2241], Tmin=(200,'K'), Tmax=(1006.25,'K')),
            NASAPolynomial(coeffs=[8.3157,0.0278109,-1.52623e-05,4.06826e-09,-4.24108e-13,31640.1,-18.8255], Tmin=(1006.25,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "C6H4O2_23",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,D}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {8,D}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  C u0 p0 c0 {1,S} {5,D} {12,S}
7  O u0 p2 c0 {1,D}
8  O u0 p2 c0 {4,D}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.206332,0.0499758,-2.33426e-05,-5.60267e-09,5.60355e-12,-15869.8,23.6928], Tmin=(200,'K'), Tmax=(1000.92,'K')),
            NASAPolynomial(coeffs=[8.30583,0.0317805,-1.73146e-05,4.52936e-09,-4.60628e-13,-18201.1,-18.9366], Tmin=(1000.92,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "C6H4O2_24",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,D}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {6,S} {12,S}
6  C u0 p0 c0 {1,S} {5,S} {8,D}
7  O u0 p2 c0 {1,D}
8  O u0 p2 c0 {6,D}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.190716,0.0504148,-2.45514e-05,-4.42655e-09,5.21594e-12,-11861.9,25.3088], Tmin=(200,'K'), Tmax=(1001.38,'K')),
            NASAPolynomial(coeffs=[8.34158,0.0316915,-1.72294e-05,4.49582e-09,-4.5605e-13,-14188,-17.4892], Tmin=(1001.38,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "C6H5_2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {8,S}
2  C u0 p0 c0 {1,B} {4,B} {7,S}
3  C u0 p0 c0 {1,B} {5,B} {9,S}
4  C u0 p0 c0 {2,B} {6,B} {10,S}
5  C u0 p0 c0 {3,B} {6,B} {11,S}
6  C u1 p0 c0 {4,B} {5,B}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.17895,0.0436842,-6.91687e-06,-2.47228e-08,1.36176e-11,40740.5,34.5865], Tmin=(200,'K'), Tmax=(892.06,'K')),
            NASAPolynomial(coeffs=[3.51814,0.0345603,-1.91882e-05,5.08444e-09,-5.19212e-13,39070.7,4.08971], Tmin=(892.06,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "C6H5O_7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {6,B} {8,S}
2  C u0 p0 c0 {1,B} {3,B} {7,S}
3  C u0 p0 c0 {2,B} {4,B} {9,S}
4  C u0 p0 c0 {3,B} {5,B} {10,S}
5  C u0 p0 c0 {4,B} {6,B} {11,S}
6  C u0 p0 c0 {1,B} {5,B} {12,S}
7  O u1 p2 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.956124,0.0365877,5.95999e-06,-2.9701e-08,1.24966e-11,4430.61,21.5708], Tmin=(200,'K'), Tmax=(1018.86,'K')),
            NASAPolynomial(coeffs=[5.84651,0.0360635,-2.07628e-05,5.77497e-09,-6.22585e-13,2464.77,-6.87067], Tmin=(1018.86,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "C6H5O_8",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {9,D}
4  C u1 p0 c0 {1,S} {6,S} {10,S}
5  C u0 p0 c0 {2,S} {6,D} {11,S}
6  C u0 p0 c0 {4,S} {5,D} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.457553,0.0438179,-7.81401e-06,-1.98689e-08,1.00348e-11,27027.1,25.0059], Tmin=(200,'K'), Tmax=(1015.83,'K')),
            NASAPolynomial(coeffs=[8.19333,0.032047,-1.8031e-05,4.94847e-09,-5.30408e-13,24491.1,-17.1828], Tmin=(1015.83,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "C6H5O_9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {5,S} {10,S}
5  C u0 p0 c0 {3,D} {4,S} {11,S}
6  C u1 p0 c0 {1,S} {12,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.506879,0.044284,-1.13011e-05,-1.57572e-08,8.66459e-12,21770.3,25.9979], Tmin=(200,'K'), Tmax=(1001.84,'K')),
            NASAPolynomial(coeffs=[7.60601,0.0322279,-1.76379e-05,4.68836e-09,-4.87165e-13,19530.5,-12.3439], Tmin=(1001.84,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "C6H5O2_1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {5,B} {8,S}
3  C u0 p0 c0 {1,B} {4,B} {12,S}
4  C u0 p0 c0 {3,B} {6,B} {9,S}
5  C u0 p0 c0 {2,B} {6,B} {10,S}
6  C u0 p0 c0 {4,B} {5,B} {11,S}
7  O u0 p2 c0 {1,S} {13,S}
8  O u1 p2 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.197216,0.0542408,-2.32432e-05,-9.07864e-09,7.2445e-12,-17392.2,26.6659], Tmin=(200,'K'), Tmax=(1005,'K')),
            NASAPolynomial(coeffs=[9.38534,0.0334979,-1.82488e-05,4.83222e-09,-5.00468e-13,-20196.8,-23.9831], Tmin=(1005,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "C6H5O2_10",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,D} {5,S} {11,S}
5  C u0 p0 c0 {3,D} {4,S} {12,S}
6  O u0 p2 c0 {1,S} {7,S}
7  C u1 p0 c0 {6,S} {13,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.174107,0.0545353,-2.45597e-05,-7.41456e-09,6.6271e-12,2992.57,29.9036], Tmin=(200,'K'), Tmax=(1001.77,'K')),
            NASAPolynomial(coeffs=[8.99542,0.0342406,-1.86059e-05,4.88405e-09,-5.00099e-13,336.587,-18.4372], Tmin=(1001.77,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "C6H5O2_11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {6,S} {12,S}
6  O u0 p2 c0 {1,S} {5,S}
7  C u1 p0 c0 {1,S} {13,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.267132,0.05784,-3.44293e-05,2.54186e-09,3.2794e-12,3534.27,29.0013], Tmin=(200,'K'), Tmax=(1007.03,'K')),
            NASAPolynomial(coeffs=[9.1829,0.0335055,-1.7847e-05,4.58242e-09,-4.59052e-13,961.578,-19.9795], Tmin=(1007.03,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "C6H5O2_12",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u1 p0 c0 {1,S} {5,S} {10,S}
4  C u0 p0 c0 {2,D} {6,S} {13,S}
5  C u0 p0 c0 {3,S} {6,D} {11,S}
6  C u0 p0 c0 {4,S} {5,D} {12,S}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {2,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.00203041,0.0497878,-1.06836e-05,-2.06924e-08,1.07989e-11,33049.9,26.4283], Tmin=(200,'K'), Tmax=(1013.84,'K')),
            NASAPolynomial(coeffs=[8.752,0.0357541,-2.02575e-05,5.55179e-09,-5.91697e-13,30221.1,-21.1221], Tmin=(1013.84,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "C6H5O2_13",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {9,D}
4  C u0 p0 c0 {2,D} {6,S} {11,S}
5  C u0 p0 c0 {3,S} {6,D} {13,S}
6  C u0 p0 c0 {4,S} {5,D} {12,S}
7  O u1 p2 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.295062,0.0572259,-3.10324e-05,-1.49217e-09,4.73776e-12,6671.94,28.6311], Tmin=(200,'K'), Tmax=(1004.07,'K')),
            NASAPolynomial(coeffs=[9.30823,0.0338143,-1.82358e-05,4.73714e-09,-4.7977e-13,3995.12,-21.4648], Tmin=(1004.07,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "C6H5O2_14",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {8,S}
2  C u1 p0 c0 {1,S} {4,S} {7,S}
3  C u0 p0 c0 {1,D} {5,S} {9,S}
4  C u0 p0 c0 {2,S} {6,D} {10,S}
5  C u0 p0 c0 {3,S} {11,D} {12,S}
6  C u0 p0 c0 {4,D} {13,D}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 O u0 p2 c0 {5,D}
12 H u0 p0 c0 {5,S}
13 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.65028,0.0508821,-3.14458e-05,6.24728e-09,7.43666e-13,-4142.71,16.6785], Tmin=(200,'K'), Tmax=(1075.81,'K')),
            NASAPolynomial(coeffs=[9.77107,0.0324688,-1.70141e-05,4.27051e-09,-4.15832e-13,-6141.42,-20.3641], Tmin=(1075.81,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "C6H5O2_15",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {9,S}
3  C u1 p0 c0 {1,S} {5,S} {10,S}
4  C u0 p0 c0 {2,S} {6,D} {11,S}
5  C u0 p0 c0 {3,S} {6,S} {12,D}
6  C u0 p0 c0 {4,D} {5,S} {13,S}
7  O u0 p2 c0 {1,S} {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.00785992,0.0504497,-1.33606e-05,-1.79061e-08,9.91131e-12,2997.59,27.4717], Tmin=(200,'K'), Tmax=(1008.44,'K')),
            NASAPolynomial(coeffs=[8.636,0.0354775,-1.98187e-05,5.35503e-09,-5.6348e-13,272.159,-19.1718], Tmin=(1008.44,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "C6H5O2_16",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {10,D}
4  C u0 p0 c0 {1,S} {6,D} {11,S}
5  C u1 p0 c0 {3,S} {6,S} {12,S}
6  C u0 p0 c0 {4,D} {5,S} {13,S}
7  O u0 p2 c0 {1,S} {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0726432,0.0490166,-1.0065e-05,-2.06548e-08,1.06975e-11,-1616.68,27.1756], Tmin=(200,'K'), Tmax=(1010.39,'K')),
            NASAPolynomial(coeffs=[8.34178,0.0361018,-2.03189e-05,5.52696e-09,-5.84721e-13,-4299.47,-17.8105], Tmin=(1010.39,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "C6H5O2_17",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {4,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {8,D}
4  C u0 p0 c0 {1,S} {6,D} {9,S}
5  C u1 p0 c0 {3,S} {7,S} {12,S}
6  C u0 p0 c0 {4,D} {7,S} {13,S}
7  O u0 p2 c0 {5,S} {6,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.120575,0.0543247,-2.53653e-05,-5.99711e-09,6.05783e-12,1240.7,27.2402], Tmin=(200,'K'), Tmax=(999.62,'K')),
            NASAPolynomial(coeffs=[8.66887,0.0344884,-1.86109e-05,4.84496e-09,-4.91877e-13,-1282.68,-18.9927], Tmin=(999.62,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "C6H5O2_18",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  C u0 p0 c0 {1,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {6,S} {12,S}
6  C u1 p0 c0 {5,S} {7,S} {13,S}
7  O u0 p2 c0 {2,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.227368,0.0541453,-2.15218e-05,-1.12246e-08,7.99768e-12,12095.6,28.6828], Tmin=(200,'K'), Tmax=(1007.6,'K')),
            NASAPolynomial(coeffs=[9.54226,0.0337698,-1.85933e-05,4.96938e-09,-5.19018e-13,9192.41,-23.161], Tmin=(1007.6,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "C6H5O2_19",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,D}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {6,S} {11,S}
5  C u0 p0 c0 {2,S} {6,D} {13,S}
6  C u0 p0 c0 {4,S} {5,D} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {2,D}
10 H u0 p0 c0 {3,S}
11 O u1 p2 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.144797,0.0555579,-2.88468e-05,-2.38594e-09,4.80142e-12,-9861.33,28.6179], Tmin=(200,'K'), Tmax=(1001.39,'K')),
            NASAPolynomial(coeffs=[8.54355,0.0348403,-1.87658e-05,4.85152e-09,-4.87818e-13,-12302.7,-16.8121], Tmin=(1001.39,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "C6H5O2_20",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {2,S} {3,D} {11,S}
5  C u0 p0 c0 {2,S} {6,D} {12,S}
6  C u0 p0 c0 {1,S} {5,D} {13,S}
7  O u0 p2 c0 {1,S} {2,S}
8  O u1 p2 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.270107,0.0528265,-1.48513e-05,-1.87232e-08,1.04879e-11,18714.3,27.0524], Tmin=(200,'K'), Tmax=(1024.18,'K')),
            NASAPolynomial(coeffs=[10.4002,0.0334682,-1.91826e-05,5.37067e-09,-5.86434e-13,15358.2,-30.3945], Tmin=(1024.18,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "C6H5O2_21",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {5,S} {11,S}
4  C u0 p0 c0 {1,S} {7,D} {10,S}
5  C u0 p0 c0 {3,S} {6,S} {12,D}
6  O u0 p2 c0 {1,S} {5,S}
7  C u1 p0 c0 {4,D} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.377804,0.0585306,-3.39778e-05,9.13731e-10,4.04277e-12,5274.12,29.4061], Tmin=(200,'K'), Tmax=(1006.53,'K')),
            NASAPolynomial(coeffs=[9.76941,0.0328809,-1.76237e-05,4.56754e-09,-4.62693e-13,2488.01,-23.3074], Tmin=(1006.53,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "C6H5O2_22",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  C u0 p0 c0 {1,S} {5,D} {11,S}
5  C u0 p0 c0 {2,S} {4,D} {12,S}
6  C u0 p0 c0 {1,S} {7,S} {13,D}
7  O u0 p2 c0 {2,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.248042,0.0452628,-3.2837e-07,-2.91675e-08,1.31234e-11,1466.89,25.7173], Tmin=(200,'K'), Tmax=(1027.07,'K')),
            NASAPolynomial(coeffs=[7.98669,0.0376161,-2.20097e-05,6.22807e-09,-6.82319e-13,-1309.04,-17.5991], Tmin=(1027.07,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "C6H5O2_23",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  C u1 p0 c0 {1,S} {6,S} {11,S}
5  C u0 p0 c0 {2,S} {6,D} {12,S}
6  C u0 p0 c0 {4,S} {5,D} {13,S}
7  O u0 p2 c0 {1,S} {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.00124827,0.0496491,-1.03764e-05,-2.09826e-08,1.08861e-11,4686.9,27.0519], Tmin=(200,'K'), Tmax=(1015.63,'K')),
            NASAPolynomial(coeffs=[8.85955,0.0355005,-2.01248e-05,5.53159e-09,-5.91854e-13,1816.9,-21.1022], Tmin=(1015.63,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "C6H5O2_24",
    molecule = 
"""
multiplicity 4
1  O u1 p2 c0 {3,S}
2  O u0 p2 c0 {6,D}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
4  C u1 p0 c0 {3,S} {6,S} {10,S}
5  C u0 p0 c0 {3,S} {7,D} {11,S}
6  C u0 p0 c0 {2,D} {4,S} {8,S}
7  C u0 p0 c0 {5,D} {8,S} {13,S}
8  C u1 p0 c0 {6,S} {7,S} {12,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.44573,0.0578919,-2.90353e-05,-5.19551e-09,6.24692e-12,26245.9,29.7289], Tmin=(200,'K'), Tmax=(1008.5,'K')),
            NASAPolynomial(coeffs=[10.2061,0.0331272,-1.82056e-05,4.83552e-09,-5.00982e-13,23208.3,-26.1583], Tmin=(1008.5,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "C6H5O2_25",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {6,B} {11,S}
3  C u0 p0 c0 {1,B} {5,B} {12,S}
4  C u0 p0 c0 {5,B} {6,B} {9,S}
5  C u0 p0 c0 {3,B} {4,B} {8,S}
6  C u0 p0 c0 {2,B} {4,B} {10,S}
7  O u0 p2 c0 {1,S} {13,S}
8  O u1 p2 c0 {5,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.313446,0.0561957,-2.74397e-05,-5.65046e-09,6.24684e-12,-17613,27.0415], Tmin=(200,'K'), Tmax=(1006.26,'K')),
            NASAPolynomial(coeffs=[9.8639,0.0327109,-1.77303e-05,4.67767e-09,-4.83259e-13,-20520.4,-26.3912], Tmin=(1006.26,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "C6H5O2_26",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,D}
3  C u0 p0 c0 {1,S} {5,S} {10,D}
4  C u1 p0 c0 {2,S} {6,S} {11,S}
5  C u0 p0 c0 {3,S} {6,D} {13,S}
6  C u0 p0 c0 {4,S} {5,D} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {2,D}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.381453,0.0453571,-7.19241e-06,-2.10057e-08,1.04661e-11,-15654.2,24.7405], Tmin=(200,'K'), Tmax=(1002.9,'K')),
            NASAPolynomial(coeffs=[7.248,0.0359389,-1.99806e-05,5.35961e-09,-5.59349e-13,-17935.1,-12.9117], Tmin=(1002.9,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "C6H5O2_27",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,D} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {9,D}
4  C u0 p0 c0 {3,S} {6,S} {11,D}
5  C u0 p0 c0 {2,D} {6,S} {13,S}
6  C u1 p0 c0 {4,S} {5,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.133583,0.0552122,-2.79161e-05,-3.30113e-09,5.10942e-12,-10718,27.9954], Tmin=(200,'K'), Tmax=(1000.54,'K')),
            NASAPolynomial(coeffs=[8.52027,0.0348732,-1.87991e-05,4.86665e-09,-4.9013e-13,-13163.4,-17.3255], Tmin=(1000.54,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "C6H5O2_5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {8,S}
3  C u0 p0 c0 {1,B} {6,B} {12,S}
4  C u0 p0 c0 {2,B} {5,B} {9,S}
5  C u0 p0 c0 {4,B} {6,B} {10,S}
6  C u0 p0 c0 {3,B} {5,B} {11,S}
7  O u0 p2 c0 {1,S} {13,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.104015,0.0489208,-1.08238e-05,-1.95636e-08,1.03108e-11,14672,26.3553], Tmin=(200,'K'), Tmax=(1006.76,'K')),
            NASAPolynomial(coeffs=[8.12791,0.0361147,-2.01624e-05,5.43895e-09,-5.70931e-13,12089.7,-17.2102], Tmin=(1006.76,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "C6H5O2_6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {4,S} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,S} {6,D} {11,S}
5  C u0 p0 c0 {3,D} {6,S} {13,S}
6  C u0 p0 c0 {4,D} {5,S} {12,S}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {1,S} {7,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.210352,0.0533291,-1.87414e-05,-1.40456e-08,8.90589e-12,21655.7,25.9437], Tmin=(200,'K'), Tmax=(1011.24,'K')),
            NASAPolynomial(coeffs=[9.61035,0.0339625,-1.89088e-05,5.11351e-09,-5.39878e-13,18673.4,-26.4699], Tmin=(1011.24,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "C6H5O2_7",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {10,S}
3  C u0 p0 c0 {2,D} {5,S} {9,S}
4  C u0 p0 c0 {1,S} {6,D} {11,S}
5  C u0 p0 c0 {3,S} {7,S} {12,D}
6  C u0 p0 c0 {4,D} {7,S} {13,S}
7  O u0 p2 c0 {5,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0672223,0.0526366,-2.04335e-05,-1.08699e-08,7.65972e-12,-9917.08,27.3727], Tmin=(200,'K'), Tmax=(1000.56,'K')),
            NASAPolynomial(coeffs=[8.61606,0.0347881,-1.89596e-05,4.99435e-09,-5.1331e-13,-12498.9,-18.7427], Tmin=(1000.56,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "C6H5O2_8",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {9,S}
3  C u1 p0 c0 {1,S} {6,S} {10,S}
4  C u0 p0 c0 {2,S} {6,D} {11,S}
5  C u0 p0 c0 {1,S} {7,S} {12,D}
6  C u0 p0 c0 {3,S} {4,D} {13,S}
7  O u0 p2 c0 {2,S} {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.213874,0.0462,-3.04359e-06,-2.67064e-08,1.2426e-11,-8699.15,26.6673], Tmin=(200,'K'), Tmax=(1019.87,'K')),
            NASAPolynomial(coeffs=[7.96649,0.0372616,-2.14719e-05,5.97962e-09,-6.45841e-13,-11396.9,-16.3607], Tmin=(1019.87,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "C6H5O2_9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {5,S} {10,S}
5  C u0 p0 c0 {3,D} {4,S} {11,S}
6  C u0 p0 c0 {1,S} {12,S} {13,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 O u1 p2 c0 {6,S}
13 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.321616,0.0566105,-2.82437e-05,-4.84006e-09,5.95876e-12,913.933,28.6717], Tmin=(200,'K'), Tmax=(1005.26,'K')),
            NASAPolynomial(coeffs=[9.6759,0.0333253,-1.81126e-05,4.76483e-09,-4.89474e-13,-1929.56,-23.7586], Tmin=(1005.26,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "C6H6_7",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {6,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {8,S}
3  C u0 p0 c0 {2,B} {4,B} {9,S}
4  C u0 p0 c0 {3,B} {5,B} {10,S}
5  C u0 p0 c0 {4,B} {6,B} {11,S}
6  C u0 p0 c0 {1,B} {5,B} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.34956,0.0426033,4.18859e-06,-3.77183e-08,1.85245e-11,8835.36,33.1038], Tmin=(200,'K'), Tmax=(880.42,'K')),
            NASAPolynomial(coeffs=[2.44278,0.0393145,-2.16999e-05,5.73056e-09,-5.84085e-13,7275.11,6.52533], Tmin=(880.42,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "C7H7_5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {8,S}
3  C u0 p0 c0 {1,B} {6,B} {12,S}
4  C u0 p0 c0 {2,B} {5,B} {9,S}
5  C u0 p0 c0 {4,B} {6,B} {10,S}
6  C u0 p0 c0 {3,B} {5,B} {11,S}
7  C u1 p0 c0 {1,S} {13,S} {14,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.472652,0.0428009,6.14098e-06,-3.34592e-08,1.42086e-11,23372.9,23.0709], Tmin=(200,'K'), Tmax=(1010.21,'K')),
            NASAPolynomial(coeffs=[5.90426,0.0420204,-2.34754e-05,6.39506e-09,-6.80282e-13,21217.9,-8.4231], Tmin=(1010.21,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "C7H7_6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {7,B}
3  C u0 p0 c0 {2,B} {4,B} {13,S}
4  C u0 p0 c0 {3,B} {5,B} {12,S}
5  C u0 p0 c0 {4,B} {6,B} {11,S}
6  C u0 p0 c0 {5,B} {7,B} {14,S}
7  C u1 p0 c0 {2,B} {6,B}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.611907,0.0417216,6.38883e-06,-3.26132e-08,1.38453e-11,35404.9,24.7782], Tmin=(200,'K'), Tmax=(994.55,'K')),
            NASAPolynomial(coeffs=[4.90883,0.0430189,-2.35892e-05,6.26487e-09,-6.48916e-13,33631.4,-0.54794], Tmin=(994.55,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "C7H7_7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {11,S}
4  C u0 p0 c0 {2,B} {6,B} {12,S}
5  C u0 p0 c0 {3,B} {7,B} {13,S}
6  C u0 p0 c0 {4,B} {7,B} {14,S}
7  C u1 p0 c0 {5,B} {6,B}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.602113,0.0418853,6.06096e-06,-3.23615e-08,1.37787e-11,35999.5,26.8283], Tmin=(200,'K'), Tmax=(994.17,'K')),
            NASAPolynomial(coeffs=[4.93868,0.042974,-2.35497e-05,6.24939e-09,-6.46798e-13,34221.2,1.3251], Tmin=(994.17,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "C7H7_8",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {5,B}
3  C u0 p0 c0 {2,B} {4,B} {12,S}
4  C u0 p0 c0 {3,B} {6,B} {11,S}
5  C u0 p0 c0 {2,B} {7,B} {13,S}
6  C u0 p0 c0 {4,B} {7,B} {14,S}
7  C u1 p0 c0 {5,B} {6,B}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.599922,0.0418657,6.1944e-06,-3.25129e-08,1.38257e-11,35407.8,24.9681], Tmin=(200,'K'), Tmax=(995.01,'K')),
            NASAPolynomial(coeffs=[4.96673,0.042959,-2.35659e-05,6.26206e-09,-6.49011e-13,33615.7,-0.716122], Tmin=(995.01,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "C7H8_27",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {11,S}
4  C u0 p0 c0 {2,B} {7,B} {15,S}
5  C u0 p0 c0 {3,B} {6,B} {12,S}
6  C u0 p0 c0 {5,B} {7,B} {13,S}
7  C u0 p0 c0 {4,B} {6,B} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.91933,0.0472277,9.25348e-06,-4.42895e-08,2.04341e-11,4144.24,34.2103], Tmin=(200,'K'), Tmax=(896.73,'K')),
            NASAPolynomial(coeffs=[2.14773,0.0488592,-2.65512e-05,6.91884e-09,-6.97615e-13,2619.81,10.5995], Tmin=(896.73,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "C7H8_53",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {5,S} {6,S} {7,D}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {1,S} {6,D} {11,S}
5  C u0 p0 c0 {2,S} {3,D} {12,S}
6  C u0 p0 c0 {2,S} {4,D} {13,S}
7  C u0 p0 c0 {2,D} {14,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.522711,0.0421934,1.23618e-05,-3.91307e-08,1.59196e-11,18578.7,22.1888], Tmin=(200,'K'), Tmax=(999.87,'K')),
            NASAPolynomial(coeffs=[4.33753,0.047393,-2.61343e-05,7.00313e-09,-7.32669e-13,16793.1,-1.32952], Tmin=(999.87,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "C7H8_54",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {7,D}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,S} {6,D} {11,S}
5  C u0 p0 c0 {3,D} {6,S} {13,S}
6  C u0 p0 c0 {4,D} {5,S} {12,S}
7  C u0 p0 c0 {2,D} {14,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.461779,0.0430807,1.06089e-05,-3.78556e-08,1.55969e-11,20567.8,23.6192], Tmin=(200,'K'), Tmax=(999.45,'K')),
            NASAPolynomial(coeffs=[4.63512,0.046843,-2.57522e-05,6.88619e-09,-7.19471e-13,18711.5,-1.62584], Tmin=(999.45,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "C7H9_4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,D} {12,S}
4  C u0 p0 c0 {1,S} {6,D} {13,S}
5  C u0 p0 c0 {3,D} {7,S} {15,S}
6  C u0 p0 c0 {4,D} {7,S} {16,S}
7  C u1 p0 c0 {5,S} {6,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.17429,0.0469534,9.54105e-06,-3.90124e-08,1.62996e-11,19036.6,26.1256], Tmin=(200,'K'), Tmax=(994.23,'K')),
            NASAPolynomial(coeffs=[4.71393,0.0500091,-2.72342e-05,7.21456e-09,-7.47509e-13,17080.2,-1.04842], Tmin=(994.23,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "C8H10_157",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {4,B} {5,B}
4  C u0 p0 c0 {3,B} {6,B} {14,S}
5  C u0 p0 c0 {3,B} {8,B} {18,S}
6  C u0 p0 c0 {4,B} {7,B} {15,S}
7  C u0 p0 c0 {6,B} {8,B} {16,S}
8  C u0 p0 c0 {5,B} {7,B} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.292222,0.0531668,1.07291e-05,-4.38536e-08,1.83663e-11,978.653,28.757], Tmin=(200,'K'), Tmax=(985.19,'K')),
            NASAPolynomial(coeffs=[4.2249,0.0577742,-3.12242e-05,8.17793e-09,-8.36556e-13,-1025.04,1.37994], Tmin=(985.19,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "C8H10_327",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
4  C u0 p0 c0 {7,S} {8,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {7,D} {15,S}
6  C u0 p0 c0 {1,S} {8,D} {18,S}
7  C u0 p0 c0 {4,S} {5,D} {16,S}
8  C u0 p0 c0 {4,S} {6,D} {17,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.368081,0.0531629,1.30017e-05,-4.66721e-08,1.924e-11,21243.3,27.2334], Tmin=(200,'K'), Tmax=(999.97,'K')),
            NASAPolynomial(coeffs=[4.84428,0.0576525,-3.17438e-05,8.50076e-09,-8.89255e-13,18934,-4.24782], Tmin=(999.97,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "C8H10_328",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {7,D} {15,S}
6  C u0 p0 c0 {4,S} {8,D} {16,S}
7  C u0 p0 c0 {5,D} {8,S} {17,S}
8  C u0 p0 c0 {6,D} {7,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.376961,0.0531645,1.32499e-05,-4.69826e-08,1.93341e-11,21755.8,27.086], Tmin=(200,'K'), Tmax=(1001.77,'K')),
            NASAPolynomial(coeffs=[4.92187,0.0576347,-3.18177e-05,8.54666e-09,-8.96671e-13,19408.2,-4.9056], Tmin=(1001.77,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "C8H5_2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,B} {6,B} {7,S}
2  C u0 p0 c0 {3,B} {4,B} {10,S}
3  C u0 p0 c0 {1,B} {2,B} {11,S}
4  C u0 p0 c0 {2,B} {5,B} {9,S}
5  C u0 p0 c0 {4,B} {6,B} {12,S}
6  C u1 p0 c0 {1,B} {5,B}
7  C u0 p0 c0 {1,S} {8,T}
8  C u0 p0 c0 {7,T} {13,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.202,0.0548923,-2.58854e-05,-6.24097e-09,6.29813e-12,68882.4,26.7988], Tmin=(200,'K'), Tmax=(1002.63,'K')),
            NASAPolynomial(coeffs=[9.36413,0.0330972,-1.77679e-05,4.64508e-09,-4.76473e-13,66141.4,-23.4804], Tmin=(1002.63,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "C8H6_12",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {9,S}
3  C u0 p0 c0 {1,B} {6,B} {13,S}
4  C u0 p0 c0 {2,B} {5,B} {10,S}
5  C u0 p0 c0 {4,B} {6,B} {11,S}
6  C u0 p0 c0 {3,B} {5,B} {12,S}
7  C u0 p0 c0 {1,S} {8,T}
8  C u0 p0 c0 {7,T} {14,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.176456,0.0533377,-1.55083e-05,-1.66668e-08,9.6539e-12,36244.6,25.3683], Tmin=(200,'K'), Tmax=(999.16,'K')),
            NASAPolynomial(coeffs=[8.36218,0.0378834,-2.04245e-05,5.37379e-09,-5.5489e-13,33603.4,-20.4968], Tmin=(999.16,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "C8H7_2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {4,S} {8,B}
2  C u0 p0 c0 {1,B} {3,B} {12,S}
3  C u0 p0 c0 {2,B} {5,B} {11,S}
4  C u0 p0 c0 {1,S} {7,D} {9,S}
5  C u0 p0 c0 {3,B} {6,B} {10,S}
6  C u0 p0 c0 {5,B} {8,B} {13,S}
7  C u0 p0 c0 {4,D} {14,S} {15,S}
8  C u1 p0 c0 {1,B} {6,B}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.160933,0.0522535,-5.67708e-06,-2.65587e-08,1.27832e-11,46259.8,27.5584], Tmin=(200,'K'), Tmax=(996.93,'K')),
            NASAPolynomial(coeffs=[7.06977,0.04381,-2.39205e-05,6.33631e-09,-6.55628e-13,43796,-12.4296], Tmin=(996.93,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "C8H7_3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {9,S}
3  C u0 p0 c0 {1,B} {6,B} {13,S}
4  C u0 p0 c0 {2,B} {5,B} {10,S}
5  C u0 p0 c0 {4,B} {6,B} {11,S}
6  C u0 p0 c0 {3,B} {5,B} {12,S}
7  C u0 p0 c0 {1,S} {8,D} {14,S}
8  C u1 p0 c0 {7,D} {15,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.305423,0.0543171,-9.50797e-06,-2.38011e-08,1.20606e-11,46792.3,27.8292], Tmin=(200,'K'), Tmax=(998.65,'K')),
            NASAPolynomial(coeffs=[7.73719,0.0428047,-2.33108e-05,6.17118e-09,-6.3914e-13,44153.7,-16.1292], Tmin=(998.65,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "C8H8_49",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {4,S}
2  C u0 p0 c0 {1,B} {5,B} {10,S}
3  C u0 p0 c0 {1,B} {7,B} {14,S}
4  C u0 p0 c0 {1,S} {8,D} {9,S}
5  C u0 p0 c0 {2,B} {6,B} {11,S}
6  C u0 p0 c0 {5,B} {7,B} {12,S}
7  C u0 p0 c0 {3,B} {6,B} {13,S}
8  C u0 p0 c0 {4,D} {15,S} {16,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.129028,0.0510074,3.37121e-06,-3.53233e-08,1.54856e-11,15759.2,27.6842], Tmin=(200,'K'), Tmax=(997.93,'K')),
            NASAPolynomial(coeffs=[5.96983,0.0487977,-2.67311e-05,7.1155e-09,-7.40013e-13,13434.8,-7.27414], Tmin=(997.93,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "C8H8_92",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {2,S} {3,D} {13,S}
5  C u0 p0 c0 {1,S} {7,D} {12,S}
6  C u0 p0 c0 {3,S} {8,D} {16,S}
7  C u0 p0 c0 {5,D} {8,S} {15,S}
8  C u0 p0 c0 {6,D} {7,S} {14,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.70936,0.06604,-1.70482e-05,-2.61104e-08,1.52936e-11,38879.7,42.4115], Tmin=(200,'K'), Tmax=(917.73,'K')),
            NASAPolynomial(coeffs=[4.52763,0.0515132,-2.82414e-05,7.39998e-09,-7.48621e-13,36467.7,-1.5241], Tmin=(917.73,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "C8H9_11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {11,S}
4  C u0 p0 c0 {2,B} {7,B} {15,S}
5  C u0 p0 c0 {3,B} {6,B} {12,S}
6  C u0 p0 c0 {5,B} {7,B} {13,S}
7  C u0 p0 c0 {4,B} {6,B} {14,S}
8  C u1 p0 c0 {1,S} {16,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.757156,0.0615161,-1.34338e-05,-2.2902e-08,1.21698e-11,26241.2,32.0562], Tmin=(200,'K'), Tmax=(984.5,'K')),
            NASAPolynomial(coeffs=[7.13581,0.0497305,-2.6381e-05,6.79257e-09,-6.84962e-13,23704.1,-10.8917], Tmin=(984.5,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "C8H9_12",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {4,B} {5,B}
3  C u1 p0 c0 {1,S} {2,S} {12,S}
4  C u0 p0 c0 {2,B} {6,B} {13,S}
5  C u0 p0 c0 {2,B} {8,B} {17,S}
6  C u0 p0 c0 {4,B} {7,B} {14,S}
7  C u0 p0 c0 {6,B} {8,B} {15,S}
8  C u0 p0 c0 {5,B} {7,B} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.571906,0.0583155,-6.45063e-06,-2.86634e-08,1.38509e-11,19362.1,30.0958], Tmin=(200,'K'), Tmax=(984.69,'K')),
            NASAPolynomial(coeffs=[6.41085,0.0509486,-2.72155e-05,7.05121e-09,-7.14761e-13,16968.9,-8.65348], Tmin=(984.69,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "C8H9_13",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {4,B} {8,B}
4  C u0 p0 c0 {3,B} {5,B} {16,S}
5  C u0 p0 c0 {4,B} {6,B} {15,S}
6  C u0 p0 c0 {5,B} {7,B} {14,S}
7  C u0 p0 c0 {6,B} {8,B} {17,S}
8  C u1 p0 c0 {3,B} {7,B}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.325594,0.0545339,1.20082e-06,-3.45661e-08,1.54841e-11,32825.9,29.5288], Tmin=(200,'K'), Tmax=(983.17,'K')),
            NASAPolynomial(coeffs=[5.31356,0.0527548,-2.83738e-05,7.38235e-09,-7.49883e-13,30694.2,-2.78297], Tmin=(983.17,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "C8H9_14",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {6,D} {13,S}
5  C u0 p0 c0 {1,S} {7,D} {14,S}
6  C u0 p0 c0 {4,D} {8,S} {16,S}
7  C u0 p0 c0 {5,D} {8,S} {17,S}
8  C u1 p0 c0 {6,S} {7,S} {15,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.512292,0.0551638,3.92674e-06,-3.8825e-08,1.69495e-11,31055.3,27.8415], Tmin=(200,'K'), Tmax=(1007.83,'K')),
            NASAPolynomial(coeffs=[6.84185,0.0514569,-2.84813e-05,7.6996e-09,-8.1437e-13,28278.9,-14.1155], Tmin=(1007.83,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "C8H9_15",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {6,D}
5  C u0 p0 c0 {1,S} {7,D} {14,S}
6  C u0 p0 c0 {4,D} {8,S} {17,S}
7  C u0 p0 c0 {5,D} {8,S} {16,S}
8  C u1 p0 c0 {6,S} {7,S} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.21518,0.070422,-1.85028e-05,-2.71592e-08,1.59834e-11,35670.2,45.3054], Tmin=(200,'K'), Tmax=(918.49,'K')),
            NASAPolynomial(coeffs=[4.46569,0.055069,-3.00963e-05,7.86974e-09,-7.95027e-13,33128.5,-0.992157], Tmin=(918.49,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "C8H9_16",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  C u0 p0 c0 {1,S} {5,D} {11,S}
3  C u0 p0 c0 {1,S} {6,D} {12,S}
4  C u0 p0 c0 {1,S} {8,D} {10,S}
5  C u0 p0 c0 {2,D} {7,S} {14,S}
6  C u0 p0 c0 {3,D} {7,S} {15,S}
7  C u1 p0 c0 {5,S} {6,S} {13,S}
8  C u0 p0 c0 {4,D} {16,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.634758,0.0582078,-4.26663e-06,-3.15094e-08,1.48413e-11,32077.2,30.6449], Tmin=(200,'K'), Tmax=(993.75,'K')),
            NASAPolynomial(coeffs=[6.98823,0.0504853,-2.72682e-05,7.17195e-09,-7.38988e-13,29428.4,-11.7882], Tmin=(993.75,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "C8H9_17",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,D} {5,S}
3  C u0 p0 c0 {1,S} {6,D} {11,S}
4  C u0 p0 c0 {2,D} {7,S} {14,S}
5  C u0 p0 c0 {2,S} {8,D} {13,S}
6  C u0 p0 c0 {3,D} {7,S} {15,S}
7  C u1 p0 c0 {4,S} {6,S} {12,S}
8  C u0 p0 c0 {5,D} {16,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.598659,0.0579556,-4.20715e-06,-3.12592e-08,1.47202e-11,27016.1,29.0471], Tmin=(200,'K'), Tmax=(990.88,'K')),
            NASAPolynomial(coeffs=[6.70237,0.0508885,-2.74269e-05,7.18323e-09,-7.36392e-13,24469.3,-11.6596], Tmin=(990.88,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "C8H9_18",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {3,D} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {2,D} {12,S}
4  C u0 p0 c0 {1,S} {6,D} {11,S}
5  C u1 p0 c0 {2,S} {6,S} {13,S}
6  C u0 p0 c0 {4,D} {5,S} {15,S}
7  C u0 p0 c0 {2,S} {8,D} {14,S}
8  C u0 p0 c0 {7,D} {16,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.693467,0.0598824,-8.93105e-06,-2.71198e-08,1.34885e-11,29823.9,30.0913], Tmin=(200,'K'), Tmax=(987.64,'K')),
            NASAPolynomial(coeffs=[6.989,0.0502243,-2.68497e-05,6.9719e-09,-7.08988e-13,27259.9,-12.1744], Tmin=(987.64,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "C8H9_19",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
2  C u1 p0 c0 {5,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {1,S} {6,D} {12,S}
5  C u0 p0 c0 {2,S} {3,D} {14,S}
6  C u0 p0 c0 {2,S} {4,D} {15,S}
7  C u0 p0 c0 {2,S} {8,D} {13,S}
8  C u0 p0 c0 {7,D} {16,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.609299,0.0583968,-5.60989e-06,-2.9883e-08,1.42907e-11,27142.7,29.2917], Tmin=(200,'K'), Tmax=(988.56,'K')),
            NASAPolynomial(coeffs=[6.67459,0.0507992,-2.72739e-05,7.11105e-09,-7.25702e-13,24633.7,-11.1712], Tmin=(988.56,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "C9H10_16",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,B} {5,B}
3  C u0 p0 c0 {1,S} {9,D} {12,S}
4  C u0 p0 c0 {2,B} {6,B} {13,S}
5  C u0 p0 c0 {2,B} {8,B} {17,S}
6  C u0 p0 c0 {4,B} {7,B} {14,S}
7  C u0 p0 c0 {6,B} {8,B} {15,S}
8  C u0 p0 c0 {5,B} {7,B} {16,S}
9  C u0 p0 c0 {3,D} {18,S} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.08886,0.0642475,-2.73258e-06,-3.65006e-08,1.68926e-11,13861.9,33.2125], Tmin=(200,'K'), Tmax=(987.1,'K')),
            NASAPolynomial(coeffs=[6.39964,0.0585424,-3.15063e-05,8.22075e-09,-8.38443e-13,11183.1,-8.89864], Tmin=(987.1,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "C9H10_466",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {5,B} {6,B}
5  C u0 p0 c0 {3,S} {4,B} {7,B}
6  C u0 p0 c0 {4,B} {9,B} {18,S}
7  C u0 p0 c0 {5,B} {8,B} {19,S}
8  C u0 p0 c0 {7,B} {9,B} {16,S}
9  C u0 p0 c0 {6,B} {8,B} {17,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.52086,0.0660481,7.60528e-06,-5.57799e-08,2.62385e-11,4786.6,41.7799], Tmin=(200,'K'), Tmax=(905.04,'K')),
            NASAPolynomial(coeffs=[2.92991,0.064815,-3.55602e-05,9.31832e-09,-9.42644e-13,2501.81,5.13046], Tmin=(905.04,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "C9H10_470",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {9,D}
3  C u0 p0 c0 {2,S} {4,B} {5,B}
4  C u0 p0 c0 {3,B} {6,B} {13,S}
5  C u0 p0 c0 {3,B} {8,B} {17,S}
6  C u0 p0 c0 {4,B} {7,B} {14,S}
7  C u0 p0 c0 {6,B} {8,B} {15,S}
8  C u0 p0 c0 {5,B} {7,B} {16,S}
9  C u0 p0 c0 {2,D} {18,S} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.24984,0.0673941,-1.04102e-05,-2.98026e-08,1.4896e-11,11537.5,32.3567], Tmin=(200,'K'), Tmax=(983.81,'K')),
            NASAPolynomial(coeffs=[6.98194,0.057233,-3.04547e-05,7.86134e-09,-7.94271e-13,8789.8,-12.9551], Tmin=(983.81,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "C9H10_471",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {5,B} {6,B}
3  C u0 p0 c0 {1,S} {4,D} {13,S}
4  C u0 p0 c0 {2,S} {3,D} {14,S}
5  C u0 p0 c0 {2,B} {7,B} {15,S}
6  C u0 p0 c0 {2,B} {9,B} {19,S}
7  C u0 p0 c0 {5,B} {8,B} {16,S}
8  C u0 p0 c0 {7,B} {9,B} {17,S}
9  C u0 p0 c0 {6,B} {8,B} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.18184,0.0672254,-1.13385e-05,-2.81915e-08,1.42564e-11,11478.2,33.1146], Tmin=(200,'K'), Tmax=(978.91,'K')),
            NASAPolynomial(coeffs=[6.41003,0.0580755,-3.08326e-05,7.90886e-09,-7.92132e-13,8943.9,-8.70263], Tmin=(978.91,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "C9H10_474",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {5,B} {7,B}
5  C u0 p0 c0 {2,S} {4,B} {6,B}
6  C u0 p0 c0 {5,B} {8,B} {16,S}
7  C u0 p0 c0 {4,B} {9,B} {19,S}
8  C u0 p0 c0 {6,B} {9,B} {17,S}
9  C u0 p0 c0 {7,B} {8,B} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.787654,0.0589607,9.45348e-06,-4.65261e-08,1.9704e-11,17290.8,30.2771], Tmin=(200,'K'), Tmax=(993.97,'K')),
            NASAPolynomial(coeffs=[5.16067,0.0612647,-3.36243e-05,8.92713e-09,-9.23765e-13,14812,-4.90504], Tmin=(993.97,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "C9H11_13",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {10,S}
2  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {2,S} {9,D}
4  C u0 p0 c0 {1,S} {6,D} {14,S}
5  C u0 p0 c0 {1,S} {7,D} {15,S}
6  C u0 p0 c0 {4,D} {8,S} {17,S}
7  C u0 p0 c0 {5,D} {8,S} {18,S}
8  C u1 p0 c0 {6,S} {7,S} {16,S}
9  C u0 p0 c0 {3,D} {19,S} {20,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.75769,0.0752336,-2.02894e-05,-2.34222e-08,1.32941e-11,26940.4,36.1833], Tmin=(200,'K'), Tmax=(982.94,'K')),
            NASAPolynomial(coeffs=[7.8994,0.0591422,-3.11489e-05,7.96351e-09,-7.97937e-13,23920.8,-15.9432], Tmin=(982.94,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "C9H11_14",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {10,S}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {1,S} {2,S} {7,S}
6  C u0 p0 c0 {2,S} {8,D} {17,S}
7  C u0 p0 c0 {5,S} {9,D} {20,S}
8  C u0 p0 c0 {6,D} {9,S} {18,S}
9  C u0 p0 c0 {7,D} {8,S} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.26005,0.0654436,3.58555e-06,-4.42641e-08,1.95173e-11,30666.3,33.5176], Tmin=(200,'K'), Tmax=(992.12,'K')),
            NASAPolynomial(coeffs=[6.10828,0.0631335,-3.43445e-05,9.05799e-09,-9.33078e-13,27855.9,-8.76735], Tmin=(992.12,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "C9H11_16",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {9,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {5,D} {16,S}
5  C u0 p0 c0 {4,D} {6,S} {19,S}
6  C u0 p0 c0 {5,S} {7,D} {18,S}
7  C u0 p0 c0 {6,D} {8,S} {17,S}
8  C u0 p0 c0 {7,S} {9,D} {20,S}
9  C u1 p0 c0 {3,S} {8,D}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.51784,0.0715283,-1.24005e-05,-2.97096e-08,1.50903e-11,69130.9,32.8486], Tmin=(200,'K'), Tmax=(979.57,'K')),
            NASAPolynomial(coeffs=[6.7029,0.0613226,-3.25483e-05,8.35021e-09,-8.36962e-13,66399.5,-12.3635], Tmin=(979.57,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "C9H11_17",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {5,B} {9,B}
5  C u0 p0 c0 {4,B} {6,B} {19,S}
6  C u0 p0 c0 {5,B} {7,B} {18,S}
7  C u0 p0 c0 {6,B} {8,B} {17,S}
8  C u0 p0 c0 {7,B} {9,B} {20,S}
9  C u1 p0 c0 {4,B} {8,B}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.28723,0.068617,-7.87338e-06,-3.24586e-08,1.57174e-11,29792.4,35.1831], Tmin=(200,'K'), Tmax=(974.33,'K')),
            NASAPolynomial(coeffs=[5.61222,0.062696,-3.32488e-05,8.50365e-09,-8.48265e-13,27384.5,-3.3806], Tmin=(974.33,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "C9H11_18",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {2,S} {6,D}
4  C u0 p0 c0 {2,S} {7,D} {15,S}
5  C u0 p0 c0 {1,S} {9,D} {14,S}
6  C u0 p0 c0 {3,D} {8,S} {17,S}
7  C u0 p0 c0 {4,D} {8,S} {18,S}
8  C u1 p0 c0 {6,S} {7,S} {16,S}
9  C u0 p0 c0 {5,D} {19,S} {20,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.58795,0.0725416,-1.44419e-05,-2.81561e-08,1.46601e-11,27496.6,35.6515], Tmin=(200,'K'), Tmax=(980.85,'K')),
            NASAPolynomial(coeffs=[7.0594,0.0607079,-3.21776e-05,8.25378e-09,-8.27775e-13,24673.2,-11.6453], Tmin=(980.85,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "C9H11_19",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
3  C u1 p0 c0 {1,S} {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,B} {6,B}
5  C u0 p0 c0 {4,B} {7,B} {16,S}
6  C u0 p0 c0 {4,B} {9,B} {20,S}
7  C u0 p0 c0 {5,B} {8,B} {17,S}
8  C u0 p0 c0 {7,B} {9,B} {18,S}
9  C u0 p0 c0 {6,B} {8,B} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.58943,0.07555,-2.54064e-05,-1.6122e-08,1.04206e-11,15409.6,35.5401], Tmin=(200,'K'), Tmax=(980.3,'K')),
            NASAPolynomial(coeffs=[6.73266,0.0606408,-3.17397e-05,8.00685e-09,-7.87926e-13,12862.7,-9.11173], Tmin=(980.3,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "C9H11_20",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,B} {5,B}
4  C u0 p0 c0 {3,B} {6,B} {14,S}
5  C u0 p0 c0 {3,B} {8,B} {18,S}
6  C u0 p0 c0 {4,B} {7,B} {15,S}
7  C u0 p0 c0 {6,B} {8,B} {16,S}
8  C u0 p0 c0 {5,B} {7,B} {17,S}
9  C u1 p0 c0 {2,S} {19,S} {20,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.70896,0.0758715,-2.37243e-05,-1.91861e-08,1.17294e-11,23030,36.6916], Tmin=(200,'K'), Tmax=(980.41,'K')),
            NASAPolynomial(coeffs=[7.4093,0.0597675,-3.13649e-05,7.95904e-09,-7.89565e-13,20228.1,-12.2894], Tmin=(980.41,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "C9H11_21",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {5,B} {6,B}
4  C u1 p0 c0 {1,S} {3,S} {15,S}
5  C u0 p0 c0 {3,B} {7,B} {16,S}
6  C u0 p0 c0 {3,B} {9,B} {20,S}
7  C u0 p0 c0 {5,B} {8,B} {17,S}
8  C u0 p0 c0 {7,B} {9,B} {18,S}
9  C u0 p0 c0 {6,B} {8,B} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.91694,0.0744489,-1.94193e-05,-2.35913e-08,1.33568e-11,16614.4,38.0177], Tmin=(200,'K'), Tmax=(959.82,'K')),
            NASAPolynomial(coeffs=[5.80862,0.0628669,-3.35342e-05,8.58812e-09,-8.52817e-13,14181.8,-3.88328], Tmin=(959.82,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "C9H11_22",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,B} {6,B}
4  C u1 p0 c0 {1,S} {2,S} {15,S}
5  C u0 p0 c0 {3,B} {7,B} {16,S}
6  C u0 p0 c0 {3,B} {9,B} {20,S}
7  C u0 p0 c0 {5,B} {8,B} {17,S}
8  C u0 p0 c0 {7,B} {9,B} {18,S}
9  C u0 p0 c0 {6,B} {8,B} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.59414,0.0749581,-2.29613e-05,-1.88725e-08,1.14033e-11,21835.1,37.4888], Tmin=(200,'K'), Tmax=(979.07,'K')),
            NASAPolynomial(coeffs=[6.72555,0.0609194,-3.202e-05,8.10915e-09,-8.00833e-13,19249.7,-7.35645], Tmin=(979.07,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "C9H11_23",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {4,B} {5,B}
4  C u0 p0 c0 {3,B} {6,B} {14,S}
5  C u0 p0 c0 {3,B} {8,B} {18,S}
6  C u0 p0 c0 {4,B} {7,B} {15,S}
7  C u0 p0 c0 {6,B} {8,B} {16,S}
8  C u0 p0 c0 {5,B} {7,B} {17,S}
9  C u1 p0 c0 {1,S} {19,S} {20,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.83487,0.0786364,-3.06917e-05,-1.27426e-08,9.65213e-12,22485.3,36.444], Tmin=(200,'K'), Tmax=(983.73,'K')),
            NASAPolynomial(coeffs=[7.93861,0.0587456,-3.06293e-05,7.72705e-09,-7.62707e-13,19601.9,-15.4288], Tmin=(983.73,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "C9H11_24",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {7,D} {16,S}
6  C u0 p0 c0 {1,S} {8,D} {17,S}
7  C u0 p0 c0 {5,D} {9,S} {19,S}
8  C u0 p0 c0 {6,D} {9,S} {20,S}
9  C u1 p0 c0 {7,S} {8,S} {18,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.67522,0.0726662,-1.30039e-05,-3.04921e-08,1.55713e-11,27213.2,35.269], Tmin=(200,'K'), Tmax=(987.4,'K')),
            NASAPolynomial(coeffs=[7.86272,0.059478,-3.16318e-05,8.18893e-09,-8.31556e-13,24089,-16.9076], Tmin=(987.4,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "C9H11_25",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {4,S} {7,D}
6  C u1 p0 c0 {1,S} {8,S} {17,S}
7  C u0 p0 c0 {5,D} {9,S} {20,S}
8  C u0 p0 c0 {6,S} {9,D} {18,S}
9  C u0 p0 c0 {7,S} {8,D} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.784997,0.057583,2.06439e-05,-5.75512e-08,2.30131e-11,20108.6,30.9122], Tmin=(200,'K'), Tmax=(1004.47,'K')),
            NASAPolynomial(coeffs=[4.08746,0.0674478,-3.77938e-05,1.02415e-08,-1.07921e-12,17653.3,0.0339788], Tmin=(1004.47,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "C9H12_1103",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
4  C u0 p0 c0 {8,S} {9,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {8,D} {18,S}
7  C u0 p0 c0 {1,S} {9,D} {21,S}
8  C u0 p0 c0 {4,S} {6,D} {19,S}
9  C u0 p0 c0 {4,S} {7,D} {20,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.49465,0.0699076,-1.95356e-06,-4.02327e-08,1.84931e-11,17635.3,34.2871], Tmin=(200,'K'), Tmax=(979.61,'K')),
            NASAPolynomial(coeffs=[5.81125,0.0657735,-3.49729e-05,9.01754e-09,-9.09904e-13,14970.9,-7.10258], Tmin=(979.61,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "C9H12_1104",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {8,D} {18,S}
7  C u0 p0 c0 {4,S} {9,D} {19,S}
8  C u0 p0 c0 {6,D} {9,S} {20,S}
9  C u0 p0 c0 {7,D} {8,S} {21,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.52053,0.0700758,-1.89491e-06,-4.05152e-08,1.86121e-11,17898,34.2905], Tmin=(200,'K'), Tmax=(981.3,'K')),
            NASAPolynomial(coeffs=[5.98109,0.0655925,-3.49302e-05,9.02671e-09,-9.131e-13,15169.3,-8.16072], Tmin=(981.3,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "C9H12_1105",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
5  C u0 p0 c0 {8,S} {9,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {8,D} {18,S}
7  C u0 p0 c0 {1,S} {9,D} {21,S}
8  C u0 p0 c0 {5,S} {6,D} {19,S}
9  C u0 p0 c0 {5,S} {7,D} {20,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.0585,0.0617149,1.74905e-05,-5.65196e-08,2.30836e-11,18075.7,31.174], Tmin=(200,'K'), Tmax=(994.7,'K')),
            NASAPolynomial(coeffs=[4.20475,0.0695978,-3.82017e-05,1.01653e-08,-1.05531e-12,15591.6,-1.41376], Tmin=(994.7,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "C9H12_1106",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {8,D} {18,S}
7  C u0 p0 c0 {5,S} {9,D} {19,S}
8  C u0 p0 c0 {6,D} {9,S} {20,S}
9  C u0 p0 c0 {7,D} {8,S} {21,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.08101,0.0618891,1.74378e-05,-5.66298e-08,2.31282e-11,17976.1,30.8423], Tmin=(200,'K'), Tmax=(996.53,'K')),
            NASAPolynomial(coeffs=[4.35456,0.0694637,-3.82065e-05,1.01935e-08,-1.0611e-12,15433.3,-2.68492], Tmin=(996.53,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "C9H7_1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {5,S} {8,B}
2  C u0 p0 c0 {1,B} {3,B} {12,S}
3  C u0 p0 c0 {2,B} {4,B} {11,S}
4  C u0 p0 c0 {3,B} {6,B} {10,S}
5  C u0 p0 c0 {1,S} {9,D} {13,S}
6  C u0 p0 c0 {4,B} {8,B} {14,S}
7  C u0 p0 c0 {9,D} {15,S} {16,S}
8  C u1 p0 c0 {1,B} {6,B}
9  C u0 p0 c0 {5,D} {7,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.10702,0.0678071,-3.18337e-05,-6.76635e-09,7.23217e-12,63592.3,32.254], Tmin=(200,'K'), Tmax=(996.4,'K')),
            NASAPolynomial(coeffs=[9.4283,0.0438404,-2.3343e-05,6.01192e-09,-6.05353e-13,60583.1,-23.1001], Tmin=(996.4,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "C9H7_2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {8,S}
4  C u0 p0 c0 {2,B} {7,B} {15,S}
5  C u0 p0 c0 {3,B} {6,B} {12,S}
6  C u0 p0 c0 {5,B} {7,B} {13,S}
7  C u0 p0 c0 {4,B} {6,B} {14,S}
8  C u0 p0 c0 {3,S} {9,D} {16,S}
9  C u1 p0 c0 {1,S} {8,D}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.232249,0.0510722,8.14255e-06,-4.11398e-08,1.73417e-11,50275,26.9249], Tmin=(200,'K'), Tmax=(1014.9,'K')),
            NASAPolynomial(coeffs=[6.30654,0.0507688,-2.90498e-05,8.01626e-09,-8.57481e-13,47636.1,-11.1796], Tmin=(1014.9,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "C9H7_3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,B} {7,B}
3  C u0 p0 c0 {2,B} {4,B} {14,S}
4  C u0 p0 c0 {3,B} {5,B} {13,S}
5  C u0 p0 c0 {4,B} {6,B} {12,S}
6  C u0 p0 c0 {5,B} {7,B} {15,S}
7  C u1 p0 c0 {2,B} {6,B}
8  C u0 p0 c0 {1,S} {9,T}
9  C u0 p0 c0 {8,T} {16,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.17787,0.069647,-3.7059e-05,-1.71515e-09,5.58079e-12,65959.5,33.4024], Tmin=(200,'K'), Tmax=(998.95,'K')),
            NASAPolynomial(coeffs=[9.74148,0.0429954,-2.26741e-05,5.79225e-09,-5.79366e-13,62926.2,-23.5291], Tmin=(998.95,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "C9H8_118",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {10,S}
3  C u0 p0 c0 {1,B} {6,B} {14,S}
4  C u0 p0 c0 {2,B} {5,B} {11,S}
5  C u0 p0 c0 {4,B} {6,B} {12,S}
6  C u0 p0 c0 {3,B} {5,B} {13,S}
7  C u0 p0 c0 {1,S} {9,D} {15,S}
8  C u0 p0 c0 {9,D} {16,S} {17,S}
9  C u0 p0 c0 {7,D} {8,D}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.0779,0.0658915,-2.02695e-05,-1.85453e-08,1.11041e-11,32316.9,31.5074], Tmin=(200,'K'), Tmax=(990.79,'K')),
            NASAPolynomial(coeffs=[8.41516,0.0486112,-2.59687e-05,6.72718e-09,-6.82006e-13,29402.8,-19.4161], Tmin=(990.79,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "C9H8_119",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {5,D} {6,S}
3  C u0 p0 c0 {1,S} {7,D} {11,S}
4  C u0 p0 c0 {1,S} {8,D} {12,S}
5  C u0 p0 c0 {2,D} {8,S} {16,S}
6  C u0 p0 c0 {2,S} {9,D} {17,S}
7  C u0 p0 c0 {3,D} {9,S} {14,S}
8  C u0 p0 c0 {4,D} {5,S} {15,S}
9  C u0 p0 c0 {6,D} {7,S} {13,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.450644,0.0534923,1.04618e-05,-4.50646e-08,1.87697e-11,33949.1,27.6896], Tmin=(200,'K'), Tmax=(1016.75,'K')),
            NASAPolynomial(coeffs=[6.28147,0.0543287,-3.10785e-05,8.60075e-09,-9.23792e-13,31167.9,-11.8456], Tmin=(1016.75,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "C9H8_120",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,B} {5,B}
3  C u0 p0 c0 {2,B} {6,S} {7,B}
4  C u0 p0 c0 {1,S} {6,D} {12,S}
5  C u0 p0 c0 {2,B} {9,B} {15,S}
6  C u0 p0 c0 {3,S} {4,D} {16,S}
7  C u0 p0 c0 {3,B} {8,B} {17,S}
8  C u0 p0 c0 {7,B} {9,B} {13,S}
9  C u0 p0 c0 {5,B} {8,B} {14,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.230094,0.050486,1.5661e-05,-4.84147e-08,1.95199e-11,16892.7,26.1245], Tmin=(200,'K'), Tmax=(1016.89,'K')),
            NASAPolynomial(coeffs=[5.16687,0.0560979,-3.22099e-05,8.92578e-09,-9.58453e-13,14407.2,-6.82681], Tmin=(1016.89,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "C9H8_21",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {12,S}
4  C u0 p0 c0 {2,B} {7,B} {16,S}
5  C u0 p0 c0 {3,B} {6,B} {13,S}
6  C u0 p0 c0 {5,B} {7,B} {14,S}
7  C u0 p0 c0 {4,B} {6,B} {15,S}
8  C u0 p0 c0 {1,S} {9,T}
9  C u0 p0 c0 {8,T} {17,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.15653,0.0676422,-2.50431e-05,-1.41057e-08,9.70706e-12,34551.3,33.1768], Tmin=(200,'K'), Tmax=(990.55,'K')),
            NASAPolynomial(coeffs=[8.74763,0.0477169,-2.52613e-05,6.49541e-09,-6.54688e-13,31604.6,-19.4809], Tmin=(990.55,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "C9H8_7",
    molecule = 
"""
1  C u0 p0 c0 {8,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {3,B} {4,B} {9,S}
3  C u0 p0 c0 {2,B} {5,B} {13,S}
4  C u0 p0 c0 {2,B} {7,B} {17,S}
5  C u0 p0 c0 {3,B} {6,B} {14,S}
6  C u0 p0 c0 {5,B} {7,B} {15,S}
7  C u0 p0 c0 {4,B} {6,B} {16,S}
8  C u0 p0 c0 {1,S} {9,T}
9  C u0 p0 c0 {2,S} {8,T}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.02533,0.0692007,-3.35804e-05,-3.34318e-09,5.62539e-12,30740.4,33.5562], Tmin=(200,'K'), Tmax=(995.92,'K')),
            NASAPolynomial(coeffs=[7.77421,0.0488771,-2.55905e-05,6.45017e-09,-6.339e-13,28242.8,-12.5999], Tmin=(995.92,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "C9H9_10",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {4,B} {6,B}
4  C u0 p0 c0 {2,S} {3,B} {7,B}
5  C u1 p0 c0 {1,S} {2,S} {14,S}
6  C u0 p0 c0 {3,B} {8,B} {15,S}
7  C u0 p0 c0 {4,B} {9,B} {18,S}
8  C u0 p0 c0 {6,B} {9,B} {16,S}
9  C u0 p0 c0 {7,B} {8,B} {17,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.69658,0.0574274,7.87875e-06,-4.43938e-08,1.8916e-11,27288.9,29.3237], Tmin=(200,'K'), Tmax=(1002.76,'K')),
            NASAPolynomial(coeffs=[5.9406,0.0575592,-3.21201e-05,8.66035e-09,-9.08324e-13,24620.1,-9.38539], Tmin=(1002.76,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "C9H9_11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,B} {6,B}
4  C u0 p0 c0 {2,S} {3,B} {5,B}
5  C u0 p0 c0 {4,B} {7,B} {13,S}
6  C u0 p0 c0 {3,B} {8,B} {16,S}
7  C u0 p0 c0 {5,B} {8,B} {14,S}
8  C u0 p0 c0 {6,B} {7,B} {15,S}
9  C u1 p0 c0 {1,S} {17,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.27684,0.0673392,-1.43846e-05,-2.62594e-08,1.38338e-11,42274.1,32.7145], Tmin=(200,'K'), Tmax=(993.19,'K')),
            NASAPolynomial(coeffs=[8.32188,0.0526441,-2.83818e-05,7.42879e-09,-7.60818e-13,39185.5,-19.4782], Tmin=(993.19,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "C9H9_12",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {4,B} {5,B}
3  C u0 p0 c0 {1,S} {2,S} {9,D}
4  C u0 p0 c0 {2,B} {6,B} {13,S}
5  C u0 p0 c0 {2,B} {8,B} {17,S}
6  C u0 p0 c0 {4,B} {7,B} {14,S}
7  C u0 p0 c0 {6,B} {8,B} {15,S}
8  C u0 p0 c0 {5,B} {7,B} {16,S}
9  C u1 p0 c0 {3,D} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.4006,0.0713771,-2.64829e-05,-1.43231e-08,9.94953e-12,42223.7,33.9298], Tmin=(200,'K'), Tmax=(987.73,'K')),
            NASAPolynomial(coeffs=[8.48113,0.0516238,-2.72597e-05,6.97283e-09,-6.98032e-13,39283.1,-18.6258], Tmin=(987.73,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "C9H9_13",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {7,D} {14,S}
5  C u0 p0 c0 {2,S} {8,D} {15,S}
6  C u0 p0 c0 {3,S} {9,D} {16,S}
7  C u0 p0 c0 {4,D} {8,S} {17,S}
8  C u0 p0 c0 {5,D} {7,S} {18,S}
9  C u1 p0 c0 {2,S} {6,D}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.562545,0.0550415,1.32335e-05,-4.86058e-08,2.00049e-11,57059.8,29.6685], Tmin=(200,'K'), Tmax=(1009.68,'K')),
            NASAPolynomial(coeffs=[5.43836,0.058794,-3.32345e-05,9.07648e-09,-9.62844e-13,54444.9,-6.28833], Tmin=(1009.68,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "C9H9_14",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {1,S} {3,D} {13,S}
5  C u0 p0 c0 {1,S} {7,D} {14,S}
6  C u0 p0 c0 {1,S} {8,D} {15,S}
7  C u0 p0 c0 {5,D} {9,S} {17,S}
8  C u0 p0 c0 {6,D} {9,S} {18,S}
9  C u1 p0 c0 {7,S} {8,S} {16,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.7256,0.0771046,-3.90075e-05,-3.74337e-09,6.74001e-12,51892.5,34.9068], Tmin=(200,'K'), Tmax=(994.83,'K')),
            NASAPolynomial(coeffs=[9.85039,0.0494758,-2.58699e-05,6.56544e-09,-6.53581e-13,48653.2,-25.5852], Tmin=(994.83,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "C9H9_15",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {11,S}
3  C u1 p0 c0 {2,S} {7,S} {12,S}
4  C u0 p0 c0 {1,S} {7,D} {13,S}
5  C u0 p0 c0 {1,S} {8,D} {14,S}
6  C u0 p0 c0 {2,S} {9,D} {15,S}
7  C u0 p0 c0 {3,S} {4,D} {16,S}
8  C u0 p0 c0 {5,D} {9,S} {17,S}
9  C u0 p0 c0 {6,D} {8,S} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.786798,0.0579556,8.54464e-06,-4.57867e-08,1.94015e-11,43360.3,30.2276], Tmin=(200,'K'), Tmax=(1012.21,'K')),
            NASAPolynomial(coeffs=[6.61019,0.0571333,-3.23361e-05,8.86638e-09,-9.45393e-13,40407.6,-12.7373], Tmin=(1012.21,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "C9H9_16",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {8,D} {15,S}
5  C u0 p0 c0 {2,S} {7,D} {14,S}
6  C u0 p0 c0 {2,S} {9,D} {16,S}
7  C u0 p0 c0 {5,D} {8,S} {17,S}
8  C u0 p0 c0 {4,D} {7,S} {18,S}
9  C u1 p0 c0 {3,S} {6,D}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.577744,0.0552941,1.26869e-05,-4.81891e-08,1.99e-11,56964.4,29.7602], Tmin=(200,'K'), Tmax=(1009.08,'K')),
            NASAPolynomial(coeffs=[5.50363,0.0586443,-3.31081e-05,9.03138e-09,-9.57112e-13,54339.2,-6.5604], Tmin=(1009.08,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "C9H9_17",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {8,D}
3  C u0 p0 c0 {2,S} {4,B} {9,B}
4  C u0 p0 c0 {3,B} {5,B} {15,S}
5  C u0 p0 c0 {4,B} {6,B} {14,S}
6  C u0 p0 c0 {5,B} {7,B} {13,S}
7  C u0 p0 c0 {6,B} {9,B} {16,S}
8  C u0 p0 c0 {2,D} {17,S} {18,S}
9  C u1 p0 c0 {3,B} {7,B}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.29622,0.0695737,-2.25038e-05,-1.76544e-08,1.09453e-11,42705.9,33.3023], Tmin=(200,'K'), Tmax=(986.15,'K')),
            NASAPolynomial(coeffs=[8.02378,0.0524022,-2.77678e-05,7.12024e-09,-7.13899e-13,39864.5,-16.6179], Tmin=(986.15,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "C9H9_18",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {12,S}
4  C u0 p0 c0 {2,B} {7,B} {16,S}
5  C u0 p0 c0 {3,B} {6,B} {13,S}
6  C u0 p0 c0 {5,B} {7,B} {14,S}
7  C u0 p0 c0 {4,B} {6,B} {15,S}
8  C u0 p0 c0 {9,D} {17,S} {18,S}
9  C u1 p0 c0 {1,S} {8,D}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.27269,0.0688717,-2.03282e-05,-1.98089e-08,1.16503e-11,41672.9,34.4007], Tmin=(200,'K'), Tmax=(986.38,'K')),
            NASAPolynomial(coeffs=[7.93195,0.0527548,-2.80732e-05,7.22547e-09,-7.26756e-13,38825.2,-15.1103], Tmin=(986.38,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "C9H9_19",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,B} {9,B}
3  C u0 p0 c0 {1,S} {8,D} {12,S}
4  C u0 p0 c0 {2,B} {5,B} {15,S}
5  C u0 p0 c0 {4,B} {6,B} {14,S}
6  C u0 p0 c0 {5,B} {7,B} {13,S}
7  C u0 p0 c0 {6,B} {9,B} {16,S}
8  C u0 p0 c0 {3,D} {17,S} {18,S}
9  C u1 p0 c0 {2,B} {7,B}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.12573,0.0658982,-1.31893e-05,-2.61488e-08,1.36043e-11,45920.6,34.6304], Tmin=(200,'K'), Tmax=(987.17,'K')),
            NASAPolynomial(coeffs=[7.45079,0.0536495,-2.87712e-05,7.46644e-09,-7.56906e-13,43130.8,-12.1892], Tmin=(987.17,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "C9H9_20",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {4,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {8,S}
3  C u0 p0 c0 {2,B} {5,B} {10,S}
4  C u0 p0 c0 {1,B} {6,B} {13,S}
5  C u0 p0 c0 {3,B} {6,B} {11,S}
6  C u0 p0 c0 {4,B} {5,B} {12,S}
7  C u0 p0 c0 {1,S} {9,D} {14,S}
8  C u1 p0 c0 {2,S} {15,S} {16,S}
9  C u0 p0 c0 {7,D} {17,S} {18,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.5183,0.0720422,-2.60652e-05,-1.59268e-08,1.06939e-11,30957.5,32.9304], Tmin=(200,'K'), Tmax=(991.86,'K')),
            NASAPolynomial(coeffs=[9.29559,0.0504489,-2.67065e-05,6.88454e-09,-6.96714e-13,27729.3,-24.6114], Tmin=(991.86,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "C9H9_21",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {7,D}
4  C u0 p0 c0 {1,S} {8,D} {13,S}
5  C u0 p0 c0 {2,S} {6,D} {14,S}
6  C u0 p0 c0 {3,S} {5,D} {17,S}
7  C u0 p0 c0 {3,D} {9,S} {18,S}
8  C u0 p0 c0 {4,D} {9,S} {16,S}
9  C u1 p0 c0 {7,S} {8,S} {15,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.622151,0.0555978,1.28456e-05,-4.86887e-08,2.00751e-11,31216.4,29.3096], Tmin=(200,'K'), Tmax=(1013.51,'K')),
            NASAPolynomial(coeffs=[5.80965,0.0584752,-3.32405e-05,9.13915e-09,-9.75812e-13,28461.1,-8.96723], Tmin=(1013.51,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "C9H9_22",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {9,D}
4  C u0 p0 c0 {1,S} {6,D} {12,S}
5  C u0 p0 c0 {1,S} {7,D} {13,S}
6  C u0 p0 c0 {4,D} {8,S} {15,S}
7  C u0 p0 c0 {5,D} {8,S} {16,S}
8  C u1 p0 c0 {6,S} {7,S} {14,S}
9  C u0 p0 c0 {3,D} {17,S} {18,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.59814,0.072294,-2.4639e-05,-1.82412e-08,1.15913e-11,47603.1,33.9318], Tmin=(200,'K'), Tmax=(996.03,'K')),
            NASAPolynomial(coeffs=[9.83987,0.0499991,-2.66635e-05,6.9418e-09,-7.10242e-13,44152,-27.0909], Tmin=(996.03,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "C9H9_23",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {8,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {3,B} {4,B} {9,S}
3  C u0 p0 c0 {2,B} {5,B} {14,S}
4  C u0 p0 c0 {2,B} {7,B} {18,S}
5  C u0 p0 c0 {3,B} {6,B} {15,S}
6  C u0 p0 c0 {5,B} {7,B} {16,S}
7  C u0 p0 c0 {4,B} {6,B} {17,S}
8  C u0 p0 c0 {1,S} {9,D} {13,S}
9  C u1 p0 c0 {2,S} {8,D}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.39618,0.073016,-3.23402e-05,-7.79227e-09,7.60648e-12,37713.4,34.5892], Tmin=(200,'K'), Tmax=(989.85,'K')),
            NASAPolynomial(coeffs=[8.22562,0.0518942,-2.72458e-05,6.90266e-09,-6.82888e-13,34938.5,-16.1273], Tmin=(989.85,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "C9H9_24",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {5,D} {11,S}
3  C u0 p0 c0 {1,S} {6,D} {12,S}
4  C u0 p0 c0 {1,S} {9,D} {14,S}
5  C u0 p0 c0 {2,D} {7,S} {15,S}
6  C u0 p0 c0 {3,D} {7,S} {16,S}
7  C u1 p0 c0 {5,S} {6,S} {13,S}
8  C u0 p0 c0 {9,D} {17,S} {18,S}
9  C u0 p0 c0 {4,D} {8,D}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.60158,0.0738717,-3.03801e-05,-1.20257e-08,9.46179e-12,48915.5,35.5632], Tmin=(200,'K'), Tmax=(991.82,'K')),
            NASAPolynomial(coeffs=[9.48573,0.0502348,-2.65101e-05,6.79988e-09,-6.84294e-13,45679.4,-23.0621], Tmin=(991.82,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "C9H9_25",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,B} {4,B}
2  C u0 p0 c0 {1,S} {8,S} {9,D}
3  C u0 p0 c0 {1,B} {5,B} {10,S}
4  C u0 p0 c0 {1,B} {7,B} {14,S}
5  C u0 p0 c0 {3,B} {6,B} {11,S}
6  C u0 p0 c0 {5,B} {7,B} {12,S}
7  C u0 p0 c0 {4,B} {6,B} {13,S}
8  C u1 p0 c0 {2,S} {15,S} {16,S}
9  C u0 p0 c0 {2,D} {17,S} {18,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.49031,0.0705869,-2.13308e-05,-2.07764e-08,1.22972e-11,30278.9,32.9045], Tmin=(200,'K'), Tmax=(995.47,'K')),
            NASAPolynomial(coeffs=[9.42223,0.0505419,-2.69953e-05,7.03851e-09,-7.2091e-13,26926.9,-25.6166], Tmin=(995.47,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "C9H9_4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {9,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {3,B} {4,B} {8,S}
3  C u0 p0 c0 {2,B} {5,B} {13,S}
4  C u0 p0 c0 {2,B} {7,B} {17,S}
5  C u0 p0 c0 {3,B} {6,B} {14,S}
6  C u0 p0 c0 {5,B} {7,B} {15,S}
7  C u0 p0 c0 {4,B} {6,B} {16,S}
8  C u0 p0 c0 {2,S} {9,D} {18,S}
9  C u1 p0 c0 {1,S} {8,D}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.23719,0.0702209,-2.59308e-05,-1.32869e-08,9.2817e-12,40793,33.5956], Tmin=(200,'K'), Tmax=(985.38,'K')),
            NASAPolynomial(coeffs=[7.4444,0.0533519,-2.82195e-05,7.18336e-09,-7.12447e-13,38190.2,-12.6862], Tmin=(985.38,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "C9H9_5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,B} {6,B}
4  C u0 p0 c0 {3,B} {5,S} {7,B}
5  C u1 p0 c0 {2,S} {4,S} {14,S}
6  C u0 p0 c0 {3,B} {8,B} {15,S}
7  C u0 p0 c0 {4,B} {9,B} {18,S}
8  C u0 p0 c0 {6,B} {9,B} {16,S}
9  C u0 p0 c0 {7,B} {8,B} {17,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.569498,0.055227,1.25412e-05,-4.79683e-08,1.9826e-11,22591.6,29.1462], Tmin=(200,'K'), Tmax=(1008.61,'K')),
            NASAPolynomial(coeffs=[5.50214,0.0584863,-3.29637e-05,8.9832e-09,-9.51464e-13,19976.3,-7.09142], Tmin=(1008.61,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "C9H9_6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {10,S}
2  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
3  C u1 p0 c0 {1,S} {2,S} {7,S}
4  C u0 p0 c0 {1,S} {6,D} {14,S}
5  C u0 p0 c0 {1,S} {8,D} {13,S}
6  C u0 p0 c0 {2,S} {4,D} {15,S}
7  C u0 p0 c0 {3,S} {9,D} {18,S}
8  C u0 p0 c0 {5,D} {9,S} {17,S}
9  C u0 p0 c0 {7,D} {8,S} {16,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.695655,0.0567991,1.03954e-05,-4.68964e-08,1.96427e-11,35270.3,29.7548], Tmin=(200,'K'), Tmax=(1010.71,'K')),
            NASAPolynomial(coeffs=[6.11832,0.0578366,-3.27064e-05,8.94819e-09,-9.51528e-13,32462.6,-10.2674], Tmin=(1010.71,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "C9H9_7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {13,S}
4  C u0 p0 c0 {2,B} {7,B} {17,S}
5  C u0 p0 c0 {3,B} {6,B} {14,S}
6  C u0 p0 c0 {5,B} {7,B} {15,S}
7  C u0 p0 c0 {4,B} {6,B} {16,S}
8  C u0 p0 c0 {1,S} {9,D} {12,S}
9  C u1 p0 c0 {8,D} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.27588,0.0680548,-1.72687e-05,-2.31352e-08,1.2786e-11,43721.6,34.2188], Tmin=(200,'K'), Tmax=(989.64,'K')),
            NASAPolynomial(coeffs=[8.151,0.0525888,-2.81366e-05,7.2985e-09,-7.40633e-13,40747.3,-16.7627], Tmin=(989.64,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "C9H9_8",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,D} {13,S}
4  C u0 p0 c0 {1,S} {6,D} {14,S}
5  C u0 p0 c0 {3,D} {7,S} {16,S}
6  C u0 p0 c0 {4,D} {7,S} {17,S}
7  C u1 p0 c0 {5,S} {6,S} {15,S}
8  C u0 p0 c0 {2,S} {9,T}
9  C u0 p0 c0 {8,T} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.65276,0.0752559,-3.44521e-05,-8.05629e-09,8.16707e-12,48928.5,35.2114], Tmin=(200,'K'), Tmax=(992.39,'K')),
            NASAPolynomial(coeffs=[9.70006,0.049565,-2.59543e-05,6.61288e-09,-6.61862e-13,45687,-24.4517], Tmin=(992.39,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "C9H9_9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,B} {4,B}
2  C u0 p0 c0 {1,S} {8,D} {11,S}
3  C u0 p0 c0 {1,B} {5,B} {12,S}
4  C u0 p0 c0 {1,B} {7,B} {16,S}
5  C u0 p0 c0 {3,B} {6,B} {13,S}
6  C u0 p0 c0 {5,B} {7,B} {14,S}
7  C u0 p0 c0 {4,B} {6,B} {15,S}
8  C u0 p0 c0 {2,D} {9,S} {10,S}
9  C u1 p0 c0 {8,S} {17,S} {18,S}
10 H u0 p0 c0 {8,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.28034,0.0676308,-1.57305e-05,-2.48386e-08,1.33708e-11,27403.9,32.7956], Tmin=(200,'K'), Tmax=(992.21,'K')),
            NASAPolynomial(coeffs=[8.36223,0.0522663,-2.80427e-05,7.31329e-09,-7.46933e-13,24333.2,-19.4803], Tmin=(992.21,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "C10H10_44",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {2,S} {6,D}
4  C u0 p0 c0 {1,S} {5,B} {7,B}
5  C u0 p0 c0 {4,B} {6,S} {8,B}
6  C u0 p0 c0 {3,D} {5,S} {16,S}
7  C u0 p0 c0 {4,B} {10,B} {20,S}
8  C u0 p0 c0 {5,B} {9,B} {17,S}
9  C u0 p0 c0 {8,B} {10,B} {18,S}
10 C u0 p0 c0 {7,B} {9,B} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.47588,0.0688522,-2.47004e-06,-3.99105e-08,1.8381e-11,11899.7,32.5418], Tmin=(200,'K'), Tmax=(990.2,'K')),
            NASAPolynomial(coeffs=[6.72699,0.062739,-3.41451e-05,8.97549e-09,-9.19672e-13,8950.35,-13.6411], Tmin=(990.2,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "C10H10_45",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {7,D}
4  C u0 p0 c0 {1,S} {9,D} {14,S}
5  C u0 p0 c0 {2,S} {8,D} {15,S}
6  C u0 p0 c0 {3,S} {10,D} {18,S}
7  C u0 p0 c0 {3,D} {9,S} {19,S}
8  C u0 p0 c0 {5,D} {10,S} {16,S}
9  C u0 p0 c0 {4,D} {7,S} {20,S}
10 C u0 p0 c0 {6,D} {8,S} {17,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.32602,0.0653787,6.75241e-06,-4.81247e-08,2.07687e-11,30474.6,32.5757], Tmin=(200,'K'), Tmax=(1001.34,'K')),
            NASAPolynomial(coeffs=[6.4243,0.0640135,-3.55352e-05,9.54509e-09,-9.98509e-13,27438.8,-12.2341], Tmin=(1001.34,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "C10H10_46",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {5,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,B} {7,B}
4  C u0 p0 c0 {2,S} {3,B} {8,B}
5  C u0 p0 c0 {2,S} {6,D} {15,S}
6  C u0 p0 c0 {1,S} {5,D} {16,S}
7  C u0 p0 c0 {3,B} {9,B} {17,S}
8  C u0 p0 c0 {4,B} {10,B} {20,S}
9  C u0 p0 c0 {7,B} {10,B} {18,S}
10 C u0 p0 c0 {8,B} {9,B} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.09148,0.0621053,1.27412e-05,-5.2237e-08,2.17725e-11,14020.4,31.8545], Tmin=(200,'K'), Tmax=(1000.44,'K')),
            NASAPolynomial(coeffs=[5.25289,0.0659141,-3.67132e-05,9.86784e-09,-1.03118e-12,11290.9,-6.05321], Tmin=(1000.44,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "C10H10_47",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
2  C u0 p0 c0 {7,S} {8,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {5,D} {9,S}
4  C u0 p0 c0 {3,S} {6,D} {10,S}
5  C u0 p0 c0 {1,S} {3,D} {16,S}
6  C u0 p0 c0 {1,S} {4,D} {17,S}
7  C u0 p0 c0 {2,S} {9,D} {15,S}
8  C u0 p0 c0 {2,S} {10,D} {18,S}
9  C u0 p0 c0 {3,S} {7,D} {19,S}
10 C u0 p0 c0 {4,S} {8,D} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.41475,0.0674329,1.35743e-06,-4.33528e-08,1.9399e-11,30224.4,31.6342], Tmin=(200,'K'), Tmax=(994.05,'K')),
            NASAPolynomial(coeffs=[6.57936,0.0632935,-3.46905e-05,9.18781e-09,-9.48363e-13,27250.3,-13.8504], Tmin=(994.05,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "C10H10_48",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,D}
3  C u0 p0 c0 {1,S} {6,D} {12,S}
4  C u0 p0 c0 {2,S} {7,D} {16,S}
5  C u0 p0 c0 {1,S} {10,D} {13,S}
6  C u0 p0 c0 {3,D} {7,S} {14,S}
7  C u0 p0 c0 {4,D} {6,S} {15,S}
8  C u0 p0 c0 {2,D} {17,S} {18,S}
9  C u0 p0 c0 {10,D} {19,S} {20,S}
10 C u0 p0 c0 {5,D} {9,D}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.40607,0.0873196,-4.6981e-05,-4.25156e-10,6.17607e-12,46428,38.7439], Tmin=(200,'K'), Tmax=(996.85,'K')),
            NASAPolynomial(coeffs=[10.3731,0.0556943,-2.89653e-05,7.30331e-09,-7.21976e-13,42903.8,-27.7656], Tmin=(996.85,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    label = "C10H10_49",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {5,B} {7,B}
4  C u0 p0 c0 {2,S} {5,S} {6,D}
5  C u0 p0 c0 {3,B} {4,S} {8,B}
6  C u0 p0 c0 {1,S} {4,D} {16,S}
7  C u0 p0 c0 {3,B} {9,B} {17,S}
8  C u0 p0 c0 {5,B} {10,B} {20,S}
9  C u0 p0 c0 {7,B} {10,B} {18,S}
10 C u0 p0 c0 {8,B} {9,B} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.46361,0.0685417,-1.66973e-06,-4.06329e-08,1.85965e-11,11644.4,32.3395], Tmin=(200,'K'), Tmax=(991.17,'K')),
            NASAPolynomial(coeffs=[6.7225,0.0627734,-3.42061e-05,9.0067e-09,-9.24559e-13,8682.25,-13.8379], Tmin=(991.17,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "C10H10_50",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,S} {7,D}
4  C u0 p0 c0 {2,S} {3,S} {8,D}
5  C u0 p0 c0 {1,S} {9,D} {15,S}
6  C u0 p0 c0 {2,S} {10,D} {16,S}
7  C u0 p0 c0 {3,D} {10,S} {18,S}
8  C u0 p0 c0 {4,D} {9,S} {20,S}
9  C u0 p0 c0 {5,D} {8,S} {17,S}
10 C u0 p0 c0 {6,D} {7,S} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.868362,0.0589476,1.63157e-05,-5.40034e-08,2.20423e-11,28611.8,30.3432], Tmin=(200,'K'), Tmax=(1003.21,'K')),
            NASAPolynomial(coeffs=[4.75659,0.065431,-3.66065e-05,9.89195e-09,-1.03919e-12,26028.3,-4.06294], Tmin=(1003.21,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    label = "C10H10_51",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {7,D} {15,S}
6  C u0 p0 c0 {2,S} {9,D} {16,S}
7  C u0 p0 c0 {4,S} {5,D} {20,S}
8  C u0 p0 c0 {4,S} {10,D} {19,S}
9  C u0 p0 c0 {6,D} {10,S} {17,S}
10 C u0 p0 c0 {8,D} {9,S} {18,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.4448,0.0675088,1.92479e-06,-4.41869e-08,1.96856e-11,29143.5,32.0093], Tmin=(200,'K'), Tmax=(997.41,'K')),
            NASAPolynomial(coeffs=[6.82775,0.0631131,-3.47472e-05,9.25433e-09,-9.60642e-13,26061.7,-15.056], Tmin=(997.41,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "C10H10_52",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {7,S} {11,S} {12,S}
2  C u0 p0 c0 {6,S} {8,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {5,D} {9,S}
4  C u0 p0 c0 {3,S} {6,D} {10,S}
5  C u0 p0 c0 {1,S} {3,D} {16,S}
6  C u0 p0 c0 {2,S} {4,D} {18,S}
7  C u0 p0 c0 {1,S} {9,D} {15,S}
8  C u0 p0 c0 {2,S} {10,D} {17,S}
9  C u0 p0 c0 {3,S} {7,D} {19,S}
10 C u0 p0 c0 {4,S} {8,D} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.741,0.0716023,-5.44834e-06,-3.91004e-08,1.84095e-11,30475.7,34.7514], Tmin=(200,'K'), Tmax=(1000.22,'K')),
            NASAPolynomial(coeffs=[8.26864,0.0609316,-3.34749e-05,8.92615e-09,-9.29467e-13,27004.7,-20.8829], Tmin=(1000.22,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    label = "C10H10_53",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {6,B} {14,S}
4  C u0 p0 c0 {2,B} {8,B} {18,S}
5  C u0 p0 c0 {1,S} {10,D} {13,S}
6  C u0 p0 c0 {3,B} {7,B} {15,S}
7  C u0 p0 c0 {6,B} {8,B} {16,S}
8  C u0 p0 c0 {4,B} {7,B} {17,S}
9  C u0 p0 c0 {10,D} {19,S} {20,S}
10 C u0 p0 c0 {5,D} {9,D}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.03639,0.0799433,-2.93407e-05,-1.62205e-08,1.11606e-11,30814.7,38.2408], Tmin=(200,'K'), Tmax=(986.89,'K')),
            NASAPolynomial(coeffs=[8.78088,0.0585474,-3.09396e-05,7.90785e-09,-7.9021e-13,27586.4,-19.342], Tmin=(986.89,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    label = "C10H10_54",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {5,S} {6,S} {11,S}
2  C u0 p0 c0 {3,S} {4,S} {12,S} {13,S}
3  C u1 p0 c0 {1,S} {2,S} {7,S}
4  C u0 p0 c0 {2,S} {5,D} {10,S}
5  C u0 p0 c0 {1,S} {4,D} {14,S}
6  C u0 p0 c0 {1,S} {8,D} {15,S}
7  C u0 p0 c0 {3,S} {9,D} {18,S}
8  C u0 p0 c0 {6,D} {9,S} {16,S}
9  C u0 p0 c0 {7,D} {8,S} {17,S}
10 C u1 p0 c0 {4,S} {19,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.08872,0.0769967,-1.59721e-05,-3.11606e-08,1.62686e-11,47735.8,36.1928], Tmin=(200,'K'), Tmax=(999.55,'K')),
            NASAPolynomial(coeffs=[9.65003,0.0588926,-3.21311e-05,8.5147e-09,-8.8239e-13,43946.8,-27.6493], Tmin=(999.55,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
    label = "C10H10_55",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,B} {7,B}
4  C u0 p0 c0 {3,B} {6,S} {8,B}
5  C u0 p0 c0 {1,S} {6,D} {15,S}
6  C u0 p0 c0 {4,S} {5,D} {16,S}
7  C u0 p0 c0 {3,B} {10,B} {20,S}
8  C u0 p0 c0 {4,B} {9,B} {17,S}
9  C u0 p0 c0 {8,B} {10,B} {18,S}
10 C u0 p0 c0 {7,B} {9,B} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.3964,0.0668441,2.92325e-06,-4.48108e-08,1.98333e-11,13239.6,32.7389], Tmin=(200,'K'), Tmax=(997.09,'K')),
            NASAPolynomial(coeffs=[6.66222,0.0632119,-3.47825e-05,9.26363e-09,-9.61775e-13,10206.1,-13.2691], Tmin=(997.09,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
    label = "C10H10_56",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {7,D}
4  C u0 p0 c0 {1,S} {8,D} {15,S}
5  C u0 p0 c0 {2,S} {6,D} {14,S}
6  C u0 p0 c0 {3,S} {5,D} {19,S}
7  C u0 p0 c0 {3,D} {10,S} {18,S}
8  C u0 p0 c0 {4,D} {9,S} {20,S}
9  C u0 p0 c0 {8,S} {10,D} {16,S}
10 C u0 p0 c0 {7,S} {9,D} {17,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.29627,0.0648405,7.9735e-06,-4.90895e-08,2.10211e-11,29196.3,32.3678], Tmin=(200,'K'), Tmax=(1002.59,'K')),
            NASAPolynomial(coeffs=[6.30666,0.0642926,-3.5769e-05,9.62802e-09,-1.00903e-12,26174.8,-11.7972], Tmin=(1002.59,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 128,
    label = "C10H10_57",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  C u0 p0 c0 {1,S} {5,B} {6,B}
5  C u0 p0 c0 {2,S} {4,B} {7,B}
6  C u0 p0 c0 {4,B} {8,B} {15,S}
7  C u0 p0 c0 {5,B} {9,B} {18,S}
8  C u0 p0 c0 {6,B} {9,B} {16,S}
9  C u0 p0 c0 {7,B} {8,B} {17,S}
10 C u0 p0 c0 {3,D} {19,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.855428,0.0584441,1.79004e-05,-5.54675e-08,2.24469e-11,15638.4,28.3474], Tmin=(200,'K'), Tmax=(1007.64,'K')),
            NASAPolynomial(coeffs=[4.80769,0.0656409,-3.69915e-05,1.00785e-08,-1.0671e-12,12990.4,-6.49306], Tmin=(1007.64,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
    label = "C10H10_58",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
2  C u0 p0 c0 {5,S} {7,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,S} {8,D}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {2,S} {4,D} {17,S}
6  C u0 p0 c0 {1,S} {10,D} {15,S}
7  C u0 p0 c0 {2,S} {9,D} {16,S}
8  C u0 p0 c0 {3,D} {10,S} {19,S}
9  C u0 p0 c0 {4,S} {7,D} {20,S}
10 C u0 p0 c0 {6,D} {8,S} {18,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.71431,0.0712133,-4.70683e-06,-3.96388e-08,1.85493e-11,30099.7,34.462], Tmin=(200,'K'), Tmax=(1000.13,'K')),
            NASAPolynomial(coeffs=[8.14321,0.0611351,-3.36055e-05,8.9632e-09,-9.33322e-13,26660.2,-20.4338], Tmin=(1000.13,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 130,
    label = "C10H10_59",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,B} {5,B}
4  C u0 p0 c0 {3,B} {6,B} {15,S}
5  C u0 p0 c0 {3,B} {8,B} {19,S}
6  C u0 p0 c0 {4,B} {7,B} {16,S}
7  C u0 p0 c0 {6,B} {8,B} {17,S}
8  C u0 p0 c0 {5,B} {7,B} {18,S}
9  C u0 p0 c0 {2,S} {10,T}
10 C u0 p0 c0 {9,T} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.09326,0.081662,-3.45007e-05,-1.10996e-08,9.46058e-12,30848.8,37.6566], Tmin=(200,'K'), Tmax=(988.22,'K')),
            NASAPolynomial(coeffs=[9.02527,0.0577766,-3.03014e-05,7.6928e-09,-7.64293e-13,27620,-21.0696], Tmin=(988.22,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 131,
    label = "C10H10_60",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {4,S} {6,S} {11,S}
2  C u0 p0 c0 {3,S} {5,S} {12,S} {13,S}
3  C u1 p0 c0 {1,S} {2,S} {7,S}
4  C u0 p0 c0 {1,S} {5,D} {10,S}
5  C u0 p0 c0 {2,S} {4,D} {14,S}
6  C u0 p0 c0 {1,S} {8,D} {15,S}
7  C u0 p0 c0 {3,S} {9,D} {16,S}
8  C u0 p0 c0 {6,D} {9,S} {18,S}
9  C u0 p0 c0 {7,D} {8,S} {17,S}
10 C u1 p0 c0 {4,S} {19,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.08292,0.0769424,-1.59185e-05,-3.11693e-08,1.62658e-11,47627.9,36.1967], Tmin=(200,'K'), Tmax=(999.3,'K')),
            NASAPolynomial(coeffs=[9.61474,0.0589367,-3.21481e-05,8.51626e-09,-8.82214e-13,43851.2,-27.4289], Tmin=(999.3,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 132,
    label = "C10H10_61",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {7,S} {12,S}
4  C u0 p0 c0 {2,S} {8,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {10,D} {15,S}
6  C u0 p0 c0 {1,S} {9,D} {16,S}
7  C u0 p0 c0 {3,S} {8,D} {17,S}
8  C u0 p0 c0 {4,S} {7,D} {18,S}
9  C u0 p0 c0 {6,D} {10,S} {19,S}
10 C u0 p0 c0 {5,D} {9,S} {20,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.44806,0.0659209,8.2989e-06,-5.06475e-08,2.16116e-11,36946.2,33.9542], Tmin=(200,'K'), Tmax=(1014.45,'K')),
            NASAPolynomial(coeffs=[7.38122,0.0634769,-3.59508e-05,9.88685e-09,-1.05812e-12,33489.2,-16.9781], Tmin=(1014.45,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 133,
    label = "C10H10_62",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {11,S}
2  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {4,D} {8,S}
4  C u0 p0 c0 {2,S} {3,D} {17,S}
5  C u0 p0 c0 {1,S} {10,D} {14,S}
6  C u0 p0 c0 {1,S} {9,D} {15,S}
7  C u0 p0 c0 {2,S} {8,D} {16,S}
8  C u0 p0 c0 {3,S} {7,D} {20,S}
9  C u0 p0 c0 {6,D} {10,S} {18,S}
10 C u0 p0 c0 {5,D} {9,S} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.66192,0.0697839,-6.46574e-07,-4.33717e-08,1.96484e-11,33144.9,35.1918], Tmin=(200,'K'), Tmax=(1005.86,'K')),
            NASAPolynomial(coeffs=[8.12954,0.0615653,-3.42009e-05,9.23006e-09,-9.71925e-13,29621.2,-19.8283], Tmin=(1005.86,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 134,
    label = "C10H10_63",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {11,S}
2  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {2,S} {7,D}
4  C u0 p0 c0 {1,S} {9,D} {15,S}
5  C u0 p0 c0 {1,S} {10,D} {16,S}
6  C u0 p0 c0 {2,S} {8,D} {14,S}
7  C u0 p0 c0 {3,D} {8,S} {18,S}
8  C u0 p0 c0 {6,D} {7,S} {17,S}
9  C u0 p0 c0 {4,D} {10,S} {19,S}
10 C u0 p0 c0 {5,D} {9,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.65744,0.0697921,-8.0475e-07,-4.31777e-08,1.95863e-11,33415.2,35.4846], Tmin=(200,'K'), Tmax=(1005.16,'K')),
            NASAPolynomial(coeffs=[8.08414,0.0615926,-3.41835e-05,9.21436e-09,-9.69096e-13,29912.7,-19.2441], Tmin=(1005.16,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "C10H10_64",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,B} {4,B}
2  C u0 p0 c0 {1,S} {5,D} {13,S}
3  C u0 p0 c0 {1,B} {6,B} {14,S}
4  C u0 p0 c0 {1,B} {8,B} {18,S}
5  C u0 p0 c0 {2,D} {9,S} {12,S}
6  C u0 p0 c0 {3,B} {7,B} {15,S}
7  C u0 p0 c0 {6,B} {8,B} {16,S}
8  C u0 p0 c0 {4,B} {7,B} {17,S}
9  C u0 p0 c0 {5,S} {10,D} {11,S}
10 C u0 p0 c0 {9,D} {19,S} {20,S}
11 H u0 p0 c0 {9,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.93058,0.0776172,-2.35851e-05,-2.14909e-08,1.28339e-11,22170.5,36.72], Tmin=(200,'K'), Tmax=(986.26,'K')),
            NASAPolynomial(coeffs=[8.43011,0.0591939,-3.14534e-05,8.08637e-09,-8.12479e-13,18979.2,-18.9392], Tmin=(986.26,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "C10H10_65",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {8,D} {13,S}
4  C u0 p0 c0 {1,S} {7,D} {14,S}
5  C u0 p0 c0 {2,S} {9,D} {15,S}
6  C u0 p0 c0 {2,S} {10,D} {16,S}
7  C u0 p0 c0 {4,D} {8,S} {17,S}
8  C u0 p0 c0 {3,D} {7,S} {18,S}
9  C u0 p0 c0 {5,D} {10,S} {19,S}
10 C u0 p0 c0 {6,D} {9,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.59306,0.0683546,2.92561e-06,-4.64319e-08,2.05043e-11,34771.3,34.6538], Tmin=(200,'K'), Tmax=(1010.19,'K')),
            NASAPolynomial(coeffs=[7.96849,0.0621355,-3.48226e-05,9.48545e-09,-1.00724e-12,31225,-19.5631], Tmin=(1010.19,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "C10H10_66",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {11,S}
2  C u0 p0 c0 {6,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {8,S} {9,D}
4  C u0 p0 c0 {1,S} {6,D} {15,S}
5  C u0 p0 c0 {1,S} {10,D} {14,S}
6  C u0 p0 c0 {2,S} {4,D} {16,S}
7  C u0 p0 c0 {2,S} {8,D} {17,S}
8  C u0 p0 c0 {3,S} {7,D} {19,S}
9  C u0 p0 c0 {3,D} {10,S} {20,S}
10 C u0 p0 c0 {5,D} {9,S} {18,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.46046,0.067324,3.06557e-06,-4.54831e-08,2.00972e-11,32950.6,32.8812], Tmin=(200,'K'), Tmax=(1001.36,'K')),
            NASAPolynomial(coeffs=[7.05108,0.0629849,-3.48653e-05,9.35003e-09,-9.77466e-13,29758.9,-15.6189], Tmin=(1001.36,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "C10H10_67",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {8,D}
4  C u0 p0 c0 {1,S} {6,D} {14,S}
5  C u0 p0 c0 {3,S} {7,D} {17,S}
6  C u0 p0 c0 {4,D} {7,S} {15,S}
7  C u0 p0 c0 {5,D} {6,S} {16,S}
8  C u0 p0 c0 {3,D} {18,S} {19,S}
9  C u0 p0 c0 {2,S} {10,T}
10 C u0 p0 c0 {9,T} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.44985,0.0886179,-5.08571e-05,3.4218e-09,4.89107e-12,46293,38.2699], Tmin=(200,'K'), Tmax=(1000.08,'K')),
            NASAPolynomial(coeffs=[10.6299,0.0549753,-2.84036e-05,7.12351e-09,-7.01325e-13,42743.1,-29.5018], Tmin=(1000.08,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "C10H10_68",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {7,S} {13,S} {14,S}
2  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,S} {5,D}
4  C u0 p0 c0 {3,S} {6,D} {8,S}
5  C u0 p0 c0 {2,S} {3,D} {16,S}
6  C u0 p0 c0 {2,S} {4,D} {15,S}
7  C u0 p0 c0 {1,S} {9,D} {17,S}
8  C u0 p0 c0 {4,S} {10,D} {20,S}
9  C u0 p0 c0 {7,D} {10,S} {18,S}
10 C u0 p0 c0 {8,D} {9,S} {19,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.46243,0.0678699,9.78357e-07,-4.33622e-08,1.94497e-11,30069.5,32.3231], Tmin=(200,'K'), Tmax=(996.55,'K')),
            NASAPolynomial(coeffs=[6.89669,0.0628965,-3.45527e-05,9.18478e-09,-9.51929e-13,26984.3,-15.096], Tmin=(996.55,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    label = "C10H10_69",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,S} {7,D}
4  C u0 p0 c0 {2,S} {3,S} {8,D}
5  C u0 p0 c0 {1,S} {9,D} {15,S}
6  C u0 p0 c0 {2,S} {10,D} {16,S}
7  C u0 p0 c0 {3,D} {9,S} {18,S}
8  C u0 p0 c0 {4,D} {10,S} {19,S}
9  C u0 p0 c0 {5,D} {7,S} {17,S}
10 C u0 p0 c0 {6,D} {8,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.69466,0.0709408,-4.21186e-06,-3.99874e-08,1.86387e-11,29599.8,33.6313], Tmin=(200,'K'), Tmax=(999.94,'K')),
            NASAPolynomial(coeffs=[8.04864,0.0612805,-3.36955e-05,8.98766e-09,-9.35733e-13,26185.6,-20.7022], Tmin=(999.94,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "C10H10_70",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {7,S} {13,S} {14,S}
2  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,S} {9,D}
4  C u0 p0 c0 {3,S} {5,D} {8,S}
5  C u0 p0 c0 {2,S} {4,D} {16,S}
6  C u0 p0 c0 {2,S} {10,D} {15,S}
7  C u0 p0 c0 {1,S} {8,D} {17,S}
8  C u0 p0 c0 {4,S} {7,D} {19,S}
9  C u0 p0 c0 {3,D} {10,S} {20,S}
10 C u0 p0 c0 {6,D} {9,S} {18,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.845347,0.0587413,1.64701e-05,-5.39989e-08,2.20311e-11,32127,29.3161], Tmin=(200,'K'), Tmax=(1001.61,'K')),
            NASAPolynomial(coeffs=[4.62176,0.0655435,-3.6601e-05,9.86863e-09,-1.03453e-12,29595.5,-4.23868], Tmin=(1001.61,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 142,
    label = "C10H10_71",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
2  C u0 p0 c0 {5,S} {7,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {9,S} {10,S}
5  C u0 p0 c0 {2,S} {9,D} {15,S}
6  C u0 p0 c0 {1,S} {10,D} {16,S}
7  C u0 p0 c0 {2,S} {8,D} {17,S}
8  C u0 p0 c0 {3,S} {7,D} {20,S}
9  C u0 p0 c0 {4,S} {5,D} {18,S}
10 C u0 p0 c0 {4,S} {6,D} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.906102,0.0595773,1.50892e-05,-5.31488e-08,2.18499e-11,31358.3,29.5296], Tmin=(200,'K'), Tmax=(1001.64,'K')),
            NASAPolynomial(coeffs=[4.91356,0.0651387,-3.63708e-05,9.80876e-09,-1.02867e-12,28747.6,-5.7688], Tmin=(1001.64,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 143,
    label = "C10H10_72",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {7,D}
4  C u0 p0 c0 {1,S} {9,D} {15,S}
5  C u0 p0 c0 {2,S} {8,D} {14,S}
6  C u0 p0 c0 {3,S} {10,D} {19,S}
7  C u0 p0 c0 {3,D} {8,S} {20,S}
8  C u0 p0 c0 {5,D} {7,S} {16,S}
9  C u0 p0 c0 {4,D} {10,S} {17,S}
10 C u0 p0 c0 {6,D} {9,S} {18,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.25994,0.0643608,8.85731e-06,-4.97026e-08,2.11759e-11,27869.9,31.9102], Tmin=(200,'K'), Tmax=(1002.05,'K')),
            NASAPolynomial(coeffs=[6.10969,0.0646239,-3.59672e-05,9.67891e-09,-1.01377e-12,24902.8,-11.0947], Tmin=(1002.05,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 144,
    label = "C10H10_73",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {5,B} {6,B}
4  C u0 p0 c0 {1,S} {5,S} {10,D}
5  C u0 p0 c0 {3,B} {4,S} {7,B}
6  C u0 p0 c0 {3,B} {8,B} {15,S}
7  C u0 p0 c0 {5,B} {9,B} {18,S}
8  C u0 p0 c0 {6,B} {9,B} {16,S}
9  C u0 p0 c0 {7,B} {8,B} {17,S}
10 C u0 p0 c0 {4,D} {19,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.831694,0.0581082,1.8342e-05,-5.56733e-08,2.24707e-11,14265.2,29.2674], Tmin=(200,'K'), Tmax=(1008.01,'K')),
            NASAPolynomial(coeffs=[4.72437,0.0656813,-3.70055e-05,1.00836e-08,-1.06792e-12,11640.2,-5.04622], Tmin=(1008.01,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 145,
    label = "C10H10_74",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {4,S}
2  C u0 p0 c0 {1,D} {6,S} {14,S}
3  C u0 p0 c0 {1,S} {7,D} {15,S}
4  C u0 p0 c0 {1,S} {8,D} {18,S}
5  C u0 p0 c0 {6,D} {9,S} {12,S}
6  C u0 p0 c0 {2,S} {5,D} {13,S}
7  C u0 p0 c0 {3,D} {8,S} {16,S}
8  C u0 p0 c0 {4,D} {7,S} {17,S}
9  C u0 p0 c0 {5,S} {10,D} {11,S}
10 C u0 p0 c0 {9,D} {19,S} {20,S}
11 H u0 p0 c0 {9,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.25984,0.0840313,-3.8625e-05,-8.20251e-09,8.68807e-12,37017.9,37.7048], Tmin=(200,'K'), Tmax=(991.88,'K')),
            NASAPolynomial(coeffs=[9.73339,0.0569752,-2.99345e-05,7.61622e-09,-7.5827e-13,33590.5,-25.3419], Tmin=(991.88,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 146,
    label = "C10H10_75",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,B} {6,B}
4  C u0 p0 c0 {3,B} {7,S} {8,B}
5  C u0 p0 c0 {2,S} {7,D} {15,S}
6  C u0 p0 c0 {3,B} {10,B} {18,S}
7  C u0 p0 c0 {4,S} {5,D} {19,S}
8  C u0 p0 c0 {4,B} {9,B} {20,S}
9  C u0 p0 c0 {8,B} {10,B} {16,S}
10 C u0 p0 c0 {6,B} {9,B} {17,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.05869,0.0613721,1.45438e-05,-5.374e-08,2.21702e-11,12451.4,30.393], Tmin=(200,'K'), Tmax=(1003.89,'K')),
            NASAPolynomial(coeffs=[5.19856,0.0661674,-3.70397e-05,1.00134e-08,-1.05227e-12,9697.15,-7.27969], Tmin=(1003.89,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 147,
    label = "C10H11_10",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {3,S} {8,D}
5  C u1 p0 c0 {1,S} {9,S} {16,S}
6  C u0 p0 c0 {2,S} {9,D} {17,S}
7  C u0 p0 c0 {3,S} {10,D} {18,S}
8  C u0 p0 c0 {4,D} {10,S} {20,S}
9  C u0 p0 c0 {5,S} {6,D} {19,S}
10 C u0 p0 c0 {7,D} {8,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.98069,0.0745497,-4.35306e-06,-4.20163e-08,1.95793e-11,36581.4,37.8127], Tmin=(200,'K'), Tmax=(999.28,'K')),
            NASAPolynomial(coeffs=[8.19845,0.0645036,-3.53564e-05,9.41209e-09,-9.7889e-13,33014.3,-18.9578], Tmin=(999.28,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "C10H11_11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u1 p0 c0 {1,S} {5,S} {12,S}
3  C u0 p0 c0 {1,S} {6,D} {13,S}
4  C u0 p0 c0 {1,S} {7,D} {14,S}
5  C u0 p0 c0 {2,S} {8,D} {17,S}
6  C u0 p0 c0 {3,D} {7,S} {18,S}
7  C u0 p0 c0 {4,D} {6,S} {19,S}
8  C u0 p0 c0 {5,D} {9,S} {16,S}
9  C u0 p0 c0 {8,S} {10,D} {15,S}
10 C u0 p0 c0 {9,D} {20,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.63056,0.0883811,-3.92215e-05,-1.0607e-08,9.91336e-12,41342.5,41.2427], Tmin=(200,'K'), Tmax=(991.55,'K')),
            NASAPolynomial(coeffs=[10.2907,0.0597311,-3.13941e-05,8.00813e-09,-8.00501e-13,37626.1,-26.8046], Tmin=(991.55,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 149,
    label = "C10H11_12",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {12,S}
3  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {3,S} {15,S}
5  C u0 p0 c0 {1,S} {8,D} {17,S}
6  C u0 p0 c0 {2,S} {9,D} {18,S}
7  C u0 p0 c0 {2,S} {10,D} {19,S}
8  C u0 p0 c0 {3,S} {5,D} {16,S}
9  C u0 p0 c0 {6,D} {10,S} {20,S}
10 C u0 p0 c0 {7,D} {9,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.0581,0.0757187,-6.5817e-06,-4.03972e-08,1.91609e-11,44604,38.2453], Tmin=(200,'K'), Tmax=(999.12,'K')),
            NASAPolynomial(coeffs=[8.53409,0.0639903,-3.5031e-05,9.31777e-09,-9.68639e-13,40956.3,-20.5093], Tmin=(999.12,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 150,
    label = "C10H11_13",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {9,D} {17,S}
5  C u1 p0 c0 {2,S} {8,S} {15,S}
6  C u0 p0 c0 {2,S} {10,D} {18,S}
7  C u0 p0 c0 {3,S} {8,D} {16,S}
8  C u0 p0 c0 {5,S} {7,D} {19,S}
9  C u0 p0 c0 {4,D} {10,S} {20,S}
10 C u0 p0 c0 {6,D} {9,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.65127,0.0695688,5.56197e-06,-4.93888e-08,2.15086e-11,34216,34.7548], Tmin=(200,'K'), Tmax=(1000.35,'K')),
            NASAPolynomial(coeffs=[6.69784,0.0670982,-3.70887e-05,9.92785e-09,-1.0359e-12,30998.8,-13.259], Tmin=(1000.35,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 151,
    label = "C10H11_14",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {7,S} {8,D}
5  C u0 p0 c0 {1,S} {7,D} {17,S}
6  C u1 p0 c0 {2,S} {9,S} {16,S}
7  C u0 p0 c0 {4,S} {5,D} {18,S}
8  C u0 p0 c0 {4,D} {10,S} {19,S}
9  C u0 p0 c0 {6,S} {10,D} {21,S}
10 C u0 p0 c0 {8,S} {9,D} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.80992,0.07238,-9.10395e-07,-4.41177e-08,2.0059e-11,27405.3,35.7684], Tmin=(200,'K'), Tmax=(996.18,'K')),
            NASAPolynomial(coeffs=[7.33423,0.0656482,-3.59238e-05,9.52899e-09,-9.86711e-13,24095.6,-15.7796], Tmin=(996.18,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 152,
    label = "C10H11_15",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {4,B} {5,B}
3  C u0 p0 c0 {1,S} {10,D} {12,S}
4  C u0 p0 c0 {2,B} {6,B} {13,S}
5  C u0 p0 c0 {2,B} {8,B} {17,S}
6  C u0 p0 c0 {4,B} {7,B} {14,S}
7  C u0 p0 c0 {6,B} {8,B} {15,S}
8  C u0 p0 c0 {5,B} {7,B} {16,S}
9  C u1 p0 c0 {1,S} {18,S} {19,S}
10 C u0 p0 c0 {3,D} {20,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.61503,0.0904535,-4.71273e-05,-1.69118e-09,6.70359e-12,35539.6,40.6702], Tmin=(200,'K'), Tmax=(996.08,'K')),
            NASAPolynomial(coeffs=[10.0518,0.059692,-3.10799e-05,7.83228e-09,-7.72528e-13,32018.8,-25.3969], Tmin=(996.08,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 153,
    label = "C10H11_16",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {5,D}
3  C u1 p0 c0 {1,S} {6,S} {13,S}
4  C u0 p0 c0 {2,S} {7,D} {16,S}
5  C u0 p0 c0 {2,D} {8,S} {17,S}
6  C u0 p0 c0 {3,S} {8,D} {19,S}
7  C u0 p0 c0 {4,D} {9,S} {15,S}
8  C u0 p0 c0 {5,S} {6,D} {18,S}
9  C u0 p0 c0 {7,S} {10,D} {14,S}
10 C u0 p0 c0 {9,D} {20,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.38633,0.0850823,-3.32238e-05,-1.47802e-08,1.09794e-11,32535.8,38.4784], Tmin=(200,'K'), Tmax=(987.27,'K')),
            NASAPolynomial(coeffs=[9.06559,0.0616429,-3.24937e-05,8.28163e-09,-8.25097e-13,29155.6,-22.2904], Tmin=(987.27,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 154,
    label = "C10H11_17",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {11,S}
2  C u0 p0 c0 {5,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {5,B} {8,B}
5  C u0 p0 c0 {2,S} {4,B} {7,B}
6  C u1 p0 c0 {1,S} {2,S} {17,S}
7  C u0 p0 c0 {5,B} {9,B} {18,S}
8  C u0 p0 c0 {4,B} {10,B} {21,S}
9  C u0 p0 c0 {7,B} {10,B} {19,S}
10 C u0 p0 c0 {8,B} {9,B} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.87214,0.0746409,-7.79834e-06,-3.74497e-08,1.79934e-11,23443.1,35.7906], Tmin=(200,'K'), Tmax=(987.23,'K')),
            NASAPolynomial(coeffs=[7.19384,0.0653033,-3.52354e-05,9.18706e-09,-9.34651e-13,20318,-14.5924], Tmin=(987.23,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 155,
    label = "C10H11_18",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {6,S} {8,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,D} {9,S}
5  C u1 p0 c0 {1,S} {10,S} {16,S}
6  C u0 p0 c0 {3,S} {4,D} {19,S}
7  C u0 p0 c0 {2,S} {10,D} {17,S}
8  C u0 p0 c0 {3,S} {9,D} {18,S}
9  C u0 p0 c0 {4,S} {8,D} {21,S}
10 C u0 p0 c0 {5,S} {7,D} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.99011,0.0746275,-4.42963e-06,-4.19909e-08,1.95731e-11,36360.8,37.7865], Tmin=(200,'K'), Tmax=(999.88,'K')),
            NASAPolynomial(coeffs=[8.25633,0.0644298,-3.53256e-05,9.40865e-09,-9.79127e-13,32772.4,-19.3427], Tmin=(999.88,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 156,
    label = "C10H11_19",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {7,D} {8,S}
5  C u0 p0 c0 {1,S} {9,D} {17,S}
6  C u1 p0 c0 {2,S} {10,S} {16,S}
7  C u0 p0 c0 {4,D} {9,S} {19,S}
8  C u0 p0 c0 {4,S} {10,D} {20,S}
9  C u0 p0 c0 {5,D} {7,S} {18,S}
10 C u0 p0 c0 {6,S} {8,D} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.89922,0.0736621,-3.42782e-06,-4.22592e-08,1.95672e-11,27776.2,35.8866], Tmin=(200,'K'), Tmax=(996.81,'K')),
            NASAPolynomial(coeffs=[7.7774,0.0648838,-3.54406e-05,9.39565e-09,-9.73172e-13,24354,-18.2556], Tmin=(996.81,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 157,
    label = "C10H11_20",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {7,S} {8,D}
5  C u0 p0 c0 {2,S} {6,D} {16,S}
6  C u0 p0 c0 {3,S} {5,D} {17,S}
7  C u1 p0 c0 {4,S} {9,S} {18,S}
8  C u0 p0 c0 {4,D} {10,S} {21,S}
9  C u0 p0 c0 {7,S} {10,D} {19,S}
10 C u0 p0 c0 {8,S} {9,D} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.98764,0.0749039,-5.79394e-06,-4.05426e-08,1.91156e-11,35164.9,38.5543], Tmin=(200,'K'), Tmax=(997.69,'K')),
            NASAPolynomial(coeffs=[8.21202,0.064173,-3.5008e-05,9.28004e-09,-9.61774e-13,31628.5,-18.1528], Tmin=(997.69,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 158,
    label = "C10H11_21",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {5,B} {7,B}
5  C u0 p0 c0 {4,B} {6,S} {8,B}
6  C u1 p0 c0 {1,S} {5,S} {17,S}
7  C u0 p0 c0 {4,B} {10,B} {21,S}
8  C u0 p0 c0 {5,B} {9,B} {18,S}
9  C u0 p0 c0 {8,B} {10,B} {19,S}
10 C u0 p0 c0 {7,B} {9,B} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.75047,0.0720839,-1.55834e-06,-4.29357e-08,1.96263e-11,18765.3,35.7793], Tmin=(200,'K'), Tmax=(991.52,'K')),
            NASAPolynomial(coeffs=[6.91289,0.0659485,-3.58674e-05,9.44171e-09,-9.69975e-13,15630.9,-13.0851], Tmin=(991.52,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 159,
    label = "C10H11_22",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {13,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {14,S}
4  C u0 p0 c0 {2,S} {3,S} {8,S} {12,S}
5  C u0 p0 c0 {1,S} {9,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {9,D} {20,S}
7  C u1 p0 c0 {2,S} {10,S} {17,S}
8  C u0 p0 c0 {4,S} {10,D} {18,S}
9  C u0 p0 c0 {5,S} {6,D} {19,S}
10 C u0 p0 c0 {7,S} {8,D} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.1445,0.0937218,-2.77578e-05,-3.44758e-08,2.12821e-11,40455.9,61.2428], Tmin=(200,'K'), Tmax=(912.71,'K')),
            NASAPolynomial(coeffs=[5.41576,0.0693973,-3.82715e-05,1.0083e-08,-1.02467e-12,36883.6,-5.21589], Tmin=(912.71,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 160,
    label = "C10H11_23",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {6,S} {13,S}
4  C u1 p0 c0 {2,S} {7,S} {14,S}
5  C u0 p0 c0 {1,S} {8,D} {15,S}
6  C u0 p0 c0 {3,S} {7,D} {16,S}
7  C u0 p0 c0 {4,S} {6,D} {19,S}
8  C u0 p0 c0 {5,D} {9,S} {18,S}
9  C u0 p0 c0 {8,S} {10,D} {17,S}
10 C u0 p0 c0 {9,D} {20,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.55373,0.0850138,-2.88916e-05,-2.11605e-08,1.34659e-11,47174.7,41.2411], Tmin=(200,'K'), Tmax=(993.41,'K')),
            NASAPolynomial(coeffs=[10.4098,0.0598893,-3.18348e-05,8.24873e-09,-8.39155e-13,43263.2,-27.9387], Tmin=(993.41,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 161,
    label = "C10H11_24",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {7,S} {8,D}
5  C u1 p0 c0 {3,S} {9,S} {16,S}
6  C u0 p0 c0 {2,S} {7,D} {17,S}
7  C u0 p0 c0 {4,S} {6,D} {21,S}
8  C u0 p0 c0 {4,D} {10,S} {20,S}
9  C u0 p0 c0 {5,S} {10,D} {18,S}
10 C u0 p0 c0 {8,S} {9,D} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.55205,0.0682444,7.82377e-06,-5.08965e-08,2.18791e-11,28390.5,34.3129], Tmin=(200,'K'), Tmax=(999.21,'K')),
            NASAPolynomial(coeffs=[6.22507,0.0677644,-3.74718e-05,1.00262e-08,-1.04514e-12,25306.1,-10.8583], Tmin=(999.21,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 162,
    label = "C10H11_25",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {3,S} {8,D}
5  C u1 p0 c0 {1,S} {9,S} {16,S}
6  C u0 p0 c0 {2,S} {7,D} {18,S}
7  C u0 p0 c0 {3,S} {6,D} {17,S}
8  C u0 p0 c0 {4,D} {10,S} {21,S}
9  C u0 p0 c0 {5,S} {10,D} {19,S}
10 C u0 p0 c0 {8,S} {9,D} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.53486,0.0679918,8.37416e-06,-5.13226e-08,2.19945e-11,28515.6,34.1528], Tmin=(200,'K'), Tmax=(999.16,'K')),
            NASAPolynomial(coeffs=[6.13433,0.0679506,-3.75945e-05,1.00614e-08,-1.04894e-12,25452.5,-10.4991], Tmin=(999.16,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 163,
    label = "C10H11_26",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
2  C u0 p0 c0 {4,S} {5,B} {6,B}
3  C u0 p0 c0 {1,S} {7,D} {14,S}
4  C u1 p0 c0 {2,S} {7,S} {15,S}
5  C u0 p0 c0 {2,B} {8,B} {17,S}
6  C u0 p0 c0 {2,B} {10,B} {21,S}
7  C u0 p0 c0 {3,D} {4,S} {16,S}
8  C u0 p0 c0 {5,B} {9,B} {18,S}
9  C u0 p0 c0 {8,B} {10,B} {19,S}
10 C u0 p0 c0 {6,B} {9,B} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.24445,0.0837458,-3.20037e-05,-1.47114e-08,1.07188e-11,23065.5,38.2487], Tmin=(200,'K'), Tmax=(985.53,'K')),
            NASAPolynomial(coeffs=[8.34697,0.0625597,-3.29403e-05,8.36843e-09,-8.29773e-13,19919.1,-18.0659], Tmin=(985.53,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 164,
    label = "C10H11_27",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u1 p0 c0 {1,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {5,D} {13,S}
4  C u0 p0 c0 {1,S} {7,D} {14,S}
5  C u0 p0 c0 {3,D} {9,S} {16,S}
6  C u0 p0 c0 {2,S} {8,D} {17,S}
7  C u0 p0 c0 {4,D} {8,S} {19,S}
8  C u0 p0 c0 {6,D} {7,S} {18,S}
9  C u0 p0 c0 {5,S} {10,D} {15,S}
10 C u0 p0 c0 {9,D} {20,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.42875,0.0852834,-3.30778e-05,-1.53678e-08,1.12669e-11,38761.8,40.1754], Tmin=(200,'K'), Tmax=(987.94,'K')),
            NASAPolynomial(coeffs=[9.37463,0.0610967,-3.2192e-05,8.21765e-09,-8.21065e-13,35277.7,-22.4555], Tmin=(987.94,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 165,
    label = "C10H11_28",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {3,D} {5,S} {6,S}
3  C u0 p0 c0 {1,S} {2,D} {14,S}
4  C u1 p0 c0 {1,S} {9,S} {13,S}
5  C u0 p0 c0 {2,S} {7,D} {16,S}
6  C u0 p0 c0 {2,S} {8,D} {19,S}
7  C u0 p0 c0 {5,D} {8,S} {17,S}
8  C u0 p0 c0 {6,D} {7,S} {18,S}
9  C u0 p0 c0 {4,S} {10,D} {15,S}
10 C u0 p0 c0 {9,D} {20,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.66428,0.0900492,-4.45364e-05,-5.07353e-09,8.01239e-12,43799.8,41.5768], Tmin=(200,'K'), Tmax=(993.4,'K')),
            NASAPolynomial(coeffs=[10.353,0.0593558,-3.09899e-05,7.84705e-09,-7.78691e-13,40141.7,-26.5327], Tmin=(993.4,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 166,
    label = "C10H11_29",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {7,S} {12,S}
4  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {8,S} {15,S} {16,S}
6  C u0 p0 c0 {2,S} {8,D} {20,S}
7  C u1 p0 c0 {3,S} {10,S} {17,S}
8  C u0 p0 c0 {5,S} {6,D} {19,S}
9  C u0 p0 c0 {4,S} {10,D} {18,S}
10 C u0 p0 c0 {7,S} {9,D} {21,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.6332,0.0686571,8.67667e-06,-5.24024e-08,2.23942e-11,36873.9,35.024], Tmin=(200,'K'), Tmax=(1006.87,'K')),
            NASAPolynomial(coeffs=[6.82214,0.0674243,-3.76923e-05,1.0217e-08,-1.07882e-12,33531,-13.971], Tmin=(1006.87,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 167,
    label = "C10H11_30",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {11,S}
2  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u1 p0 c0 {1,S} {2,S} {5,S}
5  C u0 p0 c0 {4,S} {8,S} {9,D}
6  C u0 p0 c0 {1,S} {10,D} {17,S}
7  C u0 p0 c0 {2,S} {8,D} {18,S}
8  C u0 p0 c0 {5,S} {7,D} {21,S}
9  C u0 p0 c0 {5,D} {10,S} {20,S}
10 C u0 p0 c0 {6,D} {9,S} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.95026,0.0753098,-8.15005e-06,-3.77979e-08,1.82076e-11,27297.6,35.9136], Tmin=(200,'K'), Tmax=(990.6,'K')),
            NASAPolynomial(coeffs=[7.69856,0.0647002,-3.50165e-05,9.17596e-09,-9.391e-13,23994.9,-17.5666], Tmin=(990.6,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 168,
    label = "C10H11_31",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,B} {5,B}
3  C u1 p0 c0 {1,S} {9,S} {13,S}
4  C u0 p0 c0 {2,B} {6,B} {15,S}
5  C u0 p0 c0 {2,B} {8,B} {19,S}
6  C u0 p0 c0 {4,B} {7,B} {16,S}
7  C u0 p0 c0 {6,B} {8,B} {17,S}
8  C u0 p0 c0 {5,B} {7,B} {18,S}
9  C u0 p0 c0 {3,S} {10,D} {14,S}
10 C u0 p0 c0 {9,D} {20,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.26698,0.0817265,-2.42943e-05,-2.34106e-08,1.38251e-11,27545.1,39.9174], Tmin=(200,'K'), Tmax=(986.95,'K')),
            NASAPolynomial(coeffs=[8.87421,0.0619706,-3.28695e-05,8.45603e-09,-8.51665e-13,24109,-19.9528], Tmin=(986.95,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 169,
    label = "C10H11_32",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {5,S} {6,D}
3  C u1 p0 c0 {1,S} {2,S} {13,S}
4  C u0 p0 c0 {1,S} {5,D} {14,S}
5  C u0 p0 c0 {2,S} {4,D} {19,S}
6  C u0 p0 c0 {2,D} {8,S} {18,S}
7  C u0 p0 c0 {8,D} {9,S} {16,S}
8  C u0 p0 c0 {6,S} {7,D} {17,S}
9  C u0 p0 c0 {7,S} {10,D} {15,S}
10 C u0 p0 c0 {9,D} {20,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.62524,0.0893787,-4.28321e-05,-6.55686e-09,8.45742e-12,36117.8,39.7731], Tmin=(200,'K'), Tmax=(992.7,'K')),
            NASAPolynomial(coeffs=[10.1117,0.059934,-3.13983e-05,7.96553e-09,-7.90991e-13,32511,-27.0114], Tmin=(992.7,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 170,
    label = "C10H11_33",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
2  C u0 p0 c0 {4,S} {5,S} {6,D}
3  C u0 p0 c0 {1,S} {7,D} {14,S}
4  C u1 p0 c0 {2,S} {9,S} {15,S}
5  C u0 p0 c0 {2,S} {8,D} {18,S}
6  C u0 p0 c0 {2,D} {10,S} {21,S}
7  C u0 p0 c0 {3,D} {8,S} {16,S}
8  C u0 p0 c0 {5,D} {7,S} {17,S}
9  C u0 p0 c0 {4,S} {10,D} {19,S}
10 C u0 p0 c0 {6,S} {9,D} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.53453,0.0901034,-4.74923e-05,-4.60082e-10,6.08629e-12,33915.3,40.4032], Tmin=(200,'K'), Tmax=(999.25,'K')),
            NASAPolynomial(coeffs=[9.62591,0.0604461,-3.15258e-05,7.9369e-09,-7.80409e-13,30535.4,-23.0064], Tmin=(999.25,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 171,
    label = "C10H11_34",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {8,S} {15,S}
5  C u0 p0 c0 {1,S} {9,D} {17,S}
6  C u0 p0 c0 {2,S} {8,D} {16,S}
7  C u0 p0 c0 {3,S} {10,D} {18,S}
8  C u0 p0 c0 {4,S} {6,D} {19,S}
9  C u0 p0 c0 {5,D} {10,S} {20,S}
10 C u0 p0 c0 {7,D} {9,S} {21,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.93994,0.0740554,-3.81167e-06,-4.21977e-08,1.95879e-11,35951.8,36.1634], Tmin=(200,'K'), Tmax=(998.56,'K')),
            NASAPolynomial(coeffs=[8.03422,0.064564,-3.53138e-05,9.38431e-09,-9.74749e-13,32441.1,-19.5466], Tmin=(998.56,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 172,
    label = "C10H11_35",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {11,S}
2  C u0 p0 c0 {4,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {8,S} {14,S} {15,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  C u0 p0 c0 {1,S} {7,D} {17,S}
6  C u0 p0 c0 {1,S} {10,D} {16,S}
7  C u0 p0 c0 {2,S} {5,D} {18,S}
8  C u0 p0 c0 {3,S} {9,D} {19,S}
9  C u0 p0 c0 {8,D} {10,S} {20,S}
10 C u0 p0 c0 {6,D} {9,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.68336,0.0709236,1.52849e-06,-4.55909e-08,2.03915e-11,43337.3,35.6551], Tmin=(200,'K'), Tmax=(992.14,'K')),
            NASAPolynomial(coeffs=[6.50069,0.0670654,-3.66904e-05,9.69089e-09,-9.97232e-13,40279.3,-10.9908], Tmin=(992.14,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 173,
    label = "C10H11_36",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {8,S} {15,S}
5  C u0 p0 c0 {2,S} {9,D} {17,S}
6  C u0 p0 c0 {2,S} {10,D} {18,S}
7  C u0 p0 c0 {3,S} {8,D} {16,S}
8  C u0 p0 c0 {4,S} {7,D} {19,S}
9  C u0 p0 c0 {5,D} {10,S} {20,S}
10 C u0 p0 c0 {6,D} {9,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.91826,0.0730669,-4.10794e-07,-4.55385e-08,2.06025e-11,37826.4,37.907], Tmin=(200,'K'), Tmax=(1003.96,'K')),
            NASAPolynomial(coeffs=[8.10897,0.0649777,-3.59287e-05,9.65745e-09,-1.01363e-12,34207.3,-18.5051], Tmin=(1003.96,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 174,
    label = "C10H11_37",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {5,B} {7,B}
5  C u0 p0 c0 {4,B} {6,S} {8,B}
6  C u1 p0 c0 {2,S} {5,S} {17,S}
7  C u0 p0 c0 {4,B} {10,B} {21,S}
8  C u0 p0 c0 {5,B} {9,B} {18,S}
9  C u0 p0 c0 {8,B} {10,B} {19,S}
10 C u0 p0 c0 {7,B} {9,B} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.73704,0.0718976,-1.18202e-06,-4.32265e-08,1.97081e-11,18622.8,35.8146], Tmin=(200,'K'), Tmax=(991.3,'K')),
            NASAPolynomial(coeffs=[6.84638,0.0660663,-3.59433e-05,9.46285e-09,-9.72127e-13,15505.8,-12.6588], Tmin=(991.3,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 175,
    label = "C10H11_38",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
4  C u1 p0 c0 {1,S} {3,S} {6,S}
5  C u0 p0 c0 {2,S} {6,B} {7,B}
6  C u0 p0 c0 {4,S} {5,B} {8,B}
7  C u0 p0 c0 {5,B} {9,B} {18,S}
8  C u0 p0 c0 {6,B} {10,B} {21,S}
9  C u0 p0 c0 {7,B} {10,B} {19,S}
10 C u0 p0 c0 {8,B} {9,B} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.73896,0.0730334,-5.27429e-06,-3.89631e-08,1.8336e-11,17263,36.0354], Tmin=(200,'K'), Tmax=(983.8,'K')),
            NASAPolynomial(coeffs=[6.48146,0.066323,-3.57717e-05,9.30301e-09,-9.42776e-13,14352.9,-10.0592], Tmin=(983.8,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 176,
    label = "C10H11_39",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {5,B} {7,B}
5  C u0 p0 c0 {4,B} {6,S} {8,B}
6  C u1 p0 c0 {3,S} {5,S} {17,S}
7  C u0 p0 c0 {4,B} {10,B} {20,S}
8  C u0 p0 c0 {5,B} {9,B} {21,S}
9  C u0 p0 c0 {8,B} {10,B} {18,S}
10 C u0 p0 c0 {7,B} {9,B} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.38727,0.0658873,1.21681e-05,-5.39356e-08,2.26348e-11,17195.1,32.526], Tmin=(200,'K'), Tmax=(999.15,'K')),
            NASAPolynomial(coeffs=[5.46572,0.0689542,-3.8228e-05,1.02441e-08,-1.0686e-12,14303.1,-8.14893], Tmin=(999.15,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 177,
    label = "C10H11_5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u1 p0 c0 {1,S} {4,S} {13,S}
3  C u0 p0 c0 {1,S} {5,D} {14,S}
4  C u0 p0 c0 {2,S} {6,D} {15,S}
5  C u0 p0 c0 {3,D} {10,S} {21,S}
6  C u0 p0 c0 {4,D} {7,S} {16,S}
7  C u0 p0 c0 {6,S} {8,D} {17,S}
8  C u0 p0 c0 {7,D} {9,S} {18,S}
9  C u0 p0 c0 {8,S} {10,D} {19,S}
10 C u0 p0 c0 {5,S} {9,D} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.37222,0.0846409,-3.16765e-05,-1.63378e-08,1.1491e-11,70650.5,36.9326], Tmin=(200,'K'), Tmax=(986.96,'K')),
            NASAPolynomial(coeffs=[8.95057,0.0620756,-3.28298e-05,8.38566e-09,-8.36659e-13,67279.5,-23.2998], Tmin=(986.96,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 178,
    label = "C10H11_6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {8,S} {15,S}
5  C u0 p0 c0 {2,S} {8,D} {16,S}
6  C u0 p0 c0 {2,S} {9,D} {17,S}
7  C u0 p0 c0 {3,S} {10,D} {18,S}
8  C u0 p0 c0 {4,S} {5,D} {19,S}
9  C u0 p0 c0 {6,D} {10,S} {20,S}
10 C u0 p0 c0 {7,D} {9,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.69142,0.0702198,4.14588e-06,-4.82927e-08,2.12196e-11,37646.3,35.1875], Tmin=(200,'K'), Tmax=(999.72,'K')),
            NASAPolynomial(coeffs=[6.88863,0.0666985,-3.67963e-05,9.83569e-09,-1.02529e-12,34391.2,-13.9039], Tmin=(999.72,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 179,
    label = "C10H11_7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {9,D} {16,S}
5  C u0 p0 c0 {2,S} {7,D} {18,S}
6  C u1 p0 c0 {2,S} {8,S} {15,S}
7  C u0 p0 c0 {3,S} {5,D} {17,S}
8  C u0 p0 c0 {6,S} {10,D} {19,S}
9  C u0 p0 c0 {4,D} {10,S} {21,S}
10 C u0 p0 c0 {8,D} {9,S} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.61391,0.0688821,7.12326e-06,-5.06686e-08,2.18597e-11,34143.6,34.919], Tmin=(200,'K'), Tmax=(1001.81,'K')),
            NASAPolynomial(coeffs=[6.58713,0.0673572,-3.73388e-05,1.00261e-08,-1.04918e-12,30933.7,-12.4803], Tmin=(1001.81,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 180,
    label = "C10H11_8",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {3,S} {8,D}
5  C u1 p0 c0 {1,S} {9,S} {16,S}
6  C u0 p0 c0 {2,S} {10,D} {18,S}
7  C u0 p0 c0 {3,S} {9,D} {17,S}
8  C u0 p0 c0 {4,D} {10,S} {20,S}
9  C u0 p0 c0 {5,S} {7,D} {19,S}
10 C u0 p0 c0 {6,D} {8,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.66232,0.0702152,3.40969e-06,-4.73373e-08,2.09119e-11,33504.9,34.6764], Tmin=(200,'K'), Tmax=(995.7,'K')),
            NASAPolynomial(coeffs=[6.61803,0.0669078,-3.67378e-05,9.76016e-09,-1.011e-12,30371,-12.6928], Tmin=(995.7,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 181,
    label = "C10H11_9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {5,D}
3  C u0 p0 c0 {1,S} {6,D} {13,S}
4  C u1 p0 c0 {2,S} {6,S} {14,S}
5  C u0 p0 c0 {2,D} {8,S} {18,S}
6  C u0 p0 c0 {3,D} {4,S} {19,S}
7  C u0 p0 c0 {8,D} {9,S} {16,S}
8  C u0 p0 c0 {5,S} {7,D} {17,S}
9  C u0 p0 c0 {7,S} {10,D} {15,S}
10 C u0 p0 c0 {9,D} {20,S} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.59375,0.0886258,-4.09183e-05,-8.35435e-09,9.04407e-12,34546.9,39.5492], Tmin=(200,'K'), Tmax=(991.68,'K')),
            NASAPolynomial(coeffs=[9.9922,0.0601492,-3.156e-05,8.01956e-09,-7.97574e-13,30954.7,-26.5915], Tmin=(991.68,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 182,
    label = "C10H12_64",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {6,B} {8,B}
6  C u0 p0 c0 {3,S} {5,B} {7,B}
7  C u0 p0 c0 {6,B} {9,B} {19,S}
8  C u0 p0 c0 {5,B} {10,B} {22,S}
9  C u0 p0 c0 {7,B} {10,B} {20,S}
10 C u0 p0 c0 {8,B} {9,B} {21,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.47947,0.0675854,1.34893e-05,-5.59326e-08,2.34196e-11,244.078,33.5539], Tmin=(200,'K'), Tmax=(989.53,'K')),
            NASAPolynomial(coeffs=[4.60765,0.0728716,-3.98372e-05,1.05231e-08,-1.0831e-12,-2424.07,-3.14367], Tmin=(989.53,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 183,
    label = "C10H12_65",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {6,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {6,B} {7,B}
6  C u0 p0 c0 {4,S} {5,B} {8,B}
7  C u0 p0 c0 {5,B} {10,B} {21,S}
8  C u0 p0 c0 {6,B} {9,B} {22,S}
9  C u0 p0 c0 {8,B} {10,B} {19,S}
10 C u0 p0 c0 {7,B} {9,B} {20,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.15539,0.0622359,2.49327e-05,-6.46716e-08,2.56567e-11,-250.351,31.4017], Tmin=(200,'K'), Tmax=(998.21,'K')),
            NASAPolynomial(coeffs=[3.18917,0.0758752,-4.22193e-05,1.13365e-08,-1.18327e-12,-2664.6,2.70125], Tmin=(998.21,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 184,
    label = "C10H13_2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {12,S}
3  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {4,S} {8,D}
7  C u1 p0 c0 {2,S} {9,S} {20,S}
8  C u0 p0 c0 {6,D} {10,S} {21,S}
9  C u0 p0 c0 {7,S} {10,D} {23,S}
10 C u0 p0 c0 {8,S} {9,D} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.97026,0.0743571,7.09699e-06,-5.32976e-08,2.31376e-11,15959.2,37.1417], Tmin=(200,'K'), Tmax=(987.99,'K')),
            NASAPolynomial(coeffs=[5.6217,0.0746705,-4.05206e-05,1.06435e-08,-1.09118e-12,12943.6,-7.06279], Tmin=(987.99,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 185,
    label = "C10H13_3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,S} {12,S} {13,S}
5  C u0 p0 c0 {4,S} {6,S} {18,S} {19,S}
6  C u0 p0 c0 {1,S} {5,S} {8,D}
7  C u1 p0 c0 {1,S} {9,S} {20,S}
8  C u0 p0 c0 {6,D} {10,S} {23,S}
9  C u0 p0 c0 {7,S} {10,D} {21,S}
10 C u0 p0 c0 {8,S} {9,D} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.58176,0.0678497,2.11733e-05,-6.42834e-08,2.60455e-11,13613,34.3154], Tmin=(200,'K'), Tmax=(996.62,'K')),
            NASAPolynomial(coeffs=[4.01028,0.0779871,-4.3122e-05,1.15278e-08,-1.19989e-12,10880.3,-0.761829], Tmin=(996.62,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 186,
    label = "C10H14_88",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {9,S} {10,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {1,S} {9,D} {21,S}
8  C u0 p0 c0 {1,S} {10,D} {24,S}
9  C u0 p0 c0 {5,S} {7,D} {22,S}
10 C u0 p0 c0 {5,S} {8,D} {23,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.44459,0.0836013,-9.92456e-06,-3.9167e-08,1.90457e-11,14388.4,39.6137], Tmin=(200,'K'), Tmax=(974.13,'K')),
            NASAPolynomial(coeffs=[6.13265,0.0757298,-3.99161e-05,1.0179e-08,-1.01495e-12,11419.7,-8.202], Tmin=(974.13,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 187,
    label = "C10H14_89",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {8,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {1,S} {9,D} {21,S}
8  C u0 p0 c0 {5,S} {10,D} {22,S}
9  C u0 p0 c0 {7,D} {10,S} {23,S}
10 C u0 p0 c0 {8,D} {9,S} {24,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.46793,0.0837225,-9.77807e-06,-3.95351e-08,1.91997e-11,14887.3,39.7223], Tmin=(200,'K'), Tmax=(975.25,'K')),
            NASAPolynomial(coeffs=[6.28158,0.0755606,-3.98661e-05,1.01816e-08,-1.01697e-12,11862.2,-9.02935], Tmin=(975.25,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 188,
    label = "C10H14_90",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
5  C u0 p0 c0 {9,S} {10,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {1,S} {9,D} {21,S}
8  C u0 p0 c0 {1,S} {10,D} {24,S}
9  C u0 p0 c0 {5,S} {7,D} {22,S}
10 C u0 p0 c0 {5,S} {8,D} {23,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.21742,0.078849,1.95249e-06,-4.97669e-08,2.22791e-11,13570.2,37.9464], Tmin=(200,'K'), Tmax=(978.05,'K')),
            NASAPolynomial(coeffs=[5.35813,0.0774623,-4.131e-05,1.06605e-08,-1.07501e-12,10672.9,-5.66955], Tmin=(978.05,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 189,
    label = "C10H14_91",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {8,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {1,S} {9,D} {21,S}
8  C u0 p0 c0 {5,S} {10,D} {22,S}
9  C u0 p0 c0 {7,D} {10,S} {23,S}
10 C u0 p0 c0 {8,D} {9,S} {24,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.23214,0.0786571,3.02985e-06,-5.10118e-08,2.26928e-11,13926.1,37.6983], Tmin=(200,'K'), Tmax=(980.79,'K')),
            NASAPolynomial(coeffs=[5.54122,0.0773137,-4.13461e-05,1.07115e-08,-1.0848e-12,10941.1,-7.09681], Tmin=(980.79,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 190,
    label = "C10H14_92",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {4,S} {15,S} {16,S}
6  C u0 p0 c0 {9,S} {10,S} {19,S} {20,S}
7  C u0 p0 c0 {1,S} {9,D} {21,S}
8  C u0 p0 c0 {1,S} {10,D} {24,S}
9  C u0 p0 c0 {6,S} {7,D} {22,S}
10 C u0 p0 c0 {6,S} {8,D} {23,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.76368,0.0704834,2.12012e-05,-6.56202e-08,2.66938e-11,6185.1,35.4945], Tmin=(200,'K'), Tmax=(991.1,'K')),
            NASAPolynomial(coeffs=[3.70681,0.0810902,-4.43206e-05,1.17286e-08,-1.21062e-12,3495.45,1.05291], Tmin=(991.1,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 191,
    label = "C10H14_93",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {4,S} {15,S} {16,S}
6  C u0 p0 c0 {1,S} {8,S} {19,S} {20,S}
7  C u0 p0 c0 {1,S} {9,D} {21,S}
8  C u0 p0 c0 {6,S} {10,D} {22,S}
9  C u0 p0 c0 {7,D} {10,S} {23,S}
10 C u0 p0 c0 {8,D} {9,S} {24,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.77866,0.0705725,2.13376e-05,-6.59141e-08,2.68044e-11,5965.19,35.0375], Tmin=(200,'K'), Tmax=(992.32,'K')),
            NASAPolynomial(coeffs=[3.83009,0.0809976,-4.43549e-05,1.17665e-08,-1.21758e-12,3225.63,-0.173237], Tmin=(992.32,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 192,
    label = "C10H6_3",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {8,S}
3  C u0 p0 c0 {1,B} {5,B} {11,S}
4  C u0 p0 c0 {2,B} {6,B} {14,S}
5  C u0 p0 c0 {3,B} {6,B} {12,S}
6  C u0 p0 c0 {4,B} {5,B} {13,S}
7  C u0 p0 c0 {1,S} {9,T}
8  C u0 p0 c0 {2,S} {10,T}
9  C u0 p0 c0 {7,T} {15,S}
10 C u0 p0 c0 {8,T} {16,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.09803,0.0884509,-8.14488e-05,3.83127e-08,-7.20209e-12,64468.4,33.6362], Tmin=(200,'K'), Tmax=(1258.27,'K')),
            NASAPolynomial(coeffs=[15.0386,0.0339734,-1.65046e-05,3.90302e-09,-3.65305e-13,60156,-52.975], Tmin=(1258.27,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 193,
    label = "C10H6_4",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,S} {4,B}
2  C u0 p0 c0 {1,B} {5,B} {10,S}
3  C u0 p0 c0 {1,S} {8,D} {9,S}
4  C u0 p0 c0 {1,B} {7,B} {14,S}
5  C u0 p0 c0 {2,B} {6,B} {11,S}
6  C u0 p0 c0 {5,B} {7,B} {12,S}
7  C u0 p0 c0 {4,B} {6,B} {13,S}
8  C u0 p0 c0 {3,D} {15,S} {16,S}
9  C u0 p0 c0 {3,S} {10,T}
10 C u0 p0 c0 {2,S} {9,T}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.3602,0.0709901,-3.57495e-05,-4.97025e-09,6.94917e-12,81659.1,31.4703], Tmin=(200,'K'), Tmax=(1001.77,'K')),
            NASAPolynomial(coeffs=[10.3717,0.0434654,-2.34645e-05,6.10617e-09,-6.19564e-13,78339.2,-29.9887], Tmin=(1001.77,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 194,
    label = "C10H6_5",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {5,S}
2  C u0 p0 c0 {1,B} {4,B} {9,S}
3  C u0 p0 c0 {1,B} {7,B} {14,S}
4  C u0 p0 c0 {2,B} {6,B} {11,S}
5  C u0 p0 c0 {1,S} {8,D} {15,S}
6  C u0 p0 c0 {4,B} {7,B} {12,S}
7  C u0 p0 c0 {3,B} {6,B} {13,S}
8  C u0 p0 c0 {5,D} {10,S} {16,S}
9  C u0 p0 c0 {2,S} {10,T}
10 C u0 p0 c0 {8,S} {9,T}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.868763,0.060845,-1.0675e-05,-2.73572e-08,1.38038e-11,60159.5,28.9232], Tmin=(200,'K'), Tmax=(1006.87,'K')),
            NASAPolynomial(coeffs=[8.82624,0.0468093,-2.62342e-05,7.09178e-09,-7.45244e-13,56966.3,-24.0779], Tmin=(1006.87,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 195,
    label = "C10H6_6",
    molecule = 
"""
1  C u0 p0 c0 {3,D} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {4,S} {8,D}
3  C u0 p0 c0 {1,D} {2,S} {9,S}
4  C u0 p0 c0 {2,S} {5,D} {11,S}
5  C u0 p0 c0 {1,S} {4,D} {12,S}
6  C u0 p0 c0 {1,S} {7,D} {13,S}
7  C u0 p0 c0 {6,D} {10,S} {14,S}
8  C u0 p0 c0 {2,D} {15,S} {16,S}
9  C u0 p0 c0 {3,S} {10,T}
10 C u0 p0 c0 {7,S} {9,T}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.28222,0.068319,-2.77995e-05,-1.29011e-08,9.56986e-12,72048.8,30.7369], Tmin=(200,'K'), Tmax=(1002.83,'K')),
            NASAPolynomial(coeffs=[10.3252,0.0439068,-2.40214e-05,6.35026e-09,-6.54777e-13,68620.2,-30.7821], Tmin=(1002.83,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 196,
    label = "C10H6_7",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {8,S}
3  C u0 p0 c0 {1,B} {5,B} {11,S}
4  C u0 p0 c0 {2,B} {6,B} {14,S}
5  C u0 p0 c0 {3,B} {6,B} {12,S}
6  C u0 p0 c0 {4,B} {5,B} {13,S}
7  C u0 p0 c0 {1,S} {10,D} {15,S}
8  C u0 p0 c0 {2,S} {9,D} {16,S}
9  C u0 p0 c0 {8,D} {10,D}
10 C u0 p0 c0 {7,D} {9,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.888124,0.0612048,-1.1442e-05,-2.6727e-08,1.36239e-11,61767.4,28.9432], Tmin=(200,'K'), Tmax=(1006.26,'K')),
            NASAPolynomial(coeffs=[8.862,0.0467735,-2.61927e-05,7.07061e-09,-7.41824e-13,58573.5,-24.2761], Tmin=(1006.26,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 197,
    label = "C10H7_3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {5,B}
2  C u0 p0 c0 {1,B} {4,B} {8,B}
3  C u0 p0 c0 {1,B} {6,B} {12,S}
4  C u0 p0 c0 {2,B} {7,B} {15,S}
5  C u0 p0 c0 {1,B} {9,B} {11,S}
6  C u0 p0 c0 {3,B} {7,B} {13,S}
7  C u0 p0 c0 {4,B} {6,B} {14,S}
8  C u0 p0 c0 {2,B} {10,B} {17,S}
9  C u0 p0 c0 {5,B} {10,B} {16,S}
10 C u1 p0 c0 {8,B} {9,B}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.799466,0.0584404,2.44476e-06,-4.00096e-08,1.76498e-11,46039.9,29.3838], Tmin=(200,'K'), Tmax=(1013.96,'K')),
            NASAPolynomial(coeffs=[7.60704,0.0528932,-3.02024e-05,8.316e-09,-8.87921e-13,42915.5,-18.2897], Tmin=(1013.96,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 198,
    label = "C10H7_4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {4,B}
2  C u0 p0 c0 {1,B} {5,B} {10,B}
3  C u0 p0 c0 {1,B} {8,B} {12,S}
4  C u0 p0 c0 {1,B} {6,B} {13,S}
5  C u0 p0 c0 {2,B} {7,B} {16,S}
6  C u0 p0 c0 {4,B} {7,B} {14,S}
7  C u0 p0 c0 {5,B} {6,B} {15,S}
8  C u0 p0 c0 {3,B} {9,B} {11,S}
9  C u0 p0 c0 {8,B} {10,B} {17,S}
10 C u1 p0 c0 {2,B} {9,B}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.774659,0.0580717,3.19858e-06,-4.05981e-08,1.78114e-11,46188.5,29.3421], Tmin=(200,'K'), Tmax=(1014.08,'K')),
            NASAPolynomial(coeffs=[7.50909,0.0530721,-3.03428e-05,8.36451e-09,-8.93968e-13,43085.4,-17.7542], Tmin=(1014.08,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 199,
    label = "C10H7_5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,B} {5,S} {6,B}
2  C u0 p0 c0 {3,S} {4,S} {9,D}
3  C u0 p0 c0 {1,B} {2,S} {10,B}
4  C u0 p0 c0 {2,S} {5,D} {11,S}
5  C u0 p0 c0 {1,S} {4,D} {12,S}
6  C u0 p0 c0 {1,B} {7,B} {13,S}
7  C u0 p0 c0 {6,B} {8,B} {14,S}
8  C u0 p0 c0 {7,B} {10,B} {15,S}
9  C u0 p0 c0 {2,D} {16,S} {17,S}
10 C u1 p0 c0 {3,B} {8,B}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.20882,0.0651664,-1.2189e-05,-2.84112e-08,1.44922e-11,56864.8,31.309], Tmin=(200,'K'), Tmax=(1006.83,'K')),
            NASAPolynomial(coeffs=[9.29022,0.0494713,-2.75659e-05,7.43512e-09,-7.81259e-13,53432,-25.9627], Tmin=(1006.83,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 200,
    label = "C10H7_6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,S} {5,B}
2  C u0 p0 c0 {1,B} {4,B} {8,S}
3  C u0 p0 c0 {1,S} {9,D} {10,S}
4  C u0 p0 c0 {2,B} {6,B} {11,S}
5  C u0 p0 c0 {1,B} {7,B} {14,S}
6  C u0 p0 c0 {4,B} {7,B} {12,S}
7  C u0 p0 c0 {5,B} {6,B} {13,S}
8  C u0 p0 c0 {2,S} {10,D} {15,S}
9  C u0 p0 c0 {3,D} {16,S} {17,S}
10 C u1 p0 c0 {3,S} {8,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.19649,0.0651842,-1.26366e-05,-2.784e-08,1.42985e-11,59890.1,31.3545], Tmin=(200,'K'), Tmax=(1005.18,'K')),
            NASAPolynomial(coeffs=[9.17829,0.049529,-2.7522e-05,7.39936e-09,-7.75025e-13,56509.6,-25.1921], Tmin=(1005.18,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 201,
    label = "C10H7_7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {8,S}
3  C u0 p0 c0 {1,B} {5,B} {11,S}
4  C u0 p0 c0 {2,B} {6,B} {14,S}
5  C u0 p0 c0 {3,B} {6,B} {12,S}
6  C u0 p0 c0 {4,B} {5,B} {13,S}
7  C u0 p0 c0 {1,S} {9,D} {15,S}
8  C u0 p0 c0 {2,S} {10,T}
9  C u1 p0 c0 {7,D} {16,S}
10 C u0 p0 c0 {8,T} {17,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.20499,0.0883391,-7.18611e-05,2.71119e-08,-3.28545e-12,73478.6,36.1124], Tmin=(200,'K'), Tmax=(1056.54,'K')),
            NASAPolynomial(coeffs=[13.2192,0.0412699,-2.11151e-05,5.23777e-09,-5.10338e-13,69587.2,-42.1403], Tmin=(1056.54,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 202,
    label = "C10H7_8",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,S} {6,B}
2  C u0 p0 c0 {1,B} {4,S} {5,B}
3  C u0 p0 c0 {1,S} {7,S} {10,D}
4  C u0 p0 c0 {2,S} {7,D} {12,S}
5  C u0 p0 c0 {2,B} {8,B} {13,S}
6  C u0 p0 c0 {1,B} {9,B} {16,S}
7  C u0 p0 c0 {3,S} {4,D} {11,S}
8  C u0 p0 c0 {5,B} {9,B} {14,S}
9  C u0 p0 c0 {6,B} {8,B} {15,S}
10 C u1 p0 c0 {3,D} {17,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.32004,0.0667831,-1.52774e-05,-2.61706e-08,1.39091e-11,56546.2,31.6181], Tmin=(200,'K'), Tmax=(1007.45,'K')),
            NASAPolynomial(coeffs=[9.82124,0.0486123,-2.70308e-05,7.28779e-09,-7.66299e-13,52978.7,-28.7795], Tmin=(1007.45,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 203,
    label = "C10H8_10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,D} {6,S}
2  C u0 p0 c0 {1,S} {5,D} {7,S}
3  C u0 p0 c0 {4,S} {5,S} {10,D}
4  C u0 p0 c0 {1,D} {3,S} {11,S}
5  C u0 p0 c0 {2,D} {3,S} {16,S}
6  C u0 p0 c0 {1,S} {8,D} {12,S}
7  C u0 p0 c0 {2,S} {9,D} {15,S}
8  C u0 p0 c0 {6,D} {9,S} {13,S}
9  C u0 p0 c0 {7,D} {8,S} {14,S}
10 C u0 p0 c0 {3,D} {17,S} {18,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.41333,0.0678879,-1.17148e-05,-3.03423e-08,1.53111e-11,37146.2,32.1064], Tmin=(200,'K'), Tmax=(1003.42,'K')),
            NASAPolynomial(coeffs=[9.11432,0.052702,-2.90483e-05,7.77284e-09,-8.12231e-13,33685.3,-25.4375], Tmin=(1003.42,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 204,
    label = "C10H8_11",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {9,S}
3  C u0 p0 c0 {1,B} {6,B} {14,S}
4  C u0 p0 c0 {2,B} {5,B} {11,S}
5  C u0 p0 c0 {4,B} {6,B} {12,S}
6  C u0 p0 c0 {3,B} {5,B} {13,S}
7  C u0 p0 c0 {1,S} {8,D} {15,S}
8  C u0 p0 c0 {7,D} {16,S} {17,S}
9  C u0 p0 c0 {2,S} {10,T}
10 C u0 p0 c0 {9,T} {18,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.66952,0.0754157,-3.61741e-05,-6.54169e-09,7.71844e-12,43636.2,32.9132], Tmin=(200,'K'), Tmax=(995.24,'K')),
            NASAPolynomial(coeffs=[10.1331,0.0480879,-2.52935e-05,6.47138e-09,-6.50054e-13,40291,-28.9747], Tmin=(995.24,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 205,
    label = "C10H8_12",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,S} {7,B}
2  C u0 p0 c0 {1,B} {5,S} {6,B}
3  C u0 p0 c0 {1,S} {4,S} {10,D}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  C u0 p0 c0 {2,S} {4,D} {12,S}
6  C u0 p0 c0 {2,B} {8,B} {13,S}
7  C u0 p0 c0 {1,B} {9,B} {16,S}
8  C u0 p0 c0 {6,B} {9,B} {14,S}
9  C u0 p0 c0 {7,B} {8,B} {15,S}
10 C u0 p0 c0 {3,D} {17,S} {18,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.19171,0.0641814,-3.64408e-06,-3.67985e-08,1.70948e-11,26380.5,30.5696], Tmin=(200,'K'), Tmax=(1006.77,'K')),
            NASAPolynomial(coeffs=[8.23566,0.0544159,-3.03506e-05,8.20537e-09,-8.64439e-13,23078.9,-21.9451], Tmin=(1006.77,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 206,
    label = "C10H8_13",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {4,S}
2  C u0 p0 c0 {1,D} {5,S} {6,S}
3  C u0 p0 c0 {1,S} {8,D} {13,S}
4  C u0 p0 c0 {1,S} {7,D} {14,S}
5  C u0 p0 c0 {2,S} {9,D} {15,S}
6  C u0 p0 c0 {2,S} {10,D} {18,S}
7  C u0 p0 c0 {4,D} {8,S} {11,S}
8  C u0 p0 c0 {3,D} {7,S} {12,S}
9  C u0 p0 c0 {5,D} {10,S} {16,S}
10 C u0 p0 c0 {6,D} {9,S} {17,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.46836,0.0680428,-1.07327e-05,-3.18363e-08,1.58389e-11,43272.4,31.3635], Tmin=(200,'K'), Tmax=(1008.99,'K')),
            NASAPolynomial(coeffs=[9.57628,0.0523286,-2.91022e-05,7.87332e-09,-8.31661e-13,39614.7,-29.1001], Tmin=(1008.99,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 207,
    label = "C10H8_14",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {4,S}
2  C u0 p0 c0 {1,B} {5,B} {12,S}
3  C u0 p0 c0 {1,B} {7,B} {16,S}
4  C u0 p0 c0 {1,S} {8,D} {11,S}
5  C u0 p0 c0 {2,B} {6,B} {13,S}
6  C u0 p0 c0 {5,B} {7,B} {14,S}
7  C u0 p0 c0 {3,B} {6,B} {15,S}
8  C u0 p0 c0 {4,D} {9,S} {17,S}
9  C u0 p0 c0 {8,S} {10,T}
10 C u0 p0 c0 {9,T} {18,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.96581,0.0816316,-4.86539e-05,4.5279e-09,4.15016e-12,43602.8,36.3489], Tmin=(200,'K'), Tmax=(1004.7,'K')),
            NASAPolynomial(coeffs=[10.7415,0.0485434,-2.5386e-05,6.42849e-09,-6.3745e-13,40165.9,-29.4126], Tmin=(1004.7,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 208,
    label = "C10H8_15",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {11,S}
3  C u0 p0 c0 {1,B} {6,B} {15,S}
4  C u0 p0 c0 {2,B} {5,B} {12,S}
5  C u0 p0 c0 {4,B} {6,B} {13,S}
6  C u0 p0 c0 {3,B} {5,B} {14,S}
7  C u0 p0 c0 {1,S} {9,D} {16,S}
8  C u0 p0 c0 {10,D} {17,S} {18,S}
9  C u0 p0 c0 {7,D} {10,D}
10 C u0 p0 c0 {8,D} {9,D}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.88626,0.0806514,-4.67854e-05,3.28066e-09,4.43628e-12,47122.2,35.4777], Tmin=(200,'K'), Tmax=(1003.95,'K')),
            NASAPolynomial(coeffs=[10.2906,0.0494118,-2.59225e-05,6.56718e-09,-6.50311e-13,43806.5,-27.653], Tmin=(1003.95,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 209,
    label = "C10H8_16",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,D}
2  C u0 p0 c0 {1,S} {4,S} {10,D}
3  C u0 p0 c0 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {2,S} {6,D} {14,S}
5  C u0 p0 c0 {3,D} {6,S} {12,S}
6  C u0 p0 c0 {4,D} {5,S} {13,S}
7  C u0 p0 c0 {9,D} {15,S} {16,S}
8  C u0 p0 c0 {10,D} {17,S} {18,S}
9  C u0 p0 c0 {1,D} {7,D}
10 C u0 p0 c0 {2,D} {8,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.16452,0.0887226,-6.81584e-05,2.40632e-08,-2.56097e-12,62840.7,35.5142], Tmin=(200,'K'), Tmax=(1060.07,'K')),
            NASAPolynomial(coeffs=[11.9788,0.0463192,-2.36714e-05,5.84231e-09,-5.64771e-13,59226.1,-36.4498], Tmin=(1060.07,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 210,
    label = "C10H8_17",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,B} {4,B}
2  C u0 p0 c0 {1,S} {8,D} {9,S}
3  C u0 p0 c0 {1,B} {5,B} {11,S}
4  C u0 p0 c0 {1,B} {7,B} {15,S}
5  C u0 p0 c0 {3,B} {6,B} {12,S}
6  C u0 p0 c0 {5,B} {7,B} {13,S}
7  C u0 p0 c0 {4,B} {6,B} {14,S}
8  C u0 p0 c0 {2,D} {16,S} {17,S}
9  C u0 p0 c0 {2,S} {10,T}
10 C u0 p0 c0 {9,T} {18,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.0637,0.0820538,-4.79832e-05,2.77545e-09,4.96906e-12,44091.1,35.5026], Tmin=(200,'K'), Tmax=(1002.5,'K')),
            NASAPolynomial(coeffs=[11.3267,0.0476258,-2.48992e-05,6.33025e-09,-6.32108e-13,40451.6,-33.8937], Tmin=(1002.5,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 211,
    label = "C10H8_18",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {9,S}
2  C u0 p0 c0 {1,B} {4,B} {11,S}
3  C u0 p0 c0 {1,B} {6,B} {15,S}
4  C u0 p0 c0 {2,B} {5,B} {12,S}
5  C u0 p0 c0 {4,B} {6,B} {13,S}
6  C u0 p0 c0 {3,B} {5,B} {14,S}
7  C u0 p0 c0 {8,D} {10,S} {16,S}
8  C u0 p0 c0 {7,D} {17,S} {18,S}
9  C u0 p0 c0 {1,S} {10,T}
10 C u0 p0 c0 {7,S} {9,T}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.78567,0.0792609,-4.4447e-05,1.70653e-09,4.83127e-12,42916,36.2461], Tmin=(200,'K'), Tmax=(1002.15,'K')),
            NASAPolynomial(coeffs=[9.86103,0.0499189,-2.61904e-05,6.63261e-09,-6.5618e-13,39720.8,-24.263], Tmin=(1002.15,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 212,
    label = "C10H8_7",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {4,B}
2  C u0 p0 c0 {1,B} {5,B} {6,B}
3  C u0 p0 c0 {1,B} {8,B} {13,S}
4  C u0 p0 c0 {1,B} {9,B} {14,S}
5  C u0 p0 c0 {2,B} {10,B} {17,S}
6  C u0 p0 c0 {2,B} {7,B} {18,S}
7  C u0 p0 c0 {6,B} {8,B} {11,S}
8  C u0 p0 c0 {3,B} {7,B} {12,S}
9  C u0 p0 c0 {4,B} {10,B} {15,S}
10 C u0 p0 c0 {5,B} {9,B} {16,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.740238,0.0570314,1.14171e-05,-4.83123e-08,2.00982e-11,15300.9,27.1224], Tmin=(200,'K'), Tmax=(1015.3,'K')),
            NASAPolynomial(coeffs=[6.24886,0.0584511,-3.34575e-05,9.24135e-09,-9.8955e-13,12389.3,-14.0516], Tmin=(1015.3,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 213,
    label = "C10H8_8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {4,S}
2  C u0 p0 c0 {1,S} {5,D} {6,S}
3  C u0 p0 c0 {1,D} {8,S} {13,S}
4  C u0 p0 c0 {1,S} {9,D} {14,S}
5  C u0 p0 c0 {2,D} {9,S} {16,S}
6  C u0 p0 c0 {2,S} {10,D} {17,S}
7  C u0 p0 c0 {8,D} {10,S} {11,S}
8  C u0 p0 c0 {3,S} {7,D} {12,S}
9  C u0 p0 c0 {4,D} {5,S} {15,S}
10 C u0 p0 c0 {6,D} {7,S} {18,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.01669,0.0613202,2.62311e-06,-4.17291e-08,1.84172e-11,32719.9,29.8061], Tmin=(200,'K'), Tmax=(1010.12,'K')),
            NASAPolynomial(coeffs=[7.46679,0.0560484,-3.16063e-05,8.61986e-09,-9.13947e-13,29561.2,-18.3594], Tmin=(1010.12,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 214,
    label = "C10H8_9",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {9,S}
3  C u0 p0 c0 {1,B} {6,B} {14,S}
4  C u0 p0 c0 {2,B} {5,B} {11,S}
5  C u0 p0 c0 {4,B} {6,B} {12,S}
6  C u0 p0 c0 {3,B} {5,B} {13,S}
7  C u1 p0 c0 {1,S} {15,S} {16,S}
8  C u1 p0 c0 {10,S} {17,S} {18,S}
9  C u0 p0 c0 {2,S} {10,T}
10 C u0 p0 c0 {8,S} {9,T}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.31542,0.0950594,-8.37722e-05,3.82617e-08,-7.0685e-12,65178.4,37.0208], Tmin=(200,'K'), Tmax=(1259.95,'K')),
            NASAPolynomial(coeffs=[14.3063,0.0422886,-2.09456e-05,5.01786e-09,-4.72069e-13,60990,-47.0095], Tmin=(1259.95,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 215,
    label = "C10H9_10",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {5,B} {7,B}
5  C u0 p0 c0 {4,B} {6,S} {8,B}
6  C u1 p0 c0 {2,S} {5,S} {15,S}
7  C u0 p0 c0 {4,B} {10,B} {19,S}
8  C u0 p0 c0 {5,B} {9,B} {16,S}
9  C u0 p0 c0 {8,B} {10,B} {17,S}
10 C u0 p0 c0 {7,B} {9,B} {18,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.27008,0.0636711,6.62249e-06,-4.76946e-08,2.05007e-11,36035.4,32.4233], Tmin=(200,'K'), Tmax=(1017.57,'K')),
            NASAPolynomial(coeffs=[7.72279,0.0598312,-3.41664e-05,9.46009e-09,-1.01783e-12,32573.8,-19.1347], Tmin=(1017.57,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 216,
    label = "C10H9_11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,D} {6,S}
3  C u0 p0 c0 {1,S} {2,D} {11,S}
4  C u0 p0 c0 {1,S} {7,D} {12,S}
5  C u0 p0 c0 {1,S} {8,D} {13,S}
6  C u0 p0 c0 {2,S} {10,D} {15,S}
7  C u0 p0 c0 {4,D} {9,S} {16,S}
8  C u0 p0 c0 {5,D} {9,S} {17,S}
9  C u1 p0 c0 {7,S} {8,S} {14,S}
10 C u0 p0 c0 {6,D} {18,S} {19,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.4716,0.0874739,-5.11627e-05,2.85657e-09,5.35474e-12,63367.9,38.6483], Tmin=(200,'K'), Tmax=(1002.75,'K')),
            NASAPolynomial(coeffs=[11.898,0.0505618,-2.64754e-05,6.74047e-09,-6.73915e-13,59460,-35.8324], Tmin=(1002.75,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 217,
    label = "C10H9_12",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {11,S}
3  C u0 p0 c0 {1,B} {6,B} {15,S}
4  C u0 p0 c0 {2,B} {5,B} {12,S}
5  C u0 p0 c0 {4,B} {6,B} {13,S}
6  C u0 p0 c0 {3,B} {5,B} {14,S}
7  C u0 p0 c0 {1,S} {10,D} {17,S}
8  C u0 p0 c0 {9,D} {10,S} {16,S}
9  C u0 p0 c0 {8,D} {18,S} {19,S}
10 C u1 p0 c0 {7,D} {8,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.01165,0.0815201,-4.07881e-05,-3.9454e-09,6.95261e-12,51824,38.9075], Tmin=(200,'K'), Tmax=(996.55,'K')),
            NASAPolynomial(coeffs=[9.58179,0.0542169,-2.86379e-05,7.29082e-09,-7.24005e-13,48558.4,-21.7753], Tmin=(996.55,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 218,
    label = "C10H9_13",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {4,B} {5,B}
3  C u1 p0 c0 {1,S} {2,S} {13,S}
4  C u0 p0 c0 {2,B} {6,B} {14,S}
5  C u0 p0 c0 {2,B} {8,B} {18,S}
6  C u0 p0 c0 {4,B} {7,B} {15,S}
7  C u0 p0 c0 {6,B} {8,B} {16,S}
8  C u0 p0 c0 {5,B} {7,B} {17,S}
9  C u0 p0 c0 {1,S} {10,T}
10 C u0 p0 c0 {9,T} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.31854,0.0870289,-5.3504e-05,7.01845e-09,3.59859e-12,50033.4,38.4473], Tmin=(200,'K'), Tmax=(1006.79,'K')),
            NASAPolynomial(coeffs=[11.1198,0.0513358,-2.66931e-05,6.72481e-09,-6.63972e-13,46430.5,-30.9307], Tmin=(1006.79,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 219,
    label = "C10H9_14",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {10,S}
3  C u0 p0 c0 {1,B} {6,B} {14,S}
4  C u0 p0 c0 {2,B} {5,B} {11,S}
5  C u0 p0 c0 {4,B} {6,B} {12,S}
6  C u0 p0 c0 {3,B} {5,B} {13,S}
7  C u0 p0 c0 {1,S} {8,D} {15,S}
8  C u0 p0 c0 {7,D} {16,S} {17,S}
9  C u0 p0 c0 {10,D} {18,S} {19,S}
10 C u1 p0 c0 {2,S} {9,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.30645,0.0889164,-5.98512e-05,1.41649e-08,9.58084e-13,48363.2,38.0364], Tmin=(200,'K'), Tmax=(1024.93,'K')),
            NASAPolynomial(coeffs=[11.0994,0.0514101,-2.6639e-05,6.66283e-09,-6.51477e-13,44837.2,-30.7645], Tmin=(1024.93,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 220,
    label = "C10H9_15",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,B} {6,B}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,B} {5,S} {7,B}
5  C u0 p0 c0 {3,D} {4,S} {13,S}
6  C u0 p0 c0 {2,B} {9,B} {17,S}
7  C u0 p0 c0 {4,B} {8,B} {14,S}
8  C u0 p0 c0 {7,B} {9,B} {15,S}
9  C u0 p0 c0 {6,B} {8,B} {16,S}
10 C u1 p0 c0 {3,S} {18,S} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.56956,0.0694933,-7.66865e-06,-3.56323e-08,1.7146e-11,28293,32.7969], Tmin=(200,'K'), Tmax=(1002.58,'K')),
            NASAPolynomial(coeffs=[8.67134,0.0570158,-3.14625e-05,8.42476e-09,-8.80583e-13,24813.2,-23.7494], Tmin=(1002.58,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 221,
    label = "C10H9_16",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {4,D} {6,S}
3  C u0 p0 c0 {2,S} {5,D} {7,S}
4  C u0 p0 c0 {1,S} {2,D} {13,S}
5  C u0 p0 c0 {1,S} {3,D} {14,S}
6  C u0 p0 c0 {2,S} {9,D} {17,S}
7  C u0 p0 c0 {3,S} {10,D} {18,S}
8  C u1 p0 c0 {9,S} {10,S} {15,S}
9  C u0 p0 c0 {6,D} {8,S} {16,S}
10 C u0 p0 c0 {7,D} {8,S} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.46074,0.0676071,-3.25053e-06,-3.92599e-08,1.81561e-11,37775,32.3326], Tmin=(200,'K'), Tmax=(1004.72,'K')),
            NASAPolynomial(coeffs=[8.18588,0.0581444,-3.23335e-05,8.70933e-09,-9.14215e-13,34375.7,-21.5219], Tmin=(1004.72,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 222,
    label = "C10H9_17",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {12,S}
4  C u0 p0 c0 {2,B} {7,B} {16,S}
5  C u0 p0 c0 {3,B} {6,B} {13,S}
6  C u0 p0 c0 {5,B} {7,B} {14,S}
7  C u0 p0 c0 {4,B} {6,B} {15,S}
8  C u1 p0 c0 {1,S} {17,S} {18,S}
9  C u0 p0 c0 {1,S} {10,T}
10 C u0 p0 c0 {9,T} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.58303,0.0943797,-7.30227e-05,2.59156e-08,-2.73442e-12,56717.7,39.7377], Tmin=(200,'K'), Tmax=(1053.29,'K')),
            NASAPolynomial(coeffs=[12.7022,0.0483313,-2.4533e-05,6.04044e-09,-5.8417e-13,52832.2,-37.9578], Tmin=(1053.29,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 223,
    label = "C10H9_18",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {10,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {5,D} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {10,D}
5  C u0 p0 c0 {1,S} {3,D} {15,S}
6  C u0 p0 c0 {3,S} {8,D} {16,S}
7  C u0 p0 c0 {4,S} {9,D} {19,S}
8  C u0 p0 c0 {6,D} {9,S} {17,S}
9  C u0 p0 c0 {7,D} {8,S} {18,S}
10 C u1 p0 c0 {2,S} {4,D}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.33017,0.0663793,-2.26739e-06,-3.91605e-08,1.79896e-11,54162.5,32.1582], Tmin=(200,'K'), Tmax=(998.39,'K')),
            NASAPolynomial(coeffs=[7.35664,0.0590778,-3.26169e-05,8.69615e-09,-9.02766e-13,51057.3,-16.601], Tmin=(998.39,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 224,
    label = "C10H9_19",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {6,S} {12,S}
4  C u0 p0 c0 {1,S} {9,D} {15,S}
5  C u0 p0 c0 {1,S} {10,D} {16,S}
6  C u1 p0 c0 {3,S} {8,S} {13,S}
7  C u0 p0 c0 {2,S} {8,D} {14,S}
8  C u0 p0 c0 {6,S} {7,D} {17,S}
9  C u0 p0 c0 {4,D} {10,S} {18,S}
10 C u0 p0 c0 {5,D} {9,S} {19,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.71439,0.0700523,-5.49004e-06,-3.91252e-08,1.83755e-11,51775.5,35.3836], Tmin=(200,'K'), Tmax=(1016.33,'K')),
            NASAPolynomial(coeffs=[9.86908,0.0561344,-3.16926e-05,8.72433e-09,-9.36904e-13,47785.3,-28.7348], Tmin=(1016.33,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 225,
    label = "C10H9_20",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {5,D}
3  C u0 p0 c0 {2,S} {4,B} {8,B}
4  C u0 p0 c0 {3,B} {6,S} {7,B}
5  C u0 p0 c0 {2,D} {6,S} {15,S}
6  C u1 p0 c0 {4,S} {5,S} {14,S}
7  C u0 p0 c0 {4,B} {9,B} {16,S}
8  C u0 p0 c0 {3,B} {10,B} {19,S}
9  C u0 p0 c0 {7,B} {10,B} {17,S}
10 C u0 p0 c0 {8,B} {9,B} {18,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.55688,0.070295,-1.11808e-05,-3.18266e-08,1.59099e-11,25648.2,34.2475], Tmin=(200,'K'), Tmax=(995.41,'K')),
            NASAPolynomial(coeffs=[8.29331,0.0571359,-3.11688e-05,8.22753e-09,-8.47363e-13,22378.1,-19.8043], Tmin=(995.41,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 226,
    label = "C10H9_21",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,B} {4,B}
2  C u0 p0 c0 {1,S} {8,S} {10,D}
3  C u0 p0 c0 {1,B} {5,B} {12,S}
4  C u0 p0 c0 {1,B} {7,B} {16,S}
5  C u0 p0 c0 {3,B} {6,B} {13,S}
6  C u0 p0 c0 {5,B} {7,B} {14,S}
7  C u0 p0 c0 {4,B} {6,B} {15,S}
8  C u0 p0 c0 {2,S} {9,D} {11,S}
9  C u0 p0 c0 {8,D} {17,S} {18,S}
10 C u1 p0 c0 {2,D} {19,S}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.13187,0.0817102,-3.88515e-05,-7.32779e-09,8.39374e-12,53574.7,37.3351], Tmin=(200,'K'), Tmax=(995.26,'K')),
            NASAPolynomial(coeffs=[10.4004,0.0529187,-2.7977e-05,7.17032e-09,-7.19554e-13,50011.6,-28.4348], Tmin=(995.26,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 227,
    label = "C10H9_22",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {4,S} {6,S} {14,S} {15,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  C u0 p0 c0 {1,S} {6,B} {7,B}
6  C u0 p0 c0 {3,S} {5,B} {8,B}
7  C u0 p0 c0 {5,B} {10,B} {18,S}
8  C u0 p0 c0 {6,B} {9,B} {19,S}
9  C u0 p0 c0 {8,B} {10,B} {16,S}
10 C u0 p0 c0 {7,B} {9,B} {17,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.11243,0.0617779,9.59942e-06,-4.94182e-08,2.08694e-11,47401.7,31.5886], Tmin=(200,'K'), Tmax=(1013.73,'K')),
            NASAPolynomial(coeffs=[6.77243,0.0612529,-3.48831e-05,9.59925e-09,-1.02533e-12,44231.5,-14.3106], Tmin=(1013.73,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 228,
    label = "C10H9_23",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,B} {6,B}
3  C u0 p0 c0 {2,B} {4,S} {7,B}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {1,S} {4,D} {13,S}
6  C u0 p0 c0 {2,B} {8,B} {14,S}
7  C u0 p0 c0 {3,B} {9,B} {17,S}
8  C u0 p0 c0 {6,B} {9,B} {15,S}
9  C u0 p0 c0 {7,B} {8,B} {16,S}
10 C u1 p0 c0 {4,S} {18,S} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.64358,0.0707662,-1.0475e-05,-3.33341e-08,1.64945e-11,31213.9,32.9345], Tmin=(200,'K'), Tmax=(1001.48,'K')),
            NASAPolynomial(coeffs=[8.93179,0.0565221,-3.10707e-05,8.28841e-09,-8.63484e-13,27691.8,-25.1103], Tmin=(1001.48,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 229,
    label = "C10H9_24",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {5,S} {6,D}
3  C u0 p0 c0 {4,B} {5,S} {7,B}
4  C u0 p0 c0 {3,B} {6,S} {8,B}
5  C u1 p0 c0 {2,S} {3,S} {14,S}
6  C u0 p0 c0 {2,D} {4,S} {19,S}
7  C u0 p0 c0 {3,B} {9,B} {15,S}
8  C u0 p0 c0 {4,B} {10,B} {18,S}
9  C u0 p0 c0 {7,B} {10,B} {16,S}
10 C u0 p0 c0 {8,B} {9,B} {17,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.63825,0.0717632,-1.45503e-05,-2.89857e-08,1.50802e-11,26848.4,35.0191], Tmin=(200,'K'), Tmax=(994.5,'K')),
            NASAPolynomial(coeffs=[8.59318,0.0565474,-3.072e-05,8.07772e-09,-8.29176e-13,23530.8,-20.7336], Tmin=(994.5,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 230,
    label = "C10H9_25",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,D} {6,S}
3  C u1 p0 c0 {1,S} {7,S} {12,S}
4  C u0 p0 c0 {1,S} {8,D} {13,S}
5  C u0 p0 c0 {2,D} {9,S} {16,S}
6  C u0 p0 c0 {2,S} {10,D} {17,S}
7  C u0 p0 c0 {3,S} {9,D} {14,S}
8  C u0 p0 c0 {4,D} {10,S} {19,S}
9  C u0 p0 c0 {5,S} {7,D} {15,S}
10 C u0 p0 c0 {6,D} {8,S} {18,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.34568,0.0653984,2.27492e-06,-4.39775e-08,1.94873e-11,37224.3,31.9046], Tmin=(200,'K'), Tmax=(1009.74,'K')),
            NASAPolynomial(coeffs=[7.78638,0.0593237,-3.3417e-05,9.11046e-09,-9.66156e-13,33845.6,-19.8394], Tmin=(1009.74,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 231,
    label = "C10H9_26",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {5,D}
3  C u0 p0 c0 {2,S} {6,S} {7,D}
4  C u0 p0 c0 {1,S} {8,D} {13,S}
5  C u0 p0 c0 {2,D} {8,S} {18,S}
6  C u1 p0 c0 {3,S} {9,S} {14,S}
7  C u0 p0 c0 {3,D} {10,S} {17,S}
8  C u0 p0 c0 {4,D} {5,S} {19,S}
9  C u0 p0 c0 {6,S} {10,D} {15,S}
10 C u0 p0 c0 {7,S} {9,D} {16,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.73217,0.0714932,-1.06567e-05,-3.39475e-08,1.67926e-11,40242.5,35.3158], Tmin=(200,'K'), Tmax=(1006.09,'K')),
            NASAPolynomial(coeffs=[9.51422,0.0559526,-3.09811e-05,8.3406e-09,-8.76929e-13,36503,-26.3474], Tmin=(1006.09,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 232,
    label = "C10H9_27",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {10,S}
2  C u0 p0 c0 {1,B} {4,B} {12,S}
3  C u0 p0 c0 {1,B} {6,B} {16,S}
4  C u0 p0 c0 {2,B} {5,B} {13,S}
5  C u0 p0 c0 {4,B} {6,B} {14,S}
6  C u0 p0 c0 {3,B} {5,B} {15,S}
7  C u0 p0 c0 {8,S} {9,D} {11,S}
8  C u0 p0 c0 {7,S} {10,D} {17,S}
9  C u0 p0 c0 {7,D} {18,S} {19,S}
10 C u1 p0 c0 {1,S} {8,D}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.12953,0.0833982,-4.48306e-05,-6.69436e-10,6.00122e-12,48825.2,38.4073], Tmin=(200,'K'), Tmax=(999.21,'K')),
            NASAPolynomial(coeffs=[10.1781,0.0531355,-2.79333e-05,7.09343e-09,-7.03912e-13,45416.7,-25.7083], Tmin=(999.21,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 233,
    label = "C10H9_28",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {10,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,B} {5,B}
4  C u0 p0 c0 {3,B} {6,B} {9,S}
5  C u0 p0 c0 {3,B} {8,B} {18,S}
6  C u0 p0 c0 {4,B} {7,B} {15,S}
7  C u0 p0 c0 {6,B} {8,B} {16,S}
8  C u0 p0 c0 {5,B} {7,B} {17,S}
9  C u0 p0 c0 {4,S} {10,D} {19,S}
10 C u1 p0 c0 {2,S} {9,D}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.1213,0.0628844,5.24143e-06,-4.50845e-08,1.95946e-11,43267.3,31.2836], Tmin=(200,'K'), Tmax=(1002.61,'K')),
            NASAPolynomial(coeffs=[6.54861,0.0606442,-3.3836e-05,9.11186e-09,-9.54104e-13,40304,-12.8476], Tmin=(1002.61,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 234,
    label = "C10H9_29",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {4,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {8,S}
3  C u0 p0 c0 {2,B} {5,B} {11,S}
4  C u0 p0 c0 {1,B} {6,B} {14,S}
5  C u0 p0 c0 {3,B} {6,B} {12,S}
6  C u0 p0 c0 {4,B} {5,B} {13,S}
7  C u0 p0 c0 {1,S} {10,D} {15,S}
8  C u1 p0 c0 {2,S} {16,S} {17,S}
9  C u0 p0 c0 {10,D} {18,S} {19,S}
10 C u0 p0 c0 {7,D} {9,D}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.00388,0.0795701,-3.6803e-05,-8.52456e-09,8.71646e-12,47433.5,34.8988], Tmin=(200,'K'), Tmax=(994.76,'K')),
            NASAPolynomial(coeffs=[10.445,0.051292,-2.70044e-05,6.91861e-09,-6.96157e-13,43879.1,-30.511], Tmin=(994.76,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 235,
    label = "C10H9_30",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,B} {5,B}
3  C u0 p0 c0 {2,B} {6,S} {7,B}
4  C u1 p0 c0 {1,S} {8,S} {13,S}
5  C u0 p0 c0 {2,B} {10,B} {19,S}
6  C u0 p0 c0 {3,S} {8,D} {15,S}
7  C u0 p0 c0 {3,B} {9,B} {16,S}
8  C u0 p0 c0 {4,S} {6,D} {14,S}
9  C u0 p0 c0 {7,B} {10,B} {17,S}
10 C u0 p0 c0 {5,B} {9,B} {18,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.22666,0.0640653,3.74604e-06,-4.44408e-08,1.9501e-11,26436.7,31.8839], Tmin=(200,'K'), Tmax=(1006.15,'K')),
            NASAPolynomial(coeffs=[7.14829,0.0599327,-3.35687e-05,9.09021e-09,-9.57547e-13,23275.3,-15.9072], Tmin=(1006.15,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 236,
    label = "C10H9_31",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {10,D}
3  C u0 p0 c0 {2,S} {4,B} {7,B}
4  C u0 p0 c0 {3,B} {5,S} {6,B}
5  C u1 p0 c0 {1,S} {4,S} {13,S}
6  C u0 p0 c0 {4,B} {8,B} {14,S}
7  C u0 p0 c0 {3,B} {9,B} {17,S}
8  C u0 p0 c0 {6,B} {9,B} {15,S}
9  C u0 p0 c0 {7,B} {8,B} {16,S}
10 C u0 p0 c0 {2,D} {18,S} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.61598,0.070364,-9.72737e-06,-3.38727e-08,1.6635e-11,31497.9,33.1826], Tmin=(200,'K'), Tmax=(1001.35,'K')),
            NASAPolynomial(coeffs=[8.81068,0.0566984,-3.11777e-05,8.31811e-09,-8.66579e-13,28006.8,-24.1397], Tmin=(1001.35,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 237,
    label = "C10H9_32",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {6,D}
3  C u1 p0 c0 {1,S} {7,S} {12,S}
4  C u0 p0 c0 {1,S} {8,D} {13,S}
5  C u0 p0 c0 {2,S} {10,D} {17,S}
6  C u0 p0 c0 {2,D} {8,S} {18,S}
7  C u0 p0 c0 {3,S} {9,D} {14,S}
8  C u0 p0 c0 {4,D} {6,S} {19,S}
9  C u0 p0 c0 {7,D} {10,S} {15,S}
10 C u0 p0 c0 {5,D} {9,S} {16,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.46746,0.0673963,-2.22567e-06,-4.03818e-08,1.85112e-11,40738.4,33.2581], Tmin=(200,'K'), Tmax=(1007.57,'K')),
            NASAPolynomial(coeffs=[8.33436,0.0580963,-3.24659e-05,8.79644e-09,-9.28644e-13,37260.1,-21.5631], Tmin=(1007.57,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 238,
    label = "C10H9_33",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {6,S} {12,S}
4  C u0 p0 c0 {1,S} {8,D} {14,S}
5  C u0 p0 c0 {1,S} {9,D} {15,S}
6  C u1 p0 c0 {3,S} {8,S} {13,S}
7  C u0 p0 c0 {2,S} {10,D} {16,S}
8  C u0 p0 c0 {4,D} {6,S} {17,S}
9  C u0 p0 c0 {5,D} {10,S} {18,S}
10 C u0 p0 c0 {7,D} {9,S} {19,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.63458,0.0693938,-5.30495e-06,-3.86128e-08,1.81317e-11,48332.2,34.4557], Tmin=(200,'K'), Tmax=(1011.8,'K')),
            NASAPolynomial(coeffs=[9.30427,0.0566958,-3.17659e-05,8.66033e-09,-9.21219e-13,44555,-26.1731], Tmin=(1011.8,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 239,
    label = "C10H9_34",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {14,S}
4  C u0 p0 c0 {2,B} {7,B} {18,S}
5  C u0 p0 c0 {3,B} {6,B} {15,S}
6  C u0 p0 c0 {5,B} {7,B} {16,S}
7  C u0 p0 c0 {4,B} {6,B} {17,S}
8  C u1 p0 c0 {1,S} {9,S} {13,S}
9  C u0 p0 c0 {8,S} {10,T}
10 C u0 p0 c0 {9,T} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.29887,0.0877399,-5.62895e-05,1.03087e-08,2.36006e-12,49457.9,39.6355], Tmin=(200,'K'), Tmax=(1013.81,'K')),
            NASAPolynomial(coeffs=[11.0223,0.0514668,-2.67165e-05,6.70664e-09,-6.58907e-13,45920,-28.9417], Tmin=(1013.81,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 240,
    label = "C10H9_35",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u1 p0 c0 {1,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {7,D} {12,S}
4  C u0 p0 c0 {1,S} {8,D} {13,S}
5  C u0 p0 c0 {1,S} {9,D} {14,S}
6  C u0 p0 c0 {2,S} {10,D} {15,S}
7  C u0 p0 c0 {3,D} {10,S} {17,S}
8  C u0 p0 c0 {4,D} {9,S} {18,S}
9  C u0 p0 c0 {5,D} {8,S} {19,S}
10 C u0 p0 c0 {6,D} {7,S} {16,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.69478,0.0705552,-8.26009e-06,-3.60892e-08,1.74198e-11,44556.4,33.9004], Tmin=(200,'K'), Tmax=(1009.41,'K')),
            NASAPolynomial(coeffs=[9.54068,0.0559986,-3.11595e-05,8.44546e-09,-8.94261e-13,40761.6,-27.9714], Tmin=(1009.41,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 241,
    label = "C10H9_36",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {5,B} {8,B}
5  C u0 p0 c0 {3,S} {4,B} {7,B}
6  C u1 p0 c0 {1,S} {2,S} {15,S}
7  C u0 p0 c0 {5,B} {9,B} {16,S}
8  C u0 p0 c0 {4,B} {10,B} {19,S}
9  C u0 p0 c0 {7,B} {10,B} {17,S}
10 C u0 p0 c0 {8,B} {9,B} {18,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.21964,0.0631963,7.28015e-06,-4.80047e-08,2.0566e-11,47276.7,32.5503], Tmin=(200,'K'), Tmax=(1014.46,'K')),
            NASAPolynomial(coeffs=[7.32778,0.060451,-3.44342e-05,9.48923e-09,-1.01558e-12,43949.6,-16.66], Tmin=(1014.46,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 242,
    label = "C10H9_37",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {3,B} {4,S} {8,B}
3  C u0 p0 c0 {2,B} {6,S} {7,B}
4  C u1 p0 c0 {1,S} {2,S} {13,S}
5  C u0 p0 c0 {1,S} {6,D} {14,S}
6  C u0 p0 c0 {3,S} {5,D} {15,S}
7  C u0 p0 c0 {3,B} {9,B} {16,S}
8  C u0 p0 c0 {2,B} {10,B} {19,S}
9  C u0 p0 c0 {7,B} {10,B} {17,S}
10 C u0 p0 c0 {8,B} {9,B} {18,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.24846,0.0644711,2.92922e-06,-4.38522e-08,1.93641e-11,28762.8,31.6219], Tmin=(200,'K'), Tmax=(1004.89,'K')),
            NASAPolynomial(coeffs=[7.22265,0.0597969,-3.34494e-05,9.04524e-09,-9.51616e-13,25593.7,-16.5845], Tmin=(1004.89,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 243,
    label = "C10H9_38",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,B} {10,B}
2  C u0 p0 c0 {1,S} {4,D} {13,S}
3  C u0 p0 c0 {1,B} {5,B} {16,S}
4  C u0 p0 c0 {2,D} {7,S} {12,S}
5  C u0 p0 c0 {3,B} {6,B} {15,S}
6  C u0 p0 c0 {5,B} {8,B} {14,S}
7  C u0 p0 c0 {4,S} {9,D} {11,S}
8  C u0 p0 c0 {6,B} {10,B} {17,S}
9  C u0 p0 c0 {7,D} {18,S} {19,S}
10 C u1 p0 c0 {1,B} {8,B}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.93677,0.0791888,-3.43708e-05,-1.03097e-08,9.10827e-12,53728.5,36.8341], Tmin=(200,'K'), Tmax=(992.03,'K')),
            NASAPolynomial(coeffs=[9.36769,0.0546203,-2.89942e-05,7.429e-09,-7.4295e-13,50451.7,-22.8242], Tmin=(992.03,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 244,
    label = "C10H9_39",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,B} {6,B}
3  C u0 p0 c0 {2,B} {5,S} {7,B}
4  C u0 p0 c0 {1,S} {5,D} {12,S}
5  C u0 p0 c0 {3,S} {4,D} {13,S}
6  C u0 p0 c0 {2,B} {9,B} {17,S}
7  C u0 p0 c0 {3,B} {8,B} {14,S}
8  C u0 p0 c0 {7,B} {9,B} {15,S}
9  C u0 p0 c0 {6,B} {8,B} {16,S}
10 C u1 p0 c0 {1,S} {18,S} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.86786,0.0751031,-2.09459e-05,-2.42806e-08,1.38221e-11,38578.4,35.3653], Tmin=(200,'K'), Tmax=(996.99,'K')),
            NASAPolynomial(coeffs=[9.68305,0.0548387,-2.96938e-05,7.8055e-09,-8.02557e-13,34979,-26.8264], Tmin=(996.99,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 245,
    label = "C10H9_40",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,B} {6,B}
3  C u1 p0 c0 {1,S} {7,S} {12,S}
4  C u0 p0 c0 {1,S} {7,D} {13,S}
5  C u0 p0 c0 {2,B} {8,B} {15,S}
6  C u0 p0 c0 {2,B} {10,B} {19,S}
7  C u0 p0 c0 {3,S} {4,D} {14,S}
8  C u0 p0 c0 {5,B} {9,B} {16,S}
9  C u0 p0 c0 {8,B} {10,B} {17,S}
10 C u0 p0 c0 {6,B} {9,B} {18,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.74639,0.0722652,-1.33112e-05,-3.1282e-08,1.59572e-11,48700.6,36.2521], Tmin=(200,'K'), Tmax=(1002.1,'K')),
            NASAPolynomial(coeffs=[9.39571,0.0558249,-3.06661e-05,8.1811e-09,-8.52602e-13,45059.9,-24.5488], Tmin=(1002.1,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 246,
    label = "C10H9_41",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,B} {4,B}
2  C u0 p0 c0 {1,S} {8,D} {12,S}
3  C u0 p0 c0 {1,B} {5,B} {13,S}
4  C u0 p0 c0 {1,B} {7,B} {17,S}
5  C u0 p0 c0 {3,B} {6,B} {14,S}
6  C u0 p0 c0 {5,B} {7,B} {15,S}
7  C u0 p0 c0 {4,B} {6,B} {16,S}
8  C u0 p0 c0 {2,D} {9,S} {11,S}
9  C u0 p0 c0 {8,S} {10,D} {18,S}
10 C u1 p0 c0 {9,D} {19,S}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.07631,0.0813212,-3.86208e-05,-7.0075e-09,8.17082e-12,52982.1,37.7079], Tmin=(200,'K'), Tmax=(994.79,'K')),
            NASAPolynomial(coeffs=[10.0163,0.0536122,-2.83761e-05,7.26114e-09,-7.26213e-13,49541.3,-25.7705], Tmin=(994.79,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 247,
    label = "C10H9_42",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {5,D}
3  C u1 p0 c0 {2,S} {6,S} {7,S}
4  C u0 p0 c0 {1,S} {6,D} {13,S}
5  C u0 p0 c0 {2,D} {9,S} {16,S}
6  C u0 p0 c0 {3,S} {4,D} {17,S}
7  C u0 p0 c0 {3,S} {10,D} {18,S}
8  C u0 p0 c0 {9,D} {10,S} {14,S}
9  C u0 p0 c0 {5,S} {8,D} {15,S}
10 C u0 p0 c0 {7,D} {8,S} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.69449,0.0716831,-1.24575e-05,-3.1706e-08,1.603e-11,37388.5,33.4174], Tmin=(200,'K'), Tmax=(1000.46,'K')),
            NASAPolynomial(coeffs=[9.07218,0.0563045,-3.08838e-05,8.21578e-09,-8.53535e-13,33849.5,-25.4507], Tmin=(1000.46,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 248,
    label = "C10H9_43",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {3,B} {6,B}
3  C u0 p0 c0 {2,B} {4,S} {7,B}
4  C u1 p0 c0 {1,S} {3,S} {12,S}
5  C u0 p0 c0 {1,S} {10,D} {13,S}
6  C u0 p0 c0 {2,B} {9,B} {17,S}
7  C u0 p0 c0 {3,B} {8,B} {14,S}
8  C u0 p0 c0 {7,B} {9,B} {15,S}
9  C u0 p0 c0 {6,B} {8,B} {16,S}
10 C u0 p0 c0 {5,D} {18,S} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.85429,0.0750645,-2.1103e-05,-2.39848e-08,1.37028e-11,50991.1,35.9431], Tmin=(200,'K'), Tmax=(996.07,'K')),
            NASAPolynomial(coeffs=[9.54999,0.055051,-2.97927e-05,7.81911e-09,-8.02254e-13,47440.1,-25.4516], Tmin=(996.07,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 249,
    label = "C10H9_44",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {3,S} {4,D} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,D}
4  C u0 p0 c0 {1,S} {2,D} {14,S}
5  C u0 p0 c0 {1,S} {6,D} {13,S}
6  C u0 p0 c0 {2,S} {5,D} {19,S}
7  C u0 p0 c0 {3,S} {10,D} {17,S}
8  C u0 p0 c0 {3,D} {9,S} {18,S}
9  C u1 p0 c0 {8,S} {10,S} {15,S}
10 C u0 p0 c0 {7,D} {9,S} {16,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.80613,0.0726913,-1.32148e-05,-3.19102e-08,1.6226e-11,42278.6,35.6811], Tmin=(200,'K'), Tmax=(1005.56,'K')),
            NASAPolynomial(coeffs=[9.81428,0.0553969,-3.05718e-05,8.20806e-09,-8.61281e-13,38479,-27.7178], Tmin=(1005.56,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 250,
    label = "C10H9_45",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {6,D}
3  C u0 p0 c0 {1,S} {7,D} {12,S}
4  C u0 p0 c0 {1,S} {8,D} {13,S}
5  C u1 p0 c0 {2,S} {9,S} {14,S}
6  C u0 p0 c0 {2,D} {10,S} {17,S}
7  C u0 p0 c0 {3,D} {8,S} {18,S}
8  C u0 p0 c0 {4,D} {7,S} {19,S}
9  C u0 p0 c0 {5,S} {10,D} {15,S}
10 C u0 p0 c0 {6,S} {9,D} {16,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.89271,0.0737119,-1.47519e-05,-3.10697e-08,1.60593e-11,48020.3,36.6824], Tmin=(200,'K'), Tmax=(1007.76,'K')),
            NASAPolynomial(coeffs=[10.3255,0.0546533,-3.02007e-05,8.13633e-09,-8.57429e-13,44062.9,-29.7744], Tmin=(1007.76,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 251,
    label = "C10H9_46",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {4,D} {6,S}
3  C u0 p0 c0 {2,S} {5,D} {7,S}
4  C u0 p0 c0 {1,S} {2,D} {12,S}
5  C u0 p0 c0 {1,S} {3,D} {13,S}
6  C u0 p0 c0 {2,S} {8,D} {14,S}
7  C u0 p0 c0 {3,S} {9,D} {17,S}
8  C u0 p0 c0 {6,D} {9,S} {15,S}
9  C u0 p0 c0 {7,D} {8,S} {16,S}
10 C u1 p0 c0 {1,S} {18,S} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.09744,0.079201,-3.01928e-05,-1.64776e-08,1.1511e-11,49957.6,35.7043], Tmin=(200,'K'), Tmax=(996.98,'K')),
            NASAPolynomial(coeffs=[10.5682,0.0532491,-2.85564e-05,7.44342e-09,-7.60169e-13,46196.4,-31.5589], Tmin=(996.98,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 252,
    label = "C10H9_5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,B} {6,B}
4  C u0 p0 c0 {1,S} {2,S} {10,D}
5  C u0 p0 c0 {3,B} {7,B} {14,S}
6  C u0 p0 c0 {3,B} {9,B} {18,S}
7  C u0 p0 c0 {5,B} {8,B} {15,S}
8  C u0 p0 c0 {7,B} {9,B} {16,S}
9  C u0 p0 c0 {6,B} {8,B} {17,S}
10 C u1 p0 c0 {4,D} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.08695,0.0791947,-3.05725e-05,-1.59495e-08,1.13152e-11,60847.6,37.7267], Tmin=(200,'K'), Tmax=(996.56,'K')),
            NASAPolynomial(coeffs=[10.5093,0.0532218,-2.84854e-05,7.41087e-09,-7.55569e-13,57116.2,-29.1251], Tmin=(996.56,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 253,
    label = "C10H9_6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {4,S}
2  C u0 p0 c0 {1,B} {5,B} {12,S}
3  C u0 p0 c0 {1,B} {7,B} {16,S}
4  C u0 p0 c0 {1,S} {8,D} {11,S}
5  C u0 p0 c0 {2,B} {6,B} {13,S}
6  C u0 p0 c0 {5,B} {7,B} {14,S}
7  C u0 p0 c0 {3,B} {6,B} {15,S}
8  C u0 p0 c0 {4,D} {10,S} {17,S}
9  C u0 p0 c0 {10,D} {18,S} {19,S}
10 C u1 p0 c0 {8,S} {9,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.16901,0.0834542,-4.40724e-05,-1.91257e-09,6.51955e-12,44786.7,37.3498], Tmin=(200,'K'), Tmax=(998.07,'K')),
            NASAPolynomial(coeffs=[10.396,0.0528686,-2.78204e-05,7.08036e-09,-7.04808e-13,41293.8,-28.1783], Tmin=(998.07,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 254,
    label = "C10H9_7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,B} {8,B}
4  C u0 p0 c0 {3,B} {5,B} {17,S}
5  C u0 p0 c0 {4,B} {6,B} {16,S}
6  C u0 p0 c0 {5,B} {7,B} {15,S}
7  C u0 p0 c0 {6,B} {8,B} {18,S}
8  C u1 p0 c0 {3,B} {7,B}
9  C u0 p0 c0 {2,S} {10,T}
10 C u0 p0 c0 {9,T} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.07837,0.0833454,-4.61086e-05,1.26423e-09,5.22963e-12,62731.5,38.3085], Tmin=(200,'K'), Tmax=(1000.87,'K')),
            NASAPolynomial(coeffs=[9.97661,0.0531511,-2.78087e-05,7.0274e-09,-6.94121e-13,59417.6,-24.3601], Tmin=(1000.87,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 255,
    label = "C10H9_8",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u0 p0 c0 {2,S} {5,B} {6,B}
4  C u0 p0 c0 {1,S} {2,D} {12,S}
5  C u0 p0 c0 {3,B} {7,B} {13,S}
6  C u0 p0 c0 {3,B} {9,B} {17,S}
7  C u0 p0 c0 {5,B} {8,B} {14,S}
8  C u0 p0 c0 {7,B} {9,B} {15,S}
9  C u0 p0 c0 {6,B} {8,B} {16,S}
10 C u1 p0 c0 {1,S} {18,S} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.39964,0.0868969,-5.08418e-05,3.23868e-09,5.08782e-12,59976.2,38.4678], Tmin=(200,'K'), Tmax=(1002.88,'K')),
            NASAPolynomial(coeffs=[11.504,0.0511208,-2.67654e-05,6.80004e-09,-6.77466e-13,56197.9,-33.5833], Tmin=(1002.88,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 256,
    label = "C10H9_9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {4,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {8,S}
3  C u0 p0 c0 {2,B} {5,B} {11,S}
4  C u0 p0 c0 {1,B} {6,B} {14,S}
5  C u0 p0 c0 {3,B} {6,B} {12,S}
6  C u0 p0 c0 {4,B} {5,B} {13,S}
7  C u0 p0 c0 {1,S} {9,D} {15,S}
8  C u0 p0 c0 {2,S} {10,D} {16,S}
9  C u0 p0 c0 {7,D} {17,S} {18,S}
10 C u1 p0 c0 {8,D} {19,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.23577,0.0849934,-4.79818e-05,1.74303e-09,5.32754e-12,53910.6,37.2013], Tmin=(200,'K'), Tmax=(1001.47,'K')),
            NASAPolynomial(coeffs=[10.6851,0.052333,-2.74416e-05,6.96084e-09,-6.90829e-13,50372.5,-29.8969], Tmin=(1001.47,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 257,
    label = "C11H10_14",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,B} {5,B}
3  C u0 p0 c0 {2,B} {4,B} {8,B}
4  C u0 p0 c0 {3,B} {6,B} {7,B}
5  C u0 p0 c0 {2,B} {9,B} {15,S}
6  C u0 p0 c0 {4,B} {9,B} {17,S}
7  C u0 p0 c0 {4,B} {10,B} {18,S}
8  C u0 p0 c0 {3,B} {11,B} {21,S}
9  C u0 p0 c0 {5,B} {6,B} {16,S}
10 C u0 p0 c0 {7,B} {11,B} {19,S}
11 C u0 p0 c0 {8,B} {10,B} {20,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.98789,0.0753641,-6.60784e-06,-3.9783e-08,1.88818e-11,10908.6,34.5458], Tmin=(200,'K'), Tmax=(993.62,'K')),
            NASAPolynomial(coeffs=[7.79262,0.0653073,-3.56831e-05,9.41947e-09,-9.69129e-13,7517.83,-19.8592], Tmin=(993.62,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 258,
    label = "C11H11_1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {12,S}
2  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {4,B} {6,B}
4  C u0 p0 c0 {3,B} {7,S} {8,B}
5  C u1 p0 c0 {1,S} {9,S} {16,S}
6  C u0 p0 c0 {3,B} {11,B} {22,S}
7  C u0 p0 c0 {4,S} {9,D} {18,S}
8  C u0 p0 c0 {4,B} {10,B} {19,S}
9  C u0 p0 c0 {5,S} {7,D} {17,S}
10 C u0 p0 c0 {8,B} {11,B} {20,S}
11 C u0 p0 c0 {6,B} {10,B} {21,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.3895,0.0808362,-1.06089e-05,-3.87865e-08,1.89832e-11,22825.1,38.0428], Tmin=(200,'K'), Tmax=(992.93,'K')),
            NASAPolynomial(coeffs=[8.41836,0.0677383,-3.6809e-05,9.68062e-09,-9.93753e-13,19178.2,-21.5788], Tmin=(992.93,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 259,
    label = "C11H11_2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
2  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
3  C u1 p0 c0 {1,S} {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,B} {9,B}
5  C u0 p0 c0 {4,B} {7,S} {8,B}
6  C u0 p0 c0 {1,S} {7,D} {17,S}
7  C u0 p0 c0 {5,S} {6,D} {18,S}
8  C u0 p0 c0 {5,B} {10,B} {19,S}
9  C u0 p0 c0 {4,B} {11,B} {22,S}
10 C u0 p0 c0 {8,B} {11,B} {20,S}
11 C u0 p0 c0 {9,B} {10,B} {21,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.43514,0.0829903,-1.71945e-05,-3.21946e-08,1.68519e-11,24305.2,38.619], Tmin=(200,'K'), Tmax=(986.34,'K')),
            NASAPolynomial(coeffs=[8.13683,0.0679271,-3.658e-05,9.49432e-09,-9.60274e-13,20866.9,-19.0968], Tmin=(986.34,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 260,
    label = "C11H11_3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
2  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
3  C u0 p0 c0 {1,S} {5,B} {8,B}
4  C u0 p0 c0 {2,S} {5,S} {7,D}
5  C u0 p0 c0 {3,B} {4,S} {9,B}
6  C u1 p0 c0 {1,S} {7,S} {17,S}
7  C u0 p0 c0 {4,D} {6,S} {18,S}
8  C u0 p0 c0 {3,B} {10,B} {19,S}
9  C u0 p0 c0 {5,B} {11,B} {22,S}
10 C u0 p0 c0 {8,B} {11,B} {20,S}
11 C u0 p0 c0 {9,B} {10,B} {21,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.39551,0.0820222,-1.46997e-05,-3.45063e-08,1.75782e-11,21956.9,37.768], Tmin=(200,'K'), Tmax=(987.39,'K')),
            NASAPolynomial(coeffs=[8.06994,0.0680805,-3.67479e-05,9.56708e-09,-9.70836e-13,18503.1,-19.6129], Tmin=(987.39,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 261,
    label = "C11H11_4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {7,S} {12,S} {13,S}
2  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {6,D}
4  C u0 p0 c0 {3,S} {5,B} {9,B}
5  C u0 p0 c0 {4,B} {7,S} {8,B}
6  C u0 p0 c0 {1,S} {3,D} {18,S}
7  C u1 p0 c0 {1,S} {5,S} {17,S}
8  C u0 p0 c0 {5,B} {10,B} {19,S}
9  C u0 p0 c0 {4,B} {11,B} {22,S}
10 C u0 p0 c0 {8,B} {11,B} {20,S}
11 C u0 p0 c0 {9,B} {10,B} {21,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.45596,0.0828539,-1.62569e-05,-3.338e-08,1.7279e-11,24236.8,37.2914], Tmin=(200,'K'), Tmax=(988.32,'K')),
            NASAPolynomial(coeffs=[8.37595,0.067585,-3.64454e-05,9.48771e-09,-9.63376e-13,20700.4,-21.8984], Tmin=(988.32,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 262,
    label = "C11H12_37",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {1,S} {5,B} {8,B}
5  C u0 p0 c0 {4,B} {7,S} {9,B}
6  C u0 p0 c0 {1,S} {7,D} {18,S}
7  C u0 p0 c0 {5,S} {6,D} {19,S}
8  C u0 p0 c0 {4,B} {11,B} {23,S}
9  C u0 p0 c0 {5,B} {10,B} {20,S}
10 C u0 p0 c0 {9,B} {11,B} {21,S}
11 C u0 p0 c0 {8,B} {10,B} {22,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.38417,0.0807964,-5.23771e-06,-4.40369e-08,2.06322e-11,10361.7,38.3054], Tmin=(200,'K'), Tmax=(987.23,'K')),
            NASAPolynomial(coeffs=[7.14425,0.0727,-3.92931e-05,1.02647e-08,-1.04612e-12,6993.51,-15.0714], Tmin=(987.23,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 263,
    label = "C11H12_38",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {12,S} {13,S}
2  C u0 p0 c0 {5,S} {7,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {1,S} {6,S} {7,D}
5  C u0 p0 c0 {2,S} {6,B} {8,B}
6  C u0 p0 c0 {4,S} {5,B} {9,B}
7  C u0 p0 c0 {2,S} {4,D} {19,S}
8  C u0 p0 c0 {5,B} {10,B} {20,S}
9  C u0 p0 c0 {6,B} {11,B} {23,S}
10 C u0 p0 c0 {8,B} {11,B} {21,S}
11 C u0 p0 c0 {9,B} {10,B} {22,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.42369,0.082118,-9.10871e-06,-4.02936e-08,1.9453e-11,8975.88,37.7455], Tmin=(200,'K'), Tmax=(983.68,'K')),
            NASAPolynomial(coeffs=[7.11338,0.0725217,-3.89794e-05,1.0112e-08,-1.02303e-12,5687.59,-15.2856], Tmin=(983.68,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 264,
    label = "C11H12_39",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {1,S} {6,B} {8,B}
5  C u0 p0 c0 {3,S} {6,S} {7,D}
6  C u0 p0 c0 {4,B} {5,S} {9,B}
7  C u0 p0 c0 {2,S} {5,D} {19,S}
8  C u0 p0 c0 {4,B} {10,B} {20,S}
9  C u0 p0 c0 {6,B} {11,B} {23,S}
10 C u0 p0 c0 {8,B} {11,B} {21,S}
11 C u0 p0 c0 {9,B} {10,B} {22,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.25375,0.0791485,-2.5185e-06,-4.57577e-08,2.10415e-11,7887.16,36.0404], Tmin=(200,'K'), Tmax=(984.6,'K')),
            NASAPolynomial(coeffs=[6.46526,0.0736727,-3.97974e-05,1.03735e-08,-1.05399e-12,4718.69,-13.2597], Tmin=(984.6,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 265,
    label = "C11H12_40",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {1,S} {5,B} {8,B}
5  C u0 p0 c0 {4,B} {7,S} {9,B}
6  C u0 p0 c0 {2,S} {7,D} {18,S}
7  C u0 p0 c0 {5,S} {6,D} {19,S}
8  C u0 p0 c0 {4,B} {11,B} {23,S}
9  C u0 p0 c0 {5,B} {10,B} {20,S}
10 C u0 p0 c0 {9,B} {11,B} {21,S}
11 C u0 p0 c0 {8,B} {10,B} {22,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.2358,0.0782058,5.05019e-07,-4.87517e-08,2.19778e-11,8486.2,36.6304], Tmin=(200,'K'), Tmax=(988.93,'K')),
            NASAPolynomial(coeffs=[6.596,0.0737105,-4.00423e-05,1.05134e-08,-1.07647e-12,5212.42,-13.6], Tmin=(988.93,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 266,
    label = "C11H13_1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {6,B} {8,B}
6  C u0 p0 c0 {5,B} {7,S} {9,B}
7  C u1 p0 c0 {3,S} {6,S} {20,S}
8  C u0 p0 c0 {5,B} {11,B} {24,S}
9  C u0 p0 c0 {6,B} {10,B} {21,S}
10 C u0 p0 c0 {9,B} {11,B} {22,S}
11 C u0 p0 c0 {8,B} {10,B} {23,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.71478,0.0859439,-9.8664e-06,-4.173e-08,2.02081e-11,15625.4,41.0131], Tmin=(200,'K'), Tmax=(983.03,'K')),
            NASAPolynomial(coeffs=[7.23869,0.0757748,-4.06332e-05,1.0524e-08,-1.06359e-12,12202.9,-14.2906], Tmin=(983.03,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 267,
    label = "C11H13_2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {6,S} {16,S} {17,S}
3  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
5  C u1 p0 c0 {1,S} {3,S} {7,S}
6  C u0 p0 c0 {2,S} {7,B} {8,B}
7  C u0 p0 c0 {5,S} {6,B} {9,B}
8  C u0 p0 c0 {6,B} {10,B} {21,S}
9  C u0 p0 c0 {7,B} {11,B} {24,S}
10 C u0 p0 c0 {8,B} {11,B} {22,S}
11 C u0 p0 c0 {9,B} {10,B} {23,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.67303,0.086246,-1.2015e-05,-3.90529e-08,1.92536e-11,14549.3,41.657], Tmin=(200,'K'), Tmax=(979.09,'K')),
            NASAPolynomial(coeffs=[6.81121,0.0762434,-4.07286e-05,1.04843e-08,-1.05184e-12,11314.4,-10.9344], Tmin=(979.09,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 268,
    label = "C11H13_3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {6,S} {16,S} {17,S}
4  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
5  C u1 p0 c0 {2,S} {4,S} {7,S}
6  C u0 p0 c0 {3,S} {7,B} {8,B}
7  C u0 p0 c0 {5,S} {6,B} {9,B}
8  C u0 p0 c0 {6,B} {10,B} {21,S}
9  C u0 p0 c0 {7,B} {11,B} {24,S}
10 C u0 p0 c0 {8,B} {11,B} {22,S}
11 C u0 p0 c0 {9,B} {10,B} {23,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.53322,0.0835227,-5.50897e-06,-4.47518e-08,2.09858e-11,12739.3,39.3149], Tmin=(200,'K'), Tmax=(979.97,'K')),
            NASAPolynomial(coeffs=[6.31184,0.0772128,-4.14539e-05,1.07246e-08,-1.08107e-12,9575.09,-10.4776], Tmin=(979.97,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 269,
    label = "C11H13_4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {7,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {6,B} {8,B}
6  C u0 p0 c0 {5,B} {7,S} {9,B}
7  C u1 p0 c0 {3,S} {6,S} {20,S}
8  C u0 p0 c0 {5,B} {11,B} {24,S}
9  C u0 p0 c0 {6,B} {10,B} {21,S}
10 C u0 p0 c0 {9,B} {11,B} {22,S}
11 C u0 p0 c0 {8,B} {10,B} {23,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.54252,0.0827043,-2.36935e-06,-4.81259e-08,2.20979e-11,13679.5,38.6271], Tmin=(200,'K'), Tmax=(985.16,'K')),
            NASAPolynomial(coeffs=[6.65659,0.0768715,-4.14775e-05,1.08137e-08,-1.09988e-12,10337.5,-13.3783], Tmin=(985.16,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 270,
    label = "C11H14_71",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {15,S} {16,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {7,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {7,B} {9,B}
7  C u0 p0 c0 {4,S} {6,B} {8,B}
8  C u0 p0 c0 {7,B} {10,B} {22,S}
9  C u0 p0 c0 {6,B} {11,B} {25,S}
10 C u0 p0 c0 {8,B} {11,B} {23,S}
11 C u0 p0 c0 {9,B} {10,B} {24,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.48385,0.0816732,5.27769e-06,-5.53284e-08,2.43281e-11,-2432.9,39.2732], Tmin=(200,'K'), Tmax=(980.65,'K')),
            NASAPolynomial(coeffs=[5.23387,0.0821032,-4.41897e-05,1.14827e-08,-1.16349e-12,-5480.91,-5.63269], Tmin=(980.65,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 271,
    label = "C11H14_72",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {7,B} {9,B}
7  C u0 p0 c0 {4,S} {6,B} {8,B}
8  C u0 p0 c0 {7,B} {10,B} {22,S}
9  C u0 p0 c0 {6,B} {11,B} {25,S}
10 C u0 p0 c0 {8,B} {11,B} {23,S}
11 C u0 p0 c0 {9,B} {10,B} {24,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.32128,0.0788639,1.14765e-05,-6.03605e-08,2.57419e-11,-3693.02,37.7999], Tmin=(200,'K'), Tmax=(982.81,'K')),
            NASAPolynomial(coeffs=[4.60587,0.0832937,-4.50753e-05,1.17749e-08,-1.19885e-12,-6630.18,-3.515], Tmin=(982.81,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 272,
    label = "C11H15_1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {12,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {16,S} {17,S}
4  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {20,S} {21,S} {22,S}
7  C u0 p0 c0 {2,S} {5,S} {9,D}
8  C u1 p0 c0 {2,S} {10,S} {23,S}
9  C u0 p0 c0 {7,D} {11,S} {24,S}
10 C u0 p0 c0 {8,S} {11,D} {26,S}
11 C u0 p0 c0 {9,S} {10,D} {25,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.921,0.0878387,-2.74101e-07,-5.3005e-08,2.40346e-11,14746.9,42.6796], Tmin=(200,'K'), Tmax=(979.89,'K')),
            NASAPolynomial(coeffs=[5.94519,0.0844196,-4.52094e-05,1.16994e-08,-1.18175e-12,11435.9,-7.94317], Tmin=(979.89,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 273,
    label = "C11H15_2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {12,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {13,S}
3  C u0 p0 c0 {1,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,S} {16,S} {17,S}
5  C u0 p0 c0 {4,S} {7,S} {18,S} {19,S}
6  C u0 p0 c0 {1,S} {20,S} {21,S} {22,S}
7  C u0 p0 c0 {2,S} {5,S} {9,D}
8  C u1 p0 c0 {2,S} {10,S} {23,S}
9  C u0 p0 c0 {7,D} {11,S} {24,S}
10 C u0 p0 c0 {8,S} {11,D} {26,S}
11 C u0 p0 c0 {9,S} {10,D} {25,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.74361,0.0844399,7.6718e-06,-5.97431e-08,2.59884e-11,9908.71,40.2359], Tmin=(200,'K'), Tmax=(983.65,'K')),
            NASAPolynomial(coeffs=[5.36467,0.0856121,-4.61839e-05,1.20468e-08,-1.22633e-12,6661.72,-7.14477], Tmin=(983.65,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 274,
    label = "C11H16_83",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {10,S} {11,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  C u0 p0 c0 {1,S} {10,D} {24,S}
9  C u0 p0 c0 {1,S} {11,D} {27,S}
10 C u0 p0 c0 {6,S} {8,D} {25,S}
11 C u0 p0 c0 {6,S} {9,D} {26,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {11,S}
27 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.37181,0.0978593,-2.03168e-05,-3.51025e-08,1.84288e-11,11665.1,45.1422], Tmin=(200,'K'), Tmax=(971.87,'K')),
            NASAPolynomial(coeffs=[6.2819,0.0860083,-4.50585e-05,1.13883e-08,-1.12359e-12,8471.96,-7.93023], Tmin=(971.87,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 275,
    label = "C11H16_84",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {9,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  C u0 p0 c0 {1,S} {10,D} {24,S}
9  C u0 p0 c0 {6,S} {11,D} {25,S}
10 C u0 p0 c0 {8,D} {11,S} {26,S}
11 C u0 p0 c0 {9,D} {10,S} {27,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.38445,0.0975404,-1.88921e-05,-3.67919e-08,1.90476e-11,11959.8,44.9131], Tmin=(200,'K'), Tmax=(972.25,'K')),
            NASAPolynomial(coeffs=[6.40229,0.0858845,-4.50463e-05,1.14062e-08,-1.12786e-12,8704.65,-8.98045], Tmin=(972.25,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 276,
    label = "C11H16_85",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {12,S}
3  C u0 p0 c0 {1,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {3,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {10,S} {11,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  C u0 p0 c0 {1,S} {10,D} {24,S}
9  C u0 p0 c0 {1,S} {11,D} {27,S}
10 C u0 p0 c0 {6,S} {8,D} {25,S}
11 C u0 p0 c0 {6,S} {9,D} {26,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {11,S}
27 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.16887,0.0927608,-6.73216e-06,-4.79917e-08,2.2611e-11,10538.4,43.4866], Tmin=(200,'K'), Tmax=(972.13,'K')),
            NASAPolynomial(coeffs=[5.63238,0.0874532,-4.62316e-05,1.18003e-08,-1.17594e-12,7366.82,-6.2369], Tmin=(972.13,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 277,
    label = "C11H16_86",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {12,S}
3  C u0 p0 c0 {1,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {3,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {9,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  C u0 p0 c0 {1,S} {10,D} {24,S}
9  C u0 p0 c0 {6,S} {11,D} {25,S}
10 C u0 p0 c0 {8,D} {11,S} {26,S}
11 C u0 p0 c0 {9,D} {10,S} {27,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.19258,0.0928191,-6.35179e-06,-4.86269e-08,2.28606e-11,10631.4,43.1219], Tmin=(200,'K'), Tmax=(973.31,'K')),
            NASAPolynomial(coeffs=[5.8103,0.0872356,-4.61618e-05,1.18023e-08,-1.17854e-12,7390.87,-7.71259], Tmin=(973.31,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 278,
    label = "C11H16_87",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {4,S} {15,S} {16,S}
6  C u0 p0 c0 {10,S} {11,S} {19,S} {20,S}
7  C u0 p0 c0 {2,S} {21,S} {22,S} {23,S}
8  C u0 p0 c0 {1,S} {10,D} {24,S}
9  C u0 p0 c0 {1,S} {11,D} {27,S}
10 C u0 p0 c0 {6,S} {8,D} {25,S}
11 C u0 p0 c0 {6,S} {9,D} {26,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {11,S}
27 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.93477,0.0880778,4.37066e-06,-5.7688e-08,2.55417e-11,1537.16,41.7597], Tmin=(200,'K'), Tmax=(975.01,'K')),
            NASAPolynomial(coeffs=[4.87113,0.0888693,-4.73313e-05,1.2182e-08,-1.22424e-12,-1544.8,-3.70059], Tmin=(975.01,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 279,
    label = "C11H16_88",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {4,S} {15,S} {16,S}
6  C u0 p0 c0 {1,S} {9,S} {19,S} {20,S}
7  C u0 p0 c0 {2,S} {21,S} {22,S} {23,S}
8  C u0 p0 c0 {1,S} {10,D} {24,S}
9  C u0 p0 c0 {6,S} {11,D} {25,S}
10 C u0 p0 c0 {8,D} {11,S} {26,S}
11 C u0 p0 c0 {9,D} {10,S} {27,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.97588,0.088462,4.05517e-06,-5.77481e-08,2.56183e-11,1785.64,41.4869], Tmin=(200,'K'), Tmax=(976.38,'K')),
            NASAPolynomial(coeffs=[5.13196,0.0885364,-4.72029e-05,1.21715e-08,-1.22592e-12,-1384.43,-5.56095], Tmin=(976.38,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 280,
    label = "C11H16_89",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {20,S} {21,S}
4  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
7  C u0 p0 c0 {10,S} {11,S} {22,S} {23,S}
8  C u0 p0 c0 {1,S} {10,D} {24,S}
9  C u0 p0 c0 {1,S} {11,D} {27,S}
10 C u0 p0 c0 {7,S} {8,D} {25,S}
11 C u0 p0 c0 {7,S} {9,D} {26,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {11,S}
27 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.57059,0.0812181,2.04129e-05,-7.11275e-08,2.93641e-11,597.442,38.1099], Tmin=(200,'K'), Tmax=(983.71,'K')),
            NASAPolynomial(coeffs=[3.56861,0.0917118,-4.96543e-05,1.29981e-08,-1.32731e-12,-2325.98,-0.127275], Tmin=(983.71,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 281,
    label = "C11H16_90",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {20,S} {21,S}
4  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
7  C u0 p0 c0 {1,S} {9,S} {22,S} {23,S}
8  C u0 p0 c0 {1,S} {10,D} {24,S}
9  C u0 p0 c0 {7,S} {11,D} {25,S}
10 C u0 p0 c0 {8,D} {11,S} {26,S}
11 C u0 p0 c0 {9,D} {10,S} {27,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.59649,0.0814232,2.03824e-05,-7.13246e-08,2.94518e-11,131.123,37.4742], Tmin=(200,'K'), Tmax=(985.13,'K')),
            NASAPolynomial(coeffs=[3.74483,0.0915435,-4.96423e-05,1.30231e-08,-1.33295e-12,-2858.76,-1.85774], Tmin=(985.13,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 282,
    label = "C12H12_23",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
3  C u0 p0 c0 {1,S} {4,B} {6,B}
4  C u0 p0 c0 {3,B} {5,B} {9,B}
5  C u0 p0 c0 {4,B} {7,B} {8,B}
6  C u0 p0 c0 {3,B} {10,B} {18,S}
7  C u0 p0 c0 {5,B} {10,B} {20,S}
8  C u0 p0 c0 {5,B} {11,B} {21,S}
9  C u0 p0 c0 {4,B} {12,B} {24,S}
10 C u0 p0 c0 {6,B} {7,B} {19,S}
11 C u0 p0 c0 {8,B} {12,B} {22,S}
12 C u0 p0 c0 {9,B} {11,B} {23,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {12,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.94188,0.0888997,-1.40653e-05,-3.93466e-08,1.96872e-11,8225.57,39.8334], Tmin=(200,'K'), Tmax=(986.5,'K')),
            NASAPolynomial(coeffs=[8.14176,0.0751207,-4.04966e-05,1.05358e-08,-1.06872e-12,4522.43,-21.1735], Tmin=(986.5,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 283,
    label = "C12H13_1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
4  C u0 p0 c0 {1,S} {5,B} {7,B}
5  C u0 p0 c0 {4,B} {8,S} {9,B}
6  C u1 p0 c0 {1,S} {10,S} {19,S}
7  C u0 p0 c0 {4,B} {12,B} {25,S}
8  C u0 p0 c0 {5,S} {10,D} {21,S}
9  C u0 p0 c0 {5,B} {11,B} {22,S}
10 C u0 p0 c0 {6,S} {8,D} {20,S}
11 C u0 p0 c0 {9,B} {12,B} {23,S}
12 C u0 p0 c0 {7,B} {11,B} {24,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.36415,0.0949882,-1.97832e-05,-3.66578e-08,1.92264e-11,19984.2,43.3653], Tmin=(200,'K'), Tmax=(986,'K')),
            NASAPolynomial(coeffs=[8.77958,0.0775136,-4.15605e-05,1.07651e-08,-1.08827e-12,16044.1,-22.8862], Tmin=(986,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 284,
    label = "C12H13_2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {13,S} {14,S}
2  C u0 p0 c0 {4,S} {7,S} {15,S} {16,S}
3  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
4  C u1 p0 c0 {1,S} {2,S} {5,S}
5  C u0 p0 c0 {4,S} {6,B} {10,B}
6  C u0 p0 c0 {5,B} {8,S} {9,B}
7  C u0 p0 c0 {2,S} {8,D} {20,S}
8  C u0 p0 c0 {6,S} {7,D} {21,S}
9  C u0 p0 c0 {6,B} {11,B} {22,S}
10 C u0 p0 c0 {5,B} {12,B} {25,S}
11 C u0 p0 c0 {9,B} {12,B} {23,S}
12 C u0 p0 c0 {10,B} {11,B} {24,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.8754,0.0873812,-6.46837e-06,-4.65581e-08,2.19369e-11,22156.4,39.7563], Tmin=(200,'K'), Tmax=(984.82,'K')),
            NASAPolynomial(coeffs=[7.14785,0.0788755,-4.25657e-05,1.10834e-08,-1.12503e-12,18620.4,-16.3758], Tmin=(984.82,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 285,
    label = "C12H13_3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {13,S} {14,S}
2  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
3  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
4  C u0 p0 c0 {1,S} {6,S} {8,D}
5  C u0 p0 c0 {2,S} {6,B} {9,B}
6  C u0 p0 c0 {4,S} {5,B} {10,B}
7  C u1 p0 c0 {2,S} {8,S} {20,S}
8  C u0 p0 c0 {4,D} {7,S} {21,S}
9  C u0 p0 c0 {5,B} {11,B} {22,S}
10 C u0 p0 c0 {6,B} {12,B} {25,S}
11 C u0 p0 c0 {9,B} {12,B} {23,S}
12 C u0 p0 c0 {10,B} {11,B} {24,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.66674,0.0973937,-2.50997e-05,-3.28577e-08,1.86029e-11,19291.6,44.5689], Tmin=(200,'K'), Tmax=(954.47,'K')),
            NASAPolynomial(coeffs=[7.09523,0.0807204,-4.35732e-05,1.12506e-08,-1.12369e-12,15942.3,-13.6333], Tmin=(954.47,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 286,
    label = "C12H13_4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {13,S} {14,S}
2  C u0 p0 c0 {7,S} {8,S} {15,S} {16,S}
3  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
4  C u0 p0 c0 {1,S} {5,S} {7,D}
5  C u0 p0 c0 {4,S} {6,B} {10,B}
6  C u0 p0 c0 {5,B} {8,S} {9,B}
7  C u0 p0 c0 {2,S} {4,D} {21,S}
8  C u1 p0 c0 {2,S} {6,S} {20,S}
9  C u0 p0 c0 {6,B} {11,B} {22,S}
10 C u0 p0 c0 {5,B} {12,B} {25,S}
11 C u0 p0 c0 {9,B} {12,B} {23,S}
12 C u0 p0 c0 {10,B} {11,B} {24,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.98366,0.100177,-3.16028e-05,-2.66269e-08,1.64459e-11,21790.5,44.9875], Tmin=(200,'K'), Tmax=(961.16,'K')),
            NASAPolynomial(coeffs=[7.45086,0.0800742,-4.31223e-05,1.11127e-08,-1.10816e-12,18322.9,-16.3286], Tmin=(961.16,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 287,
    label = "C12H14_58",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {6,B} {9,B}
6  C u0 p0 c0 {5,B} {8,S} {10,B}
7  C u0 p0 c0 {1,S} {8,D} {21,S}
8  C u0 p0 c0 {6,S} {7,D} {22,S}
9  C u0 p0 c0 {5,B} {12,B} {26,S}
10 C u0 p0 c0 {6,B} {11,B} {23,S}
11 C u0 p0 c0 {10,B} {12,B} {24,S}
12 C u0 p0 c0 {9,B} {11,B} {25,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
26 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.34015,0.0946724,-1.3738e-05,-4.24847e-08,2.10461e-11,7411.52,43.7603], Tmin=(200,'K'), Tmax=(980.72,'K')),
            NASAPolynomial(coeffs=[7.42177,0.082685,-4.42045e-05,1.13995e-08,-1.14632e-12,3766.24,-15.7731], Tmin=(980.72,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 288,
    label = "C12H14_59",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
3  C u0 p0 c0 {6,S} {8,S} {17,S} {18,S}
4  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
5  C u0 p0 c0 {2,S} {7,S} {8,D}
6  C u0 p0 c0 {3,S} {7,B} {9,B}
7  C u0 p0 c0 {5,S} {6,B} {10,B}
8  C u0 p0 c0 {3,S} {5,D} {22,S}
9  C u0 p0 c0 {6,B} {11,B} {23,S}
10 C u0 p0 c0 {7,B} {12,B} {26,S}
11 C u0 p0 c0 {9,B} {12,B} {24,S}
12 C u0 p0 c0 {10,B} {11,B} {25,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.82719,0.0916219,-5.7762e-06,-5.21235e-08,2.5249e-11,5898.03,40.9158], Tmin=(200,'K'), Tmax=(939.75,'K')),
            NASAPolynomial(coeffs=[5.84605,0.0858832,-4.6383e-05,1.19885e-08,-1.19887e-12,2891.17,-7.71355], Tmin=(939.75,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 289,
    label = "C12H14_60",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {17,S} {18,S}
2  C u0 p0 c0 {4,S} {5,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {8,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
5  C u0 p0 c0 {2,S} {7,S} {8,D}
6  C u0 p0 c0 {1,S} {7,B} {9,B}
7  C u0 p0 c0 {5,S} {6,B} {10,B}
8  C u0 p0 c0 {3,S} {5,D} {22,S}
9  C u0 p0 c0 {6,B} {11,B} {23,S}
10 C u0 p0 c0 {7,B} {12,B} {26,S}
11 C u0 p0 c0 {9,B} {12,B} {24,S}
12 C u0 p0 c0 {10,B} {11,B} {25,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.21747,0.0931669,-1.14052e-05,-4.38674e-08,2.13541e-11,5534.69,41.3249], Tmin=(200,'K'), Tmax=(978.37,'K')),
            NASAPolynomial(coeffs=[6.81113,0.0834924,-4.46018e-05,1.14805e-08,-1.15164e-12,2073.06,-14.5003], Tmin=(978.37,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 290,
    label = "C12H14_61",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {13,S}
2  C u0 p0 c0 {1,S} {4,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {7,S} {16,S} {17,S}
4  C u0 p0 c0 {2,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {6,B} {9,B}
6  C u0 p0 c0 {5,B} {8,S} {10,B}
7  C u0 p0 c0 {3,S} {8,D} {21,S}
8  C u0 p0 c0 {6,S} {7,D} {22,S}
9  C u0 p0 c0 {5,B} {12,B} {26,S}
10 C u0 p0 c0 {6,B} {11,B} {23,S}
11 C u0 p0 c0 {10,B} {12,B} {24,S}
12 C u0 p0 c0 {9,B} {11,B} {25,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
26 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.22678,0.0925676,-8.99036e-06,-4.65274e-08,2.22573e-11,5728.07,42.3025], Tmin=(200,'K'), Tmax=(981.11,'K')),
            NASAPolynomial(coeffs=[7.03417,0.0833111,-4.46455e-05,1.15445e-08,-1.16417e-12,2146.73,-14.9955], Tmin=(981.11,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 291,
    label = "C12H15_1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {8,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {20,S} {21,S} {22,S}
6  C u0 p0 c0 {1,S} {7,B} {9,B}
7  C u0 p0 c0 {6,B} {8,S} {10,B}
8  C u1 p0 c0 {4,S} {7,S} {23,S}
9  C u0 p0 c0 {6,B} {12,B} {27,S}
10 C u0 p0 c0 {7,B} {11,B} {24,S}
11 C u0 p0 c0 {10,B} {12,B} {25,S}
12 C u0 p0 c0 {9,B} {11,B} {26,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {12,S}
27 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.20398,0.0960987,-8.21199e-06,-5.17713e-08,2.53332e-11,12621.1,44.4497], Tmin=(200,'K'), Tmax=(942.21,'K')),
            NASAPolynomial(coeffs=[5.93668,0.089222,-4.80948e-05,1.24136e-08,-1.24006e-12,9481.37,-6.62548], Tmin=(942.21,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 292,
    label = "C12H15_2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
3  C u0 p0 c0 {4,S} {6,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {7,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {21,S} {22,S} {23,S}
6  C u1 p0 c0 {2,S} {3,S} {8,S}
7  C u0 p0 c0 {4,S} {8,B} {9,B}
8  C u0 p0 c0 {6,S} {7,B} {10,B}
9  C u0 p0 c0 {7,B} {11,B} {24,S}
10 C u0 p0 c0 {8,B} {12,B} {27,S}
11 C u0 p0 c0 {9,B} {12,B} {25,S}
12 C u0 p0 c0 {10,B} {11,B} {26,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {12,S}
27 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.60878,0.100445,-2.20211e-05,-3.55079e-08,1.88448e-11,11477.6,46.7521], Tmin=(200,'K'), Tmax=(976.31,'K')),
            NASAPolynomial(coeffs=[6.99542,0.0864769,-4.5851e-05,1.16907e-08,-1.16049e-12,8002.13,-11.3476], Tmin=(976.31,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 293,
    label = "C12H15_3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {6,S} {17,S} {18,S}
3  C u0 p0 c0 {1,S} {7,S} {19,S} {20,S}
4  C u0 p0 c0 {5,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {21,S} {22,S} {23,S}
6  C u1 p0 c0 {2,S} {4,S} {8,S}
7  C u0 p0 c0 {3,S} {8,B} {9,B}
8  C u0 p0 c0 {6,S} {7,B} {10,B}
9  C u0 p0 c0 {7,B} {11,B} {24,S}
10 C u0 p0 c0 {8,B} {12,B} {27,S}
11 C u0 p0 c0 {9,B} {12,B} {25,S}
12 C u0 p0 c0 {10,B} {11,B} {26,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {12,S}
27 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.45387,0.0964765,-1.16304e-05,-4.53595e-08,2.20473e-11,9819.6,43.6018], Tmin=(200,'K'), Tmax=(976.66,'K')),
            NASAPolynomial(coeffs=[6.60763,0.0872222,-4.64933e-05,1.19374e-08,-1.19436e-12,6330.31,-12.5033], Tmin=(976.66,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 294,
    label = "C12H15_4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {13,S}
2  C u0 p0 c0 {1,S} {4,S} {16,S} {17,S}
3  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {8,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {20,S} {21,S} {22,S}
6  C u0 p0 c0 {1,S} {7,B} {9,B}
7  C u0 p0 c0 {6,B} {8,S} {10,B}
8  C u1 p0 c0 {4,S} {7,S} {23,S}
9  C u0 p0 c0 {6,B} {12,B} {27,S}
10 C u0 p0 c0 {7,B} {11,B} {24,S}
11 C u0 p0 c0 {10,B} {12,B} {25,S}
12 C u0 p0 c0 {9,B} {11,B} {26,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {12,S}
27 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.53387,0.0974328,-1.31488e-05,-4.44572e-08,2.18498e-11,11247.8,44.2481], Tmin=(200,'K'), Tmax=(978.2,'K')),
            NASAPolynomial(coeffs=[7.03511,0.0865836,-4.61475e-05,1.18595e-08,-1.18845e-12,7631.4,-14.424], Tmin=(978.2,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 295,
    label = "C12H16_128",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,S} {3,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {4,S} {17,S} {18,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {6,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {12,S} {21,S} {22,S}
6  C u0 p0 c0 {4,S} {7,B} {8,B}
7  C u0 p0 c0 {6,B} {9,B} {23,S}
8  C u0 p0 c0 {6,B} {11,B} {27,S}
9  C u0 p0 c0 {7,B} {10,B} {24,S}
10 C u0 p0 c0 {9,B} {11,B} {25,S}
11 C u0 p0 c0 {8,B} {10,B} {26,S}
12 C u2 p0 c0 {5,S} {28,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {11,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.556691,0.0905875,2.0049e-06,-5.83938e-08,2.67545e-11,42506.3,36.6407], Tmin=(200,'K'), Tmax=(947.21,'K')),
            NASAPolynomial(coeffs=[6.78801,0.0911229,-4.88075e-05,1.25349e-08,-1.24732e-12,39699.5,-5.86642], Tmin=(947.21,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 296,
    label = "C12H16_128s",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {5,S} {19,S} {20,S}
4  C u0 p0 c0 {1,S} {6,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {7,B} {8,B}
6  C u0 p0 c0 {4,S} {12,D} {21,S}
7  C u0 p0 c0 {5,B} {9,B} {22,S}
8  C u0 p0 c0 {5,B} {11,B} {26,S}
9  C u0 p0 c0 {7,B} {10,B} {23,S}
10 C u0 p0 c0 {9,B} {11,B} {24,S}
11 C u0 p0 c0 {8,B} {10,B} {25,S}
12 C u0 p0 c0 {6,D} {27,S} {28,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {12,S}
28 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.89209,0.106642,-3.20551e-05,-2.66068e-08,1.59121e-11,4884.71,49.784], Tmin=(200,'K'), Tmax=(978.52,'K')),
            NASAPolynomial(coeffs=[7.08433,0.0889856,-4.67049e-05,1.17949e-08,-1.16023e-12,1433.74,-9.5897], Tmin=(978.52,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 297,
    label = "C12H16_129",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {13,S}
2  C u0 p0 c0 {1,S} {4,S} {16,S} {17,S}
3  C u0 p0 c0 {1,S} {5,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {8,S} {20,S} {21,S}
6  C u0 p0 c0 {4,S} {22,S} {23,S} {24,S}
7  C u0 p0 c0 {1,S} {8,B} {10,B}
8  C u0 p0 c0 {5,S} {7,B} {9,B}
9  C u0 p0 c0 {8,B} {11,B} {25,S}
10 C u0 p0 c0 {7,B} {12,B} {28,S}
11 C u0 p0 c0 {9,B} {12,B} {26,S}
12 C u0 p0 c0 {10,B} {11,B} {27,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {11,S}
27 H u0 p0 c0 {12,S}
28 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.41797,0.0952898,-2.71823e-06,-5.41863e-08,2.48787e-11,-5629.4,44.6234], Tmin=(200,'K'), Tmax=(973.63,'K')),
            NASAPolynomial(coeffs=[5.38647,0.09229,-4.92018e-05,1.26349e-08,-1.26418e-12,-8916.12,-5.69195], Tmin=(973.63,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 298,
    label = "C12H16_130",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {13,S}
2  C u0 p0 c0 {1,S} {4,S} {16,S} {17,S}
3  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {8,S} {20,S} {21,S}
6  C u0 p0 c0 {3,S} {22,S} {23,S} {24,S}
7  C u0 p0 c0 {1,S} {8,B} {10,B}
8  C u0 p0 c0 {5,S} {7,B} {9,B}
9  C u0 p0 c0 {8,B} {11,B} {25,S}
10 C u0 p0 c0 {7,B} {12,B} {28,S}
11 C u0 p0 c0 {9,B} {12,B} {26,S}
12 C u0 p0 c0 {10,B} {11,B} {27,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {11,S}
27 H u0 p0 c0 {12,S}
28 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.28973,0.0927091,3.3801e-06,-5.95152e-08,2.64901e-11,-6299.05,43.1203], Tmin=(200,'K'), Tmax=(975.33,'K')),
            NASAPolynomial(coeffs=[5.00252,0.0929772,-4.97468e-05,1.28307e-08,-1.28976e-12,-9546.86,-5.03544], Tmin=(975.33,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 299,
    label = "C12H17_1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {4,S} {17,S} {18,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {7,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {21,S} {22,S} {23,S}
6  C u0 p0 c0 {7,S} {8,B} {9,B}
7  C u1 p0 c0 {4,S} {6,S} {24,S}
8  C u0 p0 c0 {6,B} {10,B} {25,S}
9  C u0 p0 c0 {6,B} {12,B} {29,S}
10 C u0 p0 c0 {8,B} {11,B} {26,S}
11 C u0 p0 c0 {10,B} {12,B} {27,S}
12 C u0 p0 c0 {9,B} {11,B} {28,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.616899,0.0896685,1.11716e-05,-6.83451e-08,3.02474e-11,7441.96,36.1477], Tmin=(200,'K'), Tmax=(941.11,'K')),
            NASAPolynomial(coeffs=[5.72553,0.0957514,-5.11853e-05,1.3132e-08,-1.3061e-12,4785,-1.8395], Tmin=(941.11,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 300,
    label = "C12H17_10",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {20,S} {21,S}
4  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
6  C u0 p0 c0 {3,S} {4,S} {18,S} {19,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {1,S} {10,D} {25,S}
9  C u0 p0 c0 {1,S} {11,D} {26,S}
10 C u0 p0 c0 {8,D} {12,S} {28,S}
11 C u0 p0 c0 {9,D} {12,S} {29,S}
12 C u1 p0 c0 {10,S} {11,S} {27,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {12,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.03765,0.104153,-1.39749e-05,-4.73125e-08,2.32622e-11,9691.52,47.7864], Tmin=(200,'K'), Tmax=(976.44,'K')),
            NASAPolynomial(coeffs=[7.08144,0.0928165,-4.91178e-05,1.25654e-08,-1.2559e-12,5889.1,-13.9434], Tmin=(976.44,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 301,
    label = "C12H17_11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {20,S} {21,S}
4  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
7  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {1,S} {10,D} {25,S}
9  C u0 p0 c0 {1,S} {11,D} {26,S}
10 C u0 p0 c0 {8,D} {12,S} {28,S}
11 C u0 p0 c0 {9,D} {12,S} {29,S}
12 C u1 p0 c0 {10,S} {11,S} {27,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {12,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.9068,0.101288,-6.70662e-06,-5.39228e-08,2.53191e-11,7566.94,45.5783], Tmin=(200,'K'), Tmax=(978.01,'K')),
            NASAPolynomial(coeffs=[6.68828,0.0936783,-4.9826e-05,1.28183e-08,-1.28853e-12,3786.04,-14.0358], Tmin=(978.01,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 302,
    label = "C12H17_2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {7,S} {17,S} {18,S}
4  C u0 p0 c0 {6,S} {7,S} {19,S} {20,S}
5  C u0 p0 c0 {2,S} {21,S} {22,S} {23,S}
6  C u0 p0 c0 {4,S} {8,B} {9,B}
7  C u1 p0 c0 {3,S} {4,S} {24,S}
8  C u0 p0 c0 {6,B} {10,B} {25,S}
9  C u0 p0 c0 {6,B} {12,B} {29,S}
10 C u0 p0 c0 {8,B} {11,B} {26,S}
11 C u0 p0 c0 {10,B} {12,B} {27,S}
12 C u0 p0 c0 {9,B} {11,B} {28,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.214719,0.0862164,1.74812e-05,-7.36447e-08,3.19337e-11,12732,34.0093], Tmin=(200,'K'), Tmax=(938.32,'K')),
            NASAPolynomial(coeffs=[5.81121,0.0957872,-5.1257e-05,1.316e-08,-1.30962e-12,10210.2,-0.475829], Tmin=(938.32,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 303,
    label = "C12H17_3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
3  C u0 p0 c0 {4,S} {6,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {21,S} {22,S} {23,S}
6  C u0 p0 c0 {3,S} {8,B} {9,B}
7  C u1 p0 c0 {2,S} {4,S} {24,S}
8  C u0 p0 c0 {6,B} {10,B} {25,S}
9  C u0 p0 c0 {6,B} {12,B} {29,S}
10 C u0 p0 c0 {8,B} {11,B} {26,S}
11 C u0 p0 c0 {10,B} {12,B} {27,S}
12 C u0 p0 c0 {9,B} {11,B} {28,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.139833,0.0867675,1.618e-05,-7.23773e-08,3.14881e-11,12500.7,33.4477], Tmin=(200,'K'), Tmax=(939.32,'K')),
            NASAPolynomial(coeffs=[5.8599,0.0956785,-5.11778e-05,1.31355e-08,-1.30684e-12,9958.42,-1.60289], Tmin=(939.32,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 304,
    label = "C12H17_4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {6,S} {19,S} {20,S}
3  C u0 p0 c0 {1,S} {7,S} {17,S} {18,S}
4  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {21,S} {22,S} {23,S}
6  C u0 p0 c0 {2,S} {8,B} {9,B}
7  C u1 p0 c0 {3,S} {4,S} {24,S}
8  C u0 p0 c0 {6,B} {10,B} {25,S}
9  C u0 p0 c0 {6,B} {12,B} {29,S}
10 C u0 p0 c0 {8,B} {11,B} {26,S}
11 C u0 p0 c0 {10,B} {12,B} {27,S}
12 C u0 p0 c0 {9,B} {11,B} {28,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.117624,0.0868778,1.59861e-05,-7.22232e-08,3.1441e-11,12525,33.8026], Tmin=(200,'K'), Tmax=(939.4,'K')),
            NASAPolynomial(coeffs=[5.86416,0.0956741,-5.11758e-05,1.3135e-08,-1.30679e-12,9977.6,-1.37421], Tmin=(939.4,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 305,
    label = "C12H17_5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {6,S} {19,S} {20,S}
4  C u0 p0 c0 {1,S} {7,S} {17,S} {18,S}
5  C u0 p0 c0 {7,S} {21,S} {22,S} {23,S}
6  C u0 p0 c0 {3,S} {8,B} {9,B}
7  C u1 p0 c0 {4,S} {5,S} {24,S}
8  C u0 p0 c0 {6,B} {10,B} {25,S}
9  C u0 p0 c0 {6,B} {12,B} {29,S}
10 C u0 p0 c0 {8,B} {11,B} {26,S}
11 C u0 p0 c0 {10,B} {12,B} {27,S}
12 C u0 p0 c0 {9,B} {11,B} {28,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.550678,0.0846969,2.03104e-05,-7.60487e-08,3.27066e-11,12317.5,32.1994], Tmin=(200,'K'), Tmax=(936.98,'K')),
            NASAPolynomial(coeffs=[5.81511,0.0958251,-5.12975e-05,1.31745e-08,-1.31138e-12,9855.92,-0.726964], Tmin=(936.98,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 306,
    label = "C12H17_6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {13,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {14,S}
3  C u0 p0 c0 {1,S} {5,S} {17,S} {18,S}
4  C u0 p0 c0 {1,S} {6,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {8,S} {21,S} {22,S}
7  C u0 p0 c0 {5,S} {23,S} {24,S} {25,S}
8  C u0 p0 c0 {2,S} {6,S} {10,D}
9  C u1 p0 c0 {2,S} {11,S} {26,S}
10 C u0 p0 c0 {8,D} {12,S} {27,S}
11 C u0 p0 c0 {9,S} {12,D} {29,S}
12 C u0 p0 c0 {10,S} {11,D} {28,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {10,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.88727,0.101942,-9.23912e-06,-5.10591e-08,2.43248e-11,10259.3,48.1356], Tmin=(200,'K'), Tmax=(974.63,'K')),
            NASAPolynomial(coeffs=[6.27262,0.0943761,-5.01261e-05,1.28409e-08,-1.28309e-12,6657.75,-8.93528], Tmin=(974.63,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 307,
    label = "C12H17_7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {13,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {14,S}
3  C u0 p0 c0 {1,S} {5,S} {17,S} {18,S}
4  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {6,S} {19,S} {20,S}
6  C u0 p0 c0 {5,S} {8,S} {21,S} {22,S}
7  C u0 p0 c0 {4,S} {23,S} {24,S} {25,S}
8  C u0 p0 c0 {2,S} {6,S} {10,D}
9  C u1 p0 c0 {2,S} {11,S} {26,S}
10 C u0 p0 c0 {8,D} {12,S} {27,S}
11 C u0 p0 c0 {9,S} {12,D} {29,S}
12 C u0 p0 c0 {10,S} {11,D} {28,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {10,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.72425,0.0985387,-1.02579e-06,-5.8344e-08,2.65551e-11,7148.66,45.8355], Tmin=(200,'K'), Tmax=(976.62,'K')),
            NASAPolynomial(coeffs=[5.7949,0.0952603,-5.08369e-05,1.30978e-08,-1.31677e-12,3586.36,-8.58245], Tmin=(976.62,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 308,
    label = "C12H17_8",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {13,S}
3  C u0 p0 c0 {1,S} {2,S} {20,S} {21,S}
4  C u0 p0 c0 {2,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
6  C u0 p0 c0 {5,S} {7,S} {14,S} {15,S}
7  C u0 p0 c0 {6,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {1,S} {10,D} {25,S}
9  C u0 p0 c0 {1,S} {11,D} {26,S}
10 C u0 p0 c0 {8,D} {12,S} {28,S}
11 C u0 p0 c0 {9,D} {12,S} {29,S}
12 C u1 p0 c0 {10,S} {11,S} {27,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {12,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.44905,0.114543,-4.12524e-05,-2.13618e-08,1.4755e-11,18329.8,51.2741], Tmin=(200,'K'), Tmax=(981.39,'K')),
            NASAPolynomial(coeffs=[8.47868,0.090069,-4.69748e-05,1.18237e-08,-1.16218e-12,14433.5,-17.775], Tmin=(981.39,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 309,
    label = "C12H17_9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {20,S} {21,S}
4  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {3,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
7  C u0 p0 c0 {6,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {1,S} {10,D} {25,S}
9  C u0 p0 c0 {1,S} {11,D} {26,S}
10 C u0 p0 c0 {8,D} {12,S} {28,S}
11 C u0 p0 c0 {9,D} {12,S} {29,S}
12 C u1 p0 c0 {10,S} {11,S} {27,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {12,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.24107,0.108601,-2.49453e-05,-3.73205e-08,2.01024e-11,18331.4,49.4903], Tmin=(200,'K'), Tmax=(976.33,'K')),
            NASAPolynomial(coeffs=[7.73301,0.0916491,-4.82264e-05,1.22574e-08,-1.2169e-12,14463.1,-15.8272], Tmin=(976.33,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 310,
    label = "C12H18_119",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {5,S} {19,S} {20,S}
4  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {7,S} {21,S} {22,S}
6  C u0 p0 c0 {4,S} {23,S} {24,S} {25,S}
7  C u0 p0 c0 {5,S} {8,B} {9,B}
8  C u0 p0 c0 {7,B} {10,B} {26,S}
9  C u0 p0 c0 {7,B} {12,B} {30,S}
10 C u0 p0 c0 {8,B} {11,B} {27,S}
11 C u0 p0 c0 {10,B} {12,B} {28,S}
12 C u0 p0 c0 {9,B} {11,B} {29,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {10,S}
28 H u0 p0 c0 {11,S}
29 H u0 p0 c0 {12,S}
30 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.238003,0.0794403,4.34526e-05,-1.01407e-07,4.20353e-11,-11221.2,32.1316], Tmin=(200,'K'), Tmax=(918.97,'K')),
            NASAPolynomial(coeffs=[3.4988,0.102516,-5.50467e-05,1.41814e-08,-1.41572e-12,-13394.2,8.11347], Tmin=(918.97,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 311,
    label = "C12H18_122",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {13,S}
3  C u0 p0 c0 {1,S} {2,S} {20,S} {21,S}
4  C u0 p0 c0 {2,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
6  C u0 p0 c0 {5,S} {8,S} {14,S} {15,S}
7  C u0 p0 c0 {11,S} {12,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  C u0 p0 c0 {1,S} {11,D} {27,S}
10 C u0 p0 c0 {1,S} {12,D} {30,S}
11 C u0 p0 c0 {7,S} {9,D} {28,S}
12 C u0 p0 c0 {7,S} {10,D} {29,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {11,S}
29 H u0 p0 c0 {12,S}
30 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.25987,0.112307,-3.19407e-05,-2.91473e-08,1.69476e-11,8709.2,50.3753], Tmin=(200,'K'), Tmax=(976.49,'K')),
            NASAPolynomial(coeffs=[6.42704,0.096409,-5.03445e-05,1.26543e-08,-1.23958e-12,5292.88,-7.73452], Tmin=(976.49,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 312,
    label = "C12H18_123",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {20,S} {21,S}
4  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {3,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {8,S} {14,S} {15,S}
7  C u0 p0 c0 {11,S} {12,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  C u0 p0 c0 {1,S} {11,D} {27,S}
10 C u0 p0 c0 {1,S} {12,D} {30,S}
11 C u0 p0 c0 {7,S} {9,D} {28,S}
12 C u0 p0 c0 {7,S} {10,D} {29,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {11,S}
29 H u0 p0 c0 {12,S}
30 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.09437,0.106792,-1.63608e-05,-4.47648e-08,2.22962e-11,7579.63,48.7292], Tmin=(200,'K'), Tmax=(969.89,'K')),
            NASAPolynomial(coeffs=[5.78849,0.0977393,-5.13943e-05,1.30206e-08,-1.28634e-12,4171.32,-6.33553], Tmin=(969.89,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 313,
    label = "C12H18_124",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {20,S} {21,S}
4  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {8,S} {14,S} {15,S}
6  C u0 p0 c0 {3,S} {4,S} {18,S} {19,S}
7  C u0 p0 c0 {11,S} {12,S} {22,S} {23,S}
8  C u0 p0 c0 {5,S} {24,S} {25,S} {26,S}
9  C u0 p0 c0 {1,S} {11,D} {27,S}
10 C u0 p0 c0 {1,S} {12,D} {30,S}
11 C u0 p0 c0 {7,S} {9,D} {28,S}
12 C u0 p0 c0 {7,S} {10,D} {29,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {11,S}
29 H u0 p0 c0 {12,S}
30 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.44341,0.091374,2.31177e-05,-8.54714e-08,3.72246e-11,-1614,41.3262], Tmin=(200,'K'), Tmax=(924.85,'K')),
            NASAPolynomial(coeffs=[3.52014,0.102599,-5.51272e-05,1.42083e-08,-1.41878e-12,-4300.24,4.46239], Tmin=(924.85,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 314,
    label = "C12H18_125",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {20,S} {21,S}
4  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
7  C u0 p0 c0 {11,S} {12,S} {22,S} {23,S}
8  C u0 p0 c0 {2,S} {24,S} {25,S} {26,S}
9  C u0 p0 c0 {1,S} {11,D} {27,S}
10 C u0 p0 c0 {1,S} {12,D} {30,S}
11 C u0 p0 c0 {7,S} {9,D} {28,S}
12 C u0 p0 c0 {7,S} {10,D} {29,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {11,S}
29 H u0 p0 c0 {12,S}
30 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.74005,0.0988674,3.45931e-06,-6.28958e-08,2.80249e-11,-3627.07,44.5626], Tmin=(200,'K'), Tmax=(971.94,'K')),
            NASAPolynomial(coeffs=[4.70052,0.0997949,-5.30132e-05,1.35927e-08,-1.36011e-12,-6952.38,-4.58397], Tmin=(971.94,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 315,
    label = "C12H18_126",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {13,S}
3  C u0 p0 c0 {1,S} {2,S} {20,S} {21,S}
4  C u0 p0 c0 {2,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
6  C u0 p0 c0 {5,S} {8,S} {14,S} {15,S}
7  C u0 p0 c0 {1,S} {10,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  C u0 p0 c0 {1,S} {11,D} {27,S}
10 C u0 p0 c0 {7,S} {12,D} {28,S}
11 C u0 p0 c0 {9,D} {12,S} {29,S}
12 C u0 p0 c0 {10,D} {11,S} {30,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {11,S}
30 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.28745,0.111845,-2.97864e-05,-3.18251e-08,1.79814e-11,9005.29,50.1508], Tmin=(200,'K'), Tmax=(974.54,'K')),
            NASAPolynomial(coeffs=[6.55474,0.0962628,-5.0314e-05,1.26672e-08,-1.24346e-12,5518.78,-8.92264], Tmin=(974.54,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 316,
    label = "C12H18_127",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {20,S} {21,S}
4  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {3,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {8,S} {14,S} {15,S}
7  C u0 p0 c0 {1,S} {10,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  C u0 p0 c0 {1,S} {11,D} {27,S}
10 C u0 p0 c0 {7,S} {12,D} {28,S}
11 C u0 p0 c0 {9,D} {12,S} {29,S}
12 C u0 p0 c0 {10,D} {11,S} {30,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {11,S}
30 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.11854,0.106779,-1.5757e-05,-4.56659e-08,2.26543e-11,7675.31,48.4397], Tmin=(200,'K'), Tmax=(970.46,'K')),
            NASAPolynomial(coeffs=[5.95722,0.0975133,-5.13058e-05,1.30138e-08,-1.28767e-12,4200.39,-7.69565], Tmin=(970.46,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 317,
    label = "C12H18_128",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {20,S} {21,S}
4  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {8,S} {14,S} {15,S}
6  C u0 p0 c0 {3,S} {4,S} {18,S} {19,S}
7  C u0 p0 c0 {1,S} {10,S} {22,S} {23,S}
8  C u0 p0 c0 {5,S} {24,S} {25,S} {26,S}
9  C u0 p0 c0 {1,S} {11,D} {27,S}
10 C u0 p0 c0 {7,S} {12,D} {28,S}
11 C u0 p0 c0 {9,D} {12,S} {29,S}
12 C u0 p0 c0 {10,D} {11,S} {30,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {11,S}
30 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.89191,0.101298,-1.67749e-06,-5.87831e-08,2.68453e-11,-349.561,47.3033], Tmin=(200,'K'), Tmax=(972.63,'K')),
            NASAPolynomial(coeffs=[5.36895,0.0986656,-5.22953e-05,1.3389e-08,-1.33847e-12,-3828.01,-5.73882], Tmin=(972.63,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 318,
    label = "C12H18_129",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {20,S} {21,S}
4  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
7  C u0 p0 c0 {1,S} {10,S} {22,S} {23,S}
8  C u0 p0 c0 {2,S} {24,S} {25,S} {26,S}
9  C u0 p0 c0 {1,S} {11,D} {27,S}
10 C u0 p0 c0 {7,S} {12,D} {28,S}
11 C u0 p0 c0 {9,D} {12,S} {29,S}
12 C u0 p0 c0 {10,D} {11,S} {30,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {11,S}
30 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.77346,0.0992349,2.89344e-06,-6.25687e-08,2.79506e-11,-3029.18,44.3269], Tmin=(200,'K'), Tmax=(972.85,'K')),
            NASAPolynomial(coeffs=[4.88848,0.0995095,-5.28664e-05,1.35627e-08,-1.35822e-12,-6412.87,-5.95227], Tmin=(972.85,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 319,
    label = "C12H8_10",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {6,S}
2  C u0 p0 c0 {1,B} {4,B} {10,B}
3  C u0 p0 c0 {1,B} {5,S} {7,B}
4  C u0 p0 c0 {2,B} {8,B} {9,B}
5  C u0 p0 c0 {3,S} {6,D} {13,S}
6  C u0 p0 c0 {1,S} {5,D} {14,S}
7  C u0 p0 c0 {3,B} {8,B} {15,S}
8  C u0 p0 c0 {4,B} {7,B} {16,S}
9  C u0 p0 c0 {4,B} {11,B} {17,S}
10 C u0 p0 c0 {2,B} {12,B} {20,S}
11 C u0 p0 c0 {9,B} {12,B} {18,S}
12 C u0 p0 c0 {10,B} {11,B} {19,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {11,S}
19 H u0 p0 c0 {12,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.39512,0.0804616,-1.85749e-05,-3.12855e-08,1.66604e-11,56438.2,35.8408], Tmin=(200,'K'), Tmax=(1006,'K')),
            NASAPolynomial(coeffs=[10.7612,0.0591376,-3.29834e-05,8.88175e-09,-9.30548e-13,52223.1,-35.5028], Tmin=(1006,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 320,
    label = "C12H8_11",
    molecule = 
"""
1  C u0 p0 c0 {4,B} {5,B} {8,S}
2  C u0 p0 c0 {3,B} {5,B} {9,B}
3  C u0 p0 c0 {2,B} {6,B} {10,B}
4  C u0 p0 c0 {1,B} {6,B} {7,S}
5  C u0 p0 c0 {1,B} {2,B} {15,S}
6  C u0 p0 c0 {3,B} {4,B} {20,S}
7  C u0 p0 c0 {4,S} {8,D} {13,S}
8  C u0 p0 c0 {1,S} {7,D} {14,S}
9  C u0 p0 c0 {2,B} {11,B} {16,S}
10 C u0 p0 c0 {3,B} {12,B} {19,S}
11 C u0 p0 c0 {9,B} {12,B} {17,S}
12 C u0 p0 c0 {10,B} {11,B} {18,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {11,S}
18 H u0 p0 c0 {12,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.27779,0.0783909,-1.39047e-05,-3.51423e-08,1.77578e-11,50841.3,34.6682], Tmin=(200,'K'), Tmax=(1007.71,'K')),
            NASAPolynomial(coeffs=[10.3412,0.0599763,-3.36433e-05,9.10847e-09,-9.58728e-13,46689.8,-34.2877], Tmin=(1007.71,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 321,
    label = "C12H8_13",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {4,B}
2  C u0 p0 c0 {1,B} {5,B} {6,B}
3  C u0 p0 c0 {1,B} {7,B} {8,S}
4  C u0 p0 c0 {1,B} {9,S} {10,B}
5  C u0 p0 c0 {2,B} {11,B} {14,S}
6  C u0 p0 c0 {2,B} {12,B} {15,S}
7  C u0 p0 c0 {3,B} {12,B} {17,S}
8  C u0 p0 c0 {3,S} {9,D} {18,S}
9  C u0 p0 c0 {4,S} {8,D} {19,S}
10 C u0 p0 c0 {4,B} {11,B} {20,S}
11 C u0 p0 c0 {5,B} {10,B} {13,S}
12 C u0 p0 c0 {6,B} {7,B} {16,S}
13 H u0 p0 c0 {11,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {12,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.86479,0.0714353,1.38804e-06,-4.73596e-08,2.1094e-11,28567.2,32.5238], Tmin=(200,'K'), Tmax=(1015.31,'K')),
            NASAPolynomial(coeffs=[8.74444,0.0632875,-3.62871e-05,1.00202e-08,-1.07198e-12,24678.5,-27.3619], Tmin=(1015.31,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 322,
    label = "C12H8_8",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {6,B}
2  C u0 p0 c0 {1,B} {4,B} {5,B}
3  C u0 p0 c0 {1,B} {7,B} {11,S}
4  C u0 p0 c0 {2,B} {8,B} {15,S}
5  C u0 p0 c0 {2,B} {9,B} {16,S}
6  C u0 p0 c0 {1,B} {10,B} {19,S}
7  C u0 p0 c0 {3,B} {8,B} {13,S}
8  C u0 p0 c0 {4,B} {7,B} {14,S}
9  C u0 p0 c0 {5,B} {10,B} {17,S}
10 C u0 p0 c0 {6,B} {9,B} {18,S}
11 C u0 p0 c0 {3,S} {12,T}
12 C u0 p0 c0 {11,T} {20,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.82036,0.0895248,-4.20237e-05,-1.00241e-08,1.01222e-11,43012.2,37.9388], Tmin=(200,'K'), Tmax=(1001.07,'K')),
            NASAPolynomial(coeffs=[12.1805,0.055525,-2.99463e-05,7.81709e-09,-7.97419e-13,38709,-40.9396], Tmin=(1001.07,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 323,
    label = "C12H8_9",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {5,B} {6,B}
2  C u0 p0 c0 {1,B} {4,B} {7,B}
3  C u0 p0 c0 {4,B} {8,B} {11,S}
4  C u0 p0 c0 {2,B} {3,B} {19,S}
5  C u0 p0 c0 {1,B} {8,B} {14,S}
6  C u0 p0 c0 {1,B} {9,B} {15,S}
7  C u0 p0 c0 {2,B} {10,B} {18,S}
8  C u0 p0 c0 {3,B} {5,B} {13,S}
9  C u0 p0 c0 {6,B} {10,B} {16,S}
10 C u0 p0 c0 {7,B} {9,B} {17,S}
11 C u0 p0 c0 {3,S} {12,T}
12 C u0 p0 c0 {11,T} {20,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.84261,0.0899832,-4.31383e-05,-9.01869e-09,9.80689e-12,43180.1,38.1238], Tmin=(200,'K'), Tmax=(1001.28,'K')),
            NASAPolynomial(coeffs=[12.2558,0.0553861,-2.9839e-05,7.78048e-09,-7.92891e-13,38867.3,-41.1747], Tmin=(1001.28,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 324,
    label = "C12H9_11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {13,S}
2  C u0 p0 c0 {1,S} {7,D} {8,S}
3  C u0 p0 c0 {4,B} {5,S} {9,B}
4  C u0 p0 c0 {3,B} {7,S} {10,B}
5  C u1 p0 c0 {1,S} {3,S} {14,S}
6  C u0 p0 c0 {1,S} {8,D} {15,S}
7  C u0 p0 c0 {2,D} {4,S} {20,S}
8  C u0 p0 c0 {2,S} {6,D} {21,S}
9  C u0 p0 c0 {3,B} {11,B} {16,S}
10 C u0 p0 c0 {4,B} {12,B} {19,S}
11 C u0 p0 c0 {9,B} {12,B} {17,S}
12 C u0 p0 c0 {10,B} {11,B} {18,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {11,S}
18 H u0 p0 c0 {12,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.64323,0.0830647,-1.57145e-05,-3.61402e-08,1.84612e-11,59580.4,38.3068], Tmin=(200,'K'), Tmax=(1007.5,'K')),
            NASAPolynomial(coeffs=[10.8355,0.062831,-3.51384e-05,9.49929e-09,-9.99466e-13,55175.4,-35.2034], Tmin=(1007.5,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 325,
    label = "C12H9_13",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {4,B} {6,B}
2  C u0 p0 c0 {1,B} {5,B} {10,B}
3  C u0 p0 c0 {4,B} {9,S} {12,B}
4  C u0 p0 c0 {1,B} {3,B} {18,S}
5  C u0 p0 c0 {2,B} {7,B} {14,S}
6  C u0 p0 c0 {1,B} {8,B} {17,S}
7  C u0 p0 c0 {5,B} {8,B} {15,S}
8  C u0 p0 c0 {6,B} {7,B} {16,S}
9  C u0 p0 c0 {3,S} {11,D} {13,S}
10 C u0 p0 c0 {2,B} {12,B} {19,S}
11 C u0 p0 c0 {9,D} {20,S} {21,S}
12 C u1 p0 c0 {3,B} {10,B}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.83144,0.0887431,-3.26801e-05,-1.97302e-08,1.32789e-11,52825.8,39.5042], Tmin=(200,'K'), Tmax=(996.93,'K')),
            NASAPolynomial(coeffs=[10.9764,0.0612288,-3.32415e-05,8.70491e-09,-8.88389e-13,48686.9,-34.0186], Tmin=(996.93,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 326,
    label = "C12H9_14",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {13,S}
2  C u1 p0 c0 {1,S} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {4,B} {10,B}
4  C u0 p0 c0 {3,B} {8,S} {9,B}
5  C u0 p0 c0 {1,S} {7,D} {14,S}
6  C u0 p0 c0 {1,S} {8,D} {15,S}
7  C u0 p0 c0 {2,S} {5,D} {16,S}
8  C u0 p0 c0 {4,S} {6,D} {17,S}
9  C u0 p0 c0 {4,B} {11,B} {18,S}
10 C u0 p0 c0 {3,B} {12,B} {21,S}
11 C u0 p0 c0 {9,B} {12,B} {19,S}
12 C u0 p0 c0 {10,B} {11,B} {20,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {11,S}
20 H u0 p0 c0 {12,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.57336,0.0821211,-1.40897e-05,-3.72255e-08,1.87273e-11,57758.9,38.3199], Tmin=(200,'K'), Tmax=(1006.77,'K')),
            NASAPolynomial(coeffs=[10.4941,0.0633188,-3.5416e-05,9.5687e-09,-1.00572e-12,53449.4,-33.1463], Tmin=(1006.77,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 327,
    label = "C12H9_16",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,B} {7,B}
3  C u0 p0 c0 {2,B} {4,B} {5,B}
4  C u0 p0 c0 {3,B} {6,S} {10,B}
5  C u0 p0 c0 {3,B} {8,B} {9,B}
6  C u1 p0 c0 {1,S} {4,S} {15,S}
7  C u0 p0 c0 {2,B} {11,B} {16,S}
8  C u0 p0 c0 {5,B} {11,B} {18,S}
9  C u0 p0 c0 {5,B} {12,B} {19,S}
10 C u0 p0 c0 {4,B} {12,B} {21,S}
11 C u0 p0 c0 {7,B} {8,B} {17,S}
12 C u0 p0 c0 {9,B} {10,B} {20,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {11,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {12,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.27248,0.0771487,-3.40923e-06,-4.5674e-08,2.10365e-11,32238.6,35.5364], Tmin=(200,'K'), Tmax=(1010.62,'K')),
            NASAPolynomial(coeffs=[9.31486,0.0655754,-3.7125e-05,1.01396e-08,-1.07528e-12,28145.5,-29.1515], Tmin=(1010.62,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 328,
    label = "C12H9_17",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {13,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {8,S} {9,B}
4  C u0 p0 c0 {2,B} {7,S} {10,B}
5  C u1 p0 c0 {1,S} {11,S} {14,S}
6  C u0 p0 c0 {1,S} {7,D} {15,S}
7  C u0 p0 c0 {4,S} {6,D} {21,S}
8  C u0 p0 c0 {3,S} {11,D} {17,S}
9  C u0 p0 c0 {3,B} {12,B} {18,S}
10 C u0 p0 c0 {4,B} {12,B} {20,S}
11 C u0 p0 c0 {5,S} {8,D} {16,S}
12 C u0 p0 c0 {9,B} {10,B} {19,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {11,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {12,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.32692,0.0776282,-3.5205e-06,-4.60551e-08,2.12169e-11,42484.9,36.3848], Tmin=(200,'K'), Tmax=(1012.98,'K')),
            NASAPolynomial(coeffs=[9.6528,0.0653336,-3.71571e-05,1.02003e-08,-1.087e-12,38261.6,-30.4311], Tmin=(1012.98,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 329,
    label = "C12H9_18",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,B} {4,B} {7,S}
2  C u0 p0 c0 {3,B} {5,B} {6,B}
3  C u0 p0 c0 {1,B} {2,B} {12,B}
4  C u0 p0 c0 {1,B} {8,B} {14,S}
5  C u0 p0 c0 {2,B} {8,B} {16,S}
6  C u0 p0 c0 {2,B} {9,B} {17,S}
7  C u0 p0 c0 {1,S} {11,D} {13,S}
8  C u0 p0 c0 {4,B} {5,B} {15,S}
9  C u0 p0 c0 {6,B} {10,B} {18,S}
10 C u0 p0 c0 {9,B} {12,B} {19,S}
11 C u0 p0 c0 {7,D} {20,S} {21,S}
12 C u1 p0 c0 {3,B} {10,B}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.83631,0.0887669,-3.26395e-05,-1.98305e-08,1.33232e-11,53337.6,39.8771], Tmin=(200,'K'), Tmax=(997.05,'K')),
            NASAPolynomial(coeffs=[11.0164,0.0611721,-3.32192e-05,8.7031e-09,-8.88689e-13,49184.5,-33.8876], Tmin=(997.05,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 330,
    label = "C12H9_19",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,B}
2  C u0 p0 c0 {1,B} {5,B} {6,B}
3  C u0 p0 c0 {1,B} {4,B} {11,S}
4  C u0 p0 c0 {3,B} {8,B} {13,S}
5  C u0 p0 c0 {2,B} {8,B} {15,S}
6  C u0 p0 c0 {2,B} {9,B} {16,S}
7  C u0 p0 c0 {1,B} {10,B} {19,S}
8  C u0 p0 c0 {4,B} {5,B} {14,S}
9  C u0 p0 c0 {6,B} {10,B} {17,S}
10 C u0 p0 c0 {7,B} {9,B} {18,S}
11 C u0 p0 c0 {3,S} {12,D} {20,S}
12 C u1 p0 c0 {11,D} {21,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.96182,0.0905017,-3.57651e-05,-1.7636e-08,1.27546e-11,53384,39.8967], Tmin=(200,'K'), Tmax=(998.85,'K')),
            NASAPolynomial(coeffs=[11.6278,0.0602662,-3.2694e-05,8.56993e-09,-8.76499e-13,49063.2,-37.5124], Tmin=(998.85,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 331,
    label = "C12H9_23",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {5,B}
2  C u0 p0 c0 {1,B} {4,B} {6,B}
3  C u0 p0 c0 {1,B} {9,S} {12,B}
4  C u0 p0 c0 {2,B} {7,B} {15,S}
5  C u0 p0 c0 {1,B} {8,B} {18,S}
6  C u0 p0 c0 {2,B} {10,B} {14,S}
7  C u0 p0 c0 {4,B} {8,B} {16,S}
8  C u0 p0 c0 {5,B} {7,B} {17,S}
9  C u0 p0 c0 {3,S} {11,D} {13,S}
10 C u0 p0 c0 {6,B} {12,B} {19,S}
11 C u0 p0 c0 {9,D} {20,S} {21,S}
12 C u1 p0 c0 {3,B} {10,B}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.83216,0.0887804,-3.28549e-05,-1.95485e-08,1.32194e-11,54011.5,39.856], Tmin=(200,'K'), Tmax=(996.92,'K')),
            NASAPolynomial(coeffs=[10.9882,0.0611676,-3.31958e-05,8.69119e-09,-8.86868e-13,49872.6,-33.715], Tmin=(996.92,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 332,
    label = "C12H9_25",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {13,S}
2  C u0 p0 c0 {1,S} {6,D} {7,S}
3  C u0 p0 c0 {1,S} {8,D} {9,S}
4  C u0 p0 c0 {1,S} {5,S} {10,D}
5  C u1 p0 c0 {4,S} {6,S} {14,S}
6  C u0 p0 c0 {2,D} {5,S} {15,S}
7  C u0 p0 c0 {2,S} {11,D} {16,S}
8  C u0 p0 c0 {3,D} {11,S} {18,S}
9  C u0 p0 c0 {3,S} {12,D} {19,S}
10 C u0 p0 c0 {4,D} {12,S} {21,S}
11 C u0 p0 c0 {7,D} {8,S} {17,S}
12 C u0 p0 c0 {9,D} {10,S} {20,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {11,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {12,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.54342,0.0807654,-9.42085e-06,-4.18479e-08,2.01519e-11,46865.8,37.0459], Tmin=(200,'K'), Tmax=(1012.91,'K')),
            NASAPolynomial(coeffs=[10.6482,0.0637324,-3.61189e-05,9.8976e-09,-1.05423e-12,42394.8,-35.6438], Tmin=(1012.91,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 333,
    label = "C12H9_26",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {13,S}
2  C u0 p0 c0 {1,S} {4,B} {7,B}
3  C u1 p0 c0 {1,S} {6,S} {8,S}
4  C u0 p0 c0 {2,B} {9,S} {10,B}
5  C u0 p0 c0 {1,S} {6,D} {14,S}
6  C u0 p0 c0 {3,S} {5,D} {20,S}
7  C u0 p0 c0 {2,B} {12,B} {17,S}
8  C u0 p0 c0 {3,S} {9,D} {19,S}
9  C u0 p0 c0 {4,S} {8,D} {18,S}
10 C u0 p0 c0 {4,B} {11,B} {21,S}
11 C u0 p0 c0 {10,B} {12,B} {15,S}
12 C u0 p0 c0 {7,B} {11,B} {16,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {11,S}
16 H u0 p0 c0 {12,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.55527,0.0816134,-1.25931e-05,-3.86322e-08,1.91526e-11,55841.6,38.1753], Tmin=(200,'K'), Tmax=(1008.29,'K')),
            NASAPolynomial(coeffs=[10.4865,0.0634876,-3.56312e-05,9.66143e-09,-1.01885e-12,51503,-33.324], Tmin=(1008.29,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 334,
    label = "C12H9_27",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {4,B} {5,B}
2  C u0 p0 c0 {1,B} {6,B} {12,B}
3  C u0 p0 c0 {7,B} {10,S} {12,B}
4  C u0 p0 c0 {1,B} {9,B} {17,S}
5  C u0 p0 c0 {1,B} {7,B} {18,S}
6  C u0 p0 c0 {2,B} {8,B} {14,S}
7  C u0 p0 c0 {3,B} {5,B} {19,S}
8  C u0 p0 c0 {6,B} {9,B} {15,S}
9  C u0 p0 c0 {4,B} {8,B} {16,S}
10 C u0 p0 c0 {3,S} {11,D} {13,S}
11 C u0 p0 c0 {10,D} {20,S} {21,S}
12 C u1 p0 c0 {2,B} {3,B}
13 H u0 p0 c0 {10,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.80938,0.0883918,-3.19856e-05,-2.02735e-08,1.34335e-11,53423.7,39.8589], Tmin=(200,'K'), Tmax=(996.74,'K')),
            NASAPolynomial(coeffs=[10.8876,0.061351,-3.33181e-05,8.72717e-09,-8.90796e-13,49306.1,-33.135], Tmin=(996.74,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 335,
    label = "C12H9_4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,B} {4,B}
2  C u0 p0 c0 {1,S} {5,B} {12,B}
3  C u0 p0 c0 {1,B} {7,B} {16,S}
4  C u0 p0 c0 {1,B} {9,B} {20,S}
5  C u0 p0 c0 {2,B} {6,B} {15,S}
6  C u0 p0 c0 {5,B} {10,B} {14,S}
7  C u0 p0 c0 {3,B} {8,B} {17,S}
8  C u0 p0 c0 {7,B} {9,B} {18,S}
9  C u0 p0 c0 {4,B} {8,B} {19,S}
10 C u0 p0 c0 {6,B} {11,B} {13,S}
11 C u0 p0 c0 {10,B} {12,B} {21,S}
12 C u1 p0 c0 {2,B} {11,B}
13 H u0 p0 c0 {10,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.47999,0.0813187,-1.40458e-05,-3.64201e-08,1.83619e-11,51288,39.0324], Tmin=(200,'K'), Tmax=(1003.16,'K')),
            NASAPolynomial(coeffs=[9.97846,0.0635963,-3.53262e-05,9.4751e-09,-9.88963e-13,47180.6,-29.1256], Tmin=(1003.16,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 336,
    label = "C12H9_5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,B} {5,B}
2  C u0 p0 c0 {1,S} {3,B} {10,B}
3  C u0 p0 c0 {2,B} {9,B} {14,S}
4  C u0 p0 c0 {1,B} {6,B} {15,S}
5  C u0 p0 c0 {1,B} {8,B} {19,S}
6  C u0 p0 c0 {4,B} {7,B} {16,S}
7  C u0 p0 c0 {6,B} {8,B} {17,S}
8  C u0 p0 c0 {5,B} {7,B} {18,S}
9  C u0 p0 c0 {3,B} {11,B} {13,S}
10 C u0 p0 c0 {2,B} {12,B} {21,S}
11 C u0 p0 c0 {9,B} {12,B} {20,S}
12 C u1 p0 c0 {10,B} {11,B}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.47471,0.0811435,-1.35043e-05,-3.69441e-08,1.8524e-11,51178.7,38.6955], Tmin=(200,'K'), Tmax=(1003.73,'K')),
            NASAPolynomial(coeffs=[9.9849,0.0636404,-3.53932e-05,9.50568e-09,-9.93424e-13,47057.9,-29.5289], Tmin=(1003.73,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 337,
    label = "C12H9_6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,B} {6,B}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {7,B} {15,S}
4  C u0 p0 c0 {2,B} {9,B} {19,S}
5  C u0 p0 c0 {1,B} {10,B} {13,S}
6  C u0 p0 c0 {1,B} {11,B} {14,S}
7  C u0 p0 c0 {3,B} {8,B} {16,S}
8  C u0 p0 c0 {7,B} {9,B} {17,S}
9  C u0 p0 c0 {4,B} {8,B} {18,S}
10 C u0 p0 c0 {5,B} {12,B} {20,S}
11 C u0 p0 c0 {6,B} {12,B} {21,S}
12 C u1 p0 c0 {10,B} {11,B}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.47723,0.081239,-1.378e-05,-3.66831e-08,1.84449e-11,51430.8,38.0404], Tmin=(200,'K'), Tmax=(1003.34,'K')),
            NASAPolynomial(coeffs=[9.9732,0.0636439,-3.53764e-05,9.49444e-09,-9.9151e-13,47319.7,-30.1042], Tmin=(1003.34,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 338,
    label = "C12H9_7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {6,B} {7,B}
2  C u0 p0 c0 {1,B} {4,B} {8,B}
3  C u0 p0 c0 {4,B} {5,B} {11,S}
4  C u0 p0 c0 {2,B} {3,B} {19,S}
5  C u0 p0 c0 {3,B} {6,B} {13,S}
6  C u0 p0 c0 {1,B} {5,B} {14,S}
7  C u0 p0 c0 {1,B} {9,B} {15,S}
8  C u0 p0 c0 {2,B} {10,B} {18,S}
9  C u0 p0 c0 {7,B} {10,B} {16,S}
10 C u0 p0 c0 {8,B} {9,B} {17,S}
11 C u0 p0 c0 {3,S} {12,D} {20,S}
12 C u1 p0 c0 {11,D} {21,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.96624,0.0906045,-3.59806e-05,-1.74454e-08,1.26949e-11,52119.3,39.716], Tmin=(200,'K'), Tmax=(998.77,'K')),
            NASAPolynomial(coeffs=[11.6266,0.060293,-3.27071e-05,8.57097e-09,-8.76293e-13,47801.2,-37.6923], Tmin=(998.77,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 339,
    label = "C12H9_9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {13,S}
2  C u1 p0 c0 {1,S} {5,S} {6,S}
3  C u0 p0 c0 {1,S} {7,S} {8,D}
4  C u0 p0 c0 {1,S} {9,S} {10,D}
5  C u0 p0 c0 {2,S} {11,D} {15,S}
6  C u0 p0 c0 {2,S} {7,D} {16,S}
7  C u0 p0 c0 {3,S} {6,D} {17,S}
8  C u0 p0 c0 {3,D} {12,S} {18,S}
9  C u0 p0 c0 {4,S} {12,D} {20,S}
10 C u0 p0 c0 {4,D} {11,S} {21,S}
11 C u0 p0 c0 {5,D} {10,S} {14,S}
12 C u0 p0 c0 {8,S} {9,D} {19,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {11,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {12,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.49051,0.080134,-8.47101e-06,-4.23507e-08,2.02437e-11,46486.3,36.9816], Tmin=(200,'K'), Tmax=(1011.87,'K')),
            NASAPolynomial(coeffs=[10.3194,0.0642226,-3.63636e-05,9.94373e-09,-1.05646e-12,42116.1,-33.7548], Tmin=(1011.87,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 340,
    label = "C12H10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,B} {4,B}
2  C u0 p0 c0 {1,S} {5,B} {6,B}
3  C u0 p0 c0 {1,B} {8,B} {15,S}
4  C u0 p0 c0 {1,B} {9,B} {16,S}
5  C u0 p0 c0 {2,B} {10,B} {18,S}
6  C u0 p0 c0 {2,B} {12,B} {22,S}
7  C u0 p0 c0 {8,B} {9,B} {13,S}
8  C u0 p0 c0 {3,B} {7,B} {14,S}
9  C u0 p0 c0 {4,B} {7,B} {17,S}
10 C u0 p0 c0 {5,B} {11,B} {19,S}
11 C u0 p0 c0 {10,B} {12,B} {20,S}
12 C u0 p0 c0 {6,B} {11,B} {21,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {12,S}
22 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.42175,0.0795815,-3.79592e-06,-4.62345e-08,2.1377e-11,18323.2,36.4874], Tmin=(200,'K'), Tmax=(1003.86,'K')),
            NASAPolynomial(coeffs=[8.7914,0.0687906,-3.83102e-05,1.03156e-08,-1.08108e-12,14364.4,-26.1578], Tmin=(1003.86,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 341,
    label = "C14H10_10",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {4,B}
2  C u0 p0 c0 {1,B} {6,B} {7,B}
3  C u0 p0 c0 {1,B} {8,B} {9,S}
4  C u0 p0 c0 {1,B} {5,B} {10,S}
5  C u0 p0 c0 {4,B} {11,B} {15,S}
6  C u0 p0 c0 {2,B} {11,B} {17,S}
7  C u0 p0 c0 {2,B} {12,B} {18,S}
8  C u0 p0 c0 {3,B} {12,B} {20,S}
9  C u0 p0 c0 {3,S} {13,D} {21,S}
10 C u0 p0 c0 {4,S} {14,D} {24,S}
11 C u0 p0 c0 {5,B} {6,B} {16,S}
12 C u0 p0 c0 {7,B} {8,B} {19,S}
13 C u0 p0 c0 {9,D} {14,S} {22,S}
14 C u0 p0 c0 {10,D} {13,S} {23,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {11,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {12,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {13,S}
23 H u0 p0 c0 {14,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.50565,0.0944129,-1.67952e-05,-4.16345e-08,2.10843e-11,34293,40.7102], Tmin=(200,'K'), Tmax=(1001.81,'K')),
            NASAPolynomial(coeffs=[10.7326,0.0741268,-4.11679e-05,1.10165e-08,-1.14617e-12,29605.3,-37.1646], Tmin=(1001.81,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 342,
    label = "C14H10_12",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {4,B}
2  C u0 p0 c0 {1,B} {5,B} {9,S}
3  C u0 p0 c0 {1,B} {6,B} {7,B}
4  C u0 p0 c0 {1,B} {8,B} {13,S}
5  C u0 p0 c0 {2,B} {10,B} {16,S}
6  C u0 p0 c0 {3,B} {10,B} {18,S}
7  C u0 p0 c0 {3,B} {11,B} {19,S}
8  C u0 p0 c0 {4,B} {11,B} {21,S}
9  C u0 p0 c0 {2,S} {12,D} {15,S}
10 C u0 p0 c0 {5,B} {6,B} {17,S}
11 C u0 p0 c0 {7,B} {8,B} {20,S}
12 C u0 p0 c0 {9,D} {22,S} {23,S}
13 C u0 p0 c0 {4,S} {14,T}
14 C u0 p0 c0 {13,T} {24,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {12,S}
23 H u0 p0 c0 {12,S}
24 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.68997,0.120571,-8.28107e-05,1.89525e-08,1.87415e-12,53251.5,46.7156], Tmin=(200,'K'), Tmax=(1021.03,'K')),
            NASAPolynomial(coeffs=[15.1493,0.0651904,-3.42733e-05,8.69175e-09,-8.60909e-13,48035.6,-55.1134], Tmin=(1021.03,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 343,
    label = "C14H10_13",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {7,B}
2  C u0 p0 c0 {1,B} {4,B} {11,S}
3  C u0 p0 c0 {1,B} {5,B} {6,B}
4  C u0 p0 c0 {2,B} {8,B} {13,S}
5  C u0 p0 c0 {3,B} {8,B} {16,S}
6  C u0 p0 c0 {3,B} {9,B} {17,S}
7  C u0 p0 c0 {1,B} {10,B} {20,S}
8  C u0 p0 c0 {4,B} {5,B} {15,S}
9  C u0 p0 c0 {6,B} {10,B} {18,S}
10 C u0 p0 c0 {7,B} {9,B} {19,S}
11 C u0 p0 c0 {2,S} {12,D} {21,S}
12 C u0 p0 c0 {11,D} {22,S} {23,S}
13 C u0 p0 c0 {4,S} {14,T}
14 C u0 p0 c0 {13,T} {24,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {12,S}
23 H u0 p0 c0 {12,S}
24 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.69332,0.121406,-8.55777e-05,2.19781e-08,7.84533e-13,51885.1,46.6955], Tmin=(200,'K'), Tmax=(1026.54,'K')),
            NASAPolynomial(coeffs=[15.2012,0.0650353,-3.4113e-05,8.62594e-09,-8.51649e-13,46686.2,-55.2331], Tmin=(1026.54,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 344,
    label = "C14H10_14",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {6,B} {7,B}
2  C u0 p0 c0 {1,B} {5,B} {8,B}
3  C u0 p0 c0 {4,B} {5,B} {11,S}
4  C u0 p0 c0 {3,B} {6,B} {13,S}
5  C u0 p0 c0 {2,B} {3,B} {20,S}
6  C u0 p0 c0 {1,B} {4,B} {15,S}
7  C u0 p0 c0 {1,B} {9,B} {16,S}
8  C u0 p0 c0 {2,B} {10,B} {19,S}
9  C u0 p0 c0 {7,B} {10,B} {17,S}
10 C u0 p0 c0 {8,B} {9,B} {18,S}
11 C u0 p0 c0 {3,S} {12,D} {21,S}
12 C u0 p0 c0 {11,D} {22,S} {23,S}
13 C u0 p0 c0 {4,S} {14,T}
14 C u0 p0 c0 {13,T} {24,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {12,S}
23 H u0 p0 c0 {12,S}
24 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.68526,0.121326,-8.54762e-05,2.195e-08,7.78467e-13,50655.6,46.9596], Tmin=(200,'K'), Tmax=(1026.71,'K')),
            NASAPolynomial(coeffs=[15.1636,0.0650936,-3.41444e-05,8.63292e-09,-8.52174e-13,45467.8,-54.738], Tmin=(1026.71,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 345,
    label = "C14H10_15",
    molecule = 
"""
1  C u0 p0 c0 {4,B} {5,B} {7,B}
2  C u0 p0 c0 {3,B} {5,B} {8,B}
3  C u0 p0 c0 {2,B} {6,B} {9,B}
4  C u0 p0 c0 {1,B} {6,B} {10,B}
5  C u0 p0 c0 {1,B} {2,B} {18,S}
6  C u0 p0 c0 {3,B} {4,B} {23,S}
7  C u0 p0 c0 {1,B} {12,B} {17,S}
8  C u0 p0 c0 {2,B} {13,B} {19,S}
9  C u0 p0 c0 {3,B} {14,B} {22,S}
10 C u0 p0 c0 {4,B} {11,B} {24,S}
11 C u0 p0 c0 {10,B} {12,B} {15,S}
12 C u0 p0 c0 {7,B} {11,B} {16,S}
13 C u0 p0 c0 {8,B} {14,B} {20,S}
14 C u0 p0 c0 {9,B} {13,B} {21,S}
15 H u0 p0 c0 {11,S}
16 H u0 p0 c0 {12,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {13,S}
21 H u0 p0 c0 {14,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.48015,0.0933946,-1.34233e-05,-4.49695e-08,2.21259e-11,23870.5,39.6277], Tmin=(200,'K'), Tmax=(1005.05,'K')),
            NASAPolynomial(coeffs=[10.7999,0.0744269,-4.16276e-05,1.12245e-08,-1.17625e-12,19087.6,-38.8517], Tmin=(1005.05,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 346,
    label = "C14H10_16",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {4,B} {8,B}
2  C u0 p0 c0 {1,B} {6,B} {7,B}
3  C u0 p0 c0 {4,B} {5,B} {9,S}
4  C u0 p0 c0 {1,B} {3,B} {13,S}
5  C u0 p0 c0 {3,B} {6,B} {16,S}
6  C u0 p0 c0 {2,B} {5,B} {17,S}
7  C u0 p0 c0 {2,B} {10,B} {18,S}
8  C u0 p0 c0 {1,B} {11,B} {21,S}
9  C u0 p0 c0 {3,S} {12,D} {15,S}
10 C u0 p0 c0 {7,B} {11,B} {19,S}
11 C u0 p0 c0 {8,B} {10,B} {20,S}
12 C u0 p0 c0 {9,D} {22,S} {23,S}
13 C u0 p0 c0 {4,S} {14,T}
14 C u0 p0 c0 {13,T} {24,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {12,S}
23 H u0 p0 c0 {12,S}
24 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.68046,0.121299,-8.55221e-05,2.20459e-08,7.37385e-13,50193.8,48.1668], Tmin=(200,'K'), Tmax=(1026.93,'K')),
            NASAPolynomial(coeffs=[15.1523,0.0650813,-3.41296e-05,8.6276e-09,-8.51504e-13,45011.4,-53.4419], Tmin=(1026.93,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 347,
    label = "C14H10_9",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {5,B}
2  C u0 p0 c0 {1,B} {4,B} {9,B}
3  C u0 p0 c0 {1,B} {6,B} {10,B}
4  C u0 p0 c0 {2,B} {7,B} {8,B}
5  C u0 p0 c0 {1,B} {12,B} {17,S}
6  C u0 p0 c0 {3,B} {7,B} {18,S}
7  C u0 p0 c0 {4,B} {6,B} {19,S}
8  C u0 p0 c0 {4,B} {13,B} {20,S}
9  C u0 p0 c0 {2,B} {14,B} {23,S}
10 C u0 p0 c0 {3,B} {11,B} {24,S}
11 C u0 p0 c0 {10,B} {12,B} {15,S}
12 C u0 p0 c0 {5,B} {11,B} {16,S}
13 C u0 p0 c0 {8,B} {14,B} {21,S}
14 C u0 p0 c0 {9,B} {13,B} {22,S}
15 H u0 p0 c0 {11,S}
16 H u0 p0 c0 {12,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {13,S}
22 H u0 p0 c0 {14,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.43048,0.0925859,-1.17718e-05,-4.62551e-08,2.24773e-11,21075,40.2857], Tmin=(200,'K'), Tmax=(1005.44,'K')),
            NASAPolynomial(coeffs=[10.6183,0.074719,-4.18434e-05,1.1297e-08,-1.18515e-12,16328,-37.1253], Tmin=(1005.44,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 348,
    label = "C14H11_10",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {5,B} {7,B}
2  C u0 p0 c0 {1,B} {6,B} {8,B}
3  C u0 p0 c0 {4,B} {6,B} {11,S}
4  C u0 p0 c0 {3,B} {5,B} {12,S}
5  C u0 p0 c0 {1,B} {4,B} {15,S}
6  C u0 p0 c0 {2,B} {3,B} {20,S}
7  C u0 p0 c0 {1,B} {9,B} {16,S}
8  C u0 p0 c0 {2,B} {10,B} {19,S}
9  C u0 p0 c0 {7,B} {10,B} {17,S}
10 C u0 p0 c0 {8,B} {9,B} {18,S}
11 C u0 p0 c0 {3,S} {13,D} {21,S}
12 C u0 p0 c0 {4,S} {14,D} {22,S}
13 C u0 p0 c0 {11,D} {23,S} {24,S}
14 C u1 p0 c0 {12,D} {25,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {12,S}
23 H u0 p0 c0 {13,S}
24 H u0 p0 c0 {13,S}
25 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.83736,0.121672,-7.69105e-05,1.16328e-08,4.44757e-12,60609,48.8091], Tmin=(200,'K'), Tmax=(1013.08,'K')),
            NASAPolynomial(coeffs=[14.4472,0.0701657,-3.71262e-05,9.45681e-09,-9.39126e-13,55437.3,-50.7182], Tmin=(1013.08,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 349,
    label = "C14H11_11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {7,S} {15,S} {16,S}
2  C u0 p0 c0 {3,B} {6,S} {9,B}
3  C u0 p0 c0 {2,B} {8,B} {10,S}
4  C u0 p0 c0 {5,B} {8,B} {11,B}
5  C u0 p0 c0 {4,B} {9,B} {12,B}
6  C u1 p0 c0 {1,S} {2,S} {18,S}
7  C u0 p0 c0 {1,S} {10,D} {17,S}
8  C u0 p0 c0 {3,B} {4,B} {20,S}
9  C u0 p0 c0 {2,B} {5,B} {25,S}
10 C u0 p0 c0 {3,S} {7,D} {19,S}
11 C u0 p0 c0 {4,B} {13,B} {21,S}
12 C u0 p0 c0 {5,B} {14,B} {24,S}
13 C u0 p0 c0 {11,B} {14,B} {22,S}
14 C u0 p0 c0 {12,B} {13,B} {23,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {13,S}
23 H u0 p0 c0 {14,S}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.94662,0.100796,-2.29114e-05,-3.87723e-08,2.06251e-11,35633.9,43.9098], Tmin=(200,'K'), Tmax=(999.53,'K')),
            NASAPolynomial(coeffs=[11.3544,0.0766279,-4.22667e-05,1.12373e-08,-1.16257e-12,30723.6,-39.1633], Tmin=(999.53,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 350,
    label = "C14H11_12",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {4,B} {8,B}
2  C u0 p0 c0 {1,B} {3,B} {12,S}
3  C u0 p0 c0 {2,B} {5,B} {9,S}
4  C u0 p0 c0 {1,B} {6,B} {7,B}
5  C u0 p0 c0 {3,B} {6,B} {16,S}
6  C u0 p0 c0 {4,B} {5,B} {17,S}
7  C u0 p0 c0 {4,B} {10,B} {18,S}
8  C u0 p0 c0 {1,B} {11,B} {21,S}
9  C u0 p0 c0 {3,S} {13,D} {15,S}
10 C u0 p0 c0 {7,B} {11,B} {19,S}
11 C u0 p0 c0 {8,B} {10,B} {20,S}
12 C u0 p0 c0 {2,S} {14,D} {22,S}
13 C u0 p0 c0 {9,D} {23,S} {24,S}
14 C u1 p0 c0 {12,D} {25,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {12,S}
23 H u0 p0 c0 {13,S}
24 H u0 p0 c0 {13,S}
25 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.81182,0.120583,-7.37901e-05,8.43104e-09,5.56184e-12,61288.6,48.5134], Tmin=(200,'K'), Tmax=(1009.52,'K')),
            NASAPolynomial(coeffs=[14.3529,0.0703287,-3.72785e-05,9.51875e-09,-9.4786e-13,56110.5,-50.6086], Tmin=(1009.52,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 351,
    label = "C14H11_13",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {7,S} {15,S} {16,S}
2  C u0 p0 c0 {3,S} {4,S} {8,D}
3  C u0 p0 c0 {2,S} {5,B} {12,B}
4  C u0 p0 c0 {2,S} {6,D} {9,S}
5  C u0 p0 c0 {3,B} {10,S} {11,B}
6  C u0 p0 c0 {1,S} {4,D} {18,S}
7  C u1 p0 c0 {1,S} {8,S} {17,S}
8  C u0 p0 c0 {2,D} {7,S} {19,S}
9  C u0 p0 c0 {4,S} {10,D} {20,S}
10 C u0 p0 c0 {5,S} {9,D} {21,S}
11 C u0 p0 c0 {5,B} {13,B} {22,S}
12 C u0 p0 c0 {3,B} {14,B} {25,S}
13 C u0 p0 c0 {11,B} {14,B} {23,S}
14 C u0 p0 c0 {12,B} {13,B} {24,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {13,S}
24 H u0 p0 c0 {14,S}
25 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.9375,0.10062,-2.25081e-05,-3.91226e-08,2.073e-11,35631.2,44.1039], Tmin=(200,'K'), Tmax=(999.65,'K')),
            NASAPolynomial(coeffs=[11.3313,0.0766692,-4.23073e-05,1.12536e-08,-1.16477e-12,30722.6,-38.8368], Tmin=(999.65,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 352,
    label = "C14H11_14",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {7,B} {8,B}
2  C u0 p0 c0 {1,B} {4,B} {9,B}
3  C u0 p0 c0 {4,B} {5,S} {6,B}
4  C u0 p0 c0 {2,B} {3,B} {23,S}
5  C u0 p0 c0 {3,S} {12,D} {16,S}
6  C u0 p0 c0 {3,B} {7,B} {17,S}
7  C u0 p0 c0 {1,B} {6,B} {18,S}
8  C u0 p0 c0 {1,B} {10,B} {19,S}
9  C u0 p0 c0 {2,B} {11,B} {22,S}
10 C u0 p0 c0 {8,B} {11,B} {20,S}
11 C u0 p0 c0 {9,B} {10,B} {21,S}
12 C u0 p0 c0 {5,D} {13,S} {15,S}
13 C u0 p0 c0 {12,S} {14,D} {24,S}
14 C u1 p0 c0 {13,D} {25,S}
15 H u0 p0 c0 {12,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {13,S}
25 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.69005,0.117918,-6.71086e-05,2.2688e-09,7.54826e-12,58815.6,48.9973], Tmin=(200,'K'), Tmax=(1004.75,'K')),
            NASAPolynomial(coeffs=[13.7731,0.0714358,-3.80549e-05,9.75726e-09,-9.74839e-13,53741.5,-46.9514], Tmin=(1004.75,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 353,
    label = "C14H11_15",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {15,S}
2  C u0 p0 c0 {1,S} {7,D} {8,S}
3  C u0 p0 c0 {4,B} {5,S} {10,B}
4  C u0 p0 c0 {3,B} {7,S} {9,B}
5  C u1 p0 c0 {1,S} {3,S} {17,S}
6  C u0 p0 c0 {1,S} {11,D} {16,S}
7  C u0 p0 c0 {2,D} {4,S} {21,S}
8  C u0 p0 c0 {2,S} {12,D} {20,S}
9  C u0 p0 c0 {4,B} {13,B} {22,S}
10 C u0 p0 c0 {3,B} {14,B} {25,S}
11 C u0 p0 c0 {6,D} {12,S} {18,S}
12 C u0 p0 c0 {8,D} {11,S} {19,S}
13 C u0 p0 c0 {9,B} {14,B} {23,S}
14 C u0 p0 c0 {10,B} {13,B} {24,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {11,S}
19 H u0 p0 c0 {12,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {13,S}
24 H u0 p0 c0 {14,S}
25 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.0352,0.101487,-2.29455e-05,-3.95536e-08,2.09905e-11,45795.5,44.9513], Tmin=(200,'K'), Tmax=(1002.55,'K')),
            NASAPolynomial(coeffs=[11.9247,0.0760621,-4.21383e-05,1.12674e-08,-1.17275e-12,40673,-41.6744], Tmin=(1002.55,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 354,
    label = "C14H11_16",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {15,S}
2  C u0 p0 c0 {1,S} {4,B} {8,B}
3  C u0 p0 c0 {1,S} {6,D} {7,S}
4  C u0 p0 c0 {2,B} {9,S} {10,B}
5  C u1 p0 c0 {1,S} {11,S} {16,S}
6  C u0 p0 c0 {3,D} {12,S} {19,S}
7  C u0 p0 c0 {3,S} {9,D} {20,S}
8  C u0 p0 c0 {2,B} {14,B} {25,S}
9  C u0 p0 c0 {4,S} {7,D} {21,S}
10 C u0 p0 c0 {4,B} {13,B} {22,S}
11 C u0 p0 c0 {5,S} {12,D} {17,S}
12 C u0 p0 c0 {6,S} {11,D} {18,S}
13 C u0 p0 c0 {10,B} {14,B} {23,S}
14 C u0 p0 c0 {8,B} {13,B} {24,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {11,S}
18 H u0 p0 c0 {12,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {13,S}
24 H u0 p0 c0 {14,S}
25 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.91674,0.099366,-1.81916e-05,-4.35011e-08,2.21241e-11,41245.7,45.0005], Tmin=(200,'K'), Tmax=(1003.88,'K')),
            NASAPolynomial(coeffs=[11.5241,0.0768184,-4.27406e-05,1.1478e-08,-1.19928e-12,36181.6,-39.3344], Tmin=(1003.88,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 355,
    label = "C14H11_3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {8,B}
2  C u0 p0 c0 {1,B} {4,S} {5,B}
3  C u0 p0 c0 {1,B} {6,B} {7,B}
4  C u0 p0 c0 {2,S} {12,D} {16,S}
5  C u0 p0 c0 {2,B} {9,B} {17,S}
6  C u0 p0 c0 {3,B} {9,B} {19,S}
7  C u0 p0 c0 {3,B} {10,B} {20,S}
8  C u0 p0 c0 {1,B} {11,B} {23,S}
9  C u0 p0 c0 {5,B} {6,B} {18,S}
10 C u0 p0 c0 {7,B} {11,B} {21,S}
11 C u0 p0 c0 {8,B} {10,B} {22,S}
12 C u0 p0 c0 {4,D} {13,S} {15,S}
13 C u0 p0 c0 {12,S} {14,D} {24,S}
14 C u1 p0 c0 {13,D} {25,S}
15 H u0 p0 c0 {12,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {13,S}
25 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.67765,0.117321,-6.53266e-05,4.18339e-10,8.19199e-12,62338,48.5646], Tmin=(200,'K'), Tmax=(1003.47,'K')),
            NASAPolynomial(coeffs=[13.7514,0.0714937,-3.81291e-05,9.79158e-09,-9.79983e-13,57248.1,-47.3411], Tmin=(1003.47,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 356,
    label = "C14H11_4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {15,S}
2  C u1 p0 c0 {1,S} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,B} {10,B}
4  C u0 p0 c0 {3,B} {7,S} {9,B}
5  C u0 p0 c0 {1,S} {7,D} {16,S}
6  C u0 p0 c0 {1,S} {11,D} {17,S}
7  C u0 p0 c0 {4,S} {5,D} {20,S}
8  C u0 p0 c0 {2,S} {13,D} {23,S}
9  C u0 p0 c0 {4,B} {12,B} {19,S}
10 C u0 p0 c0 {3,B} {14,B} {24,S}
11 C u0 p0 c0 {6,D} {13,S} {21,S}
12 C u0 p0 c0 {9,B} {14,B} {18,S}
13 C u0 p0 c0 {8,D} {11,S} {22,S}
14 C u0 p0 c0 {10,B} {12,B} {25,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {12,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {13,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.95323,0.100091,-1.99386e-05,-4.19889e-08,2.16806e-11,42281,44.8356], Tmin=(200,'K'), Tmax=(1003.09,'K')),
            NASAPolynomial(coeffs=[11.6245,0.076583,-4.25245e-05,1.13957e-08,-1.18834e-12,37213.3,-40.0487], Tmin=(1003.09,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 357,
    label = "C14H11_5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {15,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {7,S} {9,B}
4  C u0 p0 c0 {2,B} {8,B} {10,S}
5  C u0 p0 c0 {1,S} {11,D} {16,S}
6  C u0 p0 c0 {1,S} {12,D} {17,S}
7  C u1 p0 c0 {3,S} {11,S} {21,S}
8  C u0 p0 c0 {4,B} {13,B} {18,S}
9  C u0 p0 c0 {3,B} {13,B} {20,S}
10 C u0 p0 c0 {4,S} {14,D} {25,S}
11 C u0 p0 c0 {5,D} {7,S} {22,S}
12 C u0 p0 c0 {6,D} {14,S} {23,S}
13 C u0 p0 c0 {8,B} {9,B} {19,S}
14 C u0 p0 c0 {10,D} {12,S} {24,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {13,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {12,S}
24 H u0 p0 c0 {14,S}
25 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.96652,0.100592,-2.16746e-05,-4.02661e-08,2.11405e-11,44586.3,43.9964], Tmin=(200,'K'), Tmax=(1001.83,'K')),
            NASAPolynomial(coeffs=[11.6413,0.0762898,-4.22059e-05,1.12723e-08,-1.17211e-12,39551.3,-40.8519], Tmin=(1001.83,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 358,
    label = "C14H11_6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {4,B}
2  C u0 p0 c0 {1,B} {6,B} {7,B}
3  C u0 p0 c0 {1,B} {8,B} {11,S}
4  C u0 p0 c0 {1,B} {5,B} {12,S}
5  C u0 p0 c0 {4,B} {9,B} {15,S}
6  C u0 p0 c0 {2,B} {9,B} {17,S}
7  C u0 p0 c0 {2,B} {10,B} {18,S}
8  C u0 p0 c0 {3,B} {10,B} {20,S}
9  C u0 p0 c0 {5,B} {6,B} {16,S}
10 C u0 p0 c0 {7,B} {8,B} {19,S}
11 C u0 p0 c0 {3,S} {13,D} {21,S}
12 C u0 p0 c0 {4,S} {14,D} {22,S}
13 C u0 p0 c0 {11,D} {23,S} {24,S}
14 C u1 p0 c0 {12,D} {25,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {12,S}
23 H u0 p0 c0 {13,S}
24 H u0 p0 c0 {13,S}
25 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.82416,0.120378,-7.27475e-05,7.1508e-09,6.04406e-12,62839.1,48.2134], Tmin=(200,'K'), Tmax=(1008.23,'K')),
            NASAPolynomial(coeffs=[14.4157,0.0702987,-3.7299e-05,9.53665e-09,-9.51143e-13,57625.2,-51.3827], Tmin=(1008.23,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 359,
    label = "C14H11_7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {7,S} {15,S} {16,S}
2  C u0 p0 c0 {3,B} {4,B} {5,B}
3  C u0 p0 c0 {2,B} {6,S} {9,B}
4  C u0 p0 c0 {2,B} {10,B} {11,B}
5  C u0 p0 c0 {2,B} {8,S} {12,B}
6  C u1 p0 c0 {1,S} {3,S} {18,S}
7  C u0 p0 c0 {1,S} {8,D} {17,S}
8  C u0 p0 c0 {5,S} {7,D} {25,S}
9  C u0 p0 c0 {3,B} {13,B} {19,S}
10 C u0 p0 c0 {4,B} {13,B} {21,S}
11 C u0 p0 c0 {4,B} {14,B} {22,S}
12 C u0 p0 c0 {5,B} {14,B} {24,S}
13 C u0 p0 c0 {9,B} {10,B} {20,S}
14 C u0 p0 c0 {11,B} {12,B} {23,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {13,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {14,S}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.3619,0.0915137,-6.12011e-06,-5.1295e-08,2.39777e-11,41570.4,40.825], Tmin=(200,'K'), Tmax=(1002.67,'K')),
            NASAPolynomial(coeffs=[9.50733,0.078418,-4.37421e-05,1.17602e-08,-1.2289e-12,37067.2,-30.8824], Tmin=(1002.67,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 360,
    label = "C14H11_8",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {8,B}
2  C u0 p0 c0 {1,B} {4,B} {11,S}
3  C u0 p0 c0 {1,B} {6,B} {7,B}
4  C u0 p0 c0 {2,B} {5,B} {12,S}
5  C u0 p0 c0 {4,B} {6,B} {15,S}
6  C u0 p0 c0 {3,B} {5,B} {16,S}
7  C u0 p0 c0 {3,B} {9,B} {17,S}
8  C u0 p0 c0 {1,B} {10,B} {20,S}
9  C u0 p0 c0 {7,B} {10,B} {18,S}
10 C u0 p0 c0 {8,B} {9,B} {19,S}
11 C u0 p0 c0 {2,S} {13,D} {21,S}
12 C u0 p0 c0 {4,S} {14,D} {22,S}
13 C u0 p0 c0 {11,D} {23,S} {24,S}
14 C u1 p0 c0 {12,D} {25,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {12,S}
23 H u0 p0 c0 {13,S}
24 H u0 p0 c0 {13,S}
25 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.82678,0.1212,-7.55458e-05,1.02275e-08,4.93781e-12,61032.9,48.461], Tmin=(200,'K'), Tmax=(1011.42,'K')),
            NASAPolynomial(coeffs=[14.4044,0.0702428,-3.71956e-05,9.48434e-09,-9.42967e-13,55859,-50.8831], Tmin=(1011.42,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 361,
    label = "C14H11_9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {7,S} {15,S} {16,S}
2  C u0 p0 c0 {3,B} {5,B} {6,S}
3  C u0 p0 c0 {2,B} {4,B} {12,B}
4  C u0 p0 c0 {3,B} {9,B} {10,B}
5  C u0 p0 c0 {2,B} {8,S} {11,B}
6  C u1 p0 c0 {1,S} {2,S} {18,S}
7  C u0 p0 c0 {1,S} {8,D} {17,S}
8  C u0 p0 c0 {5,S} {7,D} {23,S}
9  C u0 p0 c0 {4,B} {13,B} {20,S}
10 C u0 p0 c0 {4,B} {11,B} {21,S}
11 C u0 p0 c0 {5,B} {10,B} {22,S}
12 C u0 p0 c0 {3,B} {14,B} {24,S}
13 C u0 p0 c0 {9,B} {14,B} {19,S}
14 C u0 p0 c0 {12,B} {13,B} {25,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {13,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.93366,0.100509,-2.22069e-05,-3.93874e-08,2.08055e-11,35130.3,44.1526], Tmin=(200,'K'), Tmax=(999.94,'K')),
            NASAPolynomial(coeffs=[11.3201,0.0767132,-4.23496e-05,1.12693e-08,-1.16678e-12,30218.8,-38.7425], Tmin=(999.94,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 362,
    label = "C14H9_5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {8,B}
2  C u0 p0 c0 {1,B} {4,B} {5,B}
3  C u0 p0 c0 {1,B} {6,B} {7,B}
4  C u0 p0 c0 {2,B} {9,B} {14,B}
5  C u0 p0 c0 {2,B} {12,B} {16,S}
6  C u0 p0 c0 {3,B} {9,B} {18,S}
7  C u0 p0 c0 {3,B} {10,B} {19,S}
8  C u0 p0 c0 {1,B} {11,B} {22,S}
9  C u0 p0 c0 {4,B} {6,B} {17,S}
10 C u0 p0 c0 {7,B} {11,B} {20,S}
11 C u0 p0 c0 {8,B} {10,B} {21,S}
12 C u0 p0 c0 {5,B} {13,B} {15,S}
13 C u0 p0 c0 {12,B} {14,B} {23,S}
14 C u1 p0 c0 {4,B} {13,B}
15 H u0 p0 c0 {12,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.46351,0.0939193,-2.11908e-05,-3.70638e-08,1.96185e-11,52375.6,41.7804], Tmin=(200,'K'), Tmax=(1005.56,'K')),
            NASAPolynomial(coeffs=[11.7115,0.0697127,-3.9018e-05,1.0514e-08,-1.10042e-12,47495.7,-40.6039], Tmin=(1005.56,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 363,
    label = "C14H9_6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {4,B} {9,B}
2  C u0 p0 c0 {1,B} {7,B} {8,B}
3  C u0 p0 c0 {4,B} {5,B} {6,B}
4  C u0 p0 c0 {1,B} {3,B} {14,B}
5  C u0 p0 c0 {3,B} {12,B} {16,S}
6  C u0 p0 c0 {3,B} {7,B} {17,S}
7  C u0 p0 c0 {2,B} {6,B} {18,S}
8  C u0 p0 c0 {2,B} {10,B} {19,S}
9  C u0 p0 c0 {1,B} {11,B} {22,S}
10 C u0 p0 c0 {8,B} {11,B} {20,S}
11 C u0 p0 c0 {9,B} {10,B} {21,S}
12 C u0 p0 c0 {5,B} {13,B} {15,S}
13 C u0 p0 c0 {12,B} {14,B} {23,S}
14 C u1 p0 c0 {4,B} {13,B}
15 H u0 p0 c0 {12,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.44758,0.0936221,-2.04175e-05,-3.77396e-08,1.98171e-11,51562.8,41.6028], Tmin=(200,'K'), Tmax=(1005.75,'K')),
            NASAPolynomial(coeffs=[11.6363,0.0699154,-3.91756e-05,1.05649e-08,-1.10634e-12,46693.6,-40.3778], Tmin=(1005.75,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 364,
    label = "C15H12_18",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {3,B} {7,B}
3  C u0 p0 c0 {2,B} {4,B} {12,B}
4  C u0 p0 c0 {3,B} {5,B} {8,B}
5  C u0 p0 c0 {4,B} {6,B} {9,B}
6  C u0 p0 c0 {5,B} {10,B} {11,B}
7  C u0 p0 c0 {2,B} {13,B} {19,S}
8  C u0 p0 c0 {4,B} {13,B} {21,S}
9  C u0 p0 c0 {5,B} {14,B} {22,S}
10 C u0 p0 c0 {6,B} {15,B} {25,S}
11 C u0 p0 c0 {6,B} {12,B} {26,S}
12 C u0 p0 c0 {3,B} {11,B} {27,S}
13 C u0 p0 c0 {7,B} {8,B} {20,S}
14 C u0 p0 c0 {9,B} {15,B} {23,S}
15 C u0 p0 c0 {10,B} {14,B} {24,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {13,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {14,S}
24 H u0 p0 c0 {15,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {11,S}
27 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.66195,0.112043,-3.42497e-05,-3.23176e-08,1.91747e-11,16833.6,46.8121], Tmin=(200,'K'), Tmax=(993.76,'K')),
            NASAPolynomial(coeffs=[11.6832,0.0826934,-4.49558e-05,1.17655e-08,-1.19844e-12,11785.5,-40.9954], Tmin=(993.76,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 365,
    label = "C16H10_12",
    molecule = 
"""
1  C u0 p0 c0 {4,B} {5,B} {6,B}
2  C u0 p0 c0 {3,B} {5,S} {7,B}
3  C u0 p0 c0 {2,B} {4,S} {8,B}
4  C u0 p0 c0 {1,B} {3,S} {9,B}
5  C u0 p0 c0 {1,B} {2,S} {12,B}
6  C u0 p0 c0 {1,B} {10,B} {11,B}
7  C u0 p0 c0 {2,B} {14,B} {19,S}
8  C u0 p0 c0 {3,B} {13,B} {20,S}
9  C u0 p0 c0 {4,B} {15,B} {21,S}
10 C u0 p0 c0 {6,B} {15,B} {23,S}
11 C u0 p0 c0 {6,B} {16,B} {24,S}
12 C u0 p0 c0 {5,B} {16,B} {26,S}
13 C u0 p0 c0 {8,B} {14,B} {17,S}
14 C u0 p0 c0 {7,B} {13,B} {18,S}
15 C u0 p0 c0 {9,B} {10,B} {22,S}
16 C u0 p0 c0 {11,B} {12,B} {25,S}
17 H u0 p0 c0 {13,S}
18 H u0 p0 c0 {14,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {15,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {16,S}
26 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.45016,0.105785,-2.00032e-05,-4.61218e-08,2.35389e-11,29903.2,45.1824], Tmin=(200,'K'), Tmax=(1006.69,'K')),
            NASAPolynomial(coeffs=[12.4407,0.0807825,-4.5497e-05,1.23157e-08,-1.29306e-12,24368.5,-47.0175], Tmin=(1006.69,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 366,
    label = "C16H10_13",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {6,B}
2  C u0 p0 c0 {1,B} {4,B} {5,B}
3  C u0 p0 c0 {1,B} {7,B} {8,B}
4  C u0 p0 c0 {2,B} {9,B} {10,B}
5  C u0 p0 c0 {2,B} {11,B} {12,B}
6  C u0 p0 c0 {1,B} {13,B} {14,B}
7  C u0 p0 c0 {3,B} {15,B} {18,S}
8  C u0 p0 c0 {3,B} {9,B} {19,S}
9  C u0 p0 c0 {4,B} {8,B} {20,S}
10 C u0 p0 c0 {4,B} {16,B} {21,S}
11 C u0 p0 c0 {5,B} {16,B} {23,S}
12 C u0 p0 c0 {5,B} {13,B} {24,S}
13 C u0 p0 c0 {6,B} {12,B} {25,S}
14 C u0 p0 c0 {6,B} {15,B} {26,S}
15 C u0 p0 c0 {7,B} {14,B} {17,S}
16 C u0 p0 c0 {10,B} {11,B} {22,S}
17 H u0 p0 c0 {15,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {16,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {13,S}
26 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.35997,0.10427,-1.67087e-05,-4.87844e-08,2.4288e-11,22569.7,42.7438], Tmin=(200,'K'), Tmax=(1007.34,'K')),
            NASAPolynomial(coeffs=[12.1076,0.0813953,-4.59557e-05,1.24694e-08,-1.31195e-12,17094.9,-47.5303], Tmin=(1007.34,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 367,
    label = "C16H10_14",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {5,B}
2  C u0 p0 c0 {1,B} {4,B} {10,B}
3  C u0 p0 c0 {1,B} {6,B} {7,B}
4  C u0 p0 c0 {2,B} {8,B} {9,B}
5  C u0 p0 c0 {1,B} {11,B} {15,S}
6  C u0 p0 c0 {3,B} {12,B} {19,S}
7  C u0 p0 c0 {3,B} {8,B} {20,S}
8  C u0 p0 c0 {4,B} {7,B} {21,S}
9  C u0 p0 c0 {4,B} {13,B} {22,S}
10 C u0 p0 c0 {2,B} {14,B} {25,S}
11 C u0 p0 c0 {5,B} {12,B} {17,S}
12 C u0 p0 c0 {6,B} {11,B} {18,S}
13 C u0 p0 c0 {9,B} {14,B} {23,S}
14 C u0 p0 c0 {10,B} {13,B} {24,S}
15 C u0 p0 c0 {5,S} {16,T}
16 C u0 p0 c0 {15,T} {26,S}
17 H u0 p0 c0 {11,S}
18 H u0 p0 c0 {12,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {13,S}
24 H u0 p0 c0 {14,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {16,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.45884,0.126223,-7.04422e-05,-1.13466e-09,9.72878e-12,50992.4,50.7638], Tmin=(200,'K'), Tmax=(1005.62,'K')),
            NASAPolynomial(coeffs=[15.9801,0.0732185,-3.95173e-05,1.02763e-08,-1.04151e-12,45048.7,-60.9], Tmin=(1005.62,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 368,
    label = "C16H10_15",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {6,B}
2  C u0 p0 c0 {1,B} {4,B} {10,B}
3  C u0 p0 c0 {1,B} {5,B} {7,B}
4  C u0 p0 c0 {2,B} {8,B} {9,B}
5  C u0 p0 c0 {3,B} {11,B} {15,S}
6  C u0 p0 c0 {1,B} {12,B} {19,S}
7  C u0 p0 c0 {3,B} {8,B} {20,S}
8  C u0 p0 c0 {4,B} {7,B} {21,S}
9  C u0 p0 c0 {4,B} {13,B} {22,S}
10 C u0 p0 c0 {2,B} {14,B} {25,S}
11 C u0 p0 c0 {5,B} {12,B} {17,S}
12 C u0 p0 c0 {6,B} {11,B} {18,S}
13 C u0 p0 c0 {9,B} {14,B} {23,S}
14 C u0 p0 c0 {10,B} {13,B} {24,S}
15 C u0 p0 c0 {5,S} {16,T}
16 C u0 p0 c0 {15,T} {26,S}
17 H u0 p0 c0 {11,S}
18 H u0 p0 c0 {12,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {13,S}
24 H u0 p0 c0 {14,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {16,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.4623,0.126455,-7.12224e-05,-2.99511e-10,9.43761e-12,48845.6,49.9623], Tmin=(200,'K'), Tmax=(1005.91,'K')),
            NASAPolynomial(coeffs=[15.9721,0.0731925,-3.94728e-05,1.02552e-08,-1.03837e-12,42915.9,-61.6127], Tmin=(1005.91,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 369,
    label = "C16H12_18",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {4,S} {19,S} {20,S}
3  C u0 p0 c0 {1,S} {5,B} {9,B}
4  C u0 p0 c0 {2,S} {5,B} {10,B}
5  C u0 p0 c0 {3,B} {4,B} {7,B}
6  C u0 p0 c0 {7,B} {8,B} {11,B}
7  C u0 p0 c0 {5,B} {6,B} {13,B}
8  C u0 p0 c0 {6,B} {9,B} {12,B}
9  C u0 p0 c0 {3,B} {8,B} {25,S}
10 C u0 p0 c0 {4,B} {16,B} {26,S}
11 C u0 p0 c0 {6,B} {15,B} {23,S}
12 C u0 p0 c0 {8,B} {14,B} {24,S}
13 C u0 p0 c0 {7,B} {16,B} {28,S}
14 C u0 p0 c0 {12,B} {15,B} {21,S}
15 C u0 p0 c0 {11,B} {14,B} {22,S}
16 C u0 p0 c0 {10,B} {13,B} {27,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {14,S}
22 H u0 p0 c0 {15,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {16,S}
28 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.74857,0.109939,-1.66804e-05,-5.14876e-08,2.55137e-11,20632.8,47.5334], Tmin=(200,'K'), Tmax=(1000.48,'K')),
            NASAPolynomial(coeffs=[11.2677,0.0888381,-4.94149e-05,1.32176e-08,-1.37292e-12,15279.3,-40.4824], Tmin=(1000.48,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 370,
    label = "C16H9_2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,B} {4,B} {5,B}
2  C u0 p0 c0 {3,B} {6,B} {12,B}
3  C u0 p0 c0 {1,B} {2,B} {11,B}
4  C u0 p0 c0 {1,B} {7,B} {8,S}
5  C u0 p0 c0 {1,B} {9,S} {10,B}
6  C u0 p0 c0 {2,B} {7,B} {14,B}
7  C u0 p0 c0 {4,B} {6,B} {18,S}
8  C u0 p0 c0 {4,S} {9,D} {19,S}
9  C u0 p0 c0 {5,S} {8,D} {20,S}
10 C u0 p0 c0 {5,B} {13,B} {21,S}
11 C u0 p0 c0 {3,B} {13,B} {23,S}
12 C u0 p0 c0 {2,B} {15,B} {17,S}
13 C u0 p0 c0 {10,B} {11,B} {22,S}
14 C u0 p0 c0 {6,B} {16,B} {25,S}
15 C u0 p0 c0 {12,B} {16,B} {24,S}
16 C u1 p0 c0 {14,B} {15,B}
17 H u0 p0 c0 {12,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {13,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {15,S}
25 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.60882,0.109159,-3.37342e-05,-3.34724e-08,1.96936e-11,63884.6,46.296], Tmin=(200,'K'), Tmax=(1007.22,'K')),
            NASAPolynomial(coeffs=[14.0582,0.0748973,-4.20881e-05,1.13591e-08,-1.18913e-12,58101.8,-53.9358], Tmin=(1007.22,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 371,
    label = "C16H9_3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {5,B} {6,B}
2  C u0 p0 c0 {1,B} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {8,B} {9,B}
4  C u0 p0 c0 {2,B} {10,B} {11,B}
5  C u0 p0 c0 {1,B} {7,B} {14,B}
6  C u0 p0 c0 {1,B} {12,B} {15,B}
7  C u0 p0 c0 {5,B} {8,B} {17,S}
8  C u0 p0 c0 {3,B} {7,B} {18,S}
9  C u0 p0 c0 {3,B} {13,B} {19,S}
10 C u0 p0 c0 {4,B} {13,B} {21,S}
11 C u0 p0 c0 {4,B} {12,B} {22,S}
12 C u0 p0 c0 {6,B} {11,B} {23,S}
13 C u0 p0 c0 {9,B} {10,B} {20,S}
14 C u0 p0 c0 {5,B} {16,B} {24,S}
15 C u0 p0 c0 {6,B} {16,B} {25,S}
16 C u1 p0 c0 {14,B} {15,B}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {13,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {12,S}
24 H u0 p0 c0 {14,S}
25 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.42404,0.10612,-2.72918e-05,-3.85958e-08,2.11287e-11,54330,44.9824], Tmin=(200,'K'), Tmax=(1007.64,'K')),
            NASAPolynomial(coeffs=[13.3055,0.0762001,-4.29836e-05,1.16357e-08,-1.22087e-12,48703,-50.8797], Tmin=(1007.64,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 372,
    label = "C18H10_1",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {6,B}
2  C u0 p0 c0 {1,B} {4,B} {5,B}
3  C u0 p0 c0 {1,B} {8,B} {10,B}
4  C u0 p0 c0 {2,B} {11,B} {12,B}
5  C u0 p0 c0 {2,B} {13,B} {14,B}
6  C u0 p0 c0 {1,B} {9,B} {15,B}
7  C u0 p0 c0 {8,B} {9,B} {17,S}
8  C u0 p0 c0 {3,B} {7,B} {19,S}
9  C u0 p0 c0 {6,B} {7,B} {27,S}
10 C u0 p0 c0 {3,B} {11,B} {20,S}
11 C u0 p0 c0 {4,B} {10,B} {21,S}
12 C u0 p0 c0 {4,B} {16,B} {22,S}
13 C u0 p0 c0 {5,B} {16,B} {24,S}
14 C u0 p0 c0 {5,B} {15,B} {25,S}
15 C u0 p0 c0 {6,B} {14,B} {26,S}
16 C u0 p0 c0 {12,B} {13,B} {23,S}
17 C u0 p0 c0 {7,S} {18,T}
18 C u0 p0 c0 {17,T} {28,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {12,S}
23 H u0 p0 c0 {16,S}
24 H u0 p0 c0 {13,S}
25 H u0 p0 c0 {14,S}
26 H u0 p0 c0 {15,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {18,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.42618,0.138671,-7.73594e-05,-1.85024e-09,1.09792e-11,50359,52.6301], Tmin=(200,'K'), Tmax=(1007.24,'K')),
            NASAPolynomial(coeffs=[17.5465,0.0796717,-4.3408e-05,1.13609e-08,-1.15636e-12,43693.4,-72.3133], Tmin=(1007.24,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 373,
    label = "C18H10_2",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {5,B} {6,B}
2  C u0 p0 c0 {1,B} {3,B} {7,B}
3  C u0 p0 c0 {2,B} {4,B} {8,B}
4  C u0 p0 c0 {3,B} {5,S} {15,B}
5  C u0 p0 c0 {1,B} {4,S} {16,B}
6  C u0 p0 c0 {1,B} {9,B} {10,B}
7  C u0 p0 c0 {2,B} {11,B} {12,B}
8  C u0 p0 c0 {3,B} {13,B} {14,B}
9  C u0 p0 c0 {6,B} {17,B} {20,S}
10 C u0 p0 c0 {6,B} {11,B} {21,S}
11 C u0 p0 c0 {7,B} {10,B} {22,S}
12 C u0 p0 c0 {7,B} {13,B} {23,S}
13 C u0 p0 c0 {8,B} {12,B} {24,S}
14 C u0 p0 c0 {8,B} {18,B} {25,S}
15 C u0 p0 c0 {4,B} {18,B} {27,S}
16 C u0 p0 c0 {5,B} {17,B} {28,S}
17 C u0 p0 c0 {9,B} {16,B} {19,S}
18 C u0 p0 c0 {14,B} {15,B} {26,S}
19 H u0 p0 c0 {17,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {12,S}
24 H u0 p0 c0 {13,S}
25 H u0 p0 c0 {14,S}
26 H u0 p0 c0 {18,S}
27 H u0 p0 c0 {15,S}
28 H u0 p0 c0 {16,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.40683,0.117869,-2.58509e-05,-4.78774e-08,2.51165e-11,38716.4,48.2123], Tmin=(200,'K'), Tmax=(1008.64,'K')),
            NASAPolynomial(coeffs=[14.0581,0.087198,-4.94241e-05,1.34317e-08,-1.4136e-12,32423.3,-57.593], Tmin=(1008.64,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 374,
    label = "C18H12_7",
    molecule = 
"""
1  C u0 p0 c0 {3,B} {5,B} {7,B}
2  C u0 p0 c0 {3,B} {4,B} {9,B}
3  C u0 p0 c0 {1,B} {2,B} {10,B}
4  C u0 p0 c0 {2,B} {6,B} {13,B}
5  C u0 p0 c0 {1,B} {8,B} {14,B}
6  C u0 p0 c0 {4,B} {11,B} {12,B}
7  C u0 p0 c0 {1,B} {16,B} {21,S}
8  C u0 p0 c0 {5,B} {9,B} {22,S}
9  C u0 p0 c0 {2,B} {8,B} {23,S}
10 C u0 p0 c0 {3,B} {11,B} {24,S}
11 C u0 p0 c0 {6,B} {10,B} {25,S}
12 C u0 p0 c0 {6,B} {17,B} {26,S}
13 C u0 p0 c0 {4,B} {18,B} {29,S}
14 C u0 p0 c0 {5,B} {15,B} {30,S}
15 C u0 p0 c0 {14,B} {16,B} {19,S}
16 C u0 p0 c0 {7,B} {15,B} {20,S}
17 C u0 p0 c0 {12,B} {18,B} {27,S}
18 C u0 p0 c0 {13,B} {17,B} {28,S}
19 H u0 p0 c0 {15,S}
20 H u0 p0 c0 {16,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {12,S}
27 H u0 p0 c0 {17,S}
28 H u0 p0 c0 {18,S}
29 H u0 p0 c0 {13,S}
30 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.13433,0.129397,-3.92272e-05,-3.94162e-08,2.31062e-11,27633.8,52.7451], Tmin=(200,'K'), Tmax=(1001.77,'K')),
            NASAPolynomial(coeffs=[14.6782,0.0917067,-5.07915e-05,1.3533e-08,-1.40116e-12,21185.3,-59.0731], Tmin=(1001.77,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 375,
    label = "C20H12_1",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {4,B} {6,B}
2  C u0 p0 c0 {1,B} {7,B} {8,B}
3  C u0 p0 c0 {4,B} {5,B} {10,B}
4  C u0 p0 c0 {1,B} {3,B} {17,B}
5  C u0 p0 c0 {3,B} {9,B} {11,B}
6  C u0 p0 c0 {1,B} {9,B} {12,B}
7  C u0 p0 c0 {2,B} {13,B} {14,B}
8  C u0 p0 c0 {2,B} {15,B} {16,B}
9  C u0 p0 c0 {5,B} {6,B} {25,S}
10 C u0 p0 c0 {3,B} {19,B} {23,S}
11 C u0 p0 c0 {5,B} {18,B} {24,S}
12 C u0 p0 c0 {6,B} {13,B} {26,S}
13 C u0 p0 c0 {7,B} {12,B} {27,S}
14 C u0 p0 c0 {7,B} {20,B} {28,S}
15 C u0 p0 c0 {8,B} {20,B} {30,S}
16 C u0 p0 c0 {8,B} {17,B} {31,S}
17 C u0 p0 c0 {4,B} {16,B} {32,S}
18 C u0 p0 c0 {11,B} {19,B} {21,S}
19 C u0 p0 c0 {10,B} {18,B} {22,S}
20 C u0 p0 c0 {14,B} {15,B} {29,S}
21 H u0 p0 c0 {18,S}
22 H u0 p0 c0 {19,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {12,S}
27 H u0 p0 c0 {13,S}
28 H u0 p0 c0 {14,S}
29 H u0 p0 c0 {20,S}
30 H u0 p0 c0 {15,S}
31 H u0 p0 c0 {16,S}
32 H u0 p0 c0 {17,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.08305,0.141453,-4.50954e-05,-4.10876e-08,2.46453e-11,30113.6,56.5416], Tmin=(200,'K'), Tmax=(1003.67,'K')),
            NASAPolynomial(coeffs=[16.2058,0.0982992,-5.48212e-05,1.46715e-08,-1.5232e-12,22937.4,-68.3598], Tmin=(1003.67,'K'), Tmax=(3200,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3200,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

