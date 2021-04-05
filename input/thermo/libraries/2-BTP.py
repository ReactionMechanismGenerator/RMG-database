#!/usr/bin/env python
# encoding: utf-8

name = "2-BTP"
shortDesc = "2-BTP thermo library (Burgess, 2015)"
longDesc = """
Burgess, D. R., Babushok, V. I., Linteris, G. T., & Manion, J. A. (2015).
A Chemical Kinetic Mechanism for 2-Bromo-3,3,3-trifluoropropene (2-BTP) Flame Inhibition.
International Journal of Chemical Kinetics, 47(9), 533?563. https://doi.org/10.1002/kin.20923\
Obtained from https://onlinelibrary.wiley.com/doi/full/10.1002/kin.20923

This library contains C/H/O/F/Br chemistry
It is recommended for fluorinated and chlorinated hydrocarbons
"""
entry(
    index = 0,
    label = "HF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43657,0.000486021,-1.2524e-06,1.36475e-09,-4.09574e-13,-33800.1,1.20682], Tmin=(298,'K'), Tmax=(1250,'K')),
            NASAPolynomial(coeffs=[2.7813,0.00103959,-2.41735e-07,2.68416e-11,-1.09766e-15,-33504.2,5.0197], Tmin=(1250,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-281.113,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """71STUPRO""",
    longDesc = 
"""
71STUPRO
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 1,
    label = "F",
    molecule = 
"""
multiplicity 2
1 F u1 p3 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.90371,-0.000635296,2.64735e-07,7.69063e-11,-5.45254e-14,8672.27,2.70828], Tmin=(298,'K'), Tmax=(1400,'K')),
            NASAPolynomial(coeffs=[2.65117,-0.00014013,5.19236e-08,-8.84954e-12,5.9028e-16,8758.29,4.07857], Tmin=(1400,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (72.8916,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """71STUPRO""",
    longDesc = 
"""
71STUPRO
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[F]
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 2,
    label = "F2",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 F u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.66955,0.00529418,-6.47091e-06,3.91833e-09,-9.38451e-13,-980.801,7.82659], Tmin=(298,'K'), Tmax=(1150,'K')),
            NASAPolynomial(coeffs=[4.05774,0.000600034,-2.19218e-07,4.31508e-11,-3.12588e-15,-1324.39,0.863214], Tmin=(1150,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-8.80492,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """71STUPRO""",
    longDesc = 
"""
71STUPRO
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FF
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 3,
    label = "CH3F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.59624,0.00365317,1.31032e-05,-1.4533e-08,4.48014e-12,-29006.8,10.4823], Tmin=(298,'K'), Tmax=(1100,'K')),
            NASAPolynomial(coeffs=[2.644,0.00997251,-3.98497e-06,7.25148e-10,-4.8844e-14,-29427.1,8.42306], Tmin=(1100,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-242.471,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """78KOL74CHEROD""",
    longDesc = 
"""
78KOL74CHEROD
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CF
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 4,
    label = "CH2F2",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.73901,0.0119379,-2.69321e-07,-5.51894e-09,2.18135e-12,-55439.7,16.2342], Tmin=(298,'K'), Tmax=(1100,'K')),
            NASAPolynomial(coeffs=[4.5585,0.00831979,-3.37157e-06,6.18797e-10,-4.19515e-14,-56506.2,0.436637], Tmin=(1100,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-462.682,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """78KOL74CHEROD""",
    longDesc = 
"""
78KOL74CHEROD
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FCF
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 5,
    label = "CHF3",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.680758,0.0239859,-2.18336e-05,9.98026e-09,-1.85179e-12,-84989.4,21.0617], Tmin=(298,'K'), Tmax=(1300,'K')),
            NASAPolynomial(coeffs=[7.52417,0.00523005,-2.036e-06,3.57296e-10,-2.30997e-14,-87022.5,-14.6112], Tmin=(1300,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-708.855,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """78KOL74CHEROD""",
    longDesc = 
"""
78KOL74CHEROD
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 6,
    label = "CF4",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {5,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.329574,0.0332696,-3.88267e-05,2.20593e-08,-4.94837e-12,-113504,21.2017], Tmin=(298,'K'), Tmax=(1250,'K')),
            NASAPolynomial(coeffs=[9.80832,0.00328269,-1.34045e-06,2.43738e-10,-1.62862e-14,-116025,-27.0002], Tmin=(1250,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-946.655,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """78KOL74CHEROD""",
    longDesc = 
"""
78KOL74CHEROD
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC(F)(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 7,
    label = "CF3",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u1 p0 c0 {1,S} {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.35729,0.0215758,-2.3902e-05,1.29611e-08,-2.80173e-12,-57391.3,18.6474], Tmin=(298,'K'), Tmax=(1250,'K')),
            NASAPolynomial(coeffs=[7.73167,0.00227115,-8.90496e-07,1.52938e-10,-9.50838e-15,-59145.7,-14.0202], Tmin=(1250,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-479.453,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """82MCMGOL71STU""",
    longDesc = 
"""
82MCMGOL71STU
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[C](F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 8,
    label = "CHF2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u1 p0 c0 {1,S} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.83276,0.0134164,-9.54328e-06,2.9593e-09,-2.792e-13,-30857.1,16.7589], Tmin=(298,'K'), Tmax=(1150,'K')),
            NASAPolynomial(coeffs=[5.44828,0.00441165,-1.74189e-06,3.092e-10,-2.01762e-14,-31961,-2.29455], Tmin=(1150,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-258.032,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """82MCMGOL96ZAC""",
    longDesc = 
"""
82MCMGOL96ZAC
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[CH]F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 9,
    label = "CH2F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.11797,0.0102393,-6.62089e-06,2.37857e-09,-3.89336e-13,-4957.42,13.3394], Tmin=(298,'K'), Tmax=(1300,'K')),
            NASAPolynomial(coeffs=[4.06013,0.00546642,-2.10949e-06,3.74458e-10,-2.474e-14,-5592.77,3.01379], Tmin=(1300,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-42.4604,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """82MCMGOL96ZAC""",
    longDesc = 
"""
82MCMGOL96ZAC
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 10,
    label = "CHF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p1 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.34484,0.00235461,1.93983e-06,-2.65251e-09,7.91169e-13,18514,7.05286], Tmin=(298,'K'), Tmax=(1300,'K')),
            NASAPolynomial(coeffs=[4.48366,0.00174964,-5.0479e-07,1.08953e-10,-9.87898e-15,17958.1,0.289222], Tmin=(1300,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (153.289,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """84PRINIL71STU""",
    longDesc = 
"""
84PRINIL71STU
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 11,
    label = "CF2",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p1 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.28591,0.0107608,-1.05382e-05,4.89881e-09,-8.86384e-13,-23521.2,13.1348], Tmin=(298,'K'), Tmax=(1300,'K')),
            NASAPolynomial(coeffs=[5.33121,0.00197748,-9.60248e-07,2.10704e-10,-1.5954e-14,-24371.4,-2.56367], Tmin=(1300,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-196.899,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """78ROD71STUPRO""",
    longDesc = 
"""
78ROD71STUPRO
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[C]F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 12,
    label = "CF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p1 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.35384,0.000209097,3.20774e-06,-3.66875e-09,1.19863e-12,27907.7,6.33463], Tmin=(298,'K'), Tmax=(1100,'K')),
            NASAPolynomial(coeffs=[3.66497,0.000973681,-4.10982e-07,8.00629e-11,-5.64981e-15,27724.2,4.28163], Tmin=(1100,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (231.934,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """91GURVEY71STU""",
    longDesc = 
"""
91GURVEY71STU
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 13,
    label = "CF3O",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 O u1 p2 c0 {5,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.38724,0.0298955,-3.42745e-05,1.91806e-08,-4.24959e-12,-80336.9,19.7276], Tmin=(298,'K'), Tmax=(1250,'K')),
            NASAPolynomial(coeffs=[9.82041,0.00338916,-1.44654e-06,2.76962e-10,-1.9558e-14,-82586.6,-23.1971], Tmin=(1250,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-669.668,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """82BATWAL96ZAC""",
    longDesc = 
"""
82BATWAL96ZAC
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]C(F)(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 14,
    label = "CH3-CH2F",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.152357,0.0284098,-1.87546e-05,7.32933e-09,-1.50297e-12,-32810.9,23.294], Tmin=(298,'K'), Tmax=(1150,'K')),
            NASAPolynomial(coeffs=[4.95749,0.0163476,-6.80279e-06,1.26802e-09,-8.58109e-14,-34339.5,-2.14873], Tmin=(1150,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-276.178,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """75CHEROD""",
    longDesc = 
"""
75CHEROD
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCF
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 15,
    label = "CH3-CHF2",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.225714,0.0340095,-2.86848e-05,1.39498e-08,-3.0824e-12,-61591.9,23.7067], Tmin=(298,'K'), Tmax=(1150,'K')),
            NASAPolynomial(coeffs=[6.7084,0.0150294,-6.41896e-06,1.23178e-09,-8.61696e-14,-63428.6,-9.73887], Tmin=(1150,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-515.091,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """75CHEROD""",
    longDesc = 
"""
75CHEROD
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 16,
    label = "CH3-CF3",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.214139,0.0444773,-4.85709e-05,2.87261e-08,-7.06581e-12,-91218.9,24.4576], Tmin=(298,'K'), Tmax=(1150,'K')),
            NASAPolynomial(coeffs=[9.56471,0.0120541,-5.11001e-06,9.72843e-10,-6.75072e-14,-93737.6,-24.901], Tmin=(1150,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-761.419,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """75CHEROD""",
    longDesc = 
"""
75CHEROD
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(F)(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 17,
    label = "CH2F-CHF2",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.647376,0.0362925,-3.11432e-05,1.44646e-08,-3.0121e-12,-81526.6,23.2953], Tmin=(298,'K'), Tmax=(1100,'K')),
            NASAPolynomial(coeffs=[9.27265,0.0120402,-4.8606e-06,8.86567e-10,-5.96506e-14,-83983.5,-21.388], Tmin=(1100,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-680.064,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """68LACSKI96ZAC""",
    longDesc = 
"""
68LACSKI96ZAC
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FCC(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 18,
    label = "CH2F-CF3",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {6,S}
3 F u0 p3 c0 {6,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.219524,0.048987,-5.35013e-05,2.97849e-08,-6.73935e-12,-109444,26.8259], Tmin=(298,'K'), Tmax=(1150,'K')),
            NASAPolynomial(coeffs=[11.789,0.0101279,-4.32428e-06,8.25437e-10,-5.76051e-14,-112514,-33.8751], Tmin=(1150,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-912.68,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """75CHEROD""",
    longDesc = 
"""
75CHEROD
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FCC(F)(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 19,
    label = "CHF2-CHF2",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {6,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
6 C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.952865,0.0412528,-4.06818e-05,2.11611e-08,-4.66006e-12,-107383,22.5582], Tmin=(298,'K'), Tmax=(1150,'K')),
            NASAPolynomial(coeffs=[11.5136,0.00988762,-3.99141e-06,7.26044e-10,-4.86781e-14,-110308,-31.717], Tmin=(1150,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-894.413,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """95BURZAC96ZAC""",
    longDesc = 
"""
95BURZAC96ZAC
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC(F)C(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 20,
    label = "CHF2-CF3",
    molecule = 
"""
1 F u0 p3 c0 {6,S}
2 F u0 p3 c0 {6,S}
3 F u0 p3 c0 {7,S}
4 F u0 p3 c0 {7,S}
5 F u0 p3 c0 {7,S}
6 C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
7 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.410676,0.0522724,-6.01225e-05,3.46436e-08,-8.06476e-12,-134841,24.6241], Tmin=(298,'K'), Tmax=(1150,'K')),
            NASAPolynomial(coeffs=[14.0589,0.00799841,-3.482e-06,6.74927e-10,-4.77896e-14,-138347,-44.3854], Tmin=(1150,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-1122.91,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """75CHEROD""",
    longDesc = 
"""
75CHEROD
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC(F)C(F)(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 21,
    label = "CF3-CF3",
    molecule = 
"""
1 F u0 p3 c0 {7,S}
2 F u0 p3 c0 {7,S}
3 F u0 p3 c0 {7,S}
4 F u0 p3 c0 {8,S}
5 F u0 p3 c0 {8,S}
6 F u0 p3 c0 {8,S}
7 C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
8 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.148066,0.0617936,-7.84096e-05,4.83716e-08,-1.18224e-11,-163686,23.7295], Tmin=(298,'K'), Tmax=(1150,'K')),
            NASAPolynomial(coeffs=[17.1501,0.00461143,-1.9269e-06,3.55533e-10,-2.39644e-14,-167951,-61.7238], Tmin=(1150,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-1362.66,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """75CHEROD""",
    longDesc = 
"""
75CHEROD
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC(F)(F)C(F)(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 22,
    label = "CH3-CHF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u1 p0 c0 {1,S} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.40043,0.0170574,-4.32069e-06,-2.67974e-09,1.28658e-12,-10589.5,14.4186], Tmin=(298,'K'), Tmax=(1100,'K')),
            NASAPolynomial(coeffs=[4.40083,0.0144742,-6.24385e-06,1.20968e-09,-8.54199e-14,-11355.6,3.19125], Tmin=(1100,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-89.1038,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """95BURZAC90CHE""",
    longDesc = 
"""
95BURZAC90CHE
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 23,
    label = "CH3-CF2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u1 p0 c0 {1,S} {2,S} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.31422,0.0237018,-1.63892e-05,5.72572e-09,-8.07296e-13,-37994.9,15.3584], Tmin=(298,'K'), Tmax=(1150,'K')),
            NASAPolynomial(coeffs=[6.47721,0.0124876,-5.35782e-06,1.03049e-09,-7.24509e-14,-39202,-6.31953], Tmin=(1150,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-316.759,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """78ROD90CHERAU""",
    longDesc = 
"""
78ROD90CHERAU
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C](F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 24,
    label = "CH2F-CH2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u1 p0 c0 {2,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.40169,0.0223911,-1.38687e-05,4.57314e-09,-7.26492e-13,-6683.25,19.5876], Tmin=(298,'K'), Tmax=(1100,'K')),
            NASAPolynomial(coeffs=[4.53673,0.0143225,-6.19589e-06,1.20562e-09,-8.55302e-14,-7628.35,3.12555], Tmin=(1100,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-57.6949,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """90CHERAU""",
    longDesc = 
"""
90CHERAU
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CF
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 25,
    label = "CH2F-CHF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u1 p0 c0 {2,S} {3,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.28983,0.0255773,-1.99128e-05,7.58804e-09,-1.12378e-12,-30343.3,15.4313], Tmin=(298,'K'), Tmax=(1250,'K')),
            NASAPolynomial(coeffs=[8.72145,0.00868155,-3.54229e-06,6.63135e-10,-4.47423e-14,-32272.9,-18.2518], Tmin=(1250,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-253.074,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """95BURZAC91CHE""",
    longDesc = 
"""
95BURZAC91CHE
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[CH]CF
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 26,
    label = "CH2F-CF2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 C u1 p0 c0 {2,S} {3,S} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.09008,0.0293901,-2.55533e-05,1.17108e-08,-2.31129e-12,-55373.1,17.8136], Tmin=(298,'K'), Tmax=(1150,'K')),
            NASAPolynomial(coeffs=[8.87024,0.0100895,-4.39156e-06,8.57582e-10,-6.11641e-14,-57295.5,-17.249], Tmin=(1150,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-461.245,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """91CHERAU""",
    longDesc = 
"""
91CHERAU
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC[C](F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 27,
    label = "CHF2-CH2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 C u1 p0 c0 {3,S} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.21237,0.0299528,-2.78097e-05,1.45866e-08,-3.35363e-12,-34840,21.1127], Tmin=(298,'K'), Tmax=(1100,'K')),
            NASAPolynomial(coeffs=[6.79826,0.0121309,-5.28714e-06,1.03624e-09,-7.40874e-14,-36291.2,-7.21609], Tmin=(1100,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-291.607,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """90CHERAU""",
    longDesc = 
"""
90CHERAU
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 28,
    label = "CHF2-CHF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 C u1 p0 c0 {3,S} {4,S} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.81368,0.0327767,-3.24205e-05,1.68313e-08,-3.60024e-12,-56094.6,18.5911], Tmin=(298,'K'), Tmax=(1250,'K')),
            NASAPolynomial(coeffs=[9.42456,0.00938455,-4.0695e-06,7.95489e-10,-5.68744e-14,-58166,-20.3132], Tmin=(1250,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-467.484,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """91CHERAU""",
    longDesc = 
"""
91CHERAU
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[CH]C(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 29,
    label = "CHF2-CF2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {6,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
6 C u1 p0 c0 {3,S} {4,S} {5,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.03038,0.0313636,-2.9519e-05,1.39839e-08,-2.71243e-12,-82031.4,14.0888], Tmin=(298,'K'), Tmax=(1250,'K')),
            NASAPolynomial(coeffs=[11.6275,0.00710202,-3.03218e-06,5.8031e-10,-4.05959e-14,-84517.3,-30.4865], Tmin=(1250,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-682.532,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """95BURZAC91CHE""",
    longDesc = 
"""
95BURZAC91CHE
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[C](F)C(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 30,
    label = "CF3-CH2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 C u1 p0 c0 {4,S} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.717008,0.0405315,-4.78641e-05,2.94408e-08,-7.31258e-12,-63850.1,22.1032], Tmin=(298,'K'), Tmax=(1150,'K')),
            NASAPolynomial(coeffs=[9.58796,0.00929988,-4.07747e-06,8.05717e-10,-5.81855e-14,-65995.3,-22.1077], Tmin=(1150,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-532.954,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """78ROD90CHERAU""",
    longDesc = 
"""
78ROD90CHERAU
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(F)(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 31,
    label = "CF3-CHF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u1 p0 c0 {4,S} {5,S} {7,S}
7 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.17776,0.0376992,-4.16073e-05,2.31106e-08,-5.13915e-12,-83881.2,17.2676], Tmin=(298,'K'), Tmax=(1250,'K')),
            NASAPolynomial(coeffs=[11.7531,0.00713118,-3.12251e-06,6.15301e-10,-4.44146e-14,-86403.9,-31.3333], Tmin=(1250,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-697.945,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """95BURZAC91CHE""",
    longDesc = 
"""
95BURZAC91CHE
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[CH]C(F)(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 32,
    label = "CF3-CF2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {6,S}
2 F u0 p3 c0 {6,S}
3 F u0 p3 c0 {6,S}
4 F u0 p3 c0 {7,S}
5 F u0 p3 c0 {7,S}
6 C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
7 C u1 p0 c0 {4,S} {5,S} {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.57479,0.0461494,-5.69635e-05,3.48343e-08,-8.52354e-12,-109277,20.4809], Tmin=(298,'K'), Tmax=(1150,'K')),
            NASAPolynomial(coeffs=[13.9595,0.00491266,-2.10538e-06,3.99134e-10,-2.7649e-14,-112424,-41.9106], Tmin=(1150,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-909.395,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """78ROD91CHERAU""",
    longDesc = 
"""
78ROD91CHERAU
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[C](F)C(F)(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 33,
    label = "C2HF",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,T} {4,S}
3 C u0 p0 c0 {1,S} {2,T}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.18923,0.0212705,-3.16798e-05,2.41573e-08,-7.12746e-12,13736.5,10.2276], Tmin=(298,'K'), Tmax=(1050,'K')),
            NASAPolynomial(coeffs=[5.95051,0.00426834,-1.69498e-06,3.11124e-10,-2.12963e-14,13021.6,-7.57253], Tmin=(1050,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (113.503,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (87.302,'J/mol/K'),
    ),
    shortDesc = """71STUPRO""",
    longDesc = 
"""
71STUPRO
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#CF
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 34,
    label = "C2F2",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {2,S} {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.05931,0.0178762,-2.08076e-05,1.26242e-08,-3.15671e-12,971.086,7.40321], Tmin=(298,'K'), Tmax=(1150,'K')),
            NASAPolynomial(coeffs=[7.80969,0.00274474,-1.11041e-06,1.99095e-10,-1.30596e-14,-303.537,-16.7743], Tmin=(1150,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (7.89999,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (87.302,'J/mol/K'),
    ),
    shortDesc = """71STUPRO""",
    longDesc = 
"""
71STUPRO
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC#CF
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 35,
    label = "CHFCO",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {4,D}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.96237,0.0225075,-2.56389e-05,1.67917e-08,-4.73482e-12,-19104,15.6743], Tmin=(298,'K'), Tmax=(1050,'K')),
            NASAPolynomial(coeffs=[6.77764,0.00623359,-2.55958e-06,4.75314e-10,-3.25951e-14,-20336.9,-8.59113], Tmin=(1050,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-160.19,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """96ZACWES""",
    longDesc = 
"""
96ZACWES
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C=CF
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 36,
    label = "CF2CO",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 O u0 p2 c0 {5,D}
4 C u0 p0 c0 {1,S} {2,S} {5,D}
5 C u0 p0 c0 {3,D} {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40543,0.0226943,-2.80353e-05,1.91247e-08,-5.5122e-12,-36737.3,9.64872], Tmin=(298,'K'), Tmax=(1050,'K')),
            NASAPolynomial(coeffs=[8.86841,0.00426277,-1.73813e-06,3.12287e-10,-2.04266e-14,-38145.6,-17.9075], Tmin=(1050,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-305.506,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """96ZACWES""",
    longDesc = 
"""
96ZACWES
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C=C(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 37,
    label = "CFCO",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {4,D}
3 C u1 p0 c0 {1,S} {4,D}
4 C u0 p0 c0 {2,D} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75942,0.014232,-1.60103e-05,9.88857e-09,-2.66132e-12,6674.73,8.18592], Tmin=(298,'K'), Tmax=(1050,'K')),
            NASAPolynomial(coeffs=[7.30331,0.00297939,-1.30582e-06,2.54074e-10,-1.81035e-14,5735.56,-9.84341], Tmin=(1050,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (55.396,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """96ZACWES""",
    longDesc = 
"""
96ZACWES
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C=[C]F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 38,
    label = "CF3COF",
    molecule = 
"""
1 F u0 p3 c0 {6,S}
2 F u0 p3 c0 {6,S}
3 F u0 p3 c0 {6,S}
4 F u0 p3 c0 {7,S}
5 O u0 p2 c0 {7,D}
6 C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
7 C u0 p0 c0 {4,S} {5,D} {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.76997,0.0424508,-5.06967e-05,3.11138e-08,-7.89598e-12,-126352,20.183], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.0627,0.0121434,-7.26341e-06,2.01144e-09,-2.11896e-13,-128230,-20.7307], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-1049.51,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """hynes""",
    longDesc = 
"""
hynes
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C(F)C(F)(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 39,
    label = "CF3CO",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 O u0 p2 c0 {6,D}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u1 p0 c0 {4,D} {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.05844,0.104164,-0.000237752,2.50068e-07,-9.59472e-11,-74412.7,49.502], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.27366,0.00945656,-5.54495e-06,1.5095e-09,-1.56671e-13,-76812,-18.8993], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-625.524,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (128.874,'J/mol/K'),
    ),
    shortDesc = """NIST""",
    longDesc = 
"""
NIST
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=[C]C(F)(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 40,
    label = "CF3CHO",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 O u0 p2 c0 {6,D}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u0 p0 c0 {4,D} {5,S} {7,S}
7 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.9864,0.028195,-2.0916e-05,5.04802e-09,6.02563e-13,-95123.4,13.7466], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.04771,0.013775,-7.75122e-06,2.0531e-09,-2.09098e-13,-96451.9,-12.1768], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-789.584,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """NIST""",
    longDesc = 
"""
NIST
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=CC(F)(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 41,
    label = "CH2",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76268,0.000968872,2.7949e-06,-3.85091e-09,1.68742e-12,46004,1.56253], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.8741,0.00365639,-1.40895e-06,2.6018e-10,-1.87728e-14,46263.6,6.17119], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (382.229,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """L S/93""",
    longDesc = 
"""
L S/93.
[CH2]
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 42,
    label = "AR",
    molecule = 
"""
1 Ar u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.366], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.366], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-6.19738,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """120186""",
    longDesc = 
"""
120186
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[Ar]
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 43,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29868,0.00140824,-3.96322e-06,5.64152e-09,-2.44485e-12,-1020.9,3.95037], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.92664,0.00148798,-5.68476e-07,1.0097e-10,-6.75335e-15,-922.798,5.98053], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-8.62479,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """121286""",
    longDesc = 
"""
121286
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
N#N
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 44,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.34433,0.00798052,-1.94782e-05,2.01572e-08,-7.37612e-12,-917.935,0.68301], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.33728,-4.94025e-05,4.99457e-07,-1.79566e-10,2.00255e-14,-950.159,-3.20502], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-8.65194,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """TPIS78""",
    longDesc = 
"""
TPIS78.
[H][H]
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 45,
    label = "H",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,7.05333e-13,-1.99592e-15,2.30082e-18,-9.27732e-22,25473.7,-0.446683], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,-2.30843e-11,1.61562e-14,-4.73515e-18,4.98197e-22,25473.7,-0.446683], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (211.8,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """L 7/88""",
    longDesc = 
"""
L 7/88.
[H]
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 46,
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78246,-0.00299673,9.8473e-06,-9.6813e-09,3.24373e-12,-1063.94,3.65768], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.28254,0.00148309,-7.57967e-07,2.09471e-10,-2.16718e-14,-1088.46,5.45323], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-8.63696,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """TPIS89""",
    longDesc = 
"""
TPIS89.
[O][O]
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 47,
    label = "O",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16827,-0.00327932,6.64306e-06,-6.12807e-09,2.11266e-12,29122.3,2.05193], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.56942,-8.59741e-05,4.19485e-08,-1.00178e-11,1.22834e-15,29217.6,4.78434], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (242.976,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """L 1/90""",
    longDesc = 
"""
L 1/90.
[O]
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 48,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.19864,-0.00203643,6.5204e-06,-5.48797e-09,1.77198e-12,-30293.7,-0.849032], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.03399,0.00217692,-1.64073e-07,-9.7042e-11,1.68201e-14,-30004.3,4.96677], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-251.755,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """L 8/89""",
    longDesc = 
"""
L 8/89.
O
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 49,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12531,-0.00322545,6.52765e-06,-5.79854e-09,2.06237e-12,3381.54,-0.690433], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.86473,0.0010565,-2.59083e-07,3.05219e-11,-1.33196e-15,3718.86,5.70164], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (28.6753,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """S 9/01""",
    longDesc = 
"""
S 9/01.
[OH]
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 50,
    label = "H2O2",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.27611,-0.000542822,1.67336e-05,-2.15771e-08,8.62454e-12,-17702.6,3.43505], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.165,0.00490832,-1.90139e-06,3.71186e-10,-2.87908e-14,-17861.8,2.91616], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-146.921,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (78.9875,'J/mol/K'),
    ),
    shortDesc = """L 7/88""",
    longDesc = 
"""
L 7/88.
OO
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 51,
    label = "HO2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.3018,-0.00474912,2.11583e-05,-2.42764e-08,9.29225e-12,294.808,3.71666], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.01721,0.00223982,-6.33658e-07,1.14246e-10,-1.07909e-14,111.857,3.7851], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (2.67719,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """L 5/89""",
    longDesc = 
"""
L 5/89.
[O]O
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 52,
    label = "CO",
    molecule = 
"""
1 O u0 p1 c+1 {2,T}
2 C u0 p1 c-1 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57953,-0.000610354,1.01681e-06,9.07006e-10,-9.04424e-13,-14344.1,3.50841], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.71519,0.00206253,-9.98826e-07,2.30053e-10,-2.03648e-14,-14151.9,7.81869], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-119.169,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """TPIS79""",
    longDesc = 
"""
TPIS79.
[C-]#[O+]
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 53,
    label = "CO2",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.35677,0.0089846,-7.12356e-06,2.45919e-09,-1.437e-13,-48372,9.90105], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.85746,0.00441437,-2.21481e-06,5.2349e-10,-4.72084e-14,-48759.2,2.27164], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-402.81,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (62.3585,'J/mol/K'),
    ),
    shortDesc = """L 7/88""",
    longDesc = 
"""
L 7/88.
O=C=O
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 54,
    label = "CH4",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.14988,-0.013671,4.91801e-05,-4.84743e-08,1.66694e-11,-10246.6,-4.6413], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.0748515,0.0133909,-5.73286e-06,1.22293e-09,-1.01815e-13,-9468.34,18.4373], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-84.4922,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """L 8/88""",
    longDesc = 
"""
L 8/88.
C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 55,
    label = "CH3",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67359,0.00201095,5.73022e-06,-6.87117e-09,2.54386e-12,16445,1.60456], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.28572,0.0072399,-2.98714e-06,5.95685e-10,-4.67154e-14,16775.6,8.48007], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (136.42,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """L11/89""",
    longDesc = 
"""
L11/89.
[CH3]
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 56,
    label = "C",
    molecule = 
"""
1 C u0 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.55424,-0.000321538,7.33792e-07,-7.32235e-10,2.66521e-13,85443.9,4.53131], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.49267,4.79889e-05,-7.24335e-08,3.74291e-11,-4.87278e-15,85451.3,4.8015], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (710.479,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """L11/88""",
    longDesc = 
"""
L11/88.
[C]
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 57,
    label = "CH",
    molecule = 
"""
multiplicity 2
1 C u1 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48982,0.000323836,-1.68899e-06,3.16217e-09,-1.40609e-12,70797.3,2.08401], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.87846,0.000970914,1.44446e-07,-1.30688e-10,1.76079e-14,71012.4,5.48498], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (588.632,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """TPIS79""",
    longDesc = 
"""
TPIS79.
[CH]
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 58,
    label = "CH3OH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.7154,-0.0152309,6.52441e-05,-7.10807e-08,2.61353e-11,-25642.8,-1.5041], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.78971,0.0140938,-6.36501e-06,1.38171e-09,-1.1706e-13,-25374.9,14.5024], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-211.924,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (128.874,'J/mol/K'),
    ),
    shortDesc = """L 8/88""",
    longDesc = 
"""
L 8/88.
CO
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 59,
    label = "C2H6",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.29142,-0.00550154,5.99438e-05,-7.08466e-08,2.68686e-11,-11522.2,2.66682], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.07188,0.0216853,-1.00256e-05,2.21412e-09,-1.90003e-13,-11426.4,15.1156], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-95.6539,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """L 8/88""",
    longDesc = 
"""
L 8/88.
CC
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 60,
    label = "C2H5",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.30647,-0.00418659,4.97143e-05,-5.99127e-08,2.30509e-11,12841.6,4.70721], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.95466,0.0173973,-7.98207e-06,1.75218e-09,-1.49642e-13,12857.5,13.4624], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (106.955,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """L12/92""",
    longDesc = 
"""
L12/92.
C[CH2]
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 61,
    label = "C2H4",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9592,-0.00757052,5.7099e-05,-6.91589e-08,2.69884e-11,5089.78,4.09733], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.03611,0.0146454,-6.71078e-06,1.47223e-09,-1.25706e-13,4939.89,10.3054], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (42.313,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (133.032,'J/mol/K'),
    ),
    shortDesc = """L 1/91""",
    longDesc = 
"""
L 1/91.
C=C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 62,
    label = "C2H",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {3,S}
2 C u1 p0 c0 {1,T}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.88966,0.01341,-2.8477e-05,2.94791e-08,-1.09332e-11,66839.4,6.22296], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.16781,0.00475222,-1.83787e-06,3.0419e-10,-1.77233e-14,67121.1,6.63589], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (555.472,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (62.3585,'J/mol/K'),
    ),
    shortDesc = """L 1/91""",
    longDesc = 
"""
L 1/91.
[C]#C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 63,
    label = "C3H8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.928511,0.0264606,6.03324e-06,-2.1915e-08,9.49615e-12,-14057.9,19.2255], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.52442,0.0188983,-6.2921e-06,9.21615e-10,-4.86845e-14,-16564.4,-17.8384], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-119.487,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = """P11/94""",
    longDesc = 
"""
P11/94
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 64,
    label = "C2H2",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.808681,0.0233616,-3.55172e-05,2.80152e-08,-8.50073e-12,26429,13.9397], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.14757,0.00596167,-2.37295e-06,4.67412e-10,-3.61235e-14,25936,-1.23028], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (217.646,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (87.302,'J/mol/K'),
    ),
    shortDesc = """L 1/91""",
    longDesc = 
"""
L 1/91.
C#C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 65,
    label = "C2H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u1 p0 c0 {1,D} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.21247,0.00151479,2.59209e-05,-3.57658e-08,1.47151e-11,34859.8,8.51054], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.01672,0.0103302,-4.68082e-06,1.01763e-09,-8.62607e-14,34612.9,7.78732], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (289.567,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """L 2/92""",
    longDesc = 
"""
L 2/92.
[CH]=C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 66,
    label = "CH3O",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71181,-0.00280463,3.76551e-05,-4.73072e-08,1.86588e-11,1295.7,6.57241], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.75779,0.00744142,-2.69705e-06,4.38091e-10,-2.63537e-14,378.112,-1.9668], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (10.4739,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """IU1/03""",
    longDesc = 
"""
IU1/03.
C[O]
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 67,
    label = "CH2OH",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.47834,-0.0013507,2.78485e-05,-3.64869e-08,1.47907e-11,-3500.73,3.30913], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.09314,0.00594761,-2.06497e-06,3.23008e-10,-1.88126e-14,-4034.1,-1.84691], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-28.7184,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (103.931,'J/mol/K'),
    ),
    shortDesc = """IU2/03""",
    longDesc = 
"""
IU2/03.
[CH2]O
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 68,
    label = "CH2F-CH2F",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.950246,0.026765,-1.30627e-05,1.95922e-09,5.28057e-14,-53549.5,21.6471], Tmin=(298,'K'), Tmax=(1150,'K')),
            NASAPolynomial(coeffs=[8.46896,0.0115139,-3.69124e-06,4.82192e-10,-2.00572e-14,-56187.1,-19.2187], Tmin=(1150,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-447.656,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """95BURZAC96ZAC""",
    longDesc = 
"""
95BURZAC96ZAC
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FCCF
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 69,
    label = "CH2O",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.79372,-0.00990833,3.7322e-05,-3.79285e-08,1.31773e-11,-14309,0.602813], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.76069,0.0092,-4.42259e-06,1.00641e-09,-8.83856e-14,-13995.8,13.6563], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-118.464,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """L 8/88""",
    longDesc = 
"""
L 8/88.
C=O
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 70,
    label = "HCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.22119,-0.00324393,1.37799e-05,-1.33144e-08,4.33769e-12,3839.56,3.39437], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.77217,0.00495696,-2.48446e-06,5.89162e-10,-5.33509e-14,4011.92,9.79834], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (32.0523,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """L12/89""",
    longDesc = 
"""
L12/89.
[CH]=O
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 71,
    label = "CF3CHCH2",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 C u0 p0 c0 {4,S} {6,D} {7,S}
6 C u0 p0 c0 {5,D} {8,S} {9,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.56835,0.0370716,-1.66535e-05,-1.1567e-08,9.46282e-12,-77857,19.2579], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.2166,0.0111177,-4.07567e-06,6.63455e-10,-3.9873e-14,-80878,-36.334], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-648.629,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (203.705,'J/mol/K'),
    ),
    shortDesc = """*** C3HFx ***""",
    longDesc = 
"""
*** C3HFx ***
CF3CHCH2                H   3C   3F   3    0g    300.00   5000.00 1000.00      1
1.19726859E+01 1.25436030E-02-4.97049536E-06 8.98531469E-10-6.09049619E-14    2
-8.09542161E+04-3.53084262E+01-1.76944260E-01 5.04272890E-02-4.98918705E-05    3
2.45443525E-08-4.55045979E-12-7.77960857E+04 2.64237596E+01                   4.
C=CC(F)(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 72,
    label = "C3H6",
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
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.49331,0.0209252,4.48679e-06,-1.66891e-08,7.15815e-12,1074.83,16.1453], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.73226,0.0149083,-4.9499e-06,7.21202e-10,-3.7662e-14,-923.57,-13.3133], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (6.62319,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (203.705,'J/mol/K'),
    ),
    shortDesc = """120186""",
    longDesc = 
"""
120186
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 73,
    label = "HCCOH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.24237,0.0310722,-5.08669e-05,4.31371e-08,-1.40146e-11,8031.61,13.8743], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.92383,0.00679236,-2.56586e-06,4.49878e-10,-2.99401e-14,7264.63,-7.60177], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (64.6648,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (103.931,'J/mol/K'),
    ),
    shortDesc = """SRI91""",
    longDesc = 
"""
SRI91
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#CO
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 74,
    label = "CH3CCH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,D} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.73292,0.0223946,-5.14906e-06,-6.75965e-09,3.82532e-12,29040.5,16.5689], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.42555,0.0155111,-5.66784e-06,7.92244e-10,-1.6878e-14,27843,-3.35272], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (239.753,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """PD5/98""",
    longDesc = 
"""
PD5/98
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=[C]C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 75,
    label = "HCCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 C u1 p0 c0 {3,D} {4,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.25172,0.017655,-2.37291e-05,1.72758e-08,-5.06648e-12,20059.4,12.4904], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.62821,0.00408534,-1.59345e-06,2.86261e-10,-1.94078e-14,19327.2,-3.93026], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (4000,'K'),
        E0 = (165.461,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """SRIC91""",
    longDesc = 
"""
SRIC91
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=C=O
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 76,
    label = "CH3CO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u1 p0 c0 {1,D} {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.16343,-0.000232616,3.42678e-05,-4.41052e-08,1.72756e-11,-2657.45,7.34683], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.94477,0.00786672,-2.88659e-06,4.72709e-10,-2.85999e-14,-3787.31,-5.01368], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-22.0975,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (128.874,'J/mol/K'),
    ),
    shortDesc = """T 9/92""",
    longDesc = 
"""
T 9/92.
C[C]=O
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 77,
    label = "CH2CO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.13584,0.0181189,-1.73947e-05,9.34398e-09,-2.01458e-12,-7270,12.2156], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.5113,0.0090036,-4.1694e-06,9.23346e-10,-7.94838e-14,-7778.5,0.632247], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-61.7931,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """D05/90""",
    longDesc = 
"""
D05/90.
C=C=O
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 78,
    label = "CH2CHO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 C u1 p0 c0 {3,S} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40906,0.0107386,1.89149e-06,-7.15858e-09,2.86739e-12,62,9.57145], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.97567,0.00813059,-2.74362e-06,4.0703e-10,-2.17602e-14,-969.5,-5.03209], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (0.366545,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (128.874,'J/mol/K'),
    ),
    shortDesc = """D05/83""",
    longDesc = 
"""
D05/83
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C=O
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 79,
    label = "CH3CHO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.72946,-0.00319329,4.75349e-05,-5.74586e-08,2.19311e-11,-21572.9,4.10302], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.40411,0.0117231,-4.22631e-06,6.83725e-10,-4.09849e-14,-22593.1,-3.48079], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-178.765,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """L 8/88""",
    longDesc = 
"""
L 8/88.
CC=O
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 80,
    label = "CF3CCH2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
5 C u0 p0 c0 {6,D} {7,S} {8,S}
6 C u1 p0 c0 {4,S} {5,D}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.34294,0.0437082,-4.41291e-05,1.98066e-08,-2.52758e-12,-47085.9,20.2494], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.586,0.00812318,-2.95983e-06,4.80632e-10,-2.89086e-14,-49927.8,-36.5972], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-392.724,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """CF3CCH2                 H   2C   3F   3    0g    300.00   5000.00 1000.00      1""",
    longDesc = 
"""
CF3CCH2                 H   2C   3F   3    0g    300.00   5000.00 1000.00      1
1.23019497E+01 9.51096222E-03-3.81477953E-06 6.95310445E-10-4.74033015E-14    2
-4.99225413E+04-3.49756046E+01 8.07938725E-01 4.82284101E-02-5.55615570E-05    3
3.31924991E-08-8.04824987E-12-4.70705880E+04 2.27361360E+01                   4.
C=[C]C(F)(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 81,
    label = "CF3CCH",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {4,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 C u0 p0 c0 {4,S} {6,T}
6 C u0 p0 c0 {5,T} {7,S}
7 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.281616,0.052517,-7.44406e-05,5.3525e-08,-1.53176e-11,-53396.6,23.4333], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.0876,0.00673608,-2.69301e-06,4.89992e-10,-3.33727e-14,-56020.5,-34.348], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-446.183,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#CC(F)(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 82,
    label = "CF3COCH3",
    molecule = 
"""
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {6,S}
3  F u0 p3 c0 {6,S}
4  O u0 p2 c0 {7,D}
5  C u0 p0 c0 {7,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
7  C u0 p0 c0 {4,D} {5,S} {6,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.31184,0.0462932,-3.86726e-05,1.4578e-08,-1.48757e-12,-103128,17.5782], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.7707,0.0139114,-5.56646e-06,1.01277e-09,-6.89535e-14,-106312,-41.5671], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-857.388,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """*** C2HOFx ***""",
    longDesc = 
"""
*** C2HOFx ***
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)C(F)(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 83,
    label = "BR2",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 Br u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.34375,0.00634804,-1.36289e-05,1.31573e-08,-4.67761e-12,2531.64,9.07775], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.18756,-0.00138705,9.35013e-07,-2.07121e-10,1.41849e-14,2103.48,0.0761703], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (21.4067,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """J12/61""",
    longDesc = 
"""
J12/61
BR2               J12/61BR  20   00   00   0G   300.00   5000.00  1000.00      1
0.44479495E+01 0.10051208E-03-0.16393816E-07 0.22685621E-11-0.10236774E-15    2
0.23659941E+04 0.40888431E+01 0.38469580E+01 0.26111841E-02-0.40034147E-05    3
0.28120689E-08-0.73256202E-12 0.24846984E+04 0.69696985E+01                   4.
BrBr
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 84,
    label = "CF3BR",
    molecule = 
"""
1 Br u0 p3 c0 {5,S}
2 F  u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.92067,0.0310919,-3.85951e-05,2.31847e-08,-5.4647e-12,-79904.4,17.1123], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.2442,0.00282089,-1.10431e-06,1.88475e-10,-1.17194e-14,-81930.9,-24.5567], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-665.417,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """0""",
    longDesc = 
"""
0
CF3BR                  0C   1F   3BR  1    0G   300.000  4000.000 1000.00      1
0.10835589E+02+0.15757806E-02-0.20505728E-06-0.81578432E-10 0.17003094E-13    2
-0.81927266E+05-0.27720734E+02 0.44576893E+01 0.14666174E-01-0.20081193E-05    3
-0.10235016E-07+0.52610143E-11-0.80003992E+05 0.62208567E+01                   4.
FC(F)(F)Br
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 85,
    label = "H2CC",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p1 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28155,0.00697648,-2.38552e-06,-1.21044e-09,9.81895e-13,48621.8,5.92039], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.27803,0.00475628,-1.6301e-06,2.54628e-10,-1.48864e-14,48316.7,0.640237], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (403.718,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """L12/89""",
    longDesc = 
"""
L12/89.
[C]=C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 86,
    label = "CH2OCH2",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75905,-0.00944122,8.03097e-05,-1.00808e-07,4.00399e-11,-7560.81,7.84975], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.48876,0.0120462,-4.33369e-06,7.00283e-10,-4.19491e-14,-9180.43,-7.07996], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-61.9909,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (157.975,'J/mol/K'),
    ),
    shortDesc = """T 6/92""",
    longDesc = 
"""
T 6/92
_low T polynomial Tmin changed from 298.15 to 298.0 K when importing to RMG.
C1CO1
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 87,
    label = "nC3H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u1 p0 c0 {1,S} {9,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.04912,0.026009,2.35425e-06,-1.95951e-08,9.37202e-12,10312.3,21.136], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.70975,0.0160315,-5.27202e-06,7.58884e-10,-3.88627e-14,7976.22,-15.5153], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (83.3079,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """P11/94""",
    longDesc = 
"""
P11/94
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 88,
    label = "CH2*",
    molecule = 
"""
1 C u0 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.1986,-0.00236661,8.23296e-06,-6.68816e-09,1.94315e-12,50496.8,-0.769119], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.29204,0.00465589,-2.01192e-06,4.17906e-10,-3.39716e-14,50926,8.6265], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (419.976,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """L S/93""",
    longDesc = 
"""
L S/93.
Duplicate of species CH2 (i.e. same molecular structure according to RMG)
[CH2]
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 89,
    label = "C4H612",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {4,D} {9,S} {10,S}
4  C u0 p0 c0 {2,D} {3,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.02347,0.0349592,-2.2009e-05,6.94227e-09,-7.87919e-13,18118,19.7507], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.8156,-0.0042575,1.05118e-05,-4.47384e-09,5.84814e-13,12673.4,-69.8266], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (149.017,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (228.648,'J/mol/K'),
    ),
    shortDesc = """A 8/83""",
    longDesc = 
