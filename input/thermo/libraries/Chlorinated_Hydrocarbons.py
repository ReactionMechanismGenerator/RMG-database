#!/usr/bin/env python
# encoding: utf-8

name = "Chlorinated_Hydrocarbons"
shortDesc = u"Chlorinated Hydrocarbons used to fit/validate Benson and Bozzelli Cl GAV's and non-NNI's."
longDesc = u"""
Experimental values curated in the following references:

1976 Benson = Thermochemical Kinetics (book), 2nd edition, by Sidney Benson

1993 Wong and Bozzelli = 
David K. Wong, Douglas A. Kretkowski, Joseph W. Bozzelli, 
Standard Chemical Thermodynamic Properties of Monochloroalkanes, 
Ind. Eng. Chem. Res., 1993, 32, 3184-3188

1998 Chen and Bozzelli = 
Chinugh-Ju Chen, D. Wong, Joseph W. Bozzelli,
Standard Chemical Thermodynamic Properties of Multichloro Alkanes and Alkenes: A Modified Group Additivity Scheme
JPCA, 1998, 102, 4551-4558
"""
entry(
    index = 0,
    label = "Cl",
    molecule =
"""
multiplicity 2
1 Cl u1 p3 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.61674,9.55905e-13,-2.26881e-15,2.23748e-18,-7.78638e-22,13763.2,4.96934], Tmin=(298,'K'), Tmax=(1167.42,'K')),
            NASAPolynomial(coeffs=[2.61674,3.8212e-10,-4.56773e-13,2.41658e-16,-4.77396e-20,13763.2,4.96935], Tmin=(1167.42,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1976 Benson""",
    longDesc =
u"""

""",
)

entry(
    index = 1,
    label = "Cl2",
    molecule =
"""
1 Cl u0 p3 c0 {2,S}
2 Cl u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14206,0.00479031,-6.92268e-06,4.81713e-09,-1.29784e-12,-1096.85,7.7609], Tmin=(298,'K'), Tmax=(894.11,'K')),
            NASAPolynomial(coeffs=[3.88928,0.00148489,-1.44019e-06,7.76119e-10,-1.8104e-13,-1231.97,4.23125], Tmin=(894.11,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1976 Benson""",
    longDesc =
u"""

""",
)

entry(
    index = 2,
    label = "HCl",
    molecule =
"""
1 Cl u0 p3 c0 {2,S}
2 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53628,0.000374097,-2.62701e-06,4.78617e-09,-2.27479e-12,-12126.4,2.26447], Tmin=(298,'K'), Tmax=(674.86,'K')),
            NASAPolynomial(coeffs=[4.11121,-0.00302163,4.89403e-06,-2.61729e-09,4.58076e-13,-12204.3,-0.285156], Tmin=(674.86,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1976 Benson""",
    longDesc =
u"""

""",
)

