#!/usr/bin/env python
# encoding: utf-8

name = "NitrogenCurran"
shortDesc = u"Thermo data for emissions of nitrogen-containing compounds"
longDesc = u"""
Taken from:
John Bugler, Kieran P. Somers, John M. Simmie, Felix Guthe, and Henry J. Curran,
H. Phys. Chem. A, 2016
DOI: 10.1021/acs.jpca.6b05723

Several quantum-chemical composite methods (CBS-APNO, G3, and G4) were utilized to derive enthalpies of formation via the atomization method.
Entropies and heat capacities were calculated from traditional statistical thermodynamics, with oscillators treated as anharmonic based on 
o-vibrational property analyses carried out at the B3LYP/cc-pVTZ level of theory.

Paper: http://pubs.acs.org/doi/abs/10.1021/acs.jpca.6b05723
Supp Info: http://pubs.acs.org/doi/suppl/10.1021/acs.jpca.6b05723
"""
entry(
    index = 0,
    label = "C2H3NO2",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {6,S} {7,S}
2 C u0 p0 c0 {1,D} {3,S} {8,S}
3 N u0 p0 c+1 {2,S} {4,D} {5,S}
4 O u0 p2 c0 {3,D}
5 O u0 p3 c-1 {3,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.522506,0.031972,-2.14395e-05,5.01495e-09,3.99306e-13,2311.28,24.1729], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.85274,0.0196482,-1.04496e-05,2.6855e-09,-2.67622e-13,1195.37,2.03276], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 1,
    label = "C2H5NO2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  N u0 p0 c+1 {1,S} {9,S} {10,D}
4  H u0 p0 c0 {1,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  O u0 p3 c-1 {3,S}
10 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.804449,0.0302577,-5.72513e-06,-1.03205e-08,5.15313e-12,-14630.3,25.8115], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.35426,0.0281207,-1.46127e-05,3.66675e-09,-3.59228e-13,-15543.4,11.4946], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 2,
    label = "C2H5ONO2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  O u0 p2 c0 {2,S} {4,S}
4  N u0 p0 c+1 {3,S} {5,D} {6,S}
5  O u0 p2 c0 {4,D}
6  O u0 p3 c-1 {4,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.55981,0.0416273,-2.22411e-05,-6.8473e-11,2.75844e-12,-21509.4,20.7489], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.89094,0.0288116,-1.57806e-05,4.13331e-09,-4.19196e-13,-23001,-7.09794], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 3,
    label = "C2H5ONO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  O u0 p2 c0 {1,S} {4,S}
