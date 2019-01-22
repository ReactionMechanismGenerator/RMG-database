#!/usr/bin/env python
# encoding: utf-8

name = "chlorines_ccsd(t)23"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "2-CHLOROETHANOL",
    molecule =
"""
1 Cl u0 p3 c0 {4,S}
2 O  u0 p2 c0 {3,S} {9,S}
3 C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 C  u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {4,S}
9 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96267,0.00250254,0.0001004,-2.08861e-07,1.4101e-10,-35043.3,9.67316], Tmin=(10,'K'), Tmax=(429.9,'K')),
            NASAPolynomial(coeffs=[1.42865,0.031442,-1.92828e-05,5.74934e-09,-6.63849e-13,-34875,19.1829], Tmin=(429.9,'K'), Tmax=(3000,'K')),
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
    index = 1,
    label = "1,1,2-trichloroethene",
    molecule =
"""
1 Cl u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {4,S}
4 C  u0 p0 c0 {3,S} {5,D} {6,S}
5 C  u0 p0 c0 {1,S} {2,S} {4,D}
6 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84377,0.0112638,9.15468e-05,-2.82796e-07,2.37448e-10,-3429.34,11.7931], Tmin=(10,'K'), Tmax=(435.38,'K')),
            NASAPolynomial(coeffs=[5.80337,0.0174021,-1.27767e-05,4.30722e-09,-5.40732e-13,-3828.78,1.34095], Tmin=(435.38,'K'), Tmax=(3000,'K')),
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
    label = "Chlorobenzene",
    molecule =
"""
1  Cl u0 p3 c0 {5,S}
2  C  u0 p0 c0 {3,D} {7,S} {8,S}
3  C  u0 p0 c0 {2,D} {4,S} {9,S}
4  C  u0 p0 c0 {3,S} {5,D} {10,S}
5  C  u0 p0 c0 {1,S} {4,D} {6,S}
6  C  u0 p0 c0 {5,S} {7,D} {11,S}
7  C  u0 p0 c0 {2,S} {6,D} {12,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {4,S}
11 H  u0 p0 c0 {6,S}
12 H  u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92277,0.00441223,0.000135288,-2.38654e-07,1.29791e-10,3379.02,10.0474], Tmin=(10,'K'), Tmax=(573.76,'K')),
            NASAPolynomial(coeffs=[-0.716947,0.0534581,-3.65937e-05,1.17893e-08,-1.43659e-12,3636.57,27.4584], Tmin=(573.76,'K'), Tmax=(3000,'K')),
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
    label = "Chloroform",
    molecule =
"""
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 Cl u0 p3 c0 {4,S}
4 C  u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91063,0.00580614,6.48188e-05,-1.66225e-07,1.19576e-10,-13793.4,9.93428], Tmin=(10,'K'), Tmax=(499.28,'K')),
            NASAPolynomial(coeffs=[5.19048,0.0130488,-9.5045e-06,3.20096e-09,-4.02723e-13,-14139.3,2.4648], Tmin=(499.28,'K'), Tmax=(3000,'K')),
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
    index = 4,
    label = "1,1,2,2-Tetrachloroethene",
    molecule =
"""
1 Cl u0 p3 c0 {6,S}
2 Cl u0 p3 c0 {6,S}
3 Cl u0 p3 c0 {5,S}
4 Cl u0 p3 c0 {5,S}
5 C  u0 p0 c0 {3,S} {4,S} {6,D}
6 C  u0 p0 c0 {1,S} {2,S} {5,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70011,0.0239185,9.2989e-05,-4.06758e-07,4.10275e-10,-4349.25,11.5632], Tmin=(10,'K'), Tmax=(390.19,'K')),
            NASAPolynomial(coeffs=[7.82628,0.0166022,-1.33719e-05,4.75285e-09,-6.16836e-13,-4937.55,-7.87243], Tmin=(390.19,'K'), Tmax=(3000,'K')),
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
    index = 5,
    label = "COCl",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O  u0 p2 c0 {1,S} {6,S}
3 H  u0 p0 c0 {1,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 Cl u0 p3 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9776,0.0013953,4.67712e-05,-8.68058e-08,5.28053e-11,-9324.26,6.96789], Tmin=(10,'K'), Tmax=(421.43,'K')),
            NASAPolynomial(coeffs=[2.30282,0.0172914,-9.80791e-06,2.69724e-09,-2.89418e-13,-9183.09,13.6006], Tmin=(421.43,'K'), Tmax=(3000,'K')),
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
    index = 6,
    label = "HYPOCHLOROUS ACID",
    molecule =
"""
1 Cl u0 p3 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03079,-0.00251642,2.18686e-05,-3.46004e-08,1.79688e-11,-10607.1,5.45535], Tmin=(10,'K'), Tmax=(613.11,'K')),
            NASAPolynomial(coeffs=[3.54806,0.00400524,-2.33738e-06,6.91397e-10,-7.98051e-14,-10611.3,7.03119], Tmin=(613.11,'K'), Tmax=(3000,'K')),
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
    index = 7,
    label = "[O]CCl",
    molecule =
