#!/usr/bin/env python
# encoding: utf-8

name = "CPO oxidation"
shortDesc = u"sarahkha ab initio calculations"
longDesc = u"""
Calculated at the CBS-QB3 level with 1D HR with Gaussian09 on NERSC and Pharos
/home/sarahkha/Cantherm/CPO
"""
entry(
    index = 1,
    label = "CPO-O2rad_alpha",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,S} {8,S} {13,S}
6  O u0 p2 c0 {5,S} {7,S}
7  O u1 p2 c0 {6,S}
8  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.92161, 0.0325256, 2.62016e-05, -4.78606e-08, 1.77082e-11, -18186.6, 13.4727],
                Tmin = (10, 'K'),
                Tmax = (1042.42, 'K'),
            ),
            NASAPolynomial(
                coeffs = [8.2152, 0.0408222, -2.13826e-05, 5.36784e-09, -5.24604e-13, -20427.7, -13.8756],
                Tmin = (1042.42, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-151.106, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (353.365, 'J/(mol*K)'),
),
    shortDesc = u"""sarahkha cantherm from CBSQB3 calculations performed with G09 NERSC entered Feb. 8, 2018 """,
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/ELIMHO2/species/react
optical isomer =2
one HR = CCOO
""",
)

entry(
    index = 2,
    label = "CPO-O2rad_beta",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {5,S} {7,S} {15,S}
7  O u0 p2 c0 {6,S} {8,S}
8  O u1 p2 c0 {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.77574, 0.0345216, 2.58676e-05, -5.30017e-08, 2.13353e-11, -21048.3, 13.0869],
                Tmin = (10, 'K'),
                Tmax = (947.788, 'K'),
            ),
            NASAPolynomial(
                coeffs = [6.29811, 0.0452858, -2.50516e-05, 6.6478e-09, -6.85156e-13, -22488, -4.01973],
                Tmin = (947.788, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-174.951, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (353.365, 'J/(mol*K)'),
    ),
shortDesc = u"""sarahkha cantherm from CBSQB3 calculations performed with G09 NERSC entered Feb. 8, 2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/ELIMHO2/species/reactBeta
optical isomer =2
one HR = CCOO
""",
)

entry(
    index = 3,
    label = "CPO-OH_alpha",
    molecule = 
"""
multiplicity 1
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,S} {8,S} {13,S}
6  O u0 p2 c0 {5,S} {7,S}
7  H u0 p0 c0 {6,S}
8  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
       polynomials = [
           NASAPolynomial(
                coeffs = [3.90586, 0.00568266, 0.000177794, -3.34342e-07, 1.96696e-10, -46078.5, 12.0884],
                Tmin = (10, 'K'),
                Tmax = (524.065, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-1.21317, 0.0635166, -4.14424e-05, 1.28649e-08, -1.52391e-12, -45799.6, 31.019],
                Tmin = (524.065, 'K'),
                Tmax = (3000, 'K'),
                )],
                ),
shortDesc = u"""sarahkha cantherm from CBSQB3 calculations performed with G09 NERSC entered Feb. 8, 2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/OHADDfrh2o2/species/ProdA
optical isomer =2
one HR = CCOH
""",
)

entry(
    index = 4,
    label = "CPO-OH_beta",
    molecule = 
"""
multiplicity 1
1  C u0 p0 c0 {2,S} {6,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,D} {5,S}
4  O u0 p2 c0 {3,D}
5  C u0 p0 c0 {3,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {5,S} {7,S} {15,S}
7  O u0 p2 c0 {6,S} {8,S}
8  H u0 p0 c0 {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
""",
 thermo = NASA(
      polynomials = [
            NASAPolynomial(
                coeffs = [3.90172, 0.00622239, 0.00018336, -3.69234e-07, 2.34295e-10, -46478.5, 12.6888],
                Tmin = (10, 'K'),
                Tmax = (487.237, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-0.277544, 0.0592081, -3.7256e-05, 1.12943e-08, -1.31821e-12, -46292.9, 27.5716],
                Tmin = (487.237, 'K'),
                Tmax = (3000, 'K'),
    )],
    ),
    shortDesc = u"""sarahkha cantherm from CBSQB3 calculations performed with G09 on NERSC entered Feb. 8, 2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/OHADDfrh2o2/species/ProdB
optical isomer =2
one HR = CCOH
""",
)

