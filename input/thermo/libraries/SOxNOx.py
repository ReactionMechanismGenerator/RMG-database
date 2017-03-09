#!/usr/bin/env python
# encoding: utf-8

name = ""
shortDesc = u"SOx-NOx"
longDesc = u"""

"""

entry(
    index = 1,
    label = "C",
    molecule = 
"""
multiplicity 5
1 C u4 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.55424,-0.000321538,7.33792e-07,-7.32235e-10,2.66521e-13,85442.7,4.53131], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.60558,-0.000195934,1.06737e-07,-1.64239e-11,8.18706e-16,85411.7,4.19239], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""L 7/88""",
    longDesc = 
u"""
AramcoMech
W. K. Metcalfe, S. M. Burke, S. S. Ahmed, H. J. Curran
A Hierarchical and Comparative Kinetic Modeling Study of C1-C2 Hydrocarbon and Oxygenated Fuels
Intl. J. Chemical Kinetics 45 (2013) 638-675. Release date: August 26th 2013. 
http://c3.nuigalway.ie/Mechanism_release/frontmatter.html
""",
)

