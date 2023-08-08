#!/usr/bin/env python
# encoding: utf-8

name = "2-BTP_G4"
shortDesc = "2-BTP G4 thermo library"
longDesc = """
This library contains fluorinated and brominated hydrocarbons from 2-BTP RMG model
Each species was calculated at G4 level of theory with RRHO Approximation

It is recommended to pair this library with the `2-BTP` library
"""
entry(
    index = 0,
    label = "CCC(DO)C(F)(F)F",
    molecule = 
"""
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {7,S}
3  F u0 p3 c0 {7,S}
4  O u0 p2 c0 {8,D}
5  C u0 p0 c0 {6,S} {8,S} {9,S} {10,S}
6  C u0 p0 c0 {5,S} {11,S} {12,S} {13,S}
7  C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
8  C u0 p0 c0 {4,D} {5,S} {7,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61821,0.0466342,-2.53406e-05,3.48332e-09,8.65657e-13,-105988,12.9734], Tmin=(10,'K'), Tmax=(1241.8,'K')),
            NASAPolynomial(coeffs=[12.4136,0.0276185,-1.36237e-05,3.23412e-09,-3.00374e-13,-108891,-34.2563], Tmin=(1241.8,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -204.79 kcal/mol
S298: 92.19 cal/mol/K

Coordinates (Angstoms):
F 1.27979 -0.83705 1.08405
F 1.89848 0.93340 -0.00005
F 1.27977 -0.83715 -1.08399
O -0.66626 1.58495 -0.00002
C -1.46484 -0.69517 0.00001
C -2.89820 -0.17204 0.00001
C 1.04700 -0.07881 -0.00000
C -0.43130 0.40700 -0.00001
H -1.26179 -1.33333 0.87011
H -1.26181 -1.33334 -0.87009
H -3.60736 -1.00336 0.00003
H -3.08868 0.44586 -0.88094
H -3.08866 0.44588 0.88095

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 26.0,64.3,172.4,182.8,238.3,287.9,347.1,419.9,493.8,571.4,595.5,687.4,772.8,809.1,974.6,1026.5,1083.4,1105.5,1176.6,1235.3,1270.5,1305.8,1381.7,1416.2,1448.7,1493.3,1497.3,1848.9,3029.9,3053.4,3056.9,3127.7,3128.0
""",
    rank = 5,
)

entry(
    index = 1,
    label = "OCDC(O)C(F)(F)F",
    molecule = 
"""
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {6,S}
3  F u0 p3 c0 {6,S}
4  O u0 p2 c0 {7,S} {11,S}
5  O u0 p2 c0 {8,S} {10,S}
6  C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
7  C u0 p0 c0 {4,S} {6,S} {8,D}
8  C u0 p0 c0 {5,S} {7,D} {9,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72533,0.0203505,0.000168827,-4.9406e-07,4.06505e-10,-118845,12.3752], Tmin=(10,'K'), Tmax=(429.884,'K')),
            NASAPolynomial(coeffs=[5.50532,0.040313,-2.82749e-05,9.25236e-09,-1.13776e-12,-119336,1.36509], Tmin=(429.884,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -230.77 kcal/mol
S298: 86.65 cal/mol/K

Coordinates (Angstoms):
F -1.59331 0.60096 -0.94207
F -1.56645 0.16584 1.16715
F -1.18309 -1.42442 -0.25021
O 0.81402 1.53753 0.09150
O 2.77821 -0.41014 -0.00366
C -0.95961 -0.13263 0.00748
C 0.49302 0.19805 0.00914
C 1.46515 -0.71637 -0.00817
H 1.26121 -1.77755 -0.00863
H 2.84930 0.55550 -0.00274
H 0.24596 2.02727 -0.51581

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 66.5,156.5,184.2,256.2,343.5,371.7,390.5,420.4,498.5,576.8,586.4,639.4,721.8,850.1,906.2,1070.0,1144.4,1167.1,1218.7,1262.6,1324.7,1385.8,1418.5,1773.6,3246.0,3747.1,3785.2
""",
    rank = 5,
)