"""
A 8/83
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C=CC
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 90,
    label = "C5H5OH",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3  C u0 p0 c0 {2,S} {5,D} {8,S}
4  C u0 p0 c0 {2,S} {6,D} {9,S}
5  C u0 p0 c0 {3,D} {6,S} {10,S}
6  C u0 p0 c0 {4,D} {5,S} {11,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.04302,0.0712535,-7.09182e-05,3.86802e-08,-8.78883e-12,-6416.78,48.6171], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.4894,0.0380526,-2.16545e-05,5.92386e-09,-6.27635e-13,-8213.1,7.12481], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-61.3004,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (278.535,'J/mol/K'),
    ),
    shortDesc = """HWZD99""",
    longDesc = 
"""
HWZD99
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
OC1C=CC=C1
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 91,
    label = "C2O",
    molecule = 
"""
multiplicity 3
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 C u2 p0 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.86486,0.0119902,-1.83624e-05,1.57697e-08,-5.38975e-12,33749.9,8.88678], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.15127,0.00237267,-7.6136e-07,1.17064e-10,-7.02578e-15,33241.9,-2.21831], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (280.419,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (62.3585,'J/mol/K'),
    ),
    shortDesc = """RUS 79""",
    longDesc = 
"""
RUS 79.
[C]=C=O
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 92,
    label = "CH3CHCH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u1 p0 c0 {2,D} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.913729,0.0264323,-1.1759e-05,-2.30357e-09,2.77155e-12,30916.9,19.9893], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.37253,0.0157805,-5.99229e-06,9.30897e-10,-3.6551e-14,29614.8,-3.41865], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (254.446,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """PD5/98""",
    longDesc = 
"""
PD5/98
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=CC
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 93,
    label = "C2H3CHOCH2",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3  C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {10,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.797985,0.0344034,-1.24599e-05,-5.18063e-18,1.9936e-21,-648.928,21.8897], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[-4.72093,0.0391414,-6.52873e-06,-7.68209e-09,2.51473e-12,1753.52,51.719], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-5.01318,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (253.591,'J/mol/K'),
    ),
    shortDesc = """A 8/83""",
    longDesc = 
