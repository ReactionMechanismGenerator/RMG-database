#!/usr/bin/env python
# encoding: utf-8

name = "Narayanaswamy"
shortDesc = u"Aromatic reactions only from 2010 Narayanaswamy et al. Combustion and Flame mechanism"
longDesc = u"""
Includes thermo for species from the mechanism in:
K. Narayanaswamy et al.,
A Consistent Chemical Mechanism for Oxidation of Substituted Aromatic Species
Combustion and Flame 157 (2010) 1879-1898
"""
entry(
    index = 0,
    label = "CH4(1)",
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
            NASAPolynomial(coeffs=[4.20542,-0.00535566,2.51126e-05,-2.13766e-08,5.97538e-12,-10161.9,-0.921305], Tmin=(100,'K'), Tmax=(1084.11,'K')),
            NASAPolynomial(coeffs=[0.908224,0.0114542,-4.57178e-06,8.29201e-10,-5.66322e-14,-9719.96,13.9933], Tmin=(1084.11,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "H(2)",
    molecule = 
"""
multiplicity 2
1 H u1 p0 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,-1.91243e-12,2.45329e-15,-1.02377e-18,1.31369e-22,25474.2,-0.444973], Tmin=(100,'K'), Tmax=(4563.27,'K')),
            NASAPolynomial(coeffs=[2.50167,-1.43051e-06,4.6025e-10,-6.57826e-14,3.52412e-18,25472.7,-0.455578], Tmin=(4563.27,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "O2(3)",
    molecule = 
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53732,-0.00121571,5.31618e-06,-4.89443e-09,1.45845e-12,-1038.59,4.68368], Tmin=(100,'K'), Tmax=(1074.56,'K')),
            NASAPolynomial(coeffs=[3.15382,0.00167804,-7.69971e-07,1.51275e-10,-1.08782e-14,-1040.82,6.16754], Tmin=(1074.56,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "O(4)",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,-1.91243e-12,2.45329e-15,-1.02377e-18,1.31369e-22,29230.2,4.09104], Tmin=(100,'K'), Tmax=(4563.27,'K')),
            NASAPolynomial(coeffs=[2.50167,-1.43051e-06,4.6025e-10,-6.57826e-14,3.52412e-18,29228.7,4.08044], Tmin=(4563.27,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "OH(5)",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51457,2.92796e-05,-5.32171e-07,1.0195e-09,-3.85948e-13,3414.25,2.10435], Tmin=(100,'K'), Tmax=(1145.75,'K')),
            NASAPolynomial(coeffs=[3.07194,0.000604013,-1.3977e-08,-2.13449e-11,2.48068e-15,3579.39,4.57799], Tmin=(1145.75,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "H2(6)",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43536,0.000212707,-2.78618e-07,3.40262e-10,-7.76019e-14,-1031.36,-3.90842], Tmin=(100,'K'), Tmax=(1959.09,'K')),
            NASAPolynomial(coeffs=[2.78813,0.000587687,1.58989e-07,-5.52696e-11,4.34279e-15,-596.123,0.112943], Tmin=(1959.09,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "H2O(7)",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05764,-0.000787936,2.90878e-06,-1.47519e-09,2.12843e-13,-30281.6,-0.311364], Tmin=(100,'K'), Tmax=(1130.24,'K')),
            NASAPolynomial(coeffs=[2.84325,0.00275109,-7.81032e-07,1.07244e-10,-5.79392e-15,-29958.6,5.91042], Tmin=(1130.24,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "CO2(8)",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.35677,0.0089846,-7.12356e-06,2.45919e-09,-1.437e-13,-48372,9.90105], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.85746,0.00441437,-2.21481e-06,5.2349e-10,-4.72084e-14,-48759.2,2.27164], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "HO2(9)",
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

""",
)

entry(
    index = 9,
    label = "H2O2(10)",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.27611,-0.000542822,1.67336e-05,-2.15771e-08,8.62454e-12,-17702.6,3.43505], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.165,0.00490832,-1.90139e-06,3.71186e-10,-2.87908e-14,-17861.8,2.91616], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "CO(11)",
    molecule = 
"""
1 C u0 p1 c-1 {2,T}
2 O u0 p1 c+1 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57953,-0.000610354,1.01681e-06,9.07006e-10,-9.04424e-13,-14344.1,3.50841], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.71519,0.00206253,-9.98826e-07,2.30053e-10,-2.03648e-14,-14151.9,7.81869], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "HCO(12)",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.22119,-0.00324393,1.37799e-05,-1.33144e-08,4.33769e-12,3839.56,3.39437], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.77217,0.00495696,-2.48446e-06,5.89162e-10,-5.33509e-14,4011.92,9.79834], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "C(13)",
    molecule = 
"""
1 C u0 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,-1.91243e-12,2.45329e-15,-1.02377e-18,1.31369e-22,100099,2.56126], Tmin=(100,'K'), Tmax=(4563.27,'K')),
            NASAPolynomial(coeffs=[2.50167,-1.43051e-06,4.6025e-10,-6.57826e-14,3.52412e-18,100097,2.55065], Tmin=(4563.27,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "CH(14)",
    molecule = 
"""
multiplicity 4
1 C u3 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48982,0.000323836,-1.68899e-06,3.16217e-09,-1.40609e-12,70797.3,2.08401], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.87846,0.000970914,1.44446e-07,-1.30688e-10,1.76079e-14,71012.4,5.48498], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "T-CH2(15)",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01192,-0.000154979,3.26298e-06,-2.40422e-09,5.69497e-13,45867.7,0.5332], Tmin=(100,'K'), Tmax=(1104.58,'K')),
            NASAPolynomial(coeffs=[3.14983,0.00296674,-9.76055e-07,1.54115e-10,-9.50337e-15,46058.1,4.77807], Tmin=(1104.58,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "CH3(16)",
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
            NASAPolynomial(coeffs=[3.65718,0.0021266,5.45839e-06,-6.6181e-09,2.46571e-12,16422.7,1.67354], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.97812,0.00579785,-1.97558e-06,3.07298e-10,-1.79174e-14,16509.5,4.72248], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "CH2O(17)",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.79372,-0.00990833,3.7322e-05,-3.79285e-08,1.31773e-11,-14309,0.602813], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.76069,0.0092,-4.42259e-06,1.00641e-09,-8.83856e-14,-13995.8,13.6563], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "HCCO(18)",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {4,S}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.25172,0.017655,-2.37291e-05,1.72758e-08,-5.06648e-12,20059.4,12.4904], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.62821,0.00408534,-1.59345e-06,2.86261e-10,-1.94078e-14,19327.2,-3.93026], Tmin=(1000,'K'), Tmax=(4000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (4000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "C2H(19)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,T} {3,S}
2 C u1 p0 c0 {1,T}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.88966,0.01341,-2.8477e-05,2.94791e-08,-1.09332e-11,66839.4,6.22296], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.16781,0.00475222,-1.83787e-06,3.0419e-10,-1.77233e-14,67121.1,6.63589], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "CH2CO(20)",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {5,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.13584,0.0181189,-1.73947e-05,9.34398e-09,-2.01458e-12,-7042.92,12.2156], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.5113,0.0090036,-4.1694e-06,9.23346e-10,-7.94838e-14,-7551.05,0.632247], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "C2H2(21)",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.808681,0.0233616,-3.55172e-05,2.80152e-08,-8.50073e-12,26429,13.9397], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.14757,0.00596167,-2.37295e-06,4.67412e-10,-3.61235e-14,25936,-1.23028], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "S-CH2(22)",
    molecule = 
"""
1 C u0 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.10264,-0.00144068,5.45067e-06,-3.58e-09,7.56187e-13,50400.6,-0.411763], Tmin=(100,'K'), Tmax=(1442.37,'K')),
            NASAPolynomial(coeffs=[2.62649,0.00394761,-1.49923e-06,2.54537e-10,-1.62954e-14,50691.7,6.78371], Tmin=(1442.37,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
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

""",
)

entry(
    index = 23,
    label = "AR",
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

""",
)

entry(
    index = 24,
    label = "CH3OH(25)",
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
            NASAPolynomial(coeffs=[5.7154,-0.0152309,6.52441e-05,-7.10807e-08,2.61353e-11,-25642.8,-1.5041], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.78971,0.0140938,-6.36501e-06,1.38171e-09,-1.1706e-13,-25374.9,14.5024], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "CH2OH(26)",
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
            NASAPolynomial(coeffs=[3.86389,0.00559672,5.93272e-06,-1.04532e-08,4.36967e-12,-3193.91,5.47302], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.69267,0.00864577,-3.75101e-06,7.87235e-10,-6.48554e-14,-3242.51,5.81043], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "CH3O(27)",
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
            NASAPolynomial(coeffs=[2.1062,0.0072166,5.33847e-06,-7.37764e-09,2.07561e-12,978.601,13.1522], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.7708,0.0078715,-2.65638e-06,3.94443e-10,-2.11262e-14,127.833,2.92957], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "CH3O2(28)",
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
            NASAPolynomial(coeffs=[4.76598,-0.00351077,4.54394e-05,-5.66764e-08,2.21591e-11,-482.401,4.76095], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.92506,0.00900195,-3.24254e-06,5.24363e-10,-3.14263e-14,-1532.59,-4.9367], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "C2H3(29)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u1 p0 c0 {1,D} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.21247,0.00151479,2.59209e-05,-3.57658e-08,1.47151e-11,34859.8,8.51054], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.01672,0.0103302,-4.68082e-06,1.01763e-09,-8.62607e-14,34612.9,7.78732], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "C2H4(30)",
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
            NASAPolynomial(coeffs=[3.9592,-0.00757052,5.7099e-05,-6.91589e-08,2.69884e-11,5089.78,4.09733], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.03611,0.0146454,-6.71078e-06,1.47223e-09,-1.25706e-13,4939.89,10.3054], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "C2H5(31)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.30647,-0.00418659,4.97143e-05,-5.99127e-08,2.30509e-11,12841.6,4.70721], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.95466,0.0173973,-7.98207e-06,1.75218e-09,-1.49642e-13,12857.5,13.4624], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "HCCOH(32)",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,T}
2 O u0 p2 c0 {1,S} {4,S}
3 C u0 p0 c0 {1,T} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.24237,0.0310722,-5.08669e-05,4.31371e-08,-1.40146e-11,8031.61,13.8743], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.92383,0.00679236,-2.56586e-06,4.49878e-10,-2.99401e-14,7264.63,-7.60177], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "CH2CHO(33)",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.09686,0.0220229,-1.44583e-05,3.0078e-09,6.08993e-13,1069.43,19.0095], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.42606,0.01724,-9.77132e-06,2.66556e-09,-2.8212e-13,833.107,12.6039], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "CH3CHO(34)",
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
            NASAPolynomial(coeffs=[1.40654,0.0216984,-1.47573e-05,7.30435e-09,-2.09119e-12,-21797.3,17.7513], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.68543,0.0176802,-8.65403e-06,2.03681e-09,-1.87631e-13,-22165.4,11.1636], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "H2C2(35)",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u2 p0 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28155,0.00697648,-2.38552e-06,-1.21044e-09,9.81895e-13,48621.8,5.92039], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.27803,0.00475628,-1.6301e-06,2.54628e-10,-1.48864e-14,48316.7,0.640237], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "C2H5O(36)",
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
            NASAPolynomial(coeffs=[0.494421,0.0271774,-1.65909e-05,5.15204e-09,-6.48497e-13,-3352.53,22.8079], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.46262,0.0209504,-9.39292e-06,1.56441e-09,0,-3839.33,12.8739], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "N-C3H7(37)",
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
            NASAPolynomial(coeffs=[1.04755,0.0260078,2.35623e-06,-1.95923e-08,9.36801e-12,10632.6,21.1419], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.70404,0.0160415,-5.2816e-06,7.62544e-10,-3.93535e-14,8297.95,-15.4875], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "C2H6(38)",
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
            NASAPolynomial(coeffs=[4.29142,-0.00550154,5.99438e-05,-7.08466e-08,2.68686e-11,-11522.2,2.66682], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.07188,0.0216853,-1.00256e-05,2.21412e-09,-1.90003e-13,-11426.4,15.1156], Tmin=(1000,'K'), Tmax=(3500,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3500,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "C3H8(39)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  H u0 p0 c0 {1,S}
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
            NASAPolynomial(coeffs=[0.933554,0.0264246,6.10597e-06,-2.19775e-08,9.51493e-12,-13958.5,19.2017], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.53414,0.0188722,-6.27185e-06,9.14756e-10,-4.78381e-14,-16467.5,-17.8923], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "C3H6(40)",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.00229262,0.0310261,-1.67152e-05,1.89594e-09,1.24958e-12,1134.37,23.572], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.471698,0.0289513,-1.56602e-05,4.11443e-09,-4.23075e-13,1126.03,21.5237], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "C3H3(41)",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {6,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.40299,0.0301773,-3.98449e-05,2.93535e-08,-8.70555e-12,39310.8,15.1528], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.14915,0.00934063,-3.75055e-06,6.90156e-10,-4.60825e-14,38385.5,-7.45345], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "P-C3H4(42)",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.46175,0.0246027,-1.90219e-05,8.60363e-09,-1.66729e-12,20921,14.9263], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.81461,0.0185524,-9.55027e-06,2.39951e-09,-2.37485e-13,20701.1,8.60605], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "A-C3H4(43)",
    molecule = 
