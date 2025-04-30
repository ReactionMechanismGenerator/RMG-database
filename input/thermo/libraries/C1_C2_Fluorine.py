#!/ usr/bin/env python
# encoding: utf-8

name = "C1_C2_Fluorine"
shortDesc = u"Thermo File for C1 and C2 fluorinated species"
longDesc = u"""
ANL0 method extended to include Fluorine is used.

Theory-Based Mechanism for Fluoromethane Combustion I: Thermochemistry and Abstraction Reactions.
Siddha Sharma, Kento Abeywardane, and C. Franklin Goldsmith.
The Journal of Physical Chemistry A 2023 127 (6), 1499-1511, DOI: 10.1021/acs.jpca.2c06623T


"""
entry(
    index = 0,
    label = "F",
    molecule = 
"""
multiplicity 2
1 F u1 p3 c0
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.4193242, 2.93848449e-03, -8.91441625e-06, 9.90063549e-09, -3.78936967e-12, 8998.3259, 4.73388583], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.73547309, -3.18376264e-04, 1.80404747e-07, -4.76650983e-11, 4.82178946e-15, 9007.23724, 3.62700929], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""Hf(0 K) = 18.95 kcal/mol (ANL0);  Hf(298 K) = 19.45 (kcal/mol). partition function via MESS, conversion via automech""",
)

entry(
    index = 1,
    label = "F2",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 F u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.05475955E+00, 2.39284287E-03, 1.02445470E-06, -4.21369121E-09, 2.20531535E-12,-1.01889608E+03, 6.25912496E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.88707643E+00, 7.48865564E-04,-1.61882213E-07,-1.33318562E-11, 2.95334585E-15, -1.24339610E+03, 1.89730015E+00], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""Hf(0 K) = 0.0 kcal/mol (ANL0). ATcT ver 1.124, fit January 2023""",
)

entry(
    index = 2,
    label = "HF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47861056E+00, 2.30210129E-04,-7.26207054E-07, 8.90789862E-10,-2.44257848E-13,-3.38440904E+04, 1.03719885E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.92408264E+00, 8.52279140E-04, -1.60115398E-07, 1.31455482E-11, -2.46281644E-16, -3.36186854E+04, 4.19417238E+00], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""Hf(0 K) = -65.17 kcal/mol (ANL0). HF <g> ATcT ver. 1.124, DHf298 = -272.727 ± 0.019 kJ/mol - fit JAN23. polynomial from ATcT""",
)

entry(
    index = 3,
    label = "CF",
    molecule = 
"""
multiplicity 2
1 C u1 p1 c0 {2,S}
2 F u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84369209E+00,-3.50188886E-03, 1.29819685E-05,-1.43766790E-08, 5.35553536E-12, 2.85946414E+04, 4.30541730E+00], Tmin=(100,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.76688366E+00, 7.72455711E-04,-2.81687813E-07, 4.79035640E-11,-2.92695193E-15, 2.84210431E+04, 3.72489614E+00], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = u"""Hf(0 K) = 58.19 kcal/mol (ANL0). CF <g> ATcT ver. 1.124, DHf298 = 246.72 ± 0.12 kJ/mol - fit JAN23. polynomial from ATcT""",
)

entry(
    index = 4,
    label = "CHF",
    molecule = 
"""
multiplicity 1
1 C u0 p1 c0 {2,S} {3,S}
2 F u0 p3 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.44899439, -5.68990301e-03, 2.16897836e-05, -2.28311208e-08, 8.17372154e-12, 1.66128322e+04, 2.40536115], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.86475765, 4.88458805e-03, -2.5223093e-06, 6.24855712e-10, -6.04163955e-14, 1.67633545e+04, 9.12031189], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""ground state singlet""",
    longDesc = u"""Hf(0 K) = 35.38 kcal/mol (ANL0);  Hf(298 K) = 35.45 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 5,
    label = "CHF(T)",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 F u0 p3 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.30446655, -4.90241108e-03, 2.19779829e-05, -2.52270701e-08, 9.6421829e-12, 2.41242421e+04, 3.96478878], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.37631926, 3.87567905e-03, -1.84589811e-06, 4.28329224e-10, -3.92782763e-14, 2.41270804e+04, 7.37861901], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""excited state triplet""",
    longDesc = u"""Hf(0 K) = 50.28 kcal/mol (ANL0);  Hf(298 K) = 50.35 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 6,
    label = "CH2F",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 F u0 p3 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77938639, -3.9761268e-04, 1.87718416e-05, -2.40689064e-08, 9.55051041e-12, -4993.31979, 6.23834236], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.20982001, 6.97057987e-03, -3.20030736e-06, 7.19313063e-10, -6.41861685e-14, -5057.91555, 7.93158384], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -6.64 kcal/mol (ANL0);  Hf(298 K) = -7.47 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 7,
    label = "CH3F",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 F u0 p3 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.13884995, -0.01522257, 6.07163912e-05, -6.52865359e-08, 2.38092602e-11, -2.96183839e+04, -0.155798184], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.09543626, 0.0130467027, -6.3468948e-06, 1.49984057e-09, -1.39689327e-13, -2.92619821e+04, 16.7625962], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -54.40 kcal/mol (ANL0);  Hf(298 K) = -56.33 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 8,
    label = "CF2",
    molecule = 