entry(
    index = 5,
    label = "CPO-HO2_alpha",
    molecule = 
"""
multiplicity 1
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {9,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u0 p2 c0 {4,S} {10,S}
6  C u0 p0 c0 {3,S} {7,S} {11,S} {12,S}
7  C u0 p0 c0 {6,S} {8,S} {13,S} {14,S}
8  C u0 p0 c0 {2,S} {7,S} {15,S} {16,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.81091, 0.0111448, 0.000213666, -4.26212e-07, 2.53462e-10, -37189.6, 12.9487],
                Tmin = (10, 'K'),
                Tmax = (564.294, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.25648, 0.0652735, -4.48128e-05, 1.45447e-08, -1.78652e-12, -37700.5, 13.4768],
                Tmin = (564.294, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-309.288, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (374.151, 'J/(mol*K)'),
        ),
    shortDesc = u"""sarahkha cantherm from CBSQB3 calculations performed with G09 on NERSC entered Feb. 8, 2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/THERMO/species/cpoOOHrad/A
optical isomer=2
2 HR treatments: CCOO and COOH2 HR treatments: CCOO and COOH
""",
)

entry(
    index = 6,
    label = "CPO-HO2_beta",
    molecule = 
"""
multiplicity 1
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {6,S} {8,S} {13,S}
6  O u0 p2 c0 {5,S} {7,S}
7  O u0 p2 c0 {6,S} {14,S}
8  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.7132, 0.0358703, 4.04228e-05, -8.0367e-08, 3.51137e-11, -38747.2, 12.6663],
                Tmin = (10, 'K'),
                Tmax = (845.209, 'K'),
            ),
            NASAPolynomial(
                coeffs = [5.24165, 0.0521928, -3.03501e-05, 8.42987e-09, -9.04363e-13, -39847, 0.57206],
                Tmin = (845.209, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-322.136, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (374.151, 'J/(mol*K)'),
),
    shortDesc = u"""sarahkha cantherm from CBSQB3 calculations performed with G09 on NERSC entered Feb. 8, 2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/THERMO/species/cpoOOHrad/B
optical isomer=2
2 HR treatments: CCOO and COOH
""",
)

entry(
    index = 7,
    label = "CPO-HO2_alpha-rad_alpha",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u0 p2 c0 {4,S} {11,S}
6  C u0 p0 c0 {3,S} {7,S} {12,S} {13,S}
7  C u0 p0 c0 {6,S} {8,S} {14,S} {15,S}
8  C u1 p0 c0 {2,S} {7,S} {9,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.73477, 0.0184878, 0.000232225, -6.00312e-07, 4.56261e-10, -17320.6, 12.5818],
                Tmin = (10, 'K'),
                Tmax = (450.36, 'K'),
            ),
            NASAPolynomial(
                coeffs = [4.26976, 0.0567367, -3.839e-05, 1.22885e-08, -1.4894e-12, -17804.9, 5.58612],
                Tmin = (450.36, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-144.04, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (349.208, 'J/(mol*K)'),
),
shortDesc = u"""sarahkha cantherm from CBSQB3 calculations performed with G09 on NERSC entered Feb. 8, 2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/THERMO/species/cpoOOHrad/A/fromHabs
optisomer=2
2 HR treatments: CCOO and COOH
""",
)