4  N u0 p1 c0 {3,S} {10,D}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.3535,0.0290188,-1.04499e-05,-3.67802e-09,2.72969e-12,-14163.2,11.3556], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.64637,0.0251803,-1.26916e-05,3.14938e-09,-3.10406e-13,-14888.4,-1.03944], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Data taken from the cis form, which is the more favorable conformation due to lower enthalpy of formation
Appears in original paper as C2H5ONOcis
Data for C2H5ONOtrans was ignored
""",
)

entry(
    index = 4,
    label = "CH2CN",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 C u0 p0 c0 {1,S} {5,T}
5 N u0 p1 c0 {4,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.4165,0.0168217,-1.54133e-05,8.32908e-09,-1.93672e-12,29742,11.638], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.06052,0.0100706,-5.02399e-06,1.22784e-09,-1.1765e-13,29421.9,3.7503], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 5,
    label = "CH2NH",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 N u0 p1 c0 {1,D} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.59904,0.00386561,1.31922e-05,-1.5423e-08,5.07645e-12,9678.57,10.8793], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.36087,0.0127895,-6.15038e-06,1.44318e-09,-1.32887e-13,9727.64,15.8599], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 6,
    label = "CH2NH2",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.26708,0.0275622,-3.78182e-05,2.75878e-08,-7.77379e-12,16982.9,16.9541], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.06946,0.00842221,-3.21265e-06,5.8697e-10,-4.0977e-14,16418.9,-0.407549], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 7,
    label = "CH3CN",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,T}
3 N u0 p1 c0 {2,T}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.50891,0.0133697,-1.84756e-06,-3.80515e-09,1.68422e-12,7598,10.9987], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.4238,0.0154861,-7.68638e-06,1.86346e-09,-1.76952e-13,7526.22,10.9652], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 8,
    label = "CH3NH",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 N u1 p1 c0 {1,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.71758,0.00729787,9.95588e-06,-1.33912e-08,4.52254e-12,20249.4,11.567], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.67934,0.0150886,-7.18687e-06,1.67511e-09,-1.53477e-13,20275.2,15.6665], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 9,
    label = "CH3NH2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 N u0 p1 c0 {1,S} {6,S} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.75019,0.00767848,1.44236e-05,-1.80318e-08,6.02382e-12,-3767.01,10.7147], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.58569,0.0173392,-7.57168e-06,1.63449e-09,-1.43458e-13,-3784.25,15.082], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 10,
    label = "CH3NO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 N u0 p1 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.05468,0.0102237,4.63674e-06,-9.75622e-09,3.60544e-12,7342.48,10.7868], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.79545,0.0147873,-7.49889e-06,1.86098e-09,-1.80544e-13,7217.99,11.1557], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 11,
    label = "CH3NO2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 N u0 p0 c+1 {1,S} {6,D} {7,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 O u0 p2 c0 {2,D}
7 O u0 p3 c-1 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.36489,0.0204311,-4.53033e-06,-6.45794e-09,3.36219e-12,-10628.9,19.7377], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.29539,0.0182397,-9.53896e-06,2.4117e-09,-2.37862e-13,-11291.6,9.04149], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 12,
    label = "CH3ONO2",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,S} {5,S}
5 C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
6 H u0 p0 c0 {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.52175,0.0252086,-7.11047e-06,-7.60984e-09,4.2969e-12,-16792.7,14.7738], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.66705,0.0203893,-1.15244e-05,3.09466e-09,-3.19699e-13,-17809.9,-2.34099], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 13,
    label = "CH3ONO",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 O u0 p2 c0 {1,S} {3,S}
3 N u0 p1 c0 {2,S} {7,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 O u0 p2 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.0870648,0.0397148,-4.57917e-05,2.83162e-08,-7.07324e-12,-9661.98,22.7004], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.57446,0.0164276,-8.85442e-06,2.35371e-09,-2.48209e-13,-10692.6,-3.43872], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Data taken from the cis form, which is the more favorable conformation due to lower enthalpy of formation
Appears in original paper as CH3ONOcis
Data for CH3ONOtrans was ignored
""",
)

entry(
    index = 14,
    label = "CN",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,T}
2 N u0 p1 c0 {1,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83481,-0.00257891,6.22133e-06,-4.76724e-09,1.27618e-12,51910.2,3.02396], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.54417,0.00263413,-1.67394e-06,5.46747e-10,-6.49316e-14,52165.8,9.23794], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 15,
    label = "H2CN",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 N u1 p1 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.85394,0.0049229,3.96887e-06,-6.19348e-09,2.13281e-12,27595.6,9.08866], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.29739,0.00882573,-4.40034e-06,1.06264e-09,-1.00387e-13,27623,11.3545], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 16,
    label = "H2CNO",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 N u0 p1 c0 {1,D} {3,S}
3 O u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.83948,0.0156746,-9.24972e-06,1.62784e-09,3.47131e-13,17271.5,15.7327], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.46969,0.0112766,-5.83684e-06,1.47537e-09,-1.45446e-13,16839.4,7.33722], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 17,
    label = "H2CNO2",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {5,S} {6,S}
2 N u0 p0 c+1 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 O u0 p3 c-1 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.888443,0.0289125,-2.62143e-05,1.10257e-08,-1.5657e-12,14029.2,20.2243], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.93787,0.0123889,-6.93995e-06,1.85019e-09,-1.90338e-13,12835.6,-5.05476], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 18,
    label = "H2NN",
    molecule = 