"""
multiplicity 1
1 F u0 p3 c0 {2,S}
2 C u0 p1 c0 {1,S} {3,S}
3 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65163442, 5.18866653e-04, 1.52247353e-05, -2.21767603e-08, 9.27643387e-12, -2.4486645e+04, 7.48151723], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.59662945, 3.42444206e-03, -2.0202923e-06, 5.51455076e-10, -5.73243175e-14, -2.49513874e+04, 1.42802895], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""ground state singlet""",
    longDesc = u"""Hf(0 K) = -46.37 kcal/mol (ANL0);  Hf(298 K) = -46.26 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 9,
    label = "CF2(T)",
    molecule = 
"""
multiplicity 3
1 F u0 p3 c0 {2,S}
2 C u2 p0 c0 {1,S} {3,S}
3 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.67009489, 2.31202126e-03, 8.41229465e-06, -1.37130948e-08, 5.81157528e-12, 3986.77477, 8.29624589], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.60518097, 3.40196683e-03, -2.00413888e-06, 5.46698342e-10, -5.68160227e-14, 3587.59038, 2.66900468], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""excited state triplet""",
    longDesc = u"""Hf(0 K) = 10.24 kcal/mol (ANL0);  Hf(298 K) = 10.40 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 10,
    label = "CHF2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80077977, -1.68643237e-03, 2.92795649e-05, -3.86542877e-08, 1.55755441e-11, -3.05196133e+04, 8.6212524], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.09781181, 7.11977695e-03, -3.7596166e-06, 9.50799123e-10, -9.36026598e-14, -3.09741319e+04, 4.99840022], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -57.33 kcal/mol (ANL0);  Hf(298 K) = -58.17 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 11,
    label = "CH2F2",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.37317686, -7.71427672e-03, 4.92370006e-05, -5.80822441e-08, 2.2123818e-11, -5.55282863e+04, 5.28732619], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.73057188, 0.0119968871, -6.16999426e-06, 1.5279607e-09, -1.47950731e-13, -5.57204624e+04, 10.324247], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -105.94 kcal/mol (ANL0);  Hf(298 K) = -107.78 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 12,
    label = "CF3",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.46154028, 0.012950989, -2.16596832e-06, -9.8060505e-09, 5.70993719e-12, -5.75635077e+04, 14.0623986], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.91197113, 5.85949131e-03, -3.47369564e-06, 9.51960392e-10, -9.9279589e-14, -5.855994e+04, -4.16067146], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""Hf(0 K) = -111.18 kcal/mol (ANL0);  Hf(298 K) = -111.86 (kcal/mol)""",
    longDesc = u"""partition function via MESS, conversion via automech.""",
)

entry(
    index = 13,
    label = "CHF3",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.90173834, 7.36063374e-03, 1.92369637e-05, -3.26727174e-08, 1.40244111e-11, -8.50995183e+04, 11.8531926], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.94386987, 0.0101602618, -5.5471806e-06, 1.43839185e-09, -1.4431344e-13, -8.59741148e+04, -0.489096854], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -164.84 kcal/mol (ANL0);  Hf(298 K) = -166.52 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 14,
    label = "CF4",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.12886163, 0.0269669118, -2.32266221e-05, 5.92826358e-09, 1.04127288e-12, -1.13621904e+05, 17.8860148], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.3749656, 8.0910984e-03, -4.81102763e-06, 1.32179412e-09, -1.38142724e-13, -1.15181132e+05, -13.762183], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -221.68 kcal/mol (ANL0);  Hf(298 K) = -223.12 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 15,
    label = "OF",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 F u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.12523435E+00,-4.05489906E-03, 1.48376058E-05,-1.71470326E-08, 6.66439670E-12, 1.21878876E+04, 3.19599877E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.29579412E+00,-1.53396225E-05, 2.06380037E-07,-6.67261993E-11, 5.19689372E-15,1.19363867E+04, 1.26523156E+00], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (6000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = 26.54 kcal/mol (ANL0). FO <g> ATcT ver. 1.124, DHf298 = 110.90 ± 0.14 kJ/mol - fit JAN23. partition function via MESS, conversion via automech.""",
)

entry(
    index = 16,
    label = "FOH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 F u0 p3 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.01427827, -2.24815893e-03, 1.58056202e-05, -1.97272454e-08, 7.87692696e-12, -1.17278465e+04, 4.49581402], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.91008189, 2.65833789e-03, -1.02774881e-06, 1.95623141e-10, -1.48729696e-14, -1.18681327e+04, 4.05775859], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -20.22 kcal/mol (ANL0);  Hf(298 K) = -20.92 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 17,
    label = "F2O",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.80546077, 0.0102440633, -8.08223326e-06, 1.08048406e-10, 1.62921486e-12, 1654.71494, 11.028197], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.50548399, 2.19029088e-03, -1.31768027e-06, 3.64783273e-10, -3.83238319e-14, 996.050938, -2.62010033], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = 6.27 kcal/mol (ANL0);  Hf(298 K) = 5.72 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 18,
    label = "FOO",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.09573104, 0.0113826157, -1.7233058e-05, 1.38769848e-08, -4.52972342e-12, 1495.69342, 10.7381197], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.09030167, 2.70913318e-03, -1.59858244e-06, 4.37280609e-10, -4.55829164e-14, 1089.47013, 1.17522481], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = 6.02 kcal/mol (ANL0);  Hf(298 K) = 5.56 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 19,
    label = "FOOH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.24513645, 0.0162412373, -1.45288921e-05, 4.48516893e-09, 2.16757296e-13, -6948.6866, 14.4170111], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.95496734, 4.81484445e-03, -2.7882228e-06, 7.56373861e-10, -7.85549623e-14, -7867.61627, -4.33677485], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -9.89 kcal/mol (ANL0);  Hf(298 K) = -11.28 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 20,
    label = "FOOF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 F u0 p3 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.65951099, 0.0294089843, -4.36141196e-05, 3.04949699e-08, -8.25886128e-12, 2029.1131, 17.0475212], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.11219327, 2.95182744e-03, -1.81630974e-06, 4.93370239e-10, -5.05968794e-14, 731.153014, -14.0193097], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = 7.95 kcal/mol (ANL0);  Hf(298 K) = 6.96 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 21,
    label = "FCO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 C u1 p0 c0 {1,D} {3,S}
