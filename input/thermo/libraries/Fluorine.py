#!/usr/bin/env python
# encoding: utf-8

name = "Fluorine"
shortDesc = u"/Users/rwest/Code/Importer/RMG-models/Fluorine/thermo-hfo1234zee-burcat-c.txt"
longDesc = u"""
Valeri I. Babushok, Michael J. Hegetschweiler, Gregory T. Linteris, Donald R. Burgess, Jr., Jeffrey A. Manion, Robert R. Burrell, Michael J. Hegetschweiler
Obtained via email from Gregory T. Linteris (NIST) at the 11th U. S. National Combustion Meeting
Model for C1-C2 Hydrofluorocarbon (HFC) combustion of refrigerants
To be submitted to ?Journal of Fluorine Chemistry?
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
    shortDesc = u"""71STUPRO""",
    longDesc = 
u"""
71STUPRO
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
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
    shortDesc = u"""71STUPRO""",
    longDesc = 
u"""
71STUPRO
********************************
*** Hydrogen/Oxygen/Fluorine ***
********************************
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[F]
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
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
    shortDesc = u"""71STUPRO""",
    longDesc = 
u"""
71STUPRO
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FF
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
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
    shortDesc = u"""78KOL74CHEROD""",
    longDesc = 
u"""
78KOL74CHEROD
************************
*** C1 Fluorocarbons ***
************************
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CF
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
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
    shortDesc = u"""78KOL74CHEROD""",
    longDesc = 
u"""
78KOL74CHEROD
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FCF
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
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
    shortDesc = u"""78KOL74CHEROD""",
    longDesc = 
