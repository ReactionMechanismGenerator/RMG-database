#!/usr/bin/env python
# encoding: utf-8

name = "Chernov"
shortDesc = u"Thermo from 2014 Chernov et al. Combustion and Flame mechanism"
longDesc = u"""
Includes thermo for species from the mechanism in:
V. Chernov, et al., 
Soot Formation with C1 and C2 Fuels Using an Improved Chemical Mechanism for PAH growth
Combustion and Flame 161 (2014) 592-601
except for CH2HCO, which was found to have innacurate thermo and removed
"""
entry(
    index = 0,
    label = "H2",
    molecule = 
"""
1 H u0 p0 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.3443,0.00798042,-1.94779e-05,2.0157e-08,-7.37603e-12,-917.924,0.683002], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.93283,0.000826598,-1.46401e-07,1.54099e-11,-6.88796e-16,-813.056,-1.02432], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 1,
    label = "CH4",
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
            NASAPolynomial(coeffs=[5.14826,-0.0137002,4.93749e-05,-4.91952e-08,1.70097e-11,-10245.3,-4.63323], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.91179,0.00960268,-3.38388e-06,5.38797e-10,-3.19307e-14,-10099.2,8.48242], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 2,
    label = "C2H2",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.80868,0.0233616,-3.55172e-05,2.80153e-08,-8.50075e-12,26429,13.9397], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.65878,0.00488397,-1.60829e-06,2.46975e-10,-1.38606e-14,25759.4,-3.99838], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 3,
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
            NASAPolynomial(coeffs=[3.9592,-0.00757051,5.7099e-05,-6.91588e-08,2.69884e-11,5089.78,4.0973], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.99183,0.0104834,-3.71721e-06,5.94628e-10,-3.5363e-14,4268.66,-0.269082], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 4,
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
            NASAPolynomial(coeffs=[4.29143,-0.00550155,5.99438e-05,-7.08466e-08,2.68686e-11,-11522.2,2.66679], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.04666,0.0153539,-5.47039e-06,8.77827e-10,-5.23168e-14,-12447.3,-0.968698], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 5,
    label = "C3H4",
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
            NASAPolynomial(coeffs=[2.61304,0.0121226,1.85399e-05,-3.45251e-08,1.53351e-11,21541.6,10.2261], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.31687,0.0111337,-3.96294e-06,6.35642e-10,-3.78755e-14,20117.5,-10.9958], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 6,
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
            NASAPolynomial(coeffs=[1.45752,0.0211423,4.0468e-06,-1.6319e-08,7.04752e-12,1074.02,17.3995], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.7214,0.0149318,-4.96524e-06,7.25108e-10,-3.80015e-14,-924.531,-12.1556], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    index = 7,
    label = "C4H2",
    molecule = 
"""
1 C u0 p0 c0 {3,T} {5,S}
2 C u0 p0 c0 {4,T} {6,S}
3 C u0 p0 c0 {1,T} {4,S}
4 C u0 p0 c0 {2,T} {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.395185,0.0519558,-9.17866e-05,8.05239e-08,-2.69171e-11,51451.7,20.9691], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.667,0.00671664,-2.3545e-06,3.73831e-10,-2.21189e-14,49856.9,-21.1142], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 8,
    label = "C4H4",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {5,S}
2 C u0 p0 c0 {1,T} {4,S}
3 C u0 p0 c0 {4,D} {6,S} {7,S}
4 C u0 p0 c0 {2,S} {3,D} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.37369,0.0288801,-1.46864e-05,-3.91045e-09,4.78134e-12,33063.3,17.5941], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.98456,0.0120559,-4.23587e-06,6.73646e-10,-3.9906e-14,31199.3,-16.7959], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 9,
    label = "C4H6",
    molecule = 
"""
1  C u0 p0 c0 {3,D} {5,S} {6,S}
2  C u0 p0 c0 {4,D} {7,S} {8,S}
3  C u0 p0 c0 {1,D} {4,S} {9,S}
4  C u0 p0 c0 {2,D} {3,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.106,0.00505576,5.83885e-05,-8.0595e-08,3.27448e-11,11509.2,8.42978], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.62637,0.0172523,-6.09185e-06,9.708e-10,-5.7617e-14,9553.06,-14.8325], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 10,
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

""",
)

entry(
    index = 11,
    label = "C2",
    molecule = 
"""
multiplicity 3
1 C u1 p0 c0 {2,T}
2 C u1 p0 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.864706,0.0393531,-0.000119818,1.39081e-07,-5.52055e-11,98731.3,11.5301], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.79137,0.000516505,-2.5487e-08,-8.22636e-12,1.00862e-15,99023.1,2.81518], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 12,
    label = "H2O",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.19864,-0.0020364,6.52034e-06,-5.48793e-09,1.77197e-12,-30293.7,-0.849009], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.67704,0.00297318,-7.73769e-07,9.44335e-11,-4.269e-15,-29885.9,6.88255], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 13,
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
            NASAPolynomial(coeffs=[4.31515,-0.000847391,1.76404e-05,-2.26763e-08,9.0895e-12,-17706.7,3.27373], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.57977,0.00405326,-1.29845e-06,1.98211e-10,-1.13969e-14,-18007.2,0.664971], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 14,
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

""",
)

entry(
    index = 15,
    label = "CO2",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
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

""",
)

entry(
    index = 16,
    label = "CH2O",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.7937,-0.00990815,3.73215e-05,-3.79279e-08,1.3177e-11,-14309,0.602887], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.16948,0.00619327,-2.2506e-06,3.65982e-10,-2.20154e-14,-14478.4,6.04235], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 17,
    label = "CH2CO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.14012,0.0180884,-1.73242e-05,9.27675e-09,-1.9915e-12,-7043.05,12.1987], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.75779,0.00634965,-2.25844e-06,3.62085e-10,-2.1569e-14,-7978.61,-6.1064], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 18,
    label = "CH3CHO",
    molecule = 
"""
1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.72946,-0.00319329,4.75349e-05,-5.74586e-08,2.19311e-11,-21572.9,4.10302], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.40411,0.0117231,-4.22631e-06,6.83725e-10,-4.09849e-14,-22593.1,-3.48079], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 19,
    label = "C",
    molecule = 
"""
1 C u0 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.55424,-0.000321538,7.33792e-07,-7.32235e-10,2.66521e-13,85442.7,4.53131], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.60558,-0.000195934,1.06737e-07,-1.64239e-11,8.18706e-16,85411.7,4.19239], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 20,
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

""",
)

