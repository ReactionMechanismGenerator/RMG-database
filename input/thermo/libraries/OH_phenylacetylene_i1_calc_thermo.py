#!/usr/bin/env python
# encoding: utf-8

name = "OH_phenylacetylene_i1_calc_thermo"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "i1_calc",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {8,S}
2  C u0 p0 c0 {1,B} {4,B} {11,S}
3  C u0 p0 c0 {1,B} {6,B} {14,S}
4  C u0 p0 c0 {2,B} {5,B} {12,S}
5  C u0 p0 c0 {4,B} {6,B} {10,S}
6  C u0 p0 c0 {3,B} {5,B} {13,S}
7  C u0 p0 c0 {8,D} {9,S} {15,S}
8  C u1 p0 c0 {1,S} {7,D}
9  O u0 p2 c0 {7,S} {16,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82517,0.011586,0.000231769,-5.20586e-07,3.59184e-10,31557.7,14.1379], Tmin=(10,'K'), Tmax=(468.98,'K')),
            NASAPolynomial(coeffs=[1.0834,0.0663411,-4.36955e-05,1.36185e-08,-1.61407e-12,31469.9,21.6112], Tmin=(468.98,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