entry(
    index = 2,
    label = "C#CC(DO)O",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {6,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 C u0 p0 c0 {3,S} {5,T}
5 C u0 p0 c0 {4,T} {7,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90939,0.00553843,8.39435e-05,-1.84571e-07,1.18491e-10,-16550.3,9.10216], Tmin=(10,'K'), Tmax=(540.05,'K')),
            NASAPolynomial(coeffs=[4.49162,0.021058,-1.4246e-05,4.63799e-09,-5.75307e-13,-16902.4,3.97438], Tmin=(540.05,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -29.23 kcal/mol
S298: 70.26 cal/mol/K

Coordinates (Angstoms):
O -1.07410 -1.08951 0.00010
O -1.06841 1.16581 -0.00017
C -0.47410 0.11840 -0.00003
C 0.96529 -0.00648 0.00001
C 2.16555 -0.04704 0.00008
H -2.02837 -0.91601 0.00007
H 3.22794 -0.08362 0.00013

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 196.0,251.7,528.4,600.3,609.8,666.7,712.1,782.0,827.0,1176.0,1370.8,1813.9,2239.5,3494.1,3740.5
""",
    rank = 5,
)

entry(
    index = 3,
    label = "C#CC[C]DO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
3 C u0 p0 c0 {2,S} {5,T}
4 C u1 p0 c0 {1,D} {2,S}
5 C u0 p0 c0 {3,T} {8,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86091,0.0115829,0.000101893,-3.28908e-07,3.12745e-10,27895.3,10.1603], Tmin=(10,'K'), Tmax=(356.529,'K')),
            NASAPolynomial(coeffs=[3.91283,0.025347,-1.63757e-05,5.10676e-09,-6.10596e-13,27800.4,8.68463], Tmin=(356.529,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 59.53 kcal/mol
S298: 75.21 cal/mol/K

Coordinates (Angstoms):
O -1.59375 -0.93090 -0.00005
C -0.08136 1.01026 0.00003
C 1.10997 0.18052 0.00002
C -1.41848 0.23312 0.00001
C 2.06831 -0.54404 -0.00000
H -0.12083 1.67262 -0.87312
H -0.12083 1.67257 0.87323
H 2.92102 -1.17708 -0.00002

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 120.7,143.1,318.3,363.3,636.8,638.3,671.6,756.4,840.0,972.3,1203.4,1269.1,1427.0,1940.1,2233.5,3038.4,3067.6,3502.5
""",
    rank = 5,
)

entry(
    index = 4,
    label = "ODC1OC1(F)F",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 O u0 p2 c0 {5,S} {6,S}
4 O u0 p2 c0 {6,D}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u0 p0 c0 {3,S} {4,D} {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.91019,0.00539157,7.97453e-05,-1.73168e-07,1.08347e-10,-71590.6,9.9872], Tmin=(10,'K'), Tmax=(556.534,'K')),
            NASAPolynomial(coeffs=[4.52544,0.0208649,-1.55822e-05,5.25854e-09,-6.57926e-13,-71967.2,4.61143], Tmin=(556.534,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -138.65 kcal/mol
S298: 71.73 cal/mol/K

Coordinates (Angstoms):
F -1.22081 1.07798 -0.24289
F -1.22081 -1.07798 -0.24289
O 0.31723 -0.00000 1.13418
O 2.07023 0.00000 -0.48243
C -0.48601 0.00000 -0.06739
C 0.96515 -0.00000 -0.07294

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 199.0,347.0,450.1,497.1,655.2,668.7,688.6,815.9,1179.6,1274.2,1351.5,2058.1
""",
    rank = 5,
)

entry(
    index = 5,
    label = "FC1DCC1(F)F",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 C u0 p0 c0 {3,S} {4,S} {6,D}
6 C u0 p0 c0 {4,S} {5,D} {7,S}
7 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90533,0.00560985,9.08669e-05,-1.89954e-07,1.15706e-10,-39564.3,10.133], Tmin=(10,'K'), Tmax=(565.045,'K')),
            NASAPolynomial(coeffs=[4.14369,0.0253568,-1.84551e-05,6.16339e-09,-7.67829e-13,-39933.5,6.09131], Tmin=(565.045,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -74.86 kcal/mol
S298: 72.81 cal/mol/K

Coordinates (Angstoms):
F 1.26553 1.08034 -0.30341
F 1.26556 -1.08017 -0.30390
F -2.02632 0.00014 -0.57808
C 0.53532 -0.00001 0.04938
C -0.90376 -0.00004 0.08406
C -0.32693 -0.00030 1.25602
H -0.37058 -0.00057 2.33171

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 201.7,286.5,390.8,507.7,584.9,629.2,789.4,824.3,858.9,1017.3,1133.1,1185.3,1417.2,1859.5,3281.3
""",
    rank = 5,
)

entry(
    index = 6,
    label = "CC(Br)(O[O])C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  Br u0 p3 c0 {7,S}
2  F  u0 p3 c0 {9,S}
3  F  u0 p3 c0 {9,S}
4  F  u0 p3 c0 {9,S}
5  O  u0 p2 c0 {6,S} {7,S}
6  O  u1 p2 c0 {5,S}
7  C  u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
8  C  u0 p0 c0 {7,S} {10,S} {11,S} {12,S}
9  C  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
10 H  u0 p0 c0 {8,S}
11 H  u0 p0 c0 {8,S}
12 H  u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.34136,0.0575724,-1.91433e-05,-7.6118e-08,7.55928e-11,-83507.6,15.5908], Tmin=(10,'K'), Tmax=(517.298,'K')),
            NASAPolynomial(coeffs=[8.03679,0.0409548,-2.8051e-05,8.94126e-09,-1.07418e-12,-84256.8,-6.51329], Tmin=(517.298,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -159.45 kcal/mol
S298: 100.18 cal/mol/K

Coordinates (Angstoms):
Br 1.72558 -0.06938 -0.09342
F -0.86253 -1.26647 -1.29207
F -2.30985 -0.49726 0.11357
F -0.73965 -1.81823 0.79880
O -0.42156 1.39644 -0.79233
O -1.46411 2.14305 -0.50050
C -0.13687 0.40516 0.24765
C -0.33207 0.94438 1.64776
C -1.02525 -0.82762 -0.04973
H -0.06341 0.17324 2.37078
H -1.37622 1.22692 1.78628
H 0.30314 1.81819 1.79848

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 53.4,87.9,155.0,194.0,224.6,236.2,284.4,301.4,329.9,370.5,433.1,543.9,578.9,607.8,731.0,782.2,865.4,1093.4,1106.7,1129.1,1184.1,1211.0,1243.3,1284.4,1402.2,1474.0,1482.0,3072.6,3159.5,3161.4
""",
    rank = 5,
)

entry(
    index = 7,
    label = "C[CH]C(DO)C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {6,S}
3  F u0 p3 c0 {6,S}
4  O u0 p2 c0 {8,D}
5  C u0 p0 c0 {7,S} {9,S} {10,S} {11,S}
6  C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
7  C u1 p0 c0 {5,S} {8,S} {12,S}
8  C u0 p0 c0 {4,D} {6,S} {7,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54027,0.0452741,-2.15631e-05,-5.25192e-09,5.53733e-12,-87455.4,14.0991], Tmin=(10,'K'), Tmax=(934.271,'K')),
            NASAPolynomial(coeffs=[8.9041,0.0330219,-1.90911e-05,5.25699e-09,-5.58808e-13,-88925.2,-13.9157], Tmin=(934.271,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -168.09 kcal/mol
S298: 92.94 cal/mol/K

Coordinates (Angstoms):
F 1.64211 -0.35556 1.08053
F 1.12210 1.44770 0.00095
F 1.64154 -0.35397 -1.08155
O -0.66704 -1.57638 0.00002
C -2.92395 0.25450 -0.00002
C 1.01017 0.10854 0.00001
C -1.48942 0.62562 0.00003
C -0.46335 -0.36097 0.00005
H -3.43181 0.67946 -0.87635
H -3.04606 -0.82941 -0.00017
H -3.43179 0.67919 0.87646
H -1.20644 1.67215 0.00006

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 16.0,123.8,136.4,196.1,280.2,297.9,358.0,422.0,508.4,578.9,643.0,704.0,766.3,787.0,986.1,995.3,1097.0,1161.9,1203.5,1214.5,1297.6,1383.0,1435.3,1469.6,1491.2,1572.5,3010.2,3051.2,3144.0,3206.0
""",
    rank = 5,
)

entry(
    index = 8,
    label = "OD[C]CC(DO)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 O u0 p2 c0 {5,D}
3 O u0 p2 c0 {6,D}
4 C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5 C u0 p0 c0 {1,S} {2,D} {4,S}
6 C u1 p0 c0 {3,D} {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80867,0.0272005,-1.69173e-05,4.15653e-09,-1.50107e-13,-46546.3,11.3153], Tmin=(10,'K'), Tmax=(1337.46,'K')),
            NASAPolynomial(coeffs=[10.2604,0.0126424,-5.90284e-06,1.31461e-09,-1.13919e-13,-48695.8,-23.2703], Tmin=(1337.46,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -88.12 kcal/mol
S298: 80.29 cal/mol/K

Coordinates (Angstoms):
F -0.82698 1.17244 0.47739
O -1.74784 -0.44002 -0.71921
O 1.89148 0.53977 -0.54914
C 0.25224 -0.90563 0.56594
C -0.89621 -0.08898 0.02591
C 1.62259 -0.43261 0.05732
H 0.29796 -0.83151 1.65770
H 0.12397 -1.95510 0.29751

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 52.8,144.4,155.4,373.2,495.4,579.9,757.1,819.6,856.6,902.5,1130.2,1241.5,1266.8,1423.7,1904.4,1944.0,3068.7,3139.3
""",
    rank = 5,
)

entry(
    index = 9,
    label = "[O]C(DO)O",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 O u1 p2 c0 {4,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97086,0.00159581,4.23066e-05,-7.29624e-08,3.78807e-11,-46086.4,8.41125], Tmin=(10,'K'), Tmax=(620.938,'K')),
            NASAPolynomial(coeffs=[2.60714,0.0173834,-1.27477e-05,4.30843e-09,-5.42128e-13,-46052.1,13.2535], Tmin=(620.938,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -88.60 kcal/mol
S298: 65.22 cal/mol/K

Coordinates (Angstoms):
O 1.24047 -0.28639 0.00001
O -0.89647 -0.93249 -0.00001
O -0.52007 1.15237 0.00000
C -0.05468 -0.00233 0.00000
H 1.73666 0.54601 0.00001

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 486.4,509.1,552.9,761.8,1039.5,1162.6,1283.4,1595.6,3757.0
""",
    rank = 5,
)

entry(
    index = 10,
    label = "[O]OC[C](Br)C(F)(F)F",
    molecule = 
"""
multiplicity 3
1  Br u0 p3 c0 {9,S}
2  F  u0 p3 c0 {8,S}
3  F  u0 p3 c0 {8,S}
4  F  u0 p3 c0 {8,S}
5  O  u0 p2 c0 {6,S} {7,S}
6  O  u1 p2 c0 {5,S}
7  C  u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
8  C  u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
9  C  u1 p0 c0 {1,S} {7,S} {8,S}
10 H  u0 p0 c0 {7,S}
11 H  u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.35318,0.0695369,-0.000119464,1.40995e-07,-7.41888e-11,-59824.2,17.4308], Tmin=(10,'K'), Tmax=(446.687,'K')),
            NASAPolynomial(coeffs=[6.25262,0.0435727,-3.22749e-05,1.08663e-08,-1.35866e-12,-60083.2,5.77934], Tmin=(446.687,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -112.37 kcal/mol
S298: 105.42 cal/mol/K

Coordinates (Angstoms):
Br 0.82331 -1.45274 -0.02264
F -2.23856 -0.78032 -0.36410
F -2.03259 1.37766 -0.36906
F -1.54634 0.23657 1.40607
O 1.20832 2.18570 0.06658
O 2.21812 1.64671 0.68868
C 0.65467 1.27037 -0.99612
C -1.48085 0.23488 0.06737
C -0.06770 0.12460 -0.43067
H 1.50788 0.96930 -1.60259
H -0.01455 1.93277 -1.54673

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 23.4,41.6,81.7,121.7,161.4,252.2,301.9,331.0,421.6,459.8,532.7,576.0,626.0,648.6,712.0,857.2,1064.8,1114.0,1167.6,1177.4,1211.1,1249.6,1330.0,1335.2,1455.7,3094.7,3166.8
""",
    rank = 5,
)

entry(
    index = 11,
    label = "FC1(F)CDCO1",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 O u0 p2 c0 {4,S} {6,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {5,S}
5 C u0 p0 c0 {4,S} {6,D} {7,S}
6 C u0 p0 c0 {3,S} {5,D} {8,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92973,0.00392644,9.03532e-05,-1.63598e-07,8.8608e-11,-48724.4,9.48339], Tmin=(10,'K'), Tmax=(607.082,'K')),
            NASAPolynomial(coeffs=[2.04344,0.033297,-2.40774e-05,8.03352e-09,-1.00128e-12,-48807.6,15.0709], Tmin=(607.082,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -93.13 kcal/mol
S298: 71.11 cal/mol/K

Coordinates (Angstoms):
F -1.13841 1.07317 0.02272
F -1.13840 -1.07319 0.02256
O 0.58517 0.00009 -1.04439
C -0.35474 -0.00000 0.06734
C 0.81746 -0.00007 1.02884
C 1.57957 0.00001 -0.06305
H 0.93466 -0.00017 2.09677
H 2.62153 0.00002 -0.34792

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 237.6,352.8,477.0,514.9,636.5,697.2,750.3,841.7,930.7,986.4,1085.6,1101.0,1232.4,1293.6,1336.9,1639.8,3253.2,3313.2
""",
    rank = 5,
)

entry(
    index = 12,
    label = "[O]OCCDC(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {7,S}
3  O u0 p2 c0 {4,S} {5,S}
4  O u1 p2 c0 {3,S}
5  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
6  C u0 p0 c0 {5,S} {7,D} {10,S}
7  C u0 p0 c0 {1,S} {2,S} {6,D}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77037,0.0339655,-1.4863e-05,-2.56905e-09,2.54298e-12,-39757.7,12.4737], Tmin=(10,'K'), Tmax=(1145.31,'K')),
            NASAPolynomial(coeffs=[10.3071,0.021058,-1.09529e-05,2.71897e-09,-2.62379e-13,-41905.8,-22.7903], Tmin=(1145.31,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -74.05 kcal/mol
S298: 86.24 cal/mol/K

Coordinates (Angstoms):
F 1.75939 1.11874 -0.22665
F 2.33938 -0.95141 -0.13731
O -2.00095 0.39622 -0.45173
O -2.72814 -0.66955 -0.21189
C -0.96137 0.56236 0.57493
C 0.12749 -0.43722 0.40503
C 1.35134 -0.10579 0.02505
H -1.46889 0.46267 1.53725
H -0.60772 1.58520 0.43654
H -0.08444 -1.48330 0.58081

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 56.7,75.5,156.4,219.4,366.5,506.1,571.5,586.1,657.2,828.5,844.9,902.1,1021.4,1137.3,1179.6,1254.1,1296.2,1348.6,1392.0,1472.1,1801.5,3072.6,3142.4,3225.3
""",
    rank = 5,
)

entry(
    index = 13,
    label = "CDC(CO[O])C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {7,S}
3  F u0 p3 c0 {7,S}
4  O u0 p2 c0 {5,S} {6,S}
5  O u1 p2 c0 {4,S}
6  C u0 p0 c0 {4,S} {8,S} {10,S} {11,S}
7  C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
8  C u0 p0 c0 {6,S} {7,S} {9,D}
9  C u0 p0 c0 {8,D} {12,S} {13,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {9,S}
13 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.54178,0.050481,-2.44521e-05,-4.61275e-09,5.26384e-12,-74559.8,14.2711], Tmin=(10,'K'), Tmax=(994.298,'K')),
            NASAPolynomial(coeffs=[10.8878,0.0340307,-1.94012e-05,5.2535e-09,-5.49084e-13,-76668.3,-24.3839], Tmin=(994.298,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -142.06 kcal/mol
S298: 96.13 cal/mol/K

Coordinates (Angstoms):
F 1.47852 -0.84157 1.13925
F 2.19091 0.94044 0.13662
F 1.70754 -0.83137 -1.00828
O -2.41108 -0.32849 -0.49730
O -3.06477 0.06544 0.57653
C -1.07768 -0.77433 -0.16817
C 1.33248 -0.07545 0.04172
C -0.09914 0.37190 -0.10721
C -0.41561 1.65797 -0.17524
H -0.80564 -1.47288 -0.96593
H -1.12570 -1.31226 0.78243
H 0.34897 2.42225 -0.12247
H -1.44381 1.97930 -0.28280

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 42.4,55.9,90.6,182.8,231.5,301.5,343.4,415.8,472.8,513.6,578.9,591.1,668.7,765.5,804.3,915.5,953.9,987.9,1057.5,1143.3,1164.3,1178.0,1208.3,1278.9,1325.2,1384.6,1449.3,1463.3,1737.9,3056.3,3112.0,3177.9,3267.7
""",
    rank = 5,
)

entry(
    index = 14,
    label = "ODC(CC(F)(F)F)C(F)(F)F",
    molecule = 
"""
1  F u0 p3 c0 {9,S}
2  F u0 p3 c0 {9,S}
3  F u0 p3 c0 {9,S}
4  F u0 p3 c0 {10,S}
5  F u0 p3 c0 {10,S}
6  F u0 p3 c0 {10,S}
7  O u0 p2 c0 {11,D}
8  C u0 p0 c0 {9,S} {11,S} {12,S} {13,S}
9  C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
10 C u0 p0 c0 {4,S} {5,S} {6,S} {11,S}
11 C u0 p0 c0 {7,D} {8,S} {10,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.39659,0.0663186,-5.87184e-05,2.51295e-08,-4.19609e-12,-183138,15.7986], Tmin=(10,'K'), Tmax=(1268.36,'K')),
            NASAPolynomial(coeffs=[17.6764,0.0246879,-1.35098e-05,3.4829e-09,-3.46428e-13,-187034,-57.5673], Tmin=(1268.36,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -357.00 kcal/mol
S298: 104.37 cal/mol/K

Coordinates (Angstoms):
F 2.22585 0.62299 1.08318
F 2.84420 -1.14382 -0.00024
F 2.22674 0.62426 -1.08209
F -2.14985 -0.89279 1.08448
F -2.15015 -0.89362 -1.08382
F -2.85373 0.84715 -0.00023
O -0.31278 1.61138 -0.00017
C 0.55572 -0.65202 -0.00087
C 1.97762 -0.11784 0.00000
C -1.96122 -0.12479 0.00001
C -0.50815 0.43028 -0.00035
H 0.41516 -1.29185 0.87617
H 0.41572 -1.29042 -0.87906

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 15.4,40.3,90.9,119.3,186.7,219.4,301.9,331.0,340.1,423.3,490.9,531.7,533.2,556.3,620.4,639.2,734.1,832.7,865.7,927.1,1017.2,1129.1,1177.6,1180.7,1236.3,1275.0,1304.7,1315.6,1395.3,1441.3,1864.5,3066.5,3109.1
""",
    rank = 5,
)

entry(
    index = 15,
    label = "FC(F)(F)C1(Br)CO1",
    molecule = 
"""
1  Br u0 p3 c0 {6,S}
2  F  u0 p3 c0 {8,S}
3  F  u0 p3 c0 {8,S}
4  F  u0 p3 c0 {8,S}
5  O  u0 p2 c0 {6,S} {7,S}
6  C  u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
7  C  u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
8  C  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
9  H  u0 p0 c0 {7,S}
10 H  u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65194,0.0297126,5.76117e-05,-1.73959e-07,1.1988e-10,-87643.3,14.1788], Tmin=(10,'K'), Tmax=(543.533,'K')),
            NASAPolynomial(coeffs=[6.07967,0.0357163,-2.48314e-05,7.95919e-09,-9.57524e-13,-88259.8,0.702931], Tmin=(543.533,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -168.94 kcal/mol
S298: 89.62 cal/mol/K

Coordinates (Angstoms):
Br 1.61583 -0.29476 -0.01088
F -1.18472 -1.24214 -1.07333
F -1.25067 -1.17917 1.08820
F -2.43142 0.21457 -0.06947
O -0.27854 1.66137 0.82735
C -0.11641 0.57367 -0.01397
C -0.27182 1.90643 -0.59732
C -1.26333 -0.43450 -0.01497
H 0.61447 2.40667 -0.97585
H -1.22955 2.20596 -1.01307

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 55.2,158.0,209.8,273.5,311.1,320.4,409.5,458.4,561.0,597.3,687.6,805.1,869.8,1003.5,1066.0,1118.9,1167.4,1218.2,1230.1,1264.7,1401.3,1512.6,3116.9,3220.8
""",
    rank = 5,
)

entry(
    index = 16,
    label = "FC(F)(F)C(Br)DCBr",
    molecule = 
"""
1 Br u0 p3 c0 {7,S}
2 Br u0 p3 c0 {8,S}
3 F  u0 p3 c0 {6,S}
4 F  u0 p3 c0 {6,S}
5 F  u0 p3 c0 {6,S}
6 C  u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
7 C  u0 p0 c0 {1,S} {6,S} {8,D}
8 C  u0 p0 c0 {2,S} {7,D} {9,S}
9 H  u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41437,0.0514458,-5.76023e-05,3.21306e-08,-7.12607e-12,-70985.7,15.372], Tmin=(10,'K'), Tmax=(1064.94,'K')),
            NASAPolynomial(coeffs=[12.1142,0.018768,-1.15739e-05,3.31578e-09,-3.61526e-13,-72838.6,-27.1468], Tmin=(1064.94,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -135.39 kcal/mol
S298: 95.12 cal/mol/K

Coordinates (Angstoms):
Br -0.40788 1.64345 0.00008
Br 2.42053 -0.43190 -0.00009
F -2.51586 -0.45411 1.07878
F -2.51593 -0.45402 -1.07865
F -1.77472 -2.17526 -0.00004
C -1.82598 -0.83655 0.00002
C -0.43501 -0.23814 0.00000
C 0.64053 -1.01848 -0.00007
H 0.53851 -2.09458 -0.00011

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 42.9,108.6,137.2,156.7,252.8,307.3,333.9,483.8,513.3,590.3,619.1,675.2,787.7,851.1,936.7,1197.8,1209.0,1246.9,1270.8,1665.0,3235.6
""",
    rank = 5,
)

entry(
    index = 17,
    label = "C[C]CDC(F)F",
    molecule = 
"""
multiplicity 3
1  F u0 p3 c0 {5,S}
2  F u0 p3 c0 {5,S}
3  C u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {5,D} {6,S} {10,S}
5  C u0 p0 c0 {1,S} {2,S} {4,D}
6  C u2 p0 c0 {3,S} {4,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66732,0.0350149,-2.2938e-05,7.34141e-09,-9.2277e-13,-4836.01,11.7512], Tmin=(10,'K'), Tmax=(2116.67,'K')),
            NASAPolynomial(coeffs=[1.05977,0.0338062,-1.7733e-05,4.33243e-09,-4.05615e-13,-2357.52,29.5335], Tmin=(2116.67,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -4.72 kcal/mol
S298: 83.71 cal/mol/K

Coordinates (Angstoms):
F -1.33427 1.24250 0.00007
F -2.10060 -0.79489 -0.00005
C 2.84651 -0.01681 0.00000
C 0.25309 -0.52609 -0.00003
C -1.02363 -0.03550 -0.00001
C 1.40056 0.22027 0.00002
H 3.33614 0.41695 0.88234
H 3.06745 -1.09643 -0.00006
H 3.33614 0.41704 -0.88228
H 0.31486 -1.61725 -0.00010

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 98.7,139.1,141.7,228.7,319.1,396.8,457.0,599.0,798.9,881.8,940.6,1011.7,1040.4,1220.3,1362.7,1393.3,1444.5,1465.2,1490.6,1579.6,2968.6,3031.2,3040.7,3081.7
""",
    rank = 5,
)

entry(
    index = 18,
    label = "2-BTP",
    molecule = 
"""
1 Br u0 p3 c0 {6,S}
2 F  u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
6 C  u0 p0 c0 {1,S} {5,S} {7,D}
7 C  u0 p0 c0 {6,D} {8,S} {9,S}
8 H  u0 p0 c0 {7,S}
9 H  u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77484,0.0160868,0.00014174,-4.08016e-07,3.27433e-10,-74062.2,13.2383], Tmin=(10,'K'), Tmax=(445.508,'K')),
            NASAPolynomial(coeffs=[5.83701,0.031236,-2.26124e-05,7.53602e-09,-9.36898e-13,-74580,1.20745], Tmin=(445.508,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (203.705,'J/(mol*K)'),
    ),
    reference = 'G4 with m062xd3/jun-cc-pvtz 1D Hindered Rotor',
    referenceType = "Theory",
    shortDesc = """G4 with m062xd3/jun-cc-pvtz 1D Hindered Rotor""",
    longDesc = 
"""
H298: -142.33 kcal/mol
S298: 85.21 cal/mol/K

Coordinates (Angstoms):
Br -1.57319 -0.18934 0.00004
F 2.43159 0.48069 -0.00007
F 1.28800 -1.00397 1.07926
F 1.28794 -1.00402 -1.07928
C 1.28716 -0.21412 -0.00003
C 0.09429 0.71407 -0.00001
C 0.19940 2.03342 -0.00003
H 1.17939 2.49532 -0.00006
H -0.67048 2.67723 -0.00002

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
HinderedRotor
Frequencies (cm^-1) = 167.2,224.4,329.3,335.1,483.3,485.3,585.4,622.9,693.3,738.9,834.8,966.7,1094.6,1197.8,1210.3,1280.9,1427.7,1704.3,3173.2,3266.5
""",
    rank = 5,
)

entry(
    index = 19,
    label = "O[C](C1OO1)C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {8,S}
2  F u0 p3 c0 {8,S}
3  F u0 p3 c0 {8,S}
4  O u0 p2 c0 {5,S} {7,S}
5  O u0 p2 c0 {4,S} {7,S}
6  O u0 p2 c0 {9,S} {11,S}
7  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
8  C u0 p0 c0 {1,S} {2,S} {3,S} {9,S}
9  C u1 p0 c0 {6,S} {7,S} {8,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.47598,0.0482499,-1.71011e-05,-3.11245e-08,2.40524e-11,-87074.8,14.4654], Tmin=(10,'K'), Tmax=(714.569,'K')),
            NASAPolynomial(coeffs=[9.05311,0.0338998,-2.23897e-05,6.84747e-09,-7.91208e-13,-88302.5,-13.5803], Tmin=(714.569,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -167.12 kcal/mol
S298: 94.71 cal/mol/K

Coordinates (Angstoms):
F 1.02732 -0.90909 1.20110
F 0.64800 -1.32077 -0.87866
F 2.15583 0.14651 -0.31612
O -2.01170 -0.49778 0.74134
O -2.11894 -0.40680 -0.74226
O 0.39076 2.04014 0.02930
C -1.50749 0.59424 0.02306
C 0.92779 -0.35005 -0.01437
C -0.06213 0.77342 -0.06437
H -2.06395 1.52921 0.11526
H 1.35365 2.03080 -0.06506

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 27.6,77.2,126.9,156.0,301.6,328.3,364.8,462.5,481.7,509.0,536.1,584.2,644.9,771.5,810.8,845.4,1077.7,1140.2,1146.6,1211.9,1231.5,1265.7,1337.4,1430.2,1497.8,3109.6,3765.9
""",
    rank = 5,
)

entry(
    index = 20,
    label = "FC(F)(F)C1(Br)COO1",
    molecule = 
"""
1  Br u0 p3 c0 {7,S}
2  F  u0 p3 c0 {9,S}
3  F  u0 p3 c0 {9,S}
4  F  u0 p3 c0 {9,S}
5  O  u0 p2 c0 {6,S} {7,S}
6  O  u0 p2 c0 {5,S} {8,S}
7  C  u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
8  C  u0 p0 c0 {6,S} {7,S} {10,S} {11,S}
9  C  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
10 H  u0 p0 c0 {8,S}
11 H  u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51075,0.0482645,-2.48273e-05,-1.07471e-08,1.05429e-11,-80688.2,14.703], Tmin=(10,'K'), Tmax=(830.796,'K')),
            NASAPolynomial(coeffs=[10.0152,0.0311948,-1.97306e-05,5.80396e-09,-6.48752e-13,-82260.6,-18.4304], Tmin=(830.796,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -154.47 kcal/mol
S298: 95.21 cal/mol/K

Coordinates (Angstoms):
Br 1.66816 -0.32570 0.00523
F -0.99339 -1.51615 1.08225
F -2.40726 -0.24935 0.04919
F -1.04576 -1.48575 -1.08748
O -0.39376 1.29487 -1.06768
O -0.49524 2.45052 -0.15474
C -0.15950 0.41841 0.00919
C -0.39822 1.55749 0.98658
C -1.16575 -0.74489 0.00788
H -1.34343 1.49197 1.53265
H 0.42823 1.81971 1.64631

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 52.1,86.6,153.9,198.2,261.5,284.6,313.1,361.6,436.7,551.3,580.6,687.9,795.2,879.5,923.3,964.9,1062.9,1111.9,1141.2,1147.6,1214.2,1244.6,1313.3,1347.6,1499.8,3066.6,3145.2
""",
    rank = 5,
)

entry(
    index = 21,
    label = "CDCC(Br)C(F)(F)F",
    molecule = 
"""
1  Br u0 p3 c0 {5,S}
2  F  u0 p3 c0 {6,S}
3  F  u0 p3 c0 {6,S}
4  F  u0 p3 c0 {6,S}
5  C  u0 p0 c0 {1,S} {6,S} {7,S} {9,S}
6  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
7  C  u0 p0 c0 {5,S} {8,D} {10,S}
8  C  u0 p0 c0 {7,D} {11,S} {12,S}
9  H  u0 p0 c0 {5,S}
10 H  u0 p0 c0 {7,S}
11 H  u0 p0 c0 {8,S}
12 H  u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50005,0.0456366,-1.59264e-05,-1.93709e-08,1.40619e-11,-78474.1,14.5018], Tmin=(10,'K'), Tmax=(781.482,'K')),
            NASAPolynomial(coeffs=[7.69715,0.0365804,-2.23956e-05,6.4955e-09,-7.22198e-13,-79509.6,-7.13973], Tmin=(781.482,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -150.19 kcal/mol
S298: 93.78 cal/mol/K

Coordinates (Angstoms):
Br -1.62869 -0.30169 -0.00156
F 1.02683 -1.74561 -0.70676
F 1.21714 -0.90794 1.27974
F 2.43236 -0.14598 -0.34025
C 0.17112 0.44785 -0.37104
C 1.21529 -0.61601 -0.02402
C 0.36855 1.71364 0.38946
C 0.45943 2.90546 -0.19147
H 0.19970 0.60685 -1.44827
H 0.43526 1.60778 1.46825
H 0.60752 3.80778 0.39093
H 0.38827 3.02673 -1.26816

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 61.7,90.0,153.1,198.5,238.1,295.6,358.3,402.3,531.3,557.7,582.9,703.2,758.5,865.9,965.9,974.3,1031.5,1136.8,1143.9,1205.8,1217.7,1268.9,1319.4,1349.5,1458.9,1706.9,3130.5,3149.0,3179.8,3236.3
""",
    rank = 5,
)

entry(
    index = 22,
    label = "[C]DCC(DO)O",
    molecule = 
"""
1 O u0 p2 c0 {3,S} {7,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 C u0 p0 c0 {3,S} {5,D} {6,S}
5 C u0 p1 c0 {4,D}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87854,0.00930285,7.76064e-05,-2.09523e-07,1.64164e-10,5260.85,9.45532], Tmin=(10,'K'), Tmax=(434.397,'K')),
            NASAPolynomial(coeffs=[3.90628,0.0226157,-1.5216e-05,4.83441e-09,-5.82239e-13,5130.42,7.87112], Tmin=(434.397,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 14.26 kcal/mol
S298: 72.03 cal/mol/K

Coordinates (Angstoms):
O -0.50402 1.22736 -0.00000
O -1.38882 -0.84590 0.00000
C -0.43307 -0.12012 0.00000
C 0.98330 -0.57638 0.00000
C 2.02068 0.21988 0.00000
H 1.16264 -1.65039 0.00000
H -1.44548 1.45839 -0.00000

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 103.0,182.9,450.1,563.6,573.6,622.3,809.9,861.8,964.8,1190.5,1357.2,1711.2,1840.6,3160.6,3748.4
""",
    rank = 5,
)

entry(
    index = 23,
    label = "[O]C[C](Br)C(F)(F)F",
    molecule = 
"""
multiplicity 3
1  Br u0 p3 c0 {8,S}
2  F  u0 p3 c0 {7,S}
3  F  u0 p3 c0 {7,S}
4  F  u0 p3 c0 {7,S}
5  O  u1 p2 c0 {6,S}
6  C  u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
7  C  u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
8  C  u1 p0 c0 {1,S} {6,S} {7,S}
9  H  u0 p0 c0 {6,S}
10 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57778,0.0512759,-5.32752e-05,2.9955e-08,-7.20515e-12,-58923.4,16.7364], Tmin=(10,'K'), Tmax=(900.953,'K')),
            NASAPolynomial(coeffs=[7.78986,0.0325753,-2.21404e-05,6.91656e-09,-8.12342e-13,-59682.3,-3.14518], Tmin=(900.953,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -111.27 kcal/mol
S298: 99.92 cal/mol/K

Coordinates (Angstoms):
Br 1.48150 -0.62786 -0.00877
F -2.38736 0.43710 -0.44276
F -1.55171 -0.47600 1.33263
F -1.45448 -1.51750 -0.55319
O 0.65083 2.52885 0.52112
C 0.05264 1.84692 -0.50391
C -1.36624 -0.30967 0.01253
C -0.06449 0.36442 -0.30087
H 0.68446 2.06480 -1.39277
H -0.93310 2.27730 -0.74597

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 18.6,48.3,121.1,160.6,246.3,320.7,337.6,445.6,521.0,569.5,623.3,664.6,725.2,912.3,1029.1,1113.6,1143.7,1157.6,1205.1,1304.4,1338.6,1357.0,2868.0,2986.2
""",
    rank = 5,
)

entry(
    index = 24,
    label = "FC(F)(F)C1(Br)CC1(F)F",
    molecule = 
"""
1  Br u0 p3 c0 {7,S}
2  F  u0 p3 c0 {9,S}
3  F  u0 p3 c0 {9,S}
4  F  u0 p3 c0 {10,S}
5  F  u0 p3 c0 {10,S}
6  F  u0 p3 c0 {10,S}
7  C  u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
8  C  u0 p0 c0 {7,S} {9,S} {11,S} {12,S}
9  C  u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
10 C  u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
11 H  u0 p0 c0 {8,S}
12 H  u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.44797,0.0481355,3.03546e-05,-1.47458e-07,1.05445e-10,-119500,15.2273], Tmin=(10,'K'), Tmax=(571.819,'K')),
            NASAPolynomial(coeffs=[8.26845,0.0427771,-2.99883e-05,9.63379e-09,-1.15871e-12,-120515,-9.38885], Tmin=(571.819,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -231.13 kcal/mol
S298: 98.31 cal/mol/K

Coordinates (Angstoms):
Br 1.76275 -0.27513 -0.05612
F 0.29127 2.41870 -0.40406
F -1.77066 1.70622 -0.52596
F -0.95956 -1.37423 -1.34776
F -0.61416 -2.16033 0.63489
F -2.26061 -0.80899 0.28653
C -0.09055 0.10784 0.26608
C -0.47681 1.02521 1.43848
C -0.57692 1.51055 0.03853
C -0.99022 -1.07566 -0.04834
H -1.39590 0.77477 1.95586
H 0.33021 1.41476 2.04700

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 51.9,129.9,155.4,159.6,183.2,299.6,318.9,327.5,414.4,434.5,493.6,542.1,576.7,666.4,712.8,807.8,837.2,911.4,1008.3,1058.8,1062.3,1099.6,1192.6,1218.8,1279.0,1324.7,1392.3,1477.1,3147.5,3248.0
""",
    rank = 5,
)

entry(
    index = 25,
    label = "ODCC(DO)C(F)(F)F",
    molecule = 
"""
1 F u0 p3 c0 {6,S}
2 F u0 p3 c0 {6,S}
3 F u0 p3 c0 {6,S}
4 O u0 p2 c0 {7,D}
5 O u0 p2 c0 {8,D}
6 C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
7 C u0 p0 c0 {4,D} {6,S} {8,S}
8 C u0 p0 c0 {5,D} {7,S} {9,S}
9 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56166,0.0423326,-3.73194e-05,1.52697e-08,-2.17031e-12,-106891,12.1999], Tmin=(10,'K'), Tmax=(1034.81,'K')),
            NASAPolynomial(coeffs=[10.6164,0.0198542,-1.16816e-05,3.22742e-09,-3.42048e-13,-108608,-23.3162], Tmin=(1034.81,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -207.17 kcal/mol
S298: 86.60 cal/mol/K

Coordinates (Angstoms):
F -0.71415 -0.97534 -1.08564
F -0.71420 -0.97516 1.08579
F -1.92002 0.45827 -0.00007
O 0.26867 1.97690 -0.00008
O 2.05122 -0.99647 0.00006
C -0.76971 -0.20057 0.00001
C 0.42591 0.78801 -0.00004
C 1.83586 0.18312 -0.00004
H 2.62392 0.96326 -0.00012

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 56.2,112.3,157.5,205.1,277.3,386.3,494.5,501.2,541.0,629.9,681.7,769.7,1012.4,1108.6,1205.3,1238.6,1318.3,1370.9,1830.3,1846.7,2941.4
""",
    rank = 5,
)

entry(
    index = 26,
    label = "FC[C](CBr)C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  Br u0 p3 c0 {7,S}
2  F  u0 p3 c0 {6,S}
3  F  u0 p3 c0 {8,S}
4  F  u0 p3 c0 {8,S}
5  F  u0 p3 c0 {8,S}
6  C  u0 p0 c0 {2,S} {9,S} {10,S} {11,S}
7  C  u0 p0 c0 {1,S} {9,S} {12,S} {13,S}
8  C  u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
9  C  u1 p0 c0 {6,S} {7,S} {8,S}
10 H  u0 p0 c0 {6,S}
11 H  u0 p0 c0 {6,S}
12 H  u0 p0 c0 {7,S}
13 H  u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.25923,0.0777666,-0.000193074,4.03784e-07,-3.52577e-10,-95003.3,17.8571], Tmin=(10,'K'), Tmax=(337.605,'K')),
            NASAPolynomial(coeffs=[4.66177,0.0517913,-3.60864e-05,1.16799e-08,-1.42218e-12,-95044.7,13.4034], Tmin=(337.605,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -182.13 kcal/mol
S298: 107.10 cal/mol/K

Coordinates (Angstoms):
Br 2.03699 -0.38829 0.15227
F -0.26067 2.80421 -0.13213
F -2.87565 -0.31209 -0.29944
F -1.58458 -0.97940 1.29761
F -1.30044 -1.74304 -0.71117
C -0.90733 1.75105 0.47196
C 0.52268 0.29490 -1.08014
C -1.60481 -0.64996 -0.00777
C -0.67457 0.48858 -0.29395
H -0.52559 1.65433 1.50022
H -1.98103 1.97031 0.53075
H 0.93323 1.22079 -1.46885
H 0.45498 -0.48976 -1.82600

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 15.4,42.7,62.2,111.5,169.3,234.9,297.4,357.2,380.1,403.6,477.7,573.3,594.7,650.3,775.5,866.4,976.4,1017.4,1098.8,1139.8,1155.8,1162.4,1204.2,1252.7,1323.7,1346.6,1419.7,1474.9,1485.9,2988.0,3048.7,3145.8,3228.0
""",
    rank = 5,
)

entry(
    index = 27,
    label = "[CH2]C1(C(F)(F)F)OO1",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {7,S}
3  F u0 p3 c0 {7,S}
4  O u0 p2 c0 {5,S} {6,S}
5  O u0 p2 c0 {4,S} {6,S}
6  C u0 p0 c0 {4,S} {5,S} {7,S} {8,S}
7  C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
8  C u1 p0 c0 {6,S} {9,S} {10,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72625,0.0195489,0.000168421,-4.86534e-07,3.90196e-10,-66023.4,13.1069], Tmin=(10,'K'), Tmax=(446.908,'K')),
            NASAPolynomial(coeffs=[6.31983,0.0370683,-2.70968e-05,9.0701e-09,-1.13003e-12,-66662,-1.86771], Tmin=(446.908,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -125.86 kcal/mol
S298: 87.67 cal/mol/K

Coordinates (Angstoms):
F -1.31105 0.53247 -1.08313
F -1.31110 0.53265 1.08302
F -1.07640 -1.32791 0.00010
O 1.46916 -0.75439 -0.74293
O 1.46918 -0.75440 0.74291
C 0.74532 0.18792 0.00001
C -0.77003 -0.04165 0.00001
C 1.19605 1.56873 0.00001
H 0.49138 2.38800 -0.00017
H 2.26087 1.75740 0.00012

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 43.3,205.9,214.9,220.7,324.2,368.0,386.7,466.1,541.0,573.0,604.2,622.0,763.2,830.3,859.5,984.3,1143.0,1197.5,1249.7,1327.3,1399.4,1451.4,3181.0,3302.7
""",
    rank = 5,
)

entry(
    index = 28,
    label = "FC(F)(Br)[CH]Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {5,S}
2 Br u0 p3 c0 {6,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
6 C  u1 p0 c0 {2,S} {5,S} {7,S}
7 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66498,0.0278786,5.79488e-05,-2.69438e-07,2.58041e-10,-31686.2,15.5382], Tmin=(10,'K'), Tmax=(416.954,'K')),
            NASAPolynomial(coeffs=[7.19457,0.0212386,-1.60904e-05,5.51868e-09,-6.99578e-13,-32217.1,-1.23985], Tmin=(416.954,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -58.14 kcal/mol
S298: 90.28 cal/mol/K

Coordinates (Angstoms):
Br -1.80701 -0.71906 -0.00485
Br 2.13377 -0.30299 0.01484
F -1.18036 1.86756 -0.56827
F -0.27115 1.14068 1.26529
C -0.51612 0.85301 -0.00826
C 0.68182 0.51145 -0.78484
H 0.63255 0.51079 -1.86424

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 49.0,156.7,248.7,275.0,282.7,367.8,471.0,566.0,656.1,760.5,925.5,1147.0,1263.0,1309.4,3242.4
""",
    rank = 5,
)

entry(
    index = 29,
    label = "FC(F)(F)C1DCC1(F)F",
    molecule = 
"""
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {6,S}
3  F u0 p3 c0 {7,S}
4  F u0 p3 c0 {7,S}
5  F u0 p3 c0 {7,S}
6  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
7  C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
8  C u0 p0 c0 {6,S} {7,S} {9,D}
9  C u0 p0 c0 {6,S} {8,D} {10,S}
10 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61299,0.036083,2.56013e-05,-9.93123e-08,6.214e-11,-99567.9,13.6182], Tmin=(10,'K'), Tmax=(646.076,'K')),
            NASAPolynomial(coeffs=[7.77029,0.0337741,-2.34351e-05,7.41763e-09,-8.79094e-13,-100594,-8.40665], Tmin=(646.076,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -192.42 kcal/mol
S298: 90.10 cal/mol/K

Coordinates (Angstoms):
F -2.15370 -0.41737 1.08275
F -2.15369 -0.41780 -1.08259
F 1.55883 -0.81245 -1.08133
F 1.55880 -0.81216 1.08157
F 2.14876 0.96779 -0.00011
C -1.52957 0.08644 -0.00002
C 1.30663 -0.06928 0.00002
C -0.10906 0.39153 -0.00007
C -0.93132 1.41496 -0.00028
H -1.05094 2.48612 -0.00048

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 31.1,103.7,119.8,292.4,304.5,412.1,442.3,512.5,512.8,559.4,658.0,664.1,769.4,848.6,851.4,982.0,1121.4,1154.3,1202.5,1210.0,1269.7,1384.4,1804.6,3271.9
""",
    rank = 5,
)

entry(
    index = 30,
    label = "FC(F)(F)C(Br)[CH]CBr",
    molecule = 
"""
multiplicity 2
1  Br u0 p3 c0 {6,S}
2  Br u0 p3 c0 {8,S}
3  F  u0 p3 c0 {7,S}
4  F  u0 p3 c0 {7,S}
5  F  u0 p3 c0 {7,S}
6  C  u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
7  C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
8  C  u0 p0 c0 {2,S} {9,S} {11,S} {12,S}
9  C  u1 p0 c0 {6,S} {8,S} {13,S}
10 H  u0 p0 c0 {6,S}
11 H  u0 p0 c0 {8,S}
12 H  u0 p0 c0 {8,S}
13 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.57013,0.0527284,0.000315976,-2.72188e-06,5.93007e-09,-70455.3,17.4466], Tmin=(10,'K'), Tmax=(173,'K')),
            NASAPolynomial(coeffs=[5.35056,0.0525668,-3.81498e-05,1.28058e-08,-1.60719e-12,-70578.3,10.2073], Tmin=(173,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -133.07 kcal/mol
S298: 108.84 cal/mol/K

Coordinates (Angstoms):
Br 0.72417 1.65138 -0.02195
Br -2.95886 -0.12783 0.04606
F 2.39203 -2.08554 -0.33906
F 2.43638 -0.70011 1.32285
F 3.20458 -0.10295 -0.61074
C 0.84703 -0.33415 -0.40690
C 2.24830 -0.79391 0.00475
C -1.45663 -1.46220 -0.34302
C -0.21580 -1.05359 0.29378
H 0.76792 -0.39199 -1.49153
H -1.86683 -2.38332 0.06459
H -1.41791 -1.49274 -1.42966
H -0.10346 -1.19582 1.36332

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 26.3,44.0,63.9,116.5,153.7,202.2,264.4,300.7,359.0,404.7,442.5,520.8,553.5,612.5,687.2,733.2,825.4,893.6,1036.7,1115.6,1126.8,1153.9,1194.7,1201.5,1235.0,1268.2,1328.9,1436.1,1484.8,3111.9,3134.3,3181.4,3200.3
""",
    rank = 5,
)

entry(
    index = 31,
    label = "FC(F)[CH]Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {5,S}
2 F  u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 C  u1 p0 c0 {1,S} {4,S} {7,S}
6 H  u0 p0 c0 {4,S}
7 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.74775,0.023088,-7.57064e-06,-1.11776e-08,7.98199e-12,-34307.6,13.5997], Tmin=(10,'K'), Tmax=(769.006,'K')),
            NASAPolynomial(coeffs=[5.91513,0.018432,-1.1397e-05,3.32994e-09,-3.72307e-13,-34836.7,2.44035], Tmin=(769.006,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -64.09 kcal/mol
S298: 82.29 cal/mol/K

Coordinates (Angstoms):
Br 1.44062 0.01038 -0.04528
F -2.50161 -0.81016 -0.10795
F -1.78061 1.23445 0.20443
C -1.43989 0.01202 -0.29927
C -0.26674 -0.55590 0.41876
H -1.26231 0.13117 -1.37494
H -0.37976 -1.04989 1.37464

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 46.3,188.6,308.9,364.6,501.4,576.0,798.9,1048.0,1099.1,1120.5,1217.2,1378.3,1411.8,3051.9,3226.8
""",
    rank = 5,
)

entry(
    index = 32,
    label = "FCDC(CBr)C(F)(F)F",
    molecule = 
"""
1  Br u0 p3 c0 {6,S}
2  F  u0 p3 c0 {7,S}
3  F  u0 p3 c0 {7,S}
4  F  u0 p3 c0 {7,S}
5  F  u0 p3 c0 {9,S}
6  C  u0 p0 c0 {1,S} {8,S} {10,S} {11,S}
7  C  u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
8  C  u0 p0 c0 {6,S} {7,S} {9,D}
9  C  u0 p0 c0 {5,S} {8,D} {12,S}
10 H  u0 p0 c0 {6,S}
11 H  u0 p0 c0 {6,S}
12 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45545,0.0543376,-4.20611e-05,1.36471e-08,-9.43998e-13,-101046,15.8633], Tmin=(10,'K'), Tmax=(1042.79,'K')),
            NASAPolynomial(coeffs=[12.1844,0.0286827,-1.64181e-05,4.45183e-09,-4.65327e-13,-103292,-28.6551], Tmin=(1042.79,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -194.64 kcal/mol
S298: 99.35 cal/mol/K

Coordinates (Angstoms):
Br -2.04217 -0.35076 -0.14790
F 1.01046 -1.56776 -0.78409
F 2.74817 -0.29223 -0.61393
F 1.90511 -1.23104 1.14806
F 0.33002 2.82034 -0.05986
C -0.55513 0.33719 0.98253
C 1.59683 -0.63780 -0.01962
C 0.69961 0.54641 0.21217
C 1.07521 1.73925 -0.24405
H -0.43223 -0.40766 1.76540
H -0.92699 1.26978 1.39692
H 1.99219 1.94037 -0.78358

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 32.5,55.9,113.4,188.2,233.3,258.1,356.0,391.3,414.8,477.0,568.4,582.2,690.3,703.5,797.7,911.6,934.1,1050.9,1168.4,1178.3,1183.5,1225.7,1256.1,1342.8,1382.9,1476.2,1739.7,3123.4,3195.0,3226.4
""",
    rank = 5,
)

entry(
    index = 33,
    label = "ODC[C](O)C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {6,S}
3  F u0 p3 c0 {6,S}
4  O u0 p2 c0 {7,S} {10,S}
5  O u0 p2 c0 {8,D}
6  C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
7  C u1 p0 c0 {4,S} {6,S} {8,S}
8  C u0 p0 c0 {5,D} {7,S} {9,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65028,0.0306988,3.76839e-05,-1.20252e-07,7.83491e-11,-107251,13.2989], Tmin=(10,'K'), Tmax=(585.911,'K')),
            NASAPolynomial(coeffs=[5.98921,0.0346575,-2.34652e-05,7.37048e-09,-8.72982e-13,-107867,0.34642], Tmin=(585.911,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -208.00 kcal/mol
S298: 87.46 cal/mol/K

Coordinates (Angstoms):
F -1.56189 -0.42276 -1.07867
F -1.15377 1.41462 -0.00007
F -1.56180 -0.42258 1.07888
O 0.84402 -1.48803 0.00009
O 2.73443 0.33151 -0.00014
C -0.95923 0.08997 0.00003
C 0.51001 -0.20828 -0.00000
C 1.56969 0.74939 -0.00013
H 1.31864 1.81746 -0.00021
H 1.82806 -1.47530 0.00005

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 39.0,147.0,192.1,291.3,333.5,390.9,418.3,489.7,583.7,615.6,735.7,754.8,875.9,954.0,1089.8,1183.1,1210.2,1266.5,1355.9,1486.8,1499.1,1594.8,3054.6,3491.8
""",
    rank = 5,
)

entry(
    index = 34,
    label = "[C]DCC(F)F",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {6,S}
4 C u0 p0 c0 {3,S} {5,D} {7,S}
5 C u0 p1 c0 {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80945,0.0170374,1.46858e-05,-4.44495e-08,2.58525e-11,-2070.63,9.64016], Tmin=(10,'K'), Tmax=(647.052,'K')),
            NASAPolynomial(coeffs=[4.53088,0.0208185,-1.31836e-05,3.9479e-09,-4.51556e-13,-2336.5,5.14069], Tmin=(647.052,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -0.25 kcal/mol
S298: 72.99 cal/mol/K

Coordinates (Angstoms):
F 1.01443 1.09191 0.07527
F 1.01444 -1.09190 0.07527
C 0.32128 0.00000 -0.32245
C -1.03396 -0.00001 0.33742
C -2.19801 0.00000 -0.24352
H 0.25755 0.00000 -1.41424
H -1.05328 -0.00001 1.43071

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 116.5,168.2,348.3,444.6,582.4,701.0,849.6,1072.8,1115.1,1139.1,1388.7,1399.9,1745.8,3085.3,3118.7
""",
    rank = 5,
)

entry(
    index = 35,
    label = "FC(F)(F)C[CH]CBr",
    molecule = 
"""
multiplicity 2
1  Br u0 p3 c0 {7,S}
2  F  u0 p3 c0 {6,S}
3  F  u0 p3 c0 {6,S}
4  F  u0 p3 c0 {6,S}
5  C  u0 p0 c0 {6,S} {8,S} {9,S} {10,S}
6  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
7  C  u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
8  C  u1 p0 c0 {5,S} {7,S} {13,S}
9  H  u0 p0 c0 {5,S}
10 H  u0 p0 c0 {5,S}
11 H  u0 p0 c0 {7,S}
12 H  u0 p0 c0 {7,S}
13 H  u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.53856,0.0523372,-3.66153e-05,1.17962e-08,-1.30572e-12,-73734.8,16.4236], Tmin=(10,'K'), Tmax=(1310.37,'K')),
            NASAPolynomial(coeffs=[14.2422,0.0255237,-1.26298e-05,3.00627e-09,-2.79866e-13,-77043,-40.0284], Tmin=(1310.37,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -140.41 kcal/mol
S298: 100.66 cal/mol/K

Coordinates (Angstoms):
Br 2.54673 -0.21788 -0.00748
F -3.14778 -1.15789 -0.19013
F -2.96830 0.99634 -0.27631
F -2.02399 -0.10352 1.32939
C -1.04723 -0.28425 -0.82776
C -2.31038 -0.13374 0.01585
C 0.82727 0.87945 0.48433
C -0.08174 0.84082 -0.63237
H -0.59425 -1.24217 -0.54598
H -1.36987 -0.35883 -1.86912
H 1.25119 1.85396 0.70693
H 0.49144 0.35961 1.37678
H 0.01901 1.58518 -1.41376

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 27.8,52.0,99.3,142.2,262.2,320.7,339.9,365.4,445.2,534.9,545.5,582.3,691.7,831.3,862.7,911.5,989.4,1072.0,1125.5,1168.2,1188.4,1218.1,1255.1,1303.0,1351.5,1402.7,1465.8,1494.9,3044.3,3111.2,3133.8,3193.0,3216.7
""",
    rank = 5,
)

entry(
    index = 36,
    label = "[O]OCC(DO)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {6,S}
2 O u0 p2 c0 {4,S} {5,S}
3 O u0 p2 c0 {6,D}
4 O u1 p2 c0 {2,S}
5 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6 C u0 p0 c0 {1,S} {3,D} {5,S}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.81447,0.024853,-7.75773e-06,-6.46438e-09,3.7492e-12,-43928,11.2993], Tmin=(10,'K'), Tmax=(1043.58,'K')),
            NASAPolynomial(coeffs=[7.79384,0.0179742,-9.90682e-06,2.59764e-09,-2.63701e-13,-45214.6,-10.2533], Tmin=(1043.58,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -83.00 kcal/mol
S298: 79.57 cal/mol/K

Coordinates (Angstoms):
F 2.01062 -0.46485 0.26950
O -1.49072 -0.27407 -0.48020
O 0.80624 1.32733 -0.23056
O -2.00532 0.37284 0.54643
C -0.23781 -0.87097 -0.12412
C 0.86478 0.16385 -0.04929
H -0.33217 -1.38346 0.83673
H -0.00685 -1.59894 -0.90707

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 76.4,98.6,247.5,386.3,515.5,560.9,661.4,880.9,963.2,1049.8,1144.4,1171.2,1267.9,1371.8,1436.2,1949.5,3069.8,3129.2
""",
    rank = 5,
)

entry(
    index = 37,
    label = "CDC(C(DC)C(F)(F)F)C(F)(F)F",
    molecule = 
"""
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {7,S}
3  F u0 p3 c0 {7,S}
4  F u0 p3 c0 {8,S}
5  F u0 p3 c0 {8,S}
6  F u0 p3 c0 {8,S}
7  C u0 p0 c0 {1,S} {2,S} {3,S} {10,S}
8  C u0 p0 c0 {4,S} {5,S} {6,S} {9,S}
9  C u0 p0 c0 {8,S} {10,S} {11,D}
10 C u0 p0 c0 {7,S} {9,S} {12,D}
11 C u0 p0 c0 {9,D} {13,S} {14,S}
12 C u0 p0 c0 {10,D} {15,S} {16,S}
13 H u0 p0 c0 {11,S}
14 H u0 p0 c0 {11,S}
15 H u0 p0 c0 {12,S}
16 H u0 p0 c0 {12,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.34812,0.0568864,5.65719e-05,-2.02756e-07,1.36645e-10,-151759,15.3741], Tmin=(10,'K'), Tmax=(576.525,'K')),
            NASAPolynomial(coeffs=[7.82678,0.0600585,-4.07814e-05,1.28498e-08,-1.5262e-12,-152845,-8.70218], Tmin=(576.525,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (382.466,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -294.25 kcal/mol
S298: 104.12 cal/mol/K

Coordinates (Angstoms):
F 2.20180 0.79392 -1.08053
F 2.20175 0.79392 1.08056
F 2.87421 -0.94826 0.00003
F -2.87422 0.94826 0.00001
F -2.20176 -0.79391 1.08055
F -2.20179 -0.79392 -1.08054
C 1.96307 0.02922 0.00001
C -1.96307 -0.02922 0.00000
C -0.54152 0.50192 -0.00002
C 0.54152 -0.50191 -0.00002
C -0.36609 1.82645 -0.00004
C 0.36609 -1.82645 -0.00004
H -1.21825 2.49223 -0.00003
H 0.61371 2.28075 -0.00006
H 1.21825 -2.49223 -0.00003
H -0.61371 -2.28075 -0.00006

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 15.8,60.1,94.9,171.0,207.6,216.6,249.3,336.4,371.6,391.7,437.5,440.4,515.7,535.7,563.4,565.8,643.9,666.2,715.0,740.4,765.9,791.1,821.9,941.9,974.4,977.4,1108.2,1163.5,1176.1,1185.3,1202.9,1208.8,1301.1,1399.0,1451.2,1476.8,1669.6,1708.2,3195.8,3196.0,3285.4,3285.5
""",
    rank = 5,
)

entry(
    index = 38,
    label = "[C]1DCC1",
    molecule = 
"""
multiplicity 2
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {6,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.11584,-0.00970435,9.13816e-05,-1.4595e-07,7.65443e-11,61102.4,6.93866], Tmin=(10,'K'), Tmax=(597.139,'K')),
            NASAPolynomial(coeffs=[1.65103,0.019061,-1.16596e-05,3.45687e-09,-3.95038e-13,61178.2,15.7297], Tmin=(597.139,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 124.11 kcal/mol
S298: 60.44 cal/mol/K

Coordinates (Angstoms):
C 0.82850 -0.16705 -0.00001
C -0.76479 -0.34626 -0.00007
C -0.27604 0.83449 0.00010
H 1.37484 -0.38933 -0.91705
H 1.37480 -0.38953 0.91701
H -1.47565 -1.14824 -0.00012

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 659.0,667.6,764.1,894.1,1009.5,1044.8,1080.7,1507.5,1769.0,3063.4,3142.5,3359.8
""",
    rank = 5,
)

entry(
    index = 39,
    label = "[O]OCD[C]C(F)(F)F",
    molecule = 
"""
multiplicity 3
1 F u0 p3 c0 {6,S}
2 F u0 p3 c0 {6,S}
3 F u0 p3 c0 {6,S}
4 O u0 p2 c0 {5,S} {7,S}
5 O u1 p2 c0 {4,S}
6 C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
7 C u0 p0 c0 {4,S} {8,D} {9,S}
8 C u1 p0 c0 {6,S} {7,D}
9 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56325,0.0443457,-3.98092e-05,1.60978e-08,-2.14923e-12,-38082.7,13.6481], Tmin=(10,'K'), Tmax=(1030.34,'K')),
            NASAPolynomial(coeffs=[11.5503,0.0191146,-1.14864e-05,3.213e-09,-3.43078e-13,-40035.2,-26.6115], Tmin=(1030.34,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -70.29 kcal/mol
S298: 90.48 cal/mol/K

Coordinates (Angstoms):
F -1.97983 -0.48925 1.07919
F -1.97980 -0.48923 -1.07922
F -1.43038 1.30906 0.00002
O 2.42067 -0.54121 0.00000
O 3.48201 0.24576 -0.00000
C -1.33720 -0.03406 0.00000
C 1.24017 0.17039 0.00000
C 0.08126 -0.44651 0.00002
H 1.38325 1.24947 -0.00000

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 62.0,100.9,134.3,159.1,314.3,348.6,423.4,496.0,590.2,595.9,685.9,849.9,887.2,1041.8,1162.1,1179.3,1196.2,1205.7,1289.6,1722.0,3146.5
""",
    rank = 5,
)

entry(
    index = 40,
    label = "CDCC(F)(F)O[O]",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {5,S}
2  F u0 p3 c0 {5,S}
3  O u0 p2 c0 {4,S} {5,S}
4  O u1 p2 c0 {3,S}
5  C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6  C u0 p0 c0 {5,S} {7,D} {8,S}
7  C u0 p0 c0 {6,D} {9,S} {10,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71336,0.0242891,6.10834e-05,-1.65846e-07,1.12176e-10,-44647.8,12.0981], Tmin=(10,'K'), Tmax=(530.596,'K')),
            NASAPolynomial(coeffs=[4.7076,0.0355569,-2.38143e-05,7.4701e-09,-8.8692e-13,-45017.4,5.44266], Tmin=(530.596,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -83.86 kcal/mol
S298: 83.39 cal/mol/K

Coordinates (Angstoms):
F -0.54356 0.83809 1.19177
F 0.45080 1.33075 -0.67442
O -1.17124 -0.12922 -0.73704
O -1.80653 -1.10208 -0.12004
C -0.04076 0.33340 0.05904
C 0.94482 -0.75526 0.32969
C 2.20269 -0.69938 -0.08443
H 0.53851 -1.58673 0.89330
H 2.57775 0.14508 -0.65108
H 2.90031 -1.50009 0.13247

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 89.4,117.1,244.6,282.4,352.9,422.1,473.0,563.6,652.1,722.0,783.6,998.2,1007.1,1026.1,1043.6,1192.7,1209.1,1311.5,1326.2,1451.4,1721.5,3162.9,3210.1,3251.3
""",
    rank = 5,
)

entry(
    index = 41,
    label = "[C]DCO",
    molecule = 
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {5,S}
2 C u0 p0 c0 {1,S} {3,D} {4,S}
3 C u2 p0 c0 {2,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.05211,-0.00483582,6.57607e-05,-1.15121e-07,6.54453e-11,48084.2,7.57695], Tmin=(10,'K'), Tmax=(555.637,'K')),
            NASAPolynomial(coeffs=[2.65445,0.0139892,-8.7171e-06,2.62401e-09,-3.0363e-13,48104.2,12.2812], Tmin=(555.637,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 98.29 kcal/mol
S298: 62.11 cal/mol/K

Coordinates (Angstoms):
O -1.03833 -0.13490 -0.00000
C 0.16716 0.43473 0.00005
C 1.35341 -0.32555 -0.00006
H 0.07207 1.52359 0.00018
H -0.88880 -1.09949 -0.00010

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 450.8,512.4,894.6,1111.3,1196.2,1312.8,1474.3,3103.5,3620.7
""",
    rank = 5,
)

entry(
    index = 42,
    label = "[O]OC(Br)(CO)C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  Br u0 p3 c0 {8,S}
2  F  u0 p3 c0 {10,S}
3  F  u0 p3 c0 {10,S}
4  F  u0 p3 c0 {10,S}
5  O  u0 p2 c0 {7,S} {8,S}
6  O  u0 p2 c0 {9,S} {13,S}
7  O  u1 p2 c0 {5,S}
8  C  u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
9  C  u0 p0 c0 {6,S} {8,S} {11,S} {12,S}
10 C  u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
11 H  u0 p0 c0 {9,S}
12 H  u0 p0 c0 {9,S}
13 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.22683,0.0672537,-4.45148e-05,-2.53728e-08,3.53357e-11,-100862,16.1541], Tmin=(10,'K'), Tmax=(593.781,'K')),
            NASAPolynomial(coeffs=[9.60038,0.0426738,-2.87906e-05,9.034e-09,-1.06991e-12,-101942,-13.9972], Tmin=(593.781,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -193.43 kcal/mol
S298: 104.23 cal/mol/K

Coordinates (Angstoms):
Br 1.85071 -0.20903 0.08913
F -0.04711 1.90736 -0.92907
F -1.96599 1.09549 -0.39193
F -0.57125 1.69193 1.15981
O -0.33755 -0.86568 -1.34682
O -2.00914 -1.10095 1.31120
O -1.43811 -1.58392 -1.40035
C -0.09346 -0.29821 -0.02084
C -0.62506 -1.18166 1.12416
C -0.68002 1.13757 -0.04621
H -0.27091 -2.20209 0.92234
H -0.15504 -0.83427 2.04598
H -2.42014 -1.44246 0.50790

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 60.3,66.1,149.0,155.8,188.2,227.0,248.9,295.3,310.7,328.2,369.3,459.4,523.4,547.6,587.3,614.6,760.8,807.6,929.4,1024.7,1085.2,1112.0,1187.3,1219.9,1228.3,1241.7,1281.7,1389.5,1432.9,1477.6,3017.6,3121.3,3792.6
""",
    rank = 5,
)

entry(
    index = 43,
    label = "[CH2]C(Br)C(F)F",
    molecule = 
"""
multiplicity 2
1  Br u0 p3 c0 {4,S}
2  F  u0 p3 c0 {5,S}
3  F  u0 p3 c0 {5,S}
4  C  u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5  C  u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
6  C  u1 p0 c0 {4,S} {9,S} {10,S}
7  H  u0 p0 c0 {4,S}
8  H  u0 p0 c0 {5,S}
9  H  u0 p0 c0 {6,S}
10 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70941,0.026317,6.9159e-05,-2.59811e-07,2.46599e-10,-38435,13.7738], Tmin=(10,'K'), Tmax=(372.139,'K')),
            NASAPolynomial(coeffs=[4.17448,0.0353231,-2.3593e-05,7.4772e-09,-9.00685e-13,-38566.6,10.6869], Tmin=(372.139,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -71.43 kcal/mol
S298: 87.47 cal/mol/K

Coordinates (Angstoms):
Br 1.51244 -0.18624 -0.05170
F -1.49410 -0.82965 1.07083
F -2.57290 -0.11444 -0.69445
C -0.38416 0.63933 -0.41366
C -1.35823 -0.52052 -0.23735
C -0.56692 1.75102 0.47961
H -0.28706 0.90149 -1.46459
H -1.05590 -1.41726 -0.78687
H -0.17613 2.72779 0.22668
H -0.95758 1.58421 1.47518

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 75.9,163.8,227.9,241.0,274.2,348.9,499.6,547.6,675.0,723.1,903.5,1008.5,1062.9,1110.1,1175.0,1194.5,1367.4,1388.7,1410.8,1470.8,3082.3,3151.3,3170.9,3282.8
""",
    rank = 5,
)

entry(
    index = 44,
    label = "[CH]DC1OOC1(F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 O u0 p2 c0 {4,S} {5,S}
4 O u0 p2 c0 {3,S} {6,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u0 p0 c0 {4,S} {5,S} {7,D}
7 C u1 p0 c0 {6,D} {8,S}
8 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84362,0.00974583,0.00012516,-2.93928e-07,1.96433e-10,-14943.4,11.5827], Tmin=(10,'K'), Tmax=(529.046,'K')),
            NASAPolynomial(coeffs=[5.62518,0.028865,-2.14475e-05,7.2529e-09,-9.10441e-13,-15587.9,-0.188253], Tmin=(529.046,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -25.33 kcal/mol
S298: 78.96 cal/mol/K

Coordinates (Angstoms):
F 1.19000 -0.55967 -1.07153
F 1.19013 -0.55965 1.07141
O 0.44188 1.30334 -0.00003
O -1.04403 1.20170 0.00003
C 0.54514 -0.10559 -0.00003
C -0.96122 -0.20213 0.00006
C -1.86694 -1.12272 0.00012
H -2.90589 -1.38384 0.00016

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 132.7,201.1,277.4,440.1,473.0,508.7,602.2,650.2,667.2,726.2,821.6,896.2,972.7,1145.4,1213.0,1317.4,1765.2,3359.5
""",
    rank = 5,
)

entry(
    index = 45,
    label = "[CH2]C(Br)(CF)C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  Br u0 p3 c0 {6,S}
2  F  u0 p3 c0 {7,S}
3  F  u0 p3 c0 {8,S}
4  F  u0 p3 c0 {8,S}
5  F  u0 p3 c0 {8,S}
6  C  u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
7  C  u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
8  C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
9  C  u1 p0 c0 {6,S} {12,S} {13,S}
10 H  u0 p0 c0 {7,S}
11 H  u0 p0 c0 {7,S}
12 H  u0 p0 c0 {9,S}
13 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40529,0.0522084,4.39102e-05,-2.50354e-07,2.31185e-10,-93455.3,15.4483], Tmin=(10,'K'), Tmax=(434.969,'K')),
            NASAPolynomial(coeffs=[6.89943,0.0472402,-3.26325e-05,1.05358e-08,-1.28216e-12,-94016.2,-1.45401], Tmin=(434.969,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -179.09 kcal/mol
S298: 100.56 cal/mol/K

Coordinates (Angstoms):
Br -1.39871 -0.86728 -0.05949
F -1.21833 2.34985 -0.23249
F 1.42527 -0.64059 -1.37040
F 2.48090 0.58029 0.06386
F 1.65430 -1.32263 0.67175
C 0.15057 0.48647 0.29906
C -0.09898 1.67132 -0.63687
C 1.43654 -0.25505 -0.09312
C 0.07745 0.80229 1.70798
H 0.76364 2.34698 -0.57964
H -0.23030 1.33134 -1.66675
H 0.52378 0.14283 2.43988
H -0.57512 1.60130 2.03177

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 66.3,96.4,143.5,170.2,227.3,245.0,267.7,308.1,356.2,379.8,423.9,470.0,571.3,596.5,670.1,704.9,797.0,900.0,1035.4,1093.6,1134.8,1181.9,1207.9,1267.4,1283.6,1320.1,1416.0,1454.4,1504.1,3035.0,3110.7,3177.1,3293.6
""",
    rank = 5,
)

entry(
    index = 46,
    label = "[O]OC(DO)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 O u0 p2 c0 {4,S} {5,S}
3 O u0 p2 c0 {5,D}
4 O u1 p2 c0 {2,S}
5 C u0 p0 c0 {1,S} {2,S} {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92964,0.00448623,6.20575e-05,-1.45434e-07,9.86982e-11,-40867.8,10.2015], Tmin=(10,'K'), Tmax=(509.958,'K')),
            NASAPolynomial(coeffs=[4.25304,0.0157357,-1.15832e-05,3.84885e-09,-4.74388e-13,-41080,7.10146], Tmin=(509.958,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (108.088,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -77.88 kcal/mol
S298: 70.73 cal/mol/K

Coordinates (Angstoms):
F -1.46512 -0.68430 0.00001
O 0.67950 -0.68127 -0.00001
O -0.49340 1.31971 -0.00000
O 1.80146 0.02024 0.00000
C -0.45240 0.14822 0.00000

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 150.6,329.1,524.2,688.3,724.8,899.0,1150.9,1216.9,1983.6
""",
    rank = 5,
)

entry(
    index = 47,
    label = "C[C]C(Br)C(F)(F)F",
    molecule = 
"""
multiplicity 3
1  Br u0 p3 c0 {5,S}
2  F  u0 p3 c0 {6,S}
3  F  u0 p3 c0 {6,S}
4  F  u0 p3 c0 {6,S}
5  C  u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
6  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
7  C  u0 p0 c0 {8,S} {10,S} {11,S} {12,S}
8  C  u2 p0 c0 {5,S} {7,S}
9  H  u0 p0 c0 {5,S}
10 H  u0 p0 c0 {7,S}
11 H  u0 p0 c0 {7,S}
12 H  u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.30509,0.071412,-0.00016349,2.98822e-07,-2.32953e-10,-44698.5,15.973], Tmin=(10,'K'), Tmax=(353.722,'K')),
            NASAPolynomial(coeffs=[5.20792,0.0450168,-3.08747e-05,9.8957e-09,-1.1973e-12,-44802.6,9.20184], Tmin=(353.722,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -82.48 kcal/mol
S298: 101.35 cal/mol/K

Coordinates (Angstoms):
Br -1.70724 -0.15668 0.03661
F 0.83988 -1.96020 -0.04198
F 2.40308 -0.55730 -0.53976
F 1.27159 -0.30529 1.28634
C 0.20555 0.21677 -0.77962
C 1.18096 -0.67516 0.00633
C 0.84395 2.59959 0.26764
C 0.47486 1.60425 -0.73884
H 0.08026 -0.18946 -1.78290
H 0.02304 2.74146 0.98645
H 1.73481 2.29382 0.83489
H 1.05224 3.57036 -0.19410

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 56.6,58.4,93.0,141.7,160.3,204.8,294.3,323.4,446.8,493.5,542.3,599.1,688.9,817.4,886.3,988.8,1023.5,1057.5,1164.1,1204.5,1244.2,1312.0,1381.5,1407.8,1443.6,1450.7,2982.9,3037.0,3084.4,3125.1
""",
    rank = 5,
)

entry(
    index = 48,
    label = "[O]CC([O])(Br)C(F)(F)F",
    molecule = 
"""
multiplicity 3
1  Br u0 p3 c0 {7,S}
2  F  u0 p3 c0 {9,S}
3  F  u0 p3 c0 {9,S}
4  F  u0 p3 c0 {9,S}
5  O  u1 p2 c0 {7,S}
6  O  u1 p2 c0 {8,S}
7  C  u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
8  C  u0 p0 c0 {6,S} {7,S} {10,S} {11,S}
9  C  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
10 H  u0 p0 c0 {8,S}
11 H  u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.26241,0.0672023,-8.20635e-05,5.24769e-08,-1.36834e-11,-74571.3,16.5866], Tmin=(10,'K'), Tmax=(894.412,'K')),
            NASAPolynomial(coeffs=[11.5792,0.0300079,-1.96855e-05,5.98229e-09,-6.87529e-13,-76059,-22.6091], Tmin=(894.412,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -141.57 kcal/mol
S298: 103.32 cal/mol/K

Coordinates (Angstoms):
Br 1.78968 -0.03036 -0.11128
F -0.98638 -0.76889 -1.41801
F -0.65422 -2.01834 0.31868
F -2.32197 -0.64538 0.27864
O -0.31829 0.49142 1.78653
O -1.75751 2.04284 -0.42010
C -0.18260 0.29867 0.57308
C -0.50192 1.77538 -0.27485
C -1.05532 -0.82202 -0.08729
H 0.03702 2.53244 0.32234
H 0.03286 1.63731 -1.23828

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 33.0,74.3,140.4,145.2,209.7,221.7,265.5,291.8,308.3,425.4,483.3,513.7,571.2,641.0,690.5,781.5,825.6,995.2,1138.3,1195.2,1220.2,1231.9,1242.9,1280.4,1466.2,2863.3,2959.1
""",
    rank = 5,
)

entry(
    index = 49,
    label = "CDCC(O[O])C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {7,S}
3  F u0 p3 c0 {7,S}
4  O u0 p2 c0 {5,S} {6,S}
5  O u1 p2 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {10,S}
7  C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
8  C u0 p0 c0 {6,S} {9,D} {11,S}
9  C u0 p0 c0 {8,D} {12,S} {13,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {9,S}
13 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.51597,0.0525938,-3.11268e-05,2.83912e-09,2.45099e-12,-73550.1,13.8099], Tmin=(10,'K'), Tmax=(1042.63,'K')),
            NASAPolynomial(coeffs=[11.7147,0.0323456,-1.81174e-05,4.82888e-09,-4.9776e-13,-75868.9,-29.0071], Tmin=(1042.63,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -139.97 kcal/mol
S298: 95.71 cal/mol/K

Coordinates (Angstoms):
F 1.50367 -1.27487 -0.72806
F 1.83702 0.75681 -0.05334
F 0.98504 -0.69920 1.29705
O -0.87726 1.19158 0.32403
O -0.60489 2.35083 -0.23703
C -0.39609 0.08192 -0.47397
C 1.00891 -0.28339 0.03067
C -1.34543 -1.07544 -0.37567
C -2.55016 -1.02550 0.17753
H -0.28349 0.44776 -1.49928
H -0.96619 -1.99408 -0.81385
H -3.18546 -1.90340 0.20112
H -2.94256 -0.11968 0.62392

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 57.4,69.8,84.4,186.0,217.3,255.0,345.9,357.5,466.7,536.3,570.9,575.8,598.5,725.5,879.7,960.0,980.0,1006.6,1037.4,1120.4,1164.2,1203.0,1215.2,1282.9,1318.2,1324.2,1353.6,1451.0,1719.9,3073.7,3162.1,3178.5,3251.0
""",
    rank = 5,
)

entry(
    index = 50,
    label = "CCDC(O[O])C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {6,S}
3  F u0 p3 c0 {6,S}
4  O u0 p2 c0 {5,S} {8,S}
5  O u1 p2 c0 {4,S}
6  C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
7  C u0 p0 c0 {9,S} {10,S} {11,S} {12,S}
8  C u0 p0 c0 {4,S} {6,S} {9,D}
9  C u0 p0 c0 {7,S} {8,D} {13,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41961,0.055346,-3.8454e-05,9.28856e-09,6.1696e-13,-73587.3,13.5298], Tmin=(10,'K'), Tmax=(1000.77,'K')),
            NASAPolynomial(coeffs=[10.9943,0.0338083,-1.92689e-05,5.23263e-09,-5.49216e-13,-75540.9,-25.2058], Tmin=(1000.77,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -139.96 kcal/mol
S298: 95.15 cal/mol/K

Coordinates (Angstoms):
F -1.62329 0.00410 -1.08248
F -1.62337 0.00456 1.08237
F -1.02110 -1.76323 0.00033
O 0.73557 1.38937 0.00014
O -0.33411 2.16590 -0.00036
C -0.96901 -0.42159 0.00006
C 2.95799 -0.41989 -0.00007
C 0.47865 0.02663 0.00004
C 1.51564 -0.81290 -0.00002
H 3.46276 -0.83799 0.87867
H 3.46266 -0.83786 -0.87894
H 3.09442 0.66161 0.00000
H 1.27875 -1.87020 -0.00002

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 60.3,113.3,134.7,162.5,200.8,216.7,324.1,340.9,377.3,503.8,512.3,604.3,656.8,673.5,774.9,863.0,979.2,1038.9,1060.5,1144.0,1199.0,1206.0,1207.0,1312.1,1331.8,1408.9,1480.5,1482.4,1726.1,3032.0,3079.6,3148.2,3209.3
""",
    rank = 5,
)

entry(
    index = 51,
    label = "[CH2]C(DCC)O[O]",
    molecule = 
"""
multiplicity 3
1  O u0 p2 c0 {2,S} {4,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {5,D} {6,S}
5  C u0 p0 c0 {3,S} {4,D} {10,S}
6  C u1 p0 c0 {4,S} {11,S} {12,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63361,0.032678,8.87767e-06,-3.86733e-08,1.98337e-11,20321.2,12.2311], Tmin=(10,'K'), Tmax=(762.655,'K')),
            NASAPolynomial(coeffs=[4.50069,0.0383718,-2.2464e-05,6.33158e-09,-6.90891e-13,19891.1,6.33024], Tmin=(762.655,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 45.44 kcal/mol
S298: 84.98 cal/mol/K

Coordinates (Angstoms):
O 1.19725 -0.75971 0.00006
O 2.37028 -0.17520 -0.00007
C -2.48802 -0.08014 -0.00002
C 0.06925 0.09855 0.00002
C -1.10612 -0.64074 0.00004
C 0.25718 1.46190 0.00002
H -3.05011 -0.42512 0.87773
H -3.04929 -0.42296 -0.87915
H -2.50378 1.01153 0.00133
H -0.99445 -1.72076 -0.00017
H 1.25625 1.87045 0.00011
H -0.59258 2.12872 -0.00014

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 60.7,86.9,180.8,242.9,372.5,468.0,504.9,561.6,580.2,727.1,769.0,840.6,890.0,1017.0,1066.5,1098.9,1192.1,1228.1,1353.2,1412.2,1454.3,1470.5,1483.4,1517.9,3012.1,3051.8,3122.1,3177.3,3197.8,3303.0
""",
    rank = 5,
)

entry(
    index = 52,
    label = "FC1(F)[C]C1",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5 C u0 p1 c0 {3,S} {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90624,0.00588841,9.08554e-05,-2.04946e-07,1.35751e-10,11532.3,9.69899], Tmin=(10,'K'), Tmax=(517.5,'K')),
            NASAPolynomial(coeffs=[4.11155,0.0236024,-1.64341e-05,5.33953e-09,-6.53013e-13,11252.6,6.34668], Tmin=(517.5,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 26.67 kcal/mol
S298: 71.94 cal/mol/K

Coordinates (Angstoms):
F 0.88541 1.10651 -0.05268
F 0.88542 -1.10651 -0.05268
C 0.13583 -0.00000 0.01310
C -1.21365 -0.00000 -0.52986
C -1.03192 -0.00000 0.98989
H -1.63953 -0.91350 -0.94524
H -1.63953 0.91350 -0.94524

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 90.5,253.8,443.5,529.6,548.2,705.7,774.1,911.1,989.0,1066.5,1227.3,1304.3,1455.7,3088.0,3165.6
""",
    rank = 5,
)

entry(
    index = 53,
    label = "ODC([CH]C(F)(F)F)C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {8,S}
2  F u0 p3 c0 {8,S}
3  F u0 p3 c0 {8,S}
4  F u0 p3 c0 {9,S}
5  F u0 p3 c0 {9,S}
6  F u0 p3 c0 {9,S}
7  O u0 p2 c0 {11,D}
8  C u0 p0 c0 {1,S} {2,S} {3,S} {10,S}
9  C u0 p0 c0 {4,S} {5,S} {6,S} {11,S}
10 C u1 p0 c0 {8,S} {11,S} {12,S}
11 C u0 p0 c0 {7,D} {9,S} {10,S}
12 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.34362,0.0678013,-6.67891e-05,3.18699e-08,-5.97502e-12,-161151,17.5981], Tmin=(10,'K'), Tmax=(1261.3,'K')),
            NASAPolynomial(coeffs=[17.517,0.022853,-1.33345e-05,3.61619e-09,-3.74921e-13,-164726,-54.0703], Tmin=(1261.3,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -313.33 kcal/mol
S298: 107.62 cal/mol/K

Coordinates (Angstoms):
F 2.78675 -1.20999 -0.00501
F 2.26085 0.57511 1.09999
F 2.30561 0.61592 -1.06316
F -2.79440 0.71004 -0.56693
F -2.33250 -0.35454 1.26045
F -2.02991 -1.31636 -0.65589
O -0.32699 1.62107 -0.01218
C 1.99262 -0.13183 -0.00130
C -1.95328 -0.14406 -0.00603
C -0.50499 0.41158 -0.02975
C 0.54999 -0.55752 -0.03913
H 0.34231 -1.61915 -0.07032

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 7.5,33.5,74.2,118.7,197.3,235.1,301.4,327.8,360.6,424.7,491.2,522.5,531.9,561.2,605.2,652.4,738.7,776.4,864.2,886.2,1084.9,1184.2,1187.9,1191.1,1235.7,1263.6,1305.3,1430.6,1616.7,3230.4
""",
    rank = 5,
)

entry(
    index = 54,
    label = "[O]OCC(DO)C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {8,S}
2  F u0 p3 c0 {8,S}
3  F u0 p3 c0 {8,S}
4  O u0 p2 c0 {6,S} {7,S}
5  O u0 p2 c0 {9,D}
6  O u1 p2 c0 {4,S}
7  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
8  C u0 p0 c0 {1,S} {2,S} {3,S} {9,S}
9  C u0 p0 c0 {5,D} {7,S} {8,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79196,0.029574,0.000603018,-5.73759e-06,1.62657e-08,-93767.3,10.3537], Tmin=(10,'K'), Tmax=(124.064,'K')),
            NASAPolynomial(coeffs=[4.37485,0.0465429,-3.45236e-05,1.16931e-08,-1.47259e-12,-93809.3,7.64881], Tmin=(124.064,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -180.28 kcal/mol
S298: 89.44 cal/mol/K

Coordinates (Angstoms):
F 1.45931 -0.75323 1.18762
F 2.15476 0.99242 0.10470
F 1.72455 -0.84614 -0.96191
O -2.43894 -0.36147 -0.45722
O -0.43422 1.52676 -0.28280
O -2.97568 0.21913 0.59799
C -1.10605 -0.79599 -0.17344
C 1.34791 -0.04937 0.05087
C -0.13252 0.37827 -0.15396
H -0.83022 -1.49610 -0.96822
H -1.08262 -1.31416 0.78994

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 20.3,54.7,98.8,170.2,218.8,279.0,322.6,417.3,483.6,505.6,569.2,612.1,725.2,812.4,938.6,1014.0,1035.4,1165.9,1178.4,1231.6,1264.0,1312.4,1365.5,1435.9,1874.8,3059.8,3117.6
""",
    rank = 5,
)

entry(
    index = 55,
    label = "CDC[C]C",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
2  C u0 p0 c0 {3,D} {4,S} {8,S}
3  C u0 p0 c0 {2,D} {9,S} {10,S}
4  C u2 p0 c0 {1,S} {2,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82318,0.0162321,2.56053e-05,-4.32653e-08,1.82895e-11,41938.3,9.29681], Tmin=(10,'K'), Tmax=(797.605,'K')),
            NASAPolynomial(coeffs=[2.27487,0.0315908,-1.75603e-05,4.75089e-09,-5.02135e-13,41943.8,14.9022], Tmin=(797.605,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 87.33 kcal/mol
S298: 72.94 cal/mol/K

Coordinates (Angstoms):
C 1.92713 -0.01864 -0.00000
C -0.69046 0.36750 0.00000
C -1.96186 -0.17733 -0.00000
C 0.49152 -0.31589 0.00000
H 2.43202 -0.43517 0.88177
H 2.10638 1.06880 0.00004
H 2.43200 -0.43510 -0.88181
H -0.61578 1.46306 0.00000
H -2.11206 -1.25063 -0.00000
H -2.84057 0.45524 -0.00000

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 132.1,195.7,220.0,472.3,552.0,770.4,842.2,903.5,988.3,1013.4,1097.0,1223.8,1321.5,1392.6,1446.8,1466.4,1499.2,1502.0,2968.1,3021.6,3033.6,3045.7,3158.1,3255.1
""",
    rank = 5,
)

entry(
    index = 56,
    label = "CCDC1CDCC1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,D} {6,S}
4  C u0 p0 c0 {2,S} {3,D} {12,S}
5  C u0 p0 c0 {1,S} {6,D} {13,S}
6  C u0 p0 c0 {3,S} {5,D} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94804,0.00334669,0.000159119,-3.05646e-07,1.9211e-10,24065.9,10.407], Tmin=(10,'K'), Tmax=(408.419,'K')),
            NASAPolynomial(coeffs=[-1.43878,0.0560832,-3.44881e-05,1.02534e-08,-1.17849e-12,24506.1,31.5738], Tmin=(408.419,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 52.23 kcal/mol
S298: 76.79 cal/mol/K

Coordinates (Angstoms):
C 0.78313 1.08282 -0.00002
C -2.40089 0.28246 0.00001
C 0.04894 -0.27691 0.00000
C -1.22795 -0.65183 0.00002
C 2.04141 0.21733 -0.00002
C 1.35774 -0.94407 0.00000
H 0.62758 1.70184 0.89075
H 0.62757 1.70182 -0.89079
H -3.03873 0.12318 -0.87894
H -2.08210 1.32858 0.00000
H -3.03872 0.12320 0.87897
H -1.45238 -1.71769 0.00003
H 3.09434 0.46846 -0.00002
H 1.64813 -1.98815 0.00001

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 158.0,191.0,193.8,314.6,484.7,493.2,682.2,772.8,851.9,881.9,945.7,954.8,968.9,1017.1,1058.3,1059.2,1097.1,1121.8,1156.6,1210.0,1320.8,1346.3,1409.5,1471.2,1478.5,1490.9,1592.5,1773.5,3011.8,3030.8,3055.0,3073.9,3102.9,3133.2,3189.6,3224.2
""",
    rank = 5,
)

entry(
    index = 57,
    label = "CD[C]C1OO1",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
4 C u0 p0 c0 {5,D} {7,S} {8,S}
5 C u1 p0 c0 {3,S} {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.85796,0.0129864,4.04035e-05,-8.20453e-08,4.45545e-11,34431.8,10.0398], Tmin=(10,'K'), Tmax=(630.79,'K')),
            NASAPolynomial(coeffs=[3.46732,0.0261664,-1.6389e-05,4.87579e-09,-5.55447e-13,34268.1,10.0566], Tmin=(630.79,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 72.28 kcal/mol
S298: 73.62 cal/mol/K

Coordinates (Angstoms):
O -1.38997 -0.74510 -0.12549
O -1.38997 0.74510 -0.12549
C -0.32850 -0.00000 0.38359
C 2.21125 0.00000 -0.01138
C 0.94141 -0.00001 -0.32945
H -0.24817 0.00000 1.47937
H 2.99991 -0.00000 -0.75936
H 2.54282 0.00001 1.03127

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 98.4,229.1,324.1,474.8,585.8,813.7,877.5,900.2,927.1,1076.2,1129.6,1290.8,1370.3,1432.3,1750.5,3018.5,3059.1,3172.6
""",
    rank = 5,
)

entry(
    index = 58,
    label = "FC(F)[C]DCBr",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {5,S}
2 F  u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
5 C  u0 p0 c0 {1,S} {6,D} {8,S}
6 C  u1 p0 c0 {4,S} {5,D}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72704,0.0316281,-2.49766e-05,9.60935e-09,-1.45072e-12,-15849.7,14.078], Tmin=(10,'K'), Tmax=(1700.2,'K')),
            NASAPolynomial(coeffs=[10.1044,0.0140696,-7.23162e-06,1.76755e-09,-1.67687e-13,-17649,-18.9877], Tmin=(1700.2,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -26.90 kcal/mol
S298: 86.86 cal/mol/K

Coordinates (Angstoms):
Br -1.77080 0.00082 -0.22274
F 2.63569 1.09575 -0.19476
F 2.63581 -1.09423 -0.20272
C 1.84192 0.00094 -0.26039
C -0.38055 -0.00426 1.14969
C 0.87723 -0.00317 0.85478
H 1.32007 0.00444 -1.23012
H -0.81730 -0.00786 2.13883

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 30.3,87.2,196.0,326.6,486.9,528.5,549.6,643.5,764.5,929.5,1117.6,1132.2,1167.4,1356.2,1368.7,1778.1,2998.5,3224.8
""",
    rank = 5,
)

entry(
    index = 59,
    label = "[CH]DC(Br)C(F)(F)F",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {6,S}
2 F  u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
6 C  u0 p0 c0 {1,S} {5,S} {7,D}
7 C  u1 p0 c0 {6,D} {8,S}
8 H  u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72592,0.0201018,0.000132516,-4.29359e-07,3.6634e-10,-44612.1,13.924], Tmin=(10,'K'), Tmax=(435.025,'K')),
            NASAPolynomial(coeffs=[7.27072,0.0258873,-1.97685e-05,6.8158e-09,-8.66639e-13,-45283.7,-4.4011], Tmin=(435.025,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (178.761,'J/(mol*K)'),
    ),
    reference = 'G4 with m062xd3/jun-cc-pvtz 1D Hindered Rotor',
    referenceType = "Theory",
    shortDesc = """G4 with m062xd3/jun-cc-pvtz 1D Hindered Rotor""",
    longDesc = 
"""
H298: -83.69 kcal/mol
S298: 87.36 cal/mol/K

Coordinates (Angstoms):
Br 1.57356 -0.19069 0.00000
F -1.32419 -0.94888 1.07904
F -2.45056 0.55013 0.00009
F -1.32428 -0.94874 -1.07914
C -1.32177 -0.16119 0.00000
C -0.11788 0.75637 0.00001
C -0.16494 2.04917 0.00000
H 0.44414 2.93536 -0.00000

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
HinderedRotor
Frequencies (cm^-1) = 155.2,219.2,291.0,301.3,472.2,478.2,580.6,632.5,666.1,718.4,741.3,873.9,1198.6,1219.6,1248.8,1709.7,3321.5
""",
    rank = 5,
)

entry(
    index = 60,
    label = "[CH2]C(Br)(O[O])C(F)(F)F",
    molecule = 
"""
multiplicity 3
1  Br u0 p3 c0 {7,S}
2  F  u0 p3 c0 {8,S}
3  F  u0 p3 c0 {8,S}
4  F  u0 p3 c0 {8,S}
5  O  u0 p2 c0 {6,S} {7,S}
6  O  u1 p2 c0 {5,S}
7  C  u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
8  C  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
9  C  u1 p0 c0 {7,S} {10,S} {11,S}
10 H  u0 p0 c0 {9,S}
11 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4155,0.0495174,7.38312e-05,-3.70042e-07,3.49602e-10,-57769,15.9283], Tmin=(10,'K'), Tmax=(427.391,'K')),
            NASAPolynomial(coeffs=[8.89104,0.0384697,-2.84789e-05,9.61656e-09,-1.20594e-12,-58604.2,-10.1287], Tmin=(427.391,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -108.24 kcal/mol
S298: 101.04 cal/mol/K

Coordinates (Angstoms):
Br 1.53420 -0.64383 -0.05535
F -1.29194 -0.85317 -1.33470
F -1.43620 -1.45598 0.74133
F -2.49037 0.29892 0.04200
O -0.15750 1.51996 -0.70377
O 0.56949 2.55882 -0.37175
C -0.16430 0.48091 0.28840
C -1.36715 -0.41404 -0.08626
C -0.12748 0.91878 1.65951
H -0.43478 0.23123 2.43440
H 0.36214 1.85079 1.89935

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 65.5,83.3,141.5,191.2,218.0,248.7,281.8,313.7,355.2,389.8,424.0,501.1,571.9,610.8,675.0,687.3,786.9,833.3,1103.4,1154.9,1199.6,1226.7,1257.7,1337.1,1424.5,3191.0,3313.9
""",
    rank = 5,
)

entry(
    index = 61,
    label = "FC1(F)OC1(F)F",
    molecule = 
"""
1 F u0 p3 c0 {6,S}
2 F u0 p3 c0 {6,S}
3 F u0 p3 c0 {7,S}
4 F u0 p3 c0 {7,S}
5 O u0 p2 c0 {6,S} {7,S}
6 C u0 p0 c0 {1,S} {2,S} {5,S} {7,S}
7 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.86803,0.00818545,0.000108116,-2.50383e-07,1.65379e-10,-109579,10.2581], Tmin=(10,'K'), Tmax=(532.564,'K')),
            NASAPolynomial(coeffs=[5.14834,0.0260802,-1.97726e-05,6.70734e-09,-8.39604e-13,-110105,1.22508], Tmin=(532.564,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -213.67 kcal/mol
S298: 74.82 cal/mol/K

Coordinates (Angstoms):
F -1.44083 1.08230 -0.26050
F -1.44083 -1.08228 -0.26057
F 1.44083 1.08230 -0.26051
F 1.44083 -1.08228 -0.26058
O 0.00000 -0.00004 1.18988
C -0.72624 0.00000 -0.01163
C 0.72624 0.00000 -0.01164

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 173.8,227.1,318.9,503.2,509.7,526.8,553.4,699.8,763.8,800.5,1142.6,1176.6,1265.3,1302.2,1618.7
""",
    rank = 5,
)

entry(
    index = 62,
    label = "FC1DC(F)C1",
    molecule = 
"""
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {5,S}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {3,S} {5,D}
5 C u0 p0 c0 {2,S} {3,S} {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94869,0.00307939,7.47805e-05,-1.45655e-07,8.68807e-11,-6470.71,8.67605], Tmin=(10,'K'), Tmax=(539.608,'K')),
            NASAPolynomial(coeffs=[2.5013,0.024875,-1.65693e-05,5.21062e-09,-6.23012e-13,-6475.62,13.2731], Tmin=(539.608,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -9.43 kcal/mol
S298: 68.15 cal/mol/K

Coordinates (Angstoms):
F 1.79608 -0.64029 0.00007
F -1.79607 -0.64030 -0.00012
C -0.00001 1.33670 0.00006
C 0.64024 -0.03135 0.00003
C -0.64024 -0.03135 -0.00004
H -0.00007 1.94062 0.91358
H 0.00004 1.94071 -0.91341

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 248.9,295.7,452.6,547.5,792.0,802.3,983.6,1106.8,1120.1,1220.2,1300.3,1535.3,2083.1,3013.8,3075.9
""",
    rank = 5,
)

entry(
    index = 63,
    label = "[O]OC(F)(F)CDCF",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {6,S}
3  F u0 p3 c0 {8,S}
4  O u0 p2 c0 {5,S} {6,S}
5  O u1 p2 c0 {4,S}
6  C u0 p0 c0 {1,S} {2,S} {4,S} {7,S}
7  C u0 p0 c0 {6,S} {8,D} {9,S}
8  C u0 p0 c0 {3,S} {7,D} {10,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.56815,0.038736,-1.05527e-06,-4.98231e-08,3.42986e-11,-67009.3,13.7593], Tmin=(10,'K'), Tmax=(658.258,'K')),
            NASAPolynomial(coeffs=[7.24477,0.0319792,-2.11717e-05,6.51728e-09,-7.58828e-13,-67831,-5.00552], Tmin=(658.258,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -127.81 kcal/mol
S298: 89.85 cal/mol/K

Coordinates (Angstoms):
F 1.19223 -0.68583 1.21310
F 0.42945 -1.48662 -0.65574
F -2.99293 0.51169 0.04751
O 1.53367 0.39728 -0.72161
O 1.80265 1.54214 -0.13260
C 0.57920 -0.37354 0.06621
C -0.69411 0.35692 0.29649
C -1.84579 -0.11892 -0.15348
H -0.62319 1.28600 0.84590
H -1.96180 -1.04141 -0.71142

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 77.4,109.1,177.6,197.6,292.9,379.9,412.0,426.3,524.9,629.0,673.8,861.5,876.1,977.7,995.6,1147.8,1208.4,1217.9,1286.4,1330.5,1354.4,1748.2,3209.3,3231.1
""",
    rank = 5,
)

entry(
    index = 64,
    label = "[CH2]C[C]DO",
    molecule = 
"""
multiplicity 3
1 O u0 p2 c0 {4,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u1 p0 c0 {2,S} {7,S} {8,S}
4 C u1 p0 c0 {1,D} {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92285,0.00807469,0.000134335,-5.94186e-07,9.00227e-10,19130.6,9.24482], Tmin=(10,'K'), Tmax=(166.124,'K')),
            NASAPolynomial(coeffs=[3.23683,0.0245927,-1.48121e-05,4.34469e-09,-4.94261e-13,19153.4,11.323], Tmin=(166.124,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 41.91 kcal/mol
S298: 72.48 cal/mol/K

Coordinates (Angstoms):
O 1.50918 -0.48529 -0.00001
C -0.63742 0.66876 -0.00000
C -1.39994 -0.61199 0.00000
C 0.87836 0.51474 0.00002
H -0.87899 1.30651 -0.86566
H -0.87902 1.30654 0.86562
H -2.48313 -0.60032 -0.00002
H -0.87828 -1.55956 0.00003

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 150.4,189.8,251.3,443.7,619.6,785.3,796.1,978.2,1091.0,1146.3,1299.2,1411.7,1435.2,1928.3,2984.1,2994.5,3161.3,3277.3
""",
    rank = 5,
)

entry(
    index = 65,
    label = "[O]OC(F)(F)[C]DO",
    molecule = 
"""
multiplicity 3
1 F u0 p3 c0 {6,S}
2 F u0 p3 c0 {6,S}
3 O u0 p2 c0 {4,S} {6,S}
4 O u1 p2 c0 {3,S}
5 O u0 p2 c0 {7,D}
6 C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
7 C u1 p0 c0 {5,D} {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6122,0.0343711,-2.17072e-05,-1.5484e-08,1.81845e-11,-41013,12.8259], Tmin=(10,'K'), Tmax=(642.598,'K')),
            NASAPolynomial(coeffs=[7.91255,0.0192588,-1.36396e-05,4.37407e-09,-5.2316e-13,-41806.4,-7.89162], Tmin=(642.598,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -76.75 kcal/mol
S298: 84.62 cal/mol/K

Coordinates (Angstoms):
F -0.12896 1.53109 -0.74213
F 0.06576 0.74101 1.26272
O -1.37541 -0.19905 -0.17188
O -1.26046 -1.50137 0.01542
O 2.01577 -0.77556 0.00465
C -0.09598 0.42389 -0.01684
C 1.01760 -0.53071 -0.56164

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 53.9,111.3,207.5,289.6,380.5,440.5,493.8,620.8,627.6,752.6,1042.0,1184.7,1201.2,1250.8,1966.3
""",
    rank = 5,
)

entry(
    index = 66,
    label = "FC1(F)OO[CH]C12OO2",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {8,S}
2  F u0 p3 c0 {8,S}
3  O u0 p2 c0 {4,S} {7,S}
4  O u0 p2 c0 {3,S} {7,S}
5  O u0 p2 c0 {6,S} {8,S}
6  O u0 p2 c0 {5,S} {9,S}
7  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
8  C u0 p0 c0 {1,S} {2,S} {5,S} {7,S}
9  C u1 p0 c0 {6,S} {7,S} {10,S}
10 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65691,0.0283369,9.50588e-05,-2.68874e-07,1.8947e-10,-41324.6,13.0817], Tmin=(10,'K'), Tmax=(525.528,'K')),
            NASAPolynomial(coeffs=[6.93449,0.0372868,-2.72371e-05,9.00112e-09,-1.10495e-12,-42137.2,-5.07548], Tmin=(525.528,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -76.66 kcal/mol
S298: 88.59 cal/mol/K

Coordinates (Angstoms):
F -0.47889 -1.55996 -0.91348
F -0.68669 -1.15847 1.19959
O 1.84950 -0.09794 0.72918
O 1.84239 -0.04712 -0.76948
O -1.58448 0.24560 -0.31855
O -1.17619 1.61329 0.00986
C 0.73772 0.31151 0.00065
C -0.51021 -0.59251 -0.00390
C 0.17366 1.63816 0.02923
H 0.63336 2.61224 0.06114

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 65.6,158.4,205.4,225.0,264.8,334.3,418.8,448.8,535.4,577.9,612.5,701.7,758.0,846.5,865.4,877.7,1070.6,1141.6,1157.1,1210.0,1280.0,1365.5,1445.9,3276.5
""",
    rank = 5,
)

entry(
    index = 67,
    label = "CDCDCDCDCBr",
    molecule = 
"""
1 Br u0 p3 c0 {3,S}
2 C  u0 p0 c0 {4,D} {7,S} {8,S}
3 C  u0 p0 c0 {1,S} {5,D} {9,S}
4 C  u0 p0 c0 {2,D} {6,D}
5 C  u0 p0 c0 {3,D} {6,D}
6 C  u0 p0 c0 {4,D} {5,D}
7 H  u0 p0 c0 {2,S}
8 H  u0 p0 c0 {2,S}
9 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77502,0.0182666,0.000122087,-4.17838e-07,3.95605e-10,54837.2,12.341], Tmin=(10,'K'), Tmax=(377.028,'K')),
            NASAPolynomial(coeffs=[5.07391,0.0291744,-1.95306e-05,6.24919e-09,-7.60759e-13,54563.8,5.01455], Tmin=(377.028,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 113.69 kcal/mol
S298: 83.08 cal/mol/K

Coordinates (Angstoms):
Br -1.94476 -0.26268 0.00000
C 4.44281 -0.43938 0.00002
C -0.50797 1.00127 -0.00003
C 3.18571 -0.07720 0.00001
C 0.74142 0.63475 -0.00001
C 1.96258 0.27458 0.00001
H 4.98863 -0.59742 -0.92651
H 4.98863 -0.59737 0.92655
H -0.85778 2.02466 -0.00006

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 75.4,141.6,203.8,331.6,391.8,456.3,565.4,567.3,659.5,750.1,801.5,875.7,1009.6,1191.9,1377.2,1502.5,1970.2,2235.3,3122.9,3197.5,3213.2
""",
    rank = 5,
)

entry(
    index = 68,
    label = "[CH]DCC(DC)[CH]C",
    molecule = 
"""
multiplicity 3
1  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
2  C u0 p0 c0 {3,S} {4,S} {5,D}
3  C u1 p0 c0 {1,S} {2,S} {10,S}
4  C u0 p0 c0 {2,S} {6,D} {11,S}
5  C u0 p0 c0 {2,D} {12,S} {13,S}
6  C u1 p0 c0 {4,D} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.69963,0.0272858,8.35283e-05,-2.36103e-07,1.95533e-10,51292.2,12.6731], Tmin=(10,'K'), Tmax=(312.014,'K')),
            NASAPolynomial(coeffs=[1.8365,0.0511711,-3.13004e-05,9.24868e-09,-1.055e-12,51408.5,19.4916], Tmin=(312.014,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 107.25 kcal/mol
S298: 87.22 cal/mol/K

Coordinates (Angstoms):
C -2.21837 -0.67998 -0.00000
C 0.11338 0.38962 -0.00000
C -0.72447 -0.73785 -0.00002
C 1.58522 0.19223 -0.00001
C -0.36307 1.68320 0.00004
C 2.23934 -0.94453 -0.00004
H -2.60781 -0.14739 -0.87875
H -2.65373 -1.68189 -0.00091
H -2.60784 -0.14902 0.87973
H -0.24761 -1.71301 0.00005
H 2.16976 1.12084 0.00001
H -1.42353 1.90095 0.00008
H 0.31256 2.53050 0.00004
H 3.26602 -1.27712 -0.00005

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 29.2,111.7,192.6,205.8,310.7,461.0,476.3,547.2,569.5,642.8,714.2,773.5,793.1,844.6,863.3,972.8,1010.7,1096.6,1112.2,1242.2,1265.1,1350.4,1399.8,1452.2,1476.4,1484.7,1535.1,1674.8,2999.1,3024.7,3036.9,3110.9,3160.5,3172.5,3251.3,3261.2
""",
    rank = 5,
)

entry(
    index = 69,
    label = "FC(F)(F)[CH]Br",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {6,S}
2 F  u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
6 C  u1 p0 c0 {1,S} {5,S} {7,S}
7 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71083,0.0246956,2.47692e-05,-1.07889e-07,8.23783e-11,-63329.5,14.3542], Tmin=(10,'K'), Tmax=(526.592,'K')),
            NASAPolynomial(coeffs=[6.3515,0.021773,-1.57181e-05,5.16391e-09,-6.31835e-13,-63845.2,1.05207], Tmin=(526.592,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -121.38 kcal/mol
S298: 85.78 cal/mol/K

Coordinates (Angstoms):
Br -1.57705 -0.01748 0.00068
F 1.27677 -1.04191 -0.82379
F 2.35786 0.78532 -0.36342
F 1.56465 -0.44833 1.22918
C 1.31749 0.01766 -0.00924
C 0.06666 0.82596 -0.07180
H 0.09842 1.89421 0.08485

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 41.2,152.5,266.0,319.3,420.6,524.1,570.6,646.7,769.7,897.7,1136.0,1153.4,1250.3,1325.5,3244.6
""",
    rank = 5,
)

entry(
    index = 70,
    label = "F[C]1COOC1(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {7,S}
3  F u0 p3 c0 {8,S}
4  O u0 p2 c0 {5,S} {6,S}
5  O u0 p2 c0 {4,S} {7,S}
6  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
7  C u0 p0 c0 {1,S} {2,S} {5,S} {8,S}
8  C u1 p0 c0 {3,S} {6,S} {7,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.8324,0.0110821,0.000155289,-3.72491e-07,2.62484e-10,-64853.7,12.9701], Tmin=(10,'K'), Tmax=(483.862,'K')),
            NASAPolynomial(coeffs=[3.92875,0.0403482,-2.86336e-05,9.32412e-09,-1.13563e-12,-65214.9,8.93867], Tmin=(483.862,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -124.12 kcal/mol
S298: 83.93 cal/mol/K

Coordinates (Angstoms):
F -1.35780 -0.61468 1.09494
F -1.55071 0.22870 -0.88392
F 0.18790 2.06443 0.05018
O 1.36123 -1.23898 0.02479
O 0.02463 -1.28221 -0.56756
C 1.71557 0.14334 0.01221
C -0.66173 -0.21593 0.01274
C 0.41331 0.79530 0.34125
H 2.50080 0.26044 0.76610
H 2.09486 0.46675 -0.97189

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 68.6,188.8,234.6,288.1,398.0,439.8,506.7,589.7,624.8,670.6,765.5,900.0,986.2,1013.8,1080.3,1136.2,1172.0,1183.9,1284.6,1326.8,1426.4,1473.5,2965.1,3078.5
""",
    rank = 5,
)

entry(
    index = 71,
    label = "FC1DCC(F)C1",
    molecule = 
"""
1  F u0 p3 c0 {3,S}
2  F u0 p3 c0 {5,S}
3  C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
4  C u0 p0 c0 {3,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {2,S} {4,S} {6,D}
6  C u0 p0 c0 {3,S} {5,D} {10,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94595,0.00314398,0.000107795,-1.91154e-07,1.05601e-10,-30956.7,10.0951], Tmin=(10,'K'), Tmax=(552.471,'K')),
            NASAPolynomial(coeffs=[-0.0136736,0.04264,-2.88369e-05,9.19418e-09,-1.11106e-12,-30684.4,25.3531], Tmin=(552.471,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -57.66 kcal/mol
S298: 73.17 cal/mol/K

Coordinates (Angstoms):
F -2.08770 -0.07804 -0.46399
F 2.24889 -0.03742 -0.21660
C -1.03601 -0.03899 0.42217
C 0.00453 1.10027 0.13310
C 0.94825 -0.06137 -0.01670
C 0.06931 -1.04459 0.18046
H -1.45493 -0.02149 1.43364
H 0.20491 1.79913 0.95089
H -0.22423 1.65252 -0.78168
H 0.10698 -2.12298 0.20822

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 139.3,338.2,466.7,476.1,482.5,679.0,801.9,864.5,961.7,993.5,1008.4,1074.7,1140.2,1177.4,1207.3,1257.0,1338.5,1383.3,1475.5,1728.5,3051.5,3058.1,3111.5,3246.0
""",
    rank = 5,
)

entry(
    index = 72,
    label = "ODC[C]1OO1",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {5,D}
4 C u1 p0 c0 {1,S} {2,S} {5,S}
5 C u0 p0 c0 {3,D} {4,S} {6,S}
6 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88881,0.00869699,5.8473e-05,-1.58264e-07,1.22873e-10,8074.14,9.84706], Tmin=(10,'K'), Tmax=(435.037,'K')),
            NASAPolynomial(coeffs=[3.75774,0.019761,-1.36687e-05,4.38152e-09,-5.28778e-13,7992.25,9.29805], Tmin=(435.037,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 19.63 kcal/mol
S298: 71.61 cal/mol/K

Coordinates (Angstoms):
O -1.54318 0.59875 0.00009
O -1.12721 -0.90598 -0.00011
O 1.95583 -0.35582 0.00002
C -0.30043 0.12957 -0.00007
C 1.04963 0.49113 0.00005
H 1.22132 1.58026 0.00014

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 190.5,214.4,332.0,543.7,728.7,885.8,936.6,1081.4,1376.0,1521.0,1723.7,2984.7
""",
    rank = 5,
)

entry(
    index = 73,
    label = "FC1(F)[CH]COO1",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {5,S}
2  F u0 p3 c0 {5,S}
3  O u0 p2 c0 {4,S} {6,S}
4  O u0 p2 c0 {3,S} {5,S}
5  C u0 p0 c0 {1,S} {2,S} {4,S} {7,S}
6  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
7  C u1 p0 c0 {5,S} {6,S} {10,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.87326,0.00776821,0.000138051,-2.93328e-07,1.85307e-10,-44178.8,11.8383], Tmin=(10,'K'), Tmax=(532.978,'K')),
            NASAPolynomial(coeffs=[3.239,0.0395574,-2.74862e-05,8.88199e-09,-1.07987e-12,-44495.1,10.8977], Tmin=(532.978,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -83.37 kcal/mol
S298: 79.74 cal/mol/K

Coordinates (Angstoms):
F 1.59205 0.28298 -0.90831
F 1.26839 -0.24897 1.15603
O -1.45398 -0.84074 0.07630
O -0.11914 -1.02384 -0.46859
C 0.62786 0.05995 0.00226
C -1.69339 0.57012 -0.02907
C -0.35303 1.16561 0.16775
H -2.42699 0.81718 0.74793
H -2.12739 0.81949 -1.01358
H -0.09329 2.19987 0.32892

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 111.0,209.8,254.8,381.1,434.8,508.5,553.6,679.7,710.7,878.4,910.0,944.0,970.9,1023.5,1107.9,1149.5,1186.3,1209.8,1340.9,1372.6,1468.5,2941.5,3051.4,3266.4
""",
    rank = 5,
)

entry(
    index = 74,
    label = "FC1C[C]1C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {5,S}
2  F u0 p3 c0 {7,S}
3  F u0 p3 c0 {7,S}
4  F u0 p3 c0 {7,S}
5  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
6  C u0 p0 c0 {5,S} {8,S} {10,S} {11,S}
7  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
8  C u1 p0 c0 {5,S} {6,S} {7,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.71055,0.0290721,4.18981e-05,-1.02819e-07,5.58223e-11,-71782.7,13.1646], Tmin=(10,'K'), Tmax=(688.894,'K')),
            NASAPolynomial(coeffs=[5.94819,0.037859,-2.46575e-05,7.48187e-09,-8.60597e-13,-72607.8,-0.547821], Tmin=(688.894,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -137.50 kcal/mol
S298: 87.50 cal/mol/K

Coordinates (Angstoms):
F -1.92745 -1.06704 0.27949
F 1.33742 -1.07023 -0.77658
F 0.83057 -0.43019 1.23027
F 1.93707 0.88877 -0.08218
C -1.67821 0.02065 -0.49400
C -1.32844 1.34950 0.17788
C 0.95031 -0.01731 -0.04827
C -0.32302 0.55267 -0.54873
H -2.32288 0.05092 -1.36917
H -1.24596 1.38133 1.26270
H -1.75352 2.24295 -0.27389

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 44.7,104.4,173.4,290.8,362.5,421.3,490.5,516.9,582.4,655.6,756.9,821.1,887.6,930.6,1024.0,1066.2,1087.4,1131.3,1171.3,1201.8,1223.9,1363.3,1416.1,1483.8,3096.9,3139.0,3181.3
""",
    rank = 5,
)

entry(
    index = 75,
    label = "CDC(C(F)Br)C(F)(F)F",
    molecule = 
"""
1  Br u0 p3 c0 {6,S}
2  F  u0 p3 c0 {6,S}
3  F  u0 p3 c0 {7,S}
4  F  u0 p3 c0 {7,S}
5  F  u0 p3 c0 {7,S}
6  C  u0 p0 c0 {1,S} {2,S} {8,S} {10,S}
7  C  u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
8  C  u0 p0 c0 {6,S} {7,S} {9,D}
9  C  u0 p0 c0 {8,D} {11,S} {12,S}
10 H  u0 p0 c0 {6,S}
11 H  u0 p0 c0 {9,S}
12 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.4392,0.0506535,-1.78728e-05,-3.00264e-08,2.32322e-11,-100348,15.9163], Tmin=(10,'K'), Tmax=(712.953,'K')),
            NASAPolynomial(coeffs=[8.55178,0.0378651,-2.44103e-05,7.35869e-09,-8.42678e-13,-101481,-9.85232], Tmin=(712.953,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -193.32 kcal/mol
S298: 98.55 cal/mol/K

Coordinates (Angstoms):
Br -1.81982 -0.57776 -0.18120
F -1.15438 1.94108 0.59880
F 2.91160 -0.10745 -0.43697
F 1.27680 -1.51454 -0.45300
F 1.85772 -0.56870 1.39923
C -0.54587 0.73510 0.60468
C 1.70486 -0.36212 0.07683
C 0.74008 0.77606 -0.16445
C 1.05352 1.79055 -0.96269
H -0.41539 0.39386 1.63170
H 0.36509 2.61332 -1.10774
H 2.00278 1.82333 -1.48097

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 24.0,74.9,131.8,195.9,245.9,297.2,334.5,379.0,425.0,486.8,562.2,591.0,677.2,725.0,777.3,817.5,953.6,1000.2,1101.5,1154.3,1176.5,1214.1,1227.6,1322.4,1402.4,1441.5,1720.2,3121.4,3180.5,3273.0
""",
    rank = 5,
)

entry(
    index = 76,
    label = "Br[C]1CC1",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {4,S}
2 C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C  u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4 C  u1 p0 c0 {1,S} {2,S} {3,S}
5 H  u0 p0 c0 {2,S}
6 H  u0 p0 c0 {2,S}
7 H  u0 p0 c0 {3,S}
8 H  u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.96253,0.00220134,7.70471e-05,-1.37446e-07,7.69014e-11,33895.9,10.7499], Tmin=(10,'K'), Tmax=(542.719,'K')),
            NASAPolynomial(coeffs=[1.21639,0.0297925,-1.95291e-05,6.14485e-09,-7.39502e-13,34085.8,21.3227], Tmin=(542.719,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 70.78 kcal/mol
S298: 72.22 cal/mol/K

Coordinates (Angstoms):
Br -1.03326 0.00000 0.01937
C 1.89892 -0.77330 0.09491
C 1.89892 0.77330 0.09491
C 0.78004 0.00000 -0.45267
H 2.56852 -1.27772 -0.59823
H 1.77992 -1.28337 1.04771
H 1.77992 1.28337 1.04771
H 2.56852 1.27772 -0.59824

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 222.1,296.4,469.7,746.2,833.7,843.9,1007.8,1027.8,1077.0,1077.3,1148.7,1297.3,1447.4,1476.5,3100.8,3100.9,3173.8,3186.2
""",
    rank = 5,
)

entry(
    index = 77,
    label = "FC1DCC(F)(F)O1",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {7,S}
4 O u0 p2 c0 {5,S} {7,S}
5 C u0 p0 c0 {1,S} {2,S} {4,S} {6,S}
6 C u0 p0 c0 {5,S} {7,D} {8,S}
7 C u0 p0 c0 {3,S} {4,S} {6,D}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88726,0.00660468,0.000109124,-2.24183e-07,1.34132e-10,-73083,10.7267], Tmin=(10,'K'), Tmax=(574.596,'K')),
            NASAPolynomial(coeffs=[4.06958,0.0312823,-2.30324e-05,7.73795e-09,-9.66989e-13,-73532.2,6.22091], Tmin=(574.596,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -141.19 kcal/mol
S298: 75.46 cal/mol/K

Coordinates (Angstoms):
F -1.55004 1.07236 -0.06387
F -1.55007 -1.07238 -0.06329
F 2.39821 -0.00003 -0.12460
O 0.27084 -0.00027 -0.96925
C -0.78014 0.00002 0.07010
C 0.29020 0.00030 1.13327
C 1.12882 0.00002 0.09911
H 0.31704 0.00062 2.20500

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 141.5,339.7,376.9,451.5,543.6,602.5,640.2,682.8,713.7,754.6,903.7,1089.7,1129.0,1242.6,1330.9,1389.5,1777.3,3327.5
""",
    rank = 5,
)

entry(
    index = 78,
    label = "OD[C]C(O)C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {7,S}
3  F u0 p3 c0 {7,S}
4  O u0 p2 c0 {6,S} {10,S}
5  O u0 p2 c0 {8,D}
6  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
7  C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
8  C u1 p0 c0 {5,D} {6,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.49748,0.0437827,-1.45764e-05,-4.30586e-08,3.815e-11,-102546,13.1273], Tmin=(10,'K'), Tmax=(589.061,'K')),
            NASAPolynomial(coeffs=[7.38944,0.0319219,-2.14689e-05,6.724e-09,-7.95409e-13,-103257,-5.73471], Tmin=(589.061,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -198.23 kcal/mol
S298: 89.72 cal/mol/K

Coordinates (Angstoms):
F 1.23362 -1.29162 -0.54594
F 1.85562 0.74960 -0.18916
F 0.74018 -0.31467 1.32924
O -0.79662 1.62717 -0.06860
O -2.51139 -0.56713 0.23572
C -0.44481 0.38423 -0.59186
C 0.87559 -0.13045 0.00655
C -1.51951 -0.71311 -0.38517
H -0.29286 0.49527 -1.67009
H -1.17542 1.49063 0.80871

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 60.5,92.2,191.3,203.7,266.0,299.8,370.0,406.5,526.1,565.3,674.2,712.9,785.4,870.9,1102.7,1142.1,1223.6,1252.9,1267.6,1329.7,1411.6,1939.1,3083.3,3789.5
""",
    rank = 5,
)

entry(
    index = 79,
    label = "[O]C(F)(F)CC(DO)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {7,S}
3  F u0 p3 c0 {8,S}
4  O u1 p2 c0 {7,S}
5  O u0 p2 c0 {8,D}
6  C u0 p0 c0 {7,S} {8,S} {9,S} {10,S}
7  C u0 p0 c0 {1,S} {2,S} {4,S} {6,S}
8  C u0 p0 c0 {3,S} {5,D} {6,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60622,0.0375617,-3.2286e-06,-3.65749e-08,2.3029e-11,-101106,13.5354], Tmin=(10,'K'), Tmax=(739.406,'K')),
            NASAPolynomial(coeffs=[7.67466,0.0306386,-1.97884e-05,5.94956e-09,-6.78537e-13,-102120,-7.65278], Tmin=(739.406,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -195.65 kcal/mol
S298: 89.13 cal/mol/K

Coordinates (Angstoms):
F -2.12588 -0.90747 -0.06381
F -1.16173 0.74902 -1.07076
F 2.53006 -0.75117 -0.08206
O -1.19524 0.70911 1.16488
O 1.56740 1.23409 0.03738
C 0.21970 -0.79597 0.10788
C -1.11289 -0.00772 0.04702
C 1.45962 0.05851 0.01998
H 0.18887 -1.49114 -0.73786
H 0.25325 -1.39683 1.02006

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 40.0,82.4,152.6,300.7,319.2,336.7,504.5,515.2,566.3,601.3,665.8,851.8,888.3,913.4,1038.4,1078.6,1141.6,1171.4,1287.0,1366.3,1423.5,1937.7,3065.6,3121.8
""",
    rank = 5,
)

entry(
    index = 80,
    label = "[O]OCC(F)DC(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {8,S}
3  F u0 p3 c0 {8,S}
4  O u0 p2 c0 {5,S} {6,S}
5  O u1 p2 c0 {4,S}
6  C u0 p0 c0 {4,S} {7,S} {9,S} {10,S}
7  C u0 p0 c0 {1,S} {6,S} {8,D}
8  C u0 p0 c0 {2,S} {3,S} {7,D}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60318,0.0445675,-3.75686e-05,1.5689e-08,-2.61163e-12,-59101.5,13.1667], Tmin=(10,'K'), Tmax=(1378.24,'K')),
            NASAPolynomial(coeffs=[11.9555,0.0203269,-1.11863e-05,2.92758e-09,-2.96804e-13,-61403.7,-29.8079], Tmin=(1378.24,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -111.98 kcal/mol
S298: 90.30 cal/mol/K

Coordinates (Angstoms):
F -0.31032 1.84237 -0.17415
F -2.31863 0.05013 -0.51997
F -1.16696 -1.52333 0.43665
O 2.18956 0.08439 -0.09326
O 1.97463 -0.93454 -0.88961
C 1.09984 0.22108 0.89148
C -0.18279 0.57879 0.25385
C -1.18831 -0.26905 0.05442
H 1.02561 -0.72409 1.42980
H 1.45159 1.01785 1.55190

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 55.0,77.7,144.6,213.1,232.5,349.7,422.0,502.1,529.2,593.2,669.3,800.1,834.4,976.8,1157.4,1182.1,1261.6,1312.5,1355.3,1380.1,1455.2,1834.3,3078.6,3150.6
""",
    rank = 5,
)

entry(
    index = 81,
    label = "CDC([CH]Br)O[O]",
    molecule = 
"""
multiplicity 3
1 Br u0 p3 c0 {5,S}
2 O  u0 p2 c0 {3,S} {4,S}
3 O  u1 p2 c0 {2,S}
4 C  u0 p0 c0 {2,S} {5,S} {6,D}
5 C  u1 p0 c0 {1,S} {4,S} {7,S}
6 C  u0 p0 c0 {4,D} {8,S} {9,S}
7 H  u0 p0 c0 {5,S}
8 H  u0 p0 c0 {6,S}
9 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77782,0.0169319,0.000125481,-3.80878e-07,3.22519e-10,27337.3,13.5542], Tmin=(10,'K'), Tmax=(418.818,'K')),
            NASAPolynomial(coeffs=[5.13046,0.0309998,-2.15559e-05,7.0232e-09,-8.61857e-13,26987.3,5.3801], Tmin=(418.818,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 59.06 kcal/mol
S298: 85.39 cal/mol/K

Coordinates (Angstoms):
Br 1.65457 -0.13100 0.00016
O -2.49427 0.06406 -0.00025
O -2.71179 -1.23026 0.00001
C -1.14281 0.47076 -0.00018
C -0.17114 -0.52161 0.00003
C -1.00591 1.83800 -0.00035
H -0.42949 -1.56766 0.00012
H -0.02650 2.29282 -0.00034
H -1.88609 2.46651 -0.00049

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 92.1,165.6,186.2,247.6,430.7,502.0,548.7,568.5,658.4,767.4,771.1,860.3,1012.9,1118.3,1218.5,1321.8,1400.8,1494.6,3187.5,3273.6,3295.2
""",
    rank = 5,
)

entry(
    index = 82,
    label = "[CH2]C(F)[C](F)F",
    molecule = 
"""
multiplicity 3
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {6,S}
3 F u0 p3 c0 {6,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 C u1 p0 c0 {4,S} {8,S} {9,S}
6 C u1 p0 c0 {2,S} {3,S} {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62149,0.0330581,-1.09026e-05,-2.05207e-08,1.6191e-11,-37261.2,12.1296], Tmin=(10,'K'), Tmax=(672.969,'K')),
            NASAPolynomial(coeffs=[6.13539,0.0269634,-1.70384e-05,5.0933e-09,-5.81594e-13,-37799.9,-0.491397], Tmin=(672.969,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -69.24 kcal/mol
S298: 83.42 cal/mol/K

Coordinates (Angstoms):
F -0.86033 -1.14434 0.73299
F 1.67829 -0.60408 -0.41943
F 0.91970 1.14602 0.64251
C -0.70386 -0.31303 -0.37638
C -1.76757 0.71710 -0.38854
C 0.68944 0.27634 -0.33111
H -0.74216 -0.94563 -1.27384
H -2.00550 1.24327 -1.30371
H -2.19928 1.04152 0.54912

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 69.7,122.5,206.6,230.9,351.3,478.7,496.6,585.1,709.1,825.8,877.1,1068.5,1120.0,1206.6,1313.6,1340.7,1352.1,1437.9,3019.3,3168.6,3286.5
""",
    rank = 5,
)

entry(
    index = 83,
    label = "CCC(Br)(O[O])C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  Br u0 p3 c0 {7,S}
2  F  u0 p3 c0 {9,S}
3  F  u0 p3 c0 {9,S}
4  F  u0 p3 c0 {9,S}
5  O  u0 p2 c0 {6,S} {7,S}
6  O  u1 p2 c0 {5,S}
7  C  u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
8  C  u0 p0 c0 {7,S} {10,S} {11,S} {12,S}
9  C  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
10 C  u0 p0 c0 {8,S} {13,S} {14,S} {15,S}
11 H  u0 p0 c0 {8,S}
12 H  u0 p0 c0 {8,S}
13 H  u0 p0 c0 {10,S}
14 H  u0 p0 c0 {10,S}
15 H  u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.2176,0.0743303,-7.24369e-05,3.89606e-08,-8.95569e-12,-86897.5,15.8097], Tmin=(10,'K'), Tmax=(952.772,'K')),
            NASAPolynomial(coeffs=[9.81814,0.0466193,-2.88097e-05,8.43394e-09,-9.45684e-13,-88155.2,-15.7147], Tmin=(952.772,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -165.34 kcal/mol
S298: 106.12 cal/mol/K

Coordinates (Angstoms):
Br 1.46249 -0.89468 -0.18130
F -1.51423 -1.45718 -0.71681
F -2.41303 0.21703 0.30515
F -1.22575 -1.20945 1.41531
O -0.20388 0.87015 -1.34250
O -0.94741 1.95587 -1.35444
C -0.07114 0.30389 0.00184
C 0.12345 1.35682 1.08508
C -1.33090 -0.56542 0.25003
C 1.30835 2.29982 0.87086
H -0.80813 1.92722 1.12955
H 0.21844 0.81782 2.03170
H 2.25660 1.75771 0.85562
H 1.21057 2.85488 -0.06481
H 1.34408 3.02375 1.68907

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 60.8,97.1,109.6,149.3,161.5,201.6,231.3,253.1,300.3,321.3,350.1,369.5,426.3,545.3,571.9,651.4,711.6,754.8,853.0,922.2,969.7,1093.3,1112.2,1135.7,1179.1,1208.6,1240.2,1268.2,1307.6,1370.6,1414.7,1466.5,1496.9,1503.9,3054.8,3069.1,3110.1,3125.6,3138.3
""",
    rank = 5,
)

entry(
    index = 84,
    label = "C[C]C(F)(F)F",
    molecule = 
"""
multiplicity 3
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u2 p0 c0 {4,S} {5,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.80625,0.029907,-1.40897e-05,-8.10383e-10,1.66255e-12,-42069.3,12.2103], Tmin=(10,'K'), Tmax=(1186.68,'K')),
            NASAPolynomial(coeffs=[9.97088,0.017436,-8.82796e-06,2.13361e-09,-2.00625e-13,-44117.4,-21.0505], Tmin=(1186.68,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -78.96 kcal/mol
S298: 83.82 cal/mol/K

Coordinates (Angstoms):
F 0.64801 1.08107 -0.73200
F 1.38782 0.00005 0.99683
F 0.64802 -1.08114 -0.73189
C -2.25069 0.00000 0.05795
C 0.44053 0.00000 0.05243
C -0.90733 0.00003 0.63969
H -3.01609 0.00006 0.84139
H -2.41682 -0.88936 -0.56908
H -2.41680 0.88929 -0.56919

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 46.8,72.4,167.6,403.5,406.2,543.5,564.6,608.4,790.0,998.0,1024.6,1103.5,1110.6,1181.9,1372.4,1381.2,1445.9,1447.9,2972.1,3022.2,3081.8
""",
    rank = 5,
)

entry(
    index = 85,
    label = "[O]OC(DO)[CH]C(F)(F)F",
    molecule = 
"""
multiplicity 3
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {7,S}
3  F u0 p3 c0 {7,S}
4  O u0 p2 c0 {6,S} {9,S}
5  O u0 p2 c0 {9,D}
6  O u1 p2 c0 {4,S}
7  C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
8  C u1 p0 c0 {7,S} {9,S} {10,S}
9  C u0 p0 c0 {4,S} {5,D} {8,S}
10 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45568,0.0528405,-4.90284e-05,1.98664e-08,-2.3396e-12,-77848.4,15.0704], Tmin=(10,'K'), Tmax=(951.056,'K')),
            NASAPolynomial(coeffs=[12.3315,0.0232244,-1.44851e-05,4.18119e-09,-4.58425e-13,-79885.6,-29.1392], Tmin=(951.056,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -148.78 kcal/mol
S298: 96.38 cal/mol/K

Coordinates (Angstoms):
F 1.65466 0.54361 -1.08160
F 2.07852 -1.28316 -0.00016
F 1.65471 0.54334 1.08177
O -2.48566 0.09237 0.00000
O -0.92676 1.69239 -0.00000
O -2.67214 -1.21168 -0.00000
C 1.33318 -0.17274 -0.00000
C -0.12433 -0.53817 -0.00001
C -1.11042 0.50448 -0.00000
H -0.40513 -1.58006 0.00000

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 27.3,65.9,132.1,138.2,249.6,330.0,336.8,483.0,509.6,535.9,565.9,566.3,703.6,732.4,879.5,905.3,1054.3,1185.1,1186.9,1222.0,1264.2,1408.1,1717.3,3265.1
""",
    rank = 5,
)

entry(
    index = 86,
    label = "[O]OC(Br)(CBr)C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  Br u0 p3 c0 {8,S}
2  Br u0 p3 c0 {9,S}
3  F  u0 p3 c0 {10,S}
4  F  u0 p3 c0 {10,S}
5  F  u0 p3 c0 {10,S}
6  O  u0 p2 c0 {7,S} {8,S}
7  O  u1 p2 c0 {6,S}
8  C  u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
9  C  u0 p0 c0 {2,S} {8,S} {11,S} {12,S}
10 C  u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
11 H  u0 p0 c0 {9,S}
12 H  u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.218,0.0791418,-0.000112849,9.10358e-08,-3.09413e-11,-78706.6,17.1885], Tmin=(10,'K'), Tmax=(684.787,'K')),
            NASAPolynomial(coeffs=[9.77127,0.0408625,-2.89996e-05,9.4046e-09,-1.13956e-12,-79604.1,-11.9458], Tmin=(684.787,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -149.17 kcal/mol
S298: 108.97 cal/mol/K

Coordinates (Angstoms):
Br 0.42521 1.67484 -0.27772
Br -2.52983 -0.35250 -0.04418
F 1.86757 -0.77914 -1.65142
F 1.73909 -2.15903 0.01186
F 2.77427 -0.28004 0.24773
O 0.20119 -0.48741 1.52365
O 0.98628 0.21491 2.30649
C 0.38002 -0.23134 0.11129
C -0.76098 -0.95637 -0.59157
C 1.73495 -0.86354 -0.32514
H -0.68366 -0.81295 -1.66598
H -0.70684 -2.01745 -0.34973

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 55.4,66.5,101.9,112.3,141.6,183.3,238.6,265.7,281.1,313.3,354.3,497.3,540.3,585.7,597.4,672.4,732.1,788.0,919.8,960.5,1109.5,1168.7,1202.2,1224.6,1227.6,1266.7,1280.4,1455.4,3111.5,3188.1
""",
    rank = 5,
)

entry(
    index = 87,
    label = "CDC(OO)C(F)(F)F",
    molecule = 
"""
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {6,S}
3  F u0 p3 c0 {6,S}
4  O u0 p2 c0 {5,S} {7,S}
5  O u0 p2 c0 {4,S} {11,S}
6  C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
7  C u0 p0 c0 {4,S} {6,S} {8,D}
8  C u0 p0 c0 {7,D} {9,S} {10,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {8,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.55851,0.0378875,3.91745e-05,-1.60663e-07,1.22951e-10,-87305.8,12.5767], Tmin=(10,'K'), Tmax=(508.685,'K')),
            NASAPolynomial(coeffs=[6.20485,0.0385972,-2.6373e-05,8.40352e-09,-1.00976e-12,-87853.4,-1.13827], Tmin=(508.685,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -167.87 kcal/mol
S298: 88.84 cal/mol/K

Coordinates (Angstoms):
F 1.21167 -0.86473 1.06867
F 1.80919 0.94090 0.03669
F 1.24084 -0.81696 -1.08924
O -1.27069 -0.73113 -0.03018
O -2.65453 -0.35205 -0.08860
C 0.96503 -0.09229 0.00130
C -0.47468 0.37935 -0.00499
C -0.83276 1.65494 0.00689
H -0.06945 2.41810 0.02508
H -1.87242 1.94467 -0.01006
H -2.95717 -0.68227 0.77093

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 56.6,97.6,172.4,201.8,262.8,348.9,382.9,410.6,505.4,577.5,674.6,689.1,755.1,812.3,894.0,937.9,991.5,1169.4,1190.8,1221.6,1341.9,1406.6,1431.1,1743.8,3205.0,3301.8,3744.5
""",
    rank = 5,
)

entry(
    index = 88,
    label = "FC(F)(F)[C]DCBr",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {6,S}
2 F  u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
6 C  u0 p0 c0 {1,S} {7,D} {8,S}
7 C  u1 p0 c0 {5,S} {6,D}
8 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60503,0.0357064,-1.64084e-05,-2.12049e-08,1.88592e-11,-43829.4,15.1984], Tmin=(10,'K'), Tmax=(681.459,'K')),
            NASAPolynomial(coeffs=[7.92495,0.0228378,-1.55716e-05,4.86856e-09,-5.71722e-13,-44708.2,-6.11355], Tmin=(681.459,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -82.17 kcal/mol
S298: 90.42 cal/mol/K

Coordinates (Angstoms):
Br 1.91054 -0.17649 -0.00000
F -2.53191 0.10658 1.08052
F -2.53135 0.10602 -1.08099
F -1.24201 -1.25602 0.00046
C -1.75287 -0.01578 0.00000
C 0.58233 1.23295 0.00000
C -0.69086 1.00907 0.00002
H 1.04707 2.21049 -0.00000

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 19.0,86.2,195.0,238.1,453.2,486.2,506.0,574.9,612.7,657.8,769.3,813.2,1150.0,1174.0,1191.3,1229.3,1783.7,3211.2
""",
    rank = 5,
)

entry(
    index = 89,
    label = "[CH2]C1(F)OOC1(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {7,S}
3  F u0 p3 c0 {7,S}
4  O u0 p2 c0 {5,S} {6,S}
5  O u0 p2 c0 {4,S} {7,S}
6  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
7  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
8  C u1 p0 c0 {6,S} {9,S} {10,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.75511,0.0169479,0.00016865,-4.59145e-07,3.52345e-10,-64193.2,12.6034], Tmin=(10,'K'), Tmax=(462.329,'K')),
            NASAPolynomial(coeffs=[5.92084,0.0378275,-2.7628e-05,9.2284e-09,-1.14687e-12,-64816.9,-0.753285], Tmin=(462.329,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -122.36 kcal/mol
S298: 85.81 cal/mol/K

Coordinates (Angstoms):
F 1.25462 -1.15163 -0.61732
F -1.36656 -0.83833 -0.86220
F -1.26636 1.25277 -0.36083
O 0.65553 -0.17514 1.37802
O -0.82560 -0.27171 1.26271
C 0.79744 -0.01322 -0.05093
C -0.75046 0.04943 -0.09627
C 1.61121 1.14371 -0.42637
H 2.48543 1.00377 -1.04674
H 1.33072 2.12636 -0.07464

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 96.5,147.7,199.0,272.6,323.4,385.1,443.9,499.1,536.4,573.5,643.1,717.5,776.2,899.7,910.1,950.3,1154.8,1197.9,1225.3,1267.3,1352.6,1441.2,3181.3,3304.8
""",
    rank = 5,
)

entry(
    index = 90,
    label = "[O]OCCDCC(F)(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {7,S}
3  F u0 p3 c0 {7,S}
4  O u0 p2 c0 {5,S} {6,S}
5  O u1 p2 c0 {4,S}
6  C u0 p0 c0 {4,S} {8,S} {10,S} {11,S}
7  C u0 p0 c0 {1,S} {2,S} {3,S} {9,S}
8  C u0 p0 c0 {6,S} {9,D} {12,S}
9  C u0 p0 c0 {7,S} {8,D} {13,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61867,0.0513922,-3.11574e-05,5.67458e-09,7.21499e-13,-74619.7,13.9925], Tmin=(10,'K'), Tmax=(1204.6,'K')),
            NASAPolynomial(coeffs=[14.2426,0.0267539,-1.3726e-05,3.35983e-09,-3.19843e-13,-77951.1,-42.4438], Tmin=(1204.6,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -142.13 kcal/mol
S298: 96.56 cal/mol/K

Coordinates (Angstoms):
F 2.02081 -1.04658 -0.84529
F 2.18519 -0.36439 1.19585
F 2.07118 1.07504 -0.41734
O -2.70459 -0.21290 0.53106
O -2.86233 -1.14832 -0.38302
C -2.13635 0.98898 -0.04082
C 1.60060 -0.10401 0.01416
C -0.64448 0.93236 -0.14591
C 0.10920 -0.12024 0.14064
H -2.60114 1.14600 -1.01965
H -2.44868 1.79392 0.63442
H -0.17828 1.85234 -0.48875
H -0.30501 -1.06165 0.48218

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 42.2,70.7,104.5,147.4,199.2,239.2,392.6,399.7,454.8,539.3,559.3,596.1,712.5,814.3,857.9,906.6,1002.0,1025.3,1057.0,1162.0,1177.2,1178.1,1279.0,1286.7,1309.6,1330.9,1383.7,1452.0,1756.2,3041.9,3093.1,3173.1,3209.3
""",
    rank = 5,
)

entry(
    index = 91,
    label = "[O]OC1DCOOC1(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {7,S}
3  O u0 p2 c0 {4,S} {7,S}
4  O u0 p2 c0 {3,S} {9,S}
5  O u0 p2 c0 {6,S} {8,S}
6  O u1 p2 c0 {5,S}
7  C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
8  C u0 p0 c0 {5,S} {7,S} {9,D}
9  C u0 p0 c0 {4,S} {8,D} {10,S}
10 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6658,0.0305233,5.31724e-05,-1.49294e-07,9.29897e-11,-43406.5,13.1411], Tmin=(10,'K'), Tmax=(609.657,'K')),
            NASAPolynomial(coeffs=[6.95918,0.0356052,-2.49993e-05,7.99583e-09,-9.56028e-13,-44304.1,-5.18572], Tmin=(609.657,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -80.96 kcal/mol
S298: 88.13 cal/mol/K

Coordinates (Angstoms):
F -1.11841 -1.19981 1.07263
F -1.11850 -1.19982 -1.07248
O -1.60316 0.70918 0.00010
O -0.73928 1.87458 -0.00001
O 1.64628 -0.77587 -0.00004
O 2.81782 -0.15476 -0.00018
C -0.80582 -0.45189 0.00006
C 0.58755 0.07696 -0.00002
C 0.52844 1.40934 -0.00006
H 1.29788 2.16504 -0.00015

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 94.3,100.6,186.1,220.0,356.6,364.1,438.9,443.0,600.0,621.7,672.9,766.6,829.2,862.0,909.8,1039.2,1142.9,1156.9,1163.0,1197.6,1261.0,1384.3,1671.9,3276.5
""",
    rank = 5,
)

entry(
    index = 92,
    label = "FC(F)(F)C1DC(C(F)(F)F)CC1",
    molecule = 
"""
1  F u0 p3 c0 {9,S}
2  F u0 p3 c0 {9,S}
3  F u0 p3 c0 {9,S}
4  F u0 p3 c0 {10,S}
5  F u0 p3 c0 {10,S}
6  F u0 p3 c0 {10,S}
7  C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
8  C u0 p0 c0 {7,S} {11,S} {15,S} {16,S}
9  C u0 p0 c0 {1,S} {2,S} {3,S} {11,S}
10 C u0 p0 c0 {4,S} {5,S} {6,S} {12,S}
11 C u0 p0 c0 {8,S} {9,S} {12,D}
12 C u0 p0 c0 {7,S} {10,S} {11,D}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.43978,0.065349,-2.58122e-05,-1.62651e-08,1.15071e-11,-147184,15.2002], Tmin=(10,'K'), Tmax=(951.804,'K')),
            NASAPolynomial(coeffs=[13.3513,0.0447039,-2.6385e-05,7.32618e-09,-7.8046e-13,-150022,-37.1268], Tmin=(951.804,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (382.466,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -285.19 kcal/mol
S298: 105.33 cal/mol/K

Coordinates (Angstoms):
F 2.24845 -0.56501 1.22838
F 1.29448 -1.58762 -0.42369
F 2.74475 -0.02368 -0.80474
F -2.24844 -0.56502 -1.22838
F -2.74476 -0.02367 0.80473
F -1.29449 -1.58762 0.42370
C -0.78590 2.15647 0.00083
C 0.78590 2.15647 -0.00083
C 1.73527 -0.40025 -0.00207
C -1.73527 -0.40025 0.00207
C 0.66867 0.64534 -0.00340
C -0.66867 0.64534 0.00340
H -1.24842 2.58946 -0.89024
H -1.25101 2.58800 0.89078
H 1.25101 2.58800 -0.89078
H 1.24842 2.58947 0.89024

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 18.2,27.7,127.9,138.0,145.0,185.8,260.2,307.1,324.6,431.8,432.8,483.3,495.5,567.4,583.4,628.4,665.2,741.2,756.2,814.3,907.5,966.6,1048.4,1089.0,1094.1,1119.7,1159.6,1173.4,1176.2,1201.5,1207.8,1217.6,1243.7,1327.1,1356.4,1465.0,1482.4,1772.4,3060.0,3064.1,3107.0,3119.3
""",
    rank = 5,
)

entry(
    index = 93,
    label = "[C]DCC",
    molecule = 
"""
multiplicity 3
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 C u2 p0 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0396,-0.00292207,5.24476e-05,-7.18958e-08,3.22684e-11,67876.6,7.72334], Tmin=(10,'K'), Tmax=(632.059,'K')),
            NASAPolynomial(coeffs=[0.693022,0.0211953,-1.17612e-05,3.18413e-09,-3.37469e-13,68241,21.869], Tmin=(632.059,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (149.66,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 137.69 kcal/mol
S298: 62.84 cal/mol/K

Coordinates (Angstoms):
C -1.09033 -0.14360 0.00000
C 0.32658 0.38451 -0.00002
C 1.41878 -0.35341 0.00001
H -1.63085 0.21743 -0.88307
H -1.11088 -1.23460 -0.00031
H -1.63068 0.21692 0.88340
H 0.44225 1.47529 0.00004

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 301.4,712.0,856.4,1024.8,1051.6,1242.4,1338.6,1444.2,1462.8,1725.2,2999.4,3019.6,3078.4,3138.5
""",
    rank = 5,
)

entry(
    index = 94,
    label = "[O]OC1CDCC1",
    molecule = 
"""
multiplicity 2
1  O u0 p2 c0 {2,S} {3,S}
2  O u1 p2 c0 {1,S}
3  C u0 p0 c0 {1,S} {4,S} {5,S} {7,S}
4  C u0 p0 c0 {3,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {6,D} {10,S}
6  C u0 p0 c0 {4,S} {5,D} {11,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.93617,0.00384152,0.000124174,-2.3155e-07,1.35241e-10,22987.5,11.9919], Tmin=(10,'K'), Tmax=(525.16,'K')),
            NASAPolynomial(coeffs=[0.17964,0.0450461,-2.94835e-05,9.16947e-09,-1.08746e-12,23208.5,26.0424], Tmin=(525.16,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 49.75 kcal/mol
S298: 78.10 cal/mol/K

Coordinates (Angstoms):
O -1.20864 -0.43458 -0.39751
O -2.27110 0.21835 0.02329
C -0.05697 -0.15775 0.44167
C 0.78041 1.09652 0.01851
C 1.15457 -0.98136 0.08407
C 1.89613 0.09151 -0.21672
H -0.40623 -0.17099 1.47636
H 0.93946 1.84415 0.80196
H 0.38758 1.58885 -0.87499
H 1.33603 -2.04784 0.11693
H 2.93626 0.22215 -0.49169

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 48.3,183.9,312.5,463.3,481.2,705.6,851.2,878.2,924.0,951.3,987.5,1024.3,1044.2,1119.3,1144.5,1193.9,1202.3,1233.5,1317.8,1338.2,1474.6,1636.3,3050.6,3090.4,3105.5,3192.3,3227.0
""",
    rank = 5,
)

entry(
    index = 95,
    label = "CDC1CDCC1C",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {6,D}
4  C u0 p0 c0 {1,S} {5,D} {11,S}
5  C u0 p0 c0 {3,S} {4,D} {12,S}
6  C u0 p0 c0 {3,D} {13,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.95216,0.0030951,0.000161574,-3.09243e-07,1.93265e-10,24023.5,10.0367], Tmin=(10,'K'), Tmax=(411.537,'K')),
            NASAPolynomial(coeffs=[-1.62544,0.0573146,-3.60751e-05,1.09794e-08,-1.28844e-12,24482.5,31.9925], Tmin=(411.537,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (332.579,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 52.15 kcal/mol
S298: 76.11 cal/mol/K

Coordinates (Angstoms):
C -0.68415 -0.09468 0.47704
C -1.64621 -0.97154 -0.32068
C 0.80845 -0.12339 0.06569
C -0.58153 1.38497 0.09703
C 0.71971 1.31026 -0.24384
C 1.73553 -1.07337 0.01360
H -0.82821 -0.25810 1.55302
H -1.49696 -0.83716 -1.39660
H -1.49768 -2.03077 -0.08614
H -2.68748 -0.72343 -0.08670
H -1.30931 2.18751 0.10663
H 1.44599 2.02908 -0.60458
H 1.51813 -2.09429 0.30949
H 2.74467 -0.86633 -0.32810

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 171.1,225.4,237.1,326.5,394.3,642.6,709.5,716.6,802.9,811.1,880.6,894.0,926.5,947.9,1043.2,1063.0,1104.2,1137.4,1189.1,1216.6,1308.3,1351.1,1404.8,1450.9,1492.8,1495.1,1592.2,1746.8,3019.3,3026.7,3091.6,3104.5,3141.5,3186.2,3217.8,3221.7
""",
    rank = 5,
)

entry(
    index = 96,
    label = "[CH]DC(Br)C(F)F",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {5,S}
2 F  u0 p3 c0 {4,S}
3 F  u0 p3 c0 {4,S}
4 C  u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
5 C  u0 p0 c0 {1,S} {4,S} {6,D}
6 C  u1 p0 c0 {5,D} {8,S}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72065,0.0236242,4.79563e-05,-1.75246e-07,1.45176e-10,-15725.7,13.9732], Tmin=(10,'K'), Tmax=(454.13,'K')),
            NASAPolynomial(coeffs=[5.36781,0.0264075,-1.83513e-05,5.93856e-09,-7.2306e-13,-16053.6,5.36372], Tmin=(454.13,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -26.67 kcal/mol
S298: 85.61 cal/mol/K

Coordinates (Angstoms):
Br -1.45178 -0.15940 0.05526
F 1.41815 -1.35893 -0.55327
F 2.61668 0.27952 0.26654
C 1.41693 -0.33535 0.33089
C 0.32398 0.64859 -0.01978
C 0.47062 1.89461 -0.32700
H 1.27946 -0.74915 1.33782
H -0.04963 2.79569 -0.59617

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 58.6,165.3,272.8,291.9,313.4,515.0,582.7,674.1,706.8,767.2,971.5,1131.9,1152.1,1384.2,1393.6,1716.0,3047.0,3327.7
""",
    rank = 5,
)

entry(
    index = 97,
    label = "[CH2]CC(Br)(OO)C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  Br u0 p3 c0 {7,S}
2  F  u0 p3 c0 {9,S}
3  F  u0 p3 c0 {9,S}
4  F  u0 p3 c0 {9,S}
5  O  u0 p2 c0 {6,S} {7,S}
6  O  u0 p2 c0 {5,S} {15,S}
7  C  u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
8  C  u0 p0 c0 {7,S} {10,S} {11,S} {12,S}
9  C  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
10 C  u1 p0 c0 {8,S} {13,S} {14,S}
11 H  u0 p0 c0 {8,S}
12 H  u0 p0 c0 {8,S}
13 H  u0 p0 c0 {10,S}
14 H  u0 p0 c0 {10,S}
15 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.21076,0.0719647,3.70062e-05,-3.68825e-07,4.11294e-10,-80492.4,15.9715], Tmin=(10,'K'), Tmax=(382.525,'K')),
            NASAPolynomial(coeffs=[8.38579,0.0544864,-3.81173e-05,1.24741e-08,-1.53637e-12,-81156.4,-7.5256], Tmin=(382.525,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (357.522,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -152.12 kcal/mol
S298: 109.12 cal/mol/K

Coordinates (Angstoms):
Br -1.63017 -0.59229 -0.22672
F 0.97012 -1.42794 1.41047
F 2.39116 -0.23449 0.29582
F 1.17776 -1.69308 -0.72824
O 0.30092 0.89934 -1.25053
O 1.37616 1.87047 -1.16770
C 0.10094 0.30793 0.02076
C 0.04062 1.29987 1.18564
C 1.16329 -0.79717 0.25192
C -0.93160 2.40684 0.98282
H 1.06298 1.69297 1.30070
H -0.17722 0.73498 2.09597
H -1.41467 2.86531 1.83525
H -1.06498 2.84761 0.00399
H 2.14248 1.32544 -1.40412

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 53.7,100.7,109.4,142.6,149.0,162.1,228.9,238.2,290.2,313.2,334.9,350.2,355.7,427.6,468.4,543.3,574.1,659.2,717.8,768.1,897.7,926.2,964.1,1022.7,1118.1,1142.9,1178.9,1229.3,1246.7,1284.5,1363.2,1404.4,1447.3,1455.7,2985.3,3091.6,3171.5,3283.7,3734.7
""",
    rank = 5,
)

entry(
    index = 98,
    label = "[CH2]C([CH2])C(F)(F)F",
    molecule = 
"""
multiplicity 3
1  F u0 p3 c0 {5,S}
2  F u0 p3 c0 {5,S}
3  F u0 p3 c0 {5,S}
4  C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5  C u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
6  C u1 p0 c0 {4,S} {9,S} {10,S}
7  C u1 p0 c0 {4,S} {11,S} {12,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.59943,0.0352468,9.48677e-05,-3.6492e-07,3.44964e-10,-49076.7,12.7673], Tmin=(10,'K'), Tmax=(385.463,'K')),
            NASAPolynomial(coeffs=[5.08155,0.0435344,-2.94838e-05,9.43929e-09,-1.1452e-12,-49366.8,4.74916], Tmin=(385.463,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -91.73 kcal/mol
S298: 90.32 cal/mol/K

Coordinates (Angstoms):
F 1.23334 -1.08146 -0.47736
F 0.71074 -0.02175 1.33515
F 1.24036 1.08132 -0.44846
C -0.88387 0.00255 -0.44795
C 0.59234 -0.00543 0.00306
C -1.55581 1.26262 -0.01456
C -1.59034 -1.23445 0.00160
H -0.79501 -0.01961 -1.55238
H -1.03710 2.21045 -0.07523
H -2.60007 1.25028 0.26829
H -1.32521 -2.19748 -0.41570
H -2.27654 -1.19833 0.83819

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 80.2,90.7,120.7,218.7,238.8,335.4,401.9,440.8,496.5,509.4,544.8,580.3,683.4,805.7,912.0,941.7,1102.3,1134.3,1158.3,1192.9,1251.2,1306.8,1312.4,1440.9,1465.9,2889.6,3160.7,3166.4,3273.5,3279.6
""",
    rank = 5,
)

entry(
    index = 99,
    label = "C#CC(F)(F)O[O]",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 O u0 p2 c0 {4,S} {5,S}
4 O u1 p2 c0 {3,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
6 C u0 p0 c0 {5,S} {7,T}
7 C u0 p0 c0 {6,T} {8,S}
8 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.76844,0.0166425,0.000130911,-3.93762e-07,3.22647e-10,-19463.8,12.0952], Tmin=(10,'K'), Tmax=(443.75,'K')),
            NASAPolynomial(coeffs=[6.39648,0.0271437,-2.01592e-05,6.83024e-09,-8.58469e-13,-20033.7,-2.24135], Tmin=(443.75,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -33.93 kcal/mol
S298: 82.47 cal/mol/K

Coordinates (Angstoms):
F 0.22184 -1.52007 -0.71667
F 0.53858 -0.66641 1.25133
O 1.07396 0.48653 -0.60757
O 1.09419 1.64487 0.01602
C 0.11475 -0.41090 0.01350
C -1.23454 0.13296 0.00237
C -2.35415 0.55855 -0.02210
H -3.34535 0.94345 -0.04224

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 93.6,163.0,185.0,290.2,434.9,455.5,515.2,579.8,685.5,703.9,709.0,767.4,1012.6,1200.9,1209.2,1265.9,2262.5,3491.9
""",
    rank = 5,
)

entry(
    index = 100,
    label = "C[CH]C1(C(F)(F)F)OO1",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {7,S}
3  F u0 p3 c0 {7,S}
4  O u0 p2 c0 {5,S} {6,S}
5  O u0 p2 c0 {4,S} {6,S}
6  C u0 p0 c0 {4,S} {5,S} {7,S} {9,S}
7  C u0 p0 c0 {1,S} {2,S} {3,S} {6,S}
8  C u0 p0 c0 {9,S} {10,S} {11,S} {12,S}
9  C u1 p0 c0 {6,S} {8,S} {13,S}
10 H u0 p0 c0 {8,S}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41215,0.0525792,-1.63011e-05,-3.21155e-08,2.37686e-11,-70660.6,13.7123], Tmin=(10,'K'), Tmax=(714.649,'K')),
            NASAPolynomial(coeffs=[8.10954,0.041863,-2.65012e-05,7.89737e-09,-8.97515e-13,-71729.7,-10.1545], Tmin=(714.649,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -134.15 kcal/mol
S298: 95.11 cal/mol/K

Coordinates (Angstoms):
F -1.94692 -0.42683 -0.07643
F -0.37790 -1.31327 1.11834
F -0.25408 -1.36192 -1.04616
O -0.52218 1.72188 0.72792
O -0.48147 1.71086 -0.75748
C 0.13166 0.70725 0.01271
C -0.64081 -0.61785 0.00069
C 2.44545 -0.53796 -0.01081
C 1.58893 0.67716 0.05390
H 3.41862 -0.34224 0.44769
H 2.63855 -0.83945 -1.05241
H 1.99122 -1.39726 0.48775
H 2.03960 1.66372 0.05279

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 66.7,87.0,94.4,181.5,215.5,281.0,348.3,362.2,451.7,459.6,520.2,559.0,589.4,619.0,757.4,839.3,858.7,961.4,995.2,1118.4,1165.8,1187.3,1245.7,1273.0,1388.5,1403.6,1416.5,1478.1,1485.6,2984.7,3077.6,3126.9,3194.4
""",
    rank = 5,
)

entry(
    index = 101,
    label = "[O]OC(F)CDC(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {8,S}
3  F u0 p3 c0 {8,S}
4  O u0 p2 c0 {5,S} {6,S}
5  O u1 p2 c0 {4,S}
6  C u0 p0 c0 {1,S} {4,S} {7,S} {9,S}
7  C u0 p0 c0 {6,S} {8,D} {10,S}
8  C u0 p0 c0 {2,S} {3,S} {7,D}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.65992,0.0425584,-3.19533e-05,1.05636e-08,-1.08804e-12,-64025.6,13.5348], Tmin=(10,'K'), Tmax=(1226.4,'K')),
            NASAPolynomial(coeffs=[12.8695,0.0184586,-9.73982e-06,2.43648e-09,-2.36145e-13,-66731.1,-34.5963], Tmin=(1226.4,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -121.83 kcal/mol
S298: 90.90 cal/mol/K

Coordinates (Angstoms):
F -1.64466 -1.59029 0.26068
F 2.57893 -0.10985 -0.69570
F 1.61878 0.47832 1.13514
O -1.89952 0.51685 -0.36333
O -1.48881 1.74974 -0.18700
C -0.96074 -0.42441 0.27050
C 0.29437 -0.52541 -0.50904
C 1.44681 -0.06810 -0.04346
H -0.81435 -0.07173 1.29363
H 0.26086 -0.95702 -1.50010

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 41.3,67.0,138.0,174.4,303.3,384.1,479.9,520.3,552.9,608.7,657.6,821.6,919.1,970.3,1133.0,1147.5,1215.6,1249.3,1326.7,1361.7,1426.5,1797.9,3105.4,3229.1
""",
    rank = 5,
)

entry(
    index = 102,
    label = "[O]OCDC(O)C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {7,S}
3  F u0 p3 c0 {7,S}
4  O u0 p2 c0 {8,S} {11,S}
5  O u0 p2 c0 {6,S} {9,S}
6  O u1 p2 c0 {5,S}
7  C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
8  C u0 p0 c0 {4,S} {7,S} {9,D}
9  C u0 p0 c0 {5,S} {8,D} {10,S}
10 H u0 p0 c0 {9,S}
11 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58117,0.0369153,4.08311e-05,-1.38498e-07,9.12375e-11,-91968.2,13.7484], Tmin=(10,'K'), Tmax=(589.31,'K')),
            NASAPolynomial(coeffs=[6.8747,0.0390288,-2.68294e-05,8.50071e-09,-1.01219e-12,-92781.3,-4.0043], Tmin=(589.31,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -177.12 kcal/mol
S298: 91.26 cal/mol/K

Coordinates (Angstoms):
F 1.86804 -0.50502 -1.07906
F 1.62287 1.35811 -0.00018
F 1.86809 -0.50479 1.07909
O -0.55299 -1.42079 0.00020
O -2.38091 0.79869 -0.00006
O -2.88770 -0.44649 0.00011
C 1.31675 0.05498 -0.00003
C -0.18306 -0.15136 0.00002
C -1.03229 0.90623 -0.00010
H -0.71260 1.93598 -0.00024
H -1.55404 -1.38099 0.00021

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 48.9,115.8,185.5,229.0,281.4,312.4,366.7,414.9,518.5,557.7,584.5,689.4,756.6,800.4,877.4,924.5,1016.5,1049.1,1149.4,1203.5,1222.0,1305.1,1406.8,1454.1,1651.0,3054.2,3272.3
""",
    rank = 5,
)

entry(
    index = 103,
    label = "FC(F)(F)[C](Br)COBr",
    molecule = 
"""
multiplicity 2
1  Br u0 p3 c0 {9,S}
2  Br u0 p3 c0 {6,S}
3  F  u0 p3 c0 {8,S}
4  F  u0 p3 c0 {8,S}
5  F  u0 p3 c0 {8,S}
6  O  u0 p2 c0 {2,S} {7,S}
7  C  u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
8  C  u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
9  C  u1 p0 c0 {1,S} {7,S} {8,S}
10 H  u0 p0 c0 {7,S}
11 H  u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.28479,0.0758586,-0.000151836,2.06108e-07,-1.20869e-10,-68598.4,18.9545], Tmin=(10,'K'), Tmax=(408.359,'K')),
            NASAPolynomial(coeffs=[6.60777,0.0433089,-3.22731e-05,1.09143e-08,-1.36936e-12,-68869.8,5.89912], Tmin=(408.359,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -129.65 kcal/mol
S298: 109.52 cal/mol/K

Coordinates (Angstoms):
Br 1.59487 -1.40928 -0.21130
Br -2.42633 -0.01960 -0.35067
F 0.68940 1.58845 -1.25732
F 2.43525 1.57732 0.00756
F 0.56342 2.37039 0.75754
O -1.48672 -0.93354 0.96205
C -0.39640 -0.17539 1.49225
C 1.10837 1.40325 0.00406
C 0.72153 0.05277 0.53472
H -0.73523 0.78412 1.89453
H -0.06373 -0.81406 2.32162

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 16.8,29.3,55.9,142.5,159.3,189.9,321.3,331.0,358.9,438.1,525.0,564.7,575.1,628.7,699.7,865.7,953.3,1064.8,1131.9,1158.0,1208.5,1249.0,1323.9,1363.8,1450.3,3021.5,3090.9
""",
    rank = 5,
)

entry(
    index = 104,
    label = "CC(Br)[C](Br)C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  Br u0 p3 c0 {6,S}
2  Br u0 p3 c0 {9,S}
3  F  u0 p3 c0 {8,S}
4  F  u0 p3 c0 {8,S}
5  F  u0 p3 c0 {8,S}
6  C  u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
7  C  u0 p0 c0 {6,S} {11,S} {12,S} {13,S}
8  C  u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
9  C  u1 p0 c0 {2,S} {6,S} {8,S}
10 H  u0 p0 c0 {6,S}
11 H  u0 p0 c0 {7,S}
12 H  u0 p0 c0 {7,S}
13 H  u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.22764,0.0770012,-0.000122834,1.3233e-07,-6.29553e-11,-71447.1,17.9132], Tmin=(10,'K'), Tmax=(493.905,'K')),
            NASAPolynomial(coeffs=[6.89855,0.0472715,-3.25439e-05,1.04578e-08,-1.26721e-12,-71809.7,2.79269], Tmin=(493.905,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -134.97 kcal/mol
S298: 108.97 cal/mol/K

Coordinates (Angstoms):
Br 2.22433 0.14417 -0.47114
Br -1.43266 -1.38566 -0.37039
F -1.01671 1.72964 -1.12970
F -2.37359 1.44593 0.52268
F -0.42160 2.31928 0.86608
C 0.80696 -0.15268 1.02561
C 1.11572 -1.47705 1.69597
C -1.08496 1.39033 0.16371
C -0.50394 0.02418 0.42148
H 1.03001 0.69967 1.66370
H 1.03222 -2.31062 0.99731
H 0.40671 -1.63834 2.51630
H 2.12727 -1.46111 2.10416

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 27.0,41.3,82.8,160.1,166.8,225.6,244.5,253.9,327.6,357.2,418.3,473.7,511.6,578.0,600.7,709.8,916.2,958.6,1029.4,1084.5,1159.5,1168.5,1192.1,1218.1,1282.6,1378.5,1411.7,1479.8,1487.5,3040.9,3121.4,3141.9,3157.6
""",
    rank = 5,
)

entry(
    index = 105,
    label = "FC1(F)CDC1",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 C u0 p0 c0 {3,S} {5,D} {6,S}
5 C u0 p0 c0 {3,S} {4,D} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94756,0.00289645,7.1868e-05,-1.26533e-07,6.69252e-11,-19583.6,7.86706], Tmin=(10,'K'), Tmax=(615.385,'K')),
            NASAPolynomial(coeffs=[2.03451,0.0280179,-2.02892e-05,6.80462e-09,-8.52836e-13,-19588.4,14.2158], Tmin=(615.385,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -35.50 kcal/mol
S298: 66.43 cal/mol/K

Coordinates (Angstoms):
F -0.93396 -1.08309 -0.00001
F -0.93397 1.08309 0.00001
C -0.12070 0.00000 0.00000
C 1.17108 0.00001 -0.65783
C 1.17107 -0.00000 0.65783
H 1.74135 0.00002 -1.57253
H 1.74134 -0.00004 1.57254

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 389.3,422.4,506.8,535.6,711.6,792.5,931.9,963.8,972.1,1131.7,1140.1,1378.9,1668.8,3246.5,3286.1
""",
    rank = 5,
)

entry(
    index = 106,
    label = "FC(F)(F)[C]1COOC1",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {8,S}
2  F u0 p3 c0 {8,S}
3  F u0 p3 c0 {8,S}
4  O u0 p2 c0 {5,S} {6,S}
5  O u0 p2 c0 {4,S} {7,S}
6  C u0 p0 c0 {4,S} {9,S} {10,S} {11,S}
7  C u0 p0 c0 {5,S} {9,S} {12,S} {13,S}
8  C u0 p0 c0 {1,S} {2,S} {3,S} {9,S}
9  C u1 p0 c0 {6,S} {7,S} {8,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73212,0.0397879,9.09142e-06,-4.11756e-08,1.88052e-11,-73331.7,14.1912], Tmin=(10,'K'), Tmax=(927.08,'K')),
            NASAPolynomial(coeffs=[9.17256,0.0376827,-2.20759e-05,6.09892e-09,-6.47389e-13,-75258.7,-16.5963], Tmin=(927.08,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -139.99 kcal/mol
S298: 94.17 cal/mol/K

Coordinates (Angstoms):
F -1.82794 1.15951 -0.42154
F -1.83873 -0.99845 -0.70580
F -1.64796 -0.16464 1.27923
O 2.31230 -0.68849 0.32388
O 2.38318 0.66602 -0.20780
C 1.07447 -1.18512 -0.18336
C 1.08279 1.19356 0.03891
C -1.27962 0.00541 -0.01070
C 0.18853 0.01828 -0.17544
H 1.19452 -1.60275 -1.19669
H 0.75028 -1.98426 0.49343
H 0.99579 1.59393 1.06447
H 0.93015 2.01229 -0.67341

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 25.5,49.9,153.1,190.5,296.6,339.0,398.7,412.7,560.2,572.0,699.6,711.2,801.3,850.0,937.6,972.5,1011.1,1014.4,1063.0,1128.4,1161.7,1183.4,1205.8,1262.2,1302.2,1343.6,1411.4,1467.8,1474.7,2945.2,2962.1,3061.6,3062.9
""",
    rank = 5,
)

entry(
    index = 107,
    label = "C#CC(F)(F)[C]DO",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 O u0 p2 c0 {6,D}
4 C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5 C u0 p0 c0 {4,S} {7,T}
6 C u1 p0 c0 {3,D} {4,S}
7 C u0 p0 c0 {5,T} {8,S}
8 H u0 p0 c0 {7,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.70382,0.0233759,0.000108745,-3.9532e-07,3.63227e-10,-16785.4,12.8318], Tmin=(10,'K'), Tmax=(408.597,'K')),
            NASAPolynomial(coeffs=[6.73733,0.0259364,-1.90747e-05,6.44439e-09,-8.1027e-13,-17302.6,-2.38317], Tmin=(408.597,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -28.40 kcal/mol
S298: 85.36 cal/mol/K

Coordinates (Angstoms):
F 0.28865 -1.21383 1.09427
F 0.28866 -1.21384 -1.09425
O 1.26479 1.75377 0.00000
C 0.10580 -0.44600 0.00000
C -1.20283 0.17836 -0.00001
C 1.32008 0.58406 0.00000
C -2.24591 0.77240 -0.00001
H -3.17692 1.28601 -0.00002

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 35.4,127.6,183.3,312.2,396.0,400.9,490.0,567.6,625.7,665.0,696.8,711.5,967.1,1132.5,1218.8,1963.5,2235.7,3492.2
""",
    rank = 5,
)

entry(
    index = 108,
    label = "F[C]1CO1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {4,S}
2 O u0 p2 c0 {3,S} {4,S}
3 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
4 C u1 p0 c0 {1,S} {2,S} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0833,-0.00721118,9.09117e-05,-1.49953e-07,7.93911e-11,-6880.04,8.78012], Tmin=(10,'K'), Tmax=(604.187,'K')),
            NASAPolynomial(coeffs=[2.03214,0.0205895,-1.34147e-05,4.11922e-09,-4.80386e-13,-6891.75,15.4942], Tmin=(604.187,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -10.81 kcal/mol
S298: 65.11 cal/mol/K

Coordinates (Angstoms):
F -1.42905 -0.14172 0.10938
O 0.65679 0.84734 0.12453
C 1.01455 -0.59701 0.04457
C -0.22469 -0.00235 -0.43569
H 1.05733 -1.07417 1.02068
H 1.81071 -0.83295 -0.65463

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 404.7,505.3,738.0,905.9,985.3,1087.9,1145.5,1179.9,1408.3,1520.4,3111.3,3214.4
""",
    rank = 5,
)

entry(
    index = 109,
    label = "ODCDC(O)C(F)(F)F",
    molecule = 
"""
1 F u0 p3 c0 {6,S}
2 F u0 p3 c0 {6,S}
3 F u0 p3 c0 {6,S}
4 O u0 p2 c0 {7,S} {9,S}
5 O u0 p2 c0 {8,D}
6 C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
7 C u0 p0 c0 {4,S} {6,S} {8,D}
8 C u0 p0 c0 {5,D} {7,D}
9 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61088,0.0326598,5.58763e-05,-2.26713e-07,1.91247e-10,-102050,12.3685], Tmin=(10,'K'), Tmax=(462.698,'K')),
            NASAPolynomial(coeffs=[6.8465,0.0307158,-2.21994e-05,7.35446e-09,-9.08719e-13,-102628,-3.75862], Tmin=(462.698,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -197.50 kcal/mol
S298: 86.50 cal/mol/K

Coordinates (Angstoms):
F -0.57693 -1.54651 -0.10819
F -1.52801 -0.02181 1.11061
F -1.57241 0.15777 -1.03035
O 0.46979 1.89733 0.11696
O 2.64846 -0.70627 -0.00508
C -0.80233 -0.22850 0.00567
C 0.48772 0.52034 0.01683
C 1.63620 -0.14114 -0.00610
H 0.22064 2.26234 -0.74208

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 59.2,138.4,162.7,219.2,319.0,401.9,435.4,482.2,535.2,574.7,601.2,709.3,772.0,1097.0,1165.2,1200.8,1252.2,1349.5,1435.7,2237.7,3752.8
""",
    rank = 5,
)

entry(
    index = 110,
    label = "ODC([CH]O)C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {6,S}
3  F u0 p3 c0 {6,S}
4  O u0 p2 c0 {8,S} {10,S}
5  O u0 p2 c0 {7,D}
6  C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
7  C u0 p0 c0 {5,D} {6,S} {8,S}
8  C u1 p0 c0 {4,S} {7,S} {9,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.66288,0.029119,5.05447e-05,-1.50619e-07,1.00705e-10,-107734,13.5099], Tmin=(10,'K'), Tmax=(560.062,'K')),
            NASAPolynomial(coeffs=[5.85244,0.0352424,-2.41386e-05,7.65659e-09,-9.14081e-13,-108320,1.1689], Tmin=(560.062,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -208.96 kcal/mol
S298: 87.77 cal/mol/K

Coordinates (Angstoms):
F 1.59348 -0.40978 -1.07953
F 1.13117 1.41278 -0.00067
F 1.59321 -0.40864 1.08020
O -2.75144 0.32835 -0.00009
O -0.84378 -1.49968 0.00023
C 0.97904 0.07689 -0.00000
C -0.50262 -0.30645 0.00002
C -1.48830 0.71237 -0.00016
H -1.31145 1.77778 -0.00037
H -2.71625 -0.65327 0.00009

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 31.0,159.8,192.3,302.1,326.1,366.9,424.2,512.0,582.8,648.8,734.9,751.5,853.0,882.4,1116.0,1199.0,1206.1,1214.8,1336.0,1391.5,1559.6,1579.0,3254.3,3524.4
""",
    rank = 5,
)

entry(
    index = 111,
    label = "[O]OCDCDC(F)F",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {6,S}
2 F u0 p3 c0 {6,S}
3 O u0 p2 c0 {4,S} {5,S}
4 O u1 p2 c0 {3,S}
5 C u0 p0 c0 {3,S} {7,D} {8,S}
6 C u0 p0 c0 {1,S} {2,S} {7,D}
7 C u0 p0 c0 {5,D} {6,D}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63909,0.034529,-2.60251e-05,5.50585e-09,1.39872e-12,-14744.9,12.4608], Tmin=(10,'K'), Tmax=(895.655,'K')),
            NASAPolynomial(coeffs=[8.56669,0.0192981,-1.18648e-05,3.41232e-09,-3.74554e-13,-15899.4,-12.2862], Tmin=(895.655,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -24.53 kcal/mol
S298: 84.21 cal/mol/K

Coordinates (Angstoms):
F -2.22089 1.07565 -0.10645
F -2.22084 -1.07568 -0.10644
O 2.00994 -0.00000 -0.50636
O 3.24917 -0.00000 -0.04810
C 1.07249 0.00001 0.52417
C -1.47859 0.00000 0.02770
C -0.20048 0.00003 0.25624
H 1.54217 0.00000 1.50311

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 84.4,93.9,156.1,288.1,405.1,433.8,595.7,599.0,630.6,890.2,896.9,999.9,1180.8,1269.1,1290.9,1499.2,2101.8,3180.5
""",
    rank = 5,
)

entry(
    index = 112,
    label = "ODC(F)OO",
    molecule = 
"""
1 F u0 p3 c0 {5,S}
2 O u0 p2 c0 {3,S} {5,S}
3 O u0 p2 c0 {2,S} {6,S}
4 O u0 p2 c0 {5,D}
5 C u0 p0 c0 {1,S} {2,S} {4,D}
6 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92212,0.00493879,7.38492e-05,-1.69733e-07,1.14297e-10,-62737,9.3347], Tmin=(10,'K'), Tmax=(510.617,'K')),
            NASAPolynomial(coeffs=[4.17798,0.0187211,-1.30128e-05,4.22274e-09,-5.16224e-13,-62969,6.25709], Tmin=(510.617,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -121.18 kcal/mol
S298: 69.87 cal/mol/K

Coordinates (Angstoms):
F 1.60024 -0.53675 -0.00002
O -0.51797 -0.77829 0.00000
O -1.79418 -0.12026 0.00001
O 0.35289 1.30831 0.00002
C 0.46584 0.12154 -0.00000
H -1.52300 0.82341 0.00004

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 202.3,337.0,367.6,533.7,689.5,771.8,946.9,1067.2,1322.2,1518.8,1896.6,3543.6
""",
    rank = 5,
)

entry(
    index = 113,
    label = "FC1(F)[C]DC1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
4 C u0 p0 c0 {3,S} {5,D} {6,S}
5 C u1 p0 c0 {3,S} {4,D}
6 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.94042,0.00332616,6.51123e-05,-1.21761e-07,6.69658e-11,8577.56,9.31645], Tmin=(10,'K'), Tmax=(613.804,'K')),
            NASAPolynomial(coeffs=[3.31003,0.0220561,-1.6392e-05,5.57215e-09,-7.03772e-13,8379.51,9.80628], Tmin=(613.804,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (133.032,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 20.40 kcal/mol
S298: 68.97 cal/mol/K

Coordinates (Angstoms):
F -0.88755 1.07471 0.05187
F -0.88760 -1.07468 0.05188
C -0.10567 -0.00000 -0.06337
C 1.30919 -0.00003 0.48118
C 1.15255 -0.00002 -0.80964
H 1.84000 0.00008 1.41724

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 333.8,461.9,503.1,541.0,746.1,793.4,851.8,958.5,1193.4,1287.2,1692.2,3303.1
""",
    rank = 5,
)

entry(
    index = 114,
    label = "[O]C(F)(F)C1(CDO)OO1",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {8,S}
2  F u0 p3 c0 {8,S}
3  O u0 p2 c0 {4,S} {7,S}
4  O u0 p2 c0 {3,S} {7,S}
5  O u1 p2 c0 {8,S}
6  O u0 p2 c0 {9,D}
7  C u0 p0 c0 {3,S} {4,S} {8,S} {9,S}
8  C u0 p0 c0 {1,S} {2,S} {5,S} {7,S}
9  C u0 p0 c0 {6,D} {7,S} {10,S}
10 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.50543,0.0479269,-3.40064e-05,2.13886e-09,5.08114e-12,-56793.3,13.7218], Tmin=(10,'K'), Tmax=(847.45,'K')),
            NASAPolynomial(coeffs=[10.4752,0.0266896,-1.70554e-05,5.04035e-09,-5.64586e-13,-58393.3,-21.2202], Tmin=(847.45,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -107.14 kcal/mol
S298: 92.39 cal/mol/K

Coordinates (Angstoms):
F -1.85016 0.80043 -0.26960
F -1.11658 -1.16032 -0.96057
O 0.63188 1.44435 0.76101
O 0.78787 1.33835 -0.72293
O -1.44346 -0.79788 1.16528
O 2.57343 -0.77492 -0.16923
C 0.42952 0.26541 0.05739
C -1.02540 -0.20896 -0.00571
C 1.46308 -0.84564 0.26983
H 1.09959 -1.70521 0.86936

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 43.1,75.0,164.2,191.3,267.0,312.6,376.5,398.4,445.7,578.2,610.8,714.2,754.0,865.9,940.1,1001.9,1052.7,1133.1,1228.3,1285.3,1411.4,1450.9,1853.8,2933.5
""",
    rank = 5,
)

entry(
    index = 115,
    label = "CDCDCO[O]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 C u0 p0 c0 {1,S} {5,D} {6,S}
4 C u0 p0 c0 {5,D} {7,S} {8,S}
5 C u0 p0 c0 {3,D} {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.82887,0.0145545,4.55269e-05,-1.14629e-07,7.80082e-11,29358.8,9.99716], Tmin=(10,'K'), Tmax=(493.38,'K')),
            NASAPolynomial(coeffs=[3.41252,0.0265279,-1.70151e-05,5.19968e-09,-6.07504e-13,29295.2,10.6512], Tmin=(493.38,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 62.32 kcal/mol
S298: 74.15 cal/mol/K

Coordinates (Angstoms):
O -1.06571 -0.49591 -0.00005
O -2.28238 0.01589 -0.00009
C -0.07959 0.49090 0.00001
C 2.44274 -0.15792 0.00009
C 1.18227 0.15650 0.00005
H -0.48010 1.49731 0.00001
H 2.99617 -0.29706 -0.92580
H 2.99611 -0.29709 0.92601

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 102.4,176.5,316.0,469.1,569.1,601.9,876.3,927.4,996.7,1013.7,1134.6,1190.5,1338.4,1475.0,2059.9,3118.3,3190.4,3207.4
""",
    rank = 5,
)

entry(
    index = 116,
    label = "[O]OC(O)([C]DO)C(F)(F)F",
    molecule = 
"""
multiplicity 3
1  F u0 p3 c0 {9,S}
2  F u0 p3 c0 {9,S}
3  F u0 p3 c0 {9,S}
4  O u0 p2 c0 {6,S} {8,S}
5  O u0 p2 c0 {8,S} {11,S}
6  O u1 p2 c0 {4,S}
7  O u0 p2 c0 {10,D}
8  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
9  C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
10 C u1 p0 c0 {7,D} {8,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.24577,0.0659153,-4.75547e-05,-4.52443e-08,6.30138e-11,-94560.7,14.9314], Tmin=(10,'K'), Tmax=(527.179,'K')),
            NASAPolynomial(coeffs=[10.2244,0.035585,-2.56185e-05,8.40937e-09,-1.02891e-12,-95610.8,-17.2501], Tmin=(527.179,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (257.749,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -181.13 kcal/mol
S298: 100.71 cal/mol/K

Coordinates (Angstoms):
F -1.79489 -0.99840 0.53689
F -1.71050 1.16510 0.45596
F -1.47877 0.00122 -1.35712
O 0.80081 -1.16314 -0.62607
O 0.58022 -0.11382 1.48263
O 1.96169 -1.54698 -0.16396
O 2.00304 1.70280 -0.15966
C 0.30681 0.01100 0.16901
C -1.21334 0.03779 -0.05392
C 0.99789 1.22469 -0.54196
H 1.54318 -0.18299 1.57613

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 51.7,73.6,103.8,156.2,183.7,256.0,278.2,326.3,355.3,361.1,407.8,425.8,551.1,570.3,612.2,728.7,758.1,831.0,950.8,1185.9,1224.5,1238.5,1248.5,1271.1,1459.1,1944.9,3732.2
""",
    rank = 5,
)

entry(
    index = 117,
    label = "[O]C(F)(F)CBr",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {6,S}
2 F  u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 O  u1 p2 c0 {5,S}
5 C  u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
6 C  u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
7 H  u0 p0 c0 {6,S}
8 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.77604,0.0185751,6.13654e-05,-1.68179e-07,1.17491e-10,-53163.6,13.203], Tmin=(10,'K'), Tmax=(518.76,'K')),
            NASAPolynomial(coeffs=[5.13219,0.0272377,-1.89669e-05,6.10373e-09,-7.37404e-13,-53561.6,5.07082], Tmin=(518.76,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -101.25 kcal/mol
S298: 82.91 cal/mol/K

Coordinates (Angstoms):
Br 1.49589 -0.03526 0.00000
F -1.31151 -0.80294 1.08253
F -1.31159 -0.80286 -1.08258
O -2.41256 0.81015 0.00007
C -1.36999 0.00561 0.00001
C -0.14818 0.99467 -0.00001
H -0.16931 1.60167 0.90041
H -0.16931 1.60164 -0.90045

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 67.4,157.2,288.7,311.3,526.8,528.6,597.3,666.8,748.4,867.2,948.3,1060.6,1224.9,1232.9,1246.1,1440.4,3132.2,3215.3
""",
    rank = 5,
)

entry(
    index = 118,
    label = "CDCDC[C]DO",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {5,D}
2 C u0 p0 c0 {4,D} {5,S} {6,S}
3 C u0 p0 c0 {4,D} {7,S} {8,S}
4 C u0 p0 c0 {2,D} {3,D}
5 C u1 p0 c0 {1,D} {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.88731,0.00912491,9.60575e-05,-2.72121e-07,2.34293e-10,25257.6,9.78344], Tmin=(10,'K'), Tmax=(378.033,'K')),
            NASAPolynomial(coeffs=[3.2921,0.0265401,-1.71562e-05,5.32505e-09,-6.32847e-13,25223.2,11.0253], Tmin=(378.033,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 54.14 kcal/mol
S298: 73.48 cal/mol/K

Coordinates (Angstoms):
O 2.37208 -0.15156 -0.00005
C 0.09010 0.56310 0.00002
C -2.38829 -0.24738 0.00004
C -1.15683 0.15719 0.00003
C 1.21111 -0.40031 -0.00004
H 0.33460 1.62597 0.00005
H -2.92390 -0.42459 0.92809
H -2.92393 -0.42452 -0.92800

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 135.5,168.8,388.8,438.1,540.9,553.3,875.2,878.2,978.1,994.9,1117.9,1296.1,1449.7,1880.0,2052.4,3108.0,3137.4,3213.2
""",
    rank = 5,
)

entry(
    index = 119,
    label = "[CH2]C(C)(Br)C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  Br u0 p3 c0 {5,S}
2  F  u0 p3 c0 {7,S}
3  F  u0 p3 c0 {7,S}
4  F  u0 p3 c0 {7,S}
5  C  u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6  C  u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
7  C  u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
8  C  u1 p0 c0 {5,S} {12,S} {13,S}
9  H  u0 p0 c0 {6,S}
10 H  u0 p0 c0 {6,S}
11 H  u0 p0 c0 {6,S}
12 H  u0 p0 c0 {8,S}
13 H  u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.61432,0.0317023,0.000190066,-6.73218e-07,6.48969e-10,-72779.9,14.5943], Tmin=(10,'K'), Tmax=(372.899,'K')),
            NASAPolynomial(coeffs=[5.88606,0.0471428,-3.21774e-05,1.03924e-08,-1.27105e-12,-73226.1,2.1642], Tmin=(372.899,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (307.635,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -138.39 kcal/mol
S298: 96.21 cal/mol/K

Coordinates (Angstoms):
Br 1.62407 -0.29358 -0.03427
F -1.17460 -1.01994 -1.18752
F -2.49678 0.19600 0.00978
F -1.22381 -1.26951 0.96118
C -0.21924 0.72998 0.12841
C -0.25780 1.71667 -1.03003
C -1.27733 -0.37393 -0.02633
C -0.20109 1.30101 1.45360
H -0.14045 1.20567 -1.98595
H 0.53895 2.45400 -0.92176
H -1.22228 2.23513 -1.02266
H 0.24671 2.27394 1.61102
H -0.47585 0.70521 2.31381

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 73.5,145.0,199.2,224.9,242.8,252.5,275.5,334.3,369.6,422.6,460.6,572.3,578.3,599.5,704.3,775.4,909.9,988.9,1062.6,1145.6,1188.1,1217.2,1279.8,1334.3,1407.0,1461.9,1482.9,1491.4,3049.4,3127.4,3156.1,3168.2,3280.6
""",
    rank = 5,
)

entry(
    index = 120,
    label = "[O]OC(O)(CDO)C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {9,S}
2  F u0 p3 c0 {9,S}
3  F u0 p3 c0 {9,S}
4  O u0 p2 c0 {7,S} {8,S}
5  O u0 p2 c0 {8,S} {12,S}
6  O u0 p2 c0 {10,D}
7  O u1 p2 c0 {4,S}
8  C u0 p0 c0 {4,S} {5,S} {9,S} {10,S}
9  C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
10 C u0 p0 c0 {6,D} {8,S} {11,S}
11 H u0 p0 c0 {10,S}
12 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.34495,0.0569868,-9.92532e-06,-8.59906e-08,7.39234e-11,-115408,14.5743], Tmin=(10,'K'), Tmax=(560.51,'K')),
            NASAPolynomial(coeffs=[8.81554,0.0409164,-2.8389e-05,9.08206e-09,-1.09074e-12,-116382,-11.8699], Tmin=(560.51,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -222.77 kcal/mol
S298: 98.48 cal/mol/K

Coordinates (Angstoms):
F -1.93330 0.00195 0.82990
F -1.34003 0.52238 -1.18542
F -1.19206 -1.52883 -0.51642
O 0.54124 1.37893 0.76045
O 0.61726 -0.79515 1.44789
O 2.33648 -1.07255 -0.50623
O 0.60748 2.20009 -0.26788
C 0.38771 -0.03635 0.35051
C -1.06136 -0.25259 -0.13577
C 1.43288 -0.32083 -0.75499
H 1.31564 0.20382 -1.71332
H 1.49791 -1.19519 1.32850

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 39.1,77.5,123.1,198.0,213.8,267.0,300.9,314.6,364.9,386.1,494.0,510.3,539.3,570.5,617.8,733.7,825.4,885.0,981.2,1046.2,1183.7,1214.6,1227.1,1263.1,1335.1,1364.9,1440.1,1827.1,3049.7,3633.6
""",
    rank = 5,
)

entry(
    index = 121,
    label = "CDC(O[O])C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {6,S}
3  F u0 p3 c0 {6,S}
4  O u0 p2 c0 {5,S} {7,S}
5  O u1 p2 c0 {4,S}
6  C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
7  C u0 p0 c0 {4,S} {6,S} {8,D}
8  C u0 p0 c0 {7,D} {9,S} {10,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.63684,0.0315994,4.29624e-05,-1.38938e-07,9.33166e-11,-69508.7,13.1313], Tmin=(10,'K'), Tmax=(569.735,'K')),
            NASAPolynomial(coeffs=[6.31256,0.0349368,-2.40701e-05,7.6544e-09,-9.14773e-13,-70172.7,-1.4233], Tmin=(569.735,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -132.89 kcal/mol
S298: 87.70 cal/mol/K

Coordinates (Angstoms):
F 1.17991 -0.83502 -1.07912
F 1.75720 0.95207 -0.00011
F 1.17997 -0.83492 1.07911
O -1.34979 -0.73201 0.00025
O -2.63594 -0.45404 0.00016
C 0.92118 -0.08875 -0.00004
C -0.51364 0.38186 -0.00002
C -0.91155 1.64462 -0.00020
H -0.17828 2.43785 -0.00040
H -1.96561 1.88507 -0.00017

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 56.5,104.5,196.9,242.6,340.8,395.2,420.6,495.0,575.9,667.9,680.2,746.7,811.6,901.3,950.2,1132.3,1196.3,1199.8,1226.5,1313.1,1414.0,1705.7,3195.9,3297.1
""",
    rank = 5,
)

entry(
    index = 122,
    label = "[CH2]C(DC)O[O]",
    molecule = 
"""
multiplicity 3
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 C u0 p0 c0 {1,S} {4,S} {5,D}
4 C u1 p0 c0 {3,S} {6,S} {7,S}
5 C u0 p0 c0 {3,D} {8,S} {9,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89885,0.00605457,0.000108771,-2.23925e-07,1.37096e-10,24577.2,10.4413], Tmin=(10,'K'), Tmax=(552.735,'K')),
            NASAPolynomial(coeffs=[3.57237,0.0311169,-2.08443e-05,6.70671e-09,-8.23194e-13,24266.5,8.68609], Tmin=(552.735,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 52.84 kcal/mol
S298: 74.68 cal/mol/K

Coordinates (Angstoms):
O -0.67378 -0.74219 -0.00000
O -1.81563 -0.09715 -0.00010
C 0.48760 0.06028 0.00002
C 1.64117 -0.70066 0.00008
C 0.37699 1.43495 0.00000
H 1.58859 -1.78104 0.00010
H 2.60904 -0.21910 0.00011
H 1.27512 2.03716 0.00002
H -0.59201 1.91028 -0.00004

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 110.0,349.1,398.9,499.4,528.6,584.7,591.1,737.7,782.0,827.2,954.2,1004.8,1218.5,1285.6,1362.1,1476.2,1491.3,3180.0,3191.1,3285.3,3301.9
""",
    rank = 5,
)

entry(
    index = 123,
    label = "FC1[CH]C(F)(F)OO1",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {7,S}
3  F u0 p3 c0 {7,S}
4  O u0 p2 c0 {5,S} {7,S}
5  O u0 p2 c0 {4,S} {6,S}
6  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
7  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
8  C u1 p0 c0 {6,S} {7,S} {10,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83093,0.0106478,0.000155524,-3.55933e-07,2.37202e-10,-69942.5,12.8916], Tmin=(10,'K'), Tmax=(517.42,'K')),
            NASAPolynomial(coeffs=[4.46356,0.0400006,-2.88413e-05,9.5176e-09,-1.17095e-12,-70466.4,5.82682], Tmin=(517.42,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -134.23 kcal/mol
S298: 83.71 cal/mol/K

Coordinates (Angstoms):
F 2.21286 -0.69802 -0.30204
F -1.57878 -1.01911 -0.71620
F -1.86188 0.54570 0.74072
O -0.28857 0.75488 -0.88313
O 0.92337 1.19945 -0.19814
C 1.40263 0.07880 0.49185
C -0.92369 -0.10783 0.01712
C 0.16896 -0.65290 0.86994
H 2.01459 0.47239 1.31073
H 0.06975 -1.47255 1.56374

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 78.0,160.8,278.2,302.9,409.7,468.7,510.6,541.8,597.2,683.3,818.8,888.1,905.6,943.9,1019.3,1044.8,1114.8,1154.5,1213.8,1342.4,1360.1,1368.5,3069.2,3269.6
""",
    rank = 5,
)

entry(
    index = 124,
    label = "[CH]DC(Br)C(DO)O",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {4,S}
2 O  u0 p2 c0 {5,S} {8,S}
3 O  u0 p2 c0 {5,D}
4 C  u0 p0 c0 {1,S} {5,S} {6,D}
5 C  u0 p0 c0 {2,S} {3,D} {4,S}
6 C  u1 p0 c0 {4,D} {7,S}
7 H  u0 p0 c0 {6,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.79899,0.0147027,0.000120864,-3.64993e-07,3.04939e-10,-7679.5,13.2112], Tmin=(10,'K'), Tmax=(430.875,'K')),
            NASAPolynomial(coeffs=[5.72788,0.0257259,-1.82234e-05,6.03516e-09,-7.49742e-13,-8114.27,2.41311], Tmin=(430.875,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -10.74 kcal/mol
S298: 83.43 cal/mol/K

Coordinates (Angstoms):
Br -1.40785 -0.16768 0.00014
O 2.66772 0.29304 -0.00018
O 1.35694 -1.53824 -0.00027
C 0.35234 0.64065 -0.00001
C 1.47907 -0.34406 -0.00017
C 0.47334 1.93393 0.00001
H -0.09587 2.84723 0.00009
H 3.34495 -0.40012 -0.00030

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 58.1,182.6,295.3,327.8,333.7,565.6,593.0,632.6,710.6,730.9,789.2,916.7,1175.2,1364.5,1668.1,1835.5,3310.4,3751.5
""",
    rank = 5,
)

entry(
    index = 125,
    label = "CDC(F)C(F)(F)O[O]",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {6,S}
3  F u0 p3 c0 {7,S}
4  O u0 p2 c0 {5,S} {6,S}
5  O u1 p2 c0 {4,S}
6  C u0 p0 c0 {1,S} {2,S} {4,S} {7,S}
7  C u0 p0 c0 {3,S} {6,S} {8,D}
8  C u0 p0 c0 {7,D} {9,S} {10,S}
9  H u0 p0 c0 {8,S}
10 H u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6031,0.0345283,3.06441e-05,-1.20135e-07,8.33145e-11,-66487.9,13.1761], Tmin=(10,'K'), Tmax=(569.141,'K')),
            NASAPolynomial(coeffs=[6.57921,0.0343658,-2.36258e-05,7.50549e-09,-8.96545e-13,-67162.8,-2.45749], Tmin=(569.141,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -126.80 kcal/mol
S298: 88.35 cal/mol/K

Coordinates (Angstoms):
F 0.51331 -1.61147 -0.48446
F 0.76425 -0.50362 1.37078
F -1.45306 0.08265 -1.27086
O 1.30424 0.41312 -0.61739
O 1.28479 1.64099 -0.14175
C 0.36574 -0.42567 0.10422
C -1.04756 0.07576 -0.00309
C -1.80285 0.45526 1.01049
H -1.40838 0.42815 2.01557
H -2.81632 0.79883 0.84871

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 50.3,97.9,200.0,232.4,304.7,366.7,431.5,512.2,540.0,593.5,722.3,751.5,760.2,924.8,964.2,1015.1,1184.3,1205.2,1255.1,1372.6,1416.7,1759.3,3189.0,3289.5
""",
    rank = 5,
)

entry(
    index = 126,
    label = "FC1[C]C1(F)F",
    molecule = 
"""
multiplicity 3
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
6 C u2 p0 c0 {4,S} {5,S}
7 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89778,0.00619726,9.54933e-05,-2.07348e-07,1.30864e-10,-6394.61,11.342], Tmin=(10,'K'), Tmax=(546.859,'K')),
            NASAPolynomial(coeffs=[4.28763,0.0255864,-1.86948e-05,6.22719e-09,-7.71951e-13,-6769.81,6.65579], Tmin=(546.859,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -8.87 kcal/mol
S298: 75.64 cal/mol/K

Coordinates (Angstoms):
F 1.87341 0.32239 -0.32567
F -0.72445 1.29831 0.13666
F -1.60631 -0.58232 -0.48802
C 0.90376 -0.59007 -0.13385
C -0.58505 -0.02068 0.14899
C 0.20403 -0.70983 1.13986
H 0.97971 -1.42195 -0.83668

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 182.9,224.3,366.1,511.6,553.4,596.1,715.9,849.3,957.8,1021.3,1165.0,1234.2,1296.5,1415.3,3102.4
""",
    rank = 5,
)

entry(
    index = 127,
    label = "[O]OC1C(F)OOC1(F)F",
    molecule = 
"""
multiplicity 2
1  F u0 p3 c0 {9,S}
2  F u0 p3 c0 {10,S}
3  F u0 p3 c0 {10,S}
4  O u0 p2 c0 {5,S} {9,S}
5  O u0 p2 c0 {4,S} {10,S}
6  O u0 p2 c0 {7,S} {8,S}
7  O u1 p2 c0 {6,S}
8  C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
9  C u0 p0 c0 {1,S} {4,S} {8,S} {12,S}
10 C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {9,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.60699,0.0409425,2.42701e-05,-8.61574e-08,4.77346e-11,-85323.9,14.172], Tmin=(10,'K'), Tmax=(729.604,'K')),
            NASAPolynomial(coeffs=[8.36417,0.040284,-2.66422e-05,8.12071e-09,-9.34083e-13,-86694.8,-11.9161], Tmin=(729.604,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -163.68 kcal/mol
S298: 94.06 cal/mol/K

Coordinates (Angstoms):
F -2.16120 -0.93481 0.79338
F 1.28076 1.11339 -0.82380
F 0.67286 1.57439 1.19968
O -1.49015 0.25320 -1.03423
O -0.90457 1.36692 -0.30072
O 1.07165 -1.43556 -0.38566
O 2.27193 -1.38704 0.15499
C 0.14335 -0.62854 0.35651
C -1.25604 -0.85392 -0.21935
C 0.34582 0.88994 0.10434
H 0.22009 -0.86767 1.41629
H -1.34161 -1.73403 -0.86361

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 38.4,86.3,175.1,189.8,261.1,316.4,373.3,400.7,486.5,526.2,579.3,632.3,682.4,800.7,861.1,915.9,986.7,1025.1,1065.5,1110.4,1128.7,1188.9,1197.7,1230.8,1284.8,1329.4,1360.6,1381.9,3093.9,3139.5
""",
    rank = 5,
)

entry(
    index = 128,
    label = "FC(F)(F)[C]CBr",
    molecule = 
"""
1 Br u0 p3 c0 {6,S}
2 F  u0 p3 c0 {5,S}
3 F  u0 p3 c0 {5,S}
4 F  u0 p3 c0 {5,S}
5 C  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
6 C  u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
7 C  u0 p1 c0 {5,S} {6,S}
8 H  u0 p0 c0 {6,S}
9 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.5523,0.0395859,-1.57655e-05,-2.91514e-08,2.52847e-11,-35763.6,14.3361], Tmin=(10,'K'), Tmax=(645.742,'K')),
            NASAPolynomial(coeffs=[7.69853,0.0273131,-1.84088e-05,5.73889e-09,-6.74378e-13,-36578.7,-6.01861], Tmin=(645.742,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -65.84 kcal/mol
S298: 90.34 cal/mol/K

Coordinates (Angstoms):
Br -2.25465 -0.06777 -0.01316
F 2.20940 1.23280 0.26211
F 2.20935 -0.79162 1.06611
F 2.90724 -0.38547 -0.96459
C 2.00081 -0.06463 -0.04936
C -0.36455 0.47864 0.01115
C 0.59992 -0.47674 -0.44793
H -0.24270 1.20332 -0.82773
H -0.19569 1.04373 0.93263

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 58.3,105.3,148.6,211.8,336.3,383.2,427.5,548.4,556.0,599.3,718.9,831.1,942.7,1114.3,1138.2,1191.0,1232.2,1271.3,1312.7,2906.1,3074.1
""",
    rank = 5,
)

entry(
    index = 129,
    label = "BrCD[C]C1OO1",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {5,S}
2 O  u0 p2 c0 {3,S} {4,S}
3 O  u0 p2 c0 {2,S} {4,S}
4 C  u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
5 C  u0 p0 c0 {1,S} {6,D} {8,S}
6 C  u1 p0 c0 {4,S} {5,D}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.73846,0.0307277,-2.18461e-05,6.26287e-09,-3.13964e-13,37068.7,13.8095], Tmin=(10,'K'), Tmax=(1161.81,'K')),
            NASAPolynomial(coeffs=[9.6963,0.0151771,-8.17482e-06,2.09383e-09,-2.07823e-13,35349.5,-17.2683], Tmin=(1161.81,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 78.23 kcal/mol
S298: 86.14 cal/mol/K

Coordinates (Angstoms):
Br -1.77932 -0.22157 0.00002
O 2.98517 -0.18847 -0.74542
O 2.98531 -0.18816 0.74535
C 1.81434 -0.29586 0.00010
C -0.37226 1.13013 -0.00009
C 0.88516 0.82044 -0.00003
H 1.34356 -1.28585 0.00035
H -0.79454 2.12565 -0.00019

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 29.8,87.6,214.4,291.5,522.6,530.4,567.8,760.0,826.4,879.7,951.8,1129.4,1167.7,1286.0,1384.1,1767.6,3051.7,3223.9
""",
    rank = 5,
)

entry(
    index = 130,
    label = "[C]DC(F)F",
    molecule = 
"""
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,D}
4 C u0 p1 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[4.0034,-0.00170153,6.62144e-05,-1.46515e-07,1.00196e-10,14006.2,7.56617], Tmin=(10,'K'), Tmax=(491.989,'K')),
            NASAPolynomial(coeffs=[3.91032,0.0108368,-7.93332e-06,2.63178e-09,-3.24409e-13,13872.8,6.50008], Tmin=(491.989,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 30.73 kcal/mol
S298: 63.02 cal/mol/K

Coordinates (Angstoms):
F 1.09661 -0.55610 0.00000
F -1.09661 -0.55610 0.00000
C 0.00000 0.16163 0.00000
C -0.00000 1.50667 0.00000

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 299.0,511.6,596.8,952.5,1298.6,1720.2
""",
    rank = 5,
)

entry(
    index = 131,
    label = "C#CCO[O]",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u1 p2 c0 {1,S}
3 C u0 p0 c0 {1,S} {4,S} {6,S} {7,S}
4 C u0 p0 c0 {3,S} {5,T}
5 C u0 p0 c0 {4,T} {8,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92509,0.00875061,0.000179553,-9.26497e-07,1.64698e-09,30257.8,10.0736], Tmin=(10,'K'), Tmax=(141.455,'K')),
            NASAPolynomial(coeffs=[3.26534,0.0274063,-1.82695e-05,5.81168e-09,-7.04153e-13,30276.5,11.9662], Tmin=(141.455,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 64.22 kcal/mol
S298: 75.46 cal/mol/K

Coordinates (Angstoms):
O 0.96132 -0.51537 0.00000
O 2.20267 -0.09728 0.00001
C 0.04037 0.63223 0.00000
C -1.32090 0.14071 -0.00000
C -2.45183 -0.26190 -0.00001
H 0.26775 1.22598 -0.89034
H 0.26774 1.22598 0.89036
H -3.45323 -0.61697 -0.00002

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 62.2,169.2,326.2,433.8,504.2,628.7,701.6,919.3,984.2,998.3,1205.0,1209.8,1363.0,1469.6,2247.7,3052.5,3101.4,3500.3
""",
    rank = 5,
)

entry(
    index = 132,
    label = "ODC(F)CBr",
    molecule = 
"""
1 Br u0 p3 c0 {4,S}
2 F  u0 p3 c0 {5,S}
3 O  u0 p2 c0 {5,D}
4 C  u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
5 C  u0 p0 c0 {2,S} {3,D} {4,S}
6 H  u0 p0 c0 {4,S}
7 H  u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.84178,0.018638,-3.05665e-07,-1.27686e-08,6.19568e-12,-48741.6,12.5489], Tmin=(10,'K'), Tmax=(929.657,'K')),
            NASAPolynomial(coeffs=[5.94913,0.0170427,-9.78742e-06,2.67622e-09,-2.82568e-13,-49456.3,0.799351], Tmin=(929.657,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -92.99 kcal/mol
S298: 79.24 cal/mol/K

Coordinates (Angstoms):
Br 1.30271 0.03196 -0.11662
F -1.60462 1.23763 0.15452
O -2.40153 -0.70515 -0.52202
C -0.33341 -0.65896 0.71391
C -1.55283 -0.09437 0.03513
H -0.32458 -1.74028 0.61299
H -0.29888 -0.35577 1.75997

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 53.9,160.0,384.9,524.7,632.9,753.3,862.6,909.6,1118.0,1235.9,1259.6,1455.0,1911.8,3110.1,3197.4
""",
    rank = 5,
)

entry(
    index = 133,
    label = "FC1(F)[C]DCOO1",
    molecule = 
"""
multiplicity 2
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 O u0 p2 c0 {4,S} {5,S}
4 O u0 p2 c0 {3,S} {6,S}
5 C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
6 C u0 p0 c0 {4,S} {7,D} {8,S}
7 C u1 p0 c0 {5,S} {6,D}
8 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89815,0.00579962,0.000105606,-2.05547e-07,1.17041e-10,-9970.46,11.4876], Tmin=(10,'K'), Tmax=(597.501,'K')),
            NASAPolynomial(coeffs=[3.40064,0.0334911,-2.50691e-05,8.49086e-09,-1.06507e-12,-10345.9,9.99272], Tmin=(597.501,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -15.84 kcal/mol
S298: 76.57 cal/mol/K

Coordinates (Angstoms):
F -1.36572 0.03419 -1.08215
F -1.36581 0.03411 1.08209
O 0.22183 -1.11841 0.00001
O 1.56485 -0.66313 -0.00003
C -0.58856 0.11131 0.00001
C 1.55601 0.67092 0.00003
C 0.31983 1.31307 0.00007
H 2.56662 1.06579 0.00004

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 101.9,319.2,424.8,479.2,507.9,674.7,728.9,766.2,838.6,859.9,880.4,976.4,1113.6,1217.2,1235.7,1296.3,1409.6,3213.3
""",
    rank = 5,
)

entry(
    index = 134,
    label = "ODC(O)[C]DCBr",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {5,S}
2 O  u0 p2 c0 {4,S} {8,S}
3 O  u0 p2 c0 {4,D}
4 C  u0 p0 c0 {2,S} {3,D} {6,S}
5 C  u0 p0 c0 {1,S} {6,D} {7,S}
6 C  u1 p0 c0 {4,S} {5,D}
7 H  u0 p0 c0 {5,S}
8 H  u0 p0 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.62779,0.0331082,-2.69092e-05,8.66677e-09,-9.68967e-14,-7984.67,15.5124], Tmin=(10,'K'), Tmax=(874.749,'K')),
            NASAPolynomial(coeffs=[7.67301,0.0194135,-1.16619e-05,3.3233e-09,-3.63673e-13,-8876.13,-4.51244], Tmin=(874.749,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -11.24 kcal/mol
S298: 89.28 cal/mol/K

Coordinates (Angstoms):
Br 1.69251 -0.17600 0.14797
O -2.91353 0.49473 0.72658
O -2.16124 -1.21523 -0.54812
C -2.03323 -0.09620 -0.10632
C 0.33016 1.02438 -0.54074
C -0.92913 0.76736 -0.43615
H 0.77164 1.90329 -0.99181
H -3.61818 -0.15257 0.88428

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 17.8,70.0,216.7,333.0,508.8,544.2,581.2,593.9,746.5,753.5,822.0,1150.5,1174.9,1363.6,1746.0,1810.7,3211.7,3743.2
""",
    rank = 5,
)

entry(
    index = 135,
    label = "[CH2]C(Br)(Br)C(F)(F)F",
    molecule = 
"""
multiplicity 2
1  Br u0 p3 c0 {6,S}
2  Br u0 p3 c0 {6,S}
3  F  u0 p3 c0 {7,S}
4  F  u0 p3 c0 {7,S}
5  F  u0 p3 c0 {7,S}
6  C  u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
7  C  u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
8  C  u1 p0 c0 {6,S} {9,S} {10,S}
9  H  u0 p0 c0 {8,S}
10 H  u0 p0 c0 {8,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.45432,0.0466269,7.92339e-05,-4.26639e-07,4.37327e-10,-63110,15.8653], Tmin=(10,'K'), Tmax=(396.567,'K')),
            NASAPolynomial(coeffs=[8.84982,0.0331511,-2.46716e-05,8.39927e-09,-1.06166e-12,-63859.9,-9.23394], Tmin=(396.567,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -119.13 kcal/mol
S298: 99.47 cal/mol/K

Coordinates (Angstoms):
Br -1.63963 -0.86541 -0.14335
Br 1.60345 -0.91360 -0.13351
F 1.13917 2.15104 0.19316
F -0.01318 1.41769 -1.48020
F -1.01799 2.18116 0.27729
C 0.04530 0.08502 0.50624
C 0.03651 1.48219 -0.15681
C -0.00048 0.14101 1.95225
H 0.25804 -0.73225 2.53377
H -0.45198 0.99930 2.43395

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 70.9,136.8,139.2,191.1,209.2,252.2,271.4,295.0,311.7,461.9,515.4,582.9,613.4,668.0,689.0,819.8,1071.6,1147.4,1199.8,1238.2,1288.0,1444.6,3170.7,3292.2
""",
    rank = 5,
)

entry(
    index = 136,
    label = "C#CC(Br)O[O]",
    molecule = 
"""
multiplicity 2
1 Br u0 p3 c0 {4,S}
2 O  u0 p2 c0 {3,S} {4,S}
3 O  u1 p2 c0 {2,S}
4 C  u0 p0 c0 {1,S} {2,S} {5,S} {7,S}
5 C  u0 p0 c0 {4,S} {6,T}
6 C  u0 p0 c0 {5,T} {8,S}
7 H  u0 p0 c0 {4,S}
8 H  u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.72586,0.0225814,9.05615e-05,-3.43999e-07,3.27647e-10,34053.3,13.944], Tmin=(10,'K'), Tmax=(392.335,'K')),
            NASAPolynomial(coeffs=[5.93285,0.0255372,-1.80676e-05,5.96977e-09,-7.40669e-13,33684.2,2.86453], Tmin=(392.335,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 72.42 kcal/mol
S298: 86.51 cal/mol/K

Coordinates (Angstoms):
Br -1.19228 -0.48695 -0.03213
O 0.84768 1.39897 -0.43711
O 0.34115 2.47953 0.11082
C 0.60715 0.23478 0.38614
C 1.62929 -0.74088 0.12533
C 2.49829 -1.54301 -0.08176
H 0.54689 0.56744 1.42076
H 3.26401 -2.25744 -0.26415

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 71.7,140.5,186.0,275.7,390.8,459.4,517.6,641.6,669.7,698.7,907.7,1031.3,1183.8,1200.6,1308.8,2243.7,3136.9,3495.6
""",
    rank = 5,
)

entry(
    index = 137,
    label = "OCDC(OO)C(F)(F)F",
    molecule = 
"""
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {7,S}
3  F u0 p3 c0 {7,S}
4  O u0 p2 c0 {6,S} {8,S}
5  O u0 p2 c0 {9,S} {11,S}
6  O u0 p2 c0 {4,S} {12,S}
7  C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
8  C u0 p0 c0 {4,S} {7,S} {9,D}
9  C u0 p0 c0 {5,S} {8,D} {10,S}
10 H u0 p0 c0 {9,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.48447,0.0440309,5.76237e-05,-2.43794e-07,2.02675e-10,-108980,13.2016], Tmin=(10,'K'), Tmax=(468.946,'K')),
            NASAPolynomial(coeffs=[6.91393,0.0431151,-3.00869e-05,9.75425e-09,-1.18827e-12,-109613,-4.0686], Tmin=(468.946,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (282.692,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -210.37 kcal/mol
S298: 93.36 cal/mol/K

Coordinates (Angstoms):
F -1.54052 0.85471 -0.71883
F -1.51027 -1.31900 -0.60477
F -1.73020 -0.12442 1.18827
O 0.91744 0.98563 0.66856
O 2.52705 -1.13933 -0.02316
O 1.09526 1.98056 -0.42029
C -1.10054 -0.20030 0.00650
C 0.38571 -0.16258 0.14821
C 1.20005 -1.18775 -0.14768
H 0.82828 -2.14361 -0.49394
H 2.75797 -0.25296 0.29917
H 0.21338 2.38383 -0.43028

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 51.5,103.9,152.5,178.9,239.6,293.9,307.2,361.5,392.7,430.7,528.6,588.3,645.5,684.6,724.3,807.5,857.2,968.7,1078.3,1150.7,1182.2,1217.5,1338.8,1352.1,1369.2,1399.7,1717.3,3229.1,3709.1,3739.9
""",
    rank = 5,
)

entry(
    index = 138,
    label = "C#CC1OO1",
    molecule = 
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {3,S}
3 C u0 p0 c0 {1,S} {2,S} {4,S} {6,S}
4 C u0 p0 c0 {3,S} {5,T}
5 C u0 p0 c0 {4,T} {7,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.92151,0.0047575,8.20785e-05,-1.73213e-07,1.08288e-10,28490.2,9.02184], Tmin=(10,'K'), Tmax=(543.282,'K')),
            NASAPolynomial(coeffs=[3.80364,0.0228712,-1.55493e-05,5.01727e-09,-6.14436e-13,28248.5,7.17621], Tmin=(543.282,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (157.975,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 60.22 kcal/mol
S298: 69.77 cal/mol/K

Coordinates (Angstoms):
O 1.25788 -0.74540 -0.23942
O 1.25780 0.74549 -0.23930
C 0.34653 -0.00006 0.50646
C -1.03935 -0.00009 0.10634
C -2.20833 0.00005 -0.16755
H 0.52067 -0.00014 1.58487
H -3.23922 0.00006 -0.42664

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 206.7,216.9,525.5,553.0,677.7,691.7,828.0,881.9,971.9,1151.2,1293.4,1415.6,2247.6,3096.2,3496.3
""",
    rank = 5,
)

entry(
    index = 139,
    label = "OC(DCBr)C(F)(F)F",
    molecule = 
"""
1  Br u0 p3 c0 {8,S}
2  F  u0 p3 c0 {6,S}
3  F  u0 p3 c0 {6,S}
4  F  u0 p3 c0 {6,S}
5  O  u0 p2 c0 {7,S} {10,S}
6  C  u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
7  C  u0 p0 c0 {5,S} {6,S} {8,D}
8  C  u0 p0 c0 {1,S} {7,D} {9,S}
9  H  u0 p0 c0 {8,S}
10 H  u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.58925,0.0344914,6.21351e-05,-2.33634e-07,1.89181e-10,-95955.1,13.9931], Tmin=(10,'K'), Tmax=(475.052,'K')),
            NASAPolynomial(coeffs=[6.72164,0.0350992,-2.49845e-05,8.19222e-09,-1.00482e-12,-96557.2,-1.99192], Tmin=(475.052,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (232.805,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -185.16 kcal/mol
S298: 91.00 cal/mol/K

Coordinates (Angstoms):
Br -2.28089 -0.08248 -0.00003
F 2.59458 0.33481 -1.07890
F 2.08878 -1.47281 -0.00015
F 2.59452 0.33454 1.07908
O 0.39050 1.61501 0.00012
C 1.96528 -0.14161 0.00001
C 0.51043 0.27728 0.00002
C -0.46608 -0.62789 -0.00005
H -0.30047 -1.69145 -0.00013
H -0.55122 1.84248 0.00013

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 52.8,135.4,151.6,214.4,298.3,317.0,417.5,434.1,523.8,573.8,667.2,698.7,756.5,759.0,839.5,1097.0,1197.3,1216.4,1253.3,1268.6,1432.5,1717.4,3284.6,3725.0
""",
    rank = 5,
)

entry(
    index = 140,
    label = "FC1C(F)(F)C1(F)F",
    molecule = 
"""
1 F u0 p3 c0 {6,S}
2 F u0 p3 c0 {7,S}
3 F u0 p3 c0 {7,S}
4 F u0 p3 c0 {8,S}
5 F u0 p3 c0 {8,S}
6 C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
7 C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
8 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
9 H u0 p0 c0 {6,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.6936,0.0246357,7.40945e-05,-2.15866e-07,1.55915e-10,-103629,11.8713], Tmin=(10,'K'), Tmax=(507.904,'K')),
            NASAPolynomial(coeffs=[5.7001,0.0333381,-2.39759e-05,7.85027e-09,-9.58322e-13,-104149,0.438988], Tmin=(507.904,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (207.862,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -200.97 kcal/mol
S298: 83.36 cal/mol/K

Coordinates (Angstoms):
F -0.00002 1.96947 -0.63762
F 1.37732 0.27144 1.10906
F 1.41963 -1.31007 -0.43531
F -1.37732 0.27141 1.10905
F -1.41960 -1.31010 -0.43530
C -0.00001 0.64675 -0.88336
C 0.75107 -0.27354 0.07065
C -0.75107 -0.27356 0.07065
H 0.00000 0.37272 -1.93650

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 138.9,145.9,195.3,253.8,286.7,427.9,433.8,534.3,604.1,687.8,790.8,833.6,984.9,1022.2,1198.7,1239.7,1281.1,1301.1,1341.5,1544.3,3145.5
""",
    rank = 5,
)

entry(
    index = 141,
    label = "[C]1DCOOC1",
    molecule = 
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {4,S}
3 C u0 p0 c0 {1,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {2,S} {5,D} {8,S}
5 C u1 p0 c0 {3,S} {4,D}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.97423,0.00160452,8.35186e-05,-1.52693e-07,8.98612e-11,34800.6,10.9445], Tmin=(10,'K'), Tmax=(438.869,'K')),
            NASAPolynomial(coeffs=[0.579353,0.0324763,-2.17571e-05,6.86215e-09,-8.2079e-13,35099.2,24.5347], Tmin=(438.869,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 72.60 kcal/mol
S298: 72.74 cal/mol/K

Coordinates (Angstoms):
O 0.58951 -0.97649 -0.03270
O -0.88311 -0.81253 0.02424
C 1.21031 0.33411 0.02187
C -1.09718 0.53932 -0.00552
C 0.02228 1.23354 -0.02126
H 1.79743 0.42424 0.94758
H 1.87997 0.43005 -0.84328
H -2.14105 0.81597 -0.00716

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 41.9,237.3,705.9,782.0,831.4,847.5,945.4,1005.6,1017.0,1075.1,1151.2,1241.0,1340.0,1520.1,1685.4,2983.6,3023.3,3261.3
""",
    rank = 5,
)

entry(
    index = 142,
    label = "[C]DC(F)Br",
    molecule = 
"""
multiplicity 3
1 Br u0 p3 c0 {3,S}
2 F  u0 p3 c0 {3,S}
3 C  u0 p0 c0 {1,S} {2,S} {4,D}
4 C  u2 p0 c0 {3,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.90689,0.0065336,5.22733e-05,-1.60581e-07,1.31703e-10,52177.8,11.3267], Tmin=(10,'K'), Tmax=(451.943,'K')),
            NASAPolynomial(coeffs=[5.38425,0.00891265,-6.91707e-06,2.39658e-09,-3.05682e-13,51886.4,3.62647], Tmin=(451.943,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (83.1447,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: 106.99 kcal/mol
S298: 72.92 cal/mol/K

Coordinates (Angstoms):
Br 0.00000 0.87255 0.00000
F -1.02573 -1.58710 0.00000
C 0.15445 -1.02243 0.00000
C 1.38414 -1.68681 0.00000

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 256.7,298.3,347.9,597.1,1040.5,1396.4
""",
    rank = 5,
)

entry(
    index = 143,
    label = "OD[C]C[C](F)F",
    molecule = 
"""
multiplicity 3
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 O u0 p2 c0 {6,D}
4 C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5 C u1 p0 c0 {1,S} {2,S} {4,S}
6 C u1 p0 c0 {3,D} {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.83288,0.0293857,-2.14755e-05,7.65592e-09,-1.07841e-12,-29321.8,12.1615], Tmin=(10,'K'), Tmax=(1615.06,'K')),
            NASAPolynomial(coeffs=[9.89848,0.0143632,-7.52343e-06,1.89685e-09,-1.86956e-13,-31281.1,-20.0092], Tmin=(1615.06,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (182.918,'J/(mol*K)'),
    ),
    reference = 'G4 / RRHO',
    referenceType = "Theory",
    shortDesc = """G4 / RRHO""",
    longDesc = 
"""
H298: -53.75 kcal/mol
S298: 83.20 cal/mol/K

Coordinates (Angstoms):
F 1.52119 -0.98646 -0.39900
F 1.30738 1.17755 -0.19681
O -2.51945 0.10419 -0.30776
C -0.37694 -0.18220 0.81850
C 1.04405 -0.00293 0.35416
C -1.36555 -0.14375 -0.34305
H -0.47325 -1.16531 1.29162
H -0.63760 0.58527 1.55511

modes:
IdealGasTranslation
NonlinearRotor
HarmonicOscillator
Frequencies (cm^-1) = 40.3,93.7,183.8,345.3,407.8,539.6,678.6,778.8,864.7,933.0,1095.3,1253.2,1312.1,1329.9,1406.7,1944.8,3042.8,3103.4
""",
    rank = 5,
)

