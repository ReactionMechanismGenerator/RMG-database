#!/usr/bin/env python
# encoding: utf-8

name = "C6H5_O2_oxygenated"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "C6H4O2_24",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,D}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {6,S} {12,S}
6  C u0 p0 c0 {1,S} {5,S} {8,D}
7  O u0 p2 c0 {1,D}
8  O u0 p2 c0 {6,D}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.27877,0.0656594,-5.83355e-05,2.65985e-08,-4.90157e-12,-11461.7,37.0874], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[1.2491,0.0494302,-3.39113e-05,1.141e-08,-1.5186e-12,-11888.2,20.9591], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: O=C1C=CC=CC1=O
Info: mw=108.095 crc=-1640820116 symm=['C1', 1]
Filename: C6H4O2_24
FKM: -19861.0172103 79.9488 19.011 5.1062e-002 -1.6167e-005 -6.6829e+005
Aspen: -19861.0172103 -43697.7562213 2.557 9.3743e-002 -5.3973e-005 1.1123e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "C6H4O2_23",
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
            NASAPolynomial(coeffs=[-2.38008,0.0659406,-5.86315e-05,2.67276e-08,-4.91972e-12,-15449.1,37.3619], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[0.786632,0.0505725,-3.49728e-05,1.18459e-08,-1.58523e-12,-15756.1,23.1605], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: O=C1C=CC(=O)C=C1
Info: mw=108.095 crc=-1586105560 symm=['C1', 1]
Filename: C6H4O2_23
FKM: -27821.6848541 79.4973 18.953 5.1155e-002 -1.6206e-005 -6.7247e+005
Aspen: -27821.6848541 -51523.8182571 2.401 9.4081e-002 -5.4221e-005 1.1182e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "C6H4O_5",
    molecule = 
"""
1  O u0 p2 c0 {3,D}
2  C u0 p0 c0 {3,S} {4,D} {9,S}
3  C u0 p0 c0 {1,D} {2,S} {5,S}
4  C u0 p0 c0 {2,D} {6,S} {8,S}
5  C u0 p0 c0 {3,S} {7,D} {10,S}
6  C u0 p0 c0 {4,S} {7,D} {11,S}
7  C u0 p0 c0 {5,D} {6,D}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.28222,0.0674214,-6.74423e-05,3.50397e-08,-7.36216e-12,34790.5,41.6349], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[14.8097,0.0115053,-3.06423e-07,-1.93139e-09,4.68382e-13,29937.6,-50.6414], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: O=C1[CH][C][CH]C=C1
Info: mw=92.095 crc=1270001973 multiplicity=5 symm=['C1', 1]
Filename: C6H4O_5
FKM: 71527.0074743 78.1876 19.110 4.3873e-002 -1.3747e-005 -6.9601e+005
Aspen: 71527.0074743 48215.36113 2.459 8.6175e-002 -5.0372e-005 1.0530e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "C6H5O2_9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {5,S} {10,S}
5  C u0 p0 c0 {3,D} {4,S} {11,S}
6  C u0 p0 c0 {1,S} {12,S} {13,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 O u1 p2 c0 {6,S}
13 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.92402,0.078205,-7.43133e-05,3.609e-08,-7.02366e-12,1552.42,45.5407], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[1.17858,0.0543432,-3.77179e-05,1.28584e-08,-1.73272e-12,941.251,22.2872], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: O=C([O])[C@H]1C=CC=C1
Info: mw=109.103 crc=-1735442242 multiplicity=2 symm=['C1', 1]
Filename: C6H5O2_9
FKM: 5844.36431548 84.1527 21.775 5.3939e-002 -1.7067e-005 -8.2344e+005
Aspen: 5844.36431548 -19245.7661594 1.881 0.1048 -6.1499e-005 1.2883e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "C6H5O2_8",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {6,D} {11,S}
4  C u1 p0 c0 {2,S} {6,S} {10,S}
5  C u0 p0 c0 {1,S} {7,S} {12,D}
6  C u0 p0 c0 {3,D} {4,S} {13,S}
7  O u0 p2 c0 {2,S} {5,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.41552,0.0852911,-8.29111e-05,4.1061e-08,-8.13959e-12,-7616.97,55.3771], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[1.87536,0.0518612,-3.50562e-05,1.16859e-08,-1.54662e-12,-9113.9,15.7567], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: O=C1O[C@H]2[CH]C=C[C@@H]12
Info: mw=109.103 crc=1471086147 multiplicity=2 symm=['C1', 1]
Filename: C6H5O2_8
FKM: -13305.1900353 79.1972 20.024 5.6409e-002 -1.7983e-005 -9.0700e+005
Aspen: -13305.1900353 -36917.8411332 -1.800 0.1121 -6.6416e-005 1.3998e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "C6H5O2_7",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {2,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {10,S}
3  C u0 p0 c0 {2,D} {5,S} {9,S}
4  C u0 p0 c0 {1,S} {6,D} {11,S}
5  C u0 p0 c0 {3,S} {7,S} {12,D}
6  C u0 p0 c0 {4,D} {7,S} {13,S}
7  O u0 p2 c0 {5,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.77724,0.0753165,-6.94333e-05,3.30454e-08,-6.36057e-12,-9542.08,44.6102], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[2.30694,0.0503832,-3.35795e-05,1.10689e-08,-1.45226e-12,-10592.9,15.6922], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: O=C1C=C[CH]C=CO1
Info: mw=109.103 crc=1504001099 multiplicity=2 symm=['C1', 1]
Filename: C6H5O2_7
FKM: -16276.9968193 82.6948 20.072 5.5465e-002 -1.7436e-005 -7.7225e+005
Aspen: -16276.9968193 -40932.451836 1.257 0.1039 -5.9990e-005 1.2418e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "C6H5O2_15",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {9,S}
3  C u1 p0 c0 {1,S} {5,S} {10,S}
4  C u0 p0 c0 {2,S} {6,D} {11,S}
5  C u0 p0 c0 {3,S} {6,S} {12,D}
6  C u0 p0 c0 {4,D} {5,S} {13,S}
7  O u0 p2 c0 {1,S} {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.90196,0.0800102,-7.57485e-05,3.67208e-08,-7.15639e-12,3831.65,48.5069], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[2.02944,0.0516078,-3.48567e-05,1.16092e-08,-1.53517e-12,2630.51,15.5539], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: O=C1[CH][C@H]2O[C@H]2C=C1
Info: mw=109.103 crc=-363025902 multiplicity=2 symm=['C1', 1]
Filename: C6H5O2_15
FKM: 9958.52600873 80.027 20.340 5.5812e-002 -1.7708e-005 -8.3830e+005
Aspen: 9958.52600873 -13901.5264434 4.0346e-002 0.1078 -6.3205e-005 1.3217e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "C6H5O2_20",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {5,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {4,D} {10,S}
4  C u0 p0 c0 {2,S} {3,D} {11,S}
5  C u0 p0 c0 {2,S} {6,D} {12,S}
6  C u0 p0 c0 {1,S} {5,D} {13,S}
7  O u0 p2 c0 {1,S} {2,S}
8  O u1 p2 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.83493,0.0981596,-0.000107913,6.00841e-08,-1.32602e-11,19929,59.774], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[27.3995,-0.00918949,2.00567e-05,-1.03939e-08,1.75695e-12,10289.1,-120.551], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: [O][C@@]12C=C[C@@H](C=C1)O2
Info: mw=109.103 crc=-150591537 multiplicity=2 symm=['C1', 1]
Filename: C6H5O2_20
FKM: 41324.1775752 77.4852 24.502 5.0968e-002 -1.6149e-005 -1.0591e+006
Aspen: 41324.1775752 18221.9541274 -0.2286 0.1126 -6.8444e-005 1.4713e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "C6H5O2_18",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  C u1 p0 c0 {1,S} {5,S} {11,S}
5  C u0 p0 c0 {4,S} {6,D} {12,S}
6  C u0 p0 c0 {5,D} {7,S} {13,S}
7  O u0 p2 c0 {2,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.92769,0.0826723,-8.19813e-05,4.1835e-08,-8.58835e-12,12867.8,48.8755], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[9.68803,0.0332358,-1.82789e-05,4.97481e-09,-5.43632e-13,9335.04,-24.2323], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: O=C1[C@H]2[CH]C=CO[C@@H]12
Info: mw=109.103 crc=1747798817 multiplicity=2 symm=['C1', 1]
Filename: C6H5O2_18
FKM: 28025.899146 81.5204 21.914 5.3667e-002 -1.6932e-005 -8.6745e+005
Aspen: 28025.899146 3720.59613693 1.140 0.1065 -6.2697e-005 1.3172e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "C6H5O2_13",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {9,D}
4  C u0 p0 c0 {2,D} {6,S} {11,S}
5  C u0 p0 c0 {3,S} {6,D} {13,S}
6  C u0 p0 c0 {4,S} {5,D} {12,S}
7  O u1 p2 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.23123,0.0752534,-7.04944e-05,3.42563e-08,-6.7605e-12,7255.09,41.8332], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[6.6032,0.0406577,-2.48708e-05,7.57188e-09,-9.26758e-13,5013.29,-6.88196], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: [O][C@H]1C=CC=CC1=O
Info: mw=109.103 crc=-1006037654 multiplicity=2 symm=['C1', 1]
Filename: C6H5O2_13
FKM: 17379.4251042 83.1656 21.215 5.4484e-002 -1.7141e-005 -7.6846e+005
Aspen: 17379.4251042 -7416.39962035 2.534 0.1025 -5.9249e-005 1.2265e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "C6H5O2_16",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {9,S}
3  C u0 p0 c0 {2,S} {5,S} {10,D}
4  C u0 p0 c0 {1,S} {6,D} {11,S}
5  C u1 p0 c0 {3,S} {6,S} {12,S}
6  C u0 p0 c0 {4,D} {5,S} {13,S}
7  O u0 p2 c0 {1,S} {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.07313,0.079899,-7.47982e-05,3.57013e-08,-6.82962e-12,-741.925,49.3292], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[-0.930964,0.0587893,-4.1394e-05,1.42429e-08,-1.93086e-12,-1068,31.0622], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: O=C1[CH]C=C[C@H]2O[C@@H]12
Info: mw=109.103 crc=-1035538858 multiplicity=2 symm=['C1', 1]
Filename: C6H5O2_16
FKM: 779.895849913 79.75 19.902 5.6450e-002 -1.7955e-005 -8.3994e+005
Aspen: 779.895849913 -22997.5552766 -0.4859 0.1088 -6.3814e-005 1.3347e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "C6H5O2_10",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,D} {5,S} {11,S}
5  C u0 p0 c0 {3,D} {4,S} {12,S}
6  O u0 p2 c0 {1,S} {7,S}
7  C u1 p0 c0 {6,S} {13,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.65993,0.0754942,-6.95313e-05,3.27965e-08,-6.21196e-12,3295.75,45.5473], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[-1.13763,0.0593431,-4.2002e-05,1.45238e-08,-1.97726e-12,3406.35,35.5543], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: O=[C]O[C@H]1C=CC=C1
Info: mw=109.103 crc=820970530 multiplicity=2 symm=['C1', 1]
Filename: C6H5O2_10
FKM: 9306.69409373 85.9506 20.629 5.5047e-002 -1.7367e-005 -7.8365e+005
Aspen: 9306.69409373 -16319.4817474 1.553 0.1041 -6.0456e-005 1.2568e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "C6H5O2_21",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {5,S} {11,S}
4  C u0 p0 c0 {1,S} {7,D} {10,S}
5  C u0 p0 c0 {3,S} {6,S} {12,D}
6  O u0 p2 c0 {1,S} {5,S}
7  C u1 p0 c0 {4,D} {13,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {3,S}
12 O u0 p2 c0 {5,D}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.49484,0.0774107,-7.47241e-05,3.73759e-08,-7.56117e-12,5534.03,43.4412], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[8.45724,0.0362265,-2.10028e-05,6.07271e-09,-7.08636e-13,2717.76,-16.0802], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: [CH]=C[C@H]1C=CC(=O)O1
Info: mw=109.103 crc=1535779566 multiplicity=2 symm=['C1', 1]
Filename: C6H5O2_21
FKM: 13927.5722047 84.3195 22.065 5.3169e-002 -1.6673e-005 -7.9862e+005
Aspen: 13927.5722047 -11212.2969474 2.815 0.1023 -5.9502e-005 1.2391e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "C6H5O2_19",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u1 p0 c0 {1,S} {4,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {9,D}
4  C u0 p0 c0 {2,S} {6,S} {11,D}
5  C u0 p0 c0 {3,S} {6,D} {13,S}
6  C u0 p0 c0 {4,S} {5,D} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.53298,0.0701173,-6.11157e-05,2.73409e-08,-4.93412e-12,-9366.96,40.1435], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[-1.55686,0.0600592,-4.23743e-05,1.45874e-08,-1.97706e-12,-8951.45,37.6118], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: O=C1C=CC(=O)C[CH]1
Info: mw=109.103 crc=-850547744 multiplicity=2 symm=['C1', 1]
Filename: C6H5O2_19
FKM: -15541.7508348 85.4109 19.756 5.6085e-002 -1.7649e-005 -7.0681e+005
Aspen: -15541.7508348 -41007.0004682 2.299 0.1015 -5.7934e-005 1.1877e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "C6H5O2_14",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {8,S}
2  C u1 p0 c0 {1,S} {4,S} {7,S}
3  C u0 p0 c0 {1,D} {5,S} {9,S}
4  C u0 p0 c0 {2,S} {6,D} {10,S}
5  C u0 p0 c0 {3,S} {11,D} {12,S}
6  C u0 p0 c0 {4,D} {13,D}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 O u0 p2 c0 {5,D}
12 H u0 p0 c0 {5,S}
13 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[1.3755,0.0579035,-4.60127e-05,1.87619e-08,-3.07116e-12,-4198.54,24.2692], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[-1.83735,0.061166,-4.36335e-05,1.51629e-08,-2.07065e-12,-2694.28,42.9752], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: [O][C]/C=C/C=C/C=O
Info: mw=109.103 crc=-924263682 multiplicity=4 symm=['C1', 1]
Filename: C6H5O2_14
FKM: -3874.87004554 91.8168 21.643 5.2828e-002 -1.6299e-005 -5.5035e+005
Aspen: -3874.87004554 -31250.0475789 7.779 8.9357e-002 -4.9183e-005 9.8233e-009""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "C6H5O2_5",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {3,S} {7,S}
2  C u0 p0 c0 {1,D} {4,S} {8,S}
3  C u0 p0 c0 {1,S} {6,D} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {9,S}
5  C u0 p0 c0 {4,D} {6,S} {10,S}
6  C u0 p0 c0 {3,D} {5,S} {11,S}
7  O u0 p2 c0 {1,S} {13,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 O u1 p2 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.51709,0.0766266,-6.92448e-05,3.17164e-08,-5.78614e-12,15683.5,47.6136], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[-5.73052,0.0702025,-5.17458e-05,1.84113e-08,-2.55706e-12,16976.4,57.3168], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: [O]OC1=CC=CC=C1
Info: mw=109.103 crc=1863467229 multiplicity=2 symm=['C1', 1]
Filename: C6H5O2_5
FKM: 33540.9350912 81.1241 19.299 5.6923e-002 -1.8076e-005 -8.0190e+005
Aspen: 33540.9350912 9353.7893057 -0.3007 0.1075 -6.2629e-005 1.3039e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "C6H5O2_24",
    molecule = 
"""
multiplicity 4
1  O u1 p2 c0 {3,S}
2  O u0 p2 c0 {6,D}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {9,S}
4  C u1 p0 c0 {3,S} {6,S} {10,S}
5  C u0 p0 c0 {3,S} {7,D} {11,S}
6  C u0 p0 c0 {2,D} {4,S} {8,S}
7  C u0 p0 c0 {5,D} {8,S} {13,S}
8  C u1 p0 c0 {6,S} {7,S} {12,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.45856,0.0823093,-8.12722e-05,4.10884e-08,-8.34604e-12,27077.8,47.6452], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[8.77849,0.0366405,-2.16891e-05,6.38807e-09,-7.57571e-13,23966.9,-18.2505], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: [O][C@H]1[CH]C(=O)[CH]C=C1
Info: mw=109.103 crc=-2108880538 multiplicity=4 symm=['C1', 1]
Filename: C6H5O2_24
FKM: 56496.5763395 84.1514 22.810 5.3491e-002 -1.7032e-005 -8.7018e+005
Aspen: 56496.5763395 31406.8507619 1.927 0.1067 -6.3196e-005 1.3312e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "C6H5O2_23",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,D}
4  C u1 p0 c0 {1,S} {6,S} {11,S}
5  C u0 p0 c0 {2,S} {6,D} {12,S}
6  C u0 p0 c0 {4,S} {5,D} {13,S}
7  O u0 p2 c0 {1,S} {2,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-6.10528,0.0861975,-8.61536e-05,4.40999e-08,-9.05694e-12,5693.54,53.3958], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[8.96174,0.0348499,-1.96475e-05,5.49722e-09,-6.1894e-13,2087.88,-21.8372], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: O=C1[C@H]2[CH]C=C[C@@H]1O2
Info: mw=109.103 crc=-454568440 multiplicity=2 symm=['C1', 1]
Filename: C6H5O2_23
FKM: 13342.444535 79.0088 21.252 5.4776e-002 -1.7382e-005 -9.1282e+005
Aspen: 13342.444535 -10214.0327481 -0.5759 0.1102 -6.5354e-005 1.3790e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "C6H5O2_26",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,D}
3  C u0 p0 c0 {1,S} {5,S} {10,D}
4  C u1 p0 c0 {2,S} {6,S} {11,S}
5  C u0 p0 c0 {3,S} {6,D} {13,S}
6  C u0 p0 c0 {4,S} {5,D} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {2,D}
10 O u0 p2 c0 {3,D}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.90353,0.0714096,-6.27812e-05,2.82411e-08,-5.10674e-12,-14809.6,44.435], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[-3.39325,0.0621057,-4.42821e-05,1.53702e-08,-2.09611e-12,-14204.2,44.5157], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: O=C1C=C[CH]C(=O)C1
Info: mw=109.103 crc=1977468207 multiplicity=2 symm=['C1', 1]
Filename: C6H5O2_26
FKM: -27024.3878295 79.2502 17.763 5.6127e-002 -1.7693e-005 -7.2680e+005
Aspen: -27024.3878295 -50652.8276477 -0.1405 0.1026 -5.8849e-005 1.2111e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "C6H5O2_17",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,D} {4,S} {10,S}
2  C u0 p0 c0 {1,D} {3,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {8,D}
4  C u0 p0 c0 {1,S} {6,D} {9,S}
5  C u1 p0 c0 {3,S} {7,S} {12,S}
6  C u0 p0 c0 {4,D} {7,S} {13,S}
7  O u0 p2 c0 {5,S} {6,S}
8  O u0 p2 c0 {3,D}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.05853,0.0722919,-6.47218e-05,2.98069e-08,-5.53707e-12,1519.73,41.1355], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[-0.522862,0.0573272,-3.99518e-05,1.36489e-08,-1.84101e-12,1521.23,30.6719], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: O=C1[CH]OC=CC=C1
Info: mw=109.103 crc=1607912070 multiplicity=2 symm=['C1', 1]
Filename: C6H5O2_17
FKM: 5923.82483521 82.4683 19.983 5.5485e-002 -1.7427e-005 -7.3718e+005
Aspen: 5923.82483521 -18664.0942203 1.911 0.1022 -5.8678e-005 1.2096e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "C6H5O2_6",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,D} {9,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,D} {6,S} {12,S}
5  C u0 p0 c0 {3,D} {6,S} {13,S}
6  C u1 p0 c0 {4,S} {5,S} {11,S}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {1,S} {7,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.37475,0.0845912,-8.45444e-05,4.32844e-08,-8.88991e-12,22685.2,50.2406], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[9.59856,0.0337249,-1.8833e-05,5.22049e-09,-5.82436e-13,19088.8,-24.5761], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: C1=C[CH]C=CC21OO2
Info: mw=109.103 crc=-985577692 multiplicity=2 symm=['C1', 1]
Filename: C6H5O2_6
FKM: 47401.7895279 80.1196 22.090 5.3734e-002 -1.7029e-005 -8.9628e+005
Aspen: 47401.7895279 23514.1449166 0.6666 0.1081 -6.4089e-005 1.3524e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "C6H5O2_22",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {9,S}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  C u0 p0 c0 {1,S} {5,D} {11,S}
5  C u0 p0 c0 {2,S} {4,D} {12,S}
6  C u0 p0 c0 {1,S} {7,S} {13,D}
7  O u0 p2 c0 {2,S} {6,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-7.55321,0.0910228,-9.26994e-05,4.81145e-08,-9.98186e-12,2740.32,59.5804], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[9.63247,0.0329319,-1.78292e-05,4.75602e-09,-5.07317e-13,-1420.9,-26.4025], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: O=C1O[C@@H]2[CH][C@H]1C=C2
Info: mw=109.103 crc=923213951 multiplicity=2 symm=['C1', 1]
Filename: C6H5O2_22
FKM: 6968.40385142 77.3427 20.793 5.5417e-002 -1.7649e-005 -9.7432e+005
Aspen: 6968.40385142 -16091.328126 -2.397 0.1141 -6.8242e-005 1.4487e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "C6H5O2_25",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u1 p0 c0 {1,S} {6,S} {9,S}
3  C u0 p0 c0 {1,D} {4,S} {12,S}
4  C u0 p0 c0 {3,S} {5,S} {8,D}
5  C u0 p0 c0 {4,S} {6,D} {10,S}
6  C u0 p0 c0 {2,S} {5,D} {11,S}
7  O u0 p2 c0 {1,S} {13,S}
8  O u0 p2 c0 {4,D}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.0034,0.0787161,-7.58735e-05,3.75017e-08,-7.4393e-12,-16962.2,44.2176], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[5.14154,0.0443248,-2.86433e-05,9.23885e-09,-1.1937e-12,-18835.8,-0.315279], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: O=C1C=C[CH]C(=C1)O
Info: mw=109.103 crc=1870684941 multiplicity=2 symm=['C1', 1]
Filename: C6H5O2_25
FKM: -30966.853668 80.8185 21.991 5.3142e-002 -1.6743e-005 -8.2975e+005
Aspen: -30966.853668 -55062.8998339 2.019 0.1041 -6.1096e-005 1.2823e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "C6H5O2_1",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,D} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {8,D}
3  C u0 p0 c0 {1,D} {4,S} {12,S}
4  C u1 p0 c0 {3,S} {6,S} {9,S}
5  C u0 p0 c0 {2,S} {6,D} {10,S}
6  C u0 p0 c0 {4,S} {5,D} {11,S}
7  O u0 p2 c0 {1,S} {13,S}
8  O u0 p2 c0 {2,D}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.01579,0.0775673,-7.34083e-05,3.56311e-08,-6.94746e-12,-16718.7,44.3848], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[3.11217,0.0489358,-3.26869e-05,1.08302e-08,-1.42905e-12,-18002.6,10.3098], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: O=C1C=C[CH]C=C1O
Info: mw=109.103 crc=309447710 multiplicity=2 symm=['C1', 1]
Filename: C6H5O2_1
FKM: -30546.3454845 80.5479 21.195 5.4063e-002 -1.7037e-005 -8.1322e+005
Aspen: -30546.3454845 -54561.6874279 1.533 0.1044 -6.1006e-005 1.2759e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "C6H5O2_27",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,D} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {9,D}
4  C u0 p0 c0 {3,S} {6,S} {11,D}
5  C u0 p0 c0 {2,D} {6,S} {13,S}
6  C u1 p0 c0 {4,S} {5,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {2,S}
11 O u0 p2 c0 {4,D}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.61583,0.0703765,-6.14904e-05,2.75855e-08,-4.99322e-12,-10200.6,39.9222], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[-1.39993,0.0596163,-4.19485e-05,1.44105e-08,-1.94985e-12,-9852.67,36.1549], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: O=C1[CH]C=CCC1=O
Info: mw=109.103 crc=892087196 multiplicity=2 symm=['C1', 1]
Filename: C6H5O2_27
FKM: -17228.2809038 84.1637 19.722 5.6100e-002 -1.7652e-005 -7.0997e+005
Aspen: -17228.2809038 -42321.7028753 2.198 0.1016 -5.8055e-005 1.1906e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "C6H5O2_12",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {7,S} {9,S}
2  C u1 p0 c0 {1,S} {4,S} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {10,S}
4  C u0 p0 c0 {2,S} {6,D} {13,S}
5  C u0 p0 c0 {3,D} {6,S} {11,S}
6  C u0 p0 c0 {4,D} {5,S} {12,S}
7  O u0 p2 c0 {1,S} {8,S}
8  O u0 p2 c0 {2,S} {7,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.71559,0.084068,-8.21143e-05,4.10124e-08,-8.22411e-12,34173,51.7553], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[5.4326,0.0436457,-2.76837e-05,8.72983e-09,-1.10327e-12,31738.5,-3.06634], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: C1=CC=C[C]2OO[C@@H]12
Info: mw=109.103 crc=1473347154 multiplicity=2 symm=['C1', 1]
Filename: C6H5O2_12
FKM: 70031.2077537 79.1973 20.867 5.5520e-002 -1.7681e-005 -8.8931e+005
Aspen: 70031.2077537 46418.5361835 -0.5222 0.1101 -6.5124e-005 1.3706e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "C6H5O2_11",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,D} {9,S}
3  C u0 p0 c0 {2,D} {4,S} {10,S}
4  C u0 p0 c0 {3,S} {5,D} {11,S}
5  C u0 p0 c0 {4,D} {6,S} {12,S}
6  O u0 p2 c0 {1,S} {5,S}
7  C u1 p0 c0 {1,S} {13,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 O u0 p2 c0 {7,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-2.69115,0.072396,-6.61662e-05,3.13224e-08,-6.00727e-12,3710.57,40.0354], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[2.4351,0.0503906,-3.37488e-05,1.11796e-08,-1.47343e-12,2916.4,16.008], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: O=[C][C@H]1C=CC=CO1
Info: mw=109.103 crc=-1501339615 multiplicity=2 symm=['C1', 1]
Filename: C6H5O2_11
FKM: 10468.5691142 84.3463 20.916 5.4234e-002 -1.6966e-005 -7.3616e+005
Aspen: 10468.5691142 -14679.2887982 2.954 0.1005 -5.7680e-005 1.1894e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "C6H5O_9",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,D} {8,S}
3  C u0 p0 c0 {1,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {5,S} {10,S}
5  C u0 p0 c0 {3,D} {4,S} {11,S}
6  C u1 p0 c0 {1,S} {12,D}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 O u0 p2 c0 {6,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-3.71143,0.0696677,-6.4931e-05,3.13419e-08,-6.11259e-12,22751.3,44.7176], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[1.2664,0.0477189,-3.20543e-05,1.0662e-08,-1.41117e-12,22024.9,21.5662], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: O=[C][C@H]1C=CC=C1
Info: mw=93.103 crc=1846588092 multiplicity=2 symm=['C1', 1]
Filename: C6H5O_9
FKM: 47563.1995537 80.8872 18.252 5.0484e-002 -1.5740e-005 -7.1342e+005
Aspen: 47563.1995537 23446.6719532 0.9473 9.4887e-002 -5.4610e-005 1.1302e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "C6H5O_8",
    molecule = 
"""
multiplicity 2
1  C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {9,D}
4  C u1 p0 c0 {2,S} {6,S} {10,S}
5  C u0 p0 c0 {1,S} {6,D} {11,S}
6  C u0 p0 c0 {4,S} {5,D} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  O u0 p2 c0 {3,D}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-5.52919,0.0795575,-8.14634e-05,4.29552e-08,-9.0824e-12,28556.2,50.7723], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[12.5901,0.0206917,-7.62408e-06,8.57562e-10,5.81553e-14,23938.9,-40.7109], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: O=C1[C@H]2C=C[CH][C@@H]12
Info: mw=93.103 crc=-1916670928 multiplicity=2 symm=['C1', 1]
Filename: C6H5O_8
FKM: 58651.2362351 76.9459 19.981 4.8785e-002 -1.5263e-005 -8.3596e+005
Aspen: 58651.2362351 35709.8070622 0.1398 9.8883e-002 -5.8341e-005 1.2299e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "C6H5O_7",
    molecule = 
"""
multiplicity 2
1  C u1 p0 c0 {4,S} {5,S} {8,S}
2  C u0 p0 c0 {3,S} {6,S} {7,D}
3  C u0 p0 c0 {2,S} {4,D} {9,S}
4  C u0 p0 c0 {1,S} {3,D} {10,S}
5  C u0 p0 c0 {1,S} {6,D} {11,S}
6  C u0 p0 c0 {2,S} {5,D} {12,S}
7  O u0 p2 c0 {2,D}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.90394,0.0709001,-6.37443e-05,2.92119e-08,-5.34983e-12,5741.34,48.23], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[-5.6982,0.0641637,-4.67892e-05,1.65344e-08,-2.28627e-12,6826.42,55.4519], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: O=C1C=C[CH]C=C1
Info: mw=93.103 crc=-1933114642 multiplicity=2 symm=['C1', 1]
Filename: C6H5O_7
FKM: 13219.0851036 75.3036 16.178 5.3396e-002 -1.6834e-005 -7.3450e+005
Aspen: 13219.0851036 -9232.69584005 -1.784 9.9761e-002 -5.7689e-005 1.1959e-008""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "C5H5O_6",
    molecule = 
"""
1  O u0 p2 c0 {5,S} {6,S}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {2,S} {5,D} {9,S}
4  C u0 p0 c0 {2,S} {6,D} {10,S}
5  C u0 p0 c0 {1,S} {3,D} {11,S}
6  C u0 p0 c0 {1,S} {4,D} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[-4.89733,0.0671746,-6.39594e-05,3.15405e-08,-6.26844e-12,192170,46.8562], Tmin=(273.15,'K'), Tmax=(1298,'K')),
            NASAPolynomial(coeffs=[1.28522,0.0419041,-2.74427e-05,8.96319e-09,-1.17118e-12,191080,17.4161], Tmin=(1298,'K'), Tmax=(1998.15,'K')),
        ],
        Tmin = (273.15,'K'),
        Tmax = (1998.15,'K'),
    ),
    shortDesc = u"""Smiles: C1=CCC=CO1
Info: mw=82.101 crc=817120797 symm=['C1', 1]
Filename: C5H5O_6
FKM: 383383.467921 70.6385 15.346 4.6885e-002 -1.4552e-005 -6.9339e+005
Aspen: 383383.467921 362322.609319 -1.362 8.9551e-002 -5.1704e-005 1.0745e-008""",
    longDesc = 
u"""

""",
)