"""
A 8/83
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC1CO1
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 94,
    label = "C4H10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
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
            NASAPolynomial(coeffs=[1.56854,0.0346523,6.81681e-06,-2.79951e-08,1.23077e-11,-17130,17.908], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.5268,0.0235907,-7.85225e-06,1.14484e-09,-5.98277e-14,-20479.2,-32.1986], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-143.36,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (320.107,'J/mol/K'),
    ),
    shortDesc = """P11/94""",
    longDesc = 
"""
P11/94
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCCC
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 95,
    label = "CH3CHOCH2",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
4  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.487338,0.0285197,3.00962e-06,-2.26526e-08,1.07067e-11,-12556.4,22.6053], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.69006,0.016021,-5.39718e-06,7.99415e-10,-4.26564e-14,-15420.7,-22.485], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-107.566,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (228.648,'J/mol/K'),
    ),
    shortDesc = """T 6/92""",
    longDesc = 
"""
T 6/92
_low T polynomial Tmin changed from 298.15 to 298.0 K when importing to RMG.
CC1CO1
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 96,
    label = "C4H81",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.18114,0.0308534,5.08652e-06,-2.46549e-08,1.11102e-11,-1790.4,21.0625], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.05358,0.0343505,-1.58832e-05,3.30897e-09,-2.5361e-13,-2139.72,15.5432], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-16.5093,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (274.378,'J/mol/K'),
    ),
    shortDesc = """T 6/83""",
    longDesc = 
"""
T 6/83
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CCC
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 97,
    label = "pC3H4",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.68039,0.0157997,2.50706e-06,-1.36576e-08,6.61543e-12,20802.4,9.87694], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.02524,0.0113365,-4.02234e-06,6.43761e-10,-3.82996e-14,19620.9,-8.60438], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (172.101,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """T 2/90""",
    longDesc = 
"""
T 2/90.
C#CC
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 98,
    label = "CH3CH2CHO",
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
            NASAPolynomial(coeffs=[2.72557,0.023236,2.97407e-06,-1.66134e-08,7.42501e-12,-24556.7,14.1663], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.26374,0.0199763,-7.61951e-06,1.16871e-09,-4.196e-14,-25886,-5.77865], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-202.792,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """USC/07""",
    longDesc = 
"""
USC/07
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC=O
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 99,
    label = "l-C6H4",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  C u0 p0 c0 {1,D} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,T}