3 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44442764, 3.58299017e-03, 3.3175635e-06, -7.17713557e-09, 3.14601149e-12, -2.25576575e+04, 9.13877709], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.06597351, 3.97110832e-03, -2.26619886e-06, 6.0487021e-10, -6.18959515e-14, -2.28159283e+04, 5.45702826], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -42.57 kcal/mol (ANL0);  Hf(298 K) = -42.44 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 22,
    label = "CHFO",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75304076, -1.54852861e-03, 2.57217119e-05, -3.26531112e-08, 1.28244723e-11, -4.72465247e+04, 7.84452039], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.35899933, 7.98029314e-03, -4.19403281e-06, 1.05585946e-09, -1.03534032e-13, -4.74866206e+04, 7.99119076], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -90.60 kcal/mol (ANL0);  Hf(298 K) = -91.47 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 23,
    label = "CF2O",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.21606409, 0.013238051, -4.23784631e-06, -6.67863953e-09, 4.37910484e-12, -7.41605798e+04, 14.772971], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.20117804, 6.61606316e-03, -3.82471522e-06, 1.0303664e-09, -1.06158338e-13, -7.50026091e+04, -0.880396197], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -144.24 kcal/mol (ANL0);  Hf(298 K) = -144.99 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 24,
    label = "CHFOH",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 C u1 p0 c0 {1,S} {3,S} {5,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.98987411, 0.0237844606, -3.05105383e-05, 1.92339391e-08, -4.45640877e-12, -2.89505662e+04, 15.2412918], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.13453313, 5.92177455e-03, -2.48968364e-06, 5.17915265e-10, -4.32125545e-14, -2.97078004e+04, -4.40136414], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -53.45 kcal/mol (ANL0);  Hf(298 K) = -54.72 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 25,
    label = "CHF2O",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.47349156, 0.0117065615, 1.0433728e-05, -2.54481526e-08, 1.18740003e-11, -5.03665081e+04, 15.1612275], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.4906119, 9.58783345e-03, -5.27510353e-06, 1.37467204e-09, -1.38385117e-13, -5.13912163e+04, -1.64500285], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -95.89 kcal/mol (ANL0);  Hf(298 K) = -97.50 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 26,
    label = "CF2OH",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {5,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.11538489, 0.0160666213, -9.47228932e-06, -1.54679459e-09, 2.48528582e-12, -5.61262127e+04, 12.6285668], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.6877712, 6.55736453e-03, -3.35120285e-06, 8.363612e-10, -8.20859446e-14, -5.70666474e+04, -5.75243238], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -107.18 kcal/mol (ANL0);  Hf(298 K) = -108.44 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 27,
    label = "CF3O",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.79814049, 0.0255607305, -2.18881631e-05, 5.3104816e-09, 1.14830319e-12,
      -7.70569173e+04, 16.9982065], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.78726745, 7.5152445e-03, -4.47481513e-06, 1.23045799e-09, -1.28662165e-13,
      -7.85523516e+04, -13.3551556], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -148.92 kcal/mol (ANL0);  Hf(298 K) = -150.17 (kcal/mol) partition function via MESS, conversion via automech.""",
)

entry(
    index = 28,
    label = "CF3OO",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 F u0 p3 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.45335839, 0.0387514652, -4.70607911e-05, 2.73561158e-08, -6.13621231e-12, -7.80138572e+04, 19.9771821], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.90425321, 8.11280099e-03, -4.85106614e-06, 1.33823027e-09, -1.40282366e-13, -7.99100428e+04, -21.6920834], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -149.82 kcal/mol (ANL0);  Hf(298 K) = -151.47 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 29,
    label = "CH2FOH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {4,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78369937, 7.70382916e-04, 3.72406084e-05, -5.06195155e-08, 2.05267187e-11, -5.24864185e+04, 8.64847277], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.24798348, 0.0119655534, -5.73318156e-06, 1.34693696e-09, -1.25398329e-13, -5.30848809e+04, 3.5739147], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -98.95 kcal/mol (ANL0);  Hf(298 K) = -101.52 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 30,
    label = "CF3OH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 F u0 p3 c0 {2,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.21923787, 0.0232234134, -1.02697162e-05, -8.47151864e-09, 6.57782403e-12, -1.11067635e+05, 15.8406104], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.90029624, 9.12605266e-03, -4.8757605e-06, 1.25432841e-09, -1.25676409e-13, -1.1258876e+05, -13.5684416], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -215.45 kcal/mol (ANL0);  Hf(298 K) = -217.56 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 31,
    label = "HCCF",
    molecule = 
"""
1 C u0 p0 c0 {2,T} {4,S}
2 C u0 p0 c0 {1,T} {3,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.3152257, 0.0276494121, -4.82398959e-05, 4.20639331e-08, -1.40267248e-11, 1.13565522e+04, 13.8972542], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.42697897, 5.31806104e-03, -2.51260704e-06, 5.83315866e-10, -5.37986483e-14, 1.07436139e+04, -4.70438365], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = 24.93 kcal/mol (ANL0);  Hf(298 K) = 25.09 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 32,
    label = "CCHF",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68326384, 5.5588176e-03, 6.38916043e-06, -1.30397063e-08, 5.80716935e-12, 3.47768102e+04, 7.40824404], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.5400845, 6.45826186e-03, -3.35610502e-06, 8.38185311e-10, -8.17217469e-14, 3.44269946e+04, 2.30898396], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = 71.65 kcal/mol (ANL0);  Hf(298 K) = 71.85 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 33,
    label = "FCCF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,T}
