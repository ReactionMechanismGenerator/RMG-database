#!/usr/bin/env python
# encoding: utf-8

name = "Nitrogen_G4"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "NNCDC",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {3,S} {5,S}
2  N u0 p1 c0 {1,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {3,D} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95908,0.00252047,9.87724e-05,-1.83451e-07,1.09073e-10,18311,8.03497], Tmin=(10,'K'), Tmax=(497.267,'K')),
            NASAPolynomial(coeffs=[0.741341,0.0354405,-2.17566e-05,6.59401e-09,-7.7814e-13,18544,20.4359], Tmin=(497.267,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (152.233,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 1,
    label = "[O-][NH+]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p3 c-1 {3,S}
3 N u1 p0 c+1 {1,S} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97751,0.00132462,3.78567e-05,-6.96994e-08,3.98938e-11,-1400.4,7.36563], Tmin=(10,'K'), Tmax=(549.531,'K')),
            NASAPolynomial(coeffs=[2.96908,0.0135036,-8.5944e-06,2.6756e-09,-3.21277e-13,-1362.62,10.9623], Tmin=(549.531,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-11.6527,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 2,
    label = "[CH2]NCDC",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {3,S} {5,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u1 p0 c0 {1,S} {7,S} {8,S}
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
            NASAPolynomial(coeffs=[3.92297,0.00494619,0.000113134,-2.41664e-07,1.60365e-10,24499.1,8.17198], Tmin=(10,'K'), Tmax=(486.036,'K')),
            NASAPolynomial(coeffs=[2.47295,0.0323862,-1.94067e-05,5.77604e-09,-6.73592e-13,24456.9,12.2372], Tmin=(486.036,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (203.679,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 3,
    label = "CNDNC",
    molecule = 
"""
1  N u0 p1 c0 {2,D} {3,S}
2  N u0 p1 c0 {1,D} {4,S}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82697,0.0150324,2.11514e-05,-3.09246e-08,1.11705e-11,16548.4,5.27341], Tmin=(10,'K'), Tmax=(939.065,'K')),
            NASAPolynomial(coeffs=[1.70834,0.0314162,-1.67744e-05,4.34539e-09,-4.40869e-13,16621.8,13.6336], Tmin=(939.065,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (137.581,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 4,
    label = "N[N]CDN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {6,S} {7,S}
2 N u1 p1 c0 {1,S} {4,S}
3 N u0 p1 c0 {4,D} {8,S}
4 C u0 p0 c0 {2,S} {3,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95184,0.00289881,7.86701e-05,-1.5017e-07,8.91412e-11,30587,8.67285], Tmin=(10,'K'), Tmax=(532.848,'K')),
            NASAPolynomial(coeffs=[2.16183,0.0265553,-1.6692e-05,5.13306e-09,-6.10349e-13,30632.6,14.8204], Tmin=(532.848,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (254.297,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 5,
    label = "NNDCO",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {8,S}
2 N u0 p1 c0 {3,S} {6,S} {7,S}
3 N u0 p1 c0 {2,S} {4,D}
4 C u0 p0 c0 {1,S} {3,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9768,0.00148067,7.71915e-05,-1.44877e-07,8.86853e-11,-6608.89,8.44743], Tmin=(10,'K'), Tmax=(420.545,'K')),
            NASAPolynomial(coeffs=[1.1833,0.0280516,-1.7584e-05,5.36856e-09,-6.33105e-13,-6373.94,19.5046], Tmin=(420.545,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-54.9548,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 6,
    label = "NCCN",
    molecule = 
"""
1  N u0 p1 c0 {3,S} {9,S} {10,S}
2  N u0 p1 c0 {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90415,0.00756405,8.49426e-05,-1.46404e-07,8.01403e-11,-4637.84,7.94375], Tmin=(10,'K'), Tmax=(472.796,'K')),
            NASAPolynomial(coeffs=[-0.135451,0.0417401,-2.34838e-05,6.48127e-09,-7.0023e-13,-4255.86,24.4065], Tmin=(472.796,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-38.5807,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 7,
    label = "[O-][NH+]DCDCD[N]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {4,D} {6,S}
3 N u1 p1 c0 {5,D}
4 C u0 p0 c0 {2,D} {5,D}
5 C u0 p0 c0 {3,D} {4,D}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78883,0.0182414,-9.36249e-06,-1.24356e-09,1.95949e-12,58244.3,9.98905], Tmin=(10,'K'), Tmax=(897.222,'K')),
            NASAPolynomial(coeffs=[5.52096,0.0140436,-8.23648e-06,2.29777e-09,-2.47134e-13,57791.7,1.02988], Tmin=(897.222,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (484.252,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 8,
    label = "CDCCDN",
    molecule = 
"""
1 N u0 p1 c0 {3,D} {9,S}
2 C u0 p0 c0 {3,S} {4,D} {5,S}
3 C u0 p0 c0 {1,D} {2,S} {6,S}
4 C u0 p0 c0 {2,D} {7,S} {8,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96868,0.00182756,7.78209e-05,-1.31404e-07,7.1648e-11,14707.6,8.01836], Tmin=(10,'K'), Tmax=(474.439,'K')),
            NASAPolynomial(coeffs=[0.299034,0.0327556,-1.99277e-05,5.90052e-09,-6.77892e-13,15055.9,22.9874], Tmin=(474.439,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (122.271,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 9,
    label = "[CH2]NDCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {8,S}
2 N u0 p1 c0 {3,D} {4,S}
3 C u0 p0 c0 {1,S} {2,D} {5,S}
4 C u1 p0 c0 {2,S} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94366,0.00339743,8.22953e-05,-1.60716e-07,9.66552e-11,508.159,7.78519], Tmin=(10,'K'), Tmax=(535.602,'K')),
            NASAPolynomial(coeffs=[2.46351,0.0266347,-1.69027e-05,5.22518e-09,-6.23466e-13,491.965,12.3706], Tmin=(535.602,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (4.20443,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 10,
    label = "[NH]CDNO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 N u0 p1 c0 {1,S} {4,D}
3 N u1 p1 c0 {4,S} {6,S}
4 C u0 p0 c0 {2,D} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95726,0.0025049,6.67564e-05,-1.23887e-07,7.08315e-11,17598.6,8.59008], Tmin=(10,'K'), Tmax=(556.959,'K')),
            NASAPolynomial(coeffs=[2.32869,0.023616,-1.54564e-05,4.87047e-09,-5.87158e-13,17634,14.1829], Tmin=(556.959,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (146.305,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 11,
    label = "[CH2]NO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 N u0 p1 c0 {1,S} {3,S} {4,S}
3 C u1 p0 c0 {2,S} {5,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95121,0.00299387,6.64419e-05,-1.34492e-07,8.3729e-11,14198,6.74024], Tmin=(10,'K'), Tmax=(524.275,'K')),
            NASAPolynomial(coeffs=[3.11978,0.0198798,-1.20335e-05,3.65276e-09,-4.34629e-13,14140.3,8.83272], Tmin=(524.275,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (118.033,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 12,
    label = "[O-][N+]DCC",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u1 p0 c+1 {1,S} {4,D}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {2,D} {3,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94304,0.0114132,1.83195e-05,-2.67976e-08,9.67914e-12,12221,7.92891], Tmin=(10,'K'), Tmax=(987.735,'K')),
            NASAPolynomial(coeffs=[3.82411,0.0213743,-1.12036e-05,2.84528e-09,-2.82874e-13,11782.1,6.1604], Tmin=(987.735,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (101.639,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 13,
    label = "OONDC",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {7,S}
3 N u0 p1 c0 {1,S} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93551,0.0039034,7.47837e-05,-1.53772e-07,9.50508e-11,8746.05,8.1115], Tmin=(10,'K'), Tmax=(540.933,'K')),
            NASAPolynomial(coeffs=[3.43937,0.0217861,-1.42199e-05,4.4966e-09,-5.45499e-13,8591.78,8.27807], Tmin=(540.933,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (72.6956,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 14,
    label = "OCCD[N]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {8,S}
2 N u1 p1 c0 {4,D}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {2,D} {3,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.874,0.0108203,3.48182e-05,-6.64438e-08,3.5704e-11,4958.99,9.02167], Tmin=(10,'K'), Tmax=(582.824,'K')),
            NASAPolynomial(coeffs=[2.37781,0.0256874,-1.52801e-05,4.39896e-09,-4.90676e-13,5055.3,14.7622], Tmin=(582.824,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (41.2153,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 15,
    label = "CDC[C]DN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {4,D} {8,S}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {2,D} {6,S} {7,S}
4 C u1 p0 c0 {1,D} {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93328,0.00406401,8.53279e-05,-1.7334e-07,1.0725e-10,36396.1,8.47809], Tmin=(10,'K'), Tmax=(532.275,'K')),
            NASAPolynomial(coeffs=[3.01321,0.0255131,-1.6078e-05,4.97169e-09,-5.95805e-13,36288.2,10.4026], Tmin=(532.275,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (302.591,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 16,
    label = "[CH2]OCN",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  N u0 p1 c0 {3,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4  C u1 p0 c0 {1,S} {9,S} {10,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92136,0.00615687,0.000103019,-2.40254e-07,1.84408e-10,-2009.35,8.53619], Tmin=(10,'K'), Tmax=(332.145,'K')),
            NASAPolynomial(coeffs=[1.66934,0.0332776,-1.94598e-05,5.57701e-09,-6.23038e-13,-1859.75,16.9188], Tmin=(332.145,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-16.7109,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 17,
    label = "NN[CH]N",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {4,S} {6,S}
2  N u0 p1 c0 {1,S} {7,S} {8,S}
3  N u0 p1 c0 {4,S} {9,S} {10,S}
4  C u1 p0 c0 {1,S} {3,S} {5,S}
5  H u0 p0 c0 {4,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9313,0.00437607,0.00010886,-2.26553e-07,1.47437e-10,30622,9.17131], Tmin=(10,'K'), Tmax=(489.361,'K')),
            NASAPolynomial(coeffs=[2.18555,0.0324354,-1.94164e-05,5.78389e-09,-6.74483e-13,30627.8,14.6589], Tmin=(489.361,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (254.589,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 18,
    label = "NNDO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 N u0 p1 c0 {3,S} {4,S} {5,S}
3 N u0 p1 c0 {1,D} {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06237,-0.00495473,4.79141e-05,-7.17148e-08,3.53141e-11,7810.2,6.49608], Tmin=(10,'K'), Tmax=(625.711,'K')),
            NASAPolynomial(coeffs=[2.34649,0.0119777,-6.97324e-06,1.99644e-09,-2.22455e-13,7908.19,13.0369], Tmin=(625.711,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (64.9414,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (99.7737,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 19,
    label = "NO[CH]N",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 N u0 p1 c0 {4,S} {6,S} {7,S}
3 N u0 p1 c0 {1,S} {8,S} {9,S}
4 C u1 p0 c0 {1,S} {2,S} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94758,0.00490034,0.000144691,-4.84598e-07,5.54305e-10,16606.8,9.13711], Tmin=(10,'K'), Tmax=(220.666,'K')),
            NASAPolynomial(coeffs=[2.63181,0.028751,-1.74347e-05,5.20484e-09,-6.04116e-13,16664.9,13.4967], Tmin=(220.666,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (138.094,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 20,
    label = "OON[O]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {6,S}
3 O u1 p2 c0 {4,S}
4 N u0 p1 c0 {1,S} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90256,0.00769542,6.37566e-05,-1.85789e-07,1.57609e-10,7628.59,9.24395], Tmin=(10,'K'), Tmax=(401.294,'K')),
            NASAPolynomial(coeffs=[3.95505,0.0175169,-1.16222e-05,3.67443e-09,-4.42154e-13,7541.08,8.00085], Tmin=(401.294,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (63.4298,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 21,
    label = "NDCC#N",
    molecule = 
"""
1 N u0 p1 c0 {3,D} {6,S}
2 N u0 p1 c0 {4,T}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 C u0 p0 c0 {2,T} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9746,0.00170452,5.88272e-05,-1.24942e-07,8.54482e-11,26806.8,7.77777], Tmin=(10,'K'), Tmax=(436.211,'K')),
            NASAPolynomial(coeffs=[2.65612,0.0178957,-1.09514e-05,3.25319e-09,-3.74588e-13,26882.8,12.5976], Tmin=(436.211,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (222.882,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 22,
    label = "ODCC#N",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 N u0 p1 c0 {4,T}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 C u0 p0 c0 {2,T} {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96934,0.00261955,6.5288e-05,-2.07784e-07,2.14694e-10,4465.08,7.65968], Tmin=(10,'K'), Tmax=(298.165,'K')),
            NASAPolynomial(coeffs=[3.4956,0.0130844,-8.0315e-06,2.37417e-09,-2.71959e-13,4475.07,9.06563], Tmin=(298.165,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (37.1324,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 23,
    label = "NCDCD[CH]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {2,D} {4,D}
4 C u1 p0 c0 {3,D} {8,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88619,0.00758362,0.000101492,-2.5731e-07,1.90383e-10,40451.5,8.46324], Tmin=(10,'K'), Tmax=(473.645,'K')),
            NASAPolynomial(coeffs=[4.94607,0.02115,-1.27825e-05,3.90541e-09,-4.6971e-13,40098.6,1.47564], Tmin=(473.645,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (336.313,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 24,
    label = "C#CC#N",
    molecule = 
"""
1 N u0 p1 c0 {4,T}
2 C u0 p0 c0 {3,T} {4,S}
3 C u0 p0 c0 {2,T} {5,S}
4 C u0 p0 c0 {1,T} {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44137,0.00361554,5.06556e-05,-1.15008e-07,7.56004e-11,43385.3,6.9665], Tmin=(10,'K'), Tmax=(534.508,'K')),
            NASAPolynomial(coeffs=[4.09268,0.0115513,-7.56337e-06,2.44283e-09,-3.04942e-13,43132.7,2.52052], Tmin=(534.508,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (360.707,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (103.931,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 25,
    label = "N[NH]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u1 p1 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04873,-0.0043072,4.08716e-05,-4.52562e-08,2.92945e-12,25804.4,5.29754], Tmin=(10,'K'), Tmax=(351.866,'K')),
            NASAPolynomial(coeffs=[2.14536,0.0120565,-6.40465e-06,1.72103e-09,-1.83909e-13,25971,12.956], Tmin=(351.866,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (214.548,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 26,
    label = "[O-][CH][NH+]DC",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 N u0 p0 c+1 {3,S} {4,D} {5,S}
3 C u1 p0 c0 {1,S} {2,S} {6,S}
4 C u0 p0 c0 {2,D} {7,S} {8,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93605,0.00450774,9.64916e-05,-2.34871e-07,1.79129e-10,-3598.37,8.76827], Tmin=(10,'K'), Tmax=(419.979,'K')),
            NASAPolynomial(coeffs=[2.97736,0.0246629,-1.4869e-05,4.40303e-09,-5.08208e-13,-3615.07,11.4042], Tmin=(419.979,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-29.9203,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 27,
    label = "[NH-][N+]DCC",
    molecule = 
"""
multiplicity 2
1 N u1 p0 c+1 {2,S} {4,D}
2 N u0 p2 c-1 {1,S} {9,S}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,D} {3,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86704,0.011943,3.37532e-05,-5.62875e-08,2.58089e-11,32635.1,8.11836], Tmin=(10,'K'), Tmax=(704.999,'K')),
            NASAPolynomial(coeffs=[2.02517,0.0289989,-1.65906e-05,4.60945e-09,-4.98647e-13,32730.7,15.1962], Tmin=(704.999,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (271.331,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 28,
    label = "CNO[NH]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {4,S} {8,S}
3 N u1 p1 c0 {1,S} {9,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88383,0.0102779,4.73078e-05,-8.91407e-08,5.05137e-11,27954,8.15147], Tmin=(10,'K'), Tmax=(461.501,'K')),
            NASAPolynomial(coeffs=[1.56627,0.0303652,-1.79814e-05,5.17435e-09,-5.78112e-13,28167.9,17.5402], Tmin=(461.501,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (232.412,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 29,
    label = "ONC#[C]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 N u0 p1 c0 {1,S} {3,S} {5,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u1 p0 c0 {3,T}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88631,0.00904051,8.20181e-05,-2.87689e-07,2.83135e-10,60030.6,8.55373], Tmin=(10,'K'), Tmax=(365.956,'K')),
            NASAPolynomial(coeffs=[4.90154,0.0146109,-9.13036e-06,2.80931e-09,-3.35168e-13,59844.7,3.15153], Tmin=(365.956,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (499.136,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 30,
    label = "COO[NH]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u1 p1 c0 {2,S} {8,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85258,0.0217923,-1.08811e-05,2.15238e-09,-6.33547e-14,17293.3,8.54804], Tmin=(10,'K'), Tmax=(1691.81,'K')),
            NASAPolynomial(coeffs=[12.5435,0.00579403,-7.30805e-07,-2.57743e-10,5.78843e-14,13701.4,-39.8747], Tmin=(1691.81,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (143.754,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 31,
    label = "N[CH]NDC",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {6,S} {7,S}
2 N u0 p1 c0 {3,S} {4,D}
3 C u1 p0 c0 {1,S} {2,S} {5,S}
4 C u0 p0 c0 {2,D} {8,S} {9,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93006,0.00434695,9.75801e-05,-2.006e-07,1.27047e-10,22222.6,8.46043], Tmin=(10,'K'), Tmax=(512.97,'K')),
            NASAPolynomial(coeffs=[2.64462,0.0291002,-1.78738e-05,5.42309e-09,-6.41137e-13,22160.6,11.9149], Tmin=(512.97,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (184.747,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 32,
    label = "[O-][NH+]DNNN",
    molecule = 
"""
1 O u0 p3 c-1 {4,S}
2 N u0 p1 c0 {3,S} {5,S} {6,S}
3 N u0 p1 c0 {2,S} {7,S} {8,S}
4 N u0 p0 c+1 {1,S} {5,D} {9,S}
5 N u0 p1 c0 {2,S} {4,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93458,0.00447824,0.000108912,-2.46302e-07,1.75656e-10,32422.9,9.42328], Tmin=(10,'K'), Tmax=(437.885,'K')),
            NASAPolynomial(coeffs=[2.2066,0.0311235,-1.95656e-05,5.94201e-09,-6.93984e-13,32470.1,15.1439], Tmin=(437.885,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (269.573,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 33,
    label = "NO[CH]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,S} {8,S}
3 N u0 p1 c0 {1,S} {6,S} {7,S}
4 C u1 p0 c0 {1,S} {2,S} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93667,0.0041006,8.9053e-05,-1.93788e-07,1.30292e-10,-5879.87,9.23289], Tmin=(10,'K'), Tmax=(481.575,'K')),
            NASAPolynomial(coeffs=[2.87278,0.0253425,-1.57501e-05,4.78587e-09,-5.62437e-13,-5921.24,12.0947], Tmin=(481.575,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-48.9022,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 34,
    label = "NNDN",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {2,D} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07767,-0.00702896,8.26447e-05,-1.42172e-07,8.09268e-11,25820,6.5404], Tmin=(10,'K'), Tmax=(539.865,'K')),
            NASAPolynomial(coeffs=[1.94294,0.0176208,-1.03861e-05,3.01567e-09,-3.40952e-13,25921.8,14.3312], Tmin=(539.865,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (214.677,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 35,
    label = "NN[CH]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {9,S}
2 N u0 p1 c0 {3,S} {4,S} {5,S}
3 N u0 p1 c0 {2,S} {7,S} {8,S}
4 C u1 p0 c0 {1,S} {2,S} {6,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94235,0.00345352,9.05192e-05,-1.72639e-07,1.02106e-10,8523.1,9.04357], Tmin=(10,'K'), Tmax=(538.388,'K')),
            NASAPolynomial(coeffs=[2.00212,0.0303081,-1.89578e-05,5.8377e-09,-6.96707e-13,8551.73,15.5284], Tmin=(538.388,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (70.8433,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 36,
    label = "CDNCD[CH]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,D}
2 C u0 p0 c0 {1,S} {4,D} {5,S}
3 C u0 p0 c0 {1,D} {6,S} {7,S}
4 C u1 p0 c0 {2,D} {8,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96188,0.00239317,8.17833e-05,-1.59327e-07,9.8701e-11,49621.9,8.64533], Tmin=(10,'K'), Tmax=(487.614,'K')),
            NASAPolynomial(coeffs=[1.72974,0.0276398,-1.72165e-05,5.19613e-09,-6.06156e-13,49757.1,16.9655], Tmin=(487.614,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (412.569,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 37,
    label = "OOND[CH]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {6,S}
3 N u0 p1 c0 {1,S} {4,D}
4 C u1 p0 c0 {3,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9034,0.0063564,7.65553e-05,-1.95347e-07,1.4238e-10,35746.2,8.81886], Tmin=(10,'K'), Tmax=(486.993,'K')),
            NASAPolynomial(coeffs=[5.0377,0.0158629,-1.07036e-05,3.47435e-09,-4.29573e-13,35412.5,1.87097], Tmin=(486.993,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (297.191,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 38,
    label = "[CH2]NDC",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,D}
2 C u1 p0 c0 {1,S} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0625,-0.0065238,0.000104704,-2.00079e-07,1.27908e-10,26353.3,6.53832], Tmin=(10,'K'), Tmax=(462.674,'K')),
            NASAPolynomial(coeffs=[1.49514,0.0228366,-1.37115e-05,4.01437e-09,-4.56022e-13,26514.2,16.1169], Tmin=(462.674,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (219.111,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 39,
    label = "[O-][N+]#CCD[CH]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {4,T}
3 C u0 p0 c0 {4,S} {5,D} {6,S}
4 C u0 p0 c0 {2,T} {3,S}
5 C u1 p0 c0 {3,D} {7,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85613,0.0118331,7.73718e-05,-2.46944e-07,2.23283e-10,57578.3,10.0224], Tmin=(10,'K'), Tmax=(383.271,'K')),
            NASAPolynomial(coeffs=[4.18223,0.0218833,-1.46145e-05,4.64316e-09,-5.60975e-13,57454.5,7.47275], Tmin=(383.271,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (478.741,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 40,
    label = "[CH2]NN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {5,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96761,0.00202246,7.29254e-05,-1.39223e-07,8.52136e-11,29973.2,6.71204], Tmin=(10,'K'), Tmax=(490.195,'K')),
            NASAPolynomial(coeffs=[1.9079,0.0247245,-1.45811e-05,4.31769e-09,-5.03738e-13,30104.3,14.4581], Tmin=(490.195,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (249.202,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 41,
    label = "N[C]DNO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {7,S}
2 N u0 p1 c0 {4,S} {5,S} {6,S}
3 N u0 p1 c0 {1,S} {4,D}
4 C u1 p0 c0 {2,S} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89533,0.00726721,8.98656e-05,-2.43735e-07,1.91891e-10,26109.8,8.45689], Tmin=(10,'K'), Tmax=(446.28,'K')),
            NASAPolynomial(coeffs=[4.80542,0.0182428,-1.13317e-05,3.50021e-09,-4.20588e-13,25838.1,2.66589], Tmin=(446.28,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (217.08,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 42,
    label = "NNDCN",
    molecule = 
"""
1 N u0 p1 c0 {4,S} {6,S} {7,S}
2 N u0 p1 c0 {3,S} {8,S} {9,S}
3 N u0 p1 c0 {2,S} {4,D}
4 C u0 p0 c0 {1,S} {3,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95197,0.00288577,8.70514e-05,-1.62661e-07,9.53994e-11,15333.1,8.06925], Tmin=(10,'K'), Tmax=(530.163,'K')),
            NASAPolynomial(coeffs=[1.63277,0.0303263,-1.87168e-05,5.71278e-09,-6.78362e-13,15439.3,16.4686], Tmin=(530.163,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (127.469,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 43,
    label = "NCCO",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {11,S}
2  N u0 p1 c0 {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96099,0.00239275,0.000103794,-1.8686e-07,1.09899e-10,-27323,8.66387], Tmin=(10,'K'), Tmax=(437.377,'K')),
            NASAPolynomial(coeffs=[-0.0856923,0.0394079,-2.31728e-05,6.70168e-09,-7.57846e-13,-26969,24.8396], Tmin=(437.377,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-227.191,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 44,
    label = "[O-][NH+]DN[CH]N",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {5,S} {7,S} {8,S}
3 N u0 p0 c+1 {1,S} {4,D} {9,S}
4 N u0 p1 c0 {3,D} {5,S}
5 C u1 p0 c0 {2,S} {4,S} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87741,0.0109504,0.000122047,-4.01293e-07,4.10081e-10,19559.8,10.3486], Tmin=(10,'K'), Tmax=(311.822,'K')),
            NASAPolynomial(coeffs=[3.18062,0.0301089,-1.92784e-05,5.96921e-09,-7.09895e-13,19553.5,12.1014], Tmin=(311.822,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (162.65,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 45,
    label = "[NH]NOO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {7,S}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 N u1 p1 c0 {3,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91423,0.00534196,8.17931e-05,-1.83366e-07,1.20784e-10,27140.1,8.99927], Tmin=(10,'K'), Tmax=(523.948,'K')),
            NASAPolynomial(coeffs=[4.35269,0.0202797,-1.33202e-05,4.26293e-09,-5.2332e-13,26843.2,4.77223], Tmin=(523.948,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (225.629,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 46,
    label = "N[N]CDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,S} {5,S} {6,S}
3 N u1 p1 c0 {2,S} {4,S}
4 C u0 p0 c0 {1,D} {3,S} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94796,0.0044333,7.52213e-05,-1.95776e-07,1.68159e-10,4630.31,8.80997], Tmin=(10,'K'), Tmax=(296.293,'K')),
            NASAPolynomial(coeffs=[2.64833,0.0219786,-1.36027e-05,4.08097e-09,-4.72598e-13,4707.32,13.4991], Tmin=(296.293,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (38.5043,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 47,
    label = "CO[NH]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u1 p1 c0 {1,S} {7,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91856,0.00749126,1.83064e-05,-2.49884e-08,9.24421e-12,13275,6.51533], Tmin=(10,'K'), Tmax=(884.436,'K')),
            NASAPolynomial(coeffs=[2.20624,0.0198901,-1.06162e-05,2.76323e-09,-2.82229e-13,13395.8,13.5369], Tmin=(884.436,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (110.373,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 48,
    label = "[O-][NH+]N",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u1 p0 c+1 {1,S} {3,S} {4,S}
3 N u0 p1 c0 {2,S} {5,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92317,0.00777843,9.75872e-06,-1.51126e-08,5.62737e-12,15994.7,7.73501], Tmin=(10,'K'), Tmax=(930.528,'K')),
            NASAPolynomial(coeffs=[3.26821,0.014584,-7.64373e-06,1.96332e-09,-1.98362e-13,15943.9,9.91947], Tmin=(930.528,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (132.988,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 49,
    label = "[CH2]CC#N",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {4,T}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u1 p0 c0 {2,S} {7,S} {8,S}
4 C u0 p0 c0 {1,T} {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88823,0.0112293,8.85546e-05,-3.73926e-07,5.24136e-10,30361.3,8.43843], Tmin=(10,'K'), Tmax=(179.991,'K')),
            NASAPolynomial(coeffs=[3.33771,0.0234637,-1.34042e-05,3.71958e-09,-4.01314e-13,30381.2,10.1503], Tmin=(179.991,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (252.47,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 50,
    label = "C[C]DNN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {8,S} {9,S}
2 N u0 p1 c0 {1,S} {4,D}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u1 p0 c0 {2,D} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82061,0.0147088,3.94079e-05,-1.05566e-07,8.3138e-11,37598.7,7.70291], Tmin=(10,'K'), Tmax=(327.122,'K')),
            NASAPolynomial(coeffs=[2.86428,0.0264027,-1.42139e-05,3.71404e-09,-3.78442e-13,37661.3,11.248], Tmin=(327.122,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (312.589,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 51,
    label = "NCDCDC",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {4,D} {5,S}
3 C u0 p0 c0 {4,D} {8,S} {9,S}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94283,0.00362896,9.53792e-05,-1.95843e-07,1.26197e-10,23878.1,8.05136], Tmin=(10,'K'), Tmax=(490.027,'K')),
            NASAPolynomial(coeffs=[2.22086,0.0290917,-1.74798e-05,5.20044e-09,-6.05251e-13,23909.9,13.7332], Tmin=(490.027,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (198.519,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 52,
    label = "[NH]NCN",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {3,S} {4,S} {7,S}
2  N u0 p1 c0 {4,S} {8,S} {9,S}
3  N u1 p1 c0 {1,S} {10,S}
4  C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95347,0.0030934,0.000109568,-2.2878e-07,1.54281e-10,25236.8,9.36825], Tmin=(10,'K'), Tmax=(442.049,'K')),
            NASAPolynomial(coeffs=[1.43735,0.0335538,-1.9896e-05,5.83494e-09,-6.69673e-13,25384.1,18.6029], Tmin=(442.049,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (209.825,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 53,
    label = "NCC#N",
    molecule = 
"""
1 N u0 p1 c0 {3,S} {7,S} {8,S}
2 N u0 p1 c0 {4,T}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {2,T} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97488,0.00188417,9.40918e-05,-2.22754e-07,1.77152e-10,12601.6,8.17012], Tmin=(10,'K'), Tmax=(319.564,'K')),
            NASAPolynomial(coeffs=[2.12397,0.0250571,-1.47031e-05,4.2604e-09,-4.8395e-13,12719.9,14.9877], Tmin=(319.564,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (104.782,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 54,
    label = "[N-]([N+]DC)C",
    molecule = 
"""
multiplicity 2
1 N u0 p2 c-1 {2,S} {3,S}
2 N u1 p0 c+1 {1,S} {4,D}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {2,D} {8,S} {9,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91042,0.0151677,1.39523e-05,-2.22078e-08,7.74355e-12,35751.6,7.57416], Tmin=(10,'K'), Tmax=(1059.79,'K')),
            NASAPolynomial(coeffs=[4.4005,0.0233274,-1.17638e-05,2.88106e-09,-2.77094e-13,35085.7,2.52938], Tmin=(1059.79,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (297.282,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 55,
    label = "C[N]CDN",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {3,S} {4,S}
2 N u0 p1 c0 {4,D} {9,S}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {2,D} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94075,0.0111073,2.85545e-05,-3.99685e-08,1.48938e-11,26519.4,7.51792], Tmin=(10,'K'), Tmax=(925.141,'K')),
            NASAPolynomial(coeffs=[2.91752,0.0265173,-1.42431e-05,3.70763e-09,-3.773e-13,26238.6,9.83394], Tmin=(925.141,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (220.523,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 56,
    label = "O[N]NDC",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {7,S}
2 N u0 p1 c0 {3,S} {4,D}
3 N u1 p1 c0 {1,S} {2,S}
4 C u0 p0 c0 {2,D} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95238,0.00277643,6.8457e-05,-1.27995e-07,7.31539e-11,24229.9,8.47816], Tmin=(10,'K'), Tmax=(564.788,'K')),
            NASAPolynomial(coeffs=[2.51115,0.0237199,-1.56801e-05,4.97714e-09,-6.03512e-13,24221.5,13.0919], Tmin=(564.788,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (201.439,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 57,
    label = "NNDCD[CH]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 N u0 p1 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,D}
4 C u1 p0 c0 {3,D} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91099,0.00559213,8.09396e-05,-1.8626e-07,1.25297e-10,54424.1,8.21265], Tmin=(10,'K'), Tmax=(518.177,'K')),
            NASAPolynomial(coeffs=[4.67581,0.0186612,-1.18147e-05,3.73461e-09,-4.59273e-13,54090.2,2.56777], Tmin=(518.177,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (452.482,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 58,
    label = "CDNC#C",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {3,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {3,T} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94519,0.00338534,7.16842e-05,-1.47953e-07,9.33529e-11,42025,7.41184], Tmin=(10,'K'), Tmax=(520.287,'K')),
            NASAPolynomial(coeffs=[3.16915,0.0210751,-1.31152e-05,4.01244e-09,-4.77285e-13,41947,9.12382], Tmin=(520.287,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (349.398,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 59,
    label = "ONNO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {7,S}
2 O u0 p2 c0 {4,S} {8,S}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 N u0 p1 c0 {2,S} {3,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9373,0.00366353,8.03406e-05,-1.53659e-07,8.91378e-11,-2599.78,7.54877], Tmin=(10,'K'), Tmax=(567.472,'K')),
            NASAPolynomial(coeffs=[2.80931,0.0260362,-1.6918e-05,5.38493e-09,-6.58965e-13,-2703.96,10.3056], Tmin=(567.472,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-21.6417,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 60,
    label = "CONDN",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {2,D} {8,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77847,0.0245464,-8.01537e-05,2.29195e-07,-2.12505e-10,9894.26,7.18602], Tmin=(10,'K'), Tmax=(404.391,'K')),
            NASAPolynomial(coeffs=[1.63733,0.0264088,-1.54114e-05,4.34254e-09,-4.74657e-13,10225.4,17.5301], Tmin=(404.391,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (82.2564,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 61,
    label = "C[CH]N",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {8,S} {9,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u1 p0 c0 {1,S} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96635,0.00221155,8.46179e-05,-1.68718e-07,1.11707e-10,12100.6,6.71409], Tmin=(10,'K'), Tmax=(385.496,'K')),
            NASAPolynomial(coeffs=[1.49154,0.0278964,-1.5346e-05,4.19405e-09,-4.5389e-13,12291.4,16.294], Tmin=(385.496,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (100.602,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 62,
    label = "[O-][NH+]DCC[O]",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {4,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {2,S} {5,D} {9,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 C u0 p0 c0 {3,D} {4,S} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86274,0.0166453,2.44823e-05,-4.488e-08,1.94667e-11,10172.4,10.7281], Tmin=(10,'K'), Tmax=(829.153,'K')),
            NASAPolynomial(coeffs=[4.04584,0.0273483,-1.58407e-05,4.39406e-09,-4.71457e-13,9743.75,7.47738], Tmin=(829.153,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (84.5882,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 63,
    label = "[NH]CDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 N u1 p1 c0 {3,S} {5,S}
3 C u0 p0 c0 {1,D} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04723,-0.00439297,6.19388e-05,-1.07209e-07,6.06025e-11,6779.68,7.20496], Tmin=(10,'K'), Tmax=(548.751,'K')),
            NASAPolynomial(coeffs=[2.46434,0.0143247,-8.85058e-06,2.6333e-09,-3.01576e-13,6845.3,12.9066], Tmin=(548.751,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (56.3655,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 64,
    label = "[O-][NH+]DCO[O]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p3 c-1 {4,S}
3 O u1 p2 c0 {1,S}
4 N u0 p0 c+1 {2,S} {5,D} {7,S}
5 C u0 p0 c0 {1,S} {4,D} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92687,0.00448195,8.27826e-05,-1.74383e-07,1.09839e-10,14884.4,9.92474], Tmin=(10,'K'), Tmax=(531.711,'K')),
            NASAPolynomial(coeffs=[3.41684,0.0239662,-1.63263e-05,5.22732e-09,-6.33132e-13,14717.5,9.9832], Tmin=(531.711,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (123.731,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 65,
    label = "CO[CH]N",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  N u0 p1 c0 {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4  C u1 p0 c0 {1,S} {2,S} {8,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82669,0.020315,5.26756e-06,-1.38467e-08,4.82411e-12,-2528.5,7.89128], Tmin=(10,'K'), Tmax=(1145.68,'K')),
            NASAPolynomial(coeffs=[5.0523,0.0247549,-1.19608e-05,2.82093e-09,-2.62421e-13,-3381.55,-0.685575], Tmin=(1145.68,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-21.0194,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 66,
    label = "CN[CH]N",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {3,S} {4,S} {8,S}
2  N u0 p1 c0 {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4  C u1 p0 c0 {1,S} {2,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77274,0.0192126,2.56839e-05,-4.99871e-08,2.45986e-11,17154.4,8.08729], Tmin=(10,'K'), Tmax=(551.236,'K')),
            NASAPolynomial(coeffs=[1.44604,0.0360961,-2.0259e-05,5.57659e-09,-6.01132e-13,17410.9,17.9265], Tmin=(551.236,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (142.605,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 67,
    label = "[CH2]OON",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u0 p1 c0 {2,S} {7,S} {8,S}
4 C u1 p0 c0 {1,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47395,0.0411768,-8.52767e-05,1.03805e-07,-4.78716e-11,-10398.1,9.32604], Tmin=(10,'K'), Tmax=(673.027,'K')),
            NASAPolynomial(coeffs=[4.98407,0.0199386,-1.06111e-05,2.77228e-09,-2.85873e-13,-10323.6,4.70188], Tmin=(673.027,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-86.5187,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 68,
    label = "NOC#N",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 N u0 p1 c0 {4,T}
4 C u0 p0 c0 {1,S} {3,T}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97606,0.00291121,0.000143817,-7.639e-07,1.43023e-09,20145.6,7.85965], Tmin=(10,'K'), Tmax=(134.057,'K')),
            NASAPolynomial(coeffs=[3.51414,0.0166948,-1.04212e-05,3.17776e-09,-3.74785e-13,20158,9.15989], Tmin=(134.057,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (167.786,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 69,
    label = "[CH2]OC#N",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 N u0 p1 c0 {4,T}
3 C u1 p0 c0 {1,S} {5,S} {6,S}
4 C u0 p0 c0 {1,S} {2,T}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92473,0.00518175,7.1852e-05,-1.871e-07,1.43747e-10,23919.9,7.73849], Tmin=(10,'K'), Tmax=(449.371,'K')),
            NASAPolynomial(coeffs=[4.30174,0.0157415,-9.84686e-06,3.01677e-09,-3.58709e-13,23745.6,4.65788], Tmin=(449.371,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (198.874,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 70,
    label = "CCNDN",
    molecule = 
"""
1  N u0 p1 c0 {2,D} {3,S}
2  N u0 p1 c0 {1,D} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97914,0.0108923,3.16677e-05,-4.00744e-08,1.37331e-11,15951.7,7.09003], Tmin=(10,'K'), Tmax=(1006.87,'K')),
            NASAPolynomial(coeffs=[2.795,0.0287995,-1.46791e-05,3.63619e-09,-3.53667e-13,15520.9,9.48755], Tmin=(1006.87,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (132.675,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 71,
    label = "CNNO",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {10,S}
2  N u0 p1 c0 {3,S} {4,S} {8,S}
3  N u0 p1 c0 {1,S} {2,S} {9,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  H u0 p0 c0 {4,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91137,0.00688719,8.2636e-05,-1.68461e-07,1.10654e-10,4392.97,7.49872], Tmin=(10,'K'), Tmax=(390.811,'K')),
            NASAPolynomial(coeffs=[1.31604,0.0334507,-1.93189e-05,5.45922e-09,-6.01737e-13,4595.83,17.5813], Tmin=(390.811,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (36.5111,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 72,
    label = "OND[C]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {4,S} {6,S}
3 N u0 p1 c0 {1,S} {4,D}
4 C u1 p0 c0 {2,S} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90353,0.00683979,7.60468e-05,-2.1512e-07,1.74536e-10,6452.85,8.41067], Tmin=(10,'K'), Tmax=(435.843,'K')),
            NASAPolynomial(coeffs=[4.76668,0.0153808,-1.00055e-05,3.16912e-09,-3.8504e-13,6221.25,3.16955], Tmin=(435.843,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (53.646,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 73,
    label = "[O-][NH+]DCC#C",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {6,S}
4 C u0 p0 c0 {3,S} {5,T}
5 C u0 p0 c0 {4,T} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90996,0.00589975,9.94498e-05,-2.31545e-07,1.62046e-10,34355.6,8.92674], Tmin=(10,'K'), Tmax=(480.801,'K')),
            NASAPolynomial(coeffs=[3.69459,0.0253205,-1.61375e-05,4.98546e-09,-5.93566e-13,34172.5,7.68907], Tmin=(480.801,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (285.63,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 74,
    label = "CD[N]",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06609,-0.00297109,2.14414e-05,-2.25841e-08,7.65911e-12,27367.8,3.89967], Tmin=(10,'K'), Tmax=(926.101,'K')),
            NASAPolynomial(coeffs=[2.41621,0.0085381,-4.2992e-06,1.05609e-09,-1.02113e-13,27485.4,10.7179], Tmin=(926.101,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (227.571,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 75,
    label = "CNNN",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {4,S} {8,S}
2  N u0 p1 c0 {1,S} {3,S} {9,S}
3  N u0 p1 c0 {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  H u0 p0 c0 {4,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82281,0.0151854,3.63085e-05,-5.92876e-08,2.6587e-11,23049.1,7.62177], Tmin=(10,'K'), Tmax=(689.685,'K')),
            NASAPolynomial(coeffs=[1.01484,0.036314,-2.01774e-05,5.49483e-09,-5.86272e-13,23321.2,19.2903], Tmin=(689.685,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (191.623,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 76,
    label = "NOO[NH]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 N u0 p1 c0 {1,S} {5,S} {6,S}
4 N u1 p1 c0 {2,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.31423,0.0635144,-0.000221266,3.70692e-07,-2.24864e-10,16328.8,10.3823], Tmin=(10,'K'), Tmax=(507.497,'K')),
            NASAPolynomial(coeffs=[6.84166,0.0132907,-6.55099e-06,1.57962e-09,-1.50161e-13,16259.5,-1.39834], Tmin=(507.497,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (135.744,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 77,
    label = "CCNDO",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8901,0.0118684,2.6931e-05,-3.94337e-08,1.52464e-11,3194.4,7.22271], Tmin=(10,'K'), Tmax=(876.231,'K')),
            NASAPolynomial(coeffs=[2.35967,0.0276449,-1.51242e-05,4.01199e-09,-4.15713e-13,3125.16,12.4784], Tmin=(876.231,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (26.5664,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 78,
    label = "CN[CH]O",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {10,S}
2  N u0 p1 c0 {3,S} {4,S} {8,S}
3  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
4  C u1 p0 c0 {1,S} {2,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79755,0.0173752,2.55911e-05,-5.20122e-08,2.71972e-11,-4255.23,8.20536], Tmin=(10,'K'), Tmax=(515.254,'K')),
            NASAPolynomial(coeffs=[1.84044,0.0325686,-1.86396e-05,5.21617e-09,-5.69862e-13,-4053.54,16.3496], Tmin=(515.254,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-35.4009,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 79,
    label = "[O-][N+]DCNDN",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {4,D} {5,S}
3 N u1 p0 c+1 {1,S} {5,D}
4 N u0 p1 c0 {2,D} {7,S}
5 C u0 p0 c0 {2,S} {3,D} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89691,0.00824316,5.37733e-05,-1.15436e-07,7.20518e-11,43461.8,9.85654], Tmin=(10,'K'), Tmax=(526.726,'K')),
            NASAPolynomial(coeffs=[3.11379,0.0233118,-1.51151e-05,4.63185e-09,-5.4083e-13,43417.7,11.9315], Tmin=(526.726,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (361.344,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 80,
    label = "[NH]CDN",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {3,S} {5,S}
2 N u0 p1 c0 {3,D} {6,S}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09228,-0.00772704,8.2429e-05,-1.3143e-07,6.84665e-11,28635.2,7.25661], Tmin=(10,'K'), Tmax=(600.37,'K')),
            NASAPolynomial(coeffs=[1.75167,0.0188688,-1.1506e-05,3.39982e-09,-3.87355e-13,28718,15.7033], Tmin=(600.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (238.087,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 81,
    label = "[N-]([N+]DO)O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {4,D}
3 N u0 p2 c-1 {1,S} {4,S}
4 N u1 p0 c+1 {2,D} {3,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94035,0.00392884,5.51918e-05,-1.34202e-07,9.5666e-11,19562.2,8.3462], Tmin=(10,'K'), Tmax=(483.332,'K')),
            NASAPolynomial(coeffs=[4.18111,0.0132759,-9.00817e-06,2.89048e-09,-3.51414e-13,19406.4,5.98951], Tmin=(483.332,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (162.637,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 82,
    label = "[O-][N+]DCNC",
    molecule = 
"""
multiplicity 2
1  O u0 p3 c-1 {3,S}
2  N u0 p1 c0 {4,S} {5,S} {9,S}
3  N u1 p0 c+1 {1,S} {5,D}
4  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {2,S} {3,D} {10,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86154,0.0226139,3.51983e-06,-1.39911e-08,5.11903e-12,16486.1,8.84187], Tmin=(10,'K'), Tmax=(1151.49,'K')),
            NASAPolynomial(coeffs=[6.72428,0.0233469,-1.13442e-05,2.6675e-09,-2.46102e-13,15119,-8.44673], Tmin=(1151.49,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (137.099,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 83,
    label = "NC[N]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {9,S}
2 N u0 p1 c0 {4,S} {7,S} {8,S}
3 N u1 p1 c0 {1,S} {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90188,0.00812233,7.81285e-05,-1.86693e-07,1.43825e-10,8375.81,9.3741], Tmin=(10,'K'), Tmax=(331.906,'K')),
            NASAPolynomial(coeffs=[2.14965,0.0292394,-1.73069e-05,4.99858e-09,-5.61069e-13,8492.12,15.895], Tmin=(331.906,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (69.6354,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 84,
    label = "NDC[C]DO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,D} {6,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 C u1 p0 c0 {1,D} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95032,0.00312147,6.17871e-05,-1.3212e-07,8.58358e-11,14857.4,8.49655], Tmin=(10,'K'), Tmax=(508.537,'K')),
            NASAPolynomial(coeffs=[3.42169,0.0175831,-1.12611e-05,3.48449e-09,-4.1489e-13,14777.9,9.37952], Tmin=(508.537,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (123.517,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 85,
    label = "N#N",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50362,-0.00017653,1.11829e-07,1.39779e-09,-9.51732e-13,-1039.52,3.10326], Tmin=(10,'K'), Tmax=(807.053,'K')),
            NASAPolynomial(coeffs=[3.06763,0.000928459,2.05963e-08,-1.47983e-10,2.92796e-14,-934.755,5.32623], Tmin=(807.053,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-8.64173,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 86,
    label = "ONDNO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {4,S} {6,S}
3 N u0 p1 c0 {1,S} {4,D}
4 N u0 p1 c0 {2,S} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94685,0.00305851,5.88632e-05,-1.13865e-07,6.54605e-11,-992.236,7.19294], Tmin=(10,'K'), Tmax=(586.029,'K')),
            NASAPolynomial(coeffs=[3.53339,0.018455,-1.2731e-05,4.19456e-09,-5.23244e-13,-1159.7,7.12445], Tmin=(586.029,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-8.2728,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 87,
    label = "CONDO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {1,S} {2,D}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85844,0.0144619,1.06873e-06,-7.46341e-09,2.75879e-12,-9320.46,7.03262], Tmin=(10,'K'), Tmax=(1153.35,'K')),
            NASAPolynomial(coeffs=[5.07848,0.0158001,-7.91526e-06,1.91654e-09,-1.81978e-13,-9972.32,-0.633306], Tmin=(1153.35,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-77.4992,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 88,
    label = "[O-][N+]#CN[CH2]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {4,S} {5,S} {6,S}
3 N u0 p0 c+1 {1,S} {5,T}
4 C u1 p0 c0 {2,S} {7,S} {8,S}
5 C u0 p0 c0 {2,S} {3,T}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79554,0.0175537,0.000128826,-5.38192e-07,6.07324e-10,45783.4,9.51701], Tmin=(10,'K'), Tmax=(326.585,'K')),
            NASAPolynomial(coeffs=[5.6467,0.0217211,-1.35927e-05,4.1806e-09,-4.98322e-13,45519.3,0.4664], Tmin=(326.585,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (380.694,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 89,
    label = "[O-][N+]#CO[CH2]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {2,S} {5,T}
4 C u1 p0 c0 {1,S} {6,S} {7,S}
5 C u0 p0 c0 {1,S} {3,T}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82386,0.0146755,0.000108933,-4.27836e-07,4.56032e-10,33019.1,8.90978], Tmin=(10,'K'), Tmax=(343.886,'K')),
            NASAPolynomial(coeffs=[5.41613,0.0193498,-1.26316e-05,3.97358e-09,-4.79335e-13,32772.4,0.93355], Tmin=(343.886,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (274.56,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 90,
    label = "CD[C]C#N",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {4,T}
2 C u0 p0 c0 {3,D} {5,S} {6,S}
3 C u1 p0 c0 {2,D} {4,S}
4 C u0 p0 c0 {1,T} {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78689,0.0205454,-3.54992e-05,5.80235e-08,-4.06984e-11,49525.5,8.95996], Tmin=(10,'K'), Tmax=(445.676,'K')),
            NASAPolynomial(coeffs=[3.88696,0.0162984,-9.93435e-06,2.92223e-09,-3.32063e-13,49549.9,8.9312], Tmin=(445.676,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (411.772,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 91,
    label = "C[N]CDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 N u1 p1 c0 {3,S} {4,S}
3 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,D} {2,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79406,0.0233675,-7.83916e-05,2.42084e-07,-2.36094e-10,3768.92,7.97563], Tmin=(10,'K'), Tmax=(391.784,'K')),
            NASAPolynomial(coeffs=[1.42044,0.0273761,-1.63037e-05,4.66851e-09,-5.16857e-13,4110.13,19.1838], Tmin=(391.784,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (31.3257,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 92,
    label = "C[C]DNO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {8,S}
2 N u0 p1 c0 {1,S} {4,D}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u1 p0 c0 {2,D} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94753,0.00678892,0.000264087,-1.77837e-06,3.96296e-09,22103.2,7.49592], Tmin=(10,'K'), Tmax=(143.407,'K')),
            NASAPolynomial(coeffs=[3.71999,0.0232378,-1.3632e-05,3.91228e-09,-4.37503e-13,22099.3,7.78957], Tmin=(143.407,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (184.94,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 93,
    label = "[NH]NCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {8,S}
2 N u0 p1 c0 {3,S} {4,S} {7,S}
3 N u1 p1 c0 {2,S} {9,S}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95228,0.00305282,9.48524e-05,-1.91753e-07,1.23201e-10,2516.89,9.36354], Tmin=(10,'K'), Tmax=(476.914,'K')),
            NASAPolynomial(coeffs=[1.77848,0.0301597,-1.83175e-05,5.46344e-09,-6.33843e-13,2623.31,17.1833], Tmin=(476.914,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (20.9154,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 94,
    label = "NCOO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {9,S}
3 N u0 p1 c0 {4,S} {7,S} {8,S}
4 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95723,0.00358694,0.000125445,-3.46052e-07,3.22148e-10,-17871.4,8.5464], Tmin=(10,'K'), Tmax=(272.208,'K')),
            NASAPolynomial(coeffs=[2.18499,0.0296291,-1.80579e-05,5.39948e-09,-6.26513e-13,-17774.9,14.7904], Tmin=(272.208,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-148.577,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 95,
    label = "N[C]DCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {8,S}
2 N u0 p1 c0 {4,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u1 p0 c0 {2,S} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93589,0.00453983,9.40343e-05,-2.26086e-07,1.70468e-10,12354.4,9.23524], Tmin=(10,'K'), Tmax=(421.304,'K')),
            NASAPolynomial(coeffs=[2.84175,0.0251197,-1.55238e-05,4.69611e-09,-5.49174e-13,12356.2,12.4946], Tmin=(421.304,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (102.719,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 96,
    label = "CNCDN",
    molecule = 
"""
1  N u0 p1 c0 {3,S} {4,S} {8,S}
2  N u0 p1 c0 {4,D} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {1,S} {2,D} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87317,0.0144872,2.28511e-05,-3.31565e-08,1.20629e-11,3638.23,7.24406], Tmin=(10,'K'), Tmax=(949.718,'K')),
            NASAPolynomial(coeffs=[2.50589,0.0294775,-1.54051e-05,3.93286e-09,-3.94622e-13,3481.62,11.578], Tmin=(949.718,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (30.2606,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 97,
    label = "[O-][NH+]DCDO",
    molecule = 
"""
1 O u0 p3 c-1 {3,S}
2 O u0 p2 c0 {4,D}
3 N u0 p0 c+1 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93348,0.00480765,5.81813e-05,-1.63722e-07,1.34699e-10,8375.29,7.95092], Tmin=(10,'K'), Tmax=(421.27,'K')),
            NASAPolynomial(coeffs=[4.25675,0.0125991,-8.23306e-06,2.57818e-09,-3.09097e-13,8251.68,5.52696], Tmin=(421.27,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (69.6347,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 98,
    label = "[CH]DN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {4,S}
2 C u1 p0 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03641,-0.0028299,2.03222e-05,-1.25596e-08,-6.97523e-12,31292.1,4.54663], Tmin=(10,'K'), Tmax=(425.165,'K')),
            NASAPolynomial(coeffs=[2.30566,0.00885597,-4.68693e-06,1.22342e-09,-1.25705e-13,31480.8,11.9049], Tmin=(425.165,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (260.178,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 99,
    label = "NCNO",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {10,S}
2  N u0 p1 c0 {1,S} {4,S} {7,S}
3  N u0 p1 c0 {4,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94887,0.0032839,0.000106017,-2.14061e-07,1.37979e-10,-6708.15,8.62532], Tmin=(10,'K'), Tmax=(472.31,'K')),
            NASAPolynomial(coeffs=[1.46866,0.033648,-2.01388e-05,5.9638e-09,-6.90014e-13,-6578.25,17.6254], Tmin=(472.31,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-55.7861,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 100,
    label = "NNDNN",
    molecule = 
"""
1 N u0 p1 c0 {3,S} {5,S} {6,S}
2 N u0 p1 c0 {4,S} {7,S} {8,S}
3 N u0 p1 c0 {1,S} {4,D}
4 N u0 p1 c0 {2,S} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94322,0.00343492,8.00226e-05,-1.57786e-07,9.57149e-11,33646.3,6.99872], Tmin=(10,'K'), Tmax=(534.611,'K')),
            NASAPolynomial(coeffs=[2.69701,0.0251406,-1.56186e-05,4.80067e-09,-5.73641e-13,33602.6,10.5757], Tmin=(534.611,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (279.731,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 101,
    label = "[O-][NH+]DNN[NH]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {4,S} {5,S} {6,S}
3 N u0 p0 c+1 {1,S} {4,D} {7,S}
4 N u0 p1 c0 {2,S} {3,D}
5 N u1 p1 c0 {2,S} {8,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93337,0.00398333,8.75063e-05,-1.72505e-07,1.03317e-10,49530,9.84086], Tmin=(10,'K'), Tmax=(546.905,'K')),
            NASAPolynomial(coeffs=[2.68199,0.027863,-1.83811e-05,5.80739e-09,-7.00475e-13,49446.6,13.1092], Tmin=(546.905,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (411.79,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 102,
    label = "[N]DNCDN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,D} {4,S}
2 N u0 p1 c0 {4,D} {6,S}
3 N u1 p1 c0 {1,D}
4 C u0 p0 c0 {1,S} {2,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89483,0.009234,1.86866e-05,-3.85873e-08,2.0396e-11,42102.9,8.63949], Tmin=(10,'K'), Tmax=(638.58,'K')),
            NASAPolynomial(coeffs=[3.41749,0.0168737,-1.01807e-05,2.95192e-09,-3.30293e-13,42069.1,9.98597], Tmin=(638.58,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (350.05,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 103,
    label = "CC#CN",
    molecule = 
"""
1 N u0 p1 c0 {4,S} {8,S} {9,S}
2 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {1,S} {3,T}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69394,0.0270914,-3.29844e-05,4.60622e-08,-2.84458e-11,23775,8.79143], Tmin=(10,'K'), Tmax=(553.033,'K')),
            NASAPolynomial(coeffs=[2.95255,0.0263732,-1.45437e-05,3.95117e-09,-4.21986e-13,23950,12.7698], Tmin=(553.033,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (197.657,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 104,
    label = "CCD[N]",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97835,0.0011813,4.94373e-05,-7.90022e-08,4.10075e-11,22213.1,6.43812], Tmin=(10,'K'), Tmax=(496.775,'K')),
            NASAPolynomial(coeffs=[1.4614,0.0214483,-1.17601e-05,3.12662e-09,-3.24753e-13,22463.2,16.82], Tmin=(496.775,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (184.678,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 105,
    label = "[O-][NH+]DCD[C]N",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {4,S} {7,S} {8,S}
3 N u0 p0 c+1 {1,S} {5,D} {6,S}
4 C u1 p0 c0 {2,S} {5,D}
5 C u0 p0 c0 {3,D} {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82464,0.0142556,0.000123336,-4.49717e-07,4.57958e-10,42334.6,9.97888], Tmin=(10,'K'), Tmax=(354.486,'K')),
            NASAPolynomial(coeffs=[5.32162,0.0220089,-1.37572e-05,4.23294e-09,-5.04843e-13,42073.7,2.12521], Tmin=(354.486,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (352.013,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 106,
    label = "OCC#N",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {7,S}
2 N u0 p1 c0 {4,T}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {2,T} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96266,0.00274414,8.13863e-05,-1.98762e-07,1.57327e-10,-7877.21,8.12025], Tmin=(10,'K'), Tmax=(380.494,'K')),
            NASAPolynomial(coeffs=[2.72653,0.0211806,-1.27467e-05,3.75477e-09,-4.30551e-13,-7822.53,12.3718], Tmin=(380.494,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-65.4908,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 107,
    label = "[N-]([NH+]DO)OC",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {3,D}
3 N u0 p0 c+1 {2,D} {4,S} {9,S}
4 N u0 p2 c-1 {1,S} {3,S}
5 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91481,0.0181518,8.5525e-06,-1.78678e-08,6.35899e-12,6934.96,8.05224], Tmin=(10,'K'), Tmax=(1111.32,'K')),
            NASAPolynomial(coeffs=[6.08916,0.0213378,-1.06114e-05,2.54499e-09,-2.38892e-13,5771.67,-5.72674], Tmin=(1111.32,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (57.6959,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 108,
    label = "[O-][N+]DNCDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {5,D}
2 O u0 p3 c-1 {4,S}
3 N u0 p1 c0 {4,D} {5,S}
4 N u1 p0 c+1 {2,S} {3,D}
5 C u0 p0 c0 {1,D} {3,S} {6,S}
6 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94939,0.00551492,0.000128377,-6.31532e-07,1.0708e-09,10998.2,9.36201], Tmin=(10,'K'), Tmax=(148.328,'K')),
            NASAPolynomial(coeffs=[3.43081,0.0194994,-1.30429e-05,4.07763e-09,-4.83468e-13,11013.6,10.8742], Tmin=(148.328,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (91.5906,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 109,
    label = "[CH2]CN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {8,S} {9,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u1 p0 c0 {2,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97196,0.00192156,9.26458e-05,-1.93034e-07,1.33903e-10,16939.4,7.02344], Tmin=(10,'K'), Tmax=(367.848,'K')),
            NASAPolynomial(coeffs=[1.51485,0.0286517,-1.64006e-05,4.68026e-09,-5.27414e-13,17120.1,16.4192], Tmin=(367.848,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (140.841,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 110,
    label = "[O-][N+]DCDCDN",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u1 p0 c+1 {1,S} {4,D}
3 N u0 p1 c0 {5,D} {6,S}
4 C u0 p0 c0 {2,D} {5,D}
5 C u0 p0 c0 {3,D} {4,D}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84174,0.0127906,9.13624e-05,-3.51976e-07,3.61358e-10,53231.2,8.85549], Tmin=(10,'K'), Tmax=(361.501,'K')),
            NASAPolynomial(coeffs=[5.59318,0.015346,-1.02573e-05,3.2771e-09,-3.99597e-13,52961.2,0.205512], Tmin=(361.501,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (442.607,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 111,
    label = "[O-][NH+]DNCN",
    molecule = 
"""
1  O u0 p3 c-1 {3,S}
2  N u0 p1 c0 {5,S} {8,S} {9,S}
3  N u0 p0 c+1 {1,S} {4,D} {10,S}
4  N u0 p1 c0 {3,D} {5,S}
5  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
6  H u0 p0 c0 {5,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96658,0.00232036,0.000118228,-2.50276e-07,1.75148e-10,12336.7,9.59234], Tmin=(10,'K'), Tmax=(365.323,'K')),
            NASAPolynomial(coeffs=[0.835607,0.0366092,-2.25896e-05,6.75138e-09,-7.79608e-13,12565.4,21.544], Tmin=(365.323,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (102.574,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 112,
    label = "COCD[N]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 N u1 p1 c0 {4,D}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {2,D} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88081,0.0105078,2.32937e-05,-3.52762e-08,1.41485e-11,6985.08,7.76873], Tmin=(10,'K'), Tmax=(824.901,'K')),
            NASAPolynomial(coeffs=[2.1644,0.0249154,-1.39697e-05,3.78117e-09,-3.98481e-13,7061.23,14.4642], Tmin=(824.901,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (58.0705,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 113,
    label = "CNCD[N]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {4,S} {8,S}
2 N u1 p1 c0 {4,D}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {2,D} {9,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84334,0.0129098,2.65004e-05,-4.44453e-08,1.99761e-11,26053.9,7.91001], Tmin=(10,'K'), Tmax=(686.51,'K')),
            NASAPolynomial(coeffs=[1.62531,0.0292244,-1.65555e-05,4.56118e-09,-4.90254e-13,26278.5,17.1945], Tmin=(686.51,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (216.606,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 114,
    label = "OOC#N",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u0 p1 c0 {4,T}
4 C u0 p0 c0 {1,S} {3,T}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92132,0.00553058,5.98209e-05,-1.69133e-07,1.36037e-10,10095.5,8.02636], Tmin=(10,'K'), Tmax=(442.328,'K')),
            NASAPolynomial(coeffs=[4.72286,0.0118942,-7.91929e-06,2.53564e-09,-3.09835e-13,9891.4,3.30795], Tmin=(442.328,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (83.9322,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 115,
    label = "[CH2]ONO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {3,S} {8,S}
3 N u0 p1 c0 {1,S} {2,S} {5,S}
4 C u1 p0 c0 {1,S} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91384,0.0058047,9.76829e-05,-2.34824e-07,1.70778e-10,10724.3,8.60803], Tmin=(10,'K'), Tmax=(460.304,'K')),
            NASAPolynomial(coeffs=[3.63213,0.0243503,-1.52091e-05,4.65435e-09,-5.50981e-13,10579.7,7.89612], Tmin=(460.304,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (89.1543,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 116,
    label = "NCD[C]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {8,S}
2 N u0 p1 c0 {3,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 C u1 p0 c0 {1,S} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93085,0.00425762,8.55625e-05,-1.77655e-07,1.12085e-10,14665.4,8.91308], Tmin=(10,'K'), Tmax=(524.827,'K')),
            NASAPolynomial(coeffs=[3.19719,0.0247376,-1.55231e-05,4.80247e-09,-5.75727e-13,14537.4,10.0261], Tmin=(524.827,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (121.913,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 117,
    label = "[NH-][N+]DNC",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {4,S}
2 N u1 p0 c+1 {1,D} {3,S}
3 N u0 p2 c-1 {2,S} {8,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90612,0.0132446,1.29958e-05,-2.14039e-08,7.8193e-12,45769.5,7.65049], Tmin=(10,'K'), Tmax=(1000.86,'K')),
            NASAPolynomial(coeffs=[4.03429,0.0209758,-1.09458e-05,2.77286e-09,-2.75315e-13,45331,4.96939], Tmin=(1000.86,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (380.567,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 118,
    label = "CNON",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  N u0 p1 c0 {1,S} {4,S} {8,S}
3  N u0 p1 c0 {1,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  H u0 p0 c0 {4,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85064,0.0105701,6.62136e-05,-1.4168e-07,9.52879e-11,11983.6,7.53036], Tmin=(10,'K'), Tmax=(382.362,'K')),
            NASAPolynomial(coeffs=[1.80291,0.031992,-1.78243e-05,4.8436e-09,-5.13951e-13,12140.2,15.4408], Tmin=(382.362,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (99.6079,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 119,
    label = "CNOO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {9,S}
3 N u0 p1 c0 {1,S} {4,S} {8,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94408,0.0050574,0.000138306,-4.44106e-07,4.85014e-10,-2195.54,7.32966], Tmin=(10,'K'), Tmax=(231.321,'K')),
            NASAPolynomial(coeffs=[2.55371,0.0290999,-1.76e-05,5.21995e-09,-6.01626e-13,-2131.22,12.0019], Tmin=(231.321,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-18.24,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 120,
    label = "NNN[NH]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {5,S}
2 N u0 p1 c0 {1,S} {4,S} {6,S}
3 N u0 p1 c0 {1,S} {7,S} {8,S}
4 N u1 p1 c0 {2,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94129,0.00355818,9.11106e-05,-1.76972e-07,1.06707e-10,48150.7,9.04145], Tmin=(10,'K'), Tmax=(529.348,'K')),
            NASAPolynomial(coeffs=[2.15509,0.0296071,-1.82709e-05,5.57821e-09,-6.62554e-13,48163.9,14.8615], Tmin=(529.348,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (400.326,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 121,
    label = "NON[NH]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {4,S} {5,S}
3 N u0 p1 c0 {1,S} {6,S} {7,S}
4 N u1 p1 c0 {2,S} {8,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92056,0.00600477,9.8937e-05,-2.6184e-07,2.15713e-10,40247.4,9.31899], Tmin=(10,'K'), Tmax=(390.209,'K')),
            NASAPolynomial(coeffs=[3.12496,0.0249709,-1.5527e-05,4.71888e-09,-5.54104e-13,40227.2,11.354], Tmin=(390.209,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (334.641,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 122,
    label = "[CH2]ONN",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {3,S} {5,S}
3 N u0 p1 c0 {2,S} {6,S} {7,S}
4 C u1 p0 c0 {1,S} {8,S} {9,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92455,0.00504989,0.000105937,-2.42204e-07,1.71684e-10,26806,8.69181], Tmin=(10,'K'), Tmax=(457.544,'K')),
            NASAPolynomial(coeffs=[2.88522,0.0283664,-1.71559e-05,5.12363e-09,-5.96566e-13,26752.2,11.2656], Tmin=(457.544,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (222.867,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 123,
    label = "[NH]OCDC",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u1 p1 c0 {1,S} {8,S}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {3,D} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95233,0.00291403,8.11093e-05,-1.5738e-07,9.53534e-11,21618.7,8.83818], Tmin=(10,'K'), Tmax=(518.539,'K')),
            NASAPolynomial(coeffs=[2.10218,0.0269979,-1.69422e-05,5.17269e-09,-6.10293e-13,21678.6,15.2771], Tmin=(518.539,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (179.732,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 124,
    label = "[CH2]C#N",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,T}
2 C u1 p0 c0 {3,S} {4,S} {5,S}
3 C u0 p0 c0 {1,T} {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97543,0.00148655,3.89582e-05,-7.51769e-08,4.51351e-11,30010.3,5.57409], Tmin=(10,'K'), Tmax=(529.917,'K')),
            NASAPolynomial(coeffs=[3.18087,0.0127428,-7.78951e-06,2.36104e-09,-2.79848e-13,30020.7,8.20615], Tmin=(529.917,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (249.511,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 125,
    label = "CDCND[N]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {3,S}
2 N u1 p1 c0 {1,D}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {3,D} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96339,0.00236996,7.20804e-05,-1.48621e-07,9.72402e-11,39120.8,8.59182], Tmin=(10,'K'), Tmax=(468.51,'K')),
            NASAPolynomial(coeffs=[2.37284,0.0226049,-1.40124e-05,4.20456e-09,-4.87609e-13,39196.8,14.2798], Tmin=(468.51,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (325.262,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 126,
    label = "[O-][N+]DCDCDO",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 O u0 p2 c0 {5,D}
3 N u1 p0 c+1 {1,S} {4,D}
4 C u0 p0 c0 {3,D} {5,D}
5 C u0 p0 c0 {2,D} {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8801,0.0101142,6.85888e-05,-2.75142e-07,2.96472e-10,23136.5,8.98092], Tmin=(10,'K'), Tmax=(340.023,'K')),
            NASAPolynomial(coeffs=[4.85014,0.0132247,-9.19671e-06,2.97522e-09,-3.63327e-13,22986.6,4.11299], Tmin=(340.023,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (192.384,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 127,
    label = "CN[C]DC",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {4,D} {9,S} {10,S}
4  C u1 p0 c0 {1,S} {3,D}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79448,0.0213941,3.08519e-06,-1.22775e-08,4.45023e-12,32411.5,7.96477], Tmin=(10,'K'), Tmax=(1127.76,'K')),
            NASAPolynomial(coeffs=[4.87208,0.0253159,-1.24309e-05,2.98343e-09,-2.82507e-13,31676,0.45306], Tmin=(1127.76,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (269.48,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 128,
    label = "[O-][N+]DNCDN",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {4,S}
2 N u0 p1 c0 {4,D} {5,S}
3 N u0 p1 c0 {5,D} {7,S}
4 N u1 p0 c+1 {1,S} {2,D}
5 C u0 p0 c0 {2,S} {3,D} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87561,0.0101976,4.19077e-05,-9.32317e-08,5.85274e-11,36521.4,9.58208], Tmin=(10,'K'), Tmax=(518.459,'K')),
            NASAPolynomial(coeffs=[3.05014,0.0232042,-1.49275e-05,4.5451e-09,-5.28135e-13,36517.8,12.1619], Tmin=(518.459,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (303.64,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 129,
    label = "NC#C",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94774,0.00319063,5.4613e-05,-1.16031e-07,7.37212e-11,28215.9,5.54734], Tmin=(10,'K'), Tmax=(537.158,'K')),
            NASAPolynomial(coeffs=[4.05887,0.0140446,-8.31658e-06,2.55602e-09,-3.12722e-13,28035.4,3.51157], Tmin=(537.158,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (234.582,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 130,
    label = "[O-][NH+]DC",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {4,S}
3 C u0 p0 c0 {2,D} {5,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09246,-0.00737308,7.22744e-05,-1.07676e-07,5.28357e-11,6423.01,6.56781], Tmin=(10,'K'), Tmax=(622.007,'K')),
            NASAPolynomial(coeffs=[1.30028,0.0188936,-1.11109e-05,3.17706e-09,-3.525e-13,6609.59,17.4204], Tmin=(622.007,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (53.4093,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 131,
    label = "[O-][N+]DNC",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {3,D} {4,S}
3 N u1 p0 c+1 {1,S} {2,D}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87814,0.0114857,9.94603e-06,-1.69545e-08,6.2206e-12,22837.4,7.58112], Tmin=(10,'K'), Tmax=(985.547,'K')),
            NASAPolynomial(coeffs=[3.47934,0.0189111,-1.01936e-05,2.64726e-09,-2.68226e-13,22634,8.06856], Tmin=(985.547,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (189.878,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 132,
    label = "[NH]CCDC",
    molecule = 
"""
multiplicity 2
1  N u1 p1 c0 {2,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {4,D} {7,S}
4  C u0 p0 c0 {3,D} {8,S} {9,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96805,0.00213478,0.000109615,-2.19484e-07,1.4472e-10,28651.2,9.14123], Tmin=(10,'K'), Tmax=(388.458,'K')),
            NASAPolynomial(coeffs=[0.654399,0.0362535,-2.21221e-05,6.58565e-09,-7.614e-13,28908.7,21.9946], Tmin=(388.458,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (238.216,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 133,
    label = "[O-][NH+]DCD[C]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {5,S} {7,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {2,S} {4,D} {6,S}
4 C u0 p0 c0 {3,D} {5,D}
5 C u1 p0 c0 {1,S} {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82153,0.014453,0.000108164,-4.11172e-07,4.21759e-10,24894.6,9.81308], Tmin=(10,'K'), Tmax=(359.568,'K')),
            NASAPolynomial(coeffs=[5.70575,0.0183602,-1.18776e-05,3.73862e-09,-4.52654e-13,24598.3,0.414662], Tmin=(359.568,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (207.006,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 134,
    label = "[N]DNCDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,D} {4,S}
3 N u1 p1 c0 {2,D}
4 C u0 p0 c0 {1,D} {2,S} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96633,0.00500973,0.000207595,-1.8802e-06,5.44998e-09,17154,7.14077], Tmin=(10,'K'), Tmax=(115.512,'K')),
            NASAPolynomial(coeffs=[3.97543,0.0131739,-8.53047e-06,2.62376e-09,-3.08136e-13,17148.2,6.87164], Tmin=(115.512,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (145.932,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 135,
    label = "CNDCC",
    molecule = 
"""
1  N u0 p1 c0 {3,S} {4,D}
2  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {1,D} {2,S} {11,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82568,0.0149557,2.84191e-05,-3.92397e-08,1.41688e-11,2033.14,6.04619], Tmin=(10,'K'), Tmax=(914.096,'K')),
            NASAPolynomial(coeffs=[0.755122,0.036247,-1.94086e-05,5.04244e-09,-5.13113e-13,2266.34,18.789], Tmin=(914.096,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (16.8943,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 136,
    label = "NNDNO",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {7,S}
2 N u0 p1 c0 {3,S} {5,S} {6,S}
3 N u0 p1 c0 {2,S} {4,D}
4 N u0 p1 c0 {1,S} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94591,0.00319955,6.89318e-05,-1.34352e-07,7.94511e-11,16621.6,7.65329], Tmin=(10,'K'), Tmax=(557.09,'K')),
            NASAPolynomial(coeffs=[3.06145,0.0217926,-1.40946e-05,4.45205e-09,-5.41207e-13,16530.2,9.69784], Tmin=(557.09,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (138.179,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 137,
    label = "NC#[C]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u1 p0 c0 {2,T}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95238,0.0036459,5.38036e-05,-1.64126e-07,1.50633e-10,61411.5,6.2999], Tmin=(10,'K'), Tmax=(374.464,'K')),
            NASAPolynomial(coeffs=[4.15221,0.00996306,-5.35642e-06,1.47156e-09,-1.63054e-13,61337.3,4.74091], Tmin=(374.464,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (510.609,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 138,
    label = "[O-][NH+]DN[NH]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {5,S}
3 N u0 p1 c0 {2,D} {4,S}
4 N u1 p1 c0 {3,S} {6,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96024,0.00237678,5.72436e-05,-1.10939e-07,6.58807e-11,35467.3,8.56312], Tmin=(10,'K'), Tmax=(543.389,'K')),
            NASAPolynomial(coeffs=[2.88996,0.0189308,-1.24014e-05,3.88735e-09,-4.65885e-13,35455.5,11.8953], Tmin=(543.389,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (294.876,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 139,
    label = "CNCDO",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,S} {4,S} {8,S}
3 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,D} {2,S} {9,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95471,0.0135102,1.46854e-05,-2.05198e-08,6.61786e-12,-24543.5,7.15949], Tmin=(10,'K'), Tmax=(1141.62,'K')),
            NASAPolynomial(coeffs=[4.75218,0.0215715,-1.01698e-05,2.324e-09,-2.08612e-13,-25433,0.108291], Tmin=(1141.62,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-204.035,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 140,
    label = "[O-][NH+]D[C]C",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {4,D} {8,S}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u1 p0 c0 {2,D} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72968,0.030088,-0.00011473,3.14639e-07,-2.86666e-10,32565.4,8.28973], Tmin=(10,'K'), Tmax=(396.254,'K')),
            NASAPolynomial(coeffs=[1.86472,0.0264015,-1.55555e-05,4.41193e-09,-4.84377e-13,32890,17.7908], Tmin=(396.254,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (270.752,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 141,
    label = "[O-][NH+]DCDN",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {4,D} {5,S}
3 N u0 p1 c0 {4,D} {6,S}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95371,0.00306057,6.37233e-05,-1.43073e-07,9.90761e-11,32874.6,7.98747], Tmin=(10,'K'), Tmax=(467.518,'K')),
            NASAPolynomial(coeffs=[3.23648,0.017829,-1.13554e-05,3.4793e-09,-4.09349e-13,32847.4,9.89348], Tmin=(467.518,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (273.327,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 142,
    label = "N[C]DCN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {6,S} {7,S}
2 N u0 p1 c0 {4,S} {8,S} {9,S}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u1 p0 c0 {2,S} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92418,0.00490123,0.000101066,-2.21953e-07,1.50044e-10,33792.9,9.06018], Tmin=(10,'K'), Tmax=(484.442,'K')),
            NASAPolynomial(coeffs=[3.01101,0.0276813,-1.66578e-05,4.99307e-09,-5.85627e-13,33702.5,10.9581], Tmin=(484.442,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (280.953,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 143,
    label = "NNDCDN",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 N u0 p1 c0 {1,S} {4,D}
3 N u0 p1 c0 {4,D} {7,S}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93851,0.00401205,7.58142e-05,-1.71529e-07,1.18412e-10,33200.3,7.88321], Tmin=(10,'K'), Tmax=(480.167,'K')),
            NASAPolynomial(coeffs=[3.49521,0.0199386,-1.21559e-05,3.66954e-09,-4.3207e-13,33101.8,8.22811], Tmin=(480.167,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (276.03,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 144,
    label = "[O-][NH+]DCNDN",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {5,D} {7,S}
3 N u0 p1 c0 {4,D} {5,S}
4 N u0 p1 c0 {3,D} {8,S}
5 C u0 p0 c0 {2,D} {3,S} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95464,0.00307884,9.41146e-05,-2.04995e-07,1.42659e-10,30974.7,9.05238], Tmin=(10,'K'), Tmax=(433.738,'K')),
            NASAPolynomial(coeffs=[1.99679,0.028313,-1.79786e-05,5.4529e-09,-6.3401e-13,31077,16.084], Tmin=(433.738,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (257.535,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 145,
    label = "ONDCDN",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 N u0 p1 c0 {1,S} {4,D}
3 N u0 p1 c0 {4,D} {6,S}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93332,0.00415784,6.47508e-05,-1.44754e-07,9.53551e-11,18423.5,7.77665], Tmin=(10,'K'), Tmax=(522.501,'K')),
            NASAPolynomial(coeffs=[4.21898,0.0161784,-1.05448e-05,3.357e-09,-4.10859e-13,18199.7,4.72808], Tmin=(522.501,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (153.161,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 146,
    label = "[O-][NH+]DCD[N]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {4,D} {5,S}
3 N u1 p1 c0 {4,D}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94819,0.00341332,5.22905e-05,-1.25461e-07,8.93657e-11,30645.1,8.36977], Tmin=(10,'K'), Tmax=(479.449,'K')),
            NASAPolynomial(coeffs=[4.05655,0.0126178,-8.13204e-06,2.53064e-09,-3.0308e-13,30518.6,6.71502], Tmin=(479.449,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (254.788,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 147,
    label = "[N]DCC#C",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {5,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {6,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93557,0.00408868,6.57454e-05,-1.49111e-07,1.0041e-10,57883.6,8.20886], Tmin=(10,'K'), Tmax=(507.128,'K')),
            NASAPolynomial(coeffs=[4.05919,0.0165052,-1.05909e-05,3.31128e-09,-3.99692e-13,57698.8,5.99855], Tmin=(507.128,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (481.253,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 148,
    label = "[CH2]ONDC",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {4,D}
3 C u1 p0 c0 {1,S} {5,S} {6,S}
4 C u0 p0 c0 {2,D} {7,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93518,0.00459507,9.81017e-05,-2.37859e-07,1.80961e-10,25190.9,8.11487], Tmin=(10,'K'), Tmax=(417.544,'K')),
            NASAPolynomial(coeffs=[2.82131,0.0258122,-1.60067e-05,4.82282e-09,-5.61608e-13,25192,11.415], Tmin=(417.544,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (209.448,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 149,
    label = "NONDC",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 N u0 p1 c0 {1,S} {4,D}
4 C u0 p0 c0 {3,D} {7,S} {8,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90678,0.00783994,6.20663e-05,-1.45788e-07,1.08932e-10,20903.2,8.21366], Tmin=(10,'K'), Tmax=(343.195,'K')),
            NASAPolynomial(coeffs=[2.38862,0.0255344,-1.52702e-05,4.44007e-09,-5.00686e-13,21007.4,13.9143], Tmin=(343.195,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (173.794,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 150,
    label = "[NH]NNO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {8,S}
2 N u0 p1 c0 {3,S} {4,S} {5,S}
3 N u0 p1 c0 {1,S} {2,S} {6,S}
4 N u1 p1 c0 {2,S} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94098,0.00349054,8.04129e-05,-1.54605e-07,9.08207e-11,31533.5,8.95257], Tmin=(10,'K'), Tmax=(554.697,'K')),
            NASAPolynomial(coeffs=[2.63044,0.0261879,-1.67869e-05,5.26813e-09,-6.3734e-13,31475,12.6658], Tmin=(554.697,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (262.161,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 151,
    label = "ODN[N-][NH+]DO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {5,D}
3 N u0 p0 c+1 {1,D} {4,S} {6,S}
4 N u0 p2 c-1 {3,S} {5,S}
5 N u0 p1 c0 {2,D} {4,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92666,0.00548829,6.8647e-05,-1.74988e-07,1.35392e-10,30291,8.87808], Tmin=(10,'K'), Tmax=(419.398,'K')),
            NASAPolynomial(coeffs=[3.31866,0.0198625,-1.3434e-05,4.23998e-09,-5.06376e-13,30266.6,10.3839], Tmin=(419.398,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (251.852,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 152,
    label = "[CH2]ON",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {6,S} {7,S}
3 C u1 p0 c0 {1,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93362,0.00533372,5.65752e-05,-1.41014e-07,1.15147e-10,17736.5,6.95563], Tmin=(10,'K'), Tmax=(311.691,'K')),
            NASAPolynomial(coeffs=[2.84387,0.0193188,-1.07279e-05,2.94036e-09,-3.16406e-13,17804.4,10.9426], Tmin=(311.691,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (147.464,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 153,
    label = "O[C]DCDN",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 N u0 p1 c0 {4,D} {6,S}
3 C u1 p0 c0 {1,S} {4,D}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87195,0.0102967,8.37285e-05,-3.09023e-07,3.12736e-10,29612.2,7.92491], Tmin=(10,'K'), Tmax=(361.559,'K')),
            NASAPolynomial(coeffs=[5.18592,0.0141913,-8.89425e-06,2.75276e-09,-3.30354e-13,29396.7,1.25653], Tmin=(361.559,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (246.225,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 154,
    label = "[N-]([NH+]DO)CDC",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 N u0 p0 c+1 {1,D} {3,S} {9,S}
3 N u0 p2 c-1 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,D} {6,S}
5 C u0 p0 c0 {4,D} {7,S} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9563,0.0027832,9.89702e-05,-1.95637e-07,1.23343e-10,21142.5,9.58085], Tmin=(10,'K'), Tmax=(474.209,'K')),
            NASAPolynomial(coeffs=[1.23983,0.0332006,-2.09801e-05,6.36314e-09,-7.41481e-13,21315.8,19.7699], Tmin=(474.209,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (175.778,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 155,
    label = "ONCDC",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {9,S}
2 N u0 p1 c0 {1,S} {3,S} {6,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 C u0 p0 c0 {3,D} {7,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94724,0.00315766,8.95728e-05,-1.68403e-07,9.87427e-11,2931.2,8.16329], Tmin=(10,'K'), Tmax=(535.993,'K')),
            NASAPolynomial(coeffs=[1.72423,0.030914,-1.93543e-05,5.94874e-09,-7.08316e-13,3009.1,16.0054], Tmin=(535.993,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (24.3514,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 156,
    label = "[O-][N+]DCCC",
    molecule = 
"""
multiplicity 2
1  O u0 p3 c-1 {2,S}
2  N u1 p0 c+1 {1,S} {5,D}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {2,D} {3,S} {11,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88717,0.0201793,1.85162e-05,-3.04806e-08,1.08921e-11,9320.53,9.59261], Tmin=(10,'K'), Tmax=(1039.3,'K')),
            NASAPolynomial(coeffs=[4.77635,0.0302623,-1.55282e-05,3.8606e-09,-3.76172e-13,8406.32,1.75954], Tmin=(1039.3,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (77.5338,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 157,
    label = "[O-][NH+]DCC#[C]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {6,S}
4 C u0 p0 c0 {3,S} {5,T}
5 C u1 p0 c0 {4,T}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9437,0.00703206,0.000202751,-1.37374e-06,3.28174e-09,68859.8,8.75544], Tmin=(10,'K'), Tmax=(104.965,'K')),
            NASAPolynomial(coeffs=[3.54529,0.0222148,-1.42202e-05,4.32539e-09,-5.02886e-13,68868.2,9.77947], Tmin=(104.965,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (574.017,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 158,
    label = "ONDCO",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {6,S}
2 O u0 p2 c0 {3,S} {7,S}
3 N u0 p1 c0 {2,S} {4,D}
4 C u0 p0 c0 {1,S} {3,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94716,0.00313836,6.92596e-05,-1.35086e-07,8.01439e-11,-24355.7,8.16963], Tmin=(10,'K'), Tmax=(552.529,'K')),
            NASAPolynomial(coeffs=[2.9585,0.0221176,-1.43589e-05,4.52952e-09,-5.48347e-13,-24426.9,10.7198], Tmin=(552.529,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-202.525,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 159,
    label = "NNCD[N]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {6,S} {7,S}
3 N u1 p1 c0 {4,D}
4 C u0 p0 c0 {1,S} {3,D} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95083,0.00408712,9.75432e-05,-2.60989e-07,2.33607e-10,41396,8.86742], Tmin=(10,'K'), Tmax=(283.547,'K')),
            NASAPolynomial(coeffs=[2.43739,0.0254371,-1.54008e-05,4.56063e-09,-5.24075e-13,41481.8,14.2614], Tmin=(283.547,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (344.193,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 160,
    label = "NOCD[N]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 N u1 p1 c0 {4,D}
4 C u0 p0 c0 {1,S} {3,D} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84437,0.013682,8.87483e-06,-2.19122e-08,1.03029e-11,27917.8,8.85728], Tmin=(10,'K'), Tmax=(766.493,'K')),
            NASAPolynomial(coeffs=[3.60512,0.019407,-1.10892e-05,3.07125e-09,-3.30886e-13,27823,9.09007], Tmin=(766.493,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (232.108,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 161,
    label = "CNCN",
    molecule = 
"""
1  N u0 p1 c0 {3,S} {4,S} {10,S}
2  N u0 p1 c0 {3,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87085,0.0113642,5.88183e-05,-9.01027e-08,4.10732e-11,-2347.52,7.56261], Tmin=(10,'K'), Tmax=(654.987,'K')),
            NASAPolynomial(coeffs=[-0.178598,0.0416441,-2.32365e-05,6.352e-09,-6.80053e-13,-1936.11,24.4766], Tmin=(654.987,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-19.5319,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 162,
    label = "CDNNDN",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {4,D}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {2,D} {7,S}
4 C u0 p0 c0 {1,D} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97783,0.00141517,6.58904e-05,-1.25316e-07,7.78554e-11,41065.7,8.25632], Tmin=(10,'K'), Tmax=(413.628,'K')),
            NASAPolynomial(coeffs=[1.68403,0.0235966,-1.4546e-05,4.32213e-09,-4.9576e-13,41255.4,17.2978], Tmin=(413.628,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (341.433,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 163,
    label = "NCNDC",
    molecule = 
"""
1  N u0 p1 c0 {3,S} {7,S} {8,S}
2  N u0 p1 c0 {3,S} {4,D}
3  C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96539,0.00208738,9.12884e-05,-1.60677e-07,9.20195e-11,9959.8,8.21155], Tmin=(10,'K'), Tmax=(451.042,'K')),
            NASAPolynomial(coeffs=[0.161296,0.0358987,-2.14056e-05,6.26098e-09,-7.14541e-13,10302.2,23.5268], Tmin=(451.042,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (82.7963,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 164,
    label = "[CH2]CNDC",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {4,D}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C u1 p0 c0 {2,S} {7,S} {8,S}
4  C u0 p0 c0 {1,D} {9,S} {10,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82444,0.0157465,2.92314e-05,-4.97975e-08,2.18973e-11,28897.8,8.41457], Tmin=(10,'K'), Tmax=(753.519,'K')),
            NASAPolynomial(coeffs=[2.08014,0.0322875,-1.81914e-05,4.98353e-09,-5.32585e-13,28954,14.9645], Tmin=(753.519,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (240.256,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 165,
    label = "C[CH]C#N",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {4,T}
2 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3 C u1 p0 c0 {2,S} {4,S} {8,S}
4 C u0 p0 c0 {1,T} {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84039,0.0144958,1.21482e-05,-2.3885e-08,9.99599e-12,25383.5,7.93082], Tmin=(10,'K'), Tmax=(844.928,'K')),
            NASAPolynomial(coeffs=[3.2147,0.0229612,-1.26503e-05,3.39026e-09,-3.55155e-13,25292.8,9.68152], Tmin=(844.928,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (211.041,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 166,
    label = "CCD[C]N",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {4,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u1 p0 c0 {1,S} {3,D}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77755,0.0181889,2.88247e-05,-6.91693e-08,4.40016e-11,28506.4,7.91953], Tmin=(10,'K'), Tmax=(414.615,'K')),
            NASAPolynomial(coeffs=[2.4628,0.0308729,-1.70641e-05,4.61611e-09,-4.88805e-13,28615.5,13.1049], Tmin=(414.615,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (236.984,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 167,
    label = "C[N]NC",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {3,S} {11,S}
2  N u1 p1 c0 {1,S} {4,S}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72436,0.0270631,-4.35574e-05,1.17159e-07,-1.01469e-10,21922.5,6.8938], Tmin=(10,'K'), Tmax=(474.714,'K')),
            NASAPolynomial(coeffs=[0.269695,0.0381067,-2.13683e-05,5.83034e-09,-6.21368e-13,22454.1,23.1307], Tmin=(474.714,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (182.27,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 168,
    label = "NCC#[C]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u1 p0 c0 {3,T}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89089,0.00885689,6.47172e-05,-1.70003e-07,1.42832e-10,66746.3,8.8296], Tmin=(10,'K'), Tmax=(303.931,'K')),
            NASAPolynomial(coeffs=[2.66811,0.0249497,-1.47058e-05,4.20938e-09,-4.67659e-13,66820.6,13.2725], Tmin=(303.931,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (554.955,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 169,
    label = "CDNNDO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 N u0 p1 c0 {3,S} {4,D}
3 N u0 p1 c0 {1,D} {2,S}
4 C u0 p0 c0 {2,D} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9183,0.0091687,1.50885e-05,-2.73213e-08,1.2039e-11,26168.8,8.06771], Tmin=(10,'K'), Tmax=(803.842,'K')),
            NASAPolynomial(coeffs=[3.81334,0.0159584,-9.27655e-06,2.58534e-09,-2.7877e-13,25983.2,7.29163], Tmin=(803.842,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (217.582,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 170,
    label = "CNCO",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {11,S}
2  N u0 p1 c0 {3,S} {4,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.857,0.0134955,3.90047e-05,-5.78109e-08,2.37168e-11,-25409.6,7.49589], Tmin=(10,'K'), Tmax=(787.352,'K')),
            NASAPolynomial(coeffs=[1.0385,0.036082,-1.97762e-05,5.29671e-09,-5.55754e-13,-25222.1,18.7923], Tmin=(787.352,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-211.273,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 171,
    label = "ONCD[CH]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {8,S}
2 N u0 p1 c0 {1,S} {3,S} {5,S}
3 C u0 p0 c0 {2,S} {4,D} {6,S}
4 C u1 p0 c0 {3,D} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92456,0.00463891,8.81981e-05,-1.85034e-07,1.17133e-10,33716.6,8.83047], Tmin=(10,'K'), Tmax=(527.738,'K')),
            NASAPolynomial(coeffs=[3.39796,0.024936,-1.58389e-05,4.93772e-09,-5.94949e-13,33545.1,8.88314], Tmin=(527.738,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (280.31,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 172,
    label = "[O-][N+]#CCDC",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {5,T}
3 C u0 p0 c0 {4,D} {5,S} {6,S}
4 C u0 p0 c0 {3,D} {7,S} {8,S}
5 C u0 p0 c0 {2,T} {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89577,0.0100591,9.08037e-05,-3.05569e-07,3.35402e-10,26105.6,9.1857], Tmin=(10,'K'), Tmax=(231.213,'K')),
            NASAPolynomial(coeffs=[2.93548,0.0266722,-1.69743e-05,5.1927e-09,-6.09755e-13,26150,12.4123], Tmin=(231.213,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (217.069,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 173,
    label = "OCDN",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {5,S}
2 N u0 p1 c0 {3,D} {6,S}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09973,-0.00799065,7.72507e-05,-1.17289e-07,5.83673e-11,-18821,6.63964], Tmin=(10,'K'), Tmax=(624.983,'K')),
            NASAPolynomial(coeffs=[1.56338,0.0185212,-1.10495e-05,3.21593e-09,-3.62337e-13,-18704.7,16.0778], Tmin=(624.983,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-156.481,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 174,
    label = "CON[NH]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {3,S} {8,S}
3 N u1 p1 c0 {2,S} {9,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84509,0.0163312,1.32928e-05,-2.42905e-08,9.36502e-12,21875.1,8.20361], Tmin=(10,'K'), Tmax=(941.648,'K')),
            NASAPolynomial(coeffs=[3.56382,0.0253451,-1.35212e-05,3.51126e-09,-3.5727e-13,21581.4,7.703], Tmin=(941.648,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (181.883,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 175,
    label = "CNN[NH]",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {4,S} {8,S}
2  N u0 p1 c0 {1,S} {3,S} {9,S}
3  N u1 p1 c0 {2,S} {10,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  H u0 p0 c0 {4,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87301,0.0108542,5.19367e-05,-9.33655e-08,5.07069e-11,36196.4,8.22359], Tmin=(10,'K'), Tmax=(481.631,'K')),
            NASAPolynomial(coeffs=[1.11199,0.0337846,-1.94771e-05,5.48347e-09,-6.02003e-13,36462.4,19.5268], Tmin=(481.631,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (300.939,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 176,
    label = "NO[C]DC",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 C u0 p0 c0 {4,D} {7,S} {8,S}
4 C u1 p0 c0 {1,S} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96582,0.00427101,0.000228108,-1.279e-06,2.53725e-09,34799.7,8.79306], Tmin=(10,'K'), Tmax=(126.443,'K')),
            NASAPolynomial(coeffs=[3.3169,0.0247977,-1.53791e-05,4.66341e-09,-5.4752e-13,34816.1,10.5818], Tmin=(126.443,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (289.973,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 177,
    label = "NN[C]DC",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {6,S} {7,S}
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
            NASAPolynomial(coeffs=[3.9127,0.00872558,0.000137764,-5.59899e-07,7.77346e-10,46399.4,9.2226], Tmin=(10,'K'), Tmax=(181.396,'K')),
            NASAPolynomial(coeffs=[3.07052,0.0272967,-1.58046e-05,4.49407e-09,-4.98879e-13,46429.9,11.848], Tmin=(181.396,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (385.826,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 178,
    label = "CN[NH]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {7,S}
2 N u1 p1 c0 {1,S} {8,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94775,0.00376806,4.78431e-05,-7.62346e-08,3.86235e-11,24421.6,6.58068], Tmin=(10,'K'), Tmax=(511.635,'K')),
            NASAPolynomial(coeffs=[1.27552,0.0246598,-1.34072e-05,3.57583e-09,-3.745e-13,24695,17.6818], Tmin=(511.635,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (203.039,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 179,
    label = "CCDN",
    molecule = 
"""
1 N u0 p1 c0 {3,D} {8,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00902,-0.000869551,6.02822e-05,-8.69991e-08,4.09462e-11,3218.53,5.84092], Tmin=(10,'K'), Tmax=(549.86,'K')),
            NASAPolynomial(coeffs=[0.227521,0.0266393,-1.47609e-05,3.98527e-09,-4.20798e-13,3634.39,21.8228], Tmin=(549.86,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (26.7569,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 180,
    label = "C[C]DCN",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {3,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {4,D} {8,S}
4  C u1 p0 c0 {2,S} {3,D}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79619,0.0164037,3.63089e-05,-8.12085e-08,5.10736e-11,30268.1,7.86579], Tmin=(10,'K'), Tmax=(416.478,'K')),
            NASAPolynomial(coeffs=[2.24455,0.0313062,-1.73643e-05,4.70731e-09,-4.99149e-13,30397.4,13.9925], Tmin=(416.478,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (251.632,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 181,
    label = "ONCO",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {8,S}
2 O u0 p2 c0 {3,S} {9,S}
3 N u0 p1 c0 {2,S} {4,S} {7,S}
4 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.948,0.00326039,9.36002e-05,-1.86491e-07,1.17011e-10,-29675.9,8.60701], Tmin=(10,'K'), Tmax=(496.367,'K')),
            NASAPolynomial(coeffs=[1.88964,0.03009,-1.84294e-05,5.54625e-09,-6.48261e-13,-29597.7,15.8247], Tmin=(496.367,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-246.754,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 182,
    label = "ONDCDO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,S} {4,D}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9305,0.00512803,5.76736e-05,-1.6874e-07,1.43448e-10,-9684.5,7.78498], Tmin=(10,'K'), Tmax=(410.122,'K')),
            NASAPolynomial(coeffs=[4.31933,0.0121998,-7.92601e-06,2.48437e-09,-2.98507e-13,-9807.76,5.14179], Tmin=(410.122,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-80.5208,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 183,
    label = "NNDCDO",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,S} {5,S} {6,S}
3 N u0 p1 c0 {2,S} {4,D}
4 C u0 p0 c0 {1,D} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82041,0.0174995,-3.03515e-05,5.761e-08,-4.39852e-11,3481.68,8.11791], Tmin=(10,'K'), Tmax=(452.556,'K')),
            NASAPolynomial(coeffs=[3.41111,0.0161639,-9.50719e-06,2.71891e-09,-3.02198e-13,3569.45,10.3285], Tmin=(452.556,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (28.9429,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 184,
    label = "[O-][NH+]DCNDO",
    molecule = 
"""
1 O u0 p3 c-1 {3,S}
2 O u0 p2 c0 {4,D}
3 N u0 p0 c+1 {1,S} {5,D} {7,S}
4 N u0 p1 c0 {2,D} {5,S}
5 C u0 p0 c0 {3,D} {4,S} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92657,0.00550076,7.40861e-05,-1.70784e-07,1.21471e-10,20160.9,9.16779], Tmin=(10,'K'), Tmax=(441.504,'K')),
            NASAPolynomial(coeffs=[2.71756,0.0242198,-1.58941e-05,4.92268e-09,-5.80297e-13,20192,13.155], Tmin=(441.504,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (167.622,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 185,
    label = "ONC#C",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 N u0 p1 c0 {1,S} {3,S} {5,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90731,0.00586714,8.21825e-05,-1.92497e-07,1.31309e-10,28020.2,7.87505], Tmin=(10,'K'), Tmax=(513.01,'K')),
            NASAPolynomial(coeffs=[4.79511,0.0184657,-1.17325e-05,3.7209e-09,-4.58251e-13,27672.2,1.68089], Tmin=(513.01,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (232.947,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 186,
    label = "[N-]([NH+]DO)C#C",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 N u0 p0 c+1 {1,D} {3,S} {6,S}
3 N u0 p2 c-1 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,T}
5 C u0 p0 c0 {4,T} {7,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92271,0.00481269,8.21629e-05,-1.7944e-07,1.16682e-10,46365.2,9.0434], Tmin=(10,'K'), Tmax=(520.851,'K')),
            NASAPolynomial(coeffs=[3.79842,0.0220951,-1.46316e-05,4.63993e-09,-5.62047e-13,46156.7,7.43586], Tmin=(520.851,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (385.478,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 187,
    label = "[NH]OO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u1 p1 c0 {1,S} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95539,0.00296043,4.82302e-05,-1.14933e-07,8.2282e-11,17308.4,7.52605], Tmin=(10,'K'), Tmax=(472.07,'K')),
            NASAPolynomial(coeffs=[3.92592,0.0118321,-7.35574e-06,2.25585e-09,-2.68322e-13,17215.1,6.62858], Tmin=(472.07,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (143.902,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 188,
    label = "[NH]NCDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,S} {4,S} {5,S}
3 N u1 p1 c0 {2,S} {7,S}
4 C u0 p0 c0 {1,D} {2,S} {6,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98081,0.00122353,6.68947e-05,-1.24968e-07,7.5791e-11,5729.11,8.58042], Tmin=(10,'K'), Tmax=(426.442,'K')),
            NASAPolynomial(coeffs=[1.4802,0.0247392,-1.60329e-05,5.00545e-09,-5.99276e-13,5941.83,18.5068], Tmin=(426.442,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (47.6303,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 189,
    label = "NCCD[N]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {7,S} {8,S}
2 N u1 p1 c0 {4,D}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {2,D} {3,S} {9,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89473,0.00889686,5.56395e-05,-1.07879e-07,6.46857e-11,26107.4,9.08966], Tmin=(10,'K'), Tmax=(432.709,'K')),
            NASAPolynomial(coeffs=[1.60739,0.0300415,-1.76597e-05,5.05303e-09,-5.62051e-13,26305.3,18.2086], Tmin=(432.709,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (217.057,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 190,
    label = "CONO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {3,S} {9,S}
3 N u0 p1 c0 {1,S} {2,S} {8,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84845,0.0130844,3.00325e-05,-5.31249e-08,2.53513e-11,-11372.8,7.52308], Tmin=(10,'K'), Tmax=(666.553,'K')),
            NASAPolynomial(coeffs=[2.06412,0.0287707,-1.64711e-05,4.59198e-09,-4.9893e-13,-11245.5,14.5781], Tmin=(666.553,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-94.5761,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 191,
    label = "[CH2]NON",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {4,S} {5,S}
3 N u0 p1 c0 {1,S} {8,S} {9,S}
4 C u1 p0 c0 {2,S} {6,S} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91674,0.00526942,0.000102855,-2.22455e-07,1.4653e-10,34025.7,8.28151], Tmin=(10,'K'), Tmax=(503.121,'K')),
            NASAPolynomial(coeffs=[3.19845,0.0282938,-1.74088e-05,5.30064e-09,-6.28832e-13,33878.8,9.07568], Tmin=(503.121,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (282.882,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 192,
    label = "[O-][NH+]DC[C]DC",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {5,S} {6,S}
4 C u0 p0 c0 {5,D} {8,S} {9,S}
5 C u1 p0 c0 {3,S} {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8956,0.00912679,0.00011943,-3.58229e-07,3.40519e-10,31647.6,9.84155], Tmin=(10,'K'), Tmax=(323.418,'K')),
            NASAPolynomial(coeffs=[2.76911,0.0311203,-1.99623e-05,6.17042e-09,-7.31882e-13,31678.3,13.3528], Tmin=(323.418,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (263.151,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 193,
    label = "NDNNDN",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,D}
2 N u0 p1 c0 {1,S} {4,D}
3 N u0 p1 c0 {1,D} {5,S}
4 N u0 p1 c0 {2,D} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94125,0.00603745,2.73098e-05,-4.60272e-08,2.19416e-11,53220.7,7.26446], Tmin=(10,'K'), Tmax=(694.722,'K')),
            NASAPolynomial(coeffs=[3.08439,0.0172033,-1.02551e-05,2.93373e-09,-3.24082e-13,53189.4,10.0038], Tmin=(694.722,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (442.498,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 194,
    label = "[O-][N+]#CC[NH]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 N u1 p1 c0 {4,S} {8,S}
3 N u0 p0 c+1 {1,S} {5,T}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 C u0 p0 c0 {3,T} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62685,0.0383116,-0.000106936,2.26971e-07,-1.83434e-10,43599,10.6989], Tmin=(10,'K'), Tmax=(399.824,'K')),
            NASAPolynomial(coeffs=[3.81107,0.0252396,-1.57677e-05,4.71476e-09,-5.41656e-13,43674,11.1014], Tmin=(399.824,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (362.494,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 195,
    label = "CNO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {8,S}
2 N u0 p1 c0 {1,S} {3,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97223,0.00164217,6.20086e-05,-1.06409e-07,5.9673e-11,-7809.54,6.02296], Tmin=(10,'K'), Tmax=(458.559,'K')),
            NASAPolynomial(coeffs=[1.31645,0.0248105,-1.37841e-05,3.79055e-09,-4.11254e-13,-7565.99,16.7647], Tmin=(458.559,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-64.9451,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 196,
    label = "CNDCDN",
    molecule = 
"""
1 N u0 p1 c0 {3,S} {4,D}
2 N u0 p1 c0 {4,D} {8,S}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,D} {2,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85072,0.0149313,7.4268e-06,-1.57847e-08,5.98031e-12,16937.1,7.14574], Tmin=(10,'K'), Tmax=(987.741,'K')),
            NASAPolynomial(coeffs=[3.81417,0.0210763,-1.10122e-05,2.8073e-09,-2.8113e-13,16651.8,5.84077], Tmin=(987.741,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (140.822,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 197,
    label = "[O-][NH+]DCDNN",
    molecule = 
"""
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {4,S} {7,S} {8,S}
3 N u0 p0 c+1 {1,S} {5,D} {6,S}
4 N u0 p1 c0 {2,S} {5,D}
5 C u0 p0 c0 {3,D} {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87809,0.0100901,9.92079e-05,-3.02625e-07,2.77756e-10,44821.1,9.3396], Tmin=(10,'K'), Tmax=(360.534,'K')),
            NASAPolynomial(coeffs=[3.56457,0.0257444,-1.65791e-05,5.14982e-09,-6.13416e-13,44764.6,9.43486], Tmin=(360.534,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (372.677,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 198,
    label = "O[N]CDN",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 N u1 p1 c0 {1,S} {4,S}
3 N u0 p1 c0 {4,D} {6,S}
4 C u0 p0 c0 {2,S} {3,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06663,-0.00631776,0.000104468,-1.8275e-07,1.02677e-10,16720.5,8.81386], Tmin=(10,'K'), Tmax=(566.643,'K')),
            NASAPolynomial(coeffs=[1.8984,0.0239405,-1.52122e-05,4.62515e-09,-5.37895e-13,16726.2,15.9245], Tmin=(566.643,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (139.013,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 199,
    label = "[N-]([N+]DN)N",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 N u0 p2 c-1 {1,S} {3,S}
3 N u1 p0 c+1 {2,S} {4,D}
4 N u0 p1 c0 {3,D} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86412,0.0117601,2.85582e-05,-6.84483e-08,4.36781e-11,51820.5,9.18713], Tmin=(10,'K'), Tmax=(512.312,'K')),
            NASAPolynomial(coeffs=[3.25045,0.0212876,-1.32044e-05,3.94196e-09,-4.52833e-13,51821.2,11.1307], Tmin=(512.312,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (430.846,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 200,
    label = "NO[CH]NDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,S} {7,S} {8,S}
4 N u0 p1 c0 {2,D} {5,S}
5 C u1 p0 c0 {1,S} {4,S} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8224,0.0249569,-1.55973e-05,4.71666e-09,-5.52625e-13,18938.6,10.273], Tmin=(10,'K'), Tmax=(1768.1,'K')),
            NASAPolynomial(coeffs=[12.4263,0.00728924,-2.13324e-06,2.14839e-10,2.62852e-15,15615.2,-36.9335], Tmin=(1768.1,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (157.441,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 201,
    label = "[NH]OCN",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 N u0 p1 c0 {4,S} {7,S} {8,S}
3 N u1 p1 c0 {1,S} {9,S}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86853,0.0109136,5.80602e-05,-1.35562e-07,9.83828e-11,12787.9,9.41872], Tmin=(10,'K'), Tmax=(354.462,'K')),
            NASAPolynomial(coeffs=[2.30735,0.028531,-1.64929e-05,4.65626e-09,-5.12256e-13,12898.6,15.3313], Tmin=(354.462,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (106.311,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 202,
    label = "OONO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 N u0 p1 c0 {1,S} {2,S} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91942,0.00490057,7.85604e-05,-1.69157e-07,1.07222e-10,-8507.09,8.33336], Tmin=(10,'K'), Tmax=(542.714,'K')),
            NASAPolynomial(coeffs=[4.22792,0.0204209,-1.3517e-05,4.3641e-09,-5.39552e-13,-8802.63,4.61927], Tmin=(542.714,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-70.7605,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 203,
    label = "[O-][NH+]D[C]NO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {8,S}
2 O u0 p3 c-1 {4,S}
3 N u0 p1 c0 {1,S} {5,S} {6,S}
4 N u0 p0 c+1 {2,S} {5,D} {7,S}
5 C u1 p0 c0 {3,S} {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92358,0.00456891,9.06633e-05,-1.82436e-07,1.10341e-10,22838,10.0158], Tmin=(10,'K'), Tmax=(550.459,'K')),
            NASAPolynomial(coeffs=[3.10286,0.027565,-1.84137e-05,5.87954e-09,-7.1498e-13,22670.3,11.1414], Tmin=(550.459,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (189.856,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 204,
    label = "[O-][N+]#CC#C",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 C u0 p0 c0 {3,S} {5,T}
5 C u0 p0 c0 {4,T} {6,S}
6 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.32785,0.0124016,0.000102643,-3.34194e-07,2.91098e-10,47668.8,8.44577], Tmin=(10,'K'), Tmax=(428.66,'K')),
            NASAPolynomial(coeffs=[6.27697,0.0147224,-9.89703e-06,3.22917e-09,-4.03831e-13,47141.8,-6.48171], Tmin=(428.66,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (396.335,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (137.189,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 205,
    label = "NC[C]DC",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {4,D} {9,S} {10,S}
4  C u1 p0 c0 {2,S} {3,D}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92272,0.00598467,9.99133e-05,-2.24997e-07,1.66246e-10,32307.9,9.10139], Tmin=(10,'K'), Tmax=(345.49,'K')),
            NASAPolynomial(coeffs=[1.54537,0.0335096,-1.95927e-05,5.60874e-09,-6.25693e-13,32472.2,18.0441], Tmin=(345.49,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (268.617,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 206,
    label = "[O-][NH+]D[C]NN",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {4,S}
2 N u0 p1 c0 {3,S} {5,S} {6,S}
3 N u0 p1 c0 {2,S} {7,S} {8,S}
4 N u0 p0 c+1 {1,S} {5,D} {9,S}
5 C u1 p0 c0 {2,S} {4,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89673,0.0080239,0.000115154,-3.09884e-07,2.58522e-10,39615.3,10.0076], Tmin=(10,'K'), Tmax=(384.506,'K')),
            NASAPolynomial(coeffs=[2.94473,0.0301872,-1.9134e-05,5.87081e-09,-6.92696e-13,39597.9,12.5121], Tmin=(384.506,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (329.388,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 207,
    label = "NN[NH]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 N u1 p1 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9823,0.00116263,6.20907e-05,-1.20273e-07,7.6808e-11,36832.6,7.49286], Tmin=(10,'K'), Tmax=(401.077,'K')),
            NASAPolynomial(coeffs=[1.9779,0.0211389,-1.25673e-05,3.73706e-09,-4.36388e-13,36993.5,15.3331], Tmin=(401.077,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (306.241,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 208,
    label = "[N-]D[C][NH+]DC",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {3,D} {4,S} {5,S}
2 N u0 p2 c-1 {4,D}
3 C u0 p0 c0 {1,D} {6,S} {7,S}
4 C u1 p0 c0 {1,S} {2,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90549,0.00665653,8.89054e-05,-2.427e-07,1.94911e-10,37201.6,8.42476], Tmin=(10,'K'), Tmax=(433.34,'K')),
            NASAPolynomial(coeffs=[4.55445,0.0180551,-1.0742e-05,3.20209e-09,-3.76109e-13,36982.1,3.95275], Tmin=(433.34,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (309.306,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 209,
    label = "[NH]OCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,S} {7,S}
3 N u1 p1 c0 {1,S} {8,S}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95625,0.00287002,8.62919e-05,-1.81166e-07,1.20956e-10,-11580.8,9.3525], Tmin=(10,'K'), Tmax=(458.941,'K')),
            NASAPolynomial(coeffs=[2.14598,0.0264502,-1.62789e-05,4.8742e-09,-5.647e-13,-11496.8,15.7809], Tmin=(458.941,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-96.296,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 210,
    label = "OC#N",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 N u0 p1 c0 {3,T}
3 C u0 p0 c0 {1,S} {2,T}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9831,0.000987211,2.48764e-05,-4.62199e-08,2.64526e-11,-3037.56,5.27551], Tmin=(10,'K'), Tmax=(562.364,'K')),
            NASAPolynomial(coeffs=[3.46466,0.00849337,-5.33026e-06,1.6637e-09,-2.01875e-13,-3039.63,6.94141], Tmin=(562.364,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-25.2627,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 211,
    label = "[O-][N+]DNNN",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {5,S}
2 N u0 p1 c0 {3,S} {4,S} {6,S}
3 N u0 p1 c0 {2,S} {7,S} {8,S}
4 N u0 p1 c0 {2,S} {5,D}
5 N u1 p0 c+1 {1,S} {4,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86641,0.0130765,0.000108399,-4.33258e-07,5.24218e-10,48569.1,9.72322], Tmin=(10,'K'), Tmax=(270.165,'K')),
            NASAPolynomial(coeffs=[3.60391,0.0263415,-1.73208e-05,5.46309e-09,-6.58277e-13,48549,10.0127], Tmin=(270.165,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (403.846,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 212,
    label = "O[N]CDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {6,S}
2 O u0 p2 c0 {4,D}
3 N u1 p1 c0 {1,S} {4,S}
4 C u0 p0 c0 {2,D} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04034,-0.0039214,7.82194e-05,-1.35652e-07,7.53503e-11,-7709.12,8.7828], Tmin=(10,'K'), Tmax=(568.422,'K')),
            NASAPolynomial(coeffs=[2.15575,0.0199459,-1.27502e-05,3.86419e-09,-4.47075e-13,-7666.2,15.3032], Tmin=(568.422,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-64.1051,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 213,
    label = "[O-][NH+]DCDNO",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {7,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {2,S} {5,D} {6,S}
4 N u0 p1 c0 {1,S} {5,D}
5 C u0 p0 c0 {3,D} {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86764,0.0104791,8.13238e-05,-2.44106e-07,2.10591e-10,29193,9.31067], Tmin=(10,'K'), Tmax=(399.391,'K')),
            NASAPolynomial(coeffs=[4.13762,0.0219033,-1.46437e-05,4.65464e-09,-5.62297e-13,29058.7,6.84527], Tmin=(399.391,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (242.728,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 214,
    label = "[N-]([N+]DN)O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {6,S}
2 N u1 p0 c+1 {3,S} {4,D}
3 N u0 p2 c-1 {1,S} {2,S}
4 N u0 p1 c0 {2,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96695,0.00187107,5.39963e-05,-9.51095e-08,5.13422e-11,36543.7,8.53329], Tmin=(10,'K'), Tmax=(585.006,'K')),
            NASAPolynomial(coeffs=[2.21799,0.0212359,-1.46468e-05,4.75649e-09,-5.8341e-13,36621.6,14.9502], Tmin=(585.006,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (303.827,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 215,
    label = "[O-][N+]#CNC",
    molecule = 
"""
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {4,S} {5,S} {9,S}
3 N u0 p0 c+1 {1,S} {5,T}
4 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
5 C u0 p0 c0 {2,S} {3,T}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66294,0.0283179,-2.1077e-05,1.26602e-08,-4.77958e-12,24159.1,8.78], Tmin=(10,'K'), Tmax=(612.399,'K')),
            NASAPolynomial(coeffs=[3.75345,0.0268867,-1.55139e-05,4.36434e-09,-4.78585e-13,24163.8,8.51631], Tmin=(612.399,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (200.836,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 216,
    label = "[N-]([NH+]DO)[O]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 O u1 p2 c0 {4,S}
3 N u0 p0 c+1 {1,D} {4,S} {5,S}
4 N u0 p2 c-1 {2,S} {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9561,0.00273208,5.06544e-05,-1.08548e-07,6.97898e-11,20314.5,8.46109], Tmin=(10,'K'), Tmax=(518.833,'K')),
            NASAPolynomial(coeffs=[3.61186,0.0145223,-9.84612e-06,3.13104e-09,-3.76964e-13,20227.2,8.71095], Tmin=(518.833,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (168.89,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 217,
    label = "C[CH]CDN",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {4,D} {10,S}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3  C u1 p0 c0 {2,S} {4,S} {8,S}
4  C u0 p0 c0 {1,D} {3,S} {9,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96413,0.00230059,0.000101496,-1.94646e-07,1.22563e-10,18328.2,8.2798], Tmin=(10,'K'), Tmax=(407.314,'K')),
            NASAPolynomial(coeffs=[0.574405,0.035596,-2.11443e-05,6.12594e-09,-6.91165e-13,18604.3,21.588], Tmin=(407.314,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (152.38,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 218,
    label = "CNDCDO",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,S} {4,D}
3 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,D} {2,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75366,0.0276275,-0.000119283,3.18104e-07,-2.79985e-10,-14618.7,7.62215], Tmin=(10,'K'), Tmax=(405.307,'K')),
            NASAPolynomial(coeffs=[2.07411,0.021441,-1.2147e-05,3.31889e-09,-3.52271e-13,-14295.6,16.5146], Tmin=(405.307,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-121.557,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 219,
    label = "CNN",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {7,S}
2 N u0 p1 c0 {1,S} {8,S} {9,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96661,0.00184819,6.35207e-05,-9.92714e-08,5.03463e-11,9805.85,6.08273], Tmin=(10,'K'), Tmax=(508.922,'K')),
            NASAPolynomial(coeffs=[0.562504,0.0286073,-1.53603e-05,4.07381e-09,-4.27406e-13,10152.3,20.2058], Tmin=(508.922,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (81.5128,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 220,
    label = "[O-][NH+]DCCD[N]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {4,D} {7,S}
3 N u1 p1 c0 {5,D}
4 C u0 p0 c0 {2,D} {5,S} {6,S}
5 C u0 p0 c0 {3,D} {4,S} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91227,0.00757216,7.85584e-05,-1.94216e-07,1.53976e-10,36207,9.6869], Tmin=(10,'K'), Tmax=(323.024,'K')),
            NASAPolynomial(coeffs=[2.22866,0.0284202,-1.82511e-05,5.58119e-09,-6.52884e-13,36315.8,15.9069], Tmin=(323.024,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (301.046,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 221,
    label = "[O-][NH+]DNN",
    molecule = 
"""
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {4,S} {6,S} {7,S}
3 N u0 p0 c+1 {1,S} {4,D} {5,S}
4 N u0 p1 c0 {2,S} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08229,-0.00823301,0.000119601,-2.22855e-07,1.35019e-10,19113.7,8.16449], Tmin=(10,'K'), Tmax=(523.104,'K')),
            NASAPolynomial(coeffs=[1.99675,0.0231278,-1.45241e-05,4.40707e-09,-5.13769e-13,19121,14.8589], Tmin=(523.104,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (158.91,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 222,
    label = "NDNNDO",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,D} {4,S}
3 N u0 p1 c0 {2,D} {5,S}
4 N u0 p1 c0 {1,D} {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82752,0.0173146,-3.24316e-05,5.69312e-08,-4.38648e-11,38539.9,8.2833], Tmin=(10,'K'), Tmax=(387.161,'K')),
            NASAPolynomial(coeffs=[4.04254,0.0131209,-8.54277e-06,2.639e-09,-3.10995e-13,38538,7.64087], Tmin=(387.161,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (320.437,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 223,
    label = "[CH2]NOO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {8,S}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 C u1 p0 c0 {3,S} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91087,0.00928493,0.000151086,-6.84505e-07,9.90697e-10,6494.32,9.08845], Tmin=(10,'K'), Tmax=(220.856,'K')),
            NASAPolynomial(coeffs=[3.56123,0.0247128,-1.54696e-05,4.72352e-09,-5.57299e-13,6487.58,9.74502], Tmin=(220.856,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (54.0252,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 224,
    label = "ODNNDO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,D} {4,S}
4 N u0 p1 c0 {2,D} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72036,0.0243053,-6.77203e-05,9.81251e-08,-5.35627e-11,22627.8,7.7416], Tmin=(10,'K'), Tmax=(542.08,'K')),
            NASAPolynomial(coeffs=[5.30196,0.00704457,-4.48915e-06,1.33771e-09,-1.52126e-13,22538.5,1.83735], Tmin=(542.08,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (188.122,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 225,
    label = "OC[CH]NDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {9,S}
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {2,D} {5,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 C u1 p0 c0 {3,S} {4,S} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82574,0.0160832,3.01348e-05,-5.93285e-08,2.93283e-11,-5438.51,10.3884], Tmin=(10,'K'), Tmax=(695.648,'K')),
            NASAPolynomial(coeffs=[3.17891,0.0289298,-1.72469e-05,4.94028e-09,-5.4659e-13,-5569.36,11.6868], Tmin=(695.648,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-45.2359,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 226,
    label = "CCDCN",
    molecule = 
"""
1  N u0 p1 c0 {4,S} {10,S} {11,S}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u0 p0 c0 {1,S} {3,D} {9,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87967,0.00965216,7.11595e-05,-1.30906e-07,7.53231e-11,1574.01,7.71595], Tmin=(10,'K'), Tmax=(450.25,'K')),
            NASAPolynomial(coeffs=[0.757531,0.0373888,-2.12435e-05,5.90986e-09,-6.42528e-13,1855.16,20.2872], Tmin=(450.25,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (13.0664,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 227,
    label = "ODNC#[C]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u1 p0 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77374,0.0161194,-2.59905e-05,2.31723e-08,-8.15597e-12,74226.3,7.54427], Tmin=(10,'K'), Tmax=(820.675,'K')),
            NASAPolynomial(coeffs=[4.9662,0.00732967,-4.4825e-06,1.27943e-09,-1.40017e-13,74130.9,2.63792], Tmin=(820.675,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (617.112,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 228,
    label = "CND[C]N",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {4,S} {8,S} {9,S}
2 N u0 p1 c0 {3,S} {4,D}
3 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
4 C u1 p0 c0 {1,S} {2,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74469,0.0232177,-9.94457e-06,1.18729e-09,1.67453e-13,27161.6,7.77021], Tmin=(10,'K'), Tmax=(1591.25,'K')),
            NASAPolynomial(coeffs=[9.42216,0.0133808,-4.85225e-06,8.05265e-10,-4.76938e-14,24793.2,-24.0218], Tmin=(1591.25,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (225.788,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 229,
    label = "NOC#[C]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u1 p0 c0 {3,T}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74644,0.0218566,-3.14194e-05,3.35051e-08,-1.57531e-11,68983.3,8.82046], Tmin=(10,'K'), Tmax=(575.799,'K')),
            NASAPolynomial(coeffs=[4.57028,0.0146089,-8.56686e-06,2.44774e-09,-2.72053e-13,68913.7,5.52014], Tmin=(575.799,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (573.538,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 230,
    label = "NNC#[C]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {5,S}
2 N u0 p1 c0 {1,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u1 p0 c0 {3,T}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92716,0.00747453,0.000141394,-6.86192e-07,1.04312e-09,74859.3,8.59345], Tmin=(10,'K'), Tmax=(219.207,'K')),
            NASAPolynomial(coeffs=[3.89331,0.0189292,-1.11444e-05,3.2438e-09,-3.69349e-13,74834.7,8.11149], Tmin=(219.207,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (622.441,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 231,
    label = "ON[CH]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {7,S}
2 O u0 p2 c0 {4,S} {8,S}
3 N u0 p1 c0 {1,S} {4,S} {6,S}
4 C u1 p0 c0 {2,S} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92493,0.00453401,8.66662e-05,-1.77642e-07,1.0953e-10,-7608.45,9.14652], Tmin=(10,'K'), Tmax=(542.889,'K')),
            NASAPolynomial(coeffs=[3.38817,0.0251249,-1.61916e-05,5.11279e-09,-6.2162e-13,-7795.32,9.15036], Tmin=(542.889,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-63.2876,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 232,
    label = "CONN",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  N u0 p1 c0 {1,S} {3,S} {8,S}
3  N u0 p1 c0 {2,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  H u0 p0 c0 {4,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83966,0.0155267,2.26453e-05,-3.57313e-08,1.39518e-11,4667.56,7.68954], Tmin=(10,'K'), Tmax=(873.499,'K')),
            NASAPolynomial(coeffs=[2.30409,0.0303939,-1.63405e-05,4.29235e-09,-4.42275e-13,4636.9,13.1791], Tmin=(873.499,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (38.8058,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 233,
    label = "[N-]([NH+]DO)N[O]",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,S} {5,S} {7,S}
4 N u0 p0 c+1 {2,D} {5,S} {6,S}
5 N u0 p2 c-1 {3,S} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93488,0.00392705,7.86405e-05,-1.59781e-07,9.76942e-11,28843.8,9.7768], Tmin=(10,'K'), Tmax=(542.545,'K')),
            NASAPolynomial(coeffs=[3.15015,0.0239677,-1.61786e-05,5.15915e-09,-6.24098e-13,28719.1,11.1493], Tmin=(542.545,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (239.797,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 234,
    label = "[O-][N+]DCCDC",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u1 p0 c+1 {1,S} {4,D}
3 C u0 p0 c0 {4,S} {5,D} {6,S}
4 C u0 p0 c0 {2,D} {3,S} {7,S}
5 C u0 p0 c0 {3,D} {8,S} {9,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93054,0.00601863,0.000107863,-2.70409e-07,2.2249e-10,23230.9,9.68793], Tmin=(10,'K'), Tmax=(309.973,'K')),
            NASAPolynomial(coeffs=[1.86963,0.0326135,-2.08341e-05,6.38392e-09,-7.50121e-13,23358.7,17.2167], Tmin=(309.973,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (193.163,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 235,
    label = "CCN[NH]",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {3,S} {10,S}
2  N u1 p1 c0 {1,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87344,0.0111163,5.7375e-05,-9.66452e-08,4.92722e-11,20231.7,8.23766], Tmin=(10,'K'), Tmax=(514.562,'K')),
            NASAPolynomial(coeffs=[0.372236,0.0383336,-2.19674e-05,6.1523e-09,-6.72629e-13,20592,22.8026], Tmin=(514.562,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (168.203,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 236,
    label = "CC#N",
    molecule = 
"""
1 N u0 p1 c0 {3,T}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,T} {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9933,0.00022774,3.96937e-05,-6.125e-08,3.0894e-11,7572.57,5.04522], Tmin=(10,'K'), Tmax=(510.949,'K')),
            NASAPolynomial(coeffs=[1.87079,0.0168442,-9.08779e-06,2.39877e-09,-2.48738e-13,7789.47,13.8599], Tmin=(510.949,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (62.9552,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 237,
    label = "ONND[CH]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 N u0 p1 c0 {1,S} {3,S} {5,S}
3 N u0 p1 c0 {2,S} {4,D}
4 C u1 p0 c0 {3,D} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93653,0.0038686,7.43141e-05,-1.53965e-07,9.61083e-11,40325.3,8.67627], Tmin=(10,'K'), Tmax=(534.906,'K')),
            NASAPolynomial(coeffs=[3.44064,0.0214394,-1.38327e-05,4.34421e-09,-5.2506e-13,40180.1,8.90457], Tmin=(534.906,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (335.262,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 238,
    label = "[NH]NCDN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u1 p1 c0 {1,S} {7,S}
3 N u0 p1 c0 {4,D} {8,S}
4 C u0 p0 c0 {1,S} {3,D} {6,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96816,0.00189733,7.42461e-05,-1.32475e-07,7.49117e-11,32565.4,8.53353], Tmin=(10,'K'), Tmax=(524.922,'K')),
            NASAPolynomial(coeffs=[1.19307,0.0286928,-1.84657e-05,5.77202e-09,-6.93791e-13,32778.9,19.3919], Tmin=(524.922,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (270.752,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 239,
    label = "CCCD[N]",
    molecule = 
"""
multiplicity 2
1  N u1 p1 c0 {4,D}
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
            NASAPolynomial(coeffs=[3.9098,0.0130888,2.8719e-05,-3.98231e-08,1.44879e-11,19304.6,7.89774], Tmin=(10,'K'), Tmax=(945.892,'K')),
            NASAPolynomial(coeffs=[2.53417,0.0300605,-1.58835e-05,4.07985e-09,-4.1076e-13,19065.9,11.8202], Tmin=(945.892,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (160.531,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 240,
    label = "[NH]CO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {7,S}
2 N u1 p1 c0 {3,S} {6,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98049,0.00124798,6.29555e-05,-1.18804e-07,7.33857e-11,-1107.61,7.7231], Tmin=(10,'K'), Tmax=(416.679,'K')),
            NASAPolynomial(coeffs=[1.76713,0.0225276,-1.37637e-05,4.12745e-09,-4.81141e-13,-923.438,16.4603], Tmin=(416.679,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-9.21376,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 241,
    label = "C[N]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 N u1 p1 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97698,0.00140649,5.64671e-05,-1.01487e-07,5.96817e-11,6505.19,6.76767], Tmin=(10,'K'), Tmax=(436.755,'K')),
            NASAPolynomial(coeffs=[1.78918,0.0214384,-1.2314e-05,3.47552e-09,-3.84337e-13,6696.34,15.5107], Tmin=(436.755,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (54.0779,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 242,
    label = "[O-][NH+]NO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {7,S}
2 O u0 p3 c-1 {4,S}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 N u1 p0 c+1 {2,S} {3,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92901,0.00475171,8.12136e-05,-1.92365e-07,1.37957e-10,11583.9,9.26556], Tmin=(10,'K'), Tmax=(465.053,'K')),
            NASAPolynomial(coeffs=[3.59762,0.0208138,-1.32072e-05,4.07809e-09,-4.8455e-13,11471.8,9.07457], Tmin=(465.053,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (96.3022,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 243,
    label = "[CH]DNCDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 N u0 p1 c0 {3,S} {4,D}
3 C u0 p0 c0 {1,D} {2,S} {5,S}
4 C u1 p0 c0 {2,D} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85837,0.0117427,6.22842e-06,-1.6969e-08,8.04137e-12,18538.1,8.61904], Tmin=(10,'K'), Tmax=(768.583,'K')),
            NASAPolynomial(coeffs=[3.66072,0.0162971,-9.54138e-06,2.67835e-09,-2.9088e-13,18464.4,8.84307], Tmin=(768.583,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (154.119,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 244,
    label = "CNC#N",
    molecule = 
"""
1 N u0 p1 c0 {3,S} {4,S} {8,S}
2 N u0 p1 c0 {4,T}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {2,T}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8487,0.011624,2.74254e-05,-5.75627e-08,3.43472e-11,15577.1,7.13965], Tmin=(10,'K'), Tmax=(438.933,'K')),
            NASAPolynomial(coeffs=[2.56093,0.0233594,-1.26789e-05,3.34901e-09,-3.45876e-13,15690.1,12.292], Tmin=(438.933,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (129.486,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 245,
    label = "[CH2]NCN",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {3,S} {4,S} {7,S}
2  N u0 p1 c0 {3,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4  C u1 p0 c0 {1,S} {10,S} {11,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94583,0.00372447,0.000128447,-2.81842e-07,2.00592e-10,17501.7,8.61289], Tmin=(10,'K'), Tmax=(419.004,'K')),
            NASAPolynomial(coeffs=[1.36393,0.0370194,-2.17017e-05,6.30699e-09,-7.19199e-13,17642.2,17.9174], Tmin=(419.004,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (145.515,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 246,
    label = "NND[C]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {7,S}
2 N u0 p1 c0 {3,S} {5,S} {6,S}
3 N u0 p1 c0 {2,S} {4,D}
4 C u1 p0 c0 {1,S} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90869,0.00714744,8.99218e-05,-2.72453e-07,2.4806e-10,21878.6,8.50137], Tmin=(10,'K'), Tmax=(371.359,'K')),
            NASAPolynomial(coeffs=[3.94504,0.0195799,-1.20948e-05,3.678e-09,-4.33655e-13,21787.4,7.17142], Tmin=(371.359,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (181.918,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 247,
    label = "[O-][N+]DO",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 O u0 p2 c0 {3,D}
3 N u1 p0 c+1 {1,S} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03095,-0.00203232,1.72031e-05,-2.12688e-08,8.37285e-12,2699.81,6.59491], Tmin=(10,'K'), Tmax=(803.463,'K')),
            NASAPolynomial(coeffs=[3.03027,0.00611308,-3.90979e-06,1.14997e-09,-1.27639e-13,2758.5,10.5682], Tmin=(803.463,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (22.4549,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 248,
    label = "[O-][NH+]DCN[NH]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {4,S} {5,S} {7,S}
3 N u0 p0 c+1 {1,S} {5,D} {8,S}
4 N u1 p1 c0 {2,S} {9,S}
5 C u0 p0 c0 {2,S} {3,D} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91864,0.00502971,0.000104182,-2.16288e-07,1.36698e-10,32363.2,9.95674], Tmin=(10,'K'), Tmax=(520.416,'K')),
            NASAPolynomial(coeffs=[2.8109,0.0307855,-1.975e-05,6.13392e-09,-7.32561e-13,32245,12.3342], Tmin=(520.416,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (269.057,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 249,
    label = "NNNDN",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {5,S}
2 N u0 p1 c0 {1,S} {6,S} {7,S}
3 N u0 p1 c0 {1,S} {4,D}
4 N u0 p1 c0 {3,D} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96132,0.00239885,7.76284e-05,-1.49694e-07,9.14886e-11,37472.3,8.14435], Tmin=(10,'K'), Tmax=(500.143,'K')),
            NASAPolynomial(coeffs=[1.90734,0.0262361,-1.60867e-05,4.84682e-09,-5.67406e-13,37585,15.704], Tmin=(500.143,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (311.55,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 250,
    label = "[O-][NH+]DN[N]C",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {4,D} {9,S}
3 N u1 p1 c0 {4,S} {5,S}
4 N u0 p1 c0 {2,D} {3,S}
5 C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81818,0.0156013,5.20669e-05,-1.46857e-07,1.2316e-10,32916.2,8.73643], Tmin=(10,'K'), Tmax=(307.181,'K')),
            NASAPolynomial(coeffs=[2.71644,0.0299477,-1.79879e-05,5.18085e-09,-5.75792e-13,32983.9,12.7513], Tmin=(307.181,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (273.67,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 251,
    label = "[O-][NH+]D[CH]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {4,S}
3 C u1 p0 c0 {2,D} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84686,0.0171644,-7.29211e-05,1.96614e-07,-1.77029e-10,39908.5,7.62172], Tmin=(10,'K'), Tmax=(393.597,'K')),
            NASAPolynomial(coeffs=[2.97515,0.0130285,-7.63584e-06,2.15351e-09,-2.35078e-13,40077.8,12.2931], Tmin=(393.597,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (331.811,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 252,
    label = "[CH2]NNDN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {2,D} {8,S}
4 C u1 p0 c0 {1,S} {6,S} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94287,0.00337495,8.01071e-05,-1.52949e-07,8.9447e-11,44881,7.7303], Tmin=(10,'K'), Tmax=(554.586,'K')),
            NASAPolynomial(coeffs=[2.51553,0.0264624,-1.69386e-05,5.30295e-09,-6.40484e-13,44842.6,12.0012], Tmin=(554.586,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (373.139,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 253,
    label = "OOCDN",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {7,S}
3 N u0 p1 c0 {4,D} {6,S}
4 C u0 p0 c0 {1,S} {3,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96295,0.00213001,6.40551e-05,-1.13784e-07,6.25545e-11,-8852.67,7.85992], Tmin=(10,'K'), Tmax=(569.052,'K')),
            NASAPolynomial(coeffs=[1.91714,0.0245585,-1.628e-05,5.18531e-09,-6.30608e-13,-8750.14,15.4314], Tmin=(569.052,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-73.6216,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 254,
    label = "NCD[N]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {4,S} {5,S}
2 N u1 p1 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98423,0.000941626,4.51489e-05,-7.78781e-08,4.34497e-11,26322.7,6.92077], Tmin=(10,'K'), Tmax=(463.615,'K')),
            NASAPolynomial(coeffs=[1.95241,0.0184608,-1.14978e-05,3.52724e-09,-4.19768e-13,26511.2,15.1625], Tmin=(463.615,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (218.853,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 255,
    label = "OCD[N]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 N u1 p1 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05991,-0.00534458,6.44407e-05,-1.09142e-07,6.03927e-11,5176.57,7.20182], Tmin=(10,'K'), Tmax=(565.773,'K')),
            NASAPolynomial(coeffs=[2.48473,0.0139983,-8.59891e-06,2.55931e-09,-2.93601e-13,5223.47,12.7433], Tmin=(565.773,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (43.0375,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 256,
    label = "[N-]([NH+]DO)[C]DN",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 N u0 p0 c+1 {1,D} {3,S} {6,S}
3 N u0 p2 c-1 {2,S} {5,S}
4 N u0 p1 c0 {5,D} {7,S}
5 C u1 p0 c0 {3,S} {4,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88522,0.00798255,9.59617e-05,-2.58724e-07,2.0203e-10,39356,9.97695], Tmin=(10,'K'), Tmax=(447.789,'K')),
            NASAPolynomial(coeffs=[4.69338,0.0207559,-1.37972e-05,4.3906e-09,-5.32727e-13,39083.1,4.48923], Tmin=(447.789,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (327.213,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 257,
    label = "[NH]OOO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 N u1 p1 c0 {1,S} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9026,0.00641344,7.68405e-05,-1.96228e-07,1.43049e-10,22787.2,9.2336], Tmin=(10,'K'), Tmax=(486.854,'K')),
            NASAPolynomial(coeffs=[5.03342,0.0160033,-1.08779e-05,3.54486e-09,-4.38865e-13,22453.3,2.29392], Tmin=(486.854,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (189.443,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 258,
    label = "[NH]OC#C",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u1 p1 c0 {1,S} {5,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {3,T} {6,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9177,0.00511839,6.91906e-05,-1.60241e-07,1.06965e-10,51059.5,8.212], Tmin=(10,'K'), Tmax=(528.476,'K')),
            NASAPolynomial(coeffs=[4.90653,0.0153536,-1.01549e-05,3.2983e-09,-4.12244e-13,50707.5,1.73098], Tmin=(528.476,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (424.507,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 259,
    label = "ODC[N-][NH+]DO",
    molecule = 
"""
1 O u0 p2 c0 {5,D}
2 O u0 p2 c0 {3,D}
3 N u0 p0 c+1 {2,D} {4,S} {6,S}
4 N u0 p2 c-1 {3,S} {5,S}
5 C u0 p0 c0 {1,D} {4,S} {7,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90263,0.00797386,4.30982e-05,-8.87567e-08,5.54335e-11,-751.066,9.14833], Tmin=(10,'K'), Tmax=(416.872,'K')),
            NASAPolynomial(coeffs=[2.21288,0.0241875,-1.52422e-05,4.54202e-09,-5.18107e-13,-610.183,15.8219], Tmin=(416.872,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-6.25532,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 260,
    label = "[CH2]CDN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 C u1 p0 c0 {2,S} {5,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10724,-0.00948647,0.00010684,-1.79437e-07,9.91409e-11,23337.1,6.64579], Tmin=(10,'K'), Tmax=(561.222,'K')),
            NASAPolynomial(coeffs=[1.30942,0.0230766,-1.39281e-05,4.0961e-09,-4.66193e-13,23452.4,16.7566], Tmin=(561.222,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (194.033,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 261,
    label = "[CH2]NNDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 N u0 p1 c0 {3,S} {4,S} {5,S}
3 N u0 p1 c0 {1,D} {2,S}
4 C u1 p0 c0 {2,S} {6,S} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94395,0.00325211,7.00247e-05,-1.33499e-07,7.67966e-11,26429,7.70421], Tmin=(10,'K'), Tmax=(574.335,'K')),
            NASAPolynomial(coeffs=[2.98827,0.0229073,-1.52597e-05,4.90463e-09,-6.02317e-13,26324.4,9.91838], Tmin=(574.335,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (219.72,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 262,
    label = "ON[CH]NDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {8,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,S} {5,S} {7,S}
4 N u0 p1 c0 {2,D} {5,S}
5 C u1 p0 c0 {3,S} {4,S} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89079,0.00771442,0.000107652,-2.80403e-07,2.18043e-10,17392.9,9.94671], Tmin=(10,'K'), Tmax=(434.956,'K')),
            NASAPolynomial(coeffs=[3.86148,0.025911,-1.69251e-05,5.29813e-09,-6.33726e-13,17225.8,8.11433], Tmin=(434.956,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (144.605,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 263,
    label = "NNNDO",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,S} {4,S} {5,S}
3 N u0 p1 c0 {2,S} {6,S} {7,S}
4 N u0 p1 c0 {1,D} {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95621,0.00334495,8.06885e-05,-1.99841e-07,1.59865e-10,19787.9,8.24802], Tmin=(10,'K'), Tmax=(374.103,'K')),
            NASAPolynomial(coeffs=[2.70091,0.0218064,-1.35405e-05,4.08702e-09,-4.76244e-13,19846.6,12.5986], Tmin=(374.103,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (164.531,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 264,
    label = "[N-]([N+]DO)OC",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {4,D}
3 N u0 p2 c-1 {1,S} {4,S}
4 N u1 p0 c+1 {2,D} {3,S}
5 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72529,0.027806,-5.48724e-05,1.26386e-07,-1.12446e-10,20548.1,9.01811], Tmin=(10,'K'), Tmax=(402.23,'K')),
            NASAPolynomial(coeffs=[2.83059,0.0272003,-1.71738e-05,5.16492e-09,-5.95377e-13,20697,13.4753], Tmin=(402.23,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (170.84,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 265,
    label = "[O-][N+]DN",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u1 p0 c+1 {1,S} {3,D}
3 N u0 p1 c0 {2,D} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05263,-0.00401574,3.80164e-05,-5.47884e-08,2.56608e-11,23743.3,6.73271], Tmin=(10,'K'), Tmax=(666.618,'K')),
            NASAPolynomial(coeffs=[2.60377,0.0101672,-6.24916e-06,1.83298e-09,-2.06258e-13,23814.5,12.2203], Tmin=(666.618,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (197.418,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 266,
    label = "[O-][N+]#CND[N]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {4,D} {5,S}
3 N u0 p0 c+1 {1,S} {5,T}
4 N u1 p1 c0 {2,D}
5 C u0 p0 c0 {2,S} {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62745,0.0267938,-4.41365e-05,3.82816e-08,-1.3001e-11,62333,9.43671], Tmin=(10,'K'), Tmax=(828.683,'K')),
            NASAPolynomial(coeffs=[6.27368,0.00993053,-6.20883e-06,1.81326e-09,-2.02292e-13,62034.9,-1.98521], Tmin=(828.683,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (518.201,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 267,
    label = "CNC#[C]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {8,S}
2 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u1 p0 c0 {3,T}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7648,0.0226724,-3.5833e-05,7.26085e-08,-5.65216e-11,60233.8,7.91404], Tmin=(10,'K'), Tmax=(474.946,'K')),
            NASAPolynomial(coeffs=[2.56993,0.0242087,-1.37549e-05,3.81704e-09,-4.13872e-13,60443.4,13.8014], Tmin=(474.946,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (500.805,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 268,
    label = "N[CH]CDN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {7,S} {8,S}
2 N u0 p1 c0 {4,D} {9,S}
3 C u1 p0 c0 {1,S} {4,S} {5,S}
4 C u0 p0 c0 {2,D} {3,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94755,0.00308245,8.77255e-05,-1.61063e-07,9.19151e-11,18814.5,8.55313], Tmin=(10,'K'), Tmax=(551.833,'K')),
            NASAPolynomial(coeffs=[1.62232,0.0312938,-1.9829e-05,6.16699e-09,-7.41558e-13,18898.2,16.8219], Tmin=(551.833,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (156.411,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 269,
    label = "NND[C]N",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {5,S} {6,S}
2 N u0 p1 c0 {4,S} {7,S} {8,S}
3 N u0 p1 c0 {1,S} {4,D}
4 C u1 p0 c0 {2,S} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90833,0.00639743,9.92784e-05,-2.55959e-07,1.98732e-10,41958.6,8.52496], Tmin=(10,'K'), Tmax=(436.501,'K')),
            NASAPolynomial(coeffs=[3.98202,0.0224581,-1.34246e-05,4.00961e-09,-4.69584e-13,41792.7,6.40418], Tmin=(436.501,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (348.857,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 270,
    label = "[CH2]NCO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {10,S}
2  N u0 p1 c0 {3,S} {4,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4  C u1 p0 c0 {2,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94259,0.0038094,0.000113029,-2.41392e-07,1.6445e-10,-5339.8,8.57959], Tmin=(10,'K'), Tmax=(450.958,'K')),
            NASAPolynomial(coeffs=[1.75054,0.0335358,-2.00522e-05,5.91079e-09,-6.80257e-13,-5246.65,16.25], Tmin=(450.958,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-44.406,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 271,
    label = "[O-][NH+]NN",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {3,S} {4,S} {5,S}
3 N u1 p0 c+1 {1,S} {2,S} {6,S}
4 N u0 p1 c0 {2,S} {7,S} {8,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94715,0.00354117,8.87106e-05,-1.96488e-07,1.37144e-10,27697.2,9.56686], Tmin=(10,'K'), Tmax=(450.578,'K')),
            NASAPolynomial(coeffs=[2.57591,0.0252654,-1.54069e-05,4.60725e-09,-5.34647e-13,27723.8,14.0132], Tmin=(450.578,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (230.281,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 272,
    label = "C[N]N",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {7,S} {8,S}
2 N u1 p1 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97059,0.00175716,6.28023e-05,-1.09514e-07,6.25496e-11,23245.3,6.718], Tmin=(10,'K'), Tmax=(449.457,'K')),
            NASAPolynomial(coeffs=[1.40168,0.0246184,-1.34901e-05,3.64283e-09,-3.87967e-13,23476.2,17.0572], Tmin=(449.457,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (193.258,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 273,
    label = "O[CH]NDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {6,S}
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {2,D} {4,S}
4 C u1 p0 c0 {1,S} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95107,0.00304088,6.12127e-05,-1.28646e-07,8.20699e-11,-4303.85,8.78202], Tmin=(10,'K'), Tmax=(517.068,'K')),
            NASAPolynomial(coeffs=[3.35688,0.017894,-1.16294e-05,3.63283e-09,-4.34435e-13,-4379.51,9.93091], Tmin=(517.068,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-35.7995,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 274,
    label = "[O]NCDO",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 C u0 p0 c0 {2,D} {3,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97291,0.00179461,6.05189e-05,-1.26747e-07,8.49495e-11,-11256.1,8.62391], Tmin=(10,'K'), Tmax=(446.62,'K')),
            NASAPolynomial(coeffs=[2.54886,0.0189654,-1.19845e-05,3.62109e-09,-4.20004e-13,-11173,13.8531], Tmin=(446.62,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-93.5926,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 275,
    label = "OCND[CH]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {7,S}
2 N u0 p1 c0 {3,S} {4,D}
3 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4 C u1 p0 c0 {2,D} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84908,0.0130561,2.25345e-05,-4.34862e-08,2.133e-11,10646.8,9.11307], Tmin=(10,'K'), Tmax=(671.195,'K')),
            NASAPolynomial(coeffs=[2.73869,0.0246019,-1.42824e-05,4.02219e-09,-4.4022e-13,10684.9,13.2004], Tmin=(671.195,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (88.5057,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 276,
    label = "[O-][NH+]DCNC",
    molecule = 
"""
1  O u0 p3 c-1 {3,S}
2  N u0 p1 c0 {4,S} {5,S} {9,S}
3  N u0 p0 c+1 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {2,S} {3,D} {10,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79778,0.0201528,2.30679e-05,-4.07872e-08,1.66435e-11,3781.32,8.45927], Tmin=(10,'K'), Tmax=(862.872,'K')),
            NASAPolynomial(coeffs=[2.90822,0.0342766,-1.88686e-05,5.04465e-09,-5.26764e-13,3562.56,10.4625], Tmin=(862.872,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (31.4376,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 277,
    label = "NCDC",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u0 p0 c0 {2,D} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09257,-0.00908102,0.000126496,-2.36016e-07,1.46609e-10,5005.96,6.8158], Tmin=(10,'K'), Tmax=(489.521,'K')),
            NASAPolynomial(coeffs=[1.23981,0.0256571,-1.49659e-05,4.32483e-09,-4.88508e-13,5148.34,17.1424], Tmin=(489.521,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (41.6166,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 278,
    label = "[NH]CC#C",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {8,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9339,0.00726456,0.000159271,-7.72795e-07,1.29944e-09,50103.5,9.30058], Tmin=(10,'K'), Tmax=(149.473,'K')),
            NASAPolynomial(coeffs=[3.28496,0.0246304,-1.4997e-05,4.44847e-09,-5.11185e-13,50122.9,11.1979], Tmin=(149.473,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (416.753,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 279,
    label = "N[C]DC",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {4,S} {5,S}
2 C u0 p0 c0 {3,D} {6,S} {7,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96083,0.00244012,6.43319e-05,-1.28644e-07,8.06555e-11,32380.4,7.06941], Tmin=(10,'K'), Tmax=(505.212,'K')),
            NASAPolynomial(coeffs=[2.76385,0.0200013,-1.18101e-05,3.50351e-09,-4.09679e-13,32398.2,11.0058], Tmin=(505.212,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (269.214,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 280,
    label = "[O]ONDN",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 N u0 p1 c0 {1,S} {4,D}
4 N u0 p1 c0 {3,D} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88718,0.0105816,3.88069e-05,-1.69943e-07,1.93652e-10,35222.1,8.69246], Tmin=(10,'K'), Tmax=(313.41,'K')),
            NASAPolynomial(coeffs=[4.17648,0.0137855,-9.53354e-06,3.09304e-09,-3.78838e-13,35170.1,7.09204], Tmin=(313.41,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (292.866,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 281,
    label = "[O-][NH+]DCOC",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p3 c-1 {3,S}
3  N u0 p0 c+1 {2,S} {5,D} {10,S}
4  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {3,D} {9,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86223,0.0193449,1.42047e-05,-2.617e-08,9.73899e-12,-11706.6,8.28398], Tmin=(10,'K'), Tmax=(1008.02,'K')),
            NASAPolynomial(coeffs=[4.60305,0.0274876,-1.44038e-05,3.6576e-09,-3.63629e-13,-12419,1.91121], Tmin=(1008.02,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-97.3098,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 282,
    label = "COCN",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {4,S}
2  N u0 p1 c0 {3,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.865,0.0163733,2.26885e-05,-3.17312e-08,1.08692e-11,-22985.3,7.31556], Tmin=(10,'K'), Tmax=(1026,'K')),
            NASAPolynomial(coeffs=[2.69172,0.0319658,-1.62163e-05,4.01496e-09,-3.91282e-13,-23324.5,10.1798], Tmin=(1026,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-191.097,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 283,
    label = "[O-][N+]#CNDO",
    molecule = 
"""
1 O u0 p3 c-1 {4,S}
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {2,D} {5,S}
4 N u0 p0 c+1 {1,S} {5,T}
5 C u0 p0 c0 {3,S} {4,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82563,0.0157353,2.79749e-05,-1.57228e-07,1.77361e-10,39544.4,8.77617], Tmin=(10,'K'), Tmax=(349.669,'K')),
            NASAPolynomial(coeffs=[4.93326,0.0138331,-1.00588e-05,3.35743e-09,-4.18311e-13,39401.1,3.65502], Tmin=(349.669,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (328.804,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 284,
    label = "NDO",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01617,-0.000914049,3.04985e-06,3.18971e-09,-4.10436e-12,11516.1,3.76803], Tmin=(10,'K'), Tmax=(661.294,'K')),
            NASAPolynomial(coeffs=[2.48686,0.00484242,-2.0822e-06,3.73808e-10,-1.93565e-14,11794.8,11.0912], Tmin=(661.294,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (95.7572,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 285,
    label = "NCCDN",
    molecule = 
"""
1  N u0 p1 c0 {3,S} {8,S} {9,S}
2  N u0 p1 c0 {4,D} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {2,D} {3,S} {7,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89818,0.0110523,3.768e-05,-5.40265e-08,2.16478e-11,6928.63,8.45382], Tmin=(10,'K'), Tmax=(817.672,'K')),
            NASAPolynomial(coeffs=[1.48968,0.0319911,-1.75291e-05,4.6821e-09,-4.89373e-13,7016.4,17.7169], Tmin=(817.672,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (57.613,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 286,
    label = "C[N]C#N",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {3,S} {4,S}
2 N u0 p1 c0 {4,T}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {2,T}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80676,0.021311,-6.75031e-05,1.92701e-07,-1.81127e-10,35718.1,7.87172], Tmin=(10,'K'), Tmax=(396.7,'K')),
            NASAPolynomial(coeffs=[2.17212,0.0223917,-1.3353e-05,3.83132e-09,-4.25125e-13,35969,15.774], Tmin=(396.7,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (296.969,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 287,
    label = "[O-][NH+]ON",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p3 c-1 {3,S}
3 N u1 p0 c+1 {1,S} {2,S} {5,S}
4 N u0 p1 c0 {1,S} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93405,0.00493405,8.21941e-05,-2.11663e-07,1.69731e-10,18183.1,9.09045], Tmin=(10,'K'), Tmax=(398.832,'K')),
            NASAPolynomial(coeffs=[3.16381,0.0215265,-1.35607e-05,4.14293e-09,-4.8731e-13,18174,11.2142], Tmin=(398.832,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (151.185,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 288,
    label = "CCDNN",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {9,S} {10,S}
2  N u0 p1 c0 {1,S} {4,D}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {2,D} {3,S} {8,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96448,0.00238346,0.00010589,-2.16044e-07,1.45984e-10,13593,7.44694], Tmin=(10,'K'), Tmax=(378.095,'K')),
            NASAPolynomial(coeffs=[0.968902,0.0340771,-1.98553e-05,5.69017e-09,-6.38583e-13,13819.5,18.9851], Tmin=(378.095,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (113.014,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 289,
    label = "CDNCDC",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {4,D}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {2,D} {6,S} {7,S}
4 C u0 p0 c0 {1,D} {8,S} {9,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9683,0.00186557,7.90555e-05,-1.35063e-07,7.46384e-11,18223.5,8.02169], Tmin=(10,'K'), Tmax=(468.123,'K')),
            NASAPolynomial(coeffs=[0.364617,0.0326849,-1.9784e-05,5.81947e-09,-6.64494e-13,18560.6,22.6689], Tmin=(468.123,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (151.504,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 290,
    label = "[O-][C]D[NH+]N",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {4,S}
2 N u0 p0 c+1 {3,S} {4,D} {5,S}
3 N u0 p1 c0 {2,S} {6,S} {7,S}
4 C u1 p0 c0 {1,S} {2,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93998,0.00605725,0.000103903,-4.24004e-07,5.9149e-10,10589.9,8.85116], Tmin=(10,'K'), Tmax=(180.547,'K')),
            NASAPolynomial(coeffs=[3.31104,0.0199912,-1.1861e-05,3.44805e-09,-3.90081e-13,10612.6,10.8088], Tmin=(180.547,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (88.0809,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 291,
    label = "[O-][N+]DCDO",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 O u0 p2 c0 {4,D}
3 N u1 p0 c+1 {1,S} {4,D}
4 C u0 p0 c0 {2,D} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94144,0.00419593,4.39164e-05,-1.2744e-07,1.04984e-10,9085.67,7.83844], Tmin=(10,'K'), Tmax=(430.714,'K')),
            NASAPolynomial(coeffs=[4.46283,0.00897245,-6.216e-06,2.00421e-09,-2.44245e-13,8951.54,4.72648], Tmin=(430.714,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (75.5398,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 292,
    label = "[O-][NH+]DCDCO",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {8,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {2,S} {5,D} {7,S}
4 C u0 p0 c0 {1,S} {5,D} {6,S}
5 C u0 p0 c0 {3,D} {4,D}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79285,0.0204664,5.49916e-08,-1.35448e-08,6.49087e-12,10429.8,9.63855], Tmin=(10,'K'), Tmax=(906.292,'K')),
            NASAPolynomial(coeffs=[5.14703,0.021066,-1.18217e-05,3.19818e-09,-3.36275e-13,9914.25,1.74865], Tmin=(906.292,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (86.7119,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 293,
    label = "NDNC#C",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {5,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {3,T} {6,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94487,0.00342124,6.15863e-05,-1.32359e-07,8.53721e-11,57139,7.38345], Tmin=(10,'K'), Tmax=(521.804,'K')),
            NASAPolynomial(coeffs=[3.74203,0.016774,-1.07127e-05,3.34106e-09,-4.02575e-13,56999.6,6.69107], Tmin=(521.804,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (475.063,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 294,
    label = "[CH2]OCDN",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 N u0 p1 c0 {3,D} {8,S}
3 C u0 p0 c0 {1,S} {2,D} {5,S}
4 C u1 p0 c0 {1,S} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93694,0.00437971,9.54342e-05,-2.26115e-07,1.67737e-10,7211.06,8.08852], Tmin=(10,'K'), Tmax=(430.199,'K')),
            NASAPolynomial(coeffs=[2.85501,0.0253224,-1.5534e-05,4.65336e-09,-5.40478e-13,7203.44,11.2251], Tmin=(430.199,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (59.9523,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 295,
    label = "[N-]([NH+]DO)O[CH2]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {3,D}
3 N u0 p0 c+1 {2,D} {4,S} {6,S}
4 N u0 p2 c-1 {1,S} {3,S}
5 C u1 p0 c0 {1,S} {7,S} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86233,0.0111884,8.44172e-05,-2.34252e-07,1.91424e-10,30294.4,9.39471], Tmin=(10,'K'), Tmax=(405.834,'K')),
            NASAPolynomial(coeffs=[3.46578,0.026959,-1.77159e-05,5.54534e-09,-6.6169e-13,30228.9,9.74671], Tmin=(405.834,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (251.883,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 296,
    label = "ODNC#C",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92901,0.00467507,5.77055e-05,-1.4656e-07,1.06748e-10,46074.2,7.49981], Tmin=(10,'K'), Tmax=(485.555,'K')),
            NASAPolynomial(coeffs=[4.70539,0.0121352,-8.14526e-06,2.62376e-09,-3.22617e-13,45835.5,2.63317], Tmin=(485.555,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (383.068,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 297,
    label = "CCN",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
4  H u0 p0 c0 {2,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97065,0.00287817,6.22103e-05,-8.73315e-08,3.8746e-11,-7855.56,6.09883], Tmin=(10,'K'), Tmax=(635.618,'K')),
            NASAPolynomial(coeffs=[-0.514899,0.0341356,-1.87035e-05,5.03318e-09,-5.32006e-13,-7346.54,25.225], Tmin=(635.618,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-65.317,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 298,
    label = "[O-][N+]#CCC",
    molecule = 
"""
1  O u0 p3 c-1 {2,S}
2  N u0 p0 c+1 {1,S} {5,T}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {2,T} {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80077,0.0231093,1.39085e-06,-1.1861e-08,4.49139e-12,11141.8,8.56273], Tmin=(10,'K'), Tmax=(1130.79,'K')),
            NASAPolynomial(coeffs=[5.7846,0.0247451,-1.22576e-05,2.95281e-09,-2.79831e-13,10139.9,-3.69823], Tmin=(1130.79,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (92.6432,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 299,
    label = "NOCDN",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {6,S} {7,S}
3 N u0 p1 c0 {4,D} {8,S}
4 C u0 p0 c0 {1,S} {3,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93994,0.0123692,1.43726e-05,-2.20763e-08,7.83473e-12,3595.4,9.06528], Tmin=(10,'K'), Tmax=(1029.95,'K')),
            NASAPolynomial(coeffs=[4.31686,0.0201035,-1.02875e-05,2.55682e-09,-2.4922e-13,3029.9,4.8674], Tmin=(1029.95,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (29.9224,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 300,
    label = "[O-][NH+]DCN",
    molecule = 
"""
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {4,S} {7,S} {8,S}
3 N u0 p0 c+1 {1,S} {4,D} {6,S}
4 C u0 p0 c0 {2,S} {3,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95856,0.0024096,7.41969e-05,-1.32836e-07,7.40846e-11,3343.3,7.84219], Tmin=(10,'K'), Tmax=(557.939,'K')),
            NASAPolynomial(coeffs=[1.64445,0.027838,-1.79273e-05,5.63191e-09,-6.81108e-13,3463.96,16.4234], Tmin=(557.939,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (27.7801,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 301,
    label = "[O-][NH+]DCCDC",
    molecule = 
"""
1  O u0 p3 c-1 {2,S}
2  N u0 p0 c+1 {1,S} {3,D} {8,S}
3  C u0 p0 c0 {2,D} {4,S} {6,S}
4  C u0 p0 c0 {3,S} {5,D} {7,S}
5  C u0 p0 c0 {4,D} {9,S} {10,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95452,0.00279778,0.000105757,-1.97858e-07,1.17799e-10,11903.9,9.23428], Tmin=(10,'K'), Tmax=(499.458,'K')),
            NASAPolynomial(coeffs=[0.53466,0.0381249,-2.41811e-05,7.40343e-09,-8.72561e-13,12146.5,22.3677], Tmin=(499.458,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (98.9597,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 302,
    label = "[O-][NH+]DCO[NH]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {2,S} {5,D} {7,S}
4 N u1 p1 c0 {1,S} {8,S}
5 C u0 p0 c0 {1,S} {3,D} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91283,0.0058194,0.000101447,-2.37699e-07,1.68773e-10,26141,10.0428], Tmin=(10,'K'), Tmax=(466.972,'K')),
            NASAPolynomial(coeffs=[3.32055,0.0268766,-1.75354e-05,5.46456e-09,-6.50257e-13,26022.1,10.5832], Tmin=(466.972,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (217.334,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 303,
    label = "[O]CNDN",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {4,S}
2 N u0 p1 c0 {3,D} {4,S}
3 N u0 p1 c0 {2,D} {7,S}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9785,0.00145337,7.47824e-05,-1.52696e-07,1.02307e-10,27535.7,9.19894], Tmin=(10,'K'), Tmax=(382.531,'K')),
            NASAPolynomial(coeffs=[1.7745,0.0244957,-1.55557e-05,4.71465e-09,-5.47984e-13,27704.4,17.7144], Tmin=(382.531,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (228.944,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 304,
    label = "[O-][NH+]D[C]CN",
    molecule = 
"""
multiplicity 2
1  O u0 p3 c-1 {3,S}
2  N u0 p1 c0 {4,S} {8,S} {9,S}
3  N u0 p0 c+1 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  C u1 p0 c0 {3,D} {4,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82494,0.0156735,5.29706e-05,-1.21551e-07,8.18133e-11,35789,10.1933], Tmin=(10,'K'), Tmax=(387.235,'K')),
            NASAPolynomial(coeffs=[1.96925,0.0348422,-2.12816e-05,6.28181e-09,-7.1614e-13,35932.7,17.3854], Tmin=(387.235,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (297.557,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 305,
    label = "[CH2]NDCDC",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {4,D}
2 C u1 p0 c0 {1,S} {5,S} {6,S}
3 C u0 p0 c0 {4,D} {7,S} {8,S}
4 C u0 p0 c0 {1,D} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91895,0.00542115,9.65421e-05,-2.2853e-07,1.64496e-10,41486.4,7.73921], Tmin=(10,'K'), Tmax=(463.129,'K')),
            NASAPolynomial(coeffs=[3.55107,0.0241964,-1.47865e-05,4.44716e-09,-5.21509e-13,41353.2,7.42492], Tmin=(463.129,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (344.924,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 306,
    label = "[O-][N+]DNCN",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {4,S}
2 N u0 p1 c0 {5,S} {8,S} {9,S}
3 N u0 p1 c0 {4,D} {5,S}
4 N u1 p0 c+1 {1,S} {3,D}
5 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80256,0.0170766,2.57983e-05,-5.55544e-08,2.91734e-11,24473.8,10.4717], Tmin=(10,'K'), Tmax=(641.725,'K')),
            NASAPolynomial(coeffs=[2.93536,0.0289857,-1.72405e-05,4.94994e-09,-5.50036e-13,24451.2,13.2274], Tmin=(641.725,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (203.463,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 307,
    label = "N[CH]N",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {5,S} {6,S}
2 N u0 p1 c0 {3,S} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92755,0.00564179,6.56544e-05,-1.56226e-07,1.22175e-10,17694.2,7.42076], Tmin=(10,'K'), Tmax=(325.475,'K')),
            NASAPolynomial(coeffs=[2.5526,0.0225396,-1.22216e-05,3.28659e-09,-3.48252e-13,17783.7,12.5108], Tmin=(325.475,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (147.109,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 308,
    label = "[N-]([NH+]DO)NDN",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 N u0 p0 c+1 {1,D} {3,S} {6,S}
3 N u0 p2 c-1 {2,S} {4,S}
4 N u0 p1 c0 {3,S} {5,D}
5 N u0 p1 c0 {4,D} {7,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92193,0.00603053,5.77879e-05,-1.17099e-07,7.16866e-11,45123.7,8.90723], Tmin=(10,'K'), Tmax=(515.123,'K')),
            NASAPolynomial(coeffs=[2.53304,0.0239922,-1.54135e-05,4.68352e-09,-5.43181e-13,45171.6,13.7623], Tmin=(515.123,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (375.165,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 309,
    label = "ONNDN",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 N u0 p1 c0 {1,S} {3,S} {5,S}
3 N u0 p1 c0 {2,S} {4,D}
4 N u0 p1 c0 {3,D} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96455,0.00202801,6.28858e-05,-1.10483e-07,6.01363e-11,21965.1,7.73736], Tmin=(10,'K'), Tmax=(572.257,'K')),
            NASAPolynomial(coeffs=[1.83164,0.0245991,-1.63618e-05,5.23627e-09,-6.39466e-13,22083.8,15.7407], Tmin=(572.257,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (182.613,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 310,
    label = "CC[N]N",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {10,S} {11,S}
2  N u1 p1 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84194,0.0150066,3.50626e-05,-5.32586e-08,2.17217e-11,19314.1,8.24648], Tmin=(10,'K'), Tmax=(805.767,'K')),
            NASAPolynomial(coeffs=[1.40114,0.0357451,-1.95942e-05,5.24233e-09,-5.49184e-13,19427.5,17.758], Tmin=(805.767,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (160.581,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 311,
    label = "[NH]ONO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {3,S} {6,S}
3 N u0 p1 c0 {1,S} {2,S} {5,S}
4 N u1 p1 c0 {1,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92898,0.00448332,7.83853e-05,-1.7295e-07,1.14451e-10,22828.2,9.28817], Tmin=(10,'K'), Tmax=(508.951,'K')),
            NASAPolynomial(coeffs=[3.71406,0.0209054,-1.3436e-05,4.20308e-09,-5.05677e-13,22659.3,8.30527], Tmin=(508.951,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (189.784,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 312,
    label = "CC[N]O",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {10,S}
2  N u1 p1 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86169,0.0152632,2.50937e-05,-3.8748e-08,1.50017e-11,2710.93,8.1874], Tmin=(10,'K'), Tmax=(891.912,'K')),
            NASAPolynomial(coeffs=[2.63142,0.0303605,-1.6408e-05,4.31521e-09,-4.44222e-13,2549.34,11.8459], Tmin=(891.912,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (22.5479,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 313,
    label = "[NH]ONN",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {3,S} {5,S}
3 N u0 p1 c0 {2,S} {6,S} {7,S}
4 N u1 p1 c0 {1,S} {8,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93402,0.00415652,8.67869e-05,-1.8403e-07,1.19561e-10,38225.7,9.33532], Tmin=(10,'K'), Tmax=(504.597,'K')),
            NASAPolynomial(coeffs=[3.04788,0.0248576,-1.54064e-05,4.7001e-09,-5.56604e-13,38141,11.279], Tmin=(504.597,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (317.808,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 314,
    label = "N[CH]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {7,S}
2 N u0 p1 c0 {3,S} {5,S} {6,S}
3 C u1 p0 c0 {1,S} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96114,0.00237879,6.31582e-05,-1.23313e-07,7.5232e-11,-4441.34,7.53188], Tmin=(10,'K'), Tmax=(519.572,'K')),
            NASAPolynomial(coeffs=[2.69036,0.0203295,-1.22448e-05,3.69156e-09,-4.35853e-13,-4419.53,11.7697], Tmin=(519.572,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-36.9405,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 315,
    label = "ONNDO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {6,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 N u0 p1 c0 {2,D} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95756,0.00246978,5.65994e-05,-1.0712e-07,6.14857e-11,4305.16,7.90885], Tmin=(10,'K'), Tmax=(569.29,'K')),
            NASAPolynomial(coeffs=[2.96762,0.0191231,-1.28322e-05,4.11069e-09,-5.01064e-13,4260.73,10.7468], Tmin=(569.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (35.7773,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 316,
    label = "CNDC",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,D}
2 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00922,-0.000854083,5.68013e-05,-7.79173e-08,3.4683e-11,7834.69,5.73448], Tmin=(10,'K'), Tmax=(583.106,'K')),
            NASAPolynomial(coeffs=[-0.0478671,0.0269764,-1.47899e-05,3.93208e-09,-4.08509e-13,8307.84,23.1193], Tmin=(583.106,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (65.1389,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 317,
    label = "[O-][NH+]D[C]CO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {9,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {2,S} {5,D} {8,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 C u1 p0 c0 {3,D} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89223,0.00877331,7.43967e-05,-1.50642e-07,9.16667e-11,13550,10.0697], Tmin=(10,'K'), Tmax=(521.853,'K')),
            NASAPolynomial(coeffs=[2.18459,0.0317149,-1.98657e-05,5.95646e-09,-6.85633e-13,13594.1,15.912], Tmin=(521.853,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (112.642,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 318,
    label = "[NH]C#N",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {3,S} {4,S}
2 N u0 p1 c0 {3,T}
3 C u0 p0 c0 {1,S} {2,T}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98388,0.000932992,2.60474e-05,-4.72074e-08,2.6397e-11,37134.1,5.86798], Tmin=(10,'K'), Tmax=(566.202,'K')),
            NASAPolynomial(coeffs=[3.26756,0.0095636,-6.27493e-06,1.98611e-09,-2.40804e-13,37157.9,8.41106], Tmin=(566.202,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (308.743,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 319,
    label = "N[C]DCDC",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {5,S} {6,S}
2 C u0 p0 c0 {4,D} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {4,D}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85517,0.0116383,0.000122317,-4.32258e-07,4.3671e-10,42482,8.31693], Tmin=(10,'K'), Tmax=(353.999,'K')),
            NASAPolynomial(coeffs=[5.12128,0.020299,-1.17001e-05,3.40285e-09,-3.91953e-13,42248.4,1.49089], Tmin=(353.999,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (353.235,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 320,
    label = "[NH-][NH+]DCD[N]",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {2,S} {4,D} {5,S}
2 N u0 p2 c-1 {1,S} {6,S}
3 N u1 p1 c0 {4,D}
4 C u0 p0 c0 {1,D} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94009,0.0039448,6.49352e-05,-1.53276e-07,1.0861e-10,47366.9,8.44858], Tmin=(10,'K'), Tmax=(477.408,'K')),
            NASAPolynomial(coeffs=[3.9146,0.015962,-9.90876e-06,3.0269e-09,-3.59395e-13,47234.8,7.14394], Tmin=(477.408,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (393.819,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 321,
    label = "[NH-][N+]DCDC",
    molecule = 
"""
multiplicity 2
1 N u1 p0 c+1 {2,S} {4,D}
2 N u0 p2 c-1 {1,S} {7,S}
3 C u0 p0 c0 {4,D} {5,S} {6,S}
4 C u0 p0 c0 {1,D} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87613,0.00960117,0.00010202,-3.39652e-07,3.23029e-10,53519.5,8.05208], Tmin=(10,'K'), Tmax=(375.63,'K')),
            NASAPolynomial(coeffs=[5.025,0.0175655,-1.0442e-05,3.09721e-09,-3.61337e-13,53290.7,1.73758], Tmin=(375.63,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (444.998,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 322,
    label = "[O-][NH+]DCO",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {7,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {2,S} {4,D} {6,S}
4 C u0 p0 c0 {1,S} {3,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06619,-0.0062973,0.000103561,-1.81826e-07,1.02822e-10,-18632.1,8.21069], Tmin=(10,'K'), Tmax=(560.748,'K')),
            NASAPolynomial(coeffs=[1.86336,0.02371,-1.49444e-05,4.52172e-09,-5.2438e-13,-18609.8,15.56], Tmin=(560.748,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-154.925,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 323,
    label = "NOCDO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,S} {5,S} {6,S}
4 C u0 p0 c0 {1,S} {2,D} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93311,0.00565823,4.50631e-05,-8.75712e-08,5.32366e-11,-24495.2,8.25101], Tmin=(10,'K'), Tmax=(426.018,'K')),
            NASAPolynomial(coeffs=[2.16511,0.0222585,-1.33863e-05,3.89522e-09,-4.38743e-13,-24344.6,15.272], Tmin=(426.018,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-203.672,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 324,
    label = "OCD[C]NDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {7,S}
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {2,D} {5,S}
4 C u0 p0 c0 {1,S} {5,D} {6,S}
5 C u1 p0 c0 {3,S} {4,D}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82411,0.0146366,9.81984e-05,-3.76872e-07,3.91392e-10,13311.9,10.0005], Tmin=(10,'K'), Tmax=(351.604,'K')),
            NASAPolynomial(coeffs=[5.23076,0.0196693,-1.30119e-05,4.14401e-09,-5.04146e-13,13083,2.8355], Tmin=(351.604,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (110.703,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 325,
    label = "[O-][N+]#CC[CH2]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {5,T}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u1 p0 c0 {3,S} {8,S} {9,S}
5 C u0 p0 c0 {2,T} {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63077,0.0346075,-4.85972e-05,6.49352e-08,-4.05753e-11,36321.1,9.96875], Tmin=(10,'K'), Tmax=(468.53,'K')),
            NASAPolynomial(coeffs=[4.00997,0.0280648,-1.70691e-05,5.01746e-09,-5.70073e-13,36321.9,8.81396], Tmin=(468.53,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (301.976,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 326,
    label = "[O-][NH+]DCDCN",
    molecule = 
"""
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {4,S} {7,S} {8,S}
3 N u0 p0 c+1 {1,S} {5,D} {9,S}
4 C u0 p0 c0 {2,S} {5,D} {6,S}
5 C u0 p0 c0 {3,D} {4,D}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72886,0.023807,-2.45577e-06,-1.21692e-08,6.20985e-12,31215.2,9.91815], Tmin=(10,'K'), Tmax=(875.514,'K')),
            NASAPolynomial(coeffs=[4.68161,0.024976,-1.39194e-05,3.76372e-09,-3.96773e-13,30836.7,4.23973], Tmin=(875.514,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (259.515,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 327,
    label = "[O-][N+]DCDN",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u1 p0 c+1 {1,S} {4,D}
3 N u0 p1 c0 {4,D} {5,S}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88552,0.00949697,7.08052e-05,-2.898e-07,3.15517e-10,37320.8,7.44563], Tmin=(10,'K'), Tmax=(342.805,'K')),
            NASAPolynomial(coeffs=[5.20958,0.0106303,-6.71508e-06,2.06973e-09,-2.47078e-13,37132.6,1.05417], Tmin=(342.805,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (310.319,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 328,
    label = "NNDCD[N]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 N u0 p1 c0 {1,S} {4,D}
3 N u1 p1 c0 {4,D}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94209,0.0036641,6.24658e-05,-1.39182e-07,9.28333e-11,43078.1,8.3136], Tmin=(10,'K'), Tmax=(507.66,'K')),
            NASAPolynomial(coeffs=[3.89328,0.0161478,-1.01697e-05,3.15049e-09,-3.78479e-13,42927.2,6.98043], Tmin=(507.66,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (358.156,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 329,
    label = "CCDNO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {9,S}
2 N u0 p1 c0 {1,S} {4,D}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {2,D} {3,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94591,0.00405379,0.000100787,-2.39772e-07,1.89906e-10,-4667,7.01078], Tmin=(10,'K'), Tmax=(321.121,'K')),
            NASAPolynomial(coeffs=[1.92098,0.0292775,-1.70384e-05,4.84498e-09,-5.37372e-13,-4536.95,14.4797], Tmin=(321.121,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-38.8057,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 330,
    label = "CD[C]CDN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {8,S}
2 C u0 p0 c0 {1,D} {4,S} {5,S}
3 C u0 p0 c0 {4,D} {6,S} {7,S}
4 C u1 p0 c0 {2,S} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95139,0.00304802,8.36766e-05,-1.68139e-07,1.05897e-10,41490.4,8.74176], Tmin=(10,'K'), Tmax=(497.981,'K')),
            NASAPolynomial(coeffs=[2.21495,0.0266585,-1.65476e-05,4.99929e-09,-5.84781e-13,41543.5,14.7055], Tmin=(497.981,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (344.957,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 331,
    label = "[O-][N+]#CC",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {4,T}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {2,T} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80843,0.0187001,-2.83494e-05,6.00051e-08,-4.89141e-11,13926.6,6.6155], Tmin=(10,'K'), Tmax=(461.269,'K')),
            NASAPolynomial(coeffs=[2.77519,0.0206556,-1.19303e-05,3.35389e-09,-3.6739e-13,14096.5,11.6086], Tmin=(461.269,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (115.787,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 332,
    label = "NCCDO",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,S} {7,S} {8,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {1,D} {3,S} {9,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90822,0.0138793,1.68401e-05,-2.50922e-08,8.8123e-12,-17727,8.39387], Tmin=(10,'K'), Tmax=(1023.33,'K')),
            NASAPolynomial(coeffs=[3.69927,0.0242579,-1.23885e-05,3.08016e-09,-3.00899e-13,-18184.9,6.96055], Tmin=(1023.33,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-147.369,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 333,
    label = "ONDC",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 N u0 p1 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07259,-0.00666521,8.40843e-05,-1.46291e-07,8.36669e-11,634.51,6.62247], Tmin=(10,'K'), Tmax=(542.255,'K')),
            NASAPolynomial(coeffs=[2.03493,0.0180062,-1.08301e-05,3.18611e-09,-3.63307e-13,713.763,13.899], Tmin=(542.255,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (5.27126,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 334,
    label = "[O-][N+]#CNDN",
    molecule = 
"""
1 O u0 p3 c-1 {4,S}
2 N u0 p1 c0 {3,D} {5,S}
3 N u0 p1 c0 {2,D} {6,S}
4 N u0 p0 c+1 {1,S} {5,T}
5 C u0 p0 c0 {2,S} {4,T}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88172,0.0111274,7.59488e-05,-3.20117e-07,3.84653e-10,51618.3,8.66042], Tmin=(10,'K'), Tmax=(288.263,'K')),
            NASAPolynomial(coeffs=[4.09756,0.0181063,-1.22665e-05,3.92774e-09,-4.77169e-13,51564.4,7.16882], Tmin=(288.263,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (429.196,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 335,
    label = "NDCDO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 N u0 p1 c0 {3,D} {4,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98664,0.000755629,2.37611e-05,-4.09682e-08,2.18966e-11,-15724,5.00913], Tmin=(10,'K'), Tmax=(582.958,'K')),
            NASAPolynomial(coeffs=[3.14327,0.00948327,-6.26273e-06,2.02036e-09,-2.49909e-13,-15675.6,8.19421], Tmin=(582.958,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-130.743,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 336,
    label = "[NH]ONDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,D}
3 N u1 p1 c0 {1,S} {5,S}
4 N u0 p1 c0 {1,S} {2,D}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93401,0.0043177,5.76902e-05,-1.42118e-07,1.01542e-10,25873.8,8.62168], Tmin=(10,'K'), Tmax=(488.674,'K')),
            NASAPolynomial(coeffs=[4.4507,0.0130355,-8.81086e-06,2.82165e-09,-3.4407e-13,25668.7,4.91719], Tmin=(488.674,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (215.112,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 337,
    label = "ONCD[N]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {7,S}
2 N u0 p1 c0 {1,S} {4,S} {5,S}
3 N u1 p1 c0 {4,D}
4 C u0 p0 c0 {2,S} {3,D} {6,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94094,0.00391555,7.84931e-05,-1.78083e-07,1.24292e-10,25648.8,8.90723], Tmin=(10,'K'), Tmax=(466.835,'K')),
            NASAPolynomial(coeffs=[3.18042,0.0214979,-1.35578e-05,4.14696e-09,-4.88418e-13,25599.2,10.7055], Tmin=(466.835,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (213.245,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 338,
    label = "COON",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u0 p1 c0 {2,S} {8,S} {9,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76014,0.0235286,-2.79293e-05,6.37068e-08,-5.6278e-11,-291.73,8.10864], Tmin=(10,'K'), Tmax=(456.029,'K')),
            NASAPolynomial(coeffs=[2.11645,0.0290541,-1.68565e-05,4.76234e-09,-5.23954e-13,-49.357,15.7616], Tmin=(456.029,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-2.43268,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 339,
    label = "[O-][NH+]DCCC",
    molecule = 
"""
1  O u0 p3 c-1 {2,S}
2  N u0 p0 c+1 {1,S} {5,D} {12,S}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {2,D} {3,S} {11,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87846,0.0162687,4.18388e-05,-6.09125e-08,2.37038e-11,-2021.88,8.44411], Tmin=(10,'K'), Tmax=(874.896,'K')),
            NASAPolynomial(coeffs=[1.99109,0.0390071,-2.13367e-05,5.66004e-09,-5.86397e-13,-2231.63,14.2112], Tmin=(874.896,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-16.7882,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 340,
    label = "OOCD[N]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {6,S}
3 N u1 p1 c0 {4,D}
4 C u0 p0 c0 {1,S} {3,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88676,0.010034,4.13337e-05,-1.28071e-07,1.11334e-10,16729.3,8.94666], Tmin=(10,'K'), Tmax=(382.728,'K')),
            NASAPolynomial(coeffs=[3.69651,0.0177913,-1.16791e-05,3.65489e-09,-4.3617e-13,16701.6,9.12981], Tmin=(382.728,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (139.099,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 341,
    label = "[CH2]NC#C",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {3,T} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87378,0.00859439,0.000106206,-2.83901e-07,2.19108e-10,49842.8,7.65388], Tmin=(10,'K'), Tmax=(459.261,'K')),
            NASAPolynomial(coeffs=[5.31676,0.020436,-1.21944e-05,3.6974e-09,-4.43526e-13,49452.8,-0.987405], Tmin=(459.261,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (414.4,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 342,
    label = "NNC#C",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {5,S}
2 N u0 p1 c0 {1,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {3,T} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91174,0.0057426,9.25022e-05,-2.16593e-07,1.51711e-10,43113.4,7.92149], Tmin=(10,'K'), Tmax=(486.954,'K')),
            NASAPolynomial(coeffs=[4.11177,0.0220831,-1.32288e-05,3.99874e-09,-4.7599e-13,42880.7,4.91112], Tmin=(486.954,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (358.446,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 343,
    label = "CDCC#N",
    molecule = 
"""
1 N u0 p1 c0 {4,T}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {2,D} {6,S} {7,S}
4 C u0 p0 c0 {1,T} {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97155,0.00177111,6.5565e-05,-1.24775e-07,7.58129e-11,20994.9,7.69648], Tmin=(10,'K'), Tmax=(490.808,'K')),
            NASAPolynomial(coeffs=[1.99931,0.0228488,-1.41463e-05,4.27059e-09,-4.99972e-13,21128.3,15.1937], Tmin=(490.808,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (174.554,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 344,
    label = "[CH2]NNO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {9,S}
2 N u0 p1 c0 {3,S} {4,S} {5,S}
3 N u0 p1 c0 {1,S} {2,S} {6,S}
4 C u1 p0 c0 {2,S} {7,S} {8,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91394,0.00550052,0.00010398,-2.29132e-07,1.53503e-10,23715.5,8.4218], Tmin=(10,'K'), Tmax=(496.319,'K')),
            NASAPolynomial(coeffs=[3.31665,0.027954,-1.71917e-05,5.23803e-09,-6.21392e-13,23557.5,8.69621], Tmin=(496.319,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (197.16,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 345,
    label = "NCO[O]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u1 p2 c0 {1,S}
3 N u0 p1 c0 {4,S} {7,S} {8,S}
4 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97308,0.00202874,9.89156e-05,-2.34604e-07,1.85846e-10,-914.374,9.44035], Tmin=(10,'K'), Tmax=(321.257,'K')),
            NASAPolynomial(coeffs=[1.98698,0.0267565,-1.65361e-05,4.96607e-09,-5.76125e-13,-786.758,16.767], Tmin=(321.257,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-7.59531,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 346,
    label = "[O-][NH+]CN",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u1 p0 c+1 {1,S} {4,S} {7,S}
3 N u0 p1 c0 {4,S} {8,S} {9,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88896,0.00900787,5.8921e-05,-1.22548e-07,7.97612e-11,5475.44,9.28715], Tmin=(10,'K'), Tmax=(396.336,'K')),
            NASAPolynomial(coeffs=[1.9082,0.0289989,-1.67398e-05,4.72123e-09,-5.19117e-13,5632.44,17.0099], Tmin=(396.336,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (45.51,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 347,
    label = "[O-][NH+]DC[CH]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {5,S} {9,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {2,S} {4,D} {8,S}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 C u1 p0 c0 {1,S} {4,S} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93482,0.00387225,9.71362e-05,-1.85337e-07,1.08689e-10,-10485.7,9.76978], Tmin=(10,'K'), Tmax=(547.252,'K')),
            NASAPolynomial(coeffs=[1.9227,0.0328476,-2.13933e-05,6.69893e-09,-8.0358e-13,-10479.1,16.312], Tmin=(547.252,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-87.2087,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 348,
    label = "ND[C]CDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 N u0 p1 c0 {4,D} {6,S}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 C u1 p0 c0 {2,D} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93999,0.0044905,6.35008e-05,-1.58115e-07,1.21178e-10,17097.8,8.60639], Tmin=(10,'K'), Tmax=(419.146,'K')),
            NASAPolynomial(coeffs=[3.29142,0.0180872,-1.16658e-05,3.60263e-09,-4.25724e-13,17087.1,10.3953], Tmin=(419.146,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (142.158,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 349,
    label = "NDCCDN",
    molecule = 
"""
1 N u0 p1 c0 {3,D} {7,S}
2 N u0 p1 c0 {4,D} {8,S}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 C u0 p0 c0 {2,D} {3,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97296,0.00159663,6.83359e-05,-1.17276e-07,6.50881e-11,18447.9,7.35512], Tmin=(10,'K'), Tmax=(465.6,'K')),
            NASAPolynomial(coeffs=[0.882973,0.0281345,-1.71326e-05,5.06315e-09,-5.79749e-13,18735.7,19.9014], Tmin=(465.6,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (153.372,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 350,
    label = "[O-][NH+]DC[N]N",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {5,D} {7,S}
3 N u0 p1 c0 {4,S} {8,S} {9,S}
4 N u1 p1 c0 {3,S} {5,S}
5 C u0 p0 c0 {2,D} {4,S} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91843,0.00495847,0.00010241,-2.08388e-07,1.28655e-10,25042.1,9.73913], Tmin=(10,'K'), Tmax=(534.65,'K')),
            NASAPolynomial(coeffs=[2.84153,0.0307777,-1.98613e-05,6.21342e-09,-7.47208e-13,24903.4,11.8861], Tmin=(534.65,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (208.183,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 351,
    label = "CNNDC",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {3,S} {8,S}
2  N u0 p1 c0 {1,S} {4,D}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {2,D} {9,S} {10,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96383,0.00223758,9.39978e-05,-1.71649e-07,1.02586e-10,17980.2,7.07598], Tmin=(10,'K'), Tmax=(429.878,'K')),
            NASAPolynomial(coeffs=[0.440973,0.0350239,-2.04272e-05,5.83823e-09,-6.52669e-13,18283,21.0969], Tmin=(429.878,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (149.482,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 352,
    label = "NCC[O]",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {4,S}
2  N u0 p1 c0 {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96426,0.0022977,0.000102276,-1.96707e-07,1.24192e-10,159.135,9.48392], Tmin=(10,'K'), Tmax=(406.19,'K')),
            NASAPolynomial(coeffs=[0.564807,0.0357752,-2.13554e-05,6.21038e-09,-7.02423e-13,435.292,22.8215], Tmin=(406.19,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (1.31393,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 353,
    label = "CO[N]C",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  N u1 p1 c0 {1,S} {4,S}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7654,0.0253147,-5.48362e-05,1.6941e-07,-1.62503e-10,11958.1,7.36412], Tmin=(10,'K'), Tmax=(420.95,'K')),
            NASAPolynomial(coeffs=[0.731623,0.0348601,-2.01395e-05,5.64179e-09,-6.14726e-13,12384.4,21.4046], Tmin=(420.95,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (99.4181,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 354,
    label = "[O-][N+]#COC",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {2,S} {5,T}
4 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
5 C u0 p0 c0 {1,S} {3,T}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64341,0.0297562,-4.07032e-05,4.68724e-08,-2.38927e-11,9027.05,8.24625], Tmin=(10,'K'), Tmax=(594.691,'K')),
            NASAPolynomial(coeffs=[3.87389,0.0236589,-1.38549e-05,3.91745e-09,-4.30024e-13,9080.04,7.93011], Tmin=(594.691,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (75.0225,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 355,
    label = "ODN[CH]NDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,D} {5,S}
4 N u0 p1 c0 {2,D} {5,S}
5 C u1 p0 c0 {3,S} {4,S} {6,S}
6 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9222,0.00516962,7.52552e-05,-1.79808e-07,1.27104e-10,27488.8,9.00102], Tmin=(10,'K'), Tmax=(479.071,'K')),
            NASAPolynomial(coeffs=[3.83283,0.0197638,-1.37992e-05,4.45575e-09,-5.40159e-13,27338.5,7.70784], Tmin=(479.071,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (228.54,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 356,
    label = "CON",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85612,0.0151698,-2.84794e-05,9.18525e-08,-8.39967e-11,-4855.26,5.98135], Tmin=(10,'K'), Tmax=(462.91,'K')),
            NASAPolynomial(coeffs=[1.09817,0.0247474,-1.33263e-05,3.51143e-09,-3.63122e-13,-4447.21,18.8122], Tmin=(462.91,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-40.3694,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 357,
    label = "[N-]([NH+]DO)CD[CH]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 N u0 p0 c+1 {1,D} {3,S} {7,S}
3 N u0 p2 c-1 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,D} {6,S}
5 C u1 p0 c0 {4,D} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93628,0.00381017,8.79899e-05,-1.71981e-07,1.02536e-10,51204.3,9.7298], Tmin=(10,'K'), Tmax=(544.801,'K')),
            NASAPolynomial(coeffs=[2.4472,0.0287066,-1.90027e-05,5.98953e-09,-7.19608e-13,51159.4,14.1076], Tmin=(544.801,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (425.713,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 358,
    label = "OO[N]NDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {6,S}
3 O u0 p2 c0 {5,D}
4 N u1 p1 c0 {1,S} {5,S}
5 N u0 p1 c0 {3,D} {4,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83678,0.0127141,7.24883e-05,-2.42379e-07,2.15244e-10,28920.7,10.1064], Tmin=(10,'K'), Tmax=(411.549,'K')),
            NASAPolynomial(coeffs=[5.21673,0.0176951,-1.27055e-05,4.2227e-09,-5.24948e-13,28651.3,2.78165], Tmin=(411.549,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (240.46,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 359,
    label = "NDCDCD[N]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,D} {5,S}
2 N u1 p1 c0 {4,D}
3 C u0 p0 c0 {1,D} {4,D}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93354,0.00462885,5.73804e-05,-1.56181e-07,1.2335e-10,49249.3,7.73442], Tmin=(10,'K'), Tmax=(444.001,'K')),
            NASAPolynomial(coeffs=[4.47243,0.011809,-7.53528e-06,2.33825e-09,-2.80366e-13,49082.8,4.23625], Tmin=(444.001,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (409.476,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 360,
    label = "[CH]DCDCNDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,D} {6,S}
4 C u0 p0 c0 {3,D} {5,D}
5 C u1 p0 c0 {4,D} {7,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90158,0.00638306,9.00781e-05,-2.16373e-07,1.51926e-10,46561.5,9.84456], Tmin=(10,'K'), Tmax=(493.918,'K')),
            NASAPolynomial(coeffs=[4.51713,0.0210156,-1.39371e-05,4.43595e-09,-5.39776e-13,46261.4,4.88675], Tmin=(493.918,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (387.111,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 361,
    label = "[O-][NH+]DCDCDC",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {4,D} {6,S}
3 C u0 p0 c0 {5,D} {7,S} {8,S}
4 C u0 p0 c0 {2,D} {5,D}
5 C u0 p0 c0 {3,D} {4,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88998,0.00912028,9.67918e-05,-2.81392e-07,2.50344e-10,43748.8,9.06925], Tmin=(10,'K'), Tmax=(362.694,'K')),
            NASAPolynomial(coeffs=[3.24125,0.0264604,-1.70463e-05,5.28178e-09,-6.27227e-13,43728.8,10.6175], Tmin=(362.694,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (363.759,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 362,
    label = "[O-][NH+]D[C]ON",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p3 c-1 {4,S}
3 N u0 p1 c0 {1,S} {7,S} {8,S}
4 N u0 p0 c+1 {2,S} {5,D} {6,S}
5 C u1 p0 c0 {1,S} {4,D}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87765,0.0106877,0.000109354,-3.67928e-07,3.75919e-10,31901.4,9.70459], Tmin=(10,'K'), Tmax=(321.476,'K')),
            NASAPolynomial(coeffs=[3.54129,0.0263373,-1.71586e-05,5.36108e-09,-6.40789e-13,31863.8,10.0242], Tmin=(321.476,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (265.263,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 363,
    label = "[NH]CNDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 N u1 p1 c0 {4,S} {7,S}
3 N u0 p1 c0 {1,D} {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88964,0.00994617,3.10115e-05,-5.99963e-08,3.1534e-11,33623.8,9.14815], Tmin=(10,'K'), Tmax=(637.213,'K')),
            NASAPolynomial(coeffs=[3.18347,0.0215415,-1.31444e-05,3.84027e-09,-4.31919e-13,33568.4,11.0958], Tmin=(637.213,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (279.549,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 364,
    label = "[NH]CNDN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,D} {4,S}
2 N u1 p1 c0 {4,S} {7,S}
3 N u0 p1 c0 {1,D} {8,S}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97771,0.00152114,9.11043e-05,-1.93576e-07,1.36173e-10,46260,8.94599], Tmin=(10,'K'), Tmax=(363.22,'K')),
            NASAPolynomial(coeffs=[1.59765,0.0277326,-1.71451e-05,5.11453e-09,-5.88287e-13,46432.9,18.0179], Tmin=(363.22,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (384.629,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 365,
    label = "[O-][N+]#CND[CH]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {4,S} {5,D}
3 N u0 p0 c+1 {1,S} {4,T}
4 C u0 p0 c0 {2,S} {3,T}
5 C u1 p0 c0 {2,D} {6,S}
6 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84492,0.0128856,9.2804e-05,-3.72334e-07,3.99642e-10,61426.5,8.91766], Tmin=(10,'K'), Tmax=(344.763,'K')),
            NASAPolynomial(coeffs=[5.40735,0.0156831,-1.04092e-05,3.29594e-09,-3.98802e-13,61194.4,1.24011], Tmin=(344.763,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (510.75,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 366,
    label = "[O-][N+]DNNDC",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {4,S}
2 N u0 p1 c0 {3,S} {5,D}
3 N u0 p1 c0 {2,S} {4,D}
4 N u1 p0 c+1 {1,S} {3,D}
5 C u0 p0 c0 {2,D} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88153,0.00958396,5.24021e-05,-1.23095e-07,8.36356e-11,45384,9.60019], Tmin=(10,'K'), Tmax=(478.966,'K')),
            NASAPolynomial(coeffs=[3.1254,0.0235713,-1.54319e-05,4.7684e-09,-5.60767e-13,45368.4,11.7727], Tmin=(478.966,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (377.331,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 367,
    label = "ON[C]DC",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {8,S}
2 N u0 p1 c0 {1,S} {4,S} {5,S}
3 C u0 p0 c0 {4,D} {6,S} {7,S}
4 C u1 p0 c0 {2,S} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90561,0.00620811,9.78416e-05,-2.32683e-07,1.65143e-10,30949.3,8.97326], Tmin=(10,'K'), Tmax=(479.777,'K')),
            NASAPolynomial(coeffs=[4.04213,0.0236526,-1.47959e-05,4.56015e-09,-5.44959e-13,30722.4,6.18599], Tmin=(479.777,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (257.308,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 368,
    label = "NO[NH]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {4,S} {5,S}
3 N u1 p1 c0 {1,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90682,0.00844257,9.58106e-06,-1.65165e-08,6.68179e-12,29492,7.83432], Tmin=(10,'K'), Tmax=(846.391,'K')),
            NASAPolynomial(coeffs=[3.21527,0.0150812,-8.15714e-06,2.15984e-09,-2.24333e-13,29488.3,10.3422], Tmin=(846.391,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (245.205,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 369,
    label = "[O-][NH+]DC[N]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {8,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {2,S} {5,D} {7,S}
4 N u1 p1 c0 {1,S} {5,S}
5 C u0 p0 c0 {3,D} {4,S} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90684,0.0060875,0.000100865,-2.34035e-07,1.62743e-10,8443.03,10.0219], Tmin=(10,'K'), Tmax=(484.038,'K')),
            NASAPolynomial(coeffs=[3.66398,0.0261217,-1.7085e-05,5.36016e-09,-6.42518e-13,8255.35,8.8359], Tmin=(484.038,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (70.1791,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 370,
    label = "NDCCDO",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,D} {7,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 C u0 p0 c0 {1,D} {3,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97301,0.00175868,6.59057e-05,-1.30357e-07,8.47208e-11,-4878.5,8.17203], Tmin=(10,'K'), Tmax=(393.998,'K')),
            NASAPolynomial(coeffs=[1.92131,0.0225885,-1.33972e-05,3.82971e-09,-4.24386e-13,-4716.83,16.1593], Tmin=(393.998,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-40.5694,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 371,
    label = "[O-][NH+]DC[CH]N",
    molecule = 
"""
multiplicity 2
1  O u0 p3 c-1 {3,S}
2  N u0 p1 c0 {4,S} {9,S} {10,S}
3  N u0 p0 c+1 {1,S} {5,D} {8,S}
4  C u1 p0 c0 {2,S} {5,S} {6,S}
5  C u0 p0 c0 {3,D} {4,S} {7,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90685,0.00574266,0.000116628,-2.42152e-07,1.5285e-10,11456.2,9.81508], Tmin=(10,'K'), Tmax=(523.347,'K')),
            NASAPolynomial(coeffs=[2.8194,0.0340002,-2.15319e-05,6.66672e-09,-7.97641e-13,11296.8,11.7476], Tmin=(523.347,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (95.2214,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 372,
    label = "[N-]D[N+]DO",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 N u0 p0 c+1 {1,D} {3,D}
3 N u0 p2 c-1 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53329,-0.0037753,4.67481e-05,-9.43095e-08,6.23263e-11,8588.13,6.02136], Tmin=(10,'K'), Tmax=(480.26,'K')),
            NASAPolynomial(coeffs=[2.89374,0.00714392,-4.82328e-06,1.52557e-09,-1.82536e-13,8585.06,7.96628], Tmin=(480.26,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (71.4027,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (62.3585,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 373,
    label = "CCO[NH]",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  N u1 p1 c0 {1,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87619,0.0124572,3.58001e-05,-5.37202e-08,2.21115e-11,6346.14,8.17445], Tmin=(10,'K'), Tmax=(799.043,'K')),
            NASAPolynomial(coeffs=[1.67324,0.0322676,-1.78758e-05,4.81879e-09,-5.07592e-13,6417.83,16.5538], Tmin=(799.043,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (52.7643,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 374,
    label = "[O-][NH+]CO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {8,S}
2 O u0 p3 c-1 {3,S}
3 N u1 p0 c+1 {2,S} {4,S} {7,S}
4 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90076,0.00866699,4.8265e-05,-9.97339e-08,6.32699e-11,-16588.2,9.37489], Tmin=(10,'K'), Tmax=(408.851,'K')),
            NASAPolynomial(coeffs=[2.11836,0.0261051,-1.5712e-05,4.58593e-09,-5.18326e-13,-16442.4,16.3798], Tmin=(408.851,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-137.93,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 375,
    label = "[CH2]NNN",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {4,S} {5,S}
2  N u0 p1 c0 {1,S} {3,S} {6,S}
3  N u0 p1 c0 {2,S} {9,S} {10,S}
4  C u1 p0 c0 {1,S} {7,S} {8,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9283,0.00444539,0.000107133,-2.16525e-07,1.35792e-10,41553.7,8.28823], Tmin=(10,'K'), Tmax=(512.487,'K')),
            NASAPolynomial(coeffs=[2.22456,0.0327915,-1.98789e-05,5.99288e-09,-7.06324e-13,41530.7,13.4408], Tmin=(512.487,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (345.474,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 376,
    label = "NCDCD[N]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {6,S} {7,S}
2 N u1 p1 c0 {4,D}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92416,0.00492508,7.88901e-05,-1.84504e-07,1.28843e-10,28483.2,8.4482], Tmin=(10,'K'), Tmax=(488.629,'K')),
            NASAPolynomial(coeffs=[4.0947,0.0189583,-1.15545e-05,3.5184e-09,-4.19734e-13,28282.3,5.8628], Tmin=(488.629,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (236.805,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 377,
    label = "[NH-][N+]DN",
    molecule = 
"""
multiplicity 2
1 N u1 p0 c+1 {2,S} {3,D}
2 N u0 p2 c-1 {1,S} {4,S}
3 N u0 p1 c0 {1,D} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06972,-0.00615654,6.76048e-05,-1.13762e-07,6.27456e-11,47105.3,6.85546], Tmin=(10,'K'), Tmax=(567.525,'K')),
            NASAPolynomial(coeffs=[2.42449,0.0140636,-8.63248e-06,2.5691e-09,-2.94766e-13,47153.1,12.6372], Tmin=(567.525,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (391.653,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 378,
    label = "OND[C]NDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {6,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,S} {5,D}
4 N u0 p1 c0 {2,D} {5,S}
5 C u1 p0 c0 {3,D} {4,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84529,0.0119497,8.86414e-05,-3.11766e-07,2.94765e-10,33623.6,9.66625], Tmin=(10,'K'), Tmax=(390.156,'K')),
            NASAPolynomial(coeffs=[5.64168,0.0156687,-1.07617e-05,3.50695e-09,-4.33054e-13,33315,0.531387], Tmin=(390.156,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (279.572,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 379,
    label = "OD[C][N-][NH+]DO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {5,D}
3 N u0 p0 c+1 {1,D} {4,S} {6,S}
4 N u0 p2 c-1 {3,S} {5,S}
5 C u1 p0 c0 {2,D} {4,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88256,0.00929807,6.39694e-05,-1.92493e-07,1.63997e-10,10555.4,10.0381], Tmin=(10,'K'), Tmax=(407.155,'K')),
            NASAPolynomial(coeffs=[4.18133,0.0181985,-1.24245e-05,3.98811e-09,-4.84057e-13,10433,7.66045], Tmin=(407.155,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (87.764,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 380,
    label = "CDNND[CH]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,D}
2 N u0 p1 c0 {1,S} {4,D}
3 C u0 p0 c0 {1,D} {5,S} {6,S}
4 C u1 p0 c0 {2,D} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93102,0.006134,5.80198e-05,-1.34814e-07,9.98239e-11,55186.2,8.57146], Tmin=(10,'K'), Tmax=(346.725,'K')),
            NASAPolynomial(coeffs=[2.48099,0.022862,-1.43482e-05,4.33086e-09,-5.02691e-13,55286.8,14.0311], Tmin=(346.725,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (458.846,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 381,
    label = "CDN[C]DO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,D} {4,S}
3 C u0 p0 c0 {2,D} {5,S} {6,S}
4 C u1 p0 c0 {1,D} {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9133,0.00666567,8.00485e-05,-2.53256e-07,2.34258e-10,6661.88,8.13579], Tmin=(10,'K'), Tmax=(378.218,'K')),
            NASAPolynomial(coeffs=[4.46619,0.0149713,-9.02121e-06,2.68048e-09,-3.11689e-13,6518.83,4.66778], Tmin=(378.218,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (55.3982,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 382,
    label = "[NH]ONDN",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {4,D}
3 N u1 p1 c0 {1,S} {5,S}
4 N u0 p1 c0 {2,D} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94677,0.00335363,6.36101e-05,-1.37572e-07,8.99392e-11,46655.8,8.65167], Tmin=(10,'K'), Tmax=(508.006,'K')),
            NASAPolynomial(coeffs=[3.4896,0.0179017,-1.16741e-05,3.64943e-09,-4.36447e-13,46561,9.15713], Tmin=(508.006,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (387.903,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 383,
    label = "NDCDN",
    molecule = 
"""
1 N u0 p1 c0 {3,D} {4,S}
2 N u0 p1 c0 {3,D} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97869,0.00118941,3.52411e-05,-6.03551e-08,3.18263e-11,16071.5,4.59903], Tmin=(10,'K'), Tmax=(598.484,'K')),
            NASAPolynomial(coeffs=[2.77646,0.0141212,-9.4428e-06,3.09019e-09,-3.8672e-13,16127.7,9.0493], Tmin=(598.484,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (133.616,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 384,
    label = "[NH]NO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 N u0 p1 c0 {1,S} {3,S} {4,S}
3 N u1 p1 c0 {2,S} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96828,0.00183629,4.89598e-05,-8.90964e-08,5.00312e-11,20322.7,7.30277], Tmin=(10,'K'), Tmax=(568.567,'K')),
            NASAPolynomial(coeffs=[2.76734,0.0174471,-1.11197e-05,3.50395e-09,-4.26859e-13,20343.5,11.4005], Tmin=(568.567,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (168.959,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 385,
    label = "[O-][NH+]D[C]NDN",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {5,D} {6,S}
3 N u0 p1 c0 {4,D} {5,S}
4 N u0 p1 c0 {3,D} {7,S}
5 C u1 p0 c0 {2,D} {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89539,0.00772956,9.33709e-05,-2.61757e-07,2.17154e-10,55776.8,9.94787], Tmin=(10,'K'), Tmax=(410.732,'K')),
            NASAPolynomial(coeffs=[4.03152,0.0218196,-1.43849e-05,4.52242e-09,-5.42288e-13,55635.6,7.82931], Tmin=(410.732,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (463.755,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 386,
    label = "NC[CH]O",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {10,S}
2  N u0 p1 c0 {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u1 p0 c0 {1,S} {3,S} {7,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95422,0.00283061,0.000101698,-1.92347e-07,1.15952e-10,-6476.22,9.09886], Tmin=(10,'K'), Tmax=(497.959,'K')),
            NASAPolynomial(coeffs=[0.921086,0.0355168,-2.18293e-05,6.59132e-09,-7.73418e-13,-6277.31,20.5812], Tmin=(497.959,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-53.8606,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 387,
    label = "[O-][N+]#CC[O]",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {4,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {2,S} {5,T}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 C u0 p0 c0 {3,T} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80459,0.0212129,-9.71569e-06,-1.38086e-09,1.66472e-12,25085.1,10.4274], Tmin=(10,'K'), Tmax=(1060.78,'K')),
            NASAPolynomial(coeffs=[6.751,0.0151252,-8.20962e-06,2.13623e-09,-2.16147e-13,24177.4,-5.29314], Tmin=(1060.78,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (208.57,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 388,
    label = "C[C]DCDN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {4,D} {8,S}
2 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3 C u1 p0 c0 {2,S} {4,D}
4 C u0 p0 c0 {1,D} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67357,0.0323985,-8.46525e-05,1.70438e-07,-1.26749e-10,40533.5,8.45675], Tmin=(10,'K'), Tmax=(451.755,'K')),
            NASAPolynomial(coeffs=[3.25574,0.0235251,-1.34418e-05,3.7421e-09,-4.06431e-13,40699.5,11.5605], Tmin=(451.755,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (337.007,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 389,
    label = "NCC[NH]",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {3,S} {9,S} {10,S}
2  N u1 p1 c0 {4,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89664,0.00831443,8.23093e-05,-1.55614e-07,9.33674e-11,18991.2,9.2763], Tmin=(10,'K'), Tmax=(430.278,'K')),
            NASAPolynomial(coeffs=[0.672728,0.0382851,-2.21728e-05,6.27018e-09,-6.91043e-13,19268.6,22.111], Tmin=(430.278,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (157.885,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 390,
    label = "[O-][NH+]DCCO",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {10,S}
2  O u0 p3 c-1 {3,S}
3  N u0 p0 c+1 {2,S} {5,D} {9,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {3,D} {4,S} {8,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83846,0.0178332,2.44937e-05,-4.30733e-08,1.79952e-11,-16031.2,10.2593], Tmin=(10,'K'), Tmax=(847.625,'K')),
            NASAPolynomial(coeffs=[3.39423,0.0306646,-1.72107e-05,4.66936e-09,-4.9296e-13,-16341.6,10.0542], Tmin=(847.625,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-133.286,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 391,
    label = "[NH]ONDC",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {4,D}
3 N u1 p1 c0 {1,S} {7,S}
4 C u0 p0 c0 {2,D} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94909,0.00316863,7.33723e-05,-1.50422e-07,9.50152e-11,38151.5,8.83764], Tmin=(10,'K'), Tmax=(510.762,'K')),
            NASAPolynomial(coeffs=[2.82482,0.0225019,-1.43259e-05,4.40342e-09,-5.20799e-13,38129,12.1618], Tmin=(510.762,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (317.194,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 392,
    label = "N[N]N",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {4,S} {5,S}
2 N u0 p1 c0 {3,S} {6,S} {7,S}
3 N u1 p1 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97566,0.00146725,5.81072e-05,-1.04524e-07,6.00658e-11,32262.6,7.19976], Tmin=(10,'K'), Tmax=(514.876,'K')),
            NASAPolynomial(coeffs=[1.91752,0.0217246,-1.33429e-05,4.08982e-09,-4.89201e-13,32418,15.2135], Tmin=(514.876,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (268.238,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 393,
    label = "N[N]OO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {7,S}
3 N u0 p1 c0 {4,S} {5,S} {6,S}
4 N u1 p1 c0 {1,S} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84475,0.0128734,8.95078e-05,-3.22675e-07,3.22422e-10,10680.7,9.36296], Tmin=(10,'K'), Tmax=(358.31,'K')),
            NASAPolynomial(coeffs=[4.77954,0.0199017,-1.30245e-05,4.12179e-09,-4.99199e-13,10501.6,4.24818], Tmin=(358.31,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (88.8215,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 394,
    label = "[NH-][N+]DC",
    molecule = 
"""
multiplicity 2
1 N u1 p0 c+1 {2,S} {3,D}
2 N u0 p2 c-1 {1,S} {6,S}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05209,-0.00514863,7.96392e-05,-1.449e-07,8.74128e-11,38252.3,7.07668], Tmin=(10,'K'), Tmax=(498.863,'K')),
            NASAPolynomial(coeffs=[1.9749,0.0182401,-1.09331e-05,3.19501e-09,-3.6219e-13,38375.8,14.8136], Tmin=(498.863,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (318.044,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 395,
    label = "[O-][NH+]DC[CH]C",
    molecule = 
"""
multiplicity 2
1  O u0 p3 c-1 {2,S}
2  N u0 p0 c+1 {1,S} {5,D} {11,S}
3  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
4  C u1 p0 c0 {3,S} {5,S} {9,S}
5  C u0 p0 c0 {2,D} {4,S} {10,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8179,0.015021,6.96275e-05,-1.55834e-07,1.0631e-10,8908.04,9.05824], Tmin=(10,'K'), Tmax=(379.189,'K')),
            NASAPolynomial(coeffs=[1.60502,0.0383641,-2.2713e-05,6.51201e-09,-7.24007e-13,9075.86,17.5882], Tmin=(379.189,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (74.0452,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 396,
    label = "[O-][N+]#CCD[N]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {5,T}
3 N u1 p1 c0 {4,D}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 C u0 p0 c0 {2,T} {4,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79477,0.0211964,-1.90182e-05,9.70985e-09,-2.2158e-12,52777.3,9.96805], Tmin=(10,'K'), Tmax=(899.299,'K')),
            NASAPolynomial(coeffs=[5.0249,0.0157249,-9.89196e-06,2.94437e-09,-3.35034e-13,52556,4.16395], Tmin=(899.299,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (438.802,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 397,
    label = "[O-][NH+]DNC[CH2]",
    molecule = 
"""
multiplicity 2
1  O u0 p3 c-1 {2,S}
2  N u0 p0 c+1 {1,S} {3,D} {10,S}
3  N u0 p1 c0 {2,D} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5  C u1 p0 c0 {4,S} {8,S} {9,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81056,0.024191,2.39488e-06,-1.50333e-08,5.98514e-12,31204.1,9.53718], Tmin=(10,'K'), Tmax=(1068.46,'K')),
            NASAPolynomial(coeffs=[6.13491,0.025356,-1.30922e-05,3.27268e-09,-3.20376e-13,30144.2,-4.46588], Tmin=(1068.46,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (259.463,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 398,
    label = "CO[N]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {3,S} {8,S}
3 N u1 p1 c0 {1,S} {2,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74127,0.0256357,-4.69382e-05,9.6956e-08,-7.77716e-11,-1311.81,8.04047], Tmin=(10,'K'), Tmax=(442.243,'K')),
            NASAPolynomial(coeffs=[2.89595,0.0246832,-1.45443e-05,4.16062e-09,-4.62285e-13,-1152.96,12.3796], Tmin=(442.243,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-10.9142,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 399,
    label = "[O-][N+]#COO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 O u0 p3 c-1 {4,S}
4 N u0 p0 c+1 {3,S} {5,T}
5 C u0 p0 c0 {1,S} {4,T}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7476,0.0226747,5.05108e-05,-3.03559e-07,3.6461e-10,18280.9,9.59731], Tmin=(10,'K'), Tmax=(337.957,'K')),
            NASAPolynomial(coeffs=[6.17944,0.0151787,-1.06988e-05,3.56031e-09,-4.46185e-13,17994.9,-1.29529], Tmin=(337.957,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (152.02,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 400,
    label = "NNNN",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {3,S} {5,S}
2  N u0 p1 c0 {1,S} {4,S} {6,S}
3  N u0 p1 c0 {1,S} {7,S} {8,S}
4  N u0 p1 c0 {2,S} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94749,0.00329327,0.000102276,-2.01124e-07,1.25519e-10,33055.8,7.88912], Tmin=(10,'K'), Tmax=(492.924,'K')),
            NASAPolynomial(coeffs=[1.50315,0.0332856,-1.99005e-05,5.91958e-09,-6.89461e-13,33173.3,16.7009], Tmin=(492.924,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (274.826,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 401,
    label = "OO[C]DN",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u0 p1 c0 {4,D} {6,S}
4 C u1 p0 c0 {1,S} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86218,0.0116666,6.6077e-05,-2.49165e-07,2.5333e-10,18493,8.8118], Tmin=(10,'K'), Tmax=(356.129,'K')),
            NASAPolynomial(coeffs=[4.69888,0.0160793,-1.06777e-05,3.4084e-09,-4.14854e-13,18345.8,4.40954], Tmin=(356.129,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (153.774,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 402,
    label = "[O-][N+]DNNDN",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {4,S}
2 N u0 p1 c0 {3,S} {4,D}
3 N u0 p1 c0 {2,S} {5,D}
4 N u1 p0 c+1 {1,S} {2,D}
5 N u0 p1 c0 {3,D} {6,S}
6 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89514,0.00882046,6.54253e-05,-2.03925e-07,1.86549e-10,57818.2,9.54567], Tmin=(10,'K'), Tmax=(362.963,'K')),
            NASAPolynomial(coeffs=[3.67819,0.0195588,-1.34502e-05,4.31121e-09,-5.21597e-13,57779,9.61499], Tmin=(362.963,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (480.738,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 403,
    label = "ON[C]DN",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {6,S}
2 N u0 p1 c0 {1,S} {4,S} {5,S}
3 N u0 p1 c0 {4,D} {7,S}
4 C u1 p0 c0 {2,S} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90544,0.00655667,8.76256e-05,-2.3005e-07,1.77918e-10,26723.5,8.91586], Tmin=(10,'K'), Tmax=(446.426,'K')),
            NASAPolynomial(coeffs=[4.35248,0.0194228,-1.22941e-05,3.82083e-09,-4.58273e-13,26515.5,5.23667], Tmin=(446.426,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (222.183,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 404,
    label = "[O-][N+]#CO[O]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 O u1 p2 c0 {1,S}
3 O u0 p3 c-1 {4,S}
4 N u0 p0 c+1 {3,S} {5,T}
5 C u0 p0 c0 {1,S} {4,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78698,0.0186437,4.91006e-06,-7.22059e-08,7.48323e-11,39152.3,9.66461], Tmin=(10,'K'), Tmax=(425.224,'K')),
            NASAPolynomial(coeffs=[5.36559,0.0132909,-9.70873e-06,3.2364e-09,-4.01731e-13,38932.1,2.38907], Tmin=(425.224,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (325.525,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 405,
    label = "CDNCD[N]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,D} {4,S}
2 N u1 p1 c0 {4,D}
3 C u0 p0 c0 {1,D} {5,S} {6,S}
4 C u0 p0 c0 {1,S} {2,D} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97666,0.00158208,7.26671e-05,-1.50435e-07,1.02623e-10,41741.1,8.74747], Tmin=(10,'K'), Tmax=(375.033,'K')),
            NASAPolynomial(coeffs=[1.9368,0.0233383,-1.43483e-05,4.2425e-09,-4.84148e-13,41894.1,16.5881], Tmin=(375.033,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (347.053,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 406,
    label = "[NH]CNDC",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {4,D}
2 N u1 p1 c0 {3,S} {9,S}
3 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4 C u0 p0 c0 {1,D} {7,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97077,0.00189929,9.32372e-05,-1.80597e-07,1.14661e-10,34034.6,9.05785], Tmin=(10,'K'), Tmax=(404.389,'K')),
            NASAPolynomial(coeffs=[0.890457,0.0323785,-1.98579e-05,5.91231e-09,-6.82071e-13,34283.6,21.1287], Tmin=(404.389,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (282.974,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 407,
    label = "[O-][NH+]DCND[CH]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {4,D} {7,S}
3 N u0 p1 c0 {4,S} {5,D}
4 C u0 p0 c0 {2,D} {3,S} {6,S}
5 C u1 p0 c0 {3,D} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89793,0.00713922,0.000107477,-2.74784e-07,2.11024e-10,44477.8,10.0318], Tmin=(10,'K'), Tmax=(438.054,'K')),
            NASAPolynomial(coeffs=[3.74126,0.0260027,-1.68098e-05,5.2136e-09,-6.19752e-13,44324.3,8.74919], Tmin=(438.054,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (369.802,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 408,
    label = "[O-][NH+]DCDCDO",
    molecule = 
"""
1 O u0 p3 c-1 {3,S}
2 O u0 p2 c0 {5,D}
3 N u0 p0 c+1 {1,S} {4,D} {6,S}
4 C u0 p0 c0 {3,D} {5,D}
5 C u0 p0 c0 {2,D} {4,D}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89509,0.00852777,3.51824e-05,-7.89655e-08,4.93947e-11,15952.9,9.2775], Tmin=(10,'K'), Tmax=(531.856,'K')),
            NASAPolynomial(coeffs=[3.41311,0.0187436,-1.22177e-05,3.74932e-09,-4.37783e-13,15910.9,10.4221], Tmin=(531.856,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (132.624,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 409,
    label = "CNCD[CH]",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {3,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {4,D} {9,S}
4  C u1 p0 c0 {3,D} {10,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95796,0.00320491,0.000128333,-3.16762e-07,2.63021e-10,34889.4,7.84015], Tmin=(10,'K'), Tmax=(305.627,'K')),
            NASAPolynomial(coeffs=[1.65658,0.0333216,-1.94616e-05,5.58652e-09,-6.27557e-13,35030.1,16.2152], Tmin=(305.627,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (290.094,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 410,
    label = "[O-][NH+]DCDCDN",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {4,D} {6,S}
3 N u0 p1 c0 {5,D} {7,S}
4 C u0 p0 c0 {2,D} {5,D}
5 C u0 p0 c0 {3,D} {4,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8416,0.0136745,3.6036e-05,-1.01906e-07,7.53804e-11,45473,9.45985], Tmin=(10,'K'), Tmax=(460.36,'K')),
            NASAPolynomial(coeffs=[3.69644,0.0220255,-1.4275e-05,4.40452e-09,-5.18827e-13,45411.2,9.23157], Tmin=(460.36,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (378.073,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 411,
    label = "[O-][NH+]D[C]OC",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {2,S} {5,D} {9,S}
4 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
5 C u1 p0 c0 {1,S} {3,D}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76982,0.0238585,-5.82361e-06,-4.8272e-09,2.31192e-12,11953.6,8.80122], Tmin=(10,'K'), Tmax=(1191.64,'K')),
            NASAPolynomial(coeffs=[6.86307,0.0203695,-1.011e-05,2.4259e-09,-2.28311e-13,10726.9,-8.71809], Tmin=(1191.64,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (99.3795,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 412,
    label = "NND[N]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u1 p1 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9771,0.00135914,3.72795e-05,-6.96091e-08,4.04346e-11,37808.8,6.82036], Tmin=(10,'K'), Tmax=(545.148,'K')),
            NASAPolynomial(coeffs=[3.0956,0.0128082,-7.92913e-06,2.43806e-09,-2.92066e-13,37830.9,9.85939], Tmin=(545.148,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (314.351,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 413,
    label = "ON[C]DO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {6,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 C u1 p0 c0 {2,D} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91642,0.00606923,7.26751e-05,-2.03014e-07,1.66527e-10,-3242.51,8.87729], Tmin=(10,'K'), Tmax=(420.464,'K')),
            NASAPolynomial(coeffs=[4.23228,0.0162235,-1.04955e-05,3.29095e-09,-3.95571e-13,-3385.39,6.24387], Tmin=(420.464,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-26.9614,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 414,
    label = "[O-][N+]#CON",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p3 c-1 {4,S}
3 N u0 p1 c0 {1,S} {6,S} {7,S}
4 N u0 p0 c+1 {2,S} {5,T}
5 C u0 p0 c0 {1,S} {4,T}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80091,0.0214368,0.000106869,-7.39103e-07,1.25058e-09,29580.2,9.08865], Tmin=(10,'K'), Tmax=(226.986,'K')),
            NASAPolynomial(coeffs=[5.07557,0.0192207,-1.22802e-05,3.8037e-09,-4.53476e-13,29470.2,3.68041], Tmin=(226.986,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (245.972,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 415,
    label = "NNNO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {9,S}
2 N u0 p1 c0 {3,S} {4,S} {5,S}
3 N u0 p1 c0 {1,S} {2,S} {6,S}
4 N u0 p1 c0 {2,S} {7,S} {8,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93752,0.00383234,9.29137e-05,-1.85039e-07,1.14113e-10,14505,8.51162], Tmin=(10,'K'), Tmax=(521.355,'K')),
            NASAPolynomial(coeffs=[2.381,0.0290511,-1.78421e-05,5.43175e-09,-6.43784e-13,14486.8,13.2766], Tmin=(521.355,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (120.58,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 416,
    label = "[O-][NH+]DC[N]C",
    molecule = 
"""
multiplicity 2
1  O u0 p3 c-1 {2,S}
2  N u0 p0 c+1 {1,S} {5,D} {10,S}
3  N u1 p1 c0 {4,S} {5,S}
4  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {2,D} {3,S} {9,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75515,0.0195906,2.45921e-05,-5.63177e-08,3.18692e-11,13498.3,8.90924], Tmin=(10,'K'), Tmax=(475.726,'K')),
            NASAPolynomial(coeffs=[2.09252,0.0335703,-1.9487e-05,5.45312e-09,-5.92093e-13,13656.5,15.6953], Tmin=(475.726,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (112.196,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 417,
    label = "CNNDN",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {4,S} {8,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {2,D} {9,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92474,0.0129691,1.84928e-05,-2.61486e-08,9.02589e-12,25308,6.91364], Tmin=(10,'K'), Tmax=(1032.54,'K')),
            NASAPolynomial(coeffs=[3.58992,0.0242002,-1.22545e-05,3.02137e-09,-2.9283e-13,24847.5,5.97532], Tmin=(1032.54,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (210.447,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 418,
    label = "CO[N]N",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 N u0 p1 c0 {3,S} {8,S} {9,S}
3 N u1 p1 c0 {1,S} {2,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81537,0.019948,4.01829e-09,-8.42056e-09,3.16733e-12,15928.8,7.91397], Tmin=(10,'K'), Tmax=(1166.75,'K')),
            NASAPolynomial(coeffs=[5.47167,0.0210763,-1.01973e-05,2.40846e-09,-2.24379e-13,15079,-2.31756], Tmin=(1166.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (132.436,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 419,
    label = "[O-][NH+]DCC[NH]",
    molecule = 
"""
multiplicity 2
1  O u0 p3 c-1 {2,S}
2  N u0 p0 c+1 {1,S} {5,D} {9,S}
3  N u1 p1 c0 {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {2,D} {4,S} {8,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82994,0.0164903,3.76691e-05,-6.82212e-08,3.21804e-11,28552.2,10.5679], Tmin=(10,'K'), Tmax=(722.497,'K')),
            NASAPolynomial(coeffs=[2.81778,0.0330584,-1.9492e-05,5.52727e-09,-6.06242e-13,28412.3,13.1416], Tmin=(722.497,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (237.384,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 420,
    label = "[CH2]N",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07214,-0.00685568,8.19129e-05,-1.52251e-07,9.61278e-11,16587.8,4.81925], Tmin=(10,'K'), Tmax=(467.053,'K')),
            NASAPolynomial(coeffs=[2.07954,0.0157633,-8.56716e-06,2.35833e-09,-2.57919e-13,16713.3,12.267], Tmin=(467.053,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (137.918,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 421,
    label = "[O-][NH+]CC",
    molecule = 
"""
multiplicity 2
1  O u0 p3 c-1 {2,S}
2  N u1 p0 c+1 {1,S} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8528,0.0152813,2.20752e-05,-3.31531e-08,1.22589e-11,174.074,8.15565], Tmin=(10,'K'), Tmax=(936.372,'K')),
            NASAPolynomial(coeffs=[2.49226,0.0300465,-1.59202e-05,4.10981e-09,-4.16209e-13,36.3599,12.5341], Tmin=(936.372,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (1.45206,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 422,
    label = "NNC#N",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {6,S} {7,S}
3 N u0 p1 c0 {4,T}
4 C u0 p0 c0 {1,S} {3,T}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94302,0.00380616,7.54392e-05,-1.74337e-07,1.24174e-10,30510,7.99563], Tmin=(10,'K'), Tmax=(460.648,'K')),
            NASAPolynomial(coeffs=[3.39238,0.0195693,-1.16495e-05,3.45371e-09,-4.0169e-13,30444.2,8.96069], Tmin=(460.648,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (253.666,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 423,
    label = "CCON",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {3,S}
2  N u0 p1 c0 {1,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73354,0.027612,-5.18971e-05,1.47174e-07,-1.32769e-10,-9292.23,7.4778], Tmin=(10,'K'), Tmax=(448.321,'K')),
            NASAPolynomial(coeffs=[0.460228,0.0376077,-2.10694e-05,5.75849e-09,-6.15209e-13,-8805.69,22.7967], Tmin=(448.321,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-77.2652,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 424,
    label = "[N-]([NH+]DO)O[NH]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {3,D}
3 N u0 p0 c+1 {2,D} {4,S} {6,S}
4 N u0 p2 c-1 {1,S} {3,S}
5 N u1 p1 c0 {1,S} {7,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90046,0.00718558,8.26688e-05,-2.03496e-07,1.48284e-10,46776.1,10.0913], Tmin=(10,'K'), Tmax=(461.422,'K')),
            NASAPolynomial(coeffs=[3.6656,0.0233391,-1.5737e-05,4.98909e-09,-5.98838e-13,46647.5,9.41415], Tmin=(461.422,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (388.906,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 425,
    label = "N[N]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {6,S}
2 N u0 p1 c0 {3,S} {4,S} {5,S}
3 N u1 p1 c0 {1,S} {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96228,0.00226427,5.16465e-05,-1.01141e-07,6.08085e-11,14752.2,7.36461], Tmin=(10,'K'), Tmax=(542.028,'K')),
            NASAPolynomial(coeffs=[3.20823,0.0161801,-9.9747e-06,3.07543e-09,-3.69739e-13,14711.2,9.40904], Tmin=(542.028,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (122.642,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 426,
    label = "CNDCD[CH]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,D}
2 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3 C u0 p0 c0 {1,D} {4,D}
4 C u1 p0 c0 {3,D} {8,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97089,0.00394567,0.000279965,-1.88286e-06,4.40219e-09,44935.1,6.84601], Tmin=(10,'K'), Tmax=(126.389,'K')),
            NASAPolynomial(coeffs=[3.53211,0.0232493,-1.34234e-05,3.79246e-09,-4.18267e-13,44941.9,7.88414], Tmin=(126.389,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (375.313,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 427,
    label = "CCND[N]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {3,S}
2 N u1 p1 c0 {1,D}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83542,0.0145661,1.78065e-05,-2.91371e-08,1.13599e-11,22856.7,7.99518], Tmin=(10,'K'), Tmax=(878.677,'K')),
            NASAPolynomial(coeffs=[2.4491,0.0272811,-1.48316e-05,3.92044e-09,-4.0552e-13,22853.1,13.0973], Tmin=(878.677,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (190.032,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 428,
    label = "[O-][NH+]DCCN",
    molecule = 
"""
1  O u0 p3 c-1 {3,S}
2  N u0 p1 c0 {4,S} {9,S} {10,S}
3  N u0 p0 c+1 {1,S} {5,D} {11,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {3,D} {4,S} {8,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89967,0.00877055,8.87984e-05,-1.73887e-07,1.0783e-10,4654.58,9.58232], Tmin=(10,'K'), Tmax=(416.533,'K')),
            NASAPolynomial(coeffs=[0.62955,0.040174,-2.42909e-05,7.11542e-09,-8.06572e-13,4927,22.4948], Tmin=(416.533,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (38.6928,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 429,
    label = "[O-][NH+]DCN[O]",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 O u0 p3 c-1 {4,S}
3 N u0 p1 c0 {1,S} {5,S} {8,S}
4 N u0 p0 c+1 {2,S} {5,D} {7,S}
5 C u0 p0 c0 {3,S} {4,D} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92897,0.00439926,9.19915e-05,-1.91171e-07,1.20933e-10,13613.5,9.95727], Tmin=(10,'K'), Tmax=(518.493,'K')),
            NASAPolynomial(coeffs=[2.86653,0.0274964,-1.79364e-05,5.59875e-09,-6.68255e-13,13523.4,12.4536], Tmin=(518.493,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (113.167,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 430,
    label = "NCCD[CH]",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {4,D} {7,S}
4  C u1 p0 c0 {3,D} {10,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94972,0.00333656,0.000112036,-2.35195e-07,1.58762e-10,33963.9,9.18447], Tmin=(10,'K'), Tmax=(445.645,'K')),
            NASAPolynomial(coeffs=[1.46829,0.0341535,-2.04501e-05,6.02172e-09,-6.9197e-13,34100.2,18.1985], Tmin=(445.645,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (282.385,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 431,
    label = "[O-][NH+]DCOO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 O u0 p2 c0 {1,S} {8,S}
3 O u0 p3 c-1 {4,S}
4 N u0 p0 c+1 {3,S} {5,D} {7,S}
5 C u0 p0 c0 {1,S} {4,D} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93344,0.00404316,9.00601e-05,-1.80641e-07,1.10509e-10,-5418.21,9.52187], Tmin=(10,'K'), Tmax=(532.506,'K')),
            NASAPolynomial(coeffs=[2.6,0.0283477,-1.86509e-05,5.84686e-09,-6.99458e-13,-5478.78,13.2125], Tmin=(532.506,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-45.0732,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 432,
    label = "[O-][N+]#CNDC",
    molecule = 
"""
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {4,D} {5,S}
3 N u0 p0 c+1 {1,S} {5,T}
4 C u0 p0 c0 {2,D} {6,S} {7,S}
5 C u0 p0 c0 {2,S} {3,T}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90244,0.00879644,0.000109739,-4.1008e-07,4.67937e-10,36825.9,8.75869], Tmin=(10,'K'), Tmax=(291.133,'K')),
            NASAPolynomial(coeffs=[3.77292,0.0216906,-1.39601e-05,4.31115e-09,-5.10876e-13,36786.3,8.41478], Tmin=(291.133,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (306.205,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 433,
    label = "[O-][N+]DCDNC",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {4,S} {5,D}
3 N u1 p0 c+1 {1,S} {5,D}
4 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
5 C u0 p0 c0 {2,D} {3,D}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56114,0.0401094,-9.94202e-05,1.65124e-07,-1.04364e-10,37358.9,9.12137], Tmin=(10,'K'), Tmax=(501.757,'K')),
            NASAPolynomial(coeffs=[4.16574,0.0233649,-1.3714e-05,3.88371e-09,-4.26794e-13,37448.4,8.11732], Tmin=(501.757,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (310.603,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 434,
    label = "ONDN",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {2,D} {5,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08251,-0.00655413,6.10713e-05,-9.21232e-08,4.54138e-11,8048.77,6.51046], Tmin=(10,'K'), Tmax=(635.119,'K')),
            NASAPolynomial(coeffs=[2.1329,0.0143642,-8.73781e-06,2.57197e-09,-2.91659e-13,8122.16,13.6594], Tmin=(635.119,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (66.926,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 435,
    label = "[O-][N+]#CN",
    molecule = 
"""
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {4,S} {5,S} {6,S}
3 N u0 p0 c+1 {1,S} {4,T}
4 C u0 p0 c0 {2,S} {3,T}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72089,0.0211959,-2.53414e-05,1.9367e-08,-6.33994e-12,23907.8,8.04265], Tmin=(10,'K'), Tmax=(810.498,'K')),
            NASAPolynomial(coeffs=[5.06346,0.0129603,-7.12062e-06,1.92933e-09,-2.05419e-13,23743,2.17375], Tmin=(810.498,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (198.738,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 436,
    label = "NCDCN",
    molecule = 
"""
1  N u0 p1 c0 {3,S} {7,S} {8,S}
2  N u0 p1 c0 {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {5,S}
4  C u0 p0 c0 {2,S} {3,D} {6,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93495,0.00435365,0.000113655,-2.50285e-07,1.74538e-10,6596.31,8.40657], Tmin=(10,'K'), Tmax=(449.555,'K')),
            NASAPolynomial(coeffs=[2.15345,0.0321581,-1.90016e-05,5.58398e-09,-6.4299e-13,6635.7,14.2336], Tmin=(449.555,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (54.8361,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 437,
    label = "O[N]CO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {7,S}
2 O u0 p2 c0 {3,S} {8,S}
3 N u1 p1 c0 {2,S} {4,S}
4 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9464,0.00458599,9.72933e-05,-2.58249e-07,2.27757e-10,-12859.3,9.29328], Tmin=(10,'K'), Tmax=(288.217,'K')),
            NASAPolynomial(coeffs=[2.37076,0.0264535,-1.65144e-05,4.99705e-09,-5.82934e-13,-12768.5,14.9347], Tmin=(288.217,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-106.909,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 438,
    label = "N[N]CO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {9,S}
2 N u0 p1 c0 {3,S} {7,S} {8,S}
3 N u1 p1 c0 {2,S} {4,S}
4 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94973,0.00307565,9.09138e-05,-1.74688e-07,1.05445e-10,2266.21,9.06235], Tmin=(10,'K'), Tmax=(515.394,'K')),
            NASAPolynomial(coeffs=[1.71077,0.0306367,-1.89404e-05,5.7494e-09,-6.77239e-13,2361.74,17.0678], Tmin=(515.394,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (18.8254,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 439,
    label = "[O-][N+]DCDC",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u1 p0 c+1 {1,S} {4,D}
3 C u0 p0 c0 {4,D} {5,S} {6,S}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90376,0.00731391,8.13753e-05,-2.58176e-07,2.35929e-10,32687.9,7.79004], Tmin=(10,'K'), Tmax=(387.448,'K')),
            NASAPolynomial(coeffs=[4.69972,0.0148916,-9.11286e-06,2.74374e-09,-3.22363e-13,32507.7,3.17473], Tmin=(387.448,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (271.79,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 440,
    label = "[CH2]CDCN",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {3,S} {9,S} {10,S}
2  C u0 p0 c0 {3,D} {4,S} {5,S}
3  C u0 p0 c0 {1,S} {2,D} {6,S}
4  C u1 p0 c0 {2,S} {7,S} {8,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93163,0.00412187,0.000104291,-2.01674e-07,1.20819e-10,17389.2,8.03594], Tmin=(10,'K'), Tmax=(534.361,'K')),
            NASAPolynomial(coeffs=[1.91916,0.0339719,-2.10049e-05,6.42579e-09,-7.65286e-13,17393.2,14.5086], Tmin=(534.361,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (144.557,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 441,
    label = "[N]DCDCNDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {4,S}
3 N u1 p1 c0 {5,D}
4 C u0 p0 c0 {2,S} {5,D} {6,S}
5 C u0 p0 c0 {3,D} {4,D}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92485,0.00512975,7.45221e-05,-1.86559e-07,1.38745e-10,35965.6,9.87666], Tmin=(10,'K'), Tmax=(456.524,'K')),
            NASAPolynomial(coeffs=[3.94924,0.0182143,-1.2164e-05,3.83672e-09,-4.60217e-13,35824.8,8.26035], Tmin=(456.524,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (299.025,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 442,
    label = "CDNCDO",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,D} {4,S}
3 C u0 p0 c0 {2,D} {5,S} {6,S}
4 C u0 p0 c0 {1,D} {2,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98411,0.00858147,1.74802e-05,-2.38607e-08,8.34043e-12,-4968.36,7.96587], Tmin=(10,'K'), Tmax=(1018.21,'K')),
            NASAPolynomial(coeffs=[4.01847,0.0175172,-9.04627e-06,2.25642e-09,-2.20194e-13,-5445.57,5.49047], Tmin=(1018.21,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-41.2757,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 443,
    label = "[O-][NH+]DCDCC",
    molecule = 
"""
1  O u0 p3 c-1 {2,S}
2  N u0 p0 c+1 {1,S} {5,D} {10,S}
3  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {2,D} {4,D}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84491,0.0237447,-2.29212e-07,-1.00053e-08,3.75023e-12,26067.8,8.4301], Tmin=(10,'K'), Tmax=(1207.6,'K')),
            NASAPolynomial(coeffs=[7.35367,0.0220002,-1.03317e-05,2.34531e-09,-2.08847e-13,24500.1,-12.1416], Tmin=(1207.6,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (216.756,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 444,
    label = "[O-][N+]#CCO",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {8,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {2,S} {5,T}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 C u0 p0 c0 {3,T} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74473,0.0232643,-1.03987e-05,-8.33377e-10,1.40665e-12,-2286.02,9.87697], Tmin=(10,'K'), Tmax=(1059.74,'K')),
            NASAPolynomial(coeffs=[5.99366,0.0188801,-1.00027e-05,2.57223e-09,-2.58932e-13,-2993.15,-2.19073], Tmin=(1059.74,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-19.0241,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 445,
    label = "[O-][NH+]DCND[N]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {5,D} {7,S}
3 N u0 p1 c0 {4,D} {5,S}
4 N u1 p1 c0 {3,D}
5 C u0 p0 c0 {2,D} {3,S} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85253,0.0119463,0.000108162,-3.88668e-07,3.92745e-10,43837.1,9.81836], Tmin=(10,'K'), Tmax=(354.991,'K')),
            NASAPolynomial(coeffs=[5.02377,0.0196387,-1.26112e-05,3.9098e-09,-4.66515e-13,43622.3,3.52686], Tmin=(354.991,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (364.501,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 446,
    label = "[O-][NH+]DCCDO",
    molecule = 
"""
1 O u0 p3 c-1 {3,S}
2 O u0 p2 c0 {5,D}
3 N u0 p0 c+1 {1,S} {4,D} {7,S}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 C u0 p0 c0 {2,D} {4,S} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.938,0.00491182,7.77397e-05,-1.66598e-07,1.15289e-10,-8862.76,9.21732], Tmin=(10,'K'), Tmax=(370.93,'K')),
            NASAPolynomial(coeffs=[1.74378,0.0285736,-1.79456e-05,5.37492e-09,-6.17837e-13,-8699.98,17.6271], Tmin=(370.93,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-73.6928,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 447,
    label = "[O-][NH+]DCC[CH2]",
    molecule = 
"""
multiplicity 2
1  O u0 p3 c-1 {2,S}
2  N u0 p0 c+1 {1,S} {4,D} {11,S}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {2,D} {3,S} {8,S}
5  C u1 p0 c0 {3,S} {9,S} {10,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76084,0.0250058,1.04171e-05,-2.7039e-08,1.11314e-11,22694.5,10.33], Tmin=(10,'K'), Tmax=(935.037,'K')),
            NASAPolynomial(coeffs=[4.50459,0.0321072,-1.74712e-05,4.60655e-09,-4.74272e-13,22105.9,4.388], Tmin=(935.037,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (188.695,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 448,
    label = "[NH-][N+]DCDN",
    molecule = 
"""
multiplicity 2
1 N u1 p0 c+1 {2,S} {4,D}
2 N u0 p2 c-1 {1,S} {5,S}
3 N u0 p1 c0 {4,D} {6,S}
4 C u0 p0 c0 {1,D} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90796,0.00671625,7.62454e-05,-2.22001e-07,1.87188e-10,51523,8.54083], Tmin=(10,'K'), Tmax=(415.931,'K')),
            NASAPolynomial(coeffs=[4.55091,0.0155748,-9.94798e-06,3.09949e-09,-3.72079e-13,51339.4,4.43887], Tmin=(415.931,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (428.386,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 449,
    label = "N[C]DCDN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {5,S} {6,S}
2 N u0 p1 c0 {4,D} {7,S}
3 C u1 p0 c0 {1,S} {4,D}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85812,0.0111699,0.000104044,-3.7086e-07,3.67381e-10,45517.9,8.01469], Tmin=(10,'K'), Tmax=(368.538,'K')),
            NASAPolynomial(coeffs=[5.50521,0.0161675,-9.4005e-06,2.77385e-09,-3.24375e-13,45241.1,-0.394972], Tmin=(368.538,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (378.473,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 450,
    label = "[O-][NH+]DNND[CH]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {6,S}
3 N u0 p1 c0 {2,D} {4,S}
4 N u0 p1 c0 {3,S} {5,D}
5 C u1 p0 c0 {4,D} {7,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88677,0.00780555,9.66687e-05,-2.56306e-07,1.97285e-10,60903.5,9.83177], Tmin=(10,'K'), Tmax=(453.055,'K')),
            NASAPolynomial(coeffs=[4.63678,0.0212364,-1.41903e-05,4.51615e-09,-5.47424e-13,60629.7,4.536], Tmin=(453.055,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (506.367,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 451,
    label = "[O-][NH+]D[N]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {4,S}
3 N u1 p1 c0 {2,D}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04484,-0.00324749,3.32247e-05,-4.53918e-08,1.99842e-11,35660.9,6.95481], Tmin=(10,'K'), Tmax=(707.101,'K')),
            NASAPolynomial(coeffs=[2.47556,0.0105499,-6.4814e-06,1.88424e-09,-2.09695e-13,35759.8,13.112], Tmin=(707.101,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (296.508,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 452,
    label = "NC[NH]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {6,S} {7,S}
2 N u1 p1 c0 {3,S} {8,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97525,0.00154313,6.96931e-05,-1.27787e-07,7.68185e-11,22035.9,7.71554], Tmin=(10,'K'), Tmax=(427.312,'K')),
            NASAPolynomial(coeffs=[1.39933,0.0256599,-1.49785e-05,4.33492e-09,-4.92653e-13,22256,17.9523], Tmin=(427.312,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (183.208,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 453,
    label = "CNDN",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {7,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99783,-8.95659e-05,4.55258e-05,-6.29028e-08,2.8075e-11,19575.9,5.73678], Tmin=(10,'K'), Tmax=(582.026,'K')),
            NASAPolynomial(coeffs=[0.737778,0.0223154,-1.22166e-05,3.23698e-09,-3.34432e-13,19955.4,19.7002], Tmin=(582.026,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (162.759,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 454,
    label = "[N-]D[N+]DCD[N]",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {3,D} {4,D}
2 N u1 p1 c0 {4,D}
3 N u0 p2 c-1 {1,D}
4 C u0 p0 c0 {1,D} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93908,0.00446169,4.48117e-05,-1.38644e-07,1.20459e-10,57155.2,7.88382], Tmin=(10,'K'), Tmax=(414.221,'K')),
            NASAPolynomial(coeffs=[4.62246,0.00808797,-5.34908e-06,1.68311e-09,-2.0302e-13,57010.9,4.13029], Tmin=(414.221,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (475.215,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 455,
    label = "[O-][N+]DNCC",
    molecule = 
"""
multiplicity 2
1  O u0 p3 c-1 {3,S}
2  N u0 p1 c0 {3,D} {4,S}
3  N u1 p0 c+1 {1,S} {2,D}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84308,0.0198259,1.23251e-05,-2.36133e-08,8.65435e-12,18882.8,9.21994], Tmin=(10,'K'), Tmax=(1034.75,'K')),
            NASAPolynomial(coeffs=[4.68436,0.027368,-1.42557e-05,3.59344e-09,-3.54616e-13,18130.9,2.34019], Tmin=(1034.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (157.018,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 456,
    label = "[N-]([NH+]DO)NDC",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 N u0 p0 c+1 {1,D} {3,S} {6,S}
3 N u0 p2 c-1 {2,S} {4,S}
4 N u0 p1 c0 {3,S} {5,D}
5 C u0 p0 c0 {4,D} {7,S} {8,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9114,0.00727781,5.8037e-05,-1.07339e-07,5.91143e-11,32791.6,8.96971], Tmin=(10,'K'), Tmax=(578.702,'K')),
            NASAPolynomial(coeffs=[2.20299,0.0277038,-1.72437e-05,5.11593e-09,-5.82485e-13,32845,15.0306], Tmin=(578.702,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (272.627,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 457,
    label = "ONNDC",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {8,S}
2 N u0 p1 c0 {1,S} {3,S} {5,S}
3 N u0 p1 c0 {2,S} {4,D}
4 C u0 p0 c0 {3,D} {6,S} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95972,0.00234529,7.50179e-05,-1.33849e-07,7.45067e-11,14645.6,7.84127], Tmin=(10,'K'), Tmax=(555.37,'K')),
            NASAPolynomial(coeffs=[1.49863,0.028523,-1.85135e-05,5.82888e-09,-7.04687e-13,14788.6,17.0937], Tmin=(555.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (121.753,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 458,
    label = "NOC[O]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u1 p2 c0 {4,S}
3 N u0 p1 c0 {1,S} {7,S} {8,S}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88926,0.0130419,1.87707e-05,-3.19823e-08,1.30789e-11,-1168.72,9.13374], Tmin=(10,'K'), Tmax=(866.755,'K')),
            NASAPolynomial(coeffs=[3.58303,0.0228528,-1.27411e-05,3.4331e-09,-3.6015e-13,-1431.08,8.74765], Tmin=(866.755,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-9.7087,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 459,
    label = "CNDO",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9792,0.00116982,3.9375e-05,-6.32788e-08,3.29232e-11,6893.94,5.85023], Tmin=(10,'K'), Tmax=(496.007,'K')),
            NASAPolynomial(coeffs=[1.96906,0.0173785,-9.63648e-06,2.58805e-09,-2.71394e-13,7093.38,14.1388], Tmin=(496.007,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (57.3086,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 460,
    label = "[CH2]NDCDN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {4,D}
2 N u0 p1 c0 {4,D} {7,S}
3 C u1 p0 c0 {1,S} {5,S} {6,S}
4 C u0 p0 c0 {1,D} {2,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91097,0.00588734,8.47595e-05,-2.08323e-07,1.50888e-10,37710.2,7.52447], Tmin=(10,'K'), Tmax=(477.764,'K')),
            NASAPolynomial(coeffs=[4.45089,0.0189992,-1.17653e-05,3.61363e-09,-4.33075e-13,37457.4,3.21244], Tmin=(477.764,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (313.523,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 461,
    label = "[O]CNDC",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 N u0 p1 c0 {3,S} {4,D}
3 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4 C u0 p0 c0 {2,D} {7,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97231,0.00173992,7.81514e-05,-1.45906e-07,8.87499e-11,15006.1,9.24119], Tmin=(10,'K'), Tmax=(422.825,'K')),
            NASAPolynomial(coeffs=[1.11338,0.0287786,-1.77441e-05,5.25097e-09,-5.99309e-13,15247.9,20.5737], Tmin=(422.825,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (124.759,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 462,
    label = "[O-][NH+]D[C]CC",
    molecule = 
"""
multiplicity 2
1  O u0 p3 c-1 {2,S}
2  N u0 p0 c+1 {1,S} {5,D} {11,S}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
5  C u1 p0 c0 {2,D} {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86291,0.0233383,8.47218e-06,-1.94875e-08,6.8807e-12,29464.8,8.87859], Tmin=(10,'K'), Tmax=(1129.72,'K')),
            NASAPolynomial(coeffs=[6.26502,0.0273043,-1.33523e-05,3.16322e-09,-2.94184e-13,28126.2,-6.52539], Tmin=(1129.72,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (245.015,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 463,
    label = "N[C]DCDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,S} {5,S} {6,S}
3 C u1 p0 c0 {2,S} {4,D}
4 C u0 p0 c0 {1,D} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91453,0.00612007,7.44456e-05,-2.13153e-07,1.77093e-10,16341.8,8.11782], Tmin=(10,'K'), Tmax=(424.219,'K')),
            NASAPolynomial(coeffs=[4.6816,0.0142384,-8.54003e-06,2.56256e-09,-3.02409e-13,16138.6,3.44685], Tmin=(424.219,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (135.871,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 464,
    label = "CNN[CH2]",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {3,S} {8,S}
2  N u0 p1 c0 {1,S} {4,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4  C u1 p0 c0 {2,S} {10,S} {11,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86021,0.0110853,7.41541e-05,-1.50799e-07,9.62055e-11,29496.4,7.48438], Tmin=(10,'K'), Tmax=(404.221,'K')),
            NASAPolynomial(coeffs=[1.27503,0.0366671,-2.07758e-05,5.76597e-09,-6.25535e-13,29705.4,17.6147], Tmin=(404.221,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (245.224,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 465,
    label = "[NH-][N+]DCDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 N u1 p0 c+1 {3,S} {4,D}
3 N u0 p2 c-1 {2,S} {5,S}
4 C u0 p0 c0 {1,D} {2,D}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94517,0.00370488,5.40121e-05,-1.35216e-07,1.00271e-10,20788.2,8.04445], Tmin=(10,'K'), Tmax=(462.015,'K')),
            NASAPolynomial(coeffs=[4.11058,0.0125491,-8.06556e-06,2.50134e-09,-2.98659e-13,20663.2,6.18719], Tmin=(462.015,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (172.835,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 466,
    label = "[O-][NH+]DCC",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {4,D} {9,S}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {2,D} {3,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9922,0.0105021,2.63832e-05,-3.43215e-08,1.18211e-11,630.083,7.45886], Tmin=(10,'K'), Tmax=(1018.38,'K')),
            NASAPolynomial(coeffs=[3.59245,0.0244805,-1.24825e-05,3.08577e-09,-2.99063e-13,68.0693,6.23561], Tmin=(1018.38,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (5.28573,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 467,
    label = "CCDCDN",
    molecule = 
"""
1 N u0 p1 c0 {4,D} {9,S}
2 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {4,D} {8,S}
4 C u0 p0 c0 {1,D} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92273,0.00612533,7.19376e-05,-1.442e-07,9.27499e-11,18163.8,7.14311], Tmin=(10,'K'), Tmax=(399.764,'K')),
            NASAPolynomial(coeffs=[1.5397,0.0299696,-1.75307e-05,5.00089e-09,-5.55218e-13,18354.4,16.4549], Tmin=(399.764,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (151.011,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 468,
    label = "[NH]CNO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {9,S}
2 N u0 p1 c0 {1,S} {4,S} {7,S}
3 N u1 p1 c0 {4,S} {8,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94165,0.00424633,0.00011067,-2.64775e-07,2.03518e-10,18313.9,9.1831], Tmin=(10,'K'), Tmax=(395.223,'K')),
            NASAPolynomial(coeffs=[2.19704,0.030093,-1.85084e-05,5.5549e-09,-6.44956e-13,18387.9,15.1711], Tmin=(395.223,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (152.274,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 469,
    label = "NOCDC",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {8,S} {9,S}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {3,D} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85926,0.0123765,3.26376e-05,-5.62972e-08,2.65615e-11,5325,8.73294], Tmin=(10,'K'), Tmax=(680.714,'K')),
            NASAPolynomial(coeffs=[2.08196,0.0287452,-1.64877e-05,4.60093e-09,-4.99986e-13,5429.7,15.6156], Tmin=(680.714,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (44.2594,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 470,
    label = "[O-][N+]#CCN",
    molecule = 
"""
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {4,S} {8,S} {9,S}
3 N u0 p0 c+1 {1,S} {5,T}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 C u0 p0 c0 {3,T} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73588,0.0221486,3.51869e-06,-2.1827e-08,1.16817e-11,18433.5,9.97759], Tmin=(10,'K'), Tmax=(705.753,'K')),
            NASAPolynomial(coeffs=[3.57547,0.0271042,-1.56143e-05,4.37031e-09,-4.75969e-13,18355.3,9.9816], Tmin=(705.753,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (153.234,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 471,
    label = "[O-][NH+]CDO",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 O u0 p2 c0 {4,D}
3 N u1 p0 c+1 {1,S} {4,S} {5,S}
4 C u0 p0 c0 {2,D} {3,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9729,0.0017947,6.0515e-05,-1.26737e-07,8.49425e-11,-11255.7,8.62396], Tmin=(10,'K'), Tmax=(446.608,'K')),
            NASAPolynomial(coeffs=[2.54877,0.0189651,-1.19839e-05,3.62083e-09,-4.19963e-13,-11172.5,13.8537], Tmin=(446.608,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-93.5886,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 472,
    label = "NDNC#N",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {4,S}
2 N u0 p1 c0 {1,D} {5,S}
3 N u0 p1 c0 {4,T}
4 C u0 p0 c0 {1,S} {3,T}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96758,0.0021725,4.84763e-05,-1.09538e-07,7.70141e-11,46876.7,7.48191], Tmin=(10,'K'), Tmax=(454.82,'K')),
            NASAPolynomial(coeffs=[3.34325,0.0135649,-8.55962e-06,2.59336e-09,-3.02571e-13,46872.5,9.33104], Tmin=(454.82,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (389.75,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 473,
    label = "ODNC#N",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {4,S}
3 N u0 p1 c0 {4,T}
4 C u0 p0 c0 {2,S} {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93339,0.0050756,4.59395e-05,-1.51752e-07,1.39522e-10,37176.1,7.51576], Tmin=(10,'K'), Tmax=(392.427,'K')),
            NASAPolynomial(coeffs=[4.59402,0.00847054,-5.7528e-06,1.83543e-09,-2.22574e-13,37046.2,3.95289], Tmin=(392.427,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (309.103,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 474,
    label = "CDNCDN",
    molecule = 
"""
1 N u0 p1 c0 {3,S} {4,D}
2 N u0 p1 c0 {3,D} {8,S}
3 C u0 p0 c0 {1,S} {2,D} {5,S}
4 C u0 p0 c0 {1,D} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97137,0.00170328,6.84714e-05,-1.19022e-07,6.71411e-11,20350.7,8.29209], Tmin=(10,'K'), Tmax=(457.201,'K')),
            NASAPolynomial(coeffs=[1.01651,0.027559,-1.63699e-05,4.70847e-09,-5.25815e-13,20620.9,20.2345], Tmin=(457.201,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (169.193,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 475,
    label = "[O-][NH+]DCD[NH+][O-]",
    molecule = 
"""
1 O u0 p3 c-1 {3,S}
2 O u0 p3 c-1 {4,S}
3 N u0 p0 c+1 {1,S} {5,D} {6,S}
4 N u0 p0 c+1 {2,S} {5,D} {7,S}
5 C u0 p0 c0 {3,D} {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9044,0.00905222,3.59185e-05,-6.51398e-08,3.25767e-11,37078.6,8.598], Tmin=(10,'K'), Tmax=(676.8,'K')),
            NASAPolynomial(coeffs=[3.24598,0.0222116,-1.37878e-05,4.05557e-09,-4.56934e-13,36955.5,9.94932], Tmin=(676.8,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (308.278,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 476,
    label = "N[N]CN",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {4,S} {7,S} {8,S}
2  N u0 p1 c0 {3,S} {9,S} {10,S}
3  N u1 p1 c0 {2,S} {4,S}
4  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95562,0.00281746,0.000103381,-2.01799e-07,1.26407e-10,24568.5,9.14426], Tmin=(10,'K'), Tmax=(475.854,'K')),
            NASAPolynomial(coeffs=[1.09754,0.0345343,-2.08442e-05,6.20981e-09,-7.21747e-13,24753.5,19.8952], Tmin=(475.854,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (204.264,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 477,
    label = "NCDCO",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {9,S}
2 N u0 p1 c0 {3,S} {7,S} {8,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 C u0 p0 c0 {1,S} {3,D} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95943,0.00242729,8.61663e-05,-1.56456e-07,8.98393e-11,-15194.1,8.25439], Tmin=(10,'K'), Tmax=(526.372,'K')),
            NASAPolynomial(coeffs=[1.09735,0.0319496,-2.01133e-05,6.20387e-09,-7.40047e-13,-15000.5,19.2027], Tmin=(526.372,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-126.346,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 478,
    label = "CCCN",
    molecule = 
"""
1  N u0 p1 c0 {3,S} {12,S} {13,S}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86032,0.012956,5.57892e-05,-7.78356e-08,3.1305e-11,-10564.7,7.62774], Tmin=(10,'K'), Tmax=(787.199,'K')),
            NASAPolynomial(coeffs=[-0.450762,0.0449904,-2.45518e-05,6.54862e-09,-6.84684e-13,-10199.8,25.4014], Tmin=(787.199,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-87.8432,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 479,
    label = "[O-][NH+]OC",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p3 c-1 {3,S}
3 N u1 p0 c+1 {1,S} {2,S} {8,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92322,0.0144031,8.44817e-06,-1.55631e-08,5.41455e-12,-9.64018,7.84996], Tmin=(10,'K'), Tmax=(1106.88,'K')),
            NASAPolynomial(coeffs=[5.13958,0.0187301,-9.23621e-06,2.20751e-09,-2.07114e-13,-813.259,-0.55554], Tmin=(1106.88,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-0.0558255,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 480,
    label = "NDCC#[C]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {5,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u1 p0 c0 {3,T}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8865,0.0110577,9.54905e-06,-2.15207e-08,9.94544e-12,79343.9,8.41292], Tmin=(10,'K'), Tmax=(794.264,'K')),
            NASAPolynomial(coeffs=[4.02775,0.0156462,-9.12531e-06,2.55458e-09,-2.76687e-13,79154.2,6.71164], Tmin=(794.264,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (659.697,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 481,
    label = "NCCDC",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {4,D} {7,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9616,0.00236326,0.00010487,-1.89437e-07,1.11793e-10,4719.13,8.46441], Tmin=(10,'K'), Tmax=(435.833,'K')),
            NASAPolynomial(coeffs=[-0.100732,0.039645,-2.34363e-05,6.81572e-09,-7.75009e-13,5073.24,24.6893], Tmin=(435.833,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (39.223,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 482,
    label = "OND[CH]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 N u0 p1 c0 {1,S} {3,D}
3 C u1 p0 c0 {2,D} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9716,0.00162685,3.87284e-05,-7.11386e-08,3.97774e-11,27604.7,6.72133], Tmin=(10,'K'), Tmax=(582.714,'K')),
            NASAPolynomial(coeffs=[3.21437,0.0134649,-8.83763e-06,2.83578e-09,-3.49388e-13,27580.2,8.99823], Tmin=(582.714,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (229.506,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 483,
    label = "[C]#N",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,T}
2 C u1 p0 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50493,-0.000255314,4.44985e-07,1.48762e-09,-1.24379e-12,52661.4,4.42401], Tmin=(10,'K'), Tmax=(746.463,'K')),
            NASAPolynomial(coeffs=[2.95266,0.00144238,-4.31119e-07,5.70997e-12,1.08856e-14,52779,7.16237], Tmin=(746.463,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (437.853,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (37.4151,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 484,
    label = "NNCD[CH]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {5,S}
2 N u0 p1 c0 {1,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {4,D} {6,S}
4 C u1 p0 c0 {3,D} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93171,0.00423,9.62092e-05,-1.96384e-07,1.23615e-10,48498.5,8.73721], Tmin=(10,'K'), Tmax=(515.4,'K')),
            NASAPolynomial(coeffs=[2.61158,0.0289252,-1.77167e-05,5.3744e-09,-6.3584e-13,48442.6,12.3692], Tmin=(515.4,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (403.217,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 485,
    label = "ONDO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05999,-0.00511908,5.09696e-05,-8.37805e-08,4.4721e-11,-10632.6,6.49021], Tmin=(10,'K'), Tmax=(598.055,'K')),
            NASAPolynomial(coeffs=[2.9705,0.00996114,-6.40023e-06,1.96021e-09,-2.28853e-13,-10641.7,10.0211], Tmin=(598.055,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-88.4054,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 486,
    label = "NCND[N]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {4,S} {7,S} {8,S}
2 N u0 p1 c0 {3,D} {4,S}
3 N u1 p1 c0 {2,D}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.39492,0.0607536,-0.000240652,4.72575e-07,-3.3077e-10,15727.1,11.1721], Tmin=(10,'K'), Tmax=(453.917,'K')),
            NASAPolynomial(coeffs=[5.29428,0.0172839,-8.66555e-06,2.11568e-09,-2.02319e-13,15830,6.54247], Tmin=(453.917,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (130.751,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (174.604,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 487,
    label = "[O]ONDC",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 N u0 p1 c0 {1,S} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94532,0.00366503,6.76737e-05,-1.57013e-07,1.11213e-10,25847,8.91934], Tmin=(10,'K'), Tmax=(462.604,'K')),
            NASAPolynomial(coeffs=[3.3706,0.0184462,-1.20687e-05,3.75319e-09,-4.45105e-13,25795.2,10.1143], Tmin=(462.604,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (214.896,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 488,
    label = "[O-][NH+]DCON",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {2,S} {5,D} {7,S}
4 N u0 p1 c0 {1,S} {8,S} {9,S}
5 C u0 p0 c0 {1,S} {3,D} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92538,0.00550945,0.000108846,-2.57597e-07,1.92809e-10,7602.53,9.4742], Tmin=(10,'K'), Tmax=(412.498,'K')),
            NASAPolynomial(coeffs=[2.2299,0.0314228,-1.98294e-05,6.03121e-09,-7.05136e-13,7661.82,15.1757], Tmin=(412.498,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (63.2104,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 489,
    label = "[N-]([NH+]DO)[CH]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {5,S} {8,S}
2 O u0 p2 c0 {3,D}
3 N u0 p0 c+1 {2,D} {4,S} {7,S}
4 N u0 p2 c-1 {3,S} {5,S}
5 C u1 p0 c0 {1,S} {4,S} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93803,0.00379597,8.89552e-05,-1.78563e-07,1.10044e-10,-2743.87,9.91266], Tmin=(10,'K'), Tmax=(523.515,'K')),
            NASAPolynomial(coeffs=[2.44687,0.0282278,-1.84061e-05,5.72939e-09,-6.81456e-13,-2766.41,14.4351], Tmin=(523.515,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-22.8348,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 490,
    label = "NCDN",
    molecule = 
"""
1 N u0 p1 c0 {3,S} {5,S} {6,S}
2 N u0 p1 c0 {3,D} {7,S}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07939,-0.00755041,0.000101662,-1.83655e-07,1.10141e-10,3869.77,6.69239], Tmin=(10,'K'), Tmax=(508.551,'K')),
            NASAPolynomial(coeffs=[1.63234,0.0214247,-1.2494e-05,3.60815e-09,-4.07097e-13,3992.86,15.6066], Tmin=(508.551,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (32.1704,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 491,
    label = "[NH]CC#N",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {3,S} {7,S}
2 N u0 p1 c0 {4,T}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {2,T} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82878,0.0160248,-1.23342e-06,-7.08688e-09,3.16959e-12,37989.9,9.03485], Tmin=(10,'K'), Tmax=(1003.54,'K')),
            NASAPolynomial(coeffs=[4.68402,0.0169077,-8.96814e-06,2.31304e-09,-2.33759e-13,37602.1,3.82902], Tmin=(1003.54,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (315.857,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 492,
    label = "N[C]DN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {4,S} {5,S}
2 N u0 p1 c0 {3,D} {6,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95038,0.00323609,5.80026e-05,-1.32869e-07,9.24818e-11,27039.8,6.93553], Tmin=(10,'K'), Tmax=(481.89,'K')),
            NASAPolynomial(coeffs=[3.81092,0.0144862,-8.43175e-06,2.50035e-09,-2.93967e-13,26936.1,6.29065], Tmin=(481.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (224.811,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 493,
    label = "[O-][NH+]DCNN",
    molecule = 
"""
1  O u0 p3 c-1 {4,S}
2  N u0 p1 c0 {3,S} {5,S} {7,S}
3  N u0 p1 c0 {2,S} {9,S} {10,S}
4  N u0 p0 c+1 {1,S} {5,D} {8,S}
5  C u0 p0 c0 {2,S} {4,D} {6,S}
6  H u0 p0 c0 {5,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92264,0.00512804,0.000120384,-2.65905e-07,1.83554e-10,18080,9.65341], Tmin=(10,'K'), Tmax=(461.023,'K')),
            NASAPolynomial(coeffs=[2.21865,0.0342751,-2.11808e-05,6.38217e-09,-7.44062e-13,18084.5,14.8994], Tmin=(461.023,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (150.313,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 494,
    label = "[N-]([NH+]DO)CD[N]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 N u0 p0 c+1 {1,D} {3,S} {6,S}
3 N u0 p2 c-1 {2,S} {5,S}
4 N u1 p1 c0 {5,D}
5 C u0 p0 c0 {3,S} {4,D} {7,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95083,0.00322161,8.06689e-05,-1.73001e-07,1.15884e-10,46137.2,9.87919], Tmin=(10,'K'), Tmax=(468.12,'K')),
            NASAPolynomial(coeffs=[2.4714,0.0246504,-1.6153e-05,4.98692e-09,-5.85654e-13,46179.5,14.8652], Tmin=(468.12,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (383.597,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 495,
    label = "CDCDN",
    molecule = 
"""
1 N u0 p1 c0 {3,D} {6,S}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98464,0.00092307,4.64012e-05,-8.05272e-08,4.51304e-11,20928.2,5.63995], Tmin=(10,'K'), Tmax=(463.569,'K')),
            NASAPolynomial(coeffs=[1.90284,0.0189367,-1.20497e-05,3.7664e-09,-4.55086e-13,21120.7,14.0771], Tmin=(463.569,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (174.001,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 496,
    label = "[NH-][NH+]DCD[CH]",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {2,S} {3,D} {5,S}
2 N u0 p2 c-1 {1,S} {6,S}
3 C u0 p0 c0 {1,D} {4,D}
4 C u1 p0 c0 {3,D} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90901,0.00588628,8.28379e-05,-1.99281e-07,1.40297e-10,58854.4,8.34917], Tmin=(10,'K'), Tmax=(495.285,'K')),
            NASAPolynomial(coeffs=[4.6716,0.0183651,-1.14002e-05,3.543e-09,-4.30232e-13,58550.3,2.89822], Tmin=(495.285,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (489.322,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 497,
    label = "[O-][NH+]NC",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {3,S} {4,S} {8,S}
3 N u1 p0 c+1 {1,S} {2,S} {9,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8887,0.0155315,1.25418e-05,-2.09135e-08,7.38437e-12,15343.5,8.34607], Tmin=(10,'K'), Tmax=(1047.99,'K')),
            NASAPolynomial(coeffs=[4.18792,0.0235025,-1.19108e-05,2.93921e-09,-2.85093e-13,14780.4,4.50083], Tmin=(1047.99,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (127.592,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 498,
    label = "C[N]C",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,S} {3,S}
2 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75957,0.0284457,-0.000131053,3.85178e-07,-3.49682e-10,17204.7,5.73102], Tmin=(10,'K'), Tmax=(412.772,'K')),
            NASAPolynomial(coeffs=[0.12949,0.0302675,-1.64592e-05,4.32472e-09,-4.42571e-13,17788.6,23.474], Tmin=(412.772,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (143.037,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 499,
    label = "N[CH]CDC",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {3,S} {5,S}
3  C u0 p0 c0 {2,S} {4,D} {6,S}
4  C u0 p0 c0 {3,D} {9,S} {10,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93163,0.00412187,0.000104291,-2.01674e-07,1.20819e-10,17389.2,8.72909], Tmin=(10,'K'), Tmax=(534.361,'K')),
            NASAPolynomial(coeffs=[1.91916,0.0339719,-2.10049e-05,6.42579e-09,-7.65286e-13,17393.2,15.2017], Tmin=(534.361,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (144.557,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 500,
    label = "[O-][N+]DC",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u1 p0 c+1 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05263,-0.00477436,5.98647e-05,-1.00718e-07,5.59325e-11,17284.4,6.9483], Tmin=(10,'K'), Tmax=(546.697,'K')),
            NASAPolynomial(coeffs=[2.24732,0.0143182,-8.66402e-06,2.53473e-09,-2.86601e-13,17393.9,13.7635], Tmin=(546.697,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (143.709,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 501,
    label = "[NH]COO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {8,S}
3 N u1 p1 c0 {4,S} {7,S}
4 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93368,0.0041363,8.86213e-05,-1.84768e-07,1.17917e-10,7453.82,9.15423], Tmin=(10,'K'), Tmax=(511.837,'K')),
            NASAPolynomial(coeffs=[2.87327,0.026245,-1.66766e-05,5.14122e-09,-6.10598e-13,7381.33,11.7913], Tmin=(511.837,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (61.9544,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 502,
    label = "NNCO",
    molecule = 
"""
1  O u0 p2 c0 {4,S} {10,S}
2  N u0 p1 c0 {3,S} {4,S} {7,S}
3  N u0 p1 c0 {2,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96967,0.00213669,0.000113832,-2.44234e-07,1.74287e-10,-12646.4,8.68996], Tmin=(10,'K'), Tmax=(357.889,'K')),
            NASAPolynomial(coeffs=[1.11051,0.0341246,-2.03714e-05,6.00737e-09,-6.91896e-13,-12441.9,19.543], Tmin=(357.889,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-105.145,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 503,
    label = "CC[C]DN",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {4,D} {10,S}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u1 p0 c0 {1,D} {2,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87813,0.0142991,2.64566e-05,-3.89607e-08,1.47059e-11,22237.2,8.1762], Tmin=(10,'K'), Tmax=(910.354,'K')),
            NASAPolynomial(coeffs=[2.48669,0.0303046,-1.62146e-05,4.22385e-09,-4.31138e-13,22080.7,12.5071], Tmin=(910.354,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (184.903,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 504,
    label = "[NH]OC#N",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 N u1 p1 c0 {1,S} {5,S}
3 N u0 p1 c0 {4,T}
4 C u0 p0 c0 {1,S} {3,T}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94542,0.00343328,5.18581e-05,-1.18161e-07,7.90105e-11,39821.9,8.33233], Tmin=(10,'K'), Tmax=(516.22,'K')),
            NASAPolynomial(coeffs=[4.22217,0.0127393,-8.45474e-06,2.69816e-09,-3.29597e-13,39640.8,5.7024], Tmin=(516.22,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (331.082,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 505,
    label = "[O-][NH+]DCD[CH]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {2,D} {4,D}
4 C u1 p0 c0 {3,D} {6,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92305,0.0048913,6.83406e-05,-1.61072e-07,1.1049e-10,40935.4,8.27986], Tmin=(10,'K'), Tmax=(509.697,'K')),
            NASAPolynomial(coeffs=[4.62613,0.0154349,-9.95554e-06,3.16054e-09,-3.87977e-13,40655.1,3.31512], Tmin=(509.697,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (340.335,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 506,
    label = "[N-]([NH+]DO)[C]DC",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 N u0 p0 c+1 {1,D} {3,S} {6,S}
3 N u0 p2 c-1 {2,S} {5,S}
4 C u0 p0 c0 {5,D} {7,S} {8,S}
5 C u1 p0 c0 {3,S} {4,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87974,0.00882825,0.000111974,-3.1412e-07,2.61178e-10,41170.4,9.96433], Tmin=(10,'K'), Tmax=(410.946,'K')),
            NASAPolynomial(coeffs=[4.12642,0.0251948,-1.62698e-05,5.05973e-09,-6.03562e-13,40991.6,7.06545], Tmin=(410.946,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (342.311,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 507,
    label = "[N-]([NH+]DO)O",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {6,S}
2 O u0 p2 c0 {3,D}
3 N u0 p0 c+1 {2,D} {4,S} {5,S}
4 N u0 p2 c-1 {1,S} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07721,-0.00692791,9.09956e-05,-1.54618e-07,8.46394e-11,2760.09,8.13411], Tmin=(10,'K'), Tmax=(582.408,'K')),
            NASAPolynomial(coeffs=[2.13035,0.0199113,-1.28166e-05,3.91823e-09,-4.56582e-13,2758.44,14.5132], Tmin=(582.408,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (22.9427,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 508,
    label = "[CH2]NNDC",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {5,S}
2 N u0 p1 c0 {1,S} {4,D}
3 C u1 p0 c0 {1,S} {6,S} {7,S}
4 C u0 p0 c0 {2,D} {8,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92905,0.00445435,9.88817e-05,-2.06372e-07,1.32791e-10,37836.3,7.98293], Tmin=(10,'K'), Tmax=(505.065,'K')),
            NASAPolynomial(coeffs=[2.69672,0.0289639,-1.77152e-05,5.3529e-09,-6.30749e-13,37772.7,11.2241], Tmin=(505.065,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (314.568,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 509,
    label = "ONC[O]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {8,S}
2 O u1 p2 c0 {4,S}
3 N u0 p1 c0 {1,S} {4,S} {7,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94542,0.00348416,8.75666e-05,-1.82571e-07,1.18726e-10,-1613.31,9.50906], Tmin=(10,'K'), Tmax=(487.234,'K')),
            NASAPolynomial(coeffs=[2.41093,0.0267345,-1.68074e-05,5.11365e-09,-5.99227e-13,-1590.22,14.5112], Tmin=(487.234,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-13.4275,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 510,
    label = "NNC[O]",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {4,S}
2 N u0 p1 c0 {3,S} {4,S} {7,S}
3 N u0 p1 c0 {2,S} {8,S} {9,S}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89636,0.0089268,5.33816e-05,-1.00972e-07,5.87437e-11,16679.8,9.18272], Tmin=(10,'K'), Tmax=(447.029,'K')),
            NASAPolynomial(coeffs=[1.52784,0.0301202,-1.7732e-05,5.08129e-09,-5.65927e-13,16891.6,18.7025], Tmin=(447.029,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (138.673,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 511,
    label = "NNNDC",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {5,S}
2 N u0 p1 c0 {1,S} {6,S} {7,S}
3 N u0 p1 c0 {1,S} {4,D}
4 C u0 p0 c0 {3,D} {8,S} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97427,0.001625,8.82768e-05,-1.62436e-07,9.71757e-11,30296.9,7.77621], Tmin=(10,'K'), Tmax=(431.16,'K')),
            NASAPolynomial(coeffs=[0.586714,0.0330473,-2.10232e-05,6.53845e-09,-7.85001e-13,30589,21.2699], Tmin=(431.16,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (251.896,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 512,
    label = "[O-][NH+]DN[N]N",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {4,S} {7,S} {8,S}
3 N u0 p0 c+1 {1,S} {5,D} {6,S}
4 N u1 p1 c0 {2,S} {5,S}
5 N u0 p1 c0 {3,D} {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90014,0.00660418,0.000102941,-2.46119e-07,1.75371e-10,42100.3,9.65576], Tmin=(10,'K'), Tmax=(476.511,'K')),
            NASAPolynomial(coeffs=[3.93277,0.0254406,-1.65104e-05,5.16425e-09,-6.19147e-13,41880.2,7.24598], Tmin=(476.511,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (350.023,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 513,
    label = "[C]#CC#N",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,T}
2 C u0 p0 c0 {3,S} {4,T}
3 C u0 p0 c0 {1,T} {2,S}
4 C u1 p0 c0 {2,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94367,0.00401897,4.34827e-05,-1.25149e-07,1.02629e-10,87499.9,6.80644], Tmin=(10,'K'), Tmax=(431.978,'K')),
            NASAPolynomial(coeffs=[4.44536,0.00882659,-6.03634e-06,1.93177e-09,-2.34514e-13,87368.4,3.78631], Tmin=(431.978,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (727.513,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 514,
    label = "CDCNDN",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {8,S}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {3,D} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97378,0.00157059,7.0975e-05,-1.23876e-07,6.99296e-11,30565.4,7.90547], Tmin=(10,'K'), Tmax=(458.16,'K')),
            NASAPolynomial(coeffs=[0.872475,0.0286626,-1.77755e-05,5.3401e-09,-6.19997e-13,30849.4,20.4449], Tmin=(458.16,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (254.124,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 515,
    label = "NNCN",
    molecule = 
"""
1  N u0 p1 c0 {3,S} {4,S} {7,S}
2  N u0 p1 c0 {4,S} {8,S} {9,S}
3  N u0 p1 c0 {1,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96484,0.00234172,0.000115922,-2.31393e-07,1.52752e-10,10517.2,8.56223], Tmin=(10,'K'), Tmax=(387.413,'K')),
            NASAPolynomial(coeffs=[0.504704,0.0380612,-2.23543e-05,6.51408e-09,-7.4473e-13,10785.3,21.9749], Tmin=(387.413,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (87.4402,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 516,
    label = "NNO[O]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 N u0 p1 c0 {3,S} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89321,0.00931923,9.05919e-05,-3.20385e-07,3.37681e-10,25803.2,9.15807], Tmin=(10,'K'), Tmax=(321.078,'K')),
            NASAPolynomial(coeffs=[3.94168,0.0200588,-1.25746e-05,3.85657e-09,-4.57003e-13,25741.6,8.06878], Tmin=(321.078,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (214.557,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 517,
    label = "[NH-]CDCD[NH+]",
    molecule = 
"""
multiplicity 2
1 N u0 p2 c-1 {3,S} {6,S}
2 N u1 p0 c+1 {4,D} {7,S}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94612,0.00324799,7.10403e-05,-1.41421e-07,8.58247e-11,41441.4,8.48555], Tmin=(10,'K'), Tmax=(539.706,'K')),
            NASAPolynomial(coeffs=[2.99984,0.0220836,-1.4167e-05,4.41774e-09,-5.30672e-13,41371.4,10.8721], Tmin=(539.706,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (344.543,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 518,
    label = "NCD[CH]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u1 p0 c0 {2,D} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96562,0.00200418,5.95456e-05,-1.07211e-07,6.02e-11,35298.7,6.85428], Tmin=(10,'K'), Tmax=(557.921,'K')),
            NASAPolynomial(coeffs=[2.25957,0.0217215,-1.35916e-05,4.23059e-09,-5.12168e-13,35372.5,13.0453], Tmin=(557.921,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (293.475,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 519,
    label = "NNDC[NH]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {6,S} {7,S}
2 N u0 p1 c0 {1,S} {4,D}
3 N u1 p1 c0 {4,S} {8,S}
4 C u0 p0 c0 {2,D} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9521,0.00293916,8.02762e-05,-1.569e-07,9.57726e-11,32987.1,8.59803], Tmin=(10,'K'), Tmax=(516.105,'K')),
            NASAPolynomial(coeffs=[2.20869,0.0263199,-1.63594e-05,4.97644e-09,-5.86564e-13,33035.7,14.5825], Tmin=(516.105,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (274.255,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 520,
    label = "CNC#C",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {8,S}
2 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {3,T} {9,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93353,0.00522124,0.000123645,-3.49339e-07,3.16756e-10,28807,6.97728], Tmin=(10,'K'), Tmax=(346.79,'K')),
            NASAPolynomial(coeffs=[2.94579,0.0269973,-1.54559e-05,4.40307e-09,-4.94958e-13,28813.1,9.7963], Tmin=(346.79,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (239.527,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 521,
    label = "[O-][NH+]DCNO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {9,S}
2 O u0 p3 c-1 {4,S}
3 N u0 p1 c0 {1,S} {5,S} {7,S}
4 N u0 p0 c+1 {2,S} {5,D} {8,S}
5 C u0 p0 c0 {3,S} {4,D} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92761,0.00445193,0.000101589,-2.05734e-07,1.27914e-10,3885.42,9.66657], Tmin=(10,'K'), Tmax=(521.178,'K')),
            NASAPolynomial(coeffs=[2.3973,0.0314737,-2.01497e-05,6.23081e-09,-7.40638e-13,3837.46,14.0617], Tmin=(521.178,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (32.2812,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 522,
    label = "NOND[CH]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 N u0 p1 c0 {1,S} {4,D}
4 C u1 p0 c0 {3,D} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90452,0.00688595,9.09488e-05,-2.51932e-07,2.0659e-10,47677.5,8.78726], Tmin=(10,'K'), Tmax=(419.37,'K')),
            NASAPolynomial(coeffs=[4.25751,0.0196306,-1.22643e-05,3.75479e-09,-4.45195e-13,47506.2,5.70184], Tmin=(419.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (396.412,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 523,
    label = "CN[CH2]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {7,S}
2 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
3 C u1 p0 c0 {1,S} {8,S} {9,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96027,0.00249952,7.66396e-05,-1.43748e-07,8.90182e-11,16375.1,5.93792], Tmin=(10,'K'), Tmax=(412.722,'K')),
            NASAPolynomial(coeffs=[1.36556,0.0276466,-1.47539e-05,3.87698e-09,-4.02499e-13,16589.3,16.1597], Tmin=(412.722,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (136.135,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 524,
    label = "[O-][NH+]DCDCD[CH]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {2,D} {4,D}
4 C u0 p0 c0 {3,D} {5,D}
5 C u1 p0 c0 {4,D} {7,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87105,0.00945715,9.98108e-05,-2.95268e-07,2.50454e-10,66647.7,9.92422], Tmin=(10,'K'), Tmax=(415.577,'K')),
            NASAPolynomial(coeffs=[4.8264,0.0205738,-1.36287e-05,4.3223e-09,-5.2322e-13,66392.9,4.04382], Tmin=(415.577,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (554.139,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 525,
    label = "NCDO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 N u0 p1 c0 {3,S} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93963,0.00526703,1.97725e-05,-3.01392e-08,1.33141e-11,-24328.9,6.73829], Tmin=(10,'K'), Tmax=(684.515,'K')),
            NASAPolynomial(coeffs=[2.43592,0.01621,-8.9314e-06,2.41744e-09,-2.56751e-13,-24173.5,13.0539], Tmin=(684.515,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-202.288,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 526,
    label = "[O-][N+]DCCDN",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u1 p0 c+1 {1,S} {4,D}
3 N u0 p1 c0 {5,D} {8,S}
4 C u0 p0 c0 {2,D} {5,S} {6,S}
5 C u0 p0 c0 {3,D} {4,S} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92533,0.00652622,9.09845e-05,-2.38038e-07,2.03131e-10,26529.5,9.63647], Tmin=(10,'K'), Tmax=(298.913,'K')),
            NASAPolynomial(coeffs=[2.29846,0.0282969,-1.82656e-05,5.62495e-09,-6.62522e-13,26626.8,15.5205], Tmin=(298.913,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (220.588,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 527,
    label = "CONC",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {4,S}
2  N u0 p1 c0 {1,S} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90111,0.0163502,2.22588e-05,-3.03791e-08,1.00741e-11,-4216.65,6.25375], Tmin=(10,'K'), Tmax=(1078.36,'K')),
            NASAPolynomial(coeffs=[3.52428,0.030461,-1.50531e-05,3.62041e-09,-3.42656e-13,-4874.55,4.67288], Tmin=(1078.36,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-35.0321,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 528,
    label = "[CH2]CDNO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {8,S}
2 N u0 p1 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 C u1 p0 c0 {3,S} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94572,0.003181,7.98007e-05,-1.49479e-07,8.59507e-11,13445.9,7.77613], Tmin=(10,'K'), Tmax=(559.454,'K')),
            NASAPolynomial(coeffs=[2.24943,0.0274459,-1.77987e-05,5.60125e-09,-6.77102e-13,13445.8,13.2771], Tmin=(559.454,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (111.773,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 529,
    label = "[CH]DCC#N",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {4,T}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u1 p0 c0 {2,D} {6,S}
4 C u0 p0 c0 {1,T} {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95001,0.00305596,6.00886e-05,-1.24401e-07,7.78272e-11,51984.3,8.29474], Tmin=(10,'K'), Tmax=(531.456,'K')),
            NASAPolynomial(coeffs=[3.47718,0.0174708,-1.12368e-05,3.50707e-09,-4.2184e-13,51881.3,8.8346], Tmin=(531.456,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (432.205,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 530,
    label = "CCNN",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {3,S} {10,S}
2  N u0 p1 c0 {1,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84257,0.0134936,4.66842e-05,-6.78716e-08,2.80428e-11,5604.04,7.50932], Tmin=(10,'K'), Tmax=(759.785,'K')),
            NASAPolynomial(coeffs=[0.104076,0.0408322,-2.2405e-05,6.01355e-09,-6.32615e-13,5951.13,23.064], Tmin=(759.785,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (46.583,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 531,
    label = "CND[C]C",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {4,D}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
4  C u1 p0 c0 {1,D} {3,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69949,0.0281802,-5.14688e-05,1.13083e-07,-8.6494e-11,24329.5,6.70773], Tmin=(10,'K'), Tmax=(501.238,'K')),
            NASAPolynomial(coeffs=[1.02939,0.0333358,-1.85601e-05,5.02267e-09,-5.31176e-13,24800.1,19.7693], Tmin=(501.238,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (202.28,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 532,
    label = "NCDNO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {8,S}
2 N u0 p1 c0 {4,S} {6,S} {7,S}
3 N u0 p1 c0 {1,S} {4,D}
4 C u0 p0 c0 {2,S} {3,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93475,0.00390827,8.19551e-05,-1.62934e-07,9.83912e-11,-2694.7,7.97837], Tmin=(10,'K'), Tmax=(547.057,'K')),
            NASAPolynomial(coeffs=[3.04725,0.0249817,-1.58162e-05,4.94615e-09,-5.98876e-13,-2815.83,9.73007], Tmin=(547.057,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-22.4297,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 533,
    label = "[NH-][NH+]DN[CH2]",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {2,D} {3,S} {5,S}
2 N u0 p1 c0 {1,D} {4,S}
3 N u0 p2 c-1 {1,S} {8,S}
4 C u1 p0 c0 {2,S} {6,S} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95443,0.00269332,7.72401e-05,-1.42833e-07,8.21357e-11,44986.4,7.80138], Tmin=(10,'K'), Tmax=(546.457,'K')),
            NASAPolynomial(coeffs=[1.90645,0.0274457,-1.74989e-05,5.4358e-09,-6.51173e-13,45064.5,15.1106], Tmin=(546.457,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (374.02,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 534,
    label = "[O-][NH+]DC[C]DO",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 O u0 p2 c0 {5,D}
3 N u0 p0 c+1 {1,S} {4,D} {7,S}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 C u1 p0 c0 {2,D} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82962,0.0159534,9.87568e-05,-4.58797e-07,5.76574e-10,8062.87,10.0598], Tmin=(10,'K'), Tmax=(289.03,'K')),
            NASAPolynomial(coeffs=[4.73093,0.0205321,-1.35032e-05,4.26218e-09,-5.14362e-13,7939.55,5.59808], Tmin=(289.03,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (67.0601,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 535,
    label = "[N]DCCDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 N u1 p1 c0 {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 C u0 p0 c0 {1,D} {3,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90007,0.00834656,2.13583e-05,-4.07413e-08,2.07843e-11,14832.7,8.66682], Tmin=(10,'K'), Tmax=(644.13,'K')),
            NASAPolynomial(coeffs=[3.08517,0.0177909,-1.08434e-05,3.15297e-09,-3.52785e-13,14846.8,11.5339], Tmin=(644.13,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (123.313,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 536,
    label = "[O-][NH+]DNC",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {8,S}
3 N u0 p1 c0 {2,D} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97202,0.00157874,6.42124e-05,-1.06071e-07,5.67288e-11,10052.4,7.32102], Tmin=(10,'K'), Tmax=(482.698,'K')),
            NASAPolynomial(coeffs=[0.867493,0.0273063,-1.574e-05,4.35794e-09,-4.66995e-13,10352.1,20.0372], Tmin=(482.698,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (83.5657,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 537,
    label = "[O-][N+]#CNN",
    molecule = 
"""
1 O u0 p3 c-1 {4,S}
2 N u0 p1 c0 {3,S} {5,S} {6,S}
3 N u0 p1 c0 {2,S} {7,S} {8,S}
4 N u0 p0 c+1 {1,S} {5,T}
5 C u0 p0 c0 {2,S} {4,T}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85635,0.011925,0.000111938,-3.86264e-07,3.87591e-10,38623,9.57673], Tmin=(10,'K'), Tmax=(346.173,'K')),
            NASAPolynomial(coeffs=[4.36373,0.0236295,-1.48987e-05,4.59482e-09,-5.47048e-13,38482.6,6.14684], Tmin=(346.173,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (321.149,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 538,
    label = "NNOO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {8,S}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 N u0 p1 c0 {3,S} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91649,0.00526586,9.10152e-05,-2.01138e-07,1.33301e-10,8602.91,8.43649], Tmin=(10,'K'), Tmax=(510,'K')),
            NASAPolynomial(coeffs=[3.78936,0.0237699,-1.48996e-05,4.6212e-09,-5.55972e-13,8388.2,6.7321], Tmin=(510,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (71.5047,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 539,
    label = "[NH]CCO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {4,S} {10,S}
2  N u1 p1 c0 {3,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96822,0.00218167,0.000113532,-2.35752e-07,1.61874e-10,-3230.91,9.28871], Tmin=(10,'K'), Tmax=(372.546,'K')),
            NASAPolynomial(coeffs=[0.841723,0.0357668,-2.1759e-05,6.46542e-09,-7.46265e-13,-2998.07,21.2836], Tmin=(372.546,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-26.8633,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 540,
    label = "CNC",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {3,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
4  H u0 p0 c0 {2,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96165,0.001963,6.45136e-05,-9.11249e-08,4.14718e-11,-3872.56,5.19204], Tmin=(10,'K'), Tmax=(568.633,'K')),
            NASAPolynomial(coeffs=[-0.416717,0.0327596,-1.67181e-05,4.10326e-09,-3.91764e-13,-3374.58,23.8438], Tmin=(568.633,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-32.2182,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 541,
    label = "[O-][NH+]DN[CH2]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {5,S}
3 N u0 p1 c0 {2,D} {4,S}
4 C u1 p0 c0 {3,S} {6,S} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96397,0.00211747,6.52868e-05,-1.18699e-07,6.72203e-11,23938.5,7.8211], Tmin=(10,'K'), Tmax=(548.387,'K')),
            NASAPolynomial(coeffs=[1.97349,0.0241899,-1.57491e-05,4.93336e-09,-5.9211e-13,24043.2,15.1926], Tmin=(548.387,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (199.021,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 542,
    label = "[O-][N+]DNNC",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {4,S}
2 N u0 p1 c0 {3,S} {5,S} {9,S}
3 N u0 p1 c0 {2,S} {4,D}
4 N u1 p0 c+1 {1,S} {3,D}
5 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85916,0.0229018,-3.34606e-06,-6.9795e-09,2.91567e-12,33177.5,8.83111], Tmin=(10,'K'), Tmax=(1209.54,'K')),
            NASAPolynomial(coeffs=[7.83054,0.0185285,-8.78646e-06,2.00705e-09,-1.79421e-13,31576,-13.733], Tmin=(1209.54,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (275.873,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 543,
    label = "[O-][NH+]D[C]NC",
    molecule = 
"""
multiplicity 2
1  O u0 p3 c-1 {3,S}
2  N u0 p1 c0 {4,S} {5,S} {9,S}
3  N u0 p0 c+1 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
5  C u1 p0 c0 {2,S} {3,D}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78792,0.019362,2.25787e-05,-4.50709e-08,2.06451e-11,28283.6,9.20086], Tmin=(10,'K'), Tmax=(761.967,'K')),
            NASAPolynomial(coeffs=[3.0463,0.0316558,-1.81602e-05,5.04172e-09,-5.43983e-13,28152.8,10.9769], Tmin=(761.967,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (235.147,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 544,
    label = "[O-][NH2+]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u1 p0 c+1 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99639,0.000123896,1.39348e-05,-1.8002e-08,7.58925e-12,6677.87,4.24636], Tmin=(10,'K'), Tmax=(611.876,'K')),
            NASAPolynomial(coeffs=[2.9235,0.00713767,-3.25919e-06,7.31558e-10,-6.48787e-14,6809.17,8.89543], Tmin=(611.876,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (55.5206,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 545,
    label = "[O-][N+]#CC#N",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {4,T}
3 N u0 p1 c0 {5,T}
4 C u0 p0 c0 {2,T} {5,S}
5 C u0 p0 c0 {3,T} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.33751,0.0131363,8.22267e-05,-3.35455e-07,3.50621e-10,39028.8,8.58418], Tmin=(10,'K'), Tmax=(363.031,'K')),
            NASAPolynomial(coeffs=[5.44067,0.0125482,-8.6628e-06,2.825e-09,-3.49308e-13,38727.3,-1.48107], Tmin=(363.031,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (324.522,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (112.245,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 546,
    label = "NC[C]DN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {7,S} {8,S}
2 N u0 p1 c0 {4,D} {9,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u1 p0 c0 {2,D} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90975,0.00725417,7.6626e-05,-1.73258e-07,1.26491e-10,28686.8,9.17251], Tmin=(10,'K'), Tmax=(350.549,'K')),
            NASAPolynomial(coeffs=[1.99145,0.0291432,-1.70369e-05,4.86799e-09,-5.41636e-13,28821.3,16.4163], Tmin=(350.549,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (238.507,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 547,
    label = "CN[N]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {9,S}
2 N u0 p1 c0 {3,S} {4,S} {8,S}
3 N u1 p1 c0 {1,S} {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77872,0.0185444,9.73307e-06,-2.49989e-08,1.16103e-11,13877,8.05877], Tmin=(10,'K'), Tmax=(752.079,'K')),
            NASAPolynomial(coeffs=[2.96157,0.0269293,-1.50457e-05,4.10629e-09,-4.38191e-13,13885.7,11.0088], Tmin=(752.079,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (115.356,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 548,
    label = "NC[C]DO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,S} {7,S} {8,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 C u1 p0 c0 {1,D} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85541,0.0122484,3.13471e-05,-7.11366e-08,4.60351e-11,650.03,9.22124], Tmin=(10,'K'), Tmax=(404.283,'K')),
            NASAPolynomial(coeffs=[2.61379,0.024533,-1.42325e-05,4.02481e-09,-4.43137e-13,750.423,14.0869], Tmin=(404.283,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (5.38851,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 549,
    label = "[O]OC#N",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u1 p2 c0 {1,S}
3 N u0 p1 c0 {4,T}
4 C u0 p0 c0 {1,S} {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95482,0.00280181,3.93108e-05,-8.97291e-08,5.90789e-11,32306.2,8.40896], Tmin=(10,'K'), Tmax=(530.414,'K')),
            NASAPolynomial(coeffs=[4.31927,0.00959901,-6.9064e-06,2.28978e-09,-2.84277e-13,32133.3,5.61601], Tmin=(530.414,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (268.594,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 550,
    label = "COND[CH]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {4,D}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 C u1 p0 c0 {2,D} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82529,0.0157003,9.54043e-06,-2.14681e-08,9.12851e-12,29099.7,7.68797], Tmin=(10,'K'), Tmax=(855.388,'K')),
            NASAPolynomial(coeffs=[3.49942,0.0227792,-1.26145e-05,3.39096e-09,-3.55851e-13,28952.2,8.02127], Tmin=(855.388,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (241.938,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 551,
    label = "ONO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {3,S} {6,S}
3 N u0 p1 c0 {1,S} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96661,0.00194543,4.89404e-05,-9.06278e-08,5.16666e-11,-13480.5,6.82209], Tmin=(10,'K'), Tmax=(564.886,'K')),
            NASAPolynomial(coeffs=[2.93885,0.0167894,-1.05681e-05,3.31468e-09,-4.03287e-13,-13485.1,10.1249], Tmin=(564.886,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-112.097,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 552,
    label = "[O-][NH+]DCDNC",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {5,D} {9,S}
3 N u0 p1 c0 {4,S} {5,D}
4 C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
5 C u0 p0 c0 {2,D} {3,D}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69465,0.0281261,-3.09921e-05,4.70384e-08,-3.42959e-11,32059.6,8.36139], Tmin=(10,'K'), Tmax=(484.936,'K')),
            NASAPolynomial(coeffs=[2.88579,0.0292835,-1.75151e-05,5.06136e-09,-5.66439e-13,32202.9,12.3468], Tmin=(484.936,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (266.545,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 553,
    label = "[N-]([N+]DN)C",
    molecule = 
"""
multiplicity 2
1 N u0 p2 c-1 {2,S} {4,S}
2 N u1 p0 c+1 {1,S} {3,D}
3 N u0 p1 c0 {2,D} {8,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90612,0.0132446,1.29958e-05,-2.14039e-08,7.8193e-12,45769.5,7.65049], Tmin=(10,'K'), Tmax=(1000.86,'K')),
            NASAPolynomial(coeffs=[4.03429,0.0209758,-1.09458e-05,2.77286e-09,-2.75315e-13,45331,4.96939], Tmin=(1000.86,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (380.567,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 554,
    label = "[N-]([N+]DO)CO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {5,S} {8,S}
2 O u0 p2 c0 {4,D}
3 N u0 p2 c-1 {4,S} {5,S}
4 N u1 p0 c+1 {2,D} {3,S}
5 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80875,0.0187488,6.38919e-06,-2.17214e-08,1.00829e-11,3109.87,10.4417], Tmin=(10,'K'), Tmax=(845.277,'K')),
            NASAPolynomial(coeffs=[4.58007,0.0223283,-1.27921e-05,3.52519e-09,-3.76694e-13,2721.2,5.32245], Tmin=(845.277,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (25.8497,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 555,
    label = "CNDCDC",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {4,D}
2 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3 C u0 p0 c0 {4,D} {8,S} {9,S}
4 C u0 p0 c0 {1,D} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87776,0.00959238,5.54251e-05,-1.14984e-07,7.41608e-11,20708,7.09376], Tmin=(10,'K'), Tmax=(400.209,'K')),
            NASAPolynomial(coeffs=[1.96268,0.028733,-1.63141e-05,4.51822e-09,-4.88351e-13,20861.3,14.5791], Tmin=(400.209,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (172.156,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 556,
    label = "[O-][N+]#CNO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {7,S}
2 O u0 p3 c-1 {4,S}
3 N u0 p1 c0 {1,S} {5,S} {6,S}
4 N u0 p0 c+1 {2,S} {5,T}
5 C u0 p0 c0 {3,S} {4,T}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83918,0.0128265,9.06984e-05,-3.0948e-07,2.91319e-10,23454.8,9.68011], Tmin=(10,'K'), Tmax=(382,'K')),
            NASAPolynomial(coeffs=[4.99276,0.0200351,-1.33456e-05,4.27497e-09,-5.21778e-13,23225.9,3.38288], Tmin=(382,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (195.025,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 557,
    label = "[NH]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 N u1 p1 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04762,-0.00345872,2.80933e-05,-3.69906e-08,1.61752e-11,10126.9,5.08551], Tmin=(10,'K'), Tmax=(686.86,'K')),
            NASAPolynomial(coeffs=[2.56087,0.00831714,-4.43195e-06,1.18679e-09,-1.2574e-13,10257.6,11.1644], Tmin=(686.86,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (84.2074,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 558,
    label = "COCDN",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 N u0 p1 c0 {4,D} {9,S}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {2,D} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96167,0.00231669,7.79291e-05,-1.38754e-07,8.06473e-11,-16483.5,7.43246], Tmin=(10,'K'), Tmax=(441.984,'K')),
            NASAPolynomial(coeffs=[0.86483,0.0303435,-1.7188e-05,4.7164e-09,-5.03962e-13,-16209.7,19.8444], Tmin=(441.984,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-137.068,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 559,
    label = "CNDC[NH]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {4,D}
2 N u1 p1 c0 {4,S} {9,S}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,D} {2,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94075,0.0111073,2.85545e-05,-3.99685e-08,1.48938e-11,26519.4,7.51792], Tmin=(10,'K'), Tmax=(925.141,'K')),
            NASAPolynomial(coeffs=[2.91752,0.0265173,-1.42431e-05,3.70763e-09,-3.773e-13,26238.6,9.83394], Tmin=(925.141,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (220.523,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 560,
    label = "[N-]([NH+]DO)[N]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {5,S} {7,S}
2 O u0 p2 c0 {3,D}
3 N u0 p0 c+1 {2,D} {4,S} {6,S}
4 N u0 p2 c-1 {3,S} {5,S}
5 N u1 p1 c0 {1,S} {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90604,0.00602052,8.9215e-05,-2.07962e-07,1.42329e-10,26086.3,9.8267], Tmin=(10,'K'), Tmax=(502.602,'K')),
            NASAPolynomial(coeffs=[4.24839,0.0221223,-1.5027e-05,4.83579e-09,-5.89698e-13,25814.1,6.04502], Tmin=(502.602,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (216.869,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 561,
    label = "[O-][NH+]DC[C]DN",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {4,D} {7,S}
3 N u0 p1 c0 {5,D} {8,S}
4 C u0 p0 c0 {2,D} {5,S} {6,S}
5 C u1 p0 c0 {3,D} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8867,0.0079626,0.000109236,-2.88728e-07,2.26252e-10,33771.8,10.0104], Tmin=(10,'K'), Tmax=(436.656,'K')),
            NASAPolynomial(coeffs=[4.17574,0.0248631,-1.59721e-05,4.95892e-09,-5.91701e-13,33560.2,6.72146], Tmin=(436.656,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (280.786,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 562,
    label = "N[N]NO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {8,S}
2 N u0 p1 c0 {1,S} {4,S} {5,S}
3 N u0 p1 c0 {4,S} {6,S} {7,S}
4 N u1 p1 c0 {2,S} {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92864,0.00425096,8.39133e-05,-1.6788e-07,1.01187e-10,27524.7,8.83569], Tmin=(10,'K'), Tmax=(553.878,'K')),
            NASAPolynomial(coeffs=[3.28039,0.0250617,-1.61266e-05,5.10665e-09,-6.23613e-13,27349.1,9.34671], Tmin=(553.878,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (228.826,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 563,
    label = "CCNO",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {11,S}
2  N u0 p1 c0 {1,S} {3,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87952,0.0101847,6.40302e-05,-1.11319e-07,5.95842e-11,-11666.4,7.5494], Tmin=(10,'K'), Tmax=(487.179,'K')),
            NASAPolynomial(coeffs=[0.485719,0.03805,-2.17664e-05,6.08828e-09,-6.64907e-13,-11335.7,21.4819], Tmin=(487.179,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-97.0163,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 564,
    label = "O[N]NO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {6,S}
2 O u0 p2 c0 {4,S} {7,S}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 N u1 p1 c0 {2,S} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91163,0.00563437,8.28888e-05,-1.92836e-07,1.31709e-10,11305.9,9.04446], Tmin=(10,'K'), Tmax=(506.222,'K')),
            NASAPolynomial(coeffs=[4.40839,0.0198418,-1.2939e-05,4.12247e-09,-5.03839e-13,11023.3,4.69126], Tmin=(506.222,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (93.9791,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 565,
    label = "[CH2]CDNN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {8,S} {9,S}
2 N u0 p1 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 C u1 p0 c0 {3,S} {6,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94518,0.00328811,9.08017e-05,-1.71984e-07,1.01408e-10,30233.3,7.78585], Tmin=(10,'K'), Tmax=(535.377,'K')),
            NASAPolynomial(coeffs=[1.80912,0.0309276,-1.93627e-05,5.94675e-09,-7.07816e-13,30294.6,15.1932], Tmin=(535.377,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (251.354,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 566,
    label = "CCCDN",
    molecule = 
"""
1  N u0 p1 c0 {4,D} {11,S}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {1,D} {2,S} {10,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96339,0.0112553,3.90823e-05,-4.96554e-08,1.74532e-11,589.555,7.21236], Tmin=(10,'K'), Tmax=(965.356,'K')),
            NASAPolynomial(coeffs=[1.93745,0.0336456,-1.74554e-05,4.40737e-09,-4.36844e-13,328.568,13.5372], Tmin=(965.356,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (4.94366,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 567,
    label = "[O]CC#N",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 N u0 p1 c0 {4,T}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {2,T} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9564,0.0028056,6.23678e-05,-1.34349e-07,8.93384e-11,20015.7,8.65053], Tmin=(10,'K'), Tmax=(485.412,'K')),
            NASAPolynomial(coeffs=[3.13796,0.018129,-1.14944e-05,3.50288e-09,-4.11109e-13,19994.1,10.9664], Tmin=(485.412,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (166.41,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 568,
    label = "[O-][N+]DCCDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {5,D}
2 O u0 p3 c-1 {3,S}
3 N u1 p0 c+1 {2,S} {4,D}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 C u0 p0 c0 {1,D} {4,S} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91475,0.0075835,7.3049e-05,-2.06169e-07,1.87235e-10,3149.18,9.8898], Tmin=(10,'K'), Tmax=(281.009,'K')),
            NASAPolynomial(coeffs=[2.74363,0.0242539,-1.59369e-05,4.9437e-09,-5.83862e-13,3215,14.0532], Tmin=(281.009,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (26.192,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 569,
    label = "O[N]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {3,S} {5,S}
3 N u1 p1 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9603,0.00236826,4.27705e-05,-8.73763e-08,5.32389e-11,-2429,7.30781], Tmin=(10,'K'), Tmax=(555.837,'K')),
            NASAPolynomial(coeffs=[3.85667,0.0121237,-7.86953e-06,2.52259e-09,-3.11175e-13,-2556.65,6.49493], Tmin=(555.837,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-20.2111,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 570,
    label = "ONC#N",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 N u0 p1 c0 {1,S} {4,S} {5,S}
3 N u0 p1 c0 {4,T}
4 C u0 p0 c0 {2,S} {3,T}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93865,0.00387944,6.33045e-05,-1.42335e-07,9.52265e-11,16092.6,7.93085], Tmin=(10,'K'), Tmax=(509.597,'K')),
            NASAPolynomial(coeffs=[4.02463,0.0160262,-1.01901e-05,3.18471e-09,-3.84909e-13,15917.4,5.94053], Tmin=(509.597,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (133.785,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 571,
    label = "[N-]([NH+]DO)C#N",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 N u0 p0 c+1 {1,D} {3,S} {6,S}
3 N u0 p2 c-1 {2,S} {5,S}
4 N u0 p1 c0 {5,T}
5 C u0 p0 c0 {3,S} {4,T}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94922,0.00339064,6.78453e-05,-1.5362e-07,1.06972e-10,35978.9,9.12817], Tmin=(10,'K'), Tmax=(463.515,'K')),
            NASAPolynomial(coeffs=[3.132,0.0193797,-1.2818e-05,3.99173e-09,-4.72399e-13,35958.6,11.4069], Tmin=(463.515,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (299.137,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 572,
    label = "[O-][N+]DCDCC",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u1 p0 c+1 {1,S} {5,D}
3 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
4 C u0 p0 c0 {3,S} {5,D} {9,S}
5 C u0 p0 c0 {2,D} {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66526,0.0285731,-1.79839e-05,5.7508e-09,-7.5021e-13,28557.9,9.23482], Tmin=(10,'K'), Tmax=(1595.71,'K')),
            NASAPolynomial(coeffs=[6.94592,0.0203494,-1.02534e-05,2.52107e-09,-2.44205e-13,27510.9,-8.12554], Tmin=(1595.71,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (237.392,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 573,
    label = "[CH]DCCDN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,D} {8,S}
2 C u0 p0 c0 {3,S} {4,D} {5,S}
3 C u0 p0 c0 {1,D} {2,S} {6,S}
4 C u1 p0 c0 {2,D} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96022,0.00240709,7.85148e-05,-1.46722e-07,8.634e-11,44615.4,8.51921], Tmin=(10,'K'), Tmax=(520.434,'K')),
            NASAPolynomial(coeffs=[1.65729,0.027943,-1.76696e-05,5.41835e-09,-6.40869e-13,44749,17.106], Tmin=(520.434,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (370.939,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 574,
    label = "[O-][NH+]DC[CH2]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 C u1 p0 c0 {3,S} {7,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96288,0.00220059,7.59347e-05,-1.37069e-07,7.78272e-11,13032.7,7.89309], Tmin=(10,'K'), Tmax=(535.704,'K')),
            NASAPolynomial(coeffs=[1.41081,0.0285623,-1.83365e-05,5.70608e-09,-6.8317e-13,13201.3,17.634], Tmin=(535.704,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (108.346,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 575,
    label = "NCO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {8,S}
2 N u0 p1 c0 {3,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97484,0.00144859,6.08617e-05,-1.004e-07,5.36441e-11,-25908.9,6.92156], Tmin=(10,'K'), Tmax=(484.024,'K')),
            NASAPolynomial(coeffs=[1.0002,0.0260268,-1.52934e-05,4.47368e-09,-5.13735e-13,-25620.9,19.1145], Tmin=(484.024,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-215.431,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 576,
    label = "NONDO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,S} {5,S} {6,S}
4 N u0 p1 c0 {1,S} {2,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92223,0.00646668,6.38609e-05,-1.88945e-07,1.69616e-10,8764.29,8.34359], Tmin=(10,'K'), Tmax=(363.023,'K')),
            NASAPolynomial(coeffs=[3.57437,0.0174759,-1.12816e-05,3.50351e-09,-4.16831e-13,8742.26,9.01803], Tmin=(363.023,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (72.8784,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 577,
    label = "NO[C]DN",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 N u0 p1 c0 {4,D} {7,S}
4 C u1 p0 c0 {1,S} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79545,0.0176038,-2.89843e-06,-8.3347e-09,4.64141e-12,28454.9,10.5466], Tmin=(10,'K'), Tmax=(831.388,'K')),
            NASAPolynomial(coeffs=[4.48545,0.0179519,-1.01442e-05,2.78192e-09,-2.97041e-13,28213.4,6.58289], Tmin=(831.388,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (236.568,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 578,
    label = "ONCDO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {7,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 C u0 p0 c0 {2,D} {3,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95536,0.00276323,6.96894e-05,-1.39688e-07,8.69534e-11,-24755.9,8.06047], Tmin=(10,'K'), Tmax=(511.905,'K')),
            NASAPolynomial(coeffs=[2.66791,0.022039,-1.37971e-05,4.20681e-09,-4.95886e-13,-24744.9,12.2302], Tmin=(511.905,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-205.847,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 579,
    label = "N[CH]NO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {9,S}
2 N u0 p1 c0 {1,S} {4,S} {6,S}
3 N u0 p1 c0 {4,S} {7,S} {8,S}
4 C u1 p0 c0 {2,S} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90942,0.00587166,0.000105813,-2.39659e-07,1.64541e-10,13754.9,9.36812], Tmin=(10,'K'), Tmax=(486.805,'K')),
            NASAPolynomial(coeffs=[3.49281,0.0274913,-1.68725e-05,5.14097e-09,-6.09866e-13,13579.9,8.86357], Tmin=(486.805,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (114.344,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 580,
    label = "NN[C]DN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {6,S} {7,S}
3 N u0 p1 c0 {4,D} {8,S}
4 C u1 p0 c0 {1,S} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91677,0.00722172,0.000111394,-3.65389e-07,3.77979e-10,40592.1,8.92554], Tmin=(10,'K'), Tmax=(309.434,'K')),
            NASAPolynomial(coeffs=[3.37332,0.0237043,-1.43509e-05,4.2973e-09,-5.0103e-13,40580.4,10.1783], Tmin=(309.434,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (337.518,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 581,
    label = "NN[N]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {8,S}
2 N u0 p1 c0 {3,S} {4,S} {5,S}
3 N u0 p1 c0 {2,S} {6,S} {7,S}
4 N u1 p1 c0 {1,S} {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91472,0.00653706,9.98638e-05,-2.7434e-07,2.33086e-10,26955.4,9.0746], Tmin=(10,'K'), Tmax=(382.886,'K')),
            NASAPolynomial(coeffs=[3.32331,0.0242843,-1.49854e-05,4.54515e-09,-5.33899e-13,26915.9,10.2526], Tmin=(382.886,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (224.127,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 582,
    label = "[N-]([NH+]DO)CO",
    molecule = 
"""
1 O u0 p2 c0 {5,S} {9,S}
2 O u0 p2 c0 {3,D}
3 N u0 p0 c+1 {2,D} {4,S} {8,S}
4 N u0 p2 c-1 {3,S} {5,S}
5 C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96015,0.00250036,9.61392e-05,-1.84376e-07,1.12907e-10,-9750.48,9.46723], Tmin=(10,'K'), Tmax=(482.394,'K')),
            NASAPolynomial(coeffs=[0.994678,0.0337031,-2.14487e-05,6.54888e-09,-7.67392e-13,-9541.32,20.8146], Tmin=(482.394,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-81.081,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 583,
    label = "[O-][N+]#CCDN",
    molecule = 
"""
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {4,D} {7,S}
3 N u0 p0 c+1 {1,S} {5,T}
4 C u0 p0 c0 {2,D} {5,S} {6,S}
5 C u0 p0 c0 {3,T} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83133,0.0192338,-7.71538e-06,-1.4332e-09,1.27919e-12,31218.6,9.33098], Tmin=(10,'K'), Tmax=(1156.09,'K')),
            NASAPolynomial(coeffs=[6.65304,0.0141507,-7.19213e-06,1.76652e-09,-1.69918e-13,30253.5,-6.04395], Tmin=(1156.09,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (259.568,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 584,
    label = "CDN",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08226,-0.00488781,3.12666e-05,-3.17497e-08,1.04971e-11,9150.13,4.37558], Tmin=(10,'K'), Tmax=(918.938,'K')),
            NASAPolynomial(coeffs=[0.895978,0.0137955,-7.08822e-06,1.77635e-09,-1.74659e-13,9532.48,18.3723], Tmin=(918.938,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (76.1006,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 585,
    label = "[O-][CH]CD[NH2+]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {4,S}
2 N u0 p0 c+1 {3,D} {7,S} {8,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 C u1 p0 c0 {1,S} {3,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94668,0.0033885,8.46299e-05,-1.75601e-07,1.13698e-10,-6190.7,8.87204], Tmin=(10,'K'), Tmax=(491.072,'K')),
            NASAPolynomial(coeffs=[2.52305,0.0256156,-1.57366e-05,4.73892e-09,-5.5412e-13,-6179.07,13.4226], Tmin=(491.072,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-51.4863,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 586,
    label = "CN",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0514,-0.00210967,3.97188e-05,-4.46122e-08,1.59404e-11,-4062.68,3.94946], Tmin=(10,'K'), Tmax=(851.973,'K')),
            NASAPolynomial(coeffs=[0.455679,0.0205687,-1.04148e-05,2.60294e-09,-2.57512e-13,-3660.36,19.4861], Tmin=(851.973,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-33.7579,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 587,
    label = "NND[C]NDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,S} {6,S} {7,S}
3 N u0 p1 c0 {2,S} {5,D}
4 N u0 p1 c0 {1,D} {5,S}
5 C u1 p0 c0 {3,D} {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84923,0.0116625,0.000105662,-3.57733e-07,3.37913e-10,48623.2,9.6081], Tmin=(10,'K'), Tmax=(382.642,'K')),
            NASAPolynomial(coeffs=[5.35743,0.0187947,-1.20612e-05,3.76612e-09,-4.53227e-13,48340.1,1.5903], Tmin=(382.642,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (404.288,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 588,
    label = "[NH-][NH+]DC[CH2]",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {2,S} {3,D} {6,S}
2 N u0 p2 c-1 {1,S} {9,S}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 C u1 p0 c0 {3,S} {7,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94783,0.00319477,9.14906e-05,-1.76876e-07,1.07226e-10,32841,8.24366], Tmin=(10,'K'), Tmax=(515.909,'K')),
            NASAPolynomial(coeffs=[1.81054,0.0304388,-1.87525e-05,5.68105e-09,-6.68955e-13,32919.5,15.7638], Tmin=(515.909,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (273.038,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 589,
    label = "NCNDO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 N u0 p1 c0 {4,S} {7,S} {8,S}
3 N u0 p1 c0 {1,D} {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86773,0.0114154,2.83306e-05,-5.23026e-08,2.6257e-11,8423.83,8.52165], Tmin=(10,'K'), Tmax=(634.152,'K')),
            NASAPolynomial(coeffs=[2.43749,0.0249932,-1.45632e-05,4.12066e-09,-4.5314e-13,8513.61,14.0479], Tmin=(634.152,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (70.0237,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 590,
    label = "[N-]DCD[NH2+]",
    molecule = 
"""
1 N u0 p0 c+1 {3,D} {4,S} {5,S}
2 N u0 p2 c-1 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97651,0.00141488,3.63302e-05,-6.97487e-08,4.1716e-11,14631.8,4.91699], Tmin=(10,'K'), Tmax=(534.62,'K')),
            NASAPolynomial(coeffs=[3.28602,0.0117017,-6.89846e-06,2.07225e-09,-2.46616e-13,14632.5,7.13147], Tmin=(534.62,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (121.647,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 591,
    label = "[CH2]CNDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 C u1 p0 c0 {3,S} {7,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.10349,0.0992957,-0.000552582,1.3184e-06,-1.08069e-09,15072.5,12.4672], Tmin=(10,'K'), Tmax=(399.823,'K')),
            NASAPolynomial(coeffs=[4.37648,0.0206858,-1.05263e-05,2.49072e-09,-2.21886e-13,15497.3,14.0772], Tmin=(399.823,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (125.284,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 592,
    label = "ND[N]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {3,S}
2 N u1 p1 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01467,-0.000882685,4.77731e-06,2.38859e-10,-2.96162e-12,29181.7,4.16001], Tmin=(10,'K'), Tmax=(610.931,'K')),
            NASAPolynomial(coeffs=[2.7401,0.00470919,-2.19236e-06,4.67787e-10,-3.67146e-14,29388.8,10.1015], Tmin=(610.931,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (242.636,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (58.2013,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 593,
    label = "C[N]NN",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {3,S} {8,S}
2  N u0 p1 c0 {1,S} {9,S} {10,S}
3  N u1 p1 c0 {1,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5  H u0 p0 c0 {4,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79974,0.0195062,8.66671e-06,-1.84446e-08,6.76732e-12,34532.1,7.91122], Tmin=(10,'K'), Tmax=(1022.58,'K')),
            NASAPolynomial(coeffs=[3.64234,0.0275764,-1.41062e-05,3.53113e-09,-3.48188e-13,34174.6,6.76839], Tmin=(1022.58,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (287.112,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 594,
    label = "[N-]([NH2+])NC",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {3,S} {4,S} {8,S}
2  N u1 p0 c+1 {3,S} {9,S} {10,S}
3  N u0 p2 c-1 {1,S} {2,S}
4  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  H u0 p0 c0 {4,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8406,0.0131512,4.55686e-05,-8.87491e-08,5.10347e-11,32607,7.52068], Tmin=(10,'K'), Tmax=(454.974,'K')),
            NASAPolynomial(coeffs=[1.62989,0.0325872,-1.85103e-05,5.14521e-09,-5.58775e-13,32808.2,16.4451], Tmin=(454.974,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (271.088,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 595,
    label = "C[N]NO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {9,S}
2 N u0 p1 c0 {1,S} {3,S} {8,S}
3 N u1 p1 c0 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88526,0.00970582,7.49135e-05,-1.90568e-07,1.55253e-10,18700.7,8.07939], Tmin=(10,'K'), Tmax=(313.652,'K')),
            NASAPolynomial(coeffs=[2.37741,0.0289355,-1.705e-05,4.90078e-09,-5.47691e-13,18795.3,13.6056], Tmin=(313.652,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (155.482,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 596,
    label = "[CH2]CNDN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {9,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u1 p0 c0 {3,S} {7,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81177,0.0180059,1.01967e-05,-2.23989e-08,9.09181e-12,40979.6,8.4166], Tmin=(10,'K'), Tmax=(909.83,'K')),
            NASAPolynomial(coeffs=[3.6468,0.0256823,-1.39193e-05,3.66903e-09,-3.78419e-13,40722,7.61577], Tmin=(909.83,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (340.718,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 597,
    label = "CND[CH]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,D}
2 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
3 C u1 p0 c0 {1,D} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92577,0.00647522,2.23014e-05,-3.04887e-08,1.18079e-11,32667.3,6.22406], Tmin=(10,'K'), Tmax=(813.53,'K')),
            NASAPolynomial(coeffs=[1.82552,0.0207446,-1.12785e-05,2.98658e-09,-3.09844e-13,32878.5,15.1212], Tmin=(813.53,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (271.607,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 598,
    label = "O[N]C#C",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 N u1 p1 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {6,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91578,0.00520935,6.9659e-05,-1.60676e-07,1.06485e-10,39728.7,8.24045], Tmin=(10,'K'), Tmax=(533.433,'K')),
            NASAPolynomial(coeffs=[4.9784,0.0154618,-1.04064e-05,3.41966e-09,-4.2993e-13,39356.1,1.35183], Tmin=(533.433,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (330.295,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 599,
    label = "NCNDN",
    molecule = 
"""
1 N u0 p1 c0 {4,S} {7,S} {8,S}
2 N u0 p1 c0 {3,D} {4,S}
3 N u0 p1 c0 {2,D} {9,S}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91617,0.00729897,5.16199e-05,-8.55994e-08,4.31098e-11,21375.5,8.3978], Tmin=(10,'K'), Tmax=(590.297,'K')),
            NASAPolynomial(coeffs=[1.20066,0.0300774,-1.73858e-05,4.89645e-09,-5.37126e-13,21619.8,19.4211], Tmin=(590.297,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (177.715,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 600,
    label = "[O-][NH+]DCDC[CH2]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {5,D} {9,S}
3 C u0 p0 c0 {4,S} {5,D} {6,S}
4 C u1 p0 c0 {3,S} {7,S} {8,S}
5 C u0 p0 c0 {2,D} {3,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82754,0.0179156,1.99024e-05,-4.02177e-08,1.80357e-11,42830.2,9.40033], Tmin=(10,'K'), Tmax=(806.684,'K')),
            NASAPolynomial(coeffs=[3.9234,0.0272752,-1.57892e-05,4.39234e-09,-4.73212e-13,42494.8,6.97506], Tmin=(806.684,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (356.108,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 601,
    label = "ONDCD[N]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 N u0 p1 c0 {1,S} {4,D}
3 N u1 p1 c0 {4,D}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95007,0.00305988,4.99341e-05,-1.08145e-07,6.90748e-11,30154.3,8.35975], Tmin=(10,'K'), Tmax=(535.653,'K')),
            NASAPolynomial(coeffs=[4.0316,0.0132741,-8.97688e-06,2.8956e-09,-3.55139e-13,29990.3,6.56796], Tmin=(535.653,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (250.7,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 602,
    label = "CDNNDC",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,D}
2 N u0 p1 c0 {1,S} {4,D}
3 C u0 p0 c0 {1,D} {5,S} {6,S}
4 C u0 p0 c0 {2,D} {7,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97313,0.00168336,7.53744e-05,-1.39952e-07,8.48232e-11,30205,7.61145], Tmin=(10,'K'), Tmax=(424.193,'K')),
            NASAPolynomial(coeffs=[1.20731,0.0277614,-1.68311e-05,4.94382e-09,-5.62901e-13,30439.7,18.5834], Tmin=(424.193,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (251.13,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 603,
    label = "CNCC",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {4,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8905,0.0159382,3.63614e-05,-4.5321e-08,1.49929e-11,-7748.77,6.18358], Tmin=(10,'K'), Tmax=(1037.93,'K')),
            NASAPolynomial(coeffs=[1.54385,0.0400198,-2.01736e-05,4.95056e-09,-4.7787e-13,-8071.66,13.6901], Tmin=(1037.93,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-64.4009,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 604,
    label = "COC#N",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 N u0 p1 c0 {4,T}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {2,T}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88052,0.011801,7.84816e-06,-1.44118e-08,5.27687e-12,-928.769,6.96952], Tmin=(10,'K'), Tmax=(1004.48,'K')),
            NASAPolynomial(coeffs=[3.69581,0.0179425,-9.39608e-06,2.39109e-09,-2.3865e-13,-1164.39,6.5039], Tmin=(1004.48,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-7.72306,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 605,
    label = "[O-][N+]#CCDO",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {2,S} {5,T}
4 C u0 p0 c0 {1,D} {5,S} {6,S}
5 C u0 p0 c0 {3,T} {4,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72963,0.0284346,-8.73385e-05,1.99532e-07,-1.72976e-10,7838.18,9.57485], Tmin=(10,'K'), Tmax=(371.108,'K')),
            NASAPolynomial(coeffs=[3.92197,0.0180612,-1.18599e-05,3.67105e-09,-4.32322e-13,7881.06,9.60769], Tmin=(371.108,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (65.1649,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 606,
    label = "[O]OCDN",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u1 p2 c0 {1,S}
3 N u0 p1 c0 {4,D} {6,S}
4 C u0 p0 c0 {1,S} {3,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96608,0.00196001,5.46048e-05,-9.90659e-08,5.52534e-11,12132.3,8.73569], Tmin=(10,'K'), Tmax=(567.858,'K')),
            NASAPolynomial(coeffs=[2.42793,0.0203005,-1.36683e-05,4.36327e-09,-5.28895e-13,12186,14.2204], Tmin=(567.858,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (100.859,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 607,
    label = "[O]CCDN",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 N u0 p1 c0 {4,D} {8,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {2,D} {3,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96878,0.0021249,8.60149e-05,-1.80137e-07,1.24488e-10,12724.7,9.69982], Tmin=(10,'K'), Tmax=(369.872,'K')),
            NASAPolynomial(coeffs=[1.62884,0.0274308,-1.66138e-05,4.84618e-09,-5.46615e-13,12897.8,18.6614], Tmin=(369.872,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (105.795,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 608,
    label = "[N-]([NH+]DO)CDN",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 N u0 p0 c+1 {1,D} {3,S} {7,S}
3 N u0 p2 c-1 {2,S} {5,S}
4 N u0 p1 c0 {5,D} {8,S}
5 C u0 p0 c0 {3,S} {4,D} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94645,0.0128465,1.94461e-05,-3.10332e-08,1.18688e-11,24542.7,9.19899], Tmin=(10,'K'), Tmax=(951.413,'K')),
            NASAPolynomial(coeffs=[4.50955,0.0215639,-1.17742e-05,3.08909e-09,-3.1526e-13,23933.9,3.87386], Tmin=(951.413,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (204.096,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 609,
    label = "ONCDN",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {7,S}
2 N u0 p1 c0 {1,S} {4,S} {5,S}
3 N u0 p1 c0 {4,D} {8,S}
4 C u0 p0 c0 {2,S} {3,D} {6,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96008,0.00233222,7.45635e-05,-1.33566e-07,7.47329e-11,2363.25,7.87203], Tmin=(10,'K'), Tmax=(552.435,'K')),
            NASAPolynomial(coeffs=[1.55596,0.0281031,-1.81197e-05,5.68613e-09,-6.86339e-13,2501.25,16.8888], Tmin=(552.435,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (19.6324,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 610,
    label = "NO[C]DO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,S} {5,S} {6,S}
4 C u1 p0 c0 {1,S} {2,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8323,0.015568,-7.20397e-06,-2.0933e-10,7.95185e-13,-707.444,9.22687], Tmin=(10,'K'), Tmax=(1086.91,'K')),
            NASAPolynomial(coeffs=[5.47274,0.0122713,-6.43631e-06,1.63948e-09,-1.63606e-13,-1225.92,0.431376], Tmin=(1086.91,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-5.89229,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 611,
    label = "[O-][N+]DCCN",
    molecule = 
"""
multiplicity 2
1  O u0 p3 c-1 {3,S}
2  N u0 p1 c0 {4,S} {9,S} {10,S}
3  N u1 p0 c+1 {1,S} {5,D}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {3,D} {4,S} {8,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81255,0.0189191,2.21062e-05,-4.1624e-08,1.79307e-11,16020.2,10.9133], Tmin=(10,'K'), Tmax=(824.486,'K')),
            NASAPolynomial(coeffs=[3.37266,0.0308532,-1.74347e-05,4.76461e-09,-5.06506e-13,15759.6,10.9306], Tmin=(824.486,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (133.196,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 612,
    label = "NONDN",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 N u0 p1 c0 {1,S} {4,D}
4 N u0 p1 c0 {3,D} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95489,0.00278413,6.97779e-05,-1.39489e-07,8.6475e-11,28149.3,8.18615], Tmin=(10,'K'), Tmax=(514.721,'K')),
            NASAPolynomial(coeffs=[2.66716,0.0221507,-1.39353e-05,4.26345e-09,-5.03505e-13,28157.9,12.3391], Tmin=(514.721,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (234.032,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 613,
    label = "NCN",
    molecule = 
"""
1 N u0 p1 c0 {3,S} {6,S} {7,S}
2 N u0 p1 c0 {3,S} {8,S} {9,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04141,-0.00402941,0.000105804,-1.9552e-07,1.22375e-10,-2829.38,6.4915], Tmin=(10,'K'), Tmax=(407.129,'K')),
            NASAPolynomial(coeffs=[0.665661,0.0291377,-1.63973e-05,4.58625e-09,-5.04449e-13,-2554.51,19.7439], Tmin=(407.129,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-23.526,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 614,
    label = "[N]DCC#N",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {3,D}
2 N u0 p1 c0 {4,T}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 C u0 p0 c0 {2,T} {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9552,0.00303806,5.22571e-05,-1.26219e-07,9.24106e-11,47940.7,8.25973], Tmin=(10,'K'), Tmax=(454.699,'K')),
            NASAPolynomial(coeffs=[3.73645,0.0131974,-8.42361e-06,2.57981e-09,-3.04096e-13,47875.5,8.20658], Tmin=(454.699,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (398.596,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 615,
    label = "[CH2]ONDN",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {2,D} {7,S}
4 C u1 p0 c0 {1,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91933,0.00552537,8.60337e-05,-2.14111e-07,1.60047e-10,33217.6,8.08218], Tmin=(10,'K'), Tmax=(451.025,'K')),
            NASAPolynomial(coeffs=[3.82767,0.0208639,-1.32874e-05,4.10255e-09,-4.87523e-13,33078.1,6.81355], Tmin=(451.025,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (276.177,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 616,
    label = "CCC#N",
    molecule = 
"""
1 N u0 p1 c0 {4,T}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 C u0 p0 c0 {1,T} {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90815,0.00647587,5.74196e-05,-1.02027e-07,5.73015e-11,4999.18,7.21116], Tmin=(10,'K'), Tmax=(460.137,'K')),
            NASAPolynomial(coeffs=[1.31966,0.028978,-1.5936e-05,4.25518e-09,-4.43991e-13,5237.38,17.6898], Tmin=(460.137,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (41.5398,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 617,
    label = "[O-][NH+]DCNDC",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {4,D} {7,S}
3 N u0 p1 c0 {4,S} {5,D}
4 C u0 p0 c0 {2,D} {3,S} {6,S}
5 C u0 p0 c0 {3,D} {8,S} {9,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93396,0.00548885,8.97036e-05,-1.91582e-07,1.32302e-10,18061.4,9.01767], Tmin=(10,'K'), Tmax=(371.685,'K')),
            NASAPolynomial(coeffs=[1.39548,0.0328079,-2.05487e-05,6.17374e-09,-7.1302e-13,18250.1,18.752], Tmin=(371.685,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (150.17,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 618,
    label = "NNDCDC",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 N u0 p1 c0 {1,S} {4,D}
3 C u0 p0 c0 {4,D} {7,S} {8,S}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9396,0.00375452,8.34734e-05,-1.71946e-07,1.09045e-10,34641.5,7.80592], Tmin=(10,'K'), Tmax=(513.276,'K')),
            NASAPolynomial(coeffs=[2.88683,0.0247265,-1.51272e-05,4.58358e-09,-5.4207e-13,34581.4,10.5445], Tmin=(513.276,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (288.007,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 619,
    label = "ONDCDC",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {7,S}
2 N u0 p1 c0 {1,S} {4,D}
3 C u0 p0 c0 {4,D} {5,S} {6,S}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93549,0.00395559,7.41808e-05,-1.55589e-07,9.82463e-11,18713.5,7.79271], Tmin=(10,'K'), Tmax=(530.544,'K')),
            NASAPolynomial(coeffs=[3.55132,0.0208745,-1.32995e-05,4.15372e-09,-5.01474e-13,18556.9,7.54271], Tmin=(530.544,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (155.571,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 620,
    label = "[O-][NH+]D[C]N",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {4,S} {6,S} {7,S}
3 N u0 p0 c+1 {1,S} {4,D} {5,S}
4 C u1 p0 c0 {2,S} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95178,0.0028456,6.77359e-05,-1.29234e-07,7.54297e-11,26460.9,8.76826], Tmin=(10,'K'), Tmax=(555.386,'K')),
            NASAPolynomial(coeffs=[2.71224,0.0225584,-1.46347e-05,4.60733e-09,-5.56762e-13,26432.3,12.5218], Tmin=(555.386,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (219.989,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 621,
    label = "[O-][NH+]DCDC",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {4,D} {5,S}
3 C u0 p0 c0 {4,D} {6,S} {7,S}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90021,0.0108123,1.67456e-05,-2.89107e-08,1.21762e-11,30327.4,8.04208], Tmin=(10,'K'), Tmax=(832.133,'K')),
            NASAPolynomial(coeffs=[3.48527,0.0195074,-1.10066e-05,2.99974e-09,-3.17966e-13,30164.4,8.57376], Tmin=(832.133,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (252.158,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 622,
    label = "NCD[C]NDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 N u0 p1 c0 {4,S} {7,S} {8,S}
3 N u0 p1 c0 {1,D} {5,S}
4 C u0 p0 c0 {2,S} {5,D} {6,S}
5 C u1 p0 c0 {3,S} {4,D}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83034,0.0136252,0.000123285,-4.36607e-07,4.34943e-10,32930.7,9.97328], Tmin=(10,'K'), Tmax=(360.549,'K')),
            NASAPolynomial(coeffs=[5.24113,0.0222963,-1.39798e-05,4.30331e-09,-5.13021e-13,32670.9,2.41382], Tmin=(360.549,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (273.822,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 623,
    label = "NOO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {6,S}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95556,0.00278933,5.56651e-05,-1.18495e-07,7.70276e-11,-659.663,6.99066], Tmin=(10,'K'), Tmax=(509.085,'K')),
            NASAPolynomial(coeffs=[3.538,0.0154571,-9.31805e-06,2.82245e-09,-3.3525e-13,-738.788,7.52853], Tmin=(509.085,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-5.49775,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 624,
    label = "CNDCN",
    molecule = 
"""
1  N u0 p1 c0 {4,S} {9,S} {10,S}
2  N u0 p1 c0 {3,S} {4,D}
3  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {1,S} {2,D} {8,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91882,0.00575352,8.92827e-05,-1.88401e-07,1.30356e-10,3634.81,7.05309], Tmin=(10,'K'), Tmax=(368.968,'K')),
            NASAPolynomial(coeffs=[1.49353,0.0320458,-1.76041e-05,4.72328e-09,-4.96561e-13,3813.78,16.3356], Tmin=(368.968,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (30.2017,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 625,
    label = "NDCNDO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 N u0 p1 c0 {4,D} {6,S}
3 N u0 p1 c0 {1,D} {4,S}
4 C u0 p0 c0 {2,D} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93495,0.00731484,2.19932e-05,-3.71575e-08,1.68835e-11,22459.6,7.9098], Tmin=(10,'K'), Tmax=(750.883,'K')),
            NASAPolynomial(coeffs=[3.41859,0.0166542,-9.82562e-06,2.7785e-09,-3.03541e-13,22351.4,9.01612], Tmin=(750.883,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (186.74,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 626,
    label = "[O-][NH+]DN",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {4,S}
3 N u0 p1 c0 {2,D} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0813,-0.00563709,4.60152e-05,-5.85649e-08,2.4292e-11,15114.9,6.42626], Tmin=(10,'K'), Tmax=(741.542,'K')),
            NASAPolynomial(coeffs=[1.48757,0.0148684,-8.64128e-06,2.41982e-09,-2.62164e-13,15320.5,16.9562], Tmin=(741.542,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (125.688,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 627,
    label = "NO[N]NDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {5,D}
3 N u0 p1 c0 {1,S} {6,S} {7,S}
4 N u1 p1 c0 {1,S} {5,S}
5 N u0 p1 c0 {2,D} {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81883,0.0156427,6.71772e-05,-2.48701e-07,2.43533e-10,39684,10.103], Tmin=(10,'K'), Tmax=(366.93,'K')),
            NASAPolynomial(coeffs=[4.57684,0.0215043,-1.45277e-05,4.6578e-09,-5.66644e-13,39533.3,5.91021], Tmin=(366.93,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (329.964,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 628,
    label = "[O-][N+]DNN",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {4,S}
2 N u0 p1 c0 {3,S} {5,S} {6,S}
3 N u0 p1 c0 {2,S} {4,D}
4 N u1 p0 c+1 {1,S} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94157,0.00357202,6.34182e-05,-1.3424e-07,8.47095e-11,35658.8,8.6556], Tmin=(10,'K'), Tmax=(535.091,'K')),
            NASAPolynomial(coeffs=[3.74312,0.0177332,-1.18183e-05,3.77427e-09,-4.59412e-13,35498.5,7.79299], Tmin=(535.091,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (296.464,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 629,
    label = "[N-]([NH+]DO)OO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 O u0 p2 c0 {1,S} {7,S}
3 O u0 p2 c0 {4,D}
4 N u0 p0 c+1 {3,D} {5,S} {6,S}
5 N u0 p2 c-1 {1,S} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83126,0.0142834,3.72929e-05,-1.01853e-07,7.08819e-11,15371.4,9.503], Tmin=(10,'K'), Tmax=(505.754,'K')),
            NASAPolynomial(coeffs=[4.09002,0.021987,-1.44727e-05,4.50069e-09,-5.32056e-13,15220.5,7.19826], Tmin=(505.754,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (127.785,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 630,
    label = "[NH]CCDN",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {3,S} {8,S}
2 N u0 p1 c0 {4,D} {9,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {2,D} {3,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96786,0.00218467,9.84129e-05,-2.04549e-07,1.40532e-10,31105.6,9.17165], Tmin=(10,'K'), Tmax=(371.987,'K')),
            NASAPolynomial(coeffs=[1.26468,0.031251,-1.87893e-05,5.48927e-09,-6.22455e-13,31306.7,19.5399], Tmin=(371.987,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (258.624,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 631,
    label = "C[CH]NO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {10,S}
2  N u0 p1 c0 {1,S} {4,S} {9,S}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u1 p0 c0 {2,S} {3,S} {8,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8583,0.012509,9.10181e-05,-2.72806e-07,2.64879e-10,9583.75,8.25458], Tmin=(10,'K'), Tmax=(261.716,'K')),
            NASAPolynomial(coeffs=[2.61301,0.0315417,-1.80665e-05,5.06553e-09,-5.54225e-13,9648.93,12.5931], Tmin=(261.716,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (79.6839,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 632,
    label = "CN[C]DN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {4,S} {8,S}
2 N u0 p1 c0 {4,D} {9,S}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 C u1 p0 c0 {1,S} {2,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69997,0.0296811,-6.3463e-05,1.34508e-07,-1.04548e-10,27531.2,8.88502], Tmin=(10,'K'), Tmax=(458.96,'K')),
            NASAPolynomial(coeffs=[2.42697,0.0279404,-1.5825e-05,4.37732e-09,-4.73084e-13,27783.3,15.5078], Tmin=(458.96,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (228.9,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 633,
    label = "[O-][N+]DNCDC",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {3,D} {4,S}
3 N u1 p0 c+1 {1,S} {2,D}
4 C u0 p0 c0 {2,S} {5,D} {6,S}
5 C u0 p0 c0 {4,D} {7,S} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88717,0.00914584,6.31202e-05,-1.3686e-07,8.81456e-11,33058.1,9.63489], Tmin=(10,'K'), Tmax=(494.954,'K')),
            NASAPolynomial(coeffs=[2.62935,0.0275325,-1.75181e-05,5.31394e-09,-6.17117e-13,33081.9,13.8012], Tmin=(494.954,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (274.846,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 634,
    label = "CO[C]DN",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 N u0 p1 c0 {4,D} {8,S}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 C u1 p0 c0 {1,S} {2,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86616,0.0121623,2.18732e-05,-3.80516e-08,1.69061e-11,8304.89,7.83318], Tmin=(10,'K'), Tmax=(753.551,'K')),
            NASAPolynomial(coeffs=[2.71571,0.0241495,-1.36935e-05,3.76991e-09,-4.04361e-13,8311.31,11.9501], Tmin=(753.551,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (69.0405,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 635,
    label = "[N-]([NH+]DO)C[O]",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {5,S}
2 O u0 p2 c0 {3,D}
3 N u0 p0 c+1 {2,D} {4,S} {8,S}
4 N u0 p2 c-1 {3,S} {5,S}
5 C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9505,0.00331888,9.61458e-05,-2.0775e-07,1.42426e-10,17776.6,10.6763], Tmin=(10,'K'), Tmax=(444.887,'K')),
            NASAPolynomial(coeffs=[1.96697,0.0292948,-1.88871e-05,5.76427e-09,-6.71919e-13,17872.5,17.7336], Tmin=(444.887,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (147.797,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 636,
    label = "NONN",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {3,S} {5,S}
3 N u0 p1 c0 {2,S} {6,S} {7,S}
4 N u0 p1 c0 {1,S} {8,S} {9,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93655,0.003983,9.53308e-05,-1.96052e-07,1.25274e-10,22161.7,8.48736], Tmin=(10,'K'), Tmax=(502.473,'K')),
            NASAPolynomial(coeffs=[2.47598,0.0286738,-1.73755e-05,5.22561e-09,-6.13655e-13,22143.6,12.8875], Tmin=(502.473,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (184.245,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 637,
    label = "[NH]OCDN",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 N u0 p1 c0 {4,D} {6,S}
3 N u1 p1 c0 {1,S} {7,S}
4 C u0 p0 c0 {1,S} {2,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95995,0.00237983,6.67212e-05,-1.24861e-07,7.25023e-11,21828.7,8.75458], Tmin=(10,'K'), Tmax=(542.674,'K')),
            NASAPolynomial(coeffs=[2.26395,0.0234323,-1.51069e-05,4.70179e-09,-5.61851e-13,21886.8,14.74], Tmin=(542.674,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (181.478,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 638,
    label = "[N-]([NH+]DO)O[O]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {4,D}
3 O u1 p2 c0 {1,S}
4 N u0 p0 c+1 {2,D} {5,S} {6,S}
5 N u0 p2 c-1 {1,S} {4,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8818,0.0108769,3.16972e-05,-7.2434e-08,4.22891e-11,33124.3,10.0555], Tmin=(10,'K'), Tmax=(613.435,'K')),
            NASAPolynomial(coeffs=[4.45348,0.0179436,-1.19774e-05,3.7159e-09,-4.35655e-13,32851,5.92145], Tmin=(613.435,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (275.391,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 639,
    label = "[CH2]ONC",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  N u0 p1 c0 {1,S} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
4  C u1 p0 c0 {1,S} {9,S} {10,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80878,0.016314,2.96596e-05,-5.53312e-08,2.69988e-11,16166.5,7.65188], Tmin=(10,'K'), Tmax=(643.864,'K')),
            NASAPolynomial(coeffs=[1.85666,0.0327681,-1.87532e-05,5.23282e-09,-5.69427e-13,16328.2,15.5138], Tmin=(643.864,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (134.394,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 640,
    label = "[O-][NH+]D[C]CDN",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {5,D} {7,S}
3 N u0 p1 c0 {4,D} {8,S}
4 C u0 p0 c0 {3,D} {5,S} {6,S}
5 C u1 p0 c0 {2,D} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89571,0.0200245,-2.71267e-06,-6.66545e-09,2.79471e-12,50436,9.84357], Tmin=(10,'K'), Tmax=(1196.63,'K')),
            NASAPolynomial(coeffs=[7.6767,0.0155967,-7.45491e-06,1.71081e-09,-1.53269e-13,48943.3,-11.5326], Tmin=(1196.63,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (419.374,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 641,
    label = "C[C]DN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,D} {7,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u1 p0 c0 {1,D} {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97524,0.00150433,5.4647e-05,-9.76679e-08,5.72355e-11,25009.9,6.40067], Tmin=(10,'K'), Tmax=(437.814,'K')),
            NASAPolynomial(coeffs=[1.86045,0.020827,-1.1559e-05,3.15167e-09,-3.38138e-13,25195,14.8565], Tmin=(437.814,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (207.933,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 642,
    label = "[N-]DCD[N+]D[CH]",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {3,D} {4,D}
2 N u0 p2 c-1 {4,D}
3 C u1 p0 c0 {1,D} {5,S}
4 C u0 p0 c0 {1,D} {2,D}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94651,0.00360926,5.38949e-05,-1.34208e-07,9.92736e-11,54890.9,7.78591], Tmin=(10,'K'), Tmax=(462.097,'K')),
            NASAPolynomial(coeffs=[4.08002,0.012567,-8.0119e-06,2.4674e-09,-2.93382e-13,54770.5,6.0765], Tmin=(462.097,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (456.381,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 643,
    label = "[CH2]CNN",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {3,S} {7,S}
2  N u0 p1 c0 {1,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u1 p0 c0 {3,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90748,0.00734244,0.000118241,-2.87847e-07,2.31417e-10,30315.5,8.5254], Tmin=(10,'K'), Tmax=(316.606,'K')),
            NASAPolynomial(coeffs=[1.57532,0.0368066,-2.13514e-05,6.08545e-09,-6.77241e-13,30463.2,17.0945], Tmin=(316.606,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (252.055,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 644,
    label = "[O-][N+]#C",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.22175,0.0258371,-7.81763e-05,1.22751e-07,-7.2101e-11,19291.2,6.51552], Tmin=(10,'K'), Tmax=(502.253,'K')),
            NASAPolynomial(coeffs=[4.90093,0.00668623,-3.72626e-06,1.02532e-09,-1.10914e-13,19195.4,0.296254], Tmin=(502.253,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (160.385,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (87.302,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 645,
    label = "[NH-][N+]DNO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {6,S}
2 N u1 p0 c+1 {3,D} {4,S}
3 N u0 p1 c0 {1,S} {2,D}
4 N u0 p2 c-1 {2,S} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96695,0.00187107,5.39963e-05,-9.51095e-08,5.13422e-11,36543.7,8.53329], Tmin=(10,'K'), Tmax=(585.006,'K')),
            NASAPolynomial(coeffs=[2.21799,0.0212359,-1.46468e-05,4.75649e-09,-5.8341e-13,36621.6,14.9502], Tmin=(585.006,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (303.827,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 646,
    label = "C[NH]",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00704,-0.000596671,3.26076e-05,-4.11551e-08,1.68324e-11,19952,4.58232], Tmin=(10,'K'), Tmax=(635.692,'K')),
            NASAPolynomial(coeffs=[1.2223,0.0169253,-8.73652e-06,2.20218e-09,-2.18289e-13,20306,16.7556], Tmin=(635.692,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (165.89,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 647,
    label = "OCDCD[N]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {6,S}
2 N u1 p1 c0 {4,D}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93621,0.00408352,6.5249e-05,-1.49716e-07,1.02118e-10,9526.52,8.50066], Tmin=(10,'K'), Tmax=(500.362,'K')),
            NASAPolynomial(coeffs=[4.05248,0.0162277,-1.03494e-05,3.22774e-09,-3.88858e-13,9351.22,6.38487], Tmin=(500.362,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (79.1915,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 648,
    label = "[N-]([NH+]DO)C#[C]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 N u0 p0 c+1 {1,D} {3,S} {6,S}
3 N u0 p2 c-1 {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,T}
5 C u1 p0 c0 {4,T}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7623,0.023584,-4.14306e-05,7.07615e-08,-5.5029e-11,86652,9.63502], Tmin=(10,'K'), Tmax=(380.304,'K')),
            NASAPolynomial(coeffs=[4.01246,0.01861,-1.2571e-05,3.97207e-09,-4.74947e-13,86649.9,8.89276], Tmin=(380.304,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (720.464,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 649,
    label = "CNO[O]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 N u0 p1 c0 {1,S} {4,S} {8,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93943,0.0149247,7.40164e-06,-1.46082e-08,5.07101e-12,15383.4,8.59196], Tmin=(10,'K'), Tmax=(1133.84,'K')),
            NASAPolynomial(coeffs=[5.77349,0.0177324,-8.58681e-06,2.00943e-09,-1.84272e-13,14371.1,-3.11661], Tmin=(1133.84,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (127.936,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 650,
    label = "[NH-][N+]DNN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u1 p0 c+1 {2,D} {4,S}
4 N u0 p2 c-1 {3,S} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86403,0.0117669,2.85001e-05,-6.82889e-08,4.35412e-11,51820.5,9.18738], Tmin=(10,'K'), Tmax=(512.882,'K')),
            NASAPolynomial(coeffs=[3.25173,0.0212837,-1.32004e-05,3.94033e-09,-4.526e-13,51820.9,11.1246], Tmin=(512.882,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (430.845,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 651,
    label = "NND[CH]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {3,D}
3 C u1 p0 c0 {2,D} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97891,0.0012651,4.76453e-05,-8.58704e-08,4.92031e-11,43435.9,6.76289], Tmin=(10,'K'), Tmax=(522.028,'K')),
            NASAPolynomial(coeffs=[2.33308,0.0177806,-1.10298e-05,3.38976e-09,-4.05377e-13,43554.5,13.1236], Tmin=(522.028,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (361.138,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 652,
    label = "[CH2]CNO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {10,S}
2  N u0 p1 c0 {1,S} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u1 p0 c0 {3,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89106,0.0098964,0.000123022,-3.96329e-07,4.2592e-10,13194.7,8.42116], Tmin=(10,'K'), Tmax=(235.486,'K')),
            NASAPolynomial(coeffs=[2.57944,0.0321758,-1.88934e-05,5.43759e-09,-6.09734e-13,13256.5,12.8522], Tmin=(235.486,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (109.717,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 653,
    label = "NOCD[CH]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u1 p0 c0 {3,D} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93458,0.00633023,0.000121163,-4.33214e-07,5.25122e-10,36176.2,9.15475], Tmin=(10,'K'), Tmax=(208.269,'K')),
            NASAPolynomial(coeffs=[2.94553,0.0253257,-1.56463e-05,4.70968e-09,-5.48259e-13,36217.4,12.3746], Tmin=(208.269,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (300.804,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 654,
    label = "[O-][NH+]D[C]CDO",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 O u0 p2 c0 {4,D}
3 N u0 p0 c+1 {1,S} {5,D} {6,S}
4 C u0 p0 c0 {2,D} {5,S} {7,S}
5 C u1 p0 c0 {3,D} {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78753,0.017124,2.57343e-06,-1.60026e-08,7.95669e-12,26538.2,9.93589], Tmin=(10,'K'), Tmax=(794.44,'K')),
            NASAPolynomial(coeffs=[3.97543,0.0205952,-1.2321e-05,3.49518e-09,-3.81501e-13,26369,8.19529], Tmin=(794.44,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (220.626,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 655,
    label = "CO[CH]NDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {2,D} {5,S}
4 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
5 C u1 p0 c0 {1,S} {3,S} {9,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83487,0.0140863,6.43851e-05,-1.9147e-07,1.77133e-10,-1403.15,8.90798], Tmin=(10,'K'), Tmax=(276.039,'K')),
            NASAPolynomial(coeffs=[2.80347,0.0290318,-1.68282e-05,4.66741e-09,-5.0032e-13,-1346.21,12.5563], Tmin=(276.039,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-11.6768,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 656,
    label = "[O-][C]D[NH2+]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 N u0 p0 c+1 {3,D} {4,S} {5,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97327,0.00179309,4.27982e-05,-9.60978e-08,6.78752e-11,-3179,6.97091], Tmin=(10,'K'), Tmax=(450.991,'K')),
            NASAPolynomial(coeffs=[3.42874,0.0116623,-6.78843e-06,1.97983e-09,-2.27559e-13,-3181.13,8.59616], Tmin=(450.991,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-26.4352,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 657,
    label = "[O-][NH+]DNCC",
    molecule = 
"""
1  O u0 p3 c-1 {2,S}
2  N u0 p0 c+1 {1,S} {3,D} {11,S}
3  N u0 p1 c0 {2,D} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92631,0.0157823,3.11503e-05,-4.38506e-08,1.57911e-11,6367.55,8.17896], Tmin=(10,'K'), Tmax=(978.765,'K')),
            NASAPolynomial(coeffs=[3.37688,0.0326831,-1.72108e-05,4.38773e-09,-4.3766e-13,5773.12,7.2318], Tmin=(978.765,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (52.986,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 658,
    label = "OCND[N]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {7,S}
2 N u0 p1 c0 {3,D} {4,S}
3 N u1 p1 c0 {2,D}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9572,0.00419998,0.000118577,-4.52669e-07,5.9418e-10,7118.9,8.82956], Tmin=(10,'K'), Tmax=(191.928,'K')),
            NASAPolynomial(coeffs=[3.15042,0.0210146,-1.28388e-05,3.81841e-09,-4.40068e-13,7149.86,11.3901], Tmin=(191.928,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (59.2127,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 659,
    label = "[NH]OCDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,D}
3 N u1 p1 c0 {1,S} {6,S}
4 C u0 p0 c0 {1,S} {2,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95807,0.00278334,6.36669e-05,-1.41278e-07,9.75883e-11,-5414.65,8.62047], Tmin=(10,'K'), Tmax=(461.231,'K')),
            NASAPolynomial(coeffs=[3.05352,0.0182829,-1.16353e-05,3.54785e-09,-4.15278e-13,-5412.63,11.4017], Tmin=(461.231,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-45.0269,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 660,
    label = "[O-][N+]DCDCDC",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u1 p0 c+1 {1,S} {5,D}
3 C u0 p0 c0 {4,D} {6,S} {7,S}
4 C u0 p0 c0 {3,D} {5,D}
5 C u0 p0 c0 {2,D} {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5632,0.0400876,-9.19689e-05,1.29959e-07,-7.29246e-11,51710.5,9.32874], Tmin=(10,'K'), Tmax=(501.518,'K')),
            NASAPolynomial(coeffs=[5.79041,0.0176104,-1.06441e-05,3.11505e-09,-3.52933e-13,51546.3,0.711739], Tmin=(501.518,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (429.923,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 661,
    label = "CN[C]DO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,S} {4,S} {8,S}
3 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
4 C u1 p0 c0 {1,D} {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8081,0.0199866,-3.71871e-05,1.03681e-07,-9.59286e-11,-3499.6,8.23928], Tmin=(10,'K'), Tmax=(430.389,'K')),
            NASAPolynomial(coeffs=[1.91449,0.0255744,-1.48003e-05,4.16084e-09,-4.55201e-13,-3225.36,17.0708], Tmin=(430.389,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-29.1025,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 662,
    label = "C[CH]NN",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {4,S} {9,S}
2  N u0 p1 c0 {1,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u1 p0 c0 {1,S} {3,S} {8,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77896,0.018286,3.20687e-05,-6.32523e-08,3.3423e-11,25532.6,8.19037], Tmin=(10,'K'), Tmax=(505.29,'K')),
            NASAPolynomial(coeffs=[1.56184,0.0358374,-2.00347e-05,5.49214e-09,-5.89634e-13,25756.6,17.3732], Tmin=(505.29,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (212.261,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 663,
    label = "[N-]([NH+]DO)ON",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {5,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,S} {7,S} {8,S}
4 N u0 p0 c+1 {2,D} {5,S} {6,S}
5 N u0 p2 c-1 {1,S} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81924,0.015852,2.37471e-05,-5.48134e-08,3.00894e-11,26571.4,9.50315], Tmin=(10,'K'), Tmax=(633.232,'K')),
            NASAPolynomial(coeffs=[3.52461,0.0250156,-1.52577e-05,4.46228e-09,-5.02581e-13,26462.3,9.63387], Tmin=(633.232,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (220.904,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 664,
    label = "[NH]CCDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 N u1 p1 c0 {3,S} {8,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 C u0 p0 c0 {1,D} {3,S} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88608,0.0106873,2.99436e-05,-5.019e-08,2.28206e-11,6739.76,9.04728], Tmin=(10,'K'), Tmax=(728.932,'K')),
            NASAPolynomial(coeffs=[2.57211,0.0251051,-1.45571e-05,4.07406e-09,-4.42416e-13,6739.83,13.6575], Tmin=(728.932,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (56.0292,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 665,
    label = "[O-][NH+]DO",
    molecule = 
"""
1 O u0 p3 c-1 {3,S}
2 O u0 p2 c0 {3,D}
3 N u0 p0 c+1 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06015,-0.00378167,2.78727e-05,-3.17808e-08,1.16678e-11,-6805.89,6.34877], Tmin=(10,'K'), Tmax=(846.464,'K')),
            NASAPolynomial(coeffs=[1.97769,0.0107889,-6.32901e-06,1.75732e-09,-1.87202e-13,-6622.79,15.0474], Tmin=(846.464,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-56.5717,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 666,
    label = "[O-][NH+]DCD[C]C",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {5,D} {9,S}
3 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
4 C u1 p0 c0 {3,S} {5,D}
5 C u0 p0 c0 {2,D} {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63258,0.035017,-6.28516e-05,1.04298e-07,-7.17594e-11,35219.8,10.4571], Tmin=(10,'K'), Tmax=(466.149,'K')),
            NASAPolynomial(coeffs=[3.62637,0.027842,-1.65043e-05,4.74908e-09,-5.30527e-13,35298.9,11.3246], Tmin=(466.149,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (292.821,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 667,
    label = "[CH]DCDN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {5,S}
2 C u0 p0 c0 {1,D} {3,D}
3 C u1 p0 c0 {2,D} {4,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94011,0.00382781,4.99539e-05,-1.21029e-07,8.46196e-11,45953.2,5.8367], Tmin=(10,'K'), Tmax=(506.675,'K')),
            NASAPolynomial(coeffs=[4.71911,0.0102539,-6.3013e-06,1.97667e-09,-2.44254e-13,45712.9,1.01512], Tmin=(506.675,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (382.061,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 668,
    label = "[CH]DCDCDN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,D} {6,S}
2 C u0 p0 c0 {3,D} {4,D}
3 C u0 p0 c0 {1,D} {2,D}
4 C u1 p0 c0 {2,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88478,0.00837027,8.24015e-05,-2.55725e-07,2.2149e-10,59038.5,7.62609], Tmin=(10,'K'), Tmax=(419.394,'K')),
            NASAPolynomial(coeffs=[5.4107,0.0138178,-8.61772e-06,2.67154e-09,-3.22845e-13,58734.6,-0.506728], Tmin=(419.394,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (490.873,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 669,
    label = "CON[CH2]",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  N u0 p1 c0 {1,S} {4,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4  C u1 p0 c0 {2,S} {9,S} {10,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76636,0.0197498,1.52874e-05,-3.29347e-08,1.48841e-11,15694.2,7.59898], Tmin=(10,'K'), Tmax=(755.785,'K')),
            NASAPolynomial(coeffs=[2.56712,0.0311533,-1.73809e-05,4.73396e-09,-5.04169e-13,15731.1,12.0934], Tmin=(755.785,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (130.464,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 670,
    label = "[N]DCDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 N u1 p1 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48791,0.000692199,1.99237e-05,-3.57625e-08,1.96253e-11,13834.9,6.51947], Tmin=(10,'K'), Tmax=(575.538,'K')),
            NASAPolynomial(coeffs=[2.86442,0.00772452,-5.43873e-06,1.76394e-09,-2.14708e-13,13862,8.79465], Tmin=(575.538,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (115.025,'kJ/mol'),
        Cp0 = (29.1007,'J/(mol*K)'),
        CpInf = (62.3585,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 671,
    label = "CNDCO",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {9,S}
2 N u0 p1 c0 {3,S} {4,D}
3 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {2,D} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9143,0.00654556,5.78165e-05,-1.01313e-07,5.57148e-11,-18966,7.05547], Tmin=(10,'K'), Tmax=(471.772,'K')),
            NASAPolynomial(coeffs=[1.12852,0.0301653,-1.72824e-05,4.81059e-09,-5.21644e-13,-18703.2,18.4024], Tmin=(471.772,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-157.71,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 672,
    label = "NON",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {4,S} {5,S}
3 N u0 p1 c0 {1,S} {6,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94275,0.00431195,5.21579e-05,-1.15357e-07,8.35173e-11,13318.5,6.41486], Tmin=(10,'K'), Tmax=(352.31,'K')),
            NASAPolynomial(coeffs=[2.65158,0.0189714,-1.02563e-05,2.74788e-09,-2.90127e-13,13409.5,11.297], Tmin=(352.31,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (110.726,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 673,
    label = "CNC[O]",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {4,S}
2  N u0 p1 c0 {3,S} {4,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95245,0.0130093,2.94269e-05,-4.01598e-08,1.43284e-11,2196.87,7.88641], Tmin=(10,'K'), Tmax=(980.393,'K')),
            NASAPolynomial(coeffs=[3.25757,0.028997,-1.51577e-05,3.84162e-09,-3.81329e-13,1701.03,8.00138], Tmin=(980.393,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (18.3078,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 674,
    label = "CNCDC",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {3,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95578,0.00285114,0.000109685,-2.13099e-07,1.36653e-10,4730.91,7.317], Tmin=(10,'K'), Tmax=(398.883,'K')),
            NASAPolynomial(coeffs=[0.481529,0.037695,-2.13608e-05,5.94736e-09,-6.50126e-13,5008.04,20.8847], Tmin=(398.883,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (39.3221,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 675,
    label = "[O-][NH+]D[C]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {6,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {2,S} {4,D} {5,S}
4 C u1 p0 c0 {1,S} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95548,0.00259411,5.74744e-05,-1.09713e-07,6.33004e-11,10363.3,8.48475], Tmin=(10,'K'), Tmax=(569.414,'K')),
            NASAPolynomial(coeffs=[3.05755,0.0191052,-1.28987e-05,4.14811e-09,-5.06629e-13,10300.2,10.8586], Tmin=(569.414,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (86.1471,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 676,
    label = "NCDCDO",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {4,D} {5,S}
4 C u0 p0 c0 {1,D} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9596,0.00399898,0.000115231,-4.26496e-07,5.41479e-10,-217.546,8.20497], Tmin=(10,'K'), Tmax=(198.555,'K')),
            NASAPolynomial(coeffs=[3.11731,0.0209676,-1.29601e-05,3.9206e-09,-4.59324e-13,-184.098,10.9068], Tmin=(198.555,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-1.7887,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 677,
    label = "NNN",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 N u0 p1 c0 {1,S} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0673,-0.00676339,0.000114162,-2.17977e-07,1.39388e-10,21616.5,7.08668], Tmin=(10,'K'), Tmax=(464.772,'K')),
            NASAPolynomial(coeffs=[1.35496,0.0247834,-1.41268e-05,4.01612e-09,-4.48627e-13,21780.1,17.1408], Tmin=(464.772,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (179.727,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 678,
    label = "[N-]([N+]DC)O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {7,S}
2 N u1 p0 c+1 {3,S} {4,D}
3 N u0 p2 c-1 {1,S} {2,S}
4 C u0 p0 c0 {2,D} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95238,0.00277643,6.8457e-05,-1.27995e-07,7.31539e-11,24229.9,8.47816], Tmin=(10,'K'), Tmax=(564.788,'K')),
            NASAPolynomial(coeffs=[2.51115,0.0237199,-1.56801e-05,4.97714e-09,-6.03512e-13,24221.5,13.0919], Tmin=(564.788,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (201.439,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 679,
    label = "[O-][NH+]DCN[CH2]",
    molecule = 
"""
multiplicity 2
1  O u0 p3 c-1 {3,S}
2  N u0 p1 c0 {4,S} {5,S} {7,S}
3  N u0 p0 c+1 {1,S} {4,D} {8,S}
4  C u0 p0 c0 {2,S} {3,D} {6,S}
5  C u1 p0 c0 {2,S} {9,S} {10,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87625,0.0119859,0.000170159,-6.57406e-07,8.07358e-10,23360.8,9.70145], Tmin=(10,'K'), Tmax=(257.318,'K')),
            NASAPolynomial(coeffs=[3.19254,0.0337259,-2.13458e-05,6.56866e-09,-7.79037e-13,23359.2,11.3571], Tmin=(257.318,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (194.255,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 680,
    label = "[O-][NH+]DCO[CH2]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p3 c-1 {3,S}
3 N u0 p0 c+1 {2,S} {4,D} {7,S}
4 C u0 p0 c0 {1,S} {3,D} {6,S}
5 C u1 p0 c0 {1,S} {8,S} {9,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89022,0.00773785,0.000122209,-3.12271e-07,2.41669e-10,11498.9,9.34319], Tmin=(10,'K'), Tmax=(431.153,'K')),
            NASAPolynomial(coeffs=[3.52144,0.0297282,-1.8899e-05,5.80707e-09,-6.86553e-13,11358.1,8.81058], Tmin=(431.153,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (95.6012,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 681,
    label = "NN[CH]NDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,S} {5,S} {6,S}
3 N u0 p1 c0 {2,S} {8,S} {9,S}
4 N u0 p1 c0 {1,D} {5,S}
5 C u1 p0 c0 {2,S} {4,S} {7,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96106,0.00440449,0.000252345,-1.26478e-06,2.2288e-09,31820,9.75888], Tmin=(10,'K'), Tmax=(142.488,'K')),
            NASAPolynomial(coeffs=[3.04202,0.030204,-1.92506e-05,5.94542e-09,-7.06589e-13,31846.2,12.402], Tmin=(142.488,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (264.914,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 682,
    label = "CC[NH]",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,S} {9,S}
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
            NASAPolynomial(coeffs=[3.96585,0.00196014,7.01228e-05,-1.157e-07,6.20753e-11,16002.9,6.77963], Tmin=(10,'K'), Tmax=(480.264,'K')),
            NASAPolynomial(coeffs=[0.637866,0.0296779,-1.64469e-05,4.46914e-09,-4.77636e-13,16322.6,20.3945], Tmin=(480.264,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (133.039,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 683,
    label = "NOOO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {7,S}
4 N u0 p1 c0 {1,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91063,0.0057172,8.35575e-05,-1.95772e-07,1.34611e-10,3699.09,8.50124], Tmin=(10,'K'), Tmax=(503.598,'K')),
            NASAPolynomial(coeffs=[4.4618,0.0196887,-1.27123e-05,4.0235e-09,-4.90569e-13,3410.89,3.91006], Tmin=(503.598,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (30.7325,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 684,
    label = "NO[O]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93217,0.0067594,7.7288e-06,-1.39785e-08,5.8174e-12,17116.4,7.57816], Tmin=(10,'K'), Tmax=(847.315,'K')),
            NASAPolynomial(coeffs=[3.67223,0.0113264,-6.26859e-06,1.68656e-09,-1.77131e-13,17040.6,8.08167], Tmin=(847.315,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (142.313,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 685,
    label = "N[CH]CN",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {3,S} {8,S} {9,S}
2  N u0 p1 c0 {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u1 p0 c0 {2,S} {3,S} {7,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9413,0.0037827,0.000119626,-2.43304e-07,1.57932e-10,14748.6,9.19576], Tmin=(10,'K'), Tmax=(470.673,'K')),
            NASAPolynomial(coeffs=[1.25225,0.0374686,-2.22534e-05,6.55648e-09,-7.5686e-13,14881.8,18.8677], Tmin=(470.673,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (122.615,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 686,
    label = "C[CH]ON",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {4,S}
2  N u0 p1 c0 {1,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4  C u1 p0 c0 {1,S} {3,S} {8,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70217,0.0290179,-4.47024e-05,9.56805e-08,-7.74197e-11,12493,8.11821], Tmin=(10,'K'), Tmax=(467.364,'K')),
            NASAPolynomial(coeffs=[1.94312,0.0324629,-1.84964e-05,5.14613e-09,-5.59134e-13,12784.3,16.6231], Tmin=(467.364,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (103.865,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 687,
    label = "CNC[NH]",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {3,S} {4,S} {10,S}
2  N u1 p1 c0 {3,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86853,0.0139176,3.82641e-05,-5.56868e-08,2.20697e-11,22223.4,8.02834], Tmin=(10,'K'), Tmax=(837.51,'K')),
            NASAPolynomial(coeffs=[1.46685,0.0358049,-1.95928e-05,5.21857e-09,-5.43729e-13,22260.3,17.0082], Tmin=(837.51,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (184.781,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 688,
    label = "[O-][N+]DCNDC",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {4,S} {5,D}
3 N u1 p0 c+1 {1,S} {4,D}
4 C u0 p0 c0 {2,S} {3,D} {6,S}
5 C u0 p0 c0 {2,D} {7,S} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94556,0.00362761,9.50827e-05,-2.06541e-07,1.41269e-10,30560.1,9.95497], Tmin=(10,'K'), Tmax=(453.761,'K')),
            NASAPolynomial(coeffs=[2.17313,0.028606,-1.84104e-05,5.63393e-09,-6.58833e-13,30624.7,16.0442], Tmin=(453.761,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (254.083,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 689,
    label = "COC[NH]",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {4,S}
2  N u1 p1 c0 {3,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87881,0.0121776,3.66696e-05,-5.38882e-08,2.17664e-11,1186.26,8.01599], Tmin=(10,'K'), Tmax=(817.304,'K')),
            NASAPolynomial(coeffs=[1.61002,0.0326703,-1.81723e-05,4.90141e-09,-5.15748e-13,1243.53,16.5855], Tmin=(817.304,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (9.86429,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 690,
    label = "[NH-]CD[N+]D[CH]",
    molecule = 
"""
multiplicity 2
1 N u0 p0 c+1 {3,D} {4,D}
2 N u0 p2 c-1 {3,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {5,S}
4 C u1 p0 c0 {1,D} {7,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90926,0.00912808,2.4927e-05,-4.20677e-08,1.90701e-11,43562.4,8.60276], Tmin=(10,'K'), Tmax=(741.947,'K')),
            NASAPolynomial(coeffs=[3.02292,0.0206499,-1.19999e-05,3.36228e-09,-3.65241e-13,43508.3,11.3635], Tmin=(741.947,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (362.194,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 691,
    label = "[NH]NNDN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {5,S}
2 N u0 p1 c0 {1,S} {4,D}
3 N u1 p1 c0 {1,S} {6,S}
4 N u0 p1 c0 {2,D} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9707,0.00169496,6.23917e-05,-1.08414e-07,5.89996e-11,52844.4,8.37661], Tmin=(10,'K'), Tmax=(554.093,'K')),
            NASAPolynomial(coeffs=[1.47604,0.0253511,-1.69363e-05,5.42484e-09,-6.61944e-13,53034.2,18.1567], Tmin=(554.093,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (439.361,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 692,
    label = "NC[O]",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {3,S}
2 N u0 p1 c0 {3,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00918,-0.00111554,6.77649e-05,-1.15016e-07,6.30892e-11,2034.68,7.71987], Tmin=(10,'K'), Tmax=(544.884,'K')),
            NASAPolynomial(coeffs=[1.57133,0.0225838,-1.34517e-05,3.89852e-09,-4.38037e-13,2214.2,17.2104], Tmin=(544.884,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (16.911,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 693,
    label = "NDCCD[N]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,D} {7,S}
2 N u1 p1 c0 {4,D}
3 C u0 p0 c0 {1,D} {4,S} {5,S}
4 C u0 p0 c0 {2,D} {3,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97909,0.00144485,7.49554e-05,-1.57371e-07,1.08985e-10,38425.3,8.67955], Tmin=(10,'K'), Tmax=(369.285,'K')),
            NASAPolynomial(coeffs=[1.9404,0.023521,-1.46901e-05,4.41808e-09,-5.11998e-13,38575.9,16.4847], Tmin=(369.285,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (319.487,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 694,
    label = "C[N]CO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {10,S}
2  N u1 p1 c0 {3,S} {4,S}
3  C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73236,0.0292784,-8.05804e-05,2.35415e-07,-2.21322e-10,-2406.73,8.60042], Tmin=(10,'K'), Tmax=(409.132,'K')),
            NASAPolynomial(coeffs=[0.910822,0.0348536,-2.0324e-05,5.73624e-09,-6.28578e-13,-1991.64,21.9423], Tmin=(409.132,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-20.0206,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 695,
    label = "ODNCDO",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {2,D} {4,S}
4 C u0 p0 c0 {1,D} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89224,0.0107679,-5.93774e-07,-5.84731e-09,2.68389e-12,-718.034,8.01186], Tmin=(10,'K'), Tmax=(991.333,'K')),
            NASAPolynomial(coeffs=[4.91545,0.010444,-5.86061e-06,1.56615e-09,-1.62031e-13,-1107.86,2.1414], Tmin=(991.333,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-5.97117,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 696,
    label = "NDNCDO",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,D} {4,S}
3 N u0 p1 c0 {2,D} {6,S}
4 C u0 p0 c0 {1,D} {2,S} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96905,0.00766387,1.4981e-05,-2.25094e-08,8.53703e-12,9867.14,7.8053], Tmin=(10,'K'), Tmax=(939.481,'K')),
            NASAPolynomial(coeffs=[4.00431,0.0148098,-8.0775e-06,2.11948e-09,-2.16518e-13,9538.53,5.92378], Tmin=(939.481,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (82.063,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 697,
    label = "NDCDCDN",
    molecule = 
"""
1 N u0 p1 c0 {3,D} {5,S}
2 N u0 p1 c0 {4,D} {6,S}
3 C u0 p0 c0 {1,D} {4,D}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93527,0.00473228,7.17609e-05,-1.95879e-07,1.61852e-10,46728,6.34368], Tmin=(10,'K'), Tmax=(406.404,'K')),
            NASAPolynomial(coeffs=[3.85946,0.0161797,-9.98778e-06,3.01278e-09,-3.52643e-13,46645.8,5.55391], Tmin=(406.404,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (388.52,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 698,
    label = "CNNC",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {3,S} {11,S}
2  N u0 p1 c0 {1,S} {4,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86765,0.0147121,3.64064e-05,-4.84275e-08,1.73639e-11,9136.95,5.59115], Tmin=(10,'K'), Tmax=(933.886,'K')),
            NASAPolynomial(coeffs=[1.03013,0.0383924,-2.01429e-05,5.15744e-09,-5.18803e-13,9164.29,16.3953], Tmin=(933.886,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (75.9809,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 699,
    label = "NO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 N u0 p1 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0218,-0.00177518,3.23394e-05,-4.76153e-08,2.35788e-11,-6592.59,4.8144], Tmin=(10,'K'), Tmax=(517.104,'K')),
            NASAPolynomial(coeffs=[2.32538,0.0113476,-5.72777e-06,1.46339e-09,-1.49529e-13,-6417.15,11.8798], Tmin=(517.104,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-54.8135,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 700,
    label = "NN",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04779,-0.0038199,4.65023e-05,-6.38972e-08,2.86437e-11,10335.7,4.2633], Tmin=(10,'K'), Tmax=(462.836,'K')),
            NASAPolynomial(coeffs=[1.48216,0.0156706,-7.96996e-06,2.04127e-09,-2.08528e-13,10601.9,14.9749], Tmin=(462.836,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (85.9378,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 701,
    label = "NDCDCDO",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,D} {5,S}
3 C u0 p0 c0 {2,D} {4,D}
4 C u0 p0 c0 {1,D} {3,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93884,0.00442861,5.77375e-05,-1.6156e-07,1.33445e-10,22144.6,7.11861], Tmin=(10,'K'), Tmax=(416.763,'K')),
            NASAPolynomial(coeffs=[4.17065,0.0124408,-7.94472e-06,2.44515e-09,-2.8993e-13,22036.4,5.13657], Tmin=(416.763,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (184.12,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 702,
    label = "[O-][NH+]DCC#N",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {4,D} {7,S}
3 N u0 p1 c0 {5,T}
4 C u0 p0 c0 {2,D} {5,S} {6,S}
5 C u0 p0 c0 {3,T} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93606,0.00481376,8.72849e-05,-2.25659e-07,1.8298e-10,23825.6,8.93566], Tmin=(10,'K'), Tmax=(389.091,'K')),
            NASAPolynomial(coeffs=[2.99563,0.0228745,-1.46967e-05,4.51358e-09,-5.31079e-13,23835.2,11.7686], Tmin=(389.091,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (198.101,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 703,
    label = "NDNC#[C]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {5,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u1 p0 c0 {3,T}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92388,0.00652056,6.86629e-05,-2.61145e-07,2.87698e-10,89908,7.5327], Tmin=(10,'K'), Tmax=(318.853,'K')),
            NASAPolynomial(coeffs=[4.31189,0.0122051,-7.72005e-06,2.34944e-09,-2.75741e-13,89829.7,5.26316], Tmin=(318.853,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (747.55,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 704,
    label = "CCNDC",
    molecule = 
"""
1  N u0 p1 c0 {2,S} {4,D}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {1,D} {10,S} {11,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94929,0.00297069,9.24696e-05,-1.57078e-07,8.69736e-11,4173.88,7.87445], Tmin=(10,'K'), Tmax=(464.235,'K')),
            NASAPolynomial(coeffs=[-0.116128,0.0380006,-2.07192e-05,5.47127e-09,-5.65019e-13,4551.33,24.368], Tmin=(464.235,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (34.6785,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 705,
    label = "NDNCDN",
    molecule = 
"""
1 N u0 p1 c0 {3,D} {4,S}
2 N u0 p1 c0 {4,D} {6,S}
3 N u0 p1 c0 {1,D} {7,S}
4 C u0 p0 c0 {1,S} {2,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97742,0.00141221,6.32052e-05,-1.17158e-07,7.07914e-11,33808.1,8.1322], Tmin=(10,'K'), Tmax=(425.564,'K')),
            NASAPolynomial(coeffs=[1.63524,0.0234165,-1.43169e-05,4.2259e-09,-4.82076e-13,34007.5,17.432], Tmin=(425.564,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (281.089,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 706,
    label = "CNDC[CH2]",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {3,D}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {1,D} {4,S} {8,S}
4  C u1 p0 c0 {3,S} {9,S} {10,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89805,0.00918052,5.50534e-05,-8.79455e-08,4.16134e-11,21642.3,7.02875], Tmin=(10,'K'), Tmax=(657.595,'K')),
            NASAPolynomial(coeffs=[0.989322,0.0344567,-1.98996e-05,5.5773e-09,-6.08061e-13,21860.9,18.5958], Tmin=(657.595,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (179.932,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 707,
    label = "[CH2]CON",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  N u0 p1 c0 {1,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u1 p0 c0 {3,S} {7,S} {8,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7232,0.0253422,-5.70602e-06,-5.0896e-09,2.39171e-12,15920.1,8.74043], Tmin=(10,'K'), Tmax=(1154.91,'K')),
            NASAPolynomial(coeffs=[5.62732,0.0245115,-1.21134e-05,2.9305e-09,-2.79823e-13,15095.8,-2.38431], Tmin=(1154.91,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (132.347,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 708,
    label = "C[N]CN",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {3,S} {10,S} {11,S}
2  N u1 p1 c0 {3,S} {4,S}
3  C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71273,0.0309132,-7.79022e-05,2.23004e-07,-2.04135e-10,18510.2,8.49338], Tmin=(10,'K'), Tmax=(425.114,'K')),
            NASAPolynomial(coeffs=[0.44307,0.0383539,-2.18577e-05,6.05308e-09,-6.53154e-13,18999,23.9496], Tmin=(425.114,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (153.895,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 709,
    label = "NOC#C",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {3,T} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89323,0.00804876,9.32887e-05,-2.83791e-07,2.52023e-10,32693.6,8.32839], Tmin=(10,'K'), Tmax=(393.439,'K')),
            NASAPolynomial(coeffs=[4.54702,0.018437,-1.12637e-05,3.4192e-09,-4.04496e-13,32510.3,4.10854], Tmin=(393.439,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (271.836,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 710,
    label = "[NH]NNDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,S} {4,S} {5,S}
3 N u1 p1 c0 {2,S} {6,S}
4 N u0 p1 c0 {1,D} {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96442,0.00202014,5.39503e-05,-9.64767e-08,5.26728e-11,35527.5,8.43453], Tmin=(10,'K'), Tmax=(585.985,'K')),
            NASAPolynomial(coeffs=[2.4719,0.0203712,-1.392e-05,4.51085e-09,-5.53795e-13,35562.3,13.6415], Tmin=(585.985,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (295.377,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 711,
    label = "[CH]DCDNNDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,D}
2 N u0 p1 c0 {3,S} {4,D}
3 N u0 p1 c0 {1,D} {2,S}
4 C u0 p0 c0 {2,D} {5,D}
5 C u1 p0 c0 {4,D} {6,S}
6 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89531,0.00694976,8.12294e-05,-2.11037e-07,1.55947e-10,59128,9.184], Tmin=(10,'K'), Tmax=(481.249,'K')),
            NASAPolynomial(coeffs=[5.12337,0.0167275,-1.15381e-05,3.7636e-09,-4.65065e-13,58778.4,1.75306], Tmin=(481.249,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (491.598,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 712,
    label = "NNND[CH]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {5,S}
2 N u0 p1 c0 {1,S} {6,S} {7,S}
3 N u0 p1 c0 {1,S} {4,D}
4 C u1 p0 c0 {3,D} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94202,0.00355512,8.22956e-05,-1.65356e-07,1.02365e-10,55055.8,8.67515], Tmin=(10,'K'), Tmax=(523.156,'K')),
            NASAPolynomial(coeffs=[2.70909,0.025364,-1.5737e-05,4.80947e-09,-5.71074e-13,55015.3,12.2051], Tmin=(523.156,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (457.74,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 713,
    label = "N[CH]CO",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {3,S} {10,S}
2  N u0 p1 c0 {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4  C u1 p0 c0 {2,S} {3,S} {7,S}
5  H u0 p0 c0 {3,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93197,0.00434886,0.000110524,-2.30306e-07,1.50325e-10,-7152.08,9.25517], Tmin=(10,'K'), Tmax=(485.714,'K')),
            NASAPolynomial(coeffs=[2.07452,0.0331264,-1.99802e-05,5.96049e-09,-6.94182e-13,-7130.67,15.238], Tmin=(485.714,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-59.4826,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 714,
    label = "NOON",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 N u0 p1 c0 {1,S} {5,S} {6,S}
4 N u0 p1 c0 {2,S} {7,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90042,0.0069239,0.000101854,-2.64504e-07,2.05098e-10,14000.1,8.77676], Tmin=(10,'K'), Tmax=(440.702,'K')),
            NASAPolynomial(coeffs=[4.17002,0.0226854,-1.37683e-05,4.15468e-09,-4.89841e-13,13799.5,5.69086], Tmin=(440.702,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (116.395,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 715,
    label = "CCND[CH]",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {4,D}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4  C u1 p0 c0 {1,D} {10,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86167,0.0126891,3.40907e-05,-5.09129e-08,2.07732e-11,26641.9,7.96142], Tmin=(10,'K'), Tmax=(798.741,'K')),
            NASAPolynomial(coeffs=[1.42234,0.0326986,-1.81225e-05,4.88272e-09,-5.13976e-13,26783,17.6253], Tmin=(798.741,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (221.507,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 716,
    label = "[N-]([NH+]DO)NO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {8,S}
2 O u0 p2 c0 {4,D}
3 N u0 p1 c0 {1,S} {5,S} {6,S}
4 N u0 p0 c+1 {2,D} {5,S} {7,S}
5 N u0 p2 c-1 {3,S} {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92597,0.00481097,9.58384e-05,-2.12219e-07,1.43719e-10,17160.2,9.44851], Tmin=(10,'K'), Tmax=(482.483,'K')),
            NASAPolynomial(coeffs=[2.94608,0.0271188,-1.76121e-05,5.47151e-09,-6.49137e-13,17089.7,11.7508], Tmin=(482.483,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (142.662,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 717,
    label = "CONDC",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {4,D}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {2,D} {8,S} {9,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94027,0.013528,1.76047e-05,-2.52583e-08,8.64107e-12,2273.95,6.85542], Tmin=(10,'K'), Tmax=(1058.49,'K')),
            NASAPolynomial(coeffs=[4.16014,0.0234774,-1.17715e-05,2.86553e-09,-2.73931e-13,1623.5,2.92952], Tmin=(1058.49,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (18.9394,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 718,
    label = "CDNC#N",
    molecule = 
"""
1 N u0 p1 c0 {3,D} {4,S}
2 N u0 p1 c0 {4,T}
3 C u0 p0 c0 {1,D} {5,S} {6,S}
4 C u0 p0 c0 {1,S} {2,T}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97678,0.00152477,5.72849e-05,-1.16989e-07,7.69903e-11,30217.6,7.53425], Tmin=(10,'K'), Tmax=(448.144,'K')),
            NASAPolynomial(coeffs=[2.508,0.0183215,-1.12759e-05,3.36041e-09,-3.87966e-13,30312.2,13.0284], Tmin=(448.144,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (251.24,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 719,
    label = "NCC#C",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {9,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93663,0.00408922,9.7776e-05,-2.08525e-07,1.38907e-10,25377,8.15127], Tmin=(10,'K'), Tmax=(480.57,'K')),
            NASAPolynomial(coeffs=[2.56379,0.0281396,-1.66944e-05,4.93327e-09,-5.72654e-13,25363.2,12.2518], Tmin=(480.57,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (210.982,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 720,
    label = "[N-]([N+]DC)N",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {7,S} {8,S}
2 N u1 p0 c+1 {3,S} {4,D}
3 N u0 p2 c-1 {1,S} {2,S}
4 C u0 p0 c0 {2,D} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9441,0.00334245,8.10055e-05,-1.56473e-07,9.29507e-11,40597,8.49951], Tmin=(10,'K'), Tmax=(543.051,'K')),
            NASAPolynomial(coeffs=[2.46165,0.0265184,-1.68653e-05,5.23696e-09,-6.27674e-13,40577.3,13.0824], Tmin=(543.051,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (337.522,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 721,
    label = "OCDCDN",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {6,S}
2 N u0 p1 c0 {4,D} {7,S}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93461,0.00426003,7.78735e-05,-1.76881e-07,1.21984e-10,6302.07,8.04709], Tmin=(10,'K'), Tmax=(482.535,'K')),
            NASAPolynomial(coeffs=[3.53782,0.0204842,-1.27702e-05,3.90445e-09,-4.62438e-13,6189.78,8.11184], Tmin=(482.535,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (52.3842,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 722,
    label = "NNO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {7,S}
2 N u0 p1 c0 {1,S} {3,S} {4,S}
3 N u0 p1 c0 {2,S} {5,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97558,0.00146992,5.76805e-05,-1.03713e-07,5.95424e-11,2900.73,6.79601], Tmin=(10,'K'), Tmax=(516.606,'K')),
            NASAPolynomial(coeffs=[1.94403,0.0215436,-1.3217e-05,4.05434e-09,-4.85355e-13,3052.67,14.6943], Tmin=(516.606,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (24.1091,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 723,
    label = "NCDCDN",
    molecule = 
"""
1 N u0 p1 c0 {3,S} {6,S} {7,S}
2 N u0 p1 c0 {4,D} {8,S}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u0 p0 c0 {2,D} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94005,0.00381264,8.51398e-05,-1.80391e-07,1.18186e-10,26393.4,8.10861], Tmin=(10,'K'), Tmax=(494.611,'K')),
            NASAPolynomial(coeffs=[2.88296,0.0245888,-1.49497e-05,4.49701e-09,-5.27785e-13,26348.4,10.9523], Tmin=(494.611,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (219.431,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 724,
    label = "[O-][NH+]C",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u1 p0 c+1 {1,S} {3,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92669,0.0077036,1.56313e-05,-2.03648e-08,6.98088e-12,4091.71,6.49998], Tmin=(10,'K'), Tmax=(985.812,'K')),
            NASAPolynomial(coeffs=[2.54863,0.018815,-9.67479e-06,2.42862e-09,-2.39902e-13,4095.2,11.7682], Tmin=(985.812,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (34.0239,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 725,
    label = "NO[N]O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,S} {7,S}
3 N u0 p1 c0 {1,S} {5,S} {6,S}
4 N u1 p1 c0 {1,S} {2,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88507,0.0110819,9.93992e-05,-4.25523e-07,5.38613e-10,17886.1,9.12606], Tmin=(10,'K'), Tmax=(269.825,'K')),
            NASAPolynomial(coeffs=[4.02107,0.0201599,-1.27405e-05,3.92475e-09,-4.66328e-13,17838.4,7.89972], Tmin=(269.825,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (148.729,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 726,
    label = "NNCDO",
    molecule = 
"""
1 O u0 p2 c0 {4,D}
2 N u0 p1 c0 {3,S} {4,S} {5,S}
3 N u0 p1 c0 {2,S} {6,S} {7,S}
4 C u0 p0 c0 {1,D} {2,S} {8,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85889,0.0148109,6.67849e-06,-1.43194e-08,5.27714e-12,-10723,8.55539], Tmin=(10,'K'), Tmax=(1028.63,'K')),
            NASAPolynomial(coeffs=[4.01886,0.0203679,-1.04356e-05,2.6123e-09,-2.57298e-13,-11082.8,6.19016], Tmin=(1028.63,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-89.1545,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 727,
    label = "[O-][NH+]DC[NH]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {4,D} {6,S}
3 N u1 p1 c0 {4,S} {7,S}
4 C u0 p0 c0 {2,D} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96814,0.00191999,6.53574e-05,-1.20822e-07,7.0386e-11,14304,8.58941], Tmin=(10,'K'), Tmax=(522.019,'K')),
            NASAPolynomial(coeffs=[1.91694,0.0237999,-1.52212e-05,4.69828e-09,-5.57345e-13,14434.2,16.3476], Tmin=(522.019,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (118.918,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 728,
    label = "CNDNO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {8,S}
2 N u0 p1 c0 {3,D} {4,S}
3 N u0 p1 c0 {1,S} {2,D}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94315,0.00425234,7.1267e-05,-1.47668e-07,9.94462e-11,5839.57,6.96038], Tmin=(10,'K'), Tmax=(380.585,'K')),
            NASAPolynomial(coeffs=[1.84628,0.0262907,-1.5593e-05,4.48391e-09,-5.00257e-13,5999.18,15.0509], Tmin=(380.585,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (48.5442,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 729,
    label = "[O-][NH+]DN[CH]C",
    molecule = 
"""
multiplicity 2
1  O u0 p3 c-1 {2,S}
2  N u0 p0 c+1 {1,S} {3,D} {10,S}
3  N u0 p1 c0 {2,D} {5,S}
4  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5  C u1 p0 c0 {3,S} {4,S} {9,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84648,0.0130126,8.59834e-05,-2.33828e-07,2.02096e-10,18175.2,8.92776], Tmin=(10,'K'), Tmax=(295.52,'K')),
            NASAPolynomial(coeffs=[2.30019,0.0339424,-2.02528e-05,5.83284e-09,-6.50165e-13,18266.6,14.5027], Tmin=(295.52,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (151.112,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 730,
    label = "[O-][NH+]DNN[CH2]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {4,S} {5,S} {6,S}
3 N u0 p0 c+1 {1,S} {4,D} {9,S}
4 N u0 p1 c0 {2,S} {3,D}
5 C u1 p0 c0 {2,S} {7,S} {8,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89871,0.00653799,0.000113335,-2.57481e-07,1.7596e-10,38593.2,9.09934], Tmin=(10,'K'), Tmax=(491.515,'K')),
            NASAPolynomial(coeffs=[3.56076,0.0295779,-1.88969e-05,5.85718e-09,-6.99183e-13,38381.4,7.9966], Tmin=(491.515,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (320.858,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 731,
    label = "[CH2]NDCC",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {3,D} {4,S}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3  C u0 p0 c0 {1,D} {2,S} {8,S}
4  C u1 p0 c0 {1,S} {9,S} {10,S}
5  H u0 p0 c0 {2,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85193,0.0130137,4.12396e-05,-6.90263e-08,3.23843e-11,20727.4,7.0858], Tmin=(10,'K'), Tmax=(675.835,'K')),
            NASAPolynomial(coeffs=[1.52097,0.0335373,-1.92436e-05,5.36546e-09,-5.82557e-13,20888.8,16.2814], Tmin=(675.835,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (172.321,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 732,
    label = "NC#CO",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {7,S}
2 N u0 p1 c0 {3,S} {5,S} {6,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {1,S} {3,T}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88559,0.00824424,9.30457e-05,-2.75411e-07,2.33454e-10,13436.8,7.3639], Tmin=(10,'K'), Tmax=(421.345,'K')),
            NASAPolynomial(coeffs=[5.17335,0.0165638,-9.71247e-06,2.90115e-09,-3.43475e-13,13145.9,0.100127], Tmin=(421.345,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (111.718,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 733,
    label = "NOCO",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {4,S} {9,S}
3 N u0 p1 c0 {1,S} {7,S} {8,S}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8824,0.00980758,5.15171e-05,-1.0237e-07,6.23404e-11,-28050.4,8.60669], Tmin=(10,'K'), Tmax=(426.248,'K')),
            NASAPolynomial(coeffs=[1.80695,0.0292841,-1.70226e-05,4.82876e-09,-5.33414e-13,-27873.5,16.8497], Tmin=(426.248,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-233.24,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 734,
    label = "[O-][NH+]DCCD[CH]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {8,S}
3 C u0 p0 c0 {2,D} {4,S} {6,S}
4 C u0 p0 c0 {3,S} {5,D} {7,S}
5 C u1 p0 c0 {4,D} {9,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93101,0.00413011,9.93556e-05,-1.92838e-07,1.14764e-10,40807.4,9.74582], Tmin=(10,'K'), Tmax=(542.314,'K')),
            NASAPolynomial(coeffs=[2.09927,0.0326947,-2.12903e-05,6.65864e-09,-7.97704e-13,40784.7,15.421], Tmin=(542.314,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (339.266,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 735,
    label = "OONDO",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {4,D}
4 N u0 p1 c0 {1,S} {3,D}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95063,0.00287243,4.96382e-05,-9.98752e-08,5.89487e-11,-3213.79,7.86275], Tmin=(10,'K'), Tmax=(579.497,'K')),
            NASAPolynomial(coeffs=[3.93416,0.0145131,-1.03302e-05,3.439e-09,-4.30196e-13,-3405.43,6.26325], Tmin=(579.497,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-26.7416,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 736,
    label = "OC[C]DN",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {7,S}
2 N u0 p1 c0 {4,D} {8,S}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 C u1 p0 c0 {2,D} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88958,0.00953272,5.78032e-05,-1.45876e-07,1.15613e-10,7214.55,9.03857], Tmin=(10,'K'), Tmax=(323.583,'K')),
            NASAPolynomial(coeffs=[2.61667,0.0252681,-1.51402e-05,4.40806e-09,-4.97468e-13,7296.93,13.7434], Tmin=(323.583,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (59.981,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 737,
    label = "[O-][N+]DCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {6,S}
2 O u0 p3 c-1 {3,S}
3 N u1 p0 c+1 {2,S} {4,D}
4 C u0 p0 c0 {1,S} {3,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95107,0.00304088,6.12127e-05,-1.28646e-07,8.20699e-11,-4170.49,8.78202], Tmin=(10,'K'), Tmax=(517.068,'K')),
            NASAPolynomial(coeffs=[3.35688,0.017894,-1.16294e-05,3.63283e-09,-4.34435e-13,-4246.15,9.93091], Tmin=(517.068,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-34.6908,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 738,
    label = "CDCCD[N]",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {4,D}
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
            NASAPolynomial(coeffs=[3.97563,0.00160515,8.24165e-05,-1.61938e-07,1.04339e-10,34459.2,8.6798], Tmin=(10,'K'), Tmax=(398.288,'K')),
            NASAPolynomial(coeffs=[1.33545,0.0281225,-1.74587e-05,5.24869e-09,-6.09944e-13,34669.5,18.9864], Tmin=(398.288,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (286.507,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 739,
    label = "NNDC",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {6,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.08586,-0.00807036,0.000101779,-1.80629e-07,1.07033e-10,18523.1,6.65169], Tmin=(10,'K'), Tmax=(506.912,'K')),
            NASAPolynomial(coeffs=[1.35865,0.0220657,-1.2892e-05,3.71025e-09,-4.16636e-13,18688.9,16.8641], Tmin=(506.912,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (154.007,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 740,
    label = "NOC[NH]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {7,S} {8,S}
3 N u1 p1 c0 {4,S} {9,S}
4 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87929,0.0103002,5.74412e-05,-1.22832e-07,8.09878e-11,19800.8,9.2488], Tmin=(10,'K'), Tmax=(392.364,'K')),
            NASAPolynomial(coeffs=[1.94608,0.0300087,-1.79045e-05,5.18883e-09,-5.83161e-13,19952.5,16.7668], Tmin=(392.364,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (164.622,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 741,
    label = "NNC[NH]",
    molecule = 
"""
multiplicity 2
1  N u0 p1 c0 {2,S} {4,S} {7,S}
2  N u0 p1 c0 {1,S} {8,S} {9,S}
3  N u1 p1 c0 {4,S} {10,S}
4  C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9506,0.00310252,0.000104397,-2.03463e-07,1.26301e-10,34515.5,9.15158], Tmin=(10,'K'), Tmax=(488.346,'K')),
            NASAPolynomial(coeffs=[1.19195,0.0348446,-2.11951e-05,6.34197e-09,-7.38895e-13,34675.9,19.3666], Tmin=(488.346,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (286.965,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 742,
    label = "[O-][NH+]DNNC",
    molecule = 
"""
1  O u0 p3 c-1 {3,S}
2  N u0 p1 c0 {4,S} {5,S} {9,S}
3  N u0 p0 c+1 {1,S} {4,D} {10,S}
4  N u0 p1 c0 {2,S} {3,D}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  H u0 p0 c0 {5,S}
7  H u0 p0 c0 {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85829,0.0138778,3.88484e-05,-6.35683e-08,2.82112e-11,21879.9,8.27213], Tmin=(10,'K'), Tmax=(749.231,'K')),
            NASAPolynomial(coeffs=[2.12042,0.0329394,-1.89009e-05,5.24566e-09,-5.65764e-13,21865.8,14.3221], Tmin=(749.231,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (181.913,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 743,
    label = "OCNDO",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {7,S}
2 O u0 p2 c0 {3,D}
3 N u0 p1 c0 {2,D} {4,S}
4 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96791,0.00196704,6.76008e-05,-1.27686e-07,7.62501e-11,-13388.3,8.1833], Tmin=(10,'K'), Tmax=(506.887,'K')),
            NASAPolynomial(coeffs=[1.9381,0.0239829,-1.52989e-05,4.68947e-09,-5.52106e-13,-13259.5,15.8367], Tmin=(506.887,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-111.327,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 744,
    label = "CDCDCDN",
    molecule = 
"""
1 N u0 p1 c0 {4,D} {7,S}
2 C u0 p0 c0 {3,D} {5,S} {6,S}
3 C u0 p0 c0 {2,D} {4,D}
4 C u0 p0 c0 {1,D} {3,D}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94468,0.00417436,8.67673e-05,-2.31186e-07,1.94697e-10,40383.4,7.32155], Tmin=(10,'K'), Tmax=(376.772,'K')),
            NASAPolynomial(coeffs=[3.17686,0.0207245,-1.25582e-05,3.72549e-09,-4.29912e-13,40381.6,9.48529], Tmin=(376.772,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (335.773,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 745,
    label = "C[N]OO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {8,S}
3 N u1 p1 c0 {1,S} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71105,0.028359,-5.5119e-05,1.05652e-07,-8.0197e-11,14090.4,7.98441], Tmin=(10,'K'), Tmax=(445.561,'K')),
            NASAPolynomial(coeffs=[3.26273,0.0243246,-1.44056e-05,4.13988e-09,-4.61785e-13,14210.3,10.6826], Tmin=(445.561,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (117.146,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 746,
    label = "[NH-][N+]DCN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {4,S} {6,S} {7,S}
2 N u1 p0 c+1 {3,S} {4,D}
3 N u0 p2 c-1 {2,S} {8,S}
4 C u0 p0 c0 {1,S} {2,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92619,0.00674424,9.90871e-05,-3.11695e-07,3.27194e-10,31526.2,9.40077], Tmin=(10,'K'), Tmax=(241.27,'K')),
            NASAPolynomial(coeffs=[2.81574,0.0251546,-1.5373e-05,4.57985e-09,-5.28241e-13,31579.7,13.1792], Tmin=(241.27,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (262.134,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 747,
    label = "[CH]DNNDN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {4,D}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {2,D} {6,S}
4 C u1 p0 c0 {1,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88628,0.00976076,2.30258e-05,-5.39971e-08,3.31352e-11,66753.5,8.51558], Tmin=(10,'K'), Tmax=(544.952,'K')),
            NASAPolynomial(coeffs=[3.48853,0.017373,-1.08442e-05,3.23959e-09,-3.71683e-13,66727.1,9.55371], Tmin=(544.952,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (555.006,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 748,
    label = "[NH-][N+]DCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {6,S}
2 N u1 p0 c+1 {3,S} {4,D}
3 N u0 p2 c-1 {2,S} {7,S}
4 C u0 p0 c0 {1,S} {2,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97249,0.0016052,6.33987e-05,-1.10388e-07,6.04383e-11,10199.6,8.44105], Tmin=(10,'K'), Tmax=(542.609,'K')),
            NASAPolynomial(coeffs=[1.3402,0.0259228,-1.74069e-05,5.57918e-09,-6.80134e-13,10412.9,18.8646], Tmin=(542.609,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (84.7925,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 749,
    label = "O[CH]CDN",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {3,S} {7,S}
2 N u0 p1 c0 {4,D} {8,S}
3 C u1 p0 c0 {1,S} {4,S} {5,S}
4 C u0 p0 c0 {2,D} {3,S} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0728,-0.00712801,0.000123731,-2.2165e-07,1.27989e-10,-2051.86,8.9063], Tmin=(10,'K'), Tmax=(549.278,'K')),
            NASAPolynomial(coeffs=[1.58965,0.0277454,-1.73552e-05,5.24042e-09,-6.07876e-13,-2032.36,17.0926], Tmin=(549.278,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-17.0723,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 750,
    label = "C[N]ON",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 N u0 p1 c0 {1,S} {8,S} {9,S}
3 N u1 p1 c0 {1,S} {4,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.7041,0.0300833,-7.07669e-05,1.619e-07,-1.32555e-10,26007.4,7.99555], Tmin=(10,'K'), Tmax=(439.715,'K')),
            NASAPolynomial(coeffs=[2.26725,0.0286594,-1.64637e-05,4.6023e-09,-5.01324e-13,26273.9,15.3404], Tmin=(439.715,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (216.231,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 751,
    label = "NDCC#C",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {5,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {7,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94994,0.00309898,7.03564e-05,-1.43662e-07,9.03295e-11,37511,7.71128], Tmin=(10,'K'), Tmax=(515.966,'K')),
            NASAPolynomial(coeffs=[2.97099,0.0212641,-1.31984e-05,4.02285e-09,-4.7627e-13,37471.3,10.4222], Tmin=(515.966,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (311.868,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 752,
    label = "OCNDN",
    molecule = 
"""
1 O u0 p2 c0 {4,S} {7,S}
2 N u0 p1 c0 {3,D} {4,S}
3 N u0 p1 c0 {2,D} {8,S}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.975,0.00156306,7.55149e-05,-1.38928e-07,8.31983e-11,1200.67,8.16782], Tmin=(10,'K'), Tmax=(430.397,'K')),
            NASAPolynomial(coeffs=[1.10582,0.0282443,-1.75283e-05,5.27735e-09,-6.14181e-13,1447.5,19.5894], Tmin=(430.397,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (9.97525,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 753,
    label = "NCND[CH]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {7,S} {8,S}
2 N u0 p1 c0 {3,S} {4,D}
3 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4 C u1 p0 c0 {2,D} {9,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86919,0.0110254,4.46608e-05,-8.73648e-08,5.11112e-11,33361.2,9.00765], Tmin=(10,'K'), Tmax=(446.293,'K')),
            NASAPolynomial(coeffs=[1.82053,0.0293872,-1.70544e-05,4.82574e-09,-5.31819e-13,33544.1,17.2384], Tmin=(446.293,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (277.365,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 754,
    label = "CNND[N]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {4,S} {8,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u1 p1 c0 {2,D}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91705,0.00643806,6.95625e-05,-1.66466e-07,1.29664e-10,36892.9,7.77295], Tmin=(10,'K'), Tmax=(327.453,'K')),
            NASAPolynomial(coeffs=[2.42144,0.0247078,-1.41288e-05,3.92433e-09,-4.24623e-13,36990.9,13.3187], Tmin=(327.453,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (306.735,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 755,
    label = "[O-][N+]DCN",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {3,S}
2 N u0 p1 c0 {4,S} {6,S} {7,S}
3 N u1 p0 c+1 {1,S} {4,D}
4 C u0 p0 c0 {2,S} {3,D} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94132,0.00368681,7.48818e-05,-1.59143e-07,1.03109e-10,17130.1,8.83548], Tmin=(10,'K'), Tmax=(507.763,'K')),
            NASAPolynomial(coeffs=[3.21491,0.0215431,-1.37131e-05,4.24027e-09,-5.04692e-13,17047.5,10.3074], Tmin=(507.763,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (142.411,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 756,
    label = "OONDN",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {5,S}
3 N u0 p1 c0 {1,S} {4,D}
4 N u0 p1 c0 {3,D} {6,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95724,0.00243489,5.60931e-05,-1.03364e-07,5.74856e-11,15390.8,7.81915], Tmin=(10,'K'), Tmax=(589.311,'K')),
            NASAPolynomial(coeffs=[2.89745,0.0197064,-1.35209e-05,4.40756e-09,-5.44323e-13,15340.7,10.8868], Tmin=(589.311,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (127.947,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 757,
    label = "CNND[CH]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {8,S}
2 N u0 p1 c0 {1,S} {4,D}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 C u1 p0 c0 {2,D} {9,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87815,0.00943565,5.88654e-05,-1.2549e-07,8.379e-11,42942.3,7.72081], Tmin=(10,'K'), Tmax=(385.651,'K')),
            NASAPolynomial(coeffs=[2.01408,0.0287701,-1.63373e-05,4.5125e-09,-4.8589e-13,43086.1,14.9377], Tmin=(385.651,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (357.021,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 758,
    label = "[CH2]C#CN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {4,S} {7,S} {8,S}
2 C u1 p0 c0 {3,S} {5,S} {6,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {1,S} {3,T}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85517,0.0116383,0.000122317,-4.32258e-07,4.3671e-10,42324.2,7.62378], Tmin=(10,'K'), Tmax=(353.999,'K')),
            NASAPolynomial(coeffs=[5.12128,0.020299,-1.17001e-05,3.40285e-09,-3.91953e-13,42090.6,0.797746], Tmin=(353.999,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (351.923,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 759,
    label = "NOCN",
    molecule = 
"""
1  O u0 p2 c0 {3,S} {4,S}
2  N u0 p1 c0 {4,S} {7,S} {8,S}
3  N u0 p1 c0 {1,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5  H u0 p0 c0 {4,S}
6  H u0 p0 c0 {4,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88521,0.00901744,7.0339e-05,-1.44468e-07,9.40559e-11,-5694.98,8.65676], Tmin=(10,'K'), Tmax=(395.184,'K')),
            NASAPolynomial(coeffs=[1.57791,0.0323718,-1.83082e-05,5.07902e-09,-5.51073e-13,-5512.62,17.646], Tmin=(395.184,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-47.37,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 760,
    label = "N[CH]OO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {8,S}
3 N u0 p1 c0 {4,S} {6,S} {7,S}
4 C u1 p0 c0 {1,S} {3,S} {5,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86409,0.0113027,0.000111799,-3.86888e-07,3.9152e-10,-24569.9,9.66817], Tmin=(10,'K'), Tmax=(342.712,'K')),
            NASAPolynomial(coeffs=[4.34154,0.0229033,-1.41399e-05,4.31037e-09,-5.09967e-13,-24703.5,6.40468], Tmin=(342.712,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-204.266,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 761,
    label = "CND[N]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {3,S}
2 N u1 p1 c0 {1,D}
3 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93846,0.00623346,1.31708e-05,-1.75541e-08,6.18762e-12,26783.3,6.17083], Tmin=(10,'K'), Tmax=(952.832,'K')),
            NASAPolynomial(coeffs=[2.78857,0.015384,-8.04051e-06,2.04881e-09,-2.05123e-13,26806.2,10.633], Tmin=(952.832,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (222.691,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 762,
    label = "NC#CN",
    molecule = 
"""
1 N u0 p1 c0 {3,S} {5,S} {6,S}
2 N u0 p1 c0 {4,S} {7,S} {8,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {2,S} {3,T}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88542,0.00806253,0.000103625,-2.86912e-07,2.32122e-10,31248.8,6.80652], Tmin=(10,'K'), Tmax=(434.458,'K')),
            NASAPolynomial(coeffs=[4.93657,0.0198714,-1.13307e-05,3.31904e-09,-3.88686e-13,30954.7,0.277841], Tmin=(434.458,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (259.81,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 763,
    label = "OO[CH]NDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 O u0 p2 c0 {1,S} {7,S}
3 O u0 p2 c0 {4,D}
4 N u0 p1 c0 {3,D} {5,S}
5 C u1 p0 c0 {1,S} {4,S} {6,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89259,0.00761626,9.15946e-05,-2.3892e-07,1.83443e-10,10007.7,10.0202], Tmin=(10,'K'), Tmax=(443.712,'K')),
            NASAPolynomial(coeffs=[3.98382,0.0230778,-1.57236e-05,5.03294e-09,-6.08971e-13,9839.34,7.8478], Tmin=(443.712,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (83.1997,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 764,
    label = "[N]DCDCDO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 N u1 p1 c0 {3,D}
3 C u0 p0 c0 {2,D} {4,D}
4 C u0 p0 c0 {1,D} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92436,0.0059769,4.99904e-05,-1.86601e-07,1.88078e-10,24244.1,7.68122], Tmin=(10,'K'), Tmax=(367.801,'K')),
            NASAPolynomial(coeffs=[4.90305,0.00736056,-4.7036e-06,1.44503e-09,-1.71835e-13,24090.8,2.83259], Tmin=(367.801,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (201.585,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 765,
    label = "[O-][NH+]DNC[NH]",
    molecule = 
"""
multiplicity 2
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {8,S}
3 N u0 p1 c0 {2,D} {5,S}
4 N u1 p1 c0 {5,S} {9,S}
5 C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85929,0.0167115,2.13314e-05,-3.91028e-08,1.6542e-11,37057.7,10.0932], Tmin=(10,'K'), Tmax=(852.77,'K')),
            NASAPolynomial(coeffs=[3.96438,0.0268755,-1.5292e-05,4.18246e-09,-4.43752e-13,36652.3,7.3309], Tmin=(852.77,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (308.125,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 766,
    label = "CDNC#[C]",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {3,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u1 p0 c0 {3,T}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93902,0.00662117,0.000138546,-7.55484e-07,1.27651e-09,76384.6,7.71522], Tmin=(10,'K'), Tmax=(200.907,'K')),
            NASAPolynomial(coeffs=[4.03194,0.0155876,-9.15614e-06,2.6079e-09,-2.8909e-13,76359.1,6.8728], Tmin=(200.907,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (635.161,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 767,
    label = "[CH2]NCDN",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {3,S} {4,S} {5,S}
2 N u0 p1 c0 {3,D} {9,S}
3 C u0 p0 c0 {1,S} {2,D} {6,S}
4 C u1 p0 c0 {1,S} {7,S} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93022,0.00531363,0.000117753,-3.11355e-07,2.62764e-10,23976.7,8.2369], Tmin=(10,'K'), Tmax=(369.933,'K')),
            NASAPolynomial(coeffs=[2.70537,0.0285792,-1.72189e-05,5.11046e-09,-5.90544e-13,23998.7,12.0013], Tmin=(369.933,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (199.362,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 768,
    label = "CNDNN",
    molecule = 
"""
1 N u0 p1 c0 {3,S} {8,S} {9,S}
2 N u0 p1 c0 {3,D} {4,S}
3 N u0 p1 c0 {1,S} {2,D}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95999,0.0028487,9.94532e-05,-2.22506e-07,1.65862e-10,23761.7,6.95652], Tmin=(10,'K'), Tmax=(341.56,'K')),
            NASAPolynomial(coeffs=[1.69529,0.0293706,-1.70213e-05,4.83258e-09,-5.36227e-13,23916.4,15.4496], Tmin=(341.56,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (197.563,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 769,
    label = "NNCDN",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {7,S} {8,S}
3 N u0 p1 c0 {4,D} {9,S}
4 C u0 p0 c0 {1,S} {3,D} {6,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97412,0.00181953,9.96996e-05,-2.12467e-07,1.50436e-10,17161.3,8.34059], Tmin=(10,'K'), Tmax=(360.927,'K')),
            NASAPolynomial(coeffs=[1.42242,0.0301313,-1.8098e-05,5.36508e-09,-6.20694e-13,17345.3,18.0477], Tmin=(360.927,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (142.69,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

entry(
    index = 770,
    label = "NO[N]N",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 N u0 p1 c0 {4,S} {7,S} {8,S}
4 N u1 p1 c0 {1,S} {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9271,0.00722625,0.000139447,-5.61648e-07,7.35483e-10,34778.9,8.97162], Tmin=(10,'K'), Tmax=(237.651,'K')),
            NASAPolynomial(coeffs=[3.37218,0.0241099,-1.47327e-05,4.42996e-09,-5.17528e-13,34784,10.4032], Tmin=(237.651,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (289.185,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'AUTOTST Thermojob RRHO/G4 calculation with bond corrections.',
    referenceType = "Theory",
    shortDesc = """RRHO/G4 with BACs""",
    longDesc = 
"""

""",
    rank = 5,
)