4  C u0 p0 c0 {3,T} {5,S}
5  C u0 p0 c0 {4,S} {6,T}
6  C u0 p0 c0 {5,T} {10,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.295902,0.0580533,-6.77668e-05,4.33768e-08,-1.14189e-11,60001.4,22.319], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.7152,0.0138397,-4.37654e-06,3.15416e-10,4.6619e-14,57031.1,-39.4646], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (497.029,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """H6W/94""",
    longDesc = 
"""
H6W/94
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#CC#CC=C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

# entry(
#     index = 100,
#     label = "C3H3",
#     molecule = 
# """
# multiplicity 2
# 1 C u0 p0 c0 {2,D} {4,S} {5,S}
# 2 C u0 p0 c0 {1,D} {3,D}
# 3 C u1 p0 c0 {2,D} {6,S}
# 4 H u0 p0 c0 {1,S}
# 5 H u0 p0 c0 {1,S}
# 6 H u0 p0 c0 {3,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[1.35111,0.0327411,-4.73827e-05,3.7631e-08,-1.18541e-11,40105.8,15.2059], Tmin=(200,'K'), Tmax=(1000,'K')),
#             NASAPolynomial(coeffs=[7.14222,0.00761902,-2.6746e-06,4.24915e-10,-2.51475e-14,38908.7,-12.5848], Tmin=(1000,'K'), Tmax=(6000,'K')),
#         ],
#         Tmin = (200,'K'),
#         Tmax = (6000,'K'),
#         E0 = (331.804,'kJ/mol'),
#         Cp0 = (33.2579,'J/mol/K'),
#         CpInf = (133.032,'J/mol/K'),
#     ),
#     shortDesc = """T 5/97""",
#     longDesc = 
# """
# T 5/97.
# [CH]=C=C
# _imported from 2-BTP/2-BTP_thermo.txt.
# """,
# )

entry(
    index = 101,
    label = "aC3H4",
    molecule = 
"""
1 C u0 p0 c0 {3,D} {4,S} {5,S}
2 C u0 p0 c0 {3,D} {6,S} {7,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.61304,0.0121226,1.85399e-05,-3.45251e-08,1.53351e-11,21541.6,10.2261], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.31687,0.0111337,-3.96294e-06,6.35642e-10,-3.78755e-14,20117.5,-10.9958], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (177.988,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (157.975,'J/mol/K'),
    ),
    shortDesc = """L 8/89""",
    longDesc = 
"""
L 8/89.
C=C=C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 102,
    label = "aC3H5",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u1 p0 c0 {1,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.36318,0.0198138,1.24971e-05,-3.33556e-08,1.58466e-11,19245.6,17.1732], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.50079,0.0143247,-5.67816e-06,1.10808e-09,-9.03639e-14,17482.4,-11.2431], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (157.43,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """PD5/98""",
    longDesc = 
"""
PD5/98
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C=C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 103,
    label = "CH3CHCHCO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  C u1 p0 c0 {1,D} {4,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.30535,0.0157494,2.16239e-05,-3.66078e-08,1.49325e-11,5758.86,4.20435], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.76082,0.0200318,-8.0631e-06,1.33614e-09,-6.23084e-14,4570.83,-11.0956], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (52.9702,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """USC/07""",
    longDesc = 
"""
USC/07
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=C[C]=O
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 104,
    label = "pC4H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {2,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.2087,0.0382975,-7.26605e-06,-1.54285e-08,8.68594e-12,7322.1,22.1693], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.68224,0.0236911,-7.59489e-06,6.64271e-10,5.48451e-14,4964.41,-17.8917], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (62.3494,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (295.164,'J/mol/K'),
    ),
    shortDesc = """USC/07""",
    longDesc = 
"""
USC/07
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CCC
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 105,
    label = "C4H82",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.25943,0.0278084,8.70139e-06,-2.44022e-08,9.89777e-12,-2964.77,20.5011], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.827977,0.0358645,-1.66345e-05,3.47328e-09,-2.66574e-13,-3052.1,21.3425], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-26.411,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (274.378,'J/mol/K'),
    ),
    shortDesc = """T 6/83""",
    longDesc = 
"""
T 6/83
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC=CC
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 106,
    label = "cC3H4",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {1,S} {2,D} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.024621,0.0231972,-1.84744e-06,-1.59276e-08,8.68462e-12,32334.1,22.7298], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.69999,0.0103574,-3.45512e-06,5.06529e-10,-2.66823e-14,30199.1,-13.3788], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (266.448,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (157.975,'J/mol/K'),
    ),
    shortDesc = """T12/81""",
    longDesc = 