entry(
    index = 21,
    label = "CH",
    molecule = 
"""
multiplicity 2
1 C u1 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48976,0.000324322,-1.68998e-06,3.16284e-09,-1.40618e-12,70660.8,2.08428], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.52094,0.00176536,-4.61477e-07,5.92897e-11,-3.34745e-15,70994.9,7.40518], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 22,
    label = "CH2",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71758,0.00127391,2.17347e-06,-3.48858e-09,1.65209e-12,45872.4,1.75298], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.14632,0.00303671,-9.96474e-07,1.50484e-10,-8.57336e-15,46041.3,4.72342], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    label = "CH2(S)",
    molecule = 
"""
1 C u0 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.19331,-0.00233105,8.15676e-06,-6.62986e-09,1.93233e-12,50366.2,-0.746734], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.13502,0.00289594,-8.16668e-07,1.13573e-10,-6.36263e-15,50504.1,4.06031], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    label = "CH3",
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
    index = 25,
    label = "C2H",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.9018,0.013286,-2.80508e-05,2.89301e-08,-1.07447e-11,67117.1,6.17235], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.6646,0.00382189,-1.36509e-06,2.13254e-10,-1.23099e-14,67223.9,3.91355], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 26,
    label = "C2H3",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {3,S}
2 C u0 p0 c0 {1,D} {4,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.36378,0.000265766,2.79621e-05,-3.72987e-08,1.5159e-11,34475,7.9151], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.15027,0.00754021,-2.62998e-06,4.15974e-10,-2.45408e-14,33856.6,1.72812], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 27,
    label = "C2H5",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
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
    index = 28,
    label = "C3H2",
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
            NASAPolynomial(coeffs=[3.18167,-0.000337612,3.95344e-05,-5.49792e-08,2.28335e-11,56181.7,9.06482], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.69446,0.00653822,-2.35907e-06,3.82037e-10,-2.29227e-14,54926.4,-6.96164], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 29,
    label = "H2CCCH",
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
            NASAPolynomial(coeffs=[1.35111,0.0327411,-4.73827e-05,3.7631e-08,-1.18541e-11,39266.4,15.2059], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.14222,0.00761902,-2.6746e-06,4.24915e-10,-2.51475e-14,38069.3,-12.5848], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 30,
    label = "H2CCCCH",
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
            NASAPolynomial(coeffs=[2.41732,0.0241048,-1.28135e-05,-2.86062e-09,3.91945e-12,56506.5,14.4711], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.47621,0.00887823,-3.03284e-06,4.73583e-10,-2.77166e-14,54756.5,-17.1706], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "C3H5",
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
            NASAPolynomial(coeffs=[3.11351,0.00990764,3.22193e-05,-4.96733e-08,2.06446e-11,18261.8,10.6902], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.41037,0.0127002,-4.60068e-06,7.4681e-10,-4.4876e-14,16374.9,-15.0083], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 32,
    label = "i-C4H5",
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
            NASAPolynomial(coeffs=[4.41576,0.0136824,1.76533e-05,-3.06168e-08,1.2785e-11,34787.1,6.3967], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.62619,0.0147322,-5.22512e-06,8.36085e-10,-4.97358e-14,33381.6,-12.6664], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 33,
    label = "O",
    molecule = 
"""
multiplicity 3
1 O u2 p2 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.16827,-0.00327932,6.64306e-06,-6.12807e-09,2.11266e-12,29122.3,2.05193], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.54364,-2.73162e-05,-4.1903e-09,4.95482e-12,-4.79554e-16,29226,4.92229], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 34,
    label = "OH",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99198,-0.00240107,4.61664e-06,-3.87916e-09,1.3632e-12,3368.9,-0.103998], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.83853,0.00110741,-2.94e-07,4.20699e-11,-2.4229e-15,3697.81,5.84495], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    label = "HO2",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.30179,-0.00474902,2.1158e-05,-2.4276e-08,9.29207e-12,294.809,3.7167], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.17227,0.00188121,-3.46293e-07,1.94685e-11,1.76092e-16,61.8189,2.9578], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 36,
    label = "HCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.23755,-0.00332075,1.4003e-05,-1.3424e-08,4.37416e-12,3872.41,3.30835], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.92002,0.00252279,-6.71004e-07,1.05616e-10,-7.43798e-15,3653.43,3.58077], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 37,
    label = "CH3O",
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
            NASAPolynomial(coeffs=[3.71181,-0.00280463,3.76551e-05,-4.73072e-08,1.86588e-11,1307.72,6.57241], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.75779,0.00744142,-2.69705e-06,4.38091e-10,-2.63537e-14,390.139,-1.9668], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 38,
    label = "CH2OH",
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
            NASAPolynomial(coeffs=[4.47832,-0.0013507,2.78484e-05,-3.64867e-08,1.47907e-11,-3524.77,3.30912], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.09312,0.00594759,-2.06497e-06,3.23007e-10,-1.88125e-14,-4058.13,-1.84691], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 39,
    label = "HCCO",
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
            NASAPolynomial(coeffs=[2.33501,0.0170101,-2.20189e-05,1.54064e-08,-4.34551e-12,20050.3,11.9767], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.8469,0.0036406,-1.2959e-06,2.07969e-10,-1.24e-14,19248.5,-5.29165], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 40,
    label = "CH3CO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.16343,-0.000232616,3.42678e-05,-4.41052e-08,1.72756e-11,-2657.45,7.34683], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.94477,0.00786672,-2.88659e-06,4.72709e-10,-2.85999e-14,-3787.31,-5.01368], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 41,
    label = "N2",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.29868,0.00140824,-3.96322e-06,5.64152e-09,-2.44485e-12,-1020.9,3.95037], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.92664,0.00148798,-5.68476e-07,1.0097e-10,-6.75335e-15,-922.798,5.98053], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    index = 42,
    label = "AR",
    molecule = 
"""
1 Ar u0 p4 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.366], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,4.366], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    index = 43,
    label = "A1",
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
            NASAPolynomial(coeffs=[0.504819,0.0185021,7.38346e-05,-1.18136e-07,5.0721e-11,8552.48,21.6413], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.081,0.0207177,-7.52146e-06,1.22321e-09,-7.36091e-14,4306.41,-40.0413], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 44,
    label = "nC4H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u1 p0 c0 {1,S} {3,S} {8,S}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {3,D} {10,S} {11,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.54747,0.00463771,6.6134e-05,-8.97457e-08,3.61716e-11,14384.3,7.30313], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.08107,0.0195527,-6.93149e-06,1.10889e-09,-6.59584e-14,12282.3,-16.7138], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 45,
    label = "C4H8",
    molecule = 
