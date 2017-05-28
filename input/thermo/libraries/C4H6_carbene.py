#!/usr/bin/env python
# encoding: utf-8

name = "C4H6_carbene"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "C4H6_carbene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p1 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {8,S}
4  C u0 p0 c0 {3,D} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs = [3.92511, 0.0135168, 2.65849e-05, -3.73695e-08, 1.34958e-11, 45398.5, 8.76688],Tmin = (10, 'K'),Tmax = (968.356, 'K')),
            NASAPolynomial(coeffs = [3.12569, 0.0285955, -1.50143e-05, 3.82829e-09, -3.82491e-13, 45001.2, 9.74692],Tmin = (968.356, 'K'),Tmax = (3000, 'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