entry(
    index = 3,
    label = "ClO",
    molecule = 
"""
multiplicity 2
1 Cl u0 p3 c0 {2,S}
2 O  u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.32449,0.000246424,7.1635e-06,-1.16098e-08,5.42331e-12,11133.4,7.98445], Tmin=(298,'K'), Tmax=(627.97,'K')),
            NASAPolynomial(coeffs=[2.39177,0.00620933,-7.13173e-06,3.62145e-09,-6.62331e-13,11250.1,12.0469], Tmin=(627.97,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1976 Benson""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "CCl4",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 Cl u0 p3 c0 {2,S}
4 Cl u0 p3 c0 {2,S}
5 Cl u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.83114,0.0400388,-6.92547e-05,5.78087e-08,-1.8956e-11,-13639.3,11.8805], Tmin=(298,'K'), Tmax=(711.74,'K')),
            NASAPolynomial(coeffs=[7.23134,0.0153093,-1.71368e-05,8.99091e-09,-1.80854e-12,-14265.7,-7.85163], Tmin=(711.74,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1976 Benson""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "CHCl3",
    molecule = 
"""
1 Cl u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 Cl u0 p3 c0 {2,S}
4 Cl u0 p3 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.50654,0.0318882,-4.31201e-05,2.81802e-08,-6.90751e-12,-13916,19.1716], Tmin=(298,'K'), Tmax=(811.17,'K')),
            NASAPolynomial(coeffs=[5.93472,0.0128665,-1.315e-05,7.82627e-09,-1.95272e-12,-14727,-1.83579], Tmin=(811.17,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1976 Benson""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "CH2Cl2",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 H  u0 p0 c0 {1,S}
3 H  u0 p0 c0 {1,S}
4 Cl u0 p3 c0 {1,S}
5 Cl u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.67987,0.0181637,-1.07685e-05,-1.85287e-09,3.41554e-12,-12683.5,18.0126], Tmin=(298,'K'), Tmax=(684.96,'K')),
            NASAPolynomial(coeffs=[1.93499,0.0185429,-1.56921e-05,6.92293e-09,-1.24151e-12,-12762.3,16.5582], Tmin=(684.96,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1976 Benson""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "CdCCl",
    molecule = 
"""
1 C  u0 p0 c0 {2,D} {4,S} {5,S}
2 C  u0 p0 c0 {1,D} {3,S} {6,S}
3 Cl u0 p3 c0 {2,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70051,0.000863876,4.61027e-05,-6.94228e-08,3.16348e-11,1090.31,8.91651], Tmin=(298,'K'), Tmax=(590.44,'K')),
            NASAPolynomial(coeffs=[0.152401,0.0243855,-1.2344e-05,-4.90911e-09,4.9449e-12,1518.28,24.2407], Tmin=(590.44,'K'), Tmax=(1000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1000,'K'),
    ),
    shortDesc = u"""1976 Benson""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "C6H5Cl",
    molecule = 
"""
1  C  u0 p0 c0 {2,B} {6,B} {7,S}
2  C  u0 p0 c0 {1,B} {3,B} {8,S}
3  C  u0 p0 c0 {2,B} {4,B} {9,S}
4  C  u0 p0 c0 {3,B} {5,B} {10,S}
5  C  u0 p0 c0 {4,B} {6,B} {11,S}
6  C  u0 p0 c0 {1,B} {5,B} {12,S}
7  Cl u0 p3 c0 {1,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {4,S}
11 H  u0 p0 c0 {5,S}
12 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0551034,0.0337056,5.12838e-05,-1.2581e-07,7.14182e-11,4572.15,26.8036], Tmin=(298,'K'), Tmax=(522.72,'K')),
            NASAPolynomial(coeffs=[-6.02157,0.0793436,-7.96246e-05,4.10785e-08,-8.36573e-12,5196.17,51.7203], Tmin=(522.72,'K'), Tmax=(1000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1000,'K'),
    ),
    shortDesc = u"""1976 Benson""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "CCCl",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C  u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 Cl u0 p3 c0 {2,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.32978,0.0140164,2.38175e-05,-4.70191e-08,2.35863e-11,-14946.5,15.028], Tmin=(298,'K'), Tmax=(563.06,'K')),
            NASAPolynomial(coeffs=[-0.201322,0.0320051,-2.41253e-05,9.7697e-09,-1.63882e-12,-14661.6,25.7843], Tmin=(563.06,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1993 Wong and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "CCCCl",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C  u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C  u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  H  u0 p0 c0 {1,S}
5  H  u0 p0 c0 {1,S}
6  Cl u0 p3 c0 {3,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.81032,0.0280584,1.03229e-05,-3.59375e-08,1.83136e-11,-17831.6,19.0903], Tmin=(298,'K'), Tmax=(607.26,'K')),
            NASAPolynomial(coeffs=[-0.950142,0.0462881,-3.48217e-05,1.375e-08,-2.19403e-12,-17497.2,31.0239], Tmin=(607.26,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1993 Wong and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "CCCCCl",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C  u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4  C  u0 p0 c0 {2,S} {9,S} {13,S} {14,S}
5  H  u0 p0 c0 {1,S}
6  H  u0 p0 c0 {1,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  Cl u0 p3 c0 {4,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {3,S}
13 H  u0 p0 c0 {4,S}
14 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.17605,0.0347338,1.99235e-05,-5.70633e-08,2.97031e-11,-20801.5,19.5306], Tmin=(298,'K'), Tmax=(570.4,'K')),
            NASAPolynomial(coeffs=[-1.25898,0.0588244,-4.34334e-05,1.69925e-08,-2.75736e-12,-20409.6,34.1739], Tmin=(570.4,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1993 Wong and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "CCCCCCl",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C  u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C  u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C  u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
5  C  u0 p0 c0 {3,S} {12,S} {16,S} {17,S}
6  H  u0 p0 c0 {2,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {1,S}
9  H  u0 p0 c0 {1,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
12 Cl u0 p3 c0 {5,S}
13 H  u0 p0 c0 {4,S}
14 H  u0 p0 c0 {4,S}
15 H  u0 p0 c0 {4,S}
16 H  u0 p0 c0 {5,S}
17 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.30444,0.0364283,3.96983e-05,-8.54626e-08,4.20001e-11,-23853.3,16.7158], Tmin=(298,'K'), Tmax=(586.53,'K')),
            NASAPolynomial(coeffs=[-2.06428,0.0730422,-5.39397e-05,2.09702e-08,-3.36589e-12,-23223.5,39.7524], Tmin=(586.53,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1993 Wong and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "CCCCCCCl",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C  u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C  u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
4  C  u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C  u0 p0 c0 {3,S} {16,S} {17,S} {18,S}
6  C  u0 p0 c0 {4,S} {15,S} {19,S} {20,S}
7  H  u0 p0 c0 {3,S}
8  H  u0 p0 c0 {3,S}
9  H  u0 p0 c0 {1,S}
10 H  u0 p0 c0 {1,S}
11 H  u0 p0 c0 {2,S}
12 H  u0 p0 c0 {2,S}
13 H  u0 p0 c0 {4,S}
14 H  u0 p0 c0 {4,S}
15 Cl u0 p3 c0 {6,S}
16 H  u0 p0 c0 {5,S}
17 H  u0 p0 c0 {5,S}
18 H  u0 p0 c0 {5,S}
19 H  u0 p0 c0 {6,S}
20 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.89867,0.0483792,3.64182e-05,-9.2281e-08,4.7178e-11,-26739.2,20.4373], Tmin=(298,'K'), Tmax=(574.55,'K')),
            NASAPolynomial(coeffs=[-2.7015,0.0873692,-6.53791e-05,2.58426e-08,-4.22266e-12,-26095.7,44.3512], Tmin=(574.55,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1993 Wong and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "CC(Cl)C",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  Cl u0 p3 c0 {1,S}
5  H  u0 p0 c0 {1,S}
6  H  u0 p0 c0 {2,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.82242,0.0313419,-8.9434e-07,-2.37296e-08,1.40515e-11,-19298,17.2944], Tmin=(298,'K'), Tmax=(601.56,'K')),
            NASAPolynomial(coeffs=[0.354877,0.0421426,-3.04257e-05,1.18788e-08,-1.94419e-12,-19140.3,23.4718], Tmin=(601.56,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1993 Wong and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "CC(Cl)CC",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C  u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  Cl u0 p3 c0 {1,S}
6  H  u0 p0 c0 {1,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {4,S}
14 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.15563,0.0387134,4.98499e-06,-3.76851e-08,2.09343e-11,-22268.3,18.5127], Tmin=(298,'K'), Tmax=(568.34,'K')),
            NASAPolynomial(coeffs=[-0.291522,0.0559362,-4.04692e-05,1.56317e-08,-2.51797e-12,-21990.1,28.9361], Tmin=(568.34,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1993 Wong and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "CC(Cl)CCC",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C  u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C  u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C  u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C  u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  Cl u0 p3 c0 {2,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {1,S}
9  H  u0 p0 c0 {1,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {4,S}
14 H  u0 p0 c0 {4,S}
15 H  u0 p0 c0 {5,S}
16 H  u0 p0 c0 {5,S}
17 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.38652,0.04648,1.07913e-05,-5.25913e-08,2.85822e-11,-25223.5,19.517], Tmin=(298,'K'), Tmax=(570.29,'K')),
            NASAPolynomial(coeffs=[-0.977945,0.0700814,-5.12947e-05,1.99967e-08,-3.24271e-12,-24839.8,33.8587], Tmin=(570.29,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1993 Wong and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "CCC(Cl)CC",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C  u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C  u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  C  u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  Cl u0 p3 c0 {1,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {1,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {4,S}
14 H  u0 p0 c0 {4,S}
15 H  u0 p0 c0 {5,S}
16 H  u0 p0 c0 {5,S}
17 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.38652,0.04648,1.07913e-05,-5.25913e-08,2.85822e-11,-25223.5,18.8226], Tmin=(298,'K'), Tmax=(570.29,'K')),
            NASAPolynomial(coeffs=[-0.977945,0.0700814,-5.12947e-05,1.99967e-08,-3.24271e-12,-24839.8,33.1642], Tmin=(570.29,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1993 Wong and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "CC(C)C(Cl)C",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C  u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C  u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C  u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6  H  u0 p0 c0 {1,S}
7  Cl u0 p3 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {4,S}
14 H  u0 p0 c0 {4,S}
15 H  u0 p0 c0 {5,S}
16 H  u0 p0 c0 {5,S}
17 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.576411,0.057293,-1.38187e-05,-2.5751e-08,1.78024e-11,-25483.1,26.1105], Tmin=(298,'K'), Tmax=(528.58,'K')),
            NASAPolynomial(coeffs=[-1.00286,0.0692764,-4.7917e-05,1.7371e-08,-2.6476e-12,-25316.6,32.7185], Tmin=(528.58,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1993 Wong and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "CC(C)(Cl)CCC",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C  u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C  u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
4  C  u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C  u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  C  u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
7  Cl u0 p3 c0 {1,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {4,S}
14 H  u0 p0 c0 {4,S}
15 H  u0 p0 c0 {5,S}
16 H  u0 p0 c0 {5,S}
17 H  u0 p0 c0 {5,S}
18 H  u0 p0 c0 {6,S}
19 H  u0 p0 c0 {6,S}
20 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.89583,0.0571898,2.05011e-05,-8.05205e-08,4.4057e-11,-29998.9,20.7073], Tmin=(298,'K'), Tmax=(605.51,'K')),
            NASAPolynomial(coeffs=[-2.72729,0.0909842,-7.12774e-05,2.94031e-08,-4.9923e-12,-29498.6,40.1992], Tmin=(605.51,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1993 Wong and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "CCC(C)(Cl)CC",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C  u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C  u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  C  u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C  u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
6  C  u0 p0 c0 {3,S} {18,S} {19,S} {20,S}
7  Cl u0 p3 c0 {1,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {5,S}
13 H  u0 p0 c0 {5,S}
14 H  u0 p0 c0 {5,S}
15 H  u0 p0 c0 {4,S}
16 H  u0 p0 c0 {4,S}
17 H  u0 p0 c0 {4,S}
18 H  u0 p0 c0 {6,S}
19 H  u0 p0 c0 {6,S}
20 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.89583,0.0571898,2.05011e-05,-8.05205e-08,4.4057e-11,-29596.3,20.7073], Tmin=(298,'K'), Tmax=(605.51,'K')),
            NASAPolynomial(coeffs=[-2.72729,0.0909842,-7.12774e-05,2.94031e-08,-4.9923e-12,-29096.1,40.1992], Tmin=(605.51,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1993 Wong and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "CC(C)(Cl)C(C)C",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C  u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
3  C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C  u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C  u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6  C  u0 p0 c0 {2,S} {18,S} {19,S} {20,S}
7  Cl u0 p3 c0 {1,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {4,S}
14 H  u0 p0 c0 {4,S}
15 H  u0 p0 c0 {5,S}
16 H  u0 p0 c0 {5,S}
17 H  u0 p0 c0 {5,S}
18 H  u0 p0 c0 {6,S}
19 H  u0 p0 c0 {6,S}
20 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.53413,0.0484356,5.17966e-05,-1.22265e-07,6.41736e-11,-30491.7,17.2448], Tmin=(298,'K'), Tmax=(551.89,'K')),
            NASAPolynomial(coeffs=[-3.90852,0.0951286,-7.51058e-05,3.10219e-08,-5.26052e-12,-29780.6,44.4976], Tmin=(551.89,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1993 Wong and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "CC(C)(Cl)C",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C  u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  Cl u0 p3 c0 {1,S}
6  H  u0 p0 c0 {2,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {4,S}
14 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.415151,0.0495333,-1.35191e-05,-2.25363e-08,1.54893e-11,-24388.8,21.8317], Tmin=(298,'K'), Tmax=(653.69,'K')),
            NASAPolynomial(coeffs=[-1.18607,0.0621751,-4.9053e-05,2.0358e-08,-3.46058e-12,-24240.3,28.4113], Tmin=(653.69,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1993 Wong and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "CC(C)(Cl)CC",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C  u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C  u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  C  u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6  Cl u0 p3 c0 {1,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
12 H  u0 p0 c0 {4,S}
13 H  u0 p0 c0 {4,S}
14 H  u0 p0 c0 {4,S}
15 H  u0 p0 c0 {5,S}
16 H  u0 p0 c0 {5,S}
17 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.4748,0.0510053,9.76035e-06,-5.88541e-08,3.29848e-11,-27025.5,20.481], Tmin=(298,'K'), Tmax=(619.62,'K')),
            NASAPolynomial(coeffs=[-1.97116,0.0765372,-6.00037e-05,2.47665e-08,-4.20727e-12,-26661.5,34.9473], Tmin=(619.62,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1993 Wong and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "CCCl2",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3 Cl u0 p3 c0 {2,S}
4 Cl u0 p3 c0 {2,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {1,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.512359,0.0461457,-7.61626e-05,7.91009e-08,-3.28935e-11,-17320.4,22.7682], Tmin=(298,'K'), Tmax=(913.73,'K')),
            NASAPolynomial(coeffs=[23.2425,-0.0559748,9.57746e-05,-4.94791e-08,3.14363e-12,-21365.1,-84.2434], Tmin=(913.73,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "C(Cl)2CC",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  H  u0 p0 c0 {1,S}
5  H  u0 p0 c0 {1,S}
6  Cl u0 p3 c0 {2,S}
7  Cl u0 p3 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.80593,0.0407571,-2.26961e-05,-1.27102e-09,4.6747e-12,-20278.3,20.0358], Tmin=(298,'K'), Tmax=(691.58,'K')),
            NASAPolynomial(coeffs=[1.61583,0.0438948,-3.39222e-05,1.3812e-08,-2.3181e-12,-20300.8,20.5304], Tmin=(691.58,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "C(Cl)2CCC",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  Cl u0 p3 c0 {1,S}
3  Cl u0 p3 c0 {1,S}
4  C  u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
5  C  u0 p0 c0 {4,S} {6,S} {10,S} {11,S}
6  C  u0 p0 c0 {5,S} {12,S} {13,S} {14,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {4,S}
9  H  u0 p0 c0 {4,S}
10 H  u0 p0 c0 {5,S}
11 H  u0 p0 c0 {5,S}
12 H  u0 p0 c0 {6,S}
13 H  u0 p0 c0 {6,S}
14 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.17738,0.0474197,-1.38561e-05,-1.9645e-08,1.37311e-11,-23211.7,20.4564], Tmin=(298,'K'), Tmax=(659.98,'K')),
            NASAPolynomial(coeffs=[0.770368,0.0586675,-4.56024e-05,1.86681e-08,-3.14758e-12,-23085.3,26.2109], Tmin=(659.98,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "C(Cl)2CCCC",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  Cl u0 p3 c0 {1,S}
3  Cl u0 p3 c0 {1,S}
4  C  u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
5  C  u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
6  C  u0 p0 c0 {5,S} {7,S} {13,S} {14,S}
7  C  u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
8  H  u0 p0 c0 {1,S}
9  H  u0 p0 c0 {4,S}
10 H  u0 p0 c0 {4,S}
11 H  u0 p0 c0 {5,S}
12 H  u0 p0 c0 {5,S}
13 H  u0 p0 c0 {6,S}
14 H  u0 p0 c0 {6,S}
15 H  u0 p0 c0 {7,S}
16 H  u0 p0 c0 {7,S}
17 H  u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.59855,0.0538013,-4.33268e-06,-3.89755e-08,2.33426e-11,-26151.9,20.6595], Tmin=(298,'K'), Tmax=(639.74,'K')),
            NASAPolynomial(coeffs=[-0.00242983,0.0731396,-5.68863e-05,2.33048e-08,-3.93202e-12,-25882,31.554], Tmin=(639.74,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "C(Cl)2CCCCC",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  Cl u0 p3 c0 {1,S}
3  Cl u0 p3 c0 {1,S}
4  C  u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
5  C  u0 p0 c0 {4,S} {6,S} {12,S} {13,S}
6  C  u0 p0 c0 {5,S} {7,S} {14,S} {15,S}
7  C  u0 p0 c0 {6,S} {8,S} {16,S} {17,S}
8  C  u0 p0 c0 {7,S} {18,S} {19,S} {20,S}
9  H  u0 p0 c0 {1,S}
10 H  u0 p0 c0 {4,S}
11 H  u0 p0 c0 {4,S}
12 H  u0 p0 c0 {5,S}
13 H  u0 p0 c0 {5,S}
14 H  u0 p0 c0 {6,S}
15 H  u0 p0 c0 {6,S}
16 H  u0 p0 c0 {7,S}
17 H  u0 p0 c0 {7,S}
18 H  u0 p0 c0 {8,S}
19 H  u0 p0 c0 {8,S}
20 H  u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.00459,0.0601038,5.89147e-06,-5.96383e-08,3.3749e-11,-29087.9,20.9514], Tmin=(298,'K'), Tmax=(623.75,'K')),
            NASAPolynomial(coeffs=[-0.791547,0.0876997,-6.82918e-05,2.80074e-08,-4.7295e-12,-28677.6,36.9667], Tmin=(623.75,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "C(Cl)CCCl",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C  u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C  u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
4  H  u0 p0 c0 {1,S}
5  H  u0 p0 c0 {1,S}
6  Cl u0 p3 c0 {2,S}
7  Cl u0 p3 c0 {3,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.17495,0.0970173,-0.000169471,1.65367e-07,-6.567e-11,-20692.1,54.6888], Tmin=(298,'K'), Tmax=(573.76,'K')),
            NASAPolynomial(coeffs=[-0.158966,0.0550695,-5.97871e-05,3.79016e-08,-1.01212e-11,-21382.3,29.0083], Tmin=(573.76,'K'), Tmax=(1000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1000,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "CC(Cl)2C",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  Cl u0 p3 c0 {1,S}
5  Cl u0 p3 c0 {1,S}
6  H  u0 p0 c0 {2,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.979062,0.0520981,-4.7751e-05,1.94683e-08,-8.37587e-13,-23357,20.0579], Tmin=(298,'K'), Tmax=(559.02,'K')),
            NASAPolynomial(coeffs=[1.04434,0.0527663,-5.25901e-05,2.88721e-08,-6.66767e-12,-23382,19.6223], Tmin=(559.02,'K'), Tmax=(1000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1000,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "CCCl3",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 Cl u0 p3 c0 {2,S}
4 Cl u0 p3 c0 {2,S}
5 Cl u0 p3 c0 {2,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {1,S}
8 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.29913,0.0412837,-4.69313e-05,2.87332e-08,-7.36017e-12,-19271.9,14.9352], Tmin=(298,'K'), Tmax=(818.66,'K')),
            NASAPolynomial(coeffs=[4.74855,0.0293162,-2.50042e-05,1.08775e-08,-1.90761e-12,-19673,3.60819], Tmin=(818.66,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "C(Cl)3CC",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  H  u0 p0 c0 {1,S}
5  H  u0 p0 c0 {1,S}
6  Cl u0 p3 c0 {2,S}
7  Cl u0 p3 c0 {2,S}
8  Cl u0 p3 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.32005,0.0509792,-4.74012e-05,2.25688e-08,-4.14217e-12,-22174.7,16.7662], Tmin=(298,'K'), Tmax=(783.41,'K')),
            NASAPolynomial(coeffs=[4.3106,0.0425466,-3.45693e-05,1.44693e-08,-2.45745e-12,-22539.7,7.30982], Tmin=(783.41,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "C(Cl)3CCC",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  Cl u0 p3 c0 {1,S}
3  Cl u0 p3 c0 {1,S}
4  Cl u0 p3 c0 {1,S}
5  C  u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
6  C  u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
7  C  u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
8  H  u0 p0 c0 {5,S}
9  H  u0 p0 c0 {5,S}
10 H  u0 p0 c0 {6,S}
11 H  u0 p0 c0 {6,S}
12 H  u0 p0 c0 {7,S}
13 H  u0 p0 c0 {7,S}
14 H  u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.57071,0.0587221,-4.20424e-05,8.99841e-09,2.49099e-12,-25102.7,17.675], Tmin=(298,'K'), Tmax=(720.94,'K')),
            NASAPolynomial(coeffs=[3.27193,0.0580165,-4.72011e-05,1.98966e-08,-3.4131e-12,-25286.6,13.9474], Tmin=(720.94,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "C(Cl)3CCCC",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  Cl u0 p3 c0 {1,S}
3  Cl u0 p3 c0 {1,S}
4  Cl u0 p3 c0 {1,S}
5  C  u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
6  C  u0 p0 c0 {5,S} {7,S} {11,S} {12,S}
7  C  u0 p0 c0 {6,S} {8,S} {13,S} {14,S}
8  C  u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
9  H  u0 p0 c0 {5,S}
10 H  u0 p0 c0 {5,S}
11 H  u0 p0 c0 {6,S}
12 H  u0 p0 c0 {6,S}
13 H  u0 p0 c0 {7,S}
14 H  u0 p0 c0 {7,S}
15 H  u0 p0 c0 {8,S}
16 H  u0 p0 c0 {8,S}
17 H  u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.03319,0.0648658,-3.2283e-05,-9.88367e-09,1.15201e-11,-28042.3,17.7003], Tmin=(298,'K'), Tmax=(690,'K')),
            NASAPolynomial(coeffs=[2.33207,0.0731082,-5.92836e-05,2.4979e-08,-4.29061e-12,-28045,20.102], Tmin=(690,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "C(Cl)3CCCCC",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  Cl u0 p3 c0 {1,S}
3  Cl u0 p3 c0 {1,S}
4  Cl u0 p3 c0 {1,S}
5  C  u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
6  C  u0 p0 c0 {5,S} {7,S} {12,S} {13,S}
7  C  u0 p0 c0 {6,S} {8,S} {14,S} {15,S}
8  C  u0 p0 c0 {7,S} {9,S} {16,S} {17,S}
9  C  u0 p0 c0 {8,S} {18,S} {19,S} {20,S}
10 H  u0 p0 c0 {5,S}
11 H  u0 p0 c0 {5,S}
12 H  u0 p0 c0 {6,S}
13 H  u0 p0 c0 {6,S}
14 H  u0 p0 c0 {7,S}
15 H  u0 p0 c0 {7,S}
16 H  u0 p0 c0 {8,S}
17 H  u0 p0 c0 {8,S}
18 H  u0 p0 c0 {9,S}
19 H  u0 p0 c0 {9,S}
20 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.24954,0.0727667,-2.69313e-05,-2.40556e-08,1.87059e-11,-30961.1,18.7571], Tmin=(298,'K'), Tmax=(676.25,'K')),
            NASAPolynomial(coeffs=[1.56363,0.0876041,-7.0634e-05,2.96666e-08,-5.08741e-12,-30844.3,25.4086], Tmin=(676.25,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "CdCCl2",
    molecule = 
"""
1 C  u0 p0 c0 {2,D} {5,S} {6,S}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 Cl u0 p3 c0 {2,S}
4 Cl u0 p3 c0 {2,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.76352,0.028215,-2.65984e-05,1.01272e-08,-2.00787e-13,-1276.74,16.8057], Tmin=(298,'K'), Tmax=(756.3,'K')),
            NASAPolynomial(coeffs=[3.51373,0.0222079,-2.11296e-05,1.09878e-08,-2.36329e-12,-1634.41,8.23636], Tmin=(756.3,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "CdC(Cl)CdC",
    molecule = 
"""
1  C  u0 p0 c0 {2,D} {6,S} {7,S}
2  C  u0 p0 c0 {1,D} {3,S} {4,S}
3  Cl u0 p3 c0 {2,S}
4  C  u0 p0 c0 {2,S} {5,D} {8,S}
5  C  u0 p0 c0 {4,D} {9,S} {10,S}
6  H  u0 p0 c0 {1,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {4,S}
9  H  u0 p0 c0 {5,S}
10 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.28961,0.0265968,3.44156e-05,-9.70634e-08,6.01897e-11,1337.61,15.9356], Tmin=(298,'K'), Tmax=(489.98,'K')),
            NASAPolynomial(coeffs=[-1.64963,0.0589093,-6.49758e-05,3.88103e-08,-9.46387e-12,1721.79,32.1111], Tmin=(489.98,'K'), Tmax=(1000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1000,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "CdC(Cl)C(Cl)dC",
    molecule = 
"""
1  C  u0 p0 c0 {2,D} {7,S} {8,S}
2  C  u0 p0 c0 {1,D} {3,S} {4,S}
3  Cl u0 p3 c0 {2,S}
4  C  u0 p0 c0 {2,S} {5,S} {6,D}
5  Cl u0 p3 c0 {4,S}
6  C  u0 p0 c0 {4,D} {9,S} {10,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {1,S}
9  H  u0 p0 c0 {6,S}
10 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.686249,0.0517933,-3.86086e-05,-3.83053e-09,1.44456e-11,-8694.67,22.5677], Tmin=(298,'K'), Tmax=(524.67,'K')),
            NASAPolynomial(coeffs=[-0.45456,0.0619142,-7.1614e-05,4.32791e-08,-1.04659e-11,-8594.56,27.1489], Tmin=(524.67,'K'), Tmax=(1000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1000,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "C(Cl)2dC(Cl)CdC",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,D}
2  Cl u0 p3 c0 {1,S}
3  Cl u0 p3 c0 {1,S}
4  C  u0 p0 c0 {1,D} {5,S} {6,S}
5  Cl u0 p3 c0 {4,S}
6  C  u0 p0 c0 {4,S} {7,D} {8,S}
7  C  u0 p0 c0 {6,D} {9,S} {10,S}
8  H  u0 p0 c0 {6,S}
9  H  u0 p0 c0 {7,S}
10 H  u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97216,0.0506259,-5.85279e-05,3.85793e-08,-1.13178e-11,-4098.16,11.2129], Tmin=(298,'K'), Tmax=(595.58,'K')),
            NASAPolynomial(coeffs=[4.67297,0.0459202,-4.6679e-05,2.5319e-08,-5.75295e-12,-4181.66,8.19487], Tmin=(595.58,'K'), Tmax=(1000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1000,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "C(Cl)CCl",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3 Cl u0 p3 c0 {1,S}
4 Cl u0 p3 c0 {2,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.46637,0.0296883,-2.44724e-05,1.15411e-08,-2.3958e-12,-17106.5,14.8766], Tmin=(298,'K'), Tmax=(904.62,'K')),
            NASAPolynomial(coeffs=[3.39723,0.0255735,-1.76515e-05,6.51586e-09,-1.00743e-12,-17274.9,10.4788], Tmin=(904.62,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "C(Cl)C(Cl)C",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  Cl u0 p3 c0 {1,S}
5  H  u0 p0 c0 {1,S}
6  Cl u0 p3 c0 {2,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.93154,0.0393061,-1.85843e-05,-7.47791e-09,8.76435e-12,-22073.8,20.4269], Tmin=(298,'K'), Tmax=(496.47,'K')),
            NASAPolynomial(coeffs=[1.21213,0.0451024,-3.60967e-05,1.6038e-08,-3.07722e-12,-22002.3,23.3939], Tmin=(496.47,'K'), Tmax=(1000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1000,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "C(Cl)2CCl",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2 C  u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3 Cl u0 p3 c0 {1,S}
4 Cl u0 p3 c0 {1,S}
5 Cl u0 p3 c0 {2,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.00748,0.0434144,-4.58072e-05,2.44236e-08,-4.99476e-12,-19260.9,23.2526], Tmin=(298,'K'), Tmax=(783.84,'K')),
            NASAPolynomial(coeffs=[3.52069,0.0325043,-2.85934e-05,1.28999e-08,-2.31343e-12,-19713.7,11.3647], Tmin=(783.84,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "C(Cl)C(Cl)CCl",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C  u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C  u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
4  Cl u0 p3 c0 {1,S}
5  H  u0 p0 c0 {1,S}
6  Cl u0 p3 c0 {2,S}
7  Cl u0 p3 c0 {3,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.39744,0.043422,-3.525e-05,1.38905e-08,-1.53081e-12,-24999.1,15.205], Tmin=(298,'K'), Tmax=(581.33,'K')),
            NASAPolynomial(coeffs=[3.25616,0.0445961,-3.88005e-05,1.85598e-08,-3.7958e-12,-24986.1,15.7806], Tmin=(581.33,'K'), Tmax=(1000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1000,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "C(Cl)3CCl",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 Cl u0 p3 c0 {1,S}
4 Cl u0 p3 c0 {1,S}
5 Cl u0 p3 c0 {1,S}
6 Cl u0 p3 c0 {2,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2181,0.0433842,-5.04317e-05,3.0891e-08,-7.86359e-12,-20467.6,13.5188], Tmin=(298,'K'), Tmax=(822.87,'K')),
            NASAPolynomial(coeffs=[5.8541,0.0305703,-2.70732e-05,1.19663e-08,-2.11393e-12,-20901.4,1.31551], Tmin=(822.87,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "C(Cl)2CCl2",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 C  u0 p0 c0 {1,S} {5,S} {6,S} {8,S}
3 Cl u0 p3 c0 {1,S}
4 Cl u0 p3 c0 {1,S}
5 Cl u0 p3 c0 {2,S}
6 Cl u0 p3 c0 {2,S}
7 H  u0 p0 c0 {1,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.70499,0.0505274,-6.54046e-05,4.50572e-08,-1.28419e-11,-20177.1,20.4544], Tmin=(298,'K'), Tmax=(764.26,'K')),
            NASAPolynomial(coeffs=[5.2707,0.031865,-2.87759e-05,1.31056e-08,-2.39005e-12,-20722.1,4.21056], Tmin=(764.26,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "C(Cl)2CCl3",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2 Cl u0 p3 c0 {1,S}
3 Cl u0 p3 c0 {1,S}
4 C  u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 Cl u0 p3 c0 {4,S}
6 Cl u0 p3 c0 {4,S}
7 Cl u0 p3 c0 {4,S}
8 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.85077,0.0598949,-9.29124e-05,7.39932e-08,-2.38138e-11,-19933.5,15.1977], Tmin=(298,'K'), Tmax=(707.27,'K')),
            NASAPolynomial(coeffs=[8.11588,0.0301177,-2.97602e-05,1.44664e-08,-2.77279e-12,-20678.3,-8.37986], Tmin=(707.27,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "C(Cl)3CCl3",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 Cl u0 p3 c0 {1,S}
3 Cl u0 p3 c0 {1,S}
4 Cl u0 p3 c0 {1,S}
5 C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6 Cl u0 p3 c0 {5,S}
7 Cl u0 p3 c0 {5,S}
8 Cl u0 p3 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78054,0.071356,-0.000125594,1.0832e-07,-3.69183e-11,-20392.1,9.58175], Tmin=(298,'K'), Tmax=(685.6,'K')),
            NASAPolynomial(coeffs=[11.2472,0.0277925,-3.02809e-05,1.56386e-08,-3.12193e-12,-21415.9,-23.6222], Tmin=(685.6,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "C(Cl)dCCl",
    molecule = 
"""
1 C  u0 p0 c0 {2,D} {3,S} {5,S}
2 C  u0 p0 c0 {1,D} {4,S} {6,S}
3 Cl u0 p3 c0 {1,S}
4 Cl u0 p3 c0 {2,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.08652,0.0231642,-1.10394e-05,-8.49205e-09,7.71988e-12,-1876.98,16.5926], Tmin=(298,'K'), Tmax=(709.74,'K')),
            NASAPolynomial(coeffs=[1.57335,0.0295454,-3.18996e-05,1.80286e-08,-4.06163e-12,-1892.01,18.2734], Tmin=(709.74,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "C(Cl)dCCl2",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,D} {6,S}
2 Cl u0 p3 c0 {1,S}
3 C  u0 p0 c0 {1,D} {4,S} {5,S}
4 Cl u0 p3 c0 {3,S}
5 Cl u0 p3 c0 {3,S}
6 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.59814,0.035411,-4.84632e-05,3.49474e-08,-1.03615e-11,-2959.34,15.6098], Tmin=(298,'K'), Tmax=(744.83,'K')),
            NASAPolynomial(coeffs=[5.26964,0.0210647,-1.95727e-05,9.08979e-09,-1.68287e-12,-3357.32,3.50827], Tmin=(744.83,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "C(Cl)2dCCl2",
    molecule = 
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,D}
2 Cl u0 p3 c0 {1,S}
3 Cl u0 p3 c0 {1,S}
4 C  u0 p0 c0 {1,D} {5,S} {6,S}
5 Cl u0 p3 c0 {4,S}
6 Cl u0 p3 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.20208,0.0376916,-5.66531e-05,4.31468e-08,-1.33163e-11,-3964.19,7.98669], Tmin=(298,'K'), Tmax=(725.26,'K')),
            NASAPolynomial(coeffs=[7.35262,0.0203154,-2.07151e-05,1.01121e-08,-1.92906e-12,-4421.19,-6.20082], Tmin=(725.26,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""1998Chen and Bozzelli""",
    longDesc = 
u"""

""",
)

