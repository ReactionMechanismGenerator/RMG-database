#!/usr/bin/env python
# encoding: utf-8

name = "Butadiene_Dimerization"
shortDesc = u"Project Library for the fundamentals of the polymer fouling in ethylene crackers"
longDesc = u"""
This library is made by Hao-Wei Pang for the fundamentals of the polymer fouling in ethylene crackers.

It includes thermochemistry of butadiene dimers, calculated using the CBS-QB3 level of theory in March 2019 by Duminda Ranasinghe and Hao-Wei Pang.

Specifics of the calculations performed:
1. CBS-QB3 Level of theory was used after a B3LYP/6-311G(d,p) geometry optimization was performed
2. CBS-QB3 Energy calculation was performed
3. Frequency was calculated using B3LYP/CBSB7 iop(7/33=1) (Hessian was calculated)
4. 1D Hindered Rotors were calculated for steps of 10 degrees up to the full 360 degree cycle, with geometry optimization on each step.
5. All files generated were fed to Arkane (May 2019).
6. Frequency scaling factor was 0.99
7. Bond additivity corrections were applied based on Petersson et al. 1998 (http://aip.scitation.org/doi/10.1063/1.477794)

Disclaimer: The number of significant figures displayed does not reflect the accuracy of thermochemistry values. Sommers and Simmie esimates the error in enthalpy of formation by CBS-QB3 calculations to be + or - 2.4kcal/mol (http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448).
"""
entry(
    index = 1,
    label = "BD",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {5,S} {6,S}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}

""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.06611, -0.00623831, 0.000139743, -2.34106e-07, 1.24098e-10, 12064.3, 6.7553],
                Tmin = (10, 'K'),
                Tmax = (605.482, 'K'),
            ),
            NASAPolynomial(
                coeffs = [0.856124, 0.0374024, -2.39495e-05, 7.32361e-09, -8.53594e-13, 12041.8, 17.2351],
                Tmin = (605.482, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (100.294, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (228.648, 'J/(mol*K)'),
    ),
    shortDesc = u"""Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7""",
    longDesc = 
u"""
library value for butadiene dimerization reactions calculated by Duminda Ranasinghe and Hao-Wei Pang in March 2019
""",
)

entry(
    index = 2,
    label = "CB",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {4,S} {5,S}
2  C u0 p0 c0 {1,D} {3,S} {6,S}
3  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.17872, -0.0134958, 0.000136985, -1.94946e-07, 9.01194e-11, 18158.1, 7.88959],
                Tmin = (10, 'K'),
                Tmax = (670.96, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-1.52562, 0.0394628, -2.3777e-05, 6.88513e-09, -7.68053e-13, 18497, 29.9545],
                Tmin = (670.96, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (150.994, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (232.805, 'J/(mol*K)'),
    ),
    shortDesc = u"""Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7""",
    longDesc = 
u"""
library value for butadiene dimerization reactions calculated by Duminda Ranasinghe and Hao-Wei Pang in March 2019
""",
)

entry(
    index = 3,
    label = "DVCB",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {12,S}
4  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {5,S} {7,S} {17,S}
7  C u0 p0 c0 {6,S} {8,D} {18,S}
8  C u0 p0 c0 {7,D} {19,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.64572, 0.0508602, 3.88644e-06, -2.66495e-08, 9.87196e-12, 17303.2, 11.4871],
                Tmin = (10, 'K'),
                Tmax = (1164.82, 'K'),
            ),
            NASAPolynomial(
                coeffs = [9.80415, 0.0514479, -2.4861e-05, 5.82374e-09, -5.35947e-13, 14393.9, -25.493],
                Tmin = (1164.82, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (143.904, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (473.925, 'J/(mol*K)'),
    ),
    shortDesc = u"""Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7""",
    longDesc = 
u"""
library value for butadiene dimerization reactions calculated by Duminda Ranasinghe and Hao-Wei Pang in March 2019
""",
)

entry(
    index = 4,
    label = "COD",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,D} {13,S}
4  C u0 p0 c0 {3,D} {5,S} {14,S}
5  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {5,S} {7,S} {17,S} {18,S}
7  C u0 p0 c0 {6,S} {8,D} {19,S}
8  C u0 p0 c0 {1,S} {7,D} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.91856, 0.00493241, 0.000219347, -3.89485e-07, 2.2409e-10, 9745.1, 11.813],
                Tmin = (10, 'K'),
                Tmax = (448.785, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-5.23145, 0.0865182, -5.34493e-05, 1.59109e-08, -1.82854e-12, 10566.1, 48.6219],
                Tmin = (448.785, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (80.993, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (482.239, 'J/(mol*K)'),
    ),
    shortDesc = u"""Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7""",
    longDesc = 
u"""
library value for butadiene dimerization reactions calculated by Duminda Ranasinghe and Hao-Wei Pang in March 2019
""",
)

entry(
    index = 5,
    label = "VCH",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {9,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {12,S}
4  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {5,S} {7,D} {17,S}
7  C u0 p0 c0 {6,D} {8,S} {18,S}
8  C u0 p0 c0 {3,S} {7,S} {19,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.71329, 0.0282596, 9.68639e-05, -1.55189e-07, 6.90392e-11, 5823.69, 11.5197],
                Tmin = (10, 'K'),
                Tmax = (740.784, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-0.709834, 0.0747653, -4.31118e-05, 1.20056e-08, -1.29814e-12, 5858.29, 27.3421],
                Tmin = (740.784, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (48.4076, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (478.082, 'J/(mol*K)'),
    ),
    shortDesc = u"""Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7""",
    longDesc = 
u"""
library value for butadiene dimerization reactions calculated by Duminda Ranasinghe and Hao-Wei Pang in March 2019
""",
)

entry(
    index = 6,
    label = "DVT",
    molecule = 
"""
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {6,S} {14,S}
6  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
7  C u0 p0 c0 {6,S} {8,S} {17,S} {18,S}
8  C u0 p0 c0 {7,S} {9,D} {19,S}
9  C u0 p0 c0 {8,D} {10,S} {20,S}
10 C u1 p0 c0 {9,S} {11,S} {12,S}
11 H u0 p0 c0 {10,S}
12 H u0 p0 c0 {10,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.57659, 0.0532285, 8.70896e-06, -3.75139e-08, 1.48757e-11, 32509.1, 12.9964],
                Tmin = (10, 'K'),
                Tmax = (1047.54, 'K'),
            ),
            NASAPolynomial(
                coeffs = [8.13789, 0.0581318, -3.02738e-05, 7.636e-09, -7.54004e-13, 30328.8, -15.0665],
                Tmin = (1047.54, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (270.333, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (482.239, 'J/(mol*K)'),
    ),
    shortDesc = u"""Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7""",
    longDesc = 
u"""
library value for butadiene dimerization reactions calculated by Duminda Ranasinghe and Hao-Wei Pang in March 2019
""",
)
