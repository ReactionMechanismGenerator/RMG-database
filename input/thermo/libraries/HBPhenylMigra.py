#!/usr/bin/env python
# encoding: utf-8

name = "HB PhenylMigration"
shortDesc = u"sarahkha ab initio calculations"
longDesc = u"""
Calculated at the CBS-QB3 level with 1D HR
/home/sarahkha/Cantherm/HB/PhenylMig
"""
entry(
    index = 1,
    label = "HBrad2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u1 p0 c0 {4,S} {6,S} {7,S}
6  H u0 p0 c0 {5,S}
7  C u0 p0 c0 {5,S} {8,S} {23,S} {24,S}
8  C u0 p0 c0 {7,S} {9,S} {13,D}
9  C u0 p0 c0 {8,S} {10,D} {25,S}
10 C u0 p0 c0 {9,D} {11,S} {26,S}
11 C u0 p0 c0 {10,S} {12,D} {27,S}
12 C u0 p0 c0 {11,D} {13,S} {28,S}
13 C u0 p0 c0 {8,D} {12,S} {29,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {13,S}
""",
   thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [2.48737, 0.168502, -0.0007184, 1.91518e-06, -1.7376e-09, 12131, 19.0368],
                Tmin = (10, 'K'),
                Tmax = (383.765, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-3.34058, 0.115981, -7.04035e-05, 2.04241e-08, -2.28132e-12, 13412.3, 52.4385],
                Tmin = (383.765, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (100.791, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (681.787, 'J/(mol*K)'),
    ),
    shortDesc = u"""sarahkha Cantherm from Lawremce CBSQB3 calculations Feb,6 2018 """,
    longDesc = 
u"""
/home/sarahkha/Cantherm/HB/PhenylMig/wHBrad2/species/HBrad2
""",
)

entry(
    index = 2,
    label = "HBrad3",
    molecule = 
"""
multiplicity 2
1    C u0 p0 c0 {2,D} {13,S} {14,S}
2    C u0 p0 c0 {1,D} {3,S} {15,S}
3    C u0 p0 c0 {2,S} {4,S} {11,D}
4    C u0 p0 c0 {3,S} {5,S} {16,S} {17,S}
5    C u0 p0 c0 {4,S} {6,S} {18,S} {19,S}
6    C u1 p0 c0 {5,S} {7,S} {8,S}
7    H u0 p0 c0 {6,S}
8    C u0 p0 c0 {6,S} {9,S} {20,S} {21,S}
9    C u0 p0 c0 {8,S} {10,S} {22,S} {23,S}
10   C u0 p0 c0 {9,S} {24,S} {25,S} {26,S}
11   C u0 p0 c0 {3,D} {12,S} {27,S}
12   C u0 p0 c0 {11,S} {13,D} {28,S}
13   C u0 p0 c0 {1,S} {12,D} {29,S}
14   H u0 p0 c0 {1,S}
15   H u0 p0 c0 {2,S}
16   H u0 p0 c0 {4,S}
17   H u0 p0 c0 {4,S}
18   H u0 p0 c0 {5,S}
19   H u0 p0 c0 {5,S}
20   H u0 p0 c0 {8,S}
21   H u0 p0 c0 {8,S}
22   H u0 p0 c0 {9,S}
23   H u0 p0 c0 {9,S}
24   H u0 p0 c0 {10,S}
25   H u0 p0 c0 {10,S}
26   H u0 p0 c0 {10,S}
27   H u0 p0 c0 {11,S}
28   H u0 p0 c0 {12,S}
29   H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [2.59161, 0.1558, -0.000616415, 1.64751e-06, -1.50473e-09, 11949.5, 18.9421],
                Tmin = (10, 'K'),
                Tmax = (383.709, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-3.20903, 0.116274, -7.09999e-05, 2.07296e-08, -2.32958e-12, 13130.8, 50.9628],
                Tmin = (383.709, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (99.2912, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (681.787, 'J/(mol*K)'),
    ),
shortDesc = u"""sarahkha cantherm from Lawrence CBSQB3 calculations on Pharos, Feb. 8, 2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/HB/PhenylMig/wHBrad3/species/HBrad3
""",
)

entry(
    index = 3,
    label = "HBrad4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {19,S} {20,S}
6  C u0 p0 c0 {5,S} {7,S} {21,S} {22,S}
7  C u0 p0 c0 {6,S} {8,S} {23,S} {24,S}
8  C u0 p0 c0 {7,S} {9,S} {13,D}
9  C u0 p0 c0 {8,S} {10,D} {25,S}
10 C u0 p0 c0 {9,D} {11,S} {26,S}
11 C u0 p0 c0 {10,S} {12,D} {27,S}
12 C u0 p0 c0 {11,D} {13,S} {28,S}
13 C u0 p0 c0 {8,D} {12,S} {29,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
       polynomials = [
           NASAPolynomial(
                coeffs = [2.56382, 0.159389, -0.000647815, 1.73512e-06, -1.58477e-09, 11965.1, 19.5223],
                Tmin = (10, 'K'),
                Tmax = (383.139, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-3.31271, 0.1164, -7.10206e-05, 2.07116e-08, -2.3247e-12, 13181.2, 52.2297],
                Tmin = (383.139, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (99.4175, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (681.787, 'J/(mol*K)'),
    ),
shortDesc = u"""sarahkha cantherm from Lawrence CBSQB3 calculations on Pharos, Feb. 8, 2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/HB/PhenylMig/wHBrad4/species/HBrad4
""",
)

entry(
    index = 4,
    label = "HBrad5",
    molecule = 
"""
multiplicity 2
1     C u0 p0 c0 {2,D} {13,S} {14,S}
2     C u0 p0 c0 {1,D} {3,S} {15,S}
3     C u0 p0 c0 {2,S} {4,S} {11,D}
4     C u0 p0 c0 {3,S} {5,S} {16,S} {17,S}
5     C u0 p0 c0 {4,S} {6,S} {18,S} {19,S}
6     C u0 p0 c0 {5,S} {7,S} {20,S} {21,S}
7     C u0 p0 c0 {6,S} {8,S} {22,S} {23,S}
8     C u1 p0 c0 {7,S} {9,S} {10,S}
9     H u0 p0 c0 {8,S}
10    C u0 p0 c0 {8,S} {24,S} {25,S} {26,S}
11    C u0 p0 c0 {3,D} {12,S} {27,S}
12    C u0 p0 c0 {11,S} {13,D} {28,S}
13    C u0 p0 c0 {1,S} {12,D} {29,S}
14    H u0 p0 c0 {1,S}
15    H u0 p0 c0 {2,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {4,S}
18    H u0 p0 c0 {5,S}
19    H u0 p0 c0 {5,S}
20    H u0 p0 c0 {6,S}
21    H u0 p0 c0 {6,S}
22    H u0 p0 c0 {7,S}
23    H u0 p0 c0 {7,S}
24    H u0 p0 c0 {10,S}
25    H u0 p0 c0 {10,S}
26    H u0 p0 c0 {10,S}
27    H u0 p0 c0 {11,S}
28    H u0 p0 c0 {12,S}
29    H u0 p0 c0 {13,S}
""",
 thermo = NASA(
      polynomials = [
            NASAPolynomial(
                coeffs = [2.38548, 0.178647, -0.000765265, 1.98892e-06, -1.77131e-09, 11729.9, 17.6205],
                Tmin = (10, 'K'),
                Tmax = (386.99, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-2.53193, 0.114237, -6.89447e-05, 1.99004e-08, -2.21347e-12, 12973.4, 47.8247],
                Tmin = (386.99, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (97.4561, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (681.787, 'J/(mol*K)'),
    ),
    shortDesm = u"""sarahkha CBSQB3 calculations entered Feb. 6, 2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/HB/PhenylMig/wHBrad5/species/HBrad5
""",
)

entry(
    index = 5,
    label = "2HBrad",
    molecule = 
"""
multiplicity 2
1      C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
2      C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3      C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4      C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5      C u0 p0 c0 {4,S} {6,S} {12,S} {24,S}
6      C u0 p0 c0 {5,S} {7,D} {11,S}
7      C u0 p0 c0 {6,D} {8,S} {25,S}
8      C u0 p0 c0 {7,S} {9,D} {26,S}
9      C u0 p0 c0 {8,D} {10,S} {27,S}
10     C u0 p0 c0 {9,S} {11,D} {28,S}
11     C u0 p0 c0 {6,S} {10,D} {29,S}
12     C u1 p0 c0 {5,S} {13,S} {14,S}
13     H u0 p0 c0 {12,S}
14     H u0 p0 c0 {12,S}
15     H u0 p0 c0 {1,S}
16     H u0 p0 c0 {1,S}
17     H u0 p0 c0 {1,S}
18     H u0 p0 c0 {2,S}
19     H u0 p0 c0 {2,S}
20     H u0 p0 c0 {3,S}
21     H u0 p0 c0 {3,S}
22     H u0 p0 c0 {4,S}
23     H u0 p0 c0 {4,S}
24     H u0 p0 c0 {5,S}
25     H u0 p0 c0 {7,S}
26     H u0 p0 c0 {8,S}
27     H u0 p0 c0 {9,S}
28     H u0 p0 c0 {10,S}
29     H u0 p0 c0 {11,S}
""",
   thermo = NASA(
      polynomials = [
           NASAPolynomial(
                coeffs = [3.71362, 0.0959463, -4.54587e-05, 6.40983e-09, 6.14928e-13, 12273.3, 15.755],
                Tmin = (10, 'K'),
                Tmax = (1635.26, 'K'),
            ),
           NASAPolynomial(
                coeffs = [47.9868, 0.0154306, 2.91474e-06, -2.92244e-09, 4.53427e-13, -5920.7, -230.968],
                Tmin = (1635.26, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (101.99, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (681.787, 'J/(mol*K)'),
),
    shortDesc = u"""sarahkha CBSQB3 calculations Feb. 6,2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/HB/PhenylMig/wHBrad2/species/2HB
""",
)

entry(
    index = 6,
    label = "3HBrad",
    molecule = 
"""
multiplicity 2
1     C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
2     C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3     C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4     C u0 p0 c0 {3,S} {5,S} {11,S} {22,S}
5     C u0 p0 c0 {4,S} {6,D} {10,S}
6     C u0 p0 c0 {5,D} {7,S} {23,S}
7     C u0 p0 c0 {6,S} {8,D} {24,S}
8     C u0 p0 c0 {7,D} {9,S} {25,S}
9     C u0 p0 c0 {8,S} {10,D} {26,S}
10    C u0 p0 c0 {5,S} {9,D} {27,S}
11    C u0 p0 c0 {4,S} {12,S} {28,S} {29,S}
12    C u1 p0 c0 {11,S} {13,S} {14,S}
13    H u0 p0 c0 {12,S}
14    H u0 p0 c0 {12,S}
15    H u0 p0 c0 {1,S}
16    H u0 p0 c0 {1,S}
17    H u0 p0 c0 {1,S}
18    H u0 p0 c0 {2,S}
19    H u0 p0 c0 {2,S}
20    H u0 p0 c0 {3,S}
21    H u0 p0 c0 {3,S}
22    H u0 p0 c0 {4,S}
23    H u0 p0 c0 {6,S}
24    H u0 p0 c0 {7,S}
25    H u0 p0 c0 {8,S}
26    H u0 p0 c0 {9,S}
27    H u0 p0 c0 {10,S}
28    H u0 p0 c0 {11,S}
29    H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [2.77552, 0.125356, -0.000257759, 5.72544e-07, -4.9737e-10, 12012.4, 20.2648],
                Tmin = (10, 'K'),
                Tmax = (399.576, 'K'),
            ),
            NASAPolynomial(
                coeffs = [0.100075, 0.113867, -7.0963e-05, 2.11838e-08, -2.43139e-12, 12531.8, 34.541],
                Tmin = (399.576, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (99.8481, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (681.787, 'J/(mol*K)'),
),
    shortDesc = u"""sarahkha CBSQB3 calculations Feb. 6,2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/HB/PhenylMig/wHBrad3/species/3HB
""",
)

entry(
    index = 7,
    label = "4HBrad",
    molecule = 
"""
multiplicity 2
1    C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
2    C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3    C u0 p0 c0 {2,S} {4,S} {10,S} {20,S}
4    C u0 p0 c0 {3,S} {5,D} {9,S}
5    C u0 p0 c0 {4,D} {6,S} {21,S}
6    C u0 p0 c0 {5,S} {7,D} {22,S}
7    C u0 p0 c0 {6,D} {8,S} {23,S}
8    C u0 p0 c0 {7,S} {9,D} {24,S}
9    C u0 p0 c0 {4,S} {8,D} {25,S}
10   C u0 p0 c0 {3,S} {11,S} {26,S} {27,S}
11   C u0 p0 c0 {10,S} {12,S} {28,S} {29,S}
12   C u1 p0 c0 {11,S} {13,S} {14,S}
13   H u0 p0 c0 {12,S}
14   H u0 p0 c0 {12,S}
15   H u0 p0 c0 {1,S}
16   H u0 p0 c0 {1,S}
17   H u0 p0 c0 {1,S}
18   H u0 p0 c0 {2,S}
19   H u0 p0 c0 {2,S}
20   H u0 p0 c0 {3,S}
21   H u0 p0 c0 {5,S}
22   H u0 p0 c0 {6,S}
23   H u0 p0 c0 {7,S}
24   H u0 p0 c0 {8,S}
25   H u0 p0 c0 {9,S}
26   H u0 p0 c0 {10,S}
27   H u0 p0 c0 {10,S}
28   H u0 p0 c0 {11,S}
29   H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [2.88153, 0.110597, -0.000146414, 2.74364e-07, -2.31714e-10, 11947, 17.2155],
                Tmin = (10, 'K'),
                Tmax = (419.648, 'K'),
            ),
            NASAPolynomial(
                coeffs = [0.299109, 0.112108, -6.9231e-05, 2.05522e-08, -2.35084e-12, 12367.2, 29.8557],
                Tmin = (419.648, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (99.3041, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (681.787, 'J/(mol*K)'),
    ),
),
    shortDesc = u"""sarahkha CBSQB3 calculations Feb.6,2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/HB/PhenylMig/wHBrad4/species/4HB
""",
)

entry(
    index = 8,
    label = "5HBrad",
    molecule = 
"""
multiplicity 2
1    C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
2    C u0 p0 c0 {1,S} {3,S} {9,S} {18,S}
3    C u0 p0 c0 {2,S} {4,D} {8,S}
4    C u0 p0 c0 {3,D} {5,S} {19,S}
5    C u0 p0 c0 {4,S} {6,D} {20,S}
6    C u0 p0 c0 {5,D} {7,S} {21,S}
7    C u0 p0 c0 {6,S} {8,D} {22,S}
8    C u0 p0 c0 {3,S} {7,D} {23,S}
9    C u0 p0 c0 {2,S} {10,S} {24,S} {25,S}
10   C u0 p0 c0 {9,S} {11,S} {26,S} {27,S}
11   C u0 p0 c0 {10,S} {12,S} {28,S} {29,S}
12   C u1 p0 c0 {11,S} {13,S} {14,S}
13   H u0 p0 c0 {12,S}
14   H u0 p0 c0 {12,S}
15   H u0 p0 c0 {1,S}
16   H u0 p0 c0 {1,S}
17   H u0 p0 c0 {1,S}
18   H u0 p0 c0 {2,S}
19   H u0 p0 c0 {4,S}
20   H u0 p0 c0 {5,S}
21   H u0 p0 c0 {6,S}
22   H u0 p0 c0 {7,S}
23   H u0 p0 c0 {8,S}
24   H u0 p0 c0 {9,S}
25   H u0 p0 c0 {9,S}
26   H u0 p0 c0 {10,S}
27   H u0 p0 c0 {10,S}
28   H u0 p0 c0 {11,S}
29   H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [2.49854, 0.151702, -0.00035799, 7.17137e-07, -5.67369e-10, 12268.8, 19.4258],
                Tmin = (10, 'K'),
                Tmax = (406.634, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.98889, 0.110096, -6.8824e-05, 2.06014e-08, -2.36991e-12, 12533, 21.2407],
                Tmin = (406.634, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (101.974, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (681.787, 'J/(mol*K)'),
),
    shortDesc = u"""sarahkha CBSQB3 calculations Feb.6, 2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/HB/PhenylMig/wHBrad5/species/5HB
""",
)

entry(
    index = 9,
    label = "Ringrad2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {5,S} {6,S} {8,S} {13,S}
8  C u1 p0 c0 {7,S} {9,S} {10,S}
9  H u0 p0 c0 {8,S}
10 C u0 p0 c0 {8,S} {11,D} {26,S}
11 C u0 p0 c0 {10,D} {12,S} {27,S}
12 C u0 p0 c0 {11,S} {13,D} {28,S}
13 C u0 p0 c0 {7,S} {12,D} {29,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.27043, 0.0845159, 1.04362e-06, -4.72735e-08, 2.01069e-11, 17147.3, 16.1947],
                Tmin = (10, 'K'),
                Tmax = (1032.13, 'K'),
            ),
            NASAPolynomial(
                coeffs = [10.9469, 0.085587, -4.53051e-05, 1.15953e-08, -1.15989e-12, 13921, -29.0356],
                Tmin = (1032.13, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (142.605, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (690.101, 'J/(mol*K)'),
    ),
),
    shortDesc = u"""""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/HB/PhenylMig/wHBrad2/species/Ring
""",
)

entry(
    index = 10,
    label = "Ringrad3",
    molecule = 
"""
multiplicity 2
1       C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
2       C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3       C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4       C u0 p0 c0 {3,S} {5,S} {13,S} {21,S}
5       C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
6       C u1 p0 c0 {5,S} {7,S} {8,S}
7       H u0 p0 c0 {6,S}
8       C u0 p0 c0 {6,S} {9,D} {22,S}
9       C u0 p0 c0 {8,D} {10,S} {23,S}
10      C u0 p0 c0 {9,S} {11,D} {24,S}
11      C u0 p0 c0 {5,S} {10,D} {25,S}
12      C u0 p0 c0 {5,S} {13,S} {26,S} {27,S}
13      C u0 p0 c0 {4,S} {12,S} {28,S} {29,S}
14      H u0 p0 c0 {1,S}
15      H u0 p0 c0 {1,S}
16      H u0 p0 c0 {1,S}
17      H u0 p0 c0 {2,S}
18      H u0 p0 c0 {2,S}
19      H u0 p0 c0 {3,S}
20      H u0 p0 c0 {3,S}
21      H u0 p0 c0 {4,S}
22      H u0 p0 c0 {8,S}
23      H u0 p0 c0 {9,S}
24      H u0 p0 c0 {10,S}
25      H u0 p0 c0 {11,S}
26      H u0 p0 c0 {12,S}
27      H u0 p0 c0 {12,S}
28      H u0 p0 c0 {13,S}
29      H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.34161, 0.0748425, 4.91832e-05, -1.13678e-07, 4.90433e-11, 17068.6, 16.9494],
                Tmin = (10, 'K'),
                Tmax = (879.918, 'K'),
            ),
            NASAPolynomial(
                coeffs = [6.64626, 0.0980795, -5.56504e-05, 1.51633e-08, -1.60241e-12, 15005.9, -6.9872],
                Tmin = (879.918, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (141.946, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (694.258, 'J/(mol*K)'),
    ),
    shortDesc = u"""sarahkha CBSQB3 calculations Feb,6, 2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/HB/PhenylMig/wHBrad3/species/RingIC
""",
)

entry(
    index = 11,
    label = "Ringrad4",
    molecule = 
"""
multiplicity 2
1       C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
2       C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3       C u0 p0 c0 {2,S} {4,S} {13,S} {19,S}
4       C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5       C u1 p0 c0 {4,S} {6,S} {7,S}
6       H u0 p0 c0 {5,S}
7       C u0 p0 c0 {5,S} {8,D} {20,S}
8       C u0 p0 c0 {7,D} {9,S} {21,S}
9       C u0 p0 c0 {8,S} {10,D} {22,S}
10      C u0 p0 c0 {4,S} {9,D} {23,S}
11      C u0 p0 c0 {4,S} {12,S} {24,S} {25,S}
12      C u0 p0 c0 {11,S} {13,S} {26,S} {27,S}
13      C u0 p0 c0 {3,S} {12,S} {28,S} {29,S}
14      H u0 p0 c0 {1,S}
15      H u0 p0 c0 {1,S}
16      H u0 p0 c0 {1,S}
17      H u0 p0 c0 {2,S}
18      H u0 p0 c0 {2,S}
19      H u0 p0 c0 {3,S}
20      H u0 p0 c0 {7,S}
21      H u0 p0 c0 {8,S}
22      H u0 p0 c0 {9,S}
23      H u0 p0 c0 {10,S}
24      H u0 p0 c0 {11,S}
25      H u0 p0 c0 {11,S}
26      H u0 p0 c0 {12,S}
27      H u0 p0 c0 {12,S}
28      H u0 p0 c0 {13,S}
29      H u0 p0 c0 {13,S}
""",
 thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.66561, 0.0480768, 0.000134475, -2.15084e-07, 9.13801e-11, 9540.56, 15.1853],
                Tmin = (10, 'K'),
                Tmax = (814.288, 'K'),
            ),
            NASAPolynomial(
                coeffs = [1.21062, 0.107456, -6.20744e-05, 1.71986e-08, -1.84455e-12, 8371.58, 16.8919],
                Tmin = (814.288, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (79.387, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (698.416, 'J/(mol*K)'),
),
    shortDesc = u"""sarahkha CBSQB3 calculations Feb, 6, 2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/HB/PhenylMig/wHBrad4/species/Ring
""",
)

entry(
    index = 12,
    label = "Ringrad5",
    molecule = 
"""
multiplicity 2
1         C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
2         C u0 p0 c0 {1,S} {3,S} {13,S} {17,S}
3         C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4         C u1 p0 c0 {3,S} {5,S} {6,S}
5         H u0 p0 c0 {4,S}
6         C u0 p0 c0 {4,S} {7,D} {18,S}
7         C u0 p0 c0 {6,D} {8,S} {19,S}
8         C u0 p0 c0 {7,S} {9,D} {20,S}
9         C u0 p0 c0 {3,S} {8,D} {21,S}
10        C u0 p0 c0 {3,S} {11,S} {22,S} {23,S}
11        C u0 p0 c0 {10,S} {12,S} {24,S} {25,S}
12        C u0 p0 c0 {11,S} {13,S} {26,S} {27,S}
13        C u0 p0 c0 {2,S} {12,S} {28,S} {29,S}
14        H u0 p0 c0 {1,S}
15        H u0 p0 c0 {1,S}
16        H u0 p0 c0 {1,S}
17        H u0 p0 c0 {2,S}
18        H u0 p0 c0 {6,S}
19        H u0 p0 c0 {7,S}
20        H u0 p0 c0 {8,S}
21        H u0 p0 c0 {9,S}
22        H u0 p0 c0 {10,S}
23        H u0 p0 c0 {10,S}
24        H u0 p0 c0 {11,S}
25        H u0 p0 c0 {11,S}
26        H u0 p0 c0 {12,S}
27        H u0 p0 c0 {12,S}
28        H u0 p0 c0 {13,S}
29        H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.82754, 0.011084, 0.000384603, -7.71759e-07, 4.94182e-10, 7077.21, 15.6777],
                Tmin = (10, 'K'),
                Tmax = (468.315, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-6.18977, 0.126298, -7.9405e-05, 2.39853e-08, -2.7877e-12, 7690.28, 52.9343],
                Tmin = (468.315, 'K'),
                Tmax = (3000, 'K'),
    ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (58.8056, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (702.573, 'J/(mol*K)'),
   ),	
    shortDesc = u"""sarahkha CBSQB3 calculations + 1HR + Bond Corrections, Feb. 6, 2018 """,
    longDesc = 
u"""
/home/sarahkha/Cantherm/HB/PhenylMig/wHBrad5/species/Ring
optical isomers=2
""",
)