"""
multiplicity 2
1 Cl u0 p3 c0 {3,S}
2 O  u1 p2 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05829,-0.00572482,7.75455e-05,-1.41953e-07,8.41708e-11,-4028.67,8.73588], Tmin=(10,'K'), Tmax=(537.25,'K')),
            NASAPolynomial(coeffs=[2.70833,0.0149203,-9.67409e-06,2.97993e-09,-3.49878e-13,-4036.51,12.987], Tmin=(537.25,'K'), Tmax=(3000,'K')),
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
    index = 8,
    label = "1,1-Dichloroethene",
    molecule =
"""
1 C  u0 p0 c0 {2,D} {5,S} {6,S}
2 C  u0 p0 c0 {1,D} {3,S} {4,S}
3 Cl u0 p3 c0 {2,S}
4 Cl u0 p3 c0 {2,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93253,0.00400811,6.58594e-05,-1.37304e-07,8.39489e-11,-1428.06,9.18005], Tmin=(10,'K'), Tmax=(562.28,'K')),
            NASAPolynomial(coeffs=[4.12483,0.0179959,-1.24207e-05,4.07912e-09,-5.07992e-13,-1692.42,6.20449], Tmin=(562.28,'K'), Tmax=(3000,'K')),
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
    index = 9,
    label = "ClC=CCl",
    molecule =
"""
1 C  u0 p0 c0 {2,D} {4,S} {5,S}
2 C  u0 p0 c0 {1,D} {3,S} {6,S}
3 Cl u0 p3 c0 {2,S}
4 Cl u0 p3 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92422,0.00537707,7.07249e-05,-1.80966e-07,1.38122e-10,-1702.4,9.17871], Tmin=(10,'K'), Tmax=(440.5,'K')),
            NASAPolynomial(coeffs=[3.78112,0.0181973,-1.21614e-05,3.8488e-09,-4.62444e-13,-1801.57,8.48303], Tmin=(440.5,'K'), Tmax=(3000,'K')),
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
    index = 10,
    label = "Chloromethane",
    molecule =
"""
1 Cl u0 p3 c0 {2,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 H  u0 p0 c0 {2,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07279,-0.00503206,3.97254e-05,-4.88081e-08,1.97839e-11,-11643.1,5.07899], Tmin=(10,'K'), Tmax=(735.68,'K')),
            NASAPolynomial(coeffs=[1.41898,0.0137489,-7.44087e-06,1.97436e-09,-2.05626e-13,-11370.4,16.2671], Tmin=(735.68,'K'), Tmax=(3000,'K')),
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
    index = 11,
    label = "chloro hypochlorite",
    molecule =
"""
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 O  u0 p2 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96253,0.00224266,2.48337e-05,-5.84607e-08,3.77008e-11,8675.61,8.15866], Tmin=(10,'K'), Tmax=(566.96,'K')),
            NASAPolynomial(coeffs=[4.78898,0.00477549,-3.99487e-06,1.45651e-09,-1.92486e-13,8447.47,3.45502], Tmin=(566.96,'K'), Tmax=(3000,'K')),
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
    index = 12,
    label = "Dichloromethane",
    molecule =
"""
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 H  u0 p0 c0 {3,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98208,0.0010405,3.8258e-05,-6.68491e-08,3.66066e-11,-13122.4,8.3197], Tmin=(10,'K'), Tmax=(549.83,'K')),
            NASAPolynomial(coeffs=[2.47086,0.0154372,-1.03002e-05,3.28227e-09,-3.98502e-13,-13007.6,14.2389], Tmin=(549.83,'K'), Tmax=(3000,'K')),
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
    index = 13,
    label = "OOOCl",
    molecule =