"""
1 C u0 p0 c0 {3,D} {4,S} {5,S}
2 C u0 p0 c0 {3,D} {6,S} {7,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.368928,0.0289351,-2.44386e-05,1.12547e-08,-2.0304e-12,21758.5,19.5267], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.56129,0.019508,-1.04061e-05,2.70165e-09,-2.75074e-13,21389.4,9.2055], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "S-C3H5(44)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u1 p0 c0 {2,D} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.313107,0.031877,-2.5342e-05,1.02999e-08,-1.35302e-12,31376.8,22.3729], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.02509,0.0235513,-1.28255e-05,3.39579e-09,-3.51795e-13,31181.2,14.6653], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "N-C4H3(45)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,T}
3 C u1 p0 c0 {1,D} {6,S}
4 C u0 p0 c0 {2,T} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.0355175,0.0430509,-5.75729e-05,4.15883e-08,-1.20751e-11,64350.7,24.3817], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.2533,0.0119581,-5.26716e-06,1.09982e-09,-8.84017e-14,62897.8,-10.5283], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "C3H4O(46)",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {5,D} {8,S}
4 H u0 p0 c0 {1,S}
5 O u0 p2 c0 {3,D}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.292355,0.0354321,-2.94936e-05,1.281e-08,-2.26144e-12,-11652.2,22.8878], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.56155,0.0179296,-8.03465e-06,1.32295e-09,0,-12903.6,-3.47373], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "A-C3H5(47)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 C u1 p0 c0 {1,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.03516,0.0375043,-3.26381e-05,1.47663e-08,-2.43741e-12,18879.2,27.1451], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.28795,0.0236402,-1.27891e-05,3.36839e-09,-3.47449e-13,18303.4,11.4063], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "C2O(48)",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {3,T}
2 O u1 p2 c0 {1,S}
3 C u1 p0 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.86278,0.0119701,-1.80851e-05,1.52778e-08,-5.20063e-12,33750.2,8.89759], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.42468,0.00185394,-5.17933e-07,6.77646e-11,-3.53315e-15,33153.7,-3.69608], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "C4H4(49)",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {4,T}
4 C u0 p0 c0 {3,T} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.231343,0.0411814,-4.47624e-05,2.75434e-08,-7.06377e-12,34063.3,24.2662], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.97237,0.019314,-9.81197e-06,2.43005e-09,-2.371e-13,33056.1,-0.623055], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "C3H2(50)",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,D} {3,D}
2 C u1 p0 c0 {1,D} {4,S}
3 C u1 p0 c0 {1,D} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.52861,0.0177566,-2.54883e-05,2.01675e-08,-6.28545e-12,63541,0.809424], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.67921,0.00385561,-8.2343e-07,-6.18109e-11,2.93114e-14,62913.6,-14.2212], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "C3H2O(51)",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,D} {5,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {6,S}
4 O u0 p2 c0 {1,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.89402,0.0266301,-2.97185e-05,1.9429e-08,-5.43403e-12,13727.2,15.5182], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.51552,0.0120297,-6.09059e-06,1.48866e-09,-1.42588e-13,12956.8,-2.05439], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "C4H2(52)",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,T}
2 C u0 p0 c0 {1,S} {4,T}
3 C u0 p0 c0 {1,T} {5,S}
4 C u0 p0 c0 {2,T} {6,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.173325,0.0453949,-7.30124e-05,5.95252e-08,-1.87485e-11,54223.9,18.0184], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.7584,0.00378873,3.06142e-07,-6.33655e-10,1.1293e-13,52269.9,-27.9084], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "I-C4H3(53)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 C u0 p0 c0 {3,T} {7,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.02566,0.0304694,-3.68345e-05,2.60035e-08,-7.62154e-12,58055.2,9.87268], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.29284,0.0121665,-5.50925e-06,1.19291e-09,-1.00493e-13,57196.1,-10.5737], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "T-C3H5(54)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {3,D} {7,S} {8,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.880981,0.0296362,-2.52726e-05,1.43652e-08,-3.89567e-12,29232.1,20.0164], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.15894,0.0204649,-1.00948e-05,2.41157e-09,-2.26535e-13,28735.1,8.93042], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "C3H5O(55)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u0 p0 c0 {2,D} {8,S} {9,S}
4 O u1 p2 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.19823,0.030558,-1.8063e-05,4.8615e-09,-4.19855e-13,9582.18,21.5566], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.39075,0.0241302,-1.13651e-05,1.97901e-09,0,9007.57,10.346], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "C4H(56)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,T}
2 C u0 p0 c0 {1,S} {4,T}
3 C u0 p0 c0 {1,T} {5,S}
4 C u1 p0 c0 {2,T}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.23559,0.0227092,-3.18443e-05,2.44865e-08,-7.57986e-12,93908.1,7.90671], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.44965,0.00523173,-1.9634e-06,3.00668e-10,-1.16122e-14,93005.2,-12.4961], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "C8H2(57)",
    molecule = 
"""
1  C u0 p0 c0 {3,T} {5,S}
2  C u0 p0 c0 {4,T} {6,S}
3  C u0 p0 c0 {1,T} {4,S}
4  C u0 p0 c0 {2,T} {3,S}
5  C u0 p0 c0 {1,S} {7,T}
6  C u0 p0 c0 {2,S} {8,T}
7  C u0 p0 c0 {5,T} {9,S}
8  C u0 p0 c0 {6,T} {10,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.326702,0.0943329,-0.000172876,1.56817e-07,-5.40488e-11,105392,22.0322], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.3587,0.0108593,-3.91655e-06,6.34107e-10,-3.80413e-14,102367,-55.6747], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "C6H2(58)",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 C u0 p0 c0 {1,S} {5,T}
4 C u0 p0 c0 {2,S} {6,T}
5 C u0 p0 c0 {3,T} {7,S}
6 C u0 p0 c0 {4,T} {8,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.541092,0.0745326,-0.000135783,1.22266e-07,-4.18252e-11,82115.1,21.8827], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.5328,0.00877663,-3.13296e-06,5.03718e-10,-3.00719e-14,79784.3,-38.8586], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "C4H6(59)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {5,S}
2  C u0 p0 c0 {1,S} {4,D} {6,S}
3  C u0 p0 c0 {1,D} {7,S} {8,S}
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
            NASAPolynomial(coeffs=[4.01336,0.00444627,7.80683e-05,-1.11674e-07,4.60754e-11,11480.7,6.7708], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[-8.99531,0.0601715,-4.20058e-05,1.3333e-08,-1.57424e-12,14929.6,71.1867], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "N-C4H5(60)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,D} {6,S}
3 C u0 p0 c0 {1,D} {7,S} {8,S}
4 C u1 p0 c0 {2,D} {9,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.1685,0.0479006,-5.12377e-05,3.06244e-08,-7.59907e-12,42278.7,31.163], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.87675,0.0227534,-1.17715e-05,2.95251e-09,-2.91457e-13,41108.1,2.21508], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "I-C4H5(61)",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {6,S} {7,S}
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
            NASAPolynomial(coeffs=[-0.331905,0.0440164,-4.2769e-05,2.31284e-08,-5.17172e-12,36751.1,25.6363], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.34644,0.0245761,-1.30954e-05,3.38848e-09,-3.4352e-13,35871,3.29579], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "A1(62)",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {6,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {8,S}
3  C u0 p0 c0 {2,B} {4,B} {9,S}
4  C u0 p0 c0 {3,B} {5,B} {10,S}
5  C u0 p0 c0 {4,B} {6,B} {11,S}
6  C u0 p0 c0 {1,B} {5,B} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.51558,0.0645453,-4.41403e-05,7.47712e-09,3.10282e-12,9110.31,46.5332], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[-0.206241,0.0464122,-2.77654e-05,7.88911e-09,-8.60365e-13,8098.84,20.6567], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "C7H16(63)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {5,S} {16,S} {17,S}
4  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {7,S} {10,S} {11,S}
6  C u0 p0 c0 {4,S} {18,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {21,S} {22,S} {23,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.26836,0.0854356,-5.25347e-05,1.62946e-08,-2.02395e-12,-25658.7,35.3733], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.14079,0.0653079,-2.94828e-05,4.93727e-09,0,-27253.4,2.98196], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "C5H11(64)",
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
            NASAPolynomial(coeffs=[-0.905256,0.0610633,-4.09492e-05,1.46093e-08,-2.1886e-12,4839.95,32.5575], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.88921,0.0422835,-1.85843e-05,3.04125e-09,0,3434.75,3.43705], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "P-C4H9(65)",
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
            NASAPolynomial(coeffs=[-0.43778,0.0478972,-3.14023e-05,1.09786e-08,-1.62011e-12,7689.45,28.6853], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.81812,0.034079,-1.49135e-05,2.43205e-09,0,6659.01,7.30418], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "C7H15(66)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