"""
1  C u0 p0 c0 {2,D} {5,S} {6,S}
2  C u0 p0 c0 {1,D} {4,S} {7,S}
3  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.18114,0.0308534,5.08652e-06,-2.46549e-08,1.11102e-11,-1790.4,21.0756], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.05358,0.0343505,-1.58832e-05,3.30897e-09,-2.5361e-13,-2139.72,15.5564], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    index = 47,
    label = "A1-",
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
            NASAPolynomial(coeffs=[0.210307,0.0204746,5.89743e-05,-1.01534e-07,4.47106e-11,39546.9,25.291], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.8445,0.0173212,-6.29233e-06,1.0237e-09,-6.16217e-14,35559.8,-35.3735], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    label = "C6H5OH",
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
            NASAPolynomial(coeffs=[-0.290979,0.0408562,2.42829e-05,-7.14478e-08,3.46002e-11,-13413,26.8746], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.1552,0.019935,-7.1822e-06,1.16229e-09,-6.97147e-14,-18128.7,-51.7985], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 49,
    label = "C6H5O",
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
            NASAPolynomial(coeffs=[-0.466204,0.0413444,1.32413e-05,-5.72873e-08,2.89764e-11,4778.58,27.699], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.7222,0.0174689,-6.35505e-06,1.03492e-09,-6.23411e-14,287.275,-48.8182], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 50,
    label = "C5H5",
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
            NASAPolynomial(coeffs=[-0.959028,0.0313968,2.67241e-05,-6.89422e-08,3.3302e-11,30779.4,29.0728], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.8441,0.0153928,-5.56304e-06,9.01894e-10,-5.41566e-14,26950.9,-35.255], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 51,
    label = "C5H6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,D} {6,S}
2  C u0 p0 c0 {1,S} {3,D} {7,S}
3  C u0 p0 c0 {2,D} {5,S} {8,S}
4  C u0 p0 c0 {1,D} {5,S} {9,S}
5  C u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.86109,0.014804,7.21089e-05,-1.13381e-07,4.869e-11,14801.8,21.3535], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.97578,0.0189055,-6.84115e-06,1.10993e-09,-6.66802e-14,11081.7,-32.2095], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 52,
    label = "A1C2H",
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
            NASAPolynomial(coeffs=[-2.74708,0.0778284,-6.6971e-05,2.37972e-08,-8.4328e-13,36113.1,35.4221], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.3583,0.0211974,-7.65817e-06,1.24135e-09,-7.45328e-14,31037.5,-62.252], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 53,
    label = "C7H8",
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
            NASAPolynomial(coeffs=[1.61527,0.0210994,8.5366e-05,-1.32611e-07,5.59566e-11,4075.63,20.2822], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.94,0.0266913,-9.68385e-06,1.57386e-09,-9.46636e-14,-697.649,-46.7288], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 54,
    label = "A1C2H3",
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
            NASAPolynomial(coeffs=[-10.7177,0.126667,-0.000177625,1.4344e-07,-4.76166e-11,16597.1,71.5263], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.1393,0.0242108,-7.26784e-06,1.13923e-09,-7.29849e-14,10249.3,-61.1694], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    label = "A1C2H3*",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {4,S} {8,B}
2  C u0 p0 c0 {1,B} {3,B} {12,S}
3  C u0 p0 c0 {2,B} {5,B} {11,S}
4  C u0 p0 c0 {1,S} {7,D} {9,S}
5  C u0 p0 c0 {3,B} {6,B} {10,S}
6  C u0 p0 c0 {5,B} {8,B} {13,S}
7  C u0 p0 c0 {4,D} {14,S} {15,S}
8  C u1 p0 c0 {1,B} {6,B}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.88687,0.068169,-3.48059e-05,-5.64103e-09,8.07148e-12,44941.4,45.9432], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.5636,0.0302108,-1.15456e-05,1.73023e-09,-5.23798e-14,40498.5,-34.883], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    label = "n-C8H7",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {7,S}
2  C u0 p0 c0 {1,B} {4,B} {9,S}
3  C u0 p0 c0 {1,B} {6,B} {13,S}
4  C u0 p0 c0 {2,B} {5,B} {10,S}
5  C u0 p0 c0 {4,B} {6,B} {11,S}
6  C u0 p0 c0 {3,B} {5,B} {12,S}
7  C u0 p0 c0 {1,S} {8,D} {14,S}
8  C u1 p0 c0 {7,D} {15,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.885284,0.0561565,1.166e-05,-6.99146e-08,3.6359e-11,44585.1,29.7497], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.0458,0.0221499,-8.05083e-06,1.30961e-09,-7.88616e-14,38709.1,-71.7918], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    label = "C7H7",
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
            NASAPolynomial(coeffs=[0.481115,0.0385128,3.28615e-05,-7.69727e-08,3.54231e-11,23307,23.5488], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.044,0.0234939,-8.53754e-06,1.38908e-09,-8.36144e-14,18564.2,-51.6656], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    label = "A1C2H-",
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
            NASAPolynomial(coeffs=[-4.44959,0.0769951,-6.6617e-05,2.50387e-08,-1.97566e-12,65225.9,44.4279], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[12.3595,0.0254534,-1.06066e-05,1.89146e-09,-1.06306e-13,60930.5,-40.9002], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    label = "A2",
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
            NASAPolynomial(coeffs=[-1.04919,0.0462971,7.07592e-05,-1.38408e-07,6.20475e-11,15984.9,30.2122], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.613,0.0304494,-1.11225e-05,1.81615e-09,-1.09601e-13,8915.79,-80.023], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 60,
    label = "A2-",
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
            NASAPolynomial(coeffs=[-1.8956,0.0583077,2.79389e-05,-9.14375e-08,4.46422e-11,45541,35.2453], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.3535,0.0277474,-1.00886e-05,1.6423e-09,-9.89002e-14,38926.1,-74.8978], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 61,
    label = "INDENE",
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
            NASAPolynomial(coeffs=[-0.681903,0.0416587,7.07412e-05,-1.34309e-07,5.99158e-11,17705,29.7814], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.3187,0.0289828,-1.06051e-05,1.73346e-09,-1.04679e-13,11151.4,-71.5553], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 62,
    label = "INDENYL",
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
            NASAPolynomial(coeffs=[-2.66987,0.0621772,1.5067e-05,-7.96457e-08,4.0919e-11,32387,37.8612], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[18.555,0.0250351,-9.14575e-06,1.49348e-09,-9.0133e-14,25721.2,-76.3003], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 63,
    label = "P2",
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
            NASAPolynomial(coeffs=[-4.07395,0.0869733,-4.23536e-06,-6.45645e-08,3.41502e-11,19406,44.7413], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[24.289,0.0340066,-1.17224e-05,1.77293e-09,-9.68125e-14,10287,-108.024], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    label = "P2-",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,B} {5,B}
2  C u0 p0 c0 {1,S} {3,B} {10,B}
3  C u0 p0 c0 {2,B} {9,B} {17,S}
4  C u0 p0 c0 {1,B} {7,B} {18,S}
5  C u0 p0 c0 {1,B} {8,B} {19,S}
6  C u0 p0 c0 {7,B} {8,B} {14,S}
7  C u0 p0 c0 {4,B} {6,B} {15,S}
8  C u0 p0 c0 {5,B} {6,B} {16,S}
9  C u0 p0 c0 {3,B} {11,B} {13,S}
10 C u0 p0 c0 {2,B} {12,B} {21,S}
11 C u0 p0 c0 {9,B} {12,B} {20,S}
12 C u1 p0 c0 {10,B} {11,B}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {8,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.13762,0.0822173,-4.01714e-06,-6.08098e-08,3.20745e-11,48868.8,42.7304], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[23.8513,0.0319602,-1.10767e-05,1.68478e-09,-9.26412e-14,40171.3,-102.705], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    label = "A2C2H*",
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
            NASAPolynomial(coeffs=[-6.25389,0.114753,-0.000105431,4.79127e-08,-7.92157e-12,73249.2,51.9413], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.3715,0.0499657,-2.62269e-05,6.59494e-09,-6.45885e-13,68490.4,-46.4872], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 66,
    label = "A2R5",
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
            NASAPolynomial(coeffs=[-2.81264,0.0704681,3.15342e-05,-1.05176e-07,5.08714e-11,28846.3,37.5756], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.3184,0.0390205,-1.63353e-05,3.10042e-09,-2.19199e-13,21544.5,-83.2372], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    label = "A2C2H",
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
            NASAPolynomial(coeffs=[-2.59169,0.0863306,-1.76591e-05,-5.26006e-08,3.15925e-11,42772.1,37.3575], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[23.4108,0.0312979,-1.13777e-05,1.85218e-09,-1.11547e-13,34919.7,-100.595], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 68,
    label = "A2R5-",
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
            NASAPolynomial(coeffs=[-7.33803,0.111966,-9.32829e-05,3.58663e-08,-4.26602e-12,58059.8,57.3507], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.9534,0.0523861,-2.76953e-05,6.98584e-09,-6.84939e-13,53199.5,-40.3925], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 69,
    label = "A3",
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
            NASAPolynomial(coeffs=[-3.36467,0.0850733,3.75311e-05,-1.26645e-07,6.14457e-11,22019.9,40.5962], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[26.6025,0.0397697,-1.4572e-05,2.38433e-09,-1.44095e-13,12132.8,-122.667], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 70,
    label = "A3-",
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
            NASAPolynomial(coeffs=[-10.893,0.141537,-0.000114206,3.5771e-08,0,52113.6,73.7137], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[26.8173,0.0376936,-1.45586e-05,2.58487e-09,-1.73198e-13,41440.6,-121.548], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    label = "A4",
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
            NASAPolynomial(coeffs=[-4.04203,0.0915497,5.14433e-05,-1.52766e-07,7.30875e-11,24094.2,43.6653], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[29.91,0.0426681,-1.57338e-05,2.58517e-09,-1.5668e-13,12786.5,-141.87], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    label = "A4-",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {4,B} {5,B}
2  C u0 p0 c0 {1,B} {3,B} {6,B}
3  C u0 p0 c0 {2,B} {7,B} {12,B}
4  C u0 p0 c0 {1,B} {8,B} {9,B}
5  C u0 p0 c0 {1,B} {10,B} {11,B}
6  C u0 p0 c0 {2,B} {13,B} {16,B}
7  C u0 p0 c0 {3,B} {8,B} {18,S}
8  C u0 p0 c0 {4,B} {7,B} {19,S}
9  C u0 p0 c0 {4,B} {14,B} {20,S}
10 C u0 p0 c0 {5,B} {14,B} {22,S}
11 C u0 p0 c0 {5,B} {13,B} {23,S}
12 C u0 p0 c0 {3,B} {15,B} {17,S}
13 C u0 p0 c0 {6,B} {11,B} {24,S}
14 C u0 p0 c0 {9,B} {10,B} {21,S}
15 C u0 p0 c0 {12,B} {16,B} {25,S}
16 C u1 p0 c0 {6,B} {15,B}
17 H u0 p0 c0 {12,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {14,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {13,S}
25 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.70729,0.11331,-7.2442e-05,2.13864e-08,-2.29814e-12,55126.7,34.3199], Tmin=(298,'K'), Tmax=(1370,'K')),
            NASAPolynomial(coeffs=[35.258,0.0337799,-1.20577e-05,1.92626e-09,-1.14006e-13,41022.4,-172.843], Tmin=(1370,'K'), Tmax=(5000,'K')),
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
    label = "C18H12",
    molecule = 
"""
1  C u0 p0 c0 {4,B} {5,B} {7,B}
2  C u0 p0 c0 {3,B} {4,B} {10,B}
3  C u0 p0 c0 {2,B} {6,B} {11,B}
4  C u0 p0 c0 {1,B} {2,B} {14,B}
5  C u0 p0 c0 {1,B} {8,B} {9,B}
6  C u0 p0 c0 {3,B} {12,B} {13,B}
7  C u0 p0 c0 {1,B} {16,B} {21,S}
8  C u0 p0 c0 {5,B} {15,B} {22,S}
9  C u0 p0 c0 {5,B} {10,B} {23,S}
10 C u0 p0 c0 {2,B} {9,B} {24,S}
11 C u0 p0 c0 {3,B} {17,B} {25,S}
12 C u0 p0 c0 {6,B} {18,B} {28,S}
13 C u0 p0 c0 {6,B} {14,B} {29,S}
14 C u0 p0 c0 {4,B} {13,B} {30,S}
15 C u0 p0 c0 {8,B} {16,B} {19,S}
16 C u0 p0 c0 {7,B} {15,B} {20,S}
17 C u0 p0 c0 {11,B} {18,B} {26,S}
18 C u0 p0 c0 {12,B} {17,B} {27,S}
19 H u0 p0 c0 {15,S}
20 H u0 p0 c0 {16,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {17,S}
27 H u0 p0 c0 {18,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {13,S}
30 H u0 p0 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1263,0.106385,-4.827e-05,5.22817e-09,1.05962e-12,26964.4,6.40603], Tmin=(298,'K'), Tmax=(1673,'K')),
            NASAPolynomial(coeffs=[33.1662,0.0508796,-1.87182e-05,3.06105e-09,-1.84366e-13,15764.2,-159.238], Tmin=(1673,'K'), Tmax=(5000,'K')),
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
    label = "C18H11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,B} {5,B} {7,B}