"""
1 Cl u0 p3 c0 {4,S}
2 O  u0 p2 c0 {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {5,S}
4 O  u0 p2 c0 {1,S} {2,S}
5 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90584,0.00610057,6.51518e-05,-1.68914e-07,1.21745e-10,3117.59,9.45465], Tmin=(10,'K'), Tmax=(502.42,'K')),
            NASAPolynomial(coeffs=[5.43464,0.0124622,-9.17328e-06,3.13039e-09,-3.97958e-13,2730.06,0.803552], Tmin=(502.42,'K'), Tmax=(3000,'K')),
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
    index = 14,
    label = "Tetrachloromethane",
    molecule =
"""
1 Cl u0 p3 c0 {5,S}
2 Cl u0 p3 c0 {5,S}
3 Cl u0 p3 c0 {5,S}
4 Cl u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79559,0.014499,9.39786e-05,-3.22785e-07,2.78638e-10,-12629.7,9.50108], Tmin=(10,'K'), Tmax=(446.1,'K')),
            NASAPolynomial(coeffs=[7.99397,0.0110431,-9.35984e-06,3.44291e-09,-4.57974e-13,-13344.5,-11.1777], Tmin=(446.1,'K'), Tmax=(3000,'K')),
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
    index = 15,
    label = "chlorine superoxide",
    molecule =
"""
multiplicity 2
1 Cl u0 p3 c0 {2,S}
2 O  u0 p2 c0 {1,S} {3,S}
3 O  u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95764,0.00298609,2.46797e-05,-7.39934e-08,6.01097e-11,13199.7,8.48157], Tmin=(10,'K'), Tmax=(450.47,'K')),
            NASAPolynomial(coeffs=[4.52564,0.00471255,-3.61199e-06,1.23791e-09,-1.56433e-13,13079.8,5.43185], Tmin=(450.47,'K'), Tmax=(3000,'K')),
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
    index = 16,
    label = "1,1,2-TRICHLOROETHANE",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3 Cl u0 p3 c0 {2,S}
4 Cl u0 p3 c0 {2,S}
5 Cl u0 p3 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {1,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83737,0.0115009,0.000123581,-3.5414e-07,2.88225e-10,-19596.7,11.3636], Tmin=(10,'K'), Tmax=(437.79,'K')),
            NASAPolynomial(coeffs=[5.52286,0.0241876,-1.61205e-05,5.14085e-09,-6.26078e-13,-20013.4,1.55032], Tmin=(437.79,'K'), Tmax=(3000,'K')),
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
    index = 17,
    label = "1,2-dichloroethane",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2 C  u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3 Cl u0 p3 c0 {1,S}
4 Cl u0 p3 c0 {2,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88788,0.0135167,1.832e-05,-3.18984e-08,1.31023e-11,-18788.2,9.51334], Tmin=(10,'K'), Tmax=(870.32,'K')),
            NASAPolynomial(coeffs=[3.75936,0.0228364,-1.27869e-05,3.45339e-09,-3.62735e-13,-19096.4,8.21626], Tmin=(870.32,'K'), Tmax=(3000,'K')),
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
    index = 18,
    label = "ACETYL CHLORIDE",
    molecule =
"""
1 Cl u0 p3 c0 {4,S}
2 O  u0 p2 c0 {4,D}
3 C  u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C  u0 p0 c0 {1,S} {2,D} {3,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94702,0.00393052,8.68729e-05,-2.22993e-07,1.81421e-10,-31494,8.30063], Tmin=(10,'K'), Tmax=(385.86,'K')),
            NASAPolynomial(coeffs=[3.00136,0.0217322,-1.34237e-05,4.01561e-09,-4.64869e-13,-31480.5,11.1908], Tmin=(385.86,'K'), Tmax=(3000,'K')),
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
    index = 19,
    label = "hydroxy hypochlorite",
    molecule =
"""
1 Cl u0 p3 c0 {3,S}
2 O  u0 p2 c0 {3,S} {4,S}
3 O  u0 p2 c0 {1,S} {2,S}
4 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98181,0.00101072,2.24062e-05,-4.0367e-08,2.17718e-11,-294.982,7.81187], Tmin=(10,'K'), Tmax=(614.14,'K')),
            NASAPolynomial(coeffs=[3.58774,0.00803393,-5.63248e-06,1.88575e-09,-2.38136e-13,-330.623,8.83666], Tmin=(614.14,'K'), Tmax=(3000,'K')),
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
    index = 20,
    label = "OCCl",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 O  u0 p2 c0 {1,S} {6,S}
3 Cl u0 p3 c0 {1,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.98417,0.000962557,4.78781e-05,-8.45719e-08,4.8323e-11,-31768.1,7.95033], Tmin=(10,'K'), Tmax=(453.08,'K')),
            NASAPolynomial(coeffs=[1.93598,0.0190603,-1.20884e-05,3.7382e-09,-4.45922e-13,-31582.6,16.2084], Tmin=(453.08,'K'), Tmax=(3000,'K')),
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
    index = 21,
    label = "1,1,1,2,2,2-Hexachloroethane",
    molecule =
"""
1 Cl u0 p3 c0 {8,S}
2 Cl u0 p3 c0 {8,S}
3 Cl u0 p3 c0 {8,S}
4 Cl u0 p3 c0 {7,S}
5 Cl u0 p3 c0 {7,S}
6 Cl u0 p3 c0 {7,S}
7 C  u0 p0 c0 {4,S} {5,S} {6,S} {8,S}
8 C  u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4567,0.0435224,0.000143748,-6.85807e-07,7.08797e-10,-19961.4,11.4003], Tmin=(10,'K'), Tmax=(389.79,'K')),
            NASAPolynomial(coeffs=[11.5688,0.0231222,-1.95909e-05,7.18024e-09,-9.50229e-13,-21071.3,-26.2173], Tmin=(389.79,'K'), Tmax=(3000,'K')),
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
    index = 22,
    label = "Chloroethene",
    molecule =
