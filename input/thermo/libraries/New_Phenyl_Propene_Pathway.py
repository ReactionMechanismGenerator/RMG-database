#!/usr/bin/env python
# encoding: utf-8

name = "New_Phenyl_Propene_Pathway"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "i1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,B} {6,B}
4  C u1 p0 c0 {1,S} {2,S} {15,S}
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
            NASAPolynomial(coeffs=[4.00081,0.0385974,3.95697e-05,-6.16325e-08,2.12095e-11,21579.7,13.7219], Tmin=(10,'K'), Tmax=(1100.43,'K')),
            NASAPolynomial(coeffs=[9.48435,0.0526681,-2.59594e-05,6.14599e-09,-5.67864e-13,18314.1,-22.6124], Tmin=(1100.43,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "i4",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,B} {5,B}
4  C u0 p0 c0 {3,B} {6,B} {14,S}
5  C u0 p0 c0 {3,B} {8,B} {18,S}
6  C u0 p0 c0 {4,B} {7,B} {15,S}
7  C u0 p0 c0 {6,B} {8,B} {16,S}
8  C u0 p0 c0 {5,B} {7,B} {17,S}
9  C u1 p0 c0 {2,S} {19,S} {20,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64623,0.0423681,4.67715e-05,-8.66774e-08,3.58928e-11,22814.4,13.9109], Tmin=(10,'K'), Tmax=(878.37,'K')),
            NASAPolynomial(coeffs=[4.112,0.0658116,-3.69204e-05,9.97857e-09,-1.04823e-12,21746.4,6.11046], Tmin=(878.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CBS-QB3""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "inew",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {5,B} {9,B}
5  C u0 p0 c0 {4,B} {6,B} {19,S}
6  C u0 p0 c0 {5,B} {7,B} {18,S}
7  C u0 p0 c0 {6,B} {8,B} {17,S}
8  C u0 p0 c0 {7,B} {9,B} {20,S}
9  C u1 p0 c0 {4,B} {8,B}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78189,0.042472,3.68578e-05,-6.59097e-08,2.47198e-11,29524.4,13.8146], Tmin=(10,'K'), Tmax=(1004.77,'K')),
            NASAPolynomial(coeffs=[6.80813,0.059324,-3.14441e-05,8.03489e-09,-8.01227e-13,27457.5,-8.05898], Tmin=(1004.77,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CBS-QB3""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "Benzyl",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {8,S}
3  C u0 p0 c0 {1,B} {6,B} {12,S}
4  C u0 p0 c0 {2,B} {5,B} {9,S}
5  C u0 p0 c0 {4,B} {6,B} {10,S}
6  C u0 p0 c0 {3,B} {5,B} {11,S}
7  C u1 p0 c0 {1,S} {13,S} {14,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.13967,-0.0141705,0.000261827,-4.75377e-07,2.76576e-10,23303.8,10.5068], Tmin=(10,'K'), Tmax=(549.1,'K')),
            NASAPolynomial(coeffs=[-0.663236,0.0580812,-3.7343e-05,1.14398e-08,-1.33776e-12,23269.5,25.6834], Tmin=(549.1,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CBS-QB3""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
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
            NASAPolynomial(coeffs=[4.10248,-0.00693587,5.16693e-05,-6.1712e-08,2.43092e-11,5201.67,3.22857], Tmin=(10,'K'), Tmax=(759.58,'K')),
            NASAPolynomial(coeffs=[0.478818,0.018145,-9.70523e-06,2.55181e-09,-2.63747e-13,5579.12,18.5751], Tmin=(759.58,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""CBS-QB3""",
    longDesc = 
u"""

""",
)