6  C u0 p0 c0 {4,S} {16,S} {17,S} {18,S}
7  C u1 p0 c0 {3,S} {4,S} {22,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
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
            NASAPolynomial(coeffs=[-0.0379156,0.0756727,-4.07474e-05,9.32679e-09,-4.92361e-13,-2356.05,33.7322], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.74721,0.0649345,-3.01341e-05,5.17418e-09,0,-3370.18,14.278], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "P-C4H8(67)",
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
            NASAPolynomial(coeffs=[-0.831372,0.0452581,-2.93659e-05,1.0022e-08,-1.43192e-12,-1578.75,29.5084], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.0447,0.0327452,-1.45363e-05,2.39744e-09,0,-2521.78,10.0152], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "C5H10(68)",
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
            NASAPolynomial(coeffs=[-1.06223,0.0574218,-3.74487e-05,1.27365e-08,-1.7961e-12,-4465.47,32.274], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.98581,0.041243,-1.8439e-05,3.06155e-09,0,-5701.12,6.85332], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "C7H14(69)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {7,D} {21,S}
7  C u0 p0 c0 {5,S} {6,D} {20,S}
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
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.03027,0.0826324,-5.45514e-05,1.87706e-08,-2.67571e-12,-11514.1,40.2316], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.45858,0.0586158,-2.63089e-05,4.38019e-09,0,-13346.3,2.52376], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "C7H15O(70)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {7,S} {20,S} {21,S} {22,S}
7  C u1 p0 c0 {6,S} {8,S} {23,S}
8  O u0 p2 c0 {4,S} {7,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.45919,0.0874465,-5.69015e-05,1.92196e-08,-2.68753e-12,-17823.3,35.6475], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.08995,0.0632469,-2.84622e-05,4.74318e-09,0,-19670.8,-2.36655], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "C4H8O(71)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {12,D} {13,S}
5  H u0 p0 c0 {1,S}
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
            NASAPolynomial(coeffs=[1.87416,0.041924,-2.35149e-05,6.26914e-09,-6.09444e-13,-27103.2,19.1569], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.99144,0.0353603,-1.61297e-05,2.72103e-09,0,-27635.2,8.43277], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "C4H7(72)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u1 p0 c0 {1,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.07355,0.00527619,6.23441e-05,-8.54203e-08,3.4589e-11,22461.5,5.60318], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.49074,0.0191057,-6.74371e-06,1.07343e-09,-6.36252e-14,20465.9,-17.4556], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "C7H13(73)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
4  C u0 p0 c0 {3,S} {14,S} {15,S} {16,S}
5  C u1 p0 c0 {1,S} {3,S} {17,S}
6  C u0 p0 c0 {2,S} {7,D} {18,S}
7  C u0 p0 c0 {6,D} {19,S} {20,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
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
            NASAPolynomial(coeffs=[-2.01708,0.0808916,-5.43384e-05,1.88066e-08,-2.66059e-12,6811.03,38.9797], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.78336,0.0560948,-2.54855e-05,4.28951e-09,0,4888.52,-0.359537], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "C5H9(74)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u1 p0 c0 {2,S} {11,S} {12,S}
5  C u0 p0 c0 {3,D} {13,S} {14,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.38014,0.0557608,-3.70144e-05,1.26884e-08,-1.78539e-12,12559,32.6441], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.78447,0.0393,-1.78011e-05,2.98594e-09,0,11288.9,6.61027], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "C4H7O(75)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u1 p2 c0 {1,S}
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
            NASAPolynomial(coeffs=[-1.60619,0.0558563,-4.35596e-05,1.70589e-08,-2.65635e-12,4850.9,34.7113], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.2192,0.0310373,-1.47415e-05,2.57806e-09,0,2917.91,-4.77188], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "C3H7O(76)",
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
            NASAPolynomial(coeffs=[0.289707,0.0393076,-2.48069e-05,8.07084e-09,-1.07998e-12,-6244.74,25.4388], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.42509,0.0293139,-1.31458e-05,2.188e-09,0,-7015.63,9.63435], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "C8H18(77)",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {21,S} {22,S} {23,S}
6  C u0 p0 c0 {1,S} {24,S} {25,S} {26,S}
7  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
8  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.20869,0.111441,-7.91347e-05,2.92406e-08,-4.43743e-12,-29944.7,44.9522], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.114,0.0718938,-3.25718e-05,5.46437e-09,0,-32958.4,-17.0886], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "C7H15(78)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {7,S} {20,S} {21,S} {22,S}
7  C u1 p0 c0 {2,S} {5,S} {6,S}
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
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.30897,0.0696136,-3.3115e-05,5.82888e-09,3.54427e-14,-5785.13,24.5658], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.64219,0.0661233,-3.01694e-05,5.07586e-09,0,-6159.69,17.6337], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "I-C4H8(79)",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.938433,0.0390547,-2.16437e-05,5.87267e-09,-6.14435e-13,-3748.18,19.1443], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.86959,0.0329649,-1.46431e-05,2.4163e-09,0,-4226.75,9.3924], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "I-C3H7(80)",
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
            NASAPolynomial(coeffs=[1.7133,0.0254262,1.58081e-06,-1.82129e-08,8.82771e-12,7535.81,12.979], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.06337,0.0157449,-5.18239e-06,7.47724e-10,-3.85442e-14,5313.87,-21.9265], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "T-C4H9(81)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.73729,0.045539,-2.26391e-05,4.56951e-09,-1.55322e-13,4871.39,41.4145], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[-1.58632,0.0422348,-1.93281e-05,3.25654e-09,0,4566.08,35.5115], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "C8H17(82)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {1,S} {21,S} {22,S} {23,S}
7  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
8  C u1 p0 c0 {2,S} {24,S} {25,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.097316,0.0892654,-5.12874e-05,1.37641e-08,-1.27788e-12,-8811.47,28.9792], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.37959,0.0727998,-3.3509e-05,5.69649e-09,0,-10220.4,1.09221], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "C7H14(83)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {5,S} {7,D}
7  C u0 p0 c0 {6,D} {20,S} {21,S}
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
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.842233,0.0789798,-5.04574e-05,1.68934e-08,-2.37202e-12,-14597.2,31.9096], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.5195,0.0583988,-2.60086e-05,4.29182e-09,0,-16142,-0.0715568], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "C8H17O(84)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {18,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {21,S} {22,S} {23,S}
6  C u0 p0 c0 {1,S} {24,S} {25,S} {26,S}
7  C u0 p0 c0 {2,S} {13,S} {14,S} {15,S}
8  C u0 p0 c0 {2,S} {12,S} {16,S} {17,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 O u1 p2 c0 {8,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {5,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.80491,0.115185,-8.57614e-05,3.31878e-08,-5.24475e-12,-21941.8,47.1111], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.4791,0.069193,-3.13857e-05,5.27482e-09,0,-25426,-24.7628], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "C3H6O(85)",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.55639,-0.00283864,7.05723e-05,-8.78131e-08,3.40291e-11,-27832.5,2.3196], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.29797,0.0175657,-6.31678e-06,1.02026e-09,-6.10904e-14,-29536.9,-12.7592], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "I-C4H7(86)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u1 p0 c0 {2,S} {8,S} {9,S}
4  C u0 p0 c0 {2,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.000720882,0.0436496,-3.16386e-05,1.23985e-08,-2.04378e-12,14571.8,23.3234], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.86718,0.0275411,-1.19816e-05,1.93828e-09,0,13412.1,-1.0471], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "C7H13(87)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
5  C u0 p0 c0 {4,S} {6,D} {7,S}
6  C u0 p0 c0 {1,S} {5,D} {18,S}
7  C u1 p0 c0 {5,S} {19,S} {20,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.306783,0.0720691,-4.20234e-05,1.2005e-08,-1.32605e-12,1237.4,28.7285], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.05918,0.0584268,-2.65106e-05,4.4425e-09,0,147.082,6.6447], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "C4H6O(88)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D} {4,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {8,D} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {4,D}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.627184,0.046678,-3.74431e-05,1.58331e-08,-2.73952e-12,-15720.3,21.6034], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.19598,0.0249956,-1.10451e-05,1.8092e-09,0,-17289.2,-11.299], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "C4H9O(89)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  O u1 p2 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
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
            NASAPolynomial(coeffs=[-0.770464,0.0581927,-4.36198e-05,1.74942e-08,-2.91836e-12,-13650.3,27.7577], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.29677,0.0348949,-1.53075e-05,2.49416e-09,0,-15339.7,-7.64896], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "C4H7O(90)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {4,D}