"""
1 N u0 p0 c+1 {2,D} {3,S} {4,S}
2 N u0 p2 c-1 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87707,-0.00265245,1.86066e-05,-1.76694e-08,5.38801e-12,35263.7,4.2325], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.46258,0.0101014,-5.1679e-06,1.27607e-09,-1.22333e-13,35591.9,15.1071], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 19,
    label = "H2NO",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 O u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93371,0.00221176,5.8622e-06,-6.72932e-09,2.17836e-12,6595.07,4.42022], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.36486,0.00613307,-2.48864e-06,4.83818e-10,-3.63996e-14,6626.55,6.75313], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 20,
    label = "HCN",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {3,S}
2 N u0 p1 c0 {1,T}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.22381,0.00891349,-1.13836e-05,8.32413e-09,-2.41731e-12,14767.1,9.23408], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.92308,0.00444714,-2.18021e-06,5.19245e-10,-4.87687e-14,14710.7,6.27783], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 21,
    label = "HCNH",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.42541,0.00827826,-3.08575e-06,-3.79908e-10,4.40947e-13,31712.1,11.3238], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.74923,0.00782531,-3.66984e-06,8.5182e-10,-7.757e-14,31605.2,9.55092], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Data taken from the trans form, which is the more favorable conformation due to lower enthalpy of formation
Appears in original paper as HCNHtrans
Data for HCNHcis was ignored
""",
)

entry(
    index = 22,
    label = "HCNN",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 N u0 p1 c0 {1,D} {4,S}
4 N u0 p2 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.60254,0.0130918,-1.17832e-05,5.68581e-09,-1.10497e-12,54528.6,11.2686], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.28965,0.00703402,-3.73267e-06,1.00946e-09,-1.08552e-13,54156.7,2.95663], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 23,
    label = "HCNO",
    molecule = 
"""
1 N u0 p0 c+1 {2,T} {3,S}
2 C u0 p0 c0 {1,T} {4,S}
3 O u0 p3 c-1 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86648,0.0108162,-9.82914e-06,5.36663e-09,-1.30321e-12,18738.6,3.62536], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.55025,0.00757618,-4.21171e-06,1.11675e-09,-1.14509e-13,18627,0.452783], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 24,
    label = "HNCO",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {4,S}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.86225,0.0172235,-2.16501e-05,1.50085e-08,-4.13377e-12,-15620,13.7513], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.16893,0.00617768,-2.35286e-06,3.24605e-10,-8.03246e-15,-15990.4,3.07758], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 25,
    label = "HNC",
    molecule = 
"""
1 N u0 p0 c+1 {2,T} {3,S}
2 C u0 p1 c-1 {1,T}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.31995,0.00647578,-6.06482e-06,3.50489e-09,-8.70834e-13,22090.3,9.09546], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.93269,0.00380008,-1.71416e-06,3.79713e-10,-3.33568e-14,21979,6.19553], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""Hydrogen isocyanide""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "HNNO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 N u1 p1 c0 {2,S} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.86113,0.00562696,8.41811e-06,-1.29303e-08,4.71545e-12,23483.9,10.9136], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.00263,0.0100798,-5.78943e-06,1.5602e-09,-1.61895e-13,23204.7,8.97631], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Data taken from the trans form, which is the more favorable conformation due to lower enthalpy of formation
Appears in original paper as HNNOtrans
Data for HNNOcis was ignored
""",
)

entry(
    index = 27,
    label = "HNO",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.51988,-0.00542508,1.7024e-05,-1.48708e-08,4.44763e-12,11763.8,1.75619], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.5882,0.00487709,-2.29243e-06,5.82214e-10,-5.94812e-14,12021.4,10.4316], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 28,
    label = "HNO2",
    molecule = 
"""
1 N u0 p0 c+1 {2,S} {3,S} {4,D}
2 H u0 p0 c0 {1,S}
3 O u0 p3 c-1 {1,S}
4 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.86816,0.00408036,9.55139e-06,-1.29605e-08,4.57374e-12,-6421.6,10.7615], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.71887,0.00923249,-5.00922e-06,1.30155e-09,-1.30504e-13,-6619.49,10.3431], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 29,
    label = "HNOH",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.95652,0.00425182,8.05096e-06,-1.07e-08,3.62572e-12,10271,9.0126], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.99861,0.0109126,-6.184e-06,1.61915e-09,-1.61359e-13,10321.1,12.9267], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Data taken from the trans form, which is the more favorable conformation due to lower enthalpy of formation