entry(
    index = 8,
    label = "CPO-HO2_beta-rad_alpha",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {7,S} {12,S}
5  O u0 p2 c0 {4,S} {6,S}
6  O u0 p2 c0 {5,S} {13,S}
7  C u0 p0 c0 {4,S} {8,S} {14,S} {15,S}
8  C u1 p0 c0 {2,S} {7,S} {9,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
        thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.7145, 0.0277836, 8.49004e-05, -1.68492e-07, 8.85157e-11, -18449.6, 14.0484],
                Tmin = (10, 'K'),
                Tmax = (660.601, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.41684, 0.0549897, -3.45585e-05, 1.0277e-08, -1.16838e-12, -18964.5, 11.1656],
                Tmin = (660.601, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-153.434, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (349.208, 'J/(mol*K)'),
),
    shortDesc = u"""sarahkha cantherm from CBSQB3 calculations performed with G09 on NERSC entered Feb. 8, 2018""",
    longDesc = 
u"""
/home/sarahkha/Cantherm/CPO/THERMO/species/cpoOOHrad/B/fromHabs
optisomer=2
2 HR treatments: CCOO and COOH
""",
)

entry(
    index = 9,
    label = "CPOoh-O2_alpha-rad",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {9,S}
2  O u0 p2 c0 {1,S} {3,S}
3  O u1 p2 c0 {2,S}
4  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
6  C u0 p0 c0 {5,S} {7,D} {14,S}
7  C u0 p0 c0 {1,S} {6,D} {8,S}
8  O u0 p2 c0 {7,S} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {8,S}
""",
        thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.7145, 0.0277836, 8.49004e-05, -1.68492e-07, 8.85157e-11, -18449.6, 14.0484],
                Tmin = (10, 'K'),
                Tmax = (660.601, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.41684, 0.0549897, -3.45585e-05, 1.0277e-08, -1.16838e-12, -18964.5, 11.1656],
                Tmin = (660.601, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-153.434, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (349.208, 'J/(mol*K)'),
),
    shortDesc = u"""sarahkha cantherm from CBSQB3 calculations performed with G09 on NERSC entered Feb.10, 2018""",
    longDesc =
u"""
/home/sarahkha/Cantherm/CPO/THERMO/species/cpoO2OHrad/alpha
optisomer=2
2 HR treatments: CCOO and COOH
""",
)

entry(
    index = 10,
    label = "CPO-HO2_alpha-rad_beta",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u0 p2 c0 {4,S} {11,S}
6  C u0 p0 c0 {3,S} {7,S} {12,S} {13,S}
7  C u1 p0 c0 {6,S} {8,S} {14,S} 
8  C u0 p0 c0 {2,S} {7,S} {9,S} {15,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
""",
        thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.85156, 0.00862477, 0.000205061, -3.87594e-07, 2.21011e-10, -14129.8, 14.043],
                Tmin = (10, 'K'),
                Tmax = (568.843, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-0.568639, 0.0729997, -5.24822e-05, 1.71271e-08, -2.07742e-12, -14165.6, 28.1397],
                Tmin = (568.843, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-117.545, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (349.208, 'J/(mol*K)'),
    ),
    shortDesc = u"""sarahkha cantherm from CBSQB3 calculations performed with G09 on Pharos entered May23, 2018""",
    longDesc =
u"""
/home/sarahkha/Cantherm/CPO/R1/radA/reactionB/species/cpoOOHradB
optisomer=2
2 HR treatments: CCOO and COOH
""",
)

entry(
    index = 11,
    label = "CPO-HO2_beta-rad_beta",
    molecule =
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {7,S} {12,S}
5  O u0 p2 c0 {4,S} {6,S}
6  O u0 p2 c0 {5,S} {13,S}
7  C u1 p0 c0 {4,S} {8,S} {14,S} 
8  C u0 p0 c0 {2,S} {7,S} {9,S} {15,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.68851, 0.0433873, 3.57933e-06, -3.16854e-08, 1.39461e-11, -14990.5, 13.7717],
                Tmin = (10, 'K'),
                Tmax = (989.457, 'K'),
            ),
            NASAPolynomial(
                coeffs = [9.02609, 0.0413137, -2.2845e-05, 6.04051e-09, -6.1941e-13, -17001.5, -16.7471],
                Tmin = (989.457, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-124.59, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (349.208, 'J/(mol*K)'),
    ),
    shortDesc = u"""sarahkha cantherm from CBSQB3 calculations performed with G09 on Pharos entered May23, 2018""",
    longDesc =
u"""
/home/sarahkha/Cantherm/CPO/R1/radB/reactionB/species/cpoHO2radB
optisomer=2
2 HR treatments: CCOO and COOH
""",
)