3 C u0 p0 c0 {2,T} {4,S}
4 F u0 p3 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70298401, 0.0203644476, -3.5352521e-05, 3.17660905e-08, -1.10385741e-11, -1199.23353, 4.57143464], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.5181303, 5.02535538e-03, -2.73881937e-06, 7.0875438e-10, -7.09936927e-14, -1645.24966, -8.23211537], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = 0.42 kcal/mol (ANL0);  Hf(298 K) = 1.10 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 34,
    label = "CCF2",
    molecule = 
"""
multiplicity 3
1 C u2 p0 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.61879059, 0.016978508, -1.82955248e-05, 1.02336679e-08, -2.42015483e-12, 1.43824379e+04, 12.4299234], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.91060304, 5.75850601e-03, -3.37803361e-06, 9.19726209e-10, -9.55148375e-14, 1.35916868e+04, -4.02436787], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = 31.06 kcal/mol (ANL0);  Hf(298 K) = 31.35 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 35,
    label = "CHFCH",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u1 p0 c0 {2,D} {5,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.06356203, 0.0147856747, -2.86448415e-06, -9.37098546e-09, 5.69875075e-12, 1.30739406e+04, 14.9213242], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.68762709, 9.13938028e-03, -4.48556637e-06, 1.07214897e-09, -1.01072093e-13, 1.23625645e+04, 1.2206714], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = 29.28 kcal/mol (ANL0);  Hf(298 K) = 28.43 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 36,
    label = "CH2CF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5682804, 0.0109222242, 4.85413798e-06, -1.57205629e-08, 7.60497459e-12, 1.18574435e+04, 12.8268119], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.29176785, 9.69460151e-03, -4.80469113e-06, 1.15708826e-09, -1.09712163e-13, 1.12909017e+04, 3.28120763], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = 26.94 kcal/mol (ANL0);  Hf(298 K) = 26.08 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 37,
    label = "CF2CH",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,D} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.930512786, 0.0293396794, -3.61984796e-05, 2.26923854e-08, -5.64796755e-12, -1.04570112e+04, 20.6428286], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.4544182, 7.88406376e-03, -4.18152304e-06, 1.06478414e-09, -1.05612651e-13, -1.16269983e+04, -6.24420915], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -17.54 kcal/mol (ANL0);  Hf(298 K) = -18.19 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 38,
    label = "CHFCF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28113161, 0.0109839101, 6.56114891e-06, -1.8799085e-08, 8.92624379e-12, -6771.06643, 11.5803137], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.70012562, 8.92667012e-03, -4.77180618e-06, 1.21946768e-09, -1.21107816e-13, -7578.95661, -1.81680046], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -9.91 kcal/mol (ANL0);  Hf(298 K) = -10.49 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 39,
    label = "CF2CF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,D}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.82590808, 0.0242171167, -2.79887713e-05, 1.73080368e-08, -4.58130477e-12, -2.85585415e+04, 13.768787], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.41129435, 7.83994269e-03, -4.58806786e-06, 1.24719316e-09, -1.29376913e-13, -2.96307499e+04, -8.9884845], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -53.14 kcal/mol (ANL0);  Hf(298 K) = -53.37 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 40,
    label = "CH2CHF",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 C u0 p0 c0 {1,D} {3,S} {6,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.79571041, 5.25068619e-03, 3.02044739e-05, -4.54139046e-08, 1.91479844e-11, -1.84086168e+04, 11.879773], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.68249681, 0.0134347288, -6.53645477e-06, 1.54905986e-09, -1.4488036e-13, -1.90226164e+04, 5.10938602], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -32.20 kcal/mol (ANL0);  Hf(298 K) = -34.09 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 41,
    label = "CH2CF2",
    molecule = 
"""
1 C u0 p0 c0 {2,D} {5,S} {6,S}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.14782739, 0.0231962881, -1.00035951e-05, -7.45436392e-09, 5.94861218e-12, -4.3385447e+04, 18.8964912], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.60045678, 0.0120063108, -6.14504866e-06, 1.52044809e-09, -1.47398267e-13, -4.45537708e+04, -4.06808029], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -81.98 kcal/mol (ANL0);  Hf(298 K) = -83.69 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 42,
    label = "CHFCHF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {5,S}
3 C u0 p0 c0 {2,D} {4,S} {6,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.8351033, 0.0111087606, 1.77987045e-05, -3.43683453e-08, 1.5397589e-11, -3.86600799e+04, 12.3003259], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.29106003, 0.0124415345, -6.39172606e-06, 1.58472793e-09, -1.53784332e-13, -3.95969404e+04, -1.99889525], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -72.36 kcal/mol (ANL0);  Hf(298 K) = -73.97 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 43,
    label = "CHFCF2",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.07601448, 0.0265134825, -2.14317925e-05, 5.98461326e-09, 4.77219759e-13, -6.14852119e+04, 16.2976673], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.14357143, 0.0111323474, -6.07424291e-06, 1.57620588e-09, -1.58344267e-13, -6.27521699e+04, -9.37705558], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -117.69 kcal/mol (ANL0);  Hf(298 K) = -118.96 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 44,
    label = "CF2CF2",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.97197671, 0.038262241, -5.33417376e-05, 3.98819598e-08, -1.23195031e-11, -8.27744501e+04, 15.3983231], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.90664558, 9.96111722e-03, -5.83609496e-06, 1.58817688e-09, -1.64907909e-13, -8.42512446e+04, -18.2304245], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -159.89 kcal/mol (ANL0);  Hf(298 K) = -160.73 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 45,
    label = "CH3CF",
    molecule = 