"""
1 Cl u0 p3 c0 {3,S}
2 C  u0 p0 c0 {3,D} {4,S} {5,S}
3 C  u0 p0 c0 {1,S} {2,D} {6,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.07725,-0.00719671,9.01503e-05,-1.58718e-07,9.16097e-11,717.982,7.84732], Tmin=(10,'K'), Tmax=(540.62,'K')),
            NASAPolynomial(coeffs=[2.03537,0.0186711,-1.14775e-05,3.42025e-09,-3.93115e-13,781.516,14.9881], Tmin=(540.62,'K'), Tmax=(3000,'K')),
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
    index = 23,
    label = "1,1,1-Trichloroethane",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2 C  u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3 Cl u0 p3 c0 {2,S}
4 Cl u0 p3 c0 {2,S}
5 Cl u0 p3 c0 {2,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {1,S}
8 H  u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83732,0.0115054,0.000123584,-3.54226e-07,2.88348e-10,-19595.8,9.16681], Tmin=(10,'K'), Tmax=(437.72,'K')),
            NASAPolynomial(coeffs=[5.52315,0.0241862,-1.61193e-05,5.14044e-09,-6.26023e-13,-20012.4,-0.647002], Tmin=(437.72,'K'), Tmax=(3000,'K')),
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
    index = 24,
    label = "1,1-DICHLOROETHANE",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 Cl u0 p3 c0 {1,S}
4 Cl u0 p3 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93685,0.00422691,9.42987e-05,-2.12962e-07,1.49753e-10,-18621.2,9.1288], Tmin=(10,'K'), Tmax=(455.59,'K')),
            NASAPolynomial(coeffs=[2.76448,0.0261619,-1.62506e-05,4.89341e-09,-5.6991e-13,-18635.2,12.5371], Tmin=(455.59,'K'), Tmax=(3000,'K')),
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
    index = 25,
    label = "chlorooxy hypochlorite",
    molecule =
"""
1 Cl u0 p3 c0 {3,S}
2 Cl u0 p3 c0 {4,S}
3 O  u0 p2 c0 {1,S} {4,S}
4 O  u0 p2 c0 {2,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89962,0.00673556,5.57431e-05,-1.62107e-07,1.25129e-10,14681.1,10.4769], Tmin=(10,'K'), Tmax=(482.83,'K')),
            NASAPolynomial(coeffs=[5.81084,0.00898372,-7.41567e-06,2.66322e-09,-3.46823e-13,14285.8,0.465386], Tmin=(482.83,'K'), Tmax=(3000,'K')),
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
    index = 26,
    label = "Formyl chloride",
    molecule =
"""
1 Cl u0 p3 c0 {3,S}
2 O  u0 p2 c0 {3,D}
3 C  u0 p0 c0 {1,S} {2,D} {4,S}
4 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.03577,-0.00374832,5.07562e-05,-9.49165e-08,5.83579e-11,-23786.5,7.72629], Tmin=(10,'K'), Tmax=(503.66,'K')),
            NASAPolynomial(coeffs=[2.96746,0.0101003,-6.46387e-06,1.96905e-09,-2.29344e-13,-23746.9,11.4721], Tmin=(503.66,'K'), Tmax=(3000,'K')),
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
    index = 27,
    label = "Molecular chlorine",
    molecule =
"""
1 Cl u0 p3 c0 {2,S}
2 Cl u0 p3 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4877,0.000705633,8.16112e-06,-1.80959e-08,1.09714e-11,-1159.78,6.46887], Tmin=(10,'K'), Tmax=(604.05,'K')),
            NASAPolynomial(coeffs=[3.79181,0.00162955,-1.42815e-06,5.38539e-10,-7.29482e-14,-1250.12,4.71139], Tmin=(604.05,'K'), Tmax=(3000,'K')),
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
    index = 28,
    label = "Carbonyl dichloride",
    molecule =
