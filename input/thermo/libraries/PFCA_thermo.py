

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
            NASAPolynomial(coeffs=[-962.551409, 24.83162092, 3.26819899, 0.001039587354, -2.260501733e-06, 2.279324001e-09, -7.21878178e-13, -33951.0025, 2.129465739], Tmin=(100.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[725508.525, -1485.62134, 3.85872564, 0.000710849781, -2.095425721e-07, 3.031118495e-11, -1.631732228e-15, -23482.29903, -3.22409796], Tmin=(1000.0,'K'), Tmax=(6000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (6000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[0.697782922, 0.0285739134, -3.24394422e-05, 1.8224386e-08, -3.96445547e-12, -74951.2994, 21.0926135], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[6.02781603, 0.00900158456, -5.18114686e-06, 1.38567672e-09, -1.41745778e-13, -76136.1312, -5.12554403], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[2.0435424, 0.0304394678, 1.70910981e-06, -3.26143026e-08, 1.73541771e-11, -125707.432, 19.5016045], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[10.3983389, 0.0155451203, -9.30450851e-06, 2.56055653e-09, -2.67512617e-13, -128213.225, -25.1296592], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[0.200950982, 0.0748973361, -7.98183007e-05, 3.6453052e-08, -4.79392345e-12, -176614.689, 28.2351243], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[16.9328776, 0.0180874443, -1.07004707e-05, 2.92324439e-09, -3.03980537e-13, -180496.483, -55.0398361], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[1.97805189, 0.0908073415, -9.52987519e-05, 4.33465546e-08, -5.91363008e-12, -227611.404, 22.7632824], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[22.1912215, 0.0231731686, -1.38587976e-05, 3.81221859e-09, -3.98245074e-13, -232373.632, -78.1508851], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[4.80782611, 0.101515552, -9.93113942e-05, 3.87227357e-08, -2.79106355e-12, -278425.91, 11.7092063], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[27.8291848, 0.027612829, -1.66007836e-05, 4.58227924e-09, -4.79853065e-13, -283993.238, -103.966938], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[4.55638314, 0.144984388, -0.000185309907, 1.161875e-07, -2.89681492e-11, -329072.254, 10.2270189], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[35.4062608, 0.0294290547, -1.77940782e-05, 4.92571498e-09, -5.16736997e-13, -335857.911, -141.104558], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[2.89167285, 0.194212692, -0.000282542699, 2.03943206e-07, -5.86819761e-11, -379596.516, 15.9928356], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[42.7268381, 0.0313232719, -1.88915401e-05, 5.20873888e-09, -5.44412778e-13, -387814.587, -176.404465], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[-0.975635721, 0.257032821, -0.000412784275, 3.26330992e-07, -1.01484126e-10, -429913.506, 31.6970506], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[48.6116335, 0.0364453566, -2.27078135e-05, 6.46842469e-09, -6.97825166e-13, -439424.148, -203.866156], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[1.05179835, 0.0368731015, -4.20264032e-05, 2.38288219e-08, -5.38233162e-12, -70987.611, 20.7329266], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[8.46107003, 0.0105449156, -6.16029633e-06, 1.67267515e-09, -1.73377547e-13, -72690.9128, -15.9702328], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[1.30416192, 0.0615380588, -7.46510167e-05, 4.47854935e-08, -1.0695366e-11, -124631.611, 21.2721701], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[14.0808752, 0.01478695, -8.72265657e-06, 2.38455794e-09, -2.48394986e-13, -127498.05, -41.6774073], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[1.84785489, 0.0882157784, -0.000116517408, 7.77180058e-08, -2.10043444e-11, -175741.884, 21.2137902], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[19.9032222, 0.0187391419, -1.11131531e-05, 3.04910615e-09, -3.18430183e-13, -179663.643, -67.0156048], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[3.40387937, 0.105607264, -0.000136555028, 8.96385411e-08, -2.399546e-11, -225712.794, 16.4273813], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[25.0225316, 0.0237015304, -1.40921804e-05, 3.87205454e-09, -4.0473958e-13, -230476.051, -89.5435191], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[1.02946055, 0.154160987, -0.000218562952, 1.5066208e-07, -4.07540808e-11, -276039.614, 25.1651726], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[33.0247183, 0.0245093731, -1.45901159e-05, 4.01092407e-09, -4.19405067e-13, -282604.157, -129.384993], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[6.54975178, 0.146205527, -0.000187009488, 1.19120964e-07, -3.05405994e-11, -326258.974, 4.44266895], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[36.9324503, 0.0319166566, -1.93603031e-05, 5.41238079e-09, -5.75028761e-13, -332946.268, -144.55783], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[7.03708021, 0.177665793, -0.000239799376, 1.6178614e-07, -4.39738133e-11, -375667.273, 1.96930149], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[43.9773116, 0.0343004148, -2.0675567e-05, 5.71100008e-09, -5.97336119e-13, -383622.596, -178.220376], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[2.21606409, 0.013238051, -4.23784631e-06, -6.67863953e-09, 4.37910484e-12, -74140.4945, 14.772971], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.20117804, 0.00661606316, -3.82471522e-06, 1.0303664e-09, -1.06158338e-13, -74982.5237, -0.880396197], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[3.1326305, 0.0328571031, -2.83102366e-05, 8.88924879e-09, 1.10706912e-13, -125138.83, 13.8855197], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[10.0949054, 0.0118266899, -6.9325105e-06, 1.88610627e-09, -1.95738381e-13, -126899.732, -21.4556292], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[3.05484008, 0.060375614, -6.76072468e-05, 3.62700525e-08, -7.43749297e-12, -176118.3, 16.7118552], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[15.872108, 0.0158662131, -9.38402169e-06, 2.56936904e-09, -2.67901588e-13, -179097.356, -46.9877432], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[4.3777002, 0.0776200187, -8.36693338e-05, 4.18506605e-08, -7.58222371e-12, -226258.393, 13.6396804], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[21.2722004, 0.020551035, -1.22399542e-05, 3.3653919e-09, -3.51851242e-13, -230252.952, -70.688269], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[5.66465489, 0.0985071035, -0.00011194172, 6.16654923e-08, -1.33216471e-11, -276633.513, 9.48957201], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[26.8072492, 0.0250594358, -1.49932186e-05, 4.13327025e-09, -4.32853517e-13, -281563.144, -95.6296697], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[6.14700788, 0.128794859, -0.000162694688, 1.02773268e-07, -2.62726078e-11, -326687.586, 7.68275586], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[33.1901782, 0.0284052766, -1.70712025e-05, 4.71863579e-09, -4.95049718e-13, -332718.981, -125.30652], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[-6.29024012, 0.250535756, -0.0004503553, 3.96950978e-07, -1.34329819e-10, -376400.93, 61.9735291], Tmin=(100.0,'K'), Tmax=(835.14,'K')),
            NASAPolynomial(coeffs=[25.8508214, 0.0570891605, -3.19532056e-05, 6.31542769e-09, -4.38163135e-13, -380391.782, -79.0503946], Tmin=(835.14,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[1.97197671, 0.038262241, -5.33417376e-05, 3.98819598e-08, -1.23195031e-11, -82774.4501, 15.3983231], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[8.90664558, 0.00996111722, -5.83609496e-06, 1.58817688e-09, -1.64907909e-13, -84251.2446, -18.2304245], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[3.48756, 0.0445189, -1.69994e-05, -4.62355e-08, 4.1721e-11, -140912.0, 13.4084], Tmin=(10.0,'K'), Tmax=(600.48,'K')),
            NASAPolynomial(coeffs=[8.64988, 0.0279311, -2.00276e-05, 6.49183e-09, -7.83507e-13, -141852.0, -11.5361], Tmin=(600.48,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (10.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[3.52143115, 0.0767151923, -8.69304724e-05, 4.67022149e-08, -9.6704241e-12, -192428.344, 14.4819346], Tmin=(100.0,'K'), Tmax=(1186.72,'K')),
            NASAPolynomial(coeffs=[22.5152761, 0.012694137, -6.00895124e-06, 1.24291655e-09, -9.37945736e-14, -196936.438, -80.4040829], Tmin=(1186.72,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[-2.49067107, 0.15634868, -0.000272460958, 2.35797646e-07, -7.90236894e-11, -242436.135, 40.2193648], Tmin=(100.0,'K'), Tmax=(821.99,'K')),
            NASAPolynomial(coeffs=[18.4245471, 0.0362786488, -1.99728556e-05, 3.94730873e-09, -2.74849331e-13, -245256.611, -52.8256706], Tmin=(821.99,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[21.672263, 0.0452311228, -2.51008318e-05, 4.95162421e-09, -3.43430638e-13, -295614.963, -64.8766406], Tmin=(100.0,'K'), Tmax=(833.61,'K')),
            NASAPolynomial(coeffs=[-4.18355891, 0.198563691, -0.000353668534, 3.09832869e-07, -1.04407479e-10, -292321.083, 49.0581771], Tmin=(833.61,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[2.46154028, 0.012950989, -2.16596832e-06, -9.8060505e-09, 5.70993719e-12, -57563.5077, 14.0623986], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[5.91197113, 0.00585949131, -3.47369564e-06, 9.51960392e-10, -9.9279589e-14, -58559.94, -4.16067146], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[2.23382501, 0.0425452992, -5.01471841e-05, 2.91419877e-08, -6.76596452e-12, -110109.186, 17.6565538], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[11.2572121, 0.0104311142, -6.20931061e-06, 1.70753469e-09, -1.78587071e-13, -112180.301, -27.0315744], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[4.77730807, 0.0534039698, -5.11042972e-05, 1.8624915e-08, -7.10594612e-13, -161276.452, 8.32897058], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[17.1070694, 0.0143335383, -8.5614215e-06, 2.35917672e-09, -2.47061893e-13, -164278.228, -53.7369803], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[3.38422044, 0.0942547887, -0.000117679016, 6.89370232e-08, -1.54916819e-11, -213777.37, 15.0073161], Tmin=(100.0,'K'), Tmax=(1097.74,'K')),
            NASAPolynomial(coeffs=[25.7241499, 0.0128515327, -6.4461773e-06, 1.38447266e-09, -1.0724002e-13, -218682.062, -94.8532339], Tmin=(1097.74,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[-3.39439647, 0.180663345, -0.000328817177, 2.90654413e-07, -9.80931805e-11, -259903.647, 44.9439131], Tmin=(100.0,'K'), Tmax=(845.78,'K')),
            NASAPolynomial(coeffs=[19.7078289, 0.039551767, -2.20624429e-05, 4.3332147e-09, -2.98700137e-13, -262672.254, -55.9063606], Tmin=(845.78,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[22.930309, 0.0485491241, -2.72171456e-05, 5.34399257e-09, -3.67826911e-13, -313020.636, -67.8165752], Tmin=(100.0,'K'), Tmax=(849.23,'K')),
            NASAPolynomial(coeffs=[-5.08115354, 0.222801982, -0.00040974155, 3.64308234e-07, -1.23313672e-10, -309788.854, 53.7610249], Tmin=(849.23,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[1.48396531, 0.0376948019, -3.39510818e-05, 1.35397685e-08, -1.87254222e-12, -74956.6856, 19.4470993], Tmin=(200.0,'K'), Tmax=(1000.0,'K')),
            NASAPolynomial(coeffs=[9.98133068, 0.0128911865, -8.00759315e-06, 2.27339687e-09, -2.43409235e-13, -77209.3065, -24.0705762], Tmin=(1000.0,'K'), Tmax=(3000.0,'K')),
        ],
        Tmin = (200.0,'K'),
        Tmax = (3000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[0.686508965, 0.0802267674, -0.000133162247, 1.17086903e-07, -4.07342888e-11, -125465.238, 27.2940593], Tmin=(100.0,'K'), Tmax=(790.07,'K')),
            NASAPolynomial(coeffs=[9.66132623, 0.0261567179, -1.41184671e-05, 2.80852399e-09, -1.97796373e-13, -126613.975, -12.1845061], Tmin=(790.07,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[-1.07401797, 0.123680099, -0.000216205533, 1.91706792e-07, -6.59104023e-11, -175586.958, 35.804827], Tmin=(100.0,'K'), Tmax=(821.89,'K')),
            NASAPolynomial(coeffs=[13.4305056, 0.0342877079, -1.87450998e-05, 3.70559206e-09, -2.58425151e-13, -177336.169, -27.4629292], Tmin=(821.89,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[-2.76443375, 0.165862726, -0.000297282993, 2.65545172e-07, -9.11955462e-11, -225472.011, 44.6349708], Tmin=(100.0,'K'), Tmax=(833.82,'K')),
            NASAPolynomial(coeffs=[16.6734865, 0.0432487593, -2.38782471e-05, 4.71116877e-09, -3.27113587e-13, -227692.693, -39.4875657], Tmin=(833.82,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[-4.45259419, 0.208017936, -0.00037826321, 3.39262425e-07, -1.16435535e-10, -275357.159, 53.4570974], Tmin=(100.0,'K'), Tmax=(840.14,'K')),
            NASAPolynomial(coeffs=[19.9048092, 0.0522305138, -2.90237098e-05, 5.7197212e-09, -3.96053062e-13, -278044.604, -51.4471681], Tmin=(840.14,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[-6.1395419, 0.250158286, -0.000459189812, 4.12910519e-07, -1.41647863e-10, -325242.358, 62.2749184], Tmin=(100.0,'K'), Tmax=(844.08,'K')),
            NASAPolynomial(coeffs=[23.1304196, 0.0612223902, -3.41751844e-05, 6.72972459e-09, -4.65114841e-13, -328394.247, -63.3748882], Tmin=(844.08,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
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
            NASAPolynomial(coeffs=[-7.82610708, 0.292294164, -0.000540101631, 4.86542445e-07, -1.66855684e-10, -375127.573, 71.0913699], Tmin=(100.0,'K'), Tmax=(846.77,'K')),
            NASAPolynomial(coeffs=[26.3534852, 0.0702187494, -3.93293105e-05, 7.74036605e-09, -5.34230288e-13, -378742.873, -75.2883908], Tmin=(846.77,'K'), Tmax=(5000.0,'K')),
        ],
        Tmin = (100.0,'K'),
        Tmax = (5000.0,'K'),
    ),
    reference = Reference(authors=["Caroline Rocchio", "C. Franklin Goldsmith"], title="pfca_final", year="2024"),
    referenceType = "Theory",
)