"""
multiplicity 1
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p1 c0 {1,S} {3,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05673123, -4.20077535e-04, 3.80570386e-05, -5.00269145e-08, 2.00392878e-11, 7606.87682, 8.74716968], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.52113416, 0.0133526046, -6.60105409e-06, 1.58266903e-09, -1.49288114e-13, 7277.48301, 8.84725679], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""ground state singlet""",
    longDesc = u"""Hf(0 K) = 19.61 kcal/mol (ANL0);  Hf(298 K) = 17.97 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 46,
    label = "CH3CF(T)",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u2 p0 c0 {1,S} {3,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.53500906, -7.54158281e-03, 4.94838362e-05, -5.7653285e-08, 2.18173797e-11, 1.82561045e+04, 2.92291083], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.23333288, 0.0137405542, -6.81556314e-06, 1.63773968e-09, -1.54706425e-13, 1.82548397e+04, 11.419236], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""excited state triplet""",
    longDesc = u"""Hf(0 K) = 41.08 kcal/mol (ANL0);  Hf(298 K) = 39.55 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 47,
    label = "CH2FCH",
    molecule = 
"""
multiplicity 1
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u0 p1 c0 {2,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94946513, 5.24906139e-03, 2.21022862e-05, -3.30250805e-08, 1.36905597e-11, 1.88697688e+04, 7.52429443], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.15028916, 0.0128133649, -6.39536487e-06, 1.54450141e-09, -1.46498806e-13, 1.85110262e+04, 4.75764376], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""ground state singlet""",
    longDesc = u"""Hf(0 K) = 42.10 kcal/mol (ANL0);  Hf(298 K) = 40.57 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 48,
    label = "CH2FCH(T)",
    molecule = 
"""
multiplicity 3
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 C u2 p0 c0 {2,S} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77733762, 5.20936307e-03, 2.24151259e-05, -3.35084964e-08, 1.39169309e-11, 2.00951499e+04, 9.35215202], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.08569928, 0.0125179977, -6.10642605e-06, 1.44844758e-09, -1.35457379e-13, 1.97108966e+04, 6.03498894], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""excited state triplet""",
    longDesc = u"""Hf(0 K) = 44.52 kcal/mol (ANL0);  Hf(298 K) = 42.91 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 49,
    label = "CH2FCF",
    molecule = 
"""
multiplicity 1
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 C u0 p1 c0 {2,S} {4,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.99356636, 6.41183585e-03, 2.7031107e-05, -4.14298358e-08, 1.71459642e-11, -1.2650136e+04, 7.99196774], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.43036611, 0.013606902, -7.726865e-06, 2.05103435e-09, -2.08799752e-13, -1.34977429e+04, -1.90410582], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""ground state singlet""",
    longDesc = u"""Hf(0 K) = -20.46 kcal/mol (ANL0);  Hf(298 K) = -21.88 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 50,
    label = "CH2FCF(T)",
    molecule = 
"""
multiplicity 3
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 C u2 p0 c0 {2,S} {4,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.09318775, 0.0101362152, 2.12167172e-05, -3.88495248e-08, 1.71979561e-11, -2689.21628, 13.5799209], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.00119718, 0.0114828539, -6.07879006e-06, 1.54143849e-09, -1.52148179e-13, -3799.76264, -3.33291007], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""excited state triplet""",
    longDesc = u"""Hf(0 K) = -0.80 kcal/mol (ANL0);  Hf(298 K) = -2.38 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 51,
    label = "CHF2CH(S)",
    molecule = 
"""
multiplicity 1
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 C u0 p1 c0 {2,S} {6,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.04193777, 6.65970333e-03, 2.39192215e-05, -3.84380848e-08, 1.64168354e-11, -1514.68879, 9.13157563], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.61831581, 0.0116842401, -6.071496e-06, 1.51640709e-09, -1.47853794e-13, -2282.11451, -0.963827805], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""excited state singlet""",
    longDesc = u"""Hf(0 K) = 1.52 kcal/mol (ANL0);  Hf(298 K) = 0.26 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 52,
    label = "CHF2CH",
    molecule = 
"""
multiplicity 3
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 C u2 p0 c0 {2,S} {6,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.26739694, 0.0112894535, 1.47512829e-05, -3.0780796e-08, 1.40666531e-11, -5678.25464, 13.2000375], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.89857166, 0.0111185636, -5.69530225e-06, 1.40857311e-09, -1.36415714e-13, -6615.18454, -1.76031361], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""ground state triplet""",
    longDesc = u"""Hf(0 K) = -6.84 kcal/mol (ANL0);  Hf(298 K) = -8.20 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 53,
    label = "CHF2CF",
    molecule = 
"""
multiplicity 1
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3 F u0 p3 c0 {2,S}
4 C u0 p1 c0 {2,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81547381, 0.0145254768, 6.08140094e-06, -2.13783763e-08, 1.03224416e-11, -3.54081453e+04, 11.402087], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.21151615, 0.0106728488, -5.90846437e-06, 1.54675939e-09, -1.56243063e-13, -3.65167988e+04, -7.23142244], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""ground state singlet""",
    longDesc = u"""Hf(0 K) = -65.77 kcal/mol (ANL0);  Hf(298 K) = -66.79 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 54,
    label = "CHF2CF(T)",
    molecule = 