"""
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {4,S}
3 O  u0 p2 c0 {4,D}
4 C  u0 p0 c0 {1,S} {2,S} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.935,0.00400636,4.56696e-05,-1.1006e-07,7.36713e-11,-27968.5,9.26854], Tmin=(10,'K'), Tmax=(540.89,'K')),
            NASAPolynomial(coeffs=[5.12882,0.00909267,-7.02525e-06,2.45185e-09,-3.16132e-13,-28301.2,2.36108], Tmin=(540.89,'K'), Tmax=(3000,'K')),
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
    index = 29,
    label = "Chloroethane",
    molecule =
"""
1 Cl u0 p3 c0 {3,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
4 H  u0 p0 c0 {2,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.00117,-1.36814e-05,6.40164e-05,-9.84599e-08,4.88583e-11,-15835.2,7.13198], Tmin=(10,'K'), Tmax=(574.11,'K')),
            NASAPolynomial(coeffs=[0.630331,0.0269348,-1.54404e-05,4.31283e-09,-4.6979e-13,-15505.2,21.0267], Tmin=(574.11,'K'), Tmax=(3000,'K')),
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
    index = 30,
    label = "[CH2]OCCl",
    molecule =
"""
multiplicity 2
1 Cl u0 p3 c0 {3,S}
2 O  u0 p2 c0 {3,S} {4,S}
3 C  u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4 C  u1 p0 c0 {2,S} {7,S} {8,S}
5 H  u0 p0 c0 {3,S}
6 H  u0 p0 c0 {3,S}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.9196,0.00737042,9.69405e-05,-2.9624e-07,2.99371e-10,-6737.5,9.36813], Tmin=(10,'K'), Tmax=(251.07,'K')),
            NASAPolynomial(coeffs=[2.72772,0.0263593,-1.65071e-05,4.99705e-09,-5.8274e-13,-6677.65,13.4711], Tmin=(251.07,'K'), Tmax=(3000,'K')),
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
    index = 31,
    label = "1-CHLOROPROPANE",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C  u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C  u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  H  u0 p0 c0 {1,S}
5  H  u0 p0 c0 {1,S}
6  Cl u0 p3 c0 {3,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90675,0.0118016,4.57065e-05,-6.44555e-08,2.55593e-11,-19138.1,8.39584], Tmin=(10,'K'), Tmax=(832.76,'K')),
            NASAPolynomial(coeffs=[1.27692,0.0363589,-2.00075e-05,5.34794e-09,-5.58485e-13,-19113.7,18.1192], Tmin=(832.76,'K'), Tmax=(3000,'K')),
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
    index = 32,
    label = "3-Chloro-1-propylene",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C  u0 p0 c0 {1,S} {3,D} {7,S}
3 C  u0 p0 c0 {2,D} {8,S} {9,S}
4 Cl u0 p3 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {3,S}
9 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97149,0.00191961,9.85166e-05,-1.99609e-07,1.33184e-10,-2970.55,9.77927], Tmin=(10,'K'), Tmax=(383.89,'K')),
            NASAPolynomial(coeffs=[1.06611,0.0321979,-1.98124e-05,5.9176e-09,-6.84343e-13,-2747.52,21.0139], Tmin=(383.89,'K'), Tmax=(3000,'K')),
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
    index = 33,
    label = "[O]OC=CCl",
    molecule =
"""
multiplicity 2
1 Cl u0 p3 c0 {5,S}
2 O  u0 p2 c0 {3,S} {4,S}
3 O  u1 p2 c0 {2,S}
4 C  u0 p0 c0 {2,S} {5,D} {6,S}
5 C  u0 p0 c0 {1,S} {4,D} {7,S}
6 H  u0 p0 c0 {4,S}
7 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77969,0.0196671,6.7255e-06,-3.43886e-08,2.10284e-11,9374.08,10.8926], Tmin=(10,'K'), Tmax=(660.35,'K')),
            NASAPolynomial(coeffs=[5.0117,0.0202529,-1.28877e-05,3.86937e-09,-4.43142e-13,9035.88,4.13139], Tmin=(660.35,'K'), Tmax=(3000,'K')),
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
    index = 34,
    label = "CC(Cl)OO",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C  u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  O  u0 p2 c0 {1,S} {4,S}
4  O  u0 p2 c0 {3,S} {10,S}
5  Cl u0 p3 c0 {1,S}
6  H  u0 p0 c0 {1,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87227,0.0106078,0.000150076,-4.65551e-07,4.48346e-10,-29196.2,10.3043], Tmin=(10,'K'), Tmax=(335.91,'K')),
            NASAPolynomial(coeffs=[3.12945,0.0342657,-2.17099e-05,6.65414e-09,-7.85109e-13,-29229.9,11.8337], Tmin=(335.91,'K'), Tmax=(3000,'K')),
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
    index = 35,
    label = "OOCCCl",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C  u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  O  u0 p2 c0 {1,S} {4,S}