appears in original paper as HNOHtrans
Data for HNOHcis was ignored
""",
)

entry(
    index = 30,
    label = "HOCN",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 C u0 p0 c0 {1,S} {3,T}
3 N u0 p1 c0 {2,T}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.77692,0.0120359,-1.16393e-05,6.43178e-09,-1.48094e-12,-3038.41,10.0392], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.26758,0.0061478,-2.91885e-06,6.92686e-10,-6.47955e-14,-3340.27,2.82895], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 31,
    label = "HONO2",
    molecule = 
"""
1 N u0 p0 c+1 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,S} {5,S}
4 O u0 p3 c-1 {1,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.03437,0.0244808,-2.31762e-05,1.03095e-08,-1.64107e-12,-17556.2,19.8358], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.28851,0.0102508,-6.01109e-06,1.6526e-09,-1.73503e-13,-18546.4,-1.38461], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 32,
    label = "HONO",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,D}
2 O u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {1,D}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49107,0.00681117,-1.30943e-06,-2.34197e-09,1.18932e-12,-10572.3,8.99804], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.19967,0.00594217,-2.95405e-06,7.19846e-10,-6.74909e-14,-10812.3,5.0881], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Data taken from the trans form, which is the more favorable conformation due to lower enthalpy of formation
appears in original paper as HONOtrans
Data for HONOcis was ignored
""",
)

entry(
    index = 33,
    label = "HON(S)",
    molecule = 
"""
1 O u0 p1 c+1 {2,D} {3,S}
2 N u0 p2 c-1 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89125,-0.00147731,1.05762e-05,-1.0425e-08,3.31002e-12,33116.1,4.42552], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.10244,0.00424033,-1.84394e-06,4.1749e-10,-4.12e-14,33145.8,7.59046], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    label = "HON(T)",
    molecule = 
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {3,S}
2 N u2 p1 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.05582,0.00443591,-1.2222e-06,-1.14007e-09,6.69025e-13,24609.4,9.08279], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.71175,0.00316089,-1.3327e-06,2.82288e-10,-2.37382e-14,24410.8,5.58115], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 35,
    label = "N2H2trans",
    molecule = 
"""
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.06591,-0.00434024,2.1325e-05,-1.9684e-08,5.96855e-12,23295.4,3.56067], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.53341,0.00932034,-4.46173e-06,1.03778e-09,-9.45361e-14,23625.3,14.8959], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Data taken from the trans form, which is the more favorable conformation due to lower enthalpy of formation
appears in original paper as N2H2trans
Data for N2H2cis was ignored
""",
)

entry(
    index = 36,
    label = "N2H3",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 N u0 p1 c0 {1,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80272,0.00552764,6.8486e-07,-2.00296e-09,6.21446e-13,25752.3,5.58214], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.20302,0.00799163,-3.10893e-06,5.91433e-10,-4.3455e-14,25869,8.45902], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 37,
    label = "N2H4",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 N u0 p1 c0 {1,S} {5,S} {6,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.942543,0.0213488,-1.88706e-05,1.00963e-08,-2.30996e-12,10965.3,17.572], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.21894,0.0123204,-5.44372e-06,1.22223e-09,-1.10737e-13,10506.1,6.57037], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 38,
    label = "N2O",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 N u0 p0 c+1 {1,T} {3,S}
3 O u0 p3 c-1 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.49126,0.00916225,-8.24848e-06,3.8329e-09,-7.19462e-13,8849.39,9.80262], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.61317,0.0051597,-2.97228e-06,8.00505e-10,-8.26332e-14,8600.75,4.26881], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 39,
    label = "N2O3",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 N u0 p1 c0 {2,S} {5,D}
5 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.44942,0.0169956,-1.30499e-05,2.95689e-09,4.56254e-13,8434.02,6.24145], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.89162,0.0072677,-4.51929e-06,1.31072e-09,-1.42421e-13,7543.54,-11.3754], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""Dinitrogen trioxide""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "N2O4",
    molecule = 