4  C u0 p0 c0 {3,D} {11,S} {12,S}
5  O u1 p2 c0 {2,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.74701,0.0407783,-2.4475e-05,7.06503e-09,-7.51571e-13,4869.79,19.4536], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.69209,0.0318285,-1.46589e-05,2.50217e-09,0,4118.02,4.48457], Tmin=(1000,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "C6H6(91)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,D}
2  C u0 p0 c0 {1,S} {4,D} {7,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,D} {5,S} {8,S}
5  C u0 p0 c0 {3,D} {4,S} {9,S}
6  C u0 p0 c0 {1,D} {11,S} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.34008,0.0717284,-6.45824e-05,2.78691e-08,-3.95001e-12,25893.7,47.0844], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.78194,0.0406322,-2.35029e-05,6.51056e-09,-6.96809e-13,24315.6,7.84216], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "A1-(92)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {8,S}
3  C u0 p0 c0 {1,B} {5,B} {9,S}
4  C u0 p0 c0 {2,B} {6,B} {10,S}
5  C u0 p0 c0 {3,B} {6,B} {11,S}
6  C u1 p0 c0 {4,B} {5,B}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.87655,0.0626806,-4.87402e-05,1.41122e-08,5.18518e-13,39926.9,45.9964], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.38016,0.0404032,-2.42251e-05,6.88723e-09,-7.50961e-13,38697.4,15.5221], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "A1C2H2(93)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {5,B} {12,S}
3  C u0 p0 c0 {1,B} {6,B} {13,S}
4  C u0 p0 c0 {5,B} {6,B} {9,S}
5  C u0 p0 c0 {2,B} {4,B} {10,S}
6  C u0 p0 c0 {3,B} {4,B} {11,S}
7  C u0 p0 c0 {1,S} {8,D} {14,S}
8  C u1 p0 c0 {7,D} {15,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.30997,0.0950908,-9.55699e-05,4.96808e-08,-1.01792e-11,45732.9,53.5393], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.98045,0.0469432,-2.67378e-05,7.29778e-09,-7.71093e-13,43286.4,-5.85268], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "A1C2H3(94)",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {4,S}
2  C u0 p0 c0 {1,B} {5,B} {13,S}
3  C u0 p0 c0 {1,B} {7,B} {14,S}
4  C u0 p0 c0 {1,S} {8,D} {9,S}
5  C u0 p0 c0 {2,B} {6,B} {10,S}
6  C u0 p0 c0 {5,B} {7,B} {11,S}
7  C u0 p0 c0 {3,B} {6,B} {12,S}
8  C u0 p0 c0 {4,D} {15,S} {16,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.385,0.0820365,-5.34462e-05,5.59095e-09,5.61139e-12,16085.8,50.1105], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.540554,0.0617302,-3.73947e-05,1.07047e-08,-1.17305e-12,15041.3,21.4503], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "A1C2H(95)",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {5,B} {12,S}
3  C u0 p0 c0 {1,B} {6,B} {13,S}
4  C u0 p0 c0 {5,B} {6,B} {9,S}
5  C u0 p0 c0 {2,B} {4,B} {10,S}
6  C u0 p0 c0 {3,B} {4,B} {11,S}
7  C u0 p0 c0 {1,S} {8,T}
8  C u0 p0 c0 {7,T} {14,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.21037,0.0865552,-8.45007e-05,4.21921e-08,-8.16766e-12,35248.9,46.9445], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.8152,0.0440873,-2.52054e-05,6.90275e-09,-7.31379e-13,33027.2,-6.49321], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "A1C2H*(96)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {6,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {10,S}
3  C u0 p0 c0 {2,B} {4,B} {11,S}
4  C u0 p0 c0 {3,B} {5,B} {9,S}
5  C u0 p0 c0 {4,B} {6,B} {12,S}
6  C u1 p0 c0 {1,B} {5,B}
7  C u0 p0 c0 {1,S} {8,T}
8  C u0 p0 c0 {7,T} {13,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.42758,0.0836669,-8.70106e-05,4.70286e-08,-1.01817e-11,67330.2,44.8118], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.23812,0.0383812,-2.18851e-05,5.97161e-09,-6.30351e-13,64952.8,-11.7513], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "C8H7(97)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {4,S}
2  C u0 p0 c0 {1,B} {5,B} {10,S}
3  C u0 p0 c0 {1,B} {6,B} {11,S}
4  C u0 p0 c0 {1,S} {7,D} {9,S}
5  C u0 p0 c0 {2,B} {8,B} {12,S}
6  C u0 p0 c0 {3,B} {8,B} {13,S}
7  C u0 p0 c0 {4,D} {14,S} {15,S}
8  C u1 p0 c0 {5,B} {6,B}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.36215,0.0867033,-7.54298e-05,3.0114e-08,-3.40681e-12,47781.8,50.7408], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.90115,0.0515894,-3.05081e-05,8.55911e-09,-9.23047e-13,45993.5,5.96931], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "A2-(98)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {4,B}
2  C u0 p0 c0 {1,B} {5,B} {10,B}
3  C u0 p0 c0 {1,B} {8,B} {12,S}
4  C u0 p0 c0 {1,B} {6,B} {13,S}
5  C u0 p0 c0 {2,B} {7,B} {16,S}
6  C u0 p0 c0 {4,B} {7,B} {14,S}
7  C u0 p0 c0 {5,B} {6,B} {15,S}
8  C u0 p0 c0 {3,B} {9,B} {11,S}
9  C u0 p0 c0 {8,B} {10,B} {17,S}
10 C u1 p0 c0 {2,B} {9,B}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.02718,0.102925,-8.34272e-05,2.72135e-08,-7.2456e-13,50136.3,60.8902], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.22892,0.0631264,-3.80582e-05,1.08454e-08,-1.18343e-12,47840.1,5.82017], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "A2(99)",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {4,B}
2  C u0 p0 c0 {1,B} {5,B} {6,B}
3  C u0 p0 c0 {1,B} {8,B} {13,S}
4  C u0 p0 c0 {1,B} {9,B} {14,S}
5  C u0 p0 c0 {2,B} {10,B} {17,S}
6  C u0 p0 c0 {2,B} {7,B} {18,S}
7  C u0 p0 c0 {6,B} {8,B} {11,S}
8  C u0 p0 c0 {3,B} {7,B} {12,S}
9  C u0 p0 c0 {4,B} {10,B} {15,S}
10 C u0 p0 c0 {5,B} {9,B} {16,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.72435,0.105376,-8.01711e-05,2.18546e-08,1.42067e-12,16658.9,61.9829], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.76826,0.0689144,-4.14322e-05,1.17914e-08,-1.28597e-12,14541.3,10.6258], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "A2*(100)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {5,B}
2  C u0 p0 c0 {1,B} {4,B} {8,B}
3  C u0 p0 c0 {1,B} {6,B} {12,S}
4  C u0 p0 c0 {2,B} {7,B} {15,S}
5  C u0 p0 c0 {1,B} {9,B} {11,S}
6  C u0 p0 c0 {3,B} {7,B} {13,S}
7  C u0 p0 c0 {4,B} {6,B} {14,S}
8  C u0 p0 c0 {2,B} {10,B} {17,S}
9  C u0 p0 c0 {5,B} {10,B} {16,S}
10 C u1 p0 c0 {8,B} {9,B}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.00769,0.103041,-8.38191e-05,2.76492e-08,-8.88842e-13,49974.1,60.7299], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.29951,0.0630133,-3.7976e-05,1.08181e-08,-1.18008e-12,47665.8,5.41216], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "C12H9(101)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,B}
2  C u0 p0 c0 {1,B} {5,B} {6,B}
3  C u0 p0 c0 {1,B} {4,B} {11,S}
4  C u0 p0 c0 {3,B} {8,B} {13,S}
5  C u0 p0 c0 {2,B} {8,B} {15,S}
6  C u0 p0 c0 {2,B} {9,B} {16,S}
7  C u0 p0 c0 {1,B} {10,B} {19,S}
8  C u0 p0 c0 {4,B} {5,B} {14,S}
9  C u0 p0 c0 {6,B} {10,B} {17,S}
10 C u0 p0 c0 {7,B} {9,B} {18,S}
11 C u0 p0 c0 {3,S} {12,D} {20,S}
12 C u1 p0 c0 {11,D} {21,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.26785,0.135043,-0.000129792,6.2722e-08,-1.16349e-11,56483.3,67.1407], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.53385,0.0687543,-4.0175e-05,1.11481e-08,-1.19062e-12,52758.3,-19.7684], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "C12H9(102)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {6,B} {7,B}
2  C u0 p0 c0 {1,B} {4,B} {8,B}
3  C u0 p0 c0 {4,B} {5,B} {11,S}
4  C u0 p0 c0 {2,B} {3,B} {19,S}
5  C u0 p0 c0 {3,B} {6,B} {13,S}
6  C u0 p0 c0 {1,B} {5,B} {14,S}
7  C u0 p0 c0 {1,B} {9,B} {15,S}
8  C u0 p0 c0 {2,B} {10,B} {18,S}
9  C u0 p0 c0 {7,B} {10,B} {16,S}
10 C u0 p0 c0 {8,B} {9,B} {17,S}
11 C u0 p0 c0 {3,S} {12,D} {20,S}
12 C u1 p0 c0 {11,D} {21,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.38519,0.134826,-0.000128962,6.1448e-08,-1.09467e-11,56372.4,67.9545], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.59341,0.0702777,-4.10738e-05,1.14009e-08,-1.21861e-12,52937.9,-14.4754], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "C12H8(103)",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {6,B}
2  C u0 p0 c0 {1,B} {4,B} {5,B}
3  C u0 p0 c0 {1,B} {7,B} {11,S}
4  C u0 p0 c0 {2,B} {8,B} {15,S}
5  C u0 p0 c0 {2,B} {9,B} {16,S}
6  C u0 p0 c0 {1,B} {10,B} {19,S}
7  C u0 p0 c0 {3,B} {8,B} {13,S}
8  C u0 p0 c0 {4,B} {7,B} {14,S}
9  C u0 p0 c0 {5,B} {10,B} {17,S}
10 C u0 p0 c0 {6,B} {9,B} {18,S}
11 C u0 p0 c0 {3,S} {12,T}
12 C u0 p0 c0 {11,T} {20,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.23048,0.126053,-0.000117499,5.36791e-08,-8.85462e-12,42374.8,61.0992], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.55691,0.0671073,-3.92896e-05,1.0948e-08,-1.17461e-12,39137.2,-15.7914], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "C12H8(104)",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {5,B} {6,B}
2  C u0 p0 c0 {1,B} {4,B} {7,B}
3  C u0 p0 c0 {4,B} {8,B} {11,S}
4  C u0 p0 c0 {2,B} {3,B} {19,S}
5  C u0 p0 c0 {1,B} {8,B} {14,S}
6  C u0 p0 c0 {1,B} {9,B} {15,S}
7  C u0 p0 c0 {2,B} {10,B} {18,S}
8  C u0 p0 c0 {3,B} {5,B} {13,S}
9  C u0 p0 c0 {6,B} {10,B} {16,S}
10 C u0 p0 c0 {7,B} {9,B} {17,S}
11 C u0 p0 c0 {3,S} {12,T}
12 C u0 p0 c0 {11,T} {20,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.2258,0.126248,-0.000118141,5.43987e-08,-9.12585e-12,42549.5,61.1604], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.639,0.0669336,-3.915e-05,1.09e-08,-1.16866e-12,39294.7,-16.1008], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "C12H7(105)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {4,B} {6,B}
2  C u0 p0 c0 {1,B} {3,B} {8,B}
3  C u0 p0 c0 {2,B} {5,B} {11,S}
4  C u0 p0 c0 {1,B} {7,B} {15,S}
5  C u0 p0 c0 {3,B} {7,B} {13,S}
6  C u0 p0 c0 {1,B} {9,B} {16,S}
7  C u0 p0 c0 {4,B} {5,B} {14,S}
8  C u0 p0 c0 {2,B} {10,B} {18,S}
9  C u0 p0 c0 {6,B} {10,B} {17,S}
10 C u1 p0 c0 {8,B} {9,B}
11 C u0 p0 c0 {3,S} {12,T}
12 C u0 p0 c0 {11,T} {19,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.36585,0.122558,-0.000118737,5.7394e-08,-1.05059e-11,76983.7,57.9534], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.8846,0.0615767,-3.60989e-05,1.00593e-08,-1.07868e-12,73626,-21.2171], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "C12H7(106)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {4,B} {5,B}
2  C u0 p0 c0 {1,B} {6,B} {10,B}
3  C u0 p0 c0 {4,B} {9,B} {11,S}
4  C u0 p0 c0 {1,B} {3,B} {17,S}
5  C u0 p0 c0 {1,B} {8,B} {16,S}
6  C u0 p0 c0 {2,B} {7,B} {13,S}
7  C u0 p0 c0 {6,B} {8,B} {14,S}
8  C u0 p0 c0 {5,B} {7,B} {15,S}
9  C u0 p0 c0 {3,B} {10,B} {18,S}
10 C u1 p0 c0 {2,B} {9,B}
11 C u0 p0 c0 {3,S} {12,T}
12 C u0 p0 c0 {11,T} {19,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.35511,0.122525,-0.000118741,5.74311e-08,-1.05233e-11,77335.5,58.0873], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.8879,0.0615504,-3.60749e-05,1.0051e-08,-1.07768e-12,73980.4,-21.0417], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "A2R5(107)",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {4,B}
2  C u0 p0 c0 {1,B} {6,S} {7,B}
3  C u0 p0 c0 {1,B} {8,B} {9,B}
4  C u0 p0 c0 {1,B} {5,S} {10,B}
5  C u0 p0 c0 {4,S} {6,D} {13,S}
6  C u0 p0 c0 {2,S} {5,D} {14,S}
7  C u0 p0 c0 {2,B} {11,B} {15,S}
8  C u0 p0 c0 {3,B} {11,B} {17,S}
9  C u0 p0 c0 {3,B} {12,B} {18,S}
10 C u0 p0 c0 {4,B} {12,B} {20,S}
11 C u0 p0 c0 {7,B} {8,B} {16,S}
12 C u0 p0 c0 {9,B} {10,B} {19,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {11,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {12,S}
20 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-10.5498,0.125537,-0.000103646,3.52989e-08,-1.64508e-12,29442.7,70.2667], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.65433,0.0752647,-4.54865e-05,1.29795e-08,-1.41731e-12,26522.3,0.723303], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "A2R5-(108)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {4,B}
2  C u0 p0 c0 {1,B} {6,S} {7,B}
3  C u0 p0 c0 {1,B} {5,S} {10,B}
4  C u0 p0 c0 {1,B} {8,B} {11,B}
5  C u0 p0 c0 {3,S} {6,D} {13,S}
6  C u0 p0 c0 {2,S} {5,D} {14,S}
7  C u0 p0 c0 {2,B} {9,B} {15,S}
8  C u0 p0 c0 {4,B} {9,B} {17,S}
9  C u0 p0 c0 {7,B} {8,B} {16,S}
10 C u0 p0 c0 {3,B} {12,B} {18,S}
11 C u0 p0 c0 {4,B} {12,B} {19,S}
12 C u1 p0 c0 {10,B} {11,B}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.79699,0.122277,-0.000104933,3.87946e-08,-3.1629e-12,62484,68.2744], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.90109,0.0698932,-4.24226e-05,1.21346e-08,-1.32684e-12,59439.1,-3.69961], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "C14H9(109)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {4,B}
2  C u0 p0 c0 {1,B} {6,B} {8,S}
3  C u0 p0 c0 {1,B} {9,S} {10,B}
4  C u0 p0 c0 {1,B} {7,B} {11,B}
5  C u0 p0 c0 {6,B} {7,B} {13,S}
6  C u0 p0 c0 {2,B} {5,B} {15,S}
7  C u0 p0 c0 {4,B} {5,B} {21,S}
8  C u0 p0 c0 {2,S} {9,D} {16,S}
9  C u0 p0 c0 {3,S} {8,D} {17,S}
10 C u0 p0 c0 {3,B} {12,B} {18,S}
11 C u0 p0 c0 {4,B} {12,B} {20,S}
12 C u0 p0 c0 {10,B} {11,B} {19,S}
13 C u0 p0 c0 {5,S} {14,D} {22,S}
14 C u1 p0 c0 {13,D} {23,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {12,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {13,S}
23 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.79889,0.145401,-0.00012836,5.15869e-08,-6.01742e-12,68709.5,69.3518], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.80127,0.0814615,-4.8765e-05,1.38133e-08,-1.5e-12,65087.1,-16.6225], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "C14H8(110)",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {4,B}
2  C u0 p0 c0 {1,B} {6,B} {8,S}
3  C u0 p0 c0 {1,B} {9,S} {10,B}
4  C u0 p0 c0 {1,B} {7,B} {11,B}
5  C u0 p0 c0 {6,B} {7,B} {13,S}
6  C u0 p0 c0 {2,B} {5,B} {15,S}
7  C u0 p0 c0 {4,B} {5,B} {21,S}
8  C u0 p0 c0 {2,S} {9,D} {16,S}
9  C u0 p0 c0 {3,S} {8,D} {17,S}
10 C u0 p0 c0 {3,B} {12,B} {18,S}
11 C u0 p0 c0 {4,B} {12,B} {20,S}
12 C u0 p0 c0 {10,B} {11,B} {19,S}
13 C u0 p0 c0 {5,S} {14,T}
14 C u0 p0 c0 {13,T} {22,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {12,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.952,0.145414,-0.000139201,6.55033e-08,-1.13837e-11,55399.4,68.302], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.29417,0.0737696,-4.35833e-05,1.22154e-08,-1.31549e-12,51411,-25.5651], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "C14H7(111)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {4,B}
2  C u0 p0 c0 {1,B} {6,B} {8,S}
3  C u0 p0 c0 {1,B} {9,S} {10,B}
4  C u0 p0 c0 {1,B} {7,B} {11,B}
5  C u0 p0 c0 {6,B} {7,B} {13,S}
6  C u0 p0 c0 {2,B} {5,B} {15,S}
7  C u0 p0 c0 {4,B} {5,B} {18,S}
8  C u0 p0 c0 {2,S} {9,D} {16,S}
9  C u0 p0 c0 {3,S} {8,D} {17,S}
10 C u0 p0 c0 {3,B} {12,B} {19,S}
11 C u0 p0 c0 {4,B} {12,B} {20,S}
12 C u1 p0 c0 {10,B} {11,B}
13 C u0 p0 c0 {5,S} {14,T}
14 C u0 p0 c0 {13,T} {21,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.0909,0.141918,-0.000140371,6.90982e-08,-1.29788e-11,89221.2,65.2159], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.6117,0.0682676,-4.04202e-05,1.13372e-08,-1.22096e-12,85115.5,-30.8959], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "P2(112)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,B} {4,B}
2  C u0 p0 c0 {1,S} {5,B} {6,B}
3  C u0 p0 c0 {1,B} {9,B} {19,S}
4  C u0 p0 c0 {1,B} {10,B} {20,S}
5  C u0 p0 c0 {2,B} {11,B} {21,S}
6  C u0 p0 c0 {2,B} {12,B} {22,S}
7  C u0 p0 c0 {9,B} {10,B} {13,S}
8  C u0 p0 c0 {11,B} {12,B} {14,S}
9  C u0 p0 c0 {3,B} {7,B} {15,S}
10 C u0 p0 c0 {4,B} {7,B} {16,S}
11 C u0 p0 c0 {5,B} {8,B} {17,S}
12 C u0 p0 c0 {6,B} {8,B} {18,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {11,S}
18 H u0 p0 c0 {12,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-11.9438,0.142163,-0.000133497,6.20506e-08,-1.05767e-11,20193.7,78.1851], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.73687,0.0754659,-4.38685e-05,1.21616e-08,-1.30012e-12,16602.2,-7.75536], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "P2-(113)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,B} {4,B}
2  C u0 p0 c0 {1,S} {5,B} {12,B}
3  C u0 p0 c0 {1,B} {8,B} {19,S}
4  C u0 p0 c0 {1,B} {9,B} {20,S}
5  C u0 p0 c0 {2,B} {6,B} {18,S}
6  C u0 p0 c0 {5,B} {10,B} {14,S}
7  C u0 p0 c0 {8,B} {9,B} {15,S}
8  C u0 p0 c0 {3,B} {7,B} {16,S}
9  C u0 p0 c0 {4,B} {7,B} {17,S}
10 C u0 p0 c0 {6,B} {11,B} {13,S}
11 C u0 p0 c0 {10,B} {12,B} {21,S}
12 C u1 p0 c0 {2,B} {11,B}
13 H u0 p0 c0 {10,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.50092,0.125211,-9.83718e-05,2.75934e-08,1.67954e-12,52990.3,69.1608], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.9767,0.0779432,-4.74482e-05,1.36376e-08,-1.49858e-12,50296.4,3.31269], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "A3-(114)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {8,B}
2  C u0 p0 c0 {1,B} {4,B} {5,B}
3  C u0 p0 c0 {1,B} {6,B} {7,B}
4  C u0 p0 c0 {2,B} {9,B} {14,B}
5  C u0 p0 c0 {2,B} {12,B} {16,S}
6  C u0 p0 c0 {3,B} {9,B} {18,S}
7  C u0 p0 c0 {3,B} {10,B} {19,S}
8  C u0 p0 c0 {1,B} {11,B} {22,S}
9  C u0 p0 c0 {4,B} {6,B} {17,S}
10 C u0 p0 c0 {7,B} {11,B} {20,S}
11 C u0 p0 c0 {8,B} {10,B} {21,S}
12 C u0 p0 c0 {5,B} {13,B} {15,S}
13 C u0 p0 c0 {12,B} {14,B} {23,S}
14 C u1 p0 c0 {4,B} {13,B}
15 H u0 p0 c0 {12,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {9,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-10.8882,0.141187,-0.000113531,3.59175e-08,-4.50212e-13,57015.9,73.813], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.71265,0.086723,-5.26012e-05,1.5046e-08,-1.64564e-12,53794,-2.69868], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "A3(115)",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {5,B}
2  C u0 p0 c0 {1,B} {4,B} {10,B}
3  C u0 p0 c0 {1,B} {6,B} {7,B}
4  C u0 p0 c0 {2,B} {8,B} {9,B}
5  C u0 p0 c0 {1,B} {12,B} {17,S}
6  C u0 p0 c0 {3,B} {11,B} {18,S}
7  C u0 p0 c0 {3,B} {8,B} {19,S}
8  C u0 p0 c0 {4,B} {7,B} {20,S}
9  C u0 p0 c0 {4,B} {13,B} {21,S}
10 C u0 p0 c0 {2,B} {14,B} {24,S}
11 C u0 p0 c0 {6,B} {12,B} {15,S}
12 C u0 p0 c0 {5,B} {11,B} {16,S}
13 C u0 p0 c0 {9,B} {14,B} {22,S}
14 C u0 p0 c0 {10,B} {13,B} {23,S}
15 H u0 p0 c0 {11,S}
16 H u0 p0 c0 {12,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {13,S}
23 H u0 p0 c0 {14,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-11.5461,0.143758,-0.000110869,3.1218e-08,1.45975e-12,22168.8,75.4983], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.38726,0.0921886,-5.57287e-05,1.59124e-08,-1.73884e-12,19106.2,2.24294], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "A3*(116)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {4,B} {9,B}
2  C u0 p0 c0 {1,B} {7,B} {8,B}
3  C u0 p0 c0 {4,B} {5,B} {6,B}
4  C u0 p0 c0 {1,B} {3,B} {14,B}
5  C u0 p0 c0 {3,B} {12,B} {16,S}
6  C u0 p0 c0 {3,B} {7,B} {17,S}
7  C u0 p0 c0 {2,B} {6,B} {18,S}
8  C u0 p0 c0 {2,B} {10,B} {19,S}
9  C u0 p0 c0 {1,B} {11,B} {22,S}
10 C u0 p0 c0 {8,B} {11,B} {20,S}
11 C u0 p0 c0 {9,B} {10,B} {21,S}
12 C u0 p0 c0 {5,B} {13,B} {15,S}
13 C u0 p0 c0 {12,B} {14,B} {23,S}
14 C u1 p0 c0 {4,B} {13,B}
15 H u0 p0 c0 {12,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-10.8882,0.141187,-0.000113531,3.59175e-08,-4.50212e-13,57015.9,73.813], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.71265,0.086723,-5.26012e-05,1.5046e-08,-1.64564e-12,53794,-2.69868], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "A3R5-(117)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,B} {4,B} {5,B}
2  C u0 p0 c0 {3,B} {6,B} {12,B}
3  C u0 p0 c0 {1,B} {2,B} {11,B}
4  C u0 p0 c0 {1,B} {7,B} {8,S}
5  C u0 p0 c0 {1,B} {9,S} {10,B}
6  C u0 p0 c0 {2,B} {7,B} {14,B}
7  C u0 p0 c0 {4,B} {6,B} {18,S}
8  C u0 p0 c0 {4,S} {9,D} {19,S}
9  C u0 p0 c0 {5,S} {8,D} {20,S}
10 C u0 p0 c0 {5,B} {13,B} {21,S}
11 C u0 p0 c0 {3,B} {13,B} {23,S}
12 C u0 p0 c0 {2,B} {15,B} {17,S}
13 C u0 p0 c0 {10,B} {11,B} {22,S}
14 C u0 p0 c0 {6,B} {16,B} {25,S}
15 C u0 p0 c0 {12,B} {16,B} {24,S}
16 C u1 p0 c0 {14,B} {15,B}
17 H u0 p0 c0 {12,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {13,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {15,S}
25 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-12.5419,0.160371,-0.000135029,4.76044e-08,-2.93662e-12,68710.8,80.607], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.47777,0.0933338,-5.68627e-05,1.63047e-08,-1.78567e-12,64749,-12.6769], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "A3R5(118)",
    molecule = 
