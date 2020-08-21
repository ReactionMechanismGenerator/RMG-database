#!/usr/bin/env python
# encoding: utf-8

name = "ecp_1"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "C3H8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.47254,0.000383515,6.89408e-05,-8.75121e-08,3.42355e-11,-14508.1,4.49314], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.45188,0.0305567,-1.45573e-05,3.37884e-09,-3.09956e-13,-14555,15.2744], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1,
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
            NASAPolynomial(coeffs=[4.6189,0.00290963,5.43185e-05,-7.1442e-08,2.84068e-11,10273,5.84564], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.67722,0.0257288,-1.21308e-05,2.79068e-09,-2.54082e-13,10128.9,12.0848], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2,
    label = "C3H7(1)",
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
            NASAPolynomial(coeffs=[7.3912,-0.0180422,9.9681e-05,-1.1251e-07,4.20119e-11,8511.91,-4.94295], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.22767,0.0278281,-1.33544e-05,3.11809e-09,-2.8741e-13,8971.63,20.3128], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 3,
    label = "C3H6",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.20332,0.000485313,5.38783e-05,-6.80258e-08,2.64401e-11,700.811,6.02875], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.84407,0.0242848,-1.16003e-05,2.70124e-09,-2.4864e-13,642.471,14.3621], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 4,
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72403,-0.00223846,6.7333e-06,-5.74135e-09,1.63151e-12,-1114.94,3.84129], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.88191,0.00215104,-1.21178e-06,3.20432e-10,-3.25655e-14,-1001.85,7.63687], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 5,
    label = "C3H7O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.82137,0.000225504,7.08813e-05,-9.13711e-08,3.58944e-11,-7782.38,-5.5291], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.20281,0.0280695,-1.38059e-05,3.29464e-09,-3.09514e-13,-8282.39,-2.35317], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 6,
    label = "C3H7O2(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u1 p0 c0 {1,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {4,S} {12,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.07262,0.0427087,9.18167e-06,-6.31073e-08,3.43807e-11,413.776,15.9742], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.1273,0.0136252,-5.5185e-06,1.08705e-09,-8.47274e-14,-3354.61,-57.4603], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 7,
    label = "C3H7O4",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
6  O u0 p2 c0 {5,S} {7,S}
7  O u0 p2 c0 {6,S} {14,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.16283,0.0125647,7.64724e-05,-1.10052e-07,4.37575e-11,-17908.6,1.65289], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.9949,0.0289398,-1.56971e-05,4.07914e-09,-4.1165e-13,-20904,-35.9254], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 8,
    label = "C3H6O3",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  O u0 p2 c0 {4,S} {6,S}
6  O u0 p2 c0 {5,S} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.85803,0.0145769,5.53901e-05,-8.24309e-08,3.28878e-11,-34640.9,5.85496], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.30713,0.0300621,-1.72433e-05,4.63323e-09,-4.77267e-13,-36714.5,-17.8192], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 9,
    label = "C3H7O2(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {1,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.2886,0.0103361,5.00642e-05,-7.17807e-08,2.90503e-11,-9612.86,-0.45652], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.1452,0.0291737,-1.453e-05,3.50101e-09,-3.314e-13,-10300.9,-3.75496], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 10,
    label = "C3H8O2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {2,S} {5,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.22125,0.0133537,7.21225e-05,-1.17502e-07,5.21994e-11,-24494.7,5.45006], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.7247,0.0243908,-1.08878e-05,2.37245e-09,-2.05105e-13,-26334.3,-22.0476], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 11,
    label = "C3H8O2(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  O u0 p2 c0 {1,S} {5,S}
5  O u0 p2 c0 {4,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.08321,0.0161128,6.03847e-05,-9.80487e-08,4.24812e-11,-26207.8,4.41109], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.3144,0.02666,-1.26102e-05,2.91619e-09,-2.67199e-13,-28072.5,-21.8345], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 12,
    label = "C4H10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.6446,-0.00407889,0.000100814,-1.25729e-07,4.89367e-11,-17604.2,-2.854], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.52365,0.0389748,-1.89813e-05,4.48813e-09,-4.18168e-13,-17761.7,11.3893], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 13,
    label = "C4H9",
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
            NASAPolynomial(coeffs=[6.14971,0.00182057,8.04803e-05,-1.0535e-07,4.18865e-11,7255.14,1.1961], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.79783,0.0343097,-1.66964e-05,3.94247e-09,-3.6679e-13,6882.15,7.67393], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 14,
    label = "C4H9(1)",
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
            NASAPolynomial(coeffs=[8.33573,-0.0148438,0.000114704,-1.34912e-07,5.13258e-11,5654.08,-6.82737], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.23237,0.0362917,-1.77093e-05,4.18446e-09,-3.8917e-13,5896.41,16.9677], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 15,
    label = "C4H8",
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
            NASAPolynomial(coeffs=[4.87591,0.00487665,6.67773e-05,-8.86754e-08,3.52134e-11,-2054.35,5.40806], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.78326,0.0328263,-1.59458e-05,3.75181e-09,-3.47731e-13,-2356.75,11.3567], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 16,
    label = "C4H8(1)",
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
            NASAPolynomial(coeffs=[5.99566,0.000750235,6.77012e-05,-8.30114e-08,3.14703e-11,-3661.32,-1.20993], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.08893,0.0335851,-1.62306e-05,3.81676e-09,-3.54217e-13,-3536.91,13.9212], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 17,
    label = "C4H9O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u0 p2 c0 {3,S} {15,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.04695,0.00625326,7.26818e-05,-9.8149e-08,3.92598e-11,-10850,-9.69119], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.70363,0.0344794,-1.66343e-05,3.90613e-09,-3.62082e-13,-11437.2,-8.0929], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 18,
    label = "C4H9O2(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
5  O u0 p2 c0 {1,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 O u1 p2 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.9224,0.00828274,7.86813e-05,-1.09336e-07,4.42517e-11,-12672.2,-4.88601], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.98631,0.0355332,-1.75132e-05,4.19079e-09,-3.94833e-13,-13748.9,-11.1612], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 19,
    label = "C4H9O2(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {3,S} {14,S}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.50167,0.0491353,-2.74623e-06,-4.3927e-08,2.49833e-11,-4065.58,15.5208], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.07,0.0245813,-1.08567e-05,2.35638e-09,-2.03944e-13,-7186.84,-44.9123], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 20,
    label = "C4H9O2(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u1 p0 c0 {2,S} {13,S} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.04588,0.0544013,-4.70921e-06,-4.97959e-08,2.92098e-11,-4356.53,16.8905], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.2853,0.0250709,-1.15932e-05,2.62495e-09,-2.36061e-13,-7852.13,-51.904], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 21,
    label = "C4H9O4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {7,S}
6  O u0 p2 c0 {1,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.96254,0.0156544,8.81902e-05,-1.26449e-07,5.04582e-11,-23103.1,-0.468181], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.0453,0.0406152,-2.19453e-05,5.66925e-09,-5.68519e-13,-25778.7,-29.8468], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 22,
    label = "C4H9O4(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {1,S} {7,S}
6  O u0 p2 c0 {3,S} {16,S}
7  O u0 p2 c0 {5,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.55005,0.0108736,0.000103481,-1.45322e-07,5.81608e-11,-22854.7,-2.87364], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.3612,0.0377059,-1.98606e-05,5.03502e-09,-4.97958e-13,-25825.6,-36.7235], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 23,
    label = "C4H8O3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,D} {14,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.11989,0.0243,4.99009e-05,-8.11514e-08,3.29906e-11,-39636,5.43375], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.87796,0.0384835,-2.11629e-05,5.51755e-09,-5.56081e-13,-41755.8,-19.6806], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 24,
    label = "C4H8O3(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {14,D}
5  O u0 p2 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {15,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 O u0 p2 c0 {4,D}
15 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.97383,0.029335,2.38522e-05,-5.04497e-08,2.21084e-11,-41668,5.83121], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.95511,0.0418634,-2.18963e-05,5.417e-09,-5.196e-13,-42105.1,3.34108], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 25,
    label = "C4H10O2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  O u0 p2 c0 {3,S} {6,S}
6  O u0 p2 c0 {5,S} {16,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.1533,0.0237905,5.68253e-05,-1.02161e-07,4.63316e-11,-27503.6,3.00305], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.2179,0.0325089,-1.47756e-05,3.27701e-09,-2.8815e-13,-29095.9,-21.4831], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 26,
    label = "C4H10O2(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
5  O u0 p2 c0 {1,S} {6,S}
6  O u0 p2 c0 {5,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.00822,0.0221845,6.03372e-05,-1.01624e-07,4.44355e-11,-29055.5,2.34824], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.80674,0.0341635,-1.59323e-05,3.6321e-09,-3.28281e-13,-30781.6,-21.6295], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 27,
    label = "C5H12",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.54843,-0.00998236,0.000131433,-1.60006e-07,6.15724e-11,-20840.4,-13.9244], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.86719,0.0466445,-2.28811e-05,5.44505e-09,-5.10148e-13,-20980.8,6.22063], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 28,
    label = "C5H11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u1 p0 c0 {3,S} {15,S} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.13477,0.00722014,8.88561e-05,-1.21569e-07,4.92358e-11,4192.18,-1.04321], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.71432,0.0406249,-1.96568e-05,4.62442e-09,-4.29193e-13,3465.82,-0.0276754], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 29,
    label = "C5H11(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {2,S} {4,S} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.35371,-0.00685101,0.000120994,-1.49882e-07,5.81111e-11,2670.13,-5.24195], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.81026,0.0439827,-2.18081e-05,5.23423e-09,-4.9377e-13,2339.19,9.65601], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 30,
    label = "C5H11(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {1,S} {2,S} {16,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.8691,-0.00946296,0.000125199,-1.53111e-07,5.91625e-11,2750.67,-6.81204], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.36035,0.0445274,-2.19857e-05,5.24635e-09,-4.91955e-13,2667.33,12.9708], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 31,
    label = "C5H10",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {4,D} {14,S} {15,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.68101,0.0130776,6.67283e-05,-9.43187e-08,3.79808e-11,-5232.42,3.30048], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.83233,0.0395651,-1.94535e-05,4.64113e-09,-4.3593e-13,-5956.8,2.38396], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 32,
    label = "C5H10(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {5,D} {15,S}
5  C u0 p0 c0 {3,S} {4,D} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.54242,0.00759147,7.30783e-05,-9.51131e-08,3.6893e-11,-6450.19,-1.01893], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.18661,0.0419054,-2.05122e-05,4.86692e-09,-4.5466e-13,-6579.99,10.6537], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 33,
    label = "C5H11O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  O u0 p2 c0 {4,S} {18,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.3942,0.00409993,8.85653e-05,-1.14147e-07,4.46007e-11,-14021.3,-17.2895], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.95981,0.0427427,-2.05578e-05,4.81368e-09,-4.45062e-13,-14264.9,-6.03909], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 34,
    label = "C5H11O2(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {12,S} {13,S} {14,S}
6  O u0 p2 c0 {1,S} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.64363,0.0219559,5.66419e-05,-8.97773e-08,3.77429e-11,-15774.2,-7.95788], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.45817,0.0413094,-1.97332e-05,4.5958e-09,-4.2314e-13,-16767.2,-16.6666], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 35,
    label = "C5H11O2(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  O u0 p2 c0 {1,S} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 O u1 p2 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.68494,0.0280932,4.21766e-05,-7.52018e-08,3.24347e-11,-15761.9,-4.36276], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.41338,0.041346,-1.97466e-05,4.59806e-09,-4.23265e-13,-16854.1,-16.979], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 36,
    label = "C5H11O2(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {1,S} {2,S} {17,S}
6  O u0 p2 c0 {3,S} {7,S}
7  O u0 p2 c0 {6,S} {18,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.20304,0.0186793,9.07486e-05,-1.43158e-07,6.17489e-11,-7503.33,-1.36968], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.4674,0.0361557,-1.69256e-05,3.87569e-09,-3.51869e-13,-9952.92,-34.8603], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 37,
    label = "C5H11O2(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {2,S} {4,S} {17,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.46429,0.0430589,3.96757e-05,-9.89585e-08,4.78704e-11,-8963.35,9.06031], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.4874,0.0341983,-1.58446e-05,3.59305e-09,-3.2332e-13,-12048.5,-45.6914], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 38,
    label = "C5H11O2(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u1 p0 c0 {3,S} {16,S} {17,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.34968,0.0595489,-2.9975e-05,-8.69577e-09,1.02665e-11,-7717.2,8.76963], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.472,0.0364064,-1.68561e-05,3.81439e-09,-3.424e-13,-9647.03,-32.2723], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 39,
    label = "C5H11O4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {4,S} {8,S}
7  O u0 p2 c0 {1,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.16658,0.0141813,0.000116763,-1.65772e-07,6.70337e-11,-26220.7,-4.06088], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.116,0.0475439,-2.49728e-05,6.30614e-09,-6.21111e-13,-29094.8,-34.2831], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 40,
    label = "C5H11O4(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {2,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.11421,0.0221492,9.83636e-05,-1.46923e-07,6.00639e-11,-28072.9,-0.894638], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.8637,0.0487771,-2.57571e-05,6.52873e-09,-6.44709e-13,-30984,-34.2437], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 41,
    label = "C5H11O4(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {4,S} {19,S}
8  O u0 p2 c0 {6,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.4097,0.0181236,0.000101249,-1.46846e-07,5.93582e-11,-26110.6,-5.81264], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.9276,0.0456129,-2.35373e-05,5.86221e-09,-5.71387e-13,-28969,-38.0378], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 42,
    label = "C5H11O4(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  C u1 p0 c0 {3,S} {7,S} {18,S}
6  O u0 p2 c0 {1,S} {8,S}
7  O u0 p2 c0 {5,S} {9,S}
8  O u0 p2 c0 {6,S} {20,S}
9  O u0 p2 c0 {7,S} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.67497,0.0457883,4.17618e-05,-9.57466e-08,4.38163e-11,-56399,8.25357], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.4731,0.044875,-2.33069e-05,5.82113e-09,-5.67658e-13,-59566.1,-41.8341], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 43,
    label = "C5H10O3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,D} {17,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u0 p2 c0 {5,D}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.68292,0.0262271,6.20443e-05,-9.81265e-08,3.99497e-11,-42971.7,-0.267668], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.8379,0.0458404,-2.45511e-05,6.27279e-09,-6.22411e-13,-45053.5,-23.0338], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 44,
    label = "C5H10O3(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {4,S} {17,D}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {18,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u0 p2 c0 {5,D}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.59325,0.0349773,2.99643e-05,-6.11867e-08,2.6403e-11,-46937.5,3.8261], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.31782,0.049057,-2.5229e-05,6.19947e-09,-5.94119e-13,-47751.2,-3.37483], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 45,
    label = "C5H10O3(2)",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {2,S} {17,D}
6  O u0 p2 c0 {3,S} {7,S}
7  O u0 p2 c0 {6,S} {18,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 O u0 p2 c0 {5,D}
18 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.24653,0.0497311,-1.42991e-05,-1.17855e-08,7.44152e-12,-45317.8,9.08474], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.16578,0.0487143,-2.51574e-05,6.20934e-09,-5.97461e-13,-46000.2,-1.71558], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 46,
    label = "C5H12O2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {4,S} {7,S}
7  O u0 p2 c0 {6,S} {19,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.80153,0.015523,8.97597e-05,-1.3568e-07,5.79396e-11,-30713.5,-5.66922], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.90378,0.0418918,-1.94702e-05,4.4149e-09,-3.96517e-13,-31946.7,-17.1514], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 47,
    label = "C5H12O2(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {19,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.42154,0.0344033,4.70883e-05,-9.37377e-08,4.28071e-11,-32253.8,1.39928], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.882,0.0413195,-1.91702e-05,4.34066e-09,-3.89417e-13,-33966.5,-25.0933], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 48,
    label = "C5H12O2(2)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  O u0 p2 c0 {1,S} {7,S}
7  O u0 p2 c0 {6,S} {19,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.21272,0.0287208,5.77029e-05,-1.01127e-07,4.44134e-11,-32436.8,-2.3075], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.5582,0.0418427,-1.9525e-05,4.44848e-09,-4.01548e-13,-34031.5,-23.9134], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 49,
    label = "C6H14",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
6  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.6354,-0.0148675,0.000166118,-2.04436e-07,7.9706e-11,-23938.3,-20.467], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.64788,0.0523622,-2.52167e-05,5.90979e-09,-5.46737e-13,-24323.1,-0.720671], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 50,
    label = "C6H13",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u1 p0 c0 {4,S} {18,S} {19,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.712,0.00105148,0.000123102,-1.62245e-07,6.50047e-11,1045.95,-9.49928], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.28006,0.0472266,-2.27068e-05,5.31641e-09,-4.91581e-13,202.018,-5.45069], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 51,
    label = "C6H13(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
6  C u1 p0 c0 {3,S} {5,S} {19,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.05768,2.23605e-05,0.000125949,-1.63396e-07,6.47878e-11,-354.622,-6.89063], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.77311,0.0496516,-2.41992e-05,5.72996e-09,-5.34746e-13,-1052.29,1.19853], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 52,
    label = "C6H13(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  C u1 p0 c0 {2,S} {3,S} {19,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.67448,0.041477,-9.66208e-06,-1.88931e-09,-3.46968e-13,-124.202,-1.48761], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.05754,0.0486738,-2.3488e-05,5.52272e-09,-5.12905e-13,-316.819,0.0611222], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 53,
    label = "C6H12",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {6,D} {16,S}
6  C u0 p0 c0 {5,D} {17,S} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.18145,0.0297351,4.40629e-05,-7.83453e-08,3.38461e-11,-8106.4,6.00056], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.16862,0.0454385,-2.17214e-05,5.06049e-09,-4.65976e-13,-9006.22,-2.85379], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 54,
    label = "C6H12(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {6,D} {18,S}
6  C u0 p0 c0 {4,S} {5,D} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.91756,0.0108824,8.67386e-05,-1.17095e-07,4.64173e-11,-9682.94,-6.09409], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.63852,0.0471844,-2.28432e-05,5.38164e-09,-5.00322e-13,-10263.2,-0.958193], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 55,
    label = "C6H12(2)",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {6,D} {17,S}
6  C u0 p0 c0 {2,S} {5,D} {18,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.37872,0.0108071,8.92671e-05,-1.20156e-07,4.75393e-11,-9274.41,-2.92277], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.98142,0.0484101,-2.36404e-05,5.60937e-09,-5.24594e-13,-9871.43,2.58202], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 56,
    label = "C6H13O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  O u0 p2 c0 {5,S} {21,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.162,-0.0057859,0.000126798,-1.54338e-07,5.90267e-11,-17203.6,-26.9637], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.748,0.0517404,-2.49297e-05,5.84507e-09,-5.40953e-13,-17109,-2.82198], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 57,
    label = "C6H13O2(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
7  O u0 p2 c0 {1,S} {21,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.4651,0.0162048,7.83222e-05,-1.08832e-07,4.33722e-11,-18979.9,-18.1438], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.13321,0.0504675,-2.41992e-05,5.65285e-09,-5.21688e-13,-19447.9,-12.2259], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 58,
    label = "C6H13O2(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
7  O u0 p2 c0 {1,S} {21,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.01956,0.0424387,1.80653e-05,-5.13217e-08,2.352e-11,-18793.9,-5.16064], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.0948,0.0490729,-2.33771e-05,5.43002e-09,-4.98724e-13,-19756.2,-18.3214], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 59,
    label = "C6H13O2(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
6  C u1 p0 c0 {2,S} {3,S} {20,S}
7  O u0 p2 c0 {4,S} {8,S}
8  O u0 p2 c0 {7,S} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.93459,0.0278856,4.36833e-05,-6.73004e-08,2.62967e-11,-11114.4,-9.22279], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.2956,0.0520217,-2.52074e-05,5.94282e-09,-5.52906e-13,-11520.8,-5.29377], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 60,
    label = "C6H13O2(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  C u1 p0 c0 {2,S} {3,S} {20,S}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {7,S} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.1995,0.0112804,9.92449e-05,-1.36333e-07,5.49063e-11,-12492.3,-17.3113], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.79987,0.0488385,-2.32351e-05,5.38919e-09,-4.94301e-13,-13395.5,-17.3517], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 61,
    label = "C6H13O2(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
6  C u1 p0 c0 {3,S} {5,S} {20,S}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {7,S} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.00068,0.047004,1.8384e-05,-6.12218e-08,2.97196e-11,-12398.2,-0.579225], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.7467,0.0465374,-2.20096e-05,5.07498e-09,-4.63003e-13,-13984.1,-27.2532], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 62,
    label = "C6H13O2(6)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u1 p0 c0 {4,S} {19,S} {20,S}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {7,S} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.20928,0.0697597,-4.48899e-05,6.60583e-09,4.29006e-12,-10774.4,5.9214], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.8172,0.0446496,-2.07954e-05,4.72996e-09,-4.26417e-13,-12446.5,-31.7649], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 63,
    label = "C6H13O4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {5,S} {9,S}
8  O u0 p2 c0 {1,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.57407,0.0211691,0.000121943,-1.85471e-07,7.86747e-11,-28984.6,-4.34896], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.2875,0.0511177,-2.48379e-05,5.86883e-09,-5.47044e-13,-31736.2,-37.4409], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 64,
    label = "C6H13O4(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {10,S}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
7  O u0 p2 c0 {2,S} {9,S}
8  O u0 p2 c0 {1,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.47126,0.0309303,9.543e-05,-1.50513e-07,6.28865e-11,-31217.9,-1.64565], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.2795,0.0566744,-2.9356e-05,7.32024e-09,-7.13213e-13,-34041.3,-34.9222], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 65,
    label = "C6H13O4(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {10,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {2,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.37771,0.0268529,0.000108977,-1.65482e-07,6.84204e-11,-30970.3,-0.377275], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.1887,0.0567314,-2.93958e-05,7.33697e-09,-7.15652e-13,-33973.9,-34.6251], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 66,
    label = "C6H13O4(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {8,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {5,S} {22,S}
9  O u0 p2 c0 {7,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.9426,0.0102798,0.000137828,-1.88591e-07,7.5324e-11,-29057,-14.7907], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.1211,0.0542529,-2.78082e-05,6.88611e-09,-6.67824e-13,-31680.7,-37.1546], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 67,
    label = "C6H13O4(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {6,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
6  C u1 p0 c0 {4,S} {8,S} {21,S}
7  O u0 p2 c0 {1,S} {9,S}
8  O u0 p2 c0 {6,S} {10,S}
9  O u0 p2 c0 {7,S} {23,S}
10 O u0 p2 c0 {8,S} {22,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.47631,0.0388903,5.64531e-05,-1.0297e-07,4.45755e-11,-60306.1,-5.59889], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.0427,0.057352,-2.95894e-05,7.32899e-09,-7.08775e-13,-61940.3,-24.2123], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 68,
    label = "C6H13O4(7)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u1 p0 c0 {2,S} {3,S} {8,S}
7  O u0 p2 c0 {4,S} {9,S}
8  O u0 p2 c0 {6,S} {10,S}
9  O u0 p2 c0 {7,S} {22,S}
10 O u0 p2 c0 {8,S} {23,S}
11 H u0 p0 c0 {1,S}
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
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.70356,0.0302822,8.05908e-05,-1.29342e-07,5.42043e-11,-51657.8,-10.613], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.2389,0.0514161,-2.59794e-05,6.37868e-09,-6.15576e-13,-54202.9,-41.326], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 69,
    label = "C6H12O3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,D} {20,S}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {7,S} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u0 p2 c0 {6,D}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.36878,0.0276161,7.23427e-05,-1.10629e-07,4.45788e-11,-46095.2,-6.07505], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.3098,0.0538763,-2.83547e-05,7.14859e-09,-7.02096e-13,-47988.6,-23.3331], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 70,
    label = "C6H12O3(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {5,S} {20,D}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {7,S} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.26549,0.0351085,4.49466e-05,-7.94554e-08,3.33904e-11,-50290,-2.24455], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.70625,0.057234,-2.90937e-05,7.08266e-09,-6.73592e-13,-50935.1,-3.81684], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 71,
    label = "C6H12O3(2)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {2,S} {3,S} {20,D}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {7,S} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.11163,0.0617402,-2.24746e-05,-9.80518e-09,7.78302e-12,-50263.3,10.0845], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.18179,0.0566128,-2.87874e-05,7.01627e-09,-6.68301e-13,-51180.5,-6.33384], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 72,
    label = "C6H12O3(3)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {3,S} {20,D}
7  O u0 p2 c0 {4,S} {8,S}
8  O u0 p2 c0 {7,S} {21,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 O u0 p2 c0 {6,D}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.91586,0.030162,6.01712e-05,-9.5642e-08,3.91839e-11,-48570,0.779514], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.28572,0.0575197,-2.96275e-05,7.31895e-09,-7.05847e-13,-49448.1,-1.67378], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 73,
    label = "C6H14O2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {5,S} {8,S}
8  O u0 p2 c0 {7,S} {22,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.5671,0.00150447,0.000130868,-1.71644e-07,6.85316e-11,-33893,-22.4598], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.54783,0.0515959,-2.44482e-05,5.64697e-09,-5.15862e-13,-34660.8,-15.8723], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 74,
    label = "C6H14O2(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {7,S} {22,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.86787,0.0238847,7.96162e-05,-1.22906e-07,5.18438e-11,-35497.5,-11.2938], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.3206,0.050953,-2.39631e-05,5.49485e-09,-4.98623e-13,-36589.7,-19.4146], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 75,
    label = "C6H14O2(2)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {7,S} {22,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.83474,0.0408018,3.70502e-05,-7.87598e-08,3.54848e-11,-35482,-4.13384], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.7119,0.050504,-2.37644e-05,5.45612e-09,-4.95927e-13,-36796.6,-22.3806], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 76,
    label = "C7H16",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {6,S} {17,S} {18,S}
6  C u0 p0 c0 {5,S} {7,S} {19,S} {20,S}
7  C u0 p0 c0 {6,S} {21,S} {22,S} {23,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.2706,-0.0164189,0.000181666,-2.2256e-07,8.66796e-11,-27174.5,-30.6561], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.73837,0.0590969,-2.81169e-05,6.51602e-09,-5.96778e-13,-27286.2,-3.78931], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 77,
    label = "C7H15",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  C u1 p0 c0 {5,S} {21,S} {22,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.6583,5.61145e-06,0.000139588,-1.8159e-07,7.23463e-11,-2092.83,-15.7534], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.73314,0.0549805,-2.62487e-05,6.10526e-09,-5.61169e-13,-2718.29,-5.03367], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 78,
    label = "C7H15(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
7  C u1 p0 c0 {4,S} {6,S} {22,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.1792,-0.000357519,0.000136065,-1.74131e-07,6.86749e-11,-3402.87,-13.4585], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.90935,0.0569888,-2.72165e-05,6.33043e-09,-5.81777e-13,-3643.14,4.3988], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 79,
    label = "C7H15(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
7  C u1 p0 c0 {3,S} {4,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.4884,-0.0303902,0.000206589,-2.44129e-07,9.37797e-11,-3656.61,-32.6766], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.70242,0.0571289,-2.72373e-05,6.32361e-09,-5.8005e-13,-3429.38,4.42222], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 80,
    label = "C7H15(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  C u1 p0 c0 {3,S} {4,S} {22,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.8223,-0.0152548,0.000166723,-2.02139e-07,7.8174e-11,-3695.73,-27.5803], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.92728,0.0566452,-2.69019e-05,6.22442e-09,-5.69269e-13,-3551.25,2.10015], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 81,
    label = "C7H14",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {7,D} {19,S}
7  C u0 p0 c0 {6,D} {20,S} {21,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.79863,0.0233538,7.15736e-05,-1.06193e-07,4.3354e-11,-11299.7,-3.63567], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.31585,0.0538952,-2.578e-05,6.00964e-09,-5.5367e-13,-11905.5,-1.6815], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 82,
    label = "C7H14(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {7,D} {21,S}
7  C u0 p0 c0 {5,S} {6,D} {20,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.75558,0.0170528,8.21603e-05,-1.12113e-07,4.41367e-11,-12723.1,-8.68616], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.22869,0.0559593,-2.6916e-05,6.30353e-09,-5.82954e-13,-12950.8,3.01615], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 83,
    label = "C7H14(2)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {5,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {7,D} {20,S}
7  C u0 p0 c0 {2,S} {6,D} {21,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.98822,0.0238033,7.11857e-05,-1.05801e-07,4.31538e-11,-12537.4,-4.91655], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.5416,0.0542763,-2.59935e-05,6.06469e-09,-5.59082e-13,-13158.1,-3.16736], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 84,
    label = "C7H15O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {6,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {8,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  O u0 p2 c0 {6,S} {24,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[21.9019,-0.0584507,0.000270886,-3.01076e-07,1.11761e-10,-20492.4,-57.699], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.16231,0.0629432,-3.06598e-05,7.25271e-09,-6.76051e-13,-19529.1,5.73837], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 85,
    label = "C7H15O2(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {16,S} {17,S}
3  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {3,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {1,S} {21,S} {22,S} {23,S}
7  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
8  O u0 p2 c0 {1,S} {24,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.3752,3.76815e-05,0.00012919,-1.60031e-07,6.13263e-11,-22256.6,-32.4358], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.91292,0.0595232,-2.86163e-05,6.69766e-09,-6.18976e-13,-22228,-8.46802], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 86,
    label = "C7H15O2(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {7,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
6  C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {4,S} {21,S} {22,S} {23,S}
8  O u0 p2 c0 {1,S} {24,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.2721,0.0241748,7.15851e-05,-1.03107e-07,4.10952e-11,-22106.1,-20.8384], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.52607,0.0586432,-2.81055e-05,6.56153e-09,-6.05186e-13,-22441.2,-12.6237], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 87,
    label = "C7H15O2(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  O u0 p2 c0 {1,S} {24,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 O u1 p2 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.9955,0.041281,3.43659e-05,-6.94006e-08,2.99889e-11,-21920.8,-12.5738], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.4518,0.0573831,-2.73911e-05,6.37302e-09,-5.8616e-13,-22670.9,-18.5636], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 88,
    label = "C7H15O2(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {7,S} {16,S} {17,S}
5  C u0 p0 c0 {4,S} {8,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {20,S} {21,S} {22,S}
7  C u1 p0 c0 {3,S} {4,S} {23,S}
8  O u0 p2 c0 {5,S} {9,S}
9  O u0 p2 c0 {8,S} {24,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.3766,0.00237979,0.000130909,-1.64121e-07,6.31167e-11,-14442.6,-21.7677], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.41857,0.0618068,-2.9975e-05,7.06787e-09,-6.57368e-13,-14612.5,-0.715375], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 89,
    label = "C7H15O2(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {8,S} {10,S}
2  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {20,S} {21,S} {22,S}
6  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
7  C u1 p0 c0 {3,S} {4,S} {23,S}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {8,S} {24,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.44206,0.0274876,8.15509e-05,-1.23143e-07,5.04787e-11,-15425.7,-9.17447], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.50764,0.0585208,-2.82291e-05,6.6317e-09,-6.15264e-13,-16639.5,-16.2556], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 90,
    label = "C7H15O2(6)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
4  C u0 p0 c0 {6,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {20,S} {21,S} {22,S}
6  C u0 p0 c0 {4,S} {17,S} {18,S} {19,S}
7  C u1 p0 c0 {3,S} {4,S} {23,S}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {8,S} {24,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.91346,0.0330596,8.43673e-05,-1.40819e-07,6.10395e-11,-15525.4,-7.32377], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.0199,0.0535801,-2.53634e-05,5.8597e-09,-5.35768e-13,-17669.9,-34.8445], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 91,
    label = "C7H15O2(7)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  C u1 p0 c0 {5,S} {22,S} {23,S}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {8,S} {24,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.75385,0.0456516,3.40329e-05,-7.72523e-08,3.49869e-11,-13810.5,-6.83815], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.794,0.0548725,-2.59224e-05,5.97366e-09,-5.44816e-13,-15176.1,-25.9413], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 92,
    label = "C7H15O2(8)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {7,S} {20,S} {21,S} {22,S}
7  C u1 p0 c0 {4,S} {6,S} {23,S}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {8,S} {24,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.7975,0.0083104,0.000110904,-1.44928e-07,5.69036e-11,-15866.3,-31.8081], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.5279,0.0568661,-2.71331e-05,6.30526e-09,-5.79047e-13,-16174.1,-17.8927], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 93,
    label = "C7H15O4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {8,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {6,S} {10,S}
9  O u0 p2 c0 {1,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.4282,0.0265035,0.000112298,-1.69698e-07,7.08035e-11,-32024.7,-10.5655], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.215,0.0601096,-2.92748e-05,6.93239e-09,-6.47494e-13,-34291.2,-33.6502], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 94,
    label = "C7H15O4(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {9,S} {11,S}
2  C u0 p0 c0 {3,S} {6,S} {8,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {17,S} {18,S}
4  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
7  C u0 p0 c0 {5,S} {19,S} {20,S} {21,S}
8  O u0 p2 c0 {2,S} {10,S}
9  O u0 p2 c0 {1,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.227,0.0299653,0.000115841,-1.74445e-07,7.17975e-11,-34134.6,-3.28264], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.4459,0.0664255,-3.41123e-05,8.44449e-09,-8.17816e-13,-36798.4,-29.8106], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 95,
    label = "C7H15O4(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {8,S} {12,S}
2  C u0 p0 c0 {3,S} {4,S} {9,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {2,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.28654,0.0343842,0.000102659,-1.60558e-07,6.67515e-11,-34205.7,-3.70028], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.078,0.0655457,-3.36054e-05,8.30892e-09,-8.0396e-13,-36862.1,-32.3201], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 96,
    label = "C7H15O4(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {8,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {6,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.4215,-0.00631104,0.000192012,-2.44028e-07,9.49812e-11,-32518.7,-26.8188], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.4844,0.0638588,-3.2484e-05,7.98634e-09,-7.69718e-13,-34687.9,-31.4268], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 97,
    label = "C7H15O4(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {8,S} {11,S}
2  C u0 p0 c0 {3,S} {6,S} {9,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {17,S} {18,S}
4  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
7  C u0 p0 c0 {5,S} {19,S} {20,S} {21,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {2,S} {25,S}
10 O u0 p2 c0 {8,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.08439,0.0219029,0.000138704,-1.98891e-07,8.07862e-11,-34008.9,-6.02104], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.7919,0.066343,-3.42284e-05,8.50653e-09,-8.26446e-13,-36819.1,-31.4268], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 98,
    label = "C7H15O4(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {8,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {7,S} {19,S} {20,S}
6  C u0 p0 c0 {4,S} {21,S} {22,S} {23,S}
7  C u1 p0 c0 {5,S} {9,S} {24,S}
8  O u0 p2 c0 {1,S} {10,S}
9  O u0 p2 c0 {7,S} {11,S}
10 O u0 p2 c0 {8,S} {26,S}
11 O u0 p2 c0 {9,S} {25,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.3525,0.0285314,8.41944e-05,-1.29833e-07,5.38847e-11,-62422.2,-21.1568], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.8532,0.0566842,-2.71687e-05,6.34774e-09,-5.86257e-13,-64029.3,-35.7704], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 99,
    label = "C7H14O3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,D} {23,S}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {8,S} {24,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u0 p2 c0 {7,D}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.6836,0.00651932,0.000137308,-1.77583e-07,6.86481e-11,-49392.1,-21.7649], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.0285,0.0628391,-3.26418e-05,8.14278e-09,-7.92944e-13,-50790.4,-19.3179], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 100,
    label = "C7H14O3(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {7,S} {20,S} {21,S} {22,S}
