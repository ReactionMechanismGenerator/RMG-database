#!/usr/bin/env python
# encoding: utf-8

name = "SulfurGlarborgMarshall"
shortDesc = u""
longDesc = u"""
OCS chemistry

Taken from:
Oxidation of Reduced Sulfur Species: Carbonyl Sulfide
Peter Glarborg, Paul Marshall
International Journal of Chemical Kinetics, 45(7) (2013) 429-439
DOI: 10.1002/kin.20778
"""

entry(
    index = 1,
    label = "Ar",
    molecule = 
"""
1 Ar u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.37967], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.37967], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
BUR0302 L 6/88
""",
)

entry(
    index = 2,
    label = "H",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,25473.7,-0.446683], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,25473.7,-0.446683], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
BUR0302 L 6/94
""",
)

entry(
    index = 3,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29812,0.000824944,-8.14302e-07,-9.47543e-11,4.13487e-13,-1012.52,-3.29409], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.99142,0.000700064,-5.63383e-08,-9.23158e-12,1.58275e-15,-835.034,-1.35511], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
121286
LI/DRY04 (v6.1)
""",
)

entry(
    index = 4,
    label = "O",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.94643,-0.00163817,2.42103e-06,-1.60284e-09,3.8907e-13,29147.6,2.96399], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.54206,-2.75506e-05,-3.1028e-09,4.55107e-12,-4.36805e-16,29230.8,4.92031], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
120186
LI/DRY04 (v6.1)
""",
)

entry(
    index = 5,
    label = "O2",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78246,-0.00299673,9.8473e-06,-9.6813e-09,3.24373e-12,-1063.94,3.65768], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.66096,0.000656366,-1.41149e-07,2.05798e-11,-1.29913e-15,-1215.98,3.41536], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
BUR0302 RUS 89
""",
)

entry(
    index = 7,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12531,-0.00322545,6.52765e-06,-5.79854e-09,2.06237e-12,3346.31,-0.690433], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.86473,0.0010565,-2.59083e-07,3.05219e-11,-1.33196e-15,3683.63,5.70164], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
S 9/01
LI/DRY04 (v6.1)
""",
)

entry(
    index = 8,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38684,0.00347498,-6.3547e-06,6.96858e-09,-2.50659e-12,-30208.1,2.59023], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.67215,0.00305629,-8.73026e-07,1.201e-10,-6.39162e-15,-29899.2,6.86282], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
20387
LI/DRY04 (v6.1)
""",
)

entry(
    index = 9,
    label = "HO2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.3018,-0.00474912,2.11583e-05,-2.42764e-08,9.29225e-12,294.808,3.71666], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.01721,0.00223982,-6.33658e-07,1.14246e-10,-1.07909e-14,111.857,3.7851], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
L 5/89
LI/DRY04 (v6.1)
""",
)

entry(
    index = 10,
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
            NASAPolynomial(coeffs=[3.38875,0.00656923,-1.48501e-07,-4.62581e-09,2.47151e-12,-17663.1,6.78536], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.57317,0.00433614,-1.47469e-06,2.3489e-10,-1.43165e-14,-18007,0.501137], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
120186
LI/DRY04 (v6.1)
""",
)

entry(
    index = 11,
    label = "CO",
    molecule = 
"""
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57953,-0.000610354,1.01681e-06,9.07006e-10,-9.04424e-13,-14344.1,3.50841], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.04849,0.00135173,-4.85794e-07,7.88536e-11,-4.69807e-15,-14266.1,6.0171], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
BUR0302 RUS 79
""",
)

entry(
    index = 12,
    label = "CO2",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.35681,0.00898413,-7.12206e-06,2.4573e-09,-1.42885e-13,-48372,9.9009], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.63651,0.00274146,-9.95898e-07,1.60387e-10,-9.16199e-15,-49024.9,-1.9349], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