"""
T12/81
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C1=CC1
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 107,
    label = "CH2OCH",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u1 p0 c0 {1,S} {2,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.383961,0.023879,-1.24676e-05,-1.76864e-09,2.81424e-12,18836.2,25.7417], Tmin=(298,'K'), Tmax=(500,'K')),
            NASAPolynomial(coeffs=[4.49941,0.0115526,-4.81441e-06,8.92349e-10,-5.68706e-14,17474,0.339255], Tmin=(500,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (156.396,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (133.032,'J/mol/K'),
    ),
    shortDesc = """A12/04""",
    longDesc = 
"""
A12/04
_low T polynomial Tmin changed from 298.15 to 298.0 K when importing to RMG.
[CH]1CO1
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 108,
    label = "CH2CHCHCHO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,D} {4,S} {6,S}
3  C u0 p0 c0 {2,D} {5,S} {7,S}
4  C u1 p0 c0 {2,S} {8,S} {9,S}
5  C u0 p0 c0 {1,D} {3,S} {10,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.21087,0.0352059,-1.09391e-05,-1.17206e-08,7.61749e-12,2266.57,20.6135], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.30106,0.0199453,-8.29038e-06,1.51008e-09,-9.15812e-14,157.884,-16.9106], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (18.425,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """USC/07""",
    longDesc = 
"""
USC/07
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C=CC=O
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 109,
    label = "C4H4",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {3,T} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.58857,0.0365467,-3.4107e-05,1.66526e-08,-3.00646e-12,33359.5,20.6579], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.25396,0.0139141,-5.29322e-06,8.34805e-10,-3.51979e-14,31766,-12.6295], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (276.349,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """USC/07""",
    longDesc = 
"""
USC/07
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#CC=C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 110,
    label = "iC3H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.44492,0.0209991,7.70362e-06,-1.84763e-08,7.1283e-12,9422.37,20.1163], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.51927,0.0172201,-5.73642e-06,8.41307e-10,-4.45659e-14,7322.72,-9.08302], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (76.8535,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """P11/94""",
    longDesc = 
"""
P11/94
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 111,
    label = "C4H6O25",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {2,S} {4,D} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.67053,0.00492586,8.86967e-05,-1.26219e-07,5.23991e-11,-14657.2,14.5722], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.60658,0.020831,-8.42229e-06,1.56718e-09,-1.09391e-13,-17617.7,-23.2465], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
        E0 = (-122.374,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (257.749,'J/mol/K'),
    ),
    shortDesc = """T 3/97""",
    longDesc = 
"""
T 3/97.
C1=CCOC1
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 112,
    label = "C4H6O23",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {5,S}
2  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {5,D} {10,S}
5  C u0 p0 c0 {1,S} {4,D} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.67053,0.00492586,8.86967e-05,-1.26219e-07,5.23991e-11,-10278.8,14.5722], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.60658,0.020831,-8.42229e-06,1.56718e-09,-1.09391e-13,-13239.3,-23.2465], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (5000,'K'),
        E0 = (-85.9693,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (257.749,'J/mol/K'),
    ),
    shortDesc = """T 3/97""",
    longDesc = 
"""
T 3/97.
C1=COCC1
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 113,
    label = "C6H4O2",
    molecule = 
"""
1  O u0 p2 c0 {3,D}
2  O u0 p2 c0 {6,D}
3  C u0 p0 c0 {1,D} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  C u0 p0 c0 {2,D} {5,S} {7,S}
7  C u0 p0 c0 {6,S} {8,D} {11,S}
8  C u0 p0 c0 {3,S} {7,D} {12,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.95193,0.0578424,-3.82144e-05,4.63127e-09,3.62967e-12,-17611,29.2395], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.7308,0.023615,-1.02346e-05,1.95322e-09,-1.2746e-13,-21085.8,-36.3005], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-148.245,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (282.692,'J/mol/K'),
    ),
    shortDesc = """PUML96""",
    longDesc = 
"""
PUML96
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C1C=CC(=O)C=C1
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 114,
    label = "C6H2",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 C u0 p0 c0 {1,S} {5,T}
4 C u0 p0 c0 {2,S} {6,T}
5 C u0 p0 c0 {3,T} {7,S}
6 C u0 p0 c0 {4,T} {8,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.451,0.0674752,-0.000118099,1.03676e-07,-3.4851e-11,82173.1,17.7041], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.8939,0.00791451,-2.40272e-06,2.43401e-10,3.13832e-15,79832.4,-40.772], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (682.006,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """D11/99""",
    longDesc = 
"""
D11/99
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#CC#CC#C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 115,
    label = "c-C4H5",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {4,S} {7,S}
3 C u0 p0 c0 {1,S} {4,D} {8,S}
4 C u0 p0 c0 {2,S} {3,D} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.63976,0.0415492,-2.1921e-05,-4.6559e-09,6.13489e-12,35373.8,35.7018], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.74672,0.017283,-6.51686e-06,9.89176e-10,-3.46049e-14,32808.4,-12.9129], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (291.241,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (207.862,'J/mol/K'),
    ),
    shortDesc = """PUPM3""",
    longDesc = 
"""
PUPM3
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]1C=CC1
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 116,
    label = "H2C4O",
    molecule = 
"""
1 O u0 p2 c0 {5,D}
2 C u0 p0 c0 {3,D} {6,S} {7,S}
3 C u0 p0 c0 {2,D} {4,D}
4 C u0 p0 c0 {3,D} {5,D}
5 C u0 p0 c0 {1,D} {4,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.18119,0.0298408,-3.28324e-05,2.06318e-08,-5.42006e-12,24125.6,9.42101], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.42922,0.0105027,-4.20668e-06,7.11849e-10,-3.57966e-14,22907.8,-16.512], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (202.985,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (157.975,'J/mol/K'),
    ),
    shortDesc = """USC/07""",
    longDesc = 
"""
USC/07
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C=C=C=O
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 117,
    label = "C5H4O",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {6,S}
3  C u0 p0 c0 {2,S} {4,D} {7,S}
4  C u0 p0 c0 {3,D} {5,S} {8,S}
5  C u0 p0 c0 {4,S} {6,D} {9,S}
6  C u0 p0 c0 {2,S} {5,D} {10,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.264576,0.0334874,1.67738e-06,-2.96207e-08,1.54431e-11,5111.59,23.541], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.0807,0.0161143,-5.83315e-06,9.46759e-10,-5.68972e-14,1943.65,-29.4522], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (40.5036,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (232.805,'J/mol/K'),
    ),
    shortDesc = """T 8/99""",
    longDesc = 
"""
T 8/99.
O=C1C=CC=C1
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 118,
    label = "C4H6-2",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,T}
4  C u0 p0 c0 {2,S} {3,T}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.13733,0.0264862,-9.05687e-06,-5.53864e-19,2.12819e-22,15710.9,13.5294], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.03381,0.00821245,7.1754e-06,-5.88343e-09,1.03439e-12,14335.1,-20.9858], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (129.221,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """A 8/83""",
    longDesc = 
"""
A 8/83
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC#CC
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

# entry(
#     index = 119,
#     label = "C5H6",
#     molecule = 
# """
# 1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
# 2  C u0 p0 c0 {1,S} {4,D} {8,S}
# 3  C u0 p0 c0 {1,S} {5,D} {9,S}
# 4  C u0 p0 c0 {2,D} {5,S} {10,S}
# 5  C u0 p0 c0 {3,D} {4,S} {11,S}
# 6  H u0 p0 c0 {1,S}
# 7  H u0 p0 c0 {1,S}
# 8  H u0 p0 c0 {2,S}
# 9  H u0 p0 c0 {3,S}
# 10 H u0 p0 c0 {4,S}
# 11 H u0 p0 c0 {5,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[0.86109,0.014804,7.21089e-05,-1.13381e-07,4.869e-11,14801.8,21.3535], Tmin=(200,'K'), Tmax=(1000,'K')),
#             NASAPolynomial(coeffs=[9.97578,0.0189055,-6.84115e-06,1.10993e-09,-6.66802e-14,11081.7,-32.2095], Tmin=(1000,'K'), Tmax=(6000,'K')),
#         ],
#         Tmin = (200,'K'),
#         Tmax = (6000,'K'),
#         E0 = (121.584,'kJ/mol'),
#         Cp0 = (33.2579,'J/mol/K'),
#         CpInf = (257.749,'J/mol/K'),
#     ),
#     shortDesc = """T 1/90""",
#     longDesc = 
# """
# T 1/90.
# C1=CCC=C1
# _imported from 2-BTP/2-BTP_thermo.txt.
# """,
# )

entry(
    index = 120,
    label = "C5H5O(2,4)",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3  C u0 p0 c0 {2,S} {5,D} {8,S}
4  C u0 p0 c0 {2,S} {6,D} {9,S}
5  C u0 p0 c0 {3,D} {6,S} {10,S}
6  C u0 p0 c0 {4,D} {5,S} {11,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.07776,0.0525817,-2.88565e-05,-3.38855e-09,6.33614e-12,25510.5,39.5915], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.54053,0.0229895,-9.54376e-06,1.70616e-09,-9.74594e-14,22263.7,-20.8188], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (205.432,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (257.749,'J/mol/K'),
    ),
    shortDesc = """D 9/97""",
    longDesc = 
"""
D 9/97
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]C1C=CC=C1
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 121,
    label = "CH2CHCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {2,D} {6,S} {7,S}
4 C u1 p0 c0 {1,D} {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.21169,0.0118422,1.67463e-05,-3.06947e-08,1.33049e-11,7128.16,10.0882], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.95842,0.0107193,-3.85218e-06,6.22009e-10,-3.72402e-14,5648.26,-11.4746], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (59.0593,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """T05/99""",
    longDesc = 
"""
T05/99.
C=C[C]=O
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 122,
    label = "CH3COCH3",
    molecule = 
"""
1  O u0 p2 c0 {4,D}
2  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,D} {2,S} {3,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.55579,-0.00283654,7.05689e-05,-8.78105e-08,3.40283e-11,-28113.3,2.32266], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.2976,0.0175662,-6.31705e-06,1.02031e-09,-6.1094e-14,-29817.7,-12.757], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-232.314,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """T 5/92""",
    longDesc = 
"""
T 5/92.
CC(C)=O
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

# entry(
#     index = 123,
#     label = "o-C6H4",
#     molecule = 
# """
# 1  C u0 p0 c0 {2,S} {3,D} {7,S}
# 2  C u0 p0 c0 {1,S} {4,D} {8,S}
# 3  C u0 p0 c0 {1,D} {6,S} {9,S}
# 4  C u0 p0 c0 {2,D} {5,S} {10,S}
# 5  C u0 p0 c0 {4,S} {6,T}
# 6  C u0 p0 c0 {3,S} {5,T}
# 7  H u0 p0 c0 {1,S}
# 8  H u0 p0 c0 {2,S}
# 9  H u0 p0 c0 {3,S}
# 10 H u0 p0 c0 {4,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[-3.84542,0.0583916,-4.86448e-05,1.67703e-08,-7.85807e-13,52592.5,40.5871], Tmin=(298,'K'), Tmax=(1000,'K')),
#             NASAPolynomial(coeffs=[8.8433,0.0203015,-8.86743e-06,1.72643e-09,-1.1786e-13,49317.1,-24.0143], Tmin=(1000,'K'), Tmax=(3000,'K')),
#         ],
#         Tmin = (298,'K'),
#         Tmax = (3000,'K'),
#         E0 = (429.966,'kJ/mol'),
#         Cp0 = (33.2579,'J/mol/K'),
#         CpInf = (232.805,'J/mol/K'),
#     ),
#     shortDesc = """D11/99""",
#     longDesc = 
# """
# D11/99
# _low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
# C1#CC=CC=C1
# _imported from 2-BTP/2-BTP_thermo.txt.
# """,
# )