2  C u0 p0 c0 {3,B} {4,B} {10,B}
3  C u0 p0 c0 {1,B} {2,B} {17,B}
4  C u0 p0 c0 {2,B} {6,B} {11,B}
5  C u0 p0 c0 {1,B} {8,B} {9,B}
6  C u0 p0 c0 {4,B} {12,B} {18,B}
7  C u0 p0 c0 {1,B} {13,B} {19,S}
8  C u0 p0 c0 {5,B} {14,B} {22,S}
9  C u0 p0 c0 {5,B} {10,B} {23,S}
10 C u0 p0 c0 {2,B} {9,B} {24,S}
11 C u0 p0 c0 {4,B} {15,B} {25,S}
12 C u0 p0 c0 {6,B} {16,B} {28,S}
13 C u0 p0 c0 {7,B} {14,B} {20,S}
14 C u0 p0 c0 {8,B} {13,B} {21,S}
15 C u0 p0 c0 {11,B} {16,B} {26,S}
16 C u0 p0 c0 {12,B} {15,B} {27,S}
17 C u0 p0 c0 {3,B} {18,B} {29,S}
18 C u1 p0 c0 {6,B} {17,B}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {13,S}
21 H u0 p0 c0 {14,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {15,S}
27 H u0 p0 c0 {16,S}
28 H u0 p0 c0 {12,S}
29 H u0 p0 c0 {17,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.63557,0.0820164,-1.33889e-05,-1.71944e-08,6.31097e-12,56658.2,-12.1249], Tmin=(298,'K'), Tmax=(1553,'K')),
            NASAPolynomial(coeffs=[38.0928,0.0414889,-1.46997e-05,2.33682e-09,-1.37837e-13,43115.6,-186.41], Tmin=(1553,'K'), Tmax=(5000,'K')),
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
    label = "A3C2H",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {7,B}
