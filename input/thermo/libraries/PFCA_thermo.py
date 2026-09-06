#!/usr/bin/env python
# encoding: utf-8

name = "PFCA_thermo"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "HF",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-962.551,24.8316,3.2682,0.00103959,-2.2605e-06,2.27932e-09,-7.21878e-13,-33951,2.12947], Tmin=(100,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[725509,-1485.62,3.85873,0.00071085,-2.09543e-07,3.03112e-11,-1.63173e-15,-23482.3,-3.2241], Tmin=(1000,'K'), Tmax=(6000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (6000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """polynomial from ATcT.""",
    longDesc = 
"""

""",
)

entry(
    index = 1,
    label = "FC_O_OH",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {5,S}
4 F u0 p3 c0 {2,S}
5 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.697783,0.0285739,-3.24394e-05,1.82244e-08,-3.96446e-12,-74951.3,21.0926], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[6.02782,0.00900158,-5.18115e-06,1.38568e-09,-1.41746e-13,-76136.1,-5.12554], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 2,
    label = "CF3C_O_OH",
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
            NASAPolynomial(coeffs=[2.04354,0.0304395,1.70911e-06,-3.26143e-08,1.73542e-11,-125707,19.5016], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.3983,0.0155451,-9.30451e-06,2.56056e-09,-2.67513e-13,-128213,-25.1297], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 3,
    label = "C2F5C_O_OH",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {11,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 F u0 p3 c0 {7,S}
11 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.200951,0.0748973,-7.98183e-05,3.64531e-08,-4.79392e-12,-176615,28.2351], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[16.9329,0.0180874,-1.07005e-05,2.92324e-09,-3.03981e-13,-180496,-55.0398], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 4,
    label = "C3F7C_O_OH",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {14,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 F u0 p3 c0 {10,S}
14 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.97805,0.0908073,-9.52988e-05,4.33466e-08,-5.91363e-12,-227611,22.7633], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[22.1912,0.0231732,-1.38588e-05,3.81222e-09,-3.98245e-13,-232374,-78.1509], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 5,
    label = "C4F9C_O_OH",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {17,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 F u0 p3 c0 {13,S}
17 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.80783,0.101516,-9.93114e-05,3.87227e-08,-2.79106e-12,-278426,11.7092], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[27.8292,0.0276128,-1.66008e-05,4.58228e-09,-4.79853e-13,-283993,-103.967], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 6,
    label = "C5F11C_O_OH",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {20,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 F u0 p3 c0 {16,S}
20 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.55638,0.144984,-0.00018531,1.16187e-07,-2.89681e-11,-329072,10.227], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[35.4063,0.0294291,-1.77941e-05,4.92571e-09,-5.16737e-13,-335858,-141.105], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 7,
    label = "C6F13C_O_OH",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {23,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 C u0 p0 c0 {16,S} {20,S} {21,S} {22,S}
20 F u0 p3 c0 {19,S}
21 F u0 p3 c0 {19,S}
22 F u0 p3 c0 {19,S}
23 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.89167,0.194213,-0.000282543,2.03943e-07,-5.8682e-11,-379597,15.9928], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[42.7268,0.0313233,-1.88915e-05,5.20874e-09,-5.44413e-13,-387815,-176.404], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 8,
    label = "C7F15C_O_OH",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {26,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 C u0 p0 c0 {16,S} {20,S} {21,S} {22,S}
20 F u0 p3 c0 {19,S}
21 F u0 p3 c0 {19,S}
22 C u0 p0 c0 {19,S} {23,S} {24,S} {25,S}
23 F u0 p3 c0 {22,S}
24 F u0 p3 c0 {22,S}
25 F u0 p3 c0 {22,S}
26 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-0.975636,0.257033,-0.000412784,3.26331e-07,-1.01484e-10,-429914,31.6971], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[48.6116,0.0364454,-2.27078e-05,6.46842e-09,-6.97825e-13,-439424,-203.866], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 9,
    label = "c_CF2OC_O",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 F u0 p3 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.0518,0.0368731,-4.20264e-05,2.38288e-08,-5.38233e-12,-70987.6,20.7329], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.46107,0.0105449,-6.1603e-06,1.67268e-09,-1.73378e-13,-72690.9,-15.9702], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 10,
    label = "CF3_c_FCOC_O",
    molecule = 