entry(
    index = 124,
    label = "C2H3CHO",
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
            NASAPolynomial(coeffs=[1.27135,0.0262311,-9.29123e-06,-4.78373e-09,3.34805e-12,-9335.73,19.4981], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.81119,0.0171143,-7.48342e-06,1.42522e-09,-9.17468e-14,-10784.1,-4.8588], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-79.0574,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """USC/07""",
    longDesc = 
"""
USC/07
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC=O
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 125,
    label = "iC4H10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
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
            NASAPolynomial(coeffs=[0.541095,0.0378603,5.54598e-06,-3.05001e-08,1.40334e-11,-17977.6,21.1509], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.8462,0.0233384,-7.7834e-06,1.13938e-09,-5.99183e-14,-21669.9,-35.8706], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-151.72,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (320.107,'J/mol/K'),
    ),
    shortDesc = """P11/94""",
    longDesc = 
"""
P11/94
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(C)C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 126,
    label = "iC4H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72215,0.0259575,-2.63563e-05,1.55089e-08,-3.80406e-12,58837.1,7.56372], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.65385,0.0112041,-4.64013e-06,8.67866e-10,-5.74306e-14,57954.4,-11.7565], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (491.25,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """USC/07""",
    longDesc = 
"""
USC/07
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#C[C]=C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 127,
    label = "iC4H5",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u0 p0 c0 {4,D} {8,S} {9,S}
4 C u1 p0 c0 {1,S} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.113081,0.0409506,-3.54136e-05,1.5531e-08,-2.33551e-12,36383.4,23.6925], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.9646,0.0182743,-7.81337e-06,1.52922e-09,-1.09205e-13,34725.1,-10.6493], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (300.246,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (203.705,'J/mol/K'),
    ),
    shortDesc = """USC/07""",
    longDesc = 
"""
USC/07
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=[C]C=C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 128,
    label = "iC4H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u1 p0 c0 {2,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.03759,0.0455667,-3.04762e-05,7.11026e-09,9.96857e-13,14896.5,29.8637], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.14859,0.0221897,-8.44002e-06,1.31334e-09,-5.16179e-14,12712.3,-12.1312], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (121.296,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = """USC/07""",
    longDesc = 
"""
USC/07
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(=C)C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 129,
    label = "iC4H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u1 p0 c0 {1,S} {12,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.975279,0.0416138,-1.44673e-05,-9.38524e-09,6.87974e-12,6668.83,21.2776], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.49817,0.0246895,-8.64876e-06,1.07793e-09,-6.43406e-16,4428.82,-18.4414], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (56.6378,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (295.164,'J/mol/K'),
    ),
    shortDesc = """USC/07""",
    longDesc = 
"""
USC/07
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(C)C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 130,
    label = "iC4H8",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.64714,0.025903,8.19854e-06,-2.21933e-08,8.89586e-12,-4037.31,12.6764], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.46095,0.0296115,-1.30771e-05,2.65719e-09,-2.01347e-13,-5006.68,1.06715], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-33.4322,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (274.378,'J/mol/K'),
    ),
    shortDesc = """T 6/83""",
    longDesc = 
"""
T 6/83
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C(C)C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

# entry(
#     index = 131,
#     label = "C6H5O",
#     molecule = 
# """
# multiplicity 2
# 1  O u0 p2 c0 {3,D}
# 2  C u1 p0 c0 {3,S} {4,S} {8,S}
# 3  C u0 p0 c0 {1,D} {2,S} {7,S}
# 4  C u0 p0 c0 {2,S} {5,D} {9,S}
# 5  C u0 p0 c0 {4,D} {6,S} {10,S}
# 6  C u0 p0 c0 {5,S} {7,D} {11,S}
# 7  C u0 p0 c0 {3,S} {6,D} {12,S}
# 8  H u0 p0 c0 {2,S}
# 9  H u0 p0 c0 {4,S}
# 10 H u0 p0 c0 {5,S}
# 11 H u0 p0 c0 {6,S}
# 12 H u0 p0 c0 {7,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[-0.466204,0.0413444,1.32413e-05,-5.72873e-08,2.89764e-11,4778.58,27.699], Tmin=(200,'K'), Tmax=(1000,'K')),
#             NASAPolynomial(coeffs=[13.7222,0.0174689,-6.35505e-06,1.03492e-09,-6.23411e-14,287.275,-48.8182], Tmin=(1000,'K'), Tmax=(6000,'K')),
#         ],
#         Tmin = (200,'K'),
#         Tmax = (6000,'K'),
#         E0 = (35.8454,'kJ/mol'),
#         Cp0 = (33.2579,'J/mol/K'),
#         CpInf = (282.692,'J/mol/K'),
#     ),
#     shortDesc = """T05/02""",
#     longDesc = 
# """
# T05/02.
# O=C1[CH]C=CC=C1
# _imported from 2-BTP/2-BTP_thermo.txt.
# """,
# )

entry(
    index = 132,
    label = "C5H5O(1,3)",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,D}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C u1 p0 c0 {2,S} {6,S} {9,S}
4  C u0 p0 c0 {1,D} {2,S} {5,S}
5  C u0 p0 c0 {4,S} {6,D} {10,S}
6  C u0 p0 c0 {3,S} {5,D} {11,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.9567,0.0558519,-3.72416e-05,4.16244e-09,3.9272e-12,4857.32,38.6767], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.24314,0.0222013,-9.31059e-06,1.71552e-09,-1.0614e-13,1590.84,-24.0877], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (34.1797,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (257.749,'J/mol/K'),
    ),
    shortDesc = """DU0997""",
    longDesc = 
"""
DU0997
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C1C=C[CH]C1
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

# entry(
#     index = 133,
#     label = "C6H5CH2",
#     molecule = 
# """
# multiplicity 2
# 1  C u0 p0 c0 {2,S} {3,S} {7,D}
# 2  C u1 p0 c0 {1,S} {4,S} {8,S}
# 3  C u0 p0 c0 {1,S} {6,D} {12,S}
# 4  C u0 p0 c0 {2,S} {5,D} {9,S}
# 5  C u0 p0 c0 {4,D} {6,S} {10,S}
# 6  C u0 p0 c0 {3,D} {5,S} {11,S}
# 7  C u0 p0 c0 {1,D} {13,S} {14,S}
# 8  H u0 p0 c0 {2,S}
# 9  H u0 p0 c0 {4,S}
# 10 H u0 p0 c0 {5,S}
# 11 H u0 p0 c0 {6,S}
# 12 H u0 p0 c0 {3,S}
# 13 H u0 p0 c0 {7,S}
# 14 H u0 p0 c0 {7,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[0.481115,0.0385128,3.28615e-05,-7.69727e-08,3.54231e-11,23307,23.5488], Tmin=(200,'K'), Tmax=(1000,'K')),
#             NASAPolynomial(coeffs=[14.044,0.0234939,-8.53754e-06,1.38908e-09,-8.36144e-14,18564.2,-51.6656], Tmin=(1000,'K'), Tmax=(6000,'K')),
#         ],
#         Tmin = (200,'K'),
#         Tmax = (6000,'K'),
#         E0 = (192.532,'kJ/mol'),
#         Cp0 = (33.2579,'J/mol/K'),
#         CpInf = (328.422,'J/mol/K'),
#     ),
#     shortDesc = """T08/90""",
#     longDesc = 
# """
# T08/90.
# C=C1[CH]C=CC=C1
# _imported from 2-BTP/2-BTP_thermo.txt.
# """,
# )

entry(
    index = 134,
    label = "lC5H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  C u0 p0 c0 {1,D} {4,S} {6,S}
3  C u0 p0 c0 {1,S} {5,D} {8,S}
4  C u1 p0 c0 {2,S} {9,S} {10,S}
5  C u0 p0 c0 {3,D} {11,S} {12,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.09743,0.061832,-4.87708e-05,1.66964e-08,-7.53349e-13,23683.6,45.1481], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.22465,0.0396013,-2.23456e-05,6.06497e-09,-6.384e-13,22303.4,14.01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (189.582,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (274.378,'J/mol/K'),
    ),
    shortDesc = """HWZD99""",
    longDesc = 
"""
HWZD99
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C=CC=C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 135,
    label = "sC4H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {1,S} {3,S} {13,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.694284,0.0331133,6.29426e-06,-2.70253e-08,1.19893e-11,6417.57,26.2798], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.42638,0.021919,-7.28684e-06,1.06303e-09,-5.56495e-14,3196.59,-22.4061], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (50.9901,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (295.164,'J/mol/K'),
    ),
    shortDesc = """P11/94""",
    longDesc = 
"""
P11/94
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]CC
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 136,
    label = "tC4H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.961676,0.0257359,1.5609e-05,-2.66565e-08,8.9418e-12,4656.44,24.8054], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.66073,0.0238794,-8.08904e-06,1.20575e-09,-6.50098e-14,1620.76,-14.8003], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (36.9506,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (295.164,'J/mol/K'),
    ),
    shortDesc = """P11/94""",
    longDesc = 
"""
P11/94
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C](C)C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 137,
    label = "C4H5-2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2 C u1 p0 c0 {4,S} {8,S} {9,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {2,S} {3,T}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.96963,0.0244422,-9.12514e-06,-4.24669e-18,1.63047e-21,35503.3,12.0361], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.5382,-0.00856771,2.35595e-05,-1.36764e-08,2.44369e-12,33259.1,-45.3695], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (297.026,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (199.547,'J/mol/K'),
    ),
    shortDesc = """H6W/94""",
    longDesc = 
"""
H6W/94
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C#CC
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 138,
    label = "C6H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,D} {7,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {5,S}
4 C u1 p0 c0 {1,D} {8,S}
5 C u0 p0 c0 {3,S} {6,T}
6 C u0 p0 c0 {5,T} {9,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.17906,0.0555474,-7.30762e-05,5.20767e-08,-1.5047e-11,85647.3,19.1792], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.81883,0.0279334,-1.78254e-05,5.37025e-09,-6.17076e-13,85188.2,-0.921478], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (711.143,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (199.547,'J/mol/K'),
    ),
    shortDesc = """H6W/94""",
    longDesc = 
"""
H6W/94
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=CC#CC#C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

# entry(
#     index = 139,
#     label = "OC6H4CH3",
#     molecule = 
# """
# multiplicity 2
# 1  O u0 p2 c0 {8,D}
# 2  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
# 3  C u0 p0 c0 {2,S} {4,S} {5,D}
# 4  C u1 p0 c0 {3,S} {8,S} {15,S}
# 5  C u0 p0 c0 {3,D} {6,S} {12,S}
# 6  C u0 p0 c0 {5,S} {7,D} {13,S}
# 7  C u0 p0 c0 {6,D} {8,S} {14,S}
# 8  C u0 p0 c0 {1,D} {4,S} {7,S}
# 9  H u0 p0 c0 {2,S}
# 10 H u0 p0 c0 {2,S}
# 11 H u0 p0 c0 {2,S}
# 12 H u0 p0 c0 {5,S}
# 13 H u0 p0 c0 {6,S}
# 14 H u0 p0 c0 {7,S}
# 15 H u0 p0 c0 {4,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[-0.288558,0.0480035,1.8033e-05,-6.17415e-08,2.88526e-11,-689.456,26.7201], Tmin=(298,'K'), Tmax=(1000,'K')),
#             NASAPolynomial(coeffs=[22.6094,0.00756462,6.59609e-06,-4.71509e-09,8.04091e-13,-8202.52,-97.2925], Tmin=(1000,'K'), Tmax=(2500,'K')),
#         ],
#         Tmin = (298,'K'),
#         Tmax = (2500,'K'),
#         E0 = (-8.54523,'kJ/mol'),
#         Cp0 = (33.2579,'J/mol/K'),
#         CpInf = (353.365,'J/mol/K'),
#     ),
#     shortDesc = """EST/BUR P 1/93""",
#     longDesc = 
# """
# EST/BUR P 1/93
# _low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
# CC1=CC=CC(=O)[CH]1
# _imported from 2-BTP/2-BTP_thermo.txt.
# """,
# )

entry(
    index = 140,
    label = "nC4H3",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,T}
