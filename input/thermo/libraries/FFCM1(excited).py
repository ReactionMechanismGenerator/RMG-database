#!/usr/bin/env python
# encoding: utf-8

name = "FFCM1(-)"
shortDesc = u""
longDesc = u"""
Foundational Fuel Chemistry Model Version 1.0 (excited species removed)
http://web.stanford.edu/group/haiwanglab/FFCM1/pages/FFCM1.html

FFCM-1
H2/CO/C1 reaction model - Chemkin form - version v1.0c 
Release date: 05/31/2016.

G. P. Smith, Y. Tao, and H. Wang, Foundational Fuel Chemistry Model Version 1.0 (FFCM-1),
http://nanoenergy.stanford.edu/ffcm1, 2016.

This library contains only excited species from FFCM-1 (CH*, OH*)
"""

entry(
    index = 1,
    label = "OH*",
    molecule = 
"""
multiplicity 2
MolecularTermSymbol A^2S+
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.46084,0.000501872,-2.00254e-06,3.18902e-09,-1.35452e-12,50734.9,1.73976], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.75583,0.00139849,-4.19428e-07,6.33453e-11,-3.56042e-15,50975.2,5.62581], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
OH A 2Sigma+ (excited)
CAS: 3352-57-6 (?)
Uncertainty unknown => -1.0
""",
)

entry(
    index = 1,
    label = "CH*",
    molecule = 
"""
multiplicity 2
MolecularTermSymbol A^2D
1 C u1 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4725,0.000426444,-1.95182e-06,3.51755e-09,-1.60436e-12,104335,1.448], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.78221,0.00147247,-4.63436e-07,7.32736e-11,-4.19705e-15,104547,5.17421], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Goos-Burcat-Ruscic-thermodatabase; Y. Tao 25.05.2012
CH A2Delta (excited)
CAS: 3315-37-5
Uncertainty unknown => -1.0
""",
)