BUR0302 L 7/88
""",
)

entry(
    index = 13,
    label = "HOCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 C u1 p0 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.35681,0.00898413,-7.12206e-06,2.4573e-09,-1.42885e-13,-23787.2,14.3851], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.63651,0.00274146,-9.95898e-07,1.60387e-10,-9.16199e-15,-24440.1,2.54925], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Hydroxyoxomethyl radical""",
    longDesc = 
u"""
CLR est L 7/88
CLR est based on CO2 data and SANDIA
H298=-45.19 kcal/mol
S298= 60.00 cal/mol/K
""",
)

entry(
    index = 14,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53101,-0.000123661,-5.02999e-07,2.43531e-09,-1.40881e-12,-1046.98,2.96747], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.95258,0.0013969,-4.92632e-07,7.8601e-11,-4.60755e-15,-923.949,5.87189], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
BUR0302 G 8/02
""",
)

entry(
    index = 15,
    label = "S",
    molecule = 
"""
multiplicity 3
1 S u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.31726,0.00478018,-1.42083e-05,1.5657e-08,-5.96588e-12,32506.9,6.06242], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.87936,-0.00051105,2.53807e-07,-4.45455e-11,2.66717e-15,32501.4,3.98141], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
BUR0302     J 9/82
""",
)

entry(
    index = 16,
    label = "S2",
    molecule = 
"""
1 S u0 p2 c0 {2,D}
2 S u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.85858,0.00517584,-6.54934e-06,3.39986e-09,-4.01568e-13,14412.4,9.89128], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.98861,0.000557751,-5.01893e-08,-1.54703e-11,2.66618e-15,14198,4.49119], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Sulfur dimer (S=S)""",
    longDesc = 
u"""
BUR0302     J 9/77
""",
)

entry(
    index = 17,
    label = "SH",
    molecule = 
"""
multiplicity 2
1 S u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68468,0.00324598,-1.28632e-05,1.6951e-08,-7.07587e-12,16040.6,2.01782], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.03153,0.00125805,-4.05526e-07,6.19651e-11,-3.50864e-15,16342.9,6.15027], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Mercapto radical (H-S*)""",
    longDesc = 
u"""
BUR0302     s06/01
""",
)

entry(
    index = 18,
    label = "H2S",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.11941,-0.00187716,8.2066e-06,-7.05942e-09,2.14058e-12,-3681.93,1.53458], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.97708,0.00360053,-1.23285e-06,1.96927e-10,-1.16773e-14,-3515.6,6.78683], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""Hydrogen sulfide (H-S-H)""",
    longDesc = 
u"""
BUR0302     RUS 89
""",
)

entry(
    index = 19,
    label = "HS2",
    molecule = 
"""
multiplicity 2
1 S u1 p1 c0 {2,D} {3,S}
2 S u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.96047,0.00858228,-1.0127e-05,6.35903e-09,-1.57679e-12,11393.9,11.436], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.79737,0.00203257,-7.46965e-07,1.22379e-10,-7.39991e-15,10950.5,2.29333], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""H-S=S""",
    longDesc = 
u"""
ALZ/GLA01   burc01
""",
)