7  C u0 p0 c0 {4,S} {6,S} {23,D}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {8,S} {24,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 O u0 p2 c0 {7,D}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.24497,0.0310871,7.70089e-05,-1.17685e-07,4.80039e-11,-53079,-3.84696], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.45362,0.0665343,-3.37674e-05,8.2218e-09,-7.82625e-13,-53805.3,-1.30414], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 101,
    label = "C7H14O3(2)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
4  C u0 p0 c0 {6,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {20,S} {21,S} {22,S}
6  C u0 p0 c0 {4,S} {17,S} {18,S} {19,S}
7  C u0 p0 c0 {3,S} {4,S} {23,D}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {8,S} {24,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 O u0 p2 c0 {7,D}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.83148,0.0621526,-8.51774e-06,-2.672e-08,1.416e-11,-53613.2,3.79198], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.73003,0.0646061,-3.25628e-05,7.8789e-09,-7.4592e-13,-54392.1,-7.56027], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 102,
    label = "C7H14O3(3)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {7,S} {16,S} {17,S}
5  C u0 p0 c0 {4,S} {8,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {20,S} {21,S} {22,S}
7  C u0 p0 c0 {3,S} {4,S} {23,D}
8  O u0 p2 c0 {5,S} {9,S}
9  O u0 p2 c0 {8,S} {24,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 O u0 p2 c0 {7,D}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.5422,-0.00240686,0.000160629,-2.01617e-07,7.79409e-11,-51697.1,-17.2933], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.1201,0.0682004,-3.50308e-05,8.62832e-09,-8.29805e-13,-52165.9,3.90279], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 103,
    label = "C7H14O3(4)",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {8,S} {10,S}
2  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {20,S} {21,S} {22,S}
6  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
7  C u0 p0 c0 {3,S} {4,S} {23,D}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {8,S} {24,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 O u0 p2 c0 {7,D}
24 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.44165,0.0419056,5.63121e-05,-1.00332e-07,4.25135e-11,-53507.1,2.6438], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.27512,0.0655722,-3.33976e-05,8.17315e-09,-7.82228e-13,-54737.8,-7.26983], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 104,
    label = "C7H16O2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {6,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {4,S} {8,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {6,S} {9,S}
9  O u0 p2 c0 {8,S} {25,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.1015,-0.0302617,0.000232145,-2.77277e-07,1.06642e-10,-36941.3,-28.8789], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.53528,0.0659103,-3.19105e-05,7.51193e-09,-6.9756e-13,-37172,4.96323], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 105,
    label = "C7H16O2(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {17,S} {18,S}
3  C u0 p0 c0 {4,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {3,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {1,S} {22,S} {23,S} {24,S}
7  C u0 p0 c0 {5,S} {19,S} {20,S} {21,S}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {8,S} {25,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.2588,0.0112235,0.000121547,-1.64538e-07,6.61681e-11,-38728.8,-23.2994], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.92278,0.0603401,-2.86075e-05,6.60812e-09,-6.03547e-13,-39331.5,-14.6496], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 106,
    label = "C7H16O2(2)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {7,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
6  C u0 p0 c0 {5,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {4,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {8,S} {25,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.365,0.0184413,0.000102688,-1.44091e-07,5.82962e-11,-38804,-20.4956], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.98744,0.0603517,-2.86703e-05,6.63771e-09,-6.07664e-13,-39497.1,-15.8204], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 107,
    label = "C7H16O2(3)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  O u0 p2 c0 {1,S} {9,S}
9  O u0 p2 c0 {8,S} {25,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.79574,0.0264001,9.60337e-05,-1.44738e-07,6.02433e-11,-38357.3,-10.0678], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.92438,0.0606073,-2.88922e-05,6.71179e-09,-6.16343e-13,-39638.1,-17.969], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 108,
    label = "C8H18",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,S} {16,S} {17,S}
5  C u0 p0 c0 {4,S} {6,S} {18,S} {19,S}
6  C u0 p0 c0 {5,S} {7,S} {20,S} {21,S}
7  C u0 p0 c0 {6,S} {8,S} {22,S} {23,S}
8  C u0 p0 c0 {7,S} {24,S} {25,S} {26,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.7903,-0.0235389,0.000211904,-2.54475e-07,9.82073e-11,-30276.1,-38.665], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.39683,0.0680613,-3.23886e-05,7.50532e-09,-6.87211e-13,-29968,1.07376], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 109,
    label = "C8H17",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {8,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  C u1 p0 c0 {6,S} {24,S} {25,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.335,-0.00413831,0.000160323,-2.03126e-07,7.99749e-11,-5244.21,-25.5259], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.01336,0.0630109,-2.99618e-05,6.94224e-09,-6.35873e-13,-5463.75,-3.73453], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 110,
    label = "C8H17(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {8,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {8,S} {22,S} {23,S} {24,S}
8  C u1 p0 c0 {5,S} {7,S} {25,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.8045,-0.0149754,0.000182656,-2.20375e-07,8.46416e-11,-6653.49,-26.4338], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.47292,0.0663545,-3.18167e-05,7.4252e-09,-6.84262e-13,-6380.83,9.33097], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 111,
    label = "C8H17(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {8,S} {17,S} {18,S}
5  C u0 p0 c0 {7,S} {8,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {22,S} {23,S} {24,S}
7  C u0 p0 c0 {5,S} {19,S} {20,S} {21,S}
8  C u1 p0 c0 {4,S} {5,S} {25,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.491,-0.0126851,0.000160185,-1.84384e-07,6.78842e-11,-6840.04,-35.1784], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.44017,0.0677122,-3.25882e-05,7.63235e-09,-7.05642e-13,-6016.31,10.2892], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 112,
    label = "C8H17(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {3,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {8,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
8  C u1 p0 c0 {4,S} {5,S} {25,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[17.038,-0.0273582,0.000201648,-2.31332e-07,8.64286e-11,-7180.02,-41.0228], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.43308,0.0675208,-3.23962e-05,7.56452e-09,-6.97402e-13,-6298.67,10.3415], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 113,
    label = "C8H16",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {8,D} {22,S}
8  C u0 p0 c0 {7,D} {23,S} {24,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.6794,-0.0024545,0.000165106,-2.11597e-07,8.3535e-11,-14357.7,-13.0701], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.62361,0.0639464,-3.08863e-05,7.25846e-09,-6.73172e-13,-15043.8,1.54956], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 114,
    label = "C8H16(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {8,S} {20,S} {21,S} {22,S}
7  C u0 p0 c0 {4,S} {8,D} {24,S}
8  C u0 p0 c0 {6,S} {7,D} {23,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.9107,0.00877508,0.000120451,-1.55014e-07,6.02307e-11,-15872.9,-15.6791], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.07548,0.0648657,-3.1228e-05,7.31678e-09,-6.76769e-13,-15924.6,5.49466], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 115,
    label = "C8H16(2)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {8,S} {15,S} {16,S}
4  C u0 p0 c0 {6,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {20,S} {21,S} {22,S}
6  C u0 p0 c0 {4,S} {17,S} {18,S} {19,S}
7  C u0 p0 c0 {4,S} {8,D} {23,S}
8  C u0 p0 c0 {3,S} {7,D} {24,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.41963,0.0226899,8.35229e-05,-1.15335e-07,4.51609e-11,-15647.1,-9.89878], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.34187,0.0646475,-3.11684e-05,7.31506e-09,-6.77792e-13,-15812.5,4.23378], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 116,
    label = "C8H16(3)",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {20,S} {21,S} {22,S}
7  C u0 p0 c0 {3,S} {8,D} {23,S}
8  C u0 p0 c0 {4,S} {7,D} {24,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.8772,0.0183801,8.89621e-05,-1.18694e-07,4.59869e-11,-16059.5,-17.4158], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.8775,0.0637106,-3.05534e-05,7.13579e-09,-6.58313e-13,-16015,1.26606], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 117,
    label = "C8H17O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {7,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {8,S} {10,S} {11,S}