"""
1 O u0 p2 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7 F u0 p3 c0 {6,S}
8 F u0 p3 c0 {6,S}
9 F u0 p3 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.30416,0.0615381,-7.4651e-05,4.47855e-08,-1.06954e-11,-124632,21.2722], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[14.0809,0.014787,-8.72266e-06,2.38456e-09,-2.48395e-13,-127498,-41.6774], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 11,
    label = "C2F5_c_FCOC_O",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 F u0 p3 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.84785,0.0882158,-0.000116517,7.7718e-08,-2.10043e-11,-175742,21.2138], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[19.9032,0.0187391,-1.11132e-05,3.04911e-09,-3.1843e-13,-179664,-67.0156], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 12,
    label = "C3F7_c_FCOC_O",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 F u0 p3 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40388,0.105607,-0.000136555,8.96385e-08,-2.39955e-11,-225713,16.4274], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[25.0225,0.0237015,-1.40922e-05,3.87205e-09,-4.0474e-13,-230476,-89.5435], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 13,
    label = "C4F9_c_FCOC_O",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u0 p0 c0 {12,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 F u0 p3 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.02946,0.154161,-0.000218563,1.50662e-07,-4.07541e-11,-276040,25.1652], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[33.0247,0.0245094,-1.45901e-05,4.01092e-09,-4.19405e-13,-282604,-129.385], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 14,
    label = "C5F11_c_FCOC_O",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u0 p0 c0 {12,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 F u0 p3 c0 {18,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.54975,0.146206,-0.000187009,1.19121e-07,-3.05406e-11,-326259,4.44267], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[36.9325,0.0319167,-1.93603e-05,5.41238e-09,-5.75029e-13,-332946,-144.558], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 15,
    label = "C6F13_c_FCOC_O",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u0 p0 c0 {12,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 C u0 p0 c0 {15,S} {19,S} {20,S} {21,S}
19 F u0 p3 c0 {18,S}
20 F u0 p3 c0 {18,S}
21 C u0 p0 c0 {18,S} {22,S} {23,S} {24,S}
22 F u0 p3 c0 {21,S}
23 F u0 p3 c0 {21,S}
24 F u0 p3 c0 {21,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.03708,0.177666,-0.000239799,1.61786e-07,-4.39738e-11,-375667,1.9693], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[43.9773,0.0343004,-2.06756e-05,5.711e-09,-5.97336e-13,-383623,-178.22], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 16,
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
            NASAPolynomial(coeffs=[2.21606,0.0132381,-4.23785e-06,-6.67864e-09,4.3791e-12,-74140.5,14.773], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.20118,0.00661606,-3.82472e-06,1.03037e-09,-1.06158e-13,-74982.5,-0.880396], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 17,
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
            NASAPolynomial(coeffs=[3.13263,0.0328571,-2.83102e-05,8.88925e-09,1.10707e-13,-125139,13.8855], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[10.0949,0.0118267,-6.93251e-06,1.88611e-09,-1.95738e-13,-126900,-21.4556], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 18,
    label = "C2F5CFO",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 F u0 p3 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.05484,0.0603756,-6.76072e-05,3.62701e-08,-7.43749e-12,-176118,16.7119], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[15.8721,0.0158662,-9.38402e-06,2.56937e-09,-2.67902e-13,-179097,-46.9877], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 19,
    label = "C3F7CFO",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 F u0 p3 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.3777,0.07762,-8.36693e-05,4.18507e-08,-7.58222e-12,-226258,13.6397], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[21.2722,0.020551,-1.224e-05,3.36539e-09,-3.51851e-13,-230253,-70.6883], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 20,
    label = "C4F9CFO",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 F u0 p3 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[5.66465,0.0985071,-0.000111942,6.16655e-08,-1.33216e-11,-276634,9.48957], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[26.8072,0.0250594,-1.49932e-05,4.13327e-09,-4.32854e-13,-281563,-95.6297], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 21,
    label = "C5F11CFO",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 F u0 p3 c0 {16,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.14701,0.128795,-0.000162695,1.02773e-07,-2.62726e-11,-326688,7.68276], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[33.1902,0.0284053,-1.70712e-05,4.71864e-09,-4.9505e-13,-332719,-125.307], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 22,
    label = "C6F13CFO",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 C u0 p0 c0 {16,S} {20,S} {21,S} {22,S}
20 F u0 p3 c0 {19,S}
21 F u0 p3 c0 {19,S}
22 F u0 p3 c0 {19,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.29024,0.250536,-0.000450355,3.96951e-07,-1.3433e-10,-376401,61.9735], Tmin=(100,'K'), Tmax=(835.14,'K')),
            NASAPolynomial(coeffs=[25.8508,0.0570892,-3.19532e-05,6.31543e-09,-4.38163e-13,-380392,-79.0504], Tmin=(835.14,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """UPDATE RMG""",
    longDesc = 
"""