"""
1 O u0 p3 c-1 {2,S}
2 N u0 p0 c+1 {1,S} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 N u0 p0 c+1 {2,S} {5,S} {6,D}
5 O u0 p3 c-1 {4,S}
6 O u0 p2 c0 {4,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01748,0.0219402,-1.28644e-05,-7.61626e-10,2.11358e-12,-1112.75,7.52136], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.07874,0.0121149,-7.75596e-06,2.25245e-09,-2.44865e-13,-2245.99,-13.6768], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""Dinitrogen tetroxide""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "NCCN",
    molecule = 
"""
1 N u0 p1 c0 {2,T}
2 C u0 p0 c0 {1,T} {3,S}
3 C u0 p0 c0 {2,S} {4,T}
4 N u0 p1 c0 {3,T}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.64573,0.0127414,-1.55385e-05,1.04783e-08,-2.86927e-12,35522.5,4.64157], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.84081,0.0063881,-3.64904e-06,9.79067e-10,-1.012e-13,35362.1,-0.730726], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    label = "NCN",
    molecule = 
"""
multiplicity 3
1 N u1 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 N u1 p1 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.15727,0.00725557,-3.91667e-06,-6.1055e-10,8.13377e-13,53437.4,7.1146], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.47904,0.00418412,-2.63289e-06,7.49202e-10,-8.04624e-14,53062.3,0.183948], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    label = "NCO",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.80872,0.00796076,-5.45242e-06,1.26169e-09,9.9099e-14,13734.9,9.07421], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.77931,0.00523935,-3.11171e-06,8.62142e-10,-9.12475e-14,13482.7,4.10148], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    label = "NH2",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97884,-0.000513888,2.68436e-06,-9.18833e-10,-9.82251e-14,21248.7,0.77762], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.6284,0.0034438,-1.08606e-06,1.50714e-10,-4.59423e-15,21591,7.65373], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    label = "NH2OH",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.43399,0.00876264,7.67849e-06,-1.49986e-08,5.93967e-12,-6072.72,11.5654], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.54617,0.00846243,-4.09392e-06,9.98179e-10,-9.66389e-14,-6902.58,-0.661755], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""Hydroxylamine""",
    longDesc = 
u"""
Data taken from the trans form, which is the more favorable conformation due to lower enthalpy of formation
appears in original paper as NH2OHtrans
Data for NH2OHcis was ignored
""",
)

entry(
    index = 46,
    label = "NH3",
    molecule = 
"""
1 N u0 p1 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.26651,0.00305893,5.78755e-07,9.49077e-10,-9.02222e-13,-6365.11,3.58795], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.07097,0.00875467,-3.33525e-06,4.72016e-10,-1.13563e-14,-5771.69,14.9517], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    label = "NH",
    molecule = 
"""
multiplicity 3
1 N u2 p1 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44697,0.000557848,-2.00289e-06,2.85953e-09,-1.12434e-12,41789.9,2.02991], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.95101,0.000909994,-8.35582e-08,-5.17312e-11,1.13981e-14,41970.7,4.83057], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    index = 48,
    label = "NNH",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.09255,-0.00237173,1.15311e-05,-1.06308e-08,3.23938e-12,29137.5,3.93251], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.90981,0.00444718,-1.82919e-06,3.64004e-10,-3.13273e-14,29269.6,9.11654], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    label = "NO",
    molecule = 
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 O u0 p2 c0 {1,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.15037,-0.0040889,9.38072e-06,-7.50909e-09,2.11743e-12,9770.19,2.53971], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.79463,0.00212261,-1.11937e-06,2.79521e-10,-2.68625e-14,10001.9,8.88323], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    label = "NO2",
    molecule = 
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {3,S}
2 O u0 p2 c0 {1,D}
3 O u1 p2 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.39101,0.00262448,5.0979e-06,-7.6212e-09,2.7996e-12,2781.31,8.5722], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.65239,0.00471632,-2.74592e-06,7.45383e-10,-7.63891e-14,2572.16,6.52683], Tmin=(1000,'K'), Tmax=(3000,'K')),
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
    label = "NO3",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 N u0 p0 c+1 {1,D} {3,S} {4,S}
3 O u0 p3 c-1 {2,S}
4 O u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.09447,0.0151015,-1.26448e-05,3.67238e-09,8.62184e-14,7186.27,10.4315], Tmin=(298,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.38294,0.00542423,-3.34398e-06,9.48445e-10,-1.01962e-13,6354.74,-6.30266], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (298,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

