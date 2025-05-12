#!/usr/bin/env python
# encoding: utf-8

name = "PFLactone_Carbene_Ether_Thermo"
shortDesc = "Perfluoro alpha-lactone ether and carbene ether thermo"
longDesc = """
author = {Rocchio, Caroline and Goldsmith, C. Franklin},
"""

entry(
    index = 0,
    label = "C3F7OC(O)CF3",
    molecule = 
"""
1  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  F  u0 p3 c0 {1,S}
3  F  u0 p3 c0 {1,S}
4  F  u0 p3 c0 {1,S}
5  C  u0 p0 c0 {1,S} {6,D} {7,S} 
6  O  u0 p2 c0 {5,D}
7  O  u0 p2 c0 {5,S} {8,S}
8  C  u0 p0 c0 {7,S} {9,S} {10,S} {11,S}
9  F  u0 p3 c0 {8,S}
10 F  u0 p3 c0 {8,S}
11 C  u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12 F  u0 p3 c0 {11,S}
13 F  u0 p3 c0 {11,S}
14 C  u0 p0 c0 {11,S} {15,S} {16,S} {17,S}
15 F  u0 p3 c0 {14,S}
16 F  u0 p3 c0 {14,S}
17 F  u0 p3 c0 {14,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73679111E+00, 1.16981322E-01, -1.36399760E-04, 7.77834835E-08, -1.79573812E-11, -3.03341534E+05, 1.80799567E+01], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.99863394E+01, 2.70195735E-02, -1.73064672E-05, 4.98224020E-09, -5.37230787E-13, -3.09591691E+05, -1.12918353E+02], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = u""" SMILES =  O=C(OC(F)(F)C(F)(F)C(F)(F)F)C(F)(F)F; Partition function via MESS, conversion via automech,
    Hf(0 K) = -589.05 kcal/mol; Hf(298 K) = -592.36 kcal/mol; Hf(0 K) computed via CBH-1-CF4(ANL0).""",
)

entry(
    index = 1,
    label = "C2F5OC(CF3)OCO",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {2,S} {3,S} {5,S} {13,S}
5  O u0 p2 c0 {4,S} {6,S}
6  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
10 F u0 p3 c0 {9,S}
11 F u0 p3 c0 {9,S}
12 F u0 p3 c0 {9,S}
13 C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
14 F u0 p3 c0 {13,S}
15 F u0 p3 c0 {13,S}
16 F u0 p3 c0 {13,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.84059398E+00,  1.11000279E-01, -1.16645417E-04,
                       4.89987689E-08, -4.59613490E-12, -2.53234508E+05,
                       1.88395653E+01], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.02694908E+01,  2.10388559E-02, -1.29697201E-05,
                       3.64669352E-09, -3.87229646E-13, -2.59745021E+05,
                      -1.18443834E+02], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = u""" SMILES =  O=C1OC1(OC(F)(F)C(F)(F)F)C(F)(F)F; Partition function via MESS, conversion via automech,
    Hf(0 K) = -490.64 kcal/mol; Hf(298 K) = -493.60 kcal/mol; Hf(0 K) computed via CBH-1-CF4(ANL0).""",
)

entry(
    index = 2,
    label = "CF3OC(CF3)OCO",
    molecule = 
"""
1  O u0 p2 c0 {2,D}
2  C u0 p0 c0 {1,D} {3,S} {4,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {2,S} {3,S} {5,S} {10,S}
5  O u0 p2 c0 {4,S} {6,S}
6  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
7  F u0 p3 c0 {6,S}
8  F u0 p3 c0 {6,S}
9  F u0 p3 c0 {6,S}
10 C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 F u0 p3 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.53585152E-01,  9.70546077E-02, -1.13149955E-04,
                       5.90838737E-08, -1.06467920E-11, -2.02175867E+05,
                       2.64236611E+01], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.30805030E+01,  1.83535624E-02, -1.10967226E-05,
                       3.08265042E-09, -3.24673276E-13, -2.07234124E+05,
                      -8.40442494E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = u""" SMILES =  O=C1OC1(OC(F)(F)F)C(F)(F)F; Partition function via MESS, conversion via automech,
    Hf(0 K) = -391.82 kcal/mol; Hf(298 K) = -394.51 kcal/mol; Hf(0 K) computed via CBH-1-CF4(ANL0).""",
)