4  O  u0 p2 c0 {3,S} {10,S}
5  H  u0 p0 c0 {1,S}
6  H  u0 p0 c0 {1,S}
7  Cl u0 p3 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.78178,0.0286623,-1.05469e-05,-1.92983e-09,1.51756e-12,-25743.9,10.5073], Tmin=(10,'K'), Tmax=(1278.7,'K')),
            NASAPolynomial(coeffs=[9.09272,0.0197467,-9.11837e-06,2.03333e-09,-1.77741e-13,-27731.4,-18.8814], Tmin=(1278.7,'K'), Tmax=(3000,'K')),
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
    index = 36,
    label = "2,3-dichloroprop-1-ene",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C  u0 p0 c0 {1,S} {3,D} {7,S}
3 C  u0 p0 c0 {2,D} {8,S} {9,S}
4 Cl u0 p3 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 Cl u0 p3 c0 {2,S}
8 H  u0 p0 c0 {3,S}
9 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86765,0.0103599,0.000100645,-2.5506e-07,1.94577e-10,-7059.13,11.3718], Tmin=(10,'K'), Tmax=(426.59,'K')),
            NASAPolynomial(coeffs=[2.97448,0.0318058,-2.07244e-05,6.43699e-09,-7.63111e-13,-7101.86,13.5259], Tmin=(426.59,'K'), Tmax=(3000,'K')),
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
    index = 37,
    label = "ClC=CCCl",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C  u0 p0 c0 {1,S} {3,D} {7,S}
3 C  u0 p0 c0 {2,D} {8,S} {9,S}
4 Cl u0 p3 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {2,S}
8 Cl u0 p3 c0 {3,S}
9 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76614,0.0227187,6.67133e-06,-2.58353e-08,1.23662e-11,-6345.83,11.4339], Tmin=(10,'K'), Tmax=(830.06,'K')),
            NASAPolynomial(coeffs=[4.83695,0.0261804,-1.51649e-05,4.21634e-09,-4.53779e-13,-6820.62,4.67816], Tmin=(830.06,'K'), Tmax=(3000,'K')),
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
    index = 38,
    label = "[O]OC(Cl)C=O",
    molecule =
"""
multiplicity 2
1 Cl u0 p3 c0 {5,S}
2 O  u0 p2 c0 {4,S} {5,S}
3 O  u0 p2 c0 {6,D}
4 O  u1 p2 c0 {2,S}
5 C  u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
6 C  u0 p0 c0 {3,D} {5,S} {8,S}
7 H  u0 p0 c0 {5,S}
8 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69021,0.0313597,-2.41989e-05,8.72083e-09,-1.10443e-12,-14169.3,inf], Tmin=(10,'K'), Tmax=(1174.04,'K')),
            NASAPolynomial(coeffs=[9.19758,0.0158564,-8.55691e-06,2.2041e-09,-2.20444e-13,-15687.2,inf], Tmin=(1174.04,'K'), Tmax=(3000,'K')),
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
    index = 39,
    label = "OC(Cl)[CH]Cl",
    molecule =
"""
multiplicity 2
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {5,S}
3 O  u0 p2 c0 {4,S} {8,S}
4 C  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
5 C  u1 p0 c0 {2,S} {4,S} {7,S}
6 H  u0 p0 c0 {4,S}
7 H  u0 p0 c0 {5,S}
8 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79583,0.0159195,0.000111112,-3.67845e-07,3.33803e-10,-16299,inf], Tmin=(10,'K'), Tmax=(397.62,'K')),
            NASAPolynomial(coeffs=[5.40744,0.0247873,-1.69544e-05,5.5087e-09,-6.77457e-13,-16625.5,inf], Tmin=(397.62,'K'), Tmax=(3000,'K')),
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
    index = 40,
    label = "1,2,3-Trichloropropane",
    molecule =
