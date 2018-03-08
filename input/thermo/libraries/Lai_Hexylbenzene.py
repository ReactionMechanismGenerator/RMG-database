#!/usr/bin/env python
# encoding: utf-8

name = "Hexylbenzene"
shortDesc = u"Project LIbrary for Hexylbenzene Pyrolysis and Supercritical Water treatment"
longDesc = u"""
This library is made by Lawrence Lai for the Hexylbenzene Pyrolysis and Supercritical Water Treatment

This work is published in

Lai, Lawrence, Gudiyella, Soumya, Liu, Mengjie, Green, William H. "Chemistry of Alkylaromatics Reconsidered". To be submitted to Energy and Fuels, 2017.

Includes thermochemistry of alkylaromatics and many relevant compounds, calculated using the CBS-QB3 level of theory in June 2017.

Specifics of the calculations performed:
1. CBS-QB3 Level of theory was used after a B3LYP/6-311G(d,p) geometry optimization was performed
2. CBS-QB3 Energy calculation was performed
3. Frequency was calculated using B3LYP/CBSB7 iop(7/33=1) (Hessian was calculated)
4. 1D Hindered Rotors were calculated for steps of 10 degrees up to the full 360 degree cycle, with geometry optimization on each step.
5. All files generated were fed to Cantherm (June 2017).
6. Frequency scaling factor was 0.99
7. Bond additivity corrections were applied based on Petersson et al. 1998 (http://aip.scitation.org/doi/10.1063/1.477794)

Disclaimer: The number of significant figures displayed does not reflect the accuracy of thermochemistry values. Sommers and Simmie esimates
the error in enthalpy of formation by CBS-QB3 calculations to be + or - 2.4kcal/mol (http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448).
"""
entry(
    index = 0,
    label = "Hexylbenzene",
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
            NASAPolynomial(coeffs=[2.53848,0.154692,-0.000505491,1.21307e-06,-1.03076e-09,-11769.8,15.735], Tmin=(10,'K'), Tmax=(405.473,'K')),
            NASAPolynomial(coeffs=[-1.31497,0.114635,-6.84889e-05,1.97053e-08,-2.19288e-12,-10815.6,38.7611], Tmin=(405.473,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-97.9049,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (706.73,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Hexylbenzene calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: Six
Location of calculations Pharos/home/laitcl/Gaussian/2017/Alkylbenzenes
""",
)

entry(
    index = 1,
    label = "Styrene",
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
            NASAPolynomial(coeffs=[3.91381,0.00507501,0.000182357,-3.25547e-07,1.82313e-10,15456.5,11.7174], Tmin=(10,'K'), Tmax=(539.173,'K')),
            NASAPolynomial(coeffs=[-2.77087,0.0711256,-4.71867e-05,1.48906e-08,-1.78985e-12,15938.1,37.6194], Tmin=(539.173,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (128.478,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Styrene calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: One
Location of calculations Pharos/home/laitcl/Gaussian/2017/Alkylbenzenes
""",
)

entry(
    index = 2,
    label = "HexylbenzylRad1",
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
            NASAPolynomial(coeffs=[2.83083,0.124716,-0.000340437,8.86239e-07,-8.17332e-10,6898.77,17.2712], Tmin=(10,'K'), Tmax=(389.843,'K')),
            NASAPolynomial(coeffs=[-2.38727,0.116589,-7.18943e-05,2.12444e-08,-2.41624e-12,7774.22,43.54], Tmin=(389.843,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (57.3216,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (685.944,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Hexylbenzene Radical calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 5
Location of calculations Pharos/home/laitcl/Gaussian/2017/Alkylbenzene Radicals
""",
)

entry(
    index = 3,
    label = "Butyl Radical",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
5  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
6  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8048,0.0225494,1.82606e-05,-2.96978e-08,1.03636e-11,7489.25,9.68915], Tmin=(10,'K'), Tmax=(1043.96,'K')),
            NASAPolynomial(coeffs=[3.40454,0.0359845,-1.81441e-05,4.47033e-09,-4.33902e-13,6924.27,8.53122], Tmin=(1043.96,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (62.2808,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (295.164,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Butyl Radical calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 3
Location of calculations Pharos/home/laitcl/Gaussian/2017/Aliphatic Radicals
""",
)

entry(
    index = 4,
    label = "Ethylbenzene",
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
            NASAPolynomial(coeffs=[3.93256,0.0045774,0.000229019,-4.71073e-07,3.18895e-10,720.269,12.7159], Tmin=(10,'K'), Tmax=(378.139,'K')),
            NASAPolynomial(coeffs=[-2.62723,0.0739489,-4.60899e-05,1.38184e-08,-1.59588e-12,1216.5,37.9855], Tmin=(378.139,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (5.98516,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (424.038,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Ethylbenzene calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 2
Location of calculations Pharos/home/laitcl/Gaussian/2017/Alkylbenzenes
""",
)

entry(
    index = 5,
    label = "Ethylbenzyl Radical1",
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
            NASAPolynomial(coeffs=[3.91132,0.00543209,0.000200316,-3.74426e-07,2.21934e-10,19069.6,13.1774], Tmin=(10,'K'), Tmax=(504.174,'K')),
            NASAPolynomial(coeffs=[-2.56642,0.0726363,-4.66693e-05,1.43632e-08,-1.69469e-12,19521.9,37.9997], Tmin=(504.174,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (158.525,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (403.252,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Ethylbenzyl Radical1 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2017/Alkylbenzene Radicals
""",
)

entry(
    index = 6,
    label = "Propylbenzene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {5,B} {6,B}
5  C u0 p0 c0 {4,B} {7,B} {17,S}
6  C u0 p0 c0 {4,B} {9,B} {21,S}
7  C u0 p0 c0 {5,B} {8,B} {18,S}
8  C u0 p0 c0 {7,B} {9,B} {19,S}
9  C u0 p0 c0 {6,B} {8,B} {20,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72412,0.0429039,4.40028e-05,-7.58288e-08,2.88791e-11,-2582.08,12.2094], Tmin=(10,'K'), Tmax=(967.569,'K')),
            NASAPolynomial(coeffs=[5.13122,0.0655377,-3.51925e-05,9.12776e-09,-9.24042e-13,-4186.14,-1.41475], Tmin=(967.569,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-21.3967,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (494.711,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Propylbenzene calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 3
Location of calculations Pharos/home/laitcl/Gaussian/2017/Alkylbenzenes
""",
)

entry(
    index = 7,
    label = "Propylbenzyl Radical1",
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
            NASAPolynomial(coeffs=[3.89471,0.00723012,0.000275615,-5.94663e-07,4.15797e-10,16188.3,15.1717], Tmin=(10,'K'), Tmax=(414.99,'K')),
            NASAPolynomial(coeffs=[-2.59425,0.0839895,-5.32106e-05,1.61177e-08,-1.87171e-12,16604.5,39.2955], Tmin=(414.99,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (134.594,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (473.925,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Propylbenzyl Radical1 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 2
Location of calculations Pharos/home/laitcl/Gaussian/2017/Alkylbenzene Radicals
""",
)

entry(
    index = 8,
    label = "Butylbenzene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {6,B} {7,B}
6  C u0 p0 c0 {5,B} {8,B} {20,S}
7  C u0 p0 c0 {5,B} {10,B} {24,S}
8  C u0 p0 c0 {6,B} {9,B} {21,S}
9  C u0 p0 c0 {8,B} {10,B} {22,S}
10 C u0 p0 c0 {7,B} {9,B} {23,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.17901,0.0877537,-0.00021136,5.83115e-07,-5.5537e-10,-5711.02,13.8221], Tmin=(10,'K'), Tmax=(394.37,'K')),
            NASAPolynomial(coeffs=[-2.26079,0.0951888,-5.80606e-05,1.70174e-08,-1.92366e-12,-4910.72,39.7112], Tmin=(394.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-47.5121,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (565.384,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Butylbenzene calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 4
Location of calculations Pharos/home/laitcl/Gaussian/2017/Alkylbenzenes
""",
)

entry(
    index = 9,
    label = "Butylbenzyl Radical1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
4  C u0 p0 c0 {5,S} {6,B} {7,B}
5  C u1 p0 c0 {2,S} {4,S} {18,S}
6  C u0 p0 c0 {4,B} {8,B} {19,S}
7  C u0 p0 c0 {4,B} {10,B} {23,S}
8  C u0 p0 c0 {6,B} {9,B} {20,S}
9  C u0 p0 c0 {8,B} {10,B} {21,S}
10 C u0 p0 c0 {7,B} {9,B} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70217,0.0481911,5.51547e-05,-9.61555e-08,3.77439e-11,12989.5,14.9723], Tmin=(10,'K'), Tmax=(937.336,'K')),
            NASAPolynomial(coeffs=[5.6281,0.0740216,-4.06696e-05,1.07521e-08,-1.10595e-12,11132.7,-2.17348], Tmin=(937.336,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (108.088,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (544.598,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Butylbenzyl Radical1 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 3
Location of calculations Pharos/home/laitcl/Gaussian/2017/Alkylbenzene Radicals
""",
)

entry(
    index = 10,
    label = "Pentylbenzene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {4,S} {16,S} {17,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {20,S} {21,S} {22,S}
6  C u0 p0 c0 {4,S} {7,B} {8,B}
7  C u0 p0 c0 {6,B} {9,B} {23,S}
8  C u0 p0 c0 {6,B} {11,B} {27,S}
9  C u0 p0 c0 {7,B} {10,B} {24,S}
10 C u0 p0 c0 {9,B} {11,B} {25,S}
11 C u0 p0 c0 {8,B} {10,B} {26,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {11,S}
27 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.88544,0.117938,-0.000332991,8.32039e-07,-7.35791e-10,-8792.9,14.6085], Tmin=(10,'K'), Tmax=(402.152,'K')),
            NASAPolynomial(coeffs=[-1.76962,0.104944,-6.33527e-05,1.84047e-08,-2.06544e-12,-7939.01,38.7876], Tmin=(402.152,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-73.1433,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (636.057,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Pentylbenzene calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 5
Location of calculations Pharos/home/laitcl/Gaussian/2017/Alkylbenzenes
""",
)

entry(
    index = 11,
    label = "Pentylbenzyl Radical1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {16,S} {17,S}
4  C u0 p0 c0 {2,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {6,S} {7,B} {8,B}
6  C u1 p0 c0 {3,S} {5,S} {21,S}
7  C u0 p0 c0 {5,B} {9,B} {22,S}
8  C u0 p0 c0 {5,B} {11,B} {26,S}
9  C u0 p0 c0 {7,B} {10,B} {23,S}
10 C u0 p0 c0 {9,B} {11,B} {24,S}
11 C u0 p0 c0 {8,B} {10,B} {25,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65179,0.0690217,8.62318e-06,-4.20781e-08,1.57571e-11,10092.1,15.3011], Tmin=(10,'K'), Tmax=(1148.08,'K')),
            NASAPolynomial(coeffs=[14.2082,0.0663492,-3.2446e-05,7.6453e-09,-7.04837e-13,5420.35,-46.8743], Tmin=(1148.08,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (84.0184,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (615.271,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Pentylbenzyl Radical1 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 4
Location of calculations Pharos/home/laitcl/Gaussian/2017/Alkylbenzene Radicals
""",
)

entry(
    index = 12,
    label = "Benzyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {11,S}
3  C u0 p0 c0 {1,B} {5,B} {12,S}
4  C u0 p0 c0 {2,B} {6,B} {8,S}
5  C u0 p0 c0 {3,B} {6,B} {9,S}
6  C u0 p0 c0 {4,B} {5,B} {10,S}
7  C u1 p0 c0 {1,S} {13,S} {14,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.13967,-0.0141725,0.000261854,-4.75457e-07,2.76642e-10,23304.6,10.5067], Tmin=(10,'K'), Tmax=(549.061,'K')),
            NASAPolynomial(coeffs=[-0.662671,0.0580793,-3.73415e-05,1.14394e-08,-1.33771e-12,23270.3,25.6807], Tmin=(549.061,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (193.736,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    shortDesc = u"""Calculation for Benzyl done by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: None
Location of calculations Pharos/home/laitcl/Gaussian/2017/Alkylbenzene Radicals
""",
)

entry(
    index = 13,
    label = "Toluene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {14,S}
4  C u0 p0 c0 {2,B} {6,B} {15,S}
5  C u0 p0 c0 {3,B} {7,B} {11,S}
6  C u0 p0 c0 {4,B} {7,B} {12,S}
7  C u0 p0 c0 {5,B} {6,B} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04843,-0.00496311,0.000190094,-3.12375e-07,1.63599e-10,3720.16,10.905], Tmin=(10,'K'), Tmax=(590.573,'K')),
            NASAPolynomial(coeffs=[-2.46624,0.0620951,-3.84774e-05,1.14026e-08,-1.29702e-12,4089.7,35.5174], Tmin=(590.573,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (30.9121,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (353.365,'J/(mol*K)'),
    ),
    shortDesc = u"""Calculation for Toluene done by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1 - Note: Free Rotors have been found to yield extremely close results
Location of calculations Pharos/home/laitcl/Gaussian/2017/Alkylbenzenes
""",
)

entry(
    index = 14,
    label = "Indane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {5,B} {6,B}
5  C u0 p0 c0 {3,S} {4,B} {7,B}
6  C u0 p0 c0 {4,B} {8,B} {16,S}
7  C u0 p0 c0 {5,B} {9,B} {19,S}
8  C u0 p0 c0 {6,B} {9,B} {17,S}
9  C u0 p0 c0 {7,B} {8,B} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05393,-0.00590968,0.000256082,-4.22713e-07,2.21322e-10,4179.59,11.8847], Tmin=(10,'K'), Tmax=(594.808,'K')),
            NASAPolynomial(coeffs=[-4.42857,0.0838269,-5.2664e-05,1.57377e-08,-1.79928e-12,4610.35,43.5396], Tmin=(594.808,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (34.7223,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (457.296,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Indane calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: None
Location of calculations Pharos/home/laitcl/Gaussian/2017/Polycyclics/Indanes
""",
)

entry(
    index = 15,
    label = "IndaneRad",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {4,S} {7,D}
6  C u1 p0 c0 {1,S} {8,S} {17,S}
7  C u0 p0 c0 {5,D} {9,S} {20,S}
8  C u0 p0 c0 {6,S} {9,D} {19,S}
9  C u0 p0 c0 {7,S} {8,D} {18,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00206,-0.0021151,0.000260755,-4.42515e-07,2.37477e-10,19872.1,13.1337], Tmin=(10,'K'), Tmax=(577.899,'K')),
            NASAPolynomial(coeffs=[-4.52455,0.0883507,-5.56849e-05,1.6696e-08,-1.91438e-12,20332.5,45.0506], Tmin=(577.899,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (165.189,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (482.239,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Indane Radical calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: None
Location of calculations Pharos/home/laitcl/Gaussian/Polycyclics/Indanes
""",
)

entry(
    index = 16,
    label = "Ethyltetralin",
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
            NASAPolynomial(coeffs=[3.61601,0.0421213,0.00015139,-2.48903e-07,1.12973e-10,-7263.88,13.2472], Tmin=(10,'K'), Tmax=(739.354,'K')),
            NASAPolynomial(coeffs=[-1.18674,0.108057,-6.34363e-05,1.78905e-08,-1.95192e-12,-7645.69,27.5826], Tmin=(739.354,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-60.4008,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (673.472,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Ethyltetralin calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 2
Location of calculations Pharos/home/laitcl/Gaussian/Polycyclics/Tetralins
""",
)

entry(
    index = 17,
    label = "EthyltetralinRad",
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
            NASAPolynomial(coeffs=[3.61072,0.0473956,0.000136209,-2.20138e-07,9.53756e-11,6665.08,13.9706], Tmin=(10,'K'), Tmax=(788.688,'K')),
            NASAPolynomial(coeffs=[-0.103113,0.109241,-6.32144e-05,1.7577e-08,-1.89322e-12,5913.22,22.5258], Tmin=(788.688,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (55.4442,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (698.416,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Ethyltetralin Radical calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 2
Location of calculations Pharos/home/laitcl/Gaussian/Polycyclics/Tetralins
""",
)

entry(
    index = 18,
    label = "1-PentylRadical",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {3,S} {4,S}
2  H u0 p0 c0 {1,S}
3  H u0 p0 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
6  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
7  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47258,0.0518404,-9.83821e-05,2.1257e-07,-1.6797e-10,4338.11,12.5789], Tmin=(10,'K'), Tmax=(465.458,'K')),
            NASAPolynomial(coeffs=[0.536753,0.0539153,-3.045e-05,8.39691e-09,-9.05101e-13,4862.24,27.1919], Tmin=(465.458,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (36.0561,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (365.837,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Ethyltetralin Radical calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 4
Location of calculations Pharos/home/laitcl/Gaussian/2017/Aliphatic Radicals
""",
)

entry(
    index = 19,
    label = "HexylbenzeneRad2",
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
            NASAPolynomial(coeffs=[2.59877,0.154805,-0.000609286,1.62243e-06,-1.47593e-09,12181.7,19.7013], Tmin=(10,'K'), Tmax=(385.423,'K')),
            NASAPolynomial(coeffs=[-3.24183,0.115893,-7.05084e-05,2.05253e-08,-2.30125e-12,13371.2,51.9003], Tmin=(385.423,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (101.223,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (681.787,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Hexylbenzene Radical 2 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 6
Location of calculations Pharos/home/laitcl/Gaussian/2017/Alkylbenzene Radicals/Hexylbenzene Radicals
""",
)

entry(
    index = 20,
    label = "HexylbenzeneRad3",
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
            NASAPolynomial(coeffs=[2.65581,0.148005,-0.000555815,1.48704e-06,-1.36252e-09,11963.8,19.3575], Tmin=(10,'K'), Tmax=(384.533,'K')),
            NASAPolynomial(coeffs=[-3.19297,0.116297,-7.11077e-05,2.08011e-08,-2.34241e-12,13097.8,50.8816], Tmin=(384.533,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (99.4148,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (681.787,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Hexylbenzene Radical 3 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 6
Location of calculations Pharos/home/laitcl/Gaussian/2017/Alkylbenzene Radicals/Hexylbenzene Radicals
""",
)

entry(
    index = 21,
    label = "HexylbenzeneRad4",
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
            NASAPolynomial(coeffs=[2.64345,0.149629,-0.000570465,1.5282e-06,-1.40016e-09,11978.7,20.0013], Tmin=(10,'K'), Tmax=(384.254,'K')),
            NASAPolynomial(coeffs=[-3.25375,0.116365,-7.11154e-05,2.07901e-08,-2.33965e-12,13130.7,51.9042], Tmin=(384.254,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (99.5376,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (681.787,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Hexylbenzene Radical 4 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 6
Location of calculations Pharos/home/laitcl/Gaussian/2017/Alkylbenzene Radicals/Hexylbenzene Radicals
""",
)

entry(
    index = 22,
    label = "HexylbenzeneRad5",
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
            NASAPolynomial(coeffs=[2.48051,0.167113,-0.000676109,1.75368e-06,-1.56349e-09,11763.2,18.2517], Tmin=(10,'K'), Tmax=(388.368,'K')),
            NASAPolynomial(coeffs=[-2.51948,0.114282,-6.91072e-05,2.00059e-08,-2.23227e-12,12938.4,47.7742], Tmin=(388.368,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (97.7409,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (681.787,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Hexylbenzene Radical 5 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 6
Location of calculations Pharos/home/laitcl/Gaussian/2017/Alkylbenzene Radicals/Hexylbenzene Radicals
""",
)

entry(
    index = 23,
    label = "HexylbenzeneRad6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {6,S} {21,S} {22,S}
5  C u0 p0 c0 {2,S} {12,S} {19,S} {20,S}
6  C u0 p0 c0 {4,S} {7,B} {8,B}
7  C u0 p0 c0 {6,B} {9,B} {23,S}
8  C u0 p0 c0 {6,B} {11,B} {27,S}
9  C u0 p0 c0 {7,B} {10,B} {24,S}
10 C u0 p0 c0 {9,B} {11,B} {25,S}
11 C u0 p0 c0 {8,B} {10,B} {26,S}
12 C u1 p0 c0 {5,S} {28,S} {29,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {11,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.584,0.151846,-0.000517195,1.28776e-06,-1.12986e-09,13247.6,17.5928], Tmin=(10,'K'), Tmax=(393.806,'K')),
            NASAPolynomial(coeffs=[-1.35399,0.11298,-6.87556e-05,2.00694e-08,-2.2584e-12,14169.3,40.6859], Tmin=(393.806,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (110.099,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (681.787,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for Hexylbenzene Radical 6 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 6
Location of calculations Pharos/home/laitcl/Gaussian/2017/Alkylbenzene Radicals/Hexylbenzene Radicals
""",
)

entry(
    index = 24,
    label = "ToluenePlusHOrtho",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {5,D}
4  C u0 p0 c0 {1,S} {6,D} {13,S}
5  C u0 p0 c0 {3,D} {7,S} {15,S}
6  C u0 p0 c0 {4,D} {7,S} {16,S}
7  C u1 p0 c0 {5,S} {6,S} {14,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94447,0.00371676,0.000199109,-3.98552e-07,2.61611e-10,17316.8,11.5954], Tmin=(10,'K'), Tmax=(391.042,'K')),
            NASAPolynomial(coeffs=[-2.19466,0.0665475,-4.20309e-05,1.27717e-08,-1.49365e-12,17796.7,35.4456], Tmin=(391.042,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (143.977,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for ToluenePlusHOrtho calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2017/Aromatic Pi Radicals/Toluene Plus H
""",
)

entry(
    index = 25,
    label = "ToluenePlusHMeta",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,D} {6,S}
4  C u0 p0 c0 {1,S} {3,D} {13,S}
5  C u0 p0 c0 {1,S} {7,D} {14,S}
6  C u1 p0 c0 {3,S} {7,S} {15,S}
7  C u0 p0 c0 {5,D} {6,S} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94238,0.00373416,0.000189866,-3.65712e-07,2.29978e-10,17932.8,11.9908], Tmin=(10,'K'), Tmax=(408.683,'K')),
            NASAPolynomial(coeffs=[-2.52355,0.0669984,-4.2256e-05,1.28111e-08,-1.49441e-12,18461.5,37.4016], Tmin=(408.683,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (149.091,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for ToluenePlusHMeta calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2017/Aromatic Pi Radicals/Toluene Plus H
""",
)

entry(
    index = 26,
    label = "ToluenePlusHPara",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {6,D} {7,S}
4  C u1 p0 c0 {1,S} {6,S} {13,S}
5  C u0 p0 c0 {1,S} {7,D} {14,S}
6  C u0 p0 c0 {3,D} {4,S} {15,S}
7  C u0 p0 c0 {3,S} {5,D} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94034,0.00368031,0.000177387,-3.21352e-07,1.88539e-10,17945.9,12.8922], Tmin=(10,'K'), Tmax=(440.604,'K')),
            NASAPolynomial(coeffs=[-3.18806,0.0684758,-4.3479e-05,1.325e-08,-1.55155e-12,18573.3,41.4312], Tmin=(440.604,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (149.191,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for ToluenePlusHPara calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2017/Aromatic Pi Radicals/Toluene Plus H
""",
)

entry(
    index = 27,
    label = "ToluenePlusHSub",
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
            NASAPolynomial(coeffs=[3.92063,0.00475061,0.000180439,-3.25908e-07,1.86072e-10,18796.8,11.3844], Tmin=(10,'K'), Tmax=(522.294,'K')),
            NASAPolynomial(coeffs=[-2.5955,0.068928,-4.48671e-05,1.40017e-08,-1.67289e-12,19282.8,36.7249], Tmin=(522.294,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (156.255,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (378.308,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for ToluenePlusHSub calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2017/Aromatic Pi Radicals/Toluene Plus H
""",
)

entry(
    index = 28,
    label = "HexylbenzenePlusHOrtho",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {5,S} {19,S} {20,S}
4  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {8,S} {21,S} {22,S}
6  C u0 p0 c0 {8,S} {9,S} {23,S} {24,S}
7  C u0 p0 c0 {4,S} {25,S} {26,S} {27,S}
8  C u0 p0 c0 {5,S} {6,S} {10,D}
9  C u0 p0 c0 {6,S} {11,D} {28,S}
10 C u0 p0 c0 {8,D} {12,S} {30,S}
11 C u0 p0 c0 {9,D} {12,S} {31,S}
12 C u1 p0 c0 {10,S} {11,S} {29,S}
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
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {12,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5092,0.155564,-0.000463959,1.07605e-06,-8.99619e-10,2163.26,17.3803], Tmin=(10,'K'), Tmax=(410.116,'K')),
            NASAPolynomial(coeffs=[-0.830447,0.118095,-7.07428e-05,2.04243e-08,-2.28096e-12,3026.22,37.6967], Tmin=(410.116,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (17.9443,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (731.674,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for HexylbenzenePlusHOrtho calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 6
Location of calculations Pharos/home/laitcl/Gaussian/2017/Aromatic Pi Radicals/Hexylbenzene Plus H
""",
)

entry(
    index = 29,
    label = "HexylbenzenePlusHMeta",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {5,S} {19,S} {20,S}
4  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {8,S} {21,S} {22,S}
6  C u0 p0 c0 {9,S} {10,S} {23,S} {24,S}
7  C u0 p0 c0 {4,S} {25,S} {26,S} {27,S}
8  C u0 p0 c0 {5,S} {9,D} {11,S}
9  C u0 p0 c0 {6,S} {8,D} {28,S}
10 C u0 p0 c0 {6,S} {12,D} {29,S}
11 C u1 p0 c0 {8,S} {12,S} {30,S}
12 C u0 p0 c0 {10,D} {11,S} {31,S}
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
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {10,S}
30 H u0 p0 c0 {11,S}
31 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.46487,0.159417,-0.000477704,1.08646e-06,-8.93664e-10,2517.96,17.0356], Tmin=(10,'K'), Tmax=(413.815,'K')),
            NASAPolynomial(coeffs=[-0.387576,0.116927,-6.97228e-05,2.00563e-08,-2.23347e-12,3353.91,35.5284], Tmin=(413.815,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (20.8935,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (731.674,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for HexylbenzenePlusHMeta calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 6
Location of calculations Pharos/home/laitcl/Gaussian/Aromatic Pi Radicals/Hexylbenzene Plus H
""",
)

entry(
    index = 30,
    label = "HexylbenzenePlusHPara",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {5,S} {19,S} {20,S}
4  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {8,S} {21,S} {22,S}
6  C u0 p0 c0 {9,S} {10,S} {23,S} {24,S}
7  C u0 p0 c0 {4,S} {25,S} {26,S} {27,S}
8  C u0 p0 c0 {5,S} {11,S} {12,D}
9  C u0 p0 c0 {6,S} {11,D} {29,S}
10 C u1 p0 c0 {6,S} {12,S} {28,S}
11 C u0 p0 c0 {8,S} {9,D} {30,S}
12 C u0 p0 c0 {8,D} {10,S} {31,S}
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
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {11,S}
31 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.43449,0.164299,-0.000527222,1.22987e-06,-1.02501e-09,2442.97,16.4861], Tmin=(10,'K'), Tmax=(409.466,'K')),
            NASAPolynomial(coeffs=[-0.766387,0.117535,-7.00532e-05,2.01241e-08,-2.23728e-12,3359.26,37.0584], Tmin=(409.466,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (20.2667,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (731.674,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for HexylbenzenePlusHPara calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 6
Location of calculations Pharos/home/laitcl/Gaussian/Aromatic Pi Radicals/Hexylbenzene Plus H
""",
)

entry(
    index = 31,
    label = "HexylbenzenePlusHSub",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {13,S}
2  C u0 p0 c0 {1,S} {5,S} {22,S} {23,S}
3  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
6  C u0 p0 c0 {3,S} {7,S} {14,S} {15,S}
7  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
8  C u0 p0 c0 {1,S} {10,D} {27,S}
9  C u0 p0 c0 {1,S} {11,D} {28,S}
10 C u0 p0 c0 {8,D} {12,S} {30,S}
11 C u0 p0 c0 {9,D} {12,S} {31,S}
12 C u1 p0 c0 {10,S} {11,S} {29,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {12,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.57652,0.146954,-0.000385042,8.72638e-07,-7.31177e-10,3126.24,17.3622], Tmin=(10,'K'), Tmax=(409.446,'K')),
            NASAPolynomial(coeffs=[-0.418165,0.11887,-7.20885e-05,2.10489e-08,-2.37357e-12,3852.12,35.0052], Tmin=(409.446,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (25.9547,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (731.674,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for HexylbenzenePlusHSub calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 6
Location of calculations Pharos/home/laitcl/Gaussian/Aromatic Pi Radicals/Hexylbenzene Plus H
""",
)

entry(
    index = 32,
    label = "s2_5_6_diene_0_2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {6,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {1,S} {4,S} {8,D}
7  C u0 p0 c0 {5,S} {9,D} {19,S}
8  C u0 p0 c0 {6,D} {9,S} {21,S}
9  C u0 p0 c0 {7,D} {8,S} {20,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99757,-0.00147028,0.00025873,-4.32573e-07,2.30106e-10,8272.24,12.3533], Tmin=(10,'K'), Tmax=(570.669,'K')),
            NASAPolynomial(coeffs=[-5.74266,0.0928599,-5.77088e-05,1.71109e-08,-1.94559e-12,8959.63,50.163], Tmin=(570.669,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (68.7467,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (507.183,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for C1=CCC2CCCC2=C1 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: None
Location of calculations Pharos/home/laitcl/Gaussian/2017/Polycylics/2_5_6_Dienes
""",
)

entry(
    index = 33,
    label = "s2_5_6_diene_0_3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {7,S} {9,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {4,S} {7,D}
7  C u0 p0 c0 {5,S} {6,D} {20,S}
8  C u0 p0 c0 {1,S} {9,D} {21,S}
9  C u0 p0 c0 {5,S} {8,D} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97668,0.000259178,0.0002529,-4.28765e-07,2.31955e-10,8708.65,12.7211], Tmin=(10,'K'), Tmax=(552.288,'K')),
            NASAPolynomial(coeffs=[-5.85547,0.0930705,-5.78411e-05,1.71477e-08,-1.94953e-12,9465.25,51.3358], Tmin=(552.288,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (72.3762,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (507.183,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for C=1CC=C2CCCC2C1 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: None
Location of calculations Pharos/home/laitcl/Gaussian/2017/Polycylics/2_5_6_Dienes
""",
)

entry(
    index = 34,
    label = "s2_5_6_diene_1_3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {5,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {4,S} {14,S} {15,S}
6  C u0 p0 c0 {1,S} {8,D} {18,S}
7  C u0 p0 c0 {2,S} {9,D} {19,S}
8  C u0 p0 c0 {6,D} {9,S} {20,S}
9  C u0 p0 c0 {7,D} {8,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00318,-0.00185491,0.000256376,-4.22095e-07,2.20676e-10,8959.32,13.1756], Tmin=(10,'K'), Tmax=(582.446,'K')),
            NASAPolynomial(coeffs=[-5.94416,0.0933727,-5.81793e-05,1.72781e-08,-1.96553e-12,9661.57,51.8701], Tmin=(582.446,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (74.4602,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (507.183,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for C1=CC2CCCC2C=C1 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: None
Location of calculations Pharos/home/laitcl/Gaussian/2017/Polycylics/2_5_6_Dienes
""",
)

entry(
    index = 35,
    label = "s2_6_6_diene_0_2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,S} {16,S} {17,S}
5  C u0 p0 c0 {4,S} {7,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {8,S} {18,S} {19,S}
7  C u0 p0 c0 {1,S} {5,S} {9,D}
8  C u0 p0 c0 {6,S} {10,D} {22,S}
9  C u0 p0 c0 {7,D} {10,S} {24,S}
10 C u0 p0 c0 {8,D} {9,S} {23,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89996,0.00597168,0.000268757,-4.68371e-07,2.63151e-10,2865.77,12.7943], Tmin=(10,'K'), Tmax=(460.501,'K')),
            NASAPolynomial(coeffs=[-8.0572,0.109805,-6.93645e-05,2.09875e-08,-2.43984e-12,3967.34,61.212], Tmin=(460.501,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (23.7851,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (582.013,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for C1=CCC2CCCCC2=C1 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: None
Location of calculations Pharos/home/laitcl/Gaussian/2017/Polycylics/2_6_6_Dienes
""",
)

entry(
    index = 36,
    label = "s2_6_6_diene_0_3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,S} {12,S} {13,S}
5  C u0 p0 c0 {4,S} {7,S} {18,S} {19,S}
6  C u0 p0 c0 {8,S} {10,S} {20,S} {21,S}
7  C u0 p0 c0 {1,S} {5,S} {8,D}
8  C u0 p0 c0 {6,S} {7,D} {23,S}
9  C u0 p0 c0 {1,S} {10,D} {24,S}
10 C u0 p0 c0 {6,S} {9,D} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89946,0.00597198,0.000266684,-4.61897e-07,2.57724e-10,2508.5,12.6651], Tmin=(10,'K'), Tmax=(463.874,'K')),
            NASAPolynomial(coeffs=[-8.16301,0.109952,-6.94353e-05,2.10011e-08,-2.4406e-12,3627.97,61.5979], Tmin=(463.874,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (20.8133,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (582.013,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for C=1CC=C2CCCCC2C1 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: None
Location of calculations Pharos/home/laitcl/Gaussian/2017/Polycylics/2_6_6_Dienes
""",
)

entry(
    index = 37,
    label = "s2_6_6_diene_1_3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {6,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {5,S} {17,S} {18,S}
7  C u0 p0 c0 {1,S} {10,D} {21,S}
8  C u0 p0 c0 {2,S} {9,D} {22,S}
9  C u0 p0 c0 {8,D} {10,S} {23,S}
10 C u0 p0 c0 {7,D} {9,S} {24,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99014,-0.00119968,0.000302494,-5.14955e-07,2.79612e-10,3294.92,12.6133], Tmin=(10,'K'), Tmax=(556.754,'K')),
            NASAPolynomial(coeffs=[-7.01886,0.10676,-6.61404e-05,1.95763e-08,-2.22479e-12,4073.4,55.2604], Tmin=(556.754,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (27.3577,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (582.013,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for C=1C=CC2CCCCC2C1 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: None
Location of calculations Pharos/home/laitcl/Gaussian/2017/Polycylics/2_6_6_Dienes
""",
)

entry(
    index = 38,
    label = "ToluenePlusCH3Ortho",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {3,S} {6,D}
5  C u1 p0 c0 {1,S} {7,S} {16,S}
6  C u0 p0 c0 {4,D} {8,S} {19,S}
7  C u0 p0 c0 {5,S} {8,D} {17,S}
8  C u0 p0 c0 {6,S} {7,D} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72076,0.0241095,0.000129351,-2.38191e-07,1.28204e-10,13740.3,12.42], Tmin=(10,'K'), Tmax=(589.69,'K')),
            NASAPolynomial(coeffs=[-0.734489,0.0733613,-4.43407e-05,1.29026e-08,-1.44971e-12,13934.8,28.7553], Tmin=(589.69,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (114.2,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CC1=CC=C[CH]C1C calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 2
Location of calculations Pharos/home/laitcl/Gaussian/2017/Aromatic Pi Radicals/Toluene Plus CH3
""",
)

entry(
    index = 39,
    label = "ToluenePlusCH3Meta",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,S} {7,D}
5  C u1 p0 c0 {1,S} {4,S} {16,S}
6  C u0 p0 c0 {1,S} {8,D} {17,S}
7  C u0 p0 c0 {4,D} {8,S} {19,S}
8  C u0 p0 c0 {6,D} {7,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72371,0.0274434,9.94458e-05,-1.67849e-07,7.8708e-11,14002.6,12.4], Tmin=(10,'K'), Tmax=(707.48,'K')),
            NASAPolynomial(coeffs=[0.2413,0.0705396,-4.15544e-05,1.17818e-08,-1.29269e-12,13909.5,23.8555], Tmin=(707.48,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (116.404,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CC1[CH]C(C)C=CC=1 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 2
Location of calculations Pharos/home/laitcl/Gaussian/2017/Aromatic Pi Radicals/Toluene Plus CH3
""",
)

entry(
    index = 40,
    label = "ToluenePlusCH3Para",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {7,S} {8,D}
5  C u0 p0 c0 {1,S} {7,D} {17,S}
6  C u1 p0 c0 {1,S} {8,S} {16,S}
7  C u0 p0 c0 {4,S} {5,D} {18,S}
8  C u0 p0 c0 {4,D} {6,S} {19,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7767,0.0221935,0.000122585,-2.04708e-07,9.87735e-11,13994.9,13.1807], Tmin=(10,'K'), Tmax=(675.578,'K')),
            NASAPolynomial(coeffs=[-0.565165,0.07235,-4.30629e-05,1.2323e-08,-1.36284e-12,14023.6,28.2956], Tmin=(675.578,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (116.338,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CC1C=CC(C)[CH]C=1 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 2
Location of calculations Pharos/home/laitcl/Gaussian/2017/Aromatic Pi Radicals/Toluene Plus CH3
""",
)

entry(
    index = 41,
    label = "ToluenePlusCH3Sub",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {6,D} {16,S}
5  C u1 p0 c0 {1,S} {7,S} {15,S}
6  C u0 p0 c0 {4,D} {8,S} {17,S}
7  C u0 p0 c0 {5,S} {8,D} {19,S}
8  C u0 p0 c0 {6,S} {7,D} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8507,0.00911754,0.000234697,-4.61266e-07,2.80881e-10,14243,12.2953], Tmin=(10,'K'), Tmax=(522.569,'K')),
            NASAPolynomial(coeffs=[-0.884215,0.0766366,-4.88867e-05,1.50468e-08,-1.78165e-12,14310.8,27.9796], Tmin=(522.569,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (118.372,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (448.981,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CC1(C)[CH]C=CC=C1 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 2
Location of calculations Pharos/home/laitcl/Gaussian/2017/Aromatic Pi Radicals/Toluene Plus CH3
""",
)

entry(
    index = 42,
    label = "MethylindaneRad",
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
            NASAPolynomial(coeffs=[3.87145,0.00797269,0.000286891,-5.46886e-07,3.30988e-10,15350.8,13.9369], Tmin=(10,'K'), Tmax=(495.001,'K')),
            NASAPolynomial(coeffs=[-4.82043,0.101076,-6.45337e-05,1.9735e-08,-2.31577e-12,15931.1,46.9284], Tmin=(495.001,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (127.595,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (552.912,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CC1CCC2=CC=C[CH]C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/IndaneRads
""",
)

entry(
    index = 43,
    label = "EthylindaneRad",
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
            NASAPolynomial(coeffs=[3.5731,0.0392082,0.000162014,-2.91624e-07,1.47965e-10,12244,14.063], Tmin=(10,'K'), Tmax=(647.822,'K')),
            NASAPolynomial(coeffs=[-1.35071,0.102782,-6.19964e-05,1.79457e-08,-2.00379e-12,12185.9,30.3076], Tmin=(647.822,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (101.746,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (623.585,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CCC1CCC2=CC=C[CH]C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 2
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/IndaneRads
""",
)

entry(
    index = 44,
    label = "PropylindaneRad",
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
            NASAPolynomial(coeffs=[3.33,0.0603379,0.000113878,-2.24108e-07,1.11512e-10,9175.45,14.9037], Tmin=(10,'K'), Tmax=(683.912,'K')),
            NASAPolynomial(coeffs=[0.178328,0.1105,-6.57292e-05,1.8805e-08,-2.07976e-12,8864.52,23.4864], Tmin=(683.912,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (76.2158,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (694.258,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CCCC1CCC2=CC=C[CH]C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 3
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/IndaneRads
""",
)

entry(
    index = 45,
    label = "Methylindane",
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
            NASAPolynomial(coeffs=[3.92096,0.00515781,0.000281383,-5.4323e-07,3.41557e-10,-137.524,12.5997], Tmin=(10,'K'), Tmax=(409.297,'K')),
            NASAPolynomial(coeffs=[-5.73827,0.099538,-6.44375e-05,1.99373e-08,-2.36147e-12,653.326,50.573], Tmin=(409.297,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-1.15498,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (527.969,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CC1CCC2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/Indanes
""",
)

entry(
    index = 46,
    label = "Ethylindane",
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
            NASAPolynomial(coeffs=[3.65715,0.0324995,0.000173031,-3.02031e-07,1.51736e-10,-3254.41,12.9243], Tmin=(10,'K'), Tmax=(650.823,'K')),
            NASAPolynomial(coeffs=[-1.68411,0.0994848,-6.00804e-05,1.73971e-08,-1.94243e-12,-3282.57,30.841], Tmin=(650.823,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-27.1045,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (598.642,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CCC1CCC2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 2
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/Indanes
""",
)

entry(
    index = 47,
    label = "Propylindane",
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
            NASAPolynomial(coeffs=[3.40999,0.0552511,0.000114719,-2.14633e-07,1.03074e-10,-6379.51,13.8328], Tmin=(10,'K'), Tmax=(710.114,'K')),
            NASAPolynomial(coeffs=[0.289053,0.106048,-6.27461e-05,1.78466e-08,-1.96282e-12,-6773.77,21.9242], Tmin=(710.114,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-53.0952,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (669.315,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CCCC1CCC2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 3
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/Indanes
""",
)

entry(
    index = 48,
    label = "IndeneRad",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {4,B} {6,B}
4  C u0 p0 c0 {3,B} {5,S} {7,B}
5  C u1 p0 c0 {2,S} {4,S} {14,S}
6  C u0 p0 c0 {3,B} {9,B} {17,S}
7  C u0 p0 c0 {4,B} {8,B} {18,S}
8  C u0 p0 c0 {7,B} {9,B} {15,S}
9  C u0 p0 c0 {6,B} {8,B} {16,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93261,0.00413367,0.000215054,-3.85136e-07,2.21506e-10,22304.4,12.3971], Tmin=(10,'K'), Tmax=(450.293,'K')),
            NASAPolynomial(coeffs=[-5.31695,0.0861841,-5.78892e-05,1.83963e-08,-2.21985e-12,23138.5,49.6539], Tmin=(450.293,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (185.426,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (432.353,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for C1=CC=C2CC[CH]C2=C1 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 0
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/IndeneRads
""",
)

entry(
    index = 49,
    label = "MethylindeneRadFar",
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
            NASAPolynomial(coeffs=[3.86021,0.00837721,0.000258425,-4.8236e-07,2.81146e-10,18239.4,14.0511], Tmin=(10,'K'), Tmax=(531.007,'K')),
            NASAPolynomial(coeffs=[-3.58728,0.0928827,-6.05253e-05,1.88114e-08,-2.23461e-12,18629.9,41.4961], Tmin=(531.007,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (151.598,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CC1C[CH]C2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/IndeneRads
""",
)

entry(
    index = 50,
    label = "MethylindeneRadNear",
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
            NASAPolynomial(coeffs=[3.91998,0.00547133,0.000286726,-5.93413e-07,4.03433e-10,16854.2,14.8887], Tmin=(10,'K'), Tmax=(376.737,'K')),
            NASAPolynomial(coeffs=[-4.26068,0.0922982,-5.88556e-05,1.7903e-08,-2.08614e-12,17470.8,46.3725], Tmin=(376.737,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (140.133,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for C[C]1CCC2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/IndeneRads
""",
)

entry(
    index = 51,
    label = "EthylindeneRadFar",
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
            NASAPolynomial(coeffs=[3.63048,0.0379893,0.000138553,-2.42553e-07,1.16875e-10,15045.1,13.7297], Tmin=(10,'K'), Tmax=(699.543,'K')),
            NASAPolynomial(coeffs=[0.346596,0.0926916,-5.57754e-05,1.60546e-08,-1.78084e-12,14625.5,22.1163], Tmin=(699.543,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (125.064,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (573.699,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CCC1C[CH]C2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 2
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/IndeneRads
""",
)

entry(
    index = 52,
    label = "EthylindeneRadNear",
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
            NASAPolynomial(coeffs=[3.74375,0.040327,0.000104701,-1.66257e-07,6.93336e-11,13871.9,14.2845], Tmin=(10,'K'), Tmax=(835.823,'K')),
            NASAPolynomial(coeffs=[2.31239,0.086802,-4.98173e-05,1.37097e-08,-1.46114e-12,12727,12.6534], Tmin=(835.823,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (115.405,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (577.856,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CC[C]1CCC2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/IndeneRads
""",
)

entry(
    index = 53,
    label = "PropylindeneRadFar",
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
            NASAPolynomial(coeffs=[3.39035,0.0610035,7.99589e-05,-1.58513e-07,7.27885e-11,11934.9,14.6399], Tmin=(10,'K'), Tmax=(775.75,'K')),
            NASAPolynomial(coeffs=[2.8705,0.0978084,-5.71908e-05,1.60557e-08,-1.74384e-12,10988.8,10.3979], Tmin=(775.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (99.2072,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (644.372,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CCCC1C[CH]C2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 3
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/IndeneRads
""",
)

entry(
    index = 54,
    label = "PropylindeneRadNear",
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
            NASAPolynomial(coeffs=[3.63145,0.060064,5.88229e-05,-1.06e-07,4.12778e-11,10609.9,14.3421], Tmin=(10,'K'), Tmax=(956.069,'K')),
            NASAPolynomial(coeffs=[6.72759,0.0875392,-4.77132e-05,1.25168e-08,-1.27841e-12,8170.12,-10.119], Tmin=(956.069,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (88.3235,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (648.529,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CCC[C]1CCC2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 2
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/IndeneRads
""",
)

entry(
    index = 55,
    label = "Indene",
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
            NASAPolynomial(coeffs=[4.12648,-0.0123417,0.000280961,-4.80678e-07,2.61244e-10,16798.3,11.5839], Tmin=(10,'K'), Tmax=(586.093,'K')),
            NASAPolynomial(coeffs=[-2.51184,0.0745743,-4.79801e-05,1.46194e-08,-1.69721e-12,16861.8,33.9663], Tmin=(586.093,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (139.639,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (407.409,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for C1=CC=C2CC=CC2=C1 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 0
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/Indenes
""",
)

entry(
    index = 56,
    label = "MethylindeneFar",
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
            NASAPolynomial(coeffs=[3.87326,0.00747494,0.000240528,-4.37359e-07,2.48011e-10,12896.6,12.2266], Tmin=(10,'K'), Tmax=(543.271,'K')),
            NASAPolynomial(coeffs=[-3.86147,0.0903139,-5.96771e-05,1.87515e-08,-2.24574e-12,13355,41.3066], Tmin=(543.271,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (107.177,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (478.082,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CC1C=CC2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/Indenes
""",
)

entry(
    index = 57,
    label = "MethylindeneNear",
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
            NASAPolynomial(coeffs=[3.87494,0.00766011,0.000248265,-4.72926e-07,2.83475e-10,11331,12.4502], Tmin=(10,'K'), Tmax=(510.06,'K')),
            NASAPolynomial(coeffs=[-3.19975,0.0871573,-5.61498e-05,1.72662e-08,-2.03269e-12,11740.3,38.7562], Tmin=(510.06,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (94.1695,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (478.082,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CC1=CCC2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/Indenes
""",
)

entry(
    index = 58,
    label = "EthylindeneFar",
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
            NASAPolynomial(coeffs=[3.83518,0.0106899,0.000312449,-6.49336e-07,4.26128e-10,9936.96,14.0537], Tmin=(10,'K'), Tmax=(468.75,'K')),
            NASAPolynomial(coeffs=[-2.97546,0.0983983,-6.29085e-05,1.91772e-08,-2.2373e-12,10250.4,38.2831], Tmin=(468.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (82.5865,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (548.755,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CCC1C=CC2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 2
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/Indenes
""",
)

entry(
    index = 59,
    label = "EthylindeneNear",
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
            NASAPolynomial(coeffs=[3.85385,0.00990698,0.000323347,-6.98214e-07,4.83402e-10,8415.13,14.3821], Tmin=(10,'K'), Tmax=(431.533,'K')),
            NASAPolynomial(coeffs=[-3.25898,0.0983784,-6.25292e-05,1.89617e-08,-2.20327e-12,8819.14,40.2879], Tmin=(431.533,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (69.9549,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (548.755,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CCC1=CCC2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 2
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/Indenes
""",
)

entry(
    index = 60,
    label = "PropylindeneFar",
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
            NASAPolynomial(coeffs=[3.4936,0.0548245,8.80631e-05,-1.63331e-07,7.32913e-11,6718.15,13.7528], Tmin=(10,'K'), Tmax=(789.565,'K')),
            NASAPolynomial(coeffs=[2.92874,0.0938657,-5.484e-05,1.53632e-08,-1.66432e-12,5679.61,9.20296], Tmin=(789.565,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (55.8578,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (619.428,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CCCC1C=CC2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 3
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/Indenes
""",
)

entry(
    index = 61,
    label = "PropylindeneNear",
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
            NASAPolynomial(coeffs=[3.57227,0.0515251,9.19646e-05,-1.60443e-07,6.92396e-11,5208.32,14.8218], Tmin=(10,'K'), Tmax=(819.095,'K')),
            NASAPolynomial(coeffs=[2.87998,0.0929882,-5.37061e-05,1.4881e-08,-1.59636e-12,4044.22,10.2253], Tmin=(819.095,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (43.3347,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (619.428,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CCCC1=CCC2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 3
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/Indenes
""",
)

entry(
    index = 62,
    label = "TetralinRad",
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
            NASAPolynomial(coeffs=[3.90822,0.00556102,0.000268158,-4.75068e-07,2.71104e-10,13266.1,12.33], Tmin=(10,'K'), Tmax=(454.826,'K')),
            NASAPolynomial(coeffs=[-7.69058,0.107814,-6.98823e-05,2.16116e-08,-2.55652e-12,14318.6,59.1214], Tmin=(454.826,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (110.266,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (557.07,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for C1=CC=C2CCCCC2[CH]1 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 0
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/TetralinRads
""",
)

entry(
    index = 63,
    label = "MethyltetralinRad",
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
            NASAPolynomial(coeffs=[3.86316,0.00863059,0.000331304,-6.39874e-07,3.94974e-10,9272.82,14.2955], Tmin=(10,'K'), Tmax=(478.421,'K')),
            NASAPolynomial(coeffs=[-6.15246,0.11497,-7.29663e-05,2.22085e-08,-2.59689e-12,9972.5,52.5277], Tmin=(478.421,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (77.0629,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (627.743,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CC1CCCC2=CC=C[CH]C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/TetralinRads
""",
)

entry(
    index = 64,
    label = "Tetralin",
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
            NASAPolynomial(coeffs=[3.98095,-0.000430483,0.000276899,-4.72432e-07,2.5606e-10,-504.573,12.7905], Tmin=(10,'K'), Tmax=(561.625,'K')),
            NASAPolynomial(coeffs=[-5.89597,0.0980584,-6.13135e-05,1.82617e-08,-2.08374e-12,160.996,50.7912], Tmin=(561.625,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-4.23297,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (532.126,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for C1=CC=C2CCCCC2=C1 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 0
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/Tetralins
""",
)

entry(
    index = 65,
    label = "Methyltetralin",
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
            NASAPolynomial(coeffs=[3.90763,0.00613766,0.000329619,-6.53365e-07,4.23669e-10,-4305.36,13.4762], Tmin=(10,'K'), Tmax=(395.99,'K')),
            NASAPolynomial(coeffs=[-6.57847,0.112047,-7.15083e-05,2.18617e-08,-2.56504e-12,-3474.77,54.3529], Tmin=(395.99,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-35.8053,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (602.799,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CC1CCCC2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/Tetralins
""",
)

entry(
    index = 66,
    label = "DihydronaphthaleneRad",
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
            NASAPolynomial(coeffs=[3.92103,0.00492435,0.000257755,-4.71132e-07,2.7786e-10,16865.3,12.7165], Tmin=(10,'K'), Tmax=(439.897,'K')),
            NASAPolynomial(coeffs=[-6.44992,0.0995149,-6.57672e-05,2.06512e-08,-2.47112e-12,17774.9,54.202], Tmin=(439.897,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (140.203,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (507.183,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for C1=CC=C2CCC[CH]C2=C1 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 0
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/DihydronaphthaleneRads
""",
)

entry(
    index = 67,
    label = "MethyldihydronaphthaleneRadFar",
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
            NASAPolynomial(coeffs=[3.90618,0.00637912,0.000327572,-6.74205e-07,4.55856e-10,12287.5,15.0788], Tmin=(10,'K'), Tmax=(379.13,'K')),
            NASAPolynomial(coeffs=[-5.54236,0.106115,-6.72226e-05,2.03511e-08,-2.36375e-12,13003.6,51.4939], Tmin=(379.13,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (102.161,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (577.856,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for C[C]1CCCC2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/DihydronaphthaleneRads
""",
)

entry(
    index = 68,
    label = "MethyldihydronaphthaleneRadNear",
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
            NASAPolynomial(coeffs=[3.84484,0.00946585,0.000302092,-5.73677e-07,3.42289e-10,13221.1,14.0055], Tmin=(10,'K'), Tmax=(514.157,'K')),
            NASAPolynomial(coeffs=[-4.70857,0.106235,-6.84021e-05,2.1051e-08,-2.48165e-12,13701.2,45.6956], Tmin=(514.157,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (109.873,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (577.856,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CC1CC[CH]C2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/DihydronaphthaleneRads
""",
)

entry(
    index = 69,
    label = "EthyldihydronaphthaleneRadFar",
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
            NASAPolynomial(coeffs=[3.88284,0.00854295,0.000409761,-9.32105e-07,7.03554e-10,9291.07,15.5384], Tmin=(10,'K'), Tmax=(337.89,'K')),
            NASAPolynomial(coeffs=[-5.32232,0.117513,-7.39788e-05,2.23052e-08,-2.58435e-12,9913.15,49.9603], Tmin=(337.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (77.2697,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (652.686,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CC[C]1CCCC2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/DihydronaphthaleneRads
""",
)

entry(
    index = 70,
    label = "EthyldihydronaphthaleneRadNear",
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
            NASAPolynomial(coeffs=[3.88569,0.00829346,0.000407941,-9.1989e-07,6.87602e-10,10604.9,15.1459], Tmin=(10,'K'), Tmax=(341.365,'K')),
            NASAPolynomial(coeffs=[-5.48684,0.118118,-7.4645e-05,2.25776e-08,-2.62144e-12,11244.8,50.2892], Tmin=(341.365,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (88.1927,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (652.686,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CCC1CC[CH]C2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/DihydronaphthaleneRads
""",
)

entry(
    index = 71,
    label = "Dihydronaphthalene",
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
            NASAPolynomial(coeffs=[3.92322,0.00469741,0.00023911,-4.2755e-07,2.45774e-10,12024.2,11.8044], Tmin=(10,'K'), Tmax=(450.877,'K')),
            NASAPolynomial(coeffs=[-6.33371,0.0956917,-6.36106e-05,2.00471e-08,-2.40401e-12,12949.2,53.118], Tmin=(450.877,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (99.9486,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (482.239,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for C1=CC=C2CCC=CC2=C1 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 0
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/Dihydronaphthalenes
""",
)

entry(
    index = 72,
    label = "MethyldihydronaphthaleneFar",
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
            NASAPolynomial(coeffs=[3.85493,0.00898588,0.000292264,-5.64393e-07,3.43868e-10,7375.22,13.1356], Tmin=(10,'K'), Tmax=(500.64,'K')),
            NASAPolynomial(coeffs=[-4.19583,0.100667,-6.43965e-05,1.96981e-08,-2.31031e-12,7838.48,42.9817], Tmin=(500.64,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (61.2761,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (552.912,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CC1=CCCC2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/Dihydronaphthalenes
""",
)

entry(
    index = 73,
    label = "MethyldihydronaphthaleneNear",
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
            NASAPolynomial(coeffs=[3.85456,0.00877977,0.000285495,-5.3358e-07,3.12891e-10,8296.1,13.0483], Tmin=(10,'K'), Tmax=(522.457,'K')),
            NASAPolynomial(coeffs=[-4.70306,0.102889,-6.67846e-05,2.06809e-08,-2.44921e-12,8800.08,45.0438], Tmin=(522.457,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (68.9248,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (552.912,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CC1CC=CC2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/Dihydronaphthalenes
""",
)

entry(
    index = 74,
    label = "EthyldihydronaphthaleneFar",
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
            NASAPolynomial(coeffs=[3.89095,0.00790323,0.0003922,-8.82366e-07,6.57738e-10,4511.56,14.3294], Tmin=(10,'K'), Tmax=(342.367,'K')),
            NASAPolynomial(coeffs=[-5.18089,0.113893,-7.2168e-05,2.18659e-08,-2.54144e-12,5132.74,48.3719], Tmin=(342.367,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (37.5293,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (627.743,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CCC1=CCCC2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/Dihydronaphthalenes
""",
)

entry(
    index = 75,
    label = "EthyldihydronaphthaleneNear",
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
            NASAPolynomial(coeffs=[3.63851,0.040388,0.000146556,-2.4654e-07,1.14035e-10,4767,13.3608], Tmin=(10,'K'), Tmax=(730.889,'K')),
            NASAPolynomial(coeffs=[-0.0490767,0.10078,-5.99094e-05,1.70557e-08,-1.87402e-12,4232.02,22.6479], Tmin=(730.889,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (39.6284,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (627.743,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CCC1CC=CC2=CC=CC=C21 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/Dihydronaphthalenes
""",
)

entry(
    index = 76,
    label = "NaphthaleneRad",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {3,B} {4,S} {8,B}
3  C u0 p0 c0 {2,B} {6,S} {7,B}
4  C u1 p0 c0 {1,S} {2,S} {13,S}
5  C u0 p0 c0 {1,S} {6,D} {14,S}
6  C u0 p0 c0 {3,S} {5,D} {18,S}
7  C u0 p0 c0 {3,B} {10,B} {17,S}
8  C u0 p0 c0 {2,B} {9,B} {19,S}
9  C u0 p0 c0 {8,B} {10,B} {15,S}
10 C u0 p0 c0 {7,B} {9,B} {16,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89212,0.00631001,0.000227169,-4.02625e-07,2.23242e-10,26140.3,12.7799], Tmin=(10,'K'), Tmax=(545.007,'K')),
            NASAPolynomial(coeffs=[-4.70453,0.0901466,-6.06608e-05,1.92886e-08,-2.32777e-12,26769.3,46.2097], Tmin=(545.007,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (217.298,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (457.296,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for C1=CC=C2C=CC[CH]C2=C1 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 0
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/NaphthaleneRads
""",
)

entry(
    index = 77,
    label = "MethylnaphthaleneRadFar",
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
            NASAPolynomial(coeffs=[3.83251,0.00997216,0.000277293,-5.21955e-07,3.04113e-10,22415.3,13.9718], Tmin=(10,'K'), Tmax=(541.059,'K')),
            NASAPolynomial(coeffs=[-3.21384,0.0975899,-6.40998e-05,2.00427e-08,-2.3914e-12,22657.8,38.8331], Tmin=(541.059,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (186.306,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (527.969,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CC1[CH]C=CC2=CC=CC=C12 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/NaphthaleneRads
""",
)

entry(
    index = 78,
    label = "MethylnaphthaleneRadNear",
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
            NASAPolynomial(coeffs=[3.8442,0.00990569,0.000293443,-5.94037e-07,3.78699e-10,21581,14.372], Tmin=(10,'K'), Tmax=(483.667,'K')),
            NASAPolynomial(coeffs=[-2.94124,0.095087,-6.08693e-05,1.85762e-08,-2.1704e-12,21897.4,38.6648], Tmin=(483.667,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (179.395,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (527.969,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CC1=C[CH]CC2=CC=CC=C12 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/NaphthaleneRads
""",
)

entry(
    index = 79,
    label = "EthylnaphthaleneRadFar",
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
            NASAPolynomial(coeffs=[3.82248,0.012031,0.000359447,-7.83632e-07,5.44838e-10,18703.3,15.8043], Tmin=(10,'K'), Tmax=(435.801,'K')),
            NASAPolynomial(coeffs=[-3.54395,0.108037,-6.8726e-05,2.08642e-08,-2.42724e-12,19075.8,42.1313], Tmin=(435.801,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (155.491,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (602.799,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CCC1[CH]C=CC2=CC=CC=C12 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/NaphthaleneRads
""",
)

entry(
    index = 80,
    label = "EthylnaphthaleneRadNear",
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
            NASAPolynomial(coeffs=[3.80001,0.0132491,0.000354645,-7.63159e-07,5.17377e-10,18918.1,15.7442], Tmin=(10,'K'), Tmax=(457.035,'K')),
            NASAPolynomial(coeffs=[-3.03356,0.107733,-6.92646e-05,2.11989e-08,-2.47921e-12,19180.5,39.3994], Tmin=(457.035,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (157.261,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (598.642,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CCC1=C[CH]CC2=CC=CC=C12 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/NaphthaleneRads
""",
)

entry(
    index = 81,
    label = "Naphthalene",
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
            NASAPolynomial(coeffs=[4.1155,-0.0118741,0.000302555,-5.25571e-07,2.89125e-10,15184.8,12.1184], Tmin=(10,'K'), Tmax=(581.285,'K')),
            NASAPolynomial(coeffs=[-2.55933,0.0797241,-5.16554e-05,1.58185e-08,-1.84313e-12,15189.2,34.0631], Tmin=(581.285,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (126.216,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (432.353,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for C1=CC=C2C=CC=CC2=C1 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 0
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/Naphthalenes
""",
)

entry(
    index = 82,
    label = "Methylnaphthalene",
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
            NASAPolynomial(coeffs=[3.85335,0.0088481,0.000263357,-4.98642e-07,2.94455e-10,10578.1,12.7883], Tmin=(10,'K'), Tmax=(526.62,'K')),
            NASAPolynomial(coeffs=[-3.25195,0.0926529,-6.03314e-05,1.87081e-08,-2.21644e-12,10912.8,38.5828], Tmin=(526.62,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (87.8981,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (503.026,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CC1=CC=CC2=CC=CC=C12 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/Naphthalenes
""",
)

entry(
    index = 83,
    label = "Ethylnaphthalene",
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
            NASAPolynomial(coeffs=[3.82344,0.0109891,0.00031613,-6.2575e-07,3.87798e-10,7751.11,14.2484], Tmin=(10,'K'), Tmax=(501.992,'K')),
            NASAPolynomial(coeffs=[-3.60545,0.104749,-6.73134e-05,2.06413e-08,-2.42317e-12,8061.45,40.631], Tmin=(501.992,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (64.3929,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (577.856,'J/(mol*K)'),
    ),
    shortDesc = u"""library value for CCC1=CC=CC2=CC=CC=C12 calculated by Lawrence Lai""",
    longDesc = 
u"""
Level of theory: CBS-QB3
Hindered Rotors Included: 1
Location of calculations Pharos/home/laitcl/Gaussian/2018/Indenes_Naphthalenes/Naphthalenes
""",
)

