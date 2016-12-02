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
            NASAPolynomial(coeffs=[3.98446,0.0359231,4.95879e-05,-7.38265e-08,2.59884e-11,21776.3,14.6342], Tmin=(10,'K'), Tmax=(1050.19,'K')),
            NASAPolynomial(coeffs=[7.56229,0.0565955,-2.89293e-05,7.11595e-09,-6.83367e-13,19133.3,-11.8073], Tmin=(1050.19,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[3.64765,0.0422834,4.68705e-05,-8.66594e-08,3.58477e-11,22840.2,13.2101], Tmin=(10,'K'), Tmax=(879.03,'K')),
            NASAPolynomial(coeffs=[4.09979,0.0657997,-3.68981e-05,9.96885e-09,-1.04688e-12,21772.7,5.46704], Tmin=(879.03,'K'), Tmax=(3000,'K')),
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
            NASAPolynomial(coeffs=[3.84153,0.0449036,2.56378e-05,-5.06324e-08,1.82455e-11,29521.8,28.3364], Tmin=(10,'K'), Tmax=(1088.42,'K')),
            NASAPolynomial(coeffs=[9.5501,0.0534954,-2.69564e-05,6.54392e-09,-6.20926e-13,26527.6,-7.73431], Tmin=(1088.42,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