2  C u0 p0 c0 {1,B} {4,B} {11,B}
3  C u0 p0 c0 {1,B} {6,B} {8,B}
4  C u0 p0 c0 {2,B} {9,B} {10,B}
5  C u0 p0 c0 {6,B} {12,B} {15,S}
6  C u0 p0 c0 {3,B} {5,B} {25,S}
7  C u0 p0 c0 {1,B} {12,B} {18,S}
8  C u0 p0 c0 {3,B} {9,B} {19,S}
9  C u0 p0 c0 {4,B} {8,B} {20,S}
10 C u0 p0 c0 {4,B} {13,B} {21,S}
11 C u0 p0 c0 {2,B} {14,B} {24,S}
12 C u0 p0 c0 {5,B} {7,B} {17,S}
13 C u0 p0 c0 {10,B} {14,B} {22,S}
14 C u0 p0 c0 {11,B} {13,B} {23,S}
15 C u0 p0 c0 {5,S} {16,T}
16 C u0 p0 c0 {15,T} {26,S}
17 H u0 p0 c0 {12,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {13,S}
23 H u0 p0 c0 {14,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {6,S}
26 H u0 p0 c0 {16,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-11.6027,0.168244,-0.00016432,8.63944e-08,-1.93106e-11,52172.8,75.5154], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[52.1651,-0.0131973,3.43531e-05,-1.62839e-08,2.36774e-12,34235.1,-254.067], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 76,
    label = "A3C2H*",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {4,B} {7,B}
2  C u0 p0 c0 {1,B} {6,B} {8,B}
3  C u0 p0 c0 {4,B} {9,B} {10,B}
4  C u0 p0 c0 {1,B} {3,B} {14,B}
5  C u0 p0 c0 {6,B} {11,B} {15,S}
6  C u0 p0 c0 {2,B} {5,B} {23,S}
7  C u0 p0 c0 {1,B} {11,B} {18,S}
8  C u0 p0 c0 {2,B} {9,B} {19,S}
9  C u0 p0 c0 {3,B} {8,B} {20,S}
10 C u0 p0 c0 {3,B} {12,B} {21,S}
11 C u0 p0 c0 {5,B} {7,B} {17,S}
12 C u0 p0 c0 {10,B} {13,B} {22,S}
13 C u0 p0 c0 {12,B} {14,B} {24,S}
14 C u1 p0 c0 {4,B} {13,B}
15 C u0 p0 c0 {5,S} {16,T}
16 C u0 p0 c0 {15,T} {25,S}
17 H u0 p0 c0 {11,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {12,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {13,S}
25 H u0 p0 c0 {16,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-10.5579,0.169545,-0.000186995,1.20985e-07,-3.56159e-11,82880.6,70.9148], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[44.2043,0.0100322,5.84987e-06,-3.10823e-09,3.90443e-13,67415.1,-211.916], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 77,
    label = "C4H",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {4,S}
3 C u0 p0 c0 {4,T} {5,S}
4 C u0 p0 c0 {2,S} {3,T}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.32107,0.0385628,-7.13432e-05,6.532e-08,-2.2607e-11,95021.6,15.5546], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.76809,0.00498504,-1.76488e-06,2.82174e-10,-1.67796e-14,93912.1,-14.1596], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 78,
    label = "C4",
    molecule = 
"""
multiplicity 3
1 C u1 p0 c0 {3,T}
2 C u1 p0 c0 {4,T}
3 C u0 p0 c0 {1,T} {4,S}
4 C u0 p0 c0 {2,T} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.32278,0.0202592,-3.73452e-05,3.56859e-08,-1.27719e-11,122724,6.8098], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.63077,0.00483138,-1.50417e-06,2.02895e-10,-1.00361e-14,122501,-2.98873], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 79,
    label = "C6H2",
    molecule = 
"""
1 C u0 p0 c0 {3,T} {7,S}
2 C u0 p0 c0 {4,T} {8,S}
3 C u0 p0 c0 {1,T} {5,S}
4 C u0 p0 c0 {2,T} {6,S}
5 C u0 p0 c0 {3,S} {6,T}
6 C u0 p0 c0 {4,S} {5,T}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
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
    index = 80,
    label = "C8H2",
    molecule = 
"""
1  C u0 p0 c0 {3,T} {9,S}
2  C u0 p0 c0 {4,T} {10,S}
3  C u0 p0 c0 {1,T} {5,S}
4  C u0 p0 c0 {2,T} {6,S}
5  C u0 p0 c0 {3,S} {7,T}
6  C u0 p0 c0 {4,S} {8,T}
7  C u0 p0 c0 {5,T} {8,S}
8  C u0 p0 c0 {6,T} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.24704,0.0783925,-0.000124161,9.83817e-08,-3.00639e-11,109429,16.0482], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.0075,0.00936568,-3.04857e-06,4.76535e-10,-2.9169e-14,106280,-59.2246], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    label = "C6H",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 C u0 p0 c0 {1,T} {4,S}
3 C u0 p0 c0 {5,T} {7,S}
4 C u0 p0 c0 {2,S} {6,T}
5 C u0 p0 c0 {3,T} {6,S}
6 C u0 p0 c0 {4,T} {5,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.01101,0.059782,-0.000107739,9.61966e-08,-3.26813e-11,122616,17.9981], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.3618,0.00751578,-2.72161e-06,4.39175e-10,-2.6218e-14,120801,-29.9898], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 82,
    label = "C8H",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {3,T}
2 C u0 p0 c0 {4,T} {9,S}
3 C u0 p0 c0 {1,T} {5,S}
4 C u0 p0 c0 {2,T} {6,S}
5 C u0 p0 c0 {3,S} {7,T}
6 C u0 p0 c0 {4,S} {8,T}
7 C u0 p0 c0 {5,T} {8,S}
8 C u0 p0 c0 {6,T} {7,S}
9 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45668,0.0652204,-9.81414e-05,7.20468e-08,-2.0447e-11,136568,7.77198], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.4222,0.00664137,-2.25572e-06,3.66573e-10,-2.31887e-14,133765,-59.2751], Tmin=(1000,'K'), Tmax=(5000,'K')),
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
    label = "A4C2H",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {3,B} {6,B}
2  C u0 p0 c0 {1,B} {4,B} {5,B}
3  C u0 p0 c0 {1,B} {8,B} {10,B}
4  C u0 p0 c0 {2,B} {11,B} {12,B}
5  C u0 p0 c0 {2,B} {13,B} {14,B}
6  C u0 p0 c0 {1,B} {9,B} {15,B}
7  C u0 p0 c0 {8,B} {9,B} {17,S}
8  C u0 p0 c0 {3,B} {7,B} {19,S}
9  C u0 p0 c0 {6,B} {7,B} {27,S}
10 C u0 p0 c0 {3,B} {11,B} {20,S}
11 C u0 p0 c0 {4,B} {10,B} {21,S}
12 C u0 p0 c0 {4,B} {16,B} {22,S}
13 C u0 p0 c0 {5,B} {16,B} {24,S}
14 C u0 p0 c0 {5,B} {15,B} {25,S}
15 C u0 p0 c0 {6,B} {14,B} {26,S}
16 C u0 p0 c0 {12,B} {13,B} {23,S}
17 C u0 p0 c0 {7,S} {18,T}
18 C u0 p0 c0 {17,T} {28,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {11,S}
22 H u0 p0 c0 {12,S}
23 H u0 p0 c0 {16,S}
24 H u0 p0 c0 {13,S}
25 H u0 p0 c0 {14,S}
26 H u0 p0 c0 {15,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {18,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.66685,0.129147,-8.88321e-05,2.96511e-08,-3.87601e-12,50437,29.7035], Tmin=(298,'K'), Tmax=(1380,'K')),
            NASAPolynomial(coeffs=[40.055,0.0370781,-1.31322e-05,2.08714e-09,-1.2309e-13,35449.2,-196.221], Tmin=(1380,'K'), Tmax=(5000,'K')),
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
    label = "A4C2H*",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {5,B}
2  C u0 p0 c0 {1,B} {4,B} {6,B}
3  C u0 p0 c0 {1,B} {11,B} {12,B}
4  C u0 p0 c0 {2,B} {8,B} {13,B}
5  C u0 p0 c0 {1,B} {10,B} {15,B}
6  C u0 p0 c0 {2,B} {9,B} {16,B}
7  C u0 p0 c0 {8,B} {9,B} {17,S}
8  C u0 p0 c0 {4,B} {7,B} {25,S}
9  C u0 p0 c0 {6,B} {7,B} {19,S}
10 C u0 p0 c0 {5,B} {14,B} {20,S}
11 C u0 p0 c0 {3,B} {14,B} {22,S}
12 C u0 p0 c0 {3,B} {13,B} {23,S}
13 C u0 p0 c0 {4,B} {12,B} {24,S}
14 C u0 p0 c0 {10,B} {11,B} {21,S}
15 C u0 p0 c0 {5,B} {16,B} {26,S}
16 C u1 p0 c0 {6,B} {15,B}
17 C u0 p0 c0 {7,S} {18,T}
18 C u0 p0 c0 {17,T} {27,S}
19 H u0 p0 c0 {9,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {14,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {12,S}
24 H u0 p0 c0 {13,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {15,S}
27 H u0 p0 c0 {18,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.446465,0.121678,-8.16503e-05,2.6141e-08,-3.21316e-12,80569.8,25.9458], Tmin=(298,'K'), Tmax=(1376,'K')),
            NASAPolynomial(coeffs=[39.5503,0.0350981,-1.24815e-05,1.98905e-09,-1.17523e-13,66021.5,-191.256], Tmin=(1376,'K'), Tmax=(5000,'K')),
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
    index = 85,
    label = "BAPYR*S",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {4,B} {7,B}
2  C u0 p0 c0 {1,B} {6,B} {8,B}
3  C u0 p0 c0 {4,B} {5,B} {11,B}
4  C u0 p0 c0 {1,B} {3,B} {12,B}
5  C u0 p0 c0 {3,B} {9,B} {10,B}
6  C u0 p0 c0 {2,B} {13,B} {14,B}
7  C u0 p0 c0 {1,B} {9,B} {19,B}
8  C u0 p0 c0 {2,B} {15,B} {20,B}
9  C u0 p0 c0 {5,B} {7,B} {21,S}
10 C u0 p0 c0 {5,B} {16,B} {22,S}
11 C u0 p0 c0 {3,B} {17,B} {25,S}
12 C u0 p0 c0 {4,B} {13,B} {26,S}
13 C u0 p0 c0 {6,B} {12,B} {27,S}
14 C u0 p0 c0 {6,B} {18,B} {28,S}
15 C u0 p0 c0 {8,B} {18,B} {30,S}
16 C u0 p0 c0 {10,B} {17,B} {23,S}
17 C u0 p0 c0 {11,B} {16,B} {24,S}
18 C u0 p0 c0 {14,B} {15,B} {29,S}
19 C u0 p0 c0 {7,B} {20,B} {31,S}
20 C u1 p0 c0 {8,B} {19,B}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {16,S}
24 H u0 p0 c0 {17,S}
25 H u0 p0 c0 {11,S}
26 H u0 p0 c0 {12,S}
27 H u0 p0 c0 {13,S}
28 H u0 p0 c0 {14,S}
29 H u0 p0 c0 {18,S}
30 H u0 p0 c0 {15,S}
31 H u0 p0 c0 {19,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.362587,0.130525,-7.53628e-05,1.75825e-08,-8.69472e-13,59986,23.2559], Tmin=(298,'K'), Tmax=(1367,'K')),
            NASAPolynomial(coeffs=[44.2865,0.0417446,-1.48863e-05,2.37663e-09,-1.40601e-13,42985.1,-221.959], Tmin=(1367,'K'), Tmax=(5000,'K')),
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
    label = "BGHIF",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {4,B} {8,B}
2  C u0 p0 c0 {1,B} {3,B} {7,B}
3  C u0 p0 c0 {2,B} {5,B} {6,B}
4  C u0 p0 c0 {1,B} {5,S} {9,B}
5  C u0 p0 c0 {3,B} {4,S} {10,B}
6  C u0 p0 c0 {3,B} {11,B} {12,B}
7  C u0 p0 c0 {2,B} {13,B} {14,B}
8  C u0 p0 c0 {1,B} {15,B} {16,B}
9  C u0 p0 c0 {4,B} {17,B} {20,S}
10 C u0 p0 c0 {5,B} {18,B} {21,S}
11 C u0 p0 c0 {6,B} {18,B} {23,S}
12 C u0 p0 c0 {6,B} {13,B} {24,S}
13 C u0 p0 c0 {7,B} {12,B} {25,S}
14 C u0 p0 c0 {7,B} {15,B} {26,S}
15 C u0 p0 c0 {8,B} {14,B} {27,S}
16 C u0 p0 c0 {8,B} {17,B} {28,S}
17 C u0 p0 c0 {9,B} {16,B} {19,S}
18 C u0 p0 c0 {10,B} {11,B} {22,S}
19 H u0 p0 c0 {17,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {18,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {12,S}
25 H u0 p0 c0 {13,S}
26 H u0 p0 c0 {14,S}
27 H u0 p0 c0 {15,S}
28 H u0 p0 c0 {16,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-13.5025,0.175273,-0.000152006,6.58323e-08,-1.13176e-11,40573.9,80.3624], Tmin=(298,'K'), Tmax=(1397,'K')),
            NASAPolynomial(coeffs=[40.3485,0.0360369,-1.25974e-05,1.98536e-09,-1.16421e-13,23391.7,-203.795], Tmin=(1397,'K'), Tmax=(5000,'K')),
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
    label = "BAPYR",
    molecule = 
"""
1  C u0 p0 c0 {2,B} {4,B} {6,B}
2  C u0 p0 c0 {1,B} {7,B} {8,B}
3  C u0 p0 c0 {4,B} {5,B} {10,B}
4  C u0 p0 c0 {1,B} {3,B} {17,B}
5  C u0 p0 c0 {3,B} {9,B} {11,B}
6  C u0 p0 c0 {1,B} {9,B} {12,B}
7  C u0 p0 c0 {2,B} {13,B} {14,B}
8  C u0 p0 c0 {2,B} {15,B} {16,B}
9  C u0 p0 c0 {5,B} {6,B} {25,S}
10 C u0 p0 c0 {3,B} {19,B} {23,S}
11 C u0 p0 c0 {5,B} {18,B} {24,S}
12 C u0 p0 c0 {6,B} {13,B} {26,S}
13 C u0 p0 c0 {7,B} {12,B} {27,S}
14 C u0 p0 c0 {7,B} {20,B} {28,S}
15 C u0 p0 c0 {8,B} {20,B} {30,S}
16 C u0 p0 c0 {8,B} {17,B} {31,S}
17 C u0 p0 c0 {4,B} {16,B} {32,S}
18 C u0 p0 c0 {11,B} {19,B} {21,S}
19 C u0 p0 c0 {10,B} {18,B} {22,S}
20 C u0 p0 c0 {14,B} {15,B} {29,S}
21 H u0 p0 c0 {18,S}
22 H u0 p0 c0 {19,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {12,S}
27 H u0 p0 c0 {13,S}
28 H u0 p0 c0 {14,S}
29 H u0 p0 c0 {20,S}
30 H u0 p0 c0 {15,S}
31 H u0 p0 c0 {16,S}
32 H u0 p0 c0 {17,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.08146,0.140317,-8.64401e-05,2.37334e-08,-2.15248e-12,29928.1,30.0065], Tmin=(298,'K'), Tmax=(1373,'K')),
            NASAPolynomial(coeffs=[44.6588,0.0438683,-1.55934e-05,2.48422e-09,-1.46749e-13,12460.6,-225.482], Tmin=(1373,'K'), Tmax=(5000,'K')),
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
    label = "A2CH3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
2  C u0 p0 c0 {1,S} {5,B} {6,B}
3  C u0 p0 c0 {4,B} {7,B} {8,B}
4  C u0 p0 c0 {3,B} {5,B} {9,B}
5  C u0 p0 c0 {2,B} {4,B} {21,S}
6  C u0 p0 c0 {2,B} {7,B} {15,S}
7  C u0 p0 c0 {3,B} {6,B} {16,S}
8  C u0 p0 c0 {3,B} {10,B} {17,S}
9  C u0 p0 c0 {4,B} {11,B} {20,S}
10 C u0 p0 c0 {8,B} {11,B} {18,S}
11 C u0 p0 c0 {9,B} {10,B} {19,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {10,S}
19 H u0 p0 c0 {11,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.03044,0.0603358,5.45656e-05,-1.22769e-07,5.54507e-11,11324.1,32.2971], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[21.7939,0.0360214,-1.33229e-05,2.19304e-09,-1.33071e-13,3162.61,-94.8675], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 89,
    label = "A2CH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {6,B} {7,B}
2  C u0 p0 c0 {1,B} {4,B} {8,B}
3  C u0 p0 c0 {4,B} {5,B} {11,S}
4  C u0 p0 c0 {2,B} {3,B} {18,S}
5  C u0 p0 c0 {3,B} {6,B} {12,S}
6  C u0 p0 c0 {1,B} {5,B} {13,S}
7  C u0 p0 c0 {1,B} {9,B} {14,S}
8  C u0 p0 c0 {2,B} {10,B} {17,S}
9  C u0 p0 c0 {7,B} {10,B} {15,S}
10 C u0 p0 c0 {8,B} {9,B} {16,S}
11 C u1 p0 c0 {3,S} {19,S} {20,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {9,S}
16 H u0 p0 c0 {10,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {11,S}
20 H u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.53234,0.073292,2.02975e-05,-9.36548e-08,4.70754e-11,30290.7,37.9639], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[21.8978,0.0326103,-1.18401e-05,1.92575e-09,-1.15903e-13,22457.1,-94.1051], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 90,
    label = "A3CH3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {7,B} {8,B}
3  C u0 p0 c0 {4,B} {5,B} {9,B}
4  C u0 p0 c0 {3,B} {6,B} {13,B}
5  C u0 p0 c0 {3,B} {7,B} {10,B}
6  C u0 p0 c0 {4,B} {11,B} {12,B}
7  C u0 p0 c0 {2,B} {5,B} {27,S}
8  C u0 p0 c0 {2,B} {9,B} {19,S}
9  C u0 p0 c0 {3,B} {8,B} {20,S}
10 C u0 p0 c0 {5,B} {11,B} {21,S}
11 C u0 p0 c0 {6,B} {10,B} {22,S}
12 C u0 p0 c0 {6,B} {14,B} {23,S}
13 C u0 p0 c0 {4,B} {15,B} {26,S}
14 C u0 p0 c0 {12,B} {15,B} {24,S}
15 C u0 p0 c0 {13,B} {14,B} {25,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {12,S}
24 H u0 p0 c0 {14,S}
25 H u0 p0 c0 {15,S}
26 H u0 p0 c0 {13,S}
27 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.245407,0.103437,-5.52428e-05,1.17709e-08,-4.92994e-13,16936.8,23.7077], Tmin=(298,'K'), Tmax=(2025,'K')),
            NASAPolynomial(coeffs=[28.6722,0.0457936,-1.67467e-05,2.72794e-09,-1.63863e-13,6778.59,-131.269], Tmin=(2025,'K'), Tmax=(5000,'K')),
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
    index = 91,
    label = "A3CH2",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,B} {3,B} {8,B}
2  C u0 p0 c0 {1,B} {4,B} {12,B}
3  C u0 p0 c0 {1,B} {6,B} {9,B}
4  C u0 p0 c0 {2,B} {10,B} {11,B}
5  C u0 p0 c0 {6,B} {7,B} {15,S}
6  C u0 p0 c0 {3,B} {5,B} {24,S}
7  C u0 p0 c0 {5,B} {8,B} {16,S}
8  C u0 p0 c0 {1,B} {7,B} {17,S}
9  C u0 p0 c0 {3,B} {10,B} {18,S}
10 C u0 p0 c0 {4,B} {9,B} {19,S}
11 C u0 p0 c0 {4,B} {13,B} {20,S}
12 C u0 p0 c0 {2,B} {14,B} {23,S}
13 C u0 p0 c0 {11,B} {14,B} {21,S}
14 C u0 p0 c0 {12,B} {13,B} {22,S}
15 C u1 p0 c0 {5,S} {25,S} {26,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {9,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {11,S}
21 H u0 p0 c0 {13,S}
22 H u0 p0 c0 {14,S}
23 H u0 p0 c0 {12,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {15,S}
26 H u0 p0 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.133784,0.104068,-5.92363e-05,1.4318e-08,-9.91637e-13,35945.9,23.5064], Tmin=(298,'K'), Tmax=(2030,'K')),
            NASAPolynomial(coeffs=[29.562,0.042459,-1.55842e-05,2.54481e-09,-1.53125e-13,25627.3,-136.22], Tmin=(2030,'K'), Tmax=(5000,'K')),
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
    index = 92,
    label = "CH3OH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 C u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
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
    shortDesc = u"""HE                      HE  1            0 0G 200.00    6000.00   1000.00    0 1
2.50000000E+00 0.00000000E+00 0.00000000E+00 0.00000000E+00 0.00000000E+00    2
-7.45375000E+02 9.28723974E-01 2.50000000E+00 0.00000000E+00 0.00000000E+00    3
0.00000000E+00 0.00000000E+00-7.45375000E+02 9.28723974E-01                   4""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "C2H5O2H",
    molecule = 
"""
1  O u0 p2 c0 {2,S} {5,S}
2  O u0 p2 c0 {1,S} {4,S}
3  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
4  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {3,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.3731,0.0104422,4.63855e-05,-7.02773e-08,2.93035e-11,-22936.2,8.30134], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.99512,0.0147312,-5.30621e-06,8.58443e-10,-5.14815e-14,-25385.1,-25.3504], Tmin=(1000,'K'), Tmax=(6000,'K')),
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
    index = 94,
    label = "CH2CH2OH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u1 p0 c0 {1,S} {6,S} {7,S}
3 O u0 p2 c0 {1,S} {8,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.17715,0.0248116,-1.503e-05,4.79007e-09,-6.40994e-13,-4953.69,22.0082], Tmin=(298,'K'), Tmax=(1391,'K')),
            NASAPolynomial(coeffs=[7.52245,0.0110493,-3.72576e-06,5.72827e-10,-3.30062e-14,-7293.37,-12.4961], Tmin=(1391,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""C2H5O                   H  5  O  1 C  2    0G 298.00   5000.00   1000.00     0 1
6.01143460E+00 1.21652190E-02-4.04496040E-06 5.90765880E-10-3.09695950E-14    2
-4.93669920E+03-6.79017980E+00 1.73025040E+00 1.69084890E-02 3.99962210E-06    3
-1.37111800E-08 5.76436030E-12-3.29224830E+03 1.73361150E+01                   4""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "CH3CHOH",
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
            NASAPolynomial(coeffs=[1.83975,0.0187789,-4.60544e-06,-2.13117e-09,9.43773e-13,-6295.95,20.1446], Tmin=(298,'K'), Tmax=(1553,'K')),
            NASAPolynomial(coeffs=[7.2657,0.0109589,-3.63663e-06,5.5366e-10,-3.17012e-14,-8643.71,-10.6823], Tmin=(1553,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (5000,'K'),
    ),
    shortDesc = u"""CH3CH2O                 H  5  O  1 C  2    0G 298.00   5000.00   1405.00     0 1
8.31182392E+00 1.03426319E-02-3.39186089E-06 5.12212617E-10-2.91601713E-14    2
-6.13097954E+03-2.13985581E+01-2.71296378E-01 2.98839812E-02-1.97090548E-05    3
6.37339893E-09-7.77965054E-13-3.16397196E+03 2.47706003E+01                   4""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "C2H5OH",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {4,S}
2 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.8587,-0.00374017,6.95554e-05,-8.86548e-08,3.51688e-11,-29996.1,4.80185], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.56244,0.0152042,-5.38968e-06,8.6225e-10,-5.12898e-14,-31525.6,-9.47302], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