"""
1  C u0 p0 c0 {3,B} {4,B} {6,B}
2  C u0 p0 c0 {3,B} {5,B} {11,B}
3  C u0 p0 c0 {1,B} {2,B} {12,B}
4  C u0 p0 c0 {1,B} {7,B} {9,S}
5  C u0 p0 c0 {2,B} {7,B} {10,B}
6  C u0 p0 c0 {1,B} {8,S} {13,B}
7  C u0 p0 c0 {4,B} {5,B} {19,S}
8  C u0 p0 c0 {6,S} {9,D} {17,S}
9  C u0 p0 c0 {4,S} {8,D} {18,S}
10 C u0 p0 c0 {5,B} {14,B} {20,S}
11 C u0 p0 c0 {2,B} {15,B} {23,S}
12 C u0 p0 c0 {3,B} {16,B} {24,S}
13 C u0 p0 c0 {6,B} {16,B} {26,S}
14 C u0 p0 c0 {10,B} {15,B} {21,S}
15 C u0 p0 c0 {11,B} {14,B} {22,S}
16 C u0 p0 c0 {12,B} {13,B} {25,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {14,S}
22 H u0 p0 c0 {15,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {16,S}
26 H u0 p0 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-13.2242,0.162863,-0.000131967,4.24394e-08,-8.53172e-13,34443.1,83.0299], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.07025,0.0989917,-6.014e-05,1.72205e-08,-1.88476e-12,30652.8,-6.7218], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "A4(119)",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {6,B}
2  C u0 p0 c0 {1,B} {4,B} {5,B}
3  C u0 p0 c0 {1,B} {7,B} {8,B}
4  C u0 p0 c0 {2,B} {9,B} {10,B}
5  C u0 p0 c0 {2,B} {11,B} {12,B}
6  C u0 p0 c0 {1,B} {13,B} {14,B}
7  C u0 p0 c0 {3,B} {15,B} {18,S}
8  C u0 p0 c0 {3,B} {9,B} {19,S}
9  C u0 p0 c0 {4,B} {8,B} {20,S}
10 C u0 p0 c0 {4,B} {16,B} {21,S}
11 C u0 p0 c0 {5,B} {16,B} {23,S}
12 C u0 p0 c0 {5,B} {13,B} {24,S}
13 C u0 p0 c0 {6,B} {12,B} {25,S}
14 C u0 p0 c0 {6,B} {15,B} {26,S}
15 C u0 p0 c0 {7,B} {14,B} {17,S}
16 C u0 p0 c0 {10,B} {11,B} {22,S}
17 H u0 p0 c0 {15,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {16,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {13,S}
26 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-13.1524,0.160879,-0.00012772,3.90919e-08,7.43991e-14,24967.4,80.7618], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.5406,0.0998115,-6.06376e-05,1.73575e-08,-1.89902e-12,21275.6,-6.19295], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "A4-(120)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {5,B} {6,B}
2  C u0 p0 c0 {1,B} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {8,B} {9,B}
4  C u0 p0 c0 {2,B} {10,B} {11,B}
5  C u0 p0 c0 {1,B} {7,B} {14,B}
6  C u0 p0 c0 {1,B} {12,B} {15,B}
7  C u0 p0 c0 {5,B} {8,B} {17,S}
8  C u0 p0 c0 {3,B} {7,B} {18,S}
9  C u0 p0 c0 {3,B} {13,B} {19,S}
10 C u0 p0 c0 {4,B} {13,B} {21,S}
11 C u0 p0 c0 {4,B} {12,B} {22,S}
12 C u0 p0 c0 {6,B} {11,B} {23,S}
13 C u0 p0 c0 {9,B} {10,B} {20,S}
14 C u0 p0 c0 {5,B} {16,B} {24,S}
15 C u0 p0 c0 {6,B} {16,B} {25,S}
16 C u1 p0 c0 {14,B} {15,B}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {13,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {12,S}
24 H u0 p0 c0 {14,S}
25 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-12.3672,0.157658,-0.000129244,4.2863e-08,-1.54492e-12,62779.8,79.3139], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.85098,0.0943231,-5.74898e-05,1.64859e-08,-1.80542e-12,58957.3,-10.2177], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    label = "A4R5(121)",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {4,B} {8,B}
2  C u0 p0 c0 {1,B} {3,B} {7,B}
3  C u0 p0 c0 {2,B} {5,B} {6,B}
4  C u0 p0 c0 {1,B} {9,B} {11,S}
5  C u0 p0 c0 {3,B} {9,B} {12,B}
6  C u0 p0 c0 {3,B} {13,B} {14,B}
7  C u0 p0 c0 {2,B} {15,B} {16,B}
8  C u0 p0 c0 {1,B} {10,S} {17,B}
9  C u0 p0 c0 {4,B} {5,B} {21,S}
10 C u0 p0 c0 {8,S} {11,D} {19,S}
11 C u0 p0 c0 {4,S} {10,D} {20,S}
12 C u0 p0 c0 {5,B} {18,B} {22,S}
13 C u0 p0 c0 {6,B} {18,B} {24,S}
14 C u0 p0 c0 {6,B} {15,B} {25,S}
15 C u0 p0 c0 {7,B} {14,B} {26,S}
16 C u0 p0 c0 {7,B} {17,B} {27,S}
17 C u0 p0 c0 {8,B} {16,B} {28,S}
18 C u0 p0 c0 {12,B} {13,B} {23,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {12,S}
23 H u0 p0 c0 {18,S}
24 H u0 p0 c0 {13,S}
25 H u0 p0 c0 {14,S}
26 H u0 p0 c0 {15,S}
27 H u0 p0 c0 {16,S}
28 H u0 p0 c0 {17,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-14.7696,0.179658,-0.00014819,4.97722e-08,-2.06437e-12,37846.8,88.8184], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.20191,0.106656,-6.50829e-05,1.86776e-08,-2.04647e-12,33443.9,-14.2388], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "FLTN(122)",
    molecule = 
"""
1  C u0 p0 c0 {4,B} {5,B} {6,B}
2  C u0 p0 c0 {3,B} {5,S} {7,B}
3  C u0 p0 c0 {2,B} {4,S} {8,B}
4  C u0 p0 c0 {1,B} {3,S} {9,B}
5  C u0 p0 c0 {1,B} {2,S} {12,B}
6  C u0 p0 c0 {1,B} {10,B} {11,B}
7  C u0 p0 c0 {2,B} {14,B} {19,S}
8  C u0 p0 c0 {3,B} {13,B} {20,S}
9  C u0 p0 c0 {4,B} {15,B} {21,S}
10 C u0 p0 c0 {6,B} {15,B} {23,S}
11 C u0 p0 c0 {6,B} {16,B} {24,S}
12 C u0 p0 c0 {5,B} {16,B} {26,S}
13 C u0 p0 c0 {8,B} {14,B} {17,S}
14 C u0 p0 c0 {7,B} {13,B} {18,S}
15 C u0 p0 c0 {9,B} {10,B} {22,S}
16 C u0 p0 c0 {11,B} {12,B} {25,S}
17 H u0 p0 c0 {13,S}
18 H u0 p0 c0 {14,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {15,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {16,S}
26 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-12.9396,0.16032,-0.000126452,3.76049e-08,6.84839e-13,29108.5,81.2529], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.54793,0.099999,-6.08702e-05,1.74529e-08,-1.912e-12,25478,-4.65042], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    label = "C5H6(123)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,D} {8,S}
3  C u0 p0 c0 {1,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {5,S} {10,S}
5  C u0 p0 c0 {2,D} {4,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.13691,0.0606953,-4.60553e-05,1.28457e-08,7.41215e-13,15367.6,46.1568], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.230537,0.0409572,-2.41589e-05,6.79763e-09,-7.36374e-13,14377.9,20.2551], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "C5H5(124)",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {1,S} {4,D} {10,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.37844,0.0972392,-0.000169579,1.51819e-07,-5.12075e-11,30551.5,51.283], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.21465,0.0271835,-1.33173e-05,3.0898e-09,-2.7788e-13,28895.2,-0.0306], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    label = "C5H5O(125)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {5,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {8,D}
4  C u0 p0 c0 {3,S} {5,D} {10,S}
5  C u0 p0 c0 {2,S} {4,D} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.230436,0.0323226,2.89009e-05,-7.06806e-08,3.34072e-11,5555.47,25.3309], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.6065,0.0167471,-6.10976e-06,9.96746e-10,-6.01118e-14,1411.47,-42.6049], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    label = "C5H4O(126)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,D}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {4,S} {8,S}
4  C u0 p0 c0 {3,S} {5,D} {9,S}
5  C u0 p0 c0 {1,S} {4,D} {10,S}
6  O u0 p2 c0 {1,D}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.64381,0.0614329,-5.92149e-05,2.83233e-08,-5.02726e-12,5468.1,39.8672], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.25345,0.031364,-1.82864e-05,5.08408e-09,-5.44845e-13,3875.8,1.54537], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
    label = "C5H5O(127)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {5,S} {10,S}
