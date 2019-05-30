#!/usr/bin/env python
# encoding: utf-8

name = "OxygenButadiene"
shortDesc = u"Project Library for Fundamentals of Polymer Fouling in Ethylene Crackers"
longDesc = u"""
This library is made by Hao-Wei Pang for the Fundamentals of Polymer Fouling in Ethylene Crackers.

It includes thermochemistry of the products from singlet oxygen + 1,3-butadiene reactions, calculated using the CBS-QB3 level of theory in April 2019.

Specifics of the calculations performed:
1. CBS-QB3 Level of theory was used after a B3LYP/6-311G(d,p) geometry optimization was performed
2. CBS-QB3 Energy calculation was performed
3. Frequency was calculated using B3LYP/CBSB7 iop(7/33=1) (Hessian was calculated)
4. 1D Hindered Rotors were calculated for steps of 10 degrees up to the full 360 degree cycle, with geometry optimization on each step.
5. All files generated were fed to Arkane (April 2019).
6. Frequency scaling factor was 0.99
7. Bond additivity corrections were applied based on Petersson et al. 1998 (http://aip.scitation.org/doi/10.1063/1.477794)

Disclaimer: The number of significant figures displayed does not reflect the accuracy of thermochemistry values. Sommers and Simmie esimates
the error in enthalpy of formation by CBS-QB3 calculations to be + or - 2.4kcal/mol (http://pubs.acs.org/doi/abs/10.1021/acs.jpca.5b05448).
"""
entry(
    index = 0,
    label = "O2_triplet",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.50756, -0.000455604, 1.53119e-06, 1.63224e-09, -2.4256e-12, -1248.37, 4.72181],
                Tmin = (10, 'K'),
                Tmax = (597.406, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.87478, 0.00221074, -1.22018e-06, 3.01986e-10, -2.73707e-14, -1144.74, 7.68321],
                Tmin = (597.406, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-10.3768, 'kJ/mol'),
        Cp0 = (29.1007, 'J/(mol*K)'),
        CpInf = (37.4151, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for OxygenButadiene calculated by Duminda Ranasinghe""",
    longDesc = 
u"""
Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7
""",
)

entry(
    index = 1,
    label = "O2_singlet",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.50764, -0.000463071, 1.57719e-06, 1.6459e-09, -2.49778e-12, 13020.8, 3.62477],
                Tmin = (10, 'K'),
                Tmax = (591.912, 'K'),
            ),
            NASAPolynomial(
                coeffs = [2.8751, 0.00223078, -1.24376e-06, 3.1151e-10, -2.86654e-14, 13123.4, 6.57861],
                Tmin = (591.912, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (108.264, 'kJ/mol'),
        Cp0 = (29.1007, 'J/(mol*K)'),
        CpInf = (37.4151, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for OxygenButadiene calculated by Duminda Ranasinghe""",
    longDesc = 
u"""
Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7
""",
)


entry(
    index = 2,
    label = "C4H6O2_23_triplet",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {2,D} {8,S} {9,S}
2  C u0 p0 c0 {1,D} {3,S} {10,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
6  O u0 p2 c0 {5,S} {7,S}
7  O u1 p2 c0 {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.71776, 0.0355538, -1.4042e-05, -1.6851e-09, 1.73618e-12, 21529.4, 13.6117],
                Tmin = (10, 'K'),
                Tmax = (1262.5, 'K'),
            ),
            NASAPolynomial(
                coeffs = [10.0706, 0.0244229, -1.15067e-05, 2.62069e-09, -2.34195e-13, 19208.2, -21.3576],
                Tmin = (1262.5, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (179.008, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (274.378, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for OxygenButadiene calculated by Duminda Ranasinghe""",
    longDesc = 
u"""
Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7
""",
)


entry(
    index = 3,
    label = "C4H6O2_25",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  O u0 p2 c0 {3,S} {5,S}
5  O u0 p2 c0 {4,S} {6,S}
6  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.08956, -0.00841402, 0.000178833, -3.01064e-07, 1.62189e-10, -3850.24, 9.88676],
                Tmin = (10, 'K'),
                Tmax = (583.267, 'K'),
            ),
            NASAPolynomial(
                coeffs = [-0.812876, 0.0491965, -3.10204e-05, 9.3131e-09, -1.07002e-12, -3686.43, 27.3971],
                Tmin = (583.267, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-32.0288, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (282.692, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for OxygenButadiene calculated by Duminda Ranasinghe""",
    longDesc = 
u"""
Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7
""",
)


entry(
    index = 4,
    label = "S_412_singlet",
    molecule = 
"""
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
6  O u1 p2 c0 {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.72102, 0.0250551, 0.000245259, -1.08466e-06, 1.3423e-09, 12080, 10.3219],
                Tmin = (10, 'K'),
                Tmax = (293.49, 'K'),
            ),
            NASAPolynomial(
                coeffs = [6.03847, 0.0353178, -2.10712e-05, 6.14336e-09, -6.99982e-13, 11763.8, -1.08793],
                Tmin = (293.49, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (100.476, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (274.378, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for OxygenButadiene calculated by Duminda Ranasinghe""",
    longDesc = 
u"""
Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7
""",
)


entry(
    index = 5,
    label = "S_266",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {7,S} {8,S}
2  C u0 p0 c0 {1,D} {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  O u0 p2 c0 {4,S} {6,S}
6  O u0 p2 c0 {3,S} {5,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.84278, 0.0203949, 4.21572e-05, -7.13806e-08, 3.06437e-11, 6090.15, 10.1933],
                Tmin = (10, 'K'),
                Tmax = (819.351, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.48331, 0.0389355, -2.25153e-05, 6.24376e-09, -6.70083e-13, 5585.61, 8.41752],
                Tmin = (819.351, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (50.6545, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (278.535, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for OxygenButadiene calculated by Duminda Ranasinghe""",
    longDesc = 
u"""
Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7
""",
)


entry(
    index = 6,
    label = "CH2O_532",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.03246, -0.00198028, 9.28305e-06, 2.8046e-09, -8.13721e-12, -14633.1, 3.47498],
                Tmin = (10, 'K'),
                Tmax = (594.53, 'K'),
            ),
            NASAPolynomial(
                coeffs = [1.39062, 0.00965766, -4.59749e-06, 1.00884e-09, -8.19939e-14, -14210.5, 15.7586],
                Tmin = (594.53, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-121.655, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (83.1447, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for OxygenButadiene calculated by Duminda Ranasinghe""",
    longDesc = 
u"""
Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7
""",
)


entry(
    index = 7,
    label = "C3H4O_611",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 C u0 p0 c0 {2,S} {4,D} {8,S}
4 O u0 p2 c0 {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.97535, 0.00167095, 8.69742e-05, -1.7792e-07, 1.19614e-10, -9468.06, 7.19279],
                Tmin = (10, 'K'),
                Tmax = (381.324, 'K'),
            ),
            NASAPolynomial(
                coeffs = [1.43923, 0.0282903, -1.78002e-05, 5.36624e-09, -6.22796e-13, -9274.76, 16.9815],
                Tmin = (381.324, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-78.7229, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (178.761, 'J/(mol*K)'),
    ),
    shortDesc = u"""library value for OxygenButadiene calculated by Duminda Ranasinghe""",
    longDesc = 
u"""
Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7
""",
)