""",
)

entry(
    index = 23,
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
            NASAPolynomial(coeffs=[1.97198,0.0382622,-5.33417e-05,3.9882e-08,-1.23195e-11,-82774.5,15.3983], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[8.90665,0.00996112,-5.83609e-06,1.58818e-09,-1.64908e-13,-84251.2,-18.2304], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 24,
    label = "CF3CFCF2",
    molecule = 
"""
1 F u0 p3 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,D} {5,S} {6,S}
5 F u0 p3 c0 {4,S}
6 C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7 F u0 p3 c0 {6,S}
8 F u0 p3 c0 {6,S}
9 F u0 p3 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48756,0.0445189,-1.69994e-05,-4.62355e-08,4.1721e-11,-140912,13.4084], Tmin=(10,'K'), Tmax=(600.48,'K')),
            NASAPolynomial(coeffs=[8.64988,0.0279311,-2.00276e-05,6.49183e-09,-7.83507e-13,-141852,-11.5361], Tmin=(600.48,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """Thermophysical properties estimated by RMG.""",
    longDesc = 
"""

""",
)

entry(
    index = 25,
    label = "C2F5CFCF2",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,D} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 F u0 p3 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.52143,0.0767152,-8.69305e-05,4.67022e-08,-9.67042e-12,-192428,14.4819], Tmin=(100,'K'), Tmax=(1186.72,'K')),
            NASAPolynomial(coeffs=[22.5153,0.0126941,-6.00895e-06,1.24292e-09,-9.37946e-14,-196936,-80.4041], Tmin=(1186.72,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """Thermo estimated by RMG.""",
    longDesc = 
"""

""",
)

entry(
    index = 26,
    label = "C3F7CFCF2",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,D} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 F u0 p3 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.49067,0.156349,-0.000272461,2.35798e-07,-7.90237e-11,-242436,40.2194], Tmin=(100,'K'), Tmax=(821.99,'K')),
            NASAPolynomial(coeffs=[18.4245,0.0362786,-1.99729e-05,3.94731e-09,-2.74849e-13,-245257,-52.8257], Tmin=(821.99,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """Thermo estimated by RMG.""",
    longDesc = 
"""

""",
)

entry(
    index = 27,
    label = "C4F9CFCF2",
    molecule = 
"""
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,D} {5,S} {6,S}
5  F u0 p3 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 C u0 p0 c0 {9,S} {13,S} {14,S} {15,S}
13 F u0 p3 c0 {12,S}
14 F u0 p3 c0 {12,S}
15 C u0 p0 c0 {12,S} {16,S} {17,S} {18,S}
16 F u0 p3 c0 {15,S}
17 F u0 p3 c0 {15,S}
18 F u0 p3 c0 {15,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[21.6723,0.0452311,-2.51008e-05,4.95162e-09,-3.43431e-13,-295615,-64.8766], Tmin=(100,'K'), Tmax=(833.61,'K')),
            NASAPolynomial(coeffs=[-4.18356,0.198564,-0.000353669,3.09833e-07,-1.04407e-10,-292321,49.0582], Tmin=(833.61,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """Thermo estimated by RMG.""",
    longDesc = 
"""

""",
)

entry(
    index = 28,
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
            NASAPolynomial(coeffs=[2.46154,0.012951,-2.16597e-06,-9.80605e-09,5.70994e-12,-57563.5,14.0624], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[5.91197,0.00585949,-3.4737e-06,9.5196e-10,-9.92796e-14,-58559.9,-4.16067], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 29,
    label = "C2F5",
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
            NASAPolynomial(coeffs=[2.23383,0.0425453,-5.01472e-05,2.9142e-08,-6.76596e-12,-110109,17.6566], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[11.2572,0.0104311,-6.20931e-06,1.70753e-09,-1.78587e-13,-112180,-27.0316], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, CBH(ANL0), conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 30,
    label = "C2F5CF2",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  F u0 p3 c0 {2,S}
5  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6  F u0 p3 c0 {5,S}
7  F u0 p3 c0 {5,S}
8  C u1 p0 c0 {5,S} {9,S} {10,S}
9  F u0 p3 c0 {8,S}
10 F u0 p3 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.77731,0.053404,-5.11043e-05,1.86249e-08,-7.10595e-13,-161276,8.32897], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[17.1071,0.0143335,-8.56142e-06,2.35918e-09,-2.47062e-13,-164278,-53.737], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, CBH(F12b), conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 31,
    label = "C3F7CF2",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 F u0 p3 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.38422,0.0942548,-0.000117679,6.8937e-08,-1.54917e-11,-213777,15.0073], Tmin=(100,'K'), Tmax=(1097.74,'K')),
            NASAPolynomial(coeffs=[25.7241,0.0128515,-6.44618e-06,1.38447e-09,-1.0724e-13,-218682,-94.8532], Tmin=(1097.74,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """Thermo estimated by RMG.""",
    longDesc = 
"""

""",
)

entry(
    index = 32,
    label = "C4F9CF2",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 F u0 p3 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.3944,0.180663,-0.000328817,2.90654e-07,-9.80932e-11,-259904,44.9439], Tmin=(100,'K'), Tmax=(845.78,'K')),
            NASAPolynomial(coeffs=[19.7078,0.0395518,-2.20624e-05,4.33321e-09,-2.987e-13,-262672,-55.9064], Tmin=(845.78,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """Thermo estimated by RMG.""",
    longDesc = 
"""

""",
)

entry(
    index = 33,
    label = "C5F11CF2",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {2,S}
2  C u1 p0 c0 {1,S} {3,S} {4,S}
3  F u0 p3 c0 {2,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 F u0 p3 c0 {16,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[22.9303,0.0485491,-2.72171e-05,5.34399e-09,-3.67827e-13,-313021,-67.8166], Tmin=(100,'K'), Tmax=(849.23,'K')),
            NASAPolynomial(coeffs=[-5.08115,0.222802,-0.000409742,3.64308e-07,-1.23314e-10,-309789,53.761], Tmin=(849.23,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """Thermo estimated by RMG.""",
    longDesc = 
"""

""",
)

entry(
    index = 34,
    label = "CF2C_O_OH",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {2,S}
2 C u1 p0 c0 {1,S} {3,S} {4,S}
3 F u0 p3 c0 {2,S}
4 C u0 p0 c0 {2,S} {5,S} {6,D}
5 O u0 p2 c0 {4,S} {7,S}
6 O u0 p2 c0 {4,D}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.48397,0.0376948,-3.39511e-05,1.35398e-08,-1.87254e-12,-74956.7,19.4471], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[9.98133,0.0128912,-8.00759e-06,2.2734e-09,-2.43409e-13,-77209.3,-24.0706], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """partition function via MESS, CBH(ANL0), conversion via automech.""",
    longDesc = 
"""

""",
)

entry(
    index = 35,
    label = "CF2CF2C_O_OH",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {10,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u1 p0 c0 {4,S} {8,S} {9,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[0.686509,0.0802268,-0.000133162,1.17087e-07,-4.07343e-11,-125465,27.2941], Tmin=(100,'K'), Tmax=(790.07,'K')),
            NASAPolynomial(coeffs=[9.66133,0.0261567,-1.41185e-05,2.80852e-09,-1.97796e-13,-126614,-12.1845], Tmin=(790.07,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """Thermophysical properties estimated by RMG.""",
    longDesc = 
"""

""",
)

entry(
    index = 36,
    label = "CF2C2F4C_O_OH",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {13,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u1 p0 c0 {7,S} {11,S} {12,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-1.07402,0.12368,-0.000216206,1.91707e-07,-6.59104e-11,-175587,35.8048], Tmin=(100,'K'), Tmax=(821.89,'K')),
            NASAPolynomial(coeffs=[13.4305,0.0342877,-1.87451e-05,3.70559e-09,-2.58425e-13,-177336,-27.4629], Tmin=(821.89,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """Thermophysical properties estimated by RMG.""",
    longDesc = 
"""

""",
)

entry(
    index = 37,
    label = "CF2C3F6C_O_OH",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {16,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u1 p0 c0 {10,S} {14,S} {15,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.76443,0.165863,-0.000297283,2.65545e-07,-9.11955e-11,-225472,44.635], Tmin=(100,'K'), Tmax=(833.82,'K')),
            NASAPolynomial(coeffs=[16.6735,0.0432488,-2.38782e-05,4.71117e-09,-3.27114e-13,-227693,-39.4876], Tmin=(833.82,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """Thermophysical properties estimated by RMG.""",
    longDesc = 
"""

""",
)

entry(
    index = 38,
    label = "CF2C4F8C_O_OH",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {19,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u1 p0 c0 {13,S} {17,S} {18,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.45259,0.208018,-0.000378263,3.39262e-07,-1.16436e-10,-275357,53.4571], Tmin=(100,'K'), Tmax=(840.14,'K')),
            NASAPolynomial(coeffs=[19.9048,0.0522305,-2.90237e-05,5.71972e-09,-3.96053e-13,-278045,-51.4472], Tmin=(840.14,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """Thermophysical properties estimated by RMG.""",
    longDesc = 
"""

""",
)

entry(
    index = 39,
    label = "CF2C5F10C_O_OH",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {22,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 C u1 p0 c0 {16,S} {20,S} {21,S}
20 F u0 p3 c0 {19,S}
21 F u0 p3 c0 {19,S}
22 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.13954,0.250158,-0.00045919,4.12911e-07,-1.41648e-10,-325242,62.2749], Tmin=(100,'K'), Tmax=(844.08,'K')),
            NASAPolynomial(coeffs=[23.1304,0.0612224,-3.41752e-05,6.72972e-09,-4.65115e-13,-328394,-63.3749], Tmin=(844.08,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """Thermophysical properties estimated by RMG.""",
    longDesc = 
"""

""",
)

entry(
    index = 40,
    label = "CF2C6F12C_O_OH",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {25,S}
4  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5  F u0 p3 c0 {4,S}
6  F u0 p3 c0 {4,S}
7  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 C u0 p0 c0 {10,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 C u0 p0 c0 {13,S} {17,S} {18,S} {19,S}
17 F u0 p3 c0 {16,S}
18 F u0 p3 c0 {16,S}
19 C u0 p0 c0 {16,S} {20,S} {21,S} {22,S}
20 F u0 p3 c0 {19,S}
21 F u0 p3 c0 {19,S}
22 C u1 p0 c0 {19,S} {23,S} {24,S}
23 F u0 p3 c0 {22,S}
24 F u0 p3 c0 {22,S}
25 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.82611,0.292294,-0.000540102,4.86542e-07,-1.66856e-10,-375128,71.0914], Tmin=(100,'K'), Tmax=(846.77,'K')),
            NASAPolynomial(coeffs=[26.3535,0.0702187,-3.93293e-05,7.74037e-09,-5.3423e-13,-378743,-75.2884], Tmin=(846.77,'K'), Tmax=(5000,'K')),
        ],
        Tmin = (100,'K'),
        Tmax = (5000,'K'),
    ),
    reference = Reference(authors=['Caroline Rocchio', 'C. Franklin Goldsmith'], title='pfca_final', year='2024'),
    referenceType = "Theory",
    shortDesc = """Thermophysical properties estimated by RMG.""",
    longDesc = 
"""

""",
)