u"""
78KOL74CHEROD
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
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
    shortDesc = u"""78KOL74CHEROD""",
    longDesc = 
u"""
78KOL74CHEROD
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC(F)(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
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
    shortDesc = u"""82MCMGOL71STU""",
    longDesc = 
u"""
82MCMGOL71STU
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[C](F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
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
    shortDesc = u"""82MCMGOL96ZAC""",
    longDesc = 
u"""
82MCMGOL96ZAC
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[CH]F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
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
    shortDesc = u"""82MCMGOL96ZAC""",
    longDesc = 
u"""
82MCMGOL96ZAC
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
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
    shortDesc = u"""84PRINIL71STU""",
    longDesc = 
u"""
84PRINIL71STU
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
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
    shortDesc = u"""78ROD71STUPRO""",
    longDesc = 
u"""
78ROD71STUPRO
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[C]F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
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
    shortDesc = u"""91GURVEY71STU""",
    longDesc = 
u"""
91GURVEY71STU
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
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
    shortDesc = u"""82BATWAL96ZAC""",
    longDesc = 
u"""
82BATWAL96ZAC
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[O]C(F)(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 14,
    label = "CF2O",
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
    shortDesc = u"""71STUPRO""",
    longDesc = 
u"""
71STUPRO
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 15,
    label = "CHFO",
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
    shortDesc = u"""71STUPRO""",
    longDesc = 
u"""
71STUPRO
*********************************
*** Oxidized C1 Fluorocarbons ***
*********************************
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=CF
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 16,
    label = "CFO",
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
    shortDesc = u"""71STUPRO""",
    longDesc = 
u"""
71STUPRO
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=[C]F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 17,
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
    shortDesc = u"""75CHEROD""",
    longDesc = 
u"""
75CHEROD
*********************
*** Fluoroethanes ***
*********************
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCF
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 18,
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
    shortDesc = u"""75CHEROD""",
    longDesc = 
u"""
75CHEROD
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 19,
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
    shortDesc = u"""75CHEROD""",
    longDesc = 
u"""
75CHEROD
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(F)(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 20,
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
    shortDesc = u"""68LACSKI96ZAC""",
    longDesc = 
u"""
68LACSKI96ZAC
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FCC(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 21,
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
    shortDesc = u"""75CHEROD""",
    longDesc = 
u"""
75CHEROD
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FCC(F)(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 22,
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
    shortDesc = u"""95BURZAC96ZAC""",
    longDesc = 
u"""
95BURZAC96ZAC
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC(F)C(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 23,
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
    shortDesc = u"""75CHEROD""",
    longDesc = 
u"""
75CHEROD
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC(F)C(F)(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 24,
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
    shortDesc = u"""75CHEROD""",
    longDesc = 
u"""
75CHEROD
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC(F)(F)C(F)(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 25,
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
    shortDesc = u"""95BURZAC90CHE""",
    longDesc = 
u"""
95BURZAC90CHE
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[CH]F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 26,
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
    shortDesc = u"""78ROD90CHERAU""",
    longDesc = 
u"""
78ROD90CHERAU
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[C](F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 27,
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
    shortDesc = u"""90CHERAU""",
    longDesc = 
u"""
90CHERAU
********************
*** Fluoroethyls ***
********************
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CF
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 28,
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
    shortDesc = u"""95BURZAC91CHE""",
    longDesc = 
u"""
95BURZAC91CHE
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[CH]CF
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 29,
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
    shortDesc = u"""91CHERAU""",
    longDesc = 
u"""
91CHERAU
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC[C](F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 30,
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
    shortDesc = u"""90CHERAU""",
    longDesc = 
u"""
90CHERAU
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 31,
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
    shortDesc = u"""91CHERAU""",
    longDesc = 
u"""
91CHERAU
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[CH]C(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 32,
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
    shortDesc = u"""95BURZAC91CHE""",
    longDesc = 
u"""
95BURZAC91CHE
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[C](F)C(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 33,
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
    shortDesc = u"""78ROD90CHERAU""",
    longDesc = 
u"""
78ROD90CHERAU
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(F)(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 34,
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
    shortDesc = u"""95BURZAC91CHE""",
    longDesc = 
u"""
95BURZAC91CHE
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[CH]C(F)(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 35,
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
    shortDesc = u"""78ROD91CHERAU""",
    longDesc = 
u"""
78ROD91CHERAU
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[C](F)C(F)(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 36,
    label = "CH2CHF",
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
    shortDesc = u"""91GURVEY92DAU""",
    longDesc = 
u"""
91GURVEY92DAU
***********************
*** Fluoroethylenes ***
***********************
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CF
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 37,
    label = "CH2CF2",
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
    shortDesc = u"""91GURVEY69STU""",
    longDesc = 
u"""
91GURVEY69STU
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=C(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 38,
    label = "CHFCHF[Z]",
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
    shortDesc = u"""82STAVOY95ZA""",
    longDesc = 
u"""
82STAVOY95ZA
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC=CF
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 39,
    label = "CHFCF2",
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
    shortDesc = u"""91GURVEY69STU""",
    longDesc = 
u"""
91GURVEY69STU
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC=C(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 40,
    label = "CF2CF2",
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
    shortDesc = u"""71STUPRO""",
    longDesc = 
u"""
71STUPRO
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC(F)=C(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 41,
    label = "CH2CF",
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
    shortDesc = u"""96ZACWES""",
    longDesc = 
u"""
96ZACWES
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=[C]F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 42,
    label = "CHFCH[Z]",
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
    shortDesc = u"""96ZACWES""",
    longDesc = 
u"""
96ZACWES
********************
*** Fluorovinyls ***
********************
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=CF
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 43,
    label = "CHFCF[Z]",
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
    shortDesc = u"""96ZACWES""",
    longDesc = 
u"""
96ZACWES
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[C]=CF
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 44,
    label = "CF2CH",
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
    shortDesc = u"""96ZACWES""",
    longDesc = 
u"""
96ZACWES
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=C(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 45,
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
    shortDesc = u"""71STUPRO""",
    longDesc = 
u"""
71STUPRO
************************
*** Fluoroacetylenes ***
************************
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#CF
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 46,
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
    shortDesc = u"""71STUPRO""",
    longDesc = 
u"""
71STUPRO
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC#CF
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 47,
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
    shortDesc = u"""96ZACWES""",
    longDesc = 
u"""
96ZACWES
*********************
*** Fluoroketenes ***
*********************
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C=CF
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 48,
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
    shortDesc = u"""96ZACWES""",
    longDesc = 
u"""
96ZACWES
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C=C(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 49,
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
    shortDesc = u"""96ZACWES""",
    longDesc = 
u"""
96ZACWES
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C=[C]F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 50,
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
    shortDesc = u"""hynes""",
    longDesc = 
u"""
hynes
BR                J 6/74BR  1    0    0    0G   300.00   5000.00  1000.00      1
0.20843207E+01 0.71949483E-03-0.27419924E-06 0.42422650E-10-0.23791570E-14    2
0.12858837E+05 0.90838003E+01 0.24611551E+01 0.33319275E-03-0.10080655E-05    3
0.12262126E-08-0.44283510E-12 0.12711920E 05 0.69494733E+01                   4
BR2               J12/61BR  20   00   00   0G   300.00   5000.00  1000.00      1
0.44479495E+01 0.10051208E-03-0.16393816E-07 0.22685621E-11-0.10236774E-15    2
0.23659941E+04 0.40888431E+01 0.38469580E+01 0.26111841E-02-0.40034147E-05    3
0.28120689E-08-0.73256202E-12 0.24846984E+04 0.69696985E+01                   4
HBR               J 9/65H   1BR  1    0    0G   300.00   5000.00  1000.00      1
0.27935804E+01 0.15655925E-02-0.56171064E-06 0.95783142E-10-0.61813990E-14    2
-0.52338384E+04 0.76423703E+01 0.36056690E+01-0.59529431E-03 0.65029568E-06    3
0.93781219E-09-0.71141852E-12-0.54389455E+04 0.34831774E+01                   4
CF3BR                  0C   1F   3BR  1    0G   300.000  4000.000 1000.00      1
0.10835589E+02+0.15757806E-02-0.20505728E-06-0.81578432E-10 0.17003094E-13    2
-0.81927266E+05-0.27720734E+02 0.44576893E+01 0.14666174E-01-0.20081193E-05    3
-0.10235016E-07+0.52610143E-11-0.80003992E+05 0.62208567E+01                   4
CH3BR     DIPPR         C   1H   3BR  1    0G   300.00   3000.00  1100.00      1
0.26622491E+01 0.10938679E-01-0.49091741E-05 0.97218827E-09-0.69039725E-13    2
-0.58748252E+04 0.11128287E+02 0.13844668E+01 0.15781927E-01-0.13119413E-04    3
0.77319100E-08-0.21949811E-11-0.55462775E+04 0.17495386E+02                   4
CH2CHBR  DIPPR         C   2H   3BR  1    0G   300.00   3000.00  1100.00      1
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
0.15318821E-07-0.37691556E-11 0.82471016E+04 0.22526875E+02                   4
C2H5BR    DIPPR         C   2H   5BR  1    0G   300.00   3000.00  1140.00      1
0.10484190E+01 0.25329179E-01-0.13151664E-04 0.28967557E-08-0.22319548E-12    2
-0.88946358E+04 0.21877824E+02 0.52438083E+00 0.30080803E-01-0.22248551E-04    3
0.93023889E-08-0.17393510E-11-0.90132273E+04 0.23537494E+02                   4
BRO       82WAG/EVA     BR  1O   1    0    0G   300.00   2000.00   593.00      1
0.38423535E+01 0.29818127E-03-0.10111621E-08-0.45536224E-11-0.12545159E-14    2
0.13986282E+05 0.65954140E+01 0.34409032E+01 0.19365875E-02-0.11562326E-05    3
-0.23853307E-08 0.26881704E-11 0.14050726E+05 0.84726383E+01                   4
BROH      76BEN         H   1BR  1O   1    0G   300.00   2000.00   895.00      1
0.44804555E+01 0.72687612E-03 0.42097174E-07-0.49948238E-11-0.24686600E-14    2
-0.10963203E+05 0.39700594E+01 0.40847205E+01 0.15786399E-02-0.21558384E-06    3
-0.41121729E-09 0.20176279E-12-0.10846878E+05 0.60649913E+01                   4
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=C(F)C(F)(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 51,
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
    shortDesc = u"""NIST""",
    longDesc = 
u"""
NIST
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=[C]C(F)(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 52,
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
    shortDesc = u"""NIST""",
    longDesc = 
u"""
NIST
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
O=CC(F)(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 53,
    label = "CH2(S)",
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
    shortDesc = u"""L S/93""",
    longDesc = 
u"""
L S/93.
[CH2]
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 54,
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
    shortDesc = u"""L S/93""",
    longDesc = 
u"""
L S/93.
[CH2]
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 55,
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
    shortDesc = u"""120186""",
    longDesc = 
u"""
120186
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[Ar]
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 56,
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
    shortDesc = u"""121286""",
    longDesc = 
u"""
121286
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
N#N
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 57,
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
    shortDesc = u"""TPIS78""",
    longDesc = 
u"""
TPIS78.
[H][H]
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 58,
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
    shortDesc = u"""L 7/88""",
    longDesc = 
u"""
L 7/88.
[H]
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 59,
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
    shortDesc = u"""TPIS89""",
    longDesc = 
u"""
TPIS89.
[O][O]
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 60,
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
    shortDesc = u"""L 1/90""",
    longDesc = 
u"""
L 1/90
GRI-Mech Version 3.0 Thermodynamics released 7/30/99
NASA Polynomial format for CHEMKIN-II
see README file for disclaimer.
[O]
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 61,
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
    shortDesc = u"""L 8/89""",
    longDesc = 
u"""
L 8/89.
O
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 62,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99202,-0.00240132,4.61794e-06,-3.88113e-09,1.36411e-12,3615.08,-0.103925], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.09289,0.00054843,1.26505e-07,-8.79462e-11,1.17412e-14,3858.66,4.4767], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (30.4447,'kJ/mol'),
        Cp0 = (29.1007,'J/mol/K'),
        CpInf = (37.4151,'J/mol/K'),
    ),
    shortDesc = u"""RUS 78""",
    longDesc = 
u"""
RUS 78.
[OH]
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 63,
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
    shortDesc = u"""L 7/88""",
    longDesc = 
u"""
L 7/88.
OO
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 64,
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
    shortDesc = u"""L 5/89""",
    longDesc = 
u"""
L 5/89.
[O]O
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 65,
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
    shortDesc = u"""TPIS79""",
    longDesc = 
u"""
TPIS79.
[C-]#[O+]
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 66,
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
    shortDesc = u"""L 7/88""",
    longDesc = 
u"""
L 7/88.
O=C=O
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 67,
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
    shortDesc = u"""L 8/88""",
    longDesc = 
u"""
L 8/88.
C
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 68,
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
    shortDesc = u"""L11/89""",
    longDesc = 
u"""
L11/89.
[CH3]
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 69,
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
    shortDesc = u"""L11/88""",
    longDesc = 
u"""
L11/88.
[C]
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 70,
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
    shortDesc = u"""TPIS79""",
    longDesc = 
u"""
TPIS79.
[CH]
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 71,
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
    shortDesc = u"""L 8/88""",
    longDesc = 
u"""
L 8/88.
CO
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 72,
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
    shortDesc = u"""L 8/88""",
    longDesc = 
u"""
L 8/88.
CC
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 73,
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
    shortDesc = u"""L12/92""",
    longDesc = 
u"""
L12/92.
C[CH2]
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 74,
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
    shortDesc = u"""L 1/91""",
    longDesc = 
u"""
L 1/91.
C=C
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 75,
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
    shortDesc = u"""L 1/91""",
    longDesc = 
u"""
L 1/91.
[C]#C
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 76,
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
            NASAPolynomial(coeffs=[0.933554,0.0264246,6.10597e-06,-2.19775e-08,9.51493e-12,-13958.5,19.2017], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.53414,0.0188722,-6.27185e-06,9.14756e-10,-4.78381e-14,-16467.5,-17.8923], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-118.828,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (249.434,'J/mol/K'),
    ),
    shortDesc = u"""L 4/85""",
    longDesc = 
u"""
L 4/85
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CCC
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 77,
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
    shortDesc = u"""L 1/91""",
    longDesc = 
u"""
L 1/91.
C#C
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 78,
    label = "C3H7",
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
            NASAPolynomial(coeffs=[1.05155,0.025992,2.38005e-06,-1.96096e-08,9.37325e-12,10631.9,21.1226], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.7027,0.0160442,-5.28332e-06,7.62986e-10,-3.93923e-14,8298.43,-15.4802], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (85.757,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (224.491,'J/mol/K'),
    ),
    shortDesc = u"""L 9/84""",
    longDesc = 
u"""
L 9/84
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]CC
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 79,
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
    shortDesc = u"""L 2/92""",
    longDesc = 
u"""
L 2/92.
[CH]=C
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 80,
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
            NASAPolynomial(coeffs=[2.1062,0.0072166,5.33847e-06,-7.37764e-09,2.07561e-12,978.601,13.1522], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.7708,0.0078715,-2.65638e-06,3.94443e-10,-2.11262e-14,127.833,2.92957], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (6.64192,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = u"""121686""",
    longDesc = 
u"""
121686
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C[O]
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 81,
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
            NASAPolynomial(coeffs=[3.86389,0.00559672,5.93272e-06,-1.04532e-08,4.36967e-12,-3193.91,5.47302], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.69267,0.00864577,-3.75101e-06,7.87235e-10,-6.48554e-14,-3242.51,5.81043], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-26.5115,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (103.931,'J/mol/K'),
    ),
    shortDesc = u"""GUNL93""",
    longDesc = 
u"""
GUNL93.
[CH2]O
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 82,
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
    shortDesc = u"""95BURZAC96ZAC""",
    longDesc = 
u"""
95BURZAC96ZAC
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FCCF
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 83,
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
    shortDesc = u"""L 8/88""",
    longDesc = 
u"""
L 8/88.
C=O
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 84,
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
    shortDesc = u"""L12/89""",
    longDesc = 
u"""
L12/89.
[CH]=O
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 85,
    label = "CF2CF",
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
    shortDesc = u"""96ZACWES""",
    longDesc = 
u"""
96ZACWES
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[C]=C(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 86,
    label = "CHFCHCF3",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {7,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u0 p0 c0 {5,S} {7,D} {8,S}
7 C u0 p0 c0 {4,S} {6,D} {9,S}
8 H u0 p0 c0 {6,S}
9 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.941993,0.0482324,-4.46848e-05,1.93728e-08,-2.9209e-12,-101894,23.2937], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.48122,0.0200031,-1.12323e-05,2.9987e-09,-3.09262e-13,-103898,-19.385], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-848.567,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (203.705,'J/mol/K'),
    ),
    shortDesc = u"""0""",
    longDesc = 
u"""
0

*** HFO1234ZEE ***
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC=CC(F)(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 87,
    label = "CHFCCF3",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
6 C u0 p0 c0 {4,S} {7,D} {8,S}
7 C u1 p0 c0 {5,S} {6,D}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.32858,0.0408063,-3.76794e-05,1.5829e-08,-2.20385e-12,-68139.5,17.9311], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.72422,0.0166944,-9.71761e-06,2.65852e-09,-2.78897e-13,-69892.1,-19.1162], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-566.683,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = u"""0""",
    longDesc = 
u"""
0
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC=[C]C(F)(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 88,
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
    shortDesc = u"""*** C3HFx ***""",
    longDesc = 
u"""
*** C3HFx ***
CF3CHCH2                H   3C   3F   3    0g    300.00   5000.00 1000.00      1
1.19726859E+01 1.25436030E-02-4.97049536E-06 8.98531469E-10-6.09049619E-14    2
-8.09542161E+04-3.53084262E+01-1.76944260E-01 5.04272890E-02-4.98918705E-05    3
2.45443525E-08-4.55045979E-12-7.77960857E+04 2.64237596E+01                   4.
C=CC(F)(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 89,
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
    shortDesc = u"""120186""",
    longDesc = 
u"""
120186
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=CC
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 90,
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
    shortDesc = u"""SRI91""",
    longDesc = 
u"""
SRI91
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#CO
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 91,
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
    shortDesc = u"""PD5/98""",
    longDesc = 
u"""
PD5/98
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C=[C]C
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 92,
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
    shortDesc = u"""SRIC91""",
    longDesc = 
u"""
SRIC91
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH]=C=O
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 93,
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
    shortDesc = u"""T 9/92""",
    longDesc = 
u"""
T 9/92.
C[C]=O
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 94,
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
            NASAPolynomial(coeffs=[2.13584,0.0181189,-1.73947e-05,9.34398e-09,-2.01458e-12,-7042.92,12.2156], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.5113,0.0090036,-4.1694e-06,9.23346e-10,-7.94838e-14,-7551.05,0.632247], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
        E0 = (-59.9051,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (108.088,'J/mol/K'),
    ),
    shortDesc = u"""L 5/90""",
    longDesc = 
u"""
L 5/90.
C=C=O
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 95,
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
            NASAPolynomial(coeffs=[3.40906,0.0107386,1.89149e-06,-7.15858e-09,2.86738e-12,1521.48,9.55829], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.97567,0.00813059,-2.74362e-06,4.0703e-10,-2.17602e-14,490.322,-5.04525], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (12.5013,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (128.874,'J/mol/K'),
    ),
    shortDesc = u"""SAND86""",
    longDesc = 
u"""
SAND86
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C=O
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 96,
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
    shortDesc = u"""L 8/88""",
    longDesc = 
u"""
L 8/88.
CC=O
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 97,
    label = "CFCHCF3",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {7,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u0 p0 c0 {5,S} {7,D} {8,S}
7 C u1 p0 c0 {4,S} {6,D}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.21378,0.0419375,-4.01432e-05,1.79433e-08,-2.84775e-12,-70085,18.24], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.79425,0.0166275,-9.69601e-06,2.65705e-09,-2.79155e-13,-71851.7,-19.5844], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
        E0 = (-582.965,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = u"""0""",
    longDesc = 
u"""
0
CHFCHCF3               0F   4C   3H   2     G   300.000  3000.000 1000.00      1 balaganesh,2012/matsugi,2017
0.92634224E+01 0.20227539E-01-0.11331861E-04 0.30195276E-08-0.31092705E-12    2
-0.10383550E+06-0.18187751E+02 0.11738639E+01 0.46334514E-01-0.41115434E-04    3
0.16623984E-07-0.21492263E-11-0.10190502E+06 0.22402507E+02                   4
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
F[C]=CC(F)(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 98,
    label = "CFCCF3",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {7,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u0 p0 c0 {5,S} {7,T}
7 C u0 p0 c0 {4,S} {6,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.66217,0.0504259,-7.06033e-05,4.9667e-08,-1.39443e-11,-66089.2,18.0213], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.8905,0.00504275,-2.01504e-06,3.33703e-10,-1.85456e-14,-68934.9,-42.3902], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-550.221,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (153.818,'J/mol/K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
FC#CC(F)(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 99,
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
    shortDesc = u"""CF3CCH2                 H   2C   3F   3    0g    300.00   5000.00 1000.00      1""",
    longDesc = 
u"""
CF3CCH2                 H   2C   3F   3    0g    300.00   5000.00 1000.00      1
1.23019497E+01 9.51096222E-03-3.81477953E-06 6.95310445E-10-4.74033015E-14    2
-4.99225413E+04-3.49756046E+01 8.07938725E-01 4.82284101E-02-5.55615570E-05    3
3.31924991E-08-8.04824987E-12-4.70705880E+04 2.27361360E+01                   4.
C=[C]C(F)(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 100,
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
    shortDesc = u"""""",
    longDesc = 
u"""
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
C#CC(F)(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 101,
    label = "CF3COCH3",
    molecule = 
"""
1  F u0 p3 c0 {5,S}
2  F u0 p3 c0 {5,S}
3  F u0 p3 c0 {5,S}
4  O u0 p2 c0 {7,D}
5  C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
6  C u0 p0 c0 {7,S} {8,S} {9,S} {10,S}
7  C u0 p0 c0 {4,D} {5,S} {6,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
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
    shortDesc = u"""*** C2HOFx ***""",
    longDesc = 
u"""
*** C2HOFx ***
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
CC(=O)C(F)(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 102,
    label = "CH2CFCF3",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u0 p0 c0 {4,S} {5,S} {7,D}
7 C u0 p0 c0 {6,D} {8,S} {9,S}
8 H u0 p0 c0 {7,S}
9 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.00153,0.0498008,-4.61878e-05,1.64792e-08,-3.13156e-13,-99948.7,20.7747], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.311,0.00944785,-3.52268e-06,5.79392e-10,-3.50621e-14,-103384,-46.913], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-832.404,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (203.705,'J/mol/K'),
    ),
    shortDesc = u"""2,3,3,3-T 1/10""",
    longDesc = 
u"""
2,3,3,3-T 1/10.
C=C(F)C(F)(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 103,
    label = "CH-CFCF3",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 F u0 p3 c0 {6,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u0 p0 c0 {4,S} {5,S} {7,D}
7 C u1 p0 c0 {6,D} {8,S}
8 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.499663,0.0571202,-7.49546e-05,4.83898e-08,-1.22362e-11,-70396.9,23.0298], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.3232,0.00655667,-2.43588e-06,3.98836e-10,-2.40439e-14,-73556.3,-45.2117], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
        E0 = (-586.972,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (178.761,'J/mol/K'),
    ),
    shortDesc = u"""CH2CFCF3  2,3,3,3-T 1/10C   3H   2F   4    0G   200.000  6000.000 1000.00      1 Burcat""",
    longDesc = 
u"""
CH2CFCF3  2,3,3,3-T 1/10C   3H   2F   4    0G   200.000  6000.000 1000.00      1 Burcat
1.43109945E+01 9.44785369E-03-3.52268169E-06 5.79391979E-10-3.50621207E-14    2 dH-matsugi
-1.04818074E+05-4.69130460E+01 1.00153498E+00 4.98007666E-02-4.61878165E-05    3
1.64791672E-08-3.13155879E-13-1.01382684E+05 2.07746963E+01-9.78122362E+04    4.
[CH]=C(F)C(F)(F)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

entry(
    index = 104,
    label = "CH2CFO",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 O u0 p2 c0 {4,D}
3 C u1 p0 c0 {4,S} {5,S} {6,S}
4 C u0 p0 c0 {1,S} {2,D} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.807509,0.0306962,-3.16571e-05,1.70422e-08,-3.7773e-12,-31492.8,20.5216], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.36521,0.00720529,-2.94165e-06,5.42254e-10,-3.72494e-14,-33493.1,-17.9789], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
        E0 = (-264.345,'kJ/mol'),
        Cp0 = (33.2579,'J/mol/K'),
        CpInf = (128.874,'J/mol/K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Low T polynomial Tmin changed from 300.0 to 298.0 K when importing to RMG.
[CH2]C(=O)F
Imported from Fluorine/thermo-hfo1234zee-burcat-c.txt.
""",
)