"""
1  Cl u0 p3 c0 {4,S}
2  Cl u0 p3 c0 {5,S}
3  Cl u0 p3 c0 {6,S}
4  C  u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C  u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
6  C  u0 p0 c0 {3,S} {4,S} {10,S} {11,S}
7  H  u0 p0 c0 {4,S}
8  H  u0 p0 c0 {5,S}
9  H  u0 p0 c0 {5,S}
10 H  u0 p0 c0 {6,S}
11 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66394,0.0340069,-6.5199e-06,-1.44364e-08,7.66613e-12,-26136.2,12.9307], Tmin=(10,'K'), Tmax=(936.81,'K')),
            NASAPolynomial(coeffs=[6.80466,0.0306538,-1.72543e-05,4.66238e-09,-4.88809e-13,-27166,-4.37182], Tmin=(936.81,'K'), Tmax=(3000,'K')),
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
    index = 41,
    label = "CC=CCl",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C  u0 p0 c0 {1,S} {3,D} {7,S}
3 C  u0 p0 c0 {2,D} {8,S} {9,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 H  u0 p0 c0 {2,S}
8 Cl u0 p3 c0 {3,S}
9 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96954,0.00186044,7.84922e-05,-1.40952e-07,8.25212e-11,-2988.24,8.10831], Tmin=(10,'K'), Tmax=(439.33,'K')),
            NASAPolynomial(coeffs=[0.868142,0.0300851,-1.78309e-05,5.14762e-09,-5.78831e-13,-2715.61,20.5212], Tmin=(439.33,'K'), Tmax=(3000,'K')),
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
    index = 42,
    label = "1-chloroethanol",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 O  u0 p2 c0 {1,S} {9,S}
4 Cl u0 p3 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {2,S}
9 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93757,0.0040524,0.000101463,-2.16339e-07,1.44511e-10,-37547.5,9.32801], Tmin=(10,'K'), Tmax=(474.21,'K')),
            NASAPolynomial(coeffs=[2.30602,0.0298517,-1.82195e-05,5.44577e-09,-6.32889e-13,-37528.1,14.555], Tmin=(474.21,'K'), Tmax=(3000,'K')),
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
    index = 43,
    label = "2-CHLOROPROPANE",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  Cl u0 p3 c0 {1,S}
5  H  u0 p0 c0 {1,S}
6  H  u0 p0 c0 {2,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {3,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93313,0.00456923,0.000111632,-2.31062e-07,1.57688e-10,-20611.3,7.24901], Tmin=(10,'K'), Tmax=(374.14,'K')),
            NASAPolynomial(coeffs=[0.830837,0.0377362,-2.13405e-05,5.87454e-09,-6.32054e-13,-20379.2,19.1658], Tmin=(374.14,'K'), Tmax=(3000,'K')),
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
    index = 44,
    label = "COOCCl",
    molecule =
"""
1  C  u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C  u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
3  O  u0 p2 c0 {1,S} {4,S}
4  O  u0 p2 c0 {2,S} {3,S}
5  Cl u0 p3 c0 {2,S}
6  H  u0 p0 c0 {1,S}
7  H  u0 p0 c0 {1,S}
8  H  u0 p0 c0 {1,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82135,0.0245977,1.02703e-06,-1.32699e-08,5.25205e-12,-22547.7,9.347], Tmin=(10,'K'), Tmax=(1106.58,'K')),
            NASAPolynomial(coeffs=[6.67475,0.0243716,-1.23414e-05,3.02265e-09,-2.90071e-13,-23796.8,-7.49883], Tmin=(1106.58,'K'), Tmax=(3000,'K')),
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
    index = 45,
    label = "chloro-hydroperoxymethane",
    molecule =