entry(
    index = 12,
    label = "sciss-HO2_alpha-rad_alpha",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {8,D}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {12,S}
5  C u1 p0 c0 {4,S} {13,S} {14,S}
6  O u0 p2 c0 {4,S} {7,S}
7  O u0 p2 c0 {6,S} {15,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.55702, 0.0531322, -5.84227e-06, -2.95616e-08, 1.40391e-11, -4460.62, 13.3357],
                Tmin = (10, 'K'),
                Tmax = (1026.07, 'K'),
            ),
            NASAPolynomial(
                coeffs = [13.2824, 0.0406476, -2.47647e-05, 6.88542e-09, -7.25847e-13, -7795, -40.3569],
                Tmin = (1026.07, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-37.0475, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (336.736, 'J/(mol*K)'),
    ),
    shortDesc = u"""sarahkha cantherm from CBSQB3 calculations performed with G09 on Pharos entered May23, 2018""",
    longDesc =
u"""
/home/sarahkha/Cantherm/CPO/R3/Alpha/radAprim/species/prod
optisomer=2
5 HR treatments 
""",
)

entry(
    index = 13,
    label = "sciss-HO2_alpha-rad_beta",
    molecule =
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,S} {7,S} {14,S}
5  O u0 p2 c0 {4,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  C u1 p0 c0 {4,S} {8,D}
8  O u0 p2 c0 {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
        thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.28639, 0.065879, -4.90493e-05, 1.17182e-08, 1.67523e-12, -7244.91, 13.2717],
                Tmin = (10, 'K'),
                Tmax = (906.142, 'K'),
            ),
            NASAPolynomial(
                coeffs = [11.9165, 0.0390897, -2.34197e-05, 6.63218e-09, -7.20679e-13, -9273.12, -30.0743],
                Tmin = (906.142, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-60.29, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (336.736, 'J/(mol*K)'),
    ),
    shortDesc = u"""sarahkha cantherm from CBSQB3 calculations performed with G09 on Pharos entered May23, 2018""",
    longDesc =
u"""
/home/sarahkha/Cantherm/CPO/R3/Alpha/radBprim/species/prod
optisomer=2
5 HR treatments
""",
)

entry(
    index = 14,
    label = "CPOoh-O2_beta-rad_alpha",
    molecule =
"""
multiplicity 2
1  O u1 p2 c0 {3,S}
2  O u0 p2 c0 {5,S} {9,S}
3  O u0 p2 c0 {1,S} {8,S}
4  C u0 p0 c0 {5,D} {6,S} {10,S}
5  C u0 p0 c0 {2,S} {4,D} {7,S}
6  C u0 p0 c0 {4,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {5,S} {8,S} {13,S} {14,S}
8  C u0 p0 c0 {3,S} {6,S} {7,S} {15,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.81289, 0.0118387, 0.000209702, -4.62214e-07, 3.05546e-10, -16025.3, 13.8027],
                Tmin = (10, 'K'),
                Tmax = (507.011, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.85696, 0.0575067, -3.82051e-05, 1.20754e-08, -1.45252e-12, -16418.4, 12.9327],
                Tmin = (507.011, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-133.295, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (349.208, 'J/(mol*K)'),
    ),
    shortDesc = u"""sarahkha cantherm from CBSQB3 calculations performed with G09 on Pharos entered May23, 2018""",
    longDesc =
u"""
/home/sarahkha/Cantherm/CPO/R2/radB/reactionalphaprim/species/Prod
optisomer=2
2 HR treatments
""",
)