5  C u0 p0 c0 {3,D} {4,S} {11,S}
6  O u1 p2 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.07776,0.0525817,-2.88565e-05,-3.38855e-09,6.33614e-12,25510.5,39.5915], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.54053,0.0229895,-9.54376e-06,1.70616e-09,-9.74594e-14,22263.7,-20.8188], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
    label = "C9H8(128)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,B} {5,B}
3  C u0 p0 c0 {2,B} {6,S} {7,B}
4  C u0 p0 c0 {1,S} {6,D} {12,S}
5  C u0 p0 c0 {2,B} {9,B} {16,S}
6  C u0 p0 c0 {3,S} {4,D} {17,S}
7  C u0 p0 c0 {3,B} {8,B} {15,S}
8  C u0 p0 c0 {7,B} {9,B} {13,S}
9  C u0 p0 c0 {5,B} {8,B} {14,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {9,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.12448,0.0977657,-7.30436e-05,1.88295e-08,1.84033e-12,18659,60.6775], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.1546,0.0654224,-3.92505e-05,1.11569e-08,-1.21593e-12,16816.6,15.3482], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 128,
    label = "C9H7(129)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {6,S}
2  C u0 p0 c0 {1,B} {4,B} {5,S}
3  C u0 p0 c0 {1,B} {7,B} {13,S}
4  C u0 p0 c0 {2,B} {8,B} {14,S}
5  C u1 p0 c0 {2,S} {9,S} {15,S}
6  C u0 p0 c0 {1,S} {9,D} {16,S}
7  C u0 p0 c0 {3,B} {8,B} {10,S}
8  C u0 p0 c0 {4,B} {7,B} {11,S}
9  C u0 p0 c0 {5,S} {6,D} {12,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {9,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-8.73685,0.103422,-9.23423e-05,3.75623e-08,-4.40605e-12,33164.1,62.8218], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.65598,0.0574808,-3.42871e-05,9.70279e-09,-1.05386e-12,30684.3,2.5768], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
    label = "A1CH2(130)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {11,S}