"""
multiplicity 3
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3 F u0 p3 c0 {2,S}
4 C u2 p0 c0 {2,S} {5,S}
5 F u0 p3 c0 {4,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45903092, 0.0168064324, 4.66065243e-07, -1.55292514e-08, 8.14001224e-12, -2.72513654e+04, 13.8593107], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.16415687, 0.0107038952, -5.91766704e-06, 1.54826928e-09, -1.563648e-13, -2.83874168e+04, -6.05880189], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""excited state triplet""",
    longDesc = u"""Hf(0 K) = -49.56 kcal/mol (ANL0);  Hf(298 K) = -50.67 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 55,
    label = "CF3CH(S)",
    molecule = 
"""
multiplicity 1
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 C u0 p1 c0 {2,S} {6,S}
6 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.76230589, 0.0313884028, -3.25507083e-05, 1.5352385e-08, -2.34959967e-12, -3.04094086e+04, 17.1628767], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.16157122, 9.43789393e-03, -5.22910923e-06, 1.37120685e-09, -1.38776964e-13, -3.18874892e+04, -14.6442857], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""excited state singlet""",
    longDesc = u"""Hf(0 K) = -55.97 kcal/mol (ANL0);  Hf(298 K) = -57.13 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 56,
    label = "CF3CH",
    molecule = 
"""
multiplicity 3
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 C u2 p0 c0 {2,S} {6,S}
6 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.10668618, 0.0261486395, -1.58348534e-05, -4.54964993e-09, 5.68353079e-12, -3.44631379e+04, 17.1493525], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.32786277, 8.9754911e-03, -4.89026184e-06, 1.2687736e-09, -1.2751248e-13, -3.60383347e+04, -14.610874], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""ground state triplet""",
    longDesc = u"""Hf(0 K) = -64.01 kcal/mol (ANL0);  Hf(298 K) = -65.22 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 57,
    label = "CF3CF",
    molecule = 
"""
multiplicity 1
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 C u0 p1 c0 {2,S} {6,S}
6 F u0 p3 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.44182545, 0.0295100166, -2.56898161e-05, 7.25178615e-09, 6.90723159e-13, -6.36532399e+04, 16.8316967], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.21590001, 9.04396663e-03, -5.37861457e-06, 1.47769351e-09, -1.54410317e-13, -6.53521401e+04, -17.5155225], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""ground state singlet""",
    longDesc = u"""Hf(0 K) = -121.98 kcal/mol (ANL0);  Hf(298 K) = -122.86 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 58,
    label = "CF3CF(T)",
    molecule = 