3 C u1 p0 c0 {1,D} {6,S}
4 C u0 p0 c0 {2,T} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.816677,0.0387162,-4.80457e-05,3.20668e-08,-8.56282e-12,64455.8,19.7405], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.80457,0.0107124,-4.19391e-06,7.04463e-10,-3.62713e-14,62987.8,-14.1297], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (535.184,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = """USC/07""",
    longDesc = 
"""
USC/07
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=CC#C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 141,
    label = "nC4H5",
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
            NASAPolynomial(coeffs=[0.226113,0.0367424,-2.21205e-05,1.43901e-09,2.64358e-12,42428.4,24.0664], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.40873,0.0177527,-7.56015e-06,1.42038e-09,-9.11002e-14,40438.8,-13.15], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (350.683,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (203.705,'J/mol/K'),
    ),
    shortDesc = """USC/07""",
    longDesc = 
"""
USC/07
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=CC=C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

# entry(
#     index = 142,
#     label = "C5H5",
#     molecule = 
# """
# multiplicity 2
# 1  C u1 p0 c0 {2,S} {5,S} {6,S}
# 2  C u0 p0 c0 {1,S} {3,D} {7,S}
# 3  C u0 p0 c0 {2,D} {4,S} {8,S}
# 4  C u0 p0 c0 {3,S} {5,D} {9,S}
# 5  C u0 p0 c0 {1,S} {4,D} {10,S}
# 6  H u0 p0 c0 {1,S}
# 7  H u0 p0 c0 {2,S}
# 8  H u0 p0 c0 {3,S}
# 9  H u0 p0 c0 {4,S}
# 10 H u0 p0 c0 {5,S}
# """,
#     thermo = NASA(
#         polynomials = [
#             NASAPolynomial(coeffs=[0.983498,0.0336515,-1.10542e-07,-3.67434e-08,2.31412e-11,29626,16.5855], Tmin=(298,'K'), Tmax=(1000,'K')),
#             NASAPolynomial(coeffs=[7.47439,0.0160127,-6.48231e-09,-3.58197e-09,9.23651e-13,28086,-16.133], Tmin=(1000,'K'), Tmax=(2000,'K')),
#         ],
#         Tmin = (298,'K'),
#         Tmax = (2000,'K'),
#         E0 = (243.889,'kJ/mol'),
#         Cp0 = (33.2579,'J/mol/K'),
#         CpInf = (232.805,'J/mol/K'),
#     ),
#     shortDesc = """T12/89""",
#     longDesc = 
# """
# T12/89
# _low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
# [CH]1C=CC=C1
# _imported from 2-BTP/2-BTP_thermo.txt.
# """,
# )

entry(
    index = 143,
    label = "C4H2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,T}
2 C u0 p0 c0 {1,S} {4,T}
3 C u0 p0 c0 {1,T} {5,S}
4 C u0 p0 c0 {2,T} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.0544,0.041627,-6.58718e-05,5.32571e-08,-1.66832e-11,54185.2,14.8666], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.15763,0.00554305,-1.35916e-06,1.87801e-11,2.31895e-14,52588,-23.7115], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (449.343,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (133.032,'J/mol/K'),
    ),
    shortDesc = """D11/99""",
    longDesc = 
"""
D11/99
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#CC#C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 144,
    label = "C4H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.744494,0.0396789,-2.28981e-05,2.1353e-09,2.30964e-12,22653.3,23.4379], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.01348,0.0226346,-9.25455e-06,1.68079e-09,-1.04086e-13,20955,-8.88931], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (187.695,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = """USC/07""",
    longDesc = 
"""
USC/07
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC=C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 145,
    label = "C4H6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {5,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,D} {7,S} {8,S}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.112845,0.034369,-1.11074e-05,-9.21067e-09,6.20652e-12,11802.3,23.09], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.86731,0.0149187,-3.15487e-06,-4.18413e-10,1.57613e-13,9133.85,-23.3282], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (94.8824,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (228.648,'J/mol/K'),
    ),
    shortDesc = """H6W/94""",
    longDesc = 
"""
H6W/94
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC=C
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 146,
    label = "C4H4O",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {5,S}
2 C u0 p0 c0 {3,S} {4,D} {6,S}
3 C u0 p0 c0 {2,S} {5,D} {7,S}
4 C u0 p0 c0 {1,S} {2,D} {8,S}
5 C u0 p0 c0 {1,S} {3,D} {9,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.847469,0.0131774,5.99736e-05,-9.71563e-08,4.22734e-11,-5367.85,21.4945], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.38935,0.0140291,-5.07755e-06,8.24137e-10,-4.9532e-14,-8682.42,-27.9163], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-45.986,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (207.862,'J/mol/K'),
    ),
    shortDesc = """T03/97""",
    longDesc = 
"""
T03/97.
C1=COC=C1
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 147,
    label = "C5H4OH",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u1 p0 c0 {2,S} {6,S} {7,S}
4  C u0 p0 c0 {2,D} {5,S} {8,S}
5  C u0 p0 c0 {4,S} {6,D} {9,S}
6  C u0 p0 c0 {3,S} {5,D} {10,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.28398,0.0490299,-1.35844e-05,-2.92984e-08,1.90821e-11,6373.65,30.8074], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.3741,0.0151996,-5.45685e-06,8.80945e-10,-5.27493e-14,2203.58,-45.9569], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (48.5818,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (253.591,'J/mol/K'),
    ),
    shortDesc = """T 8/99""",
    longDesc = 
"""
T 8/99.
OC1=CC=C[CH]1
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 148,
    label = "CH3CHCHCHO",
    molecule = 
"""
1  O u0 p2 c0 {5,D}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  C u0 p0 c0 {1,D} {4,S} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.55578,0.0409641,-1.69869e-05,-6.00928e-18,2.31369e-21,-14139.5,37.4708], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.8795,-0.0209131,4.45361e-05,-2.60375e-08,4.86836e-12,-19527.9,-68.72], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-120.846,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = """T 5/92""",
    longDesc = 
"""
T 5/92
_low T polynomial Tmin changed from 298.15 to 298.0 K when importing to RMG.
CC=CC=O
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 149,
    label = "C6H5CO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {8,D}
2  C u0 p0 c0 {3,S} {4,S} {8,D}
3  C u1 p0 c0 {2,S} {5,S} {9,S}
4  C u0 p0 c0 {2,S} {7,D} {13,S}
5  C u0 p0 c0 {3,S} {6,D} {10,S}
6  C u0 p0 c0 {5,D} {7,S} {11,S}
7  C u0 p0 c0 {4,D} {6,S} {12,S}
8  C u0 p0 c0 {1,D} {2,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.02512,0.0615125,-3.16037e-05,-6.97246e-09,7.98351e-12,11255.8,35.7782], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.3744,0.0239993,-1.04657e-05,2.16691e-09,-1.8007e-13,6914.78,-44.6592], Tmin=(1000,'K'), Tmax=(2500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2500,'K'),
        E0 = (89.2916,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (303.478,'J/mol/K'),
    ),
    shortDesc = """EST/BUR P 1/93""",
    longDesc = 
"""
EST/BUR P 1/93
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C=C1[CH]C=CC=C1
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 150,
    label = "CHF:CF2",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {5,D} {6,S}
5 C u0 p0 c0 {2,S} {3,S} {4,D}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.35521,0.0323113,-3.57904e-05,2.09758e-08,-5.1422e-12,-60645.8,19.2938], Tmin=(298,'K'), Tmax=(1100,'K')),
            NASAPolynomial(coeffs=[9.29782,0.00669066,-2.71841e-06,4.9759e-10,-3.35867e-14,-62705.1,-20.9391], Tmin=(1100,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-505.825,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (133.032,'J/mol/K'),
    ),
    shortDesc = """91GURVEY69STU""",
    longDesc = 
"""
91GURVEY69STU
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC=C(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 151,
    label = "C2H5OH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {9,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.8587,-0.00374017,6.95554e-05,-8.86548e-08,3.51688e-11,-29996.1,4.80185], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.56244,0.0152042,-5.38968e-06,8.6225e-10,-5.12898e-14,-31525.6,-9.47302], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-248.759,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (199.547,'J/mol/K'),
    ),
    shortDesc = """L 8/88""",
    longDesc = 
"""
L 8/88.
CCO
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 152,
    label = "C2H4OH",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u1 p0 c0 {2,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.40195,0.0215432,-2.23265e-06,-1.44641e-08,8.04884e-12,-3846.45,19.149], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.5944,0.00932293,-3.03039e-06,4.32163e-10,-2.197e-14,-5772.79,-13.9556], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-34.4451,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (174.604,'J/mol/K'),
    ),
    shortDesc = """T 4/83""",
    longDesc = 
"""
T 4/83
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CO
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 153,
    label = "CH2:CHF",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,S} {2,D} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0626711,0.0257034,-2.25501e-05,1.16768e-08,-2.77022e-12,-17842.3,24.4422], Tmin=(298,'K'), Tmax=(1100,'K')),
            NASAPolynomial(coeffs=[4.84908,0.0111463,-4.66982e-06,8.74783e-10,-5.94979e-14,-19152.5,-0.0817883], Tmin=(1100,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-151.807,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (133.032,'J/mol/K'),
    ),
    shortDesc = """91GURVEY92DAU""",
    longDesc = 
"""
91GURVEY92DAU
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CF
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 154,
    label = "CH3CHOH",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {8,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u1 p0 c0 {1,S} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.48133,0.01679,3.77555e-06,-1.39235e-08,6.00952e-12,-4012.01,14.5816], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.76654,0.0116344,-3.77907e-06,5.38289e-10,-2.73153e-14,-5609.3,-9.39804], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-34.4802,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (174.604,'J/mol/K'),
    ),
    shortDesc = """T 4/83""",
    longDesc = 