3  C u0 p0 c0 {1,B} {5,B} {12,S}
4  C u0 p0 c0 {2,B} {6,B} {8,S}
5  C u0 p0 c0 {3,B} {6,B} {9,S}
6  C u0 p0 c0 {4,B} {5,B} {10,S}
7  C u1 p0 c0 {1,S} {13,S} {14,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.07053,0.0835202,-7.417e-05,3.13154e-08,-4.23671e-12,23589.5,50.7932], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.3005,0.0480055,-2.78443e-05,7.72371e-09,-8.27154e-13,21749.9,5.42372], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 130,
    label = "C9H6O(131)",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {6,S}
2  C u0 p0 c0 {1,B} {4,B} {5,S}
3  C u0 p0 c0 {1,B} {7,B} {14,S}
4  C u0 p0 c0 {2,B} {8,B} {15,S}
5  C u0 p0 c0 {2,S} {9,S} {10,D}
6  C u0 p0 c0 {1,S} {9,D} {16,S}
7  C u0 p0 c0 {3,B} {8,B} {11,S}
8  C u0 p0 c0 {4,B} {7,B} {12,S}
9  C u0 p0 c0 {5,S} {6,D} {13,S}
10 O u0 p2 c0 {5,D}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.53929,0.0969323,-8.17699e-05,2.96699e-08,-2.24993e-12,6888.84,54.0946], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.65659,0.0570056,-3.43174e-05,9.76177e-09,-1.06334e-12,4578.57,-0.703868], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 131,
    label = "C6H4(132)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,D} {6,S} {9,S}
4  C u0 p0 c0 {2,D} {5,S} {10,S}
5  C u0 p0 c0 {4,S} {6,T}
6  C u0 p0 c0 {3,S} {5,T}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.4623,0.0574017,-4.92984e-05,1.9068e-08,-1.95431e-12,52522.4,38.8489], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.98619,0.0337638,-2.00238e-05,5.63854e-09,-6.10004e-13,51223.1,7.44533], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 132,
    label = "A1CH3(133)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {14,S}
4  C u0 p0 c0 {2,B} {6,B} {15,S}
5  C u0 p0 c0 {3,B} {7,B} {11,S}
6  C u0 p0 c0 {4,B} {7,B} {12,S}
7  C u0 p0 c0 {5,B} {6,B} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.54072,0.0685427,-3.57113e-05,-4.19398e-09,7.4178e-12,4641.21,45.7565], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[-1.01117,0.0585302,-3.47595e-05,9.82181e-09,-1.06681e-12,3993.63,28.3611], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 133,
    label = "A1OH(134)",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {11,S}
3  C u0 p0 c0 {1,B} {5,B} {12,S}
4  C u0 p0 c0 {2,B} {6,B} {8,S}
5  C u0 p0 c0 {3,B} {6,B} {9,S}
6  C u0 p0 c0 {4,B} {5,B} {10,S}
7  O u0 p2 c0 {1,S} {13,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.56571,0.0660135,-3.92958e-05,-3.62254e-09,8.62416e-12,-13110.1,40.1377], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.933152,0.0506598,-3.17619e-05,9.37559e-09,-1.05294e-12,-13757.5,18.7341], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 134,
    label = "C7H8O(135)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {8,S}
4  C u0 p0 c0 {2,B} {6,B} {15,S}
5  C u0 p0 c0 {3,B} {7,B} {13,S}
6  C u0 p0 c0 {4,B} {7,B} {12,S}
7  C u0 p0 c0 {5,B} {6,B} {14,S}
8  O u0 p2 c0 {3,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.49883,0.0691527,-2.88086e-05,-1.72913e-08,1.36327e-11,-17633.6,38.749], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[-0.0671722,0.0631867,-3.90768e-05,1.14167e-08,-1.27265e-12,-17855.4,27.2089], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "C7H7O(136)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {14,S}
4  C u0 p0 c0 {2,B} {6,B} {15,S}
5  C u0 p0 c0 {3,B} {7,B} {12,S}
6  C u0 p0 c0 {4,B} {7,B} {13,S}
7  C u0 p0 c0 {5,B} {6,B} {11,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 O u1 p2 c0 {7,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.88642,0.078426,-6.20807e-05,2.17167e-08,-1.65779e-12,471.681,44.8068], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.14522,0.0502784,-2.90785e-05,8.02844e-09,-8.55794e-13,-1225.24,5.3349], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "C7H7O(137)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {14,S}
4  C u0 p0 c0 {2,B} {6,B} {15,S}
5  C u0 p0 c0 {3,B} {7,B} {11,S}
6  C u0 p0 c0 {4,B} {7,B} {12,S}
7  C u0 p0 c0 {5,B} {6,B} {13,S}
8  O u1 p2 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.75333,0.0785832,-5.57119e-05,1.19665e-08,2.51904e-12,13115.5,49.3044], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.07931,0.0552719,-3.31303e-05,9.40679e-09,-1.02415e-12,11759.9,15.8658], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "C7H8O(138)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {14,S}
4  C u0 p0 c0 {2,B} {6,B} {15,S}
5  C u0 p0 c0 {3,B} {7,B} {11,S}
6  C u0 p0 c0 {4,B} {7,B} {12,S}
7  C u0 p0 c0 {5,B} {6,B} {13,S}
8  O u0 p2 c0 {1,S} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.8574,0.0238771,8.40508e-05,-1.33986e-07,5.69939e-11,-13795.6,17.3102], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.1623,0.026937,-9.8029e-06,1.59282e-09,-9.57108e-14,-18822.6,-54.7427], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "A1CHO(139)",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {11,S}
3  C u0 p0 c0 {1,B} {5,B} {12,S}
4  C u0 p0 c0 {2,B} {6,B} {8,S}
5  C u0 p0 c0 {3,B} {6,B} {9,S}
6  C u0 p0 c0 {4,B} {5,B} {10,S}
7  C u0 p0 c0 {1,S} {13,D} {14,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 O u0 p2 c0 {7,D}
14 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.47171,0.0692892,-4.32604e-05,3.43871e-09,4.8101e-12,-6145.59,41.4094], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.87356,0.0526232,-3.17645e-05,9.06403e-09,-9.90306e-13,-7236.04,14.9787], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "A1O(140)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {6,B} {7,S}
2  C u0 p0 c0 {1,B} {3,B} {8,S}
3  C u0 p0 c0 {2,B} {4,B} {9,S}
4  C u0 p0 c0 {3,B} {5,B} {10,S}
5  C u0 p0 c0 {4,B} {6,B} {11,S}
6  C u0 p0 c0 {1,B} {5,B} {12,S}
7  O u1 p2 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.51502,0.0703952,-5.92556e-05,2.1291e-08,-1.45169e-12,5191.73,44.7023], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.39257,0.041738,-2.49837e-05,7.08827e-09,-7.71343e-13,3603.36,6.16401], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    label = "C7H7(141)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {5,B} {11,S}
4  C u0 p0 c0 {2,B} {6,B} {12,S}
5  C u0 p0 c0 {3,B} {7,B} {13,S}
6  C u0 p0 c0 {4,B} {7,B} {14,S}
7  C u1 p0 c0 {5,B} {6,B}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.91657,0.066587,-3.99725e-05,2.04681e-09,4.98559e-12,35424.3,45.1374], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.519781,0.052622,-3.12983e-05,8.84817e-09,-9.61252e-13,34568.2,23.3397], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "C8H9(142)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {6,B} {14,S}
4  C u0 p0 c0 {2,B} {7,B} {15,S}
5  C u0 p0 c0 {6,B} {7,B} {11,S}
6  C u0 p0 c0 {3,B} {5,B} {12,S}
7  C u0 p0 c0 {4,B} {5,B} {13,S}
8  C u1 p0 c0 {1,S} {16,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.733299,0.0459053,3.78257e-05,-9.12367e-08,4.2559e-11,26157.3,25.0411], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.1327,0.0282904,-1.01802e-05,1.64177e-09,-9.81375e-14,20879.1,-60.0115], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 142,
    label = "C8H10(143)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {4,B} {5,B}
4  C u0 p0 c0 {3,B} {7,B} {17,S}
5  C u0 p0 c0 {3,B} {8,B} {18,S}
6  C u0 p0 c0 {7,B} {8,B} {14,S}
7  C u0 p0 c0 {4,B} {6,B} {15,S}
8  C u0 p0 c0 {5,B} {6,B} {16,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.24077,0.0359133,7.54222e-05,-1.31904e-07,5.74747e-11,1183.92,22.4682], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.6901,0.0323663,-1.16865e-05,1.8899e-09,-1.13202e-13,-4386.7,-60.4442], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 143,
    label = "S(144)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {4,B} {5,B}
4  C u0 p0 c0 {3,B} {7,B} {17,S}
5  C u0 p0 c0 {3,B} {8,B} {18,S}
6  C u0 p0 c0 {7,B} {8,B} {14,S}
7  C u0 p0 c0 {4,B} {6,B} {15,S}
8  C u0 p0 c0 {5,B} {6,B} {16,S}
9  O u0 p2 c0 {2,S} {19,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 O u1 p2 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.87929,0.0898132,-4.93686e-05,-4.06346e-09,9.57159e-12,18192.2,48.0636], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.74947,0.0733869,-4.43641e-05,1.26916e-08,-1.39034e-12,17112.1,20.2611], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 144,
    label = "S(145)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {8,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,B} {4,B}
3  C u0 p0 c0 {2,B} {6,B} {17,S}
4  C u0 p0 c0 {2,B} {7,B} {18,S}
5  C u0 p0 c0 {6,B} {7,B} {13,S}
6  C u0 p0 c0 {3,B} {5,B} {15,S}
7  C u0 p0 c0 {4,B} {5,B} {16,S}
8  C u1 p0 c0 {1,S} {9,S} {14,S}
9  O u0 p2 c0 {8,S} {10,S}
10 O u0 p2 c0 {9,S} {19,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.87929,0.0898132,-4.93686e-05,-4.06346e-09,9.57159e-12,18192.2,48.0636], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.74947,0.0733869,-4.43641e-05,1.26916e-08,-1.39034e-12,17112.1,20.2611], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 145,
    label = "S(146)",
    molecule = 