entry(
    index = 20,
    label = "H2S2",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {3,S}
2 S u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.09117,0.019422,-2.89395e-05,2.30251e-08,-7.20185e-12,639.069,13.5884], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.69403,0.00390495,-1.41886e-06,2.30688e-10,-1.38746e-14,-117.795,-3.7414], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
BUR0302    S 1/01
""",
)

entry(
    index = 21,
    label = "SO",
    molecule = 
"""
multiplicity 3
1 S u2 p1 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14902,0.00118393,2.57407e-06,-4.44434e-09,1.87352e-12,-404.076,8.31988], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.01429,0.000270228,8.28967e-08,-3.43237e-11,3.11214e-15,-710.52,3.49974], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Sulfur monoxide (triplet) (S=O) ground state""",
    longDesc = 
u"""
BUR0302     J 6/77
""",
)

entry(
    index = 22,
    label = "SO(S)",
    molecule = 
"""
1 S u0 p2 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14902,0.00118393,2.57407e-06,-4.44434e-09,1.87352e-12,11020.2,7.23785], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.01429,0.000270228,8.28967e-08,-3.43237e-11,3.11214e-15,10713.7,2.4177], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Sulfur monoxide (singlet) (S=O) excited state""",
    longDesc = 
u"""
SO+deltaH
S298 = 50.89 cal/mol/K
""",
)

entry(
    index = 23,
    label = "SO2",
    molecule = 
"""
1 S u0 p1 c0 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.26653,0.00532379,6.84376e-07,-5.281e-09,2.55905e-12,-36908.1,9.66465], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.24514,0.00197042,-8.03758e-07,1.515e-10,-1.0558e-14,-37558.2,-1.07405], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Sulfur dioxide (O=S=O)""",
    longDesc = 
u"""
BUR0302     J 6/61
""",
)

entry(
    index = 24,
    label = "SO3",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 S u0 p0 c0 {1,D} {3,D} {4,D}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.57804,0.0145563,-9.17642e-06,-7.9203e-10,1.97095e-12,-48931.8,12.2651], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.07574,0.00317634,-1.35358e-06,2.56309e-10,-1.7936e-14,-50211.4,-11.1875], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""Sulfur trioxide (O=S(=O)=O)""",
    longDesc = 
u"""
BUR0302     J 9/65
""",
)

entry(
    index = 25,
    label = "HSO",
    molecule = 
"""
multiplicity 2
1 S u1 p1 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41309,0.00321051,3.89607e-06,-8.19581e-09,3.77898e-12,-1755.5,8.65228], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.5416,0.00226485,-8.31521e-07,1.36148e-10,-8.2291e-15,-2160.86,2.33576], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""H-S*=O""",
    longDesc = 
u"""
BUR0302     T 4/93
BURCAT
""",
)

entry(
    index = 26,
    label = "HOS",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 S u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69224,0.000445457,1.07859e-05,-1.59755e-08,6.88588e-12,-3700.68,7.3217], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.35443,0.00205499,-6.70839e-07,1.01192e-10,-5.76724e-15,-3989.56,3.23031], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""HO-S*""",
    longDesc = 
u"""
BUR0302     T 4/93
""",
)

entry(
    index = 27,
    label = "HSOH",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.56764,0.0113805,-5.86673e-06,-5.947e-10,8.74383e-13,-15571.3,11.7664], Tmin=(298,'K'), Tmax=(1500,'K')),
            NASAPolynomial(coeffs=[2.56764,0.0113805,-5.86673e-06,-5.947e-10,8.74383e-13,-15571.3,11.7664], Tmin=(1500,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""HS-OH""",
    longDesc = 
u"""
ALZ/GLA01   BOZ/R
""",
)