entry(
    index = 3,
    label = "C2H5OC(CH3)OCO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {14,S} {15,S} {16,S}
6  O u0 p2 c0 {4,S} {7,S}
7  C u0 p0 c0 {4,S} {6,S} {8,D}
8  O u0 p2 c0 {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.06143469E+00,  2.49945306E-02,  5.68029390E-05,
                      -9.60769439E-08,  4.11022219E-11, -7.51985698E+04,
                      -1.55578758E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.14755734E+01,  3.68507986E-02, -1.85201534E-05,
                       4.50916921E-09, -4.31205532E-13, -7.72729878E+04,
                      -2.93876471E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = u""" SMILES =  CCOC1(C)OC1=O; Partition function via MESS, conversion via automech,
    Hf(0 K) = -136.49 kcal/mol; Hf(298 K) = -142.39 kcal/mol; Hf(0 K) computed via CBH-1(ANL0).""",
)

entry(
    index = 4,
    label = "CH3OC(CH3)OCO",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2  O u0 p2 c0 {1,S} {3,S}
3  C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4  C u0 p0 c0 {3,S} {11,S} {12,S} {13,S}
5  O u0 p2 c0 {3,S} {6,S}
6  C u0 p0 c0 {3,S} {5,S} {7,D}
7  O u0 p2 c0 {6,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.24908909E+00,  2.22012932E-02,  3.82706304E-05,
                      -6.88430478E-08,  2.97411701E-11, -7.06844735E+04,
                       4.57732908E-02], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.04083276E+01,  2.82598504E-02, -1.41651993E-05,
                       3.44562517E-09, -3.29468977E-13, -7.24524212E+04,
                      -2.51044357E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = u""" SMILES =  COC1(C)OC1=O; Partition function via MESS, conversion via automech,
    Hf(0 K) = -129.83 kcal/mol; Hf(298 K) = -134.37 kcal/mol; Hf(0 K) computed via CBH-1(ANL0).""",
)

entry(
    index = 5,
    label = "C3F7OCCF3",
    molecule = 
"""
multiplicity 1
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  F u0 p3 c0 {2,S}
5  C u0 p1 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {7,S}
7  C u0 p0 c0 {6,S} {8,S} {9,S} {10,S}
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
            NASAPolynomial(coeffs=[3.80107003E+00,  1.00882913E-01, -1.03267310E-04,
                       4.39648484E-08, -4.56205391E-12, -2.50662406E+05,
                       1.97583907E+01], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.65998951E+01,  2.49125283E-02, -1.39298131E-05,
                       3.59457872E-09, -3.57722129E-13, -2.56003504E+05,
                      -9.40230044E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = u""" SMILES =  FC(F)(F)[C]OC(F)(F)C(F)(F)C(F)(F)F; Partition function via MESS, conversion via automech,
    Hf(0 K) = -485.90 kcal/mol; Hf(298 K) = -488.60 kcal/mol; Hf(0 K) computed via CBH-1-CF4-avg(ANL0).""",
)

entry(
    index = 6,
    label = "C2F5OCCF3",
    molecule = 
"""
multiplicity 1
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  F u0 p3 c0 {2,S}
5  C u0 p1 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {7,S}
7  C u0 p0 c0 {6,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 C u0 p0 c0 {7,S} {11,S} {12,S} {13,S}
11 F u0 p3 c0 {10,S}
12 F u0 p3 c0 {10,S}
13 F u0 p3 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.17572731E+00,  7.15219859E-02, -5.73848578E-05,
                       8.21599099E-09,  6.43626052E-12, -2.00515559E+05,
                       1.55618289E+01], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[2.16330614E+01,  1.95253284E-02, -1.05928399E-05,
                       2.65868416E-09, -2.59127065E-13, -2.04843500E+05,
                      -7.29022316E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = u""" SMILES =  FC(F)(F)[C]OC(F)(F)C(F)(F)F; Partition function via MESS, conversion via automech,
    Hf(0 K) = -388.16 kcal/mol; Hf(298 K) = -390.65 kcal/mol; Hf(0 K) computed via CBH-1-CF4(ANL0).""",
)

entry(
    index = 7,
    label = "CF3OCCF3",
    molecule = 
"""
multiplicity 1
1  F u0 p3 c0 {2,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  F u0 p3 c0 {2,S}
4  F u0 p3 c0 {2,S}
5  C u0 p1 c0 {2,S} {6,S}
6  O u0 p2 c0 {5,S} {7,S}
7  C u0 p0 c0 {6,S} {8,S} {9,S} {10,S}
8  F u0 p3 c0 {7,S}
9  F u0 p3 c0 {7,S}
10 F u0 p3 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.23126106E+00,  5.19199461E-02, -4.04486495E-05,
                       5.77082760E-09,  4.37925281E-12, -1.50031590E+05,
                       1.73744922E+01], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.49578323E+01,  1.71058298E-02, -9.33279153E-06,
                       2.35135608E-09, -2.29588607E-13, -1.52946420E+05,
                      -4.20815707E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = u""" SMILES =  FC(F)(F)[C]OC(F)(F)F; Partition function via MESS, conversion via automech,
    Hf(0 K) = -290.23 kcal/mol; Hf(298 K) = -292.33 kcal/mol; Hf(0 K) computed via CBH-1-CF4(ANL0).""",
)

entry(
    index = 8,
    label = "C2H5OCCH3",
    molecule = 
"""
multiplicity 1
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p1 c0 {1,S} {3,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {9,S} {10,S}
5  C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[6.72147581E+00,  4.29300226E-04,  8.37388963E-05,
                      -1.06929480E-07,  4.18950854E-11, -9.74282182E+03,
                      -2.64290013E-01], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[3.22622006E+00,  3.69380481E-02, -1.82273316E-05,
                       4.32094959E-09, -4.02608537E-13, -9.86626601E+03,
                       1.18453944E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = u""" SMILES =  C[C]OCC; Partition function via MESS, conversion via automech,
    Hf(0 K) = -8.93 kcal/mol; Hf(298 K) = -14.25 kcal/mol; Hf(0 K) computed via CBH-1(ANL0).""",
)

entry(
    index = 9,
    label = "CH3OCCH3",
    molecule = 
"""
multiplicity 1
1  C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  C u0 p1 c0 {1,S} {3,S}
3  O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[7.27950142E+00, -1.37518479E-02,  9.31457727E-05,
                      -1.07377077E-07,  4.03412473E-11, -5.25803426E+03,
                      -4.24978911E+00], Tmin=(200,'K'), Tmax=(1000,'K')),
            NASAPolynomial(coeffs=[1.66462515E+00,  2.94935783E-02, -1.47012494E-05,
                       3.50958294E-09, -3.28940800E-13, -4.90449117E+03,
                       1.84198139E+01], Tmin=(1000,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (200,'K'),
        Tmax = (3000,'K'),
    ),
    shortDesc = u"""""",
    longDesc = u""" SMILES =  C[C]OC; Partition function via MESS, conversion via automech,
    Hf(0 K) = -2.23 kcal/mol; Hf(298 K) = -6.10 kcal/mol; Hf(0 K) computed via CBH-1(ANL0).""",
)