"""
multiplicity 3
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 C u2 p0 c0 {2,S} {6,S}
6 F u0 p3 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1827828, 0.0266875444, -2.12230857e-05, 3.92976766e-09, 1.64655861e-12, -5.54623834e+04, 13.974076], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.33963265, 8.84559026e-03, -5.2527769e-06, 1.44166224e-09, -1.50540407e-13, -5.70402463e+04, -17.420493], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""excited state triplet""",
    longDesc = u"""Hf(0 K) = -105.56 kcal/mol (ANL0);  Hf(298 K) = -106.33 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 59,
    label = "CH3CHF",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u1 p0 c0 {1,S} {3,S} {7,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.5970993, 9.88227741e-04, 3.63760214e-05, -4.6509985e-08, 1.81123825e-11, -1.06550218e+04, 5.1012162], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.25931227, 0.0166765324, -8.11148829e-06, 1.91827168e-09, -1.78882045e-13, -1.07810285e+04, 9.32783573], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -15.46 kcal/mol (ANL0);  Hf(298 K) = -17.89 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 60,
    label = "CH2FCH2",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.14647415, 1.3840617e-03, 3.99976445e-05, -5.33598411e-08, 2.1417767e-11, -8657.50883, 8.12743932], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.48594603, 0.016292009, -7.87144281e-06, 1.85150455e-09, -1.71910555e-13, -8979.49283, 8.71043978], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -11.67 kcal/mol (ANL0);  Hf(298 K) = -14.11 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 61,
    label = "CH3CF2",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45976426, 0.0141540616, 8.38306007e-06, -2.1100113e-08, 9.48213486e-12, -3.75291717e+04, 10.6921758], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.0773002, 0.015354419, -7.7727879e-06, 1.90264869e-09, -1.82672143e-13, -3.81793326e+04, 1.14481462], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -68.94 kcal/mol (ANL0);  Hf(298 K) = -71.21 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 62,
    label = "CH2FCHF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {5,S}
3 C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45899346, 0.0157533413, 5.2534284e-06, -1.88664379e-08, 8.9303344e-12, -3.16963262e+04, 11.627709], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.619954, 0.0146879429, -7.41653522e-06, 1.81203596e-09, -1.73738092e-13, -3.24500704e+04, -0.516103993], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -57.38 kcal/mol (ANL0);  Hf(298 K) = -59.52 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 63,
    label = "CHF2CH2",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.76511808, 0.0163495758, 8.49773256e-06, -2.51884652e-08, 1.19965019e-11, -3.55117914e+04, 15.5013946], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.55820386, 0.0145212107, -7.24739474e-06, 1.75572916e-09, -1.67285916e-13, -3.64456099e+04, -0.0320808708], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -65.13 kcal/mol (ANL0);  Hf(298 K) = -67.43 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 64,
    label = "CF3CH2",
    molecule = 
"""
multiplicity 2
1 C u1 p0 c0 {2,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 F u0 p3 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.09580221, 0.0303384395, -2.34025372e-05, 4.68427564e-09, 1.67433249e-12, -6.50778647e+04, 16.1893975], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.07169362, 0.0122373061, -6.3541544e-06, 1.59125788e-09, -1.55790489e-13, -6.65467046e+04, -14.0251192], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -123.74 kcal/mol (ANL0);  Hf(298 K) = -125.79 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 65,
    label = "CHF2CHF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {6,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80702929, 0.0187048079, 1.61446139e-06, -1.81861109e-08, 9.36125029e-12, -5.72588737e+04, 11.3250733], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.4668478, 0.0131837875, -6.92336097e-06, 1.74579988e-09, -1.71636232e-13, -5.83886416e+04, -8.4268744], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -108.09 kcal/mol (ANL0);  Hf(298 K) = -109.91 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 66,
    label = "CH2FCF2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u1 p0 c0 {2,S} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.60375057, 3.64281277e-03, 3.91252701e-05, -5.65581984e-08, 2.34064846e-11, -5.71366676e+04, 4.14129025], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.01420683, 0.0138499245, -7.31037847e-06, 1.84831037e-09, -1.81943528e-13, -5.80560718e+04, -6.16281306], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -107.70 kcal/mol (ANL0);  Hf(298 K) = -109.41 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 67,
    label = "CHF2CF2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.21463277, 0.0209918662, -2.32359766e-06, -1.5107743e-08, 8.29130889e-12, -8.18646205e+04, 10.4386632], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.79168029, 0.0126963711, -7.10626583e-06, 1.87523515e-09, -1.90553485e-13, -8.32490698e+04, -14.0321589], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -156.96 kcal/mol (ANL0);  Hf(298 K) = -158.42 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 68,
    label = "CF3CHF",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 F u0 p3 c0 {3,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.45798032, 0.0345654163, -3.31883371e-05, 1.40035899e-08, -1.67100893e-12, -8.58261797e+04, 16.3358705], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.50565093, 0.0115629405, -6.41551346e-06, 1.68545277e-09, -1.70890287e-13, -8.75173765e+04, -19.0006334], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -164.97 kcal/mol (ANL0);  Hf(298 K) = -166.58 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 69,
    label = "CF3CF2",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 F u0 p3 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.23382501, 0.0425452992, -5.01471841e-05, 2.91419877e-08, -6.76596452e-12, -1.09892817e+05, 17.6565538], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.2572121, 0.0104311142, -6.20931061e-06, 1.70753469e-09, -1.78587071e-13, -1.11963932e+05, -27.0315744], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -212.77 kcal/mol (ANL0);  Hf(298 K) = -214.07 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 70,
    label = "CH3CH2F",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 F u0 p3 c0 {2,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.36377264, -2.79020056e-03, 5.80468023e-05, -7.26587306e-08, 2.83689368e-11, -3.43006441e+04, 5.82425605], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.37883757, 0.0209839495, -1.02288625e-05, 2.42285547e-09, -2.26199391e-13, -3.44955984e+04, 12.0209728], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -61.50 kcal/mol (ANL0);  Hf(298 K) = -65.06 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 71,
    label = "CH3CHF2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.3272463, 0.0109799745, 2.83727758e-05, -4.57828776e-08, 1.92990479e-11, -6.21605541e+04, 10.8359937], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[4.51829704, 0.019162071, -9.58648674e-06, 2.32356332e-09, -2.2127764e-13, -6.29121106e+04, 2.25064256], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -116.92 kcal/mol (ANL0);  Hf(298 K) = -120.25 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 72,
    label = "CH2FCH2F",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.22528446, -3.13621476e-03, 6.06721539e-05, -7.63917047e-08, 2.98135494e-11, -5.5664739e+04, 3.71142772], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.81767396, 0.0204835793, -1.04329104e-05, 2.56082124e-09, -2.46095886e-13, -5.60915399e+04, 6.56499729], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -103.79 kcal/mol (ANL0);  Hf(298 K) = -107.01 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 73,
    label = "CH3CF3",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 F u0 p3 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.77828794, 0.0296066498, -1.24802688e-05, -8.45330372e-09, 6.7032487e-12, -9.21812852e+04, 16.1933261], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.02309079, 0.0168661977, -8.68028218e-06, 2.15494307e-09, -2.09335439e-13, -9.35920691e+04, -11.0039659], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -176.70 kcal/mol (ANL0);  Hf(298 K) = -179.76 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 74,
    label = "CH2FCHF2",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.11145175, 0.0117798661, 2.88369883e-05, -4.77986539e-08, 2.01956914e-11, -8.21468342e+04, 9.49375368], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.37835683, 0.0180718067, -9.47491384e-06, 2.38393507e-09, -2.33841145e-13, -8.32488163e+04, -4.92160795], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -156.49 kcal/mol (ANL0);  Hf(298 K) = -159.43 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 75,
    label = "CH2FCF3",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 F u0 p3 c0 {3,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.84448269, 0.0260510193, 1.25553047e-06, -2.59425951e-08, 1.37994441e-11, -1.11096479e+05, 14.2339523], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.79646671, 0.015730004, -8.48188814e-06, 2.18081889e-09, -2.17519966e-13, -1.1286961e+05, -17.5614023], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -214.14 kcal/mol (ANL0);  Hf(298 K) = -216.85 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 76,
    label = "CHF2CHF2",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.22330378, 0.0387444106, -4.0051341e-05, 2.26128125e-08, -5.50757298e-12, -1.07842854e+05, 15.7218272], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.74990736, 0.0158549535, -8.57018741e-06, 2.2074289e-09, -2.20489502e-13, -1.09374518e+05, -16.7334492], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -207.71 kcal/mol (ANL0);  Hf(298 K) = -210.19 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 77,
    label = "CHF2CF3",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 F u0 p3 c0 {4,S}
8 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5957941, 0.0357554262, -2.10410865e-05, -4.93611638e-09, 6.48225818e-12, -1.3587778e+05, 15.6633868], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.7606307, 0.0142024753, -8.01995976e-06, 2.13078673e-09, -2.17657283e-13, -1.38033259e+05, -26.3755741], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -263.36 kcal/mol (ANL0);  Hf(298 K) = -265.71 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 78,
    label = "CF3CF3",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6 F u0 p3 c0 {5,S}
