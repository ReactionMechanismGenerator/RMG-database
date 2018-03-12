#!/usr/bin/env python
# encoding: utf-8

name = "HB EndoCycloaddition"
shortDesc = u"sarahkha ab initio calculations"
longDesc = u"""
Calculated at the CBS-QB3 level with 1D HR with Gaussian09 on NERSC
/home/sarahkha/Cantherm/HB/CYCLI
"""
entry(
    index = 1,
    label = "HBrad2",
    molecule = 
"""
multiplicity 2
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
    shortDesc = u"""sarahkha cantherm from CBSQB3 calculations performed by Lawrence Lai with G03 Pharos entered Feb. 6, 2018 """,
    longDesc = 
u"""
/home/sarahkha/Cantherm/HB/CYCLI/species/HBrad2
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
    
shortDesc = u"""sarahkha cantherm from CBSQB3 calculations performed by Lawrence Lai with G03 Pharos entered Feb. 6, 2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/HB/CYCLI/species/HBrad3
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
shortDesc = u"""sarahkha cantherm from CBSQB3 calculations performed by Lawrence Lai with G03 Pharos entered Feb. 6, 2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/HB/CYCLI/species/HBrad4
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
    shortDesm = u"""sarahkha cantherm from CBSQB3 calculations performed by Lawrence Lai with G03 Pharos entered Feb. 6, 2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/HB/CYCLI/species/HBrad5
""",
)

entry(
    index = 5,
    label = "Endotransrad2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {23,S} {24,S} {25,S}
7  C u0 p0 c0 {2,S} {8,S} {13,S} {26,S}
8  C u1 p0 c0 {7,S} {9,S} {10,S}
9  H u0 p0 c0 {8,S}
10 C u0 p0 c0 {8,S} {11,D} {27,S}
11 C u0 p0 c0 {10,D} {12,S} {28,S}
12 C u0 p0 c0 {11,S} {13,D} {29,S}
13 C u0 p0 c0 {1,S} {7,S} {12,D}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {10,S}
28 H u0 p0 c0 {11,S}
29 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.25978, 0.0772915, 3.09059e-05, -8.76892e-08, 3.78293e-11, 20722.5, 16.5555],
                Tmin = (10, 'K'),
                Tmax = (900.751, 'K'),
            ),
            NASAPolynomial(
                coeffs = [6.35662, 0.0957221, -5.33793e-05, 1.43579e-08, -1.50255e-12, 18859, -5.30837],
                Tmin = (900.751, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (172.299, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (690.101, 'J/(mol*K)'),
),
    shortDesc = u"""sarahkha CBSQB3 calculations Feb. 6,2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/HB/CYCLI/species/Prodrad2/trans
""",
)

entry(
    index = 6,
    label = "Endotransrad3",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {7,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {23,S} {24,S} {25,S}
7  C u0 p0 c0 {3,S} {8,S} {13,S} {26,S}
8  C u1 p0 c0 {7,S} {9,S} {10,S}
9  H u0 p0 c0 {8,S}
10 C u0 p0 c0 {8,S} {11,D} {27,S}
11 C u0 p0 c0 {10,D} {12,S} {28,S}
12 C u0 p0 c0 {11,S} {13,D} {29,S}
13 C u0 p0 c0 {1,S} {7,S} {12,D}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {10,S}
28 H u0 p0 c0 {11,S}
29 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.33001, 0.0603331, 0.000113912, -2.24179e-07, 1.11559e-10, 9120.24, 15.5969],
                Tmin = (10, 'K'),
                Tmax = (683.817, 'K'),
            ),
            NASAPolynomial(
                coeffs = [0.176636, 0.110504, -6.57333e-05, 1.88066e-08, -2.07998e-12, 8809.76, 24.188],
                Tmin = (683.817, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (75.7567, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (694.258, 'J/(mol*K)'),
    ),
    shortDesc = u"""sarahkha CBSQB3 calculations + 3HR + Bond Corrections Feb. 6,2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/HB/CYCLI/species/Prodrad3/trans
""",
)

entry(
    index = 7,
    label = "Endotransrad4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {7,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {23,S} {24,S} {25,S}
7  C u0 p0 c0 {4,S} {8,S} {13,S} {26,S}
8  C u1 p0 c0 {7,S} {9,S} {10,S}
9  H u0 p0 c0 {8,S}
10 C u0 p0 c0 {8,S} {11,D} {27,S}
11 C u0 p0 c0 {10,D} {12,S} {28,S}
12 C u0 p0 c0 {11,S} {13,D} {29,S}
13 C u0 p0 c0 {1,S} {7,S} {12,D}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {10,S}
28 H u0 p0 c0 {11,S}
29 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.59642, 0.0468564, 0.000141612, -2.31267e-07, 1.01976e-10, 6546.69, 14.6758],
                Tmin = (10, 'K'),
                Tmax = (770.979, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-0.460832, 0.110267, -6.41756e-05, 1.79436e-08, -1.94239e-12, 5913.31, 25.0296],
                Tmin = (770.979, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (54.446, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (698.416, 'J/(mol*K)'),
    ),
shortDesc = u"""sarahkha CBSQB3 calculations+2 HR treatment Feb. 6,2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/HB/CYCLI/species/Prodrad4/trans
Endotransrad4 is more stable than Endocisrad4
""",
)

entry(
    index = 8,
    label = "Endocisrad5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {7,S} {22,S}
6  C u0 p0 c0 {5,S} {23,S} {24,S} {25,S}
7  C u0 p0 c0 {5,S} {8,S} {13,S} {26,S}
8  C u1 p0 c0 {7,S} {9,S} {10,S}
9  H u0 p0 c0 {8,S}
10 C u0 p0 c0 {8,S} {11,D} {27,S}
11 C u0 p0 c0 {10,D} {12,S} {28,S}
12 C u0 p0 c0 {11,S} {13,D} {29,S}
13 C u0 p0 c0 {1,S} {7,S} {12,D}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {10,S}
28 H u0 p0 c0 {11,S}
29 H u0 p0 c0 {12,S}
""",
        thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.87138, 0.00900088, 0.000413537, -8.93258e-07, 6.37332e-10, 10341.9, 16.3878],
                Tmin = (10, 'K'),
                Tmax = (358.164, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-6.6579, 0.126602, -7.9021e-05, 2.36386e-08, -2.71873e-12, 11096.1, 56.3735],
                Tmin = (358.164, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (85.9893, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (702.573, 'J/(mol*K)'),
),
    shortDesc = u"""sarahkha CBSQB3 calculations + 1 HR Feb.6, 2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/HB/CYCLI/species/Prodrad5/cis
optisomer=2
Endocisrad5 is more stable than Endotransrad5
""",
)