entry(
    index = 28,
    label = "HOSO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 S u1 p1 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.61847,0.0211641,-2.66905e-05,1.62722e-08,-3.7779e-12,-30255.6,19.4773], Tmin=(298,'K'), Tmax=(1500,'K')),
            NASAPolynomial(coeffs=[1.61847,0.0211641,-2.66905e-05,1.62722e-08,-3.7779e-12,-30255.6,19.4773], Tmin=(1500,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""HO-S*=O""",
    longDesc = 
u"""
DAG/GLA03 GOU/MAR99
""",
)

entry(
    index = 29,
    label = "HSO2",
    molecule = 
"""
multiplicity 2
1 S u1 p0 c0 {2,S} {3,D} {4,D}
2 H u0 p0 c0 {1,S}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.56274,0.0206914,-2.31121e-05,1.26702e-08,-2.72742e-12,-18214.8,17.5568], Tmin=(298,'K'), Tmax=(1500,'K')),
            NASAPolynomial(coeffs=[1.56274,0.0206914,-2.31121e-05,1.26702e-08,-2.72742e-12,-18214.8,17.5568], Tmin=(1500,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""H-S*(=O)=O""",
    longDesc = 
u"""
ALZ/GLA01 GOU/MAR99
""",
)

entry(
    index = 30,
    label = "H2SO",
    molecule = 
"""
1 S u0 p1 c0 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.95805,0.00972652,6.84132e-07,-6.23437e-09,2.41666e-12,-6677.09,14.7835], Tmin=(298,'K'), Tmax=(1500,'K')),
            NASAPolynomial(coeffs=[1.95805,0.00972652,6.84132e-07,-6.23437e-09,2.41666e-12,-6677.09,14.7835], Tmin=(1500,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""H2S=O""",
    longDesc = 
u"""
ALZ/GLA01   BOZ/R
""",
)

entry(
    index = 31,
    label = "HOSOH",
    molecule = 
"""
1 S u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {1,S} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.92,15.88,17.33,18.40,19.85,20.85,22.57],'cal/(mol*K)'),
        H298 = (-75.31,'kcal/mol'),
        S298 = (64.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""HO-S-OH""",
    longDesc = 
u"""
ALZ/GLA01  BOZ/R
""",
)

entry(
    index = 32,
    label = "HOSHO",
    molecule = 
"""
1 S u0 p1 c0 {2,S} {3,D} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.19038,0.0256447,-2.66228e-05,1.34797e-08,-2.64746e-12,-33744.9,19.0955], Tmin=(298,'K'), Tmax=(1500,'K')),
            NASAPolynomial(coeffs=[1.19038,0.0256447,-2.66228e-05,1.34797e-08,-2.64746e-12,-33744.9,19.0955], Tmin=(1500,'K'), Tmax=(1500,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (1500,'K'),
    ),
    shortDesc = u"""HO-SH=O""",
    longDesc = 
u"""
ALZ/GLA01   BOZ/R
""",
)

entry(
    index = 33,
    label = "HOSO2",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 S u1 p0 c0 {1,S} {3,D} {5,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.62277,-0.00419909,3.52055e-05,-4.12715e-08,1.40007e-11,-46947.8,-7.80788], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.62277,-0.00419909,3.52055e-05,-4.12715e-08,1.40007e-11,-46947.8,-7.80788], Tmin=(1000,'K'), Tmax=(2000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (2000,'K'),
    ),
    shortDesc = u"""HO-S*(=O)=O""",
    longDesc = 
u"""
leeds
""",
)

entry(
    index = 34,
    label = "CS2",
    molecule = 
"""
1 S u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 S u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.17231,0.0181263,-3.0808e-05,2.65151e-08,-8.92802e-12,12806.4,11.9827], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.94905,0.00169288,-6.74334e-07,1.16461e-10,-6.37364e-15,12017.1,-6.17037], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
g 6/95
Burcat 2006
""",
)

entry(
    index = 35,
    label = "CS",
    molecule = 
"""
1 S u0 p1 c+1 {2,T}
2 C u0 p1 c-1 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73125,-0.00309804,1.24828e-05,-1.41633e-08,5.33371e-12,32442.1,4.54855], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.7696,0.000730981,-2.42921e-07,2.88071e-11,-5.21956e-17,32249.9,3.42023], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
g11/01
Burcat 2006
""",
)

entry(
    index = 36,
    label = "OCS",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 S u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.77199,0.0171487,-2.73082e-05,2.25553e-08,-7.34373e-12,-18132.9,13.681], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.37456,0.00210411,-7.76418e-07,1.29745e-10,-7.92408e-15,-18917.8,-3.78474], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
g 5/01
Burcat 2006
""",
)

entry(
    index = 37,
    label = "OCS2",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 S u0 p1 c0 {2,D} {4,D}
4 S u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.82159,0.0213606,-2.95791e-05,1.99102e-08,-5.20419e-12,1538.63,12.3498], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.471,0.005314,-3.33568e-06,9.65541e-10,-1.05777e-13,881.198,-4.89421], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298.15,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
1210
MC Lin, pw
""",
)

entry(
    index = 38,
    label = "S2O",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 S u0 p1 c0 {1,D} {3,D}
3 S u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.89888,0.0115444,-1.46502e-05,9.19412e-09,-2.31495e-12,-8193.13,12.6536], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.69256,0.00142824,-3.95224e-07,-9.64671e-11,4.47355e-14,-8829.71,-1.14896], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
haynes
""",
)