"""
1 Cl u0 p3 c0 {4,S}
2 O  u0 p2 c0 {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {7,S}
4 C  u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 H  u0 p0 c0 {4,S}
6 H  u0 p0 c0 {4,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93288,0.004695,8.26566e-05,-1.99736e-07,1.48451e-10,-22989.1,9.53449], Tmin=(10,'K'), Tmax=(437.13,'K')),
            NASAPolynomial(coeffs=[3.19942,0.0221717,-1.42551e-05,4.40338e-09,-5.2083e-13,-23027.9,11.2896], Tmin=(437.13,'K'), Tmax=(3000,'K')),
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
    index = 46,
    label = "2-CHLOROACETALDEHYDE",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C  u0 p0 c0 {1,S} {6,D} {7,S}
3 Cl u0 p3 c0 {1,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 O  u0 p2 c0 {2,D}
7 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95104,0.0124369,8.90284e-06,-1.63649e-08,5.94956e-12,-23791,9.55835], Tmin=(10,'K'), Tmax=(1057.72,'K')),
            NASAPolynomial(coeffs=[5.25246,0.0160199,-8.2391e-06,2.04117e-09,-1.97559e-13,-24542.1,0.95782], Tmin=(1057.72,'K'), Tmax=(3000,'K')),
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
    index = 47,
    label = "1,3-Dichloropropane",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C  u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C  u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
4  H  u0 p0 c0 {1,S}
5  H  u0 p0 c0 {1,S}
6  Cl u0 p3 c0 {2,S}
7  Cl u0 p3 c0 {3,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83901,0.0204099,2.66493e-05,-4.62394e-08,1.87518e-11,-22823.6,10.9819], Tmin=(10,'K'), Tmax=(886.7,'K')),
            NASAPolynomial(coeffs=[3.82449,0.0339018,-1.88874e-05,5.07394e-09,-5.3028e-13,-23348.8,8.07383], Tmin=(886.7,'K'), Tmax=(3000,'K')),
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
    index = 48,
    label = "1,2-dichloro-1-hydroperoxyethane",
    molecule =
"""
1  Cl u0 p3 c0 {5,S}
2  Cl u0 p3 c0 {6,S}
3  O  u0 p2 c0 {4,S} {5,S}
4  O  u0 p2 c0 {3,S} {10,S}
5  C  u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
6  C  u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
7  H  u0 p0 c0 {5,S}
8  H  u0 p0 c0 {6,S}
9  H  u0 p0 c0 {6,S}
10 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.68849,0.0298009,5.9998e-05,-2.7807e-07,3.02416e-10,-30763.4,inf], Tmin=(10,'K'), Tmax=(332.15,'K')),
            NASAPolynomial(coeffs=[4.29537,0.0354356,-2.38994e-05,7.6383e-09,-9.26458e-13,-30875.1,inf], Tmin=(332.15,'K'), Tmax=(3000,'K')),
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
    index = 49,
    label = "chloromethyl hypochlorite",
    molecule =
"""
1 Cl u0 p3 c0 {4,S}
2 Cl u0 p3 c0 {3,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 C  u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
5 H  u0 p0 c0 {4,S}
6 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90342,0.00815592,3.84718e-05,-8.53255e-08,5.27444e-11,-13211.6,10.435], Tmin=(10,'K'), Tmax=(550.06,'K')),
            NASAPolynomial(coeffs=[3.70174,0.0181044,-1.17877e-05,3.62242e-09,-4.23654e-13,-13317.8,10.1211], Tmin=(550.06,'K'), Tmax=(3000,'K')),
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
    index = 50,
    label = "2-chloroprop-1-ene",
    molecule =
"""
1 C  u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C  u0 p0 c0 {1,S} {3,D} {7,S}
3 C  u0 p0 c0 {2,D} {8,S} {9,S}
4 H  u0 p0 c0 {1,S}
5 H  u0 p0 c0 {1,S}
6 H  u0 p0 c0 {1,S}
7 Cl u0 p3 c0 {2,S}
8 H  u0 p0 c0 {3,S}
9 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95,0.00313071,9.51081e-05,-1.87678e-07,1.16984e-10,-5018.65,8.07954], Tmin=(10,'K'), Tmax=(495.01,'K')),
            NASAPolynomial(coeffs=[1.68024,0.0311577,-1.91705e-05,5.75717e-09,-6.71385e-13,-4912.61,16.2351], Tmin=(495.01,'K'), Tmax=(3000,'K')),
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
    index = 51,
    label = "OC=CCl",
    molecule =
"""
1 C  u0 p0 c0 {2,D} {3,S} {4,S}
2 C  u0 p0 c0 {1,D} {5,S} {6,S}
3 O  u0 p2 c0 {1,S} {7,S}
4 H  u0 p0 c0 {1,S}
5 Cl u0 p3 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91534,0.00639264,8.40744e-05,-2.27428e-07,1.86899e-10,-19228,9.05902], Tmin=(10,'K'), Tmax=(401.55,'K')),
            NASAPolynomial(coeffs=[3.53253,0.0213866,-1.37008e-05,4.24039e-09,-5.03556e-13,-19287.4,9.43419], Tmin=(401.55,'K'), Tmax=(3000,'K')),
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
    index = 52,
    label = "1,2-Dichloropropane",
    molecule =
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C  u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3  C  u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
4  Cl u0 p3 c0 {1,S}
5  H  u0 p0 c0 {1,S}
6  Cl u0 p3 c0 {3,S}
7  H  u0 p0 c0 {2,S}
8  H  u0 p0 c0 {2,S}
9  H  u0 p0 c0 {2,S}
10 H  u0 p0 c0 {3,S}
11 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76822,0.0206195,4.82282e-05,-1.17903e-07,8.036e-11,-23763.2,11.3115], Tmin=(10,'K'), Tmax=(384.88,'K')),
            NASAPolynomial(coeffs=[1.98736,0.039128,-2.3906e-05,7.0449e-09,-8.01446e-13,-23626.2,18.2027], Tmin=(384.88,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc =
u"""

""",
)