"""
T 4/83
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]O
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 155,
    label = "CH3CH2O",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.73025,0.0169085,3.99962e-06,-1.37112e-08,5.76436e-12,-3292.25,17.3361], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.01143,0.0121652,-4.04496e-06,5.90766e-10,-3.09696e-14,-4936.7,-6.79018], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-29.6458,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """T11/82""",
    longDesc = 
"""
T11/82
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC[O]
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 156,
    label = "CH2:CF2",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {4,D} {5,S} {6,S}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.544641,0.0361013,-4.24522e-05,2.68678e-08,-7.0049e-12,-41578.9,25.9139], Tmin=(298,'K'), Tmax=(1100,'K')),
            NASAPolynomial(coeffs=[7.52692,0.00816727,-3.24648e-06,5.85466e-10,-3.90185e-14,-43575.5,-14.4929], Tmin=(1100,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-349.675,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (133.032,'J/mol/K'),
    ),
    shortDesc = """91GURVEY69STU""",
    longDesc = 
"""
91GURVEY69STU
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 157,
    label = "CF2:CF2",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {6,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {6,D}
6 C u0 p0 c0 {3,S} {4,S} {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.59735,0.0339059,-4.12239e-05,2.60507e-08,-6.78805e-12,-81178.9,12.7972], Tmin=(298,'K'), Tmax=(1100,'K')),
            NASAPolynomial(coeffs=[11.3243,0.00499631,-2.11782e-06,3.98619e-10,-2.75039e-14,-83426.6,-31.2702], Tmin=(1100,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-675.664,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (133.032,'J/mol/K'),
    ),
    shortDesc = """71STUPRO""",
    longDesc = 
"""
71STUPRO
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC(F)=C(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 158,
    label = "BR",
    molecule = 
"""
multiplicity 2
1 Br u1 p3 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.48422,0.000161406,-5.63461e-07,7.46724e-10,-2.58956e-13,12708.4,6.86657], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.08902,0.000711612,-2.69887e-07,4.15012e-11,-2.3138e-15,12855.6,9.07043], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (105.654,'kJ/mol'),
        Cp0 = (20.7862,'J/mol/K'),
        CpInf = (20.7862,'J/mol/K'),
    ),
    shortDesc = """J 6/74""",
    longDesc = 
"""
J 6/74
BR                J 6/74BR  1    0    0    0G   300.00   5000.00  1000.00      1
0.20843207E+01 0.71949483E-03-0.27419924E-06 0.42422650E-10-0.23791570E-14    2
0.12858837E+05 0.90838003E+01 0.24611551E+01 0.33319275E-03-0.10080655E-05    3
0.12262126E-08-0.44283510E-12 0.12711920E 05 0.69494733E+01                   4.
[Br]
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 159,
    label = "CH2:CF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.936646,0.023455,-2.60991e-05,1.68334e-08,-4.66583e-12,12014,19.5947], Tmin=(298,'K'), Tmax=(1050,'K')),
            NASAPolynomial(coeffs=[5.93667,0.00654409,-2.37413e-06,3.82235e-10,-2.2536e-14,10745.2,-5.57304], Tmin=(1050,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (97.1583,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """96ZACWES""",
    longDesc = 
"""
96ZACWES
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=[C]F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 160,
    label = "HBR",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48118,0.000342734,-1.80533e-06,3.61181e-09,-1.74298e-12,-5355.37,4.01309], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.83372,0.00148518,-5.13137e-07,8.73711e-11,-5.72363e-15,-5176.21,7.43754], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-44.4806,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """J 9/65""",
    longDesc = 
"""
J 9/65
HBR               J 9/65H   1BR  1    0    0G   300.00   5000.00  1000.00      1
0.27935804E+01 0.15655925E-02-0.56171064E-06 0.95783142E-10-0.61813990E-14    2
-0.52338384E+04 0.76423703E+01 0.36056690E+01-0.59529431E-03 0.65029568E-06    3
0.93781219E-09-0.71141852E-12-0.54389455E+04 0.34831774E+01                   4.
Br
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 161,
    label = "BRO",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {2,S}
2 O  u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.48296,0.00685677,-3.78834e-06,-4.21358e-09,3.45838e-12,13862,12.0185], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.13723,-0.000516464,2.06072e-07,-3.26108e-11,1.97331e-15,13208.9,-1.47002], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (114.212,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = """BRO       82WAG/EVA     BR  1O   1    0    0G   300.00   2000.00   593.00      1""",
    longDesc = 
"""
BRO       82WAG/EVA     BR  1O   1    0    0G   300.00   2000.00   593.00      1
0.38423535E+01 0.29818127E-03-0.10111621E-08-0.45536224E-11-0.12545159E-14    2
0.13986282E+05 0.65954140E+01 0.34409032E+01 0.19365875E-02-0.11562326E-05    3
-0.23853307E-08 0.26881704E-11 0.14050726E+05 0.84726383E+01                   4.
[O]Br
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 162,
    label = "BROH",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.31732,0.00505329,-1.73683e-06,-2.67712e-09,1.93314e-12,-8624.68,9.49126], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.52559,0.00188368,-6.04304e-07,8.98999e-11,-5.06962e-15,-8929.77,3.31036], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-72.361,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """Burc""",
    longDesc = 
"""
Burc
BROH      76BEN         H   1BR  1O   1    0G   300.00   2000.00   895.00      1
0.44804555E+01 0.72687612E-03 0.42097174E-07-0.49948238E-11-0.24686600E-14    2
-0.10963203E+05 0.39700594E+01 0.40847205E+01 0.15786399E-02-0.21558384E-06    3
-0.41121729E-09 0.20176279E-12-0.10846878E+05 0.60649913E+01                   4.
OBr
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 163,
    label = "CF2:CF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {2,S} {5,D}
5 C u1 p0 c0 {3,S} {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.86833,0.0252551,-3.00287e-05,1.88689e-08,-4.99936e-12,-27765.2,13.4445], Tmin=(298,'K'), Tmax=(1050,'K')),
            NASAPolynomial(coeffs=[9.38451,0.00387155,-1.53696e-06,2.69644e-10,-1.76406e-14,-29433.5,-19.4758], Tmin=(1050,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-231.01,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """96ZACWES""",
    longDesc = 
"""
96ZACWES
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[C]=C(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 164,
    label = "CF2:O",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.17614,0.021087,-2.39216e-05,1.39949e-08,-3.37605e-12,-77951.3,19.1134], Tmin=(298,'K'), Tmax=(1150,'K')),
            NASAPolynomial(coeffs=[6.79131,0.00338305,-1.43012e-06,2.71226e-10,-1.90524e-14,-79454,-9.48312], Tmin=(1150,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-650.702,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """71STUPRO""",
    longDesc = 
"""
71STUPRO
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 165,
    label = "CF2:CH",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,D}
4 C u1 p0 c0 {3,D} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.647126,0.0316596,-4.14529e-05,2.86094e-08,-8.06098e-12,-9438.54,21.7994], Tmin=(298,'K'), Tmax=(1050,'K')),
            NASAPolynomial(coeffs=[7.41103,0.0064817,-3.06314e-06,6.25625e-10,-4.55126e-14,-11017.4,-11.6171], Tmin=(1050,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-81.0671,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """96ZACWES""",
    longDesc = 
"""
96ZACWES
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=C(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 166,
    label = "CF:O",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {3,D}
3 C u1 p0 c0 {1,S} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.94061,0.00747092,-6.21833e-06,2.62916e-09,-4.73222e-13,-21792.3,11.1689], Tmin=(298,'K'), Tmax=(1250,'K')),
            NASAPolynomial(coeffs=[5.14996,0.00184938,-7.40232e-07,1.32785e-10,-8.8306e-15,-22488.4,-0.49683], Tmin=(1250,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-181.964,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (58.2013,'J/mol/K'),
    ),
    shortDesc = """71STUPRO""",
    longDesc = 
"""
71STUPRO
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=[C]F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 167,
    label = "CH3BR",
    molecule = 
"""
1 Br u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61367,-0.00088654,2.94669e-05,-3.76504e-08,1.4939e-11,-5614.02,8.24979], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.14294,0.00761097,-2.67015e-06,4.24036e-10,-2.50884e-14,-6205.46,3.21433], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-47.1204,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """CH3BR     DIPPR         C   1H   3BR  1    0G   300.00   3000.00  1100.00      1""",
    longDesc = 
"""
CH3BR     DIPPR         C   1H   3BR  1    0G   300.00   3000.00  1100.00      1
0.26622491E+01 0.10938679E-01-0.49091741E-05 0.97218827E-09-0.69039725E-13    2
-0.58748252E+04 0.11128287E+02 0.13844668E+01 0.15781927E-01-0.13119413E-04    3
0.77319100E-08-0.21949811E-11-0.55462775E+04 0.17495386E+02                   4.
CBr
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 168,
    label = "C2H5BR",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.629,0.00637388,3.97847e-05,-5.78493e-08,2.39751e-11,-9022.51,10.7168], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.95002,0.0128709,-4.60447e-06,7.41067e-10,-4.42632e-14,-10639.4,-10.0518], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-75.3038,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """C2H5BR    DIPPR         C   2H   5BR  1    0G   300.00   3000.00  1140.00      1""",
    longDesc = 
"""
C2H5BR    DIPPR         C   2H   5BR  1    0G   300.00   3000.00  1140.00      1
0.10484190E+01 0.25329179E-01-0.13151664E-04 0.28967557E-08-0.22319548E-12    2
-0.88946358E+04 0.21877824E+02 0.52438083E+00 0.30080803E-01-0.22248551E-04    3
0.93023889E-08-0.17393510E-11-0.90132273E+04 0.23537494E+02                   4.
CCBr
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 169,
    label = "CHF:O",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.1185,0.010774,-5.51582e-06,5.81519e-10,2.17042e-13,-46356.7,14.6524], Tmin=(298,'K'), Tmax=(1150,'K')),
            NASAPolynomial(coeffs=[4.81925,0.00505418,-2.01421e-06,3.63591e-10,-2.44724e-14,-47263.1,0.0972251], Tmin=(1150,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-386.87,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """71STUPRO""",
    longDesc = 
"""
71STUPRO
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=CF
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 170,
    label = "HOC2H4O2",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  O u0 p2 c0 {5,S} {10,S}
3  O u1 p2 c0 {1,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.4421,0.025288,-1.51605e-05,5.24921e-09,-7.91471e-13,-21750.7,10.4122], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[10.0942,0.0123879,-3.73812e-06,5.46875e-10,-3.09944e-14,-23771.1,-20.0957], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-178.818,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (220.334,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]OCCO
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 171,
    label = "CH2BR",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {2,S}
2 C  u1 p0 c0 {1,S} {3,S} {4,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.49879,0.0144144,-8.36763e-06,2.56756e-09,-3.51519e-13,20761.3,34.9401], Tmin=(298,'K'), Tmax=(1040,'K')),
            NASAPolynomial(coeffs=[-0.287987,0.0109362,-4.72499e-06,9.0419e-10,-6.2867e-14,20433.5,28.7153], Tmin=(1040,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
        E0 = (169.453,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (83.1447,'J/mol/K'),
    ),
    shortDesc = """MCMGOLest""",
    longDesc = 
"""
MCMGOLest
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]Br
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 172,
    label = "CHF:CHF[Z]",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {2,S} {3,D} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.383152,0.0294896,-2.94145e-05,1.64336e-08,-4.01759e-12,-36926.9,22.5083], Tmin=(298,'K'), Tmax=(1100,'K')),
            NASAPolynomial(coeffs=[7.34201,0.00821939,-3.17549e-06,5.49282e-10,-3.47434e-14,-38823.3,-13.1129], Tmin=(1100,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-310.115,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (133.032,'J/mol/K'),
    ),
    shortDesc = """82STAVOY95ZA""",
    longDesc = 
"""
82STAVOY95ZA
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC=CF
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 173,
    label = "C2H3BR",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 C  u0 p0 c0 {1,S} {2,D} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.44082,0.0133417,7.36029e-06,-2.10891e-08,1.00996e-11,7559.68,15.0863], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.26545,0.00840448,-2.96023e-06,4.71565e-10,-2.79679e-14,6279.17,-5.8908], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (62.197,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (133.032,'J/mol/K'),
    ),
    shortDesc = """CH2:CHBR  DIPPR         C   2H   3BR  1    0G   300.00   3000.00  1100.00      1""",
    longDesc = 
"""
CH2:CHBR  DIPPR         C   2H   3BR  1    0G   300.00   3000.00  1100.00      1
0.48816714E+01 0.11872023E-01-0.54511750E-05 0.10926716E-08-0.77674167E-13    2
0.72374120E+04 0.14265356E+01 0.63704010E+00 0.26976451E-01-0.26856586E-04    3
0.15318821E-07-0.37691556E-11 0.82471016E+04 0.22526875E+02                   4
CH3-CH2BR DIPPR         C   2H   5BR  1    0G   300.00   3000.00  1140.00      1
0.10484190E+01 0.25329179E-01-0.13151664E-04 0.28967557E-08-0.22319548E-12    2
-0.88946358E+04 0.21877824E+02 0.52438083E+00 0.30080803E-01-0.22248551E-04    3
0.93023889E-08-0.17393510E-11-0.90132273E+04 0.23537494E+02                   4
C2H3BR    DIPPR         C   2H   3BR  1    0G   300.00   3000.00  1100.00      1
0.48816714E+01 0.11872023E-01-0.54511750E-05 0.10926716E-08-0.77674167E-13    2
0.72374120E+04 0.14265356E+01 0.63704010E+00 0.26976451E-01-0.26856586E-04    3
0.15318821E-07-0.37691556E-11 0.82471016E+04 0.22526875E+02                   4.
C=CBr
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 174,
    label = "CHF:CH[Z]",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u1 p0 c0 {2,D} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.444202,0.0266069,-3.1481e-05,2.05356e-08,-5.52525e-12,13722.2,21.6689], Tmin=(298,'K'), Tmax=(1050,'K')),
            NASAPolynomial(coeffs=[5.27205,0.00817547,-3.46738e-06,6.47886e-10,-4.39229e-14,12647.8,-1.99725], Tmin=(1050,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (110.849,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """96ZACWES""",
    longDesc = 
"""
96ZACWES
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=CF
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 175,
    label = "CHF:CF[Z]",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u1 p0 c0 {2,S} {3,D}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.48306,0.0252896,-2.89899e-05,1.83569e-08,-4.98659e-12,-6275.04,18.7682], Tmin=(298,'K'), Tmax=(1050,'K')),
            NASAPolynomial(coeffs=[7.72646,0.00500295,-1.86131e-06,3.11994e-10,-1.95361e-14,-7900.3,-12.8643], Tmin=(1050,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-53.9692,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = """96ZACWES""",
    longDesc = 
"""
96ZACWES
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[C]=CF
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 176,
    label = "BTP",
    molecule = 
"""
1 Br u0 p3 c0 {6,S}
2 F  u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
6 C  u0 p0 c0 {1,S} {5,S} {7,D}
7 C  u0 p0 c0 {6,D} {8,S} {9,S}
8 H  u0 p0 c0 {7,S}
9 H  u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.873901,0.0574719,-6.85523e-05,4.19986e-08,-1.03943e-11,-73388.8,23.8649], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.6667,0.0101381,-4.06919e-06,7.42198e-10,-5.06305e-14,-79746.3,-45.1433], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-611.478,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (203.705,'J/mol/K'),
    ),
    shortDesc = """BTP                     H   2C   3F   3BR  1g    300.00   5000.00 1000.00      1 Hf -143.7,db""",
    longDesc = 
"""
BTP                     H   2C   3F   3BR  1g    300.00   5000.00 1000.00      1 Hf -143.7,db
1.46667151E+01 1.01380748E-02-4.06918919E-06 7.42198345E-10-5.06305036E-14    2
-7.79627873E+04-4.51432754E+01 8.73900901E-01 5.74719145E-02-6.85523350E-05    3
4.19986296E-08-1.03943433E-11-7.45967271E+04 2.38649170E+01                   4
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C(Br)C(F)(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 177,
    label = "CF3CBRCH",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {6,S}
2 F  u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
6 C  u0 p0 c0 {1,S} {5,S} {7,D}
7 C  u1 p0 c0 {6,D} {8,S}
8 H  u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.65445,0.0569985,-7.77154e-05,5.34289e-08,-1.46906e-11,-43572.6,20.9212], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.1496,0.00686658,-2.79602e-06,5.15042e-10,-3.53815e-14,-46670.8,-45.6453], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-362.857,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = """""",
    longDesc = 
"""
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=C(Br)C(F)(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

entry(
    index = 178,
    label = "CF3CHBRCH2",
    molecule = 
"""
multiplicity 2
1  Br u0 p3 c0 {5,S}
2  F  u0 p3 c0 {6,S}
3  F  u0 p3 c0 {6,S}
4  F  u0 p3 c0 {6,S}
5  C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
7  C  u1 p0 c0 {5,S} {9,S} {10,S}
8  H  u0 p0 c0 {5,S}
9  H  u0 p0 c0 {7,S}
10 H  u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.47869,0.0602025,-6.99637e-05,4.19438e-08,-1.01112e-11,-66959.9,21.7133], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.5698,0.01194,-4.72448e-06,8.53282e-10,-5.78033e-14,-70395,-48.7869], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-557.311,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = """*** CHBrx ***""",
    longDesc = 
"""
*** CHBrx ***
C2H3BR                  H   3C   2Br  1    0g    300.00   5000.00 1000.00      1
6.18272332E+00 9.06458750E-03-3.48619075E-06 6.16873253E-10-4.11658974E-14    2
5.71731552E+03-5.39046319E+00 9.11868419E-01 2.57628448E-02-2.38745332E-05    3
1.17910898E-08-2.27220616E-12 7.08251435E+03 2.13419060E+01                   4

*** CHBrFx ***
_low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(Br)C(F)(F)F
_imported from 2-BTP/2-BTP_thermo.txt.
""",
)