7  C u0 p0 c0 {5,S} {9,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  O u0 p2 c0 {7,S} {27,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[17.2461,-0.0278723,0.000220053,-2.54656e-07,9.52992e-11,-23203.3,-35.4459], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.90379,0.0732374,-3.57609e-05,8.48202e-09,-7.9274e-13,-22710.7,12.9195], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 118,
    label = "C8H17O2(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {19,S} {20,S}
3  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {1,S} {24,S} {25,S} {26,S}
8  C u0 p0 c0 {6,S} {21,S} {22,S} {23,S}
9  O u0 p2 c0 {1,S} {27,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[18.9008,-0.0190792,0.000196764,-2.33963e-07,8.88875e-11,-25421.1,-43.9904], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.08057,0.0685089,-3.31617e-05,7.80722e-09,-7.2512e-13,-25273.2,-6.96712], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 119,
    label = "C8H17O2(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {17,S} {18,S}
3  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {3,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {8,S} {19,S} {20,S}
6  C u0 p0 c0 {3,S} {7,S} {11,S} {12,S}
7  C u0 p0 c0 {6,S} {21,S} {22,S} {23,S}
8  C u0 p0 c0 {5,S} {24,S} {25,S} {26,S}
9  O u0 p2 c0 {1,S} {27,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.3116,-0.00204843,0.000179181,-2.3009e-07,9.08375e-11,-24717.8,-20.6346], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.07496,0.0696449,-3.37399e-05,7.95053e-09,-7.39077e-13,-25549.1,-6.14711], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 120,
    label = "C8H17O2(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {15,S} {16,S}
3  C u0 p0 c0 {1,S} {6,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {3,S} {8,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  O u0 p2 c0 {1,S} {27,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.5842,0.0177655,0.000103155,-1.38005e-07,5.3987e-11,-25245.5,-28.5269], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.65947,0.0672795,-3.23103e-05,7.55548e-09,-6.97767e-13,-25375.9,-11.1383], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 121,
    label = "C8H17O2(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {15,S} {16,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {8,S} {17,S} {18,S}
5  C u0 p0 c0 {6,S} {8,S} {19,S} {20,S}
6  C u0 p0 c0 {5,S} {9,S} {21,S} {22,S}
7  C u0 p0 c0 {3,S} {23,S} {24,S} {25,S}
8  C u1 p0 c0 {4,S} {5,S} {26,S}
9  O u0 p2 c0 {6,S} {10,S}
10 O u0 p2 c0 {9,S} {27,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.817,0.0180978,0.000120687,-1.61412e-07,6.30197e-11,-17154.4,-11.3274], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.93317,0.0719604,-3.53059e-05,8.41145e-09,-7.89408e-13,-17898.3,-1.02048], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 122,
    label = "C8H17O2(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {9,S} {11,S}
2  C u0 p0 c0 {3,S} {5,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {8,S} {18,S} {19,S}
5  C u0 p0 c0 {2,S} {8,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {23,S} {24,S} {25,S}
7  C u0 p0 c0 {3,S} {20,S} {21,S} {22,S}
8  C u1 p0 c0 {4,S} {5,S} {26,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {27,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.58415,0.03586,0.000105418,-1.66948e-07,7.04802e-11,-18238.4,3.24027], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.86864,0.067077,-3.25062e-05,7.66919e-09,-7.14143e-13,-20572.1,-22.1102], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 123,
    label = "C8H17O2(6)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
3  C u0 p0 c0 {5,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {8,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {8,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {20,S} {21,S} {22,S}
7  C u0 p0 c0 {2,S} {23,S} {24,S} {25,S}
8  C u1 p0 c0 {4,S} {5,S} {26,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {27,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.1507,0.00660557,0.000151224,-2.01531e-07,8.09085e-11,-18961.4,-28.696], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.4312,0.0656668,-3.13606e-05,7.29007e-09,-6.6946e-13,-19800.6,-19.9839], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 124,
    label = "C8H17O2(7)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,S} {16,S} {17,S}
5  C u0 p0 c0 {4,S} {7,S} {18,S} {19,S}
6  C u0 p0 c0 {1,S} {8,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  C u1 p0 c0 {6,S} {25,S} {26,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {27,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.27469,0.0495404,6.74367e-05,-1.31052e-07,5.89292e-11,-16448.6,1.57988], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.4622,0.0637713,-3.0584e-05,7.13657e-09,-6.57588e-13,-18708,-30.6413], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 125,
    label = "C8H17O2(8)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {6,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {8,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {20,S} {21,S} {22,S}
7  C u0 p0 c0 {8,S} {23,S} {24,S} {25,S}
8  C u1 p0 c0 {5,S} {7,S} {26,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {27,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
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
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[19.0595,-0.0139192,0.000179279,-2.15279e-07,8.21365e-11,-19146,-47.118], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.96171,0.0664048,-3.18308e-05,7.4259e-09,-6.84183e-13,-18952.2,-12.5714], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 126,
    label = "C8H17O2(9)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {8,S} {18,S} {19,S}
5  C u0 p0 c0 {7,S} {8,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {23,S} {24,S} {25,S}
7  C u0 p0 c0 {5,S} {20,S} {21,S} {22,S}
8  C u1 p0 c0 {4,S} {5,S} {26,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {27,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.7372,0.00126337,0.000153343,-1.95623e-07,7.65654e-11,-18675.7,-33.6776], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.0304,0.0663218,-3.18072e-05,7.42636e-09,-6.84852e-13,-19093.6,-15.1103], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 127,
    label = "C8H17O4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {10,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {19,S} {20,S}
3  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {3,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {7,S} {21,S} {22,S}
6  C u0 p0 c0 {3,S} {8,S} {13,S} {14,S}
7  C u0 p0 c0 {5,S} {9,S} {23,S} {24,S}
8  C u0 p0 c0 {6,S} {25,S} {26,S} {27,S}
9  O u0 p2 c0 {7,S} {11,S}
10 O u0 p2 c0 {1,S} {28,S}
11 O u0 p2 c0 {9,S} {29,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.9391,-0.0098067,0.000233884,-2.97948e-07,1.16849e-10,-35105.4,-16.4297], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.28765,0.0774313,-3.96434e-05,9.78811e-09,-9.45916e-13,-37272.1,-14.8105], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 128,
    label = "C8H17O4(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {10,S} {12,S}
2  C u0 p0 c0 {3,S} {7,S} {9,S} {13,S}
3  C u0 p0 c0 {1,S} {2,S} {20,S} {21,S}
4  C u0 p0 c0 {1,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
6  C u0 p0 c0 {5,S} {8,S} {14,S} {15,S}
7  C u0 p0 c0 {2,S} {25,S} {26,S} {27,S}
8  C u0 p0 c0 {6,S} {22,S} {23,S} {24,S}
9  O u0 p2 c0 {2,S} {11,S}
10 O u0 p2 c0 {1,S} {28,S}
11 O u0 p2 c0 {9,S} {29,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.1091,0.0147292,0.000171397,-2.33817e-07,9.33973e-11,-37113.5,-11.8438], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.0312,0.0760807,-3.90041e-05,9.6409e-09,-9.32464e-13,-39576,-25.0265], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 129,
    label = "C8H17O4(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {9,S} {13,S}
2  C u0 p0 c0 {3,S} {4,S} {10,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {8,S} {20,S} {21,S}
6  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
7  C u0 p0 c0 {6,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {5,S} {25,S} {26,S} {27,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {2,S} {28,S}
11 O u0 p2 c0 {9,S} {29,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85469,0.0586039,6.18053e-05,-1.21396e-07,5.26071e-11,-32121.7,12.3313], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.11499,0.0755289,-3.7241e-05,8.90837e-09,-8.35827e-13,-34716.4,-21.4814], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 130,
    label = "C8H17O4(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {9,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {19,S} {20,S}
3  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {3,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {7,S} {21,S} {22,S}
6  C u0 p0 c0 {3,S} {8,S} {13,S} {14,S}
7  C u0 p0 c0 {5,S} {10,S} {23,S} {24,S}
8  C u0 p0 c0 {6,S} {25,S} {26,S} {27,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {7,S} {28,S}
11 O u0 p2 c0 {9,S} {29,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.3016,0.0132426,0.000175178,-2.45143e-07,1.00769e-10,-34597.7,-11.7793], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.5221,0.0711383,-3.48108e-05,8.2732e-09,-7.74783e-13,-36815.1,-25.2903], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 131,
    label = "C8H17O4(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {9,S} {12,S}
2  C u0 p0 c0 {3,S} {7,S} {10,S} {13,S}
3  C u0 p0 c0 {1,S} {2,S} {20,S} {21,S}
4  C u0 p0 c0 {1,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
6  C u0 p0 c0 {5,S} {8,S} {14,S} {15,S}
7  C u0 p0 c0 {2,S} {25,S} {26,S} {27,S}
8  C u0 p0 c0 {6,S} {22,S} {23,S} {24,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {2,S} {28,S}
11 O u0 p2 c0 {9,S} {29,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.4048,0.0103613,0.000193689,-2.63866e-07,1.06164e-10,-36898.6,-9.19242], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.086,0.0757986,-3.87771e-05,9.56974e-09,-9.24504e-13,-39751,-27.4755], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 132,
    label = "C8H17O4(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {9,S} {12,S}
2  C u0 p0 c0 {3,S} {5,S} {10,S} {13,S}
3  C u0 p0 c0 {1,S} {2,S} {18,S} {19,S}
4  C u0 p0 c0 {1,S} {6,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {8,S} {20,S} {21,S}
6  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
7  C u0 p0 c0 {6,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {5,S} {25,S} {26,S} {27,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {2,S} {28,S}
11 O u0 p2 c0 {9,S} {29,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.0227,0.0246745,0.000150188,-2.16308e-07,8.83375e-11,-37107.2,-9.02846], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.9426,0.0744986,-3.79629e-05,9.33667e-09,-8.99371e-13,-39785.6,-30.9444], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 133,
    label = "C8H17O4(6)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {9,S} {13,S}
2  C u0 p0 c0 {1,S} {4,S} {20,S} {21,S}
3  C u0 p0 c0 {4,S} {5,S} {16,S} {17,S}
4  C u0 p0 c0 {2,S} {3,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {7,S} {14,S} {15,S}
6  C u0 p0 c0 {1,S} {8,S} {22,S} {23,S}
7  C u0 p0 c0 {5,S} {24,S} {25,S} {26,S}
8  C u1 p0 c0 {6,S} {10,S} {27,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {8,S} {12,S}
11 O u0 p2 c0 {9,S} {29,S}
12 O u0 p2 c0 {10,S} {28,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.5009,0.00606784,0.000193643,-2.6101e-07,1.0479e-10,-66165.7,-18.8779], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.5162,0.0695189,-3.46295e-05,8.3847e-09,-7.98992e-13,-69046.6,-38.6072], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 134,
    label = "C8H17O4(9)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {4,S} {17,S} {18,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {8,S} {19,S} {20,S}
5  C u0 p0 c0 {6,S} {8,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {9,S} {23,S} {24,S}
7  C u0 p0 c0 {3,S} {25,S} {26,S} {27,S}
8  C u1 p0 c0 {4,S} {5,S} {10,S}
9  O u0 p2 c0 {6,S} {11,S}
10 O u0 p2 c0 {8,S} {12,S}
11 O u0 p2 c0 {9,S} {28,S}
12 O u0 p2 c0 {10,S} {29,S}
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
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {11,S}
29 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.30918,0.0438403,8.8935e-05,-1.49134e-07,6.32692e-11,-56996.3,-3.87973], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.9057,0.0687161,-3.36925e-05,8.04851e-09,-7.58448e-13,-59645.1,-35.5809], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 135,
    label = "C8H17O4(10)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {9,S} {13,S}
2  C u0 p0 c0 {3,S} {5,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {8,S} {20,S} {21,S}
5  C u0 p0 c0 {2,S} {8,S} {18,S} {19,S}
6  C u0 p0 c0 {1,S} {25,S} {26,S} {27,S}
7  C u0 p0 c0 {3,S} {22,S} {23,S} {24,S}
8  C u1 p0 c0 {4,S} {5,S} {10,S}
9  O u0 p2 c0 {1,S} {11,S}
10 O u0 p2 c0 {8,S} {12,S}
11 O u0 p2 c0 {9,S} {28,S}
12 O u0 p2 c0 {10,S} {29,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {11,S}
29 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.0765,0.0221593,0.000142469,-2.05083e-07,8.42203e-11,-59682.6,-22.1154], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.7105,0.0712952,-3.61918e-05,8.88242e-09,-8.5443e-13,-61807.4,-36.3534], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 136,
    label = "C8H16O3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {18,S} {19,S}
3  C u0 p0 c0 {4,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {3,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {1,S} {8,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {6,S} {25,D} {26,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {27,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u0 p2 c0 {8,D}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.4489,-0.00125374,0.000184461,-2.35421e-07,9.15899e-11,-52107.3,-22.4227], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.53307,0.0721287,-3.71503e-05,9.20492e-09,-8.91519e-13,-53672.5,-16.3718], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 137,
    label = "C8H16O3(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {8,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {20,S} {21,S} {22,S}
7  C u0 p0 c0 {8,S} {23,S} {24,S} {25,S}
8  C u0 p0 c0 {5,S} {7,S} {26,D}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {27,S}
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
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 O u0 p2 c0 {8,D}
27 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.0517,0.0159255,0.000120377,-1.59314e-07,6.21587e-11,-56693.5,-22.6894], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.93524,0.0746168,-3.75885e-05,9.09713e-09,-8.61715e-13,-56766.3,-0.529081], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 138,
    label = "C8H16O3(2)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {8,S} {16,S} {17,S}
5  C u0 p0 c0 {7,S} {8,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {20,S} {21,S} {22,S}
7  C u0 p0 c0 {5,S} {23,S} {24,S} {25,S}
8  C u0 p0 c0 {4,S} {5,S} {26,D}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {27,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 O u0 p2 c0 {8,D}
27 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.3733,0.0478961,5.53405e-05,-1.01539e-07,4.3206e-11,-55749.3,0.769746], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.96837,0.0747522,-3.77109e-05,9.13217e-09,-8.65069e-13,-56608.9,-2.6361], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 139,
    label = "C8H18O2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {7,S} {21,S} {22,S}
6  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {5,S} {9,S} {23,S} {24,S}
8  C u0 p0 c0 {6,S} {25,S} {26,S} {27,S}
9  O u0 p2 c0 {7,S} {10,S}
10 O u0 p2 c0 {9,S} {28,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
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
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[17.9691,-0.0490166,0.000298851,-3.49665e-07,1.33467e-10,-39944.3,-39.1241], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.67323,0.0759552,-3.69377e-05,8.72801e-09,-8.13002e-13,-39946.9,9.74863], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 140,
    label = "C8H18O2(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {20,S} {21,S}
3  C u0 p0 c0 {4,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {8,S} {12,S} {13,S}
7  C u0 p0 c0 {1,S} {25,S} {26,S} {27,S}
8  C u0 p0 c0 {6,S} {22,S} {23,S} {24,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {28,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[18.419,-0.014264,0.000197794,-2.43073e-07,9.43415e-11,-42050.6,-42.4633], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.3398,0.0687101,-3.27326e-05,7.59656e-09,-6.96811e-13,-42276.1,-14.1624], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 141,
    label = "C8H18O2(2)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {18,S} {19,S}
3  C u0 p0 c0 {4,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {3,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {8,S} {20,S} {21,S}
6  C u0 p0 c0 {3,S} {7,S} {12,S} {13,S}
7  C u0 p0 c0 {6,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {5,S} {25,S} {26,S} {27,S}
9  O u0 p2 c0 {1,S} {10,S}
10 O u0 p2 c0 {9,S} {28,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.9563,0.00547296,0.000166039,-2.21427e-07,8.91504e-11,-41462.9,-24.0026], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.3652,0.0685981,-3.26487e-05,7.57145e-09,-6.94086e-13,-42485.8,-16.8495], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 142,
    label = "C9H20",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {5,S} {17,S} {18,S}
5  C u0 p0 c0 {4,S} {6,S} {19,S} {20,S}
6  C u0 p0 c0 {5,S} {7,S} {21,S} {22,S}
7  C u0 p0 c0 {6,S} {8,S} {23,S} {24,S}
8  C u0 p0 c0 {7,S} {9,S} {25,S} {26,S}
9  C u0 p0 c0 {8,S} {27,S} {28,S} {29,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.4711,-0.00903056,0.000197495,-2.4479e-07,9.52066e-11,-32817.7,-29.8883], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.3544,0.0770678,-3.68648e-05,8.58444e-09,-7.8953e-13,-32774.6,3.71015], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 143,
    label = "C9H19",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {6,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {4,S} {8,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {9,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  C u1 p0 c0 {7,S} {27,S} {28,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[19.0689,-0.0285787,0.000230326,-2.72336e-07,1.04062e-10,-8563.09,-42.7069], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.05884,0.0729986,-3.4886e-05,8.11766e-09,-7.4618e-13,-8089.3,4.00198], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 144,
    label = "C9H19(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {5,S} {16,S} {17,S}
4  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {9,S} {25,S} {26,S} {27,S}
9  C u1 p0 c0 {6,S} {8,S} {28,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.8132,-0.0138279,0.000193278,-2.28146e-07,8.56178e-11,-9678.46,-28.8246], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.32762,0.0782413,-3.79494e-05,8.94886e-09,-8.32244e-13,-9135.06,16.641], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 145,
    label = "C9H19(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {4,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {7,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {9,S} {20,S} {21,S}
6  C u0 p0 c0 {8,S} {9,S} {18,S} {19,S}
7  C u0 p0 c0 {4,S} {25,S} {26,S} {27,S}
8  C u0 p0 c0 {6,S} {22,S} {23,S} {24,S}
9  C u1 p0 c0 {5,S} {6,S} {28,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.7703,-0.0184397,0.000206671,-2.44664e-07,9.25504e-11,-9899.03,-34.0028], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.25637,0.076793,-3.70531e-05,8.69692e-09,-8.05542e-13,-9429.22,11.0474], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 146,
    label = "C9H19(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {8,S} {16,S} {17,S}
4  C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
5  C u0 p0 c0 {4,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {4,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {3,S} {25,S} {26,S} {27,S}
9  C u1 p0 c0 {5,S} {6,S} {28,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.1046,0.000799511,0.00015795,-1.932e-07,7.32051e-11,-10064.8,-23.9059], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.93617,0.0773676,-3.74365e-05,8.81004e-09,-8.17942e-13,-9749.48,11.7213], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 147,
    label = "C9H19(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {12,S} {13,S}
2  C u0 p0 c0 {4,S} {6,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {8,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {3,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {4,S} {25,S} {26,S} {27,S}
9  C u1 p0 c0 {5,S} {6,S} {28,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.7624,-0.0126067,0.000199629,-2.43278e-07,9.36172e-11,-9954.79,-28.2578], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.16102,0.0756375,-3.64167e-05,8.53057e-09,-7.88721e-13,-9864.66,7.50989], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 148,
    label = "C9H18",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {5,S} {16,S} {17,S}
4  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {8,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {6,S} {9,D} {25,S}
9  C u0 p0 c0 {8,D} {26,S} {27,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.593,0.00363025,0.000161683,-2.07457e-07,8.12862e-11,-16796.3,-12.6007], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.3269,0.0734105,-3.56207e-05,8.40071e-09,-7.81273e-13,-17203.1,8.12021], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 149,
    label = "C9H18(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {4,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {8,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {20,S} {21,S} {22,S}
7  C u0 p0 c0 {9,S} {23,S} {24,S} {25,S}
8  C u0 p0 c0 {5,S} {9,D} {27,S}
9  C u0 p0 c0 {7,S} {8,D} {26,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.3465,0.00650784,0.000163465,-2.14476e-07,8.50972e-11,-18660.7,-10.7959], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.42673,0.0734284,-3.54825e-05,8.342e-09,-7.73942e-13,-19415.6,2.93708], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 150,
    label = "C9H18(3)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
3  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {8,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {20,S} {21,S} {22,S}
7  C u0 p0 c0 {2,S} {23,S} {24,S} {25,S}
8  C u0 p0 c0 {4,S} {9,D} {26,S}
9  C u0 p0 c0 {5,S} {8,D} {27,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.0393,0.00294338,0.00015425,-1.92309e-07,7.37049e-11,-19241.2,-20.1062], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.20118,0.0750098,-3.63547e-05,8.56933e-09,-7.96803e-13,-19220.6,8.9395], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 151,
    label = "C9H19O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {8,S} {23,S} {24,S}
7  C u0 p0 c0 {1,S} {9,S} {11,S} {12,S}
8  C u0 p0 c0 {6,S} {10,S} {25,S} {26,S}
9  C u0 p0 c0 {7,S} {27,S} {28,S} {29,S}
10 O u0 p2 c0 {8,S} {30,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
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
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 O u1 p2 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.9174,-0.0288489,0.000263817,-3.14675e-07,1.20021e-10,-25826.4,-24.1333], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.31594,0.0844983,-4.15766e-05,9.9267e-09,-9.32943e-13,-26060.4,17.3942], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 152,
    label = "C9H19O2(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {5,S} {18,S} {19,S}
4  C u0 p0 c0 {1,S} {8,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {9,S} {20,S} {21,S}
6  C u0 p0 c0 {7,S} {9,S} {22,S} {23,S}
7  C u0 p0 c0 {6,S} {10,S} {24,S} {25,S}
8  C u0 p0 c0 {4,S} {26,S} {27,S} {28,S}
9  C u1 p0 c0 {5,S} {6,S} {29,S}
10 O u0 p2 c0 {7,S} {11,S}
11 O u0 p2 c0 {10,S} {30,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.415,-0.008341,0.000235525,-3.01726e-07,1.19111e-10,-20169.5,-14.0051], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.03703,0.0796092,-3.91239e-05,9.33913e-09,-8.78063e-13,-21985.5,-8.08004], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 153,
    label = "C9H19O2(6)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {7,S} {10,S} {12,S}
2  C u0 p0 c0 {3,S} {4,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {6,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {8,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {9,S} {21,S} {22,S}
6  C u0 p0 c0 {3,S} {9,S} {19,S} {20,S}
7  C u0 p0 c0 {1,S} {26,S} {27,S} {28,S}
8  C u0 p0 c0 {4,S} {23,S} {24,S} {25,S}
9  C u1 p0 c0 {5,S} {6,S} {29,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {30,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.67458,0.0178623,0.000169671,-2.37053e-07,9.65974e-11,-21592.5,-6.97885], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.39337,0.0766319,-3.72658e-05,8.81616e-09,-8.22708e-13,-23700.3,-17.9386], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 154,
    label = "C9H19O2(7)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {10,S} {12,S}
2  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
3  C u0 p0 c0 {1,S} {8,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {9,S} {21,S} {22,S}
6  C u0 p0 c0 {2,S} {9,S} {19,S} {20,S}
7  C u0 p0 c0 {4,S} {23,S} {24,S} {25,S}
8  C u0 p0 c0 {3,S} {26,S} {27,S} {28,S}
9  C u1 p0 c0 {5,S} {6,S} {29,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {30,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.5138,0.0129623,0.000174876,-2.38807e-07,9.63929e-11,-21582.5,-15.4702], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.2553,0.0753967,-3.65234e-05,8.60975e-09,-8.00902e-13,-23490.4,-21.6858], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 155,
    label = "C9H19O2(8)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {10,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {5,S} {17,S} {18,S}
5  C u0 p0 c0 {4,S} {6,S} {19,S} {20,S}
6  C u0 p0 c0 {5,S} {8,S} {21,S} {22,S}
7  C u0 p0 c0 {1,S} {9,S} {23,S} {24,S}
8  C u0 p0 c0 {6,S} {25,S} {26,S} {27,S}
9  C u1 p0 c0 {7,S} {28,S} {29,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {30,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.8206,0.0383066,8.56968e-05,-1.35191e-07,5.62581e-11,-19850,-13.7981], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.0237,0.0736093,-3.51769e-05,8.18751e-09,-7.53073e-13,-20855.8,-16.6999], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 156,
    label = "C9H19O2(9)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {10,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {5,S} {17,S} {18,S}
5  C u0 p0 c0 {4,S} {7,S} {19,S} {20,S}
6  C u0 p0 c0 {1,S} {9,S} {21,S} {22,S}
7  C u0 p0 c0 {5,S} {23,S} {24,S} {25,S}
8  C u0 p0 c0 {9,S} {26,S} {27,S} {28,S}
9  C u1 p0 c0 {6,S} {8,S} {29,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {30,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.24668,0.0473257,8.56285e-05,-1.50696e-07,6.58553e-11,-21006.4,-5.94205], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.9879,0.071048,-3.37924e-05,7.83512e-09,-7.18351e-13,-23119.9,-31.9976], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 157,
    label = "C9H19O2(10)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {10,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {8,S} {17,S} {18,S}
4  C u0 p0 c0 {6,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {9,S} {21,S} {22,S}
6  C u0 p0 c0 {4,S} {9,S} {19,S} {20,S}
7  C u0 p0 c0 {4,S} {23,S} {24,S} {25,S}
8  C u0 p0 c0 {3,S} {26,S} {27,S} {28,S}
9  C u1 p0 c0 {5,S} {6,S} {29,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {30,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.5139,0.0255018,0.000120023,-1.66675e-07,6.61037e-11,-21803.4,-15.9676], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.41221,0.0777073,-3.77303e-05,8.90842e-09,-8.29677e-13,-22729,-9.66521], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 158,
    label = "C9H19O2(11)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {10,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {9,S} {21,S} {22,S}
6  C u0 p0 c0 {8,S} {9,S} {19,S} {20,S}
7  C u0 p0 c0 {4,S} {26,S} {27,S} {28,S}
8  C u0 p0 c0 {6,S} {23,S} {24,S} {25,S}
9  C u1 p0 c0 {5,S} {6,S} {29,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {30,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[17.84,-0.0125499,0.000212033,-2.63341e-07,1.02639e-10,-21911.2,-40.6762], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.90589,0.0751043,-3.6024e-05,8.41036e-09,-7.75421e-13,-22373.3,-14.2248], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 159,
    label = "C9H19O4(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {11,S} {13,S}
2  C u0 p0 c0 {3,S} {8,S} {10,S} {14,S}
3  C u0 p0 c0 {1,S} {2,S} {23,S} {24,S}
4  C u0 p0 c0 {1,S} {6,S} {21,S} {22,S}
5  C u0 p0 c0 {6,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {5,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {9,S} {15,S} {16,S}
8  C u0 p0 c0 {2,S} {28,S} {29,S} {30,S}
9  C u0 p0 c0 {7,S} {25,S} {26,S} {27,S}
10 O u0 p2 c0 {2,S} {12,S}
11 O u0 p2 c0 {1,S} {31,S}
12 O u0 p2 c0 {10,S} {32,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 O u1 p2 c0 {11,S}
32 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.9325,0.00426057,0.000217992,-2.86441e-07,1.13302e-10,-40277.6,-16.5649], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.261,0.0858398,-4.37944e-05,1.07788e-08,-1.03874e-12,-42570.3,-19.2845], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 160,
    label = "C9H19O4(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {10,S} {14,S}
2  C u0 p0 c0 {3,S} {4,S} {11,S} {13,S}
3  C u0 p0 c0 {1,S} {2,S} {21,S} {22,S}
4  C u0 p0 c0 {2,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {9,S} {23,S} {24,S}
7  C u0 p0 c0 {5,S} {8,S} {15,S} {16,S}
8  C u0 p0 c0 {7,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {6,S} {28,S} {29,S} {30,S}
10 O u0 p2 c0 {1,S} {12,S}
11 O u0 p2 c0 {2,S} {31,S}
12 O u0 p2 c0 {10,S} {32,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 O u1 p2 c0 {11,S}
32 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.0431,0.0322583,0.000149769,-2.19987e-07,9.02094e-11,-39724,-7.29782], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.8195,0.083418,-4.23206e-05,1.03722e-08,-9.964e-13,-42399.1,-28.6689], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 161,
    label = "C9H19O4(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {10,S} {13,S}
2  C u0 p0 c0 {1,S} {5,S} {22,S} {23,S}
3  C u0 p0 c0 {4,S} {7,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {8,S} {24,S} {25,S}
7  C u0 p0 c0 {3,S} {9,S} {14,S} {15,S}
8  C u0 p0 c0 {6,S} {11,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {28,S} {29,S} {30,S}
10 O u0 p2 c0 {1,S} {12,S}
11 O u0 p2 c0 {8,S} {31,S}
12 O u0 p2 c0 {10,S} {32,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 O u1 p2 c0 {11,S}
32 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.4259,-0.0140357,0.00025034,-3.157e-07,1.23754e-10,-37495.7,-27.9474], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.8484,0.081344,-4.00943e-05,9.58962e-09,-9.02938e-13,-39187.5,-16.8475], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 162,
    label = "C9H19O4(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {10,S} {13,S}
2  C u0 p0 c0 {3,S} {8,S} {11,S} {14,S}
3  C u0 p0 c0 {1,S} {2,S} {23,S} {24,S}
4  C u0 p0 c0 {1,S} {6,S} {21,S} {22,S}
5  C u0 p0 c0 {6,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {5,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {9,S} {15,S} {16,S}
8  C u0 p0 c0 {2,S} {28,S} {29,S} {30,S}
9  C u0 p0 c0 {7,S} {25,S} {26,S} {27,S}
10 O u0 p2 c0 {1,S} {12,S}
11 O u0 p2 c0 {2,S} {31,S}
12 O u0 p2 c0 {10,S} {32,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 O u1 p2 c0 {11,S}
32 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.3986,0.00386362,0.000218203,-2.86453e-07,1.13211e-10,-40130,-18.3835], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.0198,0.0848593,-4.32827e-05,1.06547e-08,-1.02718e-12,-42516.2,-22.6798], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 163,
    label = "C9H19O4(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {10,S} {14,S}
2  C u0 p0 c0 {3,S} {4,S} {11,S} {13,S}
3  C u0 p0 c0 {1,S} {2,S} {19,S} {20,S}
4  C u0 p0 c0 {2,S} {6,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {7,S} {21,S} {22,S}
6  C u0 p0 c0 {4,S} {8,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {9,S} {23,S} {24,S}
8  C u0 p0 c0 {6,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {28,S} {29,S} {30,S}
10 O u0 p2 c0 {1,S} {12,S}
11 O u0 p2 c0 {2,S} {31,S}
12 O u0 p2 c0 {10,S} {32,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 O u1 p2 c0 {11,S}
32 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.29097,0.0428021,0.00012573,-1.95316e-07,8.08843e-11,-39690.5,-0.611928], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.909,0.0835631,-4.25274e-05,1.04535e-08,-1.00683e-12,-42667.3,-30.3533], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 164,
    label = "C9H19O4(6)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {10,S} {13,S}
2  C u0 p0 c0 {3,S} {6,S} {11,S} {14,S}
3  C u0 p0 c0 {1,S} {2,S} {21,S} {22,S}
4  C u0 p0 c0 {1,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {9,S} {23,S} {24,S}
7  C u0 p0 c0 {5,S} {8,S} {15,S} {16,S}
8  C u0 p0 c0 {7,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {6,S} {28,S} {29,S} {30,S}
10 O u0 p2 c0 {1,S} {12,S}
11 O u0 p2 c0 {2,S} {31,S}
12 O u0 p2 c0 {10,S} {32,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 O u1 p2 c0 {11,S}
32 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.3109,0.0260688,0.000126284,-1.78575e-07,7.20503e-11,-40440.3,-27.7639], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.705,0.0781653,-3.77938e-05,8.88833e-09,-8.24905e-13,-41480.6,-24.0892], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 165,
    label = "C9H19O4(10)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {5,S} {20,S} {21,S}
4  C u0 p0 c0 {1,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {9,S} {22,S} {23,S}
6  C u0 p0 c0 {7,S} {9,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {10,S} {26,S} {27,S}
8  C u0 p0 c0 {4,S} {28,S} {29,S} {30,S}
9  C u1 p0 c0 {5,S} {6,S} {11,S}
10 O u0 p2 c0 {7,S} {12,S}
11 O u0 p2 c0 {9,S} {13,S}
12 O u0 p2 c0 {10,S} {31,S}
13 O u0 p2 c0 {11,S} {32,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {12,S}
32 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.8568,0.00720048,0.00019749,-2.5846e-07,1.01866e-10,-60694.2,-13.931], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.4803,0.0888498,-4.55188e-05,1.12249e-08,-1.08249e-12,-61970.9,-1.09409], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 166,
    label = "C9H18O3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {10,S} {12,S}
2  C u0 p0 c0 {1,S} {5,S} {21,S} {22,S}
3  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {5,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
6  C u0 p0 c0 {3,S} {8,S} {13,S} {14,S}
7  C u0 p0 c0 {1,S} {9,S} {23,S} {24,S}
8  C u0 p0 c0 {6,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {28,D} {29,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {30,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 O u0 p2 c0 {9,D}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.1909,-0.00675724,0.000237467,-3.03911e-07,1.19076e-10,-54252,-14.7972], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.8712,0.0818174,-4.20051e-05,1.03882e-08,-1.00494e-12,-56620.5,-15.4501], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 167,
    label = "C9H18O3(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {10,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {19,S} {20,S}
3  C u0 p0 c0 {4,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {3,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {9,S} {21,S} {22,S}
7  C u0 p0 c0 {5,S} {23,S} {24,S} {25,S}
8  C u0 p0 c0 {9,S} {26,S} {27,S} {28,S}
9  C u0 p0 c0 {6,S} {8,S} {29,D}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {30,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 O u0 p2 c0 {9,D}
30 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.5453,-0.000977184,0.000179138,-2.22453e-07,8.54335e-11,-59584.8,-35.5176], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.72621,0.0839958,-4.23023e-05,1.02361e-08,-9.69308e-13,-59330.5,2.0952], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 168,
    label = "C9H18O3(2)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {10,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {9,S} {19,S} {20,S}
6  C u0 p0 c0 {8,S} {9,S} {21,S} {22,S}
7  C u0 p0 c0 {4,S} {23,S} {24,S} {25,S}
8  C u0 p0 c0 {6,S} {26,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {6,S} {29,D}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {30,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 O u0 p2 c0 {9,D}
30 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.2043,0.0190746,0.000158999,-2.21016e-07,8.92415e-11,-58593,-13.565], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.9747,0.0754462,-3.68442e-05,8.74628e-09,-8.18739e-13,-60696.4,-24.5009], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 169,
    label = "C9H18O3(3)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {5,S} {18,S} {19,S}
4  C u0 p0 c0 {1,S} {8,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {9,S} {20,S} {21,S}
6  C u0 p0 c0 {7,S} {9,S} {22,S} {23,S}
7  C u0 p0 c0 {6,S} {10,S} {24,S} {25,S}
8  C u0 p0 c0 {4,S} {26,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {6,S} {29,D}
10 O u0 p2 c0 {7,S} {11,S}
11 O u0 p2 c0 {10,S} {30,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 O u0 p2 c0 {9,D}
30 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.5778,-0.0127212,0.000227512,-2.8125e-07,1.08783e-10,-58058.7,-23.4083], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.23066,0.0855272,-4.34694e-05,1.06306e-08,-1.01726e-12,-58518.6,8.55855], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 170,
    label = "C9H18O3(4)",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {7,S} {10,S} {12,S}
2  C u0 p0 c0 {3,S} {4,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {6,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {8,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {9,S} {21,S} {22,S}
6  C u0 p0 c0 {3,S} {9,S} {19,S} {20,S}
7  C u0 p0 c0 {1,S} {26,S} {27,S} {28,S}
8  C u0 p0 c0 {4,S} {23,S} {24,S} {25,S}
9  C u0 p0 c0 {5,S} {6,S} {29,D}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {30,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 O u0 p2 c0 {9,D}
30 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.3232,0.0106541,0.000179221,-2.3765e-07,9.3782e-11,-59319.6,-15.7643], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.23685,0.0785628,-3.89544e-05,9.37208e-09,-8.87326e-13,-61284.3,-18.8469], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 171,
    label = "C9H18O3(5)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {10,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {8,S} {17,S} {18,S}
4  C u0 p0 c0 {6,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {9,S} {21,S} {22,S}
6  C u0 p0 c0 {4,S} {9,S} {19,S} {20,S}
7  C u0 p0 c0 {4,S} {23,S} {24,S} {25,S}
8  C u0 p0 c0 {3,S} {26,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {6,S} {29,D}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {30,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 O u0 p2 c0 {9,D}
30 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.81968,0.0375374,0.000105888,-1.59683e-07,6.51369e-11,-59414,-4.48252], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.18053,0.0833746,-4.21311e-05,1.02519e-08,-9.77026e-13,-60614.7,-5.10386], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 172,
    label = "C9H18O3(6)",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {10,S} {12,S}
2  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
3  C u0 p0 c0 {1,S} {8,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {9,S} {21,S} {22,S}
6  C u0 p0 c0 {2,S} {9,S} {19,S} {20,S}
7  C u0 p0 c0 {4,S} {23,S} {24,S} {25,S}
8  C u0 p0 c0 {3,S} {26,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {6,S} {29,D}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {30,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 O u0 p2 c0 {9,D}
30 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.1006,0.0479828,8.6909e-05,-1.45152e-07,6.1054e-11,-59475.9,3.48164], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.96005,0.0823607,-4.15685e-05,1.01044e-08,-9.62089e-13,-61109.3,-8.84243], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 173,
    label = "C9H20O2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {8,S} {24,S} {25,S}
7  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
8  C u0 p0 c0 {6,S} {10,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {28,S} {29,S} {30,S}
10 O u0 p2 c0 {8,S} {11,S}
11 O u0 p2 c0 {10,S} {31,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.0153,-0.0162294,0.000237777,-2.90397e-07,1.11778e-10,-42240,-21.7317], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.05084,0.0857815,-4.19008e-05,9.94181e-09,-9.29537e-13,-42598.3,12.9922], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 174,
    label = "C9H20O2(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {10,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {23,S} {24,S}
3  C u0 p0 c0 {4,S} {7,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {5,S} {17,S} {18,S}
5  C u0 p0 c0 {4,S} {6,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {5,S} {21,S} {22,S}
7  C u0 p0 c0 {3,S} {9,S} {13,S} {14,S}
8  C u0 p0 c0 {1,S} {28,S} {29,S} {30,S}
9  C u0 p0 c0 {7,S} {25,S} {26,S} {27,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {31,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.7568,-0.00727592,0.000225475,-2.83975e-07,1.10804e-10,-44223.4,-20.2703], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.70848,0.0844288,-4.1212e-05,9.77403e-09,-9.13599e-13,-45225.3,0.0699969], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 175,
    label = "C9H20O2(2)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {10,S} {12,S}
2  C u0 p0 c0 {1,S} {5,S} {21,S} {22,S}
3  C u0 p0 c0 {4,S} {7,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {5,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
6  C u0 p0 c0 {1,S} {9,S} {23,S} {24,S}
7  C u0 p0 c0 {3,S} {8,S} {13,S} {14,S}
8  C u0 p0 c0 {7,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {6,S} {28,S} {29,S} {30,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {31,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.9172,-0.0132186,0.000237475,-2.98046e-07,1.16902e-10,-44341.8,-26.0487], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.29407,0.0819095,-3.96337e-05,9.32677e-09,-8.65928e-13,-45202.5,-2.97891], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 176,
    label = "C9H20O2(3)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {12,S}
2  C u0 p0 c0 {1,S} {5,S} {19,S} {20,S}
3  C u0 p0 c0 {1,S} {7,S} {21,S} {22,S}
4  C u0 p0 c0 {5,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
7  C u0 p0 c0 {3,S} {9,S} {23,S} {24,S}
8  C u0 p0 c0 {6,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {28,S} {29,S} {30,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {31,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[18.6192,-0.0310234,0.000268013,-3.19496e-07,1.22086e-10,-44633.8,-43.6628], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.99236,0.0830019,-4.04986e-05,9.60012e-09,-8.96923e-13,-44859.8,-2.06997], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 177,
    label = "C9H20O2(4)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {17,S} {18,S}
3  C u0 p0 c0 {1,S} {5,S} {19,S} {20,S}
4  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {7,S} {21,S} {22,S}
6  C u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
7  C u0 p0 c0 {5,S} {9,S} {23,S} {24,S}
8  C u0 p0 c0 {6,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {28,S} {29,S} {30,S}
10 O u0 p2 c0 {1,S} {11,S}
11 O u0 p2 c0 {10,S} {31,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.758,0.0127376,0.00016971,-2.28514e-07,9.16595e-11,-44320.9,-18.0161], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.88611,0.079635,-3.83139e-05,8.97328e-09,-8.29819e-13,-45430.5,-10.1958], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 178,
    label = "C10H22",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {11,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {6,S} {8,S} {24,S} {25,S}
8  C u0 p0 c0 {7,S} {9,S} {26,S} {27,S}
9  C u0 p0 c0 {8,S} {10,S} {28,S} {29,S}
10 C u0 p0 c0 {9,S} {30,S} {31,S} {32,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[19.958,-0.0336635,0.000271363,-3.2038e-07,1.22274e-10,-36069.5,-45.9628], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.51684,0.0868891,-4.16902e-05,9.73256e-09,-8.96964e-13,-35447.6,10.5222], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 179,
    label = "C10H21",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {7,S} {21,S} {22,S}
6  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {5,S} {9,S} {23,S} {24,S}
8  C u0 p0 c0 {6,S} {10,S} {25,S} {26,S}
9  C u0 p0 c0 {7,S} {27,S} {28,S} {29,S}
10 C u1 p0 c0 {8,S} {30,S} {31,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
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
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[24.3985,-0.0602025,0.000321918,-3.66367e-07,1.3797e-10,-12009.5,-61.102], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.09817,0.0829799,-3.97893e-05,9.28207e-09,-8.5479e-13,-10878.9,12.473], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 180,
    label = "C10H21(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {6,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {8,S} {21,S} {22,S}
7  C u0 p0 c0 {5,S} {10,S} {23,S} {24,S}
8  C u0 p0 c0 {6,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {10,S} {28,S} {29,S} {30,S}
10 C u1 p0 c0 {7,S} {9,S} {31,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.9611,-0.027759,0.000272812,-3.28366e-07,1.26178e-10,-12414.6,-23.2025], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.79067,0.0891746,-4.34728e-05,1.02948e-08,-9.60738e-13,-12520,20.9746], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 181,
    label = "C10H21(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {5,S} {17,S} {18,S}
4  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {8,S} {19,S} {20,S}
6  C u0 p0 c0 {4,S} {10,S} {23,S} {24,S}
7  C u0 p0 c0 {9,S} {10,S} {21,S} {22,S}
8  C u0 p0 c0 {5,S} {28,S} {29,S} {30,S}
9  C u0 p0 c0 {7,S} {25,S} {26,S} {27,S}
10 C u1 p0 c0 {6,S} {7,S} {31,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.4421,-0.0122306,0.000217421,-2.62118e-07,9.965e-11,-12714.2,-27.075], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.10043,0.087508,-4.25718e-05,1.00655e-08,-9.38227e-13,-12506,15.9472], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 182,
    label = "C10H21(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {4,S} {17,S} {18,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {9,S} {19,S} {20,S}
5  C u0 p0 c0 {6,S} {8,S} {11,S} {12,S}
6  C u0 p0 c0 {5,S} {10,S} {21,S} {22,S}
7  C u0 p0 c0 {3,S} {10,S} {23,S} {24,S}
8  C u0 p0 c0 {5,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {4,S} {28,S} {29,S} {30,S}
10 C u1 p0 c0 {6,S} {7,S} {31,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.1743,-0.033903,0.00028163,-3.35e-07,1.28178e-10,-12958.6,-33.2449], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.0353,0.087385,-4.24163e-05,1.00065e-08,-9.30768e-13,-12877.9,15.5267], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 183,
    label = "C10H21(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {17,S} {18,S}
2  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {8,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {9,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {10,S} {21,S} {22,S}
7  C u0 p0 c0 {3,S} {10,S} {23,S} {24,S}
8  C u0 p0 c0 {4,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {5,S} {28,S} {29,S} {30,S}
10 C u1 p0 c0 {6,S} {7,S} {31,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.0407,0.00872762,0.000161403,-2.04454e-07,7.87396e-11,-13077.1,-22.1191], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.78885,0.0849356,-4.10078e-05,9.63231e-09,-8.92876e-13,-13054.3,8.42587], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 184,
    label = "C10H20",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {6,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {8,S} {21,S} {22,S}
7  C u0 p0 c0 {5,S} {9,S} {23,S} {24,S}
8  C u0 p0 c0 {6,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {10,D} {28,S}
10 C u0 p0 c0 {9,D} {29,S} {30,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {10,S}
30 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.1519,-0.00529876,0.000224441,-2.87724e-07,1.13899e-10,-20421.7,-7.03835], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.38408,0.0842002,-4.08592e-05,9.64017e-09,-8.97003e-13,-21352.1,12.4405], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 185,
    label = "C10H20(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {5,S} {17,S} {18,S}
4  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {7,S} {19,S} {20,S}
6  C u0 p0 c0 {4,S} {9,S} {21,S} {22,S}
7  C u0 p0 c0 {5,S} {23,S} {24,S} {25,S}
8  C u0 p0 c0 {10,S} {26,S} {27,S} {28,S}
9  C u0 p0 c0 {6,S} {10,D} {30,S}
10 C u0 p0 c0 {8,S} {9,D} {29,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {10,S}
30 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.3527,0.00958124,0.000166721,-2.16326e-07,8.48174e-11,-21719.1,-13.6933], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.59659,0.0832707,-4.03418e-05,9.50518e-09,-8.83485e-13,-22104.1,8.96697], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 186,
    label = "C10H20(2)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {15,S} {16,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {7,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {10,S} {21,S} {22,S}
6  C u0 p0 c0 {8,S} {9,S} {19,S} {20,S}
7  C u0 p0 c0 {4,S} {26,S} {27,S} {28,S}
8  C u0 p0 c0 {6,S} {23,S} {24,S} {25,S}
9  C u0 p0 c0 {6,S} {10,D} {29,S}
10 C u0 p0 c0 {5,S} {9,D} {30,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.0046,-0.00192865,0.000200615,-2.53209e-07,9.86381e-11,-21433.6,-14.5885], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.23749,0.0839269,-4.07808e-05,9.63412e-09,-8.9752e-13,-21932.6,11.1764], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 187,
    label = "C10H20(3)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {8,S} {17,S} {18,S}
4  C u0 p0 c0 {5,S} {7,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {9,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {10,S} {21,S} {22,S}
7  C u0 p0 c0 {4,S} {23,S} {24,S} {25,S}
8  C u0 p0 c0 {3,S} {26,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {10,D} {29,S}
10 C u0 p0 c0 {6,S} {9,D} {30,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.9754,-0.00905445,0.000202783,-2.4453e-07,9.26642e-11,-22568.3,-25.7732], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.10365,0.0853989,-4.15894e-05,9.8431e-09,-9.18331e-13,-22342.6,15.6633], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 188,
    label = "C10H20(4)",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
2  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {8,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {9,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {10,S} {21,S} {22,S}
7  C u0 p0 c0 {3,S} {23,S} {24,S} {25,S}
8  C u0 p0 c0 {4,S} {26,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {10,D} {29,S}
10 C u0 p0 c0 {6,S} {9,D} {30,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.9762,-0.00309732,0.000195391,-2.4259e-07,9.34219e-11,-22333.8,-20.6677], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.1427,0.0840637,-4.0861e-05,9.65591e-09,-8.99778e-13,-22527.3,10.8155], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 189,
    label = "C10H21O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {9,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {10,S} {12,S} {13,S}
9  C u0 p0 c0 {7,S} {11,S} {28,S} {29,S}
10 C u0 p0 c0 {8,S} {30,S} {31,S} {32,S}
11 O u0 p2 c0 {9,S} {33,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 O u1 p2 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.9679,0.0112539,0.000182536,-2.3591e-07,9.18677e-11,-28400.4,-9.51175], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.84626,0.0924076,-4.53171e-05,1.07914e-08,-1.01216e-12,-29003.8,13.442], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 190,
    label = "C10H21O2(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {7,S} {25,S} {26,S}
3  C u0 p0 c0 {4,S} {8,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {5,S} {17,S} {18,S}
5  C u0 p0 c0 {4,S} {6,S} {19,S} {20,S}
6  C u0 p0 c0 {5,S} {7,S} {21,S} {22,S}
7  C u0 p0 c0 {2,S} {6,S} {23,S} {24,S}
8  C u0 p0 c0 {3,S} {10,S} {13,S} {14,S}
9  C u0 p0 c0 {1,S} {30,S} {31,S} {32,S}
10 C u0 p0 c0 {8,S} {27,S} {28,S} {29,S}
11 O u0 p2 c0 {1,S} {33,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {2,S}
27 H u0 p0 c0 {10,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {10,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 O u1 p2 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.287,-0.0103669,0.000244655,-3.03553e-07,1.17307e-10,-30463.1,-19.1349], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.41549,0.0926169,-4.55601e-05,1.08799e-08,-1.02296e-12,-31287.3,9.04296], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 191,
    label = "C10H21O2(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {23,S} {24,S}
3  C u0 p0 c0 {4,S} {8,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {5,S} {17,S} {18,S}
5  C u0 p0 c0 {4,S} {6,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {5,S} {21,S} {22,S}
7  C u0 p0 c0 {1,S} {10,S} {25,S} {26,S}
8  C u0 p0 c0 {3,S} {9,S} {13,S} {14,S}
9  C u0 p0 c0 {8,S} {27,S} {28,S} {29,S}
10 C u0 p0 c0 {7,S} {30,S} {31,S} {32,S}
11 O u0 p2 c0 {1,S} {33,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 O u1 p2 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.2313,0.00659717,0.000194744,-2.5168e-07,9.87643e-11,-30902.1,-16.8448], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.37634,0.0895672,-4.36651e-05,1.03451e-08,-9.66103e-13,-31622.5,4.33298], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 192,
    label = "C10H21O2(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {21,S} {22,S}
3  C u0 p0 c0 {1,S} {8,S} {23,S} {24,S}
4  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {6,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {5,S} {19,S} {20,S}
7  C u0 p0 c0 {4,S} {9,S} {13,S} {14,S}
8  C u0 p0 c0 {3,S} {10,S} {25,S} {26,S}
9  C u0 p0 c0 {7,S} {27,S} {28,S} {29,S}
10 C u0 p0 c0 {8,S} {30,S} {31,S} {32,S}
11 O u0 p2 c0 {1,S} {33,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 O u1 p2 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.6895,-0.0229181,0.000276122,-3.40369e-07,1.32453e-10,-30735.8,-32.1072], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.12971,0.088961,-4.34658e-05,1.0317e-08,-9.64958e-13,-31574.3,-1.69668], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 193,
    label = "C10H21O2(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {5,S} {19,S} {20,S}
3  C u0 p0 c0 {1,S} {6,S} {21,S} {22,S}
4  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {8,S} {23,S} {24,S}
7  C u0 p0 c0 {4,S} {9,S} {13,S} {14,S}
8  C u0 p0 c0 {6,S} {10,S} {25,S} {26,S}
9  C u0 p0 c0 {7,S} {27,S} {28,S} {29,S}
10 C u0 p0 c0 {8,S} {30,S} {31,S} {32,S}
11 O u0 p2 c0 {1,S} {33,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 O u1 p2 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.7008,-0.024812,0.000277993,-3.39371e-07,1.31244e-10,-30714.9,-32.18], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.25589,0.0900914,-4.40915e-05,1.04805e-08,-9.8141e-13,-31377.9,2.54909], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 194,
    label = "C10H21O2(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {6,S} {21,S} {22,S}
5  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
6  C u0 p0 c0 {4,S} {10,S} {23,S} {24,S}
7  C u0 p0 c0 {8,S} {10,S} {25,S} {26,S}
8  C u0 p0 c0 {7,S} {11,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {29,S} {30,S} {31,S}
10 C u1 p0 c0 {6,S} {7,S} {32,S}
11 O u0 p2 c0 {8,S} {12,S}
12 O u0 p2 c0 {11,S} {33,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.6996,0.00207275,0.000206342,-2.6277e-07,1.02438e-10,-23604.2,-20.2541], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.25229,0.0900827,-4.40233e-05,1.04473e-08,-9.76878e-13,-24328.1,3.14408], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 195,
    label = "C10H21O2(6)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {8,S} {11,S} {13,S}
2  C u0 p0 c0 {3,S} {5,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {7,S} {20,S} {21,S}
5  C u0 p0 c0 {2,S} {9,S} {14,S} {15,S}
6  C u0 p0 c0 {1,S} {10,S} {24,S} {25,S}
7  C u0 p0 c0 {4,S} {10,S} {22,S} {23,S}
8  C u0 p0 c0 {1,S} {29,S} {30,S} {31,S}
9  C u0 p0 c0 {5,S} {26,S} {27,S} {28,S}
10 C u1 p0 c0 {6,S} {7,S} {32,S}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {33,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.004,-0.00672551,0.000250594,-3.2204e-07,1.27487e-10,-24641.5,-13.2172], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.10826,0.0895363,-4.37326e-05,1.03781e-08,-9.70603e-13,-26180.9,-0.281273], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 196,
    label = "C10H21O2(7)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {11,S} {13,S}
2  C u0 p0 c0 {3,S} {5,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {7,S} {18,S} {19,S}
4  C u0 p0 c0 {1,S} {9,S} {20,S} {21,S}
5  C u0 p0 c0 {2,S} {8,S} {14,S} {15,S}
6  C u0 p0 c0 {1,S} {10,S} {24,S} {25,S}
7  C u0 p0 c0 {3,S} {10,S} {22,S} {23,S}
8  C u0 p0 c0 {5,S} {26,S} {27,S} {28,S}
9  C u0 p0 c0 {4,S} {29,S} {30,S} {31,S}
10 C u1 p0 c0 {6,S} {7,S} {32,S}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {33,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.57737,0.0342393,0.000133284,-1.94396e-07,7.91368e-11,-25117.5,-7.93728], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.51903,0.0861927,-4.18225e-05,9.87218e-09,-9.19385e-13,-26722.6,-13.1017], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 197,
    label = "C10H21O2(8)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {11,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {6,S} {9,S} {24,S} {25,S}
8  C u0 p0 c0 {1,S} {10,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {28,S} {29,S} {30,S}
10 C u1 p0 c0 {8,S} {31,S} {32,S}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {33,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.65299,0.0328042,0.000150298,-2.22506e-07,9.23398e-11,-22567.5,-7.51054], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.1162,0.0849231,-4.12928e-05,9.74971e-09,-9.07403e-13,-24641.1,-21.1405], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 198,
    label = "C10H21O2(9)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {11,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {8,S} {22,S} {23,S}
7  C u0 p0 c0 {1,S} {10,S} {24,S} {25,S}
8  C u0 p0 c0 {6,S} {26,S} {27,S} {28,S}
9  C u0 p0 c0 {10,S} {29,S} {30,S} {31,S}
10 C u1 p0 c0 {7,S} {9,S} {32,S}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {33,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[18.1868,-0.030091,0.000288774,-3.51087e-07,1.35884e-10,-24509.2,-38.9013], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.63197,0.0874385,-4.25164e-05,1.00483e-08,-9.36346e-13,-25208.9,-4.04937], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 199,
    label = "C10H21O2(10)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {11,S} {13,S}
2  C u0 p0 c0 {1,S} {5,S} {18,S} {19,S}
3  C u0 p0 c0 {4,S} {7,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {9,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {10,S} {24,S} {25,S}
7  C u0 p0 c0 {3,S} {10,S} {22,S} {23,S}
8  C u0 p0 c0 {4,S} {26,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {29,S} {30,S} {31,S}
10 C u1 p0 c0 {6,S} {7,S} {32,S}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {33,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.20358,0.0288252,0.000163918,-2.36911e-07,9.73187e-11,-24281.4,-4.15142], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.0238,0.0846812,-4.11876e-05,9.74683e-09,-9.09859e-13,-26679.9,-20.7829], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 200,
    label = "C10H21O2(11)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {11,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {8,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {10,S} {24,S} {25,S}
7  C u0 p0 c0 {9,S} {10,S} {22,S} {23,S}
8  C u0 p0 c0 {5,S} {29,S} {30,S} {31,S}
9  C u0 p0 c0 {7,S} {26,S} {27,S} {28,S}
10 C u1 p0 c0 {6,S} {7,S} {32,S}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {33,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.3128,0.040645,0.000100703,-1.5271e-07,6.20996e-11,-24343,-17.2408], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.83609,0.084104,-4.0507e-05,9.49712e-09,-8.79169e-13,-25481.6,-18.218], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 201,
    label = "C10H21O2(12)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {11,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {9,S} {20,S} {21,S}
5  C u0 p0 c0 {7,S} {8,S} {14,S} {15,S}
6  C u0 p0 c0 {1,S} {10,S} {24,S} {25,S}
7  C u0 p0 c0 {5,S} {10,S} {22,S} {23,S}
8  C u0 p0 c0 {5,S} {26,S} {27,S} {28,S}
9  C u0 p0 c0 {4,S} {29,S} {30,S} {31,S}
10 C u1 p0 c0 {6,S} {7,S} {32,S}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {33,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.6167,-0.00193653,0.000213828,-2.72036e-07,1.06442e-10,-24899,-30.181], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.89991,0.0856066,-4.14479e-05,9.76222e-09,-9.07221e-13,-25841.7,-10.7841], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 202,
    label = "C10H21O4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {12,S} {14,S}
2  C u0 p0 c0 {1,S} {6,S} {25,S} {26,S}
3  C u0 p0 c0 {4,S} {8,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {2,S} {5,S} {23,S} {24,S}
7  C u0 p0 c0 {1,S} {9,S} {27,S} {28,S}
8  C u0 p0 c0 {3,S} {10,S} {15,S} {16,S}
9  C u0 p0 c0 {7,S} {11,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {31,S} {32,S} {33,S}
11 O u0 p2 c0 {9,S} {13,S}
12 O u0 p2 c0 {1,S} {34,S}
13 O u0 p2 c0 {11,S} {35,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {2,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 O u1 p2 c0 {12,S}
35 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.7586,-0.00970069,0.000273311,-3.50229e-07,1.38117e-10,-41038.7,-23.0502], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.2409,0.0915341,-4.54051e-05,1.0921e-08,-1.03325e-12,-43357,-19.3157], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 203,
    label = "C10H21O4(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {12,S} {14,S}
2  C u0 p0 c0 {3,S} {9,S} {11,S} {15,S}
3  C u0 p0 c0 {1,S} {2,S} {26,S} {27,S}
4  C u0 p0 c0 {1,S} {7,S} {24,S} {25,S}
5  C u0 p0 c0 {6,S} {8,S} {18,S} {19,S}
6  C u0 p0 c0 {5,S} {7,S} {20,S} {21,S}
7  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
8  C u0 p0 c0 {5,S} {10,S} {16,S} {17,S}
9  C u0 p0 c0 {2,S} {31,S} {32,S} {33,S}
10 C u0 p0 c0 {8,S} {28,S} {29,S} {30,S}
11 O u0 p2 c0 {2,S} {13,S}
12 O u0 p2 c0 {1,S} {34,S}
13 O u0 p2 c0 {11,S} {35,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {10,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {9,S}
34 O u1 p2 c0 {12,S}
35 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.7163,-0.0121681,0.000283733,-3.60847e-07,1.41662e-10,-42725.7,-24.0487], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.00092,0.0961003,-4.88351e-05,1.19809e-08,-1.15166e-12,-44932.9,-15.1257], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 204,
    label = "C10H21O4(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {7,S} {11,S} {15,S}
2  C u0 p0 c0 {3,S} {4,S} {12,S} {14,S}
3  C u0 p0 c0 {1,S} {2,S} {24,S} {25,S}
4  C u0 p0 c0 {2,S} {6,S} {22,S} {23,S}
5  C u0 p0 c0 {6,S} {8,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {5,S} {20,S} {21,S}
7  C u0 p0 c0 {1,S} {10,S} {26,S} {27,S}
8  C u0 p0 c0 {5,S} {9,S} {16,S} {17,S}
9  C u0 p0 c0 {8,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {7,S} {31,S} {32,S} {33,S}
11 O u0 p2 c0 {1,S} {13,S}
12 O u0 p2 c0 {2,S} {34,S}
13 O u0 p2 c0 {11,S} {35,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 O u1 p2 c0 {12,S}
35 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.0516,0.0234296,0.000200892,-2.85377e-07,1.17056e-10,-42764.5,-9.82964], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.136,0.0875679,-4.29106e-05,1.02175e-08,-9.58758e-13,-45946.2,-35.4933], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 205,
    label = "C10H21O4(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {11,S} {14,S}
2  C u0 p0 c0 {1,S} {6,S} {25,S} {26,S}
3  C u0 p0 c0 {4,S} {8,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {2,S} {5,S} {23,S} {24,S}
7  C u0 p0 c0 {1,S} {9,S} {27,S} {28,S}
8  C u0 p0 c0 {3,S} {10,S} {15,S} {16,S}
9  C u0 p0 c0 {7,S} {12,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {31,S} {32,S} {33,S}
11 O u0 p2 c0 {1,S} {13,S}
12 O u0 p2 c0 {9,S} {34,S}
13 O u0 p2 c0 {11,S} {35,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {2,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 O u1 p2 c0 {12,S}
35 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[28.2896,-0.0796656,0.000407153,-4.67368e-07,1.77123e-10,-41664.7,-72.66], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.15887,0.0914974,-4.47527e-05,1.06205e-08,-9.92624e-13,-41354.5,-0.520656], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 206,
    label = "C10H21O4(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {11,S} {14,S}
2  C u0 p0 c0 {3,S} {9,S} {12,S} {15,S}
3  C u0 p0 c0 {1,S} {2,S} {26,S} {27,S}
4  C u0 p0 c0 {1,S} {7,S} {24,S} {25,S}
5  C u0 p0 c0 {6,S} {8,S} {18,S} {19,S}
6  C u0 p0 c0 {5,S} {7,S} {20,S} {21,S}
7  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
8  C u0 p0 c0 {5,S} {10,S} {16,S} {17,S}
9  C u0 p0 c0 {2,S} {31,S} {32,S} {33,S}
10 C u0 p0 c0 {8,S} {28,S} {29,S} {30,S}
11 O u0 p2 c0 {1,S} {13,S}
12 O u0 p2 c0 {2,S} {34,S}
13 O u0 p2 c0 {11,S} {35,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {10,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {9,S}
34 O u1 p2 c0 {12,S}
35 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.5125,0.000413149,0.000251499,-3.27273e-07,1.29188e-10,-43182.2,-18.2673], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.58948,0.0956151,-4.86693e-05,1.19545e-08,-1.15007e-12,-45543.4,-16.7769], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 207,
    label = "C10H21O4(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {11,S} {15,S}
2  C u0 p0 c0 {3,S} {4,S} {12,S} {14,S}
3  C u0 p0 c0 {1,S} {2,S} {22,S} {23,S}
4  C u0 p0 c0 {2,S} {6,S} {20,S} {21,S}
5  C u0 p0 c0 {1,S} {8,S} {24,S} {25,S}
6  C u0 p0 c0 {4,S} {7,S} {18,S} {19,S}
7  C u0 p0 c0 {6,S} {9,S} {16,S} {17,S}
8  C u0 p0 c0 {5,S} {10,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {31,S} {32,S} {33,S}
11 O u0 p2 c0 {1,S} {13,S}
12 O u0 p2 c0 {2,S} {34,S}
13 O u0 p2 c0 {11,S} {35,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 O u1 p2 c0 {12,S}
35 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.175,0.00506078,0.000226943,-2.98137e-07,1.18077e-10,-43402,-27.0929], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.0935,0.089839,-4.44922e-05,1.06889e-08,-1.01049e-12,-45620.2,-28.0373], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 208,
    label = "C10H21O4(6)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {11,S} {14,S}
2  C u0 p0 c0 {3,S} {7,S} {12,S} {15,S}
3  C u0 p0 c0 {1,S} {2,S} {24,S} {25,S}
4  C u0 p0 c0 {1,S} {6,S} {22,S} {23,S}
5  C u0 p0 c0 {6,S} {8,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {5,S} {20,S} {21,S}
7  C u0 p0 c0 {2,S} {10,S} {26,S} {27,S}
8  C u0 p0 c0 {5,S} {9,S} {16,S} {17,S}
9  C u0 p0 c0 {8,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {7,S} {31,S} {32,S} {33,S}
11 O u0 p2 c0 {1,S} {13,S}
12 O u0 p2 c0 {2,S} {34,S}
13 O u0 p2 c0 {11,S} {35,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 O u1 p2 c0 {12,S}
35 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.302,0.00318232,0.000237526,-3.14143e-07,1.25319e-10,-42713.5,-26.0292], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.3699,0.0876088,-4.31436e-05,1.03246e-08,-9.73214e-13,-45296.6,-33.3575], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 209,
    label = "C10H21O4(7)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {11,S} {14,S}
2  C u0 p0 c0 {3,S} {5,S} {12,S} {15,S}
3  C u0 p0 c0 {1,S} {2,S} {22,S} {23,S}
4  C u0 p0 c0 {1,S} {6,S} {20,S} {21,S}
5  C u0 p0 c0 {2,S} {8,S} {24,S} {25,S}
6  C u0 p0 c0 {4,S} {7,S} {18,S} {19,S}
7  C u0 p0 c0 {6,S} {9,S} {16,S} {17,S}
8  C u0 p0 c0 {5,S} {10,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {31,S} {32,S} {33,S}
11 O u0 p2 c0 {1,S} {13,S}
12 O u0 p2 c0 {2,S} {34,S}
13 O u0 p2 c0 {11,S} {35,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 O u1 p2 c0 {12,S}
35 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.9295,-0.00392655,0.000246001,-3.1616e-07,1.24368e-10,-43411,-33.8699], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.399,0.0894674,-4.42821e-05,1.06319e-08,-1.00451e-12,-45439.9,-28.4141], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 210,
    label = "C10H21O4(8)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {11,S} {15,S}
2  C u0 p0 c0 {1,S} {6,S} {26,S} {27,S}
3  C u0 p0 c0 {4,S} {7,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {2,S} {5,S} {24,S} {25,S}
7  C u0 p0 c0 {3,S} {9,S} {16,S} {17,S}
8  C u0 p0 c0 {1,S} {10,S} {28,S} {29,S}
9  C u0 p0 c0 {7,S} {30,S} {31,S} {32,S}
10 C u1 p0 c0 {8,S} {12,S} {33,S}
11 O u0 p2 c0 {1,S} {13,S}
12 O u0 p2 c0 {10,S} {14,S}
13 O u0 p2 c0 {11,S} {35,S}
14 O u0 p2 c0 {12,S} {34,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {2,S}
27 H u0 p0 c0 {2,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {14,S}
35 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[17.0521,-0.0159189,0.000275791,-3.44891e-07,1.34223e-10,-71998.1,-28.092], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.1939,0.0923022,-4.64983e-05,1.13448e-08,-1.08667e-12,-73817.8,-12.7115], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 211,
    label = "C10H20O3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {11,S} {13,S}
2  C u0 p0 c0 {1,S} {6,S} {24,S} {25,S}
3  C u0 p0 c0 {4,S} {7,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {5,S} {22,S} {23,S}
7  C u0 p0 c0 {3,S} {9,S} {14,S} {15,S}
8  C u0 p0 c0 {1,S} {10,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {31,D} {32,S}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {33,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 O u0 p2 c0 {10,D}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.0138,-0.0138403,0.000254602,-3.13464e-07,1.20385e-10,-57692,-28.8079], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.05182,0.0967883,-5.05546e-05,1.26421e-08,-1.23149e-12,-58528.7,3.65865], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 212,
    label = "C10H20O3(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {11,S} {13,S}
2  C u0 p0 c0 {1,S} {5,S} {22,S} {23,S}
3  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
6  C u0 p0 c0 {3,S} {8,S} {14,S} {15,S}
7  C u0 p0 c0 {1,S} {10,S} {24,S} {25,S}
8  C u0 p0 c0 {6,S} {26,S} {27,S} {28,S}
9  C u0 p0 c0 {10,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {9,S} {32,D}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {33,S}
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
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 O u0 p2 c0 {10,D}
33 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[20.8766,-0.0279554,0.000264141,-3.12787e-07,1.18703e-10,-62840.5,-50.4764], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.04623,0.0937566,-4.71429e-05,1.13963e-08,-1.0785e-12,-62194.5,7.7823], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 213,
    label = "C10H20O3(2)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {11,S} {13,S}
2  C u0 p0 c0 {1,S} {4,S} {20,S} {21,S}
3  C u0 p0 c0 {4,S} {5,S} {16,S} {17,S}
4  C u0 p0 c0 {2,S} {3,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {8,S} {14,S} {15,S}
6  C u0 p0 c0 {1,S} {10,S} {22,S} {23,S}
7  C u0 p0 c0 {9,S} {10,S} {24,S} {25,S}
8  C u0 p0 c0 {5,S} {26,S} {27,S} {28,S}
9  C u0 p0 c0 {7,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {7,S} {32,D}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {33,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 O u0 p2 c0 {10,D}
33 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.2679,0.0187275,0.000146048,-1.90812e-07,7.38506e-11,-63224,-28.7114], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.94097,0.0922884,-4.62511e-05,1.11583e-08,-1.05487e-12,-63089.4,2.80061], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 214,
    label = "C10H20O3(3)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {6,S} {21,S} {22,S}
5  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
6  C u0 p0 c0 {4,S} {10,S} {23,S} {24,S}
7  C u0 p0 c0 {8,S} {10,S} {25,S} {26,S}
8  C u0 p0 c0 {7,S} {11,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {7,S} {32,D}
11 O u0 p2 c0 {8,S} {12,S}
12 O u0 p2 c0 {11,S} {33,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 O u0 p2 c0 {10,D}
33 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.0611,-0.00458558,0.000225643,-2.82004e-07,1.09055e-10,-60140.3,-17.6554], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.14468,0.0959105,-4.86019e-05,1.18462e-08,-1.12995e-12,-60482.5,17.0673], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 215,
    label = "C10H20O3(4)",
    molecule = 
"""
1  C u0 p0 c0 {6,S} {8,S} {11,S} {13,S}
2  C u0 p0 c0 {3,S} {5,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {7,S} {20,S} {21,S}
5  C u0 p0 c0 {2,S} {9,S} {14,S} {15,S}
6  C u0 p0 c0 {1,S} {10,S} {24,S} {25,S}
7  C u0 p0 c0 {4,S} {10,S} {22,S} {23,S}
8  C u0 p0 c0 {1,S} {29,S} {30,S} {31,S}
9  C u0 p0 c0 {5,S} {26,S} {27,S} {28,S}
10 C u0 p0 c0 {6,S} {7,S} {32,D}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {33,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 O u0 p2 c0 {10,D}
33 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.33735,0.0310242,0.000150935,-2.13157e-07,8.56041e-11,-62673.7,-2.74339], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.69464,0.0959233,-4.85686e-05,1.182e-08,-1.12549e-12,-63877.6,3.96235], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 216,
    label = "C10H20O3(5)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {11,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {7,S} {9,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {10,S} {22,S} {23,S}
7  C u0 p0 c0 {5,S} {10,S} {24,S} {25,S}
8  C u0 p0 c0 {4,S} {26,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {7,S} {32,D}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {33,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 O u0 p2 c0 {10,D}
33 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.9152,0.026851,0.000138854,-1.9087e-07,7.55073e-11,-62689,-18.647], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.40146,0.0918798,-4.6106e-05,1.11365e-08,-1.0539e-12,-63225.6,-1.30346], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 217,
    label = "C10H20O3(6)",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {6,S} {11,S} {13,S}
2  C u0 p0 c0 {3,S} {5,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {7,S} {18,S} {19,S}
4  C u0 p0 c0 {1,S} {9,S} {20,S} {21,S}
5  C u0 p0 c0 {2,S} {8,S} {14,S} {15,S}
6  C u0 p0 c0 {1,S} {10,S} {24,S} {25,S}
7  C u0 p0 c0 {3,S} {10,S} {22,S} {23,S}
8  C u0 p0 c0 {5,S} {26,S} {27,S} {28,S}
9  C u0 p0 c0 {4,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {7,S} {32,D}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {33,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 O u0 p2 c0 {10,D}
33 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.7161,0.0142434,0.000188963,-2.52462e-07,1.00467e-10,-62000,-14.1427], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.68227,0.0943662,-4.75434e-05,1.15142e-08,-1.09146e-12,-62874.4,3.06531], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 218,
    label = "C10H20O3(7)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {11,S} {13,S}
2  C u0 p0 c0 {1,S} {5,S} {18,S} {19,S}
3  C u0 p0 c0 {4,S} {7,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {9,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {10,S} {24,S} {25,S}
7  C u0 p0 c0 {3,S} {10,S} {22,S} {23,S}
8  C u0 p0 c0 {4,S} {26,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {7,S} {32,D}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {33,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 O u0 p2 c0 {10,D}
33 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.2859,0.0223335,0.000178489,-2.46323e-07,9.91072e-11,-62274.3,-5.05392], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.38357,0.0949921,-4.80619e-05,1.16927e-08,-1.11323e-12,-63643.9,1.5694], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 219,
    label = "C10H22O2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {9,S} {27,S} {28,S}
8  C u0 p0 c0 {1,S} {10,S} {13,S} {14,S}
9  C u0 p0 c0 {7,S} {11,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {31,S} {32,S} {33,S}
11 O u0 p2 c0 {9,S} {12,S}
12 O u0 p2 c0 {11,S} {34,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[24.996,-0.0787454,0.000406396,-4.68525e-07,1.7845e-10,-46293.6,-58.8555], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.3031,0.0925401,-4.48508e-05,1.05598e-08,-9.80185e-13,-45712.9,16.679], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 220,
    label = "C10H22O2(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {11,S} {13,S}
2  C u0 p0 c0 {1,S} {7,S} {26,S} {27,S}
3  C u0 p0 c0 {4,S} {8,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {2,S} {6,S} {24,S} {25,S}
8  C u0 p0 c0 {3,S} {10,S} {14,S} {15,S}
9  C u0 p0 c0 {1,S} {31,S} {32,S} {33,S}
10 C u0 p0 c0 {8,S} {28,S} {29,S} {30,S}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {34,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {2,S}
27 H u0 p0 c0 {2,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {10,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.0262,-0.0297469,0.000313779,-3.87492e-07,1.51471e-10,-47096.2,-23.138], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.08702,0.0939459,-4.58477e-05,1.0867e-08,-1.01498e-12,-48220.4,6.9752], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 221,
    label = "C10H22O2(2)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {11,S} {13,S}
2  C u0 p0 c0 {1,S} {6,S} {24,S} {25,S}
3  C u0 p0 c0 {4,S} {8,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {5,S} {22,S} {23,S}
7  C u0 p0 c0 {1,S} {10,S} {26,S} {27,S}
8  C u0 p0 c0 {3,S} {9,S} {14,S} {15,S}
9  C u0 p0 c0 {8,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {7,S} {31,S} {32,S} {33,S}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {34,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[17.9205,-0.0242151,0.000277668,-3.39534e-07,1.31593e-10,-47782.9,-35.6066], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.04439,0.091126,-4.41853e-05,1.0415e-08,-9.68208e-13,-48268,1.59882], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 222,
    label = "C10H22O2(3)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {11,S} {13,S}
2  C u0 p0 c0 {1,S} {6,S} {22,S} {23,S}
3  C u0 p0 c0 {1,S} {8,S} {24,S} {25,S}
4  C u0 p0 c0 {5,S} {7,S} {16,S} {17,S}
5  C u0 p0 c0 {4,S} {6,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {5,S} {20,S} {21,S}
7  C u0 p0 c0 {4,S} {9,S} {14,S} {15,S}
8  C u0 p0 c0 {3,S} {10,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {31,S} {32,S} {33,S}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {34,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.1048,-0.00483172,0.000239209,-3.05634e-07,1.20466e-10,-46997.1,-24.3541], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.90388,0.0911188,-4.41415e-05,1.04002e-08,-9.6668e-13,-48043.1,-3.87328], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 223,
    label = "C10H22O2(4)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {11,S} {13,S}
2  C u0 p0 c0 {1,S} {5,S} {20,S} {21,S}
3  C u0 p0 c0 {1,S} {6,S} {22,S} {23,S}
4  C u0 p0 c0 {5,S} {7,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {8,S} {24,S} {25,S}
7  C u0 p0 c0 {4,S} {9,S} {14,S} {15,S}
8  C u0 p0 c0 {6,S} {10,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {31,S} {32,S} {33,S}
11 O u0 p2 c0 {1,S} {12,S}
12 O u0 p2 c0 {11,S} {34,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[20.0957,-0.0144775,0.000233698,-2.8558e-07,1.1011e-10,-47954.9,-46.3168], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.10879,0.0881466,-4.24277e-05,9.93717e-09,-9.18796e-13,-47911.7,-5.7316], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 224,
    label = "C11H24",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {7,S} {23,S} {24,S}
7  C u0 p0 c0 {6,S} {8,S} {25,S} {26,S}
8  C u0 p0 c0 {7,S} {9,S} {27,S} {28,S}
9  C u0 p0 c0 {8,S} {10,S} {29,S} {30,S}
10 C u0 p0 c0 {9,S} {11,S} {31,S} {32,S}
11 C u0 p0 c0 {10,S} {33,S} {34,S} {35,S}
12 H u0 p0 c0 {1,S}
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
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[18.6998,-0.0538938,0.000359501,-4.20033e-07,1.59683e-10,-38657,-38.9084], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.803998,0.102307,-4.98529e-05,1.17997e-08,-1.10061e-12,-38211.7,29.4394], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 225,
    label = "C11H23",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {8,S} {24,S} {25,S}
7  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
8  C u0 p0 c0 {6,S} {10,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {11,S} {28,S} {29,S}
10 C u0 p0 c0 {8,S} {30,S} {31,S} {32,S}
11 C u1 p0 c0 {9,S} {33,S} {34,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[17.2867,-0.0339775,0.000302424,-3.62553e-07,1.39378e-10,-13972.6,-33.7099], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.51161,0.0953767,-4.61996e-05,1.08804e-08,-1.01067e-12,-13947.3,17.0219], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 226,
    label = "C11H23(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {7,S} {22,S} {23,S}
6  C u0 p0 c0 {1,S} {8,S} {12,S} {13,S}
7  C u0 p0 c0 {5,S} {9,S} {24,S} {25,S}
8  C u0 p0 c0 {6,S} {11,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {11,S} {31,S} {32,S} {33,S}
11 C u1 p0 c0 {8,S} {10,S} {34,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.0346,-0.0386424,0.000317247,-3.75382e-07,1.42899e-10,-15370.3,-31.6849], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.0592,0.0991886,-4.85503e-05,1.15388e-08,-1.08024e-12,-15312.4,23.8501], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 227,
    label = "C11H23(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {6,S} {20,S} {21,S}
5  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {9,S} {22,S} {23,S}
7  C u0 p0 c0 {5,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {10,S} {11,S} {24,S} {25,S}
9  C u0 p0 c0 {6,S} {31,S} {32,S} {33,S}
10 C u0 p0 c0 {8,S} {28,S} {29,S} {30,S}
11 C u1 p0 c0 {7,S} {8,S} {34,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {10,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.6924,-0.0167971,0.000261861,-3.18802e-07,1.22348e-10,-15739.8,-22.8738], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.7902,0.0981287,-4.79212e-05,1.1367e-08,-1.06241e-12,-15899.9,20.1055], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 228,
    label = "C11H23(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {5,S} {20,S} {21,S}
4  C u0 p0 c0 {1,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {10,S} {22,S} {23,S}
6  C u0 p0 c0 {7,S} {9,S} {12,S} {13,S}
7  C u0 p0 c0 {6,S} {11,S} {24,S} {25,S}
8  C u0 p0 c0 {4,S} {11,S} {26,S} {27,S}
9  C u0 p0 c0 {6,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {5,S} {31,S} {32,S} {33,S}
11 C u1 p0 c0 {7,S} {8,S} {34,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.2096,0.00354239,0.000214519,-2.73945e-07,1.07102e-10,-15613.4,-10.3488], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.60235,0.0968522,-4.71368e-05,1.11491e-08,-1.03961e-12,-16087.8,18.6301], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 229,
    label = "C11H23(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
2  C u0 p0 c0 {1,S} {6,S} {20,S} {21,S}
3  C u0 p0 c0 {5,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {8,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {9,S} {12,S} {13,S}
6  C u0 p0 c0 {2,S} {10,S} {22,S} {23,S}
7  C u0 p0 c0 {3,S} {11,S} {24,S} {25,S}
8  C u0 p0 c0 {4,S} {11,S} {26,S} {27,S}
9  C u0 p0 c0 {5,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {31,S} {32,S} {33,S}
11 C u1 p0 c0 {7,S} {8,S} {34,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {1,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.1812,-0.0255672,0.000283498,-3.41782e-07,1.3106e-10,-15790.7,-30.2441], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.33533,0.0972772,-4.7394e-05,1.12186e-08,-1.04662e-12,-15898.5,16.4535], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 230,
    label = "C11H23(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {14,S} {15,S}
2  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
3  C u0 p0 c0 {1,S} {7,S} {16,S} {17,S}
4  C u0 p0 c0 {2,S} {8,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
6  C u0 p0 c0 {2,S} {10,S} {22,S} {23,S}
7  C u0 p0 c0 {3,S} {11,S} {24,S} {25,S}
8  C u0 p0 c0 {4,S} {11,S} {26,S} {27,S}
9  C u0 p0 c0 {5,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {31,S} {32,S} {33,S}
11 C u1 p0 c0 {7,S} {8,S} {34,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.0306,-0.00445982,0.000216618,-2.63749e-07,1.00035e-10,-15924.3,-26.5528], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.67044,0.0968612,-4.71845e-05,1.11704e-08,-1.04245e-12,-15804.8,16.1303], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 231,
    label = "C11H22",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {7,S} {22,S} {23,S}
6  C u0 p0 c0 {1,S} {8,S} {12,S} {13,S}
7  C u0 p0 c0 {5,S} {9,S} {24,S} {25,S}
8  C u0 p0 c0 {6,S} {10,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {11,D} {31,S}
11 C u0 p0 c0 {10,D} {32,S} {33,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.0755,-0.0143251,0.000265527,-3.33025e-07,1.30561e-10,-23521.7,-13.3902], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.99183,0.0935566,-4.5479e-05,1.07456e-08,-1.00102e-12,-24340.3,15.2792], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 232,
    label = "C11H22(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {6,S} {20,S} {21,S}
5  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {8,S} {22,S} {23,S}
7  C u0 p0 c0 {5,S} {10,S} {24,S} {25,S}
8  C u0 p0 c0 {6,S} {26,S} {27,S} {28,S}
9  C u0 p0 c0 {11,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {11,D} {33,S}
11 C u0 p0 c0 {9,S} {10,D} {32,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.4742,0.00421134,0.000211242,-2.70773e-07,1.05994e-10,-25192.8,-9.61543], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.52422,0.0950403,-4.6387e-05,1.09991e-08,-1.02779e-12,-25819.6,16.1182], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 233,
    label = "C11H22(2)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {5,S} {18,S} {19,S}
4  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {8,S} {20,S} {21,S}
6  C u0 p0 c0 {4,S} {11,S} {24,S} {25,S}
7  C u0 p0 c0 {9,S} {10,S} {22,S} {23,S}
8  C u0 p0 c0 {5,S} {29,S} {30,S} {31,S}
9  C u0 p0 c0 {7,S} {26,S} {27,S} {28,S}
10 C u0 p0 c0 {7,S} {11,D} {32,S}
11 C u0 p0 c0 {6,S} {10,D} {33,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.741,0.013697,0.00017219,-2.22344e-07,8.62551e-11,-24859.5,-16.6397], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.13203,0.0929219,-4.52111e-05,1.06933e-08,-9.97216e-13,-25204.8,9.53064], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 234,
    label = "C11H22(3)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {4,S} {18,S} {19,S}
3  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {9,S} {20,S} {21,S}
5  C u0 p0 c0 {6,S} {8,S} {12,S} {13,S}
6  C u0 p0 c0 {5,S} {10,S} {22,S} {23,S}
7  C u0 p0 c0 {3,S} {11,S} {24,S} {25,S}
8  C u0 p0 c0 {5,S} {26,S} {27,S} {28,S}
9  C u0 p0 c0 {4,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {11,D} {32,S}
11 C u0 p0 c0 {7,S} {10,D} {33,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.5027,0.000536464,0.000205012,-2.54055e-07,9.71715e-11,-25433.4,-19.3944], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.47379,0.0952038,-4.65203e-05,1.1043e-08,-1.03295e-12,-25527.7,17.1669], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 235,
    label = "C11H22(4)",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
2  C u0 p0 c0 {4,S} {6,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {7,S} {16,S} {17,S}
4  C u0 p0 c0 {2,S} {8,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {9,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {10,S} {22,S} {23,S}
7  C u0 p0 c0 {3,S} {11,S} {24,S} {25,S}
8  C u0 p0 c0 {4,S} {26,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {11,D} {32,S}
11 C u0 p0 c0 {7,S} {10,D} {33,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {1,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.0002,-0.00040824,0.000206684,-2.55892e-07,9.79121e-11,-25633.7,-20.182], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.02222,0.0944642,-4.61005e-05,1.09316e-08,-1.02162e-12,-25749.7,16.0555], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 236,
    label = "C11H23O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {8,S} {27,S} {28,S}
8  C u0 p0 c0 {7,S} {10,S} {29,S} {30,S}
9  C u0 p0 c0 {1,S} {11,S} {13,S} {14,S}
10 C u0 p0 c0 {8,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 O u0 p2 c0 {10,S} {36,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 O u1 p2 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[23.8003,-0.0671215,0.000379625,-4.31729e-07,1.61455e-10,-32540.8,-54.1322], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.07388,0.1024,-5.03126e-05,1.19941e-08,-1.12557e-12,-31677.3,27.2256], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 237,
    label = "C11H23O2(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {10,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {8,S} {28,S} {29,S}
3  C u0 p0 c0 {4,S} {9,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {6,S} {8,S} {24,S} {25,S}
8  C u0 p0 c0 {2,S} {7,S} {26,S} {27,S}
9  C u0 p0 c0 {3,S} {11,S} {14,S} {15,S}
10 C u0 p0 c0 {1,S} {33,S} {34,S} {35,S}
11 C u0 p0 c0 {9,S} {30,S} {31,S} {32,S}
12 O u0 p2 c0 {1,S} {36,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {2,S}
29 H u0 p0 c0 {2,S}
30 H u0 p0 c0 {11,S}
31 H u0 p0 c0 {11,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {10,S}
36 O u1 p2 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.1559,-0.0156809,0.000280969,-3.46699e-07,1.33885e-10,-33753.3,-19.2446], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.79474,0.102302,-5.03701e-05,1.20357e-08,-1.13206e-12,-34617.6,14.1904], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 238,
    label = "C11H23O2(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {7,S} {26,S} {27,S}
3  C u0 p0 c0 {4,S} {9,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {2,S} {6,S} {24,S} {25,S}
8  C u0 p0 c0 {1,S} {11,S} {28,S} {29,S}
9  C u0 p0 c0 {3,S} {10,S} {14,S} {15,S}
10 C u0 p0 c0 {9,S} {30,S} {31,S} {32,S}
11 C u0 p0 c0 {8,S} {33,S} {34,S} {35,S}
12 O u0 p2 c0 {1,S} {36,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {2,S}
27 H u0 p0 c0 {2,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 O u1 p2 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.7512,-0.00950012,0.000267702,-3.35718e-07,1.30648e-10,-33534.7,-21.4995], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.89459,0.100806,-4.9518e-05,1.18092e-08,-1.10901e-12,-34621.7,5.08056], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 239,
    label = "C11H23O2(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {7,S} {24,S} {25,S}
3  C u0 p0 c0 {1,S} {9,S} {26,S} {27,S}
4  C u0 p0 c0 {5,S} {8,S} {16,S} {17,S}
5  C u0 p0 c0 {4,S} {6,S} {18,S} {19,S}
6  C u0 p0 c0 {5,S} {7,S} {20,S} {21,S}
7  C u0 p0 c0 {2,S} {6,S} {22,S} {23,S}
8  C u0 p0 c0 {4,S} {10,S} {14,S} {15,S}
9  C u0 p0 c0 {3,S} {11,S} {28,S} {29,S}
10 C u0 p0 c0 {8,S} {30,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 O u0 p2 c0 {1,S} {36,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 O u1 p2 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.743,-0.00412728,0.00025005,-3.17947e-07,1.24605e-10,-33453.4,-20.7138], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.81392,0.0981817,-4.80084e-05,1.14041e-08,-1.0674e-12,-34529.3,2.41283], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 240,
    label = "C11H23O2(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {6,S} {22,S} {23,S}
3  C u0 p0 c0 {1,S} {7,S} {24,S} {25,S}
4  C u0 p0 c0 {5,S} {8,S} {16,S} {17,S}
5  C u0 p0 c0 {4,S} {6,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {5,S} {20,S} {21,S}
7  C u0 p0 c0 {3,S} {9,S} {26,S} {27,S}
8  C u0 p0 c0 {4,S} {10,S} {14,S} {15,S}
9  C u0 p0 c0 {7,S} {11,S} {28,S} {29,S}
10 C u0 p0 c0 {8,S} {30,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 O u0 p2 c0 {1,S} {36,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 O u1 p2 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.1303,-0.0206488,0.000290635,-3.57207e-07,1.38142e-10,-33689.2,-28.5284], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.38891,0.100281,-4.92638e-05,1.17486e-08,-1.10327e-12,-34503,6.51579], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 241,
    label = "C11H23O2(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {5,S} {20,S} {21,S}
3  C u0 p0 c0 {1,S} {6,S} {22,S} {23,S}
4  C u0 p0 c0 {5,S} {8,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {9,S} {26,S} {27,S}
8  C u0 p0 c0 {4,S} {10,S} {14,S} {15,S}
9  C u0 p0 c0 {7,S} {11,S} {28,S} {29,S}
10 C u0 p0 c0 {8,S} {30,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 O u0 p2 c0 {1,S} {36,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 O u1 p2 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[18.7526,-0.0345043,0.000321673,-3.89082e-07,1.50195e-10,-33865,-37.7117], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.89311,0.09919,-4.84806e-05,1.15085e-08,-1.07633e-12,-34361.4,6.78869], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 242,
    label = "C11H23O2(6)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {7,S} {24,S} {25,S}
6  C u0 p0 c0 {1,S} {10,S} {14,S} {15,S}
7  C u0 p0 c0 {5,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {9,S} {11,S} {28,S} {29,S}
9  C u0 p0 c0 {8,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u1 p0 c0 {7,S} {8,S} {35,S}
12 O u0 p2 c0 {9,S} {13,S}
13 O u0 p2 c0 {12,S} {36,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.6154,-0.00202426,0.000253552,-3.25739e-07,1.28171e-10,-26221.6,-18.3705], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.32937,0.0978507,-4.7947e-05,1.14111e-08,-1.06986e-12,-27812.9,-4.14699], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 243,
    label = "C11H23O2(7)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {7,S} {9,S} {12,S} {14,S}
2  C u0 p0 c0 {3,S} {6,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {8,S} {23,S} {24,S}
6  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
7  C u0 p0 c0 {1,S} {11,S} {27,S} {28,S}
8  C u0 p0 c0 {5,S} {11,S} {25,S} {26,S}
9  C u0 p0 c0 {1,S} {32,S} {33,S} {34,S}
10 C u0 p0 c0 {6,S} {29,S} {30,S} {31,S}
11 C u1 p0 c0 {7,S} {8,S} {35,S}
12 O u0 p2 c0 {1,S} {13,S}
13 O u0 p2 c0 {12,S} {36,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {10,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {9,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.4429,0.0111619,0.000226062,-2.99406e-07,1.18782e-10,-28110.4,-10.3059], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.26196,0.0989015,-4.86438e-05,1.1615e-08,-1.0921e-12,-30011.1,-5.51686], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 244,
    label = "C11H23O2(8)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {5,S} {7,S} {12,S} {14,S}
2  C u0 p0 c0 {3,S} {6,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {8,S} {21,S} {22,S}
5  C u0 p0 c0 {1,S} {10,S} {23,S} {24,S}
6  C u0 p0 c0 {2,S} {9,S} {15,S} {16,S}
7  C u0 p0 c0 {1,S} {11,S} {27,S} {28,S}
8  C u0 p0 c0 {4,S} {11,S} {25,S} {26,S}
9  C u0 p0 c0 {6,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {5,S} {32,S} {33,S} {34,S}
11 C u1 p0 c0 {7,S} {8,S} {35,S}
12 O u0 p2 c0 {1,S} {13,S}
13 O u0 p2 c0 {12,S} {36,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.5013,-0.00639498,0.000258761,-3.29268e-07,1.29351e-10,-28090.3,-25.2371], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.95578,0.097227,-4.74226e-05,1.12406e-08,-1.05022e-12,-29341.3,-4.5469], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 245,
    label = "C11H23O2(9)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {12,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {7,S} {23,S} {24,S}
7  C u0 p0 c0 {6,S} {8,S} {25,S} {26,S}
8  C u0 p0 c0 {7,S} {10,S} {27,S} {28,S}
9  C u0 p0 c0 {1,S} {11,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {31,S} {32,S} {33,S}
11 C u1 p0 c0 {9,S} {34,S} {35,S}
12 O u0 p2 c0 {1,S} {13,S}
13 O u0 p2 c0 {12,S} {36,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.9349,-0.0229429,0.000297236,-3.67827e-07,1.43433e-10,-25929.3,-29.4295], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.68605,0.0973924,-4.74176e-05,1.12183e-08,-1.04627e-12,-26829.3,3.12975], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 246,
    label = "C11H23O2(10)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {12,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {7,S} {23,S} {24,S}
7  C u0 p0 c0 {6,S} {9,S} {25,S} {26,S}
8  C u0 p0 c0 {1,S} {11,S} {27,S} {28,S}
9  C u0 p0 c0 {7,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {11,S} {32,S} {33,S} {34,S}
11 C u1 p0 c0 {8,S} {10,S} {35,S}
12 O u0 p2 c0 {1,S} {13,S}
13 O u0 p2 c0 {12,S} {36,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[20.89,-0.0171388,0.000259952,-3.20592e-07,1.24582e-10,-27953,-47.4254], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.0503,0.0929822,-4.49082e-05,1.05448e-08,-9.76859e-13,-28226.5,-9.22792], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 247,
    label = "C11H23O2(11)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {12,S} {14,S}
2  C u0 p0 c0 {1,S} {6,S} {21,S} {22,S}
3  C u0 p0 c0 {4,S} {5,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {8,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {9,S} {15,S} {16,S}
6  C u0 p0 c0 {2,S} {10,S} {23,S} {24,S}
7  C u0 p0 c0 {1,S} {11,S} {27,S} {28,S}
8  C u0 p0 c0 {4,S} {11,S} {25,S} {26,S}
9  C u0 p0 c0 {5,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u1 p0 c0 {7,S} {8,S} {35,S}
12 O u0 p2 c0 {1,S} {13,S}
13 O u0 p2 c0 {12,S} {36,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.2678,0.0357536,0.000150092,-2.16936e-07,8.81372e-11,-28030.3,-10.2907], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.63275,0.0948729,-4.60504e-05,1.0871e-08,-1.01231e-12,-29696.2,-13.6929], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 248,
    label = "C11H23O2(12)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {12,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {9,S} {23,S} {24,S}
7  C u0 p0 c0 {1,S} {11,S} {27,S} {28,S}
8  C u0 p0 c0 {10,S} {11,S} {25,S} {26,S}
9  C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
10 C u0 p0 c0 {8,S} {29,S} {30,S} {31,S}
11 C u1 p0 c0 {7,S} {8,S} {35,S}
12 O u0 p2 c0 {1,S} {13,S}
13 O u0 p2 c0 {12,S} {36,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {10,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {9,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.0128,-0.00982269,0.000260392,-3.27242e-07,1.27744e-10,-27980.8,-31.6005], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.50836,0.0964718,-4.69775e-05,1.11181e-08,-1.03737e-12,-29001.1,-6.05508], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 249,
    label = "C11H23O2(13)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {12,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {20,S}
3  C u0 p0 c0 {2,S} {6,S} {21,S} {22,S}
4  C u0 p0 c0 {5,S} {8,S} {17,S} {18,S}
5  C u0 p0 c0 {4,S} {9,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {10,S} {23,S} {24,S}
7  C u0 p0 c0 {1,S} {11,S} {27,S} {28,S}
8  C u0 p0 c0 {4,S} {11,S} {25,S} {26,S}
9  C u0 p0 c0 {5,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u1 p0 c0 {7,S} {8,S} {35,S}
12 O u0 p2 c0 {1,S} {13,S}
13 O u0 p2 c0 {12,S} {36,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.4165,0.0150485,0.000202008,-2.69495e-07,1.07119e-10,-27880.4,-16.9957], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.69521,0.0961386,-4.67631e-05,1.10577e-08,-1.03104e-12,-29288.5,-7.56673], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 250,
    label = "C11H23O2(14)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {12,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {10,S} {23,S} {24,S}
6  C u0 p0 c0 {8,S} {9,S} {15,S} {16,S}
7  C u0 p0 c0 {1,S} {11,S} {27,S} {28,S}
8  C u0 p0 c0 {6,S} {11,S} {25,S} {26,S}
9  C u0 p0 c0 {6,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {5,S} {32,S} {33,S} {34,S}
11 C u1 p0 c0 {7,S} {8,S} {35,S}
12 O u0 p2 c0 {1,S} {13,S}
13 O u0 p2 c0 {12,S} {36,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.8306,0.0460061,0.000102911,-1.53858e-07,6.12586e-11,-27708.7,-13.6706], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.07634,0.0955424,-4.64158e-05,1.0968e-08,-1.02237e-12,-28697.3,-8.88946], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 251,
    label = "C11H23O4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {7,S} {28,S} {29,S}
3  C u0 p0 c0 {4,S} {9,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {2,S} {6,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {3,S} {11,S} {16,S} {17,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 O u0 p2 c0 {10,S} {14,S}
13 O u0 p2 c0 {1,S} {37,S}
14 O u0 p2 c0 {12,S} {38,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {2,S}
29 H u0 p0 c0 {2,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 O u1 p2 c0 {13,S}
38 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.5702,-0.00153823,0.000289388,-3.77479e-07,1.4977e-10,-42755.3,-7.29002], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.50365,0.10511,-5.23296e-05,1.26229e-08,-1.19692e-12,-45439.3,-7.28143], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 252,
    label = "C11H23O4(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {13,S} {15,S}
2  C u0 p0 c0 {3,S} {10,S} {12,S} {16,S}
3  C u0 p0 c0 {1,S} {2,S} {29,S} {30,S}
4  C u0 p0 c0 {1,S} {8,S} {27,S} {28,S}
5  C u0 p0 c0 {6,S} {9,S} {19,S} {20,S}
6  C u0 p0 c0 {5,S} {7,S} {21,S} {22,S}
7  C u0 p0 c0 {6,S} {8,S} {23,S} {24,S}
8  C u0 p0 c0 {4,S} {7,S} {25,S} {26,S}
9  C u0 p0 c0 {5,S} {11,S} {17,S} {18,S}
10 C u0 p0 c0 {2,S} {34,S} {35,S} {36,S}
11 C u0 p0 c0 {9,S} {31,S} {32,S} {33,S}
12 O u0 p2 c0 {2,S} {14,S}
13 O u0 p2 c0 {1,S} {37,S}
14 O u0 p2 c0 {12,S} {38,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {4,S}
29 H u0 p0 c0 {3,S}
30 H u0 p0 c0 {3,S}
31 H u0 p0 c0 {11,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 O u1 p2 c0 {13,S}
38 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.9822,-0.015311,0.00031799,-4.03438e-07,1.5831e-10,-46120.3,-18.8449], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.40382,0.106116,-5.39525e-05,1.32374e-08,-1.27222e-12,-48527.1,-7.85504], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 253,
    label = "C11H23O4(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {8,S} {12,S} {16,S}
2  C u0 p0 c0 {3,S} {4,S} {13,S} {15,S}
3  C u0 p0 c0 {1,S} {2,S} {27,S} {28,S}
4  C u0 p0 c0 {2,S} {7,S} {25,S} {26,S}
5  C u0 p0 c0 {6,S} {9,S} {19,S} {20,S}
6  C u0 p0 c0 {5,S} {7,S} {21,S} {22,S}
7  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
8  C u0 p0 c0 {1,S} {11,S} {29,S} {30,S}
9  C u0 p0 c0 {5,S} {10,S} {17,S} {18,S}
10 C u0 p0 c0 {9,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {8,S} {34,S} {35,S} {36,S}
12 O u0 p2 c0 {1,S} {14,S}
13 O u0 p2 c0 {2,S} {37,S}
14 O u0 p2 c0 {12,S} {38,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {4,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {3,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 O u1 p2 c0 {13,S}
38 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.1718,0.0141282,0.000248023,-3.33961e-07,1.33388e-10,-45515.4,-9.03692], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.33654,0.104904,-5.33151e-05,1.30821e-08,-1.25769e-12,-48453.6,-18.4856], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 254,
    label = "C11H23O4(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {12,S} {15,S}
2  C u0 p0 c0 {1,S} {7,S} {28,S} {29,S}
3  C u0 p0 c0 {4,S} {9,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {2,S} {6,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {3,S} {11,S} {16,S} {17,S}
10 C u0 p0 c0 {8,S} {13,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 O u0 p2 c0 {1,S} {14,S}
13 O u0 p2 c0 {10,S} {37,S}
14 O u0 p2 c0 {12,S} {38,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {2,S}
29 H u0 p0 c0 {2,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 O u1 p2 c0 {13,S}
38 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.5658,-0.0271849,0.00033916,-4.17545e-07,1.61047e-10,-43915.6,-31.3958], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.20759,0.105617,-5.36973e-05,1.31839e-08,-1.26836e-12,-46225.1,-13.0302], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 255,
    label = "C11H23O4(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {12,S} {15,S}
2  C u0 p0 c0 {3,S} {10,S} {13,S} {16,S}
3  C u0 p0 c0 {1,S} {2,S} {29,S} {30,S}
4  C u0 p0 c0 {1,S} {8,S} {27,S} {28,S}
5  C u0 p0 c0 {6,S} {9,S} {19,S} {20,S}
6  C u0 p0 c0 {5,S} {7,S} {21,S} {22,S}
7  C u0 p0 c0 {6,S} {8,S} {23,S} {24,S}
8  C u0 p0 c0 {4,S} {7,S} {25,S} {26,S}
9  C u0 p0 c0 {5,S} {11,S} {17,S} {18,S}
10 C u0 p0 c0 {2,S} {34,S} {35,S} {36,S}
11 C u0 p0 c0 {9,S} {31,S} {32,S} {33,S}
12 O u0 p2 c0 {1,S} {14,S}
13 O u0 p2 c0 {2,S} {37,S}
14 O u0 p2 c0 {12,S} {38,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {4,S}
29 H u0 p0 c0 {3,S}
30 H u0 p0 c0 {3,S}
31 H u0 p0 c0 {11,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 O u1 p2 c0 {13,S}
38 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.9863,-0.00455446,0.000283773,-3.64095e-07,1.42771e-10,-45737.4,-21.122], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.77221,0.104417,-5.30855e-05,1.30308e-08,-1.25321e-12,-48199.3,-15.3489], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 256,
    label = "C11H23O4(6)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {12,S} {15,S}
2  C u0 p0 c0 {3,S} {8,S} {13,S} {16,S}
3  C u0 p0 c0 {1,S} {2,S} {27,S} {28,S}
4  C u0 p0 c0 {1,S} {7,S} {25,S} {26,S}
5  C u0 p0 c0 {6,S} {9,S} {19,S} {20,S}
6  C u0 p0 c0 {5,S} {7,S} {21,S} {22,S}
7  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
8  C u0 p0 c0 {2,S} {11,S} {29,S} {30,S}
9  C u0 p0 c0 {5,S} {10,S} {17,S} {18,S}
10 C u0 p0 c0 {9,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {8,S} {34,S} {35,S} {36,S}
12 O u0 p2 c0 {1,S} {14,S}
13 O u0 p2 c0 {2,S} {37,S}
14 O u0 p2 c0 {12,S} {38,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {4,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {3,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 O u1 p2 c0 {13,S}
38 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.7555,-0.00203593,0.000270429,-3.47987e-07,1.36639e-10,-46512.3,-27.6553], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.1503,0.103377,-5.22763e-05,1.27735e-08,-1.2238e-12,-48662.7,-18.7841], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 257,
    label = "C11H23O4(7)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {12,S} {16,S}
2  C u0 p0 c0 {3,S} {4,S} {13,S} {15,S}
3  C u0 p0 c0 {1,S} {2,S} {23,S} {24,S}
4  C u0 p0 c0 {2,S} {6,S} {21,S} {22,S}
5  C u0 p0 c0 {1,S} {7,S} {25,S} {26,S}
6  C u0 p0 c0 {4,S} {8,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {9,S} {27,S} {28,S}
8  C u0 p0 c0 {6,S} {10,S} {17,S} {18,S}
9  C u0 p0 c0 {7,S} {11,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 O u0 p2 c0 {1,S} {14,S}
13 O u0 p2 c0 {2,S} {37,S}
14 O u0 p2 c0 {12,S} {38,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 O u1 p2 c0 {13,S}
38 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.0583,0.0143283,0.000223932,-2.99675e-07,1.1906e-10,-45933.3,-25.1734], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.8627,0.0977236,-4.8435e-05,1.16553e-08,-1.1038e-12,-48446.4,-30.9546], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 258,
    label = "C11H23O4(8)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {12,S} {15,S}
2  C u0 p0 c0 {3,S} {5,S} {13,S} {16,S}
3  C u0 p0 c0 {1,S} {2,S} {25,S} {26,S}
4  C u0 p0 c0 {1,S} {7,S} {23,S} {24,S}
5  C u0 p0 c0 {2,S} {9,S} {27,S} {28,S}
6  C u0 p0 c0 {7,S} {8,S} {19,S} {20,S}
7  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
8  C u0 p0 c0 {6,S} {10,S} {17,S} {18,S}
9  C u0 p0 c0 {5,S} {11,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 O u0 p2 c0 {1,S} {14,S}
13 O u0 p2 c0 {2,S} {37,S}
14 O u0 p2 c0 {12,S} {38,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {5,S}
28 H u0 p0 c0 {5,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 O u1 p2 c0 {13,S}
38 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.8901,0.0430186,0.000144476,-2.14013e-07,8.69692e-11,-45619.6,-12.2656], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.1483,0.0979364,-4.81631e-05,1.15006e-08,-1.08158e-12,-47892,-25.806], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 259,
    label = "C11H22O3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {12,S} {14,S}
2  C u0 p0 c0 {1,S} {7,S} {27,S} {28,S}
3  C u0 p0 c0 {4,S} {8,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {7,S} {23,S} {24,S}
7  C u0 p0 c0 {2,S} {6,S} {25,S} {26,S}
8  C u0 p0 c0 {3,S} {10,S} {15,S} {16,S}
9  C u0 p0 c0 {1,S} {11,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,D} {35,S}
12 O u0 p2 c0 {1,S} {13,S}
13 O u0 p2 c0 {12,S} {36,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {2,S}
28 H u0 p0 c0 {2,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 O u0 p2 c0 {11,D}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.8559,0.000221227,0.000255452,-3.24795e-07,1.26051e-10,-60448.7,-10.3135], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.20069,0.110384,-5.79135e-05,1.45328e-08,-1.41955e-12,-61757.8,14.7527], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 260,
    label = "C11H22O3(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {12,S} {14,S}
2  C u0 p0 c0 {1,S} {6,S} {25,S} {26,S}
3  C u0 p0 c0 {4,S} {7,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {2,S} {5,S} {23,S} {24,S}
7  C u0 p0 c0 {3,S} {9,S} {15,S} {16,S}
8  C u0 p0 c0 {1,S} {11,S} {27,S} {28,S}
9  C u0 p0 c0 {7,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {11,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {8,S} {10,S} {35,D}
12 O u0 p2 c0 {1,S} {13,S}
13 O u0 p2 c0 {12,S} {36,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {2,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 O u0 p2 c0 {11,D}
36 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.2983,0.00491063,0.000233543,-3.00234e-07,1.17381e-10,-65320.4,-14.4499], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.86119,0.10564,-5.33251e-05,1.29556e-08,-1.23262e-12,-66199.8,11.7936], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 261,
    label = "C11H22O3(2)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {12,S} {14,S}
2  C u0 p0 c0 {1,S} {5,S} {23,S} {24,S}
3  C u0 p0 c0 {4,S} {6,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {2,S} {4,S} {21,S} {22,S}
6  C u0 p0 c0 {3,S} {9,S} {15,S} {16,S}
7  C u0 p0 c0 {1,S} {11,S} {25,S} {26,S}
8  C u0 p0 c0 {10,S} {11,S} {27,S} {28,S}
9  C u0 p0 c0 {6,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {8,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {8,S} {35,D}
12 O u0 p2 c0 {1,S} {13,S}
13 O u0 p2 c0 {12,S} {36,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 O u0 p2 c0 {11,D}
36 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.8799,0.0262914,0.000176165,-2.41319e-07,9.61889e-11,-64949.6,-7.46218], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.98121,0.104127,-5.23722e-05,1.26696e-08,-1.20011e-12,-65809.3,9.40157], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 262,
    label = "C11H22O3(3)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {7,S} {24,S} {25,S}
6  C u0 p0 c0 {1,S} {10,S} {14,S} {15,S}
7  C u0 p0 c0 {5,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {9,S} {11,S} {28,S} {29,S}
9  C u0 p0 c0 {8,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {8,S} {35,D}
12 O u0 p2 c0 {9,S} {13,S}
13 O u0 p2 c0 {12,S} {36,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 O u0 p2 c0 {11,D}
36 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[17.5364,-0.0290987,0.000309263,-3.73603e-07,1.43391e-10,-63438.2,-30.3525], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.49752,0.105697,-5.34884e-05,1.30252e-08,-1.24158e-12,-63610.3,20.487], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 263,
    label = "C11H22O3(4)",
    molecule = 
"""
1  C u0 p0 c0 {7,S} {9,S} {12,S} {14,S}
2  C u0 p0 c0 {3,S} {6,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {8,S} {23,S} {24,S}
6  C u0 p0 c0 {2,S} {10,S} {15,S} {16,S}
7  C u0 p0 c0 {1,S} {11,S} {27,S} {28,S}
8  C u0 p0 c0 {5,S} {11,S} {25,S} {26,S}
9  C u0 p0 c0 {1,S} {32,S} {33,S} {34,S}
10 C u0 p0 c0 {6,S} {29,S} {30,S} {31,S}
11 C u0 p0 c0 {7,S} {8,S} {35,D}
12 O u0 p2 c0 {1,S} {13,S}
13 O u0 p2 c0 {12,S} {36,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {10,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {9,S}
35 O u0 p2 c0 {11,D}
36 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.8326,-0.00307477,0.000261085,-3.34393e-07,1.31533e-10,-65583.3,-17.1192], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.13862,0.105083,-5.27828e-05,1.27502e-08,-1.20619e-12,-66583.6,9.18344], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 264,
    label = "C11H22O3(5)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {12,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {21,S} {22,S}
3  C u0 p0 c0 {4,S} {5,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {3,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {9,S} {15,S} {16,S}
6  C u0 p0 c0 {8,S} {10,S} {23,S} {24,S}
7  C u0 p0 c0 {1,S} {11,S} {25,S} {26,S}
8  C u0 p0 c0 {6,S} {11,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {8,S} {35,D}
12 O u0 p2 c0 {1,S} {13,S}
13 O u0 p2 c0 {12,S} {36,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 O u0 p2 c0 {11,D}
36 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[18.0752,-0.0086442,0.000248748,-3.09583e-07,1.19986e-10,-65884.4,-36.9117], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.5577,0.102054,-5.12355e-05,1.23774e-08,-1.17115e-12,-65980,4.91156], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 265,
    label = "C11H22O3(6)",
    molecule = 
"""
1  C u0 p0 c0 {5,S} {7,S} {12,S} {14,S}
2  C u0 p0 c0 {3,S} {6,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {8,S} {21,S} {22,S}
5  C u0 p0 c0 {1,S} {10,S} {23,S} {24,S}
6  C u0 p0 c0 {2,S} {9,S} {15,S} {16,S}
7  C u0 p0 c0 {1,S} {11,S} {27,S} {28,S}
8  C u0 p0 c0 {4,S} {11,S} {25,S} {26,S}
9  C u0 p0 c0 {6,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {5,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {8,S} {35,D}
12 O u0 p2 c0 {1,S} {13,S}
13 O u0 p2 c0 {12,S} {36,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 O u0 p2 c0 {11,D}
36 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.4984,0.00708987,0.000232993,-3.04616e-07,1.20358e-10,-65761.4,-13.9301], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.72342,0.103232,-5.2088e-05,1.26622e-08,-1.20584e-12,-67037,3.90058], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 266,
    label = "C11H22O3(7)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {12,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {20,S}
3  C u0 p0 c0 {2,S} {6,S} {21,S} {22,S}
4  C u0 p0 c0 {5,S} {8,S} {17,S} {18,S}
5  C u0 p0 c0 {4,S} {9,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {10,S} {23,S} {24,S}
7  C u0 p0 c0 {1,S} {11,S} {27,S} {28,S}
8  C u0 p0 c0 {4,S} {11,S} {25,S} {26,S}
9  C u0 p0 c0 {5,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {8,S} {35,D}
12 O u0 p2 c0 {1,S} {13,S}
13 O u0 p2 c0 {12,S} {36,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 O u0 p2 c0 {11,D}
36 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.2745,0.00497275,0.000229932,-2.98263e-07,1.17585e-10,-64799.6,-21.1962], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.97786,0.103224,-5.21837e-05,1.26915e-08,-1.20794e-12,-65569.8,4.96895], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 267,
    label = "C11H22O3(8)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {12,S} {14,S}
2  C u0 p0 c0 {1,S} {6,S} {21,S} {22,S}
3  C u0 p0 c0 {4,S} {5,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {8,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {9,S} {15,S} {16,S}
6  C u0 p0 c0 {2,S} {10,S} {23,S} {24,S}
7  C u0 p0 c0 {1,S} {11,S} {27,S} {28,S}
8  C u0 p0 c0 {4,S} {11,S} {25,S} {26,S}
9  C u0 p0 c0 {5,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {8,S} {35,D}
12 O u0 p2 c0 {1,S} {13,S}
13 O u0 p2 c0 {12,S} {36,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 O u0 p2 c0 {11,D}
36 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.9645,0.0184183,0.000191914,-2.56316e-07,1.01503e-10,-65250.1,-16.8067], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.03706,0.102841,-5.17256e-05,1.25176e-08,-1.1863e-12,-65991.5,4.50445], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 268,
    label = "C11H24O2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {7,S} {26,S} {27,S}
7  C u0 p0 c0 {6,S} {8,S} {28,S} {29,S}
8  C u0 p0 c0 {7,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {1,S} {11,S} {14,S} {15,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 O u0 p2 c0 {10,S} {13,S}
13 O u0 p2 c0 {12,S} {37,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[27.4284,-0.09011,0.000448455,-5.10251e-07,1.92408e-10,-49418.5,-70.0305], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.50645,0.102774,-5.01022e-05,1.1859e-08,-1.10597e-12,-48577.3,19.0455], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 269,
    label = "C11H24O2(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {10,S} {12,S} {14,S}
2  C u0 p0 c0 {1,S} {8,S} {29,S} {30,S}
3  C u0 p0 c0 {4,S} {9,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {7,S} {23,S} {24,S}
7  C u0 p0 c0 {6,S} {8,S} {25,S} {26,S}
8  C u0 p0 c0 {2,S} {7,S} {27,S} {28,S}
9  C u0 p0 c0 {3,S} {11,S} {15,S} {16,S}
10 C u0 p0 c0 {1,S} {34,S} {35,S} {36,S}
11 C u0 p0 c0 {9,S} {31,S} {32,S} {33,S}
12 O u0 p2 c0 {1,S} {13,S}
13 O u0 p2 c0 {12,S} {37,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {2,S}
30 H u0 p0 c0 {2,S}
31 H u0 p0 c0 {11,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[19.8683,-0.0491114,0.000371307,-4.45747e-07,1.722e-10,-50550.1,-37.7573], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.40535,0.102252,-4.98385e-05,1.17993e-08,-1.10092e-12,-51113.3,12.1684], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 270,
    label = "C11H24O2(2)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {12,S} {14,S}
2  C u0 p0 c0 {1,S} {7,S} {27,S} {28,S}
3  C u0 p0 c0 {4,S} {9,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {7,S} {23,S} {24,S}
7  C u0 p0 c0 {2,S} {6,S} {25,S} {26,S}
8  C u0 p0 c0 {1,S} {11,S} {29,S} {30,S}
9  C u0 p0 c0 {3,S} {10,S} {15,S} {16,S}
10 C u0 p0 c0 {9,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {8,S} {34,S} {35,S} {36,S}
12 O u0 p2 c0 {1,S} {13,S}
13 O u0 p2 c0 {12,S} {37,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {2,S}
28 H u0 p0 c0 {2,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.8813,0.00462844,0.000255443,-3.37565e-07,1.35138e-10,-49520.3,-5.16416], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.69512,0.10175,-4.95523e-05,1.17287e-08,-1.09444e-12,-51306.3,3.66458], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 271,
    label = "C11H24O2(3)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {12,S} {14,S}
2  C u0 p0 c0 {1,S} {7,S} {25,S} {26,S}
3  C u0 p0 c0 {1,S} {9,S} {27,S} {28,S}
4  C u0 p0 c0 {5,S} {8,S} {17,S} {18,S}
5  C u0 p0 c0 {4,S} {6,S} {19,S} {20,S}
6  C u0 p0 c0 {5,S} {7,S} {21,S} {22,S}
7  C u0 p0 c0 {2,S} {6,S} {23,S} {24,S}
8  C u0 p0 c0 {4,S} {10,S} {15,S} {16,S}
9  C u0 p0 c0 {3,S} {11,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 O u0 p2 c0 {1,S} {13,S}
13 O u0 p2 c0 {12,S} {37,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {2,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {3,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.9492,-0.00911134,0.000268833,-3.3734e-07,1.31373e-10,-50162.8,-29.2195], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.8487,0.10194,-4.97979e-05,1.18181e-08,-1.10527e-12,-51171.7,-1.35821], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 272,
    label = "C11H24O2(4)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {12,S} {14,S}
2  C u0 p0 c0 {1,S} {6,S} {23,S} {24,S}
3  C u0 p0 c0 {1,S} {7,S} {25,S} {26,S}
4  C u0 p0 c0 {5,S} {8,S} {17,S} {18,S}
5  C u0 p0 c0 {4,S} {6,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {5,S} {21,S} {22,S}
7  C u0 p0 c0 {3,S} {9,S} {27,S} {28,S}
8  C u0 p0 c0 {4,S} {10,S} {15,S} {16,S}
9  C u0 p0 c0 {7,S} {11,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 O u0 p2 c0 {1,S} {13,S}
13 O u0 p2 c0 {12,S} {37,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[21.8394,-0.0275719,0.000290178,-3.49597e-07,1.34318e-10,-51053.1,-50.6567], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.41277,0.0980184,-4.73625e-05,1.11283e-08,-1.03159e-12,-51019.9,-1.1336], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 273,
    label = "C11H24O2(5)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {12,S} {14,S}
2  C u0 p0 c0 {1,S} {5,S} {21,S} {22,S}
3  C u0 p0 c0 {1,S} {6,S} {23,S} {24,S}
4  C u0 p0 c0 {5,S} {8,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
6  C u0 p0 c0 {3,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {9,S} {27,S} {28,S}
8  C u0 p0 c0 {4,S} {10,S} {15,S} {16,S}
9  C u0 p0 c0 {7,S} {11,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 O u0 p2 c0 {1,S} {13,S}
13 O u0 p2 c0 {12,S} {37,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[17.4682,-0.0240599,0.000304057,-3.73976e-07,1.4522e-10,-50333.7,-30.0147], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.15531,0.101301,-4.93312e-05,1.16726e-08,-1.08874e-12,-51055.8,7.49278], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 274,
    label = "C12H26",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {8,S} {26,S} {27,S}
8  C u0 p0 c0 {7,S} {9,S} {28,S} {29,S}
9  C u0 p0 c0 {8,S} {10,S} {30,S} {31,S}
10 C u0 p0 c0 {9,S} {11,S} {32,S} {33,S}
11 C u0 p0 c0 {10,S} {12,S} {34,S} {35,S}
12 C u0 p0 c0 {11,S} {36,S} {37,S} {38,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.1969,-0.0198194,0.000291691,-3.52228e-07,1.34519e-10,-41553.6,-26.9853], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.682437,0.111306,-5.42916e-05,1.28645e-08,-1.20128e-12,-41403.1,27.3758], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 275,
    label = "C12H25",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {9,S} {27,S} {28,S}
8  C u0 p0 c0 {1,S} {10,S} {13,S} {14,S}
9  C u0 p0 c0 {7,S} {11,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 C u1 p0 c0 {10,S} {36,S} {37,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.5935,-0.0208017,0.000314143,-3.89521e-07,1.51709e-10,-17479.1,-15.1302], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.15305,0.108758,-5.32683e-05,1.26649e-08,-1.18534e-12,-18315.9,22.205], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 276,
    label = "C12H25(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {7,S} {23,S} {24,S}
6  C u0 p0 c0 {1,S} {8,S} {13,S} {14,S}
7  C u0 p0 c0 {5,S} {10,S} {25,S} {26,S}
8  C u0 p0 c0 {6,S} {12,S} {29,S} {30,S}
9  C u0 p0 c0 {11,S} {12,S} {27,S} {28,S}
10 C u0 p0 c0 {7,S} {34,S} {35,S} {36,S}
11 C u0 p0 c0 {9,S} {31,S} {32,S} {33,S}
12 C u1 p0 c0 {8,S} {9,S} {37,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {11,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.9678,-0.0309354,0.000316339,-3.77309e-07,1.43561e-10,-18781.4,-33.6713], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.04986,0.108131,-5.29806e-05,1.26036e-08,-1.18091e-12,-18820.1,21.1858], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 277,
    label = "C12H25(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {20,S}
3  C u0 p0 c0 {2,S} {4,S} {21,S} {22,S}
4  C u0 p0 c0 {3,S} {6,S} {23,S} {24,S}
5  C u0 p0 c0 {1,S} {9,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {11,S} {25,S} {26,S}
7  C u0 p0 c0 {8,S} {10,S} {13,S} {14,S}
8  C u0 p0 c0 {7,S} {12,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {12,S} {29,S} {30,S}
10 C u0 p0 c0 {7,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {6,S} {34,S} {35,S} {36,S}
12 C u1 p0 c0 {8,S} {9,S} {37,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79934,0.0653926,7.91785e-05,-1.36977e-07,5.65062e-11,-18420.9,14.4991], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.38325,0.106273,-5.19357e-05,1.23343e-08,-1.15452e-12,-19535.7,13.6029], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 278,
    label = "C12H25(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {19,S} {20,S}
2  C u0 p0 c0 {1,S} {3,S} {21,S} {22,S}
3  C u0 p0 c0 {2,S} {7,S} {23,S} {24,S}
4  C u0 p0 c0 {6,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {9,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {10,S} {13,S} {14,S}
7  C u0 p0 c0 {3,S} {11,S} {25,S} {26,S}
8  C u0 p0 c0 {4,S} {12,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {12,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {7,S} {34,S} {35,S} {36,S}
12 C u1 p0 c0 {8,S} {9,S} {37,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {1,S}
20 H u0 p0 c0 {1,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.1512,-0.0264996,0.000313812,-3.79338e-07,1.45377e-10,-18948.7,-24.08], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.514826,0.108864,-5.33986e-05,1.27144e-08,-1.19214e-12,-19289.9,24.3162], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 279,
    label = "C12H25(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
2  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
3  C u0 p0 c0 {2,S} {7,S} {23,S} {24,S}
4  C u0 p0 c0 {1,S} {8,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {9,S} {19,S} {20,S}
6  C u0 p0 c0 {1,S} {10,S} {13,S} {14,S}
7  C u0 p0 c0 {3,S} {11,S} {25,S} {26,S}
8  C u0 p0 c0 {4,S} {12,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {12,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {7,S} {34,S} {35,S} {36,S}
12 C u1 p0 c0 {8,S} {9,S} {37,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.3068,-0.0120482,0.000271486,-3.34938e-07,1.29226e-10,-19257.6,-24.429], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.72247,0.105914,-5.173e-05,1.22722e-08,-1.14715e-12,-19644,16.0944], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 280,
    label = "C12H24",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {8,S} {25,S} {26,S}
7  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
8  C u0 p0 c0 {6,S} {10,S} {27,S} {28,S}
9  C u0 p0 c0 {7,S} {11,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {12,D} {34,S}
12 C u0 p0 c0 {11,D} {35,S} {36,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.9353,-0.0360136,0.000336075,-4.03793e-07,1.54836e-10,-25810.1,-27.6596], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.18132,0.10546,-5.17889e-05,1.23458e-08,-1.15888e-12,-26340.9,20.0932], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 281,
    label = "C12H24(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {7,S} {23,S} {24,S}
6  C u0 p0 c0 {1,S} {8,S} {13,S} {14,S}
7  C u0 p0 c0 {5,S} {9,S} {25,S} {26,S}
8  C u0 p0 c0 {6,S} {11,S} {27,S} {28,S}
9  C u0 p0 c0 {7,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {12,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {8,S} {12,D} {36,S}
12 C u0 p0 c0 {10,S} {11,D} {35,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.6027,-0.0123092,0.000261269,-3.17061e-07,1.20726e-10,-28011.3,-23.6198], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.802744,0.106331,-5.21634e-05,1.24238e-08,-1.1653e-12,-28046.5,23.5204], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 282,
    label = "C12H24(2)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {6,S} {21,S} {22,S}
5  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {4,S} {9,S} {23,S} {24,S}
7  C u0 p0 c0 {5,S} {12,S} {27,S} {28,S}
8  C u0 p0 c0 {10,S} {11,S} {25,S} {26,S}
9  C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
10 C u0 p0 c0 {8,S} {29,S} {30,S} {31,S}
11 C u0 p0 c0 {8,S} {12,D} {35,S}
12 C u0 p0 c0 {7,S} {11,D} {36,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {10,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {9,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.5853,-0.0154319,0.000277722,-3.39698e-07,1.30372e-10,-27986.5,-22.0976], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.80918,0.105226,-5.16331e-05,1.23008e-08,-1.15408e-12,-28448.9,18.8171], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 283,
    label = "C12H24(3)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {20,S}
3  C u0 p0 c0 {2,S} {5,S} {21,S} {22,S}
4  C u0 p0 c0 {1,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {10,S} {23,S} {24,S}
6  C u0 p0 c0 {7,S} {9,S} {13,S} {14,S}
7  C u0 p0 c0 {6,S} {11,S} {25,S} {26,S}
8  C u0 p0 c0 {4,S} {12,S} {27,S} {28,S}
9  C u0 p0 c0 {6,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {5,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {12,D} {35,S}
12 C u0 p0 c0 {8,S} {11,D} {36,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.7686,-0.0149166,0.000267251,-3.26784e-07,1.25598e-10,-28182.2,-25.6597], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.70308,0.102434,-4.99483e-05,1.18336e-08,-1.10497e-12,-28372.4,17.739], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 284,
    label = "C12H24(4)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
2  C u0 p0 c0 {1,S} {6,S} {21,S} {22,S}
3  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {8,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {9,S} {13,S} {14,S}
6  C u0 p0 c0 {2,S} {10,S} {23,S} {24,S}
7  C u0 p0 c0 {3,S} {11,S} {25,S} {26,S}
8  C u0 p0 c0 {4,S} {12,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {12,D} {35,S}
12 C u0 p0 c0 {8,S} {11,D} {36,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {1,S}
20 H u0 p0 c0 {1,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[17.206,-0.0395394,0.000336444,-4.00885e-07,1.53309e-10,-28158.1,-34.1626], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.09957,0.104573,-5.11507e-05,1.21498e-08,-1.13688e-12,-28279,20.8071], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 285,
    label = "C12H24(5)",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {15,S} {16,S}
2  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
3  C u0 p0 c0 {1,S} {7,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {8,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
6  C u0 p0 c0 {2,S} {10,S} {23,S} {24,S}
7  C u0 p0 c0 {3,S} {11,S} {25,S} {26,S}
8  C u0 p0 c0 {4,S} {12,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {12,D} {35,S}
12 C u0 p0 c0 {8,S} {11,D} {36,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[17.7299,-0.038407,0.000334787,-4.02152e-07,1.54824e-10,-27936.4,-31.8462], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.24917,0.102948,-5.01932e-05,1.18877e-08,-1.10952e-12,-28129.7,20.2882], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 286,
    label = "C12H25O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {10,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {7,S} {26,S} {27,S}
7  C u0 p0 c0 {6,S} {8,S} {28,S} {29,S}
8  C u0 p0 c0 {7,S} {9,S} {30,S} {31,S}
9  C u0 p0 c0 {8,S} {11,S} {32,S} {33,S}
10 C u0 p0 c0 {1,S} {12,S} {14,S} {15,S}
11 C u0 p0 c0 {9,S} {13,S} {34,S} {35,S}
12 C u0 p0 c0 {10,S} {36,S} {37,S} {38,S}
13 O u0 p2 c0 {11,S} {39,S}
14 H u0 p0 c0 {10,S}
15 H u0 p0 c0 {10,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 O u1 p2 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[35.5748,-0.153454,0.000619689,-6.87358e-07,2.57043e-10,-36088.6,-96.8778], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.67865,0.112042,-5.51489e-05,1.31584e-08,-1.23514e-12,-34467.8,33.348], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 287,
    label = "C12H25O2(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {11,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {9,S} {31,S} {32,S}
3  C u0 p0 c0 {4,S} {10,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {7,S} {23,S} {24,S}
7  C u0 p0 c0 {6,S} {8,S} {25,S} {26,S}
8  C u0 p0 c0 {7,S} {9,S} {27,S} {28,S}
9  C u0 p0 c0 {2,S} {8,S} {29,S} {30,S}
10 C u0 p0 c0 {3,S} {12,S} {15,S} {16,S}
11 C u0 p0 c0 {1,S} {36,S} {37,S} {38,S}
12 C u0 p0 c0 {10,S} {33,S} {34,S} {35,S}
13 O u0 p2 c0 {1,S} {39,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {10,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {2,S}
32 H u0 p0 c0 {2,S}
33 H u0 p0 c0 {12,S}
34 H u0 p0 c0 {12,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {11,S}
39 O u1 p2 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.3882,-0.00539824,0.000304397,-3.92162e-07,1.54935e-10,-36082.2,-7.54841], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.86634,0.111281,-5.48875e-05,1.31373e-08,-1.23759e-12,-38229,4.40917], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 288,
    label = "C12H25O2(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {8,S} {29,S} {30,S}
3  C u0 p0 c0 {4,S} {10,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {7,S} {23,S} {24,S}
7  C u0 p0 c0 {6,S} {8,S} {25,S} {26,S}
8  C u0 p0 c0 {2,S} {7,S} {27,S} {28,S}
9  C u0 p0 c0 {1,S} {12,S} {31,S} {32,S}
10 C u0 p0 c0 {3,S} {11,S} {15,S} {16,S}
11 C u0 p0 c0 {10,S} {33,S} {34,S} {35,S}
12 C u0 p0 c0 {9,S} {36,S} {37,S} {38,S}
13 O u0 p2 c0 {1,S} {39,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {10,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {2,S}
30 H u0 p0 c0 {2,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 O u1 p2 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.8689,-0.00363609,0.000272432,-3.4533e-07,1.34875e-10,-36098.2,-14.9179], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.70829,0.109686,-5.3792e-05,1.28093e-08,-1.20134e-12,-37176.7,12.7907], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 289,
    label = "C12H25O2(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {8,S} {27,S} {28,S}
3  C u0 p0 c0 {1,S} {10,S} {29,S} {30,S}
4  C u0 p0 c0 {5,S} {9,S} {17,S} {18,S}
5  C u0 p0 c0 {4,S} {6,S} {19,S} {20,S}
6  C u0 p0 c0 {5,S} {7,S} {21,S} {22,S}
7  C u0 p0 c0 {6,S} {8,S} {23,S} {24,S}
8  C u0 p0 c0 {2,S} {7,S} {25,S} {26,S}
9  C u0 p0 c0 {4,S} {11,S} {15,S} {16,S}
10 C u0 p0 c0 {3,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 C u0 p0 c0 {10,S} {36,S} {37,S} {38,S}
13 O u0 p2 c0 {1,S} {39,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {2,S}
28 H u0 p0 c0 {2,S}
29 H u0 p0 c0 {3,S}
30 H u0 p0 c0 {3,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 O u1 p2 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[18.3409,-0.0418983,0.000372242,-4.50416e-07,1.73984e-10,-36420.3,-30.05], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.45158,0.110311,-5.42341e-05,1.29396e-08,-1.21537e-12,-37276.1,16.2704], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 290,
    label = "C12H25O2(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {7,S} {25,S} {26,S}
3  C u0 p0 c0 {1,S} {8,S} {27,S} {28,S}
4  C u0 p0 c0 {5,S} {9,S} {17,S} {18,S}
5  C u0 p0 c0 {4,S} {6,S} {19,S} {20,S}
6  C u0 p0 c0 {5,S} {7,S} {21,S} {22,S}
7  C u0 p0 c0 {2,S} {6,S} {23,S} {24,S}
8  C u0 p0 c0 {3,S} {10,S} {29,S} {30,S}
9  C u0 p0 c0 {4,S} {11,S} {15,S} {16,S}
10 C u0 p0 c0 {8,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 C u0 p0 c0 {10,S} {36,S} {37,S} {38,S}
13 O u0 p2 c0 {1,S} {39,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {2,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {3,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 O u1 p2 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[27.3948,-0.0795867,0.00043914,-5.06637e-07,1.92175e-10,-37524.2,-68.3238], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.00683,0.107795,-5.26253e-05,1.24756e-08,-1.16517e-12,-37015.2,13.218], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 291,
    label = "C12H25O2(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {6,S} {23,S} {24,S}
3  C u0 p0 c0 {1,S} {7,S} {25,S} {26,S}
4  C u0 p0 c0 {5,S} {9,S} {17,S} {18,S}
5  C u0 p0 c0 {4,S} {6,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {5,S} {21,S} {22,S}
7  C u0 p0 c0 {3,S} {8,S} {27,S} {28,S}
8  C u0 p0 c0 {7,S} {10,S} {29,S} {30,S}
9  C u0 p0 c0 {4,S} {11,S} {15,S} {16,S}
10 C u0 p0 c0 {8,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 C u0 p0 c0 {10,S} {36,S} {37,S} {38,S}
13 O u0 p2 c0 {1,S} {39,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {3,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 O u1 p2 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[22.1303,-0.0435498,0.000351195,-4.15829e-07,1.5851e-10,-37289.4,-50.0731], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.68002,0.108389,-5.30342e-05,1.26001e-08,-1.17923e-12,-37235.1,10.8497], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 292,
    label = "C12H25O2(6)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {20,S}
3  C u0 p0 c0 {2,S} {4,S} {21,S} {22,S}
4  C u0 p0 c0 {3,S} {5,S} {23,S} {24,S}
5  C u0 p0 c0 {4,S} {6,S} {25,S} {26,S}
6  C u0 p0 c0 {5,S} {8,S} {27,S} {28,S}
7  C u0 p0 c0 {1,S} {11,S} {15,S} {16,S}
8  C u0 p0 c0 {6,S} {12,S} {29,S} {30,S}
9  C u0 p0 c0 {10,S} {12,S} {31,S} {32,S}
10 C u0 p0 c0 {9,S} {13,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {10,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {6,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.122,-0.0149086,0.000305263,-3.81689e-07,1.48734e-10,-29536.6,-21.7894], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.12297,0.109677,-5.3942e-05,1.28731e-08,-1.2094e-12,-30747.1,8.26372], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 293,
    label = "C12H25O2(7)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {8,S} {10,S} {13,S} {15,S}
2  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {9,S} {26,S} {27,S}
7  C u0 p0 c0 {2,S} {11,S} {16,S} {17,S}
8  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
9  C u0 p0 c0 {6,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {1,S} {35,S} {36,S} {37,S}
11 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {10,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.5972,-0.011938,0.000309589,-3.95133e-07,1.56047e-10,-30872.9,-19.1305], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.93451,0.107452,-5.25305e-05,1.24734e-08,-1.16698e-12,-32657.6,-1.09456], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 294,
    label = "C12H25O2(8)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {6,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {9,S} {24,S} {25,S}
6  C u0 p0 c0 {1,S} {11,S} {26,S} {27,S}
7  C u0 p0 c0 {2,S} {10,S} {16,S} {17,S}
8  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
9  C u0 p0 c0 {5,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {6,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.7614,0.000115292,0.000263038,-3.37257e-07,1.32439e-10,-30668.8,-19.8564], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.7926,0.107582,-5.26042e-05,1.24964e-08,-1.16979e-12,-31935.7,2.36266], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 295,
    label = "C12H25O2(9)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {10,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {8,S} {26,S} {27,S}
8  C u0 p0 c0 {7,S} {9,S} {28,S} {29,S}
9  C u0 p0 c0 {8,S} {11,S} {30,S} {31,S}
10 C u0 p0 c0 {1,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u1 p0 c0 {10,S} {37,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.893,0.00353926,0.000267888,-3.52371e-07,1.40596e-10,-28856.5,-15.3083], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.69209,0.104993,-5.11012e-05,1.20889e-08,-1.12757e-12,-30823,-7.39667], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 296,
    label = "C12H25O2(10)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {8,S} {26,S} {27,S}
8  C u0 p0 c0 {7,S} {10,S} {28,S} {29,S}
9  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {8,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {12,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {9,S} {11,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.509,0.00777829,0.000254469,-3.33841e-07,1.3227e-10,-30436,-12.9392], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.82711,0.107772,-5.2801e-05,1.25653e-08,-1.17804e-12,-32239.5,-2.15507], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 297,
    label = "C12H25O2(11)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {7,S} {24,S} {25,S}
3  C u0 p0 c0 {4,S} {6,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {9,S} {22,S} {23,S}
6  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {2,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
9  C u0 p0 c0 {5,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.9721,0.0216767,0.00021054,-2.87017e-07,1.15315e-10,-30853.3,-14.5415], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.63689,0.104899,-5.09638e-05,1.20345e-08,-1.12059e-12,-32437.3,-7.64096], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 298,
    label = "C12H25O2(12)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {10,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
9  C u0 p0 c0 {11,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
11 C u0 p0 c0 {9,S} {32,S} {33,S} {34,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {10,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[18.6501,-0.02874,0.00032929,-4.0211e-07,1.5534e-10,-31169.5,-41.3232], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.71139,0.106657,-5.21736e-05,1.23962e-08,-1.16044e-12,-32101,-2.56217], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 299,
    label = "C12H25O2(13)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {4,S} {22,S} {23,S}
3  C u0 p0 c0 {5,S} {6,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {7,S} {24,S} {25,S}
5  C u0 p0 c0 {3,S} {9,S} {20,S} {21,S}
6  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {4,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
9  C u0 p0 c0 {5,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.196,0.0415652,0.000152526,-2.20602e-07,8.89555e-11,-30788.3,-8.31], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.83646,0.105023,-5.1231e-05,1.21479e-08,-1.1356e-12,-32407.9,-8.65065], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 300,
    label = "C12H25O2(14)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {11,S} {26,S} {27,S}
7  C u0 p0 c0 {9,S} {10,S} {16,S} {17,S}
8  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
9  C u0 p0 c0 {7,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {6,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.4782,-0.0136724,0.000293156,-3.66365e-07,1.42705e-10,-30573.3,-29.8526], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.60122,0.106516,-5.19952e-05,1.23321e-08,-1.15276e-12,-31643,0.494115], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 301,
    label = "C12H25O2(15)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {20,S} {21,S}
3  C u0 p0 c0 {2,S} {4,S} {22,S} {23,S}
4  C u0 p0 c0 {3,S} {7,S} {24,S} {25,S}
5  C u0 p0 c0 {6,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {5,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {4,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
9  C u0 p0 c0 {5,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u1 p0 c0 {8,S} {9,S} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.857,-0.0110858,0.000289614,-3.64601e-07,1.4252e-10,-31069.2,-30.144], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.70149,0.106336,-5.18855e-05,1.23024e-08,-1.1497e-12,-32283.2,-3.28879], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 302,
    label = "C12H25O4(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {14,S} {16,S}
2  C u0 p0 c0 {3,S} {11,S} {13,S} {17,S}
3  C u0 p0 c0 {1,S} {2,S} {32,S} {33,S}
4  C u0 p0 c0 {1,S} {9,S} {30,S} {31,S}
5  C u0 p0 c0 {6,S} {10,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {6,S} {8,S} {24,S} {25,S}
8  C u0 p0 c0 {7,S} {9,S} {26,S} {27,S}
9  C u0 p0 c0 {4,S} {8,S} {28,S} {29,S}
10 C u0 p0 c0 {5,S} {12,S} {18,S} {19,S}
11 C u0 p0 c0 {2,S} {37,S} {38,S} {39,S}
12 C u0 p0 c0 {10,S} {34,S} {35,S} {36,S}
13 O u0 p2 c0 {2,S} {15,S}
14 O u0 p2 c0 {1,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {4,S}
31 H u0 p0 c0 {4,S}
32 H u0 p0 c0 {3,S}
33 H u0 p0 c0 {3,S}
34 H u0 p0 c0 {12,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {11,S}
39 H u0 p0 c0 {11,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.022,-0.00247201,0.000322198,-4.21242e-07,1.67357e-10,-48837.5,-8.06631], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.98388,0.115509,-5.86099e-05,1.43587e-08,-1.37846e-12,-52006.9,-10.7652], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 303,
    label = "C12H25O4(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {9,S} {13,S} {17,S}
2  C u0 p0 c0 {3,S} {4,S} {14,S} {16,S}
3  C u0 p0 c0 {1,S} {2,S} {30,S} {31,S}
4  C u0 p0 c0 {2,S} {8,S} {28,S} {29,S}
5  C u0 p0 c0 {6,S} {10,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {6,S} {8,S} {24,S} {25,S}
8  C u0 p0 c0 {4,S} {7,S} {26,S} {27,S}
9  C u0 p0 c0 {1,S} {12,S} {32,S} {33,S}
10 C u0 p0 c0 {5,S} {11,S} {18,S} {19,S}
11 C u0 p0 c0 {10,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {9,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {4,S}
29 H u0 p0 c0 {4,S}
30 H u0 p0 c0 {3,S}
31 H u0 p0 c0 {3,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.77764,0.0484611,0.000158775,-2.34633e-07,9.49611e-11,-48505.8,-1.75893], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.76007,0.110359,-5.46715e-05,1.31364e-08,-1.24188e-12,-50990.1,-15.3514], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 304,
    label = "C12H25O4(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {13,S} {16,S}
2  C u0 p0 c0 {1,S} {8,S} {31,S} {32,S}
3  C u0 p0 c0 {4,S} {10,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {8,S} {27,S} {28,S}
8  C u0 p0 c0 {2,S} {7,S} {29,S} {30,S}
9  C u0 p0 c0 {1,S} {11,S} {33,S} {34,S}
10 C u0 p0 c0 {3,S} {12,S} {17,S} {18,S}
11 C u0 p0 c0 {9,S} {14,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {11,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {2,S}
32 H u0 p0 c0 {2,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {9,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.2682,-0.01631,0.000342468,-4.34419e-07,1.70408e-10,-46340.9,-19.082], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.49771,0.113641,-5.73958e-05,1.40141e-08,-1.34215e-12,-49016.3,-8.87222], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 305,
    label = "C12H25O4(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {13,S} {16,S}
2  C u0 p0 c0 {3,S} {11,S} {14,S} {17,S}
3  C u0 p0 c0 {1,S} {2,S} {32,S} {33,S}
4  C u0 p0 c0 {1,S} {9,S} {30,S} {31,S}
5  C u0 p0 c0 {6,S} {10,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {6,S} {8,S} {24,S} {25,S}
8  C u0 p0 c0 {7,S} {9,S} {26,S} {27,S}
9  C u0 p0 c0 {4,S} {8,S} {28,S} {29,S}
10 C u0 p0 c0 {5,S} {12,S} {18,S} {19,S}
11 C u0 p0 c0 {2,S} {37,S} {38,S} {39,S}
12 C u0 p0 c0 {10,S} {34,S} {35,S} {36,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {4,S}
31 H u0 p0 c0 {4,S}
32 H u0 p0 c0 {3,S}
33 H u0 p0 c0 {3,S}
34 H u0 p0 c0 {12,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {11,S}
39 H u0 p0 c0 {11,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.4662,-0.0165441,0.000341527,-4.35423e-07,1.71593e-10,-48430.4,-24.835], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.8497,0.109109,-5.41399e-05,1.30351e-08,-1.23468e-12,-51300.6,-20.1365], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 306,
    label = "C12H25O4(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {13,S} {17,S}
2  C u0 p0 c0 {3,S} {4,S} {14,S} {16,S}
3  C u0 p0 c0 {1,S} {2,S} {28,S} {29,S}
4  C u0 p0 c0 {2,S} {8,S} {26,S} {27,S}
5  C u0 p0 c0 {1,S} {10,S} {30,S} {31,S}
6  C u0 p0 c0 {7,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {6,S} {8,S} {22,S} {23,S}
8  C u0 p0 c0 {4,S} {7,S} {24,S} {25,S}
9  C u0 p0 c0 {6,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {5,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {4,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {3,S}
29 H u0 p0 c0 {3,S}
30 H u0 p0 c0 {5,S}
31 H u0 p0 c0 {5,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.7541,0.0120727,0.000260533,-3.44654e-07,1.36408e-10,-49227.4,-14.8332], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.20741,0.113744,-5.75596e-05,1.40701e-08,-1.34832e-12,-51615.4,-11.1866], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 307,
    label = "C12H25O4(6)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {13,S} {16,S}
2  C u0 p0 c0 {3,S} {9,S} {14,S} {17,S}
3  C u0 p0 c0 {1,S} {2,S} {30,S} {31,S}
4  C u0 p0 c0 {1,S} {8,S} {28,S} {29,S}
5  C u0 p0 c0 {6,S} {10,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {6,S} {8,S} {24,S} {25,S}
8  C u0 p0 c0 {4,S} {7,S} {26,S} {27,S}
9  C u0 p0 c0 {2,S} {12,S} {32,S} {33,S}
10 C u0 p0 c0 {5,S} {11,S} {18,S} {19,S}
11 C u0 p0 c0 {10,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {9,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {4,S}
29 H u0 p0 c0 {4,S}
30 H u0 p0 c0 {3,S}
31 H u0 p0 c0 {3,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.4018,0.0107863,0.000268189,-3.6054e-07,1.44829e-10,-48436,-18.5458], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.3979,0.106045,-5.20072e-05,1.23941e-08,-1.16383e-12,-51364.3,-27.6767], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 308,
    label = "C12H25O4(7)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {13,S} {17,S}
2  C u0 p0 c0 {3,S} {4,S} {14,S} {16,S}
3  C u0 p0 c0 {1,S} {2,S} {26,S} {27,S}
4  C u0 p0 c0 {2,S} {7,S} {24,S} {25,S}
5  C u0 p0 c0 {1,S} {8,S} {28,S} {29,S}
6  C u0 p0 c0 {7,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
8  C u0 p0 c0 {5,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {6,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {5,S}
29 H u0 p0 c0 {5,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[19.9974,-0.0293774,0.000359095,-4.45745e-07,1.7375e-10,-49221.2,-40.5335], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.8252,0.109256,-5.41405e-05,1.30086e-08,-1.22956e-12,-51313.2,-18.3631], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 309,
    label = "C12H25O4(8)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {13,S} {16,S}
2  C u0 p0 c0 {3,S} {5,S} {14,S} {17,S}
3  C u0 p0 c0 {1,S} {2,S} {28,S} {29,S}
4  C u0 p0 c0 {1,S} {8,S} {26,S} {27,S}
5  C u0 p0 c0 {2,S} {10,S} {30,S} {31,S}
6  C u0 p0 c0 {7,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {6,S} {8,S} {22,S} {23,S}
8  C u0 p0 c0 {4,S} {7,S} {24,S} {25,S}
9  C u0 p0 c0 {6,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {5,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {4,S}
27 H u0 p0 c0 {4,S}
28 H u0 p0 c0 {3,S}
29 H u0 p0 c0 {3,S}
30 H u0 p0 c0 {5,S}
31 H u0 p0 c0 {5,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.6315,0.00759516,0.000269493,-3.52553e-07,1.38985e-10,-49005.2,-19.6614], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.23629,0.113784,-5.76014e-05,1.40826e-08,-1.34954e-12,-51264.8,-12.1622], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 310,
    label = "C12H25O4(9)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {13,S} {16,S}
2  C u0 p0 c0 {3,S} {5,S} {14,S} {17,S}
3  C u0 p0 c0 {1,S} {2,S} {26,S} {27,S}
4  C u0 p0 c0 {1,S} {7,S} {24,S} {25,S}
5  C u0 p0 c0 {2,S} {8,S} {28,S} {29,S}
6  C u0 p0 c0 {7,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
8  C u0 p0 c0 {5,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {6,S} {11,S} {18,S} {19,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {15,S}
14 O u0 p2 c0 {2,S} {40,S}
15 O u0 p2 c0 {13,S} {41,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {5,S}
29 H u0 p0 c0 {5,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 O u1 p2 c0 {14,S}
41 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.9939,0.022529,0.000234816,-3.19939e-07,1.27909e-10,-49289.9,-14.2128], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.5673,0.111579,-5.62307e-05,1.37033e-08,-1.31023e-12,-51939.7,-19.887], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 311,
    label = "C12H24O3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {10,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {8,S} {30,S} {31,S}
3  C u0 p0 c0 {4,S} {9,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {8,S} {26,S} {27,S}
8  C u0 p0 c0 {2,S} {7,S} {28,S} {29,S}
9  C u0 p0 c0 {3,S} {11,S} {16,S} {17,S}
10 C u0 p0 c0 {1,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,D} {38,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {2,S}
31 H u0 p0 c0 {2,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 O u0 p2 c0 {12,D}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.0834,-0.00501678,0.000294533,-3.74623e-07,1.46363e-10,-63682.8,-16.2579], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.78809,0.117242,-6.00347e-05,1.47633e-08,-1.41844e-12,-65117.7,10.1273], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 312,
    label = "C12H24O3(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {7,S} {28,S} {29,S}
3  C u0 p0 c0 {4,S} {8,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {2,S} {6,S} {26,S} {27,S}
8  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
9  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {8,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {12,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {9,S} {11,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {2,S}
29 H u0 p0 c0 {2,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.2167,0.00362757,0.000256847,-3.28619e-07,1.2825e-10,-67818.8,-13.9933], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.65458,0.114871,-5.79372e-05,1.40735e-08,-1.33911e-12,-68705.4,16.3748], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 313,
    label = "C12H24O3(2)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {6,S} {26,S} {27,S}
3  C u0 p0 c0 {4,S} {7,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {2,S} {5,S} {24,S} {25,S}
7  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
8  C u0 p0 c0 {1,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {11,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {9,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {2,S}
27 H u0 p0 c0 {2,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.9287,-0.00138065,0.00025332,-3.19031e-07,1.23875e-10,-68567.6,-29.1806], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.25054,0.112648,-5.65646e-05,1.36734e-08,-1.29481e-12,-68751,12.7938], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 314,
    label = "C12H24O3(3)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {20,S}
3  C u0 p0 c0 {2,S} {4,S} {21,S} {22,S}
4  C u0 p0 c0 {3,S} {5,S} {23,S} {24,S}
5  C u0 p0 c0 {4,S} {6,S} {25,S} {26,S}
6  C u0 p0 c0 {5,S} {8,S} {27,S} {28,S}
7  C u0 p0 c0 {1,S} {11,S} {15,S} {16,S}
8  C u0 p0 c0 {6,S} {12,S} {29,S} {30,S}
9  C u0 p0 c0 {10,S} {12,S} {31,S} {32,S}
10 C u0 p0 c0 {9,S} {13,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {10,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {6,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.9941,-0.00290617,0.000286473,-3.6696e-07,1.44083e-10,-66112.2,-10.1865], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.5274,0.111287,-5.5109e-05,1.32255e-08,-1.24829e-12,-67862,7.59282], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 315,
    label = "C12H24O3(4)",
    molecule = 
"""
1  C u0 p0 c0 {8,S} {10,S} {13,S} {15,S}
2  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {9,S} {26,S} {27,S}
7  C u0 p0 c0 {2,S} {11,S} {16,S} {17,S}
8  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
9  C u0 p0 c0 {6,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {1,S} {35,S} {36,S} {37,S}
11 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {10,S}
36 H u0 p0 c0 {10,S}
37 H u0 p0 c0 {10,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.7906,0.00980488,0.000256789,-3.38233e-07,1.3419e-10,-68059.8,-7.8826], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.63382,0.114863,-5.78503e-05,1.40264e-08,-1.33214e-12,-69512.9,10.2768], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 316,
    label = "C12H24O3(5)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {5,S} {24,S} {25,S}
3  C u0 p0 c0 {4,S} {6,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {2,S} {4,S} {22,S} {23,S}
6  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {9,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {7,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[17.6448,-0.00517412,0.000263068,-3.29365e-07,1.27699e-10,-68992,-32.1478], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.77832,0.112096,-5.63463e-05,1.3638e-08,-1.29313e-12,-69241.4,10.1737], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 317,
    label = "C12H24O3(6)",
    molecule = 
"""
1  C u0 p0 c0 {6,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {9,S} {24,S} {25,S}
6  C u0 p0 c0 {1,S} {11,S} {26,S} {27,S}
7  C u0 p0 c0 {2,S} {10,S} {16,S} {17,S}
8  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
9  C u0 p0 c0 {5,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {6,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.4928,0.0237529,0.000209451,-2.81709e-07,1.11481e-10,-68087.9,-8.1514], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.84947,0.114911,-5.8073e-05,1.41253e-08,-1.34513e-12,-69242.7,9.93729], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 318,
    label = "C12H24O3(7)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {4,S} {22,S} {23,S}
3  C u0 p0 c0 {4,S} {6,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {3,S} {20,S} {21,S}
5  C u0 p0 c0 {7,S} {9,S} {24,S} {25,S}
6  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {5,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {12,S} {28,S} {29,S}
9  C u0 p0 c0 {5,S} {12,S} {30,S} {31,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.2584,-0.00403043,0.000276297,-3.51567e-07,1.37768e-10,-68336.9,-22.5499], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.99021,0.113248,-5.7017e-05,1.38163e-08,-1.31114e-12,-69133.1,10.7341], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 319,
    label = "C12H24O3(8)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {7,S} {24,S} {25,S}
3  C u0 p0 c0 {4,S} {6,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {9,S} {22,S} {23,S}
6  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {2,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
9  C u0 p0 c0 {5,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.3887,0.0233174,0.000205393,-2.75235e-07,1.08661e-10,-69131.3,-13.7189], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.39371,0.113798,-5.71883e-05,1.38324e-08,-1.31057e-12,-70122,6.54829], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 320,
    label = "C12H24O3(9)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {4,S} {22,S} {23,S}
3  C u0 p0 c0 {5,S} {6,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {7,S} {24,S} {25,S}
5  C u0 p0 c0 {3,S} {9,S} {20,S} {21,S}
6  C u0 p0 c0 {3,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {4,S} {11,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {12,S} {30,S} {31,S}
9  C u0 p0 c0 {5,S} {12,S} {28,S} {29,S}
10 C u0 p0 c0 {6,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {7,S} {35,S} {36,S} {37,S}
12 C u0 p0 c0 {8,S} {9,S} {38,D}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {39,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {2,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {4,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {11,S}
38 O u0 p2 c0 {12,D}
39 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[20.6168,-0.0212415,0.000299635,-3.66172e-07,1.41151e-10,-69029.4,-45.7423], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.84827,0.110286,-5.52054e-05,1.33204e-08,-1.26013e-12,-69135.3,4.36543], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 321,
    label = "C12H26O2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {10,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {3,S} {19,S} {20,S}
3  C u0 p0 c0 {2,S} {4,S} {21,S} {22,S}
4  C u0 p0 c0 {3,S} {5,S} {23,S} {24,S}
5  C u0 p0 c0 {4,S} {6,S} {25,S} {26,S}
6  C u0 p0 c0 {5,S} {7,S} {27,S} {28,S}
7  C u0 p0 c0 {6,S} {8,S} {29,S} {30,S}
8  C u0 p0 c0 {7,S} {9,S} {31,S} {32,S}
9  C u0 p0 c0 {8,S} {11,S} {33,S} {34,S}
10 C u0 p0 c0 {1,S} {12,S} {15,S} {16,S}
11 C u0 p0 c0 {9,S} {13,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {11,S} {14,S}
14 O u0 p2 c0 {13,S} {40,S}
15 H u0 p0 c0 {10,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {4,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {5,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {6,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {7,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {8,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {9,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.5467,-0.0219089,0.000331551,-4.07336e-07,1.57096e-10,-51665.5,-22.4244], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.48949,0.116581,-5.76347e-05,1.38172e-08,-1.30322e-12,-52732.8,16.1824], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 322,
    label = "C12H26O2(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {11,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {9,S} {32,S} {33,S}
3  C u0 p0 c0 {4,S} {10,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {8,S} {26,S} {27,S}
8  C u0 p0 c0 {7,S} {9,S} {28,S} {29,S}
9  C u0 p0 c0 {2,S} {8,S} {30,S} {31,S}
10 C u0 p0 c0 {3,S} {12,S} {16,S} {17,S}
11 C u0 p0 c0 {1,S} {37,S} {38,S} {39,S}
12 C u0 p0 c0 {10,S} {34,S} {35,S} {36,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {40,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {2,S}
33 H u0 p0 c0 {2,S}
34 H u0 p0 c0 {12,S}
35 H u0 p0 c0 {12,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {11,S}
38 H u0 p0 c0 {11,S}
39 H u0 p0 c0 {11,S}
40 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.7462,-0.00339535,0.000294757,-3.78456e-07,1.49071e-10,-53278.8,-13.7152], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.13359,0.113043,-5.54048e-05,1.31865e-08,-1.23626e-12,-55014.2,4.54208], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 323,
    label = "C12H26O2(2)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {8,S} {30,S} {31,S}
3  C u0 p0 c0 {4,S} {10,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {8,S} {26,S} {27,S}
8  C u0 p0 c0 {2,S} {7,S} {28,S} {29,S}
9  C u0 p0 c0 {1,S} {12,S} {32,S} {33,S}
10 C u0 p0 c0 {3,S} {11,S} {16,S} {17,S}
11 C u0 p0 c0 {10,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {9,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {40,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {2,S}
31 H u0 p0 c0 {2,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {9,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.575,0.0192785,0.000215658,-2.831e-07,1.10601e-10,-52917.4,-14.4705], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.66651,0.112778,-5.54048e-05,1.32139e-08,-1.24111e-12,-54114.3,4.47333], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 324,
    label = "C12H26O2(3)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {8,S} {28,S} {29,S}
3  C u0 p0 c0 {1,S} {10,S} {30,S} {31,S}
4  C u0 p0 c0 {5,S} {9,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {6,S} {8,S} {24,S} {25,S}
8  C u0 p0 c0 {2,S} {7,S} {26,S} {27,S}
9  C u0 p0 c0 {4,S} {11,S} {16,S} {17,S}
10 C u0 p0 c0 {3,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {40,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {2,S}
29 H u0 p0 c0 {2,S}
30 H u0 p0 c0 {3,S}
31 H u0 p0 c0 {3,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.452,0.00509466,0.000249894,-3.21095e-07,1.25756e-10,-53112.7,-25.6337], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.00094,0.110349,-5.38078e-05,1.27497e-08,-1.19081e-12,-54126.9,-0.204568], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 325,
    label = "C12H26O2(4)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {7,S} {26,S} {27,S}
3  C u0 p0 c0 {1,S} {8,S} {28,S} {29,S}
4  C u0 p0 c0 {5,S} {9,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {2,S} {6,S} {24,S} {25,S}
8  C u0 p0 c0 {3,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {4,S} {11,S} {16,S} {17,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {40,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {2,S}
27 H u0 p0 c0 {2,S}
28 H u0 p0 c0 {3,S}
29 H u0 p0 c0 {3,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.2515,-0.00761376,0.000280209,-3.51851e-07,1.37039e-10,-53703.2,-28.2458], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.86418,0.11041,-5.37803e-05,1.27289e-08,-1.18757e-12,-54497.5,5.50826], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 326,
    label = "C12H26O2(5)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {13,S} {15,S}
2  C u0 p0 c0 {1,S} {6,S} {24,S} {25,S}
3  C u0 p0 c0 {1,S} {7,S} {26,S} {27,S}
4  C u0 p0 c0 {5,S} {9,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {5,S} {22,S} {23,S}
7  C u0 p0 c0 {3,S} {8,S} {28,S} {29,S}
8  C u0 p0 c0 {7,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {4,S} {11,S} {16,S} {17,S}
10 C u0 p0 c0 {8,S} {12,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {37,S} {38,S} {39,S}
13 O u0 p2 c0 {1,S} {14,S}
14 O u0 p2 c0 {13,S} {40,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {2,S}
25 H u0 p0 c0 {2,S}
26 H u0 p0 c0 {3,S}
27 H u0 p0 c0 {3,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
39 H u0 p0 c0 {12,S}
40 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.7418,-0.00188923,0.000269306,-3.41468e-07,1.33232e-10,-53668,-26.236], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.38571,0.11108,-5.41875e-05,1.28443e-08,-1.2e-12,-54657.1,2.67497], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 327,
    label = "H1O1",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12368,-0.00327697,6.74833e-06,-6.18859e-09,2.23925e-12,3486.64,-0.698859], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.34971,-6.2648e-05,5.66817e-07,-2.38353e-10,3.01804e-14,3668.21,3.09284], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 328,
    label = "H1O2",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.47189,-0.00583339,2.18961e-05,-2.35458e-08,8.61926e-12,211.516,2.96556], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.27313,0.00359722,-1.57334e-06,3.40571e-10,-2.95227e-14,276.293,7.75055], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 329,
    label = "C1H3",
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
            NASAPolynomial(coeffs=[3.81283,0.00289017,1.52563e-06,-1.75083e-09,5.13963e-13,16383,0.84475], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.59738,0.00637842,-2.37062e-06,4.137e-10,-2.71156e-14,16720.2,7.11441], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 330,
    label = "C1H3O2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.06935,-0.0128809,6.1197e-05,-6.83355e-08,2.53764e-11,-115.796,-0.62497], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.77967,0.0140581,-6.90312e-06,1.64638e-09,-1.54653e-13,15.1935,12.266], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 331,
    label = "H1",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.49929,1.08316e-06,3.56328e-09,-9.26845e-12,5.08428e-15,25482.1,-0.457957], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.49851,2.67182e-06,-1.9723e-09,6.19897e-13,-7.14368e-17,25482.5,-0.453357], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 332,
    label = "H2O1",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.18344,-0.00182815,5.33678e-06,-3.96851e-09,1.12282e-12,-30291.9,-0.802818], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.14512,0.0017957,6.68882e-08,-1.92365e-10,3.10356e-14,-30034.5,4.39496], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 333,
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
            NASAPolynomial(coeffs=[4.52583,-0.00291808,2.04774e-05,-2.39534e-08,9.13584e-12,-17637.7,2.40996], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.68084,0.0053029,-2.07669e-06,3.89002e-10,-2.84217e-14,-17637.9,5.47997], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 334,
    label = "C1H4",
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
            NASAPolynomial(coeffs=[5.18716,-0.0135177,4.6656e-05,-4.52855e-08,1.53546e-11,-10242.8,-4.85353], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[-0.0373378,0.0131605,-5.91316e-06,1.29758e-09,-1.12962e-13,-9386.57,19.1817], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 335,
    label = "C1H4O2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06016,0.00412525,3.36459e-05,-4.84982e-08,2.01334e-11,-17002.5,7.26329], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.5272,0.014239,-6.69788e-06,1.53821e-09,-1.39931e-13,-17532.9,2.48479], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 336,
    label = "C3H5",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,D} {6,S}
5 C u0 p0 c0 {4,D} {7,S} {8,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.74373,0.0154325,2.2465e-05,-4.31442e-08,1.93528e-11,18842.2,15.7512], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.84997,0.0191324,-9.02363e-06,2.08131e-09,-1.9022e-13,17984.5,3.05676], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 337,
    label = "C3H5O2",
    molecule = 
"""
multiplicity 2
1  O u1 p2 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  O u0 p2 c0 {4,D}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74664,0.0297895,-1.0833e-05,-8.53443e-09,6.41633e-12,-15669.1,10.8787], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.7058,0.0229553,-1.16282e-05,2.81986e-09,-2.67723e-13,-16447.8,-4.44435], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 338,
    label = "C3H7O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  O u1 p2 c0 {3,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.5789,0.00716401,5.83286e-05,-8.18509e-08,3.33842e-11,-5855.7,7.25001], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.9409,0.0288479,-1.4274e-05,3.40991e-09,-3.19977e-13,-6433.18,6.28027], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 339,
    label = "C3H7O1(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u1 p2 c0 {1,S}
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
            NASAPolynomial(coeffs=[3.50529,0.0162879,3.52802e-05,-5.82917e-08,2.48185e-11,-13892.8,10.8775], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.44742,0.0276196,-1.32956e-05,3.11751e-09,-2.887e-13,-14639.7,3.13276], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 340,
    label = "C4H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {6,S} {7,S}
2  C u0 p0 c0 {1,D} {3,S} {8,S}
3  C u1 p0 c0 {2,S} {4,S} {5,S}
4  H u0 p0 c0 {3,S}
5  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.66887,0.00520204,6.28266e-05,-8.52928e-08,3.42916e-11,14154.7,5.87883], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.68415,0.0290296,-1.40021e-05,3.28984e-09,-3.05238e-13,13608.9,6.38943], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 341,
    label = "C4H7O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,D} {13,S}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {4,D}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.591155,0.0599531,-5.37249e-05,2.01752e-08,-5.73424e-13,-27040.2,24.0563], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.0347,0.0282194,-1.37959e-05,3.26761e-09,-3.04693e-13,-28753.4,-16.9318], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 342,
    label = "C4H7O2(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {13,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  O u1 p2 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.55941,0.023539,2.85806e-05,-5.57351e-08,2.44697e-11,-22500.9,4.20641], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.38846,0.0296185,-1.4854e-05,3.60408e-09,-3.43335e-13,-23763.7,-13.2746], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 343,
    label = "C4H9O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {9,S} {13,S} {14,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u1 p2 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.67116,0.0127241,6.44012e-05,-9.40539e-08,3.87835e-11,-8924.34,3.85266], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.65949,0.0356584,-1.76008e-05,4.20382e-09,-3.94775e-13,-9774.56,-0.957961], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 344,
    label = "C4H9O1(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  O u1 p2 c0 {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
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
            NASAPolynomial(coeffs=[5.57283,0.0161216,5.2665e-05,-7.99364e-08,3.31032e-11,-17471.1,3.13097], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.92901,0.0348627,-1.68698e-05,3.97369e-09,-3.69437e-13,-18302.6,-2.90502], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 345,
    label = "C5H9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,D} {11,S}
4  C u0 p0 c0 {3,D} {5,S} {12,S}
5  C u1 p0 c0 {4,S} {13,S} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.07928,0.0124354,6.78329e-05,-9.72935e-08,3.97333e-11,11412,6.06251], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.74486,0.0374051,-1.82949e-05,4.3372e-09,-4.04882e-13,10590.8,2.62442], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 346,
    label = "C5H9(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u1 p0 c0 {1,S} {5,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {13,S}
5  C u0 p0 c0 {3,S} {4,D} {14,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.83948,-0.00675241,0.000107286,-1.31547e-07,5.07148e-11,9637.59,-5.7843], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.49469,0.0389682,-1.90063e-05,4.50538e-09,-4.20965e-13,9433.62,9.08722], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 347,
    label = "C5H9O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,D} {16,S}
6  O u1 p2 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u0 p2 c0 {5,D}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.66837,0.0653128,-4.93644e-05,1.10342e-08,3.45228e-12,-30383.2,20.3365], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.3012,0.0352322,-1.70767e-05,4.01949e-09,-3.7303e-13,-32219.6,-22.066], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 348,
    label = "C5H9O2(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {4,S} {16,D}
6  O u1 p2 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68826,0.0459083,-6.64745e-06,-2.65685e-08,1.5381e-11,-34114.4,12.681], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.54263,0.037496,-1.81593e-05,4.28044e-09,-3.98206e-13,-35481.7,-13.0218], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 349,
    label = "C5H9O2(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {10,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {2,S} {16,D}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u1 p2 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u0 p2 c0 {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.34487,0.0540873,-4.05821e-05,1.70942e-08,-3.04014e-12,-25708,9.03907], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.44565,0.0364969,-1.79069e-05,4.26953e-09,-4.01141e-13,-26893.7,-16.328], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 350,
    label = "C5H11O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {12,S} {16,S} {17,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.16433,0.00714302,9.75936e-05,-1.33664e-07,5.41104e-11,-12095.4,-4.94187], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.27703,0.0424256,-2.0866e-05,4.97777e-09,-4.67406e-13,-13107.8,-7.435], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 351,
    label = "C5H11O1(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  O u1 p2 c0 {3,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.25512,0.0227893,6.43725e-05,-1.039e-07,4.45371e-11,-20061.1,6.17942], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.88014,0.0420173,-2.00953e-05,4.68264e-09,-4.31187e-13,-21296.3,-6.99217], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 352,
    label = "C5H11O1(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  O u1 p2 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.69526,0.0185556,8.0166e-05,-1.23484e-07,5.24384e-11,-20220.8,4.56683], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.81682,0.0410462,-1.96553e-05,4.5861e-09,-4.22797e-13,-21759.3,-12.1431], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 353,
    label = "C6H11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {2,S} {5,S} {14,S}
5  C u0 p0 c0 {4,S} {6,D} {15,S}
6  C u0 p0 c0 {5,D} {16,S} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.85637,0.0123523,8.98132e-05,-1.27329e-07,5.20072e-11,8148.87,-0.5576], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.10859,0.0430138,-2.09057e-05,4.9444e-09,-4.61355e-13,6897.48,-8.57599], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 354,
    label = "C6H11(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
4  C u1 p0 c0 {1,S} {6,S} {15,S}
5  C u0 p0 c0 {3,S} {6,D} {16,S}
6  C u0 p0 c0 {4,S} {5,D} {17,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.36514,-0.000444568,0.000114939,-1.46854e-07,5.75192e-11,6800.2,-6.10608], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.97824,0.0463536,-2.26995e-05,5.39853e-09,-5.05773e-13,6209.49,3.06643], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 355,
    label = "C6H11O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,D} {19,S}
7  O u1 p2 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 O u0 p2 c0 {6,D}
19 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72471,0.0620219,-2.56385e-05,-1.57673e-08,1.33079e-11,-33490,13.4751], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.903,0.043197,-2.09176e-05,4.9235e-09,-4.57098e-13,-35249.1,-23.1019], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 356,
    label = "C6H11O2(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {5,S} {19,D}
7  O u1 p2 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.53513,0.045191,8.67212e-06,-4.31034e-08,2.10143e-11,-37502.7,5.80668], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.95635,0.0458091,-2.22074e-05,5.23874e-09,-4.8765e-13,-38724.9,-13.7432], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 357,
    label = "C6H11O2(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {13,S} {14,S} {15,S}
6  C u0 p0 c0 {2,S} {3,S} {19,D}
7  O u1 p2 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73056,0.0652187,-4.88786e-05,2.12909e-08,-3.99502e-12,-37441.5,12.565], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.07652,0.0457453,-2.22172e-05,5.25166e-09,-4.8985e-13,-38629.1,-13.7508], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 358,
    label = "C6H11O2(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {13,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {3,S} {19,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.80379,0.0479988,-2.46516e-06,-2.93771e-08,1.53478e-11,-28700.8,5.21639], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.55537,0.0450063,-2.19853e-05,5.22032e-09,-4.88633e-13,-29931.5,-15.5194], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 359,
    label = "C6H13O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {15,S} {19,S} {20,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 O u1 p2 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.3866,0.00499359,0.000116431,-1.55437e-07,6.23773e-11,-15238.3,-11.8817], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.88814,0.0499276,-2.42583e-05,5.72671e-09,-5.3297e-13,-16019.4,-7.20588], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 360,
    label = "C6H13O1(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {6,S} {7,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  O u1 p2 c0 {4,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.84476,0.00659206,0.00011222,-1.48201e-07,5.87743e-11,-23361.2,-7.6711], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.63723,0.0526068,-2.54453e-05,5.9874e-09,-5.55903e-13,-23953.7,0.740104], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 361,
    label = "C6H13O1(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  O u1 p2 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.87298,0.0207546,7.35062e-05,-1.09433e-07,4.51397e-11,-23838.1,-8.38133], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.18469,0.0492061,-2.35247e-05,5.47884e-09,-5.04191e-13,-24631.1,-10.4558], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 362,
    label = "C7H13",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {6,D} {17,S}
6  C u0 p0 c0 {5,D} {7,S} {18,S}
7  C u1 p0 c0 {6,S} {19,S} {20,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.60469,0.019474,9.12328e-05,-1.35365e-07,5.63048e-11,5127.05,-2.33992], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.3899,0.0495848,-2.37614e-05,5.54974e-09,-5.12233e-13,3752.42,-13.1452], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 363,
    label = "C7H13(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {7,D} {19,S}
6  C u1 p0 c0 {4,S} {7,S} {18,S}
7  C u0 p0 c0 {5,D} {6,S} {20,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.73486,0.00785904,0.000115858,-1.55796e-07,6.24557e-11,4107.55,-6.54277], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.44174,0.0526823,-2.54356e-05,5.9776e-09,-5.54513e-13,3245.48,-3.05101], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 364,
    label = "C7H13(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  C u1 p0 c0 {1,S} {7,S} {18,S}
6  C u0 p0 c0 {2,S} {7,D} {19,S}
7  C u0 p0 c0 {5,S} {6,D} {20,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.84269,0.00630608,0.000121493,-1.61499e-07,6.42677e-11,4040.46,-6.93796], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.59187,0.0532244,-2.60016e-05,6.17339e-09,-5.77711e-13,3047.93,-4.24033], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 365,
    label = "C7H13O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {5,S} {8,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,D} {22,S}
8  O u1 p2 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 O u0 p2 c0 {7,D}
22 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.99493,0.0412067,3.78672e-05,-8.01968e-08,3.61097e-11,-36754.7,-2.05171], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.4667,0.0526049,-2.55633e-05,6.03517e-09,-5.61716e-13,-38005.7,-18.3852], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 366,
    label = "C7H13O2(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {13,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {7,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {4,S} {6,S} {22,D}
8  O u1 p2 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.47306,0.0343343,4.81247e-05,-8.28261e-08,3.46501e-11,-40674.6,-4.53864], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.69954,0.0551831,-2.69094e-05,6.3791e-09,-5.96186e-13,-41566.1,-10.3583], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 367,
    label = "C7H13O2(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
7  C u0 p0 c0 {3,S} {4,S} {22,D}
8  O u1 p2 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.12114,0.0587629,-1.79249e-05,-1.22384e-08,8.13663e-12,-40873.8,3.6891], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.33838,0.0541937,-2.63108e-05,6.21526e-09,-5.79261e-13,-41881.4,-13.745], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 368,
    label = "C7H13O2(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {6,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {16,S} {20,S} {21,S}
7  C u0 p0 c0 {3,S} {4,S} {22,D}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 O u1 p2 c0 {6,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.01935,0.0404781,3.51447e-05,-7.32288e-08,3.23197e-11,-31867.9,-1.58531], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.87119,0.0531523,-2.58221e-05,6.09985e-09,-5.68294e-13,-32989.2,-14.7892], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 369,
    label = "C7H13O2(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
2  C u0 p0 c0 {4,S} {6,S} {8,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {3,S} {4,S} {22,D}
8  O u1 p2 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.99852,0.0333987,5.34515e-05,-8.92936e-08,3.71338e-11,-40640.2,-2.04365], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.32161,0.0557601,-2.72655e-05,6.47948e-09,-6.06879e-13,-41633.5,-8.7676], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 370,
    label = "C7H15O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {18,S} {22,S} {23,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 O u1 p2 c0 {7,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.7131,0.00260667,0.000134012,-1.74325e-07,6.91396e-11,-18401,-19.9828], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.23476,0.0579371,-2.79906e-05,6.57491e-09,-6.09271e-13,-18862,-6.23919], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 371,
    label = "C7H15O1(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {7,S} {8,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  O u1 p2 c0 {5,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.9415,0.00206505,0.000145492,-1.90078e-07,7.56074e-11,-26483.8,-13.909], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.03993,0.0596285,-2.87674e-05,6.75261e-09,-6.25558e-13,-27238.5,-3.94326], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 372,
    label = "C7H15O1(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {5,S} {8,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  O u1 p2 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.8885,-0.00317158,0.000162898,-2.10282e-07,8.35561e-11,-26704.2,-14.2363], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.59098,0.0601409,-2.90288e-05,6.81725e-09,-6.31827e-13,-27524.7,-3.2188], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 373,
    label = "C7H15O1(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {13,S}
3  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  O u1 p2 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.3541,0.0223776,8.49274e-05,-1.23861e-07,5.0608e-11,-26882.8,-13.5888], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.68306,0.0573911,-2.749e-05,6.41257e-09,-5.90898e-13,-27574.8,-11.4757], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 374,
    label = "C8H15",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
6  C u1 p0 c0 {4,S} {7,S} {20,S}
7  C u0 p0 c0 {6,S} {8,D} {21,S}
8  C u0 p0 c0 {7,D} {22,S} {23,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.89258,0.0140287,0.00010889,-1.46937e-07,5.82833e-11,1947.79,-10.0971], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.60769,0.0604842,-2.91368e-05,6.83448e-09,-6.33014e-13,1353.95,-1.37654], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 375,
    label = "C8H15(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {7,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {3,S} {8,D} {22,S}
7  C u1 p0 c0 {5,S} {8,S} {21,S}
8  C u0 p0 c0 {6,D} {7,S} {23,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.2489,0.00686433,0.000118687,-1.5002e-07,5.75062e-11,545.109,-16.8604], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.40126,0.0628559,-3.04975e-05,7.19678e-09,-6.69892e-13,456.208,4.27282], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 376,
    label = "C8H15(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
3  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {8,D} {22,S}
7  C u1 p0 c0 {2,S} {8,S} {21,S}
8  C u0 p0 c0 {6,D} {7,S} {23,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.40822,0.0354121,3.64978e-05,-5.94678e-08,2.27629e-11,2612.7,-13.174], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.0228,0.0605498,-2.91702e-05,6.84532e-09,-6.34428e-13,2419.81,-5.25477], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 377,
    label = "C8H15O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {6,S} {9,S} {18,S}
5  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {4,S} {8,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {24,D} {25,S}
9  O u1 p2 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 O u0 p2 c0 {8,D}
25 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.1422,0.0218932,0.000109368,-1.58444e-07,6.51431e-11,-39546.4,-7.03417], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.99571,0.0635027,-3.10934e-05,7.38913e-09,-6.91579e-13,-40675.5,-9.31247], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 378,
    label = "C8H15O2(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {5,S} {9,S} {16,S}
4  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {8,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {8,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {5,S} {7,S} {25,D}
9  O u1 p2 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.0557,0.00496902,0.000150527,-1.96107e-07,7.73138e-11,-43491.4,-12.0794], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.77257,0.0666547,-3.27455e-05,7.80966e-09,-7.33426e-13,-44330.1,-1.00233], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 379,
    label = "C8H15O2(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {14,S}
3  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {7,S} {8,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {4,S} {5,S} {25,D}
9  O u1 p2 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.10027,0.0462661,2.71286e-05,-5.88732e-08,2.46438e-11,-44035.3,-6.60395], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.00627,0.0636078,-3.10132e-05,7.35171e-09,-6.87117e-13,-44721.7,-9.96774], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 380,
    label = "C8H15O2(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {7,S} {8,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {20,S} {21,S} {22,S}
7  C u0 p0 c0 {5,S} {19,S} {23,S} {24,S}
8  C u0 p0 c0 {4,S} {5,S} {25,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {7,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.17785,0.0087231,0.000159247,-2.1899e-07,8.9461e-11,-34431.8,-4.18735], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.97245,0.0642282,-3.13012e-05,7.41097e-09,-6.91528e-13,-36032.6,-9.02064], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 381,
    label = "C8H15O2(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {5,S} {7,S} {9,S} {14,S}
4  C u0 p0 c0 {1,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {8,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {3,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {4,S} {5,S} {25,D}
9  O u1 p2 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.41,0.0215991,0.000103738,-1.46728e-07,5.91114e-11,-43800.5,-10.0705], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.38403,0.0644633,-3.14935e-05,7.47593e-09,-6.99374e-13,-44718.3,-7.7726], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 382,
    label = "C8H15O2(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {9,S} {12,S}
2  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
4  C u0 p0 c0 {3,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {8,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {19,S} {20,S} {21,S}
7  C u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {4,S} {5,S} {25,D}
9  O u1 p2 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u0 p2 c0 {8,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.2437,0.0252571,9.18824e-05,-1.32812e-07,5.35662e-11,-44032.7,-9.94731], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.47021,0.0643113,-3.13966e-05,7.44868e-09,-6.96506e-13,-44906,-8.29922], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 383,
    label = "C8H17O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {6,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
6  C u0 p0 c0 {4,S} {8,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {6,S} {21,S} {25,S} {26,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 O u1 p2 c0 {8,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.1372,-0.0183062,0.000204502,-2.45652e-07,9.38834e-11,-21188.2,-27.8012], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.57336,0.0712633,-3.47257e-05,8.21988e-09,-7.66785e-13,-21204.5,7.34634], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 384,
    label = "C8H17O1(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {6,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {4,S} {8,S} {9,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  O u1 p2 c0 {6,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.0741,-0.0166903,0.000193397,-2.29546e-07,8.67704e-11,-29779.2,-31.0797], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.99795,0.0712704,-3.47129e-05,8.21642e-09,-7.66627e-13,-29580,7.24837], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 385,
    label = "C8H17O1(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {6,S} {9,S} {18,S}
5  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {4,S} {8,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  O u1 p2 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.6973,-0.011861,0.000199823,-2.50897e-07,9.86571e-11,-29915.9,-23.2937], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.93497,0.0685278,-3.30963e-05,7.77411e-09,-7.20485e-13,-30500.3,-1.8894], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 386,
    label = "C8H17O1(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {16,S}
4  C u0 p0 c0 {3,S} {6,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {4,S} {8,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  O u1 p2 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.5966,0.000784264,0.000171181,-2.22899e-07,8.87084e-11,-29728.1,-15.5918], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.73975,0.0687896,-3.32507e-05,7.81738e-09,-7.25142e-13,-30522.6,-2.37874], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 387,
    label = "C9H17",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {4,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {20,S} {21,S} {22,S}
7  C u1 p0 c0 {5,S} {8,S} {23,S}
8  C u0 p0 c0 {7,S} {9,D} {24,S}
9  C u0 p0 c0 {8,D} {25,S} {26,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.67087,0.00768039,0.00016335,-2.18876e-07,8.79003e-11,-833.391,-6.51042], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.83823,0.069231,-3.34966e-05,7.8864e-09,-7.32704e-13,-2124.3,-3.49941], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 388,
    label = "C9H17(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {7,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {8,S} {21,S} {22,S} {23,S}
7  C u0 p0 c0 {4,S} {9,D} {25,S}
8  C u1 p0 c0 {6,S} {9,S} {24,S}
9  C u0 p0 c0 {7,D} {8,S} {26,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.5679,-0.0150273,0.00019451,-2.3287e-07,8.84466e-11,-2699.89,-27.9877], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.87197,0.0724671,-3.52808e-05,8.34782e-09,-7.78637e-13,-2613.58,8.29099], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 389,
    label = "C9H17(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {8,S} {16,S} {17,S}
4  C u0 p0 c0 {6,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {21,S} {22,S} {23,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  C u1 p0 c0 {4,S} {9,S} {24,S}
8  C u0 p0 c0 {3,S} {9,D} {25,S}
9  C u0 p0 c0 {7,S} {8,D} {26,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.7511,0.0245488,8.93326e-05,-1.2142e-07,4.67129e-11,-409.694,-16.2307], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.43866,0.0701981,-3.39681e-05,8.00015e-09,-7.43624e-13,-685.421,-1.71604], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 390,
    label = "C9H17(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {8,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {21,S} {22,S} {23,S}
7  C u1 p0 c0 {3,S} {9,S} {24,S}
8  C u0 p0 c0 {4,S} {9,D} {25,S}
9  C u0 p0 c0 {7,S} {8,D} {26,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.8254,0.0158019,0.000124687,-1.6748e-07,6.62116e-11,-2269.87,-15.6431], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.84727,0.0697002,-3.36907e-05,7.92501e-09,-7.35714e-13,-2910.03,-4.60402], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 391,
    label = "C9H17O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {7,S} {10,S} {21,S}
6  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {5,S} {9,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  C u0 p0 c0 {7,S} {27,D} {28,S}
10 O u1 p2 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 O u0 p2 c0 {9,D}
28 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.7414,-0.0103485,0.000217326,-2.77241e-07,1.09834e-10,-42692.9,-21.3748], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.92278,0.0738541,-3.63098e-05,8.65817e-09,-8.12552e-13,-43775.6,-6.20343], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 392,
    label = "C9H17O2(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {6,S} {10,S} {19,S}
5  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {9,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {6,S} {8,S} {28,D}
10 O u1 p2 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 O u0 p2 c0 {9,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.4378,-0.00407322,0.000187046,-2.33553e-07,9.02711e-11,-47132.2,-21.3708], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.30364,0.0762382,-3.75401e-05,8.97021e-09,-8.4374e-13,-47699.7,1.82935], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 393,
    label = "C9H17O2(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {5,S} {10,S} {17,S}
4  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {8,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {4,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {6,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {5,S} {6,S} {28,D}
10 O u1 p2 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 O u0 p2 c0 {9,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.3216,0.0229267,0.000100439,-1.35703e-07,5.26039e-11,-47325.5,-21.4714], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.4973,0.0731232,-3.57172e-05,8.47742e-09,-7.93007e-13,-47579.9,-4.97591], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 394,
    label = "C9H17O2(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {5,S} {16,S} {17,S}
4  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
5  C u0 p0 c0 {3,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {8,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {4,S} {23,S} {24,S} {25,S}
8  C u0 p0 c0 {6,S} {22,S} {26,S} {27,S}
9  C u0 p0 c0 {5,S} {6,S} {28,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 O u1 p2 c0 {8,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 O u0 p2 c0 {9,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.3621,0.0231788,0.000103157,-1.39469e-07,5.40037e-11,-38208.3,-18.3498], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.95886,0.0736154,-3.61533e-05,8.62088e-09,-8.09585e-13,-38646.5,-4.37508], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 395,
    label = "C9H17O2(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {6,S} {8,S} {10,S} {17,S}
5  C u0 p0 c0 {2,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {3,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {4,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {5,S} {6,S} {28,D}
10 O u1 p2 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 O u0 p2 c0 {9,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.056,0.000650373,0.000198683,-2.59416e-07,1.03078e-10,-46188.2,-7.54863], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.04839,0.0765482,-3.77145e-05,9.01727e-09,-8.4862e-13,-47653.4,-1.06026], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 396,
    label = "C9H17O2(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {13,S}
3  C u0 p0 c0 {1,S} {8,S} {16,S} {17,S}
4  C u0 p0 c0 {5,S} {7,S} {11,S} {12,S}
5  C u0 p0 c0 {4,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {4,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {3,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {5,S} {6,S} {28,D}
10 O u1 p2 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 O u0 p2 c0 {9,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.5746,-0.00560855,0.000199015,-2.53092e-07,9.94897e-11,-47046.6,-23.214], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.65602,0.0742253,-3.6331e-05,8.63722e-09,-8.08946e-13,-47968.9,-6.6592], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 397,
    label = "C9H17O2(6)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {13,S} {14,S}
2  C u0 p0 c0 {4,S} {6,S} {10,S} {15,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {8,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {3,S} {22,S} {23,S} {24,S}
8  C u0 p0 c0 {4,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {5,S} {6,S} {28,D}
10 O u1 p2 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 O u0 p2 c0 {9,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.2552,0.00519761,0.000175974,-2.30164e-07,9.1009e-11,-46892.6,-14.8441], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.03654,0.0751908,-3.69385e-05,8.81107e-09,-8.27665e-13,-48076,-5.9388], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 398,
    label = "C9H19O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {7,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {8,S} {10,S} {11,S}
7  C u0 p0 c0 {5,S} {9,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {24,S} {28,S} {29,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 O u1 p2 c0 {9,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[22.0032,-0.0455842,0.000273871,-3.13421e-07,1.17705e-10,-25015,-53.5233], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.55072,0.0777041,-3.77675e-05,8.91674e-09,-8.29768e-13,-24204.6,7.93727], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 399,
    label = "C9H19O1(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {7,S} {21,S} {22,S}
6  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {5,S} {9,S} {10,S} {23,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  C u0 p0 c0 {7,S} {27,S} {28,S} {29,S}
10 O u1 p2 c0 {7,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
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
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.1612,-0.0348617,0.000281116,-3.37048e-07,1.29769e-10,-32387.7,-26.1858], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.65032,0.081934,-4.00746e-05,9.51734e-09,-8.90359e-13,-32720.5,14.2715], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 400,
    label = "C9H19O1(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {7,S} {10,S} {21,S}
6  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {5,S} {9,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  C u0 p0 c0 {7,S} {27,S} {28,S} {29,S}
10 O u1 p2 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.1006,-0.00372028,0.000216477,-2.81582e-07,1.12422e-10,-32512.8,-10.2085], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.13375,0.078533,-3.81311e-05,8.9998e-09,-8.37582e-13,-33796.6,0.606667], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 401,
    label = "C9H19O1(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {19,S}
5  C u0 p0 c0 {4,S} {7,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {5,S} {9,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  C u0 p0 c0 {7,S} {27,S} {28,S} {29,S}
10 O u1 p2 c0 {4,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.1391,-0.012655,0.000219816,-2.7327e-07,1.06549e-10,-32671,-22.4667], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.6678,0.0791228,-3.84453e-05,9.07897e-09,-8.45326e-13,-33109.8,6.13596], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 402,
    label = "C9H19O1(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {7,S} {20,S} {21,S}
6  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
7  C u0 p0 c0 {5,S} {9,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  C u0 p0 c0 {7,S} {27,S} {28,S} {29,S}
10 O u1 p2 c0 {3,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.7329,-0.0119766,0.00022979,-2.90368e-07,1.14417e-10,-32466.1,-18.5615], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.67273,0.0791676,-3.84937e-05,9.09619e-09,-8.47395e-13,-33363.3,2.20096], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 403,
    label = "C10H19",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {5,S} {17,S} {18,S}
4  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {7,S} {19,S} {20,S}
6  C u0 p0 c0 {4,S} {8,S} {21,S} {22,S}
7  C u0 p0 c0 {5,S} {23,S} {24,S} {25,S}
8  C u1 p0 c0 {6,S} {9,S} {26,S}
9  C u0 p0 c0 {8,S} {10,D} {27,S}
10 C u0 p0 c0 {9,D} {28,S} {29,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.3609,0.00244235,0.000193999,-2.51342e-07,9.92217e-11,-3436.93,-9.88785], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.0148,0.0803746,-3.90897e-05,9.24466e-09,-8.62195e-13,-4490.58,3.81245], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 404,
    label = "C10H19(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {15,S} {16,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {6,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {8,S} {19,S} {20,S}
6  C u0 p0 c0 {4,S} {21,S} {22,S} {23,S}
7  C u0 p0 c0 {9,S} {24,S} {25,S} {26,S}
8  C u1 p0 c0 {5,S} {10,S} {27,S}
9  C u0 p0 c0 {7,S} {10,D} {28,S}
10 C u0 p0 c0 {8,S} {9,D} {29,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.7025,-0.0182389,0.000244591,-3.00793e-07,1.16558e-10,-5169.67,-20.7094], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.6625,0.0830576,-4.06634e-05,9.66903e-09,-9.0572e-13,-5815.77,8.94617], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 405,
    label = "C10H19(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {9,S} {19,S} {20,S}
5  C u0 p0 c0 {7,S} {8,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {24,S} {25,S} {26,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  C u1 p0 c0 {5,S} {10,S} {27,S}
9  C u0 p0 c0 {4,S} {10,D} {28,S}
10 C u0 p0 c0 {8,S} {9,D} {29,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.3858,0.0141695,0.000175896,-2.40122e-07,9.69917e-11,-3102.98,-3.42409], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.85951,0.0800634,-3.89607e-05,9.21772e-09,-8.59907e-13,-4669.63,-3.08938], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 406,
    label = "C10H19(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
3  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {8,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {9,S} {19,S} {20,S}
6  C u0 p0 c0 {3,S} {21,S} {22,S} {23,S}
7  C u0 p0 c0 {2,S} {24,S} {25,S} {26,S}
8  C u1 p0 c0 {4,S} {10,S} {27,S}
9  C u0 p0 c0 {5,S} {10,D} {28,S}
10 C u0 p0 c0 {8,S} {9,D} {29,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.6137,0.00247746,0.000177333,-2.23953e-07,8.66901e-11,-5562.89,-20.8821], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.34649,0.0806411,-3.92454e-05,9.28564e-09,-8.66272e-13,-5982.95,3.58676], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 407,
    label = "C10H19O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {8,S} {11,S} {24,S}
7  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
8  C u0 p0 c0 {6,S} {10,S} {25,S} {26,S}
9  C u0 p0 c0 {7,S} {27,S} {28,S} {29,S}
10 C u0 p0 c0 {8,S} {30,D} {31,S}
11 O u1 p2 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 O u0 p2 c0 {10,D}
31 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.2552,-0.00231445,0.000200548,-2.56522e-07,1.01091e-10,-46096.6,-29.5851], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.24747,0.0808665,-3.9576e-05,9.39923e-09,-8.79119e-13,-46724.2,-7.44426], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 408,
    label = "C10H19O2(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {7,S} {11,S} {22,S}
6  C u0 p0 c0 {1,S} {8,S} {12,S} {13,S}
7  C u0 p0 c0 {5,S} {10,S} {23,S} {24,S}
8  C u0 p0 c0 {6,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {10,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {7,S} {9,S} {31,D}
11 O u1 p2 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 O u0 p2 c0 {10,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.5845,-0.0122412,0.00023227,-2.87323e-07,1.11172e-10,-50214.2,-23.264], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.75403,0.0858743,-4.234e-05,1.01268e-08,-9.5318e-13,-50842.3,5.80565], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 409,
    label = "C10H19O2(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {6,S} {11,S} {20,S}
5  C u0 p0 c0 {1,S} {8,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {10,S} {21,S} {22,S}
7  C u0 p0 c0 {9,S} {10,S} {23,S} {24,S}
8  C u0 p0 c0 {5,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {7,S} {31,D}
11 O u1 p2 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 O u0 p2 c0 {10,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.6468,0.0183905,0.000143387,-1.89222e-07,7.35784e-11,-50393.2,-17.8628], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.22603,0.083831,-4.11722e-05,9.81783e-09,-9.21963e-13,-51032.9,-1.29971], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 410,
    label = "C10H19O2(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {6,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {10,S} {21,S} {22,S}
7  C u0 p0 c0 {9,S} {10,S} {23,S} {24,S}
8  C u0 p0 c0 {5,S} {26,S} {27,S} {28,S}
9  C u0 p0 c0 {7,S} {25,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {7,S} {31,D}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 O u1 p2 c0 {9,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 O u0 p2 c0 {10,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.7307,0.00206723,0.000202811,-2.64629e-07,1.05278e-10,-41016.5,-17.2156], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.95469,0.0832553,-4.07151e-05,9.66735e-09,-9.04186e-13,-41996.8,-1.62792], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 411,
    label = "C10H19O2(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {6,S} {18,S} {19,S}
4  C u0 p0 c0 {1,S} {8,S} {12,S} {13,S}
5  C u0 p0 c0 {7,S} {9,S} {11,S} {20,S}
6  C u0 p0 c0 {3,S} {10,S} {21,S} {22,S}
7  C u0 p0 c0 {5,S} {10,S} {23,S} {24,S}
8  C u0 p0 c0 {4,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {5,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {7,S} {31,D}
11 O u1 p2 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 O u0 p2 c0 {10,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.47,-0.011225,0.000238934,-2.99634e-07,1.16958e-10,-49501.2,-20.2083], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.89433,0.0857161,-4.22672e-05,1.01112e-08,-9.51903e-13,-50516.7,2.0111], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 412,
    label = "C10H19O2(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {6,S} {11,S} {18,S}
4  C u0 p0 c0 {1,S} {8,S} {12,S} {13,S}
5  C u0 p0 c0 {7,S} {9,S} {19,S} {20,S}
6  C u0 p0 c0 {3,S} {10,S} {21,S} {22,S}
7  C u0 p0 c0 {5,S} {10,S} {23,S} {24,S}
8  C u0 p0 c0 {4,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {5,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {7,S} {31,D}
11 O u1 p2 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 O u0 p2 c0 {10,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.4831,-0.00291357,0.000204469,-2.56761e-07,9.94924e-11,-50389.6,-24.318], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.98712,0.0842806,-4.14706e-05,9.90395e-09,-9.31174e-13,-51092.4,-0.544476], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 413,
    label = "C10H19O2(6)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {6,S} {16,S} {17,S}
3  C u0 p0 c0 {5,S} {7,S} {11,S} {18,S}
4  C u0 p0 c0 {1,S} {8,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {9,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {10,S} {21,S} {22,S}
7  C u0 p0 c0 {3,S} {10,S} {23,S} {24,S}
8  C u0 p0 c0 {4,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {5,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {7,S} {31,D}
11 O u1 p2 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 O u0 p2 c0 {10,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.4219,-0.000989281,0.000213484,-2.73999e-07,1.07719e-10,-50116.8,-17.6876], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.44672,0.0849913,-4.18671e-05,1.00077e-08,-9.41594e-13,-51284.3,-2.22091], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 414,
    label = "C10H19O2(7)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {17,S} {18,S}
2  C u0 p0 c0 {4,S} {6,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {16,S}
4  C u0 p0 c0 {2,S} {8,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {9,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {10,S} {21,S} {22,S}
7  C u0 p0 c0 {3,S} {10,S} {23,S} {24,S}
8  C u0 p0 c0 {4,S} {25,S} {26,S} {27,S}
9  C u0 p0 c0 {5,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {7,S} {31,D}
11 O u1 p2 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 O u0 p2 c0 {10,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.9733,0.00866047,0.000172723,-2.24529e-07,8.81082e-11,-50237.4,-20.8578], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.96904,0.0827577,-4.05249e-05,9.63709e-09,-9.02796e-13,-50938.4,-2.6579], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 415,
    label = "C10H21O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
3  C u0 p0 c0 {2,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {8,S} {23,S} {24,S}
7  C u0 p0 c0 {1,S} {9,S} {11,S} {12,S}
8  C u0 p0 c0 {6,S} {10,S} {25,S} {26,S}
9  C u0 p0 c0 {7,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {27,S} {31,S} {32,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
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
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 O u1 p2 c0 {10,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[18.5197,-0.0426214,0.000307209,-3.61907e-07,1.38055e-10,-27310.7,-38.5152], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.7969,0.0899453,-4.39307e-05,1.04169e-08,-9.73016e-13,-27100,16.8385], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 416,
    label = "C10H21O1(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {8,S} {24,S} {25,S}
7  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
8  C u0 p0 c0 {6,S} {10,S} {11,S} {26,S}
9  C u0 p0 c0 {7,S} {27,S} {28,S} {29,S}
10 C u0 p0 c0 {8,S} {30,S} {31,S} {32,S}
11 O u1 p2 c0 {8,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[21.505,-0.0605181,0.000350936,-4.06633e-07,1.54447e-10,-36189.6,-50.6966], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.37722,0.0897356,-4.37776e-05,1.03704e-08,-9.6788e-13,-35785.1,14.5739], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 417,
    label = "C10H21O1(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {8,S} {11,S} {24,S}
7  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
8  C u0 p0 c0 {6,S} {10,S} {25,S} {26,S}
9  C u0 p0 c0 {7,S} {27,S} {28,S} {29,S}
10 C u0 p0 c0 {8,S} {30,S} {31,S} {32,S}
11 O u1 p2 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.625,-0.0140135,0.000254519,-3.19625e-07,1.25432e-10,-35647.1,-18.5971], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.18164,0.0887157,-4.32454e-05,1.02414e-08,-9.55879e-13,-36502.7,7.52171], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 418,
    label = "C10H21O1(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {11,S} {22,S}
6  C u0 p0 c0 {5,S} {8,S} {23,S} {24,S}
7  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
8  C u0 p0 c0 {6,S} {10,S} {25,S} {26,S}
9  C u0 p0 c0 {7,S} {27,S} {28,S} {29,S}
10 C u0 p0 c0 {8,S} {30,S} {31,S} {32,S}
11 O u1 p2 c0 {5,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
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
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[22.9498,-0.0456863,0.000295329,-3.41147e-07,1.28769e-10,-36677.5,-57.0974], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.64909,0.0865077,-4.18838e-05,9.85671e-09,-9.14788e-13,-35883.6,7.33597], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 419,
    label = "C10H21O1(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {20,S}
5  C u0 p0 c0 {4,S} {6,S} {21,S} {22,S}
6  C u0 p0 c0 {5,S} {8,S} {23,S} {24,S}
7  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
8  C u0 p0 c0 {6,S} {10,S} {25,S} {26,S}
9  C u0 p0 c0 {7,S} {27,S} {28,S} {29,S}
10 C u0 p0 c0 {8,S} {30,S} {31,S} {32,S}
11 O u1 p2 c0 {4,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
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
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.9022,0.00102996,0.000219515,-2.86122e-07,1.13831e-10,-35289.8,-12.5107], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.14239,0.0874037,-4.24978e-05,1.00429e-08,-9.35684e-13,-36467.4,1.87873], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 420,
    label = "C11H21",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {6,S} {20,S} {21,S}
5  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {8,S} {22,S} {23,S}
7  C u0 p0 c0 {5,S} {9,S} {24,S} {25,S}
8  C u0 p0 c0 {6,S} {26,S} {27,S} {28,S}
9  C u1 p0 c0 {7,S} {10,S} {29,S}
10 C u0 p0 c0 {9,S} {11,D} {30,S}
11 C u0 p0 c0 {10,D} {31,S} {32,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {11,S}
32 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.3236,-0.00261315,0.00022867,-2.9228e-07,1.14889e-10,-6603.57,-12.9464], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.38526,0.0900984,-4.39331e-05,1.04119e-08,-9.72665e-13,-7653.85,6.6403], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 421,
    label = "C11H21(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {5,S} {18,S} {19,S}
4  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {7,S} {20,S} {21,S}
6  C u0 p0 c0 {4,S} {9,S} {22,S} {23,S}
7  C u0 p0 c0 {5,S} {24,S} {25,S} {26,S}
8  C u0 p0 c0 {10,S} {27,S} {28,S} {29,S}
9  C u1 p0 c0 {6,S} {11,S} {30,S}
10 C u0 p0 c0 {8,S} {11,D} {31,S}
11 C u0 p0 c0 {9,S} {10,D} {32,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[18.5134,-0.0434406,0.000314261,-3.69869e-07,1.40842e-10,-8877.4,-37.9762], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.78909,0.0917452,-4.48961e-05,1.06676e-08,-9.98414e-13,-8792.82,16.7435], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 422,
    label = "C11H21(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {4,S} {16,S} {17,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {10,S} {22,S} {23,S}
6  C u0 p0 c0 {8,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {4,S} {27,S} {28,S} {29,S}
8  C u0 p0 c0 {6,S} {24,S} {25,S} {26,S}
9  C u0 p0 c0 {6,S} {11,D} {31,S}
10 C u1 p0 c0 {5,S} {11,S} {30,S}
11 C u0 p0 c0 {9,D} {10,S} {32,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.7614,-0.0184277,0.000263315,-3.25787e-07,1.26783e-10,-8092.05,-23.0609], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.27559,0.0897325,-4.37664e-05,1.03724e-08,-9.68832e-13,-8815.21,7.73041], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 423,
    label = "C11H21(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {8,S} {18,S} {19,S}
4  C u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {4,S} {9,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {10,S} {22,S} {23,S}
7  C u0 p0 c0 {4,S} {24,S} {25,S} {26,S}
8  C u0 p0 c0 {3,S} {27,S} {28,S} {29,S}
9  C u1 p0 c0 {5,S} {11,S} {30,S}
10 C u0 p0 c0 {6,S} {11,D} {31,S}
11 C u0 p0 c0 {9,S} {10,D} {32,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.7425,0.0191529,0.000148891,-1.96545e-07,7.66179e-11,-6986.33,-21.6814], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.6975,0.0874951,-4.23972e-05,9.99407e-09,-9.29428e-13,-7474.79,-2.08146], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 424,
    label = "C11H21(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {14,S} {15,S}
2  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
3  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {8,S} {18,S} {19,S}
5  C u0 p0 c0 {1,S} {9,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {10,S} {22,S} {23,S}
7  C u0 p0 c0 {3,S} {24,S} {25,S} {26,S}
8  C u0 p0 c0 {4,S} {27,S} {28,S} {29,S}
9  C u1 p0 c0 {5,S} {11,S} {30,S}
10 C u0 p0 c0 {6,S} {11,D} {31,S}
11 C u0 p0 c0 {9,S} {10,D} {32,S}
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
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.0691,-0.00469954,0.000223713,-2.8049e-07,1.08882e-10,-8776.5,-19.3814], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.58382,0.090653,-4.42951e-05,1.05159e-08,-9.83817e-13,-9409.95,8.34843], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 425,
    label = "C11H21O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {9,S} {12,S} {27,S}
8  C u0 p0 c0 {1,S} {10,S} {13,S} {14,S}
9  C u0 p0 c0 {7,S} {11,S} {28,S} {29,S}
10 C u0 p0 c0 {8,S} {30,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,D} {34,S}
12 O u1 p2 c0 {7,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 O u0 p2 c0 {11,D}
34 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.4251,-0.0117928,0.000286638,-3.68287e-07,1.45886e-10,-48466.3,-12.3102], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.70666,0.0931645,-4.59731e-05,1.10077e-08,-1.03726e-12,-50795.4,-8.06924], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 426,
    label = "C11H21O2(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {8,S} {12,S} {25,S}
7  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
8  C u0 p0 c0 {6,S} {11,S} {26,S} {27,S}
9  C u0 p0 c0 {7,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {11,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {8,S} {10,S} {34,D}
12 O u1 p2 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 O u0 p2 c0 {11,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.7776,-0.0266208,0.000294677,-3.58254e-07,1.38024e-10,-53173.2,-25.9424], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.35085,0.0966955,-4.78319e-05,1.14717e-08,-1.08221e-12,-53845.1,12.4634], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 427,
    label = "C11H21O2(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {7,S} {12,S} {23,S}
6  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
7  C u0 p0 c0 {5,S} {11,S} {24,S} {25,S}
8  C u0 p0 c0 {10,S} {11,S} {26,S} {27,S}
9  C u0 p0 c0 {6,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {8,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {7,S} {8,S} {34,D}
12 O u1 p2 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 O u0 p2 c0 {11,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.0134,0.011203,0.000172396,-2.19884e-07,8.46788e-11,-53324.6,-29.111], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.06187,0.0914977,-4.48135e-05,1.06591e-08,-9.98735e-13,-53617.8,-1.30225], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 428,
    label = "C11H21O2(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {7,S} {22,S} {23,S}
6  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
7  C u0 p0 c0 {5,S} {11,S} {24,S} {25,S}
8  C u0 p0 c0 {10,S} {11,S} {26,S} {27,S}
9  C u0 p0 c0 {6,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {8,S} {28,S} {32,S} {33,S}
11 C u0 p0 c0 {7,S} {8,S} {34,D}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 O u1 p2 c0 {10,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 O u0 p2 c0 {11,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.2127,0.0071488,0.000225777,-2.99114e-07,1.19464e-10,-43081.5,-3.46809], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.55775,0.0943449,-4.64772e-05,1.11076e-08,-1.04475e-12,-44726.9,4.33803], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 429,
    label = "C11H21O2(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {7,S} {21,S} {22,S}
5  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
6  C u0 p0 c0 {8,S} {10,S} {12,S} {23,S}
7  C u0 p0 c0 {4,S} {11,S} {24,S} {25,S}
8  C u0 p0 c0 {6,S} {11,S} {26,S} {27,S}
9  C u0 p0 c0 {5,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {7,S} {8,S} {34,D}
12 O u1 p2 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 O u0 p2 c0 {11,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.9756,-0.0177575,0.000267483,-3.28581e-07,1.2683e-10,-53190.2,-28.2465], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.82306,0.0947134,-4.67077e-05,1.11733e-08,-1.05181e-12,-53905.1,5.22797], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 430,
    label = "C11H21O2(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {7,S} {12,S} {21,S}
5  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
6  C u0 p0 c0 {8,S} {10,S} {22,S} {23,S}
7  C u0 p0 c0 {4,S} {11,S} {24,S} {25,S}
8  C u0 p0 c0 {6,S} {11,S} {26,S} {27,S}
9  C u0 p0 c0 {5,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {7,S} {8,S} {34,D}
12 O u1 p2 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 O u0 p2 c0 {11,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.1485,0.0121938,0.000201006,-2.64885e-07,1.04525e-10,-53097.8,-13.426], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.92311,0.0946411,-4.67041e-05,1.11815e-08,-1.05347e-12,-54427.1,-1.55026], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 431,
    label = "C11H21O2(6)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {7,S} {19,S} {20,S}
4  C u0 p0 c0 {6,S} {8,S} {12,S} {21,S}
5  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
6  C u0 p0 c0 {4,S} {10,S} {22,S} {23,S}
7  C u0 p0 c0 {3,S} {11,S} {24,S} {25,S}
8  C u0 p0 c0 {4,S} {11,S} {26,S} {27,S}
9  C u0 p0 c0 {5,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {7,S} {8,S} {34,D}
12 O u1 p2 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 O u0 p2 c0 {11,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.7569,0.0299206,0.000155626,-2.17056e-07,8.66472e-11,-52247.2,-1.66923], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.66269,0.0949216,-4.68549e-05,1.12233e-08,-1.0581e-12,-53688.7,1.77742], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 432,
    label = "C11H21O2(7)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
2  C u0 p0 c0 {1,S} {6,S} {20,S} {21,S}
3  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {8,S} {12,S} {17,S}
5  C u0 p0 c0 {3,S} {9,S} {13,S} {14,S}
6  C u0 p0 c0 {2,S} {10,S} {22,S} {23,S}
7  C u0 p0 c0 {3,S} {11,S} {24,S} {25,S}
8  C u0 p0 c0 {4,S} {11,S} {26,S} {27,S}
9  C u0 p0 c0 {5,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {7,S} {8,S} {34,D}
12 O u1 p2 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {1,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 O u0 p2 c0 {11,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.36296,0.0224677,0.000178559,-2.43156e-07,9.67699e-11,-52805.7,-5.40441], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.8832,0.0947876,-4.68358e-05,1.12278e-08,-1.05916e-12,-54384.5,-1.32695], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 433,
    label = "C11H21O2(8)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {15,S} {16,S}
2  C u0 p0 c0 {4,S} {6,S} {20,S} {21,S}
3  C u0 p0 c0 {1,S} {7,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {8,S} {12,S} {19,S}
5  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
6  C u0 p0 c0 {2,S} {10,S} {22,S} {23,S}
7  C u0 p0 c0 {3,S} {11,S} {24,S} {25,S}
8  C u0 p0 c0 {4,S} {11,S} {26,S} {27,S}
9  C u0 p0 c0 {5,S} {28,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {7,S} {8,S} {34,D}
12 O u1 p2 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 O u0 p2 c0 {11,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.9981,-0.00119776,0.000233692,-2.98378e-07,1.16835e-10,-53462.1,-19.4182], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.95504,0.0944636,-4.65541e-05,1.11327e-08,-1.04783e-12,-54635.4,-0.00440598], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 434,
    label = "C11H23O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {14,S} {15,S}
2  C u0 p0 c0 {1,S} {3,S} {16,S} {17,S}
3  C u0 p0 c0 {2,S} {4,S} {18,S} {19,S}
4  C u0 p0 c0 {3,S} {5,S} {20,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {9,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {10,S} {12,S} {13,S}
9  C u0 p0 c0 {7,S} {11,S} {28,S} {29,S}
10 C u0 p0 c0 {8,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {30,S} {34,S} {35,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 O u1 p2 c0 {11,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[28.4524,-0.0944878,0.000441531,-4.97319e-07,1.86739e-10,-31076.7,-74.1296], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.59702,0.0977611,-4.76752e-05,1.12857e-08,-1.05239e-12,-29869.8,20.4248], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 435,
    label = "C11H23O1(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {9,S} {27,S} {28,S}
8  C u0 p0 c0 {1,S} {10,S} {13,S} {14,S}
9  C u0 p0 c0 {7,S} {11,S} {12,S} {29,S}
10 C u0 p0 c0 {8,S} {30,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 O u1 p2 c0 {9,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[21.985,-0.0579218,0.0003648,-4.25495e-07,1.61845e-10,-38968.7,-49.8945], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.40761,0.0986176,-4.81671e-05,1.14227e-08,-1.06713e-12,-38652.2,16.5586], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 436,
    label = "C11H23O1(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {9,S} {12,S} {27,S}
8  C u0 p0 c0 {1,S} {10,S} {13,S} {14,S}
9  C u0 p0 c0 {7,S} {11,S} {28,S} {29,S}
10 C u0 p0 c0 {8,S} {30,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 O u1 p2 c0 {7,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.5125,-0.0258608,0.000305937,-3.7513e-07,1.45455e-10,-38694.4,-21.1887], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.04104,0.100562,-4.9336e-05,1.17494e-08,-1.10189e-12,-39418.2,16.9472], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 437,
    label = "C11H23O1(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {12,S} {25,S}
7  C u0 p0 c0 {6,S} {9,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {10,S} {13,S} {14,S}
9  C u0 p0 c0 {7,S} {11,S} {28,S} {29,S}
10 C u0 p0 c0 {8,S} {30,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 O u1 p2 c0 {6,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[21.9947,-0.0353384,0.000292457,-3.43968e-07,1.30506e-10,-39430.8,-51.6331], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.51086,0.0956234,-4.64137e-05,1.09484e-08,-1.01826e-12,-38895.3,8.37441], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 438,
    label = "C11H23O1(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {12,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {9,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {10,S} {13,S} {14,S}
9  C u0 p0 c0 {7,S} {11,S} {28,S} {29,S}
10 C u0 p0 c0 {8,S} {30,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 O u1 p2 c0 {5,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
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
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.6841,-0.0280437,0.000308198,-3.76789e-07,1.4606e-10,-38622.2,-26.3826], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.89862,0.0993769,-4.86443e-05,1.15607e-08,-1.08218e-12,-39258.4,13.3653], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 439,
    label = "C11H23O1(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {12,S} {21,S}
5  C u0 p0 c0 {4,S} {6,S} {22,S} {23,S}
6  C u0 p0 c0 {5,S} {7,S} {24,S} {25,S}
7  C u0 p0 c0 {6,S} {9,S} {26,S} {27,S}
8  C u0 p0 c0 {1,S} {10,S} {13,S} {14,S}
9  C u0 p0 c0 {7,S} {11,S} {28,S} {29,S}
10 C u0 p0 c0 {8,S} {30,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 O u1 p2 c0 {4,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {10,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[14.7524,-0.0214172,0.000290191,-3.56688e-07,1.38204e-10,-38671.6,-23.7963], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.57974,0.0998326,-4.89173e-05,1.16367e-08,-1.09025e-12,-39310.3,13.7346], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 440,
    label = "C12H23",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {7,S} {23,S} {24,S}
6  C u0 p0 c0 {1,S} {8,S} {13,S} {14,S}
7  C u0 p0 c0 {5,S} {9,S} {25,S} {26,S}
8  C u0 p0 c0 {6,S} {10,S} {27,S} {28,S}
9  C u0 p0 c0 {7,S} {29,S} {30,S} {31,S}
10 C u0 p0 c0 {8,S} {11,D} {32,S}
11 C u0 p0 c0 {10,D} {12,S} {33,S}
12 C u1 p0 c0 {11,S} {34,S} {35,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {12,S}
35 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.834,-0.00281199,0.000250436,-3.17023e-07,1.23578e-10,-9611.59,-10.2974], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.35002,0.101864,-5.0001e-05,1.19182e-08,-1.11883e-12,-10616,15.3771], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 441,
    label = "C12H23(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {6,S} {21,S} {22,S}
5  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
6  C u0 p0 c0 {4,S} {8,S} {23,S} {24,S}
7  C u0 p0 c0 {5,S} {10,S} {25,S} {26,S}
8  C u0 p0 c0 {6,S} {27,S} {28,S} {29,S}
9  C u0 p0 c0 {11,S} {30,S} {31,S} {32,S}
10 C u1 p0 c0 {7,S} {12,S} {33,S}
11 C u0 p0 c0 {9,S} {12,D} {34,S}
12 C u0 p0 c0 {10,S} {11,D} {35,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.04553,0.0157578,0.000208795,-2.75798e-07,1.08657e-10,-10794,-1.20952], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.33502,0.102748,-5.05718e-05,1.20824e-08,-1.13649e-12,-12134.4,12.4186], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 442,
    label = "C12H23(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {5,S} {19,S} {20,S}
4  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {8,S} {21,S} {22,S}
6  C u0 p0 c0 {4,S} {11,S} {25,S} {26,S}
7  C u0 p0 c0 {9,S} {10,S} {23,S} {24,S}
8  C u0 p0 c0 {5,S} {30,S} {31,S} {32,S}
9  C u0 p0 c0 {7,S} {27,S} {28,S} {29,S}
10 C u0 p0 c0 {7,S} {12,D} {34,S}
11 C u1 p0 c0 {6,S} {12,S} {33,S}
12 C u0 p0 c0 {10,D} {11,S} {35,S}
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
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {9,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {8,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.9474,0.0110608,0.000210257,-2.73607e-07,1.07251e-10,-11283.8,-13.7652], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.20993,0.100247,-4.91563e-05,1.17067e-08,-1.09822e-12,-12326.9,5.27901], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 443,
    label = "C12H23(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {4,S} {19,S} {20,S}
3  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {9,S} {21,S} {22,S}
5  C u0 p0 c0 {6,S} {8,S} {13,S} {14,S}
6  C u0 p0 c0 {5,S} {10,S} {23,S} {24,S}
7  C u0 p0 c0 {3,S} {11,S} {25,S} {26,S}
8  C u0 p0 c0 {5,S} {27,S} {28,S} {29,S}
9  C u0 p0 c0 {4,S} {30,S} {31,S} {32,S}
10 C u1 p0 c0 {6,S} {12,S} {33,S}
11 C u0 p0 c0 {7,S} {12,D} {34,S}
12 C u0 p0 c0 {10,S} {11,D} {35,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.11347,0.0390751,0.000142453,-2.05252e-07,8.25251e-11,-11081.5,1.98611], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.4057,0.0998865,-4.89298e-05,1.16447e-08,-1.09189e-12,-12485.8,4.17638], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 444,
    label = "C12H23(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {19,S} {20,S}
2  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
3  C u0 p0 c0 {1,S} {7,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {8,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {9,S} {21,S} {22,S}
6  C u0 p0 c0 {2,S} {10,S} {23,S} {24,S}
7  C u0 p0 c0 {3,S} {11,S} {25,S} {26,S}
8  C u0 p0 c0 {4,S} {27,S} {28,S} {29,S}
9  C u0 p0 c0 {5,S} {30,S} {31,S} {32,S}
10 C u0 p0 c0 {6,S} {12,D} {34,S}
11 C u1 p0 c0 {7,S} {12,S} {33,S}
12 C u0 p0 c0 {10,D} {11,S} {35,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {1,S}
20 H u0 p0 c0 {1,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {9,S}
32 H u0 p0 c0 {9,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[20.5407,-0.0382289,0.000315531,-3.75175e-07,1.43513e-10,-11791.4,-44.641], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.839,0.0976825,-4.75326e-05,1.12395e-08,-1.04765e-12,-11715.7,9.87049], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 445,
    label = "C12H23O2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {7,S} {26,S} {27,S}
7  C u0 p0 c0 {6,S} {8,S} {28,S} {29,S}
8  C u0 p0 c0 {7,S} {10,S} {13,S} {30,S}
9  C u0 p0 c0 {1,S} {11,S} {14,S} {15,S}
10 C u0 p0 c0 {8,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 C u0 p0 c0 {10,S} {36,D} {37,S}
13 O u1 p2 c0 {8,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 O u0 p2 c0 {12,D}
37 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.2978,-0.0394071,0.000374209,-4.64171e-07,1.82302e-10,-51651.4,-24.6923], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.62573,0.101874,-5.0101e-05,1.19537e-08,-1.12259e-12,-53529.9,0.140886], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 446,
    label = "C12H23O2(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {8,S} {13,S} {26,S}
7  C u0 p0 c0 {1,S} {10,S} {14,S} {15,S}
8  C u0 p0 c0 {6,S} {12,S} {27,S} {28,S}
9  C u0 p0 c0 {11,S} {12,S} {29,S} {30,S}
10 C u0 p0 c0 {7,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {8,S} {9,S} {37,D}
13 O u1 p2 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 O u0 p2 c0 {12,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[15.7208,-0.00102332,0.000237039,-2.96855e-07,1.14546e-10,-56575.6,-25.3709], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.03411,0.103239,-5.08587e-05,1.2157e-08,-1.14382e-12,-57169.2,7.1474], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 447,
    label = "C12H23O2(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {7,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {8,S} {25,S} {26,S}
7  C u0 p0 c0 {1,S} {10,S} {13,S} {14,S}
8  C u0 p0 c0 {6,S} {12,S} {27,S} {28,S}
9  C u0 p0 c0 {11,S} {12,S} {29,S} {30,S}
10 C u0 p0 c0 {7,S} {32,S} {33,S} {34,S}
11 C u0 p0 c0 {9,S} {31,S} {35,S} {36,S}
12 C u0 p0 c0 {8,S} {9,S} {37,D}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 O u1 p2 c0 {11,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {10,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 O u0 p2 c0 {12,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[9.01863,0.0137976,0.000233579,-3.11745e-07,1.24199e-10,-47199,-2.19561], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.52749,0.105063,-5.20697e-05,1.25105e-08,-1.18212e-12,-49111.9,3.64733], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 448,
    label = "C12H23O2(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {8,S} {24,S} {25,S}
6  C u0 p0 c0 {1,S} {10,S} {14,S} {15,S}
7  C u0 p0 c0 {9,S} {11,S} {13,S} {26,S}
8  C u0 p0 c0 {5,S} {12,S} {27,S} {28,S}
9  C u0 p0 c0 {7,S} {12,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {7,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {8,S} {9,S} {37,D}
13 O u1 p2 c0 {7,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 O u0 p2 c0 {12,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.0077,-0.000900435,0.000266307,-3.40987e-07,1.33578e-10,-55345.6,-9.19414], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.80228,0.106567,-5.28804e-05,1.27196e-08,-1.20307e-12,-56948.5,8.49857], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 449,
    label = "C12H23O2(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {8,S} {13,S} {24,S}
6  C u0 p0 c0 {1,S} {10,S} {14,S} {15,S}
7  C u0 p0 c0 {9,S} {11,S} {25,S} {26,S}
8  C u0 p0 c0 {5,S} {12,S} {27,S} {28,S}
9  C u0 p0 c0 {7,S} {12,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {7,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {8,S} {9,S} {37,D}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 O u0 p2 c0 {12,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.956,0.0147593,0.000215333,-2.82825e-07,1.11036e-10,-56034.7,-11.7357], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.93407,0.105001,-5.19754e-05,1.24764e-08,-1.1781e-12,-57413.7,2.89391], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 450,
    label = "C12H23O2(6)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {8,S} {22,S} {23,S}
5  C u0 p0 c0 {7,S} {9,S} {13,S} {24,S}
6  C u0 p0 c0 {1,S} {10,S} {14,S} {15,S}
7  C u0 p0 c0 {5,S} {11,S} {25,S} {26,S}
8  C u0 p0 c0 {4,S} {12,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {12,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {7,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {8,S} {9,S} {37,D}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 O u0 p2 c0 {12,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[13.0521,-0.00710598,0.000279764,-3.56764e-07,1.40309e-10,-55197.8,-12.2554], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.27217,0.104297,-5.14756e-05,1.23237e-08,-1.16097e-12,-56683.7,8.04195], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 451,
    label = "C12H23O2(7)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {8,S} {13,S} {22,S}
5  C u0 p0 c0 {7,S} {9,S} {23,S} {24,S}
6  C u0 p0 c0 {1,S} {10,S} {14,S} {15,S}
7  C u0 p0 c0 {5,S} {11,S} {25,S} {26,S}
8  C u0 p0 c0 {4,S} {12,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {12,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {7,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {8,S} {9,S} {37,D}
13 O u1 p2 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 O u0 p2 c0 {12,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[11.2114,0.0189313,0.00019943,-2.63376e-07,1.03147e-10,-56296.6,-14.148], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.38319,0.10434,-5.15808e-05,1.23686e-08,-1.16692e-12,-57575.7,0.372299], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 452,
    label = "C12H23O2(8)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {4,S} {18,S} {19,S}
3  C u0 p0 c0 {5,S} {7,S} {23,S} {24,S}
4  C u0 p0 c0 {2,S} {8,S} {20,S} {21,S}
5  C u0 p0 c0 {3,S} {9,S} {13,S} {22,S}
6  C u0 p0 c0 {1,S} {10,S} {14,S} {15,S}
7  C u0 p0 c0 {3,S} {11,S} {25,S} {26,S}
8  C u0 p0 c0 {4,S} {12,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {12,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {7,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {8,S} {9,S} {37,D}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 O u0 p2 c0 {12,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[8.70434,0.0358018,0.000158223,-2.21413e-07,8.78857e-11,-55485.2,-4.07651], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.02227,0.104674,-5.17246e-05,1.24002e-08,-1.16979e-12,-56898.8,1.7862], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 453,
    label = "C12H23O2(9)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
2  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
3  C u0 p0 c0 {2,S} {7,S} {23,S} {24,S}
4  C u0 p0 c0 {1,S} {8,S} {18,S} {19,S}
5  C u0 p0 c0 {2,S} {9,S} {13,S} {20,S}
6  C u0 p0 c0 {1,S} {10,S} {14,S} {15,S}
7  C u0 p0 c0 {3,S} {11,S} {25,S} {26,S}
8  C u0 p0 c0 {4,S} {12,S} {27,S} {28,S}
9  C u0 p0 c0 {5,S} {12,S} {29,S} {30,S}
10 C u0 p0 c0 {6,S} {31,S} {32,S} {33,S}
11 C u0 p0 c0 {7,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {8,S} {9,S} {37,D}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {2,S}
22 H u0 p0 c0 {2,S}
23 H u0 p0 c0 {3,S}
24 H u0 p0 c0 {3,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {7,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {8,S}
29 H u0 p0 c0 {9,S}
30 H u0 p0 c0 {9,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {10,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 O u0 p2 c0 {12,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[17.6713,-0.022813,0.000300318,-3.67494e-07,1.41811e-10,-56572.8,-32.4269], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.10408,0.10328,-5.09258e-05,1.21812e-08,-1.14662e-12,-57298.3,6.18601], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 454,
    label = "C12H25O1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {17,S} {18,S}
3  C u0 p0 c0 {2,S} {4,S} {19,S} {20,S}
4  C u0 p0 c0 {3,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {23,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {8,S} {27,S} {28,S}
8  C u0 p0 c0 {7,S} {10,S} {29,S} {30,S}
9  C u0 p0 c0 {1,S} {11,S} {13,S} {14,S}
10 C u0 p0 c0 {8,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {34,S} {35,S} {36,S}
12 C u0 p0 c0 {10,S} {33,S} {37,S} {38,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 O u1 p2 c0 {12,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {11,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.75477,0.0144606,0.000242131,-3.21691e-07,1.27902e-10,-32223.5,7.33087], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.846561,0.111983,-5.52511e-05,1.32231e-08,-1.24534e-12,-33848.5,19.9605], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 455,
    label = "C12H25O1(1)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {7,S} {26,S} {27,S}
7  C u0 p0 c0 {6,S} {8,S} {28,S} {29,S}
8  C u0 p0 c0 {7,S} {10,S} {30,S} {31,S}
9  C u0 p0 c0 {1,S} {11,S} {14,S} {15,S}
10 C u0 p0 c0 {8,S} {12,S} {13,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 C u0 p0 c0 {10,S} {36,S} {37,S} {38,S}
13 O u1 p2 c0 {10,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {8,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[12.7366,-0.0197419,0.000316823,-3.91538e-07,1.51723e-10,-41678.8,-15.5978], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.2329,0.11206,-5.52689e-05,1.32233e-08,-1.245e-12,-42642.1,21.4327], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 456,
    label = "C12H25O1(2)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {7,S} {26,S} {27,S}
7  C u0 p0 c0 {6,S} {8,S} {28,S} {29,S}
8  C u0 p0 c0 {7,S} {10,S} {13,S} {30,S}
9  C u0 p0 c0 {1,S} {11,S} {14,S} {15,S}
10 C u0 p0 c0 {8,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 C u0 p0 c0 {10,S} {36,S} {37,S} {38,S}
13 O u1 p2 c0 {8,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {7,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.6728,-0.0279082,0.000322497,-3.91763e-07,1.50894e-10,-41944.4,-30.0152], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.20148,0.109175,-5.35323e-05,1.27418e-08,-1.19435e-12,-42380.5,17.1592], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 457,
    label = "C12H25O1(3)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {7,S} {26,S} {27,S}
7  C u0 p0 c0 {6,S} {8,S} {13,S} {28,S}
8  C u0 p0 c0 {7,S} {10,S} {29,S} {30,S}
9  C u0 p0 c0 {1,S} {11,S} {14,S} {15,S}
10 C u0 p0 c0 {8,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 C u0 p0 c0 {10,S} {36,S} {37,S} {38,S}
13 O u1 p2 c0 {7,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[18.3866,-0.0417324,0.000359908,-4.32532e-07,1.66461e-10,-41512.5,-34.234], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.54333,0.108768,-5.33196e-05,1.26882e-08,-1.18907e-12,-41952.1,17.9184], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 458,
    label = "C12H25O1(4)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {24,S} {25,S}
6  C u0 p0 c0 {5,S} {7,S} {13,S} {26,S}
7  C u0 p0 c0 {6,S} {8,S} {27,S} {28,S}
8  C u0 p0 c0 {7,S} {10,S} {29,S} {30,S}
9  C u0 p0 c0 {1,S} {11,S} {14,S} {15,S}
10 C u0 p0 c0 {8,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 C u0 p0 c0 {10,S} {36,S} {37,S} {38,S}
13 O u1 p2 c0 {6,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[16.088,-0.0342358,0.000349506,-4.26038e-07,1.6502e-10,-41528.1,-22.8516], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.80032,0.109834,-5.39448e-05,1.28574e-08,-1.2065e-12,-42270.1,21.8507], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 459,
    label = "C12H25O1(5)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {18,S} {19,S}
3  C u0 p0 c0 {2,S} {4,S} {20,S} {21,S}
4  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
5  C u0 p0 c0 {4,S} {6,S} {13,S} {24,S}
6  C u0 p0 c0 {5,S} {7,S} {25,S} {26,S}
7  C u0 p0 c0 {6,S} {8,S} {27,S} {28,S}
8  C u0 p0 c0 {7,S} {10,S} {29,S} {30,S}
9  C u0 p0 c0 {1,S} {11,S} {14,S} {15,S}
10 C u0 p0 c0 {8,S} {12,S} {31,S} {32,S}
11 C u0 p0 c0 {9,S} {33,S} {34,S} {35,S}
12 C u0 p0 c0 {10,S} {36,S} {37,S} {38,S}
13 O u1 p2 c0 {5,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
27 H u0 p0 c0 {7,S}
28 H u0 p0 c0 {7,S}
29 H u0 p0 c0 {8,S}
30 H u0 p0 c0 {8,S}
31 H u0 p0 c0 {10,S}
32 H u0 p0 c0 {10,S}
33 H u0 p0 c0 {11,S}
34 H u0 p0 c0 {11,S}
35 H u0 p0 c0 {11,S}
36 H u0 p0 c0 {12,S}
37 H u0 p0 c0 {12,S}
38 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[10.12,0.00579044,0.000248546,-3.18328e-07,1.24035e-10,-41566.8,-9.18303], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.843,0.111305,-5.48767e-05,1.31274e-08,-1.23594e-12,-42716.1,15.0213], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 460,
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
            NASAPolynomial(coeffs=[4.48248,-0.0065564,5.90122e-05,-6.80061e-08,2.5438e-11,-11615.3,1.84269], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.326173,0.022378,-1.05315e-05,2.4171e-09,-2.1951e-13,-11219.2,19.3309], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 461,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49044,8.29803e-05,-2.40163e-07,2.14171e-10,1.98587e-14,-1017.66,-4.24206], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.67609,-0.000802544,9.95821e-07,-3.41319e-10,3.92331e-14,-1037.55,-5.07667], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 462,
    label = "cbh1_C[O]",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.37208,-0.00825127,4.6422e-05,-5.32584e-08,2.01272e-11,1380.72,5.0346], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.78703,0.0123713,-6.04634e-06,1.43346e-09,-1.33818e-13,1523.18,15.3377], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 463,
    label = "cbh1_C=O",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.78555,-0.00945726,3.44423e-05,-3.41101e-08,1.16272e-11,-14424,0.576461], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.28188,0.0098301,-4.88847e-06,1.17508e-09,-1.1091e-13,-13927.4,16.3298], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 464,
    label = "cbh1_[CH2]O",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56616,0.00722045,5.5505e-06,-1.24616e-08,5.59414e-12,24030.8,5.90128], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.51492,0.007568,-3.24221e-06,6.87318e-10,-5.84129e-14,23682.4,0.426466], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 465,
    label = "cbh2_CC[O]",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.27518,-0.000569683,4.58831e-05,-5.7206e-08,2.21294e-11,-3177.33,6.59496], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.09217,0.0200525,-9.70388e-06,2.28312e-09,-2.11881e-13,-3180.42,14.6016], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 466,
    label = "cbh2_CC(C)=O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
4  O u0 p2 c0 {2,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.31196,-0.00655541,7.4038e-05,-8.82211e-08,3.35106e-11,-28151.4,-0.452115], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.49716,0.026868,-1.30925e-05,3.1009e-09,-2.89521e-13,-28075.3,14.0507], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 467,
    label = "cbh2_CO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.78476,-0.00654756,4.05403e-05,-4.39351e-08,1.57603e-11,-25625.4,1.8014], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.58529,0.0141788,-6.48903e-06,1.45788e-09,-1.30249e-13,-25282.8,15.5325], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 468,
    label = "cbh2_C[C](C)O",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u1 p0 c0 {1,S} {2,S} {4,S}
4  O u0 p2 c0 {3,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.40829,0.0248948,-3.6789e-06,-8.76799e-09,4.43027e-12,-4609.06,5.4163], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.36928,0.0253553,-1.19388e-05,2.75226e-09,-2.51588e-13,-4990.7,-0.222198], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 469,
    label = "ccbh2_[CH2]OO",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.36838,0.015424,1.42315e-07,-1.55296e-08,8.73596e-12,-2633.67,9.9837], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.80243,0.00842607,-3.8912e-06,8.83647e-10,-7.99035e-14,-3564.4,-7.99028], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 470,
    label = "C2H6O",
    molecule = 
"""
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86485,0.00838087,2.74616e-05,-3.73191e-08,1.43758e-11,-23845.6,6.15854], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.89516,0.0239526,-1.15376e-05,2.70411e-09,-2.50169e-13,-23742.6,14.008], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 471,
    label = "C2H6O(1)",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 O u0 p2 c0 {1,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6995,0.0169686,7.30829e-07,-7.20138e-09,2.63998e-12,-30038.9,6.98109], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.22701,0.021578,-1.00569e-05,2.29793e-09,-2.08468e-13,-30080.3,8.57512], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 472,
    label = "C2H3OH",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,S} {6,S}
3 O u0 p2 c0 {1,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.62842,0.00549902,4.91448e-05,-7.54173e-08,3.23307e-11,-16451,12.5367], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.57936,0.0119578,-5.48868e-06,1.25124e-09,-1.14137e-13,-18098.3,-11.3424], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 473,
    label = "C3H8O",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {1,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.90033,0.0323786,-1.01289e-05,-6.1869e-09,4.16086e-12,-34825.3,10.7973], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.0787,0.0286968,-1.34637e-05,3.09419e-09,-2.82105e-13,-35482.9,-0.884192], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 474,
    label = "CH3CHO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {6,D} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.30614,-0.00685025,5.20132e-05,-5.91279e-08,2.18564e-11,-21531.9,1.58779], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.8556,0.0184513,-9.06843e-06,2.16219e-09,-2.02928e-13,-21282.2,15.7474], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 475,
    label = "C3H8O(1)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  O u0 p2 c0 {2,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88084,0.0240214,9.03606e-06,-2.43721e-08,1.0405e-11,-33036.3,8.35708], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.3577,0.0300316,-1.45182e-05,3.41778e-09,-3.17705e-13,-33469.8,4.24729], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 476,
    label = "CH3OCH2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {3,S} {7,S} {8,S}
3 O u0 p2 c0 {1,S} {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.74677,0.00114737,3.43098e-05,-4.05966e-08,1.4728e-11,-1865.2,-1.00278], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.49254,0.0191936,-9.36652e-06,2.22394e-09,-2.08263e-13,-1793.19,7.82138], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 477,
    label = "CH3CHOCH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {7,S}
3 O u0 p2 c0 {2,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.40118,0.0111513,1.37761e-05,-2.39328e-08,9.90212e-12,-8591.12,5.6329], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.67657,0.0167677,-7.74482e-06,1.75698e-09,-1.58489e-13,-8911.38,2.82658], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 478,
    label = "C2H5",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.76286,-0.0058158,5.05352e-05,-5.93685e-08,2.26057e-11,12985,2.61478], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.67813,0.0174543,-8.07361e-06,1.82389e-09,-1.63296e-13,13226.6,15.2524], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