7 F u0 p3 c0 {5,S}
8 F u0 p3 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.4661718, 0.0522609274, -5.77370562e-05, 2.89155609e-08, -5.05354049e-12, -1.63498853e+05, 18.3012609], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[13.2672643, 0.0120044311, -7.20108833e-06, 1.99036093e-09, -2.08904608e-13, -1.66254647e+05, -40.4653778], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -318.31 kcal/mol (ANL0);  Hf(298 K) = -320.33 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 79,
    label = "CF2CHO",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u0 p0 c0 {2,D} {4,S} {5,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.33083359, 0.0201592443, -1.04151151e-05, -1.93692805e-09, 2.50011651e-12, -4.66211337e+04, 11.6971771], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.84242846, 0.0117781512, -6.51507689e-06, 1.70482978e-09, -1.72181373e-13, -4.76181747e+04, -6.67483176], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) =  -87.97 kcal/mol (ANL0);  Hf(298 K) = -89.08 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 80,
    label = "CF3CO",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 O u0 p2 c0 {6,D}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u1 p0 c0 {4,D} {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.47266847, 0.0306829499, -3.24991738e-05, 1.66341428e-08, -3.26376621e-12, -7.44645031e+04, 16.7192915], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.71986761, 9.52904505e-03, -5.58348726e-06, 1.51907302e-09, -1.57677262e-13, -7.59490957e+04, -14.4769354], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) =  -143.73 kcal/mol (ANL0);  Hf(298 K) = -144.31 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 81,
    label = "CF2CFO",
    molecule = 
"""
multiplicity 2
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63301884, 0.0279611995, -2.99996935e-05, 1.69928295e-08, -4.13170259e-12, -7.53362003e+04, 12.5018934], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.92401195, 9.92185214e-03, -5.80362067e-06, 1.57692944e-09, -1.63521017e-13, -7.66125386e+04, -13.9590933], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) =  -145.07 kcal/mol (ANL0);  Hf(298 K) = -145.55 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 82,
    label = "CF3CHO",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 F u0 p3 c0 {3,S}
5 F u0 p3 c0 {3,S}
6 F u0 p3 c0 {3,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62918372, 0.0225901469, -6.17391734e-06, -1.08218981e-08, 6.64713157e-12, -9.49750105e+04, 11.1327884], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.08778557, 0.013551239, -7.55366829e-06, 1.98661484e-09, -2.01324393e-13, -9.62866784e+04, -12.494749], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) =  -183.03 kcal/mol (ANL0);  Hf(298 K) = -184.73 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 83,
    label = "CF3CFO",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 F u0 p3 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.1326305, 0.0328571031, -2.83102366e-05, 8.88924879e-09, 1.10706912e-13, -1.2488217e+05, 13.8855197], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.0949054, 0.0118266899, -6.9325105e-06, 1.88610627e-09, -1.95738381e-13, -1.26643072e+05, -21.4556292], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) =  -242.49 kcal/mol (ANL0);  Hf(298 K) = -243.87 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 83,
    label = "CH2FCH2OH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4 F u0 p3 c0 {3,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {3,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.297672278, 0.0483976547, -5.31458694e-05, 2.81850193e-08, -4.96136891e-12, -5.22654078e+04, 24.6832972], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.58686327, 0.0166034263, -7.54929443e-06, 1.68681256e-09, -1.50044265e-13, -5.37894007e+04, -13.1552995], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) =  -96.76 kcal/mol (ANL0);  Hf(298 K) = -100.59 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 84,
    label = "CH3CF2OH",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 O u0 p2 c0 {2,S} {9,S}
4 F u0 p3 c0 {2,S}
5 F u0 p3 c0 {2,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {1,S}
9 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.239353165, 0.0454948588, -3.54524804e-05, 2.72975026e-09, 6.02767798e-12, -8.92050636e+04, 23.0924952], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.86403558, 0.0144841358, -6.69273287e-06, 1.52134821e-09, -1.37626893e-13, -9.13758056e+04, -24.8174793], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) =  -170.00 kcal/mol (ANL0);  Hf(298 K) = -173.72 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 85,
    label = "CF3C(O)OH",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {8,S}
4 C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
7 F u0 p3 c0 {4,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.0435424, 0.0304394678, 1.70910981e-06, -3.26143026e-08, 1.73541771e-11, -1.25309934e+05, 19.5016045], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.3983389, 0.0155451203, -9.30450851e-06, 2.56055653e-09, -2.67512617e-13, -1.27815727e+05, -25.1296592], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) =  -242.61 kcal/mol (ANL0);  Hf(298 K) = -245.20 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 86,
    label = "CH2FO",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 O u1 p2 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51173748, -1.02759204e-03, 3.7772683e-05, -5.03538608e-08, 2.03525667e-11, -2.59081995e+04, 9.9428871], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.5991551, 0.0111414547, -5.78826098e-06, 1.44369781e-09, -1.40512315e-13, -2.64105997e+04, 6.80786967], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -47.23 kcal/mol (ANL0);  Hf(298 K) = -49.01 (kcal/mol). partition function via MESS, conversion via automech.""",
)

entry(
    index = 87,
    label = "CHF2OH",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3 F u0 p3 c0 {2,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.102106721, 0.0370259976, -4.57075251e-05, 2.68131483e-08, -5.6213938e-12, -8.23336712e+04, 23.4364578], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[7.16857891, 8.678821e-03, -4.10265706e-06, 9.56271284e-10, -8.86803842e-14, -8.37371679e+04, -10.5964795], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u""" """,
    longDesc = u"""Hf(0 K) = -158.71 kcal/mol (ANL0);  Hf(298 K) = -160.99 (kcal/mol). partition function via MESS, conversion via automech."""
)