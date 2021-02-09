#!/usr/bin/env python
# encoding: utf-8

name = "CHOClBr_wb97xd3"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "BrC(DCC(Br)(Br)Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {8,S}
2  Br u0 p3 c0 {8,S}
3  Br u0 p3 c0 {8,S}
4  Br u0 p3 c0 {9,S}
5  Br u0 p3 c0 {9,S}
6  Br u0 p3 c0 {9,S}
7  Br u0 p3 c0 {10,S}
8  C  u0 p0 c0 {1,S} {2,S} {3,S} {11,S}
9  C  u0 p0 c0 {4,S} {5,S} {6,S} {10,S}
10 C  u0 p0 c0 {7,S} {9,S} {11,D}
11 C  u0 p0 c0 {8,S} {10,D} {12,S}
12 H  u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.63508,0.147988,-0.000206169,-7.95595e-07,2.07286e-09,29146.4,21.3588], Tmin=(10,'K'), Tmax=(250.5,'K')),
            NASAPolynomial(coeffs=[14.4555,0.0390321,-3.15487e-05,1.12889e-08,-1.4757e-12,28303.9,-24.3022], Tmin=(250.5,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (242.39,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 67.74 kcal/mol
S298: 135.88 cal/mol/K

Coordinates (Angstoms):
Br -0.30363 -2.06793 -1.03926
C -0.51870 -0.37682 -0.25087
C 0.49713 0.33211 0.22563
C 1.96596 0.00891 0.26279
Br 2.87711 1.49969 1.12164
Br 2.70445 -0.18449 -1.52323
Br 2.33024 -1.58314 1.31398
C -1.95874 0.11059 -0.20428
Br -2.15663 1.86241 0.60884
Br -2.66606 0.23465 -2.01054
Br -3.03352 -1.12959 0.83759
H 0.26242 1.29362 0.65772

modes:
""",
    rank = 5,
)

entry(
    index = 1,
    label = "BrC(Br)C(C(Br)Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {9,S}
2  Br u0 p3 c0 {9,S}
3  Br u0 p3 c0 {10,S}
4  Br u0 p3 c0 {10,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {11,S}
8  C  u0 p0 c0 {9,S} {10,S} {11,S} {12,S}
9  C  u0 p0 c0 {1,S} {2,S} {8,S} {13,S}
10 C  u0 p0 c0 {3,S} {4,S} {8,S} {14,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
12 H  u0 p0 c0 {8,S}
13 H  u0 p0 c0 {9,S}
14 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.87145,0.133572,0.000157377,-3.55292e-06,8.29392e-09,13523.7,19.6273], Tmin=(10,'K'), Tmax=(194.95,'K')),
            NASAPolynomial(coeffs=[12.4025,0.0483644,-3.60901e-05,1.22768e-08,-1.55172e-12,12942.3,-16.1495], Tmin=(194.95,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (113.248,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 36.75 kcal/mol
S298: 133.99 cal/mol/K

Coordinates (Angstoms):
Br 2.00988 -0.18983 1.73636
C 1.44600 0.44621 0.00559
Br 2.86276 0.19856 -1.29727
C 0.07718 -0.03105 -0.54341
C -1.01517 1.04516 -0.33295
Br -0.82428 2.41690 -1.69261
Br -1.07570 1.88079 1.40900
C -0.44448 -1.46618 -0.25085
Br 0.93887 -2.78886 -0.53013
Br -1.22218 -1.72068 1.50196
Br -1.85060 -1.83488 -1.56764
H 1.39125 1.52305 0.12094
H 0.21951 -0.05623 -1.62422
H -2.00096 0.62279 -0.48646

modes:
""",
    rank = 5,
)

entry(
    index = 2,
    label = "ClC(Cl)C(Cl)(Cl)CC(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {8,S}
2  Cl u0 p3 c0 {8,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
9  C  u0 p0 c0 {8,S} {11,S} {12,S} {13,S}
10 C  u0 p0 c0 {3,S} {4,S} {8,S} {14,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
12 H  u0 p0 c0 {9,S}
13 H  u0 p0 c0 {9,S}
14 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.79095,0.105088,-0.000162456,1.33677e-07,-4.43996e-11,-31620.3,17.3237], Tmin=(10,'K'), Tmax=(721.438,'K')),
            NASAPolynomial(coeffs=[14.5498,0.0398919,-2.69015e-05,8.41436e-09,-9.92592e-13,-33316.9,-35.5665], Tmin=(721.438,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-263.036,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -54.28 kcal/mol
S298: 116.09 cal/mol/K

Coordinates (Angstoms):
Cl 2.31848 1.71091 -0.33932
C 1.96328 -0.02351 -0.34569
Cl 1.88528 -0.60375 -2.01446
C 0.66911 -0.35521 0.44957
Cl 0.50214 -2.12174 0.42962
Cl 0.99070 0.13215 2.13810
C -0.53017 0.41324 -0.12489
C -1.97746 -0.03127 0.12180
Cl -2.31999 -0.42064 1.81000
Cl -2.43118 -1.40785 -0.90056
Cl -3.00437 1.34892 -0.35578
H 2.79595 -0.52742 0.13582
H -0.44462 1.43149 0.24991
H -0.41714 0.45468 -1.20916

modes:
""",
    rank = 5,
)

entry(
    index = 3,
    label = "ClCC(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {9,S}
2  Cl u0 p3 c0 {10,S}
3  Cl u0 p3 c0 {11,S}
4  Cl u0 p3 c0 {11,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {12,S}
7  Cl u0 p3 c0 {12,S}
8  Cl u0 p3 c0 {12,S}
9  C  u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
10 C  u0 p0 c0 {2,S} {9,S} {13,S} {14,S}
11 C  u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
12 C  u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
13 H  u0 p0 c0 {10,S}
14 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.90864,0.0961481,3.26758e-05,-5.30256e-07,6.09826e-10,-23198.2,17.0996], Tmin=(10,'K'), Tmax=(396.288,'K')),
            NASAPolynomial(coeffs=[14.3533,0.0475635,-3.67784e-05,1.27966e-08,-1.63919e-12,-24630.9,-34.152], Tmin=(396.288,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-192.866,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -36.83 kcal/mol
S298: 119.83 cal/mol/K

Coordinates (Angstoms):
Cl -0.69722 2.74288 0.66306
C 0.13521 1.43721 -0.18486
C -0.01589 -0.00728 0.39433
Cl -0.46266 0.00689 2.10741
C -1.20391 -0.77037 -0.35931
Cl -2.64472 0.27059 -0.33181
Cl -0.83323 -1.09347 -2.06205
Cl -1.67397 -2.30150 0.38725
C 1.44097 -0.66745 0.30065
Cl 2.52541 0.18590 1.42936
Cl 2.16783 -0.46847 -1.31201
Cl 1.48163 -2.37582 0.71279
H 1.18318 1.71131 -0.17416
H -0.20790 1.44098 -1.21600

modes:
""",
    rank = 5,
)

entry(
    index = 4,
    label = "ClC(Cl)C(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {10,S}
2  Cl u0 p3 c0 {11,S}
3  Cl u0 p3 c0 {11,S}
4  Cl u0 p3 c0 {12,S}
5  Cl u0 p3 c0 {12,S}
6  Cl u0 p3 c0 {12,S}
7  Cl u0 p3 c0 {13,S}
8  Cl u0 p3 c0 {13,S}
9  Cl u0 p3 c0 {13,S}
10 C  u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
11 C  u0 p0 c0 {2,S} {3,S} {10,S} {14,S}
12 C  u0 p0 c0 {4,S} {5,S} {6,S} {10,S}
13 C  u0 p0 c0 {7,S} {8,S} {9,S} {10,S}
14 H  u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.76819,0.107994,3.42233e-05,-6.28851e-07,7.3929e-10,-19973.3,17.1758], Tmin=(10,'K'), Tmax=(392.106,'K')),
            NASAPolynomial(coeffs=[16.5997,0.0468429,-3.76836e-05,1.34025e-08,-1.73988e-12,-21672.6,-44.4408], Tmin=(392.106,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-166.042,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -29.70 kcal/mol
S298: 124.32 cal/mol/K

Coordinates (Angstoms):
Cl -0.05459 1.40460 -2.17168
C 0.27618 1.40905 -0.43364
Cl -0.38293 2.90050 0.24793
C -0.08413 0.06749 0.35489
Cl -0.35046 0.48259 2.05884
C 1.25106 -0.83571 0.32799
Cl 2.54654 0.01039 1.22221
Cl 1.03200 -2.40845 1.08497
Cl 1.89130 -1.09389 -1.30407
C -1.43650 -0.65909 -0.12727
Cl -2.08917 -1.79703 1.07092
Cl -2.69210 0.57278 -0.35792
Cl -1.25752 -1.57272 -1.62876
H 1.35034 1.51948 -0.34441

modes:
""",
    rank = 5,
)

entry(
    index = 5,
    label = "BrOC(Br)(C(Br)(Br)Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {10,S}
2  Br u0 p3 c0 {11,S}
3  Br u0 p3 c0 {11,S}
4  Br u0 p3 c0 {11,S}
5  Br u0 p3 c0 {12,S}
6  Br u0 p3 c0 {12,S}
7  Br u0 p3 c0 {12,S}
8  Br u0 p3 c0 {9,S}
9  O  u0 p2 c0 {8,S} {10,S}
10 C  u0 p0 c0 {1,S} {9,S} {11,S} {12,S}
11 C  u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
12 C  u0 p0 c0 {5,S} {6,S} {7,S} {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.28825,0.177943,-0.000378069,-8.52564e-08,8.61543e-10,28778.5,20.5507], Tmin=(10,'K'), Tmax=(288.326,'K')),
            NASAPolynomial(coeffs=[17.8628,0.0365792,-3.12755e-05,1.15086e-08,-1.52791e-12,27569.9,-40.6027], Tmin=(288.326,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (239.354,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 68.09 kcal/mol
S298: 140.64 cal/mol/K

Coordinates (Angstoms):
Br -0.61914 -1.75857 2.41743
O -0.84104 -1.01730 0.77969
C 0.16468 -0.33075 0.12492
Br 1.87921 -1.27333 0.18536
C 0.33034 1.13781 0.78232
Br 1.08933 2.45886 -0.40247
Br -1.38389 1.80392 1.41939
Br 1.47417 1.10875 2.36307
C -0.33827 -0.44484 -1.40892
Br -1.92942 0.60113 -1.75317
Br 0.97582 0.02387 -2.75463
Br -0.80181 -2.30956 -1.75297

modes:
""",
    rank = 5,
)

entry(
    index = 6,
    label = "BrC(Br)DC(Br)C(Br)(Br)C(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {8,S}
2  Br u0 p3 c0 {8,S}
3  Br u0 p3 c0 {9,S}
4  Br u0 p3 c0 {9,S}
5  Br u0 p3 c0 {10,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
9  C  u0 p0 c0 {3,S} {4,S} {8,S} {12,S}
10 C  u0 p0 c0 {5,S} {8,S} {11,D}
11 C  u0 p0 c0 {6,S} {7,S} {10,D}
12 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.69122,0.144196,-0.000167851,-1.05411e-06,2.6223e-09,28959.7,20.3527], Tmin=(10,'K'), Tmax=(239.099,'K')),
            NASAPolynomial(coeffs=[13.8513,0.0400336,-3.22037e-05,1.14833e-08,-1.49749e-12,28190.1,-22.4534], Tmin=(239.099,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (240.85,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 67.23 kcal/mol
S298: 133.26 cal/mol/K

Coordinates (Angstoms):
Br -3.50857 0.85167 -0.03702
C -1.81074 0.07172 -0.20554
Br -1.71716 -0.96683 -1.77272
C -0.82865 0.23670 0.69232
Br -1.21959 1.28501 2.20571
C 0.58996 -0.37063 0.58647
Br 0.42076 -2.32445 0.61704
Br 1.74599 0.07940 2.08059
C 1.27979 0.07367 -0.72562
Br 1.34426 2.00204 -0.85128
Br 3.01988 -0.69043 -1.02084
H 0.68409 -0.24787 -1.56912

modes:
""",
    rank = 5,
)

entry(
    index = 7,
    label = "BrC(C(Br)C(Br)(Br)Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {9,S}
2  Br u0 p3 c0 {10,S}
3  Br u0 p3 c0 {11,S}
4  Br u0 p3 c0 {11,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {12,S}
7  Br u0 p3 c0 {12,S}
8  Br u0 p3 c0 {12,S}
9  C  u0 p0 c0 {1,S} {10,S} {12,S} {13,S}
10 C  u0 p0 c0 {2,S} {9,S} {11,S} {14,S}
11 C  u0 p0 c0 {3,S} {4,S} {5,S} {10,S}
12 C  u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
13 H  u0 p0 c0 {9,S}
14 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5426,0.1649,-8.05211e-05,-2.14421e-06,5.03573e-09,18149,20.5011], Tmin=(10,'K'), Tmax=(220.657,'K')),
            NASAPolynomial(coeffs=[15.1925,0.047034,-3.68989e-05,1.29685e-08,-1.67614e-12,17319.4,-27.5596], Tmin=(220.657,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (151.088,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 46.97 kcal/mol
S298: 142.05 cal/mol/K

Coordinates (Angstoms):
Br 0.93438 1.90797 -1.40338
C 0.62929 0.25105 -0.45067
C -0.62842 0.25309 0.45093
Br -0.92784 1.91077 1.40410
C -1.93237 -0.22095 -0.24871
Br -2.58901 1.00444 -1.58798
Br -3.31003 -0.49529 1.09192
Br -1.63118 -1.95399 -1.09279
C 1.93162 -0.22783 0.24856
Br 3.30892 -0.50465 -1.09190
Br 1.62504 -1.96121 1.09005
Br 2.59145 0.99374 1.58977
H 0.46038 -0.47921 -1.23947
H -0.46221 -0.47795 1.23958

modes:
""",
    rank = 5,
)

entry(
    index = 8,
    label = "BrCDC(C(Br)(Br)Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {8,S}
2  Br u0 p3 c0 {8,S}
3  Br u0 p3 c0 {8,S}
4  Br u0 p3 c0 {9,S}
5  Br u0 p3 c0 {9,S}
6  Br u0 p3 c0 {9,S}
7  Br u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {2,S} {3,S} {10,S}
9  C  u0 p0 c0 {4,S} {5,S} {6,S} {10,S}
10 C  u0 p0 c0 {8,S} {9,S} {11,D}
11 C  u0 p0 c0 {7,S} {10,D} {12,S}
12 H  u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.60754,0.146791,-0.000243124,-4.10756e-07,1.24821e-09,35292.7,19.8329], Tmin=(10,'K'), Tmax=(272.579,'K')),
            NASAPolynomial(coeffs=[14.7598,0.0383521,-3.09939e-05,1.10939e-08,-1.45048e-12,34370.6,-27.7616], Tmin=(272.579,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (293.5,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 79.92 kcal/mol
S298: 132.10 cal/mol/K

Coordinates (Angstoms):
Br -2.32482 -2.00515 -0.00088
C -0.57364 -1.40012 0.17007
C -0.05430 -0.17932 0.02689
C -0.93401 1.03589 -0.33773
Br -0.09830 2.78445 -0.52441
Br -1.78242 0.71287 -2.06700
Br -2.28535 1.28599 1.04978
C 1.45556 -0.03522 0.23637
Br 2.31930 0.57686 -1.39963
Br 1.83221 1.14936 1.73687
Br 2.37821 -1.70125 0.68313
H 0.06755 -2.22436 0.42653

modes:
""",
    rank = 5,
)

entry(
    index = 9,
    label = "ClC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {9,S}
2  Cl u0 p3 c0 {9,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {10,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  Cl u0 p3 c0 {11,S}
9  C  u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
10 C  u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
11 C  u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.07391,0.0778134,0.00012696,-8.21296e-07,9.03773e-10,-19233.3,15.9444], Tmin=(10,'K'), Tmax=(384.758,'K')),
            NASAPolynomial(coeffs=[15.1941,0.0348701,-2.94356e-05,1.07567e-08,-1.42022e-12,-20780.7,-38.9413], Tmin=(384.758,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-159.873,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -29.68 kcal/mol
S298: 112.91 cal/mol/K

Coordinates (Angstoms):
Cl -1.74502 0.35173 1.73000
C -1.30368 0.53544 0.03193
Cl -1.01584 2.24658 -0.28734
Cl -2.71344 0.04989 -0.93469
C -0.06294 -0.38943 -0.38965
Cl -0.54609 -2.06460 -0.08696
Cl 0.19023 -0.14865 -2.12419
C 1.35998 -0.18151 0.32120
Cl 2.03281 1.42635 0.04762
Cl 2.50306 -1.35432 -0.36864
Cl 1.30093 -0.47147 2.06071

modes:
""",
    rank = 5,
)

entry(
    index = 10,
    label = "ClC(Cl)DC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {9,S}
2  Cl u0 p3 c0 {9,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {10,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {12,S}
8  Cl u0 p3 c0 {12,S}
9  C  u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
10 C  u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
11 C  u0 p0 c0 {6,S} {9,S} {12,D}
12 C  u0 p0 c0 {7,S} {8,S} {11,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.86514,0.100232,-2.62616e-05,-3.74538e-07,4.64822e-10,-11391.3,17.1656], Tmin=(10,'K'), Tmax=(409.148,'K')),
            NASAPolynomial(coeffs=[15.6429,0.0384786,-3.14435e-05,1.12424e-08,-1.46166e-12,-12965.6,-39.5216], Tmin=(409.148,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-94.7171,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -13.59 kcal/mol
S298: 118.84 cal/mol/K

Coordinates (Angstoms):
Cl 2.32476 -0.58465 1.51107
C 1.92766 0.35617 0.14289
Cl 3.33949 0.81803 -0.71606
C 0.70440 0.72224 -0.27930
Cl 0.64163 1.67464 -1.71524
C -0.66659 0.40125 0.35645
Cl -1.82062 1.71020 0.01497
Cl -0.57761 0.30119 2.12514
C -1.29027 -0.95512 -0.19779
Cl -1.49121 -0.87163 -1.95090
Cl -2.86634 -1.25717 0.53759
Cl -0.22529 -2.31515 0.17118

modes:
""",
    rank = 5,
)

entry(
    index = 11,
    label = "ClC(C(Cl)(Cl)Cl)C(Cl)(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {10,S}
2  Cl u0 p3 c0 {11,S}
3  Cl u0 p3 c0 {11,S}
4  Cl u0 p3 c0 {12,S}
5  Cl u0 p3 c0 {12,S}
6  Cl u0 p3 c0 {12,S}
7  Cl u0 p3 c0 {13,S}
8  Cl u0 p3 c0 {13,S}
9  Cl u0 p3 c0 {13,S}
10 C  u0 p0 c0 {1,S} {11,S} {12,S} {14,S}
11 C  u0 p0 c0 {2,S} {3,S} {10,S} {13,S}
12 C  u0 p0 c0 {4,S} {5,S} {6,S} {10,S}
13 C  u0 p0 c0 {7,S} {8,S} {9,S} {11,S}
14 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.68782,0.117036,-5.4378e-05,-3.52814e-07,4.62894e-10,-25470.2,18.0756], Tmin=(10,'K'), Tmax=(409.07,'K')),
            NASAPolynomial(coeffs=[16.6729,0.0462745,-3.68778e-05,1.30104e-08,-1.67814e-12,-27166.5,-43.642], Tmin=(409.07,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-211.778,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -40.60 kcal/mol
S298: 126.49 cal/mol/K

Coordinates (Angstoms):
Cl 1.70539 1.55851 0.17719
C 0.71648 0.14906 -0.23566
C 1.64521 -1.10728 -0.33049
Cl 0.83339 -2.42042 -1.20663
Cl 2.18710 -1.65122 1.25685
Cl 3.07302 -0.70548 -1.31097
C -0.59112 0.08735 0.67697
Cl -0.34954 0.86247 2.24838
Cl -1.15054 -1.55930 1.02489
C -1.79141 0.81780 -0.07340
Cl -1.39110 2.49817 -0.44035
Cl -2.12566 -0.01921 -1.60346
Cl -3.25251 0.79759 0.91115
H 0.37355 0.31215 -1.25560

modes:
""",
    rank = 5,
)

entry(
    index = 12,
    label = "CC(Br)(C(Br)(Br)Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {8,S}
2  Br u0 p3 c0 {10,S}
3  Br u0 p3 c0 {10,S}
4  Br u0 p3 c0 {10,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
9  C  u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
10 C  u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
12 H  u0 p0 c0 {9,S}
13 H  u0 p0 c0 {9,S}
14 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.64996,0.137383,-0.000138536,-6.02514e-07,1.25776e-09,21960.7,19.436], Tmin=(10,'K'), Tmax=(291.444,'K')),
            NASAPolynomial(coeffs=[14.6999,0.044519,-3.38274e-05,1.17402e-08,-1.50899e-12,20950.3,-29.1254], Tmin=(291.444,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (182.669,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 53.72 kcal/mol
S298: 132.12 cal/mol/K

Coordinates (Angstoms):
C 0.43769 1.39003 -0.20326
C 0.01221 0.02864 0.35943
Br 0.10606 0.14498 2.31770
C -1.53023 -0.23320 0.03143
Br -1.86850 -0.57697 -1.84929
Br -2.56603 1.37272 0.47357
Br -2.39718 -1.66378 1.02190
C 1.09177 -1.05381 -0.11408
Br 2.82407 -0.70229 0.73596
Br 0.66161 -2.89300 0.28342
Br 1.48831 -0.95382 -2.02719
H -0.02765 2.19438 0.35456
H 0.15088 1.47367 -1.25073
H 1.51650 1.49995 -0.12703

modes:
""",
    rank = 5,
)

entry(
    index = 13,
    label = "ClC(Cl)C(C(Cl)Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {9,S}
2  Cl u0 p3 c0 {9,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  C  u0 p0 c0 {9,S} {10,S} {11,S} {12,S}
9  C  u0 p0 c0 {1,S} {2,S} {8,S} {13,S}
10 C  u0 p0 c0 {3,S} {4,S} {8,S} {14,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
12 H  u0 p0 c0 {8,S}
13 H  u0 p0 c0 {9,S}
14 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.87208,0.107717,-0.000186652,1.8226e-07,-7.31098e-11,-29968.3,16.8794], Tmin=(10,'K'), Tmax=(597.13,'K')),
            NASAPolynomial(coeffs=[12.0002,0.0465704,-3.30514e-05,1.0773e-08,-1.31351e-12,-31058.5,-22.4517], Tmin=(597.13,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-249.218,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -50.97 kcal/mol
S298: 116.29 cal/mol/K

Coordinates (Angstoms):
Cl 2.42884 0.82766 1.28280
C 1.45187 -0.24907 0.25957
Cl 2.22066 -0.45093 -1.31740
C -0.03513 0.17826 0.25291
C -0.96950 -1.04127 0.40975
Cl -0.96651 -1.55305 2.11413
Cl -0.56669 -2.42744 -0.61374
C -0.54453 1.16943 -0.82722
Cl 0.56304 2.53387 -0.99697
Cl -0.82572 0.44198 -2.41203
Cl -2.11106 1.81712 -0.24637
H 1.50995 -1.22039 0.74154
H -0.16281 0.74091 1.17745
H -1.99241 -0.76707 0.17558

modes:
""",
    rank = 5,
)

entry(
    index = 14,
    label = "BrC(Br)(Br)OC(Br)(Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {10,S}
2  Br u0 p3 c0 {10,S}
3  Br u0 p3 c0 {11,S}
4  Br u0 p3 c0 {11,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {12,S}
7  Br u0 p3 c0 {12,S}
8  Br u0 p3 c0 {12,S}
9  O  u0 p2 c0 {10,S} {12,S}
10 C  u0 p0 c0 {1,S} {2,S} {9,S} {11,S}
11 C  u0 p0 c0 {3,S} {4,S} {5,S} {10,S}
12 C  u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.31335,0.178934,-0.000353687,-3.41751e-07,1.38823e-09,9522.23,21.1236], Tmin=(10,'K'), Tmax=(270.08,'K')),
            NASAPolynomial(coeffs=[17.5339,0.0372463,-3.18241e-05,1.17099e-08,-1.55512e-12,8394.67,-38.0364], Tmin=(270.08,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (79.2372,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 29.84 kcal/mol
S298: 142.37 cal/mol/K

Coordinates (Angstoms):
Br 3.21098 -0.80006 -0.09971
C 1.82625 0.53102 0.16724
Br 2.04613 1.92665 -1.17678
Br 2.05000 1.31321 1.92738
O 0.65969 -0.16547 -0.04087
C -0.62749 0.05308 0.40290
Br -0.85883 -0.67740 2.20301
Br -1.17374 1.91769 0.43257
C -1.51732 -0.76278 -0.61942
Br -1.27763 -0.04025 -2.40065
Br -0.95279 -2.61560 -0.64366
Br -3.38526 -0.68007 -0.15201

modes:
""",
    rank = 5,
)

entry(
    index = 15,
    label = "CC(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {8,S}
2  Cl u0 p3 c0 {10,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
9  C  u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
10 C  u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
12 H  u0 p0 c0 {9,S}
13 H  u0 p0 c0 {9,S}
14 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.18266,0.0682851,0.000209377,-1.01225e-06,1.07851e-09,-24413.6,16.1806], Tmin=(10,'K'), Tmax=(372.668,'K')),
            NASAPolynomial(coeffs=[12.6431,0.0480305,-3.62854e-05,1.2519e-08,-1.59982e-12,-25683.2,-27.6957], Tmin=(372.668,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-202.928,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -39.89 kcal/mol
S298: 113.58 cal/mol/K

Coordinates (Angstoms):
C 0.45500 1.38829 -0.16160
C 0.02324 0.01937 0.36791
Cl 0.12136 0.04847 2.15123
C 1.07112 -1.07070 -0.14832
Cl 0.62208 -2.73526 0.21275
Cl 2.65244 -0.77440 0.62094
Cl 1.35686 -0.94063 -1.89838
C -1.51492 -0.23568 0.02806
Cl -2.24804 -1.58885 0.89747
Cl -2.44836 1.21337 0.49247
Cl -1.78379 -0.49089 -1.70303
H 0.19208 1.49461 -1.21246
H -0.03019 2.17404 0.40684
H 1.53111 1.49827 -0.05387

modes:
""",
    rank = 5,
)

entry(
    index = 16,
    label = "ClC(Cl)DC(C(Cl)Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {8,S}
2  Cl u0 p3 c0 {8,S}
3  Cl u0 p3 c0 {9,S}
4  Cl u0 p3 c0 {9,S}
5  Cl u0 p3 c0 {9,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {2,S} {10,S} {12,S}
9  C  u0 p0 c0 {3,S} {4,S} {5,S} {10,S}
10 C  u0 p0 c0 {8,S} {9,S} {11,D}
11 C  u0 p0 c0 {6,S} {7,S} {10,D}
12 H  u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.79273,0.105618,-0.000182729,1.61579e-07,-5.66296e-11,-12586.1,17.2755], Tmin=(10,'K'), Tmax=(691.655,'K')),
            NASAPolynomial(coeffs=[15.5491,0.0318449,-2.27371e-05,7.36761e-09,-8.89748e-13,-14350.7,-39.5638], Tmin=(691.655,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-104.772,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -16.66 kcal/mol
S298: 114.98 cal/mol/K

Coordinates (Angstoms):
Cl -2.57480 -0.75801 0.96099
C -1.49687 0.22914 0.08272
Cl -2.34060 1.49650 -0.72588
C -0.16672 0.06502 0.01487
C 0.61476 1.05201 -0.81499
Cl 1.72623 2.04029 0.15623
Cl 1.41148 0.30463 -2.21496
C 0.53136 -1.08534 0.75784
Cl 0.25144 -0.94551 2.51271
Cl -0.07584 -2.65438 0.16856
Cl 2.28765 -1.12344 0.54199
H -0.07245 1.76435 -1.24462

modes:
""",
    rank = 5,
)

entry(
    index = 17,
    label = "BrC(Br)DC(C(Br)Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {8,S}
2  Br u0 p3 c0 {8,S}
3  Br u0 p3 c0 {9,S}
4  Br u0 p3 c0 {9,S}
5  Br u0 p3 c0 {9,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {2,S} {10,S} {12,S}
9  C  u0 p0 c0 {3,S} {4,S} {5,S} {10,S}
10 C  u0 p0 c0 {8,S} {9,S} {11,D}
11 C  u0 p0 c0 {6,S} {7,S} {10,D}
12 H  u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.69521,0.14488,-0.000146745,-1.2626e-06,3.07811e-09,31368.7,20.5345], Tmin=(10,'K'), Tmax=(233.477,'K')),
            NASAPolynomial(coeffs=[13.9347,0.0396556,-3.18064e-05,1.13223e-08,-1.47501e-12,30605.8,-22.4373], Tmin=(233.477,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (260.894,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 72.06 kcal/mol
S298: 134.04 cal/mol/K

Coordinates (Angstoms):
Br -0.66704 2.59504 1.31317
C 0.33637 1.06404 0.83762
Br 2.04144 1.17474 1.59806
C -0.14115 0.07039 0.06572
C -1.55444 0.22100 -0.43464
Br -2.78959 -1.08347 0.29196
Br -1.68566 0.44551 -2.35523
C 0.70854 -1.15951 -0.29659
Br -0.16382 -2.48705 -1.41987
Br 1.21511 -2.13491 1.31681
Br 2.28929 -0.61894 -1.30660
H -1.95441 1.14970 -0.06490

modes:
""",
    rank = 5,
)

entry(
    index = 18,
    label = "BrC(Br)(Br)CC(Br)(Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {10,S}
2  Br u0 p3 c0 {10,S}
3  Br u0 p3 c0 {11,S}
4  Br u0 p3 c0 {11,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {12,S}
7  Br u0 p3 c0 {12,S}
8  Br u0 p3 c0 {12,S}
9  C  u0 p0 c0 {10,S} {11,S} {13,S} {14,S}
10 C  u0 p0 c0 {1,S} {2,S} {9,S} {12,S}
11 C  u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
12 C  u0 p0 c0 {6,S} {7,S} {8,S} {10,S}
13 H  u0 p0 c0 {9,S}
14 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.47166,0.167224,-0.000167654,-1.3384e-06,3.16618e-09,20871,20.6807], Tmin=(10,'K'), Tmax=(241.89,'K')),
            NASAPolynomial(coeffs=[15.8841,0.0457125,-3.6014e-05,1.27204e-08,-1.65097e-12,19928.8,-31.0551], Tmin=(241.89,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (173.599,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 52.46 kcal/mol
S298: 142.23 cal/mol/K

Coordinates (Angstoms):
Br -2.27322 -1.50768 -1.61515
C -1.98736 -0.14982 -0.27190
Br -3.08494 1.39776 -0.74018
Br -2.62444 -0.78794 1.44754
C -0.55050 0.39096 -0.19639
C 0.71319 -0.50635 -0.16467
Br 1.25678 -0.88680 -2.00340
Br 0.47864 -2.21428 0.72555
C 1.88307 0.27352 0.55197
Br 2.17700 1.99595 -0.30712
Br 1.42384 0.62362 2.41166
Br 3.55106 -0.70131 0.52631
H -0.42339 1.04725 -1.05446
H -0.53974 1.02512 0.69025

modes:
""",
    rank = 5,
)

entry(
    index = 19,
    label = "BrC(Br)C(Br)(Br)OC(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {9,S}
2  Br u0 p3 c0 {9,S}
3  Br u0 p3 c0 {10,S}
4  Br u0 p3 c0 {10,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {11,S}
8  O  u0 p2 c0 {9,S} {11,S}
9  C  u0 p0 c0 {1,S} {2,S} {8,S} {10,S}
10 C  u0 p0 c0 {3,S} {4,S} {9,S} {12,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
12 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.62777,0.149498,-0.000216217,-7.80607e-07,2.09294e-09,1235.76,20.4574], Tmin=(10,'K'), Tmax=(248.05,'K')),
            NASAPolynomial(coeffs=[14.323,0.040017,-3.25915e-05,1.16991e-08,-1.53152e-12,412.168,-24.567], Tmin=(248.05,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (10.3302,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 12.31 kcal/mol
S298: 134.36 cal/mol/K

Coordinates (Angstoms):
Br 1.52635 0.89832 2.19907
C 1.76794 0.03792 0.48934
Br 2.52537 1.29580 -0.76160
C 0.45651 -0.59076 -0.03431
Br 0.88056 -1.55771 -1.68921
Br -0.14994 -1.92092 1.25617
O -0.40602 0.45549 -0.26904
C -1.77604 0.48962 -0.36355
Br -2.13541 2.08279 -1.40645
Br -2.58002 0.71295 1.39882
Br -2.59997 -1.02833 -1.24663
H 2.49710 -0.75247 0.62836

modes:
""",
    rank = 5,
)

entry(
    index = 20,
    label = "ClCC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {9,S}
2  Cl u0 p3 c0 {9,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {12,S}
7  Cl u0 p3 c0 {12,S}
8  Cl u0 p3 c0 {12,S}
9  C  u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
10 C  u0 p0 c0 {3,S} {4,S} {9,S} {12,S}
11 C  u0 p0 c0 {5,S} {9,S} {13,S} {14,S}
12 C  u0 p0 c0 {6,S} {7,S} {8,S} {10,S}
13 H  u0 p0 c0 {11,S}
14 H  u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.89097,0.0981494,1.86481e-05,-4.96516e-07,5.82687e-10,-25864.2,16.976], Tmin=(10,'K'), Tmax=(395.871,'K')),
            NASAPolynomial(coeffs=[14.3461,0.0475902,-3.67786e-05,1.27879e-08,-1.63713e-12,-27281.9,-34.1247], Tmin=(395.871,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-215.032,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -42.10 kcal/mol
S298: 119.81 cal/mol/K

Coordinates (Angstoms):
Cl 2.93527 0.56699 1.47599
C 1.26594 0.14092 1.08592
C 0.98807 0.06954 -0.41920
Cl 1.25685 1.67372 -1.12727
Cl 2.15672 -1.03511 -1.18198
C -0.48198 -0.48571 -0.75383
Cl -0.71444 -0.36437 -2.50114
Cl -0.54160 -2.19885 -0.28400
C -1.74543 0.20185 -0.04906
Cl -3.23354 -0.51153 -0.69423
Cl -1.81210 1.93964 -0.32754
Cl -1.76650 -0.07739 1.70536
H 1.05764 -0.82375 1.54105
H 0.63510 0.90405 1.52994

modes:
""",
    rank = 5,
)

entry(
    index = 21,
    label = "BrC(DC(Br)C(Br)(Br)Br)C(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {8,S}
2  Br u0 p3 c0 {8,S}
3  Br u0 p3 c0 {8,S}
4  Br u0 p3 c0 {9,S}
5  Br u0 p3 c0 {9,S}
6  Br u0 p3 c0 {10,S}
7  Br u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {2,S} {3,S} {11,S}
9  C  u0 p0 c0 {4,S} {5,S} {10,S} {12,S}
10 C  u0 p0 c0 {6,S} {9,S} {11,D}
11 C  u0 p0 c0 {7,S} {8,S} {10,D}
12 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.69869,0.144721,-0.000147967,-1.25786e-06,3.08217e-09,28761.2,20.5589], Tmin=(10,'K'), Tmax=(232.7,'K')),
            NASAPolynomial(coeffs=[13.8296,0.0400753,-3.22208e-05,1.14817e-08,-1.49647e-12,28008.5,-21.9557], Tmin=(232.7,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (239.218,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 66.86 kcal/mol
S298: 134.02 cal/mol/K

Coordinates (Angstoms):
Br 1.95511 -0.37413 2.11377
C 0.74587 -0.12524 0.69635
C -0.58255 -0.13064 0.89697
Br -1.24532 -0.39176 2.63556
C -1.62541 0.06627 -0.21904
Br -1.37843 1.81296 -1.05846
Br -3.47468 0.01797 0.35534
Br -1.44631 -1.34971 -1.55214
C 1.41460 0.07215 -0.63327
Br 2.50103 1.67265 -0.65275
Br 2.43765 -1.48468 -1.15387
H 0.69844 0.21417 -1.42846

modes:
""",
    rank = 5,
)

entry(
    index = 22,
    label = "BrC(Br)DC(Br)C(Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {8,S}
2  Br u0 p3 c0 {9,S}
3  Br u0 p3 c0 {9,S}
4  Br u0 p3 c0 {9,S}
5  Br u0 p3 c0 {10,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {9,S} {10,S} {12,S}
9  C  u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
10 C  u0 p0 c0 {5,S} {8,S} {11,D}
11 C  u0 p0 c0 {6,S} {7,S} {10,D}
12 H  u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.71132,0.144611,-0.000119276,-1.51671e-06,3.65509e-09,25202,20.86], Tmin=(10,'K'), Tmax=(226.536,'K')),
            NASAPolynomial(coeffs=[13.837,0.039783,-3.18328e-05,1.13093e-08,-1.47116e-12,24462.9,-21.484], Tmin=(226.536,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (209.657,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 59.80 kcal/mol
S298: 134.90 cal/mol/K

Coordinates (Angstoms):
Br 1.77217 1.91512 -1.32736
C 1.92538 0.61329 0.02521
Br 3.69961 0.20192 0.44230
C 0.86700 0.04790 0.61360
Br 1.12007 -1.22501 1.97141
C -0.54212 0.44286 0.26832
Br -1.37265 1.34077 1.77787
C -1.46892 -0.63284 -0.35713
Br -2.19245 -1.93118 0.87344
Br -0.46724 -1.55731 -1.74127
Br -2.95383 0.28958 -1.20966
H -0.47933 1.21753 -0.48939

modes:
""",
    rank = 5,
)

entry(
    index = 23,
    label = "ClC(DC(Cl)C(Cl)(Cl)Cl)C(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {8,S}
2  Cl u0 p3 c0 {8,S}
3  Cl u0 p3 c0 {8,S}
4  Cl u0 p3 c0 {9,S}
5  Cl u0 p3 c0 {9,S}
6  Cl u0 p3 c0 {10,S}
7  Cl u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {2,S} {3,S} {11,S}
9  C  u0 p0 c0 {4,S} {5,S} {10,S} {12,S}
10 C  u0 p0 c0 {6,S} {9,S} {11,D}
11 C  u0 p0 c0 {7,S} {8,S} {10,D}
12 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.81546,0.106852,-0.000191013,1.76622e-07,-6.49888e-11,-14512.2,17.3026], Tmin=(10,'K'), Tmax=(658.389,'K')),
            NASAPolynomial(coeffs=[14.8419,0.0337859,-2.4547e-05,8.0634e-09,-9.84353e-13,-16095.8,-35.6913], Tmin=(658.389,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-120.762,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -20.46 kcal/mol
S298: 115.52 cal/mol/K

Coordinates (Angstoms):
Cl 1.93298 -0.35049 1.90304
C 0.77912 -0.13950 0.65530
C -0.51058 0.08015 0.94359
Cl -1.00915 0.14783 2.57881
C -1.60680 0.28052 -0.12192
Cl -1.21933 1.70366 -1.12414
Cl -1.71354 -1.16627 -1.15887
Cl -3.20810 0.54611 0.56327
C 1.35415 -0.22801 -0.73259
Cl 2.55495 1.04771 -0.99656
Cl 2.04961 -1.83240 -1.01945
H 0.59670 -0.08931 -1.49049

modes:
""",
    rank = 5,
)

entry(
    index = 24,
    label = "BrC(Br)C(C(Br)(Br)Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {10,S}
2  Br u0 p3 c0 {10,S}
3  Br u0 p3 c0 {11,S}
4  Br u0 p3 c0 {11,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {12,S}
7  Br u0 p3 c0 {12,S}
8  Br u0 p3 c0 {12,S}
9  C  u0 p0 c0 {10,S} {11,S} {12,S} {13,S}
10 C  u0 p0 c0 {1,S} {2,S} {9,S} {14,S}
11 C  u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
12 C  u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
13 H  u0 p0 c0 {9,S}
14 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.00859,0.19965,-0.000666109,1.14568e-06,-7.61905e-10,25687.9,21.0876], Tmin=(10,'K'), Tmax=(385.262,'K')),
            NASAPolynomial(coeffs=[16.6439,0.0421942,-3.1634e-05,1.06947e-08,-1.33883e-12,24601.1,-35.0298], Tmin=(385.262,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (213.562,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 61.95 kcal/mol
S298: 141.20 cal/mol/K

Coordinates (Angstoms):
Br 0.04435 -1.74406 2.19639
C -0.73457 -1.17213 0.52292
Br -1.17393 -2.70027 -0.58721
C -0.02880 -0.04357 -0.29714
C 1.53880 -0.04588 -0.36382
Br 2.25415 -1.85733 -0.41964
Br 2.12693 0.72040 -2.06646
Br 2.40671 0.89721 1.08230
C -0.78250 1.30940 0.02384
Br -2.57153 1.11369 -0.76103
Br -0.04357 2.92267 -0.74192
Br -1.01857 1.65232 1.92247
H -1.70772 -0.80502 0.81978
H -0.30974 -0.24742 -1.33048

modes:
""",
    rank = 5,
)

entry(
    index = 25,
    label = "ClC(Cl)C(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {10,S}
2  Cl u0 p3 c0 {10,S}
3  Cl u0 p3 c0 {11,S}
4  Cl u0 p3 c0 {11,S}
5  Cl u0 p3 c0 {12,S}
6  Cl u0 p3 c0 {12,S}
7  Cl u0 p3 c0 {13,S}
8  Cl u0 p3 c0 {13,S}
9  Cl u0 p3 c0 {13,S}
10 C  u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
11 C  u0 p0 c0 {3,S} {4,S} {10,S} {13,S}
12 C  u0 p0 c0 {5,S} {6,S} {10,S} {14,S}
13 C  u0 p0 c0 {7,S} {8,S} {9,S} {11,S}
14 H  u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.76626,0.108282,2.59084e-05,-5.95616e-07,7.02023e-10,-23871.2,17.3148], Tmin=(10,'K'), Tmax=(394.473,'K')),
            NASAPolynomial(coeffs=[16.5052,0.0469956,-3.77536e-05,1.34096e-08,-1.73891e-12,-25562.2,-43.8825], Tmin=(394.473,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-198.455,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -37.47 kcal/mol
S298: 124.44 cal/mol/K

Coordinates (Angstoms):
Cl -3.01105 1.19658 0.77982
C -1.35576 0.58879 0.92754
Cl -1.20922 -0.20482 2.49446
C -0.95817 -0.30885 -0.29085
Cl -1.97555 -1.75798 -0.30204
Cl -1.36037 0.63207 -1.74388
C 0.58833 -0.78674 -0.37205
Cl 0.81638 -1.52047 -1.97059
Cl 0.89605 -2.04270 0.83584
C 1.74259 0.31030 -0.18305
Cl 1.59996 1.65884 -1.31020
Cl 1.76018 0.97054 1.46067
Cl 3.32034 -0.45027 -0.44952
H -0.70830 1.45993 0.93526

modes:
""",
    rank = 5,
)

entry(
    index = 26,
    label = "ClC(DC(Cl)C(Cl)(Cl)Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {9,S}
2  Cl u0 p3 c0 {9,S}
3  Cl u0 p3 c0 {9,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {10,S}
6  Cl u0 p3 c0 {10,S}
7  Cl u0 p3 c0 {11,S}
8  Cl u0 p3 c0 {12,S}
9  C  u0 p0 c0 {1,S} {2,S} {3,S} {12,S}
10 C  u0 p0 c0 {4,S} {5,S} {6,S} {11,S}
11 C  u0 p0 c0 {7,S} {10,S} {12,D}
12 C  u0 p0 c0 {8,S} {9,S} {11,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.80035,0.107191,-8.37615e-05,-2.13305e-07,3.15526e-10,-9496.08,17.6834], Tmin=(10,'K'), Tmax=(420.038,'K')),
            NASAPolynomial(coeffs=[15.7774,0.0379943,-3.08616e-05,1.0974e-08,-1.42043e-12,-11066,-39.3778], Tmin=(420.038,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-78.9768,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -9.76 kcal/mol
S298: 120.43 cal/mol/K

Coordinates (Angstoms):
Cl 0.08287 2.07184 0.49546
C 0.47877 0.44182 0.16178
C -0.47877 -0.44180 -0.16173
Cl -0.08285 -2.07178 -0.49552
C -1.98208 -0.09072 -0.26467
Cl -2.58159 0.49036 1.30506
Cl -2.98832 -1.47444 -0.70842
Cl -2.23143 1.14326 -1.52057
C 1.98207 0.09072 0.26469
Cl 2.58155 -0.49024 -1.30509
Cl 2.23144 -1.14338 1.52047
Cl 2.98836 1.47437 0.70855

modes:
""",
    rank = 5,
)

entry(
    index = 27,
    label = "CC(Br)(Br)C(Br)(Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {8,S}
2  Br u0 p3 c0 {8,S}
3  Br u0 p3 c0 {9,S}
4  Br u0 p3 c0 {9,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
9  C  u0 p0 c0 {3,S} {4,S} {8,S} {11,S}
10 C  u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
12 H  u0 p0 c0 {10,S}
13 H  u0 p0 c0 {10,S}
14 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.65922,0.136253,-0.000138586,-5.78639e-07,1.20972e-09,20647.6,19.0741], Tmin=(10,'K'), Tmax=(292.87,'K')),
            NASAPolynomial(coeffs=[14.5606,0.0447688,-3.39968e-05,1.17914e-08,-1.51471e-12,19645.7,-28.9311], Tmin=(292.87,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (171.751,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 51.06 kcal/mol
S298: 131.07 cal/mol/K

Coordinates (Angstoms):
C -1.04099 -0.72071 1.21870
C -1.04593 -0.17445 -0.19994
Br -2.12754 -1.40877 -1.28110
Br -2.09396 1.47657 -0.16323
C 0.38651 -0.00753 -0.88643
Br 1.12616 -1.80471 -1.13100
Br 0.13496 0.78179 -2.64584
C 1.53064 0.82520 -0.14207
Br 2.08979 0.04169 1.55389
Br 1.05574 2.66668 0.21871
Br 3.14649 0.88714 -1.23694
H -2.06754 -0.93427 1.50700
H -0.46008 -1.64011 1.27638
H -0.63424 0.01148 1.91185

modes:
""",
    rank = 5,
)

entry(
    index = 28,
    label = "BrOC(Br)(C(Br)Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {9,S}
2  Br u0 p3 c0 {10,S}
3  Br u0 p3 c0 {10,S}
4  Br u0 p3 c0 {11,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {8,S}
8  O  u0 p2 c0 {7,S} {9,S}
9  C  u0 p0 c0 {1,S} {8,S} {10,S} {11,S}
10 C  u0 p0 c0 {2,S} {3,S} {9,S} {12,S}
11 C  u0 p0 c0 {4,S} {5,S} {6,S} {9,S}
12 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.61988,0.149527,-0.000228378,-6.73668e-07,1.86858e-09,16298.5,20.1312], Tmin=(10,'K'), Tmax=(252.379,'K')),
            NASAPolynomial(coeffs=[14.3639,0.0399896,-3.25955e-05,1.1706e-08,-1.53281e-12,15461.8,-25.1902], Tmin=(252.379,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (135.568,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 42.23 kcal/mol
S298: 133.56 cal/mol/K

Coordinates (Angstoms):
Br 1.56040 0.28742 2.62847
O 0.09569 0.26598 1.57355
C 0.14330 0.27137 0.16496
Br 1.90559 0.43123 -0.61636
C -0.71826 1.52437 -0.18395
Br -1.07346 1.86533 -2.04006
Br 0.02582 3.11122 0.63005
C -0.49162 -1.12823 -0.25486
Br -2.34614 -1.19058 0.33351
Br 0.46608 -2.54709 0.66178
Br -0.44214 -1.54215 -2.14044
H -1.68421 1.38822 0.28868

modes:
""",
    rank = 5,
)

entry(
    index = 29,
    label = "BrCC(Br)(Br)C(Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {8,S}
2  Br u0 p3 c0 {8,S}
3  Br u0 p3 c0 {9,S}
4  Br u0 p3 c0 {10,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
9  C  u0 p0 c0 {3,S} {8,S} {11,S} {12,S}
10 C  u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
12 H  u0 p0 c0 {9,S}
13 H  u0 p0 c0 {10,S}
14 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.77318,0.136621,-4.59108e-05,-1.61264e-06,3.57323e-09,14439,19.8853], Tmin=(10,'K'), Tmax=(229.173,'K')),
            NASAPolynomial(coeffs=[12.7921,0.0484963,-3.68837e-05,1.27577e-08,-1.63385e-12,13752,-18.6593], Tmin=(229.173,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (120.155,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 38.58 kcal/mol
S298: 133.42 cal/mol/K

Coordinates (Angstoms):
Br -2.37362 0.47977 -1.93614
C -2.03671 0.15927 -0.05716
C -0.61396 0.49117 0.40939
Br -0.43116 2.42830 0.18699
Br -0.63332 0.07922 2.31046
C 0.50745 -0.25362 -0.37529
Br -0.05587 -2.07040 -0.81694
C 1.99006 -0.33343 0.13004
Br 3.07440 -0.78714 -1.43129
Br 2.31885 -1.67882 1.48921
Br 2.68918 1.33728 0.81450
H -2.26050 -0.88578 0.12743
H -2.72968 0.78930 0.49110
H 0.55488 0.24488 -1.34230

modes:
""",
    rank = 5,
)

entry(
    index = 30,
    label = "ClCC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {8,S}
2  Cl u0 p3 c0 {9,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
9  C  u0 p0 c0 {2,S} {8,S} {12,S} {13,S}
10 C  u0 p0 c0 {3,S} {4,S} {8,S} {14,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
12 H  u0 p0 c0 {9,S}
13 H  u0 p0 c0 {9,S}
14 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.77477,0.102248,-0.000148559,1.12706e-07,-3.4311e-11,-28823.6,16.8921], Tmin=(10,'K'), Tmax=(786.843,'K')),
            NASAPolynomial(coeffs=[15.5982,0.0370591,-2.4286e-05,7.41289e-09,-8.56837e-13,-30841.6,-41.8993], Tmin=(786.843,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-239.808,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -48.81 kcal/mol
S298: 114.27 cal/mol/K

Coordinates (Angstoms):
Cl -0.27101 -0.08131 -2.73777
C -0.26808 0.91456 -1.26652
C -0.04429 0.15521 0.05958
Cl -0.24601 1.42180 1.29538
C -1.14488 -0.93332 0.21717
Cl -2.76800 -0.25232 -0.00529
Cl -1.11180 -1.82503 1.73560
C 1.42921 -0.43752 0.19350
Cl 2.61467 0.69479 -0.49548
Cl 1.57319 -1.97895 -0.67415
Cl 1.92318 -0.71939 1.86772
H -1.23930 1.39219 -1.20955
H 0.49727 1.67219 -1.38387
H -1.01272 -1.66015 -0.57719

modes:
""",
    rank = 5,
)

entry(
    index = 31,
    label = "BrC(Br)C(Br)(C(Br)Br)C(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {8,S}
2  Br u0 p3 c0 {9,S}
3  Br u0 p3 c0 {9,S}
4  Br u0 p3 c0 {10,S}
5  Br u0 p3 c0 {10,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
9  C  u0 p0 c0 {2,S} {3,S} {8,S} {12,S}
10 C  u0 p0 c0 {4,S} {5,S} {8,S} {13,S}
11 C  u0 p0 c0 {6,S} {7,S} {8,S} {14,S}
12 H  u0 p0 c0 {9,S}
13 H  u0 p0 c0 {10,S}
14 H  u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.86065,0.133018,9.75946e-05,-2.93039e-06,6.7342e-09,12168.9,19.665], Tmin=(10,'K'), Tmax=(201.96,'K')),
            NASAPolynomial(coeffs=[12.2347,0.049258,-3.71525e-05,1.2742e-08,-1.62033e-12,11582.4,-15.7089], Tmin=(201.96,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (101.69,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 34.01 kcal/mol
S298: 133.40 cal/mol/K

Coordinates (Angstoms):
Br 0.76744 2.47548 -1.40804
C -0.39754 1.39415 -0.30055
Br -2.22891 1.82613 -0.70441
C -0.07044 -0.11862 -0.35192
Br -0.29161 -0.75724 -2.18853
C -0.93869 -0.99331 0.61283
Br -1.21185 -0.19543 2.36140
Br -2.64030 -1.64245 -0.03010
C 1.45749 -0.32806 -0.07431
Br 2.00477 -2.18372 -0.04964
Br 2.15699 0.55339 1.50599
H -0.23363 1.74859 0.71079
H -0.37740 -1.89791 0.81129
H 2.00368 0.11900 -0.89479

modes:
""",
    rank = 5,
)

entry(
    index = 32,
    label = "ClC(Cl)DC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {9,S}
2  Cl u0 p3 c0 {9,S}
3  Cl u0 p3 c0 {9,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {10,S}
6  Cl u0 p3 c0 {10,S}
7  Cl u0 p3 c0 {12,S}
8  Cl u0 p3 c0 {12,S}
9  C  u0 p0 c0 {1,S} {2,S} {3,S} {11,S}
10 C  u0 p0 c0 {4,S} {5,S} {6,S} {11,S}
11 C  u0 p0 c0 {9,S} {10,S} {12,D}
12 C  u0 p0 c0 {7,S} {8,S} {11,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.07651,0.0774845,0.000125498,-7.77742e-07,8.35975e-10,-4164.16,16.5557], Tmin=(10,'K'), Tmax=(390.972,'K')),
            NASAPolynomial(coeffs=[14.6078,0.0390551,-3.22483e-05,1.16241e-08,-1.52085e-12,-5673.81,-36.0217], Tmin=(390.972,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-34.5921,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (274.378,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 0.32 kcal/mol
S298: 114.33 cal/mol/K

Coordinates (Angstoms):
Cl 1.91081 -2.01735 0.72390
C 0.39095 -1.47658 0.15599
Cl -0.61211 -2.80806 -0.22423
C 0.04149 -0.18170 0.02031
C 1.13554 0.89848 -0.15830
Cl 1.69969 1.48153 1.42271
Cl 0.59170 2.28011 -1.14120
Cl 2.54322 0.30996 -1.08844
C -1.44526 0.23952 0.03991
Cl -2.46967 -0.81551 1.05076
Cl -2.10908 0.25795 -1.60813
Cl -1.67727 1.83167 0.80671

modes:
""",
    rank = 5,
)

entry(
    index = 33,
    label = "ClOC(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {9,S}
2  Cl u0 p3 c0 {10,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {11,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {8,S}
8  O  u0 p2 c0 {7,S} {9,S}
9  C  u0 p0 c0 {1,S} {8,S} {10,S} {11,S}
10 C  u0 p0 c0 {2,S} {3,S} {9,S} {12,S}
11 C  u0 p0 c0 {4,S} {5,S} {6,S} {9,S}
12 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.9231,0.0962919,-8.29142e-05,-1.32324e-07,2.09549e-10,-22942.9,16.4439], Tmin=(10,'K'), Tmax=(434.502,'K')),
            NASAPolynomial(coeffs=[13.76,0.0387672,-3.01471e-05,1.0451e-08,-1.33086e-12,-24283.4,-31.3933], Tmin=(434.502,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-190.794,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -37.14 kcal/mol
S298: 113.98 cal/mol/K

Coordinates (Angstoms):
Cl 1.91639 -1.98123 0.50465
O 0.58894 -1.09946 1.00614
C -0.19958 -0.49546 0.04326
Cl -0.79597 -1.64314 -1.18436
C -1.47406 -0.04130 0.83359
Cl -2.25271 -1.42252 1.61073
Cl -1.17435 1.20783 2.04151
C 0.54821 0.70025 -0.71823
Cl 1.55330 0.12654 -2.05695
Cl -0.65365 1.81516 -1.39935
Cl 1.60362 1.57273 0.39243
H -2.18051 0.36448 0.11967

modes:
""",
    rank = 5,
)

entry(
    index = 34,
    label = "BrCC(Br)(C(Br)Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {8,S}
2  Br u0 p3 c0 {9,S}
3  Br u0 p3 c0 {10,S}
4  Br u0 p3 c0 {10,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
9  C  u0 p0 c0 {2,S} {8,S} {12,S} {13,S}
10 C  u0 p0 c0 {3,S} {4,S} {8,S} {14,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
12 H  u0 p0 c0 {9,S}
13 H  u0 p0 c0 {9,S}
14 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.7726,0.136443,-5.50707e-05,-1.53229e-06,3.40514e-09,15061.4,19.6729], Tmin=(10,'K'), Tmax=(230.567,'K')),
            NASAPolynomial(coeffs=[12.7167,0.0488143,-3.72292e-05,1.28983e-08,-1.65346e-12,14377.2,-18.6044], Tmin=(230.567,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (125.323,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 39.80 kcal/mol
S298: 132.84 cal/mol/K

Coordinates (Angstoms):
Br 0.06370 2.79464 0.39819
C 1.17967 1.20945 0.42734
C 0.51299 -0.13737 0.07035
Br 2.04795 -1.35113 0.07249
C -0.09566 -0.04180 -1.35781
Br -0.85863 -1.64801 -2.09524
Br 1.14595 0.67693 -2.66288
C -0.52945 -0.63376 1.17203
Br 0.06582 -0.16118 2.96892
Br -2.28341 0.17702 0.91855
Br -0.81854 -2.55564 1.22786
H 1.96279 1.40059 -0.29523
H 1.61250 1.15760 1.41762
H -0.90531 0.67882 -1.32326

modes:
""",
    rank = 5,
)

entry(
    index = 35,
    label = "ClC(Cl)C(Cl)(C(Cl)Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {9,S}
2  Cl u0 p3 c0 {10,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {11,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {12,S}
7  Cl u0 p3 c0 {12,S}
8  Cl u0 p3 c0 {12,S}
9  C  u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
10 C  u0 p0 c0 {2,S} {3,S} {9,S} {13,S}
11 C  u0 p0 c0 {4,S} {5,S} {9,S} {14,S}
12 C  u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
13 H  u0 p0 c0 {10,S}
14 H  u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.82404,0.105834,-6.54116e-05,-2.34633e-07,3.2538e-10,-25570.3,16.7166], Tmin=(10,'K'), Tmax=(413.951,'K')),
            NASAPolynomial(coeffs=[14.1035,0.0472808,-3.60119e-05,1.23752e-08,-1.57e-12,-26936.3,-32.9714], Tmin=(413.951,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-212.618,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -41.56 kcal/mol
S298: 119.25 cal/mol/K

Coordinates (Angstoms):
Cl 1.65515 -1.65108 1.62836
C 1.41733 -0.38181 0.41047
Cl 2.15109 -0.89535 -1.11041
C -0.08153 0.10051 0.35943
Cl -0.29408 0.89232 1.95475
C -1.07542 -1.10766 0.38153
Cl -0.78546 -2.36262 -0.83002
Cl -2.78527 -0.66780 0.37034
C -0.30860 1.22601 -0.74555
Cl -1.70412 2.26021 -0.40156
Cl 1.10604 2.31097 -0.79701
Cl -0.55393 0.53596 -2.35017
H 2.00186 0.46501 0.74769
H -0.90525 -1.59120 1.33636

modes:
""",
    rank = 5,
)

entry(
    index = 36,
    label = "CC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {8,S}
2  Cl u0 p3 c0 {8,S}
3  Cl u0 p3 c0 {9,S}
4  Cl u0 p3 c0 {9,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
9  C  u0 p0 c0 {3,S} {4,S} {8,S} {11,S}
10 C  u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
12 H  u0 p0 c0 {10,S}
13 H  u0 p0 c0 {10,S}
14 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.20209,0.0662931,0.000220254,-1.03508e-06,1.09544e-09,-25387.1,15.9053], Tmin=(10,'K'), Tmax=(372.94,'K')),
            NASAPolynomial(coeffs=[12.5273,0.048183,-3.6348e-05,1.25262e-08,-1.59948e-12,-26652.2,-27.5225], Tmin=(372.94,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-211.023,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -41.87 kcal/mol
S298: 112.70 cal/mol/K

Coordinates (Angstoms):
C -1.66265 -0.46818 0.22888
C -0.70270 0.09675 -0.80383
Cl -0.42178 -1.15953 -2.03508
Cl -1.54059 1.43664 -1.64664
C 0.66895 0.68180 -0.23244
Cl 1.66497 1.19470 -1.60102
Cl 0.27198 2.10385 0.75883
C 1.57514 -0.25549 0.69531
Cl 2.04947 -1.74927 -0.10978
Cl 0.75990 -0.67716 2.21327
Cl 3.05618 0.61703 1.13317
H -1.83853 0.25195 1.02593
H -1.27601 -1.39399 0.64664
H -2.60432 -0.67909 -0.27324

modes:
""",
    rank = 5,
)

entry(
    index = 37,
    label = "BrC(DC(Br)C(Br)(Br)Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {9,S}
2  Br u0 p3 c0 {9,S}
3  Br u0 p3 c0 {9,S}
4  Br u0 p3 c0 {10,S}
5  Br u0 p3 c0 {10,S}
6  Br u0 p3 c0 {10,S}
7  Br u0 p3 c0 {11,S}
8  Br u0 p3 c0 {12,S}
9  C  u0 p0 c0 {1,S} {2,S} {3,S} {12,S}
10 C  u0 p0 c0 {4,S} {5,S} {6,S} {11,S}
11 C  u0 p0 c0 {7,S} {10,S} {12,D}
12 C  u0 p0 c0 {8,S} {9,S} {11,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.35915,0.173558,-0.000334401,-3.47273e-07,1.34144e-09,42592.3,21.646], Tmin=(10,'K'), Tmax=(271.858,'K')),
            NASAPolynomial(coeffs=[17.1565,0.0372499,-3.15168e-05,1.15434e-08,-1.52916e-12,41486.9,-36.0025], Tmin=(271.858,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (354.198,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 95.38 kcal/mol
S298: 142.16 cal/mol/K

Coordinates (Angstoms):
Br 0.35868 2.10073 -0.84662
C 0.54406 0.38493 -0.10015
C -0.54412 -0.38473 0.10061
Br -0.35960 -2.09670 0.85604
C -1.99841 0.01578 -0.23786
Br -2.18649 0.33633 -2.15333
Br -3.34483 -1.32851 0.16241
Br -2.52876 1.57369 0.80972
C 1.99855 -0.01652 0.23626
Br 2.19011 -0.32607 2.15317
Br 2.52428 -1.58128 -0.80345
Br 3.34654 1.32236 -0.17678

modes:
""",
    rank = 5,
)

entry(
    index = 38,
    label = "BrOC(Br)(Br)C(Br)(Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {10,S}
2  Br u0 p3 c0 {10,S}
3  Br u0 p3 c0 {11,S}
4  Br u0 p3 c0 {11,S}
5  Br u0 p3 c0 {12,S}
6  Br u0 p3 c0 {12,S}
7  Br u0 p3 c0 {12,S}
8  Br u0 p3 c0 {9,S}
9  O  u0 p2 c0 {8,S} {11,S}
10 C  u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
11 C  u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
12 C  u0 p0 c0 {5,S} {6,S} {7,S} {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.29577,0.178354,-0.000368775,-1.75755e-07,1.03881e-09,25047.4,21.0331], Tmin=(10,'K'), Tmax=(281.822,'K')),
            NASAPolynomial(coeffs=[17.7912,0.0366908,-3.13626e-05,1.15426e-08,-1.53291e-12,23863.2,-39.6131], Tmin=(281.822,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (208.329,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 60.69 kcal/mol
S298: 141.86 cal/mol/K

Coordinates (Angstoms):
Br -2.65288 -2.24202 0.23574
O -1.14013 -1.30097 -0.09608
C -1.17461 0.05971 -0.06768
Br -1.81371 0.73080 1.65648
Br -2.45924 0.77040 -1.38475
C 0.31671 0.51171 -0.45252
Br 0.37865 2.44728 -0.42555
Br 0.61907 -0.10165 -2.27987
C 1.53333 -0.04430 0.42224
Br 1.66422 -1.98158 0.42864
Br 3.21971 0.61657 -0.30950
Br 1.50887 0.53406 2.27283

modes:
""",
    rank = 5,
)

entry(
    index = 39,
    label = "BrOC(Br)(Br)C(Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {9,S}
2  Br u0 p3 c0 {10,S}
3  Br u0 p3 c0 {10,S}
4  Br u0 p3 c0 {11,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {8,S}
8  O  u0 p2 c0 {7,S} {10,S}
9  C  u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
10 C  u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
11 C  u0 p0 c0 {4,S} {5,S} {6,S} {9,S}
12 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.62155,0.149207,-0.00022567,-6.80601e-07,1.8715e-09,14518.6,20.5153], Tmin=(10,'K'), Tmax=(252.814,'K')),
            NASAPolynomial(coeffs=[14.3906,0.0398164,-3.2403e-05,1.16286e-08,-1.52216e-12,13678.1,-24.9349], Tmin=(252.814,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (120.768,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 38.69 kcal/mol
S298: 134.29 cal/mol/K

Coordinates (Angstoms):
Br 3.06647 1.43229 0.67165
O 1.35112 1.04099 0.22705
C 1.07805 -0.14542 -0.38656
Br 2.03092 -0.28442 -2.10787
Br 1.63750 -1.66042 0.71320
C -0.45662 -0.10177 -0.73914
Br -1.01319 -1.85392 -1.33836
C -1.45601 0.51442 0.28832
Br -1.17474 2.43629 0.45691
Br -1.37450 -0.29902 2.03345
Br -3.27193 0.34381 -0.39775
H -0.52823 0.53375 -1.62023

modes:
""",
    rank = 5,
)

entry(
    index = 40,
    label = "ClCDC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {8,S}
2  Cl u0 p3 c0 {8,S}
3  Cl u0 p3 c0 {8,S}
4  Cl u0 p3 c0 {9,S}
5  Cl u0 p3 c0 {9,S}
6  Cl u0 p3 c0 {9,S}
7  Cl u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {2,S} {3,S} {10,S}
9  C  u0 p0 c0 {4,S} {5,S} {6,S} {10,S}
10 C  u0 p0 c0 {8,S} {9,S} {11,D}
11 C  u0 p0 c0 {7,S} {10,D} {12,S}
12 H  u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.02872,0.0854297,9.87582e-06,-4.02979e-07,4.67467e-10,-9594.42,16.6772], Tmin=(10,'K'), Tmax=(405.452,'K')),
            NASAPolynomial(coeffs=[13.4557,0.0395302,-3.10737e-05,1.08929e-08,-1.40039e-12,-10908.2,-29.9885], Tmin=(405.452,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-79.7714,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -10.70 kcal/mol
S298: 113.66 cal/mol/K

Coordinates (Angstoms):
Cl 0.95252 2.22404 -1.59166
C -0.22396 1.19623 -0.91608
C -0.04468 0.14805 -0.11328
C 1.36432 -0.29409 0.32914
Cl 2.32255 -0.71791 -1.11308
Cl 2.15296 1.04250 1.20522
Cl 1.45234 -1.69988 1.40346
C -1.28694 -0.61046 0.35705
Cl -1.23469 -2.29924 -0.19740
Cl -2.81091 0.06086 -0.27899
Cl -1.42556 -0.53410 2.12862
H -1.21795 1.48400 -1.21298

modes:
""",
    rank = 5,
)

entry(
    index = 41,
    label = "OC(Br)(Br)C(Br)(Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {9,S}
2  Br u0 p3 c0 {9,S}
3  Br u0 p3 c0 {10,S}
4  Br u0 p3 c0 {10,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {11,S}
8  O  u0 p2 c0 {10,S} {12,S}
9  C  u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
10 C  u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
12 H  u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.51978,0.146183,-0.000251043,-1.25101e-07,5.53221e-10,3574.27,19.7688], Tmin=(10,'K'), Tmax=(326.796,'K')),
            NASAPolynomial(coeffs=[16.7716,0.0347053,-2.83679e-05,1.02286e-08,-1.34299e-12,2306.56,-38.1927], Tmin=(326.796,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (29.7911,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 17.12 kcal/mol
S298: 132.20 cal/mol/K

Coordinates (Angstoms):
O 1.54782 -0.06449 -0.98969
C 1.14548 0.25992 0.25684
Br 2.44828 -0.44296 1.57657
Br 1.23484 2.21045 0.50024
C -0.29004 -0.38456 0.49980
Br -0.03357 -2.31509 0.37350
Br -0.85849 0.05635 2.29780
C -1.47111 -0.01231 -0.50782
Br -1.99893 1.85365 -0.45404
Br -1.06851 -0.44408 -2.35585
Br -3.07632 -1.02187 -0.03868
H 2.42056 0.30499 -1.15868

modes:
""",
    rank = 5,
)

entry(
    index = 42,
    label = "BrC(Br)(Br)C(Br)(Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {9,S}
2  Br u0 p3 c0 {9,S}
3  Br u0 p3 c0 {10,S}
4  Br u0 p3 c0 {10,S}
5  Br u0 p3 c0 {10,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {11,S}
8  Br u0 p3 c0 {11,S}
9  C  u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
10 C  u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
11 C  u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.40752,0.163492,-0.000332855,-1.2525e-07,8.09968e-10,33406.2,19.5645], Tmin=(10,'K'), Tmax=(295.895,'K')),
            NASAPolynomial(coeffs=[17.5647,0.0308358,-2.6594e-05,9.84705e-09,-1.31313e-12,32193,-40.4463], Tmin=(295.895,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (277.829,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 76.67 kcal/mol
S298: 134.56 cal/mol/K

Coordinates (Angstoms):
Br -1.87866 0.84712 1.71073
C -1.23969 0.68387 -0.11375
Br -0.74402 2.46372 -0.70077
Br -2.81082 0.19714 -1.17313
C -0.09531 -0.42043 -0.31869
Br -0.85992 -2.12196 0.24591
Br 0.26667 -0.50187 -2.23230
C 1.32852 -0.29275 0.40906
Br 2.35590 1.26975 -0.10588
Br 2.44247 -1.82909 -0.06693
Br 1.23487 -0.29550 2.34575

modes:
""",
    rank = 5,
)

entry(
    index = 43,
    label = "BrOC(C(Br)(Br)Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {10,S}
2  Br u0 p3 c0 {10,S}
3  Br u0 p3 c0 {10,S}
4  Br u0 p3 c0 {11,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {8,S}
8  O  u0 p2 c0 {7,S} {9,S}
9  C  u0 p0 c0 {8,S} {10,S} {11,S} {12,S}
10 C  u0 p0 c0 {1,S} {2,S} {3,S} {9,S}
11 C  u0 p0 c0 {4,S} {5,S} {6,S} {9,S}
12 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.62643,0.149127,-0.000212507,-7.81067e-07,2.0653e-09,18095.7,20.2541], Tmin=(10,'K'), Tmax=(249.96,'K')),
            NASAPolynomial(coeffs=[14.4538,0.0394535,-3.20131e-05,1.14735e-08,-1.50094e-12,17255.7,-25.3821], Tmin=(249.96,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (150.51,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 45.81 kcal/mol
S298: 133.93 cal/mol/K

Coordinates (Angstoms):
Br -0.75802 -2.97204 -0.44827
O -0.34686 -1.24643 -0.82114
C -0.03139 -0.42993 0.27936
C -1.16238 0.64646 0.48631
Br -1.06947 2.17365 -0.68715
Br -2.88365 -0.21264 0.20062
Br -1.16415 1.23936 2.33914
C 1.45857 0.01432 0.04317
Br 2.07086 1.46732 1.15577
Br 1.80788 0.46016 -1.80836
Br 2.54302 -1.54860 0.48543
H -0.02966 -1.00172 1.20870

modes:
""",
    rank = 5,
)

entry(
    index = 44,
    label = "ClOC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {10,S}
2  Cl u0 p3 c0 {10,S}
3  Cl u0 p3 c0 {11,S}
4  Cl u0 p3 c0 {11,S}
5  Cl u0 p3 c0 {12,S}
6  Cl u0 p3 c0 {12,S}
7  Cl u0 p3 c0 {12,S}
8  Cl u0 p3 c0 {9,S}
9  O  u0 p2 c0 {8,S} {11,S}
10 C  u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
11 C  u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
12 C  u0 p0 c0 {5,S} {6,S} {7,S} {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.84124,0.101939,-1.965e-05,-4.07696e-07,4.98408e-10,-21832.7,17.4775], Tmin=(10,'K'), Tmax=(409.403,'K')),
            NASAPolynomial(coeffs=[16.2143,0.0382474,-3.16535e-05,1.13941e-08,-1.48732e-12,-23488.9,-41.9511], Tmin=(409.403,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-181.532,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -34.19 kcal/mol
S298: 120.34 cal/mol/K

Coordinates (Angstoms):
Cl 2.91367 0.58344 -1.51980
O 1.33197 0.23488 -1.11538
C 1.13038 -0.27464 0.14642
Cl 2.01475 -1.80760 0.37172
Cl 1.70856 0.83757 1.39925
C -0.44290 -0.56504 0.22925
Cl -0.77450 -1.22872 1.82922
Cl -0.79974 -1.78115 -1.00700
C -1.44795 0.65687 -0.01532
Cl -3.10973 0.04244 0.10204
Cl -1.25199 1.37338 -1.61574
Cl -1.27252 1.92857 1.19533

modes:
""",
    rank = 5,
)

entry(
    index = 45,
    label = "ClC(Cl)(Cl)CC(Cl)(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {10,S}
2  Cl u0 p3 c0 {10,S}
3  Cl u0 p3 c0 {11,S}
4  Cl u0 p3 c0 {11,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {12,S}
7  Cl u0 p3 c0 {12,S}
8  Cl u0 p3 c0 {12,S}
9  C  u0 p0 c0 {10,S} {11,S} {13,S} {14,S}
10 C  u0 p0 c0 {1,S} {2,S} {9,S} {12,S}
11 C  u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
12 C  u0 p0 c0 {6,S} {7,S} {8,S} {10,S}
13 H  u0 p0 c0 {9,S}
14 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.82827,0.105342,-4.57723e-05,-3.11441e-07,4.08733e-10,-30004,17.4461], Tmin=(10,'K'), Tmax=(404.37,'K')),
            NASAPolynomial(coeffs=[14.322,0.0472019,-3.61808e-05,1.24979e-08,-1.59202e-12,-31387.7,-33.2138], Tmin=(404.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-249.468,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -50.30 kcal/mol
S298: 121.17 cal/mol/K

Coordinates (Angstoms):
Cl 2.36354 1.73180 -0.39786
C 1.98495 0.00507 -0.25146
Cl 2.81170 -0.83427 -1.59354
Cl 2.63243 -0.61219 1.27025
C 0.48686 -0.27214 -0.44547
C -0.53957 -0.00546 0.67742
Cl -0.18048 1.42237 1.65746
Cl -0.61623 -1.41909 1.75695
C -1.97365 0.19439 0.03565
Cl -3.20715 0.39043 1.27610
Cl -1.97463 1.63564 -0.99680
Cl -2.38535 -1.21061 -0.96505
H 0.20129 0.30029 -1.32725
H 0.39629 -1.32623 -0.69639

modes:
""",
    rank = 5,
)

entry(
    index = 46,
    label = "ClCC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {9,S}
2  Cl u0 p3 c0 {10,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  C  u0 p0 c0 {9,S} {10,S} {11,S} {12,S}
9  C  u0 p0 c0 {1,S} {8,S} {13,S} {14,S}
10 C  u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
12 H  u0 p0 c0 {8,S}
13 H  u0 p0 c0 {9,S}
14 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.76244,0.10414,-0.000155852,1.22339e-07,-3.85551e-11,-27207.8,17.3635], Tmin=(10,'K'), Tmax=(761.181,'K')),
            NASAPolynomial(coeffs=[15.406,0.0376987,-2.49202e-05,7.66564e-09,-8.91947e-13,-29132.6,-40.184], Tmin=(761.181,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-226.37,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -45.53 kcal/mol
S298: 115.69 cal/mol/K

Coordinates (Angstoms):
Cl -0.85843 0.23840 2.71377
C -0.05422 -0.55547 1.34130
C -0.08693 0.30494 0.06092
C 1.36936 0.41202 -0.49860
Cl 2.18278 -1.16730 -0.60721
Cl 2.27722 1.40608 0.67635
Cl 1.50586 1.19820 -2.06955
C -1.22861 -0.11407 -0.92250
Cl -2.69643 -0.50464 0.00698
Cl -0.82551 -1.52906 -1.90413
Cl -1.67541 1.23459 -1.98779
H -0.53136 -1.51906 1.18415
H 0.96648 -0.72981 1.66086
H -0.34479 1.32518 0.34543

modes:
""",
    rank = 5,
)

entry(
    index = 47,
    label = "BrC(Br)CC(Br)(Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {9,S}
2  Br u0 p3 c0 {9,S}
3  Br u0 p3 c0 {10,S}
4  Br u0 p3 c0 {10,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {11,S}
8  C  u0 p0 c0 {9,S} {10,S} {12,S} {13,S}
9  C  u0 p0 c0 {1,S} {2,S} {8,S} {11,S}
10 C  u0 p0 c0 {3,S} {4,S} {8,S} {14,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
12 H  u0 p0 c0 {8,S}
13 H  u0 p0 c0 {8,S}
14 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.79332,0.137971,3.27984e-05,-2.40659e-06,5.42255e-09,11750.2,21.4902], Tmin=(10,'K'), Tmax=(213.072,'K')),
            NASAPolynomial(coeffs=[12.9338,0.0476652,-3.58844e-05,1.23176e-08,-1.56887e-12,11090.9,-17.0834], Tmin=(213.072,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (97.9636,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 33.32 kcal/mol
S298: 137.75 cal/mol/K

Coordinates (Angstoms):
Br -2.61403 1.88525 1.07638
C -1.93780 0.21000 0.38036
Br -3.18895 -0.53957 -0.89245
C -0.54143 0.37361 -0.23394
C 0.56628 -0.39803 0.49247
Br 0.12665 -2.29914 0.47945
Br 0.64091 0.18062 2.35305
C 1.96926 -0.18338 -0.17711
Br 2.44515 1.70292 -0.16741
Br 1.93525 -0.76557 -2.03285
Br 3.37148 -1.15737 0.73099
H -1.94094 -0.47323 1.22194
H -0.27119 1.42772 -0.24247
H -0.56064 0.03617 -1.26803

modes:
""",
    rank = 5,
)

entry(
    index = 48,
    label = "ClC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {11,S}
2  Cl u0 p3 c0 {11,S}
3  Cl u0 p3 c0 {12,S}
4  Cl u0 p3 c0 {12,S}
5  Cl u0 p3 c0 {13,S}
6  Cl u0 p3 c0 {13,S}
7  Cl u0 p3 c0 {13,S}
8  Cl u0 p3 c0 {14,S}
9  Cl u0 p3 c0 {14,S}
10 Cl u0 p3 c0 {14,S}
11 C  u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
12 C  u0 p0 c0 {3,S} {4,S} {11,S} {14,S}
13 C  u0 p0 c0 {5,S} {6,S} {7,S} {11,S}
14 C  u0 p0 c0 {8,S} {9,S} {10,S} {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.72743,0.10796,0.000154327,-1.09223e-06,1.23087e-09,-18925.4,16.5564], Tmin=(10,'K'), Tmax=(380.02,'K')),
            NASAPolynomial(coeffs=[19.1329,0.0461033,-3.89555e-05,1.42462e-08,-1.88219e-12,-20972.5,-57.2467], Tmin=(380.02,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-157.291,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -26.89 kcal/mol
S298: 127.00 cal/mol/K

Coordinates (Angstoms):
Cl -3.36746 -0.61060 -0.39119
C -1.60166 -0.76125 -0.53861
Cl -1.21700 -0.40783 -2.22471
Cl -1.18778 -2.43466 -0.17341
C -0.90448 0.27588 0.46752
Cl -1.41189 1.88348 -0.07491
Cl -1.63398 0.00469 2.06541
C 0.71574 0.25550 0.73105
Cl 1.15674 -1.17015 1.68481
Cl 1.03774 1.68497 1.73731
C 1.76287 0.30706 -0.48331
Cl 1.46404 1.66145 -1.57040
Cl 1.78529 -1.19788 -1.40553
Cl 3.40183 0.50935 0.17597

modes:
""",
    rank = 5,
)

entry(
    index = 49,
    label = "ClC(Cl)DC(Cl)C(Cl)(Cl)C(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {8,S}
2  Cl u0 p3 c0 {8,S}
3  Cl u0 p3 c0 {9,S}
4  Cl u0 p3 c0 {9,S}
5  Cl u0 p3 c0 {10,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
9  C  u0 p0 c0 {3,S} {4,S} {8,S} {12,S}
10 C  u0 p0 c0 {5,S} {8,S} {11,D}
11 C  u0 p0 c0 {6,S} {7,S} {10,D}
12 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.80997,0.105374,-0.000183,1.63203e-07,-5.78095e-11,-14927.6,17.1467], Tmin=(10,'K'), Tmax=(683.701,'K')),
            NASAPolynomial(coeffs=[15.2396,0.0326545,-2.34575e-05,7.63571e-09,-9.25383e-13,-16627.2,-38.0931], Tmin=(683.701,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-124.23,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -21.32 kcal/mol
S298: 114.78 cal/mol/K

Coordinates (Angstoms):
Cl 1.34211 1.98165 -0.70812
C 1.75688 0.36743 -0.30192
Cl 3.37860 -0.00595 -0.69260
C 0.92660 -0.52095 0.26011
Cl 1.53591 -2.08890 0.58267
C -0.54698 -0.24032 0.62518
Cl -1.30940 -1.61844 1.42537
Cl -0.61859 1.13569 1.76376
C -1.36218 0.12315 -0.64672
Cl -1.20207 -1.15186 -1.86156
Cl -3.05495 0.45879 -0.30573
H -0.94779 1.02570 -1.07967

modes:
""",
    rank = 5,
)

entry(
    index = 50,
    label = "ClOC(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {10,S}
2  Cl u0 p3 c0 {10,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {11,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {8,S}
8  O  u0 p2 c0 {7,S} {9,S}
9  C  u0 p0 c0 {8,S} {10,S} {11,S} {12,S}
10 C  u0 p0 c0 {1,S} {2,S} {3,S} {9,S}
11 C  u0 p0 c0 {4,S} {5,S} {6,S} {9,S}
12 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.73031,0.107914,-0.000184219,1.5794e-07,-5.33235e-11,-21741.4,17.2963], Tmin=(10,'K'), Tmax=(719.762,'K')),
            NASAPolynomial(coeffs=[16.8244,0.0295881,-2.09857e-05,6.74756e-09,-8.08901e-13,-23770.3,-46.0647], Tmin=(719.762,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-180.919,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -34.73 kcal/mol
S298: 115.49 cal/mol/K

Coordinates (Angstoms):
Cl -0.78783 1.94398 -1.98193
O -0.64051 1.37511 -0.41806
C -0.04647 0.10193 -0.31614
C 1.38005 0.23499 0.32590
Cl 2.19096 1.61560 -0.43859
Cl 1.36068 0.48888 2.06739
Cl 2.34262 -1.20552 -0.06066
C -1.13136 -0.79742 0.36914
Cl -2.37567 -1.07653 -0.87649
Cl -1.90081 0.01255 1.73603
Cl -0.51984 -2.36354 0.89510
H 0.12818 -0.33003 -1.30169

modes:
""",
    rank = 5,
)

entry(
    index = 51,
    label = "ClC(Cl)(Cl)C(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {11,S}
2  Cl u0 p3 c0 {11,S}
3  Cl u0 p3 c0 {11,S}
4  Cl u0 p3 c0 {12,S}
5  Cl u0 p3 c0 {12,S}
6  Cl u0 p3 c0 {12,S}
7  Cl u0 p3 c0 {13,S}
8  Cl u0 p3 c0 {13,S}
9  Cl u0 p3 c0 {13,S}
10 C  u0 p0 c0 {11,S} {12,S} {13,S} {14,S}
11 C  u0 p0 c0 {1,S} {2,S} {3,S} {10,S}
12 C  u0 p0 c0 {4,S} {5,S} {6,S} {10,S}
13 C  u0 p0 c0 {7,S} {8,S} {9,S} {10,S}
14 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.79679,0.10467,6.60537e-05,-7.27056e-07,8.37747e-10,-18921.4,15.9597], Tmin=(10,'K'), Tmax=(387.838,'K')),
            NASAPolynomial(coeffs=[16.5755,0.0470642,-3.79699e-05,1.35345e-08,-1.76003e-12,-20625.7,-45.6573], Tmin=(387.838,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-157.286,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -27.62 kcal/mol
S298: 121.73 cal/mol/K

Coordinates (Angstoms):
Cl -0.71608 -1.37097 2.08476
C -1.04064 -1.08541 0.36906
Cl -2.74774 -0.60964 0.25807
Cl -0.95968 -2.62446 -0.53234
C -0.01196 -0.07275 -0.30279
C 1.51272 -0.32352 0.08130
Cl 1.94010 -2.01719 0.39864
Cl 2.02920 0.59651 1.50150
Cl 2.51204 0.11875 -1.33057
C -0.46353 1.45306 -0.26535
Cl -1.11148 1.94796 1.30503
Cl 0.80681 2.62510 -0.67149
Cl -1.69517 1.69042 -1.53593
H -0.05460 -0.32785 -1.35989

modes:
""",
    rank = 5,
)

entry(
    index = 52,
    label = "ClC(Cl)C(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {10,S}
2  Cl u0 p3 c0 {10,S}
3  Cl u0 p3 c0 {11,S}
4  Cl u0 p3 c0 {11,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {12,S}
7  Cl u0 p3 c0 {12,S}
8  Cl u0 p3 c0 {12,S}
9  C  u0 p0 c0 {10,S} {11,S} {12,S} {13,S}
10 C  u0 p0 c0 {1,S} {2,S} {9,S} {14,S}
11 C  u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
12 C  u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
13 H  u0 p0 c0 {9,S}
14 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.57384,0.11982,-0.000196666,1.64487e-07,-5.44573e-11,-25954.5,17.4625], Tmin=(10,'K'), Tmax=(731.857,'K')),
            NASAPolynomial(coeffs=[17.9338,0.0358698,-2.46023e-05,7.74955e-09,-9.16413e-13,-28202.8,-51.8455], Tmin=(731.857,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-215.974,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -42.33 kcal/mol
S298: 120.11 cal/mol/K

Coordinates (Angstoms):
Cl 2.40826 1.02660 -1.73293
C 1.74676 0.39056 -0.21230
Cl 2.12388 1.46865 1.13644
C 0.25485 -0.03008 -0.38050
C -0.83607 1.05891 -0.10404
Cl -2.29265 0.69770 -1.06932
Cl -0.29188 2.65072 -0.66965
Cl -1.29409 1.18799 1.59550
C 0.07635 -1.44091 0.29246
Cl 1.03161 -2.58542 -0.70300
Cl 0.70936 -1.51019 1.94638
Cl -1.57738 -2.04651 0.31982
H 2.32437 -0.50545 -0.02141
H 0.14123 -0.23364 -1.44481

modes:
""",
    rank = 5,
)

entry(
    index = 53,
    label = "BrCC(C(Br)(Br)Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {9,S}
2  Br u0 p3 c0 {10,S}
3  Br u0 p3 c0 {10,S}
4  Br u0 p3 c0 {10,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {11,S}
8  C  u0 p0 c0 {9,S} {10,S} {11,S} {12,S}
9  C  u0 p0 c0 {1,S} {8,S} {13,S} {14,S}
10 C  u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
12 H  u0 p0 c0 {8,S}
13 H  u0 p0 c0 {9,S}
14 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.31372,0.16816,-0.000525664,8.8227e-07,-5.77744e-10,17614.6,20.7027], Tmin=(10,'K'), Tmax=(389.341,'K')),
            NASAPolynomial(coeffs=[14.0273,0.0438815,-3.16991e-05,1.04939e-08,-1.29678e-12,16732.3,-24.3762], Tmin=(389.341,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (146.438,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 44.91 kcal/mol
S298: 133.74 cal/mol/K

Coordinates (Angstoms):
Br 2.81285 -0.91666 0.54505
C 1.19853 -0.65688 -0.49196
C 0.05968 0.02201 0.30132
C -1.20718 -0.90355 0.21347
Br -2.84718 -0.19119 0.94378
Br -0.76904 -2.49217 1.26888
Br -1.60453 -1.50818 -1.59928
C -0.08188 1.55409 -0.01107
Br -1.10399 1.95823 -1.60344
Br -0.85009 2.50426 1.50606
Br 1.67891 2.36485 -0.25218
H 0.91654 -1.65408 -0.80436
H 1.46963 -0.08546 -1.37446
H 0.32776 0.00469 1.35819

modes:
""",
    rank = 5,
)

entry(
    index = 54,
    label = "BrC(Br)DC(C(Br)(Br)Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {9,S}
2  Br u0 p3 c0 {9,S}
3  Br u0 p3 c0 {9,S}
4  Br u0 p3 c0 {10,S}
5  Br u0 p3 c0 {10,S}
6  Br u0 p3 c0 {10,S}
7  Br u0 p3 c0 {12,S}
8  Br u0 p3 c0 {12,S}
9  C  u0 p0 c0 {1,S} {2,S} {3,S} {11,S}
10 C  u0 p0 c0 {4,S} {5,S} {6,S} {11,S}
11 C  u0 p0 c0 {9,S} {10,S} {12,D}
12 C  u0 p0 c0 {7,S} {8,S} {11,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.34537,0.174831,-0.000336695,-3.5164e-07,1.35043e-09,48615.7,21.2805], Tmin=(10,'K'), Tmax=(272.471,'K')),
            NASAPolynomial(coeffs=[17.3545,0.0369225,-3.1294e-05,1.14742e-08,-1.52112e-12,47491.8,-37.2299], Tmin=(272.471,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (404.279,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 107.41 kcal/mol
S298: 141.79 cal/mol/K

Coordinates (Angstoms):
Br -2.33744 -1.80930 0.65149
C -0.61581 -1.09744 0.86854
Br 0.25346 -1.95148 2.29455
C -0.07485 -0.12284 0.10351
C -0.98178 0.95922 -0.52466
Br -1.59997 0.41561 -2.28725
Br -2.54692 1.40821 0.57283
Br -0.12693 2.71646 -0.63566
C 1.45290 -0.10436 -0.14288
Br 1.97093 0.60814 -1.88979
Br 2.22937 -1.90599 -0.26492
Br 2.37703 0.88377 1.25423

modes:
""",
    rank = 5,
)

entry(
    index = 55,
    label = "ClC(Cl)CC(Cl)(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {9,S}
2  Cl u0 p3 c0 {9,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  C  u0 p0 c0 {9,S} {10,S} {12,S} {13,S}
9  C  u0 p0 c0 {1,S} {2,S} {8,S} {11,S}
10 C  u0 p0 c0 {3,S} {4,S} {8,S} {14,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
12 H  u0 p0 c0 {8,S}
13 H  u0 p0 c0 {8,S}
14 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.79854,0.106183,-0.00016807,1.4265e-07,-4.89771e-11,-31629.5,17.637], Tmin=(10,'K'), Tmax=(698.091,'K')),
            NASAPolynomial(coeffs=[14.1813,0.0409611,-2.79247e-05,8.8126e-09,-1.04708e-12,-33218.7,-33.1869], Tmin=(698.091,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-263.101,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -54.26 kcal/mol
S298: 117.09 cal/mol/K

Coordinates (Angstoms):
Cl 2.94423 -0.55776 -0.87600
C 1.83477 0.66710 -0.23063
Cl 2.69727 1.69785 0.93149
C 0.60676 0.03892 0.43225
C -0.64390 0.00995 -0.45131
Cl -1.12357 1.68478 -0.82773
Cl -0.32515 -0.83501 -1.97831
C -1.84645 -0.70401 0.27758
Cl -1.41338 -2.38236 0.64565
Cl -2.20714 0.12652 1.80142
Cl -3.29365 -0.69871 -0.72759
H 1.56669 1.30936 -1.06373
H 0.84668 -0.97469 0.74860
H 0.35684 0.61805 1.31830

modes:
""",
    rank = 5,
)

entry(
    index = 56,
    label = "ClC(Cl)C(Cl)(Cl)OC(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {9,S}
2  Cl u0 p3 c0 {9,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  O  u0 p2 c0 {9,S} {11,S}
9  C  u0 p0 c0 {1,S} {2,S} {8,S} {10,S}
10 C  u0 p0 c0 {3,S} {4,S} {9,S} {12,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
12 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.76368,0.105569,-0.000175024,1.45707e-07,-4.78447e-11,-42871.9,17.2936], Tmin=(10,'K'), Tmax=(738.369,'K')),
            NASAPolynomial(coeffs=[16.7426,0.0298409,-2.11817e-05,6.80436e-09,-8.14549e-13,-44936.2,-45.9065], Tmin=(738.369,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-356.603,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -76.79 kcal/mol
S298: 115.09 cal/mol/K

Coordinates (Angstoms):
Cl -1.30249 -1.37138 -1.79741
C -1.66351 -0.05626 -0.68218
Cl -3.27351 -0.23287 -0.00407
C -0.56907 0.05403 0.41675
Cl -0.53468 -1.38742 1.43005
Cl -0.94585 1.48006 1.42107
O 0.58768 0.29778 -0.31326
C 1.89413 0.07103 0.06022
Cl 2.84649 1.10452 -1.01257
Cl 2.25869 0.49481 1.73864
Cl 2.35428 -1.61978 -0.22975
H -1.63581 0.87054 -1.24907

modes:
""",
    rank = 5,
)

entry(
    index = 57,
    label = "ClC(DCC(Cl)(Cl)Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {8,S}
2  Cl u0 p3 c0 {8,S}
3  Cl u0 p3 c0 {8,S}
4  Cl u0 p3 c0 {9,S}
5  Cl u0 p3 c0 {9,S}
6  Cl u0 p3 c0 {9,S}
7  Cl u0 p3 c0 {10,S}
8  C  u0 p0 c0 {1,S} {2,S} {3,S} {11,S}
9  C  u0 p0 c0 {4,S} {5,S} {6,S} {10,S}
10 C  u0 p0 c0 {7,S} {9,S} {11,D}
11 C  u0 p0 c0 {8,S} {10,D} {12,S}
12 H  u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.74159,0.106227,-0.000178897,1.513e-07,-5.03934e-11,-14245.6,18.1678], Tmin=(10,'K'), Tmax=(729.335,'K')),
            NASAPolynomial(coeffs=[16.7783,0.0292435,-2.0567e-05,6.57435e-09,-7.84705e-13,-16293.1,-45.1209], Tmin=(729.335,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-118.598,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -19.90 kcal/mol
S298: 116.72 cal/mol/K

Coordinates (Angstoms):
Cl -0.06745 -1.78600 -1.20349
C -0.45997 -0.41284 -0.25829
C 0.44851 0.39948 0.26205
C 1.94845 0.30176 0.14075
Cl 2.66689 1.66003 1.03645
Cl 2.47008 0.42332 -1.55217
Cl 2.56210 -1.20740 0.84583
C -1.96109 -0.20799 -0.07634
Cl -2.34263 1.20989 0.91143
Cl -2.71489 0.01190 -1.66781
Cl -2.65756 -1.63347 0.71708
H 0.10756 1.24133 0.84450

modes:
""",
    rank = 5,
)

entry(
    index = 58,
    label = "ClC(C(Cl)C(Cl)(Cl)Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {9,S}
2  Cl u0 p3 c0 {10,S}
3  Cl u0 p3 c0 {11,S}
4  Cl u0 p3 c0 {11,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {12,S}
7  Cl u0 p3 c0 {12,S}
8  Cl u0 p3 c0 {12,S}
9  C  u0 p0 c0 {1,S} {10,S} {12,S} {13,S}
10 C  u0 p0 c0 {2,S} {9,S} {11,S} {14,S}
11 C  u0 p0 c0 {3,S} {4,S} {5,S} {10,S}
12 C  u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
13 H  u0 p0 c0 {9,S}
14 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.6361,0.1216,-0.000209959,1.88851e-07,-6.77974e-11,-31926.5,17.4801], Tmin=(10,'K'), Tmax=(673.383,'K')),
            NASAPolynomial(coeffs=[16.3462,0.0401599,-2.85474e-05,9.25007e-09,-1.11876e-12,-33773,-43.2415], Tmin=(673.383,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-265.578,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -54.16 kcal/mol
S298: 121.11 cal/mol/K

Coordinates (Angstoms):
Cl 1.25608 1.43741 1.18158
C 0.62313 -0.03093 0.43248
C -0.53228 0.22937 -0.56680
Cl -0.36074 1.73524 -1.47218
C -1.93987 0.14581 0.08676
Cl -3.18082 0.30876 -1.16293
Cl -2.18479 1.37905 1.32258
Cl -2.13140 -1.46227 0.82792
C 1.78140 -0.87220 -0.17298
Cl 1.12222 -2.41889 -0.76103
Cl 2.58727 -0.04975 -1.50787
Cl 2.96222 -1.24149 1.09103
H 0.23207 -0.64055 1.24503
H -0.52179 -0.57073 -1.30440

modes:
""",
    rank = 5,
)

entry(
    index = 59,
    label = "OC(Cl)(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {9,S}
2  Cl u0 p3 c0 {9,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  O  u0 p2 c0 {10,S} {12,S}
9  C  u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
10 C  u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
12 H  u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.12305,0.0726299,0.000166122,-8.96002e-07,9.50741e-10,-42295.4,16.4018], Tmin=(10,'K'), Tmax=(387.113,'K')),
            NASAPolynomial(coeffs=[14.6432,0.0385919,-3.13417e-05,1.12583e-08,-1.47331e-12,-43824.2,-36.4693], Tmin=(387.113,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-351.625,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -75.50 kcal/mol
S298: 113.64 cal/mol/K

Coordinates (Angstoms):
O 1.13862 0.58236 -1.32703
C 1.14286 0.39054 0.01003
Cl 2.06021 -1.08627 0.43531
Cl 2.00767 1.73848 0.83349
C -0.36508 0.36177 0.51762
Cl -0.35392 0.09846 2.26217
Cl -1.04708 1.95727 0.16091
C -1.34758 -0.71638 -0.13777
Cl -0.84849 -2.37633 0.19560
Cl -2.96471 -0.50290 0.56626
Cl -1.49151 -0.51249 -1.88423
H 2.04539 0.64123 -1.64493

modes:
""",
    rank = 5,
)

entry(
    index = 60,
    label = "ClOC(Cl)(Cl)C(Cl)(Cl)C(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {9,S}
2  Cl u0 p3 c0 {9,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {8,S}
8  O  u0 p2 c0 {7,S} {10,S}
9  C  u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
10 C  u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
11 C  u0 p0 c0 {5,S} {6,S} {9,S} {12,S}
12 H  u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.75067,0.106654,-0.000179248,1.51341e-07,-5.03752e-11,-26074.1,16.9913], Tmin=(10,'K'), Tmax=(729.047,'K')),
            NASAPolynomial(coeffs=[16.7509,0.0298397,-2.12058e-05,6.82222e-09,-8.17857e-13,-28115.5,-46.1276], Tmin=(729.047,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-216.94,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -43.37 kcal/mol
S298: 114.70 cal/mol/K

Coordinates (Angstoms):
Cl 2.48007 -2.15153 -0.69740
O 1.06247 -1.46428 -0.14539
C 1.10760 -0.11147 0.09529
Cl 1.52997 0.80357 -1.37731
Cl 2.30416 0.26358 1.35202
C -0.35316 0.28889 0.57075
Cl -0.80448 -0.73801 1.92883
Cl -0.30051 1.98519 1.08423
C -1.42031 0.21146 -0.56547
Cl -2.99458 0.77540 0.00348
Cl -1.60449 -1.38669 -1.28364
H -1.10717 0.88630 -1.35530

modes:
""",
    rank = 5,
)

entry(
    index = 61,
    label = "BrCC(Br)(Br)C(Br)(Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {9,S}
2  Br u0 p3 c0 {9,S}
3  Br u0 p3 c0 {10,S}
4  Br u0 p3 c0 {10,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {12,S}
7  Br u0 p3 c0 {12,S}
8  Br u0 p3 c0 {12,S}
9  C  u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
10 C  u0 p0 c0 {3,S} {4,S} {9,S} {12,S}
11 C  u0 p0 c0 {5,S} {9,S} {13,S} {14,S}
12 C  u0 p0 c0 {6,S} {7,S} {8,S} {10,S}
13 H  u0 p0 c0 {11,S}
14 H  u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.43732,0.166931,-0.000219864,-8.43303e-07,2.10124e-09,25890.5,20.218], Tmin=(10,'K'), Tmax=(259.635,'K')),
            NASAPolynomial(coeffs=[16.1212,0.0456237,-3.61577e-05,1.28209e-08,-1.66807e-12,24878.3,-33.1563], Tmin=(259.635,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (215.327,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 62.43 kcal/mol
S298: 140.67 cal/mol/K

Coordinates (Angstoms):
Br 3.38255 0.52418 0.77573
C 1.50530 0.09225 0.72383
C 0.85433 0.09463 -0.65973
Br 1.88320 -1.05470 -1.86270
Br 1.01990 1.88777 -1.40715
C -0.66463 -0.43966 -0.61828
Br -0.61372 -2.35283 -0.20359
Br -1.41247 -0.23650 -2.40086
C -1.70847 0.18951 0.42117
Br -1.27190 -0.17022 2.29060
Br -3.47962 -0.58794 0.16121
Br -1.92375 2.10451 0.25454
H 1.02510 0.83829 1.34749
H 1.40417 -0.88929 1.17776

modes:
""",
    rank = 5,
)

entry(
    index = 62,
    label = "ClC(Cl)C(Cl)(Cl)C(Cl)(Cl)C(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {9,S}
2  Cl u0 p3 c0 {9,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {12,S}
8  Cl u0 p3 c0 {12,S}
9  C  u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
10 C  u0 p0 c0 {3,S} {4,S} {9,S} {12,S}
11 C  u0 p0 c0 {5,S} {6,S} {9,S} {13,S}
12 C  u0 p0 c0 {7,S} {8,S} {10,S} {14,S}
13 H  u0 p0 c0 {11,S}
14 H  u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.60101,0.119358,-0.000196192,1.65104e-07,-5.51354e-11,-28890,16.7001], Tmin=(10,'K'), Tmax=(724.522,'K')),
            NASAPolynomial(coeffs=[17.5281,0.0369479,-2.55752e-05,8.112e-09,-9.6443e-13,-31053,-50.5041], Tmin=(724.522,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-240.368,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -48.18 kcal/mol
S298: 118.68 cal/mol/K

Coordinates (Angstoms):
Cl -3.24571 -1.07432 0.03693
C -2.02753 0.19011 0.22623
Cl -2.45399 1.56560 -0.78778
C -0.58711 -0.36368 -0.03167
Cl -0.52177 -1.07258 -1.64174
Cl -0.36842 -1.64632 1.19564
C 0.57750 0.71311 0.18285
Cl 0.12957 1.71769 1.59359
Cl 0.77549 1.74169 -1.23199
C 1.96299 0.09337 0.56293
Cl 3.17089 1.34891 0.85190
Cl 2.58416 -1.04686 -0.62723
H -2.08104 0.52119 1.25631
H 1.84626 -0.44624 1.49493

modes:
""",
    rank = 5,
)

entry(
    index = 63,
    label = "BrC(OC(Br)(Br)Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {9,S}
2  Br u0 p3 c0 {10,S}
3  Br u0 p3 c0 {10,S}
4  Br u0 p3 c0 {10,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {11,S}
8  O  u0 p2 c0 {9,S} {11,S}
9  C  u0 p0 c0 {1,S} {8,S} {10,S} {12,S}
10 C  u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
12 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.27852,0.173187,-0.00056947,9.59638e-07,-6.26173e-10,-241.763,22.0963], Tmin=(10,'K'), Tmax=(380.036,'K')),
            NASAPolynomial(coeffs=[15.3139,0.0359837,-2.79237e-05,9.63371e-09,-1.22187e-12,-1232.53,-28.18], Tmin=(380.036,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-2.01648,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 9.34 kcal/mol
S298: 136.39 cal/mol/K

Coordinates (Angstoms):
Br -0.42900 -1.05698 -2.26116
C -0.37150 0.16086 -0.74793
O 0.47313 -0.30960 0.25254
C 1.79546 0.01741 0.34134
Br 2.27280 -0.35814 2.17608
Br 2.90901 -1.06756 -0.83661
Br 2.16317 1.89886 -0.03926
C -1.76280 0.36632 -0.10432
Br -2.97394 1.10085 -1.41632
Br -1.55939 1.66182 1.32662
Br -2.46229 -1.27920 0.61448
H -0.03039 1.11579 -1.14458

modes:
""",
    rank = 5,
)

entry(
    index = 64,
    label = "ClC(Cl)C(Cl)C(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {8,S}
2  Cl u0 p3 c0 {9,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {9,S} {10,S} {12,S}
9  C  u0 p0 c0 {2,S} {8,S} {11,S} {13,S}
10 C  u0 p0 c0 {3,S} {4,S} {8,S} {14,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
12 H  u0 p0 c0 {8,S}
13 H  u0 p0 c0 {9,S}
14 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.87955,0.108176,-0.000191037,1.91836e-07,-7.93016e-11,-33057.6,17.5766], Tmin=(10,'K'), Tmax=(579.733,'K')),
            NASAPolynomial(coeffs=[11.6841,0.0474279,-3.38565e-05,1.1086e-08,-1.35657e-12,-34078.5,-20.1], Tmin=(579.733,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-274.892,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -57.11 kcal/mol
S298: 117.79 cal/mol/K

Coordinates (Angstoms):
Cl 1.86329 0.33356 -2.00740
C 1.81351 0.74877 -0.27970
Cl 3.37260 0.36198 0.45397
C 0.67295 0.00234 0.43190
Cl 0.66014 0.49686 2.13604
C -0.67399 0.21714 -0.27019
Cl -1.16930 1.91772 -0.21672
C -1.84518 -0.71573 0.13837
Cl -3.12563 -0.54738 -1.08146
Cl -1.26782 -2.39767 0.09206
Cl -2.53157 -0.38198 1.72305
H 1.67753 1.82426 -0.21132
H 0.90315 -1.06139 0.41286
H -0.50924 -0.01414 -1.32115

modes:
""",
    rank = 5,
)

entry(
    index = 65,
    label = "ClC(OC(Cl)(Cl)Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {9,S}
2  Cl u0 p3 c0 {10,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  O  u0 p2 c0 {9,S} {11,S}
9  C  u0 p0 c0 {1,S} {8,S} {10,S} {12,S}
10 C  u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
12 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.77637,0.105377,-0.000176126,1.48539e-07,-4.94962e-11,-44220,17.8503], Tmin=(10,'K'), Tmax=(727.249,'K')),
            NASAPolynomial(coeffs=[16.3864,0.0305195,-2.17256e-05,7.00067e-09,-8.40452e-13,-46199.5,-43.4755], Tmin=(727.249,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-367.805,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -79.48 kcal/mol
S298: 116.18 cal/mol/K

Coordinates (Angstoms):
Cl 0.76808 -0.80857 2.32415
C 0.46015 0.03136 0.79487
O -0.57721 -0.57804 0.09041
C -1.85638 -0.09825 0.17703
Cl -2.78713 -1.03939 -0.98030
Cl -1.95865 1.63168 -0.25057
Cl -2.55059 -0.29993 1.80172
C 1.71609 0.00681 -0.11788
Cl 2.16688 -1.64262 -0.53275
Cl 1.34136 0.90869 -1.59367
Cl 3.04284 0.81712 0.71955
H 0.23456 1.07113 1.02975

modes:
""",
    rank = 5,
)

entry(
    index = 66,
    label = "ClCC(Cl)(Cl)C(Cl)(Cl)C(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {8,S}
2  Cl u0 p3 c0 {8,S}
3  Cl u0 p3 c0 {9,S}
4  Cl u0 p3 c0 {9,S}
5  Cl u0 p3 c0 {10,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
9  C  u0 p0 c0 {3,S} {4,S} {8,S} {11,S}
10 C  u0 p0 c0 {5,S} {8,S} {12,S} {13,S}
11 C  u0 p0 c0 {6,S} {7,S} {9,S} {14,S}
12 H  u0 p0 c0 {10,S}
13 H  u0 p0 c0 {10,S}
14 H  u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.7852,0.104006,-0.000157252,1.25705e-07,-4.04798e-11,-29936.6,16.7666], Tmin=(10,'K'), Tmax=(743.968,'K')),
            NASAPolynomial(coeffs=[14.8974,0.0388841,-2.59516e-05,8.04776e-09,-9.42692e-13,-31738.8,-38.0855], Tmin=(743.968,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-249.047,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -50.97 kcal/mol
S298: 114.61 cal/mol/K

Coordinates (Angstoms):
Cl 3.22230 -0.37281 1.66410
C 1.97335 -0.20981 0.42764
C 0.55966 -0.03478 1.00762
Cl 0.58270 1.36755 2.08981
Cl 0.12513 -1.48497 1.94714
C -0.50434 0.14761 -0.15741
Cl -0.22325 -1.15899 -1.34857
Cl -0.24683 1.70474 -0.95116
C -1.99762 -0.01306 0.26539
Cl -3.07444 0.07494 -1.13451
Cl -2.54613 1.13916 1.47745
H 2.01064 -1.10477 -0.18187
H 2.21271 0.66123 -0.17828
H -2.11254 -1.00405 0.69144

modes:
""",
    rank = 5,
)

entry(
    index = 67,
    label = "BrC(Br)C(Br)(C(Br)Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {9,S}
2  Br u0 p3 c0 {10,S}
3  Br u0 p3 c0 {10,S}
4  Br u0 p3 c0 {11,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {12,S}
7  Br u0 p3 c0 {12,S}
8  Br u0 p3 c0 {12,S}
9  C  u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
10 C  u0 p0 c0 {2,S} {3,S} {9,S} {13,S}
11 C  u0 p0 c0 {4,S} {5,S} {9,S} {14,S}
12 C  u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
13 H  u0 p0 c0 {10,S}
14 H  u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.49657,0.165312,-0.000166834,-1.33035e-06,3.18279e-09,25683.1,19.9892], Tmin=(10,'K'), Tmax=(239.299,'K')),
            NASAPolynomial(coeffs=[15.4138,0.0470107,-3.71858e-05,1.3153e-08,-1.70781e-12,24785.4,-29.6969], Tmin=(239.299,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (213.616,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 61.93 kcal/mol
S298: 140.27 cal/mol/K

Coordinates (Angstoms):
Br -0.92706 -2.61202 -0.53780
C 0.11466 -1.11884 -1.19534
Br 1.81986 -1.80526 -1.82100
C 0.24766 0.17651 -0.30473
Br 0.94251 1.48660 -1.61243
C 1.40166 0.03267 0.73944
Br 1.80662 1.57006 1.83264
Br 1.38799 -1.54039 1.87160
C -1.16488 0.72973 0.18171
Br -2.51182 0.50386 -1.21894
Br -1.20225 2.63581 0.58797
Br -1.80029 -0.14793 1.78745
H -0.40221 -0.82384 -2.09760
H 2.29529 -0.10559 0.14511

modes:
""",
    rank = 5,
)

entry(
    index = 68,
    label = "BrCC(Br)(C(Br)(Br)Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {9,S}
2  Br u0 p3 c0 {10,S}
3  Br u0 p3 c0 {11,S}
4  Br u0 p3 c0 {11,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {12,S}
7  Br u0 p3 c0 {12,S}
8  Br u0 p3 c0 {12,S}
9  C  u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
10 C  u0 p0 c0 {2,S} {9,S} {13,S} {14,S}
11 C  u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
12 C  u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
13 H  u0 p0 c0 {10,S}
14 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.23462,0.17013,-0.000463731,6.51233e-07,-3.56403e-10,29024.5,20.1663], Tmin=(10,'K'), Tmax=(451.364,'K')),
            NASAPolynomial(coeffs=[16.9753,0.0394979,-2.96095e-05,1.00344e-08,-1.25921e-12,27693.8,-39.2229], Tmin=(451.364,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (241.29,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (324.264,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 68.10 kcal/mol
S298: 135.22 cal/mol/K

Coordinates (Angstoms):
Br -1.60992 -2.55916 -0.55301
C -0.29821 -1.16709 -0.76391
C -0.23441 0.00198 0.28056
Br -1.55997 -0.15005 1.70848
C 1.18438 -0.11024 1.01712
Br 2.71693 -0.04026 -0.18615
Br 1.52428 1.18216 2.41489
Br 1.29319 -1.87534 1.86360
C -0.61990 1.34591 -0.50266
Br -2.40928 1.11070 -1.26833
Br -0.69291 2.96199 0.55727
Br 0.52856 1.73756 -2.02834
H 0.65511 -1.68090 -0.78902
H -0.47782 -0.75727 -1.75052

modes:
""",
    rank = 5,
)

entry(
    index = 69,
    label = "ClCDC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {8,S}
2  Cl u0 p3 c0 {8,S}
3  Cl u0 p3 c0 {9,S}
4  Cl u0 p3 c0 {9,S}
5  Cl u0 p3 c0 {9,S}
6  Cl u0 p3 c0 {10,S}
7  Cl u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
9  C  u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
10 C  u0 p0 c0 {6,S} {8,S} {11,D}
11 C  u0 p0 c0 {7,S} {10,D} {12,S}
12 H  u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.99775,0.0889047,-2.4434e-05,-2.99408e-07,3.67554e-10,-14021.8,16.6834], Tmin=(10,'K'), Tmax=(413.368,'K')),
            NASAPolynomial(coeffs=[13.4054,0.0394302,-3.08281e-05,1.07564e-08,-1.37771e-12,-15320,-29.6282], Tmin=(413.368,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-116.594,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -19.50 kcal/mol
S298: 113.78 cal/mol/K

Coordinates (Angstoms):
Cl -2.99422 -1.56392 -0.85184
C -1.77629 -0.40704 -0.57640
C -0.86279 -0.49372 0.38430
Cl -0.87120 -1.82094 1.47125
C 0.23254 0.56600 0.54713
Cl 0.62536 0.78917 2.25880
Cl -0.34326 2.13429 -0.07077
C 1.56368 0.20005 -0.24340
Cl 2.78213 1.45908 -0.02755
Cl 2.22610 -1.32972 0.33719
Cl 1.21501 0.03806 -1.97137
H -1.79705 0.42869 -1.25734

modes:
""",
    rank = 5,
)

entry(
    index = 70,
    label = "BrC(CC(Br)(Br)Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {8,S}
2  Br u0 p3 c0 {10,S}
3  Br u0 p3 c0 {10,S}
4  Br u0 p3 c0 {10,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {9,S} {11,S} {12,S}
9  C  u0 p0 c0 {8,S} {10,S} {13,S} {14,S}
10 C  u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
12 H  u0 p0 c0 {8,S}
13 H  u0 p0 c0 {9,S}
14 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.79137,0.137436,1.80111e-05,-2.23992e-06,5.01562e-09,10508.1,20.5277], Tmin=(10,'K'), Tmax=(216.157,'K')),
            NASAPolynomial(coeffs=[12.9036,0.0477642,-3.59897e-05,1.23652e-08,-1.57619e-12,9843.28,-18.0348], Tmin=(216.157,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (87.5883,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 30.83 kcal/mol
S298: 135.57 cal/mol/K

Coordinates (Angstoms):
Br -0.32242 -1.64073 1.91557
C -0.43361 -0.66947 0.23213
C 0.46208 0.57693 0.26916
C 1.87804 0.43419 -0.29404
Br 2.71141 2.18588 -0.16502
Br 2.96368 -0.83279 0.68641
Br 1.84478 -0.09760 -2.16109
C -1.90683 -0.33584 -0.09725
Br -1.99590 0.45567 -1.87513
Br -2.64741 0.92306 1.17675
Br -2.99365 -1.93625 -0.13897
H -0.09880 -1.37599 -0.52672
H 0.54568 0.94273 1.29207
H -0.00703 1.37021 -0.31385

modes:
""",
    rank = 5,
)

entry(
    index = 71,
    label = "BrC(Br)DCC(Br)(Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {8,S}
2  Br u0 p3 c0 {8,S}
3  Br u0 p3 c0 {9,S}
4  Br u0 p3 c0 {9,S}
5  Br u0 p3 c0 {9,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
9  C  u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
10 C  u0 p0 c0 {8,S} {11,D} {12,S}
11 C  u0 p0 c0 {6,S} {7,S} {10,D}
12 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.62738,0.146947,-0.000223464,-6.01807e-07,1.64989e-09,28579.2,20.0336], Tmin=(10,'K'), Tmax=(260.143,'K')),
            NASAPolynomial(coeffs=[14.5237,0.0388292,-3.1364e-05,1.12214e-08,-1.46681e-12,27707.2,-26.2053], Tmin=(260.143,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (237.675,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 66.58 kcal/mol
S298: 132.77 cal/mol/K

Coordinates (Angstoms):
Br 3.01906 -2.02496 0.46522
C 2.05136 -0.43984 0.15994
Br 3.11358 1.06684 -0.12728
C 0.72577 -0.48405 0.16682
C -0.27815 0.61661 -0.03854
Br -0.05033 2.01257 1.30870
Br -0.05640 1.43002 -1.80042
C -1.73582 0.03439 0.07389
Br -1.99784 -1.35554 -1.26201
Br -1.99153 -0.77845 1.82285
Br -3.09409 1.38209 -0.17565
H 0.29438 -1.45968 0.34683

modes:
""",
    rank = 5,
)

entry(
    index = 72,
    label = "ClC(Cl)DC(Cl)C(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {8,S}
2  Cl u0 p3 c0 {9,S}
3  Cl u0 p3 c0 {9,S}
4  Cl u0 p3 c0 {9,S}
5  Cl u0 p3 c0 {10,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {9,S} {10,S} {12,S}
9  C  u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
10 C  u0 p0 c0 {5,S} {8,S} {11,D}
11 C  u0 p0 c0 {6,S} {7,S} {10,D}
12 H  u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.82087,0.10712,-0.000193677,1.81917e-07,-6.80724e-11,-17847.8,17.5317], Tmin=(10,'K'), Tmax=(647.44,'K')),
            NASAPolynomial(coeffs=[14.605,0.034316,-2.50026e-05,8.2343e-09,-1.00747e-12,-19373.7,-34.1972], Tmin=(647.44,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-148.488,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -27.09 kcal/mol
S298: 116.04 cal/mol/K

Coordinates (Angstoms):
Cl 1.91647 -1.12937 1.48130
C 1.71165 0.41282 0.75337
Cl 3.11755 1.37822 0.78087
C 0.55985 0.81463 0.20750
Cl 0.44865 2.37850 -0.48617
C -0.67996 -0.03676 0.22852
Cl -1.99560 0.80279 1.07499
C -1.15717 -0.58822 -1.14443
Cl 0.23659 -1.34463 -1.94082
Cl -1.84547 0.63164 -2.21143
Cl -2.37875 -1.84011 -0.84671
H -0.46257 -0.92264 0.81844

modes:
""",
    rank = 5,
)

entry(
    index = 73,
    label = "ClCC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {8,S}
2  Cl u0 p3 c0 {9,S}
3  Cl u0 p3 c0 {9,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {9,S} {10,S} {12,S}
9  C  u0 p0 c0 {2,S} {3,S} {8,S} {11,S}
10 C  u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
12 H  u0 p0 c0 {8,S}
13 H  u0 p0 c0 {10,S}
14 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.77478,0.104658,-0.000159128,1.27753e-07,-4.1277e-11,-29384.6,16.9104], Tmin=(10,'K'), Tmax=(742.101,'K')),
            NASAPolynomial(coeffs=[15.0088,0.0387151,-2.58383e-05,8.01254e-09,-9.38564e-13,-31200.4,-38.4627], Tmin=(742.101,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-244.46,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -49.84 kcal/mol
S298: 115.03 cal/mol/K

Coordinates (Angstoms):
Cl -3.42730 -0.12740 0.02888
C -1.85950 0.68196 -0.15995
C -0.71803 -0.24008 0.26331
Cl -0.77432 -0.42244 2.02920
C 0.65437 0.24463 -0.28744
Cl 0.50031 0.11446 -2.06447
Cl 0.94752 1.93529 0.14257
C 1.92282 -0.61691 0.12942
Cl 1.56155 -2.33350 -0.11740
Cl 2.40069 -0.36307 1.80766
Cl 3.31721 -0.17501 -0.86974
H -1.76910 0.95641 -1.20628
H -1.87435 1.57873 0.45346
H -0.88185 -1.23309 -0.14923

modes:
""",
    rank = 5,
)

entry(
    index = 74,
    label = "ClOC(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {10,S}
2  Cl u0 p3 c0 {11,S}
3  Cl u0 p3 c0 {11,S}
4  Cl u0 p3 c0 {11,S}
5  Cl u0 p3 c0 {12,S}
6  Cl u0 p3 c0 {12,S}
7  Cl u0 p3 c0 {12,S}
8  Cl u0 p3 c0 {9,S}
9  O  u0 p2 c0 {8,S} {10,S}
10 C  u0 p0 c0 {1,S} {9,S} {11,S} {12,S}
11 C  u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
12 C  u0 p0 c0 {5,S} {6,S} {7,S} {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.85259,0.100578,-5.1432e-06,-4.51825e-07,5.40817e-10,-18492.5,16.9201], Tmin=(10,'K'), Tmax=(407.042,'K')),
            NASAPolynomial(coeffs=[16.2703,0.0382604,-3.17486e-05,1.14512e-08,-1.49696e-12,-20160.9,-42.8283], Tmin=(407.042,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-153.756,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -27.54 kcal/mol
S298: 119.22 cal/mol/K

Coordinates (Angstoms):
Cl -1.51468 0.03410 2.45293
O -0.40843 -0.60445 1.37911
C 0.07189 0.20476 0.35517
Cl 0.68177 1.75324 0.95665
C -1.09125 0.46658 -0.74045
Cl -2.10515 1.84492 -0.27169
Cl -0.45404 0.81908 -2.34551
Cl -2.15280 -0.94441 -0.84424
C 1.35795 -0.64179 -0.12587
Cl 2.43459 0.27602 -1.18067
Cl 2.29994 -1.08093 1.31173
Cl 0.88022 -2.12713 -0.94718

modes:
""",
    rank = 5,
)

entry(
    index = 75,
    label = "ClOC(Cl)C(Cl)(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {9,S}
2  Cl u0 p3 c0 {9,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {11,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {8,S}
8  O  u0 p2 c0 {7,S} {10,S}
9  C  u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
10 C  u0 p0 c0 {3,S} {8,S} {9,S} {12,S}
11 C  u0 p0 c0 {4,S} {5,S} {6,S} {9,S}
12 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.73938,0.107365,-0.000182667,1.56284e-07,-5.26909e-11,-24827.8,17.1622], Tmin=(10,'K'), Tmax=(720.425,'K')),
            NASAPolynomial(coeffs=[16.7136,0.0297766,-2.11193e-05,6.79095e-09,-8.14175e-13,-26841.2,-45.6731], Tmin=(720.425,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-206.578,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -40.88 kcal/mol
S298: 115.11 cal/mol/K

Coordinates (Angstoms):
Cl 2.68259 0.12110 1.76072
O 1.58839 -0.47012 0.64423
C 0.98761 0.54109 -0.09118
Cl 2.10059 1.17522 -1.32784
C -0.31472 -0.03162 -0.72538
Cl 0.05477 -1.30029 -1.88901
Cl -1.08816 1.33541 -1.54844
C -1.33282 -0.60013 0.35428
Cl -2.89670 -0.92589 -0.40220
Cl -0.77131 -2.10359 1.08379
Cl -1.55747 0.60711 1.63643
H 0.71752 1.38836 0.53636

modes:
""",
    rank = 5,
)

entry(
    index = 76,
    label = "ClC(Cl)(Cl)C(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {11,S}
2  Cl u0 p3 c0 {12,S}
3  Cl u0 p3 c0 {12,S}
4  Cl u0 p3 c0 {12,S}
5  Cl u0 p3 c0 {13,S}
6  Cl u0 p3 c0 {13,S}
7  Cl u0 p3 c0 {13,S}
8  Cl u0 p3 c0 {14,S}
9  Cl u0 p3 c0 {14,S}
10 Cl u0 p3 c0 {14,S}
11 C  u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
12 C  u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
13 C  u0 p0 c0 {5,S} {6,S} {7,S} {11,S}
14 C  u0 p0 c0 {8,S} {9,S} {10,S} {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.76107,0.103799,0.000192244,-1.19651e-06,1.32351e-09,-12716.3,16.0552], Tmin=(10,'K'), Tmax=(380.336,'K')),
            NASAPolynomial(coeffs=[19.3495,0.0458735,-3.89079e-05,1.42664e-08,-1.88836e-12,-14821,-59.0189], Tmin=(380.336,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-105.663,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -14.56 kcal/mol
S298: 125.81 cal/mol/K

Coordinates (Angstoms):
Cl -0.83060 -1.40099 1.98995
C -0.50741 0.25961 1.46921
Cl 0.71938 0.91921 2.56571
Cl -1.96266 1.21788 1.82370
C -0.05996 0.35656 -0.10645
Cl -0.34517 2.02759 -0.60160
C 1.54248 0.07719 -0.31914
Cl 1.95926 -0.22700 -2.01455
Cl 2.12528 -1.30896 0.61475
Cl 2.53839 1.47970 0.12931
C -0.99280 -0.57606 -1.08012
Cl -2.69560 -0.57572 -0.58777
Cl -1.02716 0.01532 -2.75659
Cl -0.46344 -2.26433 -1.12641

modes:
""",
    rank = 5,
)

entry(
    index = 77,
    label = "ClC(CC(Cl)(Cl)Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {8,S}
2  Cl u0 p3 c0 {10,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {9,S} {11,S} {12,S}
9  C  u0 p0 c0 {8,S} {10,S} {13,S} {14,S}
10 C  u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
12 H  u0 p0 c0 {8,S}
13 H  u0 p0 c0 {9,S}
14 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.81199,0.105049,-0.000163862,1.37077e-07,-4.64383e-11,-33148.7,17.7198], Tmin=(10,'K'), Tmax=(706.457,'K')),
            NASAPolynomial(coeffs=[14.1191,0.0410275,-2.79285e-05,8.80061e-09,-1.04427e-12,-34746.3,-32.9016], Tmin=(706.457,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-275.732,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -57.32 kcal/mol
S298: 117.02 cal/mol/K

Coordinates (Angstoms):
Cl -0.52780 -1.77356 -1.49447
C -0.51593 -0.62473 -0.13727
C 0.54805 0.45737 -0.35106
C 1.90109 0.18917 0.30668
Cl 2.96739 1.55626 -0.07822
Cl 2.64892 -1.30294 -0.28182
Cl 1.73243 0.08129 2.07315
C -1.92944 -0.02666 0.06157
Cl -1.91433 0.97278 1.53216
Cl -2.39536 0.98007 -1.31796
Cl -3.12231 -1.30831 0.28833
H -0.30918 -1.20828 0.75930
H 0.71612 0.60152 -1.41733
H 0.20036 1.40600 0.05693

modes:
""",
    rank = 5,
)

entry(
    index = 78,
    label = "BrOC(Br)C(Br)(Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {9,S}
2  Br u0 p3 c0 {9,S}
3  Br u0 p3 c0 {10,S}
4  Br u0 p3 c0 {11,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {8,S}
8  O  u0 p2 c0 {7,S} {10,S}
9  C  u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
10 C  u0 p0 c0 {3,S} {8,S} {9,S} {12,S}
11 C  u0 p0 c0 {4,S} {5,S} {6,S} {9,S}
12 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.63065,0.149306,-0.00020525,-8.54979e-07,2.22762e-09,14300.9,20.0728], Tmin=(10,'K'), Tmax=(246.812,'K')),
            NASAPolynomial(coeffs=[14.4186,0.0395371,-3.20821e-05,1.14971e-08,-1.50389e-12,13471.5,-25.3194], Tmin=(246.812,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (118.96,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 38.28 kcal/mol
S298: 133.70 cal/mol/K

Coordinates (Angstoms):
Br 1.67563 0.98513 -2.61240
O 1.22557 -0.00185 -1.16164
C 0.90865 0.74234 -0.04421
Br 2.53800 1.38871 0.82887
C 0.01525 -0.13302 0.88419
Br -0.48602 1.02110 2.36863
Br 1.00271 -1.64996 1.56171
C -1.30349 -0.64006 0.16858
Br -2.21181 0.85698 -0.68491
Br -2.52583 -1.44091 1.44537
Br -0.98951 -1.98505 -1.19486
H 0.35651 1.64753 -0.28965

modes:
""",
    rank = 5,
)

entry(
    index = 79,
    label = "ClCC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {8,S}
2  Cl u0 p3 c0 {8,S}
3  Cl u0 p3 c0 {9,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
9  C  u0 p0 c0 {3,S} {8,S} {11,S} {12,S}
10 C  u0 p0 c0 {4,S} {8,S} {13,S} {14,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
12 H  u0 p0 c0 {9,S}
13 H  u0 p0 c0 {10,S}
14 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.78075,0.1035,-0.000153901,1.20283e-07,-3.78081e-11,-29684,17.2547], Tmin=(10,'K'), Tmax=(761.993,'K')),
            NASAPolynomial(coeffs=[15.2198,0.0382035,-2.53636e-05,7.8261e-09,-9.12697e-13,-31579.7,-39.3755], Tmin=(761.993,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-246.953,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -50.47 kcal/mol
S298: 115.44 cal/mol/K

Coordinates (Angstoms):
Cl -2.51723 -1.13032 0.98952
C -2.01413 0.01917 -0.26282
C -0.53197 -0.09846 -0.64523
Cl -0.32291 -1.70857 -1.38620
Cl -0.28003 1.15023 -1.88431
C 0.42520 0.04957 0.57586
Cl -0.16497 1.32661 1.66274
C 1.96373 0.26863 0.38183
Cl 2.39153 1.91985 -0.07782
Cl 2.72462 -0.08244 1.95603
Cl 2.66473 -0.83713 -0.80175
H -2.22343 1.02027 0.09958
H -2.60150 -0.18459 -1.15381
H 0.32887 -0.88283 1.12995

modes:
""",
    rank = 5,
)

entry(
    index = 80,
    label = "ClC(Cl)DCC(Cl)(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {8,S}
2  Cl u0 p3 c0 {8,S}
3  Cl u0 p3 c0 {9,S}
4  Cl u0 p3 c0 {9,S}
5  Cl u0 p3 c0 {9,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
9  C  u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
10 C  u0 p0 c0 {8,S} {11,D} {12,S}
11 C  u0 p0 c0 {6,S} {7,S} {10,D}
12 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.95104,0.0938699,-6.27522e-05,-1.96616e-07,2.75263e-10,-15065.6,16.9001], Tmin=(10,'K'), Tmax=(420.86,'K')),
            NASAPolynomial(coeffs=[13.5421,0.0389939,-3.03503e-05,1.05483e-08,-1.34683e-12,-16362.5,-29.8466], Tmin=(420.86,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-125.283,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -21.52 kcal/mol
S298: 114.68 cal/mol/K

Coordinates (Angstoms):
Cl 3.00596 -1.82190 0.41811
C 2.04660 -0.42268 0.13831
Cl 2.94799 0.99339 -0.16471
C 0.72393 -0.50591 0.17142
C -0.26954 0.60454 -0.03632
Cl -0.06142 1.87989 1.18999
Cl -0.08900 1.33339 -1.65100
C -1.73679 0.03546 0.08707
Cl -1.98135 -1.22630 -1.13341
Cl -1.95655 -0.68499 1.69139
Cl -2.93913 1.29822 -0.14402
H 0.30930 -1.48309 0.37352

modes:
""",
    rank = 5,
)

entry(
    index = 81,
    label = "OC(Br)(C(Br)(Br)Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {9,S}
2  Br u0 p3 c0 {10,S}
3  Br u0 p3 c0 {10,S}
4  Br u0 p3 c0 {10,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {11,S}
8  O  u0 p2 c0 {9,S} {12,S}
9  C  u0 p0 c0 {1,S} {8,S} {10,S} {11,S}
10 C  u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
12 H  u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.5288,0.144894,-0.000260327,-5.25623e-08,4.42136e-10,4503.61,20.0867], Tmin=(10,'K'), Tmax=(332.611,'K')),
            NASAPolynomial(coeffs=[16.4987,0.0352108,-2.86892e-05,1.03129e-08,-1.35066e-12,3251.72,-36.7815], Tmin=(332.611,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (37.5121,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 18.88 kcal/mol
S298: 132.19 cal/mol/K

Coordinates (Angstoms):
O -0.10855 0.32678 1.53815
C 0.07856 -0.25464 0.32426
Br 0.28309 -2.22655 0.51911
C -1.29944 0.01315 -0.43271
Br -1.31243 -0.56700 -2.26829
Br -2.72903 -0.92351 0.50702
Br -1.83042 1.88321 -0.37999
C 1.47598 0.24236 -0.30541
Br 2.83891 -0.01053 1.09347
Br 1.50618 2.12780 -0.72925
Br 2.10846 -0.71303 -1.85975
H 0.67822 0.21072 2.08687

modes:
""",
    rank = 5,
)

entry(
    index = 82,
    label = "OC(Cl)(C(Cl)(Cl)Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {9,S}
2  Cl u0 p3 c0 {10,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  O  u0 p2 c0 {9,S} {12,S}
9  C  u0 p0 c0 {1,S} {8,S} {10,S} {11,S}
10 C  u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
12 H  u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.14063,0.0707574,0.000170714,-8.88347e-07,9.29377e-10,-41456.8,16.6623], Tmin=(10,'K'), Tmax=(390.513,'K')),
            NASAPolynomial(coeffs=[14.5074,0.0388714,-3.15475e-05,1.13237e-08,-1.48082e-12,-42989.3,-35.7415], Tmin=(390.513,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-344.658,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -73.90 kcal/mol
S298: 113.70 cal/mol/K

Coordinates (Angstoms):
O -0.17826 -1.08739 -1.14351
C 0.12327 -0.40395 -0.00696
Cl 0.74774 -1.50731 1.27397
C 1.32162 0.55550 -0.43575
Cl 2.70483 -0.46058 -0.88522
Cl 0.91432 1.51379 -1.86384
Cl 1.82145 1.63938 0.85801
C -1.21581 0.23939 0.60313
Cl -1.03409 0.94267 2.20303
Cl -2.39648 -1.10574 0.73960
Cl -1.92875 1.43842 -0.47080
H -0.89793 -1.70509 -0.96644

modes:
""",
    rank = 5,
)

entry(
    index = 83,
    label = "ClC(Cl)OC(Cl)(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {9,S}
2  Cl u0 p3 c0 {9,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {10,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  O  u0 p2 c0 {9,S} {11,S}
9  C  u0 p0 c0 {1,S} {2,S} {8,S} {10,S}
10 C  u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
11 C  u0 p0 c0 {6,S} {7,S} {8,S} {12,S}
12 H  u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.79267,0.107365,-0.000186568,1.65412e-07,-5.81595e-11,-44199.5,17.7825], Tmin=(10,'K'), Tmax=(688.906,'K')),
            NASAPolynomial(coeffs=[15.6803,0.0325355,-2.36364e-05,7.74063e-09,-9.41394e-13,-45975.2,-39.5902], Tmin=(688.906,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-367.612,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -79.38 kcal/mol
S298: 116.74 cal/mol/K

Coordinates (Angstoms):
Cl 2.38725 -0.00445 -1.72433
C 1.74813 0.48511 -0.15570
Cl 2.93106 0.20118 1.12034
O 0.59898 -0.25184 0.11218
C -0.58477 0.40485 0.29757
Cl -1.02643 1.38417 -1.12568
Cl -0.51871 1.49124 1.70919
C -1.66092 -0.72612 0.52990
Cl -3.25121 -0.01531 0.78193
Cl -1.20365 -1.67371 1.94542
Cl -1.69927 -1.77863 -0.88521
H 1.54724 1.55184 -0.19335

modes:
""",
    rank = 5,
)

entry(
    index = 84,
    label = "ClC(Cl)C(Cl)(C(Cl)Cl)C(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {8,S}
2  Cl u0 p3 c0 {9,S}
3  Cl u0 p3 c0 {9,S}
4  Cl u0 p3 c0 {10,S}
5  Cl u0 p3 c0 {10,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
9  C  u0 p0 c0 {2,S} {3,S} {8,S} {12,S}
10 C  u0 p0 c0 {4,S} {5,S} {8,S} {13,S}
11 C  u0 p0 c0 {6,S} {7,S} {8,S} {14,S}
12 H  u0 p0 c0 {9,S}
13 H  u0 p0 c0 {10,S}
14 H  u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.87348,0.104252,-0.000167449,1.48234e-07,-5.37152e-11,-30809.2,16.6124], Tmin=(10,'K'), Tmax=(658.555,'K')),
            NASAPolynomial(coeffs=[12.7538,0.0442405,-3.07598e-05,9.86147e-09,-1.18656e-12,-32110.5,-26.9272], Tmin=(658.555,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-256.242,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -52.73 kcal/mol
S298: 114.89 cal/mol/K

Coordinates (Angstoms):
Cl -1.41018 -2.13770 -1.15920
C -1.37694 -0.46590 -0.57875
Cl -1.77316 0.63196 -1.91179
C -0.04829 -0.11523 0.17144
Cl -0.07420 -1.14895 1.61981
C -0.08615 1.37439 0.59828
Cl 1.31711 1.85615 1.54565
Cl -1.56860 1.77367 1.48672
C 1.20043 -0.48339 -0.70001
Cl 1.58250 0.76584 -1.90182
Cl 2.66409 -0.89444 0.19479
H -2.18420 -0.37464 0.13842
H -0.09021 1.99107 -0.29357
H 0.94488 -1.37320 -1.26475

modes:
""",
    rank = 5,
)

entry(
    index = 85,
    label = "ClC(Cl)C(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {9,S}
2  Cl u0 p3 c0 {9,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {11,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {12,S}
7  Cl u0 p3 c0 {12,S}
8  Cl u0 p3 c0 {12,S}
9  C  u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
10 C  u0 p0 c0 {3,S} {9,S} {12,S} {13,S}
11 C  u0 p0 c0 {4,S} {5,S} {9,S} {14,S}
12 C  u0 p0 c0 {6,S} {7,S} {8,S} {10,S}
13 H  u0 p0 c0 {10,S}
14 H  u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.60573,0.119501,-0.000197215,1.66928e-07,-5.6105e-11,-29428.4,17.7169], Tmin=(10,'K'), Tmax=(719.723,'K')),
            NASAPolynomial(coeffs=[17.397,0.0372954,-2.58874e-05,8.22935e-09,-9.80153e-13,-31557.6,-48.7779], Tmin=(719.723,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-244.842,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -49.25 kcal/mol
S298: 120.78 cal/mol/K

Coordinates (Angstoms):
Cl 2.43574 1.42522 0.45224
C 1.99265 -0.22196 -0.02027
Cl 3.14816 -1.37133 0.64438
C 0.52519 -0.55872 0.38682
Cl 0.44600 -0.54503 2.16088
Cl 0.18147 -2.18407 -0.22523
C -0.47110 0.50137 -0.18747
Cl -0.02837 0.93256 -1.85598
C -2.02091 0.25168 -0.16980
Cl -2.60613 -0.36072 1.37761
Cl -2.77549 1.84770 -0.42954
Cl -2.58500 -0.83593 -1.44190
H 2.07408 -0.27965 -1.09938
H -0.31630 1.39888 0.40763

modes:
""",
    rank = 5,
)

entry(
    index = 86,
    label = "BrC(Br)DC(Br)C(Br)(Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {9,S}
2  Br u0 p3 c0 {9,S}
3  Br u0 p3 c0 {10,S}
4  Br u0 p3 c0 {10,S}
5  Br u0 p3 c0 {10,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {12,S}
8  Br u0 p3 c0 {12,S}
9  C  u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
10 C  u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
11 C  u0 p0 c0 {6,S} {9,S} {12,D}
12 C  u0 p0 c0 {7,S} {8,S} {11,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.35224,0.172456,-0.000339302,-2.48976e-07,1.11596e-09,40923.4,20.4348], Tmin=(10,'K'), Tmax=(280.439,'K')),
            NASAPolynomial(coeffs=[17.3456,0.0367099,-3.10208e-05,1.1357e-08,-1.50417e-12,39775.3,-38.3134], Tmin=(280.439,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (340.327,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 92.05 kcal/mol
S298: 139.43 cal/mol/K

Coordinates (Angstoms):
Br 3.11348 -2.22999 0.00192
C 2.05703 -0.67667 -0.00109
Br 3.14846 0.84751 -0.00909
C 0.71256 -0.69890 0.00317
Br -0.08241 -2.41214 0.01923
C -0.18754 0.55538 -0.00153
Br 0.24209 1.60761 1.59649
Br 0.23941 1.59417 -1.60913
C -1.76880 0.37823 -0.00012
Br -2.41213 -0.53138 1.59154
Br -2.41046 -0.55070 -1.58125
Br -2.65169 2.11688 -0.01013

modes:
""",
    rank = 5,
)

entry(
    index = 87,
    label = "ClOC(Cl)(Cl)C(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {9,S}
2  Cl u0 p3 c0 {10,S}
3  Cl u0 p3 c0 {10,S}
4  Cl u0 p3 c0 {11,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {11,S}
7  Cl u0 p3 c0 {8,S}
8  O  u0 p2 c0 {7,S} {10,S}
9  C  u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
10 C  u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
11 C  u0 p0 c0 {4,S} {5,S} {6,S} {9,S}
12 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.74902,0.106373,-0.000177802,1.491e-07,-4.92711e-11,-24963.8,17.8733], Tmin=(10,'K'), Tmax=(734.373,'K')),
            NASAPolynomial(coeffs=[16.8452,0.0295937,-2.09759e-05,6.73333e-09,-8.05729e-13,-27034.2,-45.7807], Tmin=(734.373,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-207.711,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -41.17 kcal/mol
S298: 116.37 cal/mol/K

Coordinates (Angstoms):
Cl 2.86658 -0.78250 -1.04075
O 1.26634 -0.76882 -0.55767
C 1.00667 -0.15806 0.64870
Cl 1.86679 -0.99562 1.97827
Cl 1.52106 1.53716 0.64517
C -0.52848 -0.36291 0.91139
Cl -0.97930 0.58514 2.32903
C -1.53712 -0.13296 -0.26032
Cl -3.18461 -0.33743 0.37352
Cl -1.32741 -1.37810 -1.50661
Cl -1.39707 1.46308 -0.98934
H -0.63862 -1.41246 1.18052

modes:
""",
    rank = 5,
)

entry(
    index = 88,
    label = "BrC(Br)OC(Br)(Br)C(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {9,S}
2  Br u0 p3 c0 {9,S}
3  Br u0 p3 c0 {10,S}
4  Br u0 p3 c0 {10,S}
5  Br u0 p3 c0 {10,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {11,S}
8  O  u0 p2 c0 {9,S} {11,S}
9  C  u0 p0 c0 {1,S} {2,S} {8,S} {10,S}
10 C  u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
11 C  u0 p0 c0 {6,S} {7,S} {8,S} {12,S}
12 H  u0 p0 c0 {11,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.64253,0.149151,-0.000194234,-9.65904e-07,2.48359e-09,-439.124,20.6657], Tmin=(10,'K'), Tmax=(241.581,'K')),
            NASAPolynomial(coeffs=[14.2532,0.0400051,-3.25026e-05,1.16505e-08,-1.52388e-12,-1242.59,-23.8742], Tmin=(241.581,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-3.58924,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 8.98 kcal/mol
S298: 134.94 cal/mol/K

Coordinates (Angstoms):
Br 2.95380 -0.74475 1.16425
C 1.83679 0.40583 0.09499
Br 2.32084 2.25817 0.32499
O 0.51262 0.22812 0.46755
C -0.41207 -0.20132 -0.44244
Br 0.06855 -1.95338 -1.17843
Br -0.55460 1.03606 -1.95589
C -1.76634 -0.27760 0.35048
Br -3.21364 -0.86267 -0.77871
Br -2.18394 1.47144 1.06940
Br -1.57247 -1.51194 1.83009
H 2.01046 0.15203 -0.94629

modes:
""",
    rank = 5,
)

entry(
    index = 89,
    label = "ClC(Cl)(Cl)OC(Cl)(Cl)C(Cl)(Cl)Cl",
    molecule = 
"""
1  Cl u0 p3 c0 {10,S}
2  Cl u0 p3 c0 {10,S}
3  Cl u0 p3 c0 {11,S}
4  Cl u0 p3 c0 {11,S}
5  Cl u0 p3 c0 {11,S}
6  Cl u0 p3 c0 {12,S}
7  Cl u0 p3 c0 {12,S}
8  Cl u0 p3 c0 {12,S}
9  O  u0 p2 c0 {10,S} {12,S}
10 C  u0 p0 c0 {1,S} {2,S} {9,S} {11,S}
11 C  u0 p0 c0 {3,S} {4,S} {5,S} {10,S}
12 C  u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.79865,0.106645,-6.56895e-05,-2.68946e-07,3.64856e-10,-41509.4,17.5218], Tmin=(10,'K'), Tmax=(419.69,'K')),
            NASAPolynomial(coeffs=[16.1841,0.0380434,-3.12741e-05,1.11935e-08,-1.45457e-12,-43152.3,-41.6211], Tmin=(419.69,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-345.15,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: -73.28 kcal/mol
S298: 120.58 cal/mol/K

Coordinates (Angstoms):
Cl -2.60816 -1.15375 -0.83181
C -1.77384 -0.28078 0.45948
Cl -2.41772 1.37227 0.55702
Cl -2.07651 -1.09441 1.99826
O -0.39988 -0.26619 0.34493
C 0.36851 -0.12545 -0.79443
Cl -0.27382 1.01331 -1.98282
Cl 0.61027 -1.70023 -1.58128
C 1.75920 0.40812 -0.24705
Cl 2.90827 0.58848 -1.56725
Cl 1.50624 1.97062 0.53339
Cl 2.39743 -0.73198 0.93777

modes:
""",
    rank = 5,
)

entry(
    index = 90,
    label = "BrC(Br)C(Br)(Br)CC(Br)(Br)Br",
    molecule = 
"""
1  Br u0 p3 c0 {8,S}
2  Br u0 p3 c0 {8,S}
3  Br u0 p3 c0 {10,S}
4  Br u0 p3 c0 {10,S}
5  Br u0 p3 c0 {11,S}
6  Br u0 p3 c0 {11,S}
7  Br u0 p3 c0 {11,S}
8  C  u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
9  C  u0 p0 c0 {8,S} {11,S} {12,S} {13,S}
10 C  u0 p0 c0 {3,S} {4,S} {8,S} {14,S}
11 C  u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
12 H  u0 p0 c0 {9,S}
13 H  u0 p0 c0 {9,S}
14 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[2.78991,0.137253,9.77828e-06,-2.15561e-06,4.81724e-09,12168.1,20.0569], Tmin=(10,'K'), Tmax=(217.664,'K')),
            NASAPolynomial(coeffs=[12.882,0.0478505,-3.60973e-05,1.24136e-08,-1.58342e-12,11501.2,-18.4703], Tmin=(217.664,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (101.37,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'wb97xd3/def2-tzvp with bond corrections / RRHO',
    referenceType = "Theory",
    shortDesc = """wb97xd3/def2-tzvp""",
    longDesc = 
"""
H298: 34.12 kcal/mol
S298: 134.50 cal/mol/K

Coordinates (Angstoms):
Br -1.38303 1.49352 2.34496
C -1.80376 0.90634 0.54776
Br -1.98578 2.46433 -0.59022
C -0.78597 -0.12362 0.00039
Br -0.85305 -1.65975 1.19195
Br -1.49810 -0.74164 -1.71700
C 0.59537 0.53129 -0.19290
C 1.92177 -0.24016 -0.18760
Br 2.49065 -0.69586 1.61144
Br 1.92753 -1.82429 -1.29234
Br 3.24566 1.00356 -0.90515
H -2.78529 0.44839 0.59876
H 0.54035 1.05374 -1.14684
H 0.70715 1.29580 0.57856

modes:
""",
    rank = 5,
)