"""
1  C u0 p0 c0 {3,B} {4,B} {5,S}
2  C u0 p0 c0 {6,B} {7,B} {10,S}
3  C u0 p0 c0 {1,B} {6,B} {15,S}
4  C u0 p0 c0 {1,B} {7,B} {16,S}
5  C u0 p0 c0 {1,S} {8,D} {12,S}
6  C u0 p0 c0 {2,B} {3,B} {13,S}
7  C u0 p0 c0 {2,B} {4,B} {14,S}
8  C u0 p0 c0 {5,D} {9,S} {17,S}
9  O u0 p2 c0 {8,S} {11,S}
10 O u0 p2 c0 {2,S} {18,S}
11 O u0 p2 c0 {9,S} {19,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.93577,0.0924901,-6.0973e-05,7.8985e-09,5.41027e-12,-20171.5,39.1784], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.90515,0.0670729,-4.03281e-05,1.14966e-08,-1.25641e-12,-21751.6,0.577312], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 146,
    label = "C8H10(147)",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {4,S} {12,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {5,B} {8,B}
4  C u0 p0 c0 {2,S} {6,B} {7,B}
5  C u0 p0 c0 {3,B} {6,B} {15,S}
6  C u0 p0 c0 {4,B} {5,B} {16,S}
7  C u0 p0 c0 {4,B} {8,B} {17,S}
8  C u0 p0 c0 {3,B} {7,B} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.46067,0.0717789,-2.55611e-05,-1.74871e-08,1.22857e-11,162.315,43.6521], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[-1.95578,0.0709553,-4.19975e-05,1.18372e-08,-1.2834e-12,-69.1883,35.9161], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 147,
    label = "C8H9(148)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,B} {5,B}
3  C u0 p0 c0 {6,B} {7,B} {8,S}
4  C u0 p0 c0 {2,B} {6,B} {13,S}
5  C u0 p0 c0 {2,B} {7,B} {14,S}
6  C u0 p0 c0 {3,B} {4,B} {12,S}
7  C u0 p0 c0 {3,B} {5,B} {15,S}
8  C u1 p0 c0 {3,S} {16,S} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.06172,0.0870708,-6.4575e-05,1.84649e-08,4.97872e-13,19075,49.6831], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.36833,0.0603935,-3.50507e-05,9.7281e-09,-1.04236e-12,17634.5,13.5707], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "C8H8O(149)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,B} {5,B}
3  C u0 p0 c0 {6,B} {7,B} {8,S}
4  C u0 p0 c0 {2,B} {6,B} {12,S}
5  C u0 p0 c0 {2,B} {7,B} {15,S}
6  C u0 p0 c0 {3,B} {4,B} {13,S}
7  C u0 p0 c0 {3,B} {5,B} {14,S}
8  C u0 p0 c0 {3,S} {16,D} {17,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {5,S}
16 O u0 p2 c0 {8,D}
17 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.28641,0.0720781,-3.23579e-05,-1.04515e-08,9.86066e-12,-10739,39.2086], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[0.922059,0.0650623,-3.90203e-05,1.10867e-08,-1.20786e-12,-11389.6,22.98], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 149,
    label = "A2CH3(150)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,B} {5,B}
3  C u0 p0 c0 {2,B} {4,B} {8,B}
4  C u0 p0 c0 {3,B} {6,B} {7,B}
5  C u0 p0 c0 {2,B} {9,B} {15,S}
6  C u0 p0 c0 {4,B} {9,B} {17,S}
7  C u0 p0 c0 {4,B} {10,B} {18,S}
8  C u0 p0 c0 {3,B} {11,B} {21,S}
9  C u0 p0 c0 {5,B} {6,B} {16,S}
10 C u0 p0 c0 {7,B} {11,B} {19,S}
11 C u0 p0 c0 {8,B} {10,B} {20,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.20789,0.109245,-7.11311e-05,9.43727e-09,6.02816e-12,12140.6,56.817], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.43553,0.0812453,-4.85901e-05,1.37796e-08,-1.49925e-12,10403.1,14.2736], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 150,
    label = "C8H7O(151)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,B} {6,B} {7,S}
2  C u0 p0 c0 {4,B} {5,B} {8,S}
3  C u0 p0 c0 {1,B} {4,B} {9,S}
4  C u0 p0 c0 {2,B} {3,B} {10,S}
5  C u0 p0 c0 {2,B} {6,B} {11,S}
6  C u0 p0 c0 {1,B} {5,B} {12,S}
7  C u1 p0 c0 {1,S} {14,S} {15,S}
8  C u0 p0 c0 {2,S} {13,D} {16,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 O u0 p2 c0 {8,D}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.91655,0.0875543,-7.17107e-05,2.57665e-08,-2.00459e-12,8482.23,44.6893], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.25955,0.054488,-3.20686e-05,8.97678e-09,-9.66804e-13,6615.12,-0.114571], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 151,
    label = "S(152)",
    molecule = 
"""
1  C u0 p0 c0 {3,B} {6,B} {7,S}
2  C u0 p0 c0 {4,B} {5,B} {8,S}
3  C u0 p0 c0 {1,B} {4,B} {9,S}
4  C u0 p0 c0 {2,B} {3,B} {10,S}
5  C u0 p0 c0 {2,B} {6,B} {11,S}
6  C u0 p0 c0 {1,B} {5,B} {12,S}
7  C u0 p0 c0 {1,S} {13,D} {15,S}
8  C u0 p0 c0 {2,S} {14,D} {16,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 O u0 p2 c0 {7,D}
14 O u0 p2 c0 {8,D}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.05921,0.0725551,-3.97445e-05,-2.80273e-09,7.22e-12,-20998.3,33.2343], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.92024,0.059001,-3.59225e-05,1.02977e-08,-1.1278e-12,-22080.3,8.20067], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 152,
    label = "A2OH(153)",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {6,B}
2  C u0 p0 c0 {1,B} {4,B} {5,B}
3  C u0 p0 c0 {1,B} {7,B} {11,S}
4  C u0 p0 c0 {2,B} {8,B} {14,S}
5  C u0 p0 c0 {2,B} {9,B} {15,S}
6  C u0 p0 c0 {1,B} {10,B} {18,S}
7  C u0 p0 c0 {3,B} {8,B} {12,S}
8  C u0 p0 c0 {4,B} {7,B} {13,S}
9  C u0 p0 c0 {5,B} {10,B} {16,S}
10 C u0 p0 c0 {6,B} {9,B} {17,S}
11 O u0 p2 c0 {3,S} {19,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.08768,0.07681,-1.53593e-05,-4.04658e-08,2.3376e-11,-6290.56,34.3331], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[20.893,0.031056,-1.14408e-05,1.87873e-09,-1.13824e-13,-13588.6,-88.8597], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 153,
    label = "A2CH2(154)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,B}
2  C u0 p0 c0 {1,B} {5,B} {6,B}
3  C u0 p0 c0 {1,B} {4,B} {11,S}
4  C u0 p0 c0 {3,B} {8,B} {12,S}
5  C u0 p0 c0 {2,B} {8,B} {14,S}
6  C u0 p0 c0 {2,B} {9,B} {15,S}
7  C u0 p0 c0 {1,B} {10,B} {18,S}
8  C u0 p0 c0 {4,B} {5,B} {13,S}
9  C u0 p0 c0 {6,B} {10,B} {16,S}
10 C u0 p0 c0 {7,B} {9,B} {17,S}
11 C u1 p0 c0 {3,S} {19,S} {20,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {11,S}
20 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-9.3328,0.123841,-0.000108234,4.33682e-08,-5.01788e-12,32514.1,66.2741], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.97464,0.0711469,-4.20247e-05,1.18026e-08,-1.27462e-12,29626.8,-3.38252], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 154,
    label = "S(155)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {3,B} {5,B}
3  C u0 p0 c0 {2,B} {4,B} {8,B}
4  C u0 p0 c0 {3,B} {6,B} {7,B}
5  C u0 p0 c0 {2,B} {9,B} {15,S}
6  C u0 p0 c0 {4,B} {9,B} {17,S}
7  C u0 p0 c0 {4,B} {10,B} {18,S}
8  C u0 p0 c0 {3,B} {11,B} {21,S}
9  C u0 p0 c0 {5,B} {6,B} {16,S}
10 C u0 p0 c0 {7,B} {11,B} {19,S}
11 C u0 p0 c0 {8,B} {10,B} {20,S}
12 O u1 p2 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.78907,0.118258,-8.9261e-05,2.40235e-08,1.63301e-12,24030.6,63.3843], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.8886,0.0780883,-4.70476e-05,1.33962e-08,-1.46069e-12,21642.4,6.09699], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 155,
    label = "A2CHO(156)",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {7,B}
2  C u0 p0 c0 {1,B} {5,B} {6,B}
3  C u0 p0 c0 {1,B} {4,B} {11,S}
4  C u0 p0 c0 {3,B} {8,B} {12,S}
5  C u0 p0 c0 {2,B} {8,B} {14,S}
6  C u0 p0 c0 {2,B} {9,B} {15,S}
7  C u0 p0 c0 {1,B} {10,B} {18,S}
8  C u0 p0 c0 {4,B} {5,B} {13,S}
9  C u0 p0 c0 {6,B} {10,B} {16,S}
10 C u0 p0 c0 {7,B} {9,B} {17,S}
11 C u0 p0 c0 {3,S} {19,D} {20,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {7,S}
19 O u0 p2 c0 {11,D}
20 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.87929,0.0983094,-4.54845e-05,-2.01808e-08,1.77149e-11,1631.9,47.2936], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[-0.555792,0.0873748,-5.61818e-05,1.67233e-08,-1.88093e-12,1034.55,26.3087], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 156,
    label = "A2O(157)",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {4,B} {5,B}
2  C u0 p0 c0 {1,B} {3,B} {6,B}
3  C u0 p0 c0 {2,B} {7,B} {11,S}
4  C u0 p0 c0 {1,B} {8,B} {14,S}
5  C u0 p0 c0 {1,B} {9,B} {15,S}
6  C u0 p0 c0 {2,B} {10,B} {18,S}
7  C u0 p0 c0 {3,B} {8,B} {12,S}
8  C u0 p0 c0 {4,B} {7,B} {13,S}
9  C u0 p0 c0 {5,B} {10,B} {16,S}
10 C u0 p0 c0 {6,B} {9,B} {17,S}
11 O u1 p2 c0 {3,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {9,S}
17 H u0 p0 c0 {10,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.15176,0.0611355,3.20151e-05,-9.94285e-08,4.7999e-11,11405.9,32.5585], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[21.0591,0.0282563,-1.03329e-05,1.68867e-09,-1.01975e-13,4091.44,-88.4963], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 157,
    label = "S(158)",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,D}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,S} {8,D}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  C u0 p0 c0 {1,S} {5,D} {12,S}
7  O u0 p2 c0 {1,D}
8  O u0 p2 c0 {4,D}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.04372,0.0660964,-5.67977e-05,2.24901e-08,-2.6735e-12,-12436.9,34.3096], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.7029,0.0385045,-2.28745e-05,6.43292e-09,-6.94258e-13,-14076.9,-3.71425], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

